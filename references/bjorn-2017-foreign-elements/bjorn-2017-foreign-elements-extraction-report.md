# bjorn-2017-foreign-elements extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The extraction used the raw text layer as primary input. Superscript/subscript characters were reconstructed from the PDF text spans where the text layer encoded them as small positioned glyphs rather than Unicode modifier/subscript characters.

## Corrections applied

- Rejoined ordinary wrapped prose lines into paragraphs where block structure indicated running prose.
- Removed repeated running headers and page numbers from the main text.
- Applied Unicode NFC normalization to combine decomposed macron/diacritic sequences where possible.
- Converted small raised PDF glyphs to Unicode modifier/superscript characters where detected, e.g. ʰ, ʷ, ¹, ².
- Converted small lowered PDF digits to Unicode subscripts where detected, especially h₁, h₂, h₃ and ə₂.
- Extracted embedded map/image files from the PDF into `images/` and inserted Markdown image links at map locations.

## Unresolved issues

- No `[unclear]` markers were inserted in this automated pass.
- Dense appendix tables and some discussion tables were preserved primarily by lineation rather than normalized into formal Markdown tables; a later table-specific pass could improve tabular structure.
- The index was preserved as line-oriented text to reduce diacritic loss risk, but index alignment was not fully human-verified.
- Superscript/subscript recovery depends on consistent PDF span geometry. It should be spot-checked in dense etymological entries before treating the extraction as character-authoritative.
- Some real source hyphenation versus line-break hyphenation may remain unresolved in prose.

## Confusion-pair report

- h₁ h₂ h₃: normalized from positioned small digits where detected; not fully verified manually throughout.
- ā ē ī ō ū: normalized with NFC; dense index and bibliography sections were not fully manually verified.
- ʰ ʷ: normalized from positioned small glyphs where detected; not fully verified manually throughout.
- ə: preserved from the text layer; not fully verified against rendered pages throughout.
- ṛ ḷ ṃ ṇ: preserved/normalized from the text layer; not fully verified manually throughout.
- ǵ ḱ: preserved/normalized from the text layer where present; not fully verified manually throughout.
- *: preserved from the text layer before reconstructed forms where present.
- †: no special correction applied; count below is approximate.

## Codepoint inventory

All counts are approximate and are intended for cross-pass comparison only.

- h1: 134
- h2: 223
- h3: 79
- macron_a: 205
- macron_e: 55
- macron_i: 50
- macron_o: 91
- macron_u: 53
- schwa: 106
- greek_chars: 1540
- combining_diacritics: 338
- dagger: 0

## Structural integrity check

- Headings were generated from the source’s chapter/section labels and the §4.1 alphabetical word-list headings.
- Bibliography and index are separate files.
- Page anchors were inserted as HTML comments using PDF page and calculated source-page labels.
- Embedded maps/images were extracted and listed below.
- Footnote markers and footnote text remain inline/source-proximate rather than converted to Markdown footnote syntax.

## Image inventory

- `images/bjorn-2017-foreign-elements-p1-fig1.jpeg` — cover image, PDF page 1: Cover illustration
- `images/bjorn-2017-foreign-elements-map2-a.jpeg` — Map 2.A, PDF page 35: Map 2.A: Attestations of languages in the historic Indo-European contact sphere
- `images/bjorn-2017-foreign-elements-map2-b.jpeg` — Map 2.B, PDF page 36: Map 2.B: Attestations of languages in the Caucasus and Northern Fertile Crescent
- `images/bjorn-2017-foreign-elements-map3-a.jpeg` — Map 3.A, PDF page 49: Map 3.A: Main homeland theories and other language families: The Pontic Steppe, Central Asia, Anatolia, and Transcaucasia (arrows indicate expected loanword trajectories)
