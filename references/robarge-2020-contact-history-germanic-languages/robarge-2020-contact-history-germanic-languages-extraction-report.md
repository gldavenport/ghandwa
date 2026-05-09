---
title: Contact and the History of Germanic Languages — Extraction Report
author: Paul Roberge
date: 2020
source_type: born-digital
extraction_date: 2026-05-07
source_file: robarge-2020-contact-history-germanic-languages.pdf
---

# Extraction Report

## Source classification

Born-digital PDF with a machine-readable text layer. The raw extracted text was used as the primary input. Rendered page images were spot-checked for title structure, headings, bibliography layout, and several high-risk linguistic forms.

## Output files

- `robarge-2020-contact-history-germanic-languages.md` — clean corpus Markdown, main article text only.
- `robarge-2020-contact-history-germanic-languages-bibliography.md` — separate bibliography.
- `robarge-2020-contact-history-germanic-languages-extraction-report.md` — this QC record.
- `manifest.json` — machine-readable extraction metrics.

## Corrections applied

- Removed running heads, printed page numbers, first-page publication footer, and decorative layout.
- Rejoined line-broken prose and line-broken bibliography entries.
- Reconstructed paragraph breaks from the layout extraction's paragraph indentation.
- Separated the bibliography from the main article text.
- Normalized decomposed macron vowels to precomposed Unicode characters where the source visibly uses macron vowels, including `ē`, `ā`, `ī`, and `ǣ`.
- Corrected text-layer artifacts checked against rendered pages or source context, including `subsratum` → `substratum`, `mǣ ce`/`mǣ ce` → `mǣce`, `μáχαιρα` → `μάχαιρα`, `κáνναβις` → `κάνναβις`, `ē1`/`ē1` → `ē₁`, `*rı̄k‐` → `*rīk‐`, `rīhhi` forms, `*ı̄sarna‐` → `*īsarna‐`, `*a.̄` → `*ā`, stem-marker/gloss spacing after `‐`, and `dǫnsk` → `dǫnsk`.
- Applied Unicode NFC normalization across output files.

## Unresolved issues

- No `[unclear]` markers were inserted.
- No `[?]` inferred-character markers were inserted. The PDF was born-digital and the correction pass treated clear text-layer artifacts as extraction repairs rather than unresolved visual inference.
- Italics and small caps were not exhaustively reconstructed from font spans. The extraction prioritizes characters and clean corpus text over full typographic reconstruction.
- The bibliography was reflowed into one entry per paragraph. This should be useful for search, but a further bibliographic pass could add italics or structured fields if needed.

## Confusion-pair report

- `h₁ h₂ h₃`: no laryngeal forms were found in the output.
- `ā ē ī ō ū`: macron vowels were normalized to precomposed characters where detected. Remaining errors are possible in dense bibliography/title material.
- Superscript `ʰ ʷ`: no clear instances were found.
- `ə`: no instances found.
- Underdot consonants/vowels: no clear instances found.
- `ǵ ḱ`: no instances found.
- Asterisk `*`: reconstructed forms with asterisks were preserved in the main text.
- Dagger `†`: no instances found.
- Source-specific high-risk items checked: `ē₁`, `mǣce`, `māki`, `mēki`, `*rīk‐`, `rīhhi`, `*īsarna‐`, `dǫnsk`, Greek `μάχαιρα`, and Greek `κάνναβις`.

## Codepoint inventory

All counts are approximate and intended for cross-pass comparison only.

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 4,
  "macron_e": 8,
  "macron_i": 4,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 0,
  "greek_chars": 15,
  "combining_diacritics": 1,
  "dagger": 0
}
```

## Structural integrity check

- Headings were converted to Markdown heading levels for the article title, numbered sections, and numbered subsections.
- No tables, figures, maps, plates, or extracted embedded images were detected.
- No footnotes/endnotes were detected.
- Bibliography is in a separate file, with one reference entry per paragraph.
- A spot check found no retained running headers or printed page-number-only lines in the main text.

## Image inventory

No figures or embedded images were extracted.
