---
title: Latin Tree Names and the European Substratum
author: Corinna Leschber
date: 2012
source_type: born-digital
extraction_date: 2026-05-08
source_file: leschber-2012-latin-tree-names.pdf
chunk: extraction-report
---

# Extraction Report

## Source identification

- **Source file:** `leschber-2012-latin-tree-names.pdf`
- **Detected source type:** born-digital PDF with a machine-readable text layer.
- **Document type:** journal article.
- **Page count:** 10 PDF pages; the last rendered page is blank. The article text covers journal pages 117–125.
- **Chunking decision:** single-file article extraction, with bibliography split into a separate Markdown file according to project instructions.
- **Images:** no figures, maps, plates, diagrams, or image-only tables detected.

## Corrections applied

- Rejoined running prose paragraphs across line breaks and page boundaries.
- Removed running headers, page numbers, form-feed artifacts, and the final blank page.
- Repaired line-break hyphenation and soft-hyphen artifacts, including examples such as `thou-sand` → `thousand`, `substra-tum` → `substratum`, `Indo-Euro­pean` → `Indo-European`, and `Bedeutungs­feldern` → `Bedeutungsfeldern`.
- Preserved real compound hyphenation where context required it, e.g. `pre-Indo-European`, `Balto-Slavic`, `Celtic-Roman`, `never-ending`, and `west-östlichen`.
- Normalized laryngeal-style numeric notation where the PDF text layer exposed ASCII digits but the rendered form required subscript notation: `*meh2lom` → `*meh₂lom`; `*h1…` → `*h₁…`.
- Preserved source-specific `hₐ` notation in `*hₐebi-` and `*hₐebVl-` after visual checking against the rendered PDF.
- Repaired one private-use glyph in the text layer (`U+F03D`) by visual checking. The output gives `*h₁l̥[?]-mo-?`; the `[?]` marks the inferred syllabic consonant character.
- Repaired a likely mixed-script text-layer artifact in the bibliography: `Mоskva` with Cyrillic `о` → `Moskva` with Latin `o`.
- Preserved the visually indicated superscript edition marker in the REW bibliography entry as `2009⁷`.
- Added conservative Markdown italics around many language forms, titles, and lexical items for readability. Formatting was reconstructed from context and visual sampling, not from a complete style-layer extraction.

## Unresolved issues

1. **p.122, Lat. _ulmus_ paragraph:** the PDF text layer contains a private-use glyph in `related to PIE *h1-mo-?`. Visual inspection suggests syllabic `l̥`; output uses `*h₁l̥[?]-mo-?`. This should be reviewed against the PDF image or a cleaner source.
2. **p.121, De Vaan page range:** source/text layer reads `De Vaan (2008: 480–4981)`. This appears suspicious, but it was preserved because it appears to be in the source rather than a clear extraction error.
3. **Bibliography/source spelling variants:** body text has `Anreiter, Hasslinger`; bibliography has `Anreiter P., Haslinger M.`. Both were preserved as they appear in their respective locations.
4. **Formatting fidelity:** italics were restored conservatively for obvious forms and titles, but not certified as a complete diplomatic reconstruction of all source typography.

No `[unclear]` markers were inserted. One `[?]` inferred-character marker was inserted.

## Confusion-pair report

The following checks were performed as a targeted pass, but the extraction cannot be certified as character-perfect.

| Confusion pair | Output status |
|---|---|
| `h₁ h₂ h₃` vs. `h1 h2 h3` | `h₁` and `h₂` appear in output; no residual ASCII `h1`, `h2`, or `h3` detected in the Markdown files. |
| Macron vowels vs. dropped macrons | Macron vowels retained where detected: `ā ē ī ō ū`; counts are approximate and listed below. |
| Superscript modifier letters `ʰ ʷ` | No instances detected in this source. |
| Schwa `ə` | No instances detected. |
| Underdot characters such as `ṛ ḷ ṃ ṇ` | No Indic underdot characters detected; one inferred `l̥` uses combining ring below and is marked `[?]`. |
| Acute consonants `ǵ ḱ` | No instances detected. |
| Asterisk before reconstructed forms | Asterisks before reconstructed forms were preserved in the body text. |
| Dagger `†` | No instances detected. |
| Greek forms | Greek terms were spot-checked, including `ἄβιν`, `ἄκαστος`, `ἄκαρνα`, `μῆλον`, `μηλέη`, `μηλέα`, `ὀξύα`, `πίτυς`, `πτελέα`, `προῦμνον`, `προύμνη`, and `μόρον`. This was not an exhaustive glyph-by-glyph audit. |
| Source-specific `hₐ` | Two instances preserved after visual checking: `*hₐebi-`, `*hₐebVl-`. |

## Codepoint inventory

Approximate counts across the delivered Markdown files:

| Item | Approximate count |
|---|---:|
| `h₁` | 1 |
| `h₂` | 1 |
| `h₃` | 0 |
| `hₐ` | 2 |
| `ā` | 6 |
| `ē` | 4 |
| `ī` | 9 |
| `ō` | 6 |
| `ū` | 3 |
| `ə` | 0 |
| Greek characters | 116 |
| Combining diacritics | 1 |
| Dagger `†` | 0 |
| `[unclear]` markers | 0 |
| `[?]` inferred-character markers | 1 |

## Structural integrity check

- Headings are consistent: article title, metadata, keywords, abstract, and bibliography are separated logically.
- The bibliography was extracted into `leschber-2012-latin-tree-names-bibliography.md` and omitted from the main article file.
- No tables are present in the source article. The mentioned Table 10.1 is a referenced table in another source, not a table printed in this article.
- No footnotes or endnotes were detected.
- Journal page anchors were retained as HTML comments (`<!-- p.117 -->` etc.) for source-location checking without adding visible prose.
- Page-boundary continuation text was rejoined in the main file and bibliography.

## Image inventory

No images extracted. No `[image-only ...]` placeholders used.
