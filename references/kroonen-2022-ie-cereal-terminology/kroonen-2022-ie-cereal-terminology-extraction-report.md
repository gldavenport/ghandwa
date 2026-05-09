---
title: "Indo-European cereal terminology suggests a Northwest Pontic homeland for the core Indo-European languages — Extraction report"
author: "Guus Kroonen; Anthony Jakob; Axel I. Palmér; Paulus van Sluis; Andrew Wigman"
date: "2022-10-12"
source_type: born-digital
extraction_date: "2026-05-07"
source_file: "kroonen-2022-ie-cereal-terminology.pdf"
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The raw extracted text layer was the primary input. Visual rendering was used as a fallback for systemic glyph-mapping failures in the text layer and for figure/table image crops.

## Corrections applied

- Repaired systemic PDF text-layer glyph failures: `0x03` → `*`, `0x13` → `ḱ`, and `0x1c` → `←`.
- Converted raised small `h` and `w` in reconstructed forms to `ʰ` and `ʷ` where the PDF baseline indicated superscript placement.
- Converted lowered laryngeal digits and select lowered letters to Unicode subscripts, including `h₁`, `h₂`, `h₃`, `hₐ`, and `hₓ` where the PDF baseline indicated subscript placement.
- Rejoined broken paragraphs and repaired line-break hyphenation where the line break split ordinary prose words.
- Removed PLOS running headers, footers, page numbers, page DOI footers, duplicate title-page block, and decorative layout text.
- Reconstructed Table 1 and Table 2 as Markdown tables. Table 2 is also preserved as two page-crop images because the source uses color-coding and rotated header layout that Markdown cannot fully represent.
- Extracted/cropped Figures 1–3 into `images/` and inserted Markdown image references at the relevant source locations.
- Moved the reference list to a separate bibliography file.

## Unresolved issues list

- The PDF text layer encodes many reconstructed-form asterisks and some special symbols as control characters. These were mapped systemically after visual and contextual verification, but every occurrence was not individually hand-verified.
- Superscript/subscript conversion was algorithmic, based on font size and baseline position. This likely improves laryngeal and aspirate fidelity substantially, but a later pass could still compare dense etymological paragraphs visually against the PDF.
- Table 2 cell contents were reconstructed into Markdown, but the exact green/yellow/orange cell coloration is not represented cell-by-cell in Markdown. The page-crop images preserve the visual table.
- Figure-internal labels were preserved in image crops rather than separately transcribed as text.
- No `[unclear]` markers were inserted in the main text. The absence of markers should not be treated as a guarantee that all characters are correct.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: laryngeal digits were normalized when detected by baseline position and common laryngeal patterns. Unverified residual ASCII-like cases may remain where the PDF did not clearly encode subscript placement.
- Macron vowels: precomposed macron vowels were preserved when extracted; spacing-accent cases were normalized where detected. Dense references and names may still contain occasional spacing-diacritic artifacts.
- `ʰ ʷ` vs. `h w`: raised `h` and `w` in reconstructed forms were converted algorithmically. Some ordinary small raised letters outside reconstructed forms may have been left unchanged or converted depending on baseline behavior.
- `ə`: preserved from the text layer where present; not independently verified in every occurrence.
- Underdot letters such as `ṛ`, `ḷ`, `ṃ`, `ṇ`: preserved where the text layer exposed them; not independently verified in every occurrence.
- `ǵ` and `ḱ`: `ǵ` was preserved from the text layer. Text-layer control character `0x13` was normalized to `ḱ`; all such occurrences were systemic but not individually hand-verified.
- `*`: text-layer control character `0x03` was normalized to `*`; all such occurrences were systemic but not individually hand-verified.
- `†`: dagger characters were preserved where present; rejected-cognate cells in Table 2 were manually preserved from the visual/parsed table.

## Codepoint inventory

All counts are approximate and intended for cross-pass comparison only.

```json
{
  "laryngeals": {
    "h1": 46,
    "h2": 245,
    "h3": 28
  },
  "macron_a": 186,
  "macron_e": 23,
  "macron_i": 24,
  "macron_o": 43,
  "macron_u": 28,
  "schwa": 19,
  "greek_chars": 383,
  "combining_diacritics": 181,
  "dagger": 17
}
```

## Structural integrity check

- Headings are normalized to Markdown `##`/`###` levels while preserving the source's section numbering.
- Bibliography is separated into `kroonen-2022-ie-cereal-terminology-bibliography.md`.
- No index was present in the source.
- Tables are represented in Markdown; Table 2 additionally has image crops to preserve its visual semantics.
- Figure references and captions are attached near the corresponding discussion points.
- Page anchors are retained as HTML comments for source-location checking.

## Image inventory

| File | Source label | Page | Caption |
|---|---:|---:|---|
| `images/kroonen-2022-ie-cereal-terminology-fig1.png` | Fig. 1 | 10 | Present-day distribution of perennial ryegrass (Lolium perenne). (Data from GBIF.org, https://doi.org/10.15468/dl.4tsemc, visited 7 May 2021). |
| `images/kroonen-2022-ie-cereal-terminology-fig2.png` | Fig. 2 | 33 | The emergence of cereal cultivation and processing terminology between Indo-Anatolian and the fragmenting core Indo-European dialect continuum. The reconstructed protoforms of some agricultural terms are placed in the figure to indicate in which phase of the Indo-European language family they emerged. The accompanying arrows show the evolution of the meanings of these protoforms through time. |
| `images/kroonen-2022-ie-cereal-terminology-fig3.png` | Fig. 3 | 35 | Cereal remains, cutting tools and a plowshare alleged to be found in Yamnaya contexts. The shaded area indicates the extent of the Yamnaya culture at the end of the Copper Age [18:651]. Sites: 1 Kholmske; 2 Gura-Bykuluy; 3 Glubokoe; 4 Tetskany; 5 Alkaliya; 6 Belyaevka; 7 Rysove; 8 Mikhailovka; 9 Skelya-Kamenolomnya. Cutting tool data from Razumov [162] and Ivanova [39], plowshare data from Gimbutas [214:161], and cereal data from Pashkevich [36:15] and Anthony [3:320]. |
| `images/kroonen-2022-ie-cereal-terminology-table2-p29.png` | Table 2, p. 29 | 29 | Overview of cereal cultivation and processing terms that conform to the known sound laws and have cognates in at least two Indo-European branches. |
| `images/kroonen-2022-ie-cereal-terminology-table2-p30.png` | Table 2, p. 30 | 30 | Table 2 continued. |
