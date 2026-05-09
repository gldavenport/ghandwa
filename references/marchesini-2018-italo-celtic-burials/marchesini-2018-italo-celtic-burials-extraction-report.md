---
title: "Inscriptions from Italo-Celtic burials in the Seminario Maggiore (Verona) — extraction report"
author: "Simona Marchesini and David Stifter"
date: 2018
source_type: born-digital
extraction_date: 2026-05-08
source_file: "marchesini-2018-italo-celtic-burials.pdf"
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF. A machine-readable text layer is present and was used as the primary input. Visual/page rendering was used as a fallback for figure ordering, figure-image association, and checks against the dense table and catalogue pages.

The PDF contains the SIMA volume front matter before the chapter. The main extraction file treats pp. 143–154 as the target book chapter and uses the front matter only for bibliographic metadata.

## Corrections applied

- Removed running headers, footers, page numbers, and decorative/front-matter material not part of the target chapter body.
- Moved the chapter title and author block to the top of the Markdown file, because the PDF text layer places it after page-143 body text.
- Rejoined line-broken paragraphs and repaired line-break artifacts such as `Italo-
Celtic`, `socio-
linguistic`, and broken URL text (`http://www.
univie...`).
- Reconstructed the chapter hierarchy as Markdown headings using the source section numbers 4.5.1–4.5.8.
- Reconstructed Table 4.5.1 as a Markdown table from the born-digital text layer, checked against the page rendering.
- Extracted the embedded chapter figure images as discrete files under `images/` and linked them at the relevant catalogue entries.

## Unresolved issues list

- No. 2: the source itself says only the letter `a` is easy to read and the second connected letter is illegible; the extraction preserves this statement rather than guessing.
- No. 5: the source presents the reading uncertainty `prituli` or `pritua`; both are preserved.
- No. 8: the discussion preserves the uncertainty about whether the relevant letter should be interpreted as `P` or a vertically flipped `L`; `kasipus` is retained as the authors' upheld reading.
- No. 11: the source gives multiple possible readings (`titi`, `aś`, `ka`, and `XIXI or titi` in the catalogue). These are preserved as given.
- Table 4.5.1 contains dense Etruscan/epigraphic notation with superscripts, Greek letters, underdots, and uncertain letters. It was checked against the source text layer and page rendering, but should receive another focused pass if it will be used as a character-authoritative epigraphic dataset.
- Figure 4.5.7 caption gives tomb `US3915` in the source caption, while catalogue prose gives pit-grave `US 3195`. Both source readings are preserved in their respective locations.

## Confusion-pair report

- `h₁ h₂ h₃`: no laryngeal forms were found in this chapter output.
- `ā ē ī ō ū`: macron vowels occur and were preserved where present in the text layer (`rīg-`, `Eskingorīχs`, `Tou̯torīχs`, `māro-`, etc.). Could not certify every macron in Table 4.5.1 without a dedicated epigraphic-table pass.
- `ʰ ʷ`: no superscript aspiration/labialization letters were found in this chapter output.
- `ə`: no schwa was found in this chapter output.
- `ṛ ḷ ṃ ṇ`: underdotted letters occur in Table 4.5.1 and were preserved from the text layer where detected (`aṇcarual`, `ṇasu`, etc.).
- `ǵ ḱ`: no acute consonant instances were found.
- `*`: reconstructed forms and roots with asterisks were preserved (`*eχs`, `*esking-`, `*ku̯ritu-`, `*katu-`, etc.).
- `†`: no dagger instances were found.
- Source-specific confusions checked: Greek chi `χ` versus Latin `x`; acute s `ś` versus plain `s`; theta `θ`; phi `φ`; combining inverted breve below in `u̯`; superscript numerals in Table 4.5.1.

## Codepoint inventory

Approximate counts from the main Markdown extraction:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 4,
  "macron_e": 3,
  "macron_i": 18,
  "macron_o": 0,
  "macron_u": 3,
  "schwa": 0,
  "greek_chars": 52,
  "combining_diacritics": 6,
  "dagger": 0
}
```

## Structural integrity check

- Headings are consistent with the chapter's source numbering.
- No bibliography section is present in the supplied chapter excerpt; references remain inline.
- No index is present in the supplied chapter excerpt.
- Table 4.5.1 is represented as a Markdown table. The table is dense and should be treated as a candidate for a future focused epigraphic-table QA pass.
- Figure images were extracted from embedded PDF image streams and linked in the catalogue.
- Page-boundary continuation into the catalogue was manually repaired.

## Image inventory

| File | Source label | Page | Caption |
|---|---:|---:|---|
| `images/marchesini-2018-italo-celtic-burials-fig4-5-1.jpeg` | Figure 4.5.1 | 20 | Figure 4.5.1. Verona. Necropolis of Seminario Maggiore. VR 91591. Tomb US2631 (prepared by the authors) |
| `images/marchesini-2018-italo-celtic-burials-fig4-5-2.jpeg` | Figure 4.5.2 | 21 | Figure 4.5.2. Verona. Necropolis of Seminario Maggiore. VR 91592. Tomb US2758 (prepared by the authors) |
| `images/marchesini-2018-italo-celtic-burials-fig4-5-3.jpeg` | Figure 4.5.3 | 21 | Figure 4.5.3. Verona. Necropolis of Seminario Maggiore. VR 2006 SV. Tomb US935 (prepared by the authors) |
| `images/marchesini-2018-italo-celtic-burials-fig4-5-4.jpeg` | Figure 4.5.4 | 21 | Figure 4.5.4. Verona. Necropolis of Seminario Maggiore. VR 91594. Tomb US3178 (prepared by the authors) |
| `images/marchesini-2018-italo-celtic-burials-fig4-5-5.jpeg` | Figure 4.5.5 | 21 | Figure 4.5.5. Verona. Necropolis of Seminario Maggiore. VR 91595. Tomb US3289 (prepared by the authors) |
| `images/marchesini-2018-italo-celtic-burials-fig4-5-6.jpeg` | Figure 4.5.6 | 21 | Figure 4.5.6. Verona. Necropolis of Seminario Maggiore. VR 91596. Tomb US3243 (prepared by the authors) |
| `images/marchesini-2018-italo-celtic-burials-fig4-5-7.jpeg` | Figure 4.5.7 | 22 | Figure 4.5.7. Verona. Necropolis of Seminario Maggiore. VR 91597. Tomb US3915 (prepared by the authors) |
| `images/marchesini-2018-italo-celtic-burials-fig4-5-8.jpeg` | Figure 4.5.8 | 22 | Figure 4.5.8. Verona. Necropolis of Seminario Maggiore. VR 91598. Tomb US3206 (prepared by the authors) |
| `images/marchesini-2018-italo-celtic-burials-fig4-5-9.jpeg` | Figure 4.5.9 | 22 | Figure 4.5.9. Verona. Necropolis of Seminario Maggiore. VR 91599. Tomb US3277 (prepared by the authors) |
| `images/marchesini-2018-italo-celtic-burials-fig4-5-10.jpeg` | Figure 4.5.10 | 22 | Figure 4.5.10. Verona. Necropolis of Seminario Maggiore. VR 91600, Tomb US3277 (prepared by the authors) |
| `images/marchesini-2018-italo-celtic-burials-fig4-5-11.jpeg` | Figure 4.5.11 | 22 | Figure 4.5.11. Verona. Necropolis of Seminario Maggiore. VR IG 91593, Tomb US3218 (prepared by the authors) |

## Image-glyph inventory

No EPUB-style inline image glyphs were present.

## Extraction limitations

This is a clean corpus extraction, not a diplomatic transcription. Physical page layout, two-column geometry, running headers, page numbers, and decorative layout were not preserved. The QC pass cannot catch errors made consistently throughout the extraction; the character-heavy table and uncertain graffiti readings remain the highest-risk areas.
