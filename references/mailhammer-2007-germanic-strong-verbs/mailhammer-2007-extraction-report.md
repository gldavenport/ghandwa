# Mailhammer 2007 — Extraction report

## Source identification

- Source file: `mailhammer-2007-germanic-strong-verbs.pdf`
- Source type: born-digital PDF; a machine-readable text layer is present.
- Extraction granularity: chunked monograph. Chapter two is split by source section hierarchy because it exceeds the long-chapter threshold; references and indexes are separate files.
- Images: one embedded cover image extracted. No in-text figures were detected by embedded-image inventory.

## Corrections applied

- Removed running headers and page numbers, including the PDF text-layer artifacts such as `%JCRVGT...`, `9QTF KPFGZ`, and `4GHGTGPEGU`.
- Rejoined many paragraph line breaks and common end-of-line hyphenations while preserving page anchors.
- Repaired common PDF text-layer corruption from soft hyphen/page-boundary extraction.
- Replaced the empty-slot glyph decoded as `U+0086` with `□` after visual checking against Table 1 and adjacent prose.
- Replaced `Ɲ1` and `Ɲ2` with `ē₁` and `ē₂` where the table font mis-decoded long-e/subscript notation.
- Replaced `¼` with `ʷ` in specialist notation contexts, e.g. labiovelar symbols.
- Repaired several source-specific glyphs from SILDoulosIPA and PorsonGreek fonts; uncertain mappings are listed below.

## Unresolved issues and uncertainty list

- The PDF uses specialist fonts with incomplete/bad Unicode extraction for some IPA/Indo-European notation. The output applies targeted source-specific repairs, but the specialist notation should receive a dedicated visual character pass before being treated as character-authoritative.
- SILDoulosIPA characters decoded as control codes were not all independently verified. Mappings applied: `i/u + U+001B` and `i/u + U+0099` → `i̯/u̯`; `U+008B` → `ə`; `U+0084` in `h...i-conjugation` → `ḫi`; `U+0019` → `ǫ`; `æ + U+0005` → `ǣ`.
- Greek custom-font instances were partially repaired: `α + U+0007` → `ἀ`; `ε + U+0092` → `ἐ`. These are approximate and should be checked visually in the word index and chapter four examples.
- Laryngeal forms in the text layer are mostly ASCII `h1`, `h2`, `h3`; they were not globally normalized to subscript `h₁`, `h₂`, `h₃` because the source appears to use ASCII digits in many places and global conversion could introduce false precision.
- Dense appendix and index tables were extracted from text order. They are usable for search, but table alignment should be stress-tested before machine parsing.
- The bibliography is extracted as text and lightly reflowed; italics/small-caps styling is not fully preserved because the text-layer export does not reliably expose all semantic styling.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: not fully verified. Output retains source text-layer ASCII forms where present.
- Macron vowels: approximate counts are included in `manifest.json`. Macrons were preserved where the text layer supplied them; dense index sections may still require visual audit.
- `ʰ ʷ` vs. `h w`: `ʷ` was repaired from `¼` in specialist contexts. Superscript `ʰ` was not globally inferred.
- `ə` vs. `e` or `9`: `U+008B` was repaired to `ə`; remaining schwa-like forms should be checked.
- Underdot/underring Indic notation: preserved where Unicode was exposed; not fully verified visually.
- `ǵ ḱ` vs. ASCII approximations: not fully verified; the PDF text layer appears to lose at least some specialist consonant diacritics.
- `*` before reconstructed forms: preserved where present; the source also uses `+` for reconstructed forms according to its abbreviations list.
- Dagger `†`: approximate count included; no claim of full verification.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 15,
    "h2": 68,
    "h3": 9
  },
  "macron_a": 58,
  "macron_e": 158,
  "macron_i": 21,
  "macron_o": 137,
  "macron_u": 91,
  "schwa": 7,
  "greek_chars": 189,
  "combining_diacritics": 174,
  "dagger": 0
}
```

## Structural integrity check

- Headings are mostly consistent and page anchors are present for later citation/source checking.
- Footnotes remain near their source-page locations. Some footnote text may still be joined into surrounding prose if the source text order placed it there.
- Tables are preserved primarily as extracted line/table text rather than fully normalized Markdown tables where automated conversion risked damaging notation.
- No continuation text was intentionally omitted at page boundaries; page anchors preserve source alignment for later repair.

## Image inventory

- `images/mailhammer-2007-germanic-strong-verbs-cover.jpeg` — cover image, PDF page 1.
