---
title: An outline of Celtiberian grammar — extraction report
author: D.S. Wodtko
date: 2003
source_type: born-digital
extraction_date: 2026-05-07
source_file: wodtko-2003-outline-celtiberian-grammar.pdf
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The text layer is present but partially damaged by non-Unicode embedded/custom font encodings. Visual rendering was used selectively to identify recurring character mappings, especially Celtiberian `đ`, long vowels, semivowels, and a subset of PIE notation.

## Corrections applied

- Repaired recurring custom-font Caesar-shifted Celtiberian/Latin-form runs such as `WLđDWXđ` → `tiđatuđ`, `VODQLDđ` → `slaniađ`, `XHLđRV` → `ueiđos`, and similar forms.
- Normalized recurring custom-font long-vowel glyphs to `ā ē ī ō ū`.
- Converted recurring semivowel glyphs to `i̯` and `u̯`.
- Converted recurring laryngeal strings `h1 h2 h3` to `h₁ h₂ h₃` where they were represented as ordinary text.
- Replaced residual C0 control characters from unrecoverable custom-font fragments with `[unclear]`.
- Repaired common line-break hyphenation when a word was visibly split at the line boundary.
- Removed running page-number-only lines.
- Separated the bibliographical abbreviations and other abbreviation list into `wodtko-2003-outline-celtiberian-grammar-bibliography.md`.

## Unresolved issues

- The PDF has no usable Unicode mapping for several embedded fonts. Some Greek quotations, Greek cognates, and highly compressed PIE reconstructions remain in damaged transliteration-like form or contain `[unclear]` markers.
- Greek-font passages such as `C5KWRJ{QKM, G²WZ, T{WZ, G{ND, SU², ¸S{U, T{VVDVTD, SRT{Z` require a dedicated visual/Greek pass.
- Several PIE roots and reconstructed forms that use old custom font glyphs were only partially recoverable. These should be treated as review targets rather than authoritative forms.
- Dense tables were preserved in line-based layout rather than fully normalized Markdown tables because the source text layer interleaves ordinary text, superscripts, and custom glyph fonts inconsistently.
- Some abbreviations and author names in the bibliography may retain original capitalization or accent inconsistencies from the PDF text layer.

## Confusion-pair report

- `h₁ h₂ h₃`: normalized where ordinary `h1 h2 h3` strings were detected. Instances embedded in corrupted glyph runs could not all be verified.
- `ā ē ī ō ū`: recurring custom-font long-vowel glyphs were mapped. Some long vowels embedded in unrecovered Greek or PIE strings may remain unverified.
- `ʰ ʷ`: recurring aspiration marker `#` was mapped to `ʰ` in many contexts. Superscript `ʷ` was only partially recoverable; some labiovelar notation remains suspect.
- `ə`: no reliable source-layer inventory; not verified.
- `ṛ ḷ ṃ ṇ`: syllabic sonants were partly mapped as `m̥ n̥ r̥ l̥`; underdot Indo-Aryan-style characters were not fully verified.
- `ǵ ḱ`: `ǵ` was mapped where the custom glyph was identifiable. `ḱ` remains uncertain in several PIE-table and root contexts.
- `*`: asterisks were preserved where represented in text.
- `†`: no dagger instances verified in the cleaned text.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "laryngeals": {
    "h1": 8,
    "h2": 37,
    "h3": 6
  },
  "macron_a": 60,
  "macron_e": 23,
  "macron_i": 19,
  "macron_o": 45,
  "macron_u": 10,
  "schwa": 0,
  "greek_chars": 0,
  "combining_diacritics": 85,
  "dagger": 1
}
```

## Structural integrity check

- Logical section headings are present for title, contents, introduction, phonology, morphology, word formation, lexicon, and abbreviations.
- Footnotes are retained inline near the source page location, but not normalized into Markdown footnote syntax.
- Paradigms and sound-system lists are retained as line-based tables. They are usable for reference but should receive a dedicated table pass if database-like structure is desired.
- No figures, maps, or plates were detected.
- The extraction is serviceable for search and reading, but not character-authoritative for Greek and the densest PIE notation.

## Image inventory

No extracted images.
