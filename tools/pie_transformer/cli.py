"""
Command-line interface for the PIE transformer.

Commands:
  form          — transform a single PIE form
  batch         — batch-transform a transformer-ready TSV
  extract-lexicon — extract a transformer-ready TSV from the human lexicon TSV

Usage examples:
  python -m pie_transformer form "*ǵʰoysós" --pipeline ghandwa --mode surface --trace changed
  python -m pie_transformer form "*wĺ̥kʷos" --all --mode surface
  python -m pie_transformer batch transform-input.tsv --pipeline ghandwa --out generated.tsv
  python -m pie_transformer extract-lexicon vocab/lexicon.tsv --out transform-input.tsv
"""

from __future__ import annotations

import argparse
import copy
import sys
import unicodedata
from pathlib import Path

from .normalize import normalize
from .tokenize import tokenize, accent_char_pos_to_token_index, tokens_to_string
from .rule import Context
from .pipeline import run, run_all, ALL_PIPELINES
from .render import render, get_warnings
from .reports import format_terminal, format_markdown, result_to_tsv_row, write_jsonl_report
from .tsv_io import (
    read_lexicon, read_transformer_tsv, write_transformer_tsv,
    empty_transformer_row, TRANSFORMER_HEADER,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog='pie_transformer',
        description='PIE → Ghandwa / Wékʷos transformer and lexicon audit tool',
    )
    sub = parser.add_subparsers(dest='command', required=True)

    # ── form command ───────────────────────────────────────────────────────────
    p_form = sub.add_parser('form', help='Transform a single PIE form')
    p_form.add_argument('input', help='PIE input form (e.g. "*wĺ̥kʷos")')
    p_form.add_argument('--pipeline', '-p', default='ghandwa',
                        choices=ALL_PIPELINES, help='Target pipeline')
    p_form.add_argument('--all', dest='all_pipelines', action='store_true',
                        help='Run all pipelines')
    p_form.add_argument('--mode', '-m', default='surface',
                        choices=['surface', 'ipa', 'tokens'], help='Output mode')
    p_form.add_argument('--no-clear', dest='no_clear', action='store_true',
                        help='Do not clear the screen before output')
    p_form.add_argument('--trace', '-t', default=None,
                        choices=['changed', 'full'], help='Trace verbosity')
    p_form.add_argument('--format', '-f', default='text',
                        choices=['text', 'markdown', 'json'], help='Output format')

    # ── batch command ──────────────────────────────────────────────────────────
    p_batch = sub.add_parser('batch', help='Batch-transform a transformer-ready TSV')
    p_batch.add_argument('input_tsv', help='Transformer-ready TSV input path')
    p_batch.add_argument('--pipeline', '-p', default='ghandwa',
                         choices=ALL_PIPELINES)
    p_batch.add_argument('--all', dest='all_pipelines', action='store_true')
    p_batch.add_argument('--mode', '-m', default='surface',
                         choices=['surface', 'ipa', 'tokens'])
    p_batch.add_argument('--trace', '-t', default=None,
                         choices=['changed', 'full'])
    p_batch.add_argument('--out', '-o', help='Output TSV path')
    p_batch.add_argument('--report', help='Markdown report output path')
    p_batch.add_argument('--jsonl', help='JSONL output path')
    p_batch.add_argument('--write-back', dest='write_back', action='store_true',
                         help='Update the input TSV in place (only for transformer-ready TSV)')

    # ── extract-lexicon command ────────────────────────────────────────────────
    p_extract = sub.add_parser('extract-lexicon',
                               help='Extract transformer-ready TSV from human lexicon TSV')
    p_extract.add_argument('lexicon_tsv', help='Human lexicon TSV path (read-only)')
    p_extract.add_argument('--out', '-o', required=True, help='Output TSV path')
    p_extract.add_argument('--pipeline', '-p', default='ghandwa',
                           choices=ALL_PIPELINES,
                           help='Target pipeline column to write in output')
    p_extract.add_argument('--source-ety-col', default='lemma_1_pre_ety')
    p_extract.add_argument('--source-root-col', default='lemma_1_pre_root')
    p_extract.add_argument('--expected-surface-col', default='lemma_1')
    p_extract.add_argument('--expected-ipa-col', default='lemma_1_ipa')

    args = parser.parse_args(argv)

    if args.command == 'form':
        return _cmd_form(args)
    elif args.command == 'batch':
        return _cmd_batch(args)
    elif args.command == 'extract-lexicon':
        return _cmd_extract(args)
    else:
        parser.print_help()
        return 1


# ── form command ───────────────────────────────────────────────────────────────

def _cmd_form(args) -> int:
    import os
    if not args.no_clear:
        os.system('clear')
    raw = args.input
    norm = normalize(raw)
    tokens, char_offsets = tokenize(norm.clean)
    accent_index = accent_char_pos_to_token_index(norm.accent_char_pos, tokens, char_offsets)

    ctx = Context(accent_index=accent_index)

    if args.all_pipelines:
        pipeline_names = ALL_PIPELINES
    else:
        pipeline_names = [args.pipeline]

    for name in pipeline_names:
        ctx_copy = copy.deepcopy(ctx)
        tok_copy = list(tokens)
        result = run(name, tok_copy, ctx_copy, raw, trace_mode=args.trace)

        # Attach rendered forms to result
        result.generated_surface = render(name, 'surface', result.final_tokens, result.final_accent_index)
        result.generated_ipa     = render(name, 'ipa', result.final_tokens, result.final_accent_index)

        if args.format == 'markdown':
            print(format_markdown(result, mode=args.mode))
        elif args.format == 'json':
            from .reports import result_to_jsonl
            print(result_to_jsonl(result))
        else:  # text
            show_trace = args.trace in ('changed', 'full')
            print(format_terminal(result, mode=args.mode, show_trace=show_trace))

        if args.all_pipelines and name != pipeline_names[-1]:
            print()

    return 0


# ── batch command ──────────────────────────────────────────────────────────────

def _cmd_batch(args) -> int:
    rows = read_transformer_tsv(args.input_tsv)

    if args.all_pipelines:
        pipeline_names = ALL_PIPELINES
    else:
        pipeline_names = [args.pipeline]

    output_rows: list[dict] = []
    md_results: list[tuple] = []
    jsonl_results = []

    for row in rows:
        source_form = row.get('source_form', '')
        pipeline_col = row.get('pipeline', pipeline_names[0])
        item_id = row.get('item_id', _fallback_id(source_form))
        expected_surface = row.get('expected_surface', '')
        expected_ipa = row.get('expected_ipa', '')

        if not source_form:
            out = _no_source_row(item_id, pipeline_col, row)
            output_rows.append(out)
            continue

        norm = normalize(source_form)
        tokens, char_offsets = tokenize(norm.clean)
        accent_index = accent_char_pos_to_token_index(norm.accent_char_pos, tokens, char_offsets)

        pipelines_to_run = pipeline_names if args.all_pipelines else [pipeline_col or pipeline_names[0]]

        for name in pipelines_to_run:
            ctx = Context(accent_index=accent_index)
            result = run(name, list(tokens), ctx, source_form, trace_mode=args.trace)
            result.generated_surface = render(name, 'surface', result.final_tokens, result.final_accent_index)
            result.generated_ipa     = render(name, 'ipa', result.final_tokens, result.final_accent_index)

            tsv_row = result_to_tsv_row(result, item_id, expected_surface, expected_ipa)
            tsv_row['notes'] = row.get('notes', '')
            output_rows.append(tsv_row)
            md_results.append((item_id, source_form, name, result))
            jsonl_results.append(result)

            # Terminal progress
            match_tag = f'[{tsv_row["surface_match"] or result.status}]'
            print(f'{item_id:30s}  {source_form:25s}  →  '
                  f'{result.generated_surface:20s}  {match_tag}')

    # Write outputs
    if args.out:
        write_transformer_tsv(args.out, output_rows)
        print(f'\nTSV written to {args.out}')

    if args.write_back:
        write_transformer_tsv(args.input_tsv, output_rows)
        print(f'Write-back: updated {args.input_tsv}')

    if args.report:
        from .reports import write_markdown_report
        write_markdown_report(args.report, md_results)
        print(f'Markdown report written to {args.report}')

    if args.jsonl:
        write_jsonl_report(args.jsonl, jsonl_results)
        print(f'JSONL written to {args.jsonl}')

    return 0


# ── extract-lexicon command ────────────────────────────────────────────────────

def _cmd_extract(args) -> int:
    lexicon_path = Path(args.lexicon_tsv)
    out_path = Path(args.out)

    print(f'Extracting from {lexicon_path} → {out_path}')
    print(f'Pipeline: {args.pipeline}')

    rows_out: list[dict] = []
    skipped = 0
    extracted = 0

    for lex_row in read_lexicon(
        lexicon_path,
        source_ety_col=args.source_ety_col,
        source_root_col=args.source_root_col,
        expected_surface_col=args.expected_surface_col,
        expected_ipa_col=args.expected_ipa_col,
    ):
        if not lex_row.source_form:
            skipped += 1
            # Include in output with status=no_source_form so it's traceable
            row = empty_transformer_row(
                lex_row.item_id, '', args.pipeline,
                lex_row.expected_surface, lex_row.expected_ipa,
            )
            row['result_status'] = 'no_source_form'
            rows_out.append(row)
            continue

        row = empty_transformer_row(
            lex_row.item_id,
            lex_row.source_form,
            args.pipeline,
            lex_row.expected_surface,
            lex_row.expected_ipa,
            notes=f'source_col={lex_row.source_column}',
        )
        rows_out.append(row)
        extracted += 1

    write_transformer_tsv(out_path, rows_out)
    print(f'Done. {extracted} rows extracted, {skipped} skipped (no source form).')
    print(f'Output: {out_path}')
    return 0


# ── Helpers ────────────────────────────────────────────────────────────────────

def _fallback_id(source_form: str) -> str:
    slug = ''.join(c for c in source_form[:15] if c.isascii() and c.isalnum()) or 'item'
    return f'manual-{slug}'


def _no_source_row(item_id: str, pipeline: str, original_row: dict) -> dict:
    row = empty_transformer_row(item_id, '', pipeline)
    row['result_status'] = 'no_source_form'
    row['expected_surface'] = original_row.get('expected_surface', '')
    row['expected_ipa'] = original_row.get('expected_ipa', '')
    return row
