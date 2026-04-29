# anthony-2013 Markdown extraction

## Source

- `anthony-2013.pdf`
- David W. Anthony, “Two IE phylogenies, three PIE migrations, and four kinds of steppe pastoralism,” *Journal of Language Relationship / Вопросы языкового родства* 9 (2013), pp. 1–21.

## Files

- `anthony-2013.md` — clean, corpus-ready Markdown extraction.
- `README.md` — this extraction note.

## Passes completed

### First pass: structural extraction

The article was converted into clean Markdown with YAML front matter, title/author/source metadata, abstract, keywords, logical section headings, numbered migration/pastoralism subsections, figure captions, bibliography, and Russian abstract.

### Second pass: cleanup and structure

Completed. This pass removed obvious line-break and soft-hyphen artifacts, joined paragraphs, normalized heading hierarchy, removed running headers/page numbers from the reading text, and preserved page references as silent HTML comments.

### Third pass: character, figure, and bibliography audit

Completed. This pass focused on non-ASCII characters, names with diacritics, Russian text, German terms, reconstructed forms, isotope notation, figure captions, and bibliography continuity. Figure descriptions were added as bracketed editorial notes for corpus/accessibility use.

## Additional pass assessment

A fourth full pass is not necessary for ordinary corpus research. The article is not a lexical dictionary and does not need a structured lexical dataset. A future high-fidelity page-image proofread could still be useful if the goal is publication-quality correction of every bibliographic and reconstructed-form character. The highest-risk item is the reconstructed axle root rendered as `*haeǩs-`; it is preserved from the parsed source rather than silently normalized.

## Editorial policy

- Clean Markdown, not diplomatic transcription.
- Physical layout, running headers, and ordinary page numbers are not preserved.
- Source wording is preserved rather than modernized or rewritten.
- Editorial figure descriptions are clearly bracketed.
- Book and journal titles in the bibliography have been lightly italicized for Markdown readability; this is formatting, not content normalization.
