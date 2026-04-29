---
title: "Bibliography audit notes for anthony-2023"
source_title: "Ten Constraints that Limit the Late PIE Homeland to the Steppes"
author: "David W. Anthony"
year: 2023
source_file: "anthony-2023.pdf"
extraction_date: "2026-04-29"
companion_type: "bibliography audit"
---

# Bibliography audit notes for anthony-2023

## Pass completed

This pass focused only on the references section. It used the PDF text layer, `pdftotext -layout`, and rendered reference pages to identify entry starts and correct extraction-only bibliography artifacts.

## Changes made

- Converted the bibliography to one reference per paragraph in the main Markdown file.
- Removed hidden page-anchor comments from inside the bibliography body and replaced them with one source-page note before the references.
- Added `anthony-2023-bibliography-source-style.md` with repeated-author dashes preserved.
- Added `anthony-2023-bibliography-normalized.md` with repeated-author dashes expanded for easier lookup.
- Corrected extraction-only artifacts:
  - `Warinner2022` -> `Warinner 2022`
  - `FStatistics` -> `F-Statistics`
  - `——— .` -> `———.`

## Source-internal citation/bibliography issues left unregularized

These appear to be source-internal irregularities or unresolved bibliographic mismatches, not merely Markdown cleanup problems:

- The body cites `Maier et al. 2023`, while the bibliography entry gives `Maier ... 2022`.
- The body cites `Iverson and Kroonen 2017`, while the bibliography gives `Iversen, Rune, and Guus Kroonen. 2017`.
- The body cites `Mathieson et al. 2018`, but no corresponding `Mathieson` bibliography entry appears in the source bibliography.
- The body refers to `the edited volume Olsen et al. 2023`; the bibliography contains `Olsen, Birgit A. 2023` as a chapter/article-style entry and `Olsen, Birgit A., Thomas Olander, and Kristian Kristiansen (eds.). 2019`, but no matching multi-author 2023 edited-volume entry.
- The bibliography entry `Mallory James P., and Douglas Q. Adams 2006` is preserved as printed/extracted rather than normalized to `Mallory, James P., and Douglas Q. Adams. 2006`.
- The bibliography contains source-style spacing/punctuation irregularities such as `J.van der Plicht`; these were left as source text.

## Further-pass value

A further pass would be useful only if the goal is to convert the bibliography to a formal citation database such as CSL JSON or BibTeX, or to resolve source-internal citation mismatches against external bibliographic databases. For clean corpus Markdown, the bibliography is now in a workable form.
