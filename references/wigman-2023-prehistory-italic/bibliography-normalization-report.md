# Bibliography Normalization Report

## Source

- Source: `wigman-2023-prehistory-italic.pdf`
- Source pages: PDF pp. 433–498
- Extraction method: direct text-layer block extraction from the bibliography pages.
- Source order was preserved.
- No external bibliographic validation was performed.

## Outputs

- `data/bibliography-normalized.csv` — tabular normalized records.
- `data/bibliography-normalized.jsonl` — one JSON object per record, with parsed author arrays.
- `data/bibliography-normalized.md` — human-readable normalized bibliography with raw references in collapsible blocks.
- `data/bibliography-csl.json` — CSL-style JSON export.
- `data/bibliography.bib` — BibTeX-style export.
- `review/bibliography-review-needed.csv` — entries with medium/low confidence, missing years, missing titles, or other warnings.

## Counts

- Total records: **988**
- Electronic sources: **8**
- Print sources: **980**

### By type

- `journal_article`: 472
- `book`: 340
- `chapter`: 134
- `reference_work`: 16
- `thesis_or_dissertation`: 9
- `electronic_source`: 8
- `conference_paper_or_handout`: 4
- `journal_article_title_missing`: 2
- `book_or_report`: 2
- `newspaper_or_periodical_item`: 1

### By parse confidence

- `high`: 966
- `medium`: 22
- `low`: 0

### Warning categories

- `year-not-found`: 8
- `chapter-editors-not-detected`: 7
- `title-not-present-in-source`: 3
- `chapter-pages-not-detected`: 3
- `inserted-missing-title-container-boundary`: 1

## Normalization decisions

- Footnote bodies embedded inside the bibliography page text layer were excluded from reference records; footnote callout numbers 580–584 were removed where they attached to entries.
- Open-ended reference years such as `1988-` were normalized as `1988-present` while retaining `raw_year`.
- Forthcoming references marked `fthc.` were normalized with `year = fthc` and `date_note = forthcoming`.
- Page ranges and line-broken compounds were repaired when the PDF text layer inserted a line break after a hyphen; intentional German forms such as `Sprach- und ...` were preserved.
- Parsed fields are normalized, but `raw_reference` remains authoritative for audit.

## Items still worth hand-reviewing

- Entries in `review/bibliography-review-needed.csv`, especially source records with missing years, missing titles, or `chapter-pages-not-detected`.
- Bibliographic databases such as `[eDiAna]`, `[GPC]`, `[LKŽ]`, `[OED]`, and `[TLL]` have no explicit year in the source reference.
- A few source references appear incomplete or malformed in the dissertation bibliography itself; these are preserved rather than silently corrected.
