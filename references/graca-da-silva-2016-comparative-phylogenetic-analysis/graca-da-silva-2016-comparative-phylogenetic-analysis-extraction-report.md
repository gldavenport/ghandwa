---
title: "Comparative phylogenetic analyses uncover the ancient roots of Indo-European folktales"
author: "Sara Graça da Silva and Jamshid J. Tehrani"
date: 2016
source_type: born-digital
extraction_date: 2026-05-08
source_file: "graça-da-silva-2016-comparative-phylogenetic-analysis.pdf"
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The raw text layer was used as the primary input. Visual rendering was used to verify figure content and to check text-layer anomalies in the bibliography and the PIE vocabulary form _ai⌢os_.

## Corrections applied

- Removed running headers, page numbers, dotted rule artifacts, side masthead text, and decorative layout text.
- Rejoined line-broken paragraphs and repaired page-boundary continuations, including the interrupted sentence across pages 4–5.
- Repaired common ligature artifacts from the text layer: `ﬁ` → `fi`, `ﬂ` → `fl`.
- Repaired hyphenation across line breaks where the text layer split compounds or proper terms, e.g. Indo-European, Proto-Indo-European, sub-families, majority-rules, maximum-likelihood.
- Reconstructed Table 1 and Table 2 as Markdown tables.
- Separated the references into `graca-da-silva-2016-comparative-phylogenetic-analysis-bibliography.md`.
- Restored bibliography spacing where the PDF text layer collapsed spaces in titles and journal abbreviations.
- Visual check correction: reference 3 reads “Cathcart”, not the text-layer artifact “Cahtcart”.
- Visual/text-layer check retained the special form `_ai⌢os_` on page 9; PyMuPDF returned the arc character as U+2322 `⌢`, and the rendered page showed the same mark.
- Extracted figures 1–4 as raster crops from rendered PDF pages into `images/`.

## Unresolved issues list

- No `[unclear]` markers were inserted in the corpus Markdown.
- Figure-internal text is preserved in raster image crops rather than fully transcribed as structured text. This affects especially Figure 4, whose internal boxes and legend contain dense tale-type lists and boldface distinctions.
- Figure crops were made from rendered page images rather than discrete embedded vector objects. The resulting PNGs are suitable for corpus reference but should not be treated as source-original image assets.
- Formatting in the bibliography was regularized into readable Markdown; this may not preserve every typographic spacing convention of the journal’s reference layout.

## Confusion-pair report

- `h₁ h₂ h₃`: no instances found in the output.
- `ā ē ī ō ū`: no macron-vowel instances found in the output.
- Macron consistency across body, notes, and index: no index and no macron-vowel inventory in this article output.
- `ʰ ʷ`: no instances found in the output.
- `ə`: no instances found in the output.
- `ṛ ḷ ṃ ṇ`: no instances found in the output.
- `ǵ ḱ`: no instances found in the output.
- `*`: preserved where present in prose/captions, especially references to asterisks in Figure 4 and tale labels in figure material; figure-internal asterisks are preserved in the raster crop.
- `†`: no instances found in the output.
- Source-specific check: Greek parameter letters `λ`, `θ`, `β` were retained in the methods and figure/table captions.
- Source-specific check: the special form `_ai⌢os_` was retained with U+2322 `⌢`.

The list above reflects targeted checks and cannot certify that no consistent extraction error remains.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

| Item | Approximate count |
|---|---:|
| h₁ | 0 |
| h₂ | 0 |
| h₃ | 0 |
| ā | 0 |
| ē | 0 |
| ī | 0 |
| ō | 0 |
| ū | 0 |
| ə | 0 |
| Greek characters | 8 |
| Combining diacritics | 2 |
| † | 0 |
| ⌢ | 1 |

## Structural integrity check

- Article-level structure was preserved as a single main Markdown file, as appropriate for a journal article.
- Bibliography was separated into its own Markdown file.
- No index is present in the source.
- Section headings and subsections are consistent with the source: 1, 2, 2.1–2.5, 3, 4, followed by article-end statements.
- Figures 1–4 are placed near the relevant logical discussion and referenced from `images/`.
- Tables 1–2 are well-formed Markdown tables.
- No obvious continuation text appears lost at page boundaries, but page-boundary reflow cannot be certified as exhaustive.

## Image inventory

| File | Source label | Page | Caption |
|---|---|---:|---|
| images/graca-da-silva-2016-comparative-phylogenetic-analysis-fig1.png | Figure 1 | 4 | Approximate locations of Indo-European-speaking populations in Eurasia. Points are colour-coded by linguistic subfamily: red, Germanic; pink, Balto-Slavic; orange, Romance; green, Celtic; blue, Indo-Iranian; Turquoise, Hellenic; grey, Albanian; brown, Armenian. Numbers correspond to point references for populations listed in the electronic supplementary material, table S2. |
| images/graca-da-silva-2016-comparative-phylogenetic-analysis-fig2.png | Figure 2 | 5 | Reconstructing tale descent histories. Example of an ancestral state reconstruction, showing ATU 330 ‘The Smith and the Devil’ traced on a consensus tree derived from 1000 Bayesian language trees. The proportion of black shading in each internal node represents the average probability of the tale being present in the corresponding hypothetical ancestor across the tree sample. The proportion of red shading in each node represents the number of trees in which the corresponding hypothetical ancestor was absent. Branches are colour-coded by linguistic subfamily. The oldest ancestral node that was reconstructed, Proto-Indo-European, is labelled ‘PIE’. |
| images/graca-da-silva-2016-comparative-phylogenetic-analysis-fig3.png | Figure 3 | 6 | Estimates for phylogenetic and spatial association in the autologistic analyses. Scatter plot of phylogenetic (λ) and spatial (θ) parameters estimated for 100 tales that returned a strong phylogenetic signal in the _D_ analyses when fitted to the autologistic model. |
| images/graca-da-silva-2016-comparative-phylogenetic-analysis-fig4.png | Figure 4 | 7 | Estimated contents of ancestral tale corpora. Reconstruction of ancestral Indo-European tale corpora based on analyses of the 76 most phylogenetically conserved tales. Tales contained in each box were reconstructed with a more than 50% likelihood of being present in the corresponding ancestral tale corpus whereas tales in bold represent cases where tales could be securely reconstructed (greater than or equal to 70%). Full results for the ancestral state reconstructions are provided in the electronic supplementary material, table S5. Asterisks denote reconstructions in Proto-Indo-European are based on the results of Bayesian analyses (table 2). |
