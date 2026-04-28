# Extraction notes

## Work completed

This package supersedes the first-pass ZIP. It contains a cleaned third-pass extraction of Michiel de Vaan, “From inflexion to derivation: The PIE word for ‘salt’,” from `vaan-2022.pdf`.

## Second-pass changes

- Restored paragraph boundaries collapsed in the first pass, especially in §§2–7.
- Removed running headers, page numbers, copyright footer, and page-break artifacts.
- Rejoined line-break hyphenations from the PDF text layer.
- Moved the original footnote from the accidental §4 position to the Sanskrit / Indo-Iranian paragraph where the marker occurs.
- Corrected obvious extraction artifacts such as `LIV2` → `LIV²` and Latvian `sā̀ls` spacing.
- Kept the Russian abstract because it is part of the article, not external front matter.

## Third-pass changes

- Reviewed the main reconstructed forms, reflexes, and special characters for consistency against the PDF text layer.
- Added `vaan-2022-proto-forms-index.md`, a structured extraction of the technical forms and reflexes used in the argument.
- Added `vaan-2022-bibliography-normalized.md`, a normalized bibliography derived from the article’s reference list.
- Standardized reference formatting in the main Markdown while preserving the article’s content.

## Remaining caveats

- This is a clean Markdown extraction, not a diplomatic edition. Page layout, lineation, and font styling are intentionally not preserved.
- The PDF is born-digital, so the text layer is generally reliable; however, a fully scholarly critical transcription would still require manual visual proofing of every diacritic and combining mark.
- Proto-form asterisks are preserved raw for corpus/search fidelity. Depending on the Markdown renderer, some forms may display as emphasis unless viewed as source text.
- External bibliographic metadata was not independently checked against library catalogues or publishers; the normalized bibliography is normalized from the article’s own reference list only.

## Further pass recommendation

No additional pass is needed for ordinary corpus use. A fourth pass would only be useful if you want one of the following:

1. a fully diplomatic transcription with page anchors and visual proofing;
2. a CSV/TSV lexical dataset for import into a database;
3. external bibliography verification against catalogues/DOIs;
4. conversion of every proto-form in the main article into Markdown code spans for renderer-safe display.
