---
title: "Lipp 2020 Word Wine — Extraction Report"
author: "Reiner Lipp"
date: 2020
source_type: born-digital
extraction_date: 2026-05-07
source_file: "lipp-2020-word-wine.pdf"
chunk: extraction-report
---

# Extraction Report

## Source identification

- Source type: born-digital PDF with machine-readable text layer present.
- Processing scope: Chapter 10 text and its bibliography, source pages 195–229. Preliminary volume title/contents pages in the PDF were not extracted as chapter content.
- Images: none detected in the PDF.

## Corrections applied

- Removed running headers, page numbers, repeated author-use footer, and the copyright/DOI footer from the chapter opening page.
- Rejoined page-line breaks and repaired most line-end hyphenation in running prose and bibliography entries.
- Repaired a small set of obvious text-layer spacing artifacts in bibliography prose, numeric ranges, URLs, and overlaid macron/acute/tilde sequences.
- Normalized extracted laryngeal notation from ASCII h1/h2/h3 to h₁/h₂/h₃ where the PDF text layer exposed subscript digits as ordinary digits.
- Normalized output text to Unicode NFC after laryngeal repair.
- Split the article body and bibliography into separate Markdown files.
- Added source-page anchors for source-critical checking.

## Unresolved issues

- No `[unclear]` or extraction-inserted `[?]` markers were inserted. A literal `[?]` occurs in the source text and is preserved as source content. This does not certify character-perfect extraction.
- The PDF text layer preserves the base characters for many forms but not all visual formatting. Superscript determinatives and some small-caps styling may appear as plain inline text.
- Some line-end hyphen repairs in dense linguistic forms may require later human review; technical hyphenation was generally preserved when the token contained reconstructed-form notation, slashes, brackets, digits, or combining marks.
- Source-page headers on pages whose page numbers render as control glyphs were discarded as running headers.

## Confusion-pair report

- h₁/h₂/h₃: normalized programmatically from h1/h2/h3. Because the text layer encoded the subscript digits as ASCII digits, this repair should be spot-checked against the rendered PDF in especially dense formulas.
- ā ē ī ō ū: retained from the text layer where present; no exhaustive visual proof was performed for every occurrence.
- ʰ/ʷ: retained where the text layer exposed them; no exhaustive visual proof was performed.
- ə: retained where the text layer exposed it; no exhaustive visual proof was performed.
- ṛ ḷ ṃ ṇ and related underdot forms: retained where the text layer exposed them; no exhaustive visual proof was performed.
- ǵ/ḱ: retained where present; no exhaustive visual proof was performed.
- Asterisk `*`: retained from text layer; no systematic missing-asterisk audit was possible.
- Dagger `†`: retained where present.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 143,
    "h2": 85,
    "h3": 17
  },
  "macron_a": 50,
  "macron_e": 48,
  "macron_i": 159,
  "macron_o": 50,
  "macron_u": 11,
  "schwa": 7,
  "greek_chars": 570,
  "combining_diacritics": 1080,
  "dagger": 6
}
```

## Structural integrity check

- Headings were converted to Markdown heading hierarchy.
- Main article text and bibliography are separated.
- No tables or figures were detected.
- No standalone index is present in the extracted chapter PDF.
- Page anchors were inserted as HTML comments in the Markdown output.

## Image inventory

No images detected; no `images/` directory was created.
