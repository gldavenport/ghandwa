# Notes: Swanenvleugel 2021 extraction

## Status

- `extraction_status`: `complete-working`
- `review_status`: `appendices-cleanup-complete`
- `canonical_form_level`: `appendices-only`

This is a clean working extraction intended for search, comparative use, and Ghandwa planning. It is not a diplomatic transcription. Appendices A–C have been cleaned and checked against the rendered PDF pages; the main body has not received a full form-level canonical audit.

## Deliverables

- `swanenvleugel-2021.md` — Markdown extraction with YAML and page anchors.
- `swanenvleugel-2021-pic-sound-changes.tsv` — structured Appendix C chronology inventory.
- `swanenvleugel-2021-obstruent-systems.tsv` — structured Appendix A obstruent systems.
- `swanenvleugel-2021-pic-phonology.tsv` — structured Appendix B PIC phoneme system.
- `swanenvleugel-2021-tam-summary.tsv` — high-level structured TAM category/formant inventory based on sections 7–9 and the conclusion.
- `swanenvleugel-2021-next-pass-handoff.md` — future cleanup/upgrade instructions.

## Appendix cleanup completed

- Appendix A, reconstructed obstruent systems: checked against PDF pages 68–69.
- Appendix B, Proto-Italo-Celtic phoneme system: checked against PDF page 70.
- Appendix C, relative chronology: checked against PDF page 71.
- Removed extraction artifacts in the appendix Markdown, especially broken code blocks and spaces inside forms such as `*RD̉C`, `*g /g̉/`, `[k̉t]`, `*L̥V`, `-p̉t-`, `-ts̉t-`, `-k̉t-`, and `-k̉wt-`.

## Notation cautions

- Preserve the author’s distinctions among PIE, PIC, PIt., and PC notation.
- Do not silently normalize the author’s use of `*ƀ`, `*đ`, `*ǥ`, `*ǥw`, `*þ`, glottalic marks, or laryngeal notation into another system.
- Appendix A and C are source-derived tables; the TAM summary is a structured analytical digest rather than a direct table from the source.
- The source uses both phonological and phonetic notation in places, including slash/bracket-style distinctions. Preserve these when performing a future form-level audit.

## Main value for Ghandwa

This work is useful for designing intermediate branch stages, comparing Celtic/Italic-style phonological developments, modeling verbal TAM renewal/periphrasis, and keeping phonology and verbal morphology connected.

## Current limitations

- Footnotes are readable but not converted into a polished Markdown footnote apparatus.
- Main text is clean and searchable, but dense examples should still be checked against the PDF before being treated as canonical data.
- Appendix tables are now cleaned; the rest of the work remains a clean working extraction rather than a form-level audited edition.
