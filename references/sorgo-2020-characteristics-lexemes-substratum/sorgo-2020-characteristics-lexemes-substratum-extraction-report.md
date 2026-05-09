---
title: Characteristics of lexemes of a substratum origin in Proto-Germanic — Extraction Report
author: Aljoša Šorgo
date: 2020
source_type: born-digital
extraction_date: 2026-05-08
source_file: šorgo-2020-characteristics-lexemes-substratum.pdf
chunk: extraction-report
---

# Extraction Report

## Source-type identification

Born-digital PDF with a machine-readable text layer. The text layer was used as the primary source. Rendered page inspection was used as fallback for source-specific corrupted glyphs and the figure.

## Corrections applied

- Removed running headers, printed page numbers, and page-boundary artifacts while preserving source-page anchors.
- Rejoined ordinary line-wrapped prose into paragraphs.
- Normalized laryngeal digits in reconstructed forms from `h1 h2 h3` to `h₁ h₂ h₃`.
- Repaired Greek mu extracted as micro sign `µ` to Greek `μ`.
- Repaired source-specific custom-encoded signs observed in the born-digital text layer, including `#` → `u̯` in forms such as `*h₁reu̯dʰ-`, `$` → `l̥`, `%` → `i̯`, `!` → `ḱ`, `"` → `ǵ`, and selected `&` → `ʷ` in labialized-velar notation.
- Repaired the Georgian parenthetical for `keri` from corrupted text-layer output to `(ქერი)` after visual/contextual verification.
- Extracted Figure 1 as `images/sorgo-2020-fig1.png` from page 462.
- Separated the bibliography into `sorgo-2020-characteristics-lexemes-substratum-bibliography.md`.

## Unresolved issues list

- No inline `[unclear]` markers were inserted.
- Table extraction in sections 5.9 and 5.10 was repaired into Markdown tables from the text layer plus rendered-page/contextual checks. Treat Tables 2–5 as structurally provisional pending a dedicated visual table QA pass if they are to be used as structured data.
- Footnote placement was preserved as extracted/reflowed text rather than normalized to Markdown footnote syntax throughout. A further pass could normalize all notes to `[^n]` definitions.
- Figure 1 was rasterized from the PDF page rather than extracted as an original vector object.

## Confusion-pair report

- `h₁ h₂ h₃`: normalized from ASCII digit forms. There may be cases where a digit belonged to typography rather than laryngeal notation, though the replacements were limited to `h1`, `h2`, and `h3` patterns.
- Macron vowels: preserved from the text layer; no claim of exhaustive visual verification.
- Superscript `ʰ` and `ʷ`: `ʰ` was preserved; `ʷ` required selected repair where the text layer emitted `&`.
- `ə`: preserved where present.
- Underdot and syllabic marks: preserved where present; source-specific repairs were made for `l̥` and `i̯`.
- `ǵ` and `ḱ`: repaired where the text layer emitted custom placeholder glyphs.
- Asterisk before reconstructed forms: preserved from the text layer.
- Dagger `†`: no dagger characters were found in the output.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "h1": 11,
  "h2": 27,
  "h3": 5,
  "macron_a": 24,
  "macron_e": 34,
  "macron_i": 53,
  "macron_o": 76,
  "macron_u": 16,
  "schwa": 8,
  "greek_chars": 837,
  "combining_diacritics": 91,
  "dagger": 0
}
```

## Structural integrity check

- Headings were converted to Markdown headings.
- Lexical entries in section 4 were promoted to third-level headings.
- Bibliography was separated.
- Figure 1 was included with an image link and caption.
- Tables are present but not certified as structurally authoritative.
- Page anchors were retained as HTML comments.

## Image inventory

| Filename | Source label | Source page | Caption |
|---|---|---:|---|
| `images/sorgo-2020-fig1.png` | Figure 1 | 462 | The occurrence and co-occurrence of features of the AS language in the Proto-Germanic lexicon. |
