# Third-pass extraction notes

## Source

- Source PDF: `hartman-2023.pdf`
- Title: *Germanic Phylogeny*
- Author: Frederik Hartmann
- Publisher/year: Oxford University Press, 2023

## What changed in this pass

1. The second-pass Markdown was promoted to a third-pass version with updated extraction notes.
2. The Appendix sidecars were preserved and audited for non-binary values.
3. The three non-binary Appendix values were checked against rendered page images and retained as source anomalies.
4. A special-character and reconstructed-form audit was added, with a TSV token index for high-risk forms.
5. Figure captions were upgraded from a caption-only index to an accessible visual-description sidecar.
6. The reference list was normalized again from the PDF reference pages and exported as Markdown, BibTeX, and CSL JSON sidecars.

## Limits retained deliberately

- The third-pass main Markdown is still a clean reading/corpus extraction, not a diplomatic edition.
- The figure descriptions are accessibility descriptions, not full data recreation from plots.
- The BibTeX and CSL JSON exports are best-effort citation-manager starting points. They should be verified before publication or formal bibliography use.
- The Appendix `3` values are not corrected because the rendered source pages show them as `3`.

## Current best files for use

- Reading/corpus: `hartman-2023-third-pass.md`
- Appendix data: `appendix-innovation-dataset-third-pass.tsv` and `appendix-feature-occurrence-times-third-pass.tsv`
- Figure search/accessibility: `figures-visual-descriptions.md`
- Citation work: `references-third-pass.md` first, then verify `references-third-pass.bib` or `references-third-pass.csl.json`
