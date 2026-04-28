---
title: "Second and third pass report for de Vaan 2019 Markdown extraction"
source_file: "vaan-2019.pdf"
article: "Michiel de Vaan, On the homonymy of ‘put’ and ‘suck’ in Proto-Indo-European"
date: "2026-04-28"
---

# Pass report

## Second pass: character-fidelity cleanup

Completed.

Actions taken:

- Verified the article against the born-digital PDF text and rendered table pages.
- Rechecked the summary tables, especially the PIE forms, Greek forms, Lithuanian/Baltic diacritics, and Sanskrit forms.
- Repaired visible line-break artifacts in the clean Markdown, including `Ἀπόλ- λωνα` → `Ἀπόλλωνα`.
- Restored missing punctuation in the Baltic paragraph: `Lithuanian dėlė̃, Latvian dēle`.
- Normalized the table entry `Lith. dėlė̃, Latvian dēle ‘leech’`.
- Normalized Unicode to NFC for more stable searching and reuse.
- Repaired bibliography spacing artifacts such as `Leiden/ Boston`, `Indo- Iranian`, `Duchesne- Guillemin`, `R̥ g-Veda`, and page-range spacing.

## Third pass: structured data and bibliography normalization

Completed.

New companion files:

- `vaan-2019-summary-tables-dataset.md`
- `vaan-2019-summary-tables-dataset.csv`
- `vaan-2019-summary-tables-dataset.json`
- `vaan-2019-bibliography-normalized.md`
- `vaan-2019-bibliography-normalized.csv`

The structured dataset is based on Tables 1-5 and uses one row per evidence item. It separates table number, formation, semantic group, branch/language, form, gloss, compact source entry, and notes.

The bibliography normalization is conservative. It repairs extraction artifacts and assigns citation keys, but does not attempt external authority matching, DOI lookup, or BibTeX enrichment.

## Need for further passes

No further pass is needed for a clean corpus Markdown extraction.

A later optional pass would only be useful for one of these specialized goals:

- full diplomatic reproduction of the source typography;
- externally verified bibliography with DOIs/ISBNs and BibTeX;
- full lexical database expansion beyond the five summary tables;
- character-by-character verification against page images for every non-ASCII string in the article.
