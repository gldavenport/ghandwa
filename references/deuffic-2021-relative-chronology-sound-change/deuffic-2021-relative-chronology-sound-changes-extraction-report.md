---
title: The relative chronology of sound changes from Proto-Indo-European to Proto-Celtic
author: Maël Deuffic
date: July 2021
source_type: born-digital
extraction_date: 2026-05-07
source_file: deuffic-2021-relative-chronology-sound-changes.pdf
chunk: extraction-report
---

# Extraction report

## Source identification

- Source type identified as **born-digital PDF**: machine-readable text layer present.
- The raw extracted text layer was used as the primary input.
- Visual inference was used only for the two stop-system table areas where the PDF stores ruled-table layout as positioned text rather than a logical table.
- No scanned-only pages were identified.

## Corrections applied

- Rejoined paragraph line breaks and repaired common line-wrap artifacts.
- Removed running page numbers from the extraction.
- Separated the end bibliography into `deuffic-2021-relative-chronology-sound-changes-bibliography.md`.
- Converted laryngeal indices from text-layer `h1`, `h2`, `h3` artifacts to Unicode subscript forms `h₁`, `h₂`, `h₃` where detected.
- Reconstructed superscript labialization and aspiration from PDF span size/position where present, e.g. `kʷ`, `gʷ`, `bʰ`, `dʰ`, `gʰ`, `gʷʰ`.
- Converted body footnote markers to Markdown footnote references and gathered page footnotes into a terminal `## Footnotes` section.
- Rebuilt the stop-system tables in §2.6.2 as Markdown tables; the PDF presents these as positioned table text, not a semantic table.

## Unresolved issues

- The §2.6.2 stop-system tables were rebuilt as Markdown tables from positioned text; they should be checked against the PDF if used for exact quotation.
- Italic and bold formatting were used for heading detection but were not exhaustively encoded throughout the running text. Character fidelity was prioritized over typographic markup.
- Footnote-marker placement is reconstructed from superscript numerals and may require review in densely footnoted passages.
- Some formulas with complex combining marks, especially syllabic markers and subscript/combining marks adjacent to line breaks, should be checked against the PDF if used for quotation.
- No `[unclear]` markers were inserted because the source text layer was readable; absence of markers should not be read as a certification of perfect character accuracy.

## Confusion-pair report

- `h₁ h₂ h₃`: normalized from laryngeal index text-layer artifacts where detected. Some non-laryngeal `h1/h2/h3` contexts could not be independently audited exhaustively.
- `ā ē ī ō ū`: preserved from the PDF text layer where present. Macrons in dense footnotes and bibliography were not manually checked one by one.
- `ʰ ʷ`: reconstructed from raised small `h`/`w` spans. Contexts in tables and formulas should be reviewed before quotation.
- `ə`: preserved where present; no broad normalization was applied.
- `ṛ ḷ ṃ ṇ`: preserved where present; not exhaustively audited.
- `ǵ ḱ`: preserved where present; not exhaustively audited.
- `*`: preserved where present; no systematic missing-asterisk audit was performed.
- `†`: no dagger usage was identified in the output count.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 67,
    "h2": 101,
    "h3": 38
  },
  "macron_a": 127,
  "macron_e": 145,
  "macron_i": 130,
  "macron_o": 155,
  "macron_u": 51,
  "schwa": 14,
  "greek_chars": 550,
  "combining_diacritics": 297,
  "dagger": 0
}
```

## Structural integrity check

- Logical headings were reconstructed for title/source metadata, table of contents, abbreviations, introduction, numbered sections, conclusion, bibliography, and footnotes.
- Bibliography was separated into its own Markdown file.
- Footnotes were gathered into a terminal footnote section in the main Markdown file.
- The source has no index.
- No embedded figures requiring image extraction were detected beyond the repository-cover image on the first page; the stop-system diagrams are rendered as positioned text/lines and were represented as Markdown tables.
- No `images/` directory was created because no source figures, plates, maps, or image-only tables requiring extraction were identified.

## Image inventory

No extracted images.
