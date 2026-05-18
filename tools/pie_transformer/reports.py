"""
Report generators for terminal text, Markdown, TSV, and JSONL output.

Report types:
  terminal text  — quick single-form work
  Markdown       — human-readable derivation review and handoff
  TSV            — lexicon audit and spreadsheet workflows
  JSONL          — machine-readable traces and future UI wrappers
"""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import TextIO

from .rule import DerivationResult, TraceRow
from .render import render, get_warnings
from .tokenize import tokens_to_string


# ── Terminal report ────────────────────────────────────────────────────────────

def format_terminal(
    result: DerivationResult,
    mode: str = 'surface',
    show_trace: bool = False,
    compact: bool = False,
) -> str:
    """Format a single derivation result for terminal display.

    compact=True: single line with pipeline name at left, used for --all output.
    """
    orth = render(result.pipeline, 'surface', result.final_tokens, result.final_accent_index)
    ipa  = render(result.pipeline, 'ipa',     result.final_tokens, result.final_accent_index)
    status_tag = f'[{result.status}]' if result.status != 'ok' else ''
    warnings = get_warnings(result.final_tokens)
    warn_tag = '  \u26a0 ' + ', '.join(warnings) if warnings else ''
    ipa_str = f'  {ipa}' if ipa and ipa not in ('renderer_missing', '') else ''

    if compact:
        name_col = f'\t{result.pipeline:<26}'
        return f'{name_col}  {result.input_form}  \u2192  {orth}{ipa_str}{status_tag}{warn_tag}'.rstrip()

    lines: list[str] = []

    # Header
    lines.append(f'{result.input_form!r}  \u2192  {orth}{ipa_str}  {status_tag}{warn_tag}'.rstrip())

    # Pipeline label
    lines.append(f'  pipeline: {result.pipeline}')

    # Status-specific messages
    if result.status == 'blocked_missing_accent':
        lines.append(f'  blocked:  accent required at stage [{result.blocked_stage}]'
                     f' rule [{result.blocked_rule}]')
        lines.append(f'  form at blockage: {result.blocked_form}')

    elif result.status == 'error':
        lines.append(f'  error:    {result.error_type}: {result.error_message}')
        lines.append(f'  at stage: {result.blocked_stage}  rule: {result.blocked_rule}')

    elif result.status == 'not_implemented':
        lines.append('  (pipeline not yet implemented)')

    # Trace
    if show_trace and result.trace:
        lines.append('')
        lines.append('  Derivation trace:')
        current_stage = None
        for row in result.trace:
            if row.stage != current_stage:
                current_stage = row.stage
                lines.append(f'  ── {row.stage}')
            before = tokens_to_string(row.before_tokens)
            after  = tokens_to_string(row.after_tokens)
            arrow = '→' if row.changed else '='
            tag = f'  [{row.status.upper()}]' if row.status != 'ok' else ''
            lines.append(f'    {row.rule_name}')
            lines.append(f'      {before!r:30s} {arrow}  {after!r}{tag}')
            if row.message:
                lines.append(f'      note: {row.message}')

    return '\n'.join(lines)


# ── Markdown report ────────────────────────────────────────────────────────────

def format_markdown(
    result: DerivationResult,
    mode: str = 'surface',
) -> str:
    """Format a single derivation result as Markdown."""
    lines: list[str] = []
    surface = render(result.pipeline, mode, result.final_tokens, result.final_accent_index)
    warnings = get_warnings(result.final_tokens)

    lines.append(f'## `{result.input_form}` → {result.pipeline}')
    lines.append('')
    lines.append(f'**Status:** `{result.status}`')
    lines.append(f'**Output:** `{surface}`')
    lines.append(f'**Tokens:** `{result.generated_tokens}`')

    if warnings:
        lines.append(f'**Warnings:** ' + ', '.join(f'`{w}`' for w in warnings))

    if result.status == 'blocked_missing_accent':
        lines.append('')
        lines.append(f'Derivation blocked at stage **{result.blocked_stage}**,'
                     f' rule **{result.blocked_rule}**: accent required.')
        lines.append(f'Form at blockage: `{result.blocked_form}`')

    elif result.status == 'error':
        lines.append('')
        lines.append(f'**Error:** `{result.error_type}: {result.error_message}`')
        lines.append(f'At stage **{result.blocked_stage}**, rule **{result.blocked_rule}**.')

    if result.trace:
        lines.append('')
        lines.append('### Derivation trace')
        lines.append('')
        lines.append('| Stage | Rule | Before | After |')
        lines.append('|-------|------|--------|-------|')
        for row in result.trace:
            if not row.changed and row.status == 'ok':
                continue  # skip no-op rows in Markdown (changed-mode default)
            before = tokens_to_string(row.before_tokens)
            after  = tokens_to_string(row.after_tokens)
            status_col = f' `[{row.status.upper()}]`' if row.status != 'ok' else ''
            lines.append(
                f'| {row.stage} | {row.rule_name}{status_col}'
                f' | `{before}` | `{after}` |'
            )

    return '\n'.join(lines)


# ── TSV report row ─────────────────────────────────────────────────────────────

def result_to_tsv_row(
    result: DerivationResult,
    item_id: str,
    expected_surface: str = '',
    expected_ipa: str = '',
    mode: str = 'surface',
) -> dict[str, str]:
    """Convert a DerivationResult to a flat dict suitable for TSV output."""
    generated_surface = render(result.pipeline, 'surface', result.final_tokens, result.final_accent_index)
    generated_ipa     = render(result.pipeline, 'ipa', result.final_tokens, result.final_accent_index)
    generated_tokens  = result.generated_tokens

    # Compare generated vs expected
    surface_match = ''
    if result.status == 'ok' and expected_surface:
        import unicodedata
        gen_nfc = unicodedata.normalize('NFC', generated_surface)
        exp_nfc = unicodedata.normalize('NFC', expected_surface)
        surface_match = 'match' if gen_nfc == exp_nfc else 'differs'

    ipa_match = ''
    if result.status == 'ok' and expected_ipa:
        import unicodedata
        gen_ipa_nfc = unicodedata.normalize('NFC', generated_ipa)
        exp_ipa_nfc = unicodedata.normalize('NFC', expected_ipa)
        ipa_match = 'match' if gen_ipa_nfc == exp_ipa_nfc else 'differs'

    return {
        'item_id':           item_id,
        'source_form':       result.input_form,
        'pipeline':          result.pipeline,
        'expected_surface':  expected_surface,
        'expected_ipa':      expected_ipa,
        'generated_surface': generated_surface,
        'generated_ipa':     generated_ipa,
        'generated_tokens':  generated_tokens,
        'result_status':     result.status,
        'surface_match':     surface_match,
        'ipa_match':         ipa_match,
        'blocked_stage':     result.blocked_stage,
        'blocked_rule':      result.blocked_rule,
        'blocked_form':      result.blocked_form,
        'notes':             '',
        'trace_path':        '',
    }


# ── JSONL serialization ────────────────────────────────────────────────────────

def result_to_jsonl(result: DerivationResult) -> str:
    """Serialize a DerivationResult to a JSONL line."""
    d = {
        'pipeline':          result.pipeline,
        'input_form':        result.input_form,
        'status':            result.status,
        'generated_tokens':  result.generated_tokens,
        'generated_surface': render(result.pipeline, 'surface', result.final_tokens, result.final_accent_index),
        'blocked_stage':     result.blocked_stage,
        'blocked_rule':      result.blocked_rule,
        'error_type':        result.error_type,
        'error_message':     result.error_message,
        'trace': [
            {
                'pipeline':     row.pipeline,
                'stage':        row.stage,
                'rule_id':      row.rule_id,
                'rule_name':    row.rule_name,
                'before':       tokens_to_string(row.before_tokens),
                'after':        tokens_to_string(row.after_tokens),
                'changed':      row.changed,
                'status':       row.status,
                'message':      row.message,
            }
            for row in result.trace
        ],
    }
    return json.dumps(d, ensure_ascii=False)


# ── Batch report writers ───────────────────────────────────────────────────────

def write_markdown_report(
    path: str,
    results: list[tuple[str, str, str, DerivationResult]],  # (item_id, source, pipeline, result)
) -> None:
    """Write a multi-item Markdown report to a file."""
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write('# Transformer Batch Report\n\n')
        for item_id, source, pipeline, result in results:
            fh.write(format_markdown(result))
            fh.write('\n\n---\n\n')


def write_jsonl_report(
    path: str,
    results: list[DerivationResult],
) -> None:
    """Write JSONL output — one JSON object per line."""
    with open(path, 'w', encoding='utf-8') as fh:
        for result in results:
            fh.write(result_to_jsonl(result) + '\n')
