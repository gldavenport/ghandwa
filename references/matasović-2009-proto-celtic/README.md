# Matasović 2009 Proto-Celtic Markdown Extraction

This package contains a clean Markdown extraction of Ranko Matasović's *Etymological Dictionary of Proto-Celtic* from the uploaded PDF.

## Files

- `matasovic-2009-etymological-dictionary-of-proto-celtic.md` — main Markdown extraction with PDF page anchors.
- `matasovic-2009-entry-index.csv` — parsed lexical-entry index for spreadsheet/database use.
- `matasovic-2009-entry-index.md` — readable Markdown version of the parsed entry index.
- `matasovic-2009-character-and-ocr-audit.md` — automated checklist of suspicious character/OCR patterns.
- `matasovic-2009-extraction-notes.md` — method, pass status, limitations, and recommended further work.
- `matasovic-2009-extraction-stats.json` — summary statistics for the extraction.

## Use notes

The main Markdown is designed for corpus use and search. For exact scholarly citation of forms, verify against the PDF page image using the `<!-- pdf-page: N -->` anchors.


## Fourth-pass update

The main Markdown and entry index have been regenerated after a fourth-pass cleanup. The new companion file `matasovic-2009-fourth-pass-audit.md` records applied corrections and remaining flagged headword patterns. This remains a clean corpus extraction, not a fully manual critical transcription.


## Fifth pass

The fifth pass adds targeted verification cleanup for audit-flagged headwords, false lexical-entry breaks, bracket-class OCR errors, and selected non-ASCII OCR symbols. See `matasovic-2009-fifth-pass-audit.md`.


## Sixth-pass note

This package incorporates a targeted sixth pass addressing the remaining tilde OCR artifacts in the main Markdown, several page-image-verified suspicious headings, and three locally corrupted page regions (notably pages 92, 288, and 438).

## Seventh-pass note

This package incorporates a targeted seventh pass. It resolves the final explicit uncertainty marker, removes remaining `fJ` OCR artifacts, repairs false lexical headings created from continuation lines, and regenerates the entry index, current character/OCR audit, and extraction statistics. See `matasovic-2009-seventh-pass-audit.md`.

## Eighth-pass note

This package incorporates a targeted eighth pass based on the pass 7 search-test report. It corrects residual reference/name OCR patterns, repairs the `*bonu-` entry boundary, verifies selected `bO`/`bOn` and Greek/cognate cases against page images, and regenerates the entry index, stats, and current audit. See `matasovic-2009-eighth-pass-audit.md`.


## Ninth-pass note

This package incorporates a targeted tenth pass based on the pass 8 stress-test report. It repairs false lexical headings promoted from continuation lines, fixes abnormal lexical headings and bracket corruption, reduces residual laryngeal/labiovelar OCR artifacts, corrects reference/name spacing issues, inserts the missing `*tato-` heading, and regenerates the entry index, stats, and current audit. See `matasovic-2009-ninth-pass-audit.md`.


## Pass 10 update

Added `matasovic-2009-tenth-pass-audit.md`, `matasovic-2009-entry-index-validation-pass.md`, and `matasovic-2009-residual-character-artifact-pass.md`.
