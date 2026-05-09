---
title: "Script and Language at Ancient Voltino — Extraction Report"
author: "Joseph F. Eska; Rex E. Wallace"
date: 2011
source_type: born-digital
extraction_date: 2026-05-08
source_file: eska-2011-script-language-ancient-voltino.pdf
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The text layer was used as the primary input. Visual rendering was used as fallback for the article title, page-image figure extraction, obvious small-caps/P-case repairs, laryngeal/superscript checking, and special epigraphic glyph context.

The supplied PDF contains preliminary journal/proceedings front matter and table-of-contents pages before the article. The corpus extraction treats Joseph F. Eska – Rex E. Wallace, “Script and Language at Ancient Voltino,” pp. 93–113, as the source text. The preliminary front matter was not included in the main Markdown file.

## Corrections applied

- Rejoined line-break hyphenation in running prose.
- Removed running headers, footers, page numbers, and page geometry.
- Converted the article’s references section into a separate bibliography file.
- Converted footnotes to Markdown footnotes and kept them in the main article file.
- Normalized clear laryngeal and numbered-reference typography where the visual rendering showed subscript/superscript styling, e.g. `h₁`, `h₂`, `h₃`, `LIV²`, and note/citation superscripts.
- Repaired recurring small-caps extraction artifacts involving capital P, e.g. `pREV` → `PREV`, `pERF` → `PERF`, `pID` → `PID`, `pC` → `PC`, `pBA` → `PBA`, and bibliography/author-name P-initials.
- Preserved Private Use Area epigraphic glyphs from the PDF text layer rather than replacing them with conjectural modern Unicode characters.
- Extracted the inscription photograph pair from p. 93 as `images/eska-wallace-2011-fig1.png`.

## Unresolved issues

- Several indigenous-script characters are encoded in the PDF text layer as Private Use Area glyphs. They were retained as PUA codepoints. Because the original custom font is not packaged with the Markdown, visual rendering of those characters may vary across systems.
- Two places in the source visually refer to an “allograph” without a recoverable text-layer glyph. These remain as prose references to “its allograph” rather than a substituted glyph.
- In §14d and §14l, the source includes visible character-shape illustrations after “viz.,” that are not recoverable from the text layer in this environment. They remain as `viz., .` in the corpus text, matching the extraction limitation rather than silently supplying a guess.
- The table in §21(15e)(ii) is structurally awkward in the source. It was converted to Markdown tables, but a future visual pass could improve the exact interlinear alignment.
- Bibliography entries were lightly repaired for obvious extraction artifacts; because this included case and accent restoration in dense bibliographic prose, some residual bibliographic punctuation/capitalization errors may remain.

## Confusion-pair report

- `h₁ h₂ h₃`: normalized in reconstructed forms identified during the pass. Could not guarantee every laryngeal occurrence was fully checked in all footnotes and bibliography.
- Macron vowels `ā ē ī ō ū`: retained/inserted where visible and semantically required. Could not guarantee complete verification across all footnotes.
- Superscript modifier letters `ʰ ʷ`: retained/inserted in clear phonetic contexts such as `/tʰ/`, `dʱ`, and `au̯`. Some source-level spacing/positioning may not be fully reconstructible.
- `ə`: no source instances identified in the output.
- Underdot characters `ṛ ḷ ṃ ṇ`: retained where identified, e.g. `ḷamas`, `neṃases`, `ṭeimeziau`, `ṣ́o=`, `ạToṃ`, `Toniọn`.
- `ǵ ḱ`: no source instances identified in the output.
- Asterisk `*`: retained before reconstructed forms where identified.
- Dagger `†`: no source instances identified in the output.
- Private-use glyphs: retained, not normalized. These are the principal high-risk characters in this article.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

- `h₁`: 5
- `h₂`: 5
- `h₃`: 4
- `ā`: 9
- `ē`: 2
- `ī`: 9
- `ō`: 0
- `ū`: 2
- `ə`: 0
- Greek characters: 26
- Combining diacritics: 16
- `†`: 0

### Private Use Area glyph inventory

- U+F402 ``: approximately 3
- U+F411 ``: approximately 6
- U+F412 ``: approximately 4
- U+F421 ``: approximately 5
- U+F422 ``: approximately 1
- U+F440 ``: approximately 1
- U+F441 ``: approximately 2
- U+F444 ``: approximately 2
- U+F450 ``: approximately 4
- U+F451 ``: approximately 6
- U+F454 ``: approximately 1
- U+F473 ``: approximately 1
- U+F492 ``: approximately 1
- U+F493 ``: approximately 3
- U+F494 ``: approximately 1
- U+F497 ``: approximately 1
- U+F498 ``: approximately 1
- U+F4B1 ``: approximately 1
- U+F4B2 ``: approximately 3
- U+F4C0 ``: approximately 2
- U+F4C2 ``: approximately 2
- U+F4D4 ``: approximately 1
- U+F4D8 ``: approximately 5
- U+F4E4 ``: approximately 6
- U+F4E6 ``: approximately 3
- U+F500 ``: approximately 3
- U+F501 ``: approximately 1
- U+F514 ``: approximately 1
- U+F515 ``: approximately 1
- U+F523 ``: approximately 13
- U+F561 ``: approximately 1
- U+F562 ``: approximately 1
- U+F571 ``: approximately 4
- U+F572 ``: approximately 8
- U+F580 ``: approximately 2
- U+F5A1 ``: approximately 1
- U+F5B3 ``: approximately 30
- U+F616 ``: approximately 1
- U+F61A ``: approximately 1
- U+F631 ``: approximately 5
- U+F6AA ``: approximately 3
- U+F6C0 ``: approximately 1
- U+F6F6 ``: approximately 15
- U+F8C4 ``: approximately 1

## Structural integrity check

- Headings are consistent and mirror the article’s labeled sections.
- Footnotes are attached using Markdown footnote syntax.
- The reference list is separated into `eska-wallace-2011-script-language-ancient-voltino-bibliography.md`.
- The figure is extracted and referenced from the main Markdown file.
- No index is present for the article; no index file was produced.
- No second-pass page-by-page visual collation of every special glyph was completed. Character fidelity is good enough for a first pass but not final “character-authoritative” status.

## Image inventory

- `images/eska-wallace-2011-fig1.png` — source label `(1)`, page 93 / PDF page 7; photograph pair of the Voltino inscription, consisting of a full stone view and close-up of the inscribed text.
