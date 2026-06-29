---
title: "A Comparative Grammar of the Early Germanic Languages — extraction report"
author: "R.D. Fulk"
date: "2018"
source_type: "born-digital PDF"
extraction_date: "2026-05-23"
source_file: "fulk-2008-comparative-grammar-early-germanic.pdf"
chunk: "extraction report"
---

# Extraction report

## Source assessment

- **Source type:** born-digital PDF with an embedded text layer.
- **Length:** 438 PDF pages. The main printed pagination runs from page 1 on PDF page 18 through page 420 on PDF page 437.
- **Layout:** mostly single-column scholarly prose, with footnotes, paradigms/tables, figures, references, and an Index verborum.
- **High-risk zones:** reconstructed forms, Greek, Gothic/runic material, special Germanic characters, paradigms, references, index entries, and inline image glyphs.

## Character-risk assessment

The text layer is usable for ordinary prose but is not character-authoritative. Visual sampling confirmed a source-specific custom-glyph problem: common ligatures and one runological symbol extract as currency signs. A glyph map was applied globally.

### Source-specific glyph/confusion map applied

- `₠` → `fi`
- `₡` → `fl`
- `₢` → `ffi`
- `₦` → `ff`
- `₥` → `ffl`
- `₩` → `fj`
- `₨` → `ʀ`

## Structural work performed

- Removed running headers, page numbers, horizontal rules, and repeated page furniture.
- Split the book into front matter, chapter files, references, Index verborum, back cover, audit file, and this report.
- Added concise YAML front matter to each Markdown file.
- Repaired obvious hard line wrapping and many soft line-break hyphenations.
- Converted chapter/section labels to Markdown headings where the text-layer structure made this reliable.
- Preserved references and index as separate files.

## Inline image glyphs and figures

The PDF contains 2808 small inline image blocks across 289 pages. These are usually special glyphs, formulas, or small character clusters that are visible in the rendered PDF but absent from the text layer. They were audited but not globally OCR-resolved in this pass because automated OCR would not be character-authoritative for dense linguistic notation. See `fulk-2008-comparative-grammar-early-germanic-inline-image-glyph-audit.md`.

The PDF also contains 20 larger image/figure blocks, including visual figures. Captions present in the text layer were retained where extracted.

## QC checks performed

- Custom corrupted ligature/currency-glyph sweep.
- Replacement-character search.
- Control-character search.
- ASCII `h1`, `h2`, `h3` laryngeal-pattern search.
- Basic chunk/manifest check.
- Visual spot checks on pages with known custom glyphs and paradigms.

## QC results

```json
{
  "replacement_character": 0,
  "unresolved_unclear": 0,
  "custom_currency_glyphs_remaining": {
    "₠": 1,
    "₡": 1,
    "₢": 1,
    "₦": 1,
    "₥": 1,
    "₩": 1,
    "₨": 1
  },
  "h1_h2_h3_ascii_laryngeals": 146,
  "control_chars": 0,
  "files": {
    "fulk-2008-comparative-grammar-early-germanic-back-cover.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 0,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch1-introduction.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 14,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch10-numerals.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 4,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch11-adverbs-prepositions-conjunctions.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 0,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch12-verbs.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 28,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch2-prosodic-features-syllable.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 2,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch3-vowels-pie-proto-germanic.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 1,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch4-stressed-vowels-germanic.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 6,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch5-vowels-lesser-stress.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 2,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch6-consonants.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 19,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch7-nouns.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 14,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch8-pronouns.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 13,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-ch9-adjectives.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 3,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-front-matter.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 4,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-index-verborum.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 25,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-inline-image-glyph-audit.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {
        "₠": 1,
        "₡": 1,
        "₢": 1,
        "₦": 1,
        "₥": 1,
        "₩": 1,
        "₨": 1
      },
      "ascii_h_laryngeals": 0,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-part-phonology.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 0,
      "control_chars": 0
    },
    "fulk-2008-comparative-grammar-early-germanic-references.md": {
      "replacement_character": 0,
      "unclear": 0,
      "custom_currency_glyphs_remaining": {},
      "ascii_h_laryngeals": 11,
      "control_chars": 0
    }
  }
}
```

## Unresolved issues

- Inline image glyph/formula blocks were not globally resolved. The main Markdown is suitable for corpus search and general reference, but not character-authoritative for every reconstructed form.
- Some paradigms/tables retain text-layer ordering rather than fully reconstructed Markdown tables.
- Footnotes are preserved, but note placement remains page-local rather than fully normalized to endnotes.
- The uploaded filename says `fulk-2008`, but the source itself is the 2018 John Benjamins book. The output preserves the uploaded source filename in filenames and YAML while recording the source date as 2018.

## Further-pass recommendation

A second pass would add meaningful value if this extraction will be used for quotation, derivation, or form-level linguistic work. Recommended targeted passes:

1. Resolve inline image glyph/formula blocks page by page, prioritizing chapters 3–6, 10, 12, and the Index verborum.
2. Reconstruct major paradigms into Markdown tables.
3. Run a dedicated Greek/Gothic/runic and laryngeal fidelity pass against rendered pages.
4. Run an index fidelity pass, because the Index verborum is especially dense and contains many inline image glyphs.

## Completion status

This is a clean first-pass corpus Markdown package. It is readable and searchable, with major custom text-layer corruptions repaired. It should not be treated as quote-authoritative for dense linguistic forms until the relevant passage has been checked against the rendered PDF.
