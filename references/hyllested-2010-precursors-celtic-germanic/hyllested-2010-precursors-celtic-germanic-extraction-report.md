---
title: "The Precursors of Celtic and Germanic — Extraction Report"
author: "Adam Hyllested"
date: 2010
source_type: scanned
extraction_date: 2026-05-07
source_file: "hyllested-2010-precursors-celtic-germanic.pdf"
chunk: extraction-report
---

# Extraction report

## Source type

Scanned-only PDF. The uploaded PDF has no usable machine-readable text layer. Text was extracted from rendered page images using OCR, then lightly cleaned into corpus Markdown.

Because the whole source is scanned, all characters ultimately required visual/OCR inference. I did **not** mark every character inline with `[?]`, because doing so would make the corpus file unusable. Inline uncertainty markers are reserved here for explicit unresolved readings; global scan/OCR uncertainty is recorded in this report.

## Output files

- `hyllested-2010-precursors-celtic-germanic.md` — main text, source pages 107–124.
- `hyllested-2010-precursors-celtic-germanic-bibliography.md` — references, source pages 125–128.
- `hyllested-2010-precursors-celtic-germanic-extraction-report.md` — this QC report.
- `manifest.json` — machine-readable extraction metrics.

No figures, maps, diagrams, or plates were identified.

## Corrections applied

- Rendered the PDF pages to images at 300 DPI for OCR.
- Used OCR with English + Latin models where feasible, because this gave better recovery of Latin-script diacritics than English-only OCR.
- Removed running page headers such as `The Precursors of Celtic and Germanic 109` and `110 Adam Hyllested`.
- Removed the page-1 bibliographic footer from the main text because the information is represented in YAML/source metadata.
- Rejoined most line-broken prose paragraphs.
- Converted major section headings into Markdown headings.
- Separated the bibliography into its own Markdown file.
- Applied a conservative replacement pass for repeated OCR errors, including `PGme.`/`PGmce.` → `PGmc.`, `Olr.` → `OIr.`, `Mlr.`/`Mir.` → `MIr.`, `Riibekeil` → `Rübekeil`, and repeated bibliography diacritic repairs.

## Unresolved issues list

- The source is scanned and OCR-heavy. A second pass against page images is warranted before treating reconstructed forms, Greek, and less common diacritics as character-authoritative.
- Greek text is not fully verified. Several Greek words were OCRed into mixed Latin/Greek characters and should be manually checked.
- Old Norse/Icelandic characters such as `ð`, `þ`, and `ǫ`, and Irish/Brittonic forms with accents, may be under-recovered or misrecognized.
- Superscript/subscript and special phonological notation may not be fully preserved. In particular, laryngeal subscripts, superscript aspiration/labialization, and reconstructed PIE notation should be manually checked.
- Footnotes are preserved near their source-page locations but were not fully normalized into Markdown backlink footnote syntax.
- The list of 96 lexical items appears structurally preserved, but dense item-level forms require a character-fidelity pass.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: no reliable laryngeal-subscript recovery was confirmed. Potential laryngeal forms should be manually checked.
- `ā ē ī ō ū`: macron vowels were partly recovered, but macron loss is likely in dense forms.
- Macron consistency across body/notes/bibliography: not fully verified.
- `ʰ ʷ`: not verified; OCR likely reduced some modifier-letter notation.
- `ə`: no reliable schwa inventory confirmed.
- `ṛ ḷ ṃ ṇ`: not verified; OCR may have dropped underdots if present.
- `ǵ ḱ`: not verified.
- `*`: asterisks are broadly preserved, but some item-initial or line-initial asterisks may have been dropped or confused.
- `†`: no dagger inventory confirmed.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 0,
  "macron_e": 0,
  "macron_i": 0,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 0,
  "greek_chars": 0,
  "combining_diacritics": 0,
  "dagger": 0
}
```

## Structural integrity check

- Main section headings are represented consistently.
- Lexical categories and A/B/C subgroup headings are represented as Markdown headings.
- The bibliography is separated from the main text.
- No image inventory is included because no figures or plates were identified.
- Continuation across page boundaries was preserved by source-page anchors, but page-boundary joins should be reviewed in a second pass.

## Recommended further passes

1. Character-fidelity pass over reconstructed forms, Greek, Old Irish, Old Norse, Gothic, Sanskrit, Baltic, and Uralic forms.
2. Footnote normalization pass converting note text to Markdown footnotes and checking note numbers against callouts.
3. Bibliography pass against page images for names, accented titles, journal abbreviations, page ranges, and publisher/location strings.
4. Lexical-item audit confirming item numbers 1–96 are complete and internally ordered.
