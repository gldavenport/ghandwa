# Extraction report — Language Contact and the Origins of the Germanic Languages

## Source identification

- Source file: `schrijver-2014-language-contact-germanic.epub.zip`
- Source type used for extraction: EPUB.
- EPUB internal text source: `OEBPS/*.xhtml` files, read in OPF/spine order and then chunked by the source's own chapter/section hierarchy.
- EPUB internal image directory: `OEBPS/images/`.
- Image handling: discrete EPUB image files were copied as-is into the output `images/` directory and renamed in kebab-case. No image re-encoding, recompression, OCR, or visual inference was applied for image extraction.
- Inline image-glyph handling: all XHTML `<img>` elements were inspected by parent context. No inline character-glyph images embedded in running linguistic forms were detected.
- Extraction date: 2026-05-07

## Chunking applied

- The source was treated as a running prose monograph longer than 100 pages.
- Front matter was placed in a front-matter file.
- Chapter I and Chapters III–VI were retained as chapter-level files.
- Chapter II was longer than 50 pages, so it was split at its own top-level numbered sections, §1–§10.
- Notes, bibliography, and index were placed in separate companion files.
- `README.md` lists every output file, source label, page range, and section coverage.

## Corrections applied

- XHTML-to-Markdown structural conversion was applied to the EPUB text layer.
- Inline formatting was preserved with inline HTML tags for italics, bold, underlining, superscripts, and subscripts where that reduced conflict with reconstructed-form asterisks and other linguistic notation.
- Bibliographic and internal hyperlinks were unwrapped while preserving visible text.
- EPUB pagebreak anchors were preserved as HTML anchors such as `<a id="p1"></a>` for source-location checking.
- Endnote references were normalized to Markdown footnote-style references such as `[^en2_1]`; the source endnotes were rendered as corresponding footnote definitions in the notes file.
- Table `colspan` values were expanded into empty Markdown cells where needed.
- Laryngeal normalization was applied where the EPUB encoded laryngeals as inline markup splits: e.g. `h</i><sub>2</sub><i>` and `h</i><sub>2</sub>` were rendered as `h₂`, including inside italicized forms. No `h₁` or `h₃` instances were detected mechanically.
- No OCR-wide spelling correction was applied because the source text layer is born-digital XHTML.
- A small set of EPUB/XHTML artifacts was repaired in the Markdown: prose underscores used where a colon was intended were converted to colons in the affected passages; `<i>oastal Dutch and Eastern Dutch</i>` was repaired to `<i>Coastal Dutch and Eastern Dutch</i>`; and `<i>Binno-baamic Gradation</i>` was repaired to `<i>Finno-Saamic Gradation</i>`.
- Double-star technical notation before italicized unattested forms was escaped where needed so Markdown does not interpret it as boldface.

## Unresolved-issues list

1. Image-only figures and tables are preserved as copied image files, not transcribed text. This follows the EPUB-specific instruction not to attempt visual inference for image extraction.
2. The following image-only table/figure content remains non-textual in the corpus Markdown: `table0021_B.jpg`, `table0022_B.jpg`, `table0023_B.jpg`, `table0024_B.jpg`, `table0025_B.jpg`, `table0096_B.jpg`, and `fig5_1_B.jpg` through `fig5_5_B.jpg`.
3. `table0096_B.jpg` has no explicit caption in the XHTML. It was inserted with its internal source label rather than an inferred caption.
4. `fig5_5_B.jpg` has the caption text `Figure 5.5` only in the XHTML. No additional caption was inferred.
5. Complex EPUB tables with multi-column spans were flattened into Markdown pipe tables. The visible cell text was preserved, but table geometry is simplified.
6. Inline page anchors may occur inside paragraphs or captions when the source pagebreak occurred mid-flow. They are retained for source-location checking.
7. The QC pass did not visually certify all forms against the image rendering of the EPUB. It relies primarily on machine-readable XHTML.

## Image-glyph inventory

- Inline EPUB image glyphs substituted: 0.
- Inline EPUB image glyphs unresolved: 0.
- Inspection result: no inline `<img>` elements embedded in running text or linguistic forms were detected. All detected images were cover, logo, figure, or table images: `coverpage.jpg`, `logo_B.jpg`, `table0021_B.jpg`, `table0022_B.jpg`, `table0023_B.jpg`, `table0024_B.jpg`, `table0025_B.jpg`, `fig5_1_B.jpg`, `fig5_2_B.jpg`, `fig5_3_B.jpg`, `fig5_4_B.jpg`, `table0096_B.jpg`, and `fig5_5_B.jpg`.

## Confusion-pair report

The following report is approximate and does not certify correctness. It reports mechanical checks in the generated Markdown and known unverifiable areas.

| Confusion pair | Output status / risk |
|---|---|
| `h₁ h₂ h₃` vs. `h1 h2 h3` | `h₂` was detected where the EPUB used `h` plus subscript markup and was normalized to Unicode `h₂`, including split italic markup. No `h₁` or `h₃` instances were detected mechanically. Any such notation embedded in copied images was not transcribed. |
| Macron vowels `ā ē ī ō ū` | Macron vowels are present and were preserved from XHTML. Macron-bearing text in copied images remains non-textual. |
| Macron consistency across body, notes, index | Body, notes, bibliography, and index were extracted from XHTML; no source-wide certification is claimed. |
| Superscript modifier letters `ʰ ʷ` vs. ASCII `h w` | Modifier/special phonetic characters were mechanically preserved where present in XHTML; copied image content was not transcribed. |
| `ə` vs. `e` or `9` | Schwa count is included below. No visual collation was performed. |
| Underdot letters `ṛ ḷ ṃ ṇ` | Any such characters present in XHTML were preserved as Unicode text; no source-wide visual certification is claimed. |
| `ǵ ḱ` vs. `g' k'` | Any such characters present in XHTML were preserved as Unicode text; no silent normalization was applied. |
| Asterisk `*` before reconstructed forms | Asterisks in XHTML were preserved. Inline italics are represented with `<i>` tags to avoid converting reconstruction asterisks into Markdown emphasis. |
| Dagger `†` vs. `+` or absent | Dagger count is included below. No source-wide visual certification is claimed. |

## Codepoint inventory — approximate

| Item | Approximate count |
|---|---:|
| `h₁` | 0 |
| `h₂` | 5 |
| `h₃` | 0 |
| `ā` | 252 |
| `ē` | 182 |
| `ī` | 182 |
| `ō` | 283 |
| `ū` | 128 |
| `ə` | 85 |
| Greek characters | 91 |
| Combining diacritics | 229 |
| `†` | 0 |
| `[unclear]` markers | 0 |
| `[?]` markers inserted | 0 |
| Source literal `[?]` sequences retained | 1 |
| Inline image glyph substitutions | 0 |
| Inline unresolved image glyph annotations | 0 |

## Structural integrity check

- Output Markdown files listed in manifest: 22.
- Corpus/chunk Markdown files excluding README and report: 20.
- Images copied: 13.
- Markdown image references detected: 13.
- `[image-only...]` fallback placeholders detected: 0.
- `[image-glyph: ...]` annotations detected: 0.
- Endnote references detected: approximately 408.
- Markdown table rows detected: approximately 621; this is a row count, not a table count.
- README chunk index created.
- Body text, notes, bibliography, and index are included.
- No page-boundary continuation loss was detected mechanically; page anchors were retained to support later checking.
- Complex tables with multi-row or multi-column headers were flattened; this is a structural compromise, not a character correction.

## Suggested next pass

A useful next pass would be a targeted structural audit of generated pipe tables, especially the dense vowel and consonant tables, plus a citation/reference spot-check across Chapter II, notes, bibliography, and index. The image-only tables and figures are preserved as assets, so character transcription of those image-only assets should be treated as a separate optional image-collation task.
