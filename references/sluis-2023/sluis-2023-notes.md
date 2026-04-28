# Notes: Van Sluis / Jørgensen / Kroonen extraction

## Status

- `extraction_status`: `complete-working`
- `review_status`: `structured-appendix-extraction-complete`
- `canonical_form_level`: `false`

This is a clean working extraction intended for comparative IE research, Ghandwa lexical-strata modeling, and later corpus standardization. It is not a diplomatic transcription.

## Deliverables

- `van-sluis-jorgensen-kroonen-celto-germanic-isoglosses-revisited.md` — Markdown extraction with YAML and page anchors.
- `van-sluis-jorgensen-kroonen-isoglosses.tsv` — combined compelling + doubtful isogloss table.
- `van-sluis-jorgensen-kroonen-compelling-isoglosses.tsv` — compelling isoglosses only.
- `van-sluis-jorgensen-kroonen-doubtful-isoglosses.tsv` — doubtful isoglosses only.
- `van-sluis-jorgensen-kroonen-rejected-isoglosses.tsv` — rejected isoglosses.
- `van-sluis-jorgensen-kroonen-classification-schema.tsv` — RT/MO/SM/LX and IE/loan-category crosswalk.
- `van-sluis-jorgensen-kroonen-strata.tsv` — temporal strata 0-IV.
- `van-sluis-jorgensen-kroonen-mechanisms.tsv` — three proposed mechanisms for the isoglosses.
- `next-pass-handoff.md` — future cleanup instructions.

## Structured extraction counts

- Compelling isoglosses: 80
- Doubtful isoglosses: 50
- Rejected isoglosses: 140

## Notation cautions

- Preserve source distinctions among PC, PG, PIE, and broader CG reconstructions.
- Do not silently normalize the source’s interpretation labels: `IE`, `IE(?)`, `IE?`, `L`, `3L`, `ML`, `CGL`, `GCL`.
- Do not flatten temporal strata such as `I-II` into a single stage.
- The appendix tables are source-derived, but the Markdown appendix formatting is normalized for readability.

## Main value for Ghandwa

This work is useful for building a reusable classification system for lexical evidence:
root isoglosses, morphological isoglosses, semantic isoglosses, lexical isolates, substrate loans, mutual loans, and directionally interpreted Celtic-Germanic loans.

## Current limitations

- Every appendix entry was parsed into a structured table, but individual body-text examples outside the appendix were not exhaustively converted into an evidence database.
- Rejected-entry references occasionally wrap in the source PDF; the first `REF:` line is extracted as the reference field, and wrapped reference continuation may appear in the notes field.
- Page anchors are PDF-page anchors, not printed book-page anchors.

## Filename convention update

This package uses `van-sluis-et-al-2023` as the stable filename base for this work.

## Hidden future-pass note

- Future-pass guidance is also embedded silently at the end of `van-sluis-et-al-2023.md` as an HTML comment block.
