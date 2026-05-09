---
title: "On the homonymy of ‘put’ and ‘suck’ in Proto-Indo-European — Extraction report"
author: "Michiel de Vaan"
date: 2019
source_type: born-digital
extraction_date: 2026-05-07
source_file: vaan-2019-homonymy-put-suck.pdf
chunk: extraction-report
---

# Extraction report

## Source identification

- Source type: born-digital PDF with machine-readable text layer.
- Source length: 18 PDF pages, article pagination 176–193.
- Embedded images: none detected by `pdfimages -list`.
- Output granularity: single-file journal-article extraction with bibliography separated per project instructions.

## Corrections applied

- Removed running headers, footers, page numbers, journal title repetition, DOI/license footer material, and page-boundary artifacts.
- Rejoined paragraphs broken by line wrapping and page boundaries.
- Split bibliography into a separate Markdown file.
- Reconstructed the five summary tables as Markdown tables.
- Moved footnotes into Markdown footnote syntax and attached them to the relevant body text.
- Normalized laryngeal notation from the text layer’s `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃` where the source uses indexed laryngeals.
- Corrected common born-digital extraction losses in technical forms, including superscript aspiration in PIE reconstructed forms (`dʰ`, `bʰ`), `LIV²`, misplaced combining accents in Sanskrit/Lithuanian forms, and select page-boundary hyphenation artifacts.
- Preserved Greek, accented Latin-script forms, thorn-like symbols, delta, ḫ, and combining diacritics where recoverable from the text layer and/or visual rendering.

## Unresolved issues list

- No `[unclear]` markers were inserted.
- No inline `[?]` markers were inserted. Several character classes were normalized from consistent visual/text-layer evidence rather than treated as uncertain one-off inferences.
- The article contains dense linguistic notation. A further character-authoritative pass could still compare every reconstructed form against the rendered PDF, especially the summary tables and footnotes.
- Markdown emphasis around cited linguistic forms was regularized for readability but is not a diplomatic representation of every italic span in the PDF.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: normalized in reconstructed forms and bibliography entries; no plain `h1`, `h2`, or `h3` strings found in the generated Markdown files during final grep.
- Macron vowels: normalized/repaired in visible high-risk cases such as `dhā́tave`, `payo-dhā́-`, `dė́ti`, `dėlė̃`, and related table entries. Macrons remain potentially vulnerable in bibliography titles and dense forms.
- `ʰ` vs. `h`: superscript aspiration was restored in PIE reconstructed forms where text extraction flattened it. Sanskrit/Indic transliteration forms such as `dhénā-` retain ordinary `h`.
- `ʷ`: no instances expected or found in the output.
- `ə`: no instances expected or found in the output.
- Underdot characters: preserved where detected, including `dāt̰` and `R̥g-Veda`; no full pass can certify every possible underdot instance.
- `ǵ ḱ`: no instances expected or found in the output.
- Reconstructive `*`: retained in generated Markdown source, but some Markdown formatting remains around linguistic forms; search workflows should check rendered and raw views if exact asterisk behavior matters.
- `†`: no instances expected or found in the output.

## Codepoint inventory

Approximate counts across the main Markdown and bibliography files:

| Item | Approximate count |
|---|---:|
| `h₁` | 118 |
| `h₂` | 17 |
| `h₃` | 3 |
| `ā` | 44 |
| `ē` | 51 |
| `ī` | 38 |
| `ō` | 13 |
| `ū` | 0 |
| `ə` | 0 |
| Greek-script characters | 238 |
| Combining diacritics | 34 |
| `†` | 0 |
| `ʰ` | 134 |

All counts are approximate and intended for cross-pass comparison only.

## Structural integrity check

- Headings are consistent: title, abstract, keywords, numbered sections 1–13, acknowledgments, and separate references.
- Footnotes are present as Markdown footnotes and attached to the corresponding callouts.
- The five summary tables are represented as Markdown tables.
- Page headers, footers, and journal-pagination noise were removed.
- No images or image placeholders were needed.

## Image inventory

No images detected; no image-only placeholders inserted.
