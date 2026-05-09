---
title: "The derivational history of Greek ἵππος and ἱππεύς"
author: "Michiel de Vaan"
date: "2009"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "vaan-2009-ἵππος.pdf"
chunk: "extraction-report"
---

# Extraction report: vaan-2009-hippos

## Source type

Born-digital PDF with a machine-readable text layer. The text layer was used as the primary input. Visual rendering was used as a fallback for corrupted custom-font Greek and scholarly characters.

## Corrections applied

- Removed running headers, footers, page numbers, repeated journal title lines, and decorative page layout.
- Rejoined broken lineation and page-boundary text.
- Split the bibliography into `vaan-2009-hippos-bibliography.md` as required for single-file article extraction.
- Normalized laryngeals from ASCII h1/h2/h3 to h₁/h₂/h₃ where detected.
- Repaired common custom-font Greek encodings in the source text layer, including `·ppow` → `ἵππος`, `ﬂppeÊw` → `ἱππεύς`, and multiple Greek forms in the article's lists.
- Repaired several high-risk Sanskrit/Indo-European characters visible in the rendering, including ś, ṣ, ṛ, ʰ, ʷ, and m̥ in selected forms.
- No image files were extracted; the article contains no figures, maps, plates, or image-only tables.

## Unresolved issues list

- The PDF uses custom fonts for Greek and some linguistic characters. The text layer is corrupt in those spans; many repairs were made by visual fallback, but this pass should not be treated as character-authoritative for every Greek form.
- A small number of PIE technical forms involving syllabic resonants, palatovelars, and superscript glide/aspiration signs were repaired where clear, but not every occurrence could be fully verified against the page image.
- The phrase involving Greek `ἴσθι` and the later phrase involving the accent of `ἵππος` were reconstructed from the visual rendering because the text layer dropped or corrupted those words.
- Bibliographic italics were not encoded as Markdown italics; the bibliography is clean text rather than typographically diplomatic text.
- No `[unclear]` markers were inserted in the main files because uncertain repairs were tracked here rather than interrupting corpus text.

## Confusion-pair report

- h₁/h₂/h₃ vs. h1/h2/h3: normalized broadly; a later pass should verify that no non-laryngeal h+digit sequence was affected.
- Macron vowels: several visible Latin/Sanskrit macrons were preserved or repaired, but full verification was not exhaustive.
- Superscript ʰ/ʷ: repaired in selected PIE forms; not all candidate forms were exhaustively verified.
- ə: no clear schwa instances identified in this article body.
- ṛ/ḷ/ṃ/ṇ: repaired selected ṛ and m̥ cases; no full audit of every Indic form was performed.
- ǵ/ḱ: repaired selected dḱ/dǵ cases; not fully audited.
- Asterisk U+002A: preserved before reconstructed forms where present in the text layer.
- Dagger †: no dagger instances identified.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 49,
    "h2": 15,
    "h3": 2
  },
  "macron_a": 4,
  "macron_e": 0,
  "macron_i": 1,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 0,
  "greek_chars": 659,
  "combining_diacritics": 7,
  "dagger": 0
}
```

## Structural integrity check

- Logical article structure is preserved as a single main Markdown file with numbered section headings.
- Bibliography is separated into its own Markdown file.
- The article has no index.
- The article has no figures or image-only tables.
- No continuation text appears intentionally omitted at page boundaries, but the custom-font spans remain the main weak point.

## Image inventory

No images extracted; no image placeholders used.
