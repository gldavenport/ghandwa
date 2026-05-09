---
title: Contact and the Celtic Languages
author: Joseph F. Eska
date: 2020
source_type: born-digital
extraction_date: 2026-05-08
source_file: eska-2020-contact-celtic-languages.pdf
chunk: extraction-report
---

# Extraction Report — eska-2020-contact-celtic-languages

## Source type

Born-digital PDF. A machine-readable text layer is present. The raw extracted text was used as the primary input, with rendered-page inspection used selectively for visibly superscripted phonetic characters, obvious glyph-composition artifacts, and high-risk linguistic notation.

PDF metadata reports title *The Handbook of Language Contact*, author Raymond Hickey, 12 pages, and embedded fonts with Unicode maps for most fonts. `pdfimages -list` returned no embedded raster figures.

## Output files

- `eska-2020-contact-celtic-languages.md`
- `eska-2020-contact-celtic-languages-bibliography.md`
- `eska-2020-contact-celtic-languages-extraction-report.md`
- `manifest.json`

## Corrections applied

- Rejoined broken hyphenation and lineation from the PDF text layer, including page-boundary breaks and two-column bibliography flow.
- Removed running headers, footers, page numbers, and publisher footer matter from the corpus text.
- Converted source notes into Markdown footnotes while preserving note wording.
- Separated the `REFERENCES` section into `eska-2020-contact-celtic-languages-bibliography.md`.
- Normalized visually simple macron vowels to precomposed Unicode where the text layer exposed decomposed sequences, e.g. `lēgātus` → `lēgātus`, `amāveram` → `amāveram`, `sindā` → `sindā`, and `‐ı̄` → `‐ī`.
- Restored visibly superscript aspiration notation from rendered pages where the text layer linearized it as plain `h`, e.g. `/pʰ tʰ kʰ/`, `[kʰaʰt]`, and `*/pʰ/‐`.
- Reconstructed short examples and formula-like bracketed syntactic structures into Markdown tables or fenced text blocks to avoid loss from prose reflow.
- Normalized `Matasović` to precomposed `Matasović` where the source rendered a c-acute name.

Ligature repairs: unknown. Paragraph rejoins: unknown.

## Unresolved-issues list

- The Galatian/Lycian form rendered in the text layer as `Aρμɛδυμνoϛ` appears to mix Latin and Greek-range characters. Rendered inspection confirms the form visually but does not fully disambiguate every code point. It is preserved from the text layer.
- The deictic pronominal form `*k̑ei̯` includes combining diacritics from the text layer. Rendered inspection confirms a marked `k` plus final glide-like notation, but the exact Unicode representation is still text-layer dependent.
- The form `tud̄(d̄on)` is preserved with combining macrons over consonants because no precomposed equivalent exists. The exact visual attachment in the source was checked, but combining placement may vary by renderer.
- In examples (4a–b), the raw text layer forms `=ii`, `pannai`, `śoi`, and `atomi` are retained rather than normalized to a more interpretive segmentation.
- Bibliography title formatting was not exhaustively encoded as Markdown italics; content and character fidelity were prioritized over typographic styling.
- No `[unclear]` or `[?]` markers were inserted in the corpus files. This reflects use of the born-digital text layer, not a claim that the extraction is error-free.

## Confusion-pair report

- `h₁ h₂ h₃`: no laryngeal-index forms were present in the extracted chapter. Approximate counts are all zero.
- `ā ē ī ō ū`: macron vowels were normalized to precomposed Unicode where plain Latin vowel + combining macron was clearly an extraction artifact. Dense bibliography and notes were checked selectively, not certified exhaustively.
- Superscript `ʰ`: restored in the aspiration passages and note 4 after rendered-page verification. Superscript `ʷ` was not observed.
- `ə`: no schwa forms were observed in the output.
- `ṛ ḷ ṃ ṇ`: no Indic underdot forms were observed in the output.
- `ǵ ḱ`: no precomposed acute-on-consonant forms were observed. The source has `*k̑ei̯`, which is not silently normalized to `*ḱei`.
- `*`: reconstructed forms and marked forms with asterisks were preserved where present.
- `†`: no dagger signs were observed.
- Greek/Celtic inscriptional forms: `πραιτωρ`, `Aρμɛδυμνoϛ`, and forms containing `ś`/combining accent were reviewed; some codepoint uncertainty remains for `Aρμɛδυμνoϛ` and `*k̑ei̯` as noted above.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 4,
  "macron_e": 1,
  "macron_i": 1,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 0,
  "greek_chars": 21,
  "combining_diacritics": 7,
  "dagger": 0
}
```

## Structural integrity check

- Headings were made consistent using Markdown levels for chapter sections and subsections.
- Notes are attached as Markdown footnotes and remain in the main text file.
- The bibliography is a separate file and retains one reference per paragraph.
- No index is present in the source.
- No figures, maps, plates, or image-only tables were found; no `images/` directory was created.
- No continuation text was intentionally dropped at page boundaries; page geometry and running headers were ignored.

## Image inventory

No images were extracted. No `[image-only ...]` fallback placeholders were used.
