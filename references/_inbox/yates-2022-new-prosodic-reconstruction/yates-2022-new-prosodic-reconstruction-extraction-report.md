---
title: A new prosodic reconstruction of Proto-Indo-European *-mon-stems — Extraction report
author: Anthony D. Yates
date: 2022
source_type: born-digital
extraction_date: 2026-05-07
source_file: yates-2022-new-prosodic-reconstruction.pdf
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The text layer was used as the primary input. Visual rendering was spot-checked for the laryngeal-index convention and general layout.

## Corrections applied

- Removed running page headers, running footers, and page numbers from the corpus files.
- Split the end bibliography into a separate bibliography file.
- Rejoined many line-broken paragraphs and line-final hyphenations.
- Preserved dense examples and paradigms as fenced text blocks where automated conversion to prose Markdown would likely damage alignment.
- Normalized extracted ASCII laryngeal indices `h1`, `h2`, `h3` to Unicode subscript forms `h₁`, `h₂`, `h₃` based on spot-checking the rendered PDF.
- Collected footnotes into a final Markdown footnote section.

## Unresolved issues

- No `[unclear]` markers were inserted. This does not certify that every character is correct.
- The PDF text layer exposes laryngeal indices as ASCII digits; normalization was applied globally. This should be checked in a future character-authoritative pass.
- Italic and bold styling were not comprehensively encoded in Markdown; character fidelity was prioritized over styling.
- Some footnote references may remain as bare numeric markers or may require review where the source used multiple footnote references after one clause.
- Tables and paradigms were preserved as fenced text blocks rather than fully normalized Markdown tables. This reduces structural polish but lowers risk of losing or corrupting forms.
- The extraction pass cannot catch errors made consistently by the PDF text layer. A later targeted pass should compare high-risk forms against page renderings.

## Confusion-pair report

- `h₁ h₂ h₃`: normalized from text-layer `h1 h2 h3`; spot-checked visually, but not every instance was manually verified.
- Macron vowels: preserved from text layer where present; not every dense table and footnote instance was manually verified.
- `ʰ ʷ`: preserved if present in the text layer; no exhaustive verification.
- `ə`: preserved from the text layer where present; no exhaustive verification.
- Underdot characters such as `ṛ ḷ ṃ ṇ`: preserved where present; no exhaustive verification.
- Palatal/acute consonant notation such as `ǵ`, `ḱ`, and source-specific `k̑`, `g̑`: preserved as extracted; no silent conversion to another notation was attempted.
- Asterisk `*`: preserved.
- Dagger `†`: count is approximate; no full manual verification.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 40,
    "h2": 119,
    "h3": 5
  },
  "macron_a": 116,
  "macron_e": 8,
  "macron_i": 28,
  "macron_o": 45,
  "macron_u": 9,
  "schwa": 7,
  "greek_chars": 2986,
  "combining_diacritics": 182,
  "dagger": 0
}
```

## Structural integrity check

- Main text and bibliography were separated.
- No index was present.
- No embedded images or figures were detected by `pdfimages -list`.
- Headings were converted to Markdown where automatically identifiable.
- Dense numbered examples and paradigms remain aligned in fenced text blocks.
- Page anchors of the form `<!-- source-page: N -->` were inserted in the main text for later source checking.

## Image inventory

No images were detected or extracted.
