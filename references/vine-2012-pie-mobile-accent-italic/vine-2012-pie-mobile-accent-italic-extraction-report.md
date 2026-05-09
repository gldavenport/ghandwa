---
title: "Extraction report — PIE mobile accent in Italic: Further evidence"
author: "Brent Vine"
date: 2012
source_type: born-digital
extraction_date: 2026-05-07
source_file: "vine-2012-pie-mobile-accent-italic.pdf"
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The text layer was used as the primary input. Rendered page images were consulted for corrupted control-code glyphs and source-specific high-risk forms.

## Corrections applied

- Rejoined wrapped paragraphs and repaired obvious line-break hyphenation introduced by PDF extraction.
- Removed running page headers and page numbers from the article and bibliography text.
- Split the bibliography into `vine-2012-pie-mobile-accent-italic-bibliography.md`.
- Repaired ligatures: `ﬁ` → `fi`, `ﬂ` → `fl`.
- Applied source-specific glyph repairs after visual checks: control codes for `u̯`, `i̯`, `ʷ`, `ʰ`, syllabic-ring notation, `ḱ`, and `n̥`.
- Normalized laryngeal indices from `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃`.
- Repaired source-specific malformed syllabic-resonant forms: `CR̥HC`, `CŔ̥HC`, `*pl̥h₂-`.
- Moved footnote text into a final Notes section rather than leaving it at page bottoms.

## Unresolved-issues list

- The PDF text layer uses custom-font control codes for several linguistic glyphs. Major mappings were visually checked, but isolated reconstructed forms involving labialized/palatalized consonants may still warrant a second visual pass against rendered pages.
- Footnote reference markers in the running text were not globally converted to Markdown `[^n]` links; the note texts are preserved in a final Notes section.
- Some paragraph boundaries within long page blocks may reflect extraction-block boundaries rather than the source’s full paragraph logic.
- Greek theta appears as `ϑ` in the extracted text layer and rendered glyphs; it has been preserved rather than normalized to `θ`.
- The first two PDF pages are book-level title/copyright metadata. The corpus file focuses on the article/chapter text; publication metadata is represented in YAML and manifest.

## Confusion-pair report

- `h₁ h₂ h₃`: ASCII laryngeal indices were normalized globally where rendered by the text layer as `h1`, `h2`, `h3`. Residual false positives cannot be ruled out without a full visual pass.
- Macron vowels: macron characters are present in body and bibliography. No full visual verification of every macron was performed.
- `ʰ ʷ`: source-specific control codes were mapped to superscript modifier letters; contexts with labialized consonants were spot-checked visually.
- `ə`: no schwa was found in the output.
- Underdot / syllabic markers: `ṛ`, `ṇ`, and ring-below notation were preserved or repaired where detected. Dense forms may benefit from another character-fidelity pass.
- `ǵ ḱ`: `ḱ` was restored from a text-layer control code. No `ǵ` was detected.
- `*`: asterisks before reconstructed forms were retained. No attempt was made to certify every reconstructed-form boundary.
- `†`: no dagger was found in the output.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 29,
    "h2": 23,
    "h3": 0
  },
  "macron_a": 36,
  "macron_e": 20,
  "macron_i": 161,
  "macron_o": 65,
  "macron_u": 7,
  "schwa": 0,
  "greek_chars": 284,
  "combining_diacritics": 267,
  "dagger": 0
}
```

## Structural integrity check

- Main title, abstract, numbered sections, and numbered subsections were converted to Markdown headings.
- Bibliography is separate; entries are separated where detectable from source entry starts.
- Notes are preserved in a final Notes section.
- No images, figures, maps, plates, or rendered tables were detected in the source.
- Page anchors were retained as HTML comments for source-critical checking.
- No replacement-character or unhandled low-control-code residue was found in the final output: `none detected`.

## Image inventory

No images detected.
