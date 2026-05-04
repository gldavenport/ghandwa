# Kroonen 2013 — seventh combined targeted pass notes

Date: 2026-04-30T18:35:00Z

## Scope

This seventh pass combined four workstreams:

1. Residual-audit cleanup.
2. Selected page-image verification.
3. References support pass.
4. Dictionary headword/opening-line audit plus structured lexical dataset extraction.

This is still a targeted verification pass. It is not a complete line-by-line, page-image-controlled edition of all 833 PDF pages.

## Main Markdown changes

- Applied 115 replacements across 30 correction-ledger rows.
- Replaced remaining high-confidence arrow remnants such as `:::>` and `::>` with `⇒`.
- Corrected remaining OCR forms of `Verschärfung`.
- Corrected selected high-confidence bibliography terms and diacritics.
- Page-image-verified selected problem passages on PDF pages 91, 172, 310, and 531.

## Page-image-verified corrections in this pass

- Page 91: Greek forms in the `*barkjan-` entry: `φάρυγξ`, `φάραγξ`.
- Page 172: `*faþma-`, `faðmr`, `fæþm`, `*faþmjan-`, `*faþmōjan-`, `*faþō-`, `faþa`, `*faþþōn-`.
- Page 310: Greek forms in the `*irha-` entry: `δόρξ`, `ζόρξ`, `ἴορκες`, `ὕρκες`.
- Page 531: Greek `ἧκα` in the `*suk(k)on-` entry.

## Residual audit

The residual audit file is intentionally broad. It still flags many OCR-hostile Greek/index contexts and suspicious headword characters so they can be used as a future punch list.

Residual-audit category counts:

- suspicious_greek_ocr: 2518
- slash_in_headword: 227
- uppercase_p_in_headword: 55
- replacement_or_control: 7
- unclear_marker: 5

Remaining `[unclear]` markers are now concentrated in index material rather than the dictionary-entry corrections handled in this pass.

## Headword/opening-line audit

Parsed dictionary-entry opening lines: 2885

Verification status counts:

- pdf-text-headword-found: 2823
- not-found-in-pdf-text-layer: 39
- page-image-verified-selected: 23

Common flags:

- no-proto-arrow-or-distribution-detected: 376
- suspicious-headword-characters: 343
- missing-or-unparsed-gloss: 179

`pdf-text-headword-found` means the parsed headword was found in the PDF text layer on the same page. It does not mean the entry has been page-image verified. `page-image-verified-selected` is reserved for the selected pages checked in this pass.

## References pass

The references companion file was rebuilt from the PDF text layer for pages 642-677, reflowed into one bullet per detected citation record where possible, and cleaned for selected high-confidence OCR/diacritic problems.

- Rebuilt cited-publication records: 479
- Flagged reference records for follow-up: 32

This references file is a verification aid and cleaner working draft, not a fully character-authoritative bibliography.

## Lexical dataset

The companion lexical dataset extracts:

- headword
- homonym number when parsed
- grammatical label
- gloss
- PDF page anchor
- distribution label
- proto/comparison field
- first attestations
- verification status
- flags

It is intended for searching and downstream analysis. It should not replace the main Markdown extraction.

## Recommended next step

Use the residual audit and headword-line verification files as a punch list if you want to continue. The most valuable next unit would be an alphabet-block headword verification pass, starting with entries whose headword has `/`, `P`, `{}`, `[]`, or missing/unparsed gloss fields.
