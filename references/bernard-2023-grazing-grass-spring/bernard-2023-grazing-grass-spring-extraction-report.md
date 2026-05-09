---
title: "Grazing grass in the spring: extraction report"
author: "Chams Benoît Bernard"
date: "2023"
source_type: born-digital
extraction_date: "2026-05-07"
source_file: "bernard-2023-grazing-grass-spring.pdf"
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The raw text layer was used as the primary source. Rendered-page inspection was used only for private-use glyphs, superscript/subscript behavior, and citation-note numerals.

## Corrections applied

- Removed running headers, footers, page numbers, and copyright footer lines from corpus files.
- Rejoined wrapped paragraphs and repaired obvious line-break hyphenation.
- Separated the article bibliography into `bernard-2023-grazing-grass-spring-bibliography.md`.
- Preserved the PDF’s preliminary issue contents and foreword in `bernard-2023-grazing-grass-spring-front-matter.md` rather than mixing them into the article corpus file.
- Replaced private-use glyphs from the text layer: `\ue03b` → `u̯`; `\ue03a` → `i̯`; `\ue091` → combining inverted breve above in `g̑`; `\ue017` → `n̥`; `\ue00d` → `ṛ`; `\ue181` → macron on preceding `a`; `\ue0c1` → `ʷ`; `\ue16d` → acute on preceding `ū`.
- Normalized laryngeal indices rendered as small numerals to subscript forms: `h₁`, `h₂`, `h₃`; `hₓ` in the issue contents.
- Restored superscript aspiration in PIE forms where the PDF text layer exposed small `h` as baseline text: chiefly `g̑ʰei̯m-` and `*i̯ebʰ-`.
- Restored citation note numerals where the text layer flattened superscripts: `470²⁴`, `420¹⁵`, `177⁴`, `70²`, `8¹⁸`.
- Repaired clear extraction artifacts such as `Ramόn` / `Ramόn` → `Ramón` in the bibliography.
- Some canonically equivalent Greek accent forms may appear NFC-composed in output; a dedicated Greek codepoint audit would be warranted before treating the file as codepoint-authoritative for Greek accent subclasses.

## Unresolved issues / human-review items

- `rhaɣʷām` on source p. 15: the text layer uses a zero-width private-use glyph after `ɣ`; it was interpreted as modifier `ʷ` from glyph behavior/context, but this should be verified against the publisher PDF.
- `ciṛmū́näi` on source p. 16: the zero-width private-use glyph after `ū` was interpreted as an acute accent; verify if a later pass focuses on Iranian/Ormuri forms.
- `*u̯āhart-` and `*u̯āhara-ratu-` on source p. 14: the zero-width private-use glyph after `a` was interpreted as a macron, yielding `ā`; this is contextually supported by the surrounding discussion of `*wārat`, but should still be verified visually in a character-audit pass.
- `*lei̯s-` in the issue contents (Matteo Tarsi article title) was normalized from the private-use `i̯` glyph; because this is only in the contents page, not Bernard’s article body, it received lower priority than the article’s forms.
- The bibliography was reconstructed as one paragraph per reference; entries should be spot-checked if used as a citation database.

## Confusion-pair report

- Laryngeals: `h₁`, `h₂`, and `hₓ` were normalized where the text layer exposed small indices as baseline ASCII. I did not claim a full visual audit of every laryngeal instance.
- Macron vowels: precomposed macrons were preserved where present; one private-use macron was resolved to `ā`. Dense bibliography entries were checked only for obvious loss.
- Superscript aspiration: small `h` was restored in the main PIE forms identified by span-size inspection; possible missed aspirates cannot be excluded.
- Schwa / turned e: both `ə` and `ǝ` occur in the source and were preserved as extracted.
- Underdot/ring letters: `ṛ`, `ḍ`, `ṣ`, `ẓ`, `n̥`, and related scholarly forms were preserved or restored where private-use glyphs required mapping.
- Palatovelars: `ǵ` in the contents and `g̑` in article forms were preserved as distinct notations.
- Asterisks: reconstructed-form asterisks were retained.
- Dagger: one dagger appears in note 23 and was retained.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "h1": 1,
  "h2": 19,
  "h3": 0,
  "macron_a": 62,
  "macron_e": 31,
  "macron_i": 11,
  "macron_o": 24,
  "macron_u": 2,
  "schwa": 13,
  "greek_chars": 166,
  "combining_diacritics": 119,
  "dagger": 1
}
```

## Structural integrity check

- Article section hierarchy is preserved through §5, including subsections §3.1, §3.2, §4.1, and §4.2.
- Footnotes are attached with Markdown footnote markers and collected in the article file under `## Notes`.
- Bibliography is separated into its own file.
- No tables, figures, maps, or plates were present in the Bernard article; no images were extracted.
- The issue contents and foreword from PDF pp. 1–2 are preserved in a separate front-matter file.

## Image inventory

No figures, diagrams, maps, plates, or image-only tables were identified.
