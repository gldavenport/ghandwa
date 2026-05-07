# Extraction Notes

## Source

Ranko Matasović, *Etymological Dictionary of Proto-Celtic*. Brill, 2009. Source PDF page count: 460.

## Method

- Extracted text from the PDF's existing text layer with Poppler `pdftotext`, using page/range extraction rather than a single full-file extraction because full-file extraction stalled on this PDF.
- Reassembled all 460 PDF pages in order.
- Added `<!-- pdf-page: N -->` anchors for later source-critical checking.
- Converted probable lexical headwords into level-3 Markdown headings.
- Bolded major lexical field labels where they were recognized.
- Applied conservative OCR/field-label cleanup only. Technical forms were not globally normalized.

## Pass status

1. First pass: full text-layer extraction and page reassembly.
2. Second pass: automated structural cleanup, page anchors, lexical-heading detection, field-label cleanup, companion entry index.
3. Third pass: limited automated character/OCR audit. This pass identifies suspicious patterns but does not attempt full manual correction.
4. Fourth pass: high-confidence automated cleanup of laryngeal subscripts, long `ā` in starred forms, selected superscript labiovelars/aspirates in starred forms, common source sigla, author/name diacritics, and selected bracketed grammar-label OCR errors, and targeted run-together field labels. Representative page images were spot-checked, but the whole dictionary was not manually verified entry-by-entry.
5. Fifth pass: targeted verification cleanup of audit-flagged headwords, false entry breaks, bracket errors, and selected OCR-symbol issues, with page-image spot checks for representative high-risk forms.
6. Sixth pass: targeted cleanup of remaining tilde OCR artifacts and suspicious headings.
7. Seventh pass: targeted cleanup of residual uncertainty/bracket-glyph/false-heading issues.
8. Eighth pass: search-test-driven reference/name/entry-boundary cleanup.
9. Ninth pass: stress-test-driven cleanup of false headings, abnormal headings, residual laryngeal/labiovelar OCR artifacts, and reference/name artifacts.

## Known limitations

- The PDF text layer is OCR-derived and contains known character substitutions, especially in reconstructed forms, laryngeals, long vowels, Old Irish/Celtic abbreviations, Greek, and bibliographic sigla.
- The main Markdown should be treated as corpus-ready for search and reading, but not as character-perfect for citation of reconstructed forms without checking the page image.
- Capital vowel placeholders in some headwords and forms may represent long vowels in the printed source, but they were not automatically converted.
- ASCII `h1`, `h2`, `h3` laryngeals were preserved as extracted rather than globally converted to subscript characters.
- The page image controls whenever the extracted text conflicts with the source image.

## Recommended future pass

A further manual verification pass would still add value for Greek, Sanskrit, Old Irish forms, bibliography, remaining uppercase placeholders/variables in headwords, and dense PIE reconstructions. Use `matasovic-2009-fourth-pass-audit.md` as the current checklist.


## Sixth pass

Targeted cleanup of remaining tilde OCR artifacts and suspicious headings. Page-image checks were used for the previously flagged headings and for corrupted regions on pages 92, 288, 323, 438, and selected other pages. Remaining uncertainty is explicitly marked where the page image was not safely readable enough for a confident restoration.

## Seventh pass

Targeted cleanup of residual issues after pass 6. This pass resolved the last explicit `[unclear]` marker, corrected remaining `fJ` OCR artifacts, repaired false level-3 lexical headings created by page-boundary continuation lines, checked selected high-risk Breton/Avestan/PIE forms against page images, regenerated the entry index, and replaced the stale character/OCR audit with a current pattern-count audit.

No explicit `[unclear]` markers remain in the main Markdown after this pass. The source is still OCR-derived and should not be treated as a character-perfect scholarly edition without page-image checking of citation-critical forms.

## Eighth pass

Targeted cleanup based on the pass 7 search-test report. This pass corrected residual source-name and reference OCR patterns, repaired the `*bonu-` entry boundary on page 76, checked selected `bO`/`bOn` and Greek/cognate cases against page images, and regenerated the entry index and current OCR audit. The result is better for search and lexical lookup, but remains OCR-derived rather than character-perfect.


## Ninth pass

Targeted cleanup based on the pass 8 stress-test report. This pass removed several false lexical headings created from continuation lines; repaired abnormal lexical headings with missing quotes, bad brackets, digit/letter OCR substitutions, and corrupted glosses; inserted the missing `*tato-` heading; corrected targeted residual laryngeal and labiovelar OCR artifacts; cleaned reference/name spacing artifacts; regenerated the entry index, extraction stats, and current character/OCR audit. The source remains OCR-derived and should still be page-checked for citation-critical forms.


## Pass 10 update

Added `matasovic-2009-tenth-pass-audit.md`, `matasovic-2009-entry-index-validation-pass.md`, and `matasovic-2009-residual-character-artifact-pass.md`.
