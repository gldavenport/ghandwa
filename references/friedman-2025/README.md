# Friedman & Joseph 2025 — The Balkan Languages — Markdown Extraction

Source file: `friedman-2025.pdf`  
Source work: Victor A. Friedman and Brian D. Joseph, *The Balkan Languages* (Cambridge University Press, 2025), DOI `10.1017/9781139019095`.

This archive contains the second- and third-pass Markdown extraction.

## Main files

- `friedman-2025-the-balkan-languages-pass-3.md` — combined clean Markdown.
- `split/` — chapter/division-level Markdown files.
- `structured-data/heading-outline.tsv` — heading outline with page anchors.
- `structured-data/tables-index.tsv` — table index.
- `structured-data/tables-extracted.md` — table blocks, with draft normalization where possible.
- `structured-data/examples-index.tsv` — numbered linguistic example index.
- `structured-data/figures-index.tsv` — figure-caption index.
- `structured-data/footnotes-index.tsv` — footnote index.
- `quality-control/qa-report.md` and `quality-control/qa-report.json` — QA summary.
- `extraction-notes.md` — notes on pass decisions and remaining limitations.

## Pass decisions

The main Markdown favors clean, readable text over physical layout. Page anchors are retained as HTML comments in the form:

```markdown
<!-- pdf-page: 221 -->
```

Tables and numbered examples are preserved more conservatively because alignment and line breaks often carry linguistic information.

## Further-pass assessment

No further broad pass is recommended for corpus/search use. A further pass would only be useful for a narrower data product, especially fully normalized tables, hand-verified examples, or figure-level extraction.
