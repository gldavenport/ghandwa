# cooper-2015 extraction report

## Source type

Born-digital PDF with a machine-readable text layer. No OCR was performed. The text layer was treated as the primary source, with limited visual/image fallback only for the cover and the source-page 209 syllable-structure diagram.

## Corrections applied

- Removed running headers, standalone page numbers, copyright/DOI running lines, and blank pages where detected.
- Rejoined obvious line-break hyphenation conservatively; compound hyphens such as Indo-European, Proto-Indo-European, word-initial, and syllable-structure were preserved where the pattern was detectable.
- Repaired common ligatures: ﬁ → fi and ﬂ → fl.
- Corrected the title-page text-layer artifact `Βy` → `By`.
- Normalized laryngeal indices globally: h1/h2/h3 → h₁/h₂/h₃ and H1/H2/H3 → H₁/H₂/H₃.
- Repaired several unmapped Brill/PDF glyph controls where context was clear: U+0016 → combining acute in Vedic long-vowel forms; U+0088 → combining macron in `V̄CCV`; U+0010/U+008A/U+0090 deleted where they interrupted already present Greek/Vedic combining accents; BEL U+0007 rendered as `•` in table-like contexts.
- Normalized several constraint-name spacing artifacts, e.g. `*Complex Onset` → `*ComplexOnset`, `*Complex Coda` → `*ComplexCoda`, and `No Coda` → `NoCoda`.
- Extracted the cover illustration and the source-page 209 syllable-structure diagram image into `images/`.

## Unresolved issues list

- Several OT tableaux and syllable-structure diagrams are reconstructed from the PDF text layer and may require a targeted visual/tableau pass for exact row/column geometry.
- Example (43) on source page 209 is included as an extracted image because the text layer alone does not fully preserve the syllable-tree geometry.
- Index entries with stacked Greek/Vedic diacritics were normalized only where obvious control-character corruption occurred; these remain high-risk for a later index-only pass.

## Confusion-pair report

- h₁/h₂/h₃: ASCII h1/h2/h3 were normalized to subscript laryngeals. This was applied globally and should be spot-checked in bibliographic URLs or non-linguistic contexts if strict diplomatic fidelity is later required.
- ā/ē/ī/ō/ū: macronized vowels were preserved where the text layer exposed them. A few stacked accent/macron sequences required inferred control-character repair and remain high-risk.
- ʰ/ʷ: modifier-letter aspiration/labialization was preserved where present in the text layer; no full visual audit was performed.
- ə: schwa was preserved where present in the text layer.
- ṛ/ḷ/ṃ/ṇ and related Indic transliteration: preserved where present, but dense tables and index entries remain high-risk.
- ǵ/ḱ: preserved where present; no full form-by-form visual audit was performed.
- *: asterisks before reconstructed forms and in constraint names were preserved where present.
- †: daggers for ungrammatical/unattested forms were preserved where present.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 68,
    "h2": 133,
    "h3": 3
  },
  "macron_a": 165,
  "macron_e": 11,
  "macron_i": 101,
  "macron_o": 36,
  "macron_u": 15,
  "schwa": 88,
  "greek_chars": 4371,
  "combining_diacritics": 4518,
  "dagger": 201
}
```

## Structural integrity check

- Headings were normalized to Markdown headings where the section numbering was machine-readable.
- Bibliography and indexes were separated from the main content.
- Chapter 2 and Chapter 8 were chunked according to the source hierarchy and the supplied chunking rules.
- Page anchors are retained as HTML comments for later source-location checks.
- Footnotes remain inline in the extracted page flow rather than being converted to Markdown footnote syntax.
- Tables, paradigms, and OT tableaux are preserved primarily as text-layer line structures; they are readable, but not guaranteed to be column-perfect.
- No claim is made that this pass is character-authoritative. The most useful next pass would target OT tableaux, syllable diagrams, dense appendix tables, and indexes.

## Image inventory

| File | Source label | Source page | Caption / note |
|---|---:|---:|---|
| images/cooper-2015-cover.png | cover illustration | 1 | Cover illustration: Galen, De pulsibus (MS E 82, Venice, ca. 1550). Courtesy of the U.S. National Library of Medicine, Bethesda, Maryland. |
| images/cooper-2015-p209-fig43.png | example (43) | 209 | Syllable-structure diagrams in Chapter 8, example (43); no printed caption. |
