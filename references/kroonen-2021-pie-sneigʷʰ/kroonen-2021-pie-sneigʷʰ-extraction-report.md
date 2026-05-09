---
title: "Proto-Indo-European *sneigʷʰ- ‘to fall down; to snow’ — Extraction Report"
author: "Guus Kroonen; Andrew Wigman; Rasmus Thorsø"
date: "2021"
source_type: born-digital
extraction_date: "2026-05-07"
source_file: "kroonen-2021-pie-sneigʷʰ.pdf"
chunk: extraction-report
---

# Extraction Report

## Source type

Born-digital PDF with a machine-readable text layer. The raw extracted text was treated as primary. Visual rendering was used only to verify glyphs and resolve corrupted/private-use output from the text layer.

The PDF includes a repository/download metadata cover page before the article. That page was not transcribed as part of the article body; its citation data was used only for YAML/source identification. Article text runs from PDF page 2 through PDF page 12, corresponding to article pages 214–224.

## Deliverables produced

- `kroonen-2021-pie-sneigʷʰ.md` — main article text, including footnotes and author contact information.
- `kroonen-2021-pie-sneigʷʰ-bibliography.md` — references section.
- `kroonen-2021-pie-sneigʷʰ-extraction-report.md` — this QC record.
- `manifest.json` — machine-readable manifest and approximate character counts.

No index is present in the source. No source figures, maps, plates, or tables requiring extraction were present. `pdfimages` reported one raster image on the repository cover page; this appears to be repository/decorative metadata-page content rather than an article figure and was omitted.

## Corrections applied

- Rejoined paragraphs broken by PDF lineation and page boundaries.
- Removed running headers, side download notices, page footers, copyright footer lines, and physical page-number repetition from the corpus files.
- Repaired hyphenation across line breaks where the line break was purely typographic, e.g. `un-problematic` → `unproblematic`, `Germanic` split across line boundary, and other PDF line-end splits.
- Converted the source's title-note and numbered footnotes into Markdown footnotes, preserving their content and reconnecting notes split across pages.
- Separated the references section into `kroonen-2021-pie-sneigʷʰ-bibliography.md` according to the extraction instructions.
- Preserved reconstructed-form asterisks as literal `*` characters inside inline HTML italics to avoid Markdown emphasis ambiguity.
- Resolved PDF private-use/corrupted glyph `U+E03B` visually/contextually as `u̯` in the Latin section and bibliography where the glyph represented nonsyllabic `u`.
- Normalized obvious PDF extraction artifacts such as `LIV2` → `LIV²` where the visual source and bibliographic convention clearly use superscript ².

## Unresolved issues list

No `[unclear]` markers were inserted. However, the following items remain appropriate targets for a later character-authoritative pass:

1. The Avestan transliteration `snaēžāt̰`, especially the final combining mark on `t̰`, was preserved from the text layer and spot-checked visually, but a later specialist pass could confirm the exact Unicode representation preferred for the source's transliteration convention.
2. The PUA glyph resolved as `u̯` was visually inferred from the rendered PDF. The output uses decomposed `u` + combining inverted breve below rather than the source font's private glyph.
3. Italic formatting was preserved selectively for reconstructed forms, book/journal titles in the bibliography, and a few visibly italicized source forms. A full span-level font-style extraction was not performed.
4. The repository cover page was intentionally omitted from the corpus body. Its citation metadata is reflected in the manifest/source metadata rather than transcribed as a separate corpus section.

## Confusion-pair report

- `h₁ h₂ h₃`: Output contains subscript laryngeal digits where present in the source (`h₁`, `h₂`). No `h₃` was found. Could not certify every source instance beyond the performed pass.
- `ā ē ī ō ū`: Macron vowels were preserved across body, footnotes, and bibliography. Counts are approximate and a later pass could verify every lexical form.
- `ʰ ʷ`: Superscript modifier letters were preserved in PIE-style roots such as <i>*sneigʷʰ-</i>. Instances in older bibliographic notation using `u̯`/`uʰ` were not silently converted to `ʷʰ`.
- `ə`: Schwa appears in Avestan forms and was preserved.
- `ṛ ḷ ṃ ṇ`: `ṃ` and related Indic diacritics were preserved where present; no exhaustive external verification was performed.
- `ǵ ḱ`: Acute consonants were preserved in forms such as <i>*uoiḱ-o-</i>, <i>*ḱloi-uo-</i>, <i>*ǵʰi-ōm</i>, and <i>*ḱneikʷ-</i>.
- `*`: Reconstructed-form asterisks are preserved as literal U+002A characters, generally inside inline HTML italics.
- `†`: No dagger symbols were found in the article text or bibliography.

## Codepoint inventory

Approximate counts from the generated main and bibliography files:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 2,
    "h2": 3,
    "h3": 0
  },
  "macron_a": 9,
  "macron_e": 14,
  "macron_i": 45,
  "macron_o": 40,
  "macron_u": 12,
  "schwa": 9,
  "greek_chars": 40,
  "combining_diacritics": 6,
  "dagger": 0
}
```

## Structural integrity check

- Headings are consistent with the article's numbered structure: sections 1–9.
- Footnotes are attached as Markdown footnotes and no note text was intentionally left in page-flow position.
- References are separated into a standalone bibliography file.
- No tables, paradigms, figures, maps, plates, or index sections appear in the article.
- Page/source anchors were inserted as HTML comments at article page transitions where useful for later checking.

## Image inventory

No article figures, diagrams, maps, plates, or tables rendered as images were extracted. No `[image-only...]` placeholders were used.
