---
title: An Umbrian inscription at Poggio Civitate (Murlo) — Extraction report
author: Anthony Tuck / Rex Wallace
date: 2018
source_type: born-digital
extraction_date: 2026-05-07
source_file: tuck-2018-umbrian-inscription.pdf
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The extracted text layer was used as the primary input. Rendered page images were used only to check high-risk characters, the inscription readings, the concordance table, selected bibliography entries, and Fig. 1.

## Corrections applied

- Rejoined paragraphs and repaired line-boundary hyphenation created by PDF extraction, including words such as *subordinate*, *construction*, *Etruscan*, *architectural*, *located*, *uncharacteristic*, *manufactured*, *complete*, *excavated*, *fragment*, *deteriorated*, *subsequent*, *impossible*, *determine*, *interpretation*, *craftsman*, *community’s*, *problematic*, *limited*, *ceramic*, *language*, and *reconstruct*.
- Removed running headers, footers, printed page numbers, and separator rules while retaining page anchors as HTML comments.
- Converted footnotes from page-bottom placement to Markdown footnotes.
- Converted the abbreviation list and concordance into Markdown tables.
- Separated the bibliography into `tuck-2018-umbrian-inscription-bibliography.md`.
- Extracted/raster-cropped Fig. 1 into `images/tuck-2018-umbrian-inscription-fig1.png`.
- Checked the inscription readings on p. 277 visually against the rendered PDF and preserved underdotted forms: ]bịẹḥ[, ]bịẹṇ[, ]bịẹṃ[, ]bịẹp[, ]bịẹṿ[, plus ]bịṿḥ[ in footnote 9.
- Corrected one text-layer extraction error in the bibliography: `Urpsrung` → `Ursprung`, based on the visual rendering.

## Unresolved issues list

- No `[unclear]` markers were inserted.
- No inline `[?]` inferred-character markers were inserted because the source is born-digital and the text layer was generally usable.
- The bibliography appears to print `Hadas-Label, J.` and `provincial di Siena`; these were preserved as printed/source-layer readings rather than silently regularized to expected external forms.
- The toponym `Val d’Ombrono` was preserved as printed/source-layer text.
- This pass cannot exclude errors that are consistent across the source text layer and the visual rendering.

## Confusion-pair report

- `h₁ h₂ h₃`: no instances detected in the output; not applicable beyond this negative check.
- `ā ē ī ō ū`: macron vowels present and counted approximately below. Selected forms checked include `*-ēno-*`, `*gāwiyōy*`, `Vībiēnus`, and `Vībius`.
- `ʰ ʷ`: no instances detected in the output.
- `ə`: no instances detected in the output.
- `ṛ ḷ ṃ ṇ`: underdotted `ṃ` and `ṇ` occur in the inscription readings and were visually checked on p. 277. No `ṛ` or `ḷ` instances detected.
- `ǵ ḱ`: no instances detected in the output.
- `*`: reconstructed forms and suffixes using asterisks were preserved where present, including `*-ēno-*`, `*gāwiyōy`, and `*-ēd`.
- `†`: no instances detected in the output.
- Source-specific high-risk characters checked: underdotted `ị`, `ẹ`, `ḥ`, `ṇ`, `ṃ`, `ṿ`; acute `ú` in `k]aúieh`; macrons in `Vībiēnus`, `Vībius`, `ē-stems`, and `gāwiyōy`; en dashes in page ranges; curly apostrophes/quotation marks.

## Codepoint inventory

Approximate counts, for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 1,
  "macron_e": 4,
  "macron_i": 2,
  "macron_o": 1,
  "macron_u": 0,
  "schwa": 0,
  "greek_chars": 0,
  "combining_diacritics": 0,
  "dagger": 0
}
```

## Structural integrity check

- Headings are consistent with the article’s logical sections.
- Footnotes 1–20 are present and attached as Markdown footnotes.
- The abbreviation list and concordance are well-formed Markdown tables.
- The bibliography has been moved to a separate bibliography file.
- Fig. 1 is referenced at the end of the main Markdown file and its extracted image is present in `images/`.
- No obvious continuation text appears lost at page boundaries in this pass.

## Image inventory

| Output filename | Source label | Page | Caption |
|---|---:|---:|---|
| images/tuck-2018-umbrian-inscription-fig1.png | Fig. 1 | 282 | Fig. 1: Impasto Rim Fragment, PC 19950066 |
