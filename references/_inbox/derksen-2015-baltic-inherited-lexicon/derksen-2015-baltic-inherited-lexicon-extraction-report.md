---
title: "Etymological Dictionary of the Baltic Inherited Lexicon"
author: "Rick Derksen"
date: "2015"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "derksen-2015-baltic-inherited-lexicon.pdf"
chunk: "extraction-report"
---

# Etymological Dictionary of the Baltic Inherited Lexicon — Extraction Report

## Source type

Born-digital PDF. A machine-readable text layer is present on the substantive pages. The extraction used the text layer as the primary input, with limited visual/metadata correction for the author name and source identification. The text layer is imperfect for Greek/polytonic material, laryngeal subscripts, some Baltic/Slavic accented characters, and a small number of symbols.

## Corrections applied

- Removed discretionary soft hyphens: approximately 395.
- Repaired text-layer right-arrow encodings `-+`, `->`, and `--+` to `→`: approximately 1912.
- Normalized plain laryngeal indices `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃`: approximately 613.
- Replaced micro sign `µ` with Greek small mu `μ` as a common text-layer encoding artifact.
- Replaced U+FFFD replacement characters with `[unclear]`: approximately 326.
- Removed running headers/page-number lines where recognized: approximately 663.
- Promoted detected lexical headwords to Markdown level-3 headings: approximately 2056.
- Bolded recognized lexicographic field labels such as LITH, LATV, OPR, BSL, PSL, SL, PIE, and IE: approximately 7826.
- Split index columns into one entry per line where possible: approximately 12383 column splits.

## Unresolved issues

- `[unclear]` markers remain in the output: approximately 325. These mostly reflect malformed or unmapped glyphs in the PDF text layer rather than illegible page images.
- Greek and polytonic Greek forms were not fully repairable from the text layer. Some forms remain partially corrupted, especially where the PDF emitted replacement characters or ASCII approximations.
- Some laryngeal subscript digits were normalized from plain text, but spacing introduced by the text extractor around subscripted material may remain in some reconstructed forms.
- Some tone/accent digits and Baltic/Slavic special characters are preserved as emitted by the text layer; not every instance was visually checked.
- The index was column-split automatically. It should be treated as search-helpful, not as a final typographic reproduction.
- The extraction is corpus-ready for search and reference discovery, but not character-authoritative for Greek/polytonic forms or every dense index entry without additional targeted passes.

## Confusion-pair report

| Item | Status |
|---|---|
| `h₁ h₂ h₃` vs. `h1 h2 h3` | Plain `h1/h2/h3` were normalized globally. Residual spacing around laryngeals may remain. |
| Macron vowels | Unicode macron vowels are preserved where the text layer emitted them. Some dense index entries may still have dropped or malformed macrons. |
| Superscript `ʰ ʷ` | Not fully verified; the text layer often emitted plain `h/w` or damaged symbols in technical forms. |
| `ə` schwa | Not fully verified; source text layer did not consistently expose this distinction. |
| Underdot consonants/vowels | Not fully verified. Any source glyphs emitted as replacement characters are marked `[unclear]`. |
| `ǵ ḱ` vs. ASCII approximations | Not fully verified. |
| Asterisk before reconstructed forms | Preserved where emitted by text layer. |
| Dagger `†` | Counted approximately; not visually audited. |

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "h1": 206,
  "h2": 308,
  "h3": 99,
  "macron_a": 0,
  "macron_e": 0,
  "macron_i": 0,
  "macron_o": 0,
  "macron_u": 1460,
  "schwa": 0,
  "greek_chars": 232,
  "combining_diacritics": 0,
  "dagger": 0
}
```

## Structural integrity check

- Headings: output follows the source’s front matter/introduction/dictionary/references/index structure and chunks dictionary entries by language and letter section.
- Footnotes: footnote text is preserved inline where emitted by the text layer, but footnote attachment was not manually audited page by page.
- Tables: front-matter abbreviation and index-like tables were retained as line-based Markdown text rather than fully normalized Markdown tables where table conversion would risk character loss.
- Page boundaries: page anchors were inserted. Soft hyphenation and obvious page headers were removed; no guarantee is made that all continuation text is perfectly joined.

## Image inventory

No figures, maps, plates, or semantically necessary image-only tables were identified for extraction. Cover and decorative publisher elements were not extracted as corpus images.
