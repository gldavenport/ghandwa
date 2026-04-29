# Graça da Silva & Tehrani 2016 Markdown extraction

This ZIP contains a clean, corpus-ready Markdown extraction of:

Sara Graça da Silva and Jamshid J. Tehrani. 2016. "Comparative phylogenetic analyses uncover the ancient roots of Indo-European folktales." *Royal Society Open Science* 3: 150645. doi:10.1098/rsos.150645.

## Files

- `graca-da-silva-tehrani-2016-comparative-phylogenetic-analyses.md` — main clean Markdown extraction.
- `figure-4-ancestral-tale-corpora.csv` — companion CSV extraction of Figure 4 ancestral tale-corpus membership, now including `secure_ge_70`.
- `figure-4-confidence-audit.md` — notes from the additional Figure 4 bold/confidence pass.
- `character-audit.md` — notes from the special-character and high-risk notation pass.
- `bibliography-audit.md` — notes from the bibliography/source-critical review pass.
- `extraction-notes.md` — pass status, remaining limits, and further-pass recommendation.

## Extraction approach

The main extraction prioritizes readable Markdown and corpus usefulness over physical layout. Running headers, footers, page geometry, decorative rules, and ordinary page numbers were removed. Page boundary comments are retained as silent Markdown/HTML comments for later checking.

Figures are represented by captions and accessible descriptions. Tables are converted to Markdown tables. Figure 4 is also normalized into a companion CSV because its dense visual layout is more useful as structured data than as physical layout.

## Current status

This version includes the additional passes that were previously recommended: Figure 4 confidence audit, targeted character audit, and bibliography/source-critical review. No further pass is needed for ordinary corpus research use.
