---
title: "Extraction Report — Word Mining: Metal Names and the Indo-European Dispersal"
author: "Rasmus Thorsø; Andrew Wigman; Anthony Jakob; Axel I. Palmér; Paulus van Sluis; Guus Kroonen"
date: 2023
source_type: born-digital
extraction_date: 2026-05-07
source_file: "thorsø-2023-word-mining.pdf"
chunk: extraction-report
---

# Extraction Report

## Source type

Born-digital PDF with a machine-readable text layer. The raw extracted text layer was used as the primary input; rendered page images were used to confirm Figures 8.1 and 8.2.

## Output files

- `thorso-2023-word-mining.md` — main text, figures, abbreviations, notes
- `thorso-2023-word-mining-bibliography.md` — references
- `thorso-2023-word-mining-extraction-report.md` — this QC record
- `manifest.json` — machine-readable extraction metrics
- `images/thorso-2023-word-mining-fig8-1.png`
- `images/thorso-2023-word-mining-fig8-2.png`

## Corrections applied

- Repaired common PDF text-layer ligatures: `ﬁ`→`fi`, `ﬂ`→`fl`, `ﬀ`→`ff`, `ﬃ`→`ffi`, `ﬄ`→`ffl`.
- Removed running headers, DOI footers, source page numbers, and the repository metadata page from the corpus body.
- Rejoined paragraphs and repaired obvious line-break hyphenation where the break appeared to split a word.
- Normalized laryngeal ASCII sequences `h1`, `h2`, and `h3` to `h₁`, `h₂`, and `h₃` throughout the output.
- Extracted embedded figure images and inserted Markdown image references at the figure locations.
- Separated the References section into its own bibliography file.

## Unresolved issues

- Footnote anchors were converted conservatively; anchors adjacent to dense linguistic notation may require spot-checking against the PDF.
- Formatting such as italics/small caps from the PDF font layer was not exhaustively reconstructed; the extraction prioritizes characters and logical structure.
- Line-break hyphenation was repaired heuristically. Several scholarly compounds and segmented forms may require manual review.
- Bibliography paragraph grouping was reconstructed from text-layer order and should be spot-checked for entries with same-author year continuations.

- No `[unclear]` or `[?]` markers were inserted by this pass.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: ASCII forms were normalized globally; this cannot certify every intended laryngeal in the source.
- Macron vowels: macrons were preserved from the text layer where extractable; dense notes and bibliography entries should be spot-checked if used as lexical data.
- Superscript modifier letters `ʰ` and `ʷ`: preserved where present in the text layer; not independently verified in every form.
- Schwa `ə`: preserved where present in the text layer; not independently verified in every form.
- Underdot characters such as `ṛ`, `ḷ`, `ṃ`, `ṇ`: preserved where present in the text layer; not independently verified in every form.
- Acute consonants such as `ǵ` and `ḱ`: preserved where present in the text layer; not independently verified in every form.
- Asterisk `*`: preserved from the text layer for reconstructed forms; no full certification of every reconstructed form was attempted.
- Dagger `†`: approximate count is zero; no dagger-bearing passage was identified in this pass.

## Codepoint inventory

Approximate counts for cross-pass comparison:
- note: All counts are approximate and for cross-pass comparison only.
- laryngeals: h1=18, h2=60, h3=9
- macron_a: 66
- macron_e: 19
- macron_i: 41
- macron_o: 10
- macron_u: 20
- schwa: 28
- greek_chars: 803
- combining_diacritics: 111
- dagger: 0

## Structural integrity check

- Headings were reconstructed for sections 8.1–8.8.2.
- The article was treated as a journal-article/book-chapter extraction and kept as a single main Markdown file, with bibliography separated.
- Figures 8.1 and 8.2 were extracted as PNG files and referenced from the main Markdown file.
- No source index was present.
- Footnotes were preserved as Markdown footnotes in a Notes section.

## Image inventory

- `thorso-2023-word-mining-fig8-1.png` — Figure 8.1, source page 119: The spread of iron metallurgy in Europe.
- `thorso-2023-word-mining-fig8-2.png` — Figure 8.2, source page 121: Schematic overview of the occurrence of the most important shared metal names in the Indo-European language family.
