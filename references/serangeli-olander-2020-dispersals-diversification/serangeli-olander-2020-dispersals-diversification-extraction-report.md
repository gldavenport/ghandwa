---
title: "Extraction report — Dispersals and Diversification"
author: "Matilde Serangeli and Thomas Olander"
date: "2020"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "serangali-ed-2020-dispersals-diversification.pdf"
chunk: "extraction-report"
---

# Extraction report — *Dispersals and Diversification*

## Source type

Born-digital PDF with a machine-readable text layer. The raw text layer from `pdftotext` was used as the primary input. Visual/page rendering was used only for embedded image extraction and figure inventory.

## Corrections applied

- Removed repeated Brill download/watermark lines and recurring running headers/footers.
- Repaired common ligatures (`ﬁ`, `ﬂ`, `ﬀ`, `ﬃ`, `ﬄ`) if present in the extracted text.
- Applied laryngeal normalization from `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃` where lowercase ASCII forms appeared in the text layer. This was applied globally and should be rechecked against the PDF in any passage where ASCII `h` plus digit may have been intentional.
- Light paragraph rejoining and line-break repair were applied to running prose. Hyphenated line-breaks were repaired conservatively, retaining hyphens before uppercase continuation tokens and dropping them before lowercase continuation tokens.
- Bibliography sections were split out into per-section bibliography files. The index was extracted as a separate file and kept line-oriented.
- Embedded figures were extracted from the PDF and linked at the corresponding caption locations when detected in the text stream.

## Unresolved-issues list

- No `[unclear]` or `[?]` markers were inserted by the automated pass. This does **not** mean the extraction is error-free; it means the text layer was sufficiently machine-readable that the pass did not require page-image inference for running text.
- Dense tables, especially tables 2.1, 2.2, 3, 4, 9.1, and 9.2, were preserved primarily from the text layer. Their logical row/column structure should be manually audited in a later pass if table-level reuse is important.
- Some scholarly forms in the raw text layer contain spacing around combining marks or glide/vowel notation, e.g. sequences such as `u̯ e` or `n̥ t`; a later character-fidelity pass should compare representative forms against rendered pages.
- Figure captions were matched to five embedded images. The figure images themselves were extracted, but the surrounding flow of captions and images should be manually checked on pages 28, 35, 37, 189, and 190.
- The table-column header `References` inside chapter 11 was not treated as a bibliography boundary; the last `References` heading in each chunk was used for bibliography splitting. This should still be manually checked in chapter 11 because it contains multiple table headers labelled `References`.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: ASCII lowercase h+digit was normalized to subscript digits. Residual ASCII candidates after normalization: [].
- Macron vowels: precomposed macron vowels were preserved where present in the text layer. No full manual verification of macrons across dense tables, references, and index was performed.
- Superscript modifier letters `ʰ`, `ʷ`: preserved where present in the text layer. No full manual verification was performed.
- `ə`: preserved where present. No full manual verification was performed.
- Underdot letters (`ṛ`, `ḷ`, `ṃ`, `ṇ`): preserved where present. No full manual verification was performed.
- Acute consonants (`ǵ`, `ḱ`): preserved where present. No full manual verification was performed.
- Asterisk `*`: preserved where present. No full manual verification was performed.
- Dagger `†`: preserved where present. No full manual verification was performed.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 112,
    "h2": 186,
    "h3": 21
  },
  "macron_a": 487,
  "macron_e": 137,
  "macron_i": 187,
  "macron_o": 86,
  "macron_u": 54,
  "schwa": 79,
  "greek_chars": 6893,
  "combining_diacritics": 716,
  "dagger": 7
}
```

## Structural integrity check

- Headings: basic chapter/file-level headings were added. Internal source section headings were lightly normalized where the text layer placed the number and title on separate lines.
- Footnotes: footnote text remains inline in the source flow, usually near the page where it appears. Footnote placement was not manually audited.
- Tables: table content was retained from the text layer, but complex tables are not guaranteed to be valid Markdown tables.
- Bibliographies: per-chapter `References` sections were split into separate files using the last `References` heading in each content chunk.
- Page boundaries: source page anchors were inserted as HTML comments. No known continuation text was intentionally removed.
- Residual watermark scan: no repeated Brill download/Googlebot watermark strings found. ISBN/e-book identifiers remain where they are part of the source front matter or metadata.

## Image inventory

- `images/serangeli-olander-2020-dispersals-diversification-fig1-1.jpeg` — Figure 1.1; PDF page 40; printed page 28; caption: Sites in the Pontic–Caspian steppes and adjacent areas
- `images/serangeli-olander-2020-dispersals-diversification-fig1-2.jpeg` — Figure 1.2; PDF page 47; printed page 35; caption: Mating networks in and near the Pontic–Caspian steppes dated 4500–4000BC
- `images/serangeli-olander-2020-dispersals-diversification-fig1-3.jpeg` — Figure 1.3; PDF page 49; printed page 37; caption: Khvalynsk II, female (sister) and male (brother) skeletons 24 & 25 decorated with hundreds of shell beads, 13 copper rings, 3 copper tubes, a copper spiral ornament, beaver incisor belts, and a boar’s tusk pendant, with a polished stone mace-head at center right and bones of sheep and goat offerings at lower right.
- `images/serangeli-olander-2020-dispersals-diversification-fig9-1.jpeg` — Figure 9.1; PDF page 201; printed page 189; caption: The IE-CoR proposed cognacy system in the data-entry website
- `images/serangeli-olander-2020-dispersals-diversification-fig9-2.jpeg` — Figure 9.2; PDF page 202; printed page 190; caption: Systemised Guidelines for Cognate Judgements in the IE-CoR Database

## Suggested future passes

- Table-structure pass for tables 2.1, 2.2, 3, 4, 9.1, and 9.2.
- Character-fidelity pass focused on laryngeals, combining diacritics, Greek, Sanskrit/Indic diacritics, and reconstructed forms in chapters 2, 3, 8, 10, 11, 12, and 13.
- Bibliography/index pass focused on author names, diacritics, title punctuation, and page-number ranges.
