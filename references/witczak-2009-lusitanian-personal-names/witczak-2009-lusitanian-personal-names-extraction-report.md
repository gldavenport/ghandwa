---
title: "Lusitanian Personal Names with the Equine Motivation"
author: "Krzysztof Tomasz Witczak"
date: 2009
source_type: born-digital
extraction_date: 2026-05-07
source_file: "witczak-2009-lusitanian-personal-names.pdf"
chunk: extraction-report
---

# Extraction Report

## Source identification

- Source file: `witczak-2009-lusitanian-personal-names.pdf`
- Source type: born-digital PDF with a machine-readable text layer.
- Basis of extraction: PDF text layer, with rendered-page visual checks used where the text layer produced corrupt glyph output.
- Scope: single journal article, pp. 155–163.
- Output granularity: single main Markdown file plus separate bibliography file.
- Images: no figures, maps, plates, image-only tables, or embedded illustrations observed.
- Index: none observed.

## Corrections applied

- Removed running headers, page numbers, DOI-placement artifacts, authentication footer text, download timestamp text, and page-boundary artifacts.
- Rejoined paragraphs and repaired line-break hyphenation introduced by PDF extraction, including compounds split across page or line boundaries.
- Repaired ligature artifacts where the PDF text layer produced forms such as `ﬁ nd`, `reﬂ exes`, and similar ligature encodings.
- Split the end bibliography into `witczak-2009-lusitanian-personal-names-bibliography.md` as required by project instructions.
- Converted the article’s footnotes to Markdown footnote syntax and attached them to their source-text anchors.
- Repaired visibly corrupted non-Unicode Greek extraction. Examples include `Lewn…daj` → `Λεωνίδας`, `lšwn` → `λέων`, `Ippokr£thj` → `Ἱπποκράτης`, `†ppoj` → `ἵππος`, `m£tan` → `μᾶταν`, `lÚgx` → `λύγξ`, `kÚwn` → `κύων`, and `kunÒj` → `κυνός`.
- Repaired selected technical notation where the text layer inserted spaces inside forms, including `*ek̂ wos` → `*ek̂wos`, `*Ek̂ wonā` → `*Ek̂wonā`, `*k̂ wōn` → `*k̂wōn`, and `*pek̂ u-` → `*pek̂u-`.
- Preserved the source’s extracted schwa/turned-e character as `ǝ` rather than silently normalizing it to IPA `ə`.

## Unresolved-issues list

No `[unclear]` or `[?]` markers were inserted in the corpus files. Residual uncertainty remains around character-perfect recovery of some Greek words because the PDF text layer used a non-Unicode Greek encoding and the final Greek strings were visually checked from rendered page images rather than recovered directly from the text layer.

Specific items recommended for a later character-authoritative pass:

- Footnote 1 Hesychian gloss: `μᾶταν [acc. sg.?] · ἡ λύγξ. ἔνιοι δὲ ματακός ἢ ματακόν`.
- Footnote 4 Boeotian/Greek forms: `πυκτίς`, `κτίς`, `ἴκτις`, and prefix `πυ-`.
- Greek examples in the opening paragraphs and section 2: `Λεωνίδας`, `Ἱπποκράτης`, `ἵππος`, `ἵκκος`.
- The source appears to use `ǝ` in reconstructed forms; a later pass could compare the original publisher encoding against visual glyphs if a strict distinction between U+01DD `ǝ` and U+0259 `ə` matters.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: no indexed laryngeal forms using h plus subscript digits were observed. No normalization was applied.
- Macron vowels `ā ē ī ō ū`: present and preserved in running text, footnotes, and bibliography. Counts are approximate; full certification would require a second visual pass.
- Superscript modifier letters `ʰ ʷ`: `ʷ` was used in forms such as `*gʷou-`, `*kʷu-`, and `xʷorn`. No `ʰ` was observed.
- Schwa/turned-e: output preserves `ǝ` from the PDF extraction layer. The IPA schwa `ə` is not used in the output.
- Underdot letters: forms such as `gauḥ`, `máryaḥ`, `śunaḥ`, and `lulāpaḥ` were preserved or repaired. No full visual certification is claimed.
- Acute consonants `ǵ ḱ`: none observed.
- Asterisk `*`: preserved before reconstructed forms. Because this is Markdown, some raw asterisks may be interpreted as emphasis by renderers; they are intentionally left literal for corpus fidelity.
- Dagger `†`: no true source dagger usage was observed. Apparent daggers in extracted text represented corrupt Greek glyphs and were repaired visually.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

| Item | Approx. count |
|---|---:|
| h₁ | 0 |
| h₂ | 0 |
| h₃ | 0 |
| ā | 23 |
| ē | 2 |
| ī | 3 |
| ō | 5 |
| ū | 3 |
| ə | 0 |
| ǝ | 21 |
| Greek characters | 125 |
| Combining diacritics | 14 |
| † | 0 |
| ʷ | 4 |
| ₃ | 1 |

## Structural integrity check

- Headings are regularized into Markdown hierarchy: title, sections 1–7, notes, and separate bibliography.
- Footnotes 1–6 are attached to the corresponding note anchors and collected in the main Markdown file.
- Bibliography entries are one entry per paragraph in the separate bibliography file.
- No tables, paradigms, figures, plates, maps, or index sections were present.
- Page-boundary continuation text was rejoined; no obvious continuation loss was found during the pass.

## Image inventory

No images extracted. No `[image-only ...]` fallback placeholders were used.
