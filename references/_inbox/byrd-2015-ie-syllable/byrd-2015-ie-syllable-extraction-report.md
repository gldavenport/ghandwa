# Extraction report — Byrd 2015, *The Indo-European Syllable*

## Source type

Born-digital PDF. A machine-readable text layer is present. The raw extracted text layer was used as the primary input; rendered page inspection and embedded-image extraction were used only for image handling and a small number of source-specific glyph repairs.

## Corrections applied

- Removed running headers, page numbers, and Brill copyright/DOI footer lines where they appeared as page furniture.
- Normalized laryngeal text-layer forms `h1`, `h2`, and `h3` to Unicode subscript forms `h₁`, `h₂`, and `h₃` throughout the output.
- Replaced the custom-font OT tableau winner marker `U+F02B` with `☞`; mapped additional private-use OT symbols/arrows to `⋆`, `☹`, `→`, `↔`, and `↛`.
- Repaired two non-Greek instances where roman `H` was extracted as Greek capital eta: `H. Craig Melchert` and `H or hx`.
- Repaired a small source-specific abbreviation-list extraction error: `sub unctive` → `subjunctive`.
- Repaired obvious corrupted copyright-year/DOI text in removed footer lines where encountered before removal.
- Extracted embedded raster images into `images/` and inserted Markdown image references on the relevant pages. Placement is page-level/approximate, not a claim of exact typographic anchoring.

## Unresolved issues list

- `151` `[unclear]` markers were inserted where the PDF text layer produced replacement characters or otherwise unresolvable glyphs. These require human review against the rendered page image.
- The PDF uses custom Brill fonts, and the text layer may consistently map some technical glyphs imperfectly. The laryngeal digits, OT symbols, arrows, and candidate markers were corrected where identified, but other custom-font issues may remain.
- Table reconstruction is layout-preserving rather than fully normalized Markdown-table conversion. Dense OT tableaux, feature matrices, and form lists should be reviewed in a second pass if table-perfect structure is required.
- Paragraph lineation and line-break hyphenation were only lightly cleaned. Some hard line breaks and line-break hyphens may remain.
- Image placement is approximate. Pages with embedded images: 240, 240, 303, 303, 304, 304, 304, 305.
- Replacement characters remaining in output after conversion to `[unclear]`: 0.
- Private-use characters remaining in output after custom-glyph mapping: none detected.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: laryngeal normalization was applied. Possible remaining ASCII laryngeal-like forms detected: none by automated regex.
- Macron vowels `ā ē ī ō ū`: preserved from the text layer where present; not exhaustively verified against page images.
- Superscript modifier letters `ʰ ʷ`: preserved where present in the text layer; not exhaustively verified.
- Schwa `ə`: preserved where present in the text layer; not exhaustively verified.
- Underdot letters `ṛ ḷ ṃ ṇ`: preserved where present in the text layer; not exhaustively verified.
- Acute consonants `ǵ ḱ`: not normalized; combining-accent equivalents may remain because the Brill text layer often exposes consonant + combining mark.
- Asterisk `*`: preserved; not exhaustively verified.
- Dagger `†`: approximate count is 0; not exhaustively verified.

## Codepoint inventory — approximate

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 672,
    "h2": 1136,
    "h3": 212
  },
  "macron_a": 356,
  "macron_e": 204,
  "macron_i": 162,
  "macron_o": 231,
  "macron_u": 145,
  "schwa": 376,
  "greek_chars": 5495,
  "combining_diacritics": 3922,
  "dagger": 0
}
```

## Structural integrity check

- Chunking follows the source hierarchy: front matter, chapters 1–7, Appendix B, Appendix C, Appendix D, separate Appendix A/index file, and separate bibliography file.
- Each content chunk has YAML front matter and page anchors.
- References were separated into `byrd-2015-ie-syllable-bibliography.md`.
- Appendix A, titled “Index of Indo-European Roots & Words,” was separated into `byrd-2015-ie-syllable-index.md`.
- No separate general back-of-book index was detected after the References section.
- Footnotes are preserved in the flow of the extracted page text, but not renumbered or relocated.
- No manual claim is made that all tables are well-formed Markdown tables; many remain layout-preserving text blocks.

## Image inventory

- `images/byrd-2015-ie-syllable-p223-fig1.png` — p. 223 image 1; PDF page 240; printed page 223; caption: [none]
- `images/byrd-2015-ie-syllable-p223-fig2.png` — p. 223 image 2; PDF page 240; printed page 223; caption: [none]
- `images/byrd-2015-ie-syllable-p286-fig1.jpeg` — p. 286 image 1; PDF page 303; printed page 286; caption: [none]
- `images/byrd-2015-ie-syllable-p286-fig2.jpeg` — p. 286 image 2; PDF page 303; printed page 286; caption: [none]
- `images/byrd-2015-ie-syllable-p287-fig1.png` — p. 287 image 1; PDF page 304; printed page 287; caption: [none]
- `images/byrd-2015-ie-syllable-p287-fig2.jpeg` — p. 287 image 2; PDF page 304; printed page 287; caption: [none]
- `images/byrd-2015-ie-syllable-p287-fig3.jpeg` — p. 287 image 3; PDF page 304; printed page 287; caption: [none]
- `images/byrd-2015-ie-syllable-p288-fig1.jpeg` — p. 288 image 1; PDF page 305; printed page 288; caption: [none]
