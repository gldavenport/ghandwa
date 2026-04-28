# Wigman 2023 Markdown + Structured Data Extraction

Source file: `wigman-2023-prehistory-italic.pdf`

Work: Andrew Michael Wigman, *Unde vēnistī? The Prehistory of Italic through its Loanword Lexicon* (2023).

## Contents

- `wigman-2023-prehistory-italic.md` — combined second-pass Markdown extraction.
- `chapters/` — chapter/frontmatter split Markdown files.
- `chapters/02-linguistic-data-structured.md` — Chapter 2 recast as structured lexical entries.
- `data/lexical-dataset.csv` and `data/lexical-dataset.jsonl` — machine-readable lexical dataset.
- `data/bibliography-normalized.csv` and `data/bibliography-normalized.jsonl` — normalized bibliography records with raw references retained.
- `data/bibliography-normalized.md` — human-readable normalized bibliography.
- `data/footnotes-by-page.md` — separated footnotes by source PDF page.
- `data/dataset-summary.md` — counts and pass notes.
- `assets/figure-pages/` — rendered full-page PNGs for important figures.

## Chapter split

| File | PDF pages | Section |
|---|---:|---|
| `chapters/00-frontmatter.md` | 1-20 | Front Matter |
| `chapters/01-introduction.md` | 21-58 | 1 Introduction |
| `chapters/02-linguistic-data.md` | 59-310 | 2 The Linguistic Data |
| `chapters/03-feature-analysis.md` | 311-356 | 3 Feature Analysis |
| `chapters/04-distribution-analysis.md` | 357-386 | 4 Distribution Analysis |
| `chapters/05-semantic-analysis.md` | 387-390 | 5 Semantic Analysis |
| `chapters/06-population-genetics-italy.md` | 391-410 | 6 Population Genetics of Italy |
| `chapters/07-archaeological-theories-italicization.md` | 411-422 | 7 Archaeological Theories on the Italicization of Italy |
| `chapters/08-conclusion.md` | 423-432 | 8 Conclusion |
| `chapters/09-bibliography.md` | 433-498 | Bibliography |
| `chapters/10-nederlandse-samenvatting.md` | 499-500 | Nederlandse Samenvatting |
| `chapters/11-curriculum-vitae.md` | 501-502 | Curriculum Vitae |

## Status

This package includes the requested second pass and a first automated third pass: structured lexical data and normalized bibliography. It is suitable for corpus/search use and for building a working lexical index. The normalized bibliography and lexical dataset preserve raw strings for audit; they should be spot-checked before being treated as citation-grade data.
