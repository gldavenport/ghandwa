---
title: "Extraction report — Linnaean linguistics"
author: "Stefan Höfler"
date: "2024"
source_type: born-digital
extraction_date: 2026-05-07
source_file: "höfler-2024-linnaean-linguistics.pdf"
chunk: extraction-report
---
# Extraction report — Höfler 2024, “Linnaean linguistics”

## Source assessment

- Source type identified as **born-digital PDF**. The machine-readable text layer was used as the primary input.
- The PDF contains 34 pages. The article/book-chapter text occupies PDF pages 1–26; the references occupy PDF pages 27–34.
- No figures, plates, maps, image-only tables, or extracted embedded images were identified during this pass.

## Corrections applied

- Repaired the PDF’s Private Use Area oldstyle numeral encoding (`U+F730`–`U+F739`) to ordinary digits `0`–`9`.
- Normalized laryngeal notation after numeral repair: `h1`, `h2`, and `h3` were converted to `h₁`, `h₂`, and `h₃`.
- Repaired one ligature extraction artifact: `ﬂ` → `fl` in `Höfler`.
- Repaired systematic scholarly glyph encodings from the PDF text layer: `U+E002` → `i̯`, `U+E007` → `ā́`, `U+E00C` → `m̥`, `U+E00F` → `R̥`, `U+E015` → `l̥`, and `U+E045` → `ĺ̥`.
- Converted small inline `w`, `j`, and `h` spans in technical forms to `ʷ`, `ʲ`, and `ʰ` where they appeared as superscript modifier letters in the PDF layout.
- Converted spacing tilde artifacts after letters to combining tilde in forms such as `vil̃kas` and `ἐχι̃νος`.
- Rejoined wrapped prose lines and repaired ordinary line-break hyphenation. Compound line-break hyphens were preserved where the visible source appeared to intend a hyphenated compound.
- Moved the source’s “How to cite this book chapter” block into a source-citation section near the beginning of the main Markdown file.
- Converted footnote markers to Markdown footnote references and collected footnote text into a `## Footnotes` section.

## Unresolved issues and review cautions

- Inline italics and small-caps formatting were not exhaustively encoded as Markdown/HTML because preserving the asterisk-heavy reconstructed forms without introducing Markdown ambiguity was prioritized. Section headings, footnotes, and bibliography structure were preserved.
- The PDF text layer encodes palatovelars as base consonant plus combining inverted breve, e.g. `k̑`, rather than normalizing to acute-palatal notation such as `ḱ`. This extraction preserves the source text layer’s `k̑`/`g̑` notation.
- Greek `χϑών` was left as extracted from the PDF text layer (`ϑ`, Greek theta symbol) rather than silently normalizing to `χθών`. This should be reviewed if canonical Greek Unicode normalization is desired later.
- The mappings for `ĺ̥`, `l̥`, `m̥`, `R̥`, `i̯`, and `ā́` were systematic repairs based on context and visual inspection of rendered pages; they should still be treated as reviewable in a character-authoritative pass.
- No `[unclear]` or `[?]` markers were inserted in the corpus files during this pass. The absence of markers does not certify that every character is correct.

## Confusion-pair report

- `h₁ h₂ h₃`: normalized from PDF oldstyle digits after `h`; approximate counts are in the codepoint inventory.
- Macron vowels: preserved and counted approximately. Combined macron-plus-acute `ā́` occurs after repair of `U+E007`.
- Superscript modifier letters: small inline `w`, `j`, and `h` spans were converted to `ʷ`, `ʲ`, and `ʰ` where detected. This was not manually verified for every possible superscript span.
- Schwa `ə`: preserved where present in the PDF text layer.
- Underdot/ring-below syllabic marks: repaired for known PUA syllabic resonants and otherwise preserved from the text layer.
- Palatovelars: source uses combining inverted breve forms (`k̑`, `g̑`); no conversion to `ḱ`/`ǵ` was applied.
- Asterisk `*`: preserved in reconstructed forms.
- Dagger `†`: no dagger instances were observed in the output.

## Codepoint inventory 

All counts are approximate and are intended for cross-pass comparison, not certification.

```json
{
  "laryngeals": {
    "h1": 128,
    "h2": 71,
    "h3": 10
  },
  "macron_a": 34,
  "macron_e": 8,
  "macron_i": 4,
  "macron_o": 19,
  "macron_u": 5,
  "schwa": 6,
  "greek_chars": 381,
  "combining_diacritics": 476,
  "dagger": 0
}
```

Remaining Private Use Area codepoints in output: none observed.

## Structural integrity check

- Headings are represented with Markdown headings.
- The bibliography was separated into `hofler-2024-linnaean-linguistics-bibliography.md`.
- No index was present.
- Footnotes were collected into Markdown footnote definitions at the end of the main article file.
- No image inventory was produced because no images or image-only figures were identified.
- Page-boundary continuation was checked mechanically through line rejoining; a later character-authoritative pass could still inspect dense technical forms and notes against rendered pages.
