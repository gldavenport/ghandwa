---
title: Grounding Celtic diachronic phonology II — extraction report
author: Joseph F. Eska
date: 2022/2023
source_type: born-digital
extraction_date: 2026-05-08
source_file: eska-2023-grounding-diachronic-phonology-celtic-ii.pdf
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The raw text layer was used as the primary input. Rendered page images were checked selectively for title page, article opening, footnote/superscript treatment, and feature-spreading diagrams.

## Corrections applied

- Removed offprint cover material, journal table of contents, running headers, page footers, copyright footer text, and page numbers from the corpus files.
- Split the article into a main Markdown file and a separate bibliography file. No index is present.
- Converted private-use and font-positioned glyphs where the text layer clearly represented ordinary scholarly notation: `` → `*`, ``/`` → `⟨`/`⟩`, superscript aspiration `h` → `ʰ`, superscript labiovelarization `w` → `ʷ`, superscript palatalization `j` → `ʲ`, superscript digits → Unicode superscript digits.
- Rejoined most paragraph line breaks and repaired obvious hyphenation across line endings.
- Recast the three feature-spreading diagrams as text diagrams because the PDF text layer exposes their line/arrow geometry as private-use symbols.

## Unresolved issues

- The extraction relies on the PDF text layer plus selective visual checks, not a full manual character-by-character collation against page images. Remaining systematic errors are possible, especially in dense phonological notation.
- The three feature diagrams `(10)`, `(12)`, and `(13)` were reconstructed semantically in fenced text blocks; their exact visual line geometry is not diplomatic.
- Footnote markers and source-internal superscript digits were preserved as Unicode superscripts rather than converted to Markdown footnote syntax. This avoids misclassifying source-internal superscripts such as `Ox²` and edition markers.
- Italics were restored from PDF font metadata where extraction exposed spans as italic; some cross-span italic boundaries may remain approximate.

## Confusion-pair report

- `h₁ h₂ h₃`: no laryngeal-subscript forms detected in this article; no normalization applied.
- Macron vowels `ā ē ī ō ū`: present and retained where the text layer exposed them; counts below are approximate.
- `ʰ ʷ ʲ`: restored from font-positioned small glyphs in phonological forms. This was a high-risk source-specific correction.
- `ə`: present in IPA examples and retained where exposed.
- Underdotted Indic characters: none detected in the output.
- `ǵ ḱ`: none detected in the output.
- Asterisk before reconstructed forms: retained.
- Dagger `†`: none detected.

## Approximate codepoint inventory

All counts are approximate and intended for regression checking only.

```json
{
  "h1": 0,
  "h2": 0,
  "h3": 0,
  "macron_a": 0,
  "macron_e": 0,
  "macron_i": 3,
  "macron_o": 0,
  "macron_u": 1,
  "schwa": 9,
  "greek_chars": 49,
  "combining_diacritics": 18,
  "dagger": 0,
  "modifier_h": 115,
  "modifier_w": 3,
  "modifier_j": 21,
  "theta": 48,
  "eth": 36,
  "lateral_fricative": 19,
  "gamma": 3,
  "script_g": 5
}
```

## Structural integrity check

- Main article text is a single Markdown file, appropriate for a journal article.
- Bibliography is separated into its own Markdown file.
- No index is present.
- No figures, maps, plates, or image-only tables were identified.
- Footnotes are included in a `Notes` section in the main Markdown file.
- Tables/lists/examples are retained as block text; dense feature diagrams are fenced text blocks.

## Image inventory

No extracted images.
