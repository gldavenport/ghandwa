# Ringe 2017 Index - First-Pass Extraction Report

Generated: 2026-04-27T20:59:42Z

## Source range

- Printed pages: 348-406
- PDF pages: 359-417
- Extraction source: born-digital text layer via `pdftotext -raw`

## Purpose

This pass was prepared because the index is especially useful for comparative work and conlang construction: it clusters PIE protoforms, daughter-language reconstructions, attested Germanic forms, and non-Germanic comparanda with page references.

## Main cleanup performed

- Normalized OUP private-use numeral glyphs to ordinary digits.
- Expanded `fi`/`fl` ligatures where the PDF text layer used typographic ligatures.
- Removed running page headers/footers.
- Converted major index divisions to Markdown headings.
- Normalized PIE index entries to stable Unicode notation where practical:
  - `h1 h2 h3` -> `h₁ h₂ h₃`
  - `ḱ ǵ` -> `ḱ ǵ`
  - PIE `kw gw gwh` -> `kʷ gʷ gʷʰ`
  - PIE `bh dh gh` -> `bʰ dʰ gʰ`
- Preserved Germanic-stage `kw/gw/hw` notation in the Proto-Germanic and attested Germanic sections.

## Known limitations

- This is a line-oriented index extraction, not a fully reflowed or database-normalized index.
- Long entries that wrap across lines remain wrapped.
- Some superscript/diacritic extraction artifacts may remain, especially in dense protoform entries.
- Page references have been normalized to ordinary numerals but not validated entry-by-entry.
- The index is best treated as a search aid and navigation layer, not as a diplomatic edition.

## Suggested later improvements

- Build a TSV/CSV version with columns: section, subsection, entry, page_refs, notes.
- Create separate filtered indexes for PIE roots/forms, PGmc forms, Gothic forms, Old English forms, and non-Germanic comparanda.
- Spot-check high-value entries against the PDF before using them in formal linguistic argumentation.
