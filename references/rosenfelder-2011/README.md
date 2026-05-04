---
title: "Extraction report — The Language Construction Kit"
source_file: "rosenfelder-language-construction-kit.epub"
extraction_date: "2026-05-03"
---

# Extraction report

## Source

- Title: The Language Construction Kit
- Creator: Mark Rosenfelder
- Publisher: Yonagu Books
- EPUB date metadata: 2011-10-02T05:00:00+00:00
- Source type: born-digital EPUB

## Method

- Extracted EPUB archive and parsed the OPF spine order.
- Converted XHTML body content to clean Markdown.
- Preserved headings, paragraphs, bullet lists, block examples, tables, footnote references/definitions, external links, inline bold, italics, superscripts, and Unicode characters; inline emphasis is represented with Markdown-compatible HTML tags for stability.
- Extracted images into `images/` and supplied descriptive Markdown alt text plus `image-index.md`.
- Did not add page anchors because the EPUB spine does not contain stable source page numbers.

## Conversion counts

| Item | Source count | Converted / retained |
| --- | ---: | ---: |
| XHTML spine files | 18 | 17 processed; titlepage SVG skipped because cover/title were preserved separately |
| Headings | 295 | 295 |
| Paragraphs | 4682 | 2550 ordinary paragraphs plus 492 list items |
| Tables | 28 | 28 |
| Footnotes | 3 | 3 |
| Images | 58 | 58 image files copied |

## QA notes

- This was not OCR-based, so the main risk is EPUB-to-Markdown structural conversion rather than character recognition.
- Tables were converted into Markdown tables; one table with column spans was flattened with blank cells for spanned columns.
- Inline formatting was inferred from the EPUB CSS class rules. This preserved italics, bold, superscripts, and text-transform uppercase where encoded by the EPUB. Inline bold/italics use Markdown-compatible HTML tags to avoid conflicts with source asterisks and dense linguistic notation.
- A further pass could improve individual image descriptions and inspect wide tables, but no obvious OCR-type character-fidelity risk remains because the source text is born-digital XHTML.

## Final validation pass

See `final-validation-report.md`. The final validation pass restored the omitted inline image, repaired exact-search artifacts, audited all tables/images/footnotes, and packaged the complete image directory with the Markdown.
