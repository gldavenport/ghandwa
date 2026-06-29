---
title: "Extraction report — Reconstructing Proto-Italo-Celtic"
author: "Cid Swanenvleugel"
date: "2021-06-28"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "swanenvleugel-2021-reconstructing-proto-italo-celtic.pdf"
chunk: "extraction-report"
---

# Extraction report

## Source type

Born-digital PDF. The PDF has a machine-readable text layer and was created with Microsoft Word for Microsoft 365. The raw text layer was the primary input. Visual/layout inspection and span metadata were used for table reconstruction, headings, superscript aspiration/labialization, and laryngeal-digit normalization.

## Deliverables produced

- `swanenvleugel-2021-reconstructing-proto-italo-celtic.md` — main clean Markdown extraction, excluding the reference list.
- `swanenvleugel-2021-reconstructing-proto-italo-celtic-bibliography.md` — references extracted as a separate bibliography file.
- `manifest.json` — machine-readable extraction metrics.
- `swanenvleugel-2021-reconstructing-proto-italo-celtic-extraction-report.md` — this extraction report.

No separate image files were produced. The source contains text tables but no extractable figures, maps, plates, or image-only tables requiring an `images/` directory.

## Corrections applied

- Removed page numbers and blank spacer lines.
- Rejoined paragraph lines and repaired common line-break hyphenation.
- Normalized laryngeal digits exposed as visual subscripts in the PDF (`h1`, `h2`, `h3`, `H1`, `H2`, `H3`) to Unicode subscript digits (`h₁`, `h₂`, `h₃`, `H₁`, `H₂`, `H₃`) where detected.
- Converted small superscript `h` and `w` spans to modifier letters `ʰ` and `ʷ` in forms such as `*dʰ`, `*bʰ`, `*kʷ`, and `*gʷ`.
- Normalized text to Unicode NFC where possible, while preserving decomposed combining sequences when no precomposed equivalent exists.
- Reconstructed the nineteen numbered tables as Markdown tables from the PDF layout/text layer.
- Reconstructed Appendix A and Appendix B tables manually from the rendered/text layout because the PDF text layer collapsed table columns.
- Separated the bibliography into its own Markdown file and joined wrapped bibliography entries using indentation in the PDF text layer.

## Unresolved issues list

- The extraction does not assert character-authoritative status. A later pass should compare dense linguistic forms against rendered page images if this is going to be used as a citable lexical/phonological dataset.
- Italic/bold styling was not exhaustively represented in the main text. Technical characters and notation were prioritized over font-style encoding.
- Some table reconstructions required layout-based repair. They should be spot-checked against pages 16, 18–19, 23, 27, 35, 40, 42–43, 51, 55, 58, 63–64, and 68–70.
- Footnotes were retained in reading order rather than converted to formal Markdown footnote syntax. They should be usable for corpus search, but a later pass could make them cleaner.
- The PDF occasionally encodes scholarly notation through visual positioning rather than Unicode characters. The normalization pass catches common patterns but may miss rare cases.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: normalized by regex and span inspection; remaining ASCII `h1/h2/h3` instances may still exist if separated by unusual markup.
- Macron vowels: normalized to NFC where possible; complex combinations such as macron plus breve may remain decomposed.
- `ʰ ʷ` vs. `h w`: common superscript span cases converted; unstyled baseline `h/w` in prose or source notation were not blindly converted.
- `ə`: preserved where present in the text layer.
- Underdot/syllabic markers: preserved where present; dense table cells should be spot-checked.
- `ǵ ḱ`: preserved or normalized where the text layer exposed combining acute sequences; spot-checking recommended in reconstructed forms.
- `*`: preserved before reconstructed forms where present in the text layer.
- `†`: no dagger instances were observed in the output counts.

## Codepoint inventory

All counts are approximate and intended for cross-pass comparison only.

```json
{
  "laryngeals": {
    "h1": 75,
    "h2": 102,
    "h3": 25
  },
  "macron_a": 204,
  "macron_e": 259,
  "macron_i": 149,
  "macron_o": 76,
  "macron_u": 24,
  "schwa": 25,
  "greek_chars": 127,
  "combining_diacritics": 192,
  "dagger": 0
}
```

## Structural integrity check

- Headings were reconstructed from the source's visual/text hierarchy and numbered section labels.
- Numbered tables were rebuilt as Markdown tables and placed at their source locations.
- Appendices A–C were retained, with Appendix A/B table structure repaired.
- References were separated into `swanenvleugel-2021-reconstructing-proto-italo-celtic-bibliography.md`.
- No index section was present in the source.
- No image-only figures or plates were identified.

## Image inventory

No `[image-only...]` placeholders were used. No images were extracted.
