---
title: "Ringe 2017 whole-volume QA and corpus-readiness review"
source_title: "From Proto-Indo-European to Proto-Germanic"
author: "Don Ringe"
review_utc: "2026-04-27T21:30:00Z"
review_scope: "Generated Markdown, index, references, structured index, structured references, and bundle organization"
source_file: "ringe-pie-to-proto-germanic-2nd-ed.pdf"
---

# Ringe 2017 whole-volume QA and corpus-readiness review

## Executive assessment

The corpus is now usable for comparative work and conlang construction. The strongest files are Chapter 3, the structured index CSV/TSV, and the references table. Chapter 2 and Chapter 4 are usable for search and orientation, but individual paradigm forms should still be checked against the PDF before formal citation or before importing into a lexicon/paradigm generator.

During this review I created a QA-reviewed bundle rather than only a report. It incorporates several small but important fixes found during the audit.

## QA-reviewed fixes applied

- Added a front-matter file, because the earlier complete bundle omitted the table of contents, abbreviations, acknowledgments, and Ringe's transcription note.
- Restored the missing Chapter 4 printed p. 304, including the i/u-stem paradigm table and following discussion.
- Fixed invalid YAML in Chapter 4 front matter.
- Added the missing Chapter 2 printed p. 43 page anchor.
- Corrected a Chapter 3 joined-word extraction artifact.
- Removed the two remaining private-use glyphs in the index by normalizing the Runic Norse small-cap entry to `-AR`.
- Cleaned obvious residual line-break hyphenation in Chapter 2, Chapter 4, and the index.

## Coverage and mechanical QA

|file|anchors|range|PUA|old digits|ligatures|YAML/fences|hyphen candidates|
|---|---|---|---|---|---|---|---|
|front|4|front roman|0|0|0|ok|0|
|chapter-1|4|1-4|0|0|0|ok|0|
|chapter-2|79|5-83|0|0|0|ok|1|
|chapter-3|157|84-240|0|0|0|ok|0|
|chapter-4|89|241-329|0|0|0|ok|5|
|index-md|0||0|0|0|ok|0|
|references-md|17|331-347|0|0|0|ok|0|

Notes:

- `PUA`, old-style digit glyph, and ligature counts are now zero across the reviewed Markdown set.
- All YAML front matter now parses cleanly.
- Fenced code-block counts are balanced.
- Numeric page anchors now have no gaps in Chapters 1-4 and References.
- The index remains unanchored by printed page; the structured index CSV/TSV is the better navigation object.

## Corpus-readiness rating

| Component | Corpus/search use | Comparative/conlang use | Citation-grade use | Notes |
|---|---:|---:|---:|---|
| Front matter | Good | Good | Good after spot-check | Newly added; includes transcription note and abbreviations. |
| Chapter 1 | Good | Good | Good | Low-risk prose chapter. |
| Chapter 2 | Good | Useful with caution | Spot-check required | PIE phonology and morphology are notation-dense; paradigms remain the main risk. |
| Chapter 3 | Good | Very useful | Spot-check technical forms | Best pilot chapter; stage-sensitive notation policy is strongest here. |
| Chapter 4 | Good | Useful with caution | Spot-check required | Restored p. 304; some prose remains inside conservative fenced blocks. |
| Index Markdown | Good | Very useful | Spot-check entries | Best for browsing forms by section. |
| Structured index CSV/TSV | Excellent | Excellent | Spot-check entries | 4,802 rows; best object for filtering forms and comparanda. |
| References Markdown/CSV/TSV | Good | Secondary | Good after spot-check | 339 parsed entries; bibliography is less important for conlang construction but useful for following sources. |

## Recommended use pattern

For comparative work and conlang construction:

1. Use the structured index TSV/CSV as the primary discovery layer.
2. Use Chapter 3 for change-history and relative chronology.
3. Use Chapter 2 for PIE inventory, morphology, and high-level forms, but verify paradigm cells before reuse.
4. Use Chapter 4 for PGmc inventories and paradigms, but verify dense paradigm tables before reuse.
5. Treat the references as a source-following aid, not as the main research object.

## Remaining limitations

### Paradigm fidelity

The biggest remaining limitation is not ordinary OCR noise; it is table/paradigm fidelity. Multi-column paradigms can still contain alignment, accent-placement, or cell-boundary problems even when the text is searchable.

### Fenced text blocks

Chapters 2-4 use fenced text blocks conservatively for dense tables and paradigms. This is good for preserving visual structure but imperfect for semantic Markdown. Some Chapter 4 prose remains inside fenced blocks where the table region continued too long. This is acceptable for search/corpus use but not ideal for a polished reading edition.

### Stage-sensitive notation

The core policy remains correct:

- PIE / Proto-Core IE / Proto-Central IE: `kʷ`, `gʷ`, `gʷʰ`, `bʰ`, `dʰ`, `gʰ`, `h₁ h₂ h₃`.
- PGmc and later Germanic: `kw`, `gw`, `hw`.
- Attested-language forms: preserve source spelling/transcription.
- Ambiguous transitional forms: verify against the PDF.

### Index page anchors

The Markdown index is not page-anchored. This is not a serious problem because index entries already contain page references, and the structured index CSV/TSV is the more useful form for corpus operations. A page-anchored index could still be produced later if needed.

## Files generated by this QA review

- `front-matter/ringe-2017-front-matter-first-pass.md`
- `chapters/chapter-2/ringe-2017-chapter-2-proto-indo-european-qa-reviewed.md`
- `chapters/chapter-3/ringe-2017-chapter-3-development-proto-germanic-qa-reviewed.md`
- `chapters/chapter-4/ringe-2017-chapter-4-proto-germanic-qa-reviewed.md`
- `index/markdown/ringe-2017-index-qa-reviewed.md`
- `qa/ringe-2017-qa-issues.tsv`
- `qa/ringe-2017-qa-metrics.tsv`

## Bottom line

This is corpus-ready for search, discovery, comparison, and conlang design work. It is not yet a fully diplomatic scholarly edition. The next best improvement, if needed, would be a targeted paradigm-only verification pass for Chapters 2 and 4, not another whole-book cleanup pass.
