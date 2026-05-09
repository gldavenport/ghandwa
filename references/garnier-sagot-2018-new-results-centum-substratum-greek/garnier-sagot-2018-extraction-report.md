---
title: "New results on a centum substratum in Greek: the Lydian connection — Extraction Report"
author:
  - "Romain Garnier"
  - "Benoît Sagot"
date: "2018"
source_type: born-digital
extraction_date: "2026-05-07"
source_file: "garnier-sagot-2018.pdf"
chunk: extraction-report
---

# Extraction Report

## Source type

Born-digital PDF with a machine-readable text layer. The PDF is two pages: a HAL cover page followed by the article/abstract page. The raw text layer was used as the primary input, with visual rendering and font-size/span inspection used to check high-risk linguistic characters.

## Deliverables produced

- `garnier-sagot-2018.md` — main clean corpus Markdown, excluding the selected references section.
- `garnier-sagot-2018-bibliography.md` — selected references section.
- `garnier-sagot-2018-extraction-report.md` — this QC record.
- `manifest.json` — machine-readable extraction metrics.

No index is present. No non-decorative figures, diagrams, maps, plates, or image-rendered tables are present.

## Corrections applied

- Rejoined line-wrapped and hyphenated text from the PDF extraction, including HAL cover-page line breaks and bibliography continuation lines.
- Converted the raw text-layer `µ` in `µόλυβδος` to Greek `μ` in `μόλυβδος`; this is treated as a Greek-codepoint repair in a Greek lexical item, not as a semantic normalization.
- Converted the raw text-layer `ǝ` (U+01DD LATIN SMALL LETTER TURNED E) in `/marǝwđa/` to IPA schwa `ə` (U+0259) in `/marəwđa/`.
- Converted the reduced-size text-layer `w` in `*morgwiyo-` to superscript modifier `ʷ` in `*morgʷiyo-`, based on the PDF span data and visual rendering.
- Preserved Greek beta-symbol forms `καλύϐη` and `κολοϐός` as `ϐ` where present in the source text layer.
- Preserved `pirus` as printed in `pirus amygdaliformis`; no taxonomic modernization was applied.
- Moved `SELECTED REFERENCES` to the separate bibliography file required by the extraction instructions.
- Decorative HAL logo/authorization graphics were not extracted as corpus images.

## Unresolved issues list

No `[unclear]` or `[?]` markers were inserted. The three codepoint-level repairs above should still be considered the main human-review points because they depend on distinguishing intended scholarly characters from PDF text-layer encoding artifacts.

## Confusion-pair report

- `h₁ h₂ h₃`: no instances found.
- `ā ē ī ō ū`: Latin macron vowels found only where expected in forms such as `*lūda-`; no dropped macrons identified in the short text.
- Superscript `ʷ`: one instance restored in `*morgʷiyo-`; no other reduced-size `w` in the text layer appeared to require conversion.
- `ə`: one instance restored in `/marəwđa/` from raw `ǝ`.
- `ṛ ḷ ṃ ṇ`: no instances found.
- `ǵ ḱ`: no instances found.
- `*`: reconstructed-form asterisks preserved where present.
- `†`: no instances found.
- Source-specific `μ`/`µ`: one micro-sign instance in a Greek word was repaired to Greek `μ`.
- Source-specific `β`/`ϐ`: `β` and `ϐ` were not merged; the text-layer distinction was preserved.

This QC pass cannot certify that no consistent source-wide error remains.

## Codepoint inventory

Approximate counts below cover `garnier-sagot-2018.md` and `garnier-sagot-2018-bibliography.md` together.

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
  "macron_u": 1,
  "schwa": 1,
  "greek_chars": 87,
  "combining_diacritics": 0,
  "dagger": 0,
  "superscript_w": 1,
  "micro_sign": 0,
  "turned_e_u01dd": 0
}
```

## Structural integrity check

- Headings are consistent and source-derived sections are separated clearly.
- The HAL cover-page citation block is retained in the main Markdown as source metadata.
- The article/abstract text is extracted as running prose with the two source bullet points preserved as Markdown bullets.
- The selected references section is separated into `garnier-sagot-2018-bibliography.md`.
- No footnotes, tables, index, or appendices are present.
- No continuation text appears lost at the page boundary between HAL cover page and article page.

## Image inventory

No non-decorative article images were extracted. Page 1 contains decorative HAL/open-science and authorization graphics; these were excluded from the corpus package. The manifest therefore uses an empty `images` list.
