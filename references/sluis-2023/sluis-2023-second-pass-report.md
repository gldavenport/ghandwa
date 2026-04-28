# van-sluis-et-al-2023 Second-Pass QA Report

## Scope

This pass checked the structured appendix/isogloss data, not the full prose of the article.

## Actions completed

- Re-extracted Appendix 13.6 from source text using entry-boundary parsing.
- Verified row counts against source appendix structure:
  - Compelling Celto-Germanicisms: 80 rows.
  - Doubtful Celto-Germanicisms: 50 rows.
  - Rejected Celto-Germanicisms: 140 rows.
- Rebuilt:
  - `van-sluis-et-al-2023-isoglosses.tsv`
  - `van-sluis-et-al-2023-compelling-isoglosses.tsv`
  - `van-sluis-et-al-2023-doubtful-isoglosses.tsv`
  - `van-sluis-et-al-2023-rejected-isoglosses.tsv`
- Replaced the Markdown appendix with the checked appendix extraction.
- Normalized line-break hyphenation artifacts in notes, e.g. `nonexclu- sive` -> `nonexclusive`.
- Re-derived interpretation-code and temporal-stratum columns from the source `Interpretation:` field.
- Preserved source notation for Proto-Celtic, Proto-Germanic, and reconstructed forms.

## Data-quality notes

- `DISTANT COUSIN` has no `REF:` line in the extracted Appendix 13.6.2 source text. The references field is intentionally left blank.
- `AXE` appears in the source with an apparent missing closing parenthesis in the PC line. This has not been silently supplied.
- The TSV `stratum` field now preserves multiple/ranged values with semicolon separation where needed, e.g. `0;I`, `I, III;I-II`.
- The TSV `interpretation_category` field now preserves multiple categories with semicolon separation, e.g. `IE?;L`, `IE(?);CGL;GCL`.
- Page anchors are retained from the prior extraction package and refer to PDF page numbers, not printed book-page numbers.

## Current status

```yaml
extraction_status: "complete-clean"
review_status: "isogloss-tables-second-pass-complete"
canonical_form_level: "structured-tables"
```

## Remaining optional future work

- Full form-by-form audit of body prose outside the appendix.
- Proper Markdown footnote conversion.
- Separate normalized lexical fields for gloss, PC form, PG form, and attested forms.
- Cross-corpus mapping against Koch 2020 and Hyllested.
