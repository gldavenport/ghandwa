---
title: "Two IE phylogenies, three PIE migrations, and four kinds of steppe pastoralism"
author: "David W. Anthony"
date: "2013"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "anthony-2013-two-ie-phylogenies.pdf"
chunk: "extraction-report"
---

# Extraction report

## Source type

Born-digital PDF. The PDF contains a machine-readable text layer. The raw extracted text was used as the primary source; page renderings were consulted for figure placement, figure extraction, and high-risk character/format checks.

## Corrections applied

- Removed running headers, page numbers, and the page 1 journal footer from the main extraction.
- Rejoined paragraph text across line breaks and page boundaries; paragraph starts were inferred primarily from source indentation.
- Repaired line-break hyphenation in running prose, bibliography entries, and the Russian abstract. True compounds and names such as `Pontic-Caspian`, `Indo-European`, `Proto-Germanic`, `Yamnaya-Repin`, `Pre-Celtic`, `high-prestige`, and `well-tested` were restored after default dehyphenation.
- Replaced visible soft-hyphen uses with explicit hyphens in `1000-word` and `*ghos-ti-`.
- Split the end bibliography into `anthony-2013-two-ie-phylogenies-bibliography.md`.
- Extracted five embedded figure images into `images/` and inserted Markdown image references at the figure-caption locations.
- Visually checked the malformed text-layer form `*haeǩs-` on page 5 and represented the lowered `a` as `*hₐ[?]eǩs-`. This is marked as inferred/uncertain because the source's PDF text layer does not encode the subscript position.
- Represented the figure 5 isotope caption as `¹⁵[?]N` and `¹³[?]C` because the source displays isotope mass numbers typographically as superscripts but the text layer exposes plain digits.

## Unresolved issues

- Page 5: `*hₐ[?]eǩs-` is visually inferred from the rendered page. The PDF text layer gives `*haeǩs-`; the lowered `a` may reflect the PDF font encoding rather than a standard laryngeal index.
- Page 15 / Fig. 5 caption: `¹⁵[?]N` and `¹³[?]C` use visually inferred superscript mass numbers; the text layer gives `15N` and `13C`.
- Bibliography: several likely source-level typographical errors were preserved rather than silently corrected, including `Koivulheto`, `Orlovskata`, `culrures`, `Catcomb Grvae`, and `Jounal`. These may merit later source-image verification if the bibliography is used as citation authority.
- Italic and small-cap styling was not exhaustively encoded where the PDF text layer did not expose semantic markup. Main logical structure and character content were prioritized.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: no standard indexed laryngeals were detected in the extracted output. One non-standard visually lowered `a` in `*hₐ[?]eǩs-` remains uncertain.
- Macron vowels `ā ē ī ō ū`: no macron vowels were detected in the extracted output.
- Superscript modifier letters `ʰ ʷ`: no instances were detected.
- Schwa `ə`: no instances were detected.
- Underdot letters `ṛ ḷ ṃ ṇ`: no instances were detected.
- Acute consonants `ǵ ḱ`: no instances were detected. The output retains source/PDF text-layer `ǩ` in `*hₐ[?]eǩs-`; this may be a font/text-layer peculiarity and should not be treated as verified PIE normalization.
- Asterisk `*`: reconstructed or technical forms with asterisks were preserved where detected, including `*hₐ[?]eǩs-` and `*ghos-ti-`.
- Dagger `†`: no instances were detected.

## Codepoint inventory

All counts are approximate and intended for cross-pass comparison only.

```json
{
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 0,
  "macron_e": 0,
  "macron_i": 0,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 0,
  "greek_chars": 0,
  "combining_diacritics": 0,
  "dagger": 0
}
```

Markers inserted: `3` `[?]` markers; `0` `[unclear]` markers.

## Structural integrity check

- Headings are represented consistently.
- Figure images and captions are present at their source locations.
- The article bibliography is separated from the main corpus file.
- The Russian summary after the bibliography is included in the main corpus file under `Russian abstract`.
- No index was present in the source.
- No footnotes/endnotes were detected in the source.

## Image inventory

| File | Source label | Page | Caption |
|---|---:|---:|---|
| `images/anthony-2013-two-ie-phylogenies-fig1.png` | Fig. 1 | 7 | Fig. 1. The Proto-Indo-European homeland and the first three migrations, paralleling the phylogeny of Ringe et al. 2002 |
| `images/anthony-2013-two-ie-phylogenies-fig2.png` | Fig. 2 | 9 | Fig. 2. The first migration, 4200–4000 bc, of the Suvorovo-type immigrants into the Danube valley, Transylvania, and the Dobruja |
| `images/anthony-2013-two-ie-phylogenies-fig3.png` | Fig. 3 | 10 | Fig. 3. The second migration, 3300–2800 bc or later, of the Afanasievo-type immigrants into the western Altai Mountains. |
| `images/anthony-2013-two-ie-phylogenies-fig4.png` | Fig. 4 | 11 | Fig. 4. The third migration, 3000–2800 bc, of the Yamnaya immigrants into the Danube valley, and penetration of Usatovo-type and Yamnaya-type contacts with Tripol’ye CII and pre-Corded Ware communities on the upper Vistula |
| `images/anthony-2013-two-ie-phylogenies-fig5.png` | Fig. 5 | 15 | Fig. 5. Stable isotopes of ¹⁵[?]N and ¹³[?]C in human bone in individuals from the Eneolithic through the LBA in the middle Volga steppes. The Eneolithic diet was significantly different from the Bronze Age diet. The EBA, MBA, and LBA diets showed no difference in stable isotopes |
