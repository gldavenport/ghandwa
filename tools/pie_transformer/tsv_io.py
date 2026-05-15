"""
TSV I/O utilities.

Two TSV types:
  human lexicon TSV   — vocab/lexicon.tsv; read-only in v1 unless --write-back used
  transformer-ready TSV — extracted from human lexicon TSV; may be updated with --write-back

Both types use Windows line endings (CRLF). Strip \\r from all fields explicitly.
Column indices are resolved dynamically from the header row — never hardcoded.
"""

from __future__ import annotations

import csv
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator


# ── CRLF-safe field reader ────────────────────────────────────────────────────

def _strip_crlf(s: str) -> str:
    return s.rstrip('\r')


def _nfc(s: str) -> str:
    return unicodedata.normalize('NFC', s)


# ── Human lexicon TSV columns (provisional; verified against lexicon header) ──

LEXICON_COLUMNS = {
    'source_ety':   'lemma_1_pre_ety',    # preferred source/preform input
    'source_root':  'lemma_1_pre_root',   # fallback source/preform input
    'expected_surface': 'lemma_1',        # expected Ghandwa surface form
    'expected_ipa': 'lemma_1_ipa',        # expected Ghandwa IPA
    'entry_status': 'entry_status',
    'formation':    'entry_formation_type',
    'historical':   'entry_historical_type',
}


@dataclass
class LexiconRow:
    """A row extracted from the human lexicon TSV."""
    row_number: int
    item_id: str
    source_form: str          # the PIE preform to transform
    source_column: str        # which column the source came from
    expected_surface: str     # may be empty
    expected_ipa: str         # may be empty
    entry_status: str
    raw: dict[str, str] = field(default_factory=dict)  # full row for reference


def read_lexicon(
    path: str | Path,
    source_ety_col: str = 'lemma_1_pre_ety',
    source_root_col: str = 'lemma_1_pre_root',
    expected_surface_col: str = 'lemma_1',
    expected_ipa_col: str = 'lemma_1_ipa',
    entry_status_col: str = 'entry_status',
) -> Iterator[LexiconRow]:
    """
    Read the human lexicon TSV and yield LexiconRow objects.

    Source column precedence: lemma_1_pre_ety > lemma_1_pre_root.
    The extraction trace logs which column was used for each row.

    Rows without a usable source form are yielded with source_form='' so the
    caller can set status=no_source_form.

    NFC normalization is applied to all string fields.
    CRLF is stripped from all fields.
    """
    path = Path(path)
    with path.open(encoding='utf-8', newline='') as fh:
        reader = csv.reader(fh, delimiter='\t')
        raw_header = next(reader)
        header = [_nfc(_strip_crlf(h)) for h in raw_header]
        col = {name: i for i, name in enumerate(header)}

        def _get(row: list[str], col_name: str) -> str:
            idx = col.get(col_name)
            if idx is None or idx >= len(row):
                return ''
            return _nfc(_strip_crlf(row[idx]))

        for row_num, raw_row in enumerate(reader, start=2):  # 1-indexed; row 1 = header
            row = [_nfc(_strip_crlf(f)) for f in raw_row]

            # Determine source form (ety takes precedence over root)
            ety_val  = _get(row, source_ety_col)
            root_val = _get(row, source_root_col)

            if ety_val:
                source_form   = ety_val
                source_column = source_ety_col
            elif root_val:
                source_form   = root_val
                source_column = source_root_col
            else:
                source_form   = ''
                source_column = ''

            # Build item_id from row number and available lemma material
            lemma_val = _get(row, 'lemma_1')
            item_id = _make_item_id(row_num, lemma_val)

            # Full raw row as dict for reference
            raw_dict = {header[i]: row[i] for i in range(min(len(header), len(row)))}

            yield LexiconRow(
                row_number=row_num,
                item_id=item_id,
                source_form=source_form,
                source_column=source_column,
                expected_surface=_get(row, expected_surface_col),
                expected_ipa=_get(row, expected_ipa_col),
                entry_status=_get(row, entry_status_col),
                raw=raw_dict,
            )


def _make_item_id(row_num: int, lemma: str) -> str:
    """
    Generate a fallback item_id from row number and lemma.
    Format: row-NNNNNN-slug
    """
    # Slugify lemma: keep ASCII alphanumeric, replace everything else with hyphen
    slug = ''
    for ch in lemma[:20]:  # truncate to avoid long IDs
        if ch.isascii() and ch.isalnum():
            slug += ch.lower()
        elif slug and not slug.endswith('-'):
            slug += '-'
    slug = slug.rstrip('-') or 'item'
    return f'row-{row_num:06d}-{slug}'


# ── Transformer-ready TSV ─────────────────────────────────────────────────────

TRANSFORMER_HEADER = [
    'item_id',
    'source_form',
    'pipeline',
    'expected_surface',
    'expected_ipa',
    'notes',
    'generated_surface',
    'generated_ipa',
    'generated_tokens',
    'result_status',
    'surface_match',
    'ipa_match',
    'blocked_stage',
    'blocked_rule',
    'blocked_form',
    'trace_path',
]


def write_transformer_tsv(
    path: str | Path,
    rows: list[dict[str, str]],
) -> None:
    """
    Write a transformer-ready TSV. All rows must have keys matching TRANSFORMER_HEADER.
    Uses Unix line endings.
    """
    path = Path(path)
    with path.open('w', encoding='utf-8', newline='\n') as fh:
        writer = csv.DictWriter(fh, fieldnames=TRANSFORMER_HEADER, delimiter='\t',
                                extrasaction='ignore', lineterminator='\n')
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def read_transformer_tsv(path: str | Path) -> list[dict[str, str]]:
    """
    Read a transformer-ready TSV. Returns list of dicts with NFC-normalized,
    CRLF-stripped fields.
    """
    path = Path(path)
    rows: list[dict[str, str]] = []
    with path.open(encoding='utf-8', newline='') as fh:
        reader = csv.DictReader(fh, delimiter='\t')
        for raw_row in reader:
            row = {_nfc(_strip_crlf(k)): _nfc(_strip_crlf(v))
                   for k, v in raw_row.items()}
            rows.append(row)
    return rows


def empty_transformer_row(item_id: str, source_form: str, pipeline: str,
                           expected_surface: str = '', expected_ipa: str = '',
                           notes: str = '') -> dict[str, str]:
    """Return a transformer row with required columns set and generated columns empty."""
    return {
        'item_id': item_id,
        'source_form': source_form,
        'pipeline': pipeline,
        'expected_surface': expected_surface,
        'expected_ipa': expected_ipa,
        'notes': notes,
        'generated_surface': '',
        'generated_ipa': '',
        'generated_tokens': '',
        'result_status': '',
        'surface_match': '',
        'ipa_match': '',
        'blocked_stage': '',
        'blocked_rule': '',
        'blocked_form': '',
        'trace_path': '',
    }
