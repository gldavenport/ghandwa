# From Proto-Indo-European to Proto-Germanic: Second edition — extraction report

## Source identification

- Source file: `ringe-2017-pie-to-proto-germanic-2nd.pdf`
- Source type: born-digital PDF with a machine-readable text layer.
- Primary input used: raw extracted PDF text layer, with visual/rendered crops used for figure handling.
- Extraction date: 2026-05-07

## Corrections applied

- Normalized Oxford/private-use old-style digits to ASCII digits. Approximate raw private-use digit replacements: 41314.
- Normalized private-use small-cap letters to ASCII capitals where the PDF text layer exposed small caps as private-use codepoints.
- Repaired common typographic ligatures (`ﬁ`, `ﬂ`, etc.) to Unicode/ASCII letter sequences. Approximate ligature repairs: 2680.
- Applied broad laryngeal-index normalization: `h1`, `h2`, `h3` -> `h₁`, `h₂`, `h₃`.
- Normalized common acute-on-consonant sequences to precomposed characters where detected: `ḱ/k´` -> `ḱ`; `ǵ/g´` -> `ǵ`.
- Removed a limited set of repeated running headers/footers and the repeated OUP chapter-opening copyright footer.
- Added page anchors as HTML comments at page boundaries.
- Extracted/rasterized two labeled figures into `images/` and inserted Markdown image references at the caption locations.

## Unresolved issues and human-review targets

1. The PDF uses specialist fonts and custom encodings. The text layer is usable but not fully authoritative for every scholarly symbol.
2. Superscript aspiration/labialization in obstruent notation may remain as plain `h`/`w` in some contexts; these were not globally converted because doing so safely would require form-by-form visual verification.
3. Dense paradigms, charts, and index sections preserve much of the PDF text-layer lineation. This avoids losing characters but should be reviewed if a fully reflowed prose edition is later desired.
4. Footnotes were preserved in extracted page order but were not normalized to a uniform Markdown footnote syntax in this pass.
5. Figure 3.1 is both exposed by the text layer and rasterized as an image. The visual crop should be treated as the authoritative representation of the chart.
6. Some hyphenation across line breaks may remain. No aggressive dehyphenation was applied because many linguistic forms contain meaningful hyphens.
7. The index is included as a separate file, but dense line-entry validation against the rendered pages has not been exhaustively performed.

## Confusion-pair report

- `h₁ h₂ h₃`: broad normalization was applied. Remaining ASCII `h1/h2/h3`, if any, should be treated as high-priority review targets.
- Macron vowels: preserved where present in the text layer; no full visual audit was performed across the index and paradigms.
- Superscript `ʰ` and `ʷ`: not globally normalized because the PDF text layer mostly exposes these as plain letters in technical clusters; output may contain source-layer `h`/`w` in such forms.
- `ə`: preserved where exposed as Unicode schwa; some chart text may expose schwa-like glyphs as Cyrillic `ә` from the PDF text layer.
- Underdot letters (`ṛ`, `ḷ`, `ṃ`, `ṇ`): preserved where present in the text layer; not visually audited exhaustively.
- `ǵ`, `ḱ`: common extraction forms were normalized to precomposed characters where possible; some uppercase symbolic `K´` contexts may remain source-like.
- Asterisks: preserved where present in the text layer.
- Daggers: preserved where present; approximate count is recorded in the manifest.

## Codepoint inventory

All counts are approximate and intended for cross-pass comparison only.

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 1176,
    "h2": 1416,
    "h3": 176
  },
  "macron_a": 1028,
  "macron_e": 1155,
  "macron_i": 953,
  "macron_o": 2000,
  "macron_u": 401,
  "schwa": 193,
  "greek_chars": 4762,
  "combining_diacritics": 1709,
  "dagger": 0
}
```

## Structural integrity check

- Chunking follows the source outline and the extraction instructions: front matter; chapter/section/subsection chunks for long sections; bibliography and index as standalone files.
- Chapter 2, Chapter 3, and Chapter 4 were split at source-labeled divisions because the chapters exceed 50 pages; long top-level sections were split at the next source-labeled level.
- Bibliography and index are not mixed into main chapter files.
- Page anchors are present throughout for source checking.
- Figures are listed in the manifest and placed in `images/`.
- Tables/paradigms/charts are preserved conservatively; some may require a later table-specific pass for ideal Markdown tables.

## Image inventory

| File | Source label | Printed page | Caption |
|---|---:|---:|---|
| `images/ringe-2017-pie-to-proto-germanic-2nd-fig2-1.png` | Figure 2.1 | 7 | A probable cladistic tree of the Indo-European family. |
| `images/ringe-2017-pie-to-proto-germanic-2nd-fig3-1.png` | Figure 3.1 | 176 | Recoverable chronological relations of sound changes from PIE to PGmc. |
