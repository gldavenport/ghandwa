# Orel 2003 — A Handbook of Germanic Etymology — Markdown Extraction

Source: Vladimir Orel, *A Handbook of Germanic Etymology*. Brill, 2003.

## Files

- `orel-2003-handbook-germanic-etymology-front-matter.md`
- `orel-2003-handbook-germanic-etymology-references.md`
- `orel-2003-handbook-germanic-etymology-abbreviations.md`
- `orel-2003-handbook-germanic-etymology-dictionary.md`
- `orel-2003-handbook-germanic-etymology-indices.md`
- `orel-2003-handbook-germanic-etymology-lexical-entries.md`
- `orel-2003-handbook-germanic-etymology-lexical-entries.tsv`

## Extraction passes completed

### First pass

Extracted embedded PDF text and used PDF text-block coordinates to decolumnize the dictionary and indices. Physical layout, page geometry, running heads, and page numbers were not retained.

### Second pass

Repaired obvious Markdown structure: section files, YAML front matter, dictionary entries as headings, abbreviation tables, index tables, lexical-entry TSV, split entry-label repair, and basic line-wrap/dehyphenation cleanup.

### Third pass

Applied a targeted character-fidelity cleanup for this PDF's embedded-font artifacts: small-cap private-use glyphs, oldstyle digits, ligatures, `đ`, `z`, `ƕ`, `ǫ`, `æ`, and common Orel long-vowel placeholders (`ā`, `ē`, `ī`, `ō`, `ū`) in dictionary/index text.

## Remaining caveat

A further pass would add meaningful value only if it were page-image/manual verification rather than another automated embedded-text pass. The PDF's embedded text does not reliably encode every source glyph. In particular, polytonic Greek, some Baltic/Slavic special letters, and some overprinted macrons are not consistently recoverable from the embedded text layer alone. The files mark no readings as `[unclear]` unless the extraction was structurally incomplete; uncertain special-character fidelity should be checked against the PDF image when source-critical.


## Character-fidelity fourth pass

This package includes an additional character-context pass after the first three extraction passes. The fourth pass used the PDF's font-span context to convert KadmosNieuw Greek-font spans from keyboard-encoded extraction text into Unicode Greek wherever the span contained distinctive Greek-font characters. It also applied a small curated correction list for recurring Polish, Slavic, Baltic, Romanian, and bibliographic-name artifacts whose context was clear.

Remaining caveat: a few extremely short Greek-font spans made only of ordinary ASCII letters, and a few ambiguous scholarly transliteration signs, may still require page-image verification if the file is used for source-critical philology. For corpus search and general lexical research, this version should be materially better than the previous package.


## Character-fidelity fifth pass

This package includes an additional conservative verification pass after the fourth character-context pass. The fifth pass targeted the specific remaining issues identified in the previous notes: short Greek-font spans, page-verified KadmosNieuw signs, Slavic hard/soft signs, and context-clear Sanskrit, Tocharian, Baltic, and Slavic legacy-font artifacts.

The pass deliberately avoided broad conversion of ordinary ASCII sequences inside Greek-font contexts, because that can corrupt English and German prose. Corrections were applied only when page-image verification or linguistic/source-language context made the value clear.
