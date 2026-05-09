---
title: "The Italic words for ‘moon/month’ and ‘sun’: New evidence from the Sabellian languages — Extraction report"
author: "Paolo Poccetti"
date: 2016
source_type: born-digital
extraction_date: 2026-05-07
source_file: poccetti-2016-italic-words-moon-month-sun.pdf
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The raw extracted text was treated as the primary input. Rendered page images were used as a fallback check for page structure, source page numbering, the article title/metadata, the comparison table on source p. 354, and high-risk linguistic notation.

## Corrections applied

- Removed running headers, page numbers, page-boundary breaks, and the title-page layout while preserving source metadata.
- Rejoined wrapped paragraphs and repaired hyphenated line breaks from the PDF text layer.
- Split the source bibliography into `poccetti-2016-italic-words-moon-month-sun-bibliography.md`.
- Lifted page-bottom source footnotes into a Markdown `Footnotes` section in the main file.
- Rendered the source’s two-column syntactic comparison as a Markdown table.
- Normalized laryngeal indices to Unicode subscripts where the text layer exposed baseline digits: `h₁`, `h₂`.
- Corrected obvious extraction artifacts checked against the text layer/rendering, including `Leumann 1077` → `Leumann 1977` and missing spacing at `expected. Nevertheless`.
- Omitted the repeated decorative publisher watermark/stencil image. No substantive figures, maps, plates, or image-only tables were present.
- Avoided Markdown emphasis asterisks in the main text so reconstructed-form asterisks remain semantically meaningful in raw corpus text.

## Unresolved issues

- Source italics are not exhaustively encoded as Markdown/HTML styling in the main text. This is intentional for this pass: character fidelity and reconstructed-form asterisk fidelity were prioritized over typographic styling.
- Some source asterisks before reconstructed forms were normalized from the text-layer pattern rather than visually checked one by one. The major PIE/Sabellian/Italic forms were checked for obvious `h1/h2` and asterisk-loss problems, but the pass should not be treated as character-authoritative.
- The source text appears to contain a citation mismatch: footnote 3 cites `Rix 1997`, while the bibliography lists `Rix, Helmut. 1996. Variazioni locali in osco`. This was preserved rather than silently reconciled.
- The source uses authorial uncertainty in inscription text (`[ekuk iuvilu ?]`); this is source text, not an extraction uncertainty marker.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: no ASCII `h1`, `h2`, or `h3` remained in the output files after normalization. This was checked by pattern search, not by a full visual collation.
- Macron vowels: macron vowels were retained in the main text where present in the text layer. Dense forms and bibliography were not visually checked letter by letter.
- Superscript/subscript formatting: laryngeal digits were normalized to Unicode subscripts. The source’s `CIL I²` was retained as superscript two where represented in the cleaned extraction.
- `ʰ ʷ`, `ə`, `ṛ ḷ ṃ ṇ`, `ǵ ḱ`, and `†`: no source instances were identified in this article extraction.
- Reconstructed-form asterisk `*`: source-form asterisks were reviewed and restored conservatively after removal of Markdown emphasis. This remains a potential weak spot for future pass work because source typography and reconstructed-form marking overlap in the PDF text layer.

## Codepoint inventory

All counts are approximate and for cross-pass comparison only.

| Item | Approximate count |
|---|---:|
| `h₁` | 26 |
| `h₂` | 32 |
| `h₃` | 0 |
| `ā` | 101 |
| `ē` | 27 |
| `ī` | 3 |
| `ō` | 19 |
| `ū` | 16 |
| `ə` | 0 |
| Greek characters | 129 |
| Combining diacritics | 15 |
| `†` | 0 |

## Structural integrity check

- Headings are consistent for title, abstract, numbered sections, conclusion, and footnotes.
- Source footnotes are attached through Markdown footnote references.
- The main comparison table is well-formed Markdown.
- References were separated into a standalone bibliography file.
- No image inventory is required; no substantive source figures were extracted.

## Image inventory

No substantive figures, maps, plates, or image-only tables were present. Repeated decorative watermark/stencil images were omitted.
