---
title: "Bibliography audit for Graça da Silva & Tehrani 2016"
source_file: "graça-da-silva-2016.pdf"
extraction_date: "2026-04-28"
pass_type: "bibliography/source-critical review"
---

# Bibliography/source-critical review

This pass reviewed the reference list for line-wrap errors, missing spaces introduced by PDF extraction, author-name errors, diacritics, DOI breaks, and source spellings that should not be silently normalized.

## Results

- The main Markdown keeps a readable normalized line structure for references rather than preserving the PDF column layout.
- DOI line breaks were joined.
- Journal and book titles are italicized where the source clearly presents them as titles.
- `Cathcart` in reference 3 is retained in the main Markdown, correcting the PDF text-extraction artifact `Cahtcart` against the visually legible name.
- Reference 14 retains `folkore`, which appears in the PDF as printed/extracted.
- Reference 17 retains `State of New York University Press`, which appears in the source.

## Further-pass value

Further work would only be useful if the goal is a formal bibliographic database. That would involve checking each reference against DOI/Crossref/library metadata and adding a separate normalized bibliography file while preserving the source bibliography in the main Markdown.
