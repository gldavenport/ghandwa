---
title: "The Ancient Languages of Europe"
author: "Roger D. Woodard, ed."
date: "2008"
source_type: born-digital
extraction_date: 2026-05-07
source_file: woodard-ed-2008-ancient-languages-europe.pdf
chunk: "woodard-ed-2008-ancient-languages-europe-extraction-report"
---

# Extraction report — The Ancient Languages of Europe

## Source identification

- Source file: `woodard-ed-2008-ancient-languages-europe.pdf`
- Source type: born-digital PDF with a machine-readable text layer.
- Primary extraction method: PyMuPDF text-layer extraction, with rasterized image fallbacks for figures and maps.

## Corrections applied

- Ligature repairs: approximately 1756.
- Reconstructed-form asterisk normalization: approximately 1325 instances of `∗` normalized to `*`.
- Laryngeal normalization: approximately 168 raw `h1`, `h2`, or `h3` sequences normalized to `h₁`, `h₂`, `h₃`.
- Running headers and standalone printed page numbers removed where detected; PDF page anchors retained as HTML comments.

## Unresolved issues

- The PDF uses custom-encoded fonts; Greek, phonetic, and specialized glyphs are not reliably exposed as Unicode. Unresolved source-layer C0/C1 glyphs are marked inline as `[unclear-glyph:U+XXXX]` rather than guessed.
- Total unresolved glyph markers inserted: approximately 4567.
- Dense paradigms, alphabet/sign tables, and indexes should receive a later visual repair pass before being treated as character-authoritative.

### Control-glyph inventory

- `U+0002`: 345
- `U+0003`: 79
- `U+0004`: 198
- `U+0005`: 110
- `U+0006`: 400
- `U+0007`: 85
- `U+0008`: 137
- `U+000B`: 167
- `U+000C`: 302
- `U+000E`: 104
- `U+000F`: 217
- `U+0010`: 204
- `U+0011`: 69
- `U+0012`: 343
- `U+0013`: 138
- `U+0014`: 221
- `U+0015`: 93
- `U+0016`: 131
- `U+0017`: 113
- `U+0018`: 23
- `U+0019`: 122
- `U+001A`: 16
- `U+001B`: 142
- `U+001C`: 104
- `U+001D`: 139
- `U+001E`: 258
- `U+001F`: 302
- `U+0080`: 1
- `U+0081`: 1
- `U+0082`: 1
- `U+0083`: 1
- `U+0084`: 1

## Confusion-pair report

- `h₁ h₂ h₃` versus `h1 h2 h3`: normalization was applied mechanically and not visually verified throughout.
- Macron vowels and combining diacritics were preserved where the text layer exposed them; losses may remain in dense tables and custom-font spans.
- Superscript `ʰ`/`ʷ`, underdots, Greek, IPA, and special scripts are not certified; no silent guessing was applied to unresolved glyphs.

## Codepoint inventory

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 62,
    "h2": 91,
    "h3": 15
  },
  "macron_a": 0,
  "macron_e": 0,
  "macron_i": 0,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 9,
  "greek_chars": 610,
  "combining_diacritics": 0,
  "dagger": 5
}
```

## Structural integrity check

- Chunking mirrors source chapter/appendix hierarchy.
- Per-chapter bibliographies were split into separate files at the extracted `Bibliography` heading.
- Combined indexes are in `woodard-ed-2008-ancient-languages-europe-index.md`.
- Tables and paradigms were preserved in text-layer line order rather than aggressively reformatted.

## Image inventory

- `woodard-ed-2008-ancient-languages-europe-fig1-1.png` — Figure 1.1, PDF page 24: Cretan hieroglyphic inscription and portrait stamped on a sealing
- `woodard-ed-2008-ancient-languages-europe-fig1-2.png` — Figure 1.2, PDF page 25: The Phaistos Disk (side A)
- `woodard-ed-2008-ancient-languages-europe-fig1-3.png` — Figure 1.3, PDF page 28: The Caslir Situla
- `woodard-ed-2008-ancient-languages-europe-fig2-1.png` — Figure 2.1, PDF page 39: The vowel phonemes of Classical Attic Greek
- `woodard-ed-2008-ancient-languages-europe-map1.png` — Map 1, PDF page 72: The Greek dialects of the first millennium BC and neighboring languages
- `woodard-ed-2008-ancient-languages-europe-fig5-1.png` — Figure 5.1, PDF page 121: South Picene inscription. South Picene, Rix Sp TE 6, stele (fragmentary)
- `woodard-ed-2008-ancient-languages-europe-fig5-2.png` — Figure 5.2, PDF page 122: Oscan inscription. Oscan, Rix Cp25a, funerary stele (side a)
- `woodard-ed-2008-ancient-languages-europe-map2.png` — Map 2, PDF page 147: The ancient languages of Italy and surrounding regions (for the Greek dialects of Italy and Sicily, see Map 1)
- `woodard-ed-2008-ancient-languages-europe-fig6-1.png` — Figure 6.1, PDF page 149: Venetic votive inscriptions
- `woodard-ed-2008-ancient-languages-europe-fig6-2a.png` — Figure 6.2, PDF page 150: Venetic epitaphs
- `woodard-ed-2008-ancient-languages-europe-fig6-2b.png` — Figure 6.2 (cont.), PDF page 151: Venetic epitaphs
- `woodard-ed-2008-ancient-languages-europe-fig6-3.png` — Figure 6.3, PDF page 154: Latino-Venetic inscription
- `woodard-ed-2008-ancient-languages-europe-fig9-1.png` — Figure 9.1, PDF page 213: The Germanic languages

## Recommended further passes

1. Custom-font glyph repair pass for Greek, IPA, Indo-Europeanist symbols, scripts, and sign tables.
2. Table/paradigm pass for chapters 2–6 and Appendix 1.
3. Index fidelity pass for diacritics, Greek, macrons, and special phonetic symbols.
4. Image-crop refinement pass if figure-only crops are required.
