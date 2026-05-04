# Watkins 1995 practical pass report

## Scope

This pass reviewed the 191 structured-form suspect rows from the previous normalization pass, then rebuilt the normalized occurrence and unique-form datasets.

## Results

- Suspect rows reviewed: **191**
- Suspect rows retained after correction/acceptance: **100**
- Suspect rows excluded from the deduplicated unique-form table as OCR/regex noise or low-value fragments: **91**
- Remaining included rows with unresolved `quality_flags`: **1**
- Improved occurrence rows: **2680**
- Improved unique-form rows: **2108**
- Greek/index human-collation shortlist rows: **50**

## Resolution policy

Rows were either accepted, corrected, or excluded from the unique-form dataset. Exclusion does not delete the occurrence row: the improved occurrence table preserves the raw extraction, context, and resolution action. It only prevents non-forms such as ellipses, one-character OCR fragments, and prose false positives from polluting the unique-form lookup table.

## Main actions

- accepted-laryngeal-normalization: 90
- excluded-ocr-or-regex-fragment: 80
- excluded-slash-fragment: 6
- corrected-laryngeal-form-footnote-artifact: 3
- excluded-ellipsis-or-ocr-dropout: 2
- excluded-low-value-grade-marker: 2
- corrected-fragment-to-enclitic-kwe: 2
- accepted-short-morpheme-or-segment: 2
- corrected-empty-ending-marker-to-long-o-ending: 1
- corrected-ocr-six-to-long-o-ending: 1
- excluded-standalone-laryngeal-fragment: 1
- corrected-prose-false-positive-to-form: 1

## New files

- `watkins-1995-structured-forms-normalized-occurrences-improved.tsv`
- `watkins-1995-structured-forms-normalized-occurrences-improved.csv`
- `watkins-1995-structured-forms-normalized-unique-improved.tsv`
- `watkins-1995-structured-forms-normalized-unique-improved.csv`
- `watkins-1995-structured-forms-suspect-resolution-log.tsv`
- `watkins-1995-structured-forms-remaining-suspects-after-practical-pass.tsv`
- `watkins-1995-greek-index-human-collation-shortlist.md`
- `watkins-1995-greek-index-human-collation-shortlist.tsv`

## Remaining work

The structured dataset is now cleaner for lookup and deduplication. Remaining character-authoritative work is concentrated in the Greek/index shortlist and would require hand collation against page images, especially long Greek quotations and the index of words.
