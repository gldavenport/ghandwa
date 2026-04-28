# Second-pass notes

Targeted second pass completed: 2026-04-28.

## What was changed

- Normalized remaining HTML emphasis tags in the Markdown source.
- Converted obvious linguistic subscript/superscript notation to Unicode where useful for corpus searching:
  - `h<sub>1</sub>` / `h<sub>2</sub>` → `h₁` / `h₂`
  - `<sup>h</sup>` / `<sup>w</sup>` → `ʰ` / `ʷ`
- Spot-checked the main lexical bullet lists in sections 3.1–3.3.
- Corrected Figure 7 placement so it sits with the mythology/thunder-god discussion rather than at the end of the maritime section.
- Removed a stray Markdown heading marker before section 3.1.
- Added printed-page anchors as HTML comments, keyed to the chapter PDF:
  - `<!-- p. 195 -->` through `<!-- p. 216 -->`
- Normalized one source glyph artifact in the mythology section:
  - `perknas` → `perkū́nas`
- Normalized `*tn°ros` to `*tn̥ros` based on the printed form.

## Notes on page anchors

The page anchors are meant for citation/navigation against the PDF. Where the printed PDF page break falls in the middle of a sentence, paragraph, or bullet item, the anchor was inserted inline or at the nearest stable Markdown location rather than forcing a hard paragraph break.

## Possible value of further passes

No further pass is needed for ordinary reading, corpus searching, or comparative/conlang use.

A further pass could be useful only if this chapter becomes citation-critical or if exact diplomatic fidelity is required. In that case, the highest-value checks would be:

1. Compare every reconstructed lexical form in sections 3.1–3.3 against the PDF page images.
2. Compare the references line-by-line against the publisher PDF.
3. Decide whether to preserve publisher-style italics for every title, foreign word, and cited form. In this second-pass Markdown, some visual emphasis was intentionally flattened where that made reconstructed forms cleaner and easier to search.
4. Add full accessible descriptions for the figures beyond the captions already included.
