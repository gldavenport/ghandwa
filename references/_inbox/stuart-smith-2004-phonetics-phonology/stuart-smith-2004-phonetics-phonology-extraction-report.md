---
title: "Phonetics and Philology: Sound Change in Italic — Extraction Report"
author: "Jane Stuart-Smith"
date: "2004"
source_type: "OCR PDF"
extraction_date: "2026-05-24"
source_file: "stuart-smith-2004-phonetics-phonology.pdf"
---

# Extraction Report

## Source assessment

- **Source type:** OCR/Paper Capture PDF, 295 PDF pages.
- **Text-layer quality:** mostly usable for ordinary English prose, but not character-authoritative. The PDF metadata identifies Acrobat 5.0 Paper Capture, and visual sampling showed that Greek, reconstructed forms, superscripts/subscripts, and some phonetic notation are high risk.
- **Layout complexity:** running prose with headings, footnotes, figure captions, several consonant-system tables, bibliography, and two indexes.
- **High-risk zones:** Greek forms, Indic/Sanskrit transliteration, PIE laryngeals and labiovelars, figure/table labels, bibliography, index entries, and any passage intended for quotation or derivational use.

## Corrections applied

- Removed repeated running headers/footers and terminal page numbers where identifiable.
- Reflowed ordinary prose paragraphs at the PDF text-block level and repaired line-break hyphenation where the next line clearly continued a lowercase word.
- Preserved dense correspondence lists, tables, figures, and aligned material as fenced text blocks when forcing Markdown tables would likely damage notation.
- Split the work by source structure: front matter, chapters 1–7, bibliography, index of words, and general index.
- Applied source-specific recurring corrections where safe:
  - `gw` + line-break + `h` → `gʷh`.
  - `H1`, `H2`, `H3` → `H₁`, `H₂`, `H₃`.
  - reconstructed-form `H,` in clear local contexts → `H₁`.
  - obvious ancient-date OCR `EC` after numerals or after “century/centuries/millennium” → `BC`.

## Character-risk assessment

This extraction is suitable for ordinary corpus search and AI parsing of prose structure. It is **not** fully character-authoritative for Greek, IPA, Indic/Sanskrit transliteration, or every reconstructed form. A sample comparison of PDF page 40 showed that the OCR text layer converted Greek forms such as visible Greek letters into Latin approximations or punctuation-like strings. Some of these remain where they were not safely recoverable from recurring patterns.

## Linguistics QC checks performed

- Searched for remaining replacement characters, form feeds, baseline `H1/H2/H3`, broken `gw` + line-break + `h`, and ancient-date `EC` patterns.
- Checked high-risk sample pages visually against rendered PDF images, especially the opening of Chapter 2 with PIE voiced-aspirate notation and Greek correspondence lines.
- Kept tables and correspondence blocks in fenced text to reduce Markdown damage to slashes, brackets, angle brackets, asterisks, and alignment.
- Separated bibliography and indexes into their own files for later dedicated fidelity passes.

## QC counts after cleanup

```json
{
  "replacement_character": 0,
  "unclear_markers": 0,
  "baseline_laryngeal_H1_H2_H3": 0,
  "broken_gw_newline_h": 0,
  "remaining_form_feeds": 0,
  "remaining_EC_date_pattern": 0,
  "fenced_blocks": 11,
  "figure_placeholders": 24
}
```

## Known unresolved issues

- Greek is not globally reliable. The embedded OCR layer frequently substitutes Latin characters, punctuation, or malformed strings for Greek letters and diacritics.
- Some Sanskrit/Indic diacritics and special phonetic symbols may remain simplified or corrupted where the OCR did not capture them.
- Some bibliography and index entries remain OCR-derived and should be checked before formal citation.
- Footnotes were preserved near their page context but not exhaustively realigned to note markers.
- Figure captions are preserved as text, but image contents were not extracted. Figures and maps are represented by captions/placeholders and surrounding text only.
- Page-level locations are represented by file/chunk and PDF page ranges in YAML and manifest, not by inline page markers throughout the body.

## Further-pass recommendation

A second pass would add meaningful value if the extraction will be used for quotation, etymological derivation, or exact philological comparison. The highest-value next pass would be a targeted character-fidelity pass on Greek, Indic/Sanskrit transliteration, PIE reconstructed forms, and the two indexes, using visual page inspection rather than the OCR text layer alone.
