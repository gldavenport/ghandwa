# Extraction Notes

## Source

- Title: The Art of Language Invention
- Creator: David J. Peterson
- Publisher: Penguin Publishing Group
- Date: 2015-09-09
- Source file: `annas-arch-c68506642ad3.epub`
- Source type: EPUB

## Passes Performed

1. **First pass:** Converted the EPUB spine to Markdown with media extraction.
2. **Second pass:** Removed ebook/page-layout artifacts, normalized headings, merged chapter-number/title pairs, inserted front-matter headings, cleaned duplicate cover/title-page image handling, and normalized Markdown image alt text.
3. **Third pass:** Checked character-fidelity samples, residual raw HTML/page-break artifacts, image-link counts, chapter/section heading structure, and special-character preservation.
4. **Targeted repair after QA:** Removed stale internal EPUB anchor links, cleaned the generated contents section, verified linked media, and re-ran artifact checks.

## QA Summary

- Markdown lines: 4855
- Image links in Markdown: 705
- Unique linked image files: 712
- Extracted media files copied: 712
- Linked images missing from media folder: 0
- Raw span tags remaining: 0
- Raw div tags remaining: 0
- Page-break/ebook-anchor markers remaining in body: 0
- Blank image-alt links remaining: 0
- Special-character sample misses: none
- Headings: 73
- Residual markup/artifact patterns: none

## Remaining Limitations

- The EPUB contains many embedded images for writing systems, glyphs, diagrams, and source tables. These were retained as linked media and given generated alt text when the EPUB did not provide alt text.
- No OCR was run on uncaptioned image-only tables or glyph samples; doing so would be high-risk for conlang scripts and would likely introduce false text.
- A further automated pass would probably not add meaningful value unless the goal changes to manual image-by-image description or OCR-backed table reconstruction.
