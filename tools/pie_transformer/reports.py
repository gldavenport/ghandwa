"""
Report generators for terminal text, Markdown, TSV, and JSONL output.

Output tiers: orth (attested langs only), citation (universal), ipa (universal).
None signals a tier absent for a given pipeline; display as '—'.
"""

from __future__ import annotations

import json
from typing import TextIO

from .rule import DerivationResult, TraceRow
from .render import render, get_warnings
from pie_core.tokenize import tokens_to_string

# Fixed column widths for compact --all display
_ORTH_W = 18
_CIT_W  = 18


# ── Terminal report ────────────────────────────────────────────────────────────

def format_terminal(
    result: DerivationResult,
    mode: str = 'orth',
    show_trace: bool = False,
    compact: bool = False,
    indent: int = 0,
) -> str:
    """Format a single derivation result for terminal display.

    compact=True: one line per pipeline for --all output.
      Columns: pipeline name | orth (or —) | citation | ipa | warnings
    indent: tree depth; 0 = root, 1 = daughter.
    """
    orth = render(result.pipeline, 'orth',     result.final_tokens, result.final_accent_index)
    cit  = render(result.pipeline, 'citation', result.final_tokens, result.final_accent_index)
    ipa  = render(result.pipeline, 'ipa',      result.final_tokens, result.final_accent_index)

    status_tag = f'[{result.status}]' if result.status != 'ok' else ''
    warnings   = get_warnings(result.final_tokens)
    warn_tag   = '  \u26a0 ' + ', '.join(warnings) if warnings else ''

    if compact:
        prefix   = '  ' * indent
        name_col = f'{prefix}{result.pipeline:<{30 - 2 * indent}}'
        orth_col = f'{(orth or "\u2014"):<{_ORTH_W}}'
        cit_col  = f'{(cit  or "\u2014"):<{_CIT_W}}'
        ipa_col  = ipa or ''
        return f'{name_col}  {orth_col}  {cit_col}  {ipa_col}{status_tag}{warn_tag}'.rstrip()

    lines: list[str] = []

    # Header
    orth_str = orth or '\u2014'
    cit_str  = cit  or '\u2014'
    ipa_str  = ipa  or '\u2014'
    lines.append(f'{result.input_form!r}  \u2192')
    lines.append(f'  orth:     {orth_str}')
    lines.append(f'  citation: {cit_str}')
    lines.append(f'  ipa:      {ipa_str}')
    lines.append(f'  pipeline: {result.pipeline}')

    if status_tag:
        lines.append(f'  status:   {result.status}')

    if result.status == 'blocked_missing_accent':
        lines.append(f'  blocked:  accent required at stage [{result.blocked_stage}]'
                     f' rule [{result.blocked_rule}]')
        lines.append(f'  form at blockage: {result.blocked_form}')
    elif result.status == 'error':
        lines.append(f'  error:    {result.error_type}: {result.error_message}')
        lines.append(f'  at stage: {result.blocked_stage}  rule: {result.blocked_rule}')
    elif result.status == 'not_implemented':
        lines.append('  (pipeline not yet implemented)')

    if warn_tag:
        lines.append(f'  warnings:{warn_tag}')

    if show_trace and result.trace:
        lines.append('')
        lines.append('  Derivation trace:')
        current_stage = None
        for row in result.trace:
            if row.stage != current_stage:
                current_stage = row.stage
                lines.append(f'  \u2500\u2500 {row.stage}')
            before = tokens_to_string(row.before_tokens)
            after  = tokens_to_string(row.after_tokens)
            arrow  = '\u2192' if row.changed else '='
            tag    = f'  [{row.status.upper()}]' if row.status != 'ok' else ''
            lines.append(f'    {row.rule_name}')
            lines.append(f'      {before!r:30s} {arrow}  {after!r}{tag}')
            if row.message:
                lines.append(f'      note: {row.message}')

    return '\n'.join(lines)


# ── Markdown report ────────────────────────────────────────────────────────────

def format_markdown(
    result: DerivationResult,
    mode: str = 'orth',
) -> str:
    """Format a single derivation result as Markdown."""
    lines: list[str] = []
    orth = render(result.pipeline, 'orth',     result.final_tokens, result.final_accent_index)
    cit  = render(result.pipeline, 'citation', result.final_tokens, result.final_accent_index)
    ipa  = render(result.pipeline, 'ipa',      result.final_tokens, result.final_accent_index)
    warnings = get_warnings(result.final_tokens)

    lines.append(f'## `{result.input_form}` \u2192 {result.pipeline}')
    lines.append('')
    lines.append(f'**Status:** `{result.status}`')
    if orth:
        lines.append(f'**Orth:** `{orth}`')
    lines.append(f'**Citation:** `{cit}`')
    lines.append(f'**IPA:** `{ipa}`')
    lines.append(f'**Tokens:** `{result.generated_tokens}`')

    if warnings:
        lines.append('**Warnings:** ' + ', '.join(f'`{w}`' for w in warnings))

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
                continue
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
    expected_orth: str = '',
    expected_ipa: str = '',
    mode: str = 'orth',
) -> dict[str, str]:
    """Convert a DerivationResult to a flat dict for TSV output."""
    import unicodedata

    generated_orth     = render(result.pipeline, 'orth',     result.final_tokens, result.final_accent_index) or ''
    generated_citation = render(result.pipeline, 'citation', result.final_tokens, result.final_accent_index) or ''
    generated_ipa      = render(result.pipeline, 'ipa',      result.final_tokens, result.final_accent_index) or ''
    generated_tokens   = result.generated_tokens

    orth_match = ''
    if result.status == 'ok' and expected_orth and generated_orth:
        gen_nfc = unicodedata.normalize('NFC', generated_orth)
        exp_nfc = unicodedata.normalize('NFC', expected_orth)
        orth_match = 'match' if gen_nfc == exp_nfc else 'differs'

    ipa_match = ''
    if result.status == 'ok' and expected_ipa and generated_ipa:
        gen_nfc = unicodedata.normalize('NFC', generated_ipa)
        exp_nfc = unicodedata.normalize('NFC', expected_ipa)
        ipa_match = 'match' if gen_nfc == exp_nfc else 'differs'

    return {
        'item_id':            item_id,
        'source_form':        result.input_form,
        'pipeline':           result.pipeline,
        'expected_orth':      expected_orth,
        'expected_ipa':       expected_ipa,
        'generated_orth':     generated_orth,
        'generated_citation': generated_citation,
        'generated_ipa':      generated_ipa,
        'generated_tokens':   generated_tokens,
        'result_status':      result.status,
        'orth_match':         orth_match,
        'ipa_match':          ipa_match,
        'blocked_stage':      result.blocked_stage,
        'blocked_rule':       result.blocked_rule,
        'blocked_form':       result.blocked_form,
        'notes':              '',
        'trace_path':         '',
    }


# ── JSONL serialization ────────────────────────────────────────────────────────

def result_to_jsonl(result: DerivationResult) -> str:
    """Serialize a DerivationResult to a JSONL line."""
    d = {
        'pipeline':           result.pipeline,
        'input_form':         result.input_form,
        'status':             result.status,
        'generated_tokens':   result.generated_tokens,
        'generated_orth':     render(result.pipeline, 'orth',     result.final_tokens, result.final_accent_index),
        'generated_citation': render(result.pipeline, 'citation', result.final_tokens, result.final_accent_index),
        'generated_ipa':      render(result.pipeline, 'ipa',      result.final_tokens, result.final_accent_index),
        'blocked_stage':      result.blocked_stage,
        'blocked_rule':       result.blocked_rule,
        'error_type':         result.error_type,
        'error_message':      result.error_message,
        'trace': [
            {
                'pipeline':  row.pipeline,
                'stage':     row.stage,
                'rule_id':   row.rule_id,
                'rule_name': row.rule_name,
                'before':    tokens_to_string(row.before_tokens),
                'after':     tokens_to_string(row.after_tokens),
                'changed':   row.changed,
                'status':    row.status,
                'message':   row.message,
            }
            for row in result.trace
        ],
    }
    return json.dumps(d, ensure_ascii=False)


# ── Batch report writers ───────────────────────────────────────────────────────

def write_markdown_report(
    path: str,
    results: list[tuple[str, str, str, DerivationResult]],
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
