---
title: "Kroonen 2016 third-pass extraction notes"
source_file: "kroonen-2016.pdf"
extraction_pass: 3
---

# Third-pass extraction notes

## Scope

This pass performed three cleanup/augmentation tasks:

1. Verified the remaining uncertain linguistic forms visible in the rendered page images.
2. Normalized the bibliography into a separate reusable reference file.
3. Extracted a structured lexical/comparanda dataset for corpus use.

## Corrections and decisions

- Footnote 3 was corrected from `*μασλον` to `*μᾰσλον`, matching the rendered source image.
- Note 1 and the bibliography contain a source-internal name mismatch:
  - note 1 cites `(Tournier 1794, 76)`;
  - the printed bibliography lists `Tourner, H. M.`
  The main Markdown preserves both spellings as printed. The normalized bibliography keys the item as `tourner-1794` and records the mismatch in a note.
- `*tl̥h₂-tó-` is normalized in Unicode as `l` + combining ring below. The source visually prints the syllabic-liquid notation as `ḷ`.
- `šam(a)lu-`, `maḫla-`, `GIŠḪAŠḪUR`, `geš`, `ḫašḫur`, and `ḫašḫūru-` were checked against the rendered text and retained with Unicode diacritics.
- The main article remains clean Markdown rather than diplomatic Markdown. Page headers, page footers, and lineation are not preserved.

## Remaining uncertainty

No further pass is needed for ordinary corpus use. A future diplomatic pass could still compare every diacritic against page images, but that would mainly produce diminishing returns for this seven-page article.
