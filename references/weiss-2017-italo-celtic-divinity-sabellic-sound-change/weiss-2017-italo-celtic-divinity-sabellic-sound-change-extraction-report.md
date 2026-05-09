---
title: "An Italo-Celtic Divinity and a Common Sabellic Sound Change"
author: "Michael Weiss"
date: 2017
source_type: born-digital
extraction_date: 2026-05-07
source_file: "weiss-2017-italo-celtic-divinity-sabellic-sound-change.pdf"
chunk: extraction-report
---

# Extraction Report

## Source type

Born-digital PDF with a machine-readable text layer. The raw text layer was used as the primary input, with rendered-page inspection and span-position data used to recover subscript laryngeal numerals and superscript modifier letters in PIE notation.

## Corrections applied

- Removed running headers, page numbers, and blank terminal page output.
- Rejoined wrapped prose lines and repaired obvious line-break hyphenation in body text, footnotes, and bibliography entries.
- Converted laryngeal numerals in technical forms from positioned digits to Unicode subscripts: h₁, h₂, h₃.
- Converted positioned superscript h/w in technical forms to Unicode modifier letters ʰ and ʷ where span position supported the inference.
- Separated the source bibliography into its own Markdown file.
- Converted source footnotes into Markdown footnote definitions at the end of the main text.

## Unresolved-issues list

- No `[unclear]` markers were inserted.
- Some italic, small-caps, and typographic styling was not systematically encoded in Markdown; this was intentionally subordinated to character fidelity.
- Footnote-marker placement was inferred from superscript span position. The markers should be reviewed if this extraction is used for citation-critical publication.
- Bibliography line joins were inferred from indentation and may require manual spot-checking for entries split across lines.

## Confusion-pair report

- h₁/h₂/h₃ vs. h1/h2/h3: normalized where recognized by span-position or regex; remaining ASCII h1/h2/h3 instances were searched, but a consistent error cannot be ruled out.
- ā/ē/ī/ō/ū: retained from the PDF text layer; approximate counts are in the manifest.
- ʰ/ʷ vs. h/w: recovered where the PDF used reduced, raised spans. Remaining h/w in technical forms may require specialist review.
- ə: no schwa instances were detected.
- ṛ/ḷ/ṃ/ṇ and related Indic diacritics: retained from the text layer where present; not all individual instances were visually verified.
- ǵ/ḱ and related palatal notation: the source primarily uses ĝ and k̑-style notation; these were retained where extracted.
- * before reconstructed forms: retained from the text layer.
- † dagger: retained where present; approximate count is in the manifest.

## Codepoint inventory

All counts are approximate and intended for cross-pass comparison only.

- laryngeals: {'h1': 8, 'h2': 4, 'h3': 0}
- macron_a: 13
- macron_e: 44
- macron_i: 14
- macron_o: 61
- macron_u: 12
- schwa: 0
- greek_chars: 167
- combining_diacritics: 43
- dagger: 2
- superscript_h: 38
- superscript_w: 2

## Structural integrity check

- Headings were normalized to Markdown headings.
- Footnotes are attached as Markdown footnote definitions.
- Source examples and quoted passages were preserved in block form where the PDF layout made them distinct.
- No tables or figures were detected in the source.
- Page anchors were inserted as HTML comments for source-page navigation.

## Image inventory

No figures, maps, plates, or image-only tables were detected. No images directory was created.
