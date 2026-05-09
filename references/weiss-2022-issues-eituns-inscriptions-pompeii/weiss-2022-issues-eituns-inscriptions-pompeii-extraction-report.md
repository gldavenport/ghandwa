---
title: "Issues in the eítuns Inscriptions of Pompeii — Extraction report"
author: "Michael Weiss"
date: "2022"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "weiss-2022-issues-eituns-inscriptions-pompeii.pdf"
chunk: "extraction-report"
---

# Extraction report

## Source identification

- Source type: born-digital PDF with a machine-readable text layer.
- Extraction scope: Michael Weiss, “Issues in the eítuns Inscriptions of Pompeii,” pp. 949-960 of *EQO DUENOSIO. Studi offerti a Luciano Agostiniani*.
- The PDF also contains volume front matter and end matter. Those pages were used for metadata but were not included in the corpus text files.
- No article figures, maps, diagrams, or plates were present in the extracted article pages.

## Corrections applied

- Rejoined hyphenated line-breaks and page-break continuations in running prose.
- Removed running headers, page numbers, blank decorative lines, and page-layout artifacts.
- Preserved article page anchors as HTML comments for later source checking.
- Converted footnotes into Markdown footnotes and merged page-split footnotes.
- Separated the bibliographical references into `weiss-2022-issues-eituns-inscriptions-pompeii-bibliography.md`.
- Normalized laryngeals from text-layer ASCII `h1` to Unicode subscript `h₁` where the rendered PDF showed the subscript form.
- Repaired corrupted/private-use glyph mappings by visual comparison and contextual check:
  - `` → `i̯`
  - `` → `u̯`
  - `` → `m̥`
  - `` → `ḱ`
  - `` → `r̥`
  - control glyph after final `m` in Tocharian forms → `ṃ`
  - control glyph after `t` in `Maitreyasamiti-nāṭaka` → `ṭ`
  - control glyph after `s` in the Tocharian quoted line → `ś`
  - corrupted Vedic `dákṣiṇa-` glyphs repaired to `ṣ` and `ṇ`
- Converted two source layout comparison blocks into Markdown tables to preserve the semantic column structure.

## Unresolved issues list

- No `[unclear]` markers were inserted.
- The damaged Oscan inscription in Po 39 contains source-internal lacuna notation (`[……]`, `[…..]`) and the underdotted `ị`; these were preserved as source notation, not expanded.
- The PDF’s ToUnicode mapping fails for several scholarly glyphs. The replacements listed above are strongly supported by the visual render and linguistic context, but a later pass against publisher source files could still improve confidence.
- The bibliography entry “Fortson IV B.W. 2013” required the same `i̯` and `h₁` repairs as the body text.
- The phrase “form is less like for the reasons state above” was preserved as printed/extracted; it appears possibly typographical in the source, but was not silently emended.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: `h₁` was normalized where detected. No `h2`/`h3` instances occur in the extracted article. No remaining ASCII `h1`, `h2`, or `h3` strings were found in output files.
- Macron vowels: precomposed macron vowels were used where present (`ā ē ī ō ū`). No systematic claim of completeness is made.
- `ʰ ʷ`: no clear instances of superscript aspiration or labialization were found in this article. The high-risk symbol here was instead non-syllabic `i̯`/`u̯`.
- `ə`: retained in `maδəma-`, `*tsəm-`, and `[vø:rtǝr]`.
- Underdot letters: repaired/preserved `ṃ`, `ṭ`, `ṣ`, `ṇ`, and `ị` where detected. No full audit against original font tables was possible.
- `ǵ ḱ`: `ḱ` was repaired in `*deḱsi-no-` and `*deḱsi-u̯o-`.
- Asterisk `*`: retained for reconstructed forms. Markdown rendering may treat some bibliographical title italics specially, but source asterisks were not intentionally normalized away.
- Dagger `†`: no dagger instances were detected.

## Codepoint inventory

Approximate counts across the extracted Markdown files:

- `h₁`: 5
- `h₂`: 0
- `h₃`: 0
- `ā`: 13
- `ē`: 5
- `ī`: 2
- `ō`: 7
- `ū`: 2
- `ə`: 4
- Greek characters: 190
- Combining diacritics: 39
- Dagger `†`: 0

## Structural integrity check

- Main article text is single-file Markdown with title, author, numbered section structure, page anchors, quotation block, two comparison tables, and footnotes.
- Bibliographical references are separated into their own Markdown file.
- No index is present for the article.
- Article pages contain no figures requiring an `images/` directory.
- A scan for private-use Unicode characters and C0 control characters in the output found none.

## Image inventory

No image placeholders were used. No article images were extracted.
