# hartman-2023 third-pass Markdown package

This package contains a third-pass clean Markdown extraction of Frederik Hartmann, *Germanic Phylogeny* (Oxford University Press, 2023), plus sidecars for Appendix data, figure descriptions, special-character/form auditing, and reference normalization.

## Files

- `hartman-2023-third-pass.md` — main third-pass clean Markdown extraction.
- `appendix-innovation-dataset-third-pass.tsv` / `.csv` — normalized Tables A.1-A.21, preserving source-coded anomalies.
- `appendix-feature-occurrence-times-third-pass.tsv` / `.csv` — normalized Tables A.22-A.42.
- `appendix-combined-dataset-third-pass.tsv` / `.csv` — aligned combined Appendix dataset.
- `appendix-cell-verification.md` — third-pass Appendix value audit and anomaly notes.
- `figures-visual-descriptions.md` — accessible descriptions for figures.
- `special-character-and-forms-audit.md` — character inventory and reconstructed-form audit notes.
- `reconstructed-forms-index.tsv` — token index of reconstructed/special-character forms.
- `references-third-pass.md` — one-entry-per-paragraph normalized references.
- `references-third-pass.bib` — best-effort BibTeX export.
- `references-third-pass.csl.json` — best-effort CSL JSON export.
- `tables-index-third-pass.md` — table index.
- `third-pass-notes.md` — extraction notes and remaining limits.

## Use guidance

Use the TSV sidecars rather than Markdown tables for computational reuse. Treat the three Appendix `3` values as source anomalies requiring an explicit recoding decision before binary modelling.
