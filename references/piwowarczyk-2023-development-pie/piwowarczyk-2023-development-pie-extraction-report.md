---
title: "Extraction report — On the Development of the Proto-Indo-European *u̯ih₁-ró-, ‘Man’, in Latin"
author: "Dariusz R. Piwowarczyk"
date: 2023
source_type: born-digital
extraction_date: 2026-05-07
source_file: piwowarczyk-2023-development-pie.pdf
chunk: extraction-report
---

# Extraction report

## Source assessment

- Source type: born-digital PDF with machine-readable text layer.
- PDF metadata inspected: 10 pages; Adobe InDesign source; embedded text layer present.
- Rendered pages were generated for spot-checking high-risk notation and PDF-positioned subscript glyphs.
- No embedded raster images, figures, maps, plates, or image-only tables were detected.

## Corrections applied

- Removed running page numbers, running headers, footer artifacts, and `CC_XXVI.indb` production stamps.
- Rejoined paragraph line breaks and repaired line-break hyphenation where the split was clearly typographic.
- Converted footnote markers and footnote bodies to Markdown footnotes.
- Split the article bibliography into a separate bibliography file.
- Normalized PDF-positioned laryngeal notation where the text layer exposed the base character plus a smaller lowered index:
  - `h1` → `h₁`
  - `hx` → `hₓ`
- Removed extraction-inserted spaces caused by the combining inverted breve below:
  - `u̯ ih₁` → `u̯ih₁`
  - `u̯ ei̯h₁` → `u̯ei̯h₁`
- Repaired one extraction-order artifact in the form `*̯ueis-os` to `*u̯eis-os`, based on the same combining-breve behavior elsewhere.
- Preserved the source’s plain `LIV2` abbreviation rather than normalizing it to `LIV²`, because the PDF text layer and glyph positioning show an ordinary baseline `2`.
- Preserved source wording where it appears unusual, including `labō, ‘tottle’` and `rupex, ‘a rough’`; no emendation was made.

## Unresolved issues list

- No `[unclear]` markers were inserted.
- Italicization was reconstructed from source context and visible styling but was not exhaustively audited at the individual glyph level. Textual characters and forms should be treated as more reliable than Markdown emphasis boundaries.
- Footnote-marker placement was normalized to Markdown footnote syntax. This may slightly regularize punctuation around quotation marks and footnote numbers, but the footnote content and numbering were preserved.
- The output does not claim full character authority; consistent errors could still remain if they were present in both the raw text layer and the spot-checked rendering.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: instances of `h1` in the PDF text layer were converted to `h₁` where the glyph was positioned as a lowered index. No `h₂` or `h₃` instances were found. No remaining ASCII `h1`, `h2`, or `h3` forms are known in the output.
- Source-specific `hₓ` vs. `hx`: two lowered-index `x` instances were converted to `hₓ` in `*puhₓ-` and `*phₓu-`.
- Macron vowels: macrons in Latin, Indic, and reconstructed forms were preserved where detected. Dense forms were spot-checked, not exhaustively certified.
- Superscript modifier letters `ʰ`, `ʷ`: none detected.
- Schwa `ə`: none detected.
- Underdot letters: none detected.
- Acute consonants `ǵ`, `ḱ`: none detected.
- Asterisk before reconstructed forms: retained. Markdown emphasis may affect visual rendering in some viewers, but the asterisk character is present in the source Markdown text.
- Dagger `†`: none detected.
- Combining inverted breve below in `u̯` and `i̯`: preserved; extraction-inserted spaces after `u̯` were removed.
- Greek characters: none detected.

## Codepoint inventory

Approximate counts across main extraction and bibliography:

| Item | Approximate count |
|---|---:|
| `h₁` | 16 |
| `h₂` | 0 |
| `h₃` | 0 |
| `hₓ` | 2 |
| `ā` | 7 |
| `ē` | 3 |
| `ī` | 23 |
| `ō` | 8 |
| `ū` | 6 |
| `ă` | 1 |
| `ĕ` | 1 |
| `ə` | 0 |
| Greek characters | 0 |
| Combining diacritics | 34 |
| Dagger `†` | 0 |
| `u̯` | 23 |
| `i̯` | 3 |

All counts are approximate and intended for cross-pass comparison only.

## Structural integrity check

- Headings are consistent and follow the article’s numbered sections.
- Main text and bibliography are separated according to project deliverable rules.
- Footnotes are attached and numbered 1–42.
- Enumerated sound-change sequences in sections 3 and 6 were converted to Markdown ordered lists.
- No tables were present.
- No figures or image-only elements were present.
- Page anchors were retained as HTML comments at useful transition points.

## Deliverables produced

- `piwowarczyk-2023-development-pie.md`
- `piwowarczyk-2023-development-pie-bibliography.md`
- `piwowarczyk-2023-development-pie-extraction-report.md`
- `manifest.json`
