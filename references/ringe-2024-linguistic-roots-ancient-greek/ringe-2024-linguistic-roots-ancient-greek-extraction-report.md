---
title: "The Linguistic Roots of Ancient Greek — extraction report"
author: "Don Ringe"
date: "2024"
source_type: born-digital
extraction_date: "2026-05-07"
source_file: "ringe-2024-linguistic-roots-ancient-greek.pdf"
chunk: "extraction-report"
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The extraction used the text layer as the primary source. Visual rendering was consulted only for representative character-position behavior: superscript aspiration/labialization and subscript laryngeal digits were detectable from font size and vertical position.

## Corrections applied

- Converted the PDF text-layer mathematical asterisk `∗` to ordinary reconstructed-form asterisk `*` per the attached extraction instructions.
- Converted visually superscripted aspiration and labialization spans to modifier letters where detected: `ʰ`, `ʷ`, and occasional related superscripts.
- Converted visually subscripted laryngeal digits to Unicode subscripts: `h₁`, `h₂`, `h₃`.
- Applied fallback laryngeal normalization to any remaining whole-span `h1`, `h2`, `h3` sequences.
- Applied Unicode NFC normalization.
- Repaired common PDF ligature extraction artifacts (`fi`, `fl`, `ff`, `ft`) produced by the Oxford Scholarship Online PDF text layer.
- Repaired common split diaeresis artifacts such as `u¨` to `ü` where they occurred in the text layer.
- De-converted false superscript artifacts in the frontmatter file where the PDF text layer merged large headings with smaller ordinary prose.
- Removed running headers, page numbers, the cover page OCR/text noise, recurring Oxford DOI/copyright footer lines, and Oxford Scholarship Online navigation/link artifacts such as Google Scholar/WorldCat link labels.
- Rejoined clear alphabetic hyphenation across line breaks conservatively.

## Unresolved issues

- This is an automated first-pass extraction. Dense paradigm tables, especially in §2.3.3(vi), are not guaranteed to preserve column structure correctly. Some paradigms should be checked against page images or a later table-specific pass.
- Some Greek text-layer characters appear as source-specific mixed forms such as Latin `o` inside Greek words or epsilon-like `ɛ` with macron markers. These were not silently normalized because the extraction priority was character preservation.
- Footnotes are preserved in reading order near the page location, but not converted into full Markdown footnote syntax.
- Italics/bold/small caps are not systematically marked in Markdown; the text content and character fidelity were prioritized.
- Bibliography and index entries were extracted from the text layer, but the dense index may require a second pass for one-entry-per-line validation and diacritic spot-checking.
- No inline `[?]` inferred-character markers were inserted because this was not treated as a scanned-only source. Characters transformed from text-layer positional evidence are not certified; they should be regarded as mechanically inferred from the PDF text layer and glyph positions.

## Confusion-pair report

- `h₁ h₂ h₃`: Normalization was applied, but not every instance was visually verified.
- Macron vowels: Unicode NFC normalization was applied. Macrons in dense index/bibliography sections were not fully verified against rendering.
- `ʰ ʷ`: Positional superscript conversion was applied. Some residual ordinary `h`/`w` may remain where the PDF text layer did not expose superscript spans or where conversion would have risked false positives.
- `ə`: No special schwa repair was applied beyond preserving text-layer characters.
- Underdot/syllabic marks: Preserved from text layer where exposed; not fully visually verified.
- `ǵ ḱ`: Preserved from text layer where exposed; not fully visually verified.
- `*`: Mathematical asterisk was normalized to ASCII `*`.
- `†`: Preserved if present; not fully checked.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 1163,
    "h2": 1351,
    "h3": 242
  },
  "macron_a": 536,
  "macron_e": 193,
  "macron_i": 180,
  "macron_o": 117,
  "macron_u": 45,
  "schwa": 45,
  "greek_chars": 44847,
  "combining_diacritics": 1963,
  "dagger": 0
}
```

## Structural integrity check

- Output is chunked by the source's own chapters and sections, with bibliography and index separated.
- README lists all output files, source labels, page ranges, and coverage.
- Page anchors are included as HTML comments.
- Headings are converted to Markdown where section headings were detected.
- Tables/paradigms are structurally fragile in this pass and should be treated as requiring table-specific QA.

## Image inventory

No embedded source figures were extracted as separate image files in this pass. Figure 2.1 appears as text/vector content rather than a discrete image; it is represented in the text extraction rather than as an `images/` asset.
