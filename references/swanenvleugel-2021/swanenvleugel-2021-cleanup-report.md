# Cleanup report: Swanenvleugel 2021

## Scope

This pass cleaned and verified Appendices A–C and renamed package files to use `swanenvleugel-2021` as the work identifier.

## Appendix verification

- Appendix A, reconstructed obstruent systems: checked against PDF pages 68–69.
- Appendix B, Proto-Italo-Celtic phoneme system: checked against PDF page 70.
- Appendix C, relative chronology: checked against PDF page 71.

## Appendix Markdown cleanup

The appendix section in `swanenvleugel-2021.md` was rewritten from broken extraction blocks into clean Markdown:

- Appendix A is represented as Markdown tables for Proto-Italic, Proto-Celtic, and Proto-Italo-Celtic obstruent systems.
- Appendix B is represented as Markdown tables for consonants and vowels, with notes preserved.
- Appendix C is represented as ordered and unordered Markdown lists.

## Structured table cleanup

The appendix TSVs were rewritten from the checked appendix data:

- `swanenvleugel-2021-obstruent-systems.tsv`
- `swanenvleugel-2021-pic-phonology.tsv`
- `swanenvleugel-2021-pic-sound-changes.tsv`

Appendix C now separates stage-heading rows from subchange rows for stages 6–8.

## Notation cleanup

Targeted visible corrections included:

- `*RD̉ C` → `*RD̉C`
- `*g /g̉ /` → `*g /g̉/`
- `/n̥ /` → `/n̥/`
- `[k̉ t]` → `[k̉t]`
- `*L̥ V` → `*L̥V`
- selected spacing inside `-p̉t-`, `-ts̉t-`, `-k̉t-`, and `-k̉wt-`

## Status after cleanup

- `extraction_status`: `complete-working`
- `review_status`: `appendices-cleanup-complete`
- `canonical_form_level`: `appendices-only`
