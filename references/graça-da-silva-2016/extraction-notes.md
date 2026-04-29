---
title: "Extraction notes for Graça da Silva & Tehrani 2016"
source_file: "graça-da-silva-2016.pdf"
extraction_date: "2026-04-28"
---

# Extraction notes

## Pass status

This package contains a clean Markdown extraction of the article plus companion audit files.

Completed work:

- Removed running headers, footers, page numbers, decorative dot leaders, and page geometry.
- Reordered the article into logical reading order.
- Preserved article metadata, abstract, section structure, methods subsections, acknowledgements, funding, competing interests, references, captions, and tables.
- Converted Tables 1 and 2 into Markdown tables.
- Added accessible descriptions for Figures 1–4.
- Added an extracted Figure 4 corpus-membership companion CSV.
- Completed an additional Figure 4 confidence audit. The CSV now includes `secure_ge_70`, corresponding to bold source-figure entries.
- Completed a targeted character audit of high-risk glyphs and linguistic/statistical notation.
- Completed a bibliography/source-critical review pass focused on extraction artifacts, source spellings, diacritics, and DOI joins.

## Key additional-pass changes

- Figure 4 bold/non-bold marking was audited against a high-resolution rendering and the PDF’s embedded font data.
- The discussion’s PIE metal-word notation was changed from `*aios*` to `*ai⌢os*` to preserve the source glyph.
- The source spelling `folkore` in reference 14 is retained, with a silent Markdown note, rather than silently corrected.

## Remaining limits

- This is clean Markdown, not diplomatic transcription.
- The Figure 4 confidence audit preserves the source figure’s visual/font-based marking; it does not independently recalculate ancestral-state likelihoods.
- The bibliography is cleaned for readability and source-critical extraction, but it is not a fully authority-controlled bibliographic database.

## Further-pass recommendation

No further pass is needed for ordinary corpus research use. A further pass would only add meaningful value if you want either:

1. a formal normalized bibliography checked against DOI/Crossref/library metadata, or
2. an extraction of the electronic supplementary tables into structured data.
