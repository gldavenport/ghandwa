---
title: "Etymological Dictionary of Proto-Germanic"
author: "Guus Kroonen"
date: "2013"
source_type: mixed
extraction_date: 2026-05-07
source_file: kroonen-2013-proto-germanic.pdf
chunk: "extraction-report"
---

# Extraction Report

## Source type

The PDF is treated as **mixed**: the pages render as page images/scans, but the file also contains a machine-readable text layer. The extraction uses the embedded text layer as the main input and uses the page image only for the page 38 flowchart image. This is not a character-authoritative final pass; it is a corpus-ready first extraction from a problematic OCR/text layer.

## Corrections applied

- Removed soft hyphen characters and rejoined soft-hyphenated line breaks.
- Removed running headers and page-number blocks where detected in the top margin.
- Split the dictionary according to the PDF outline into one file per letter section.
- Separated references and index into standalone files.
- Rendered the page 38 flowchart into `images/kroonen-2013-proto-germanic-p38-flowchart.png` and linked it from the introduction file.
- Normalized the observed corrupt arrow/control mappings `0x88, 0x8c, 0x90, 0x9a` to `=>`.
- Replaced remaining C1 control characters with `[unclear]`.
- Mechanically normalized `h1`, `h2`, `h3`, `hz`, and `hJ` to `h₁`, `h₂`, and `h₃`. This was applied globally and should be audited in later passes.
- Replaced micro sign `µ` with Greek `μ`.
- Applied a small number of obvious OCR word repairs, including `Inda-European`/`lndo-European`/`Jndo-European` to `Indo-European`, `Nate on the Structure` to `Note on the Structure`, and selected `... Jaw` OCR errors to `... law`.

## Unresolved issues

- The source text layer contains substantial OCR/font-mapping corruption in Greek, IPA-like symbols, thorn/eth-like characters, special vowels, and some reconstructed forms. These were not fully corrected.
- The index was extracted into fenced text blocks using a coordinate-based four-column grouping. This preserves column order better than plain extraction, but line grouping and page-continuation behavior should be audited before treating it as final.
- Tables in the introduction and abbreviation lists were preserved as text blocks, not fully normalized into Markdown tables.
- Remaining `[unclear]` markers mostly represent non-printing control characters from the embedded text layer; some likely correspond to Greek or other special characters rather than unreadable source text.
- Superscript modifier letters, subscript notation beyond laryngeal digits, and several macron/diacritic distinctions could not be verified from the text layer.
- The extraction did not perform full visual verification of dictionary entries. Later character-critical passes should compare high-value entries against rendered page images.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: mechanical normalization applied, but not visually verified.
- Macron vowels: counts are very low because the OCR/text layer often does not preserve them; this requires targeted visual/source-critical correction.
- Superscript `ʰ` and `ʷ`: not reliably recoverable from the text layer; not systematically restored.
- `ə`: not reliably recoverable from the text layer.
- Underdot characters such as `ṛ ḷ ṃ ṇ`: not systematically verified.
- Acute consonants such as `ǵ ḱ`: not systematically verified.
- Asterisks before reconstructed forms: preserved where present in the OCR layer, but not visually verified.
- Dagger `†`: not systematically verified; approximate count is reported below.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 1008,
    "h2": 2896,
    "h3": 506
  },
  "macron_a": 0,
  "macron_e": 0,
  "macron_i": 0,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 1,
  "greek_chars": 508,
  "combining_diacritics": 22,
  "dagger": 0
}
```

## Structural integrity check

- Chunking follows the source outline: front matter, introduction, dictionary letter sections, references, and index.
- YAML front matter is present in each Markdown file.
- Page anchors are present throughout.
- The bibliography is separate.
- The index is separate and uses one fenced text block per page.
- Footnotes are preserved only insofar as they were captured by the OCR/text layer; footnote attachment should be audited in a later pass.
- Dictionary continuation text at page boundaries is likely preserved, but not manually verified entry-by-entry.

## Image inventory

| File | Source label | PDF page | Caption/description |
|---|---:|---:|---|
| `images/kroonen-2013-proto-germanic-p38-flowchart.png` | Flowchart in §2.3 | 38 | Relative chronology of selected sound changes from Proto-Indo-European to Proto-Germanic. |

## Metrics

- Approximate dictionary entry-start count from letter files: 2787
- `[unclear]` markers inserted: 19
- Output Markdown files before report/manifest: 26
