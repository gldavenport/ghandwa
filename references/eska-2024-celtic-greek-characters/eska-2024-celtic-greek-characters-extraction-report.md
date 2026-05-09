---
title: "Celtic in Greek characters and implications for Greek and Celtic phonology"
author: "Joseph F. Eska"
date: "2024"
source_type: born-digital
extraction_date: "2026-05-08"
source_file: "eska-2024-celtic-greek-characters.pdf"
chunk: extraction-report
---

# Extraction report

## Source identification

- Source file: `eska-2024-celtic-greek-characters.pdf`
- Source type: born-digital PDF with machine-readable text layer.
- Pages: 14.
- Output mode: single journal-article Markdown file plus separate bibliography.
- Images/figures: none identified. Source tables were text-based and reconstructed as Markdown tables.

## Corrections applied

- Rejoined line-break hyphenation and page-boundary splits in prose and bibliography entries.
- Removed running headers, page numbers, page ornaments, and physical lineation.
- Reconstructed logical headings, numbered examples, footnotes, three source tables, abbreviation list, and bibliography as Markdown.
- Converted source superscript-span aspirate notation in Greek-letter names and phonological notation to Unicode modifier-letter notation where available: `pʰ`, `tʰ`, `kʰ`, `kʷ`, `kʷʰ`, `ɡʲ`, `ɡʷ`, `tˢ`, and `t˗ˢ`.
- Preserved source Greek inscriptional characters, including `ϵ`, `C`, underdots, restored brackets, tie-bars, and pipe line-break markers.
- Split bibliography into `eska-2024-celtic-greek-characters-bibliography.md` per project instructions.

## Unresolved issues list

- Table 2 contains a footnote marker `3` after `[ʦʰɛnɐ]`; no corresponding footnote text was present in the supplied PDF pages. A footnote entry was added noting absence of source text rather than guessing.
- Superscript-style `ɦ` in the proto-IE voiced aspirate series was preserved as ordinary `ɦ` following the PDF text layer rather than forced into rare/nonstandard modifier-letter codepoints.
- List item (15e) appears in the text layer as `s`; visual inspection suggests the typography may imply a low marking, but no combining mark was exposed by the text layer. The output keeps `s`.
- Footnote 14 preserves the source’s nested quotation/punctuation structure around `‘qui-voit-loin’`; quote nesting may require human review against the publisher version.
- Source uses mixed epigraphic notation, including Latin `C` in Greek-character forms. These were preserved where exposed by the text layer; no normalization to Greek sigma was applied.

## Confusion-pair report

- `h₁ h₂ h₃`: no laryngeal-index forms identified in the output; none verified beyond text-layer search.
- Macron vowels `ā ē ī ō ū`: macron vowels were preserved where identified, especially `longā-`; no full guarantee against dropped macrons in references.
- Superscript modifier letters `ʰ ʷ`: common aspirate and labiovelar superscripts were converted from raised PDF spans and visually spot-checked on pages 1–5 and 10.
- `ə`: not identified in the output.
- Underdot characters such as `ṛ ḷ ṃ ṇ`: no Indic-style underdot letters identified; combining underdots in epigraphic Greek forms were preserved.
- `ǵ ḱ`: not identified in the output.
- Asterisk `*`: reconstructed forms retain `*` where identified.
- Dagger `†`: not identified in the output.
- Source-specific high-risk symbols checked: `ɡ`, `ɸ`, `ʦ`, `θ͇`, `t̜`, `t̞`, `ṱ`, `θ̱`, `⁀`, `∅`, `ϵ`, and epigraphic underdots. These were preserved where located, but not certified exhaustively.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 1,
  "macron_e": 2,
  "macron_i": 0,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 1,
  "greek_chars": 428,
  "combining_diacritics": 42,
  "dagger": 0
}
```

## Structural integrity check

- Main headings and subsections are represented consistently.
- Footnotes are moved to a final `Footnotes` section and attached using Markdown references.
- Tables 1–3 are reconstructed as Markdown tables.
- Numbered examples (1)–(16) are preserved as structured lists/blocks.
- Bibliography is separate and alphabetic order is preserved.
- No figures, maps, plates, or image-only tables were detected.
- No `[unclear]` or `[?]` markers were inserted in the clean text; uncertainties are recorded only here.

## Image inventory

No images were extracted; no `[image-only...]` fallback placeholders were used.
