# Extraction notes: Koch 2020, *Celto-Germanic*

## Source and method

- Source file: `koch-2020.pdf`.
- The PDF has an embedded text layer, so no OCR was performed.
- First pass used raw text extraction from the PDF, then removed running heads and page-number artifacts.
- Headings were lightly converted to Markdown.
- Figure captions were retained as text, but images/diagrams were not separately described.

## First-pass quality assessment

This first pass is usable for reading and broad corpus search. It should not yet be treated as a character-verified lexical reference. The source is much cleaner than a scanned OCR job, but the book is form-heavy: reconstructed forms, laryngeals, syllabic resonants, Greek, Sanskrit transliteration, Palaeohispanic material, figure captions, bibliography, and index entries all raise the risk of quiet character-level errors.

## Recommended second pass

Recommended if this extraction will be used for linguistic work rather than casual reading.

1. Verify reconstructed forms and special characters in the corpus entries, especially:
   - laryngeals such as `H1`, `H2`, `H3`;
   - syllabic resonants such as `r̥`, `l̥`, `m̥`, `n̥`;
   - long vowels and combining macrons;
   - Greek and Palaeohispanic forms;
   - forms broken across line boundaries in the PDF.
2. Check figure-heavy pages for local ordering errors between body text and figure captions.
3. Normalize any remaining line-wrap artifacts where compounds or forms were split by the PDF.
4. Spot-check the bibliography and index for wrapped entries that should be joined.

## Recommended third pass

Recommended if the goal is a reusable lexical dataset or high-confidence reference extraction.

1. Segment the corpus entries into structured fields such as:
   - section;
   - semantic domain;
   - subgroup label: CG, ICG, CGBS, ANW, NW, rejected;
   - headword/gloss;
   - reconstructed form(s);
   - Germanic evidence;
   - Celtic evidence;
   - Italic/Balto-Slavic/other evidence;
   - notes/source discussion.
2. Produce a normalized bibliography file.
3. Optionally create a TSV/CSV or JSON companion lexical dataset from §§39–51.
4. Reconcile the index against corpus headings if the index will be used as a retrieval aid.

## Recommendation

For ordinary corpus search: keep this first pass and optionally do a targeted second pass later.

For lexical extraction, citation, or conlang etymological reuse: do the second pass.

For a structured comparative dataset: do both the second and third passes.
