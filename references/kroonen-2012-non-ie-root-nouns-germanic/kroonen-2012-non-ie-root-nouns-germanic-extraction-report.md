---
title: "Extraction report — Non-Indo-European root nouns in Germanic"
author: "Guus Kroonen"
date: "2012"
source_type: "born-digital"
extraction_date: "2026-05-08"
source_file: "kroonen-2012-non-ie-root-nouns-germanic.pdf"
chunk: "extraction-report"
---

# Extraction report

## Source identification

- Source type: born-digital PDF with a machine-readable text layer.
- Primary input: PDF text layer. Rendered page images were used only for targeted visual checking of high-risk notation, especially laryngeal subscripts and superscript aspiration marks.
- Page range represented in source: 239–260.
- Output structure: single article Markdown file plus separate bibliography Markdown file.
- Embedded images: none detected by `pdfimages -list`; no `images/` directory was produced.

## Corrections applied

- Repaired typographic ligatures from text-layer extraction, especially `ﬁ` → `fi` and `ﬂ` → `fl`.
- Rejoined line-break hyphenation where it was clearly an artifact of PDF extraction. Compound forms such as Indo-European, Proto-Germanic, Balto-Slavic, Pre-Greek, and Italo-Germanic were preserved with hyphens where visually or contextually required.
- Removed running headers, page numbers, page-footer publication furniture, and page-boundary artifacts.
- Separated bibliography into `kroonen-2012-non-ie-root-nouns-germanic-bibliography.md`.
- Converted visually subscripted laryngeal digits from text-layer `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃` in the output.
- Converted visually superscripted aspiration in reconstructed/phonological forms from text-layer `h` to `ʰ` where checked or contextually indicated, e.g. `gʷʰ`, `dʰ`, `gʰ`, `bʰ`, `ǵʰ`, and `qʰ`.
- Converted footnotes to Markdown footnote syntax and moved footnote text to the notes section of the main article file.

## Unresolved issues

- Italics and small formatting distinctions were not exhaustively preserved. The pass prioritized character fidelity and logical structure over typographic styling.
- Superscript aspiration normalization was applied contextually in reconstructed forms. A later visual pass could still find isolated `h` vs. `ʰ` errors.
- Some Greek polytonic characters and combining marks were preserved from the text layer, but not every Greek form was visually rechecked glyph-by-glyph.
- Bibliography wrapping and dehyphenation were cleaned structurally, but not every title was cross-checked against an external bibliographic authority.
- No `[unclear]` markers were inserted. This means no location was judged unreadable from the available text layer and rendered images, not that the output is certified error-free.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: normalized in output where the text layer had ASCII digits for visually subscripted laryngeals. Could still require spot-checking in unusual forms such as capital-laryngeal notation.
- Macron vowels: preserved where present in the text layer. Dense bibliography and footnote areas were not visually checked exhaustively.
- `ʰ ʷ` vs. `h w`: `ʷ` was generally preserved by the text layer; `ʰ` was normalized contextually from visual/text-layer evidence. This remains the highest-risk class.
- `ə` vs. `e` or `9`: preserved where present; only a small number of schwa instances occur.
- Underdot letters such as `ṛ`, `ḷ`, `ṃ`, `ṇ`: preserved where present; not all possible Indic forms were visually checked.
- `ǵ`, `ḱ`: preserved where present; laryngeal/aspiration normalization was applied around them where indicated.
- Asterisk `*`: preserved before reconstructed forms where present in the text layer.
- Dagger `†`: no dagger characters were detected in the output.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 11,
    "h2": 33,
    "h3": 0
  },
  "macron_a": 8,
  "macron_e": 10,
  "macron_i": 41,
  "macron_o": 11,
  "macron_u": 2,
  "schwa": 2,
  "greek_chars": 444,
  "combining_diacritics": 24,
  "dagger": 0
}
```

## Structural integrity check

- Headings: source section headings 1–9 are represented as Markdown headings.
- Footnotes: footnotes 1–33 are represented as Markdown notes. Footnote 16 spans two PDF pages and was merged into a single Markdown note.
- Bibliography: separated into a standalone bibliography file.
- Tables: no semantic tables detected in the source.
- Images: no embedded figures/images detected.
- Page-boundary continuation text was joined where evident, but paragraph boundaries across page breaks remain a possible residual-risk area.

## Image inventory

No images detected or extracted.
