# Ringe 2017 Index Structured Extraction Report

Source Markdown: `ringe-2017-index-first-pass.md`

Total parsed index rows: **4802**

## Columns

- `section`: top-level index division.
- `subsection`: second-level index division.
- `group`: third-level language/proto-language group where present.
- `entry`: headword or leading form before the first page reference.
- `page_refs`: semicolon-separated page-reference tokens detected in the full raw entry.
- `notes`: full entry text beginning with the first detected page reference; retains subforms, labels, and internal references.
- `raw_entry`: full reconstructed index entry as parsed from the Markdown source.
- `source_line_start`, `source_line_end`: source Markdown line span used for the parsed entry.

## Parsing notes

This is a structured navigation/search table, not a fully diplomatic index database. Wrapped index lines were joined heuristically. The `raw_entry` column is intentionally preserved so that page references and subforms can be rechecked against the Markdown/PDF when needed. For formal citation or sensitive morphology, verify the relevant entry against the PDF.

## Row counts by section/subsection/group

- I. Protoforms > A. Proto-Indo-European: 737
- I. Protoforms > B. Daughters of PIE > 1. Proto-Germanic: 851
- I. Protoforms > B. Daughters of PIE > 2. Proto-Northwest Germanic: 23
- I. Protoforms > B. Daughters of PIE > 3. Proto-West Germanic: 23
- I. Protoforms > B. Daughters of PIE > 4. Other daughters of PIE: 21
- II. Attested forms and immediate preforms > A. Germanic languages > 1. Gothic: 562
- II. Attested forms and immediate preforms > A. Germanic languages > 2. Old Norse: 404
- II. Attested forms and immediate preforms > A. Germanic languages > 3. Old English: 570
- II. Attested forms and immediate preforms > A. Germanic languages > 4. Old Frisian: 22
- II. Attested forms and immediate preforms > A. Germanic languages > 5. Old Saxon: 43
- II. Attested forms and immediate preforms > A. Germanic languages > 6. Old High German: 411
- II. Attested forms and immediate preforms > A. Germanic languages > 7. Other Germanic languages: 11
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 1. Anatolian languages: 87
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 2. Baltic languages: 78
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 3. Celtic languages: 86
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 4. Greek: 245
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 5. Iranian languages: 38
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 6. Italic languages other than Latin: 17
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 7. Latin: 245
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 8. Sanskrit and Middle Indic: 230
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 9. Slavic languages: 44
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 10. Tocharian languages: 46
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 11. Other Indo-European languages: 4
- II. Attested forms and immediate preforms > B. Non-Germanic languages > 12. Finnish (Uralic family): 4

## Skipped/non-entry lines

Likely introductory/prose lines skipped: **56**.
