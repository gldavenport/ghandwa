---
title: "The etymology of Latin focus and the devoicing of final stops before *s in Proto-Indo-European"
author: "Ranko Matasović"
date: "2010"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "matasovic-2010-etymology-latin-focus.pdf"
chunk: "extraction-report"
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The raw text layer was used as the primary input. Visual render checks were used as fallback for characters and passages that the text layer flattened, truncated, or corrupted, especially superscript aspiration/labialization notation, PIE vowel length, the laryngeal index in *peh₂ĝ-, Armenian transliteration marks, and dropped text on pp. 214 and 216.

## Corrections applied

- Rejoined paragraphs and repaired line-break hyphenation from the PDF text layer.
- Removed running headers, page numbers, JSTOR download boilerplate, journal footer lines, and repeated copyright/footer material from the clean corpus files.
- Preserved the JSTOR/source metadata in the main file metadata section and YAML rather than repeating the cover-page boilerplate.
- Separated the References section into `matasovic-2010-etymology-latin-focus-bibliography.md`.
- Attached four footnotes to the main article text using Markdown footnote syntax.
- Restored multiple character-level items from visual rendering where the text layer flattened them: ʰ, ʷ, ō, ā, ī, h₂, ĝ, ǫ, ъ, ь, and several accented Lithuanian/Slavic/Sanskrit forms.
- Restored p. 214 and p. 216 passages that the extracted text layer partially dropped or truncated.
- Preserved the author's use of German-style quotation marks („…“) in the article text.

## Unresolved issues / human-review targets

The following output items should be treated as review targets rather than certified readings:

1. Page 212: Armenian _bocʿ_ and _-cʿ-_ were restored from visual rendering plus standard Armenological transliteration; the PDF text layer reads them as `bocc` / `-cc-`.
2. Page 212: Lith. _žvãkė_ was restored from the rendered page; the raw text layer did not preserve the initial ž or the Lithuanian diacritics reliably.
3. Page 213: PCelt. *tepnet- was restored against the rendered page; the raw text layer reads `*tefnet-`.
4. Page 214: the first paragraph on the page was reconstructed from the rendered page because the text layer dropped right-side continuations for multiple lines.
5. Page 214: Lith. _gardas_ is left without accent marking because the rendered page did not clearly require one; review against a higher-resolution source if this form matters.
6. Page 215: Gr. _pegnymi_ is left without restored accent/macron marking because the rendered page did not make a diacritic unambiguous.
7. Page 216: the bibliography entries for IEW and LIV were reconstructed from the rendered page because the text layer truncated both titles.

No `[unclear]` or `[?]` markers were inserted in the clean corpus files; instead, the doubtful or visually restored items are listed here so the main extraction remains usable for corpus search.

## Confusion-pair report

- `h₁ h₂ h₃`: output contains h₂ in *peh₂ĝ-. No h₁ or h₃ expected from this source. The h₂ was restored from visual rendering.
- `ā ē ī ō ū`: macron vowels were restored in multiple forms. Dense source forms involving ō and ā were checked visually, but the list cannot be certified as exhaustive.
- Macron consistency across body/footnotes/bibliography: checked for the article body and footnotes; bibliography titles were visually checked where the text layer was truncated.
- `ʰ ʷ`: restored throughout the PIE notation where the raw layer flattened them to ASCII h/w. This is the highest-risk correction class in the extraction.
- `ə`: no instances expected or found.
- `ṛ ḷ ṃ ṇ`: output contains ṛ in Skt. _gṛhá-_. No ḷ, ṃ, or ṇ expected or found.
- `ǵ ḱ`: no ǵ or ḱ found. The source appears to use ĝ for palatovelar notation in the relevant forms, so ĝ was preserved rather than normalizing to ǵ.
- `*`: reconstructed forms preserve literal asterisks. Asterisks were not escaped, to preserve raw corpus searchability.
- `†`: no dagger instances expected or found.
- Source-specific risk: Armenian transliteration mark ʿ; Old Church Slavonic ǫ/ъ/ь; Lithuanian accent and pitch marks; and German-style low-high quotation marks.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 0,
    "h2": 1,
    "h3": 0
  },
  "macron_a": 6,
  "macron_e": 3,
  "macron_i": 1,
  "macron_o": 9,
  "macron_u": 0,
  "schwa": 0,
  "greek_chars": 0,
  "combining_diacritics": 0,
  "dagger": 0,
  "superscript_h": 50,
  "superscript_w": 23,
  "g_circumflex": 2,
  "r_underdot": 1
}
```

## Structural integrity check

- Main article body is a single Markdown file, as appropriate for a journal article.
- References are separated into a bibliography file.
- Footnotes are attached with Markdown footnote markers and definitions.
- No figures, tables, plates, maps, or image-only content were present in the article body.
- No index is present.
- No continuation text is known to be lost at page boundaries after the visual restoration pass, but the p. 214 reconstruction remains the most important target for any future pass.

## Image inventory

No figures, diagrams, maps, plates, or tables rendered as images were present. No `images/` directory was produced.
