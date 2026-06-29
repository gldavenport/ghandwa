---
title: "Targeted character-authority pass report: Clayton 2022"
source_file: "clayton-2022-labiovelar loss.pdf"
extraction_date: "2026-05-26"
---

# Targeted character-authority pass report

## Pass scope

This pass targeted the five requested areas:

1. reconstructed forms and rule notation,
2. Vedic/Sanskrit and Iranian form fidelity,
3. tables and diagrams,
4. backtick/italic normalization for cited forms and reconstructed forms,
5. footnote cleanup.

It was not a full manual re-extraction of every paragraph. The source is a born-digital PDF with a mostly usable text layer, but the text layer is not character-authoritative for all linguistic notation.

## What changed

- Rebuilt the working Markdown from the PDF text layer and separated footnotes into Markdown footnote definitions instead of leaving many of them interleaved with body prose.
- Normalized laryngeal notation in linguistic contexts from `h1`, `h2`, `h3`, `hx` to `h₁`, `h₂`, `h₃`, `hₓ`.
- Normalized `C0` to `C₀` in rule environments.
- Normalized common labiovelar notation in formula-like contexts, especially `Kw`, `kw`, and `gw`, to `Kʷ`, `kʷ`, and `gʷ`.
- Wrapped many reconstructed forms and root forms in backticks so literal asterisks survive Markdown rendering.
- Reconstructed Tables 1-3 as Markdown tables.
- Preserved the main autosegmental/phonological diagrams as images with source-aware descriptions.
- Retained the source image glyph from the bibliography in `images/` and represented its value textually where needed.

## QC checks performed

- Rendered the PDF pages for visual reference before the pass.
- Checked dense notation zones around the numbered rules, Tables 1-3, and the diagram pages.
- Ran searches for remaining baseline laryngeal forms (`h1`, `h2`, `h3`, `hx`), malformed replacement characters, and control-glyph remnants.
- Checked the generated Markdown for table integrity and image references.

## Remaining risks

- Some italic source formatting is approximated by regex-based backtick protection rather than a full span-by-span manual italic audit.
- Some Vedic accent placement and stacked diacritics should still be verified against the rendered PDF before direct quotation.
- The footnotes are now structurally separated and searchable, but footnote definitions are structurally separated at the end. Body callout markers are mostly preserved as source digits to avoid corrupting citations and verse references; normalize them manually only where needed for publication-grade reuse.
- The diagrams are preserved as images, not fully transcribed into textual autosegmental notation. This is intentional because their geometry carries meaning.

## Completion assessment

This version is a meaningful improvement for corpus use and derivational searching. For quotation-level use of a specific form, verify that form against the PDF rendering.
