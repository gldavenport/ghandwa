# Extraction report

- Source file: `978-3-11-039324-8.epub.zip`
- Source type: EPUB with machine-readable XHTML text layer and discrete image files.
- EPUB internal image directory: `OPS/graphic/`.
- Output chunking: front matter plus 45 article/chapter files; per-article bibliography files when a `References` section was present.

## Corrections applied

- Decoded XHTML entities to Unicode characters directly from the EPUB text layer.
- Converted inline `<span class="sub">1</span>`, `<span class="sub">2</span>`, and `<span class="sub">3</span>` laryngeal-style digit spans to subscript Unicode where encountered, including inside italic/bold spans.
- Converted inline `<span class="sup">h</span>` and `<span class="sup">w</span>` to modifier-letter ʰ and ʷ where encountered, including inside italic/bold spans.
- Split per-article `References` sections into separate bibliography companion files.
- Copied EPUB image files from `OPS/graphic/` into `images/` without re-encoding or recompression; output filenames were normalized to kebab-case.
- Paragraph joins are based on the EPUB XHTML paragraph structure; no OCR-style paragraph reflow was applied.

## Unresolved-issues list

- `13_chapter06_fig_02.png` copied as `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-02.png` at 13_chapter06_4.xhtml: Avestan-script glyph sequence corresponding in context to ṇt.
- `13_chapter06_fig_03.png` copied as `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-03.png` at 13_chapter06_4.xhtml: Avestan-script glyph sequence corresponding in context to nt.
- Page ranges are recorded as `unknown` because this EPUB did not expose usable pagebreak markers in the XHTML layer.
- Many uncaptioned image-only linguistic tables/diagrams are preserved as image references. Their internal text was not transcribed, per EPUB image-handling instructions.

## Confusion-pair report

- h₁/h₂/h₃ vs h1/h2/h3: output contains approximately h₁=253, h₂=427, h₃=109; ASCII h1/h2/h3 instances were not exhaustively verified and may occur in bibliographic strings or non-laryngeal contexts.
- Precomposed macron vowels vs combining macron: precomposed counts ā=6588, ē=955, ī=1779, ō=1099, ū=711; combining sequences a/e/i/o/u + U+0304 approximate counts={'a': 8, 'e': 0, 'i': 0, 'o': 0, 'u': 0}; combining marks may be source-authentic where stacked accents are present.
- Macron retention across body text and bibliographies: checked approximately by codepoint inventory only; dense bibliography and table contexts were not visually verified.
- ʰ/ʷ vs ASCII h/w: inline <sup>h</sup> and <sup>w</sup> were converted to ʰ and ʷ by the converter where encoded as superscript spans; remaining ASCII h/w in forms were not exhaustively verified.
- ə vs e/9: ə approximate count=1253; no visual verification against images was performed except unresolved Avestan glyph images.
- ṛ/ḷ/ṃ/ṇ underdot letters: preserved from decoded XHTML where present; no exhaustive visual verification was performed.
- ǵ/ḱ acute consonants: preserved from decoded XHTML where present; no exhaustive visual verification was performed.
- Asterisk U+002A before reconstructed forms: preserved from XHTML text; no attempt was made to infer missing asterisks.
- Dagger U+2020: approximate count=2; plus signs and daggers were not visually cross-checked.

## Codepoint inventory

All counts are approximate and for cross-pass comparison only.

```json
{
  "laryngeals": {
    "h1": 253,
    "h2": 427,
    "h3": 109
  },
  "macron_a": 6588,
  "macron_e": 955,
  "macron_i": 1779,
  "macron_o": 1099,
  "macron_u": 711,
  "schwa": 1253,
  "greek_chars": 2359,
  "combining_diacritics": 4334,
  "dagger": 2
}
```

## Structural integrity check

- Article chunks detected: 45 expected 45; result: 45.
- Headings were generated from the source XHTML h1/h2/h3/h4 hierarchy. Part-level headings are represented in `README.md`, while article files begin at article heading level.
- Tables encoded as XHTML `<table>` were converted to Markdown tables. Image-only tables/diagrams were retained as image references.
- Per-article References sections were detached into bibliography files. Inline citations and ordinary footnote/endnote references were preserved in running text as decoded text.
- No page-boundary continuation loss was detected by the automated spine-walk; this cannot catch systematic source-layer omissions.

## Image-glyph inventory

### Substituted image glyphs
- `08_chapter01_fig_12.png` → `Fraktur` at 08_chapter01_2.xhtml.

### Unresolved image glyphs
- `13_chapter06_fig_02.png` copied as `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-02.png` at 13_chapter06_4.xhtml: Avestan-script glyph sequence corresponding in context to ṇt.
- `13_chapter06_fig_03.png` copied as `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-03.png` at 13_chapter06_4.xhtml: Avestan-script glyph sequence corresponding in context to nt.

## Image inventory

Complete copied image inventory, including ordinary figures/tables and inline glyph images:
- `01_Cover_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-01-cover-fig-01.png`
- `01_Cover_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-01-cover-fig-01.png`
- `04_Title_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-04-title-fig-01.png`
- `04_Title_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-04-title-fig-01.png`
- `08_chapter01_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-01.png`
- `08_chapter01_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-01.png`
- `08_chapter01_fig_02.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-02.png`
- `08_chapter01_fig_02.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-02.png`
- `08_chapter01_fig_03.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-03.png`
- `08_chapter01_fig_03.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-03.png`
- `08_chapter01_fig_04.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-04.png`
- `08_chapter01_fig_04.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-04.png`
- `08_chapter01_fig_05.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-05.png`
- `08_chapter01_fig_05.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-05.png`
- `08_chapter01_fig_06.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-06.png`
- `08_chapter01_fig_06.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-06.png`
- `08_chapter01_fig_07.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-07.png`
- `08_chapter01_fig_07.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-07.png`
- `08_chapter01_fig_08.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-08.png`
- `08_chapter01_fig_08.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-08.png`
- `08_chapter01_fig_09.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-09.png`
- `08_chapter01_fig_09.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-09.png`
- `08_chapter01_fig_10.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-10.png`
- `08_chapter01_fig_10.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-10.png`
- `08_chapter01_fig_11.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-11.png`
- `08_chapter01_fig_11.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-11.png`
- `08_chapter01_fig_12.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-12.png`
- `08_chapter01_fig_12.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-12.png`
- `08_chapter01_fig_13.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-13.png`
- `08_chapter01_fig_13.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-13.png`
- `08_chapter01_fig_14.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-14.png`
- `08_chapter01_fig_14.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-14.png`
- `08_chapter01_fig_15.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-15.png`
- `08_chapter01_fig_15.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-15.png`
- `08_chapter01_fig_16.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-16.png`
- `08_chapter01_fig_16.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-16.png`
- `08_chapter01_fig_17.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-17.png`
- `08_chapter01_fig_17.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-17.png`
- `08_chapter01_fig_18.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-18.png`
- `08_chapter01_fig_18.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-18.png`
- `08_chapter01_fig_19.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-19.png`
- `08_chapter01_fig_19.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-19.png`
- `08_chapter01_fig_20.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-20.png`
- `08_chapter01_fig_20.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-20.png`
- `08_chapter01_fig_21.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-21.png`
- `08_chapter01_fig_21.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-21.png`
- `08_chapter01_fig_22.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-22.png`
- `08_chapter01_fig_22.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-22.png`
- `08_chapter01_fig_23.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-23.png`
- `08_chapter01_fig_23.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-23.png`
- `08_chapter01_fig_24.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-24.png`
- `08_chapter01_fig_24.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-08-chapter01-fig-24.png`
- `11_chapter04_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-01.png`
- `11_chapter04_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-01.png`
- `11_chapter04_fig_02.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-02.png`
- `11_chapter04_fig_02.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-02.png`
- `11_chapter04_fig_03.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-03.png`
- `11_chapter04_fig_03.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-03.png`
- `11_chapter04_fig_04.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-04.png`
- `11_chapter04_fig_04.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-04.png`
- `11_chapter04_fig_05.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-05.png`
- `11_chapter04_fig_05.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-05.png`
- `11_chapter04_fig_06.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-06.png`
- `11_chapter04_fig_06.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-06.png`
- `11_chapter04_fig_07.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-07.png`
- `11_chapter04_fig_07.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-07.png`
- `11_chapter04_fig_08.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-08.png`
- `11_chapter04_fig_08.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-08.png`
- `11_chapter04_fig_09.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-09.png`
- `11_chapter04_fig_09.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-09.png`
- `11_chapter04_fig_10.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-10.png`
- `11_chapter04_fig_10.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-10.png`
- `11_chapter04_fig_11.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-11.png`
- `11_chapter04_fig_11.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-11.png`
- `11_chapter04_fig_12.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-12.png`
- `11_chapter04_fig_12.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-12.png`
- `11_chapter04_fig_13.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-13.png`
- `11_chapter04_fig_13.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-13.png`
- `11_chapter04_fig_14.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-14.png`
- `11_chapter04_fig_14.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-14.png`
- `11_chapter04_fig_15.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-15.png`
- `11_chapter04_fig_15.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-15.png`
- `11_chapter04_fig_16.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-16.png`
- `11_chapter04_fig_16.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-16.png`
- `11_chapter04_fig_17.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-17.png`
- `11_chapter04_fig_17.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-17.png`
- `11_chapter04_fig_18.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-18.png`
- `11_chapter04_fig_18.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-18.png`
- `11_chapter04_fig_19.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-19.png`
- `11_chapter04_fig_19.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-19.png`
- `11_chapter04_fig_20.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-20.png`
- `11_chapter04_fig_20.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-20.png`
- `11_chapter04_fig_21.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-21.png`
- `11_chapter04_fig_21.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-21.png`
- `11_chapter04_fig_22.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-22.png`
- `11_chapter04_fig_22.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-22.png`
- `11_chapter04_fig_23.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-23.png`
- `11_chapter04_fig_23.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-23.png`
- `11_chapter04_fig_24.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-24.png`
- `11_chapter04_fig_24.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-24.png`
- `11_chapter04_fig_25.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-25.png`
- `11_chapter04_fig_25.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-25.png`
- `11_chapter04_fig_26.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-26.png`
- `11_chapter04_fig_26.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-26.png`
- `11_chapter04_fig_27.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-27.png`
- `11_chapter04_fig_27.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-27.png`
- `11_chapter04_fig_28.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-28.png`
- `11_chapter04_fig_28.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-28.png`
- `11_chapter04_fig_29.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-29.png`
- `11_chapter04_fig_29.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-29.png`
- `11_chapter04_fig_30.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-30.png`
- `11_chapter04_fig_30.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-30.png`
- `11_chapter04_fig_31.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-31.png`
- `11_chapter04_fig_31.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-31.png`
- `11_chapter04_fig_32.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-32.png`
- `11_chapter04_fig_32.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-32.png`
- `11_chapter04_fig_33.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-33.png`
- `11_chapter04_fig_33.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-33.png`
- `11_chapter04_fig_34.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-34.png`
- `11_chapter04_fig_34.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-34.png`
- `11_chapter04_fig_35.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-35.png`
- `11_chapter04_fig_35.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-35.png`
- `11_chapter04_fig_36.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-36.png`
- `11_chapter04_fig_36.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-11-chapter04-fig-36.png`
- `12_chapter05_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-01.png`
- `12_chapter05_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-01.png`
- `12_chapter05_fig_03.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-03.png`
- `12_chapter05_fig_03.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-03.png`
- `12_chapter05_fig_04.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-04.png`
- `12_chapter05_fig_04.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-04.png`
- `12_chapter05_fig_05.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-05.png`
- `12_chapter05_fig_05.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-05.png`
- `12_chapter05_fig_06.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-06.png`
- `12_chapter05_fig_06.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-06.png`
- `12_chapter05_fig_07.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-07.png`
- `12_chapter05_fig_07.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-07.png`
- `12_chapter05_fig_08.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-08.png`
- `12_chapter05_fig_08.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-08.png`
- `12_chapter05_fig_09.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-09.png`
- `12_chapter05_fig_09.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-09.png`
- `12_chapter05_fig_10.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-10.png`
- `12_chapter05_fig_10.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-10.png`
- `12_chapter05_fig_11.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-11.png`
- `12_chapter05_fig_11.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-11.png`
- `12_chapter05_fig_12.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-12.png`
- `12_chapter05_fig_12.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-12.png`
- `12_chapter05_fig_13.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-13.png`
- `12_chapter05_fig_13.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-12-chapter05-fig-13.png`
- `13_chapter06_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-01.png`
- `13_chapter06_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-01.png`
- `13_chapter06_fig_02.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-02.png`
- `13_chapter06_fig_02.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-02.png`
- `13_chapter06_fig_03.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-03.png`
- `13_chapter06_fig_03.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-03.png`
- `13_chapter06_fig_04.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-04.png`
- `13_chapter06_fig_04.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-13-chapter06-fig-04.png`
- `14_chapter07_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-01.png`
- `14_chapter07_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-01.png`
- `14_chapter07_fig_02.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-02.png`
- `14_chapter07_fig_02.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-02.png`
- `14_chapter07_fig_03.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-03.png`
- `14_chapter07_fig_03.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-03.png`
- `14_chapter07_fig_04.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-04.png`
- `14_chapter07_fig_04.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-04.png`
- `14_chapter07_fig_05.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-05.png`
- `14_chapter07_fig_05.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-05.png`
- `14_chapter07_fig_06.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-06.png`
- `14_chapter07_fig_06.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-06.png`
- `14_chapter07_fig_07.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-07.png`
- `14_chapter07_fig_07.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-07.png`
- `14_chapter07_fig_08.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-08.png`
- `14_chapter07_fig_08.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-08.png`
- `14_chapter07_fig_09.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-09.png`
- `14_chapter07_fig_09.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-09.png`
- `14_chapter07_fig_10.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-10.png`
- `14_chapter07_fig_10.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-10.png`
- `14_chapter07_fig_11.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-11.png`
- `14_chapter07_fig_11.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-11.png`
- `14_chapter07_fig_12.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-12.png`
- `14_chapter07_fig_12.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-12.png`
- `14_chapter07_fig_13.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-13.png`
- `14_chapter07_fig_13.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-13.png`
- `14_chapter07_fig_14.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-14.png`
- `14_chapter07_fig_14.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-14.png`
- `14_chapter07_fig_15.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-15.png`
- `14_chapter07_fig_15.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-15.png`
- `14_chapter07_fig_16.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-16.png`
- `14_chapter07_fig_16.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-16.png`
- `14_chapter07_fig_17.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-17.png`
- `14_chapter07_fig_17.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-17.png`
- `14_chapter07_fig_18.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-18.png`
- `14_chapter07_fig_18.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-18.png`
- `14_chapter07_fig_19.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-19.png`
- `14_chapter07_fig_19.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-19.png`
- `14_chapter07_fig_20.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-20.png`
- `14_chapter07_fig_20.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-1-14-chapter07-fig-20.png`

## Output files

- `README.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-front-matter.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch01.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch01.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch02.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch02.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch03.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch03.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch04.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch04.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch05.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch05.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch06.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch06.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch07.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch07.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch08.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch08.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch09.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch09.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch10.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch10.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch11.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch11.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch12.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch12.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch13.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch13.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch14.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch14.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch15.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch15.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch16.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch17.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch17.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch18.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch18.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch19.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch19.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch20.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch20.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch21.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch21.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch22.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch22.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch23.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch23.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch24.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch24.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch25.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch25.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch26.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch26.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch27.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch27.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch28.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch28.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch29.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch29.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch30.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch30.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch31.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch31.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch32.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch32.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch33.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch33.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch34.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch34.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch35.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch35.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch36.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch36.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch37.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch37.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch38.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch38.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch39.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch39.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch40.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch40.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch41.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch41.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch42.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch42.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch43.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch43.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch44.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch44.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-ch45.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-bibliography-ch45.md`
- `handbook-comparative-historical-indo-european-linguistics-volume-1-extraction-report.md`
- `manifest.json`
