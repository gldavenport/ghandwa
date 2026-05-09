---
title: "Indo-European Poetry and Myth"
author: "M. L. West"
date: "2007"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "west-2007.pdf"
chunk: "extraction report"
---

# west-2007 extraction report
## Source type
Born-digital PDF with machine-readable text layer. Raw extracted text was used as the primary input. Visual rendering was used only for the cover image and the stemmatic diagram on source page 20.
## Corrections applied
- Repaired common ligatures: ﬁ, ﬀ, ﬂ, ﬃ, ﬄ. Count not measured separately.
- Repaired publisher private-use small-cap glyphs into normal Unicode letters/digits.
- Combined extracted spacing diacritics (macron, acute, grave, breve, ring, tilde, dot below, cedilla/ogonek-like marks) with their preceding base characters where possible.
- Applied laryngeal normalization: `h1`, `h2`, and `h3` were converted to `h₁`, `h₂`, and `h₃`.
- Repaired many broken Greek glyphs by using the embedded Greek font encoding differences and composing base vowels/consonants with Greek breathing/accent marks.
- Repaired obvious line-break hyphenation in running text where the next line began with a lowercase letter; preserved hyphens before uppercase letters.
- Removed top/bottom running headers, page-number-only running material, and repeated bibliography/index headers where detected.
## Unresolved issues list
- This is an automated first-pass corpus extraction of a long philological monograph. It has not received a full manual character-by-character visual audit.
- Greek text was repaired through font-encoding maps, but any glyphs encoded inconsistently by the source PDF may remain wrong.
- Some IPA/custom-phonetic glyphs were mapped from embedded glyph names; `hooktopk` was mapped to `ƙ`, which should be checked against the visual source if that form is important.
- Bibliography and index entries were preserved line-by-line; column order should be usable but should be manually checked before treating the index as authoritative.
- Footnotes remain in source-page order rather than being fully converted to Markdown footnote references.
- Remaining private-use characters in output: none.
- Remaining non-whitespace control characters in output: none.
## Confusion-pair report
- `h₁ h₂ h₃`: normalized globally from ASCII laryngeal digits where detected; not manually verified instance-by-instance.
- Macron vowels: combining macrons were normalized to precomposed Unicode where possible; dense Vedic and bibliographic entries may still require spot-checking.
- `ʰ ʷ`: IPA superscript h/w glyphs were mapped from the embedded TimesIPAPhonetic encoding where possible; not fully manually verified.
- `ə`: schwa was mapped from the embedded phonetic font where possible.
- Underdot letters (`ṛ ḷ ṃ ṇ` etc.): dot glyphs were attached below the preceding base character and NFC-normalized where possible; not fully manually verified.
- `ǵ ḱ`: acute combining marks were attached and normalized where possible; not fully manually verified.
- Asterisks before reconstructed forms were preserved from the text layer.
- Dagger: dagger count is approximate; no manual dagger audit was performed.
## Codepoint inventory
Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 20,
    "h2": 45,
    "h3": 4
  },
  "macron_a": 1778,
  "macron_e": 184,
  "macron_i": 389,
  "macron_o": 181,
  "macron_u": 280,
  "schwa": 218,
  "greek_chars": 14151,
  "combining_diacritics": 823,
  "dagger": 3
}
```
## Structural integrity check
- Chunked by the source’s own chapter structure, with bibliography and index separated.
- Each Markdown file has YAML front matter and source-page anchors.
- Headings are generated at chunk level. Internal section headings are generally preserved as source lines rather than aggressively promoted, to avoid false structure from verse, citations, and short formula lines.
- Tables and diagrams in running text were not manually reconstructed as Markdown tables unless available through text extraction.
- Page-boundary text was retained with page anchors; no deliberate omission of continuation text is known.
## Image inventory
- `images/west-2007-cover.jpeg` — cover image, page 1: Front cover image
- `images/west-2007-p20-fig1.png` — unlabeled diagram, page 20: Stemmatic diagram of Indo-European levels
