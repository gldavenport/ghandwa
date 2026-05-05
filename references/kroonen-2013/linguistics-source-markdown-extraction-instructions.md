# Linguistics Source Markdown Extraction Instructions

Extract this source to clean, corpus-ready Markdown.

## Core requirements

- Produce clean Markdown, not diplomatic transcription.
- Preserve logical structure: title, author/source metadata, sections, subsections, lists, tables where useful, footnotes/endnotes, captions, appendices, bibliography, abbreviation lists, and lexical-entry structure where present.
- Do not preserve physical layout unless it carries meaning. Ignore columns, page geometry, running headers, footers, decorative layout, and ordinary page numbers.
- Preserve page references or page anchors only when useful for citation, lexical lookup, source-critical checking, or later verification.
- Preserve meaningful formatting such as italics, bold, small caps, underlining, quotations, captions, and footnotes/endnotes where they affect interpretation.
- Do not silently correct, modernize, regularize, or normalize source text, spellings, citations, reconstructed forms, language labels, abbreviations, or scholarly notation.
- Maintain character fidelity, especially for diacritics, IPA, reconstructed forms, laryngeals, Greek, special letters, etymological notation, legal numbering, dates, names, and citations.
- Use Unicode characters directly where possible rather than ASCII substitutes.
- Add YAML front matter with source title, author/creator if available, date/year if available, source type, extraction date, extraction method if known, pass status, and notes.
- Use readable headings and consistent Markdown structure even when the source is visually irregular.
- If charts, images, maps, diagrams, or photo-only pages appear, include accessible descriptions rather than interpretive summaries.
- If text is unreadable or uncertain, mark it clearly with `[unclear]`, `[unclear: possible reading]`, or a short note rather than silently guessing.
- Do not summarize unless explicitly asked; transcribe/extract the source text.

## Linguistics-specific requirements

- Prioritize character fidelity for reconstructed forms, asterisks, laryngeals, accents, length marks, Greek, IPA, Gothic, Old Irish, Old Norse, Sanskrit, Latin, Proto-Celtic, Proto-Germanic, PIE, and other special characters or scholarly notation.
- Do not normalize away technical notation, phonological symbols, accent marks, vowel length, root notation, inflectional labels, grammatical abbreviations, source sigla, or etymological conventions.
- Preserve bibliography, footnotes/endnotes, abbreviation lists, source citations, cross-references, language labels, and lexical-entry structure where present.
- For etymological dictionaries or lexical studies, preserve headwords, reconstructed forms, glosses, language labels, derivational notes, cognate sets, semantic groupings, and references with special care.
- Keep source text and editorial notes clearly distinct.
- For OCR-heavy or visually complex sources, verify uncertain forms against the page image; when extracted text conflicts with the page image, the page image controls.
- If useful, create a structured lexical dataset or extracted-form list as a companion file or clearly separate section. Do not let the dataset replace or distort the main readable Markdown extraction.
- Prefer clean readable Markdown, but do not simplify technical notation.

## After the first extraction

Assess whether a second or third pass is needed.

## Second-pass criteria

- Check OCR or extraction errors.
- Fix broken headings, paragraph joins, list structure, tables, footnotes, captions, appendices, and obvious column-order problems.
- Verify names, dates, titles, language labels, reconstructed forms, citations, bibliographic entries, repeated headings, and cross-references.
- Normalize obvious Markdown inconsistencies.
- Confirm that clean Markdown structure has not erased meaningful linguistic or source-critical distinctions.

## Third-pass criteria

- Use when the document has high character-fidelity needs, complex OCR, dense bibliography, linguistic forms, tables, lexical entries, or source-critical value.
- Verify special characters, reconstructed forms, IPA, Greek, diacritics, citations, bibliography, tables, abbreviation lists, and uncertain readings.
- Spot-check dense linguistic passages against page images where available.
- Produce a short note saying whether further passes would add meaningful value.

## Optional additional passes

### Bibliography normalization pass

Preserve the original bibliography in the main Markdown, and optionally add a normalized bibliography as a companion file or separate section.

### Lexical dataset pass

Extract headwords, forms, glosses, language labels, roots, cognates, and citations into a companion Markdown table or CSV-style file when useful.

### Character audit pass

Focus only on reconstructed forms, non-ASCII characters, Greek, IPA, laryngeals, diacritics, and uncertain OCR.

## Deliverables

- Markdown file(s) using kebab-case filenames.
- One source/PDF should normally produce its own Markdown file and associated companion files.
- Include an index or README if multiple files are produced.
- Package final files in a ZIP when appropriate.
