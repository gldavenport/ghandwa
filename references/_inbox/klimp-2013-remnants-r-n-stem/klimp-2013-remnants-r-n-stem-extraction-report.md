---
title: "Remnants of *r/n-Stem Heteroclite Inflection in Germanic"
author: "J. Klimp"
date: "2013-09-25"
source_type: born-digital
extraction_date: "2026-05-07"
source_file: "klimp-2013-remnants-r-n-stem.pdf"
chunk: "extraction-report"
---


# Extraction report

## Source identification

- Source type: born-digital PDF with a machine-readable text layer.
- PDF metadata reports Microsoft Word 2010 as creator/producer, 158 pages, tagged PDF, and no encryption.
- Important qualification: several embedded/non-Unicode font mappings cause missing or corrupted glyphs in the text layer. The extraction therefore preserves the text layer as the primary input but marks detected missing-glyph gaps as `[unclear]`.

## Corrections applied

- Removed running page headers and page-number header blocks from body chunks where detected.
- Chunked the work according to the source structure: front matter, Chapters 0–7, and Literature as a separate bibliography file.
- Added page anchors in the form `<!-- page: N -->` for later source checking.
- Normalized extracted ASCII laryngeal indices `h1`, `h2`, and `h3` to `h₁`, `h₂`, and `h₃` in the Markdown output.
- Replaced the private-use extracted zero-grade/empty-set glyph U+F0C6 with `∅`.
- Preserved bold/italic spans where detected with HTML `<b>` / `<i>` tags rather than Markdown asterisks, to avoid collision with reconstructed-form asterisks.
- Inserted `[unclear]` in detected internal runs of three or more spaces, which usually indicate missing glyphs in this PDF text layer rather than ordinary spacing.
- Extracted embedded image blocks to `images/` and inserted image references at approximate page locations.

## Unresolved issues

- Detected `[unclear]` markers: approximately 1257. These are not certified one-to-one character counts; they mark likely text-layer gaps.
- Missing-glyph gaps are especially frequent in reconstructed forms, paradigms, matrices, Sanskrit/Vedic forms, and sound-law formulae. The most affected locations include the conventions section on pp. 11–12, the gradation overview on p. 30, heteroclite paradigm examples in Chapter 2, and the sound-law formulations on p. 138.
- The PDF contains custom or non-Unicode font material. Some corrupted glyphs may remain unmarked where the extraction produced plausible but wrong characters instead of spaces.
- Superscript modifier letters, subscript/superscript scientific notation, and some Sanskrit/Indo-Iranian diacritics could not be fully verified visually across the document in this pass.
- Footnotes were retained where the text layer supplied them, but footnote attachment was not manually verified page-by-page.
- Tables and paradigms were preserved in readable line-block form where detected, but not all were converted to Markdown tables because doing so would risk further character loss.

## Confusion-pair report

| Confusion pair | Status in this pass |
|---|---|
| `h₁ h₂ h₃` vs `h1 h2 h3` | ASCII laryngeal indices were normalized to subscript digits. This may over-normalize any literal prose `h1`/`h2`/`h3`, though context suggests these are linguistic laryngeals. |
| Macron vowels | Macrons present in the text layer were retained. Missing macrons caused by font extraction could not be globally detected. |
| Superscript `ʰ ʷ` vs plain `h w` | Not globally resolved. Many extracted forms still use plain `h`/`w` sequences where the source may have superscript modifiers. |
| `ə` vs `e`/`9` | Schwa characters present in the text layer were retained. Corrupted instances could not be fully verified. |
| Underdot characters | Characters present in Unicode output were retained; missing or degraded underdots could not be fully verified. |
| `ǵ ḱ` vs apostrophe forms | Not globally verified; no systematic conversion was applied. |
| Asterisk before reconstructed forms | Asterisks present in the text layer were retained. No global recovery of omitted asterisks was attempted. |
| Dagger `†` | No dagger instances were detected in the extracted Markdown. Absence was not visually verified. |
| Empty set / zero grade | Extracted private-use U+F0C6 was normalized to `∅`. |

## Codepoint inventory

All counts are approximate and intended for cross-pass comparison only.

```json
{
  "laryngeals": {
    "h1": 174,
    "h2": 619,
    "h3": 17
  },
  "macron_a": 10,
  "macron_e": 105,
  "macron_i": 51,
  "macron_o": 437,
  "macron_u": 158,
  "schwa": 81,
  "greek_chars": 1100,
  "combining_diacritics": 56,
  "dagger": 0,
  "unclear_markers": 1257
}
```

## Structural integrity check

- Headings and source page ranges are represented by chunk files and page anchors.
- The bibliography has been separated into its own file as required.
- No index was detected in the source; no index file was produced.
- Embedded images were extracted and referenced, but captions were not present for most image blocks and therefore remain blank in the manifest.
- The output should be treated as a first-pass extraction. A targeted character-fidelity pass is warranted before using the Markdown as a character-authoritative linguistic source.

## Image inventory

| File | Page | Source label | Caption |
|---|---:|---|---|
| `images/klimp-2013-remnants-r-n-stem-p2-fig1.png` | 2 | page 2 image 1 |  |
| `images/klimp-2013-remnants-r-n-stem-p58-fig1.jpeg` | 58 | page 58 image 1 |  |
| `images/klimp-2013-remnants-r-n-stem-p58-fig2.jpeg` | 58 | page 58 image 2 |  |
| `images/klimp-2013-remnants-r-n-stem-p59-fig1.jpeg` | 59 | page 59 image 1 |  |
| `images/klimp-2013-remnants-r-n-stem-p64-fig1.jpeg` | 64 | page 64 image 1 |  |
| `images/klimp-2013-remnants-r-n-stem-p64-fig2.jpeg` | 64 | page 64 image 2 |  |
| `images/klimp-2013-remnants-r-n-stem-p64-fig3.jpeg` | 64 | page 64 image 3 |  |
| `images/klimp-2013-remnants-r-n-stem-p66-fig1.png` | 66 | page 66 image 1 |  |
| `images/klimp-2013-remnants-r-n-stem-p66-fig2.png` | 66 | page 66 image 2 |  |
| `images/klimp-2013-remnants-r-n-stem-p86-fig1.png` | 86 | page 86 image 1 |  |
| `images/klimp-2013-remnants-r-n-stem-p86-fig2.png` | 86 | page 86 image 2 |  |
| `images/klimp-2013-remnants-r-n-stem-p86-fig3.png` | 86 | page 86 image 3 |  |
| `images/klimp-2013-remnants-r-n-stem-p86-fig4.png` | 86 | page 86 image 4 |  |
| `images/klimp-2013-remnants-r-n-stem-p89-fig1.jpeg` | 89 | page 89 image 1 |  |
