---
title: "Ten Constraints that Limit the Late PIE Homeland to the Steppes"
author: "David W. Anthony"
date: 2023
source_type: born-digital
extraction_date: 2026-05-07
source_file: anthony-2023-ten-constraints.pdf
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The text layer was used as the primary input. Page rendering was used only to confirm that no figures/tables were present and to spot-check high-risk linguistic forms.

## Corrections applied

- Removed running headers, page numbers, and margin line numbers.
- Rejoined paragraphs across line breaks and page boundaries.
- Repaired line-break hyphenation where the hyphen was only a lineation artifact. Preserved visible lexical hyphenation in compounds such as `Pontic-Caspian`, `Volga-Ural`, `Indo-European`, `Proto-Indo-European`, `Eastern Hunter-Gatherer`, `Indo-Aryan`, `Indo-Iranian`, and `non-IE`.
- Normalized laryngeal index notation from the PDF text layer's ASCII `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃` in linguistic forms.
- Repaired source-specific text-layer spacing in linguistic forms, including `*h₂ek̑s-`, `*g̑ʰ(e)rsd-`, `*h₂erh₃-u̯r̥/n-`, `*se-sh₁-i̯o-`, `*gʷou̯-`, `*h₂melg̑-`, `*h₂u̯l̥h₁néh₂-`, `*h₂ou̯i-`, and `*h₁ek̑u̯o-`.
- Split the article bibliography into a separate Markdown file.

## Unresolved issues list

- No `[unclear]` markers were inserted.
- The text layer is not semantically tagged. Italics and small caps were not exhaustively represented in Markdown; technical characters and logical structure were prioritized over typographic markup.
- The correction of laryngeal indices is systematic but should be considered a normalization pass rather than proof against all possible index errors.
- Bibliographic hanging indentation was used to split references. Entries were checked for obvious boundary failures, but a later bibliography-specific pass could still improve italics and rare hyphenation edge cases.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: ASCII laryngeal digits from the text layer were normalized to subscript digits in output. No remaining `h1`, `h2`, or `h3` sequences are expected, but this is not a proof of complete correctness.
- Macron vowels: retained as Unicode where present in the text layer. No dense index exists.
- Superscript modifier letters `ʰ` and `ʷ`: retained where present in the text layer.
- `ə`: no schwa characters identified.
- Underdot/syllabic and combining marks such as `r̥`, `l̥`, `u̯`, `i̯`, `g̑`, `k̑`: retained and source-specific spacing repaired where detected.
- Palatal notation: the source text layer uses combining notation such as `k̑` and `g̑`; these were preserved rather than silently normalized to `ḱ`/`ǵ`.
- Asterisk before reconstructed forms: retained.
- Dagger: no dagger characters identified.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 5,
    "h2": 15,
    "h3": 4
  },
  "macron_a": 1,
  "macron_e": 0,
  "macron_i": 0,
  "macron_o": 1,
  "macron_u": 0,
  "schwa": 0,
  "greek_chars": 0,
  "combining_diacritics": 16,
  "dagger": 0
}
```

## Structural integrity check

- Main text is a single corpus Markdown file.
- Bibliography is separated as `anthony-2023-ten-constraints-bibliography.md`.
- No index is present in the source.
- No figures, plates, maps, or image-rendered tables were identified by PDF image extraction (`pdfimages -list` returned no embedded images).
- Footnote 1 is retained as a Markdown footnote.
- The main headings are consistent: article title, `1 Introduction`, and `2 Constraints that limit the LPIE homeland to the steppes`.

## Image inventory

No images extracted; no `[image-only ...]` placeholders used.
