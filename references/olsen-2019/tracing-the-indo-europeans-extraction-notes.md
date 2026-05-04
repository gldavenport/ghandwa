---
source-title: "Tracing the Indo-Europeans"
file-type: "extraction-notes"
source-file-name: "annas-arch-ae3a34d9d3b0.epub"
extraction-date: "2026-05-02"
---

# Extraction notes

## Method

- Input was a born-digital EPUB; no OCR was used.
- EPUB XHTML files were parsed directly.
- Tables were converted to Markdown tables.
- Footnote references and definitions were converted to unique Markdown footnote labels by chapter.
- Source images were extracted to `tracing-the-indo-europeans-images/` and referenced inline.
- Captions were preserved in the main Markdown; the image manifest repeats them as accessible descriptions where available.
- CSS superscript/subscript spans were converted to Unicode superscript/subscript characters where possible.

## Automated audit

| Check | Result |
|---|---:|
| markdown chars | 526568 |
| markdown words estimate | 76879 |
| tables converted | 46 |
| images referenced | 59 |
| footnote references | 55 |
| footnote definitions | 55 |
| non ascii unique count | 139 |
| epub text files processed | 16 |
| image files extracted | 59 |
| raw span tags | 0 |
| raw div tags | 0 |
| triple blank lines | 0 |
| generic image alt remaining | 2 |
| unresolved unclear markers | 0 |
| duplicate footnote defs | 0 |


## Assessment of additional passes

A second-pass cleanup was applied programmatically: layout-only `div`/`span` material was stripped, headings were normalized, tables were converted, images were extracted, footnote labels were made unique, and obvious Markdown artifacts were audited.

A third pass would add value only if the intended use is citation-critical character authority for reconstructed forms, especially in dense tables and passages with superscript/subscript PIE notation. Because this is a born-digital EPUB rather than OCR, the remaining risk is not OCR misreading but EPUB styling semantics: some raised/lowered characters may represent phonological notation, type labels, or ordinal forms depending on context.

Recommended targeted future pass: character audit of reconstructed forms in Chapters 2, 3, and 8, plus table-image review for any tables supplied only as images.

## Unique non-ASCII character inventory

```text
©°±¹ÀÄÅÉÖØÜßàáâãäåæçèéêëìíîðñóôöøùúüýþĀāćčđēęěğĩīĺŁłńņōőřŚśşšūŭųžǫʰʷʻ˂ˊˌˡˢ̨̣̥̯̰́̃̇̊̏̑αδθλνοςσϑВавгдзкопрстъыьяәᵃᵉᶜḗḫḱḿṓṣύῆ‐–‘’“”†•…⁴⁽⁾₁₂₃₄→
```
