---
title: "LIV: Lexikon der indogermanischen Verben. Die Wurzeln und ihre Primärstammbildungen. Zweite, erweiterte und verbesserte Auflage"
author: "Helmut Rix; Martin Kümmel; Thomas Zehnder; Reiner Lipp; Brigitte Schirmer"
date: "2001"
source_type: mixed
extraction_date: "2026-05-07"
source_file: "rix-2001-liv².pdf"
chunk: "extraction-report"
---

# Extraction Report

## Source type

Mixed/scanned ClearScan PDF: the file contains scanned page images plus an OCR/ClearScan text layer. The extraction used the OCR text layer as the primary input and rendered page images for spot checks of representative lexical pages and section labels. This is not a born-digital source, and the OCR layer is visibly lossy for the highest-risk characters.

## Corrections applied

- Converted ClearScan U+00AD soft-hyphen codepoints to visible ASCII hyphens to avoid dropping root-final hyphens and line-break hyphens.
- Replaced Unicode replacement characters with `[unclear]`.
- Applied narrow laryngeal normalization for obvious OCR/text-layer forms: `h1` → `h₁`, `h2` → `h₂`, `h3` → `h₃`, and `h;z` → `h₂`.
- Repaired standard `ﬁ`/`ﬂ` ligatures if present.
- Preserved fixed-width page blocks rather than aggressively reflowing the lemmata, bibliography, or indices, because the source uses dense aligned lexical columns and OCR reflow would risk dropping forms.

## Unresolved-issues list

- `1440` `[unclear]` markers remain where the OCR/text layer emitted replacement characters. These require page-image verification.
- Superscript aspiration and labialization in reconstructed forms are not globally normalized; many instances remain as source/OCR approximations such as `bh`, `dh`, `gh`, `gY`, `kY`, or similar. These require a targeted character pass against rendered page images.
- Greek is OCR-derived and visibly lossy in sample pages (`<p`, `µ`, `az`-type confusions occur). Greek forms require a dedicated Greek pass before treating this as character-authoritative.
- Dense indices are extracted as fixed-width page blocks. They are useful for search, but headword/page-number integrity still requires an index collation pass.
- Some section labels were supplied from visual/TOC checks for chunk headings; the body text remains OCR-layer based.

## Confusion-pair report

| Confusion item | Status |
|---|---|
| `h₁ h₂ h₃` vs `h1 h2 h3` | Obvious OCR forms were normalized; 0 ASCII `h[123]` patterns remain and may include false positives or missed laryngeals. |
| `ā ē ī ō ū` macrons | OCR layer preserves some macrons but also drops or substitutes many; not fully verified. |
| Macron consistency in indices | Not verified; index pass recommended. |
| `ʰ ʷ` vs `h w` | Not globally verified; many aspirates/labiovelars remain in OCR approximations. |
| `ə` vs `e` or `9` | Not globally verified. |
| Underdot letters `ṛ ḷ ṃ ṇ` | Not globally verified. |
| `ǵ ḱ` vs ASCII/acute approximations | Chunk headings use Unicode labels, but body text remains OCR-derived and not globally verified. |
| Asterisk before reconstructed forms | Preserved where OCR captured it; omissions in the OCR layer were not globally repaired. |
| Dagger `†` | Counted but not semantically verified. |

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 1319,
    "h2": 1987,
    "h3": 463
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

- Files are chunked by source divisions and major lemma initial sections.
- Bibliography and indices are separate files.
- Each content file has YAML front matter and page anchors.
- Tables/lexical alignments were preserved as fixed-width text blocks rather than converted to Markdown tables because automatic table conversion would be unsafe for this OCR layer.
- Footnotes remain in page order inside the page blocks. Their attachment to individual lemmata is generally visible but not independently verified.
- No continuation-loss check can be certified; page boundary text appears retained in the OCR layer, but not fully verified.

## Image inventory

No source figures, maps, plates, or diagrams were extracted as separate images. The PDF consists of scanned page images, but those page images were not duplicated into `images/` because they are the source pages rather than figures embedded in the text.

## Recommended further passes

1. Character-authority pass for reconstructed forms: normalize superscript aspiration, labiovelars, palatals, laryngeals, syllabics, and accented vowels against rendered page images.
2. Greek pass for all Greek strings and Hesychius/gloss material.
3. Index collation pass: one headword per line, with headword/page-number validation.
4. Entry-heading pass: verify every lemma headword at the top of each lexical entry, because OCR frequently missed or damaged bold headwords.
