# friedman-2025 extraction report

## Source identification

- Source file: `friedman-2025.pdf`
- Source type: born-digital PDF with a machine-readable text layer.
- Extraction basis: PyMuPDF text blocks from the embedded PDF text layer; visual extraction was used only for image crops.
- Extraction date: 2026-05-07
- Output structure: chunked Markdown with front matter, introduction, chapter/section chunks, envoi, separate index file, README index, manifest, and extracted images.
- Instruction-specific note: the latest instructions add EPUB inline image-glyph handling and laryngeal checking inside inline HTML spans. This source is a PDF, not an EPUB; no EPUB image-glyph substitutions were applicable. No source HTML spans were present in the PDF text extraction.

## Corrections applied

- Ligature repairs applied globally in extracted text blocks: fi-ligature to `fi`, fl-ligature to `fl`, plus related Unicode presentation ligatures when encountered.
- Soft-hyphen/control-artifact cleanup applied for embedded-text artifacts such as U+00AD and U+FFFE-like separators.
- Cambridge Core download/footer text removed from output blocks.
- Running headers and page-number-only footer blocks removed by coordinate filtering.
- Paragraph lineation repaired heuristically: prose blocks were joined across PDF line breaks, including common end-of-line hyphenation repairs; table-like, example-like, paradigm-like, and diagram-like blocks retained lineation.
- Figures/maps were rasterized from the PDF page regions and inserted as Markdown image references.
- A targeted pass checked residual literal presentation ligatures in corpus files; none remain in extracted source-content Markdown after this pass.

## Unresolved issues list

- Table normalization is heuristic. Many tables and paradigms are preserved as text blocks rather than fully regularized Markdown tables; a later table-specific pass would improve machine parsing.
- Footnotes are preserved near their source page positions, but note anchoring was not globally verified against every note marker.
- Greek, IPA, Balkan orthographic characters, superscripts/subscripts, and combining diacritics were retained from the text layer, but no full visual collation was performed against every page.
- Index entries are separated into `friedman-2025-index.md`; a column-aware word-position pass was used for the index, but dense line wrapping was not fully human-collated.
- The source does not include the full bibliography in the PDF text; the book directs users to Cambridge for the full references. No `friedman-2025-bibliography.md` was produced.
- Figure crops were manually defined by page region and should be visually spot-checked if figure boundary precision matters.
- Inline `[?]` markers remain in two source-content locations where the prior pass treated a character/form as needing review: `friedman-2025-ch4-sec4-3-1.md` and `friedman-2025-ch5-sec5-3.md`.

## Confusion-pair report

- `h₁ h₂ h₃` versus `h1 h2 h3`: approximate source-content output counts are h₁=0, h₂=0, h₃=0. Potential ASCII candidates outside continuous alphabetic strings: h1=0, h2=0, h3=0. These were not visually verified throughout.
- Precomposed macrons versus combining macrons: approximate counts are ā=128, ē=54, ī=30, ō=48, ū=31; combining-diacritic count=32. Decomposed source characters were not normalized beyond ligature/control cleanup.
- Superscript modifier letters `ʰ ʷ` versus plain `h w`: retained where present in the PDF text layer; not globally visually verified.
- Schwa `ə` versus `e/9`: approximate schwa count=81; not globally visually verified.
- Underdot letters `ṛ ḷ ṃ ṇ`: retained where present in the text layer; not globally visually verified.
- Acute consonants `ǵ ḱ`: retained where present in the text layer; not globally visually verified.
- Asterisk `*` versus other glyphs: asterisks were retained from the text layer; no full visual audit was performed.
- Dagger `†`: approximate source-content count=3; not globally visually verified.
- Inline HTML span laryngeal check: not applicable to this PDF extraction; no EPUB/HTML source layer was processed.

## Codepoint inventory

All counts are approximate and intended for cross-pass comparison only. Counts are over extracted source-content Markdown files, excluding README, extraction report, and manifest.

```json
{
  "note": "All counts are approximate and for cross-pass comparison only. Counts are over extracted source-content Markdown files, excluding README/report/manifest.",
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 128,
  "macron_e": 54,
  "macron_i": 30,
  "macron_o": 48,
  "macron_u": 31,
  "schwa": 81,
  "greek_chars": 22867,
  "combining_diacritics": 32,
  "dagger": 3
}
```

## Structural integrity check

- Headings: chapter and section headings were preserved from the PDF text layer and converted to Markdown heading levels where block structure made this reliable. Running headers were filtered out.
- Chunking: long chapters were split according to the source's numbered chapter/section/subsection hierarchy as exposed in the PDF outline.
- Footnotes: preserved in page-local position; global anchoring not exhaustively verified.
- Tables/paradigms: preserved primarily as lineated text blocks; table grid normalization remains a candidate for a later pass.
- Page boundaries: page anchors were inserted throughout. No systematic continuation-loss was detected by the extraction script, but mid-page section boundaries depend on PDF block coordinates.

## Image inventory

| Output file | Source label | Page | Caption |
|---|---|---:|---|
| `images/friedman-2025-p7-fig1.png` | frontispiece map | pdf-7 | Ethnic map of the Republic of Macedonia (now Republic of North Macedonia) 1994. Reproduced with permission of the Bureau of Statistics of the Republic of North Macedonia (see §1.3 for discussion; see www.cambridge.org/BalkanLanguages for the color version) |
| `images/friedman-2025-fig6-1.png` | Figure 6.1 | 693 | Stages in the creation of conditionals |
| `images/friedman-2025-fig6-2.png` | Figure 6.2 | 724 | Reanalysis in Greek conditional |
| `images/friedman-2025-fig8-1.png` | Figure 8.1 | 1011 | Diagram of the path of transmission for locative determiner omission (Reprinted by permission from the author) |

## Image-glyph inventory

Not applicable. The source is a born-digital PDF, not an EPUB with inline character glyph images. No `image-glyph` substitutions or unresolved inline image glyphs were recorded.
