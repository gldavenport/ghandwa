# Extraction Notes

## Second pass

- Regenerated Markdown from the PDF text layer.
- Removed running headers/page numbers more aggressively.
- Separated footnotes into `data/footnotes-by-page.md` so bottom-of-page notes do not intrude into entry fields.
- Normalized Chapter 2 entry headings and labels where detectable.
- Added clearer diagnostics text for checkbox lines.

## Third pass

- Built `data/lexical-dataset.csv` and `data/lexical-dataset.jsonl` from Chapter 2 lexical entries.
- Built `data/bibliography-normalized.csv`, `.jsonl`, and `.md` from the bibliography.
- Rendered figure pages as PNGs for audit/reference.

## Remaining caveats

- The bibliography parser is heuristic. It preserves the raw reference string in every record, which should be the authoritative field for correction.
- The lexical dataset is structured from the PDF text layer. Special characters, line breaks in comparanda, and long references should be spot-checked for high-value entries.
- Chapter 3 tables are still text-layer extractions, not manually normalized analytical tables.
- Figures are rendered but not hand-transcribed into data tables.
