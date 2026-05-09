---
title: "Indo-European Interfaces — extraction report"
author: "Jenny Larsson, Thomas Olander & Anders Richardt Jørgensen (eds.)"
date: "2024"
source_type: "epub"
extraction_date: "2026-05-07"
source_file: "larsson-ed-2024-ie-interfaces.epub"
chunk: "extraction-report"
---

# Indo-European Interfaces — extraction report

## Source type
EPUB. The embedded XHTML text layer was used directly. Discrete EPUB image files were copied into `images/` without re-encoding or recompression.

## Corrections applied
- Removed soft hyphen characters: approximately 19.
- Converted subscript digit spans to Unicode subscript digits where detected: approximately 827.
- Converted superscript digit/modifier spans to Unicode superscript/modifier characters where detected: approximately 1866.
- Applied conservative ASCII laryngeal normalization for likely h1/h2/h3 sequences: approximately 0.
- Copied EPUB image files used in the text into `images/` and renamed them with chapter/figure/table-aware filenames.
- Separated per-chapter `References` sections into dedicated bibliography files; chapter footnotes were retained in the corresponding chapter files under `## Footnotes`.

### Private-use font glyph substitutions
The EPUB text layer used private-use codepoints for several scholarly glyphs. These were mapped using the embedded EOSabon font glyph names. These mappings should be treated as high-confidence but still reviewable because they are inferred from font metadata rather than ordinary Unicode text.
- U+E002 ibreveinvsub → i̯: 95
- U+E005 edottilde → ė̃: 2
- U+E008 imacronacute → ī́: 26
- U+E009 umacronacute → ū́: 27
- U+E00C mringsub → m̥: 20
- U+E00F Rringsub → R̥: 9
- U+E015 lringsub → l̥: 43
- U+E017 amacronbreve → ā̆: 1
- U+E01E upsilonmacronacute → ῡ́: 8
- U+E03B mringsubacute → ḿ̥: 2
- U+E045 lringsubacute → ĺ̥: 56
- U+E048 mbrevedotaccent → m̐: 6
- No unmapped private-use glyphs were found in the final Markdown corpus.

## Image-glyph inventory
No inline PNG character glyphs were detected. Font-encoded private-use glyphs were handled separately above.

## Unresolved-issues list
- No explicit `[unclear]` or unresolved image-glyph markers were inserted. This does not certify full correctness; it only means the automated pass did not identify unreadable text-layer content.
- Page ranges are not encoded in the EPUB; YAML `pages:` fields therefore use `not encoded in EPUB`.
- The EPUB contains dense scholarly notation, Vedic/Sanskrit accents, Greek, phonological notation, and private-use font glyphs. Consistent errors may remain undetected by automated passes.

## Confusion-pair report
Automated checks were run for the known high-risk confusion categories. This is a regression aid, not a certification of correctness.
- h1 subscript form count: approximately 246. Remaining ASCII `h1` instances, if any, may include non-laryngeal text and were not blindly converted.
- h2 subscript form count: approximately 169. Remaining ASCII `h2` instances, if any, may include non-laryngeal text and were not blindly converted.
- h3 subscript form count: approximately 30. Remaining ASCII `h3` instances, if any, may include non-laryngeal text and were not blindly converted.
- Macron counts: ā 662, ē 38, ī 106, ō 93, ū 137.
- Schwa `ə`: approximately 31.
- Greek characters: approximately 4633.
- Combining diacritics: approximately 1253.
- Dagger `†`: approximately 0.
- Known source-specific confusions added: private-use EOSabon glyphs; these were mapped above and should be stress-tested if this extraction is used for lexical data work.

## Codepoint inventory
Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 246,
    "h2": 169,
    "h3": 30
  },
  "macron_a": 662,
  "macron_e": 38,
  "macron_i": 106,
  "macron_o": 93,
  "macron_u": 137,
  "schwa": 31,
  "greek_chars": 4633,
  "combining_diacritics": 1253,
  "dagger": 0
}
```

## Structural integrity check
- Headings were converted from the EPUB XHTML heading hierarchy.
- Twelve chapter files were produced, matching the EPUB table of contents.
- Per-chapter bibliographies were produced for chapters 2–12; chapter 1 has no separate `References` heading in the EPUB.
- EPUB tables encoded as XHTML were converted to Markdown tables; tables rendered as images were preserved as image references with captions.
- Figure/table captions adjacent to images were attached to the image Markdown rather than duplicated as prose captions.
- Footnote paragraphs were collected and moved to `## Footnotes` in the relevant chapter files.
- No index section was found in the EPUB table of contents.

## Image inventory
- `larsson-ed-2024-ie-interfaces-cover.jpg` — cover; page: not encoded; caption: Cover image
- `larsson-ed-2024-ie-interfaces-frontmatter-image1.jpg` — img1.jpg; page: not encoded; caption: img1.jpg
- `larsson-ed-2024-ie-interfaces-frontmatter-image1-2.jpg` — img2.jpg; page: not encoded; caption: img2.jpg
- `larsson-ed-2024-ie-interfaces-ch2-image1.jpg` — img4.jpg; page: not encoded; caption: img4.jpg
- `larsson-ed-2024-ie-interfaces-ch3-table1.jpg` — Table 1; page: not encoded; caption: Table 1. Relevant elements of the myth of Hermes and Apollo.
- `larsson-ed-2024-ie-interfaces-ch3-table2.jpg` — Table 2; page: not encoded; caption: Table 2. Relevant elements of the myth of Prometheus and Zeus.
- `larsson-ed-2024-ie-interfaces-ch3-table3.jpg` — Table 3; page: not encoded; caption: Table 3. Relevant elements of the myth of Thjalfi and Thor.
- `larsson-ed-2024-ie-interfaces-ch3-table4.jpg` — Table 4; page: not encoded; caption: Table 4. Correspondences between the narratives.
- `larsson-ed-2024-ie-interfaces-ch3-table5.jpg` — Table 5; page: not encoded; caption: Table 5. Hermes’s preparation of a meal.
- `larsson-ed-2024-ie-interfaces-ch3-table6.jpg` — Table 6; page: not encoded; caption: Table 6. Prometheus’s preparation of a meal.
- `larsson-ed-2024-ie-interfaces-ch3-table7.jpg` — Table 7; page: not encoded; caption: Table 7. Thor’s preparation of a meal.
- `larsson-ed-2024-ie-interfaces-ch3-table8.jpg` — Table 8; page: not encoded; caption: Table 8. Shared elements in Hermes’s, Prometheus’s and Thjalfi’s meals.
- `larsson-ed-2024-ie-interfaces-ch3-fig1.jpg` — Figure 1; page: not encoded; caption: Figure 1. Examples of “head-and-hoof deposits”. From: Piggott 1962: 113 © Antiquity Publications Ltd 1962. License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-ch5-fig1.jpg` — Figure 1; page: not encoded; caption: Figure 1. The Kragehul spear shaft. From: Wimmer 1887: 124. License: CC-PD.
- `larsson-ed-2024-ie-interfaces-ch6-fig1.jpg` — Figure 1; page: not encoded; caption: Figure 1. Face pot from a passage grave at Svinø, southern Zealand, Denmark. From: Sophus Müller 1918, no. 164. License: CC-PD.
- `larsson-ed-2024-ie-interfaces-ch6-fig2.jpg` — Figure 2; page: not encoded; caption: Figure 2. Distribution of anthropomorphic stelae/statue menhirs across Eurasia. From: Sabine Reinhold, 2018, fig. 2 © License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-ch6-fig3.jpg` — Figure 3; page: not encoded; caption: Figure 3. The bronze figurines from Grevensvænge, Southern Zealand, Denmark. Drawn by Christian Brandt c. 1779/80. From: Djupedal and Broholm 1953. License: CC-PD.
- `larsson-ed-2024-ie-interfaces-ch6-fig4.jpg` — Figure 4; page: not encoded; caption: Figure 4. The two-faced figure from Kallerup, Thy, Denmark. Photo: Søren Greve, The National Museum of Denmark © License: CC BY-SA 4.0.
- `larsson-ed-2024-ie-interfaces-ch7-fig1.jpg` — Figure 1; page: not encoded; caption: Figure 1. Principles of variation in a set of dithematic names. Graphics: Peter Jackson Rova © License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-ch7-fig2.jpg` — Figure 2; page: not encoded; caption: Figure 2. Chiastic structure of the climactic segment in the Björketorp curse. Graphics: Peter Jackson Rova © License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-ch9-fig1.jpg` — Figure 1; page: not encoded; caption: Figure 1. The Bronze Age (c. 1000 BC) Håga mound in Uppsala, Sweden, 6 February 2021. Photo: Terje Oestigaard © License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-ch9-fig2.jpg` — Figure 2; page: not encoded; caption: Figure 2. Water from the underground overflowing rock-art. Tanum, Aspeberget. Photo: Bertil Almgren © [shfa.dh.gu.se](http://shfa.dh.gu.se) (SHFA). License: CC BY 4.0.
- `larsson-ed-2024-ie-interfaces-ch9-fig3.jpg` — Figure 3; page: not encoded; caption: Figure 3. Celestial and terrestrial powers in practice and working together. The sun shines from above and underground forces keep the water alive during cold winters. Historic source at Håga, Uppsala, Sweden, 6 February 2021. Photo: Terje Oestigaard © License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-ch9-fig4.jpg` — Figure 4; page: not encoded; caption: Figure 4. Sagaholm. Slab 30 in situ with depiction of an Indo-European horse ritual. Photo: Bertil Almgren © [shfa.dh.gu.se](http://shfa.dh.gu.se) (SHFA). License: CC BY 4.0.
- `larsson-ed-2024-ie-interfaces-ch9-fig5.jpg` — Figure 5; page: not encoded; caption: Figure 5. Skeid depicted on rock art. Litsleby 2 Tanum, Bohuslän, Sweden. Date: Younger Bronze Age. Photo: Gerhard Milstreu © [shfa.dh.gu.se](http://shfa.dh.gu.se) (SHFA). License: CC BY 4.0.
- `larsson-ed-2024-ie-interfaces-ch9-fig6.jpg` — Figure 6; page: not encoded; caption: Figure 6. Symbolic horse-fight between the Winter and the Summer. From Olaus Magnus 1555 [2001]. License: CC-PD.
- `larsson-ed-2024-ie-interfaces-ch9-fig7.jpg` — Figure 7; page: not encoded; caption: Figure 7. Boat fight or water-tournament. From Olaus Magnus 1555 [2001]. License: CC-PD.
- `larsson-ed-2024-ie-interfaces-ch9-fig8.jpg` — Figure 8; page: not encoded; caption: Figure 8. Symbolic water-tournament with naked fighters (note the skee-name): Massleberg Skee, Bohuslän. Date: Younger Bronze Age. Photo: Torsten Högberg © [shfa.dh.gu.se](http://shfa.dh.gu.se) (SHFA). License: CC BY 4.0.
- `larsson-ed-2024-ie-interfaces-ch9-fig9.jpg` — Figure 9; page: not encoded; caption: Figure 9. Fields and fertility during ploughing ritual. Litsleby 6 Tanum, Bohuslän, Sweden. Photo: Gerhard Milstreu © [shfa.dh.gu.se](http://shfa.dh.gu.se) (SHFA). License: CC BY 4.0.
- `larsson-ed-2024-ie-interfaces-ch9-fig10.jpg` — Figure 10; page: not encoded; caption: Figure 10. Late Bronze Age (c. 700 BC) razor with horses and ship found in 1958, Rinkeby, Sweden. Photo: Jan Eve Olsson, RAÄ © License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-ch10-fig1.jpg` — Figure 1; page: not encoded; caption: Figure 1. Map showing Iberian Late Bronze Age warrior stelae, rivers navigable in later prehistory, copper and tin deposits. From: M. Díaz-Guardamino 2017 © License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-ch10-fig2.jpg` — Figure 2; page: not encoded; caption: Figure 2. Rubbing of rock art image of a chariot and two-horse team from Frännarp, Skåne, Sweden, showing recurrent conventional representation of the horse, chariot frame, wheels, axles, spokes, yoke, and yoke pole. Photo: Dietrich Evers © [shfa.dh.gu.se](http://shfa.dh.gu.se) (SHFA). License: CC BY 4.0.
- `larsson-ed-2024-ie-interfaces-ch10-fig3.jpg` — Figure 3; page: not encoded; caption: Figure 3. Fragmentary Late Bronze Age stela depicting chariot with two-horse team: El Tejadillo, Capilla, Badajoz, Spain; Museo Arqueológico Provincial de Badajoz. Photo: J. Koch © License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-ch10-fig4.jpg` — Figure 4; page: not encoded; caption: Figure 4. Rock carving depicting a sea-going vessel with a mast, rigging, and crew: Auga dos Cebros, Galicia, Spain. Drawing: J. Koch © License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-ch10-fig5.jpg` — Figure 5; page: not encoded; caption: Figure 5. Bronze Age rock carving depicting a sea-going vessel with a mast, rigging, and crew: Järrested, Skåne, Sweden. Photo: Catarina Bertilsson © [shfa.dh.gu.se](http://shfa.dh.gu.se) (SHFA). License: CC BY 4.0.
- `larsson-ed-2024-ie-interfaces-ch10-fig6.jpg` — Figure 6; page: not encoded; caption: Figure 6. Bronze Age rock carving of a sea-going boat with a crew of paddlers and large bihorned figure, from Tanum, Bohuslän, Sweden. Photo: Gerhard Milstreu, Tanums Hällristningsmuseum © [shfa.dh.gu.se](http://shfa.dh.gu.se) (SHFA). License: CC BY 4.0.
- `larsson-ed-2024-ie-interfaces-ch10-fig7.jpg` — Figure 7; page: not encoded; caption: Figure 7. Rock carving, in which a large bihorned figure standing on a chariot pulled by a small horned quadruped to the apparent wonder of man standing aboard a vessel below (Vitlycke panel, Tanum, Bohuslän, Sweden) is reminiscent of the associations of Thor in Norse mythological literature, riding through the sky in a chariot pulled by goats. The zigzag in front of him might represent the namesake thunder bolt. Photo: J. Koch © License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-ch12-fig1.jpg` — Figure 1; page: not encoded; caption: Figure 1. Doubling of the ‘men and cattle’ merism. Graphics: Nicholas Zair © License: CC BY-NC.
- `larsson-ed-2024-ie-interfaces-unreferenced-image1.png` — unreferenced-image; page: not encoded; caption: Unreferenced EPUB image file: img3.png
