---
title: "Extraction report — On the Origin of Greek μῆλον, Latin mālum, Albanian mollë and Hittite šam(a)lu- ‘apple’"
author: "Guus Kroonen"
date: "2016"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "kroonen-2016.pdf"
---

# Extraction Report

## Source identification

- Source file: `kroonen-2016.pdf`
- Source type: born-digital PDF with a machine-readable text layer.
- Page range in source: pp. 85–91, rendered as 7 PDF pages.
- Output strategy: single-file journal article extraction, with bibliography separated into its own file.
- Images: none present in the article.

## Corrections applied

- Rejoined line-broken words and removed running headers, footers, printed page numbers, and journal footer text from the main corpus file.
- Normalized laryngeal indices to Unicode subscript digits, e.g. `h₂` rather than `h2`.
- Repaired corrupted text-layer glyphs by checking rendered page images, especially Greek forms, Hittite ḫ/Ḫ and š/Š, Sumerogram notation, macron vowels, Albanian ë, Czech diacritics, and footnote symbols.
- Preserved source hyphenation distinctions where visible, e.g. <i>*meh₂lo-</i> versus <i>*meh₂-lo-</i>.
- Converted footnotes to Markdown footnotes and moved the bibliography to `kroonen-2016-bibliography.md`.
- Added unobtrusive HTML page anchors as comments at source page boundaries in the main text.

## Unresolved issues and high-attention items

- The PDF text layer is notably unreliable for several linguistic characters. Rendered images were used as authority for corrupted glyphs.
- Footnote 5: the Arabic initial sign in *ʔubullat* and *ʔabal-* was read from the rendered page as `ʔ`; this should be checked against the print source if exact Arabicist transcription is critical.
- The source bibliography prints `Tourner, H. M.` while footnote 1 cites `Tournier 1794`; the bibliography spelling was preserved as printed.
- The source text appears to print `Puhvel1997` and `Ivanov1984` without spaces in two body citations; these were preserved.
- The anaptyctic-vowel notation was represented as superscript schwa `ᵊ` in <i>*CRᵊHC-</i> and <i>*CᵊRHC-</i>, based on the rendered form.
- No `[unclear]` markers were inserted in the corpus files.

## Confusion-pair report

This pass focused on the high-risk character classes named in the extraction instructions. It cannot certify that no consistent error remains.

| Item | Status |
|---|---|
| `h₁ h₂ h₃` vs. ASCII `h1 h2 h3` | `h₂` was normalized to subscript form throughout the extracted linguistic notation. No `h₁` or `h₃` instances were observed. |
| Macron vowels | Latin macron vowels were visually checked in main text, notes, and bibliography: `mālum`, `mālus`, `mēlō`, `mīlle`, `lātus`, `ḫašḫūru-`. |
| Superscript/modifier letters | `ʰ` was used in reconstructed forms such as <i>*gʰes-l-ih₂</i> and <i>*sṃ-gʰéslo-</i>. |
| Schwa / anaptyctic vowel notation | Represented as superscript schwa `ᵊ`; the exact typographic status of this small printed sign should remain a high-attention item. |
| Underdot/syllabic markers | Footnote 2 uses <i>*sṃ-gʰéslo-</i>; PIE <i>*tl̥h₂-tó-</i> uses `l̥`. These were visually checked. |
| Acute consonants `ǵ ḱ` | No such forms observed. |
| Asterisk before reconstructed forms | Preserved; reconstructed forms with leading `*` are generally wrapped in inline HTML italics to avoid Markdown parsing ambiguity. |
| Dagger `†` | No dagger instances observed. |
| Greek forms | Rendered images were used for Greek forms including *μῆλον*, *μᾶλον*, *μία*, *τλητός*, *τλᾱτός*, and <i>*μασλον</i>. |
| Hittite/Sumerian/Akkadian ḫ and š | Rendered images were used for *šam(a)lu-*, *maḫla-*, <sup>GIŠ</sup>ḪAŠḪUR, *geš*, *ḫašḫur*, and *ḫašḫūru-*. |

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "laryngeals": {
    "h1": 0,
    "h2": 24,
    "h3": 0
  },
  "macron_a": 11,
  "macron_e": 1,
  "macron_i": 1,
  "macron_o": 2,
  "macron_u": 1,
  "schwa": 2,
  "greek_chars": 86,
  "combining_diacritics": 1,
  "dagger": 0
}
```

## Structural integrity check

- Main heading, author metadata, abstract, body paragraphs, and footnotes are present.
- Bibliography is separated as required for the extraction workflow.
- Footnote markers 1–6 were preserved and attached to their note text.
- No figures, tables, plates, maps, or image-only material were present.
- No continuation text appears intentionally omitted at page boundaries, but the PDF's corrupted text layer means character-level review remains advisable for any future citation-grade use.
