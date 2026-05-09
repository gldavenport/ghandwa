---
title: "Icelandic leppa ‘fox’ < *h₂lop-n-íh₂-: A New Example of Kluge’s Law in Germanic"
author: "Guus Kroonen"
date: "2025"
source_type: born-digital
extraction_date: "2026-05-07"
source_file: "kroonen-2025-icelandic-leppa-fox.pdf"
chunk: extraction-report
---

# Extraction Report

## Source type

Born-digital PDF. The PDF has a machine-readable text layer and publisher metadata. The embedded text layer was used as the primary input. Rendered-page checks were used only for dense tables and combining-diacritic placement.

## Output files

- `kroonen-2025-icelandic-leppa-fox.md` — clean corpus Markdown, main text, tables, language-abbreviation table, and footnotes.
- `kroonen-2025-icelandic-leppa-fox-bibliography.md` — bibliography extracted as a separate file.
- `kroonen-2025-icelandic-leppa-fox-extraction-report.md` — this QC record.
- `manifest.json` — machine-readable metrics and output inventory.

No `images/` directory was produced because no figures, maps, plates, or embedded images were detected.

## Corrections applied

- Rejoined hyphenated line breaks and soft-hyphen artifacts from the text layer, including words split across line endings in the body and bibliography.
- Reconstructed paragraphs from the PDF lineation while preserving original wording and citation order.
- Rebuilt Tables 1–4 and the Language Abbreviations list as Markdown tables.
- Moved the bibliography into a separate bibliography file as required.
- Converted source footnotes to Markdown footnotes and repaired page-continuation breaks in footnote text.
- Repaired detached combining acute artifacts produced by text extraction where the raw text and visual rendering made the intended form clear, including forms such as `takṣṇī́-`, `rā́jñī-`, `wulpī́`, `wulkjā́s`, `vr̥kī́-`, `rihnī́`, `lofnī́`, `ursnī́`, and `śrī́-`.
- Preserved laryngeals with Unicode subscript digits: `h₁`, `h₂`, `h₃`.
- Preserved the source’s unusual stacked diacritic sequence in footnote 15: `*h₂lō̆p-ēḱ`.

## Unresolved-issues list

No `[unclear]` or `[?]` markers were inserted.

Remaining uncertainty:

- The PDF text layer and visual rendering were checked for high-risk forms, but a full diplomatic glyph-by-glyph verification was not performed.
- Markdown tables necessarily regularize some visual alignment from the source tables. The table cell contents were prioritized over visual layout.
- The blank fourth header cell in Table 1 and blank top header cells in Tables 2 and 4 were preserved as empty Markdown table headers rather than supplied with editorial labels.
- Publisher title/journal typography and routine italicization were not exhaustively represented as Markdown emphasis, to avoid adding markup noise around reconstructed forms. Character fidelity was prioritized.

## Confusion-pair report

- `h₁ h₂ h₃` vs `h1 h2 h3`: Unicode subscript laryngeals were used where laryngeals occur. No ASCII `h1`, `h2`, or `h3` laryngeal spellings were detected in the output.
- Macron vowels: precomposed macron vowels were preserved where available in the text layer. Combining accents over macron vowels were retained when present in the source forms.
- `ʰ` and `ʷ`: superscript modifier letters were preserved in reconstructed forms such as `dʰ`, `bʰ`, `ǵʰ`, and `kʷ`.
- `ə`: schwa was preserved in `xvarənah-`.
- Underdot/ringed/syllabic characters: `ṣ`, `ṇ`, `ṛ`, and `r̥` were preserved where detected.
- `ǵ` and `ḱ`: precomposed acute consonants were preserved.
- Asterisk before reconstructed forms: literal `*` was preserved.
- Dagger `†`: no dagger instances were detected in this source.

This report does not certify that all instances are correct; it records the checks and repairs performed.

## Codepoint inventory

Approximate counts across the extracted main text and bibliography:

| Item | Approximate count |
|---|---:|
| `h₁` | 4 |
| `h₂` | 54 |
| `h₃` | 2 |
| `ā` | 28 |
| `ē` | 19 |
| `ī` | 82 |
| `ō` | 24 |
| `ū` | 5 |
| `ə` | 1 |
| Greek characters | 171 |
| Combining diacritics | 41 |
| `†` | 0 |

## Structural integrity check

- Headings are consistent.
- Main text and bibliography are separated.
- Footnotes are attached as Markdown footnotes and retained in source order.
- Tables are well-formed Markdown tables.
- Page-boundary continuation text was reviewed and rejoined where it crossed pages.
- No figures or image-only tables were found.

## Image inventory

No images or fallback image placeholders.
