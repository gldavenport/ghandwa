---
title: "Night-mare: on the origin of a trope in Celtic and Germanic (a response to Stephen Pax Leonard)"
author: "Tatyana A. Mikhailova"
date: 2021
source_type: born-digital
extraction_date: 2026-05-08
source_file: mikhailova-2021-night-mare.pdf
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF. A machine-readable text layer is present. The raw text layer was used as the primary input, with rendered page images used only for high-risk character checks and corrupted glyph resolution.

## Corrections applied

- Removed running headers, footers, and page numbers.
- Rejoined paragraphs and repaired line-break hyphenation across page and line boundaries.
- Mapped the single private-use glyph `U+EE77` in `*h₁ék’ṷo-` to `ṷ` after comparison with the page rendering and with the later text-layer occurrence of the same form.
- Corrected the Greek article sequence emitted as `τϖν Κελτϖν` to `τῶν Κελτῶν` after visual/contextual check of the Pausanias quotation.
- Normalized extracted laryngeal ASCII `h1` to `h₁` in PIE forms where the source rendering uses a lowered/subscript-style index.
- Moved the single footnote into Markdown footnote syntax and kept it attached to the relevant sentence.
- Split the bibliography into a separate Markdown file.

## Unresolved-issues list

- No `[unclear]` markers were inserted.
- The exact source encoding of the laryngeal index is not fully recoverable from the text layer: `h1` is emitted in the raw extraction, while visual rendering shows a lowered/subscript-style `1`. The output uses `h₁` for corpus consistency under the project’s laryngeal-fidelity rule.
- Formatting fidelity is approximate. Italics in the PDF are not exhaustively preserved for every individual cited form; the extraction prioritizes character fidelity and logical structure.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: raw text emitted `h1`; output uses `h₁` in PIE laryngeal forms. No `h2` or `h3` instances were found.
- Macron vowels: precomposed macron vowels were preserved where present in the text layer.
- Superscript modifier letters `ʰ`, `ʷ`: `ʷ` was preserved in `*ekʷos` / `*ekʷo-`; no `ʰ` instances were found.
- Schwa `ə`: preserved in `*ək’ú`.
- Underdot letters: none of `ṛ ḷ ṃ ṇ` found.
- Acute consonants `ǵ ḱ`: none found.
- Asterisk before reconstructed forms: preserved where present in the text layer.
- Dagger `†`: no dagger instances found.
- Source-specific issue: `ṷ` appeared once as a private-use glyph in the raw extraction and once correctly as `ṷ`; both output instances use `ṷ`.
- Greek omega-with-circumflex in `τῶν Κελτῶν`: the raw text layer emitted `τϖν Κελτϖν`; visual/contextual checking supports `τῶν Κελτῶν`, which is used in the output.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 4,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 4,
  "macron_e": 0,
  "macron_i": 2,
  "macron_o": 1,
  "macron_u": 1,
  "schwa": 1,
  "greek_chars": 52,
  "combining_diacritics": 1,
  "dagger": 0
}
```

## Structural integrity check

- Headings were normalized to Markdown levels while preserving the source’s section sequence.
- The bibliography is separate from the main text.
- No index was present.
- No figures, maps, plates, or image-rendered tables were identified in the PDF.
- Block quotations were retained as Markdown block quotes.
- The single footnote was retained as a Markdown footnote.

## Image inventory

No extractable figures, maps, plates, diagrams, or image-rendered tables were identified. No `images/` directory was produced.
