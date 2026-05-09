---
title: "Linguistic Residues of Steppe Culture in Germanic — Extraction Report"
author: "Jenne Klimp"
date: "2019-06-07"
source_type: born-digital
extraction_date: "2026-05-07"
source_file: "klimp-linguistics-residues-steppe.pdf"
chunk: extraction-report
---

# Extraction Report

## Source identification

- Source file: `klimp-linguistics-residues-steppe.pdf`
- Source type: born-digital PDF with a machine-readable text layer.
- Length: 8 pages.
- Main output: `klimp-linguistics-residues-steppe.md`
- Bibliography output: `klimp-linguistics-residues-steppe-bibliography.md`
- Index output: none; no index is present in the source.
- Image output: one embedded image extracted to `images/klimp-linguistics-residues-steppe-p4-fig1.jpeg`.

## Corrections applied

- Rejoined line-broken prose from the PDF text layer into running paragraphs.
- Removed running page-boundary breaks while preserving logical section structure.
- Separated the `LITERATURE` section into `klimp-linguistics-residues-steppe-bibliography.md`.
- Reconstructed bullet lists and nested bullet structure for examples and section §4.5.
- Converted verse and parallel poetic passages into fenced `text` blocks where prose Markdown would damage alignment.
- Extracted the unnumbered embedded image on page 4 and inserted a Markdown image reference at the corresponding location in §4.2.
- Normalized laryngeal indices from flattened text-layer forms `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃` in reconstructed and technical forms.
- Normalized visually superscripted aspirates/labiovelars where the text layer flattened them: examples include `dʰ`, `bʰ`, `g̑ʰ`, `gʷ`, and `kʷ`.
- Normalized the visually superscripted `(w)` in `*sweh⁽ʷ⁾ōnes`.
- Preserved combining diacritics where the source text layer used decomposed forms, e.g. `ś`, `ṓ`, `r̥`, `ḫ`, and `u̯`.

## Unresolved issues list

No `[unclear]` markers were inserted.

Residual review risk remains in technical forms because the PDF text layer flattened some superscript/subscript notation. I spot-checked rendered pages against high-risk forms, but this report does not certify that every reconstructed form is error-free.

Specific items worth review in a future pass:

- `*sweh⁽ʷ⁾ōnes`: encoded with superscript parentheses and superscript w to match the visible superscripted `(w)`; the raw text layer had `*sweh(w)ōnes`.
- `*g̑ʰrh₁-h₃ṓd-s/*g̑ʰrh₁-h₃d-és` and related forms: the text layer flattened the aspirate after `g̑`; output uses `g̑ʰ` after visual spot-checking.
- `*bʰedʰh₂-` family: the text layer flattened both aspirated stop notation and the laryngeal index; output uses `bʰ`, `dʰ`, and `h₂`.
- The extracted image has no printed caption. The Markdown alt text and manifest caption are descriptive, not source caption text.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: normalized in the output. Approximate counts: h₁=24, h₂=12, h₃=13. No ASCII `h1`, `h2`, or `h3` strings remain in the Markdown outputs.
- Macron vowels: precomposed macron vowels were preserved where present. Approximate counts: ā=57, ē=14, ī=10, ō=13, ū=5. Some vowels also carry combining acute marks after macrons, matching the extracted source layer.
- `ʰ ʷ` vs. `h w`: superscript aspirate/labiovelar notation was normalized in visible technical forms where flattened by the PDF text layer. Approximate counts: ʰ=31, ʷ=11. Plain `h` and `w` remain where linguistically ordinary or part of laryngeal notation.
- `ə`: no schwa found in this source/output.
- Underdot/ring/Indic notation: output preserves `ṛ`, `ṣ`, `ṃ`, `r̥`, and related diacritic-bearing characters where present. This was not exhaustively certified.
- `ǵ ḱ`: the source appears to use `g̑` and `k̑` rather than precomposed acute-on-consonant characters in the relevant forms. Output preserves this notation.
- Asterisk `*`: reconstructed-form asterisks are preserved as literal U+002A asterisks.
- Dagger `†`: no dagger characters found in this source/output.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 24,
    "h2": 12,
    "h3": 13
  },
  "macron_a": 57,
  "macron_e": 14,
  "macron_i": 10,
  "macron_o": 13,
  "macron_u": 5,
  "schwa": 0,
  "greek_chars": 24,
  "combining_diacritics": 73,
  "dagger": 0,
  "superscript_h": 31,
  "superscript_w": 11
}
```

## Structural integrity check

- Headings are consistent with the source’s section labels, including the apparent jump from §2 to §4.
- Bibliography is separated as required.
- No footnotes or endnotes were present as discrete notes; inline citations were preserved in the main text.
- Tables are not present; verse/parallel passages were preserved using fenced blocks.
- Page-boundary continuation text was rejoined; no known continuation text was lost.
- One embedded image was extracted and linked from the Markdown body.

## Image inventory

| File | Source label | Page | Caption / note |
|---|---:|---:|---|
| `images/klimp-linguistics-residues-steppe-p4-fig1.jpeg` | unnumbered image | 4 | No printed caption. Referenced on p. 5 as “the image above” from the Helsinki Yamnaya burial news page. |
