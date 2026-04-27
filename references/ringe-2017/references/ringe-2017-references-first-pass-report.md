# Ringe 2017 References: first-pass extraction report

## Source

- Source file: `ringe-pie-to-proto-germanic-2nd-ed.pdf`
- Section: References
- Printed pages: 331-347
- PDF pages: 342-358
- Extraction method: born-digital PDF text extraction via `pdftotext -layout`, followed by cleanup.

## Output files

- `ringe-2017-references-first-pass.md`
- `ringe-2017-references-structured.csv`
- `ringe-2017-references-structured.tsv`

## Result

- Parsed bibliography entries: 339
- Page anchors inserted in Markdown: yes
- Structured rows exported: 339

## Cleanup applied

- Normalized private-use numeral glyphs to ordinary Arabic numerals.
- Expanded common ligatures: `ﬁ`, `ﬂ`, `ﬀ`, `ﬃ`, `ﬄ`.
- Reflowed hanging-indent bibliography entries into one paragraph per entry.
- Removed page headers and page-number artifacts.
- Repaired common line-break hyphenation in wrapped entries.
- Applied limited notation cleanup where it clearly reflected the source typography, including `H₂O`, `h₂e-conjugation`, and selected `gʷ`/`gʷʰ` title forms.

## Limitations

This is a cleaned bibliography extraction, not a manually verified bibliographic edition. It should be reliable for search, navigation, and corpus work, but individual entries should be checked against the PDF before formal citation. The most likely residual issues are line-break hyphenation in foreign-language titles and unusual typographic symbols in article titles.

## Entry count by printed page

| Printed page | Entries starting on page |
|---:|---:|
| 331 | 22 |
| 332 | 29 |
| 333 | 20 |
| 334 | 22 |
| 335 | 23 |
| 336 | 21 |
| 337 | 14 |
| 338 | 26 |
| 339 | 19 |
| 340 | 14 |
| 341 | 23 |
| 342 | 20 |
| 343 | 20 |
| 344 | 12 |
| 345 | 22 |
| 346 | 24 |
| 347 | 8 |
