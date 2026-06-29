---
title: "Quantity Superlatives in Germanic, or ‘Life on the Fault Line Between Adjective and Determiner’ — Extraction Report"
author: "Elizabeth Coppock"
date: 2019
source_type: born-digital
extraction_date: 2026-05-07
source_file: coppock-2019-quantity-superlatives-germanic.pdf
chunk: extraction-report
---

# Extraction Report

## Source assessment

- Source type: born-digital PDF with a machine-readable text layer.
- Primary input used: extracted text layer. Rendered page images were used as a spot-check for page layout, especially table pages and the rotated summary table.
- Page count: 92 PDF pages, corresponding to journal pages 109–200.
- Embedded images: none detected by `pdfimages -list`; tables are text/vector content rather than discrete raster images.

## Deliverables created

- `coppock-2019-quantity-superlatives-germanic.md` — main article text, including appendix, excluding references.
- `coppock-2019-quantity-superlatives-germanic-bibliography.md` — references section.
- `coppock-2019-quantity-superlatives-germanic-extraction-report.md` — this QC record.
- `manifest.json` — machine-readable manifest and approximate counts.

## Corrections applied

- Removed recurring Cambridge Core download footer and terms-of-use footer from all pages.
- Removed recurring running headers with page numbers.
- Added source-page anchors in the form `<!-- source-page: N -->` for later citation and page checking.
- Recast the title block into Markdown title/source metadata.
- Split the article body and references into separate Markdown files.
- Converted obvious section labels to Markdown headings.
- Applied only minimal hyphenation repair. Many line breaks from the source text layer remain, especially in examples, glosses, footnotes, and tables, to avoid damaging character fidelity and alignment.

## Unresolved issues list

- Footnotes are preserved in the extracted flow close to where the PDF text layer places them. They were not fully renumbered into Markdown footnote syntax in this pass.
- Tables were preserved from the text layer rather than fully normalized into GitHub-style Markdown tables. This is intentional for this pass because the dense crosslinguistic and paradigm tables are vulnerable to column-loss during automated conversion.
- The rotated table on journal p. 182 / PDF p. 74 was preserved from the text layer, but its visual orientation and column relationships should be checked if the table is used for close citation.
- Italics and bold were not systematically reconstructed from font spans. Character fidelity and text recovery were prioritized over typographic styling.
- Some hyphenated line-breaks may remain from the PDF text layer. Some true source hyphens may also be ambiguous where a compound broke at line end.

## Confusion-pair report

The standard Indo-European high-risk laryngeal and macron inventory was checked approximately, but this article is not primarily an Indo-European etymological source.

- `h₁ h₂ h₃`: no instances found.
- `ā ē ī ō ū`: macron-vowel inventory is low or absent in this source; no systematic normalization was applied.
- `ʰ ʷ`: no targeted normalization applied.
- `ə`: approximate count: 0.
- `ṛ ḷ ṃ ṇ`: no targeted normalization applied.
- `ǵ ḱ`: no targeted normalization applied.
- `*` before reconstructed forms: asterisks occur mainly in grammaticality examples, not reconstructed forms.
- `†`: approximate count: 0.

Source-specific high-risk characters and symbols observed approximately: `{"⊕": 17, "−": 68, "Ø": 2, "Ǝ": 2, "ð": 92, "ą": 6, "ä": 84, "ö": 105, "Ä": 5, "Ö": 46, "Å": 23, "á": 23, "é": 11, "í": 67, "ó": 33, "ú": 10, "æ": 36, "ø": 17, "ǫ": 3}`.

## Codepoint inventory

All counts below are approximate and intended for cross-pass regression checking only.

- `h₁`: 0
- `h₂`: 0
- `h₃`: 0
- `ā`: 0
- `ē`: 0
- `ī`: 0
- `ō`: 0
- `ū`: 0
- `ə`: 0
- Greek-range characters: 4
- Combining diacritics: 3
- Dagger `†`: 0
- Unclear markers: 0
- Inferred-character markers `[?]`: 0

## Structural integrity check

- Main section structure from sections 1–12 plus Appendix is present.
- References are separated into a bibliography file.
- Running headers and Cambridge Core footers were removed.
- Page anchors were inserted throughout.
- No embedded/raster images were detected.
- Tables and examples remain searchable but may need a second pass if fully normalized Markdown tables are desired.

## Image inventory

No embedded images were detected, and no image placeholders were inserted.
