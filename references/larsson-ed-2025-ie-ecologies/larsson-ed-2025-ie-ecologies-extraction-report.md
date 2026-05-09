---
title: "Extraction report — Indo-European Ecologies"
author: "Jenny H. Larsson, Thomas Olander & Anders Richardt Jørgensen"
date: "2025-07-26"
source_type: "epub"
extraction_date: "2026-05-07"
source_file: "larssen-ed-2025-ie-ecologies.epub"
chunk: "extraction-report"
---

# Extraction report — Indo-European Ecologies

## Source type

EPUB. The source is a structured archive with embedded XHTML text and discrete image files. The XHTML text layer was used directly. No OCR was performed.

## Output structure

- Chunked extraction by chapter: Chapters 1–9 each have a clean Markdown content file.
- Per-chapter `References` sections were separated into `bibliography-ch*.md` files.
- Front matter and contributor biographies were extracted as standalone Markdown files.
- No index section was present in the EPUB.
- Body figures were copied directly from the EPUB image directory without re-encoding or recompression. Font files were not copied.

## Corrections applied

- Removed soft hyphen/discretionary hyphen characters from the XHTML text layer.
- Replaced non-breaking spaces with ordinary spaces.
- Converted publisher class-based subscript spans to Unicode subscript characters where detected.
- Converted publisher class-based superscript spans to Unicode superscript/modifier characters where detected, including ʰ and ʷ.
- Converted internal footnote links to Markdown footnote references and definitions.
- Split per-chapter reference sections into separate bibliography files.
- Copied and renamed body figures using chapter-local figure numbering.
- Applied private-use glyph substitutions identified from linguistic context:
- U+E008 → ī: 5 instance(s)
- U+E002 → i̯: 45 instance(s)
- U+F737 → 7: 1 instance(s)
- U+E011 → a: 1 instance(s)
- U+E048 → ́: 1 instance(s)
- U+E005 → ė: 1 instance(s)
- U+E01E → ῡ: 9 instance(s)
- U+E017 → ā́: 1 instance(s)
- U+F6D2 → ́: 1 instance(s)

## Unresolved issues list

- U+E009 in OEBPS/xhtml/15_Chapter7.xhtml: 1 instance(s), retained as `[unclear-pua:U+E009]`.

- The private-use substitution `U+E011 → a` in Avestan `aηharǝ̄` and `U+E048 → ◌́` in Vedic `dasyū́r` are contextual inferences and should be checked against the print/PDF if absolute character authority is required.
- The conversion of class-based superscript/subscript markup cannot guarantee that every publisher styling instance represented linguistic notation rather than visual styling.
- The EPUB uses mixed precomposed and combining diacritics. This extraction preserved the source distribution except where private-use substitutions required a combining sequence.
- Some captions and citation boxes contain Creative Commons/license metadata; these were preserved as source text.

## Confusion-pair report

- h₁/h₂/h₃ vs h1/h2/h3: laryngeal subscript counts are approximate: h₁=85, h₂=37, h₃=7. Some forms in the source encode laryngeals as h₁/₂; those were preserved or converted from explicit subscript styling when detected.
- Macron vowels: approximate counts ā=381, ē=30, ī=102, ō=95, ū=64. The pass did not certify every macron in references and notes.
- Superscript ʰ/ʷ: superscript span classes were converted where encountered; complete correctness was not certified.
- ə: approximate count 30; not individually certified.
- ṛ ḷ ṃ ṇ and related underdot forms: preserved from XHTML text layer; combining and precomposed distribution was not normalized globally.
- ǵ/ḱ and acute consonants: preserved from XHTML text layer where present; not exhaustively certified.
- Asterisk before reconstructed forms: preserved from text layer; no global inference was attempted.
- Dagger †: approximate count 1; not individually certified.
- Private-use characters: 66 PUA instance(s) detected in source XHTML; 65 substituted by contextual mapping; 1 unresolved instance(s) marked inline.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 85,
    "h2": 37,
    "h3": 7
  },
  "macron_a": 381,
  "macron_e": 30,
  "macron_i": 102,
  "macron_o": 95,
  "macron_u": 64,
  "schwa": 30,
  "greek_chars": 2414,
  "combining_diacritics": 301,
  "dagger": 1
}
```

## Structural integrity check

- Headings: chapter/section/subsection headings were preserved using Markdown heading levels. Secondary chapter subtitles encoded as additional `h1` elements were rendered as bold subtitle paragraphs to avoid duplicate top-level headings.
- Footnotes: chapter footnote back-references were converted to Markdown footnotes. Multi-paragraph note 1 in Chapter 2 was preserved with continuation indentation.
- Tables: 0 table block(s) were flagged by the crude delimiter-count check. This does not certify table semantic correctness.
- References: every chapter with a `References` section produced a matching per-chapter bibliography file.
- Page anchors: EPUB pagebreaks were preserved as Markdown HTML comments, e.g. `<!-- p. 101 -->`.
- Images: body figures were linked at their source locations. Cover/title/copyright decorative images were not copied into the output image directory.

## Image inventory

| Output filename | Source label | Page | Caption |
|---|---|---:|---|
| `larssen-ed-2025-ie-ecologies-fig2-1.jpg` | Chapter 2 Figure 1 | 39 | Figure 1 . IE conceptions of HUMAN LIFE and the CENTRE–PERIPHERY spatial schema. Graphics: Riccardo Ginevra © License: CC BY-NC. |
| `larssen-ed-2025-ie-ecologies-fig2-2.jpg` | Chapter 2 Figure 2 | 43 | Figure 2 . IE conceptions of human ecology and CENTRE–PERIPHERY spatial schema. Graphics: Riccardo Ginevra © License: CC BY-NC. |
| `larssen-ed-2025-ie-ecologies-fig4-1.jpg` | Chapter 4 Figure 1 | 81 | Figure 1 . Heracles and Geryon. Depiction on a Chalcidian amphora produced in Calabria (c. 530 BCE ), Cabinet des Médailles, Paris (De Ridder.202) with painted inscription: ATHENAIE, GARUWONES, HERAKLES. Photo: Serge Oboukhoff / BnF-CNRS-MSH Mondes © License: CC BY-NC. |
| `larssen-ed-2025-ie-ecologies-fig4-2.jpg` | Chapter 4 Figure 2 | 82 | Figure 2 . Depiction on the golden bowl of Hasanlu (detail), north-west Iran (late 2nd millennium BCE ). Image 96557, courtesy of the Penn Museum © License: CC BY-NC. |
| `larssen-ed-2025-ie-ecologies-fig4-3.jpg` | Chapter 4 Figure 3 | 97 | Figure 3 . Snakes and tricephalic monster with an axe and a tethered horned animal. Eighteenth-century rendering of a depiction of the fifth-century CE lesser horn (B) from Gallehus. Photo: Malene Thyssen. From: Wikimedia Commons. License: CC-PD. |
| `larssen-ed-2025-ie-ecologies-fig5-1.jpg` | Chapter 5 Figure 1 | 103 | Figure 1 . The Churning of the Ocean. From: Wikimedia Commons. License: CC-PD. |
| `larssen-ed-2025-ie-ecologies-fig5-2.jpg` | Chapter 5 Figure 2 | 107 | Figure 2 . Churning butter. From: WebExhibits. License: CC BY-NC. |
| `larssen-ed-2025-ie-ecologies-fig6-1.jpg` | Chapter 6 Figure 1 | 136 | Figure 1 . Fertile fields covered by snow. Håga Valley in Uppsala, Sweden, 6 January 2022. Photo: Terje Oestigaard © License: CC BY-NC. |
| `larssen-ed-2025-ie-ecologies-fig6-2.jpg` | Chapter 6 Figure 2 | 140 | Figure 2 . Frey and wild-boar. By Jacques Reich (1852–1923). From: Guerber 1909: 118. License: CC-PD. |
| `larssen-ed-2025-ie-ecologies-fig6-3.jpg` | Chapter 6 Figure 3 | 142 | Figure 3 . The sacrifice of Domalde in Old Uppsala. By Erik Werenskiold (1855–1938). From: Snorri 2011 [1899]. License: CC-PD. |
| `larssen-ed-2025-ie-ecologies-fig6-4.jpg` | Chapter 6 Figure 4 | 144 | Figure 4 . Terrestrial and celestial forces at work in agrarian cosmologies. Graphics: Terje Oestigaard © License: CC BY-NC. |
| `larssen-ed-2025-ie-ecologies-fig6-5.jpg` | Chapter 6 Figure 5 | 145 | Figure 5 . Growth forces living and manifesting themselves beneath the snow in early spring. Photo: Terje Oestigaard © License: CC BY-NC. |
| `larssen-ed-2025-ie-ecologies-fig6-6.jpg` | Chapter 6 Figure 6 | 146 | Figure 6 . The never-freezing Ingbokällarna, Sweden. Photo: Terje Oestigaard © License: CC BY-NC. |
| `larssen-ed-2025-ie-ecologies-fig6-7.jpg` | Chapter 6 Figure 7 | 152 | Figure 7 . The Håga mound covered in snow, 6 January 2022. Photo: Terje Oestigaard © License: CC BY-NC. |
| `larssen-ed-2025-ie-ecologies-fig6-8.jpg` | Chapter 6 Figure 8 | 154 | Figure 8 . Fertile fields in the Håga Valley, Uppsala. Photo: Terje Oestigaard © License: CC BY-NC. |
