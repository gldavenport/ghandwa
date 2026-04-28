---
title: "QA report for Koch 2020 second and third passes"
source_file: "koch-2020.pdf"
generated_utc: "2026-04-28T18:34:25.034941+00:00"
---

# QA report: Koch 2020, *Celto-Germanic*

## Passes performed

- Second pass: cleaned the first-pass Markdown, repaired obvious extraction artifacts, normalized recurring category headings, and extracted figure captions into a companion file.
- Third pass: segmented §§39–51 into a machine-assisted structured lexical dataset and generated normalized bibliography companion files.

## Structured lexical dataset counts

Total parsed entries: 279

By subgroup:

- CG: 166
- ICG: 42
- CGBS: 36
- ANW: 25
- rejected: 10

By corpus section:

- §39 Water and motion over/through water: 15
- §40 Weapons and warfare: 47
- §41 Horse and wheeled vehicle: 10
- §42 Exchange and metallurgy: 12
- §43 Ideology and social organization: 35
- §44 Material culture and subsistence economy: 37
- §45 Language and oral tradition: 14
- §46 Beliefs and the supernatural: 17
- §47 Health and healing: 5
- §48 Anatomy: 12
- §49 Natural world: 40
- §50 Miscellaneous, no definite social domain: 25
- §51 Some rejected entries: 10

Quality flags:

- uncertain marker: 17
- long entry: 16
- review segmentation: 16
- gloss inferred from preceding numbered series: 15
- cross-reference entry: 7
- no reconstructed form parsed: 5
- post-Grimm/rejected-late diagnostic present: 5


## Character-sensitive areas

The second pass improves extraction quality but does not constitute a manual glyph-by-glyph collation against the PDF. The following remain the highest-risk classes for final scholarly use:

- PIE laryngeals and subscript numerals where the PDF uses typographic conventions inconsistently.
- Combining macrons and syllabic marks, especially in long reconstructed forms.
- Greek forms, Palaeohispanic forms, and inscription sigla.
- Corpus entries that contain numbered subentries; these were segmented, but the repeated gloss is sometimes inferred from the preceding entry.
- Figure-heavy pages where captions interrupt the flow of corpus entries in the source PDF.

## Count caveat

The structured lexical extractor returns a machine-assisted working count rather than a critical edition count. It may differ slightly from Koch's own category totals because some numbered subentries, cross-reference entries, rejected entries, and figure-interrupted entries require editorial judgment.

## Files generated

- `koch-2020-second-pass.md`
- `koch-2020-figure-captions.md`
- `koch-2020-lexical-dataset.md`
- `koch-2020-lexical-dataset.csv`
- `koch-2020-lexical-dataset.json`
- `koch-2020-bibliography-normalized.md`
- `koch-2020-bibliography.tsv`
- `koch-2020-second-third-pass-qa.md`
