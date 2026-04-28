# Extraction Notes: Mars Veneticus and the “Palma Rule”

- Original PDF: `prósper-mars-veneticus.pdf`
- Markdown: `prosper-mars-veneticus.md`
- Companion form list: `prosper-mars-veneticus-forms.tsv`
- Pages in source PDF: 12
- Article/body extraction began at PDF page: 1
- Text blocks processed: 86
- Blocks dropped as running headers/footers/layout noise: 12
- Markdown paragraph/block count: 72

## Pass assessment

### First pass
Extracted embedded PDF text by page/block order and generated clean Markdown with YAML front matter.

### Second pass
Removed recurrent running headers, footers, page numbers, page geometry artifacts, volume title noise, and mechanically detectable line-wrap hyphenation. Converted obvious section headings to Markdown headings.

### Third pass
Applied special-character repair where recoverable, including pseudo-small-cap epigraphic glyphs and common private-use technical signs, then produced a companion technical-form list.

## Remaining cautions

PDF uses inconsistent capitalization and some embedded-font artifacts; mechanical cleanup was applied.

Anomaly scan after cleanup:
- unclear glyph markers: 0
- remaining private-use-area characters: 0
- replacement characters: 0
- approximate mojibake markers: 0
- pseudo-small-cap glyphs remaining: 0

## Further-pass recommendation

A further pass would add limited value for general corpus search; it would mainly improve individual technical forms.
