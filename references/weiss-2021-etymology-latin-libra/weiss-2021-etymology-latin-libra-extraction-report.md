---
title: "The Etymology of Latin lībra — Extraction Report"
author: "Michael Weiss"
date: "2021-01-05"
source_type: born-digital
extraction_date: "2026-05-07"
source_file: "weiss-2021-etymology-latin-libra.pdf"
chunk: extraction-report
---

# Extraction Report

## Source type

Born-digital PDF. The PDF has an embedded machine-readable text layer and embedded fonts. The raw extracted text was used as the primary input; rendered-page inspection and character-position inspection were used where the text layer split scholarly notation into separate superscript/subscript glyphs.

## Output files

- `weiss-2021-etymology-latin-libra.md` — main text, including appendix and footnotes
- `weiss-2021-etymology-latin-libra-bibliography.md` — abbreviations and references
- `weiss-2021-etymology-latin-libra-extraction-report.md` — this QC record
- `manifest.json` — machine-readable extraction metadata

No semantic figures, maps, plates, or image-only tables were present. Two embedded image objects were detected on page 7, corresponding to the emoji in footnote 15 rather than to a figure; no `images/` directory was included.

## Corrections applied

- Rejoined paragraphs broken by PDF lineation and page boundaries.
- Removed running page numbers and page-layout line breaks.
- Preserved page anchors as HTML comments for later source-location checking.
- Converted detected superscript aspiration to Unicode modifier letter `ʰ` in forms such as `*dʰ`, `*līdʰrā`, and `*gʰeu̯d-`.
- Converted detected subscript laryngeal notation to Unicode subscript digits/letter in forms such as `h₁`, `h₂`, `h₃`, and `hₓ`.
- Replaced source-text-layer micro sign `µ` with Greek mu `μ` in Greek words where rendered/semantic context made the PDF mapping appear to be a glyph-encoding artifact.
- Converted footnote references to Markdown footnotes and consolidated footnote text at the end of the main Markdown file.
- Separated the source's abbreviation and reference sections into a bibliography file, while leaving the appendix in the main text.
- Preserved source wording where it appears odd or erroneous, including “This point is made by already…,” “ertsen Konjugation,” “both version,” and the apparent orphan close quotation mark before footnote 17.

## Unresolved-issues list

- The source appears to contain an orphan closing quotation mark and period before footnote 17 after `*lei̯hₓ-`; this was preserved as `’.[^17]`.
- The bibliography entry for Lejeune has `106:l–ll`, which may be intended as roman numerals or OCR-equivalent letterforms in the source text layer. It was preserved as `106:l–ll`.
- The title/heading hierarchy is imposed from the source numbering for Markdown readability; the source itself is formatted as a handout/article with numbered paragraphs rather than conventional named section headings.
- No `[unclear]` markers were inserted. This does not certify that all characters are correct; it only records that no specific unresolved character required an inline uncertainty marker during this pass.

## Confusion-pair report

- `h₁ h₂ h₃`: normalized where the source used subscript digits; output contains approximate counts below.
- Macron vowels `ā ē ī ō ū`: preserved where present in the text layer; no systematic loss found in spot checks.
- `ʰ ʷ`: aspiration `ʰ` was normalized from superscript `h`; no superscript `w` instances were found in the extracted article text.
- `ə`: no schwa instances found.
- `ṛ ḷ ṃ ṇ`: no instances found.
- `ǵ ḱ`: no instances found; the source used `k̑` in `*k̑litreh₂` and `*k̑es-`, which was preserved.
- `*`: reconstructed-form asterisks preserved.
- `†`: no dagger instances found.
- `hₓ`: source-specific laryngeal notation with subscript `x` was normalized and preserved.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

- `h₁`: 3
- `h₂`: 14
- `h₃`: 1
- `ā`: 24
- `ē`: 9
- `ī`: 45
- `ō`: 6
- `ū`: 2
- `ə`: 0
- Greek characters: 629
- Combining diacritics: 23
- `†`: 0

## Structural integrity check

- Headings are consistent with the source's numbered sections and subsections.
- Footnotes 1–22 are present and attached to corresponding Markdown footnote references.
- Verse/scansion examples are preserved in block quotes or fenced text blocks to avoid damage from Markdown paragraph wrapping.
- The bibliography and abbreviations are extracted as a separate file.
- The appendix remains in the main extraction file.
- No image inventory is needed because no semantic figures, maps, plates, or image-only tables were present.
