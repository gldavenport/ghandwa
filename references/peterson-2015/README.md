# The Art of Language Invention — Markdown Extraction

This package contains a clean Markdown extraction of David J. Peterson, *The Art of Language Invention*, from the uploaded EPUB source.

## Files

- `the-art-of-language-invention.md` — main corpus-ready Markdown extraction with YAML front matter.
- `media/` — extracted EPUB images referenced from the Markdown.
- `image-inventory.tsv` — inventory of image links, dimensions, generated alt descriptions, source XHTML file, and nearby context.
- `extraction-notes.md` — pass log, QA checks, and limitations.

## Extraction Notes

The EPUB text was born-digital. The extraction removes pagebreaks, anchors, columns/layout artifacts, and decorative ebook structure. Images are retained rather than OCRed. Generated descriptions are intentionally conservative where the EPUB lacks alt text.
