---
title: "Etymological Dictionary of Proto-Celtic"
author: "Ranko Matasović"
date: "2009"
source_type: mixed
extraction_date: 2026-05-07
source_file: "matasovic-2009-proto-celtic.pdf"
chunk: "extraction-report"
---

# Extraction Report

## Source identification

Source treated as **mixed/scanned-with-OCR**: the PDF consists of scanned page images with an OCR text layer. The extraction used the OCR text layer as the base input and consulted rendered pages only for source-type confirmation and for the visible classification diagrams on PDF page 21.

## Corrections applied

- Repaired repeated OCR label confusions such as `GOlD` → `GOID`, `Olr.`/`0Ir.`/`aIr.` → `OIr.`, `Mlr.` → `MIr.`, `JEW`/`lEW` → `IEW`, `LElA` → `LEIA`, `ElEC`/`£lEC` → `EIEC`, and `OIL` → `DIL`.
- Normalized ASCII laryngeal indices `h1`, `h2`, `h3` and `H1`, `H2`, `H3` to subscript forms `h₁`, `h₂`, `h₃` and `H₁`, `H₂`, `H₃` throughout the extracted Markdown.
- Replaced repeated soft-hyphen/page-break artifacts and stripped trailing whitespace.
- Promoted parsed lexical headwords to Markdown level-3 headings inside letter chunks.
- Added PDF page anchors as HTML comments for later checking.
- Extracted a broad raster crop from PDF page 21 for the two Celtic sub-classification diagrams because the OCR layer collapses the tree structures.

## Unresolved issues

- The OCR layer has systematic character degradation in technical forms. Examples visible during extraction include OCR confusions among `I/l/1`, `O/0`, `A/ā`, `R/f/ɸ`, and `W/ʷ`. These were not globally repaired where doing so could create false corrections.
- Superscript labiovelar notation is not consistently recoverable from the OCR layer. Forms such as `gW`, `kW`, `gw`, and `kw` should be checked against page images in later passes.
- Macron and accent fidelity is incomplete in the OCR base, especially in dense lexical entries and references. The extraction preserves what was present after limited cleanup but does not certify vowel-length accuracy.
- Some headwords beginning with special characters were OCR-damaged, especially entries in the F/L sections where initial symbols are sometimes rendered as `R`, `t1`, or `I`. These were kept in source-order chunks, but the characters require visual audit.
- The table of contents lists an index beginning at page 459, but this PDF copy has only 460 PDF pages and the final pages are still references. No index section was detected or extracted.
- No `[?]` markers were inserted for every OCR-derived character because this PDF is not visually transcribed character-by-character. Treat the extraction as an OCR-text-layer first pass, not a character-authoritative edition.

## Confusion-pair report

- `h₁ h₂ h₃`: normalized from OCR text where ASCII `h1/h2/h3` appeared. Some laryngeals may remain wrong if OCR produced another character.
- Macron vowels: preserved when present, but many OCR forms likely lost macrons or substituted plain vowels/digits. Not fully verified.
- `ʰ ʷ`: not normalized globally; OCR frequently represents these as `h`, `w`, `W`, or digraphs. Needs visual checking.
- `ə`: not specifically verified.
- Underdot letters: not specifically verified; likely incomplete if present in the source.
- `ǵ ḱ`: not specifically verified.
- Asterisk `*`: preserved in parsed headwords and forms where OCR retained it; some asterisks may have become `~` or disappeared.
- Dagger `†`: count is approximate; not visually verified.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

- h₁: 213
- h₂: 512
- h₃: 183
- ā: 0
- ē: 0
- ī: 0
- ō: 0
- ū: 0
- Greek-range characters: 0
- Combining diacritics: 0
- Dagger: 0
- `[unclear]` markers: 0
- `[?]` inferred-character markers: 1

## Structural integrity check

- Output is chunked into front matter, introduction, one file per dictionary letter/range, appendix, and bibliography.
- Bibliography is separate as required.
- No index file is included because no index section was detected in this PDF copy.
- Lexical entries are separated as Markdown headings where the OCR category labels were parseable.
- Page-boundary anchors are preserved; some entries split across page boundaries retain page anchors inside the entry body.
- Tables and dense lists in the introduction and bibliography remain primarily text-layer based and should be considered candidates for later targeted cleanup.

## Image inventory

- `images/matasovic-2009-proto-celtic-fig1-1-1-2.png` — PDF page 21, source labels Fig. 1.1 and Fig. 1.2, broad crop containing the Celtic sub-classification diagrams.
