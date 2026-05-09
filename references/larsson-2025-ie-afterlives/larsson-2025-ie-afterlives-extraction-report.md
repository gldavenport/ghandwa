---
title: "Indo-European Afterlives: Interdisciplinary Perspectives on Life beyond Death — Extraction Report"
author: "Jenny H. Larsson, Thomas Olander & Anders Richardt Jørgensen (eds.)"
date: "2025"
source_type: "epub"
extraction_date: "2026-05-07"
source_file: "larsson-2025-ie-afterlives.epub"
chunk: "extraction report"
---

# Extraction Report

## Source identification

- Source type: EPUB with embedded XHTML text layer.
- Primary input used: EPUB XHTML text layer.
- Visual/OCR inference: not used for running text.
- Source title used for output metadata: *Indo-European Afterlives: Interdisciplinary Perspectives on Life beyond Death*.
- Source note: the OPF `dc:title` field reads *Indo-European Ecologies*, but the EPUB visible title pages, navigation title, and chapter headers identify the book as *Indo-European Afterlives*. The visible title was used.

## Corrections applied

- EPUB span-boundary whitespace was normalized where publisher markup split single words or separated punctuation from preceding text. Fragmented publisher inline CSS styling was flattened to avoid corrupting technical forms; characters and logical structure were prioritized.
- HTML subscript digits in laryngeal contexts were converted to Unicode subscript digits where the source encoded them with subscript styling, e.g. `h` + styled `2` → `h₂`.
- HTML superscript/subscript modifier letters were converted to Unicode modifier/subscript characters where a direct simple-codepoint equivalent exists, e.g. styled `ʰ`, `ʷ`, or numeric note markers.
- EPUB figures were copied directly from `OEBPS/images/` and renamed; image bytes were not re-encoded.
- Per-chapter reference sections were separated into chapter-specific bibliography files.
- Paragraphs broken by pagebreak spans were rejoined; source page anchors were retained as Markdown HTML comments.

## Unresolved issues list

- No `[unclear]` markers were inserted during this pass.
- No scanned-source `[?]` inferred-character markers were inserted because the EPUB text layer was used directly.
- No inline image glyphs requiring substitution or unresolved annotation were detected.
- This pass does not certify that every publisher span-derived subscript/superscript was semantically correct; it reports the transformations applied and leaves the output suitable for later targeted character audit.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: styled subscript digits were converted during extraction. Potential remaining ASCII laryngeal-like strings found: none detected by regex scan.
- Macron vowels: precomposed macron vowels were preserved where present in the XHTML. Decomposed combinations such as `ə̄`, `k̑`, `ṣ̌`, and `R̥` were preserved where the source used combining marks.
- `ʰ ʷ` vs. plain `h w`: superscript modifier letters were preserved/converted where encoded as styled superscripts. Some original source forms use ordinary `h` and `w`; these were not normalized.
- `ə` vs. `e` or `9`: schwa was preserved where present.
- Underdot letters: `ṛ ḷ ṃ ṇ` and decomposed equivalents were preserved where present.
- `ǵ ḱ` vs. ASCII approximations: acute consonants were preserved where present. Some source text uses `k̑`, `g̑` notation; that notation was preserved.
- Asterisk before reconstructed forms: asterisks were preserved; no global normalization was applied.
- Dagger `†`: preserved where present; approximate dagger count below.
- Leftover publisher class spans in Markdown: 0. Publisher inline `class` spans should not remain; inline CSS styling was flattened intentionally in this character-first pass.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 53,
    "h2": 135,
    "h3": 9
  },
  "macron_a": 763,
  "macron_e": 67,
  "macron_i": 176,
  "macron_o": 133,
  "macron_u": 90,
  "schwa": 123,
  "greek_chars": 5683,
  "combining_diacritics": 1054,
  "dagger": 0
}
```

## Structural integrity check

- Headings: chapter and section headings were converted to Markdown headings following the source hierarchy.
- Footnotes/endnotes: note references and note paragraphs were converted to Markdown-style footnote references/definitions where the EPUB used backlink-number paragraphs.
- Tables: HTML tables were converted to Markdown tables.
- Bibliographies: chapter reference sections were extracted into per-chapter bibliography files and removed from chapter-body files.
- Images: image files were copied to `images/`; Markdown image references were inserted at source figure locations.
- Page anchors: EPUB pagebreak labels were retained as `<!-- page: N -->` comments.
- Index: no standalone index section was found in the EPUB navigation or XHTML spine.

## Image-glyph inventory

- Inline image glyph substitutions: none detected.
- Inline image glyphs unresolved: none detected.

## Image inventory

All image entries are also listed in `manifest.json`.

- `images/larsson-2025-ie-afterlives-cover.jpg` — Cover; page: i; caption: Cover
- `images/larsson-2025-ie-afterlives-image1.jpg` — Unnumbered image; page: ; caption: img1.jpg
- `images/larsson-2025-ie-afterlives-ch8-fig4.jpg` — Chapter 8, Figure 4; page: 133; caption: Figure 4. Varu ṇ a with noose and da ṇ ḍ a. Rajarani temple, 11th c. Photo: Benjamín Preciado Solis, Centro de Estudios de Asia y Africa, El Colegio de Mexico. Wikimedia Commons © License: CC BY-SA 3.0.
- `images/larsson-2025-ie-afterlives-ch8-fig5.jpg` — Chapter 8, Figure 5; page: 133; caption: Figure 5. Yama, painting, ca. 1820–25. Victoria and Albert Museum, London © License: CC BY-NC.
- `images/larsson-2025-ie-afterlives-ch8-fig6.jpg` — Chapter 8, Figure 6; page: 143; caption: Figure 6. Burials with reconstructions of the clothing from the Mariupol cemetary. From Kotova 2010 © License: CC BY-SA 4.0.
- `images/larsson-2025-ie-afterlives-ch9-fig1.jpg` — Chapter 9, Figure 1; page: 152; caption: Figure 1. The Håga mound, Uppsala, Sweden. Photo: Terje Oestigaard © License: CC BY-NC.
- `images/larsson-2025-ie-afterlives-ch9-fig2.jpg` — Chapter 9, Figure 2; page: 152; caption: Figure 2. Documentation of the excavation and the complete mound. From Almgren 1905, plate III. License: CC-PD.
- `images/larsson-2025-ie-afterlives-ch9-fig3.jpg` — Chapter 9, Figure 3; page: 153; caption: Figure 3. Finds from the Håga mound. Photo: Ola Myrin, Statens Historiska museer, Stockholm © License: CC BY.
- `images/larsson-2025-ie-afterlives-ch9-fig4.jpg` — Chapter 9, Figure 4; page: 155; caption: Figure 4. The cult house known as the “Håga Church”. Photo: Terje Oestigaard © License: CC BY-NC.
- `images/larsson-2025-ie-afterlives-ch9-fig5.jpg` — Chapter 9, Figure 5; page: 156; caption: Figure 5. The cleaved femur found in the Håga mound during excavation. From Almgren 1905: 26, fig. 28. License: CC-PD.
- `images/larsson-2025-ie-afterlives-ch9-fig6.jpg` — Chapter 9, Figure 6; page: 159; caption: Figure 6. Original documentation of the excavation, 1903. The bold dark line indicates the extent of the charcoal layer at the bottom of the mound. Source: Antikvarisk-topografiska arkivet, Stockholm. License: CC-PD.
- `images/larsson-2025-ie-afterlives-ch9-fig7.jpg` — Chapter 9, Figure 7; page: 159; caption: Figure 7. Hindu cremation along Bagmati River, Pashupatinath temple, Kathmandu, Nepal, 2022. Photo: Terje Oestigaard © License: CC BY-NC.
- `images/larsson-2025-ie-afterlives-image2.jpg` — Unnumbered image; page: ; caption: img2.jpg
- `images/larsson-2025-ie-afterlives-ch9-fig8.jpg` — Chapter 9, Figure 8; page: 165; caption: Figure 8. Illustration of making a need-fire or making fire by drilling. From Kaliff 2007: 188, fig. 14. Drawing: Richard Holmgren, ARCDOC © License: CC BY-NC.
- `images/larsson-2025-ie-afterlives-ch9-fig9.jpg` — Chapter 9, Figure 9; page: 167; caption: Figure 9. Eldbjørg – the fire in the hearth. The Viking Hall ‘Gildehallen’, Midgard Viking Centre, Borre, Norway. Photo: Terje Oestigaard © License: CC BY-NC.
- `images/larsson-2025-ie-afterlives-ch9-fig10.jpg` — Chapter 9, Figure 10; page: 170; caption: Figure 10. Fire altar. The Shivaratri festival at Pashupatinath, 2022. Photo: Terje Oestigaard © License: CC BY-NC.
- `images/larsson-2025-ie-afterlives-image3.jpg` — Unnumbered image; page: ; caption: img3.jpg
- `images/larsson-2025-ie-afterlives-ch2-fig1.jpg` — Chapter 2, Figure 1; page: 10; caption: Figure 1. Conceptual model. Graphics: Peter Jackson Rova © License: CC BY-NC.
- `images/larsson-2025-ie-afterlives-ch2-fig2.jpg` — Chapter 2, Figure 2; page: 16; caption: Figure 2. Welcome to Valhall! Picture stone from Broa in Halla, Gotland ( c. 8th to 9th century), found in conjunction with a burial site.
- `images/larsson-2025-ie-afterlives-ch6-fig1.jpg` — Chapter 6, Figure 1; page: 84; caption: Figure 1. From left to right: Orion (with belt and right foot Rigel), Alpha Tauri/Aldebaran (in the head of the “bull” Taurus) and the cluster of the Pleiades. Photo: Panda~thwiki, Wikimedia Commons © License: CC BY 4.0.
- `images/larsson-2025-ie-afterlives-ch8-fig1.jpg` — Chapter 8, Figure 1; page: 126; caption: Figure 1. A wasp’s nest. Photo: Russel Wills, Wikimedia Commons © License: CC BY-SA 2.0.
- `images/larsson-2025-ie-afterlives-ch8-fig2.jpg` — Chapter 8, Figure 2; page: 129; caption: Figure 2. The staff of the völva. Photo: Arnold Mikkelsen, Nationalmuseet Danmark © License: CC BY-SA.
- `images/larsson-2025-ie-afterlives-ch8-fig3.jpg` — Chapter 8, Figure 3; page: 133; caption: Figure 3. Varuṇa with noose. Rajarani temple, 11th c. Photo: Bernard Gagnon. Wikimedia Commons © License: CC BY-SA 3.0.