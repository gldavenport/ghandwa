---
title: "The Oxford Introduction to Proto-Indo-European and the Proto-Indo-European World"
author: "J. P. Mallory and D. Q. Adams"
date: "2006"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "mallory-oxford-introduction-indo-european-world.pdf"
chunk: "extraction-report"
---


# Extraction report

## Source assessment

- Source type: born-digital PDF with machine-readable text layer.
- Primary input: `pdftotext -layout`; visual rendering used for maps/figures and spot checks.
- Text layer has systematic glyph corruption, so this is a cleaned first-pass extraction, not a fully character-authoritative edition.

## Corrections applied

- Ligature artifact repairs: initial dictionary (1045), W→fi (596), X→fl (170), V→ff (620), Y→ffi (146).
- Symbol repairs: `þ`→`+` (982), `¼`→`=` (165).
- Macron, accent, caron, underdot/ring-below, palatal-velar, and laryngeal-index normalization were applied by rule.
- Running headers/footers and standalone page-number lines were removed heuristically.
- Hyphenated line-breaks were repaired by rule.

## Unresolved issues

- Dense tables, appendices, and indexes were not hand-collated against page images. They are preserved from the layout text layer and should receive a second pass if used as structured data.
- Laryngeal normalization was mechanical; verify in a character-fidelity pass.
- Resonant+`8` sequences were normalized mainly as syllabic ring-below notation; Sanskrit and PIE contexts may need human verification.
- No `[?]` inline inferred-character markers were inserted because the main source was machine-readable rather than scanned.

## Confusion-pair report

- `h₁ h₂ h₃`: normalized from ASCII forms; residual ASCII counts are in the manifest.
- `ā ē ī ō ū`: normalized from extracted overbar sequences; residual counts are in the manifest.
- `ʰ ʷ`, `ə`, `ǵ ḱ`, and `†`: not fully hand-verified.
- `*`: preserved where present in the text layer; not exhaustively checked.

## Structural integrity check

- Chunked by source chapter, with separate appendices, bibliography, and index.
- Page anchors are included as HTML comments.
- Extracted/rasterized maps and figures are included in `images/` and referenced in the relevant chapter files.

## Image inventory


## Codepoint inventory (approximate)

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 1836,
    "h2": 1138,
    "h3": 379
  },
  "macron_a": 0,
  "macron_e": 0,
  "macron_i": 0,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 0,
  "greek_chars": 0,
  "combining_diacritics": 26320,
  "dagger": 0
}
```

## Residual artifact counts for review (approximate)

```json
{
  "W": 2499,
  "X": 129,
  "Y": 83,
  "V": 241,
  "¼": 0,
  "þ": 0,
  "a¯": 0,
  "e¯": 0,
  "i¯": 0,
  "o¯": 0,
  "u¯": 0,
  "h1": 0,
  "h2": 0,
  "h3": 0
}
```
