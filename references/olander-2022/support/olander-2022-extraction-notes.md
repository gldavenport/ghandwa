---
title: "Extraction Notes: Olander 2022"
source_file: "olander-2022.pdf"
extraction_date: "2026-04-29"
---

# Extraction Notes

## Source

Thomas Olander, ed. *The Indo-European Language Family: A Phylogenetic Perspective*. Cambridge University Press, 2022. DOI: 10.1017/9781108758666.

## Method

- Extracted embedded PDF text with `pdftotext` in layout mode.
- Removed Cambridge Core download/footer boilerplate and ordinary page-number/running-header artifacts.
- Normalized common typographic ligatures (`ﬁ`, `ﬂ`, etc.) to plain Unicode letter sequences.
- Converted chapter, section, figure, table, front-matter, references, and index labels into Markdown structure where detected.
- Preserved page anchors as HTML comments: `<!-- pdf-page: N; printed-page: N -->`.
- Preserved detected table blocks in fenced monospaced text blocks rather than forcing fragile Markdown tables.

## First-pass quality assessment

The source has embedded text and is generally easy to extract. The main remaining risk areas are extraction-order and formatting issues rather than broad OCR corruption:

- Footnotes are preserved, but some may remain inline or positioned near adjacent body text rather than fully reflowed as Markdown footnotes.
- Tree diagrams and other figures are represented by extracted labels/captions, not redrawn diagrams.
- Dense tables, especially in Chapter 14, are preserved as text blocks but are not normalized into semantic Markdown tables.
- Some scholarly notation should be character-audited before high-stakes citation, especially laryngeals, combining diacritics, Greek, IPA-like symbols, and reconstructed forms.

## Recommended next passes

A second pass would add value by checking paragraph joins, footnote placement, headings, lists, and table blocks chapter by chapter.

A third pass would add value for this volume because the document contains dense Indo-European notation, reconstructed forms, Greek, laryngeals, special diacritics, and compact comparative tables. The most useful third pass would be a targeted character audit rather than a full rewrite.

## Further-pass priority

1. Chapter 14, especially Tables 14.1–14.6.
2. Chapters 5, 6, 10, 11, 12, and 15 for reconstructed forms and special notation.
3. Figure pages if the exact topology of the tree diagrams needs to be captured in text.
4. Bibliographies if a normalized cross-volume bibliography is desired.


## Second pass completed (2026-04-29)

The second pass focused on structural cleanup rather than full re-extraction. Changes made:

- Repaired split section headings where the first pass left heading continuations as body text.
- Removed two false headings created from an inline calculation and a cross-reference to Section 6.5.2 n. 10.
- Removed a stray footnote marker from the heading “7.3 The Position of Italo-Celtic”.
- Repaired the Chapter 14 table sequence around Tables 14.3–14.6, including separation of Table 14.4 from the following Nuristanic bullet list and normalization of Table 14.5 into a Markdown table.
- Added an accessible description for Figure 14.1 in the main extraction.

## Third pass completed (2026-04-29)

The third pass was a targeted character-fidelity and notation audit. It did not silently normalize linguistic notation. It checked for high-risk extraction artifacts and updated the character audit file.

Remaining limitations:

- Footnotes are preserved, but they are not converted into formal Markdown footnote syntax.
- Tree diagrams are not fully redrawn as ASCII/Markdown diagrams; captions and accessible figure descriptions are supplied in the companion file.
- Exact quotation of individual reconstructed forms should still be checked against the PDF page image, especially in dense tables and footnotes.

Further passes would add diminishing value for ordinary corpus use. A future manual pass would be useful only if you want normalized Markdown footnotes, fully redrawn tree diagrams, or citation-grade table transcription.


## Fourth pass (2026-04-29)

Scope: targeted pass for the remaining items identified after pass 3, excluding redrawn tree diagrams.

Actions performed:

- Converted machine-detectable numbered footnote paragraphs to formal Markdown footnote definitions using chapter-prefixed labels such as `[^ch14-7]`.
- Inserted matching chapter-prefixed footnote references where the reference marker could be safely detected in the body text.
- Corrected table/code-block boundaries where body prose had been swallowed by preformatted table blocks, especially Table 4.2 and Table 10.1.
- Verified and corrected principal tabular material against PDF text/rendering: Tables 4.1, 4.2, 10.1, and 14.1–14.6.
- Tightened selected character-sensitive forms in Chapter 14 tables, including Old Avestan `xratə̄uš` and `pasə̄uš`.
- Left tree diagrams as accessible descriptions rather than redrawing them.

Known limits:

- Footnote conversion is conservative. Notes that the original PDF text stream merged into ordinary body paragraphs may remain inline where automatic separation would risk damaging the text.
- The table pass focused on the formally tabular material and high-risk Indo-Iranian forms; it was not a full diplomatic collation of every reconstructed form in the volume.
