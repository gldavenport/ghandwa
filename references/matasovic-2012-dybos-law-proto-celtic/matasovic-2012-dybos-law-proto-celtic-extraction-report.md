---
title: "Dybo’s law in Proto-celtic"
author: "Ranko Matasović"
date: 2012
source_type: born-digital
extraction_date: 2026-05-07
source_file: "matasovic-2012-dybos-law-proto-celtic.pdf"
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with machine-readable text layer present, but the text layer uses nonstandard/corrupted glyph mappings for many ordinary Latin letters, small caps, ligatures, numerals, and laryngeal markers. The raw extracted text was therefore used as the primary input, with coordinate-based spacing repair and targeted visual checking against rendered pages.

## Corrections applied

- Mapped private-use glyphs to ordinary Latin letters where context and rendered page forms made the mapping clear: `r`, `s`, `t`, `u`, `w`, `x`, `y`, `z`, `q`, `Th`, `ft`, and `tt`.
- Repaired source-specific ligature confusions, including `fi`, `fl`, `ff`, and `ffi` in words such as `reflexes`, `suffix`, `affected`, `different`, and `confirmed`.
- Normalized laryngeal markers extracted as Arabic combining-like characters to subscript digits: `h₁`, `h₂`, and `h₃`.
- Recovered small-cap author names and abbreviations from rendered pages and context: KORTLANDT, SCHRIJVER, McCONE, ZAIR, ISAAC, IRSLINGER, BEEKES, BURROW, DYBO, VINE, POKORNY, RIX, WODTKO, MATASOVIĆ, SMIRNOV, and SOUTHERN.
- Repaired oldstyle/small-cap numerals in dates, EDPC page references, and numbered examples.
- Repaired selected broken lineation and page-boundary breaks. Some physical line breaks are retained where automatic reflow risked damaging technical notation.
- Separated the bibliography into `matasovic-2012-dybos-law-proto-celtic-bibliography.md`.
- Converted footnotes to Markdown footnotes in the main extraction file.

## Unresolved issues

- The PDF text layer is systematically corrupt in the body font, so a fully automatic extraction cannot certify every character. The output should be treated as a strong first-pass/second-pass extraction rather than a final character-authoritative edition.
- Some spacing around nonsyllabic markers and combining marks may need later review, especially forms with `i̯`, `u̯`, `ᵘ̯`, and syllabic resonants.
- The bibliography was manually regularized from a corrupted text layer and should be checked against the rendered final page if a citation-critical bibliography is required.
- The main file does not attempt to preserve all small-caps styling as markup; small-cap author names are represented as uppercase/plain text.
- No figure/table image extraction was needed; the source appears to contain running text only.

## Confusion-pair report

- `h₁ h₂ h₃`: normalized where the extracted layer preserved the laryngeal index as a distinct glyph. Some uppercase `H` laryngeal notation is intentionally preserved where the source used `H`.
- Macron vowels `ā ē ī ō ū`: preserved where present in the extracted layer; selected OCR-like confusions were visually checked in high-value forms, but the list is not certified exhaustive.
- Superscript/modifier letters: `ʰ`, `ʷ`, and `ᵘ̯` were preserved where identifiable. The `ᵘ̯` forms are source-sensitive and should be reviewed in a later pass if these forms are reused for formal phonological datasets.
- `ə` / `ǝ`: preserved as extracted in Pashto forms.
- Underdot letters and combining rings: preserved in forms such as `pṛṇā́ti`, `stṛṇā́ti`, and syllabic resonants; no claim of exhaustive verification.
- Acute consonants and palatals: preserved where extracted, e.g. `g̑`, `k̑`, `ĺ`, `ŕ`, `ń`.
- Asterisks before reconstructed forms were preserved as ordinary ASCII asterisks.
- Dagger `†`: no dagger instances found in output.

## Codepoint inventory

All counts are approximate and for cross-pass comparison only.

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 44,
    "h2": 61,
    "h3": 30
  },
  "macron_a": 82,
  "macron_e": 20,
  "macron_i": 25,
  "macron_o": 23,
  "macron_u": 38,
  "schwa": 3,
  "greek_chars": 0,
  "combining_diacritics": 136,
  "dagger": 0
}
```

## Structural integrity check

- Main article body, section headings, numbered examples, conclusion, footnotes, and references are represented.
- Footnotes are attached as Markdown footnotes in the main text.
- No semantic tables or figures were identified.
- Page anchors are retained as HTML comments for later source-location checks.
- Bibliography is separated from the main file.

## Image inventory

No images extracted; no image placeholders used.
