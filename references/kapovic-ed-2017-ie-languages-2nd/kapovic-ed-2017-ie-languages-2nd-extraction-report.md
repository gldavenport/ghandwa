# Extraction report — The Indo-European Languages

## Source type

EPUB. The embedded XHTML text layer was used directly as the primary source. Images were copied as discrete EPUB assets without recompression. One inline image glyph was substituted with Unicode after visual/contextual inspection.

## Corrections applied

- Converted laryngeal subscript digits in inline XHTML markup to Unicode subscript digits where represented as `<sub>1</sub>`, `<sub>2</sub>`, and `<sub>3</sub>`.
- Converted common superscript aspiration/labialization markup (`<sup>h</sup>`, `<sup>w</sup>`, and combinations such as `wh`) to Unicode modifier letters where directly represented in XHTML.
- Unwrapped internal EPUB hyperlinks while preserving visible page numbers, headings, index references, and cross-reference text where the custom converter was used.
- Preserved page anchors as `<!-- page: ... -->` comments.
- Separated per-section References divisions into bibliography files.
- Copied EPUB image assets to `images/` and rewrote Markdown image links to the renamed files.
- Substituted inline image glyph `page227.jpg` with Unicode `ἰός` in the Indo-Aryan chapter; recorded below.

## Image-glyph inventory

- `page227.jpg` → `ἰός`; context: `viṣá - ‘venom, poison’ < *wis-, cf. Gr. [image], Lat. uīrus`

## Unresolved-issues list

- No `[unclear]` markers were inserted during this pass.
- Image-only tables, maps, figures, tree diagrams, and plates are represented by copied image files and Markdown image references. Their internal text was not transcribed into Markdown. This remains the principal unresolved source-critical limitation of the EPUB extraction.
- Some uncaptioned diagram fragments named with `pg...jpg` were copied and linked as images using inferred page-based filenames; captions could not always be verified from the surrounding XHTML.
- Bibliography and index fidelity depends on the EPUB text layer. This pass did not compare every dense reference/index line against a printed visual rendering.

## Confusion-pair report

The following checks are approximate and cannot certify correctness. They are intended to identify obvious residual risks.

- ASCII h1/h2/h3 still present: approximately 0
- h<sub>1/2/3</sub> still present: approximately 0
- escaped reconstructed asterisk \* still present: approximately 151
- replacement character U+FFFD: approximately 0
- temporary page markers still present: approximately 0
- unavailable image placeholders: approximately 0

- `h₁ h₂ h₃`: normalized from HTML subscript markup where encountered; residual ASCII `h1/h2/h3` count above should be manually inspected if nonzero.
- Macron vowels: precomposed macron vowels were preserved where present in the EPUB text layer. Decomposed combining marks may remain where the EPUB source used them.
- `ʰ ʷ`: common superscript h/w markup was converted; nonstandard superscripts outside the mapped set remain as HTML `<sup>...</sup>` to avoid silent mis-conversion.
- `ə`: both `ə` and `ǝ` may occur because the EPUB source uses both in scholarly notation; this was not silently normalized.
- Underdot letters, acute consonants, asterisks, and daggers were not globally normalized beyond obvious Pandoc backslash-asterisk unescaping.

## Codepoint inventory

All counts are approximate and for cross-pass comparison only.

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 474,
    "h2": 766,
    "h3": 206
  },
  "macron_a": 2086,
  "macron_e": 862,
  "macron_i": 686,
  "macron_o": 795,
  "macron_u": 433,
  "schwa": 311,
  "greek_chars": 9233,
  "combining_diacritics": 2569,
  "dagger": 4
}
```

## Structural integrity check

- Output is chunked into 24 content/index Markdown files plus 20 bibliography files.
- README lists every output file with its section label, page range, and source coverage.
- Chapter/part headings are preserved from the EPUB structure; part divider pages are preserved as separate chunks.
- References sections were extracted to separate bibliography files.
- Tables encoded as HTML tables were converted by Pandoc to Markdown tables where possible; tables rendered as images were preserved as image references.
- The two EPUB index files were combined into one index file with one index paragraph per Markdown line.
- No page-boundary loss was detected by automated page-anchor preservation, but this was not checked visually page-by-page.

## Image inventory

Total copied image assets: 193.

- `images/kapovic-ed-2017-ie-languages-2nd-piii-figure1.jpg` — Figure; page 0; caption: Figure
- `images/kapovic-ed-2017-ie-languages-2nd-p2-figure1.jpg` — Map I.1 IE languages today; page 0; caption: Map I.1 IE languages today
- `images/kapovic-ed-2017-ie-languages-2nd-p6-figure2.jpg` — Map I.2 IE languages in the 1st millennium BCE; page 0; caption: Map I.2 IE languages in the 1st millennium BCE
- `images/kapovic-ed-2017-ie-languages-2nd-p13-figure1.jpg` — pg13.jpg; page 0; caption: pg13.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-table1-2.jpg` — Table 1.2 The reflection of PIE palatovelars in satem languages; page 0; caption: Table 1.2 The reflection of PIE palatovelars in satem languages
- `images/kapovic-ed-2017-ie-languages-2nd-map1-1.jpg` — Map 1.1 The centum - satem branches of IE; page 0; caption: Map 1.1 The centum - satem branches of IE
- `images/kapovic-ed-2017-ie-languages-2nd-table1-3.jpg` — Table 1.3 Basic reflexes of PIE stops (palatalizations and other special changes; page 0; caption: Table 1.3 Basic reflexes of PIE stops (palatalizations and other special changes, like Verner’s Law, are not included)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-4.jpg` — Table 1.4 The reflexes of PIE asyllabic resonants; page 0; caption: Table 1.4 The reflexes of PIE asyllabic resonants
- `images/kapovic-ed-2017-ie-languages-2nd-table1-5.jpg` — Table 1.5 The reflexes of PIE syllabic resonants; page 0; caption: Table 1.5 The reflexes of PIE syllabic resonants
- `images/kapovic-ed-2017-ie-languages-2nd-table1-6.jpg` — Table 1.6 The reflexes of PIE *CR̥HC; page 0; caption: Table 1.6 The reflexes of PIE *CR̥HC
- `images/kapovic-ed-2017-ie-languages-2nd-table1-7.jpg` — Table 1.7 The reflexes of PIE *CR̥HV; page 0; caption: Table 1.7 The reflexes of PIE *CR̥HV
- `images/kapovic-ed-2017-ie-languages-2nd-table1-8.jpg` — Table 1.8 The reflexes of PIE vowels; page 0; caption: Table 1.8 The reflexes of PIE vowels
- `images/kapovic-ed-2017-ie-languages-2nd-table1-9.jpg` — Table 1.9 The reflexes of PIE diphthongs; page 0; caption: Table 1.9 The reflexes of PIE diphthongs
- `images/kapovic-ed-2017-ie-languages-2nd-table1-10.jpg` — Table 1.10 IE o -stems (singular); page 0; caption: Table 1.10 IE o -stems (singular)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-11.jpg` — Table 1.11 IE o -stems (plural); page 0; caption: Table 1.11 IE o -stems (plural)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-11-2.jpg` — Table 1.11 IE o -stems (plural); page 0; caption: Table 1.11 IE o -stems (plural)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-12.jpg` — Table 1.12 IE o -stems (neuter); page 0; caption: Table 1.12 IE o -stems (neuter)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-13.jpg` — Table 1.13 IE o -stems (dual); page 0; caption: Table 1.13 IE o -stems (dual)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-14.jpg` — Table 1.14 IE eh 2 -stems (singular); page 0; caption: Table 1.14 IE eh 2 -stems (singular)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-15.jpg` — Table 1.15 IE eh 2 -stems (plural); page 0; caption: Table 1.15 IE eh 2 -stems (plural)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-19.jpg` — Table 1.19 IE i -stems (singular); page 0; caption: Table 1.19 IE i -stems (singular)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-20.jpg` — Table 1.20 IE i -stems (plural); page 0; caption: Table 1.20 IE i -stems (plural)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-21.jpg` — Table 1.21 IE u -stems (singular); page 0; caption: Table 1.21 IE u -stems (singular)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-22.jpg` — Table 1.22 IE u -stems (plural); page 0; caption: Table 1.22 IE u -stems (plural)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-23.jpg` — Table 1.23 IE r -stems (singular); page 0; caption: Table 1.23 IE r -stems (singular)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-24.jpg` — Table 1.24 IE r -stems (plural); page 0; caption: Table 1.24 IE r -stems (plural)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-25.jpg` — Table 1.25 IE n -stems (singular); page 0; caption: Table 1.25 IE n -stems (singular)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-26.jpg` — Table 1.26 IE n -stems (plural); page 0; caption: Table 1.26 IE n -stems (plural)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-27.jpg` — Table 1.27 IE s -stems (singular); page 0; caption: Table 1.27 IE s -stems (singular)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-28.jpg` — Table 1.28 IE s -stems (plural); page 0; caption: Table 1.28 IE s -stems (plural)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-29.jpg` — Table 1.29 IE demonstrative pronoun *so – *seh 2 – *tod (singular); page 0; caption: Table 1.29 IE demonstrative pronoun *so – *seh 2 – *tod (singular)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-30.jpg` — Table 1.30 IE demonstrative pronoun *so – *seh 2 – *tod (plural); page 0; caption: Table 1.30 IE demonstrative pronoun *so – *seh 2 – *tod (plural)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-32.jpg` — Table 1.32 IE demonstrative pronoun *ey (*is) – *ih 2 – *id (singular); page 0; caption: Table 1.32 IE demonstrative pronoun *ey (*is) – *ih 2 – *id (singular)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-33.jpg` — Table 1.33 IE demonstrative pronoun *ey (*is) – *ih 2 – *id (plural); page 0; caption: Table 1.33 IE demonstrative pronoun *ey (*is) – *ih 2 – *id (plural)
- `images/kapovic-ed-2017-ie-languages-2nd-table1-34.jpg` — Table 1.34 IE athematic present; page 0; caption: Table 1.34 IE athematic present
- `images/kapovic-ed-2017-ie-languages-2nd-table1-35.jpg` — Table 1.35 IE thematic present; page 0; caption: Table 1.35 IE thematic present
- `images/kapovic-ed-2017-ie-languages-2nd-table1-36.jpg` — Table 1.36 IE present dual endings; page 0; caption: Table 1.36 IE present dual endings
- `images/kapovic-ed-2017-ie-languages-2nd-table1-41.jpg` — Table 1.41 IE middle present; page 0; caption: Table 1.41 IE middle present
- `images/kapovic-ed-2017-ie-languages-2nd-table1-41-2.jpg` — Table 1.41 IE middle present; page 0; caption: Table 1.41 IE middle present
- `images/kapovic-ed-2017-ie-languages-2nd-table1-42.jpg` — Table 1.42 IE middle aorist; page 0; caption: Table 1.42 IE middle aorist
- `images/kapovic-ed-2017-ie-languages-2nd-table1-46.jpg` — Table 1.46 IE thematic optative; page 0; caption: Table 1.46 IE thematic optative
- `images/kapovic-ed-2017-ie-languages-2nd-table1-47.jpg` — Table 1.47 IE athematic imperative; page 0; caption: Table 1.47 IE athematic imperative
- `images/kapovic-ed-2017-ie-languages-2nd-table1-48.jpg` — Table 1.48 IE thematic imperative; page 0; caption: Table 1.48 IE thematic imperative
- `images/kapovic-ed-2017-ie-languages-2nd-p113-figure1.jpg` — pg113.jpg; page 0; caption: pg113.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p114-figure2.jpg` — pg114.jpg; page 0; caption: pg114.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p115-figure4.jpg` — pg115.jpg; page 0; caption: pg115.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-2.jpg` — Figure 1.2 Sentence scheme 1; page 0; caption: Figure 1.2 Sentence scheme 1
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-3.jpg` — Figure 1.3 Sentence scheme 2; page 0; caption: Figure 1.3 Sentence scheme 2
- `images/kapovic-ed-2017-ie-languages-2nd-p117-figure7.jpg` — pg117.jpg; page 0; caption: pg117.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-4.jpg` — Figure 1.4 Structure of Homer, Iliad 1,8; page 0; caption: Figure 1.4 Structure of Homer, Iliad 1,8
- `images/kapovic-ed-2017-ie-languages-2nd-p117-figure9.jpg` — pg117a.jpg; page 0; caption: pg117a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-5.jpg` — Figure 1.5 Structure of Homer Odyssey 4,353; page 0; caption: Figure 1.5 Structure of Homer Odyssey 4,353
- `images/kapovic-ed-2017-ie-languages-2nd-p118-figure11.jpg` — pg118.jpg; page 0; caption: pg118.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p119-figure12.jpg` — pg119.jpg; page 0; caption: pg119.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p119-figure13.jpg` — pg119a.jpg; page 0; caption: pg119a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p119-figure14.jpg` — pg119b.jpg; page 0; caption: pg119b.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p120-figure15.jpg` — pg120.jpg; page 0; caption: pg120.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p120-figure16.jpg` — pg120a.jpg; page 0; caption: pg120a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p121-figure17.jpg` — pg121.jpg; page 0; caption: pg121.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p121-figure18.jpg` — pg121a.jpg; page 0; caption: pg121a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p121-figure19.jpg` — pg121b.jpg; page 0; caption: pg121b.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p121-figure20.jpg` — pg121c.jpg; page 0; caption: pg121c.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p122-figure21.jpg` — pg122.jpg; page 0; caption: pg122.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-6.jpg` — Figure 1.6 Structure of Homer, Odyssey 20, 48; page 0; caption: Figure 1.6 Structure of Homer, Odyssey 20, 48
- `images/kapovic-ed-2017-ie-languages-2nd-p123-figure23.jpg` — pg123.jpg; page 0; caption: pg123.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p123-figure24.jpg` — pg123a.jpg; page 0; caption: pg123a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p124-figure25.jpg` — pg124.jpg; page 0; caption: pg124.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p127-figure28.jpg` — pg127.jpg; page 0; caption: pg127.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p127-figure29.jpg` — pg127a.jpg; page 0; caption: pg127a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p128-figure30.jpg` — pg128.jpg; page 0; caption: pg128.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p128-figure31.jpg` — pg128a.jpg; page 0; caption: pg128a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p129-figure32.jpg` — pg129.jpg; page 0; caption: pg129.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p129-figure33.jpg` — pg129a.jpg; page 0; caption: pg129a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p130-figure34.jpg` — pg130.jpg; page 0; caption: pg130.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p131-figure35.jpg` — pg131.jpg; page 0; caption: pg131.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p131-figure36.jpg` — pg131a.jpg; page 0; caption: pg131a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p132-figure37.jpg` — pg132.jpg; page 0; caption: pg132.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-7.jpg` — Figure 1.7 Structure of Rigveda 1,32,2; page 0; caption: Figure 1.7 Structure of Rigveda 1,32,2
- `images/kapovic-ed-2017-ie-languages-2nd-p134-figure39.jpg` — pg134.jpg; page 0; caption: pg134.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-8.jpg` — Figure 1.8 Structure of Homer, Iliad 18,468 / 1; page 0; caption: Figure 1.8 Structure of Homer, Iliad 18,468 / 1
- `images/kapovic-ed-2017-ie-languages-2nd-p134-figure41.jpg` — pg134a.jpg; page 0; caption: pg134a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-9.jpg` — Figure 1.9 Structure of Homer, Iliad 18,468 / 2; page 0; caption: Figure 1.9 Structure of Homer, Iliad 18,468 / 2
- `images/kapovic-ed-2017-ie-languages-2nd-p135-figure43.jpg` — pg135.jpg; page 0; caption: pg135.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-10.jpg` — Figure 1.10 Structure of Homer 5,97; page 0; caption: Figure 1.10 Structure of Homer 5,97
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-11.jpg` — Figure 1.11 Structure of Homer, Iliad 5,99; page 0; caption: Figure 1.11 Structure of Homer, Iliad 5,99
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-12.jpg` — Figure 1.12 Structure of Homer Iliad 5,100; page 0; caption: Figure 1.12 Structure of Homer Iliad 5,100
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-13.jpg` — Figure 1.13 Structure of Homer, Iliad 5,101; page 0; caption: Figure 1.13 Structure of Homer, Iliad 5,101
- `images/kapovic-ed-2017-ie-languages-2nd-p138-figure48.jpg` — pg138.jpg; page 0; caption: pg138.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p139-figure49.jpg` — pg139.jpg; page 0; caption: pg139.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p140-figure50.jpg` — pg140.jpg; page 0; caption: pg140.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p140-figure51.jpg` — pg140a.jpg; page 0; caption: pg140a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p140-figure52.jpg` — pg140b.jpg; page 0; caption: pg140b.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p140-figure53.jpg` — pg140c.jpg; page 0; caption: pg140c.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p141-figure54.jpg` — pg141.jpg; page 0; caption: pg141.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-figure1-14.jpg` — Figure 1.14 Hettrich 2002; page 0; caption: Figure 1.14 Hettrich 2002: 47 (slightly adapted): The spectrum of meaning of the R̥gvedic instrumental (prototypical meaning in the circle, other meanings radiating with arrows) with concurring cases (inside the rectangles)
- `images/kapovic-ed-2017-ie-languages-2nd-p142-figure56.jpg` — pg142.jpg; page 0; caption: pg142.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p142-figure57.jpg` — pg142a.jpg; page 0; caption: pg142a.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p142-figure58.jpg` — pg142b.jpg; page 0; caption: pg142b.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p143-figure59.jpg` — pg143.jpg; page 0; caption: pg143.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p145-figure60.jpg` — pg145.jpg; page 0; caption: pg145.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-map3-1.jpg` — Map 3.1 Anatolia in the Late Bronze Age; page 0; caption: Map 3.1 Anatolia in the Late Bronze Age
- `images/kapovic-ed-2017-ie-languages-2nd-map3-2.jpg` — Map 3.2 Anatolia in the Iron Age; page 0; caption: Map 3.2 Anatolia in the Iron Age
- `images/kapovic-ed-2017-ie-languages-2nd-table3-1.jpg` — Table 3.1 Anatolian nominal endings; page 0; caption: Table 3.1 Anatolian nominal endings
- `images/kapovic-ed-2017-ie-languages-2nd-table3-1-2.jpg` — Table 3.1 Anatolian nominal endings; page 0; caption: Table 3.1 Anatolian nominal endings
- `images/kapovic-ed-2017-ie-languages-2nd-table3-2.jpg` — Table 3.2 Anatolian personal pronouns; page 0; caption: Table 3.2 Anatolian personal pronouns
- `images/kapovic-ed-2017-ie-languages-2nd-table3-3.jpg` — Table 3.3 Anatolian anaphoric pronouns; page 0; caption: Table 3.3 Anatolian anaphoric pronouns
- `images/kapovic-ed-2017-ie-languages-2nd-table3-5.jpg` — Table 3.5 Hittite verbal inflection; page 0; caption: Table 3.5 Hittite verbal inflection
- `images/kapovic-ed-2017-ie-languages-2nd-table3-5-2.jpg` — Table 3.5 Hittite verbal inflection; page 0; caption: Table 3.5 Hittite verbal inflection
- `images/kapovic-ed-2017-ie-languages-2nd-figure4-1.jpg` — Figure 4.1 Chronology of Indo-Aryan languages and texts; page 0; caption: Figure 4.1 Chronology of Indo-Aryan languages and texts
- `images/kapovic-ed-2017-ie-languages-2nd-figure4-2.jpg` — Figure 4.2 Polyglossia in Ancient India (adapted from Bubenik 1998); page 0; caption: Figure 4.2 Polyglossia in Ancient India (adapted from Bubenik 1998)
- `images/kapovic-ed-2017-ie-languages-2nd-table4-4.jpg` — Table 4.4 Old Indo-Aryan consonantism; page 0; caption: Table 4.4 Old Indo-Aryan consonantism
- `images/kapovic-ed-2017-ie-languages-2nd-table4-6.jpg` — Table 4.6 The main alternation grades; page 0; caption: Table 4.6 The main alternation grades
- `images/kapovic-ed-2017-ie-languages-2nd-table4-13.jpg` — Table 4.13 Vedic verbal personal endings; page 0; caption: Table 4.13 Vedic verbal personal endings
- `images/kapovic-ed-2017-ie-languages-2nd-table4-14.jpg` — Table 4.14 Series of the PIE verbal endings; page 0; caption: Table 4.14 Series of the PIE verbal endings
- `images/kapovic-ed-2017-ie-languages-2nd-table4-15.jpg` — Table 4.15 PIE sources of Vedic personal endings; page 0; caption: Table 4.15 PIE sources of Vedic personal endings
- `images/kapovic-ed-2017-ie-languages-2nd-table4-15-2.jpg` — Table 4.15 PIE sources of Vedic personal endings; page 0; caption: Table 4.15 PIE sources of Vedic personal endings
- `images/kapovic-ed-2017-ie-languages-2nd-table4-16.jpg` — Table 4.16 The Vedic verbal system; page 0; caption: Table 4.16 The Vedic verbal system: examples
- `images/kapovic-ed-2017-ie-languages-2nd-table4-17.jpg` — Table 4.17 The Vedic verbal system; page 0; caption: Table 4.17 The Vedic verbal system: a selection of forms
- `images/kapovic-ed-2017-ie-languages-2nd-table4-18.jpg` — Table 4.18 The Vedic system of present stem types; page 0; caption: Table 4.18 The Vedic system of present stem types
- `images/kapovic-ed-2017-ie-languages-2nd-table4-19.jpg` — Table 4.19 The inventory of the present passive forms attested in the RV and AV; page 0; caption: Table 4.19 The inventory of the present passive forms attested in the RV and AV
- `images/kapovic-ed-2017-ie-languages-2nd-table4-20.jpg` — Table 4.20 Passive paradigm in early Vedic; page 0; caption: Table 4.20 Passive paradigm in early Vedic
- `images/kapovic-ed-2017-ie-languages-2nd-figure4-3.jpg` — Figure 4.3 Simple vowels; page 0; caption: Figure 4.3 Simple vowels
- `images/kapovic-ed-2017-ie-languages-2nd-figure4-4.jpg` — Figure 4.4 The First and second series of palatals in Iranian; page 0; caption: Figure 4.4 The First and second series of palatals in Iranian
- `images/kapovic-ed-2017-ie-languages-2nd-p271-figure4.jpg` — pg271.jpg; page 0; caption: pg271.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-table4-21.jpg` — Table 4.21 Declension of masculine a -stems (PIE stems in *o); page 0; caption: Table 4.21 Declension of masculine a -stems (PIE stems in *o)
- `images/kapovic-ed-2017-ie-languages-2nd-table4-25.jpg` — Table 4.25 Conjugation of the thematic present indicative active; page 0; caption: Table 4.25 Conjugation of the thematic present indicative active
- `images/kapovic-ed-2017-ie-languages-2nd-table9-1.jpg` — Table 9.1 The Armenian alphabet; page 0; caption: Table 9.1 The Armenian alphabet
- `images/kapovic-ed-2017-ie-languages-2nd-map9-1.jpg` — Map 9.1 Armenian in ancient and medieval times; page 0; caption: Map 9.1 Armenian in ancient and medieval times
- `images/kapovic-ed-2017-ie-languages-2nd-p424-figure3.jpg` — pg424.jpg; page 0; caption: pg424.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p424-figure4.jpg` — pg425.jpg; page 0; caption: pg425.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p436-figure5.jpg` — pg436.jpg; page 0; caption: pg436.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p437-figure6.jpg` — pg437.jpg; page 0; caption: pg437.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p440-figure7.jpg` — pg440.jpg; page 0; caption: pg440.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-p441-figure8.jpg` — pg441.jpg; page 0; caption: pg441.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-map10-1.jpg` — Map 10.1 Kucha (= Kuci) and its dependencies in Han times; page 0; caption: Map 10.1 Kucha (= Kuci) and its dependencies in Han times
- `images/kapovic-ed-2017-ie-languages-2nd-table10-2.jpg` — Table 10.2 Tocharian consonants; page 0; caption: Table 10.2 Tocharian consonants
- `images/kapovic-ed-2017-ie-languages-2nd-table10-6.jpg` — Table 10.6 Deictic pronouns in Tocharian; page 0; caption: Table 10.6 Deictic pronouns in Tocharian
- `images/kapovic-ed-2017-ie-languages-2nd-table10-7.jpg` — Table 10.7 First and second person pronouns in Tocharian; page 0; caption: Table 10.7 First and second person pronouns in Tocharian
- `images/kapovic-ed-2017-ie-languages-2nd-table10-8.jpg` — Table 10.8 Tocharian numbers from ‘one’ to ‘ten’; page 0; caption: Table 10.8 Tocharian numbers from ‘one’ to ‘ten’
- `images/kapovic-ed-2017-ie-languages-2nd-p474-figure6.jpg` — pg474.jpg; page 0; caption: pg474.jpg
- `images/kapovic-ed-2017-ie-languages-2nd-map11-1.jpg` — Map 11.1 Baltic tribes at the beginning of the second millenium ad; page 0; caption: Map 11.1 Baltic tribes at the beginning of the second millenium ad
- `images/kapovic-ed-2017-ie-languages-2nd-figure5-1.jpg` — Figure 5.1 Vowel system of Proto-Attic-Ionic after compensatory lengthening; page 0; caption: Figure 5.1 Vowel system of Proto-Attic-Ionic after compensatory lengthening
- `images/kapovic-ed-2017-ie-languages-2nd-figure5-2.jpg` — Figure 5.2 Vowel system of Proto-Attic-Ionic after compensatory lengthening; page 0; caption: Figure 5.2 Vowel system of Proto-Attic-Ionic after compensatory lengthening
- `images/kapovic-ed-2017-ie-languages-2nd-figure5-3.jpg` — Figure 5.3 Vowel system of classical Attic, showing official spellings after 403; page 0; caption: Figure 5.3 Vowel system of classical Attic, showing official spellings after 403 BC
- `images/kapovic-ed-2017-ie-languages-2nd-table5-3.jpg` — Table 5.3 Forms of the first declension ( a -stems) in classical Attic; page 0; caption: Table 5.3 Forms of the first declension ( a -stems) in classical Attic
- `images/kapovic-ed-2017-ie-languages-2nd-table5-5.jpg` — Table 5.5 Underlying endings of third declension, and consonant stem forms in cl; page 0; caption: Table 5.5 Underlying endings of third declension, and consonant stem forms in classical Attic
- `images/kapovic-ed-2017-ie-languages-2nd-table5-6.jpg` — Table 5.6 Forms of the third-declension s -stems, i -stems and u -stems in class; page 0; caption: Table 5.6 Forms of the third-declension s -stems, i -stems and u -stems in classical Attic
- `images/kapovic-ed-2017-ie-languages-2nd-table5-9.jpg` — Table 5.9 Thematic and athematic primary and secondary endings of the active voi; page 0; caption: Table 5.9 Thematic and athematic primary and secondary endings of the active voice
- `images/kapovic-ed-2017-ie-languages-2nd-table5-11.jpg` — Table 5.11 Εndings of the middle voice; page 0; caption: Table 5.11 Εndings of the middle voice
- `images/kapovic-ed-2017-ie-languages-2nd-table5-12.jpg` — Table 5.12 Forms of the perfect and pluperfect in classical Attic; page 0; caption: Table 5.12 Forms of the perfect and pluperfect in classical Attic
- `images/kapovic-ed-2017-ie-languages-2nd-figure6-1.jpg` — Figure 6.1 Fibula Praenestina (CIL 1 2 .3). Reproduced by permission of the Cent; page 0; caption: Figure 6.1 Fibula Praenestina (CIL 1 2 .3). Reproduced by permission of the Center for Epigraphical and Palaeographical Studies, the Ohio State University
- `images/kapovic-ed-2017-ie-languages-2nd-table6-1.jpg` — Table 6.1 The phonemes of Classical Latin; page 0; caption: Table 6.1 The phonemes of Classical Latin
- `images/kapovic-ed-2017-ie-languages-2nd-table6-2.jpg` — Table 6.2 Classical Latin consonant-stem endings; page 0; caption: Table 6.2 Classical Latin consonant-stem endings
- `images/kapovic-ed-2017-ie-languages-2nd-table6-3.jpg` — Table 6.3 Classical Latin o -stem endings; page 0; caption: Table 6.3 Classical Latin o -stem endings
- `images/kapovic-ed-2017-ie-languages-2nd-table6-4.jpg` — Table 6.4 Classical Latin noun paradigms, masculine and feminine genders; page 0; caption: Table 6.4 Classical Latin noun paradigms, masculine and feminine genders
- `images/kapovic-ed-2017-ie-languages-2nd-table6-11.jpg` — Table 6.11 Latin conjugation classes; page 0; caption: Table 6.11 Latin conjugation classes
- `images/kapovic-ed-2017-ie-languages-2nd-table6-12.jpg` — Table 6.12 Subjunctive mood (2 sg. act.); page 0; caption: Table 6.12 Subjunctive mood (2 sg. act.)
- `images/kapovic-ed-2017-ie-languages-2nd-map7-1.jpg` — kapovic-ed-2017-ie-languages-2nd-map7-1.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-map7-2.jpg` — kapovic-ed-2017-ie-languages-2nd-map7-2.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-figure8-1.jpg` — kapovic-ed-2017-ie-languages-2nd-figure8-1.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-table8-1.jpg` — kapovic-ed-2017-ie-languages-2nd-table8-1.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p394-figure3.jpg` — kapovic-ed-2017-ie-languages-2nd-p394-figure3.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p395-figure4.jpg` — kapovic-ed-2017-ie-languages-2nd-p395-figure4.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-table8-4.jpg` — Table 8.4 Germanic strong verbs, classes I–V; page 0; caption: Table 8.4 Germanic strong verbs, classes I–V
- `images/kapovic-ed-2017-ie-languages-2nd-table8-4-2.jpg` — Table 8.4 Germanic strong verbs, classes I–V; page 0; caption: Table 8.4 Germanic strong verbs, classes I–V
- `images/kapovic-ed-2017-ie-languages-2nd-p400-figure7.jpg` — kapovic-ed-2017-ie-languages-2nd-p400-figure7.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p400-figure8.jpg` — kapovic-ed-2017-ie-languages-2nd-p400-figure8.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-table8-5.jpg` — kapovic-ed-2017-ie-languages-2nd-table8-5.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-table8-6.jpg` — kapovic-ed-2017-ie-languages-2nd-table8-6.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-table11-12.jpg` — Table 11.12 Late Common Slavic vowels; page 0; caption: Table 11.12 Late Common Slavic vowels
- `images/kapovic-ed-2017-ie-languages-2nd-table11-20.jpg` — kapovic-ed-2017-ie-languages-2nd-table11-20.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-table11-26.jpg` — kapovic-ed-2017-ie-languages-2nd-table11-26.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p561-figure2.jpg` — kapovic-ed-2017-ie-languages-2nd-p561-figure2.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p562-figure3.jpg` — kapovic-ed-2017-ie-languages-2nd-p562-figure3.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-table12-8.jpg` — kapovic-ed-2017-ie-languages-2nd-table12-8.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-table12-12.jpg` — kapovic-ed-2017-ie-languages-2nd-table12-12.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p601-figure6.jpg` — kapovic-ed-2017-ie-languages-2nd-p601-figure6.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p601-figure7.jpg` — kapovic-ed-2017-ie-languages-2nd-p601-figure7.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p602-figure8.jpg` — kapovic-ed-2017-ie-languages-2nd-p602-figure8.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p602-figure9.jpg` — kapovic-ed-2017-ie-languages-2nd-p602-figure9.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-map11-2.jpg` — kapovic-ed-2017-ie-languages-2nd-map11-2.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-map12-1.jpg` — kapovic-ed-2017-ie-languages-2nd-map12-1.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-map5-1.jpg` — kapovic-ed-2017-ie-languages-2nd-map5-1.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-map6-1.jpg` — kapovic-ed-2017-ie-languages-2nd-map6-1.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-map6-2.jpg` — kapovic-ed-2017-ie-languages-2nd-map6-2.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p114-figure3.jpg` — kapovic-ed-2017-ie-languages-2nd-p114-figure3.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p125-figure26.jpg` — kapovic-ed-2017-ie-languages-2nd-p125-figure26.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p126-figure27.jpg` — kapovic-ed-2017-ie-languages-2nd-p126-figure27.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-p265-figure1.jpg` — kapovic-ed-2017-ie-languages-2nd-p265-figure1.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-punknown-cover1.jpg` — kapovic-ed-2017-ie-languages-2nd-punknown-cover1.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-table11-19.jpg` — kapovic-ed-2017-ie-languages-2nd-table11-19.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-table4-2-2.jpg` — kapovic-ed-2017-ie-languages-2nd-table4-2-2.jpg; page 0; caption: [no caption]
- `images/kapovic-ed-2017-ie-languages-2nd-table4-2.jpg` — kapovic-ed-2017-ie-languages-2nd-table4-2.jpg; page 0; caption: [no caption]
