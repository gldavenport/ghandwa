---
title: "A Reader in Comparative Indo-European Mythology"
author: "Ranko Matasović"
date: "2009"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "matasović-2009-reader-comparative-ie-mythology.pdf"
chunk: "extraction-report"
---

# Extraction Report

## Source type

Born-digital PDF with a machine-readable text layer. The PDF was generated from Microsoft Word/Acrobat PDFMaker. The text layer was used as the primary source. Several pages contain embedded images of source texts, tables, and illustrations; those images were extracted into `images/` and referenced from the Markdown.

## Corrections applied

- Replaced private-use TimesNewRomanStar glyphs in the Vedic text with Unicode equivalents where the mapping was inferable from repeated contexts: `ā`, `ī`, `ū`, combining acute, combining grave, combining macron, combining dot above, and combining dot below.
- Applied NFC normalization after diacritic replacement.
- Normalized laryngeal indices in the extracted text layer from `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃`.
- Converted aspiration markers inside starred reconstructed forms from flattened `bh`, `dh`, `gh`, `g'h` to `bʰ`, `dʰ`, `gʰ`, `g'ʰ` where detected. This was restricted to starred forms to avoid changing English text.
- Replaced `n~` with `ñ` in Vedic/Sanskrit words, where the source text layer used ASCII fallback.
- Removed U+FFFE object-replacement/break artifacts produced by PDF extraction.
- Preserved page anchors as HTML comments for later source checking.
- Transcribed the image-only Brahmin / Flamen Dialis comparison table on page 5 into a Markdown table and retained the source image.

## Unresolved issues list

- Pages 15-16: the Hittite source text for “Illuyankas and the Storm God” is embedded as images. The images were extracted and referenced, but the cuneiform/logographic transliteration in those images was not fully hand-transcribed.
- Page 25: the Avestan source text for Varhrān Yašt 42-46 is embedded as an image. It was extracted and referenced, but not fully hand-transcribed.
- Page 26: the English translation of Varhrān Yašt 42-46 is embedded as an image and therefore is present as an extracted image. Any machine-readable text absent from the PDF layer remains image-only in this pass.
- Page 31: the Umbrian source text from Tabulae Iguvinae VIa is embedded as an image. The accompanying English translation is present in text, but the full original-source image text should be checked in a later source-text pass.
- Page 34: the Old Irish source text for the Connlae passage is embedded as an image. The English translation is machine-readable; the Old Irish image text should be checked in a later source-text pass.
- Page 40: the Byelorussian Cyrillic source text is embedded as an image. The English translation is machine-readable; the Cyrillic source text should be checked in a later source-text pass.
- Pages 19-24: the Vedic Sanskrit text used a private-use font encoding. A contextual mapping was applied, but Vedic accent placement should be spot-checked against the page images.
- Pages 19-24: some Vedic hymn text and English translations appear in visually irregular multi-column / spaced layouts. The text layer was preserved, but line order and stanza alignment should receive a dedicated Vedic-text pass before treating the Sanskrit as character-authoritative.
- Superscript aspiration was normalized only within starred reconstructed forms. Aspirates in unstarred comparanda may remain in the PDF layer's flattened ASCII style.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: laryngeal indices were normalized globally. Because the source text layer flattened subscripts, this should be visually spot-checked in dense formula passages.
- Macron vowels: private-use `ā ī ū` in Vedic passages were normalized. Pre-existing macron vowels in the text layer were preserved. Consistency in the Vedic source blocks remains uncertain until a dedicated Vedic pass.
- `ʰ ʷ` vs. `h w`: superscript aspiration was repaired only inside starred reconstructed forms. Superscript `ʷ` was not globally inferred because the source uses ordinary `w` in many notational contexts.
- `ə`: no source-wide replacement was attempted. Both `ə` and `ǝ` are counted together as schwa-like characters in the manifest.
- Underdot characters (`ṛ ḷ ṃ ṇ`): Vedic private-use dot-below marks were mapped to Unicode combining dot below and normalized. Some sequences may remain decomposed where Unicode lacks a precomposed equivalent.
- `ǵ ḱ` vs. `g' k'`: no conversion to `ǵ` or `ḱ` was applied because the visible source appears to use apostrophe notation (`g'`, `k'`).
- Asterisks: source asterisks before reconstructed forms were preserved.
- Dagger: no dagger instances were detected in the extracted output.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "h1": 18,
  "h2": 41,
  "h3": 6,
  "macron_a": 274,
  "macron_e": 57,
  "macron_i": 59,
  "macron_o": 50,
  "macron_u": 44,
  "schwa": 26,
  "greek_chars": 1380,
  "combining_diacritics": 118,
  "dagger": 0
}
```

## Structural integrity check

- Main text, bibliography, abbreviations, and illustrations are separated according to the source's logical structure.
- Bibliography was placed in a separate Markdown file.
- No index section was present.
- Image references in the Markdown point to extracted files in `images/`.
- Page anchors were retained for source checking.
- Multi-column Vedic and image-only source-text passages are the main residual structural risk.

## Image inventory

- images/matasovic-2009-reader-comparative-ie-mythology-p01-fig1.png; p1 fig1; page 1; caption: Cover image
- images/matasovic-2009-reader-comparative-ie-mythology-p05-fig1.png; p5 fig1; page 5; caption: Priest Prohibitions of Indic and Roman priest classes.
- images/matasovic-2009-reader-comparative-ie-mythology-p15-fig1.png; p15 fig1; page 15; caption: Illuyankas and the Storm God: Hittite source text, lines 1-23
- images/matasovic-2009-reader-comparative-ie-mythology-p16-fig1.png; p16 fig1; page 16; caption: Illuyankas and the Storm God: Hittite source text, continuation
- images/matasovic-2009-reader-comparative-ie-mythology-p25-fig1.png; p25 fig1; page 25; caption: Varhrān Yašt 42-46: Avestan source text
- images/matasovic-2009-reader-comparative-ie-mythology-p26-fig1.png; p26 fig1; page 26; caption: Varhrān Yašt 42-46: English translation
- images/matasovic-2009-reader-comparative-ie-mythology-p31-fig1.png; p31 fig1; page 31; caption: Tabulae Iguvinae VIa: Umbrian source text
- images/matasovic-2009-reader-comparative-ie-mythology-p34-fig1.png; p34 fig1; page 34; caption: Echtrae Chonnlai maic Cuinn Chétchathaig in so: Old Irish source text
- images/matasovic-2009-reader-comparative-ie-mythology-p40-fig1.png; p40 fig1; page 40; caption: A Byelorussian Charm: Cyrillic source text
- images/matasovic-2009-reader-comparative-ie-mythology-p43-fig1.png; p43 fig1; page 43; caption: A Hittite God
- images/matasovic-2009-reader-comparative-ie-mythology-p43-fig2.png; p43 fig2; page 43; caption: A Procession of Hittite Gods in the Sanctuary at Yazilikaya
- images/matasovic-2009-reader-comparative-ie-mythology-p44-fig1.png; p44 fig1; page 44; caption: A Vedic Sacrifice
- images/matasovic-2009-reader-comparative-ie-mythology-p44-fig2.png; p44 fig2; page 44; caption: Indra
- images/matasovic-2009-reader-comparative-ie-mythology-p45-fig1.png; p45 fig1; page 45; caption: Varuna
- images/matasovic-2009-reader-comparative-ie-mythology-p45-fig2.png; p45 fig2; page 45; caption: Agni
- images/matasovic-2009-reader-comparative-ie-mythology-p46-fig1.png; p46 fig1; page 46; caption: The Caryatides from a Greek Temple
- images/matasovic-2009-reader-comparative-ie-mythology-p46-fig2.png; p46 fig2; page 46; caption: A Statue of Apollo
- images/matasovic-2009-reader-comparative-ie-mythology-p47-fig1.png; p47 fig1; page 47; caption: Okeanos (from a Greek Vase)
- images/matasovic-2009-reader-comparative-ie-mythology-p47-fig2.png; p47 fig2; page 47; caption: The Suovetaurilia
- images/matasovic-2009-reader-comparative-ie-mythology-p48-fig1.png; p48 fig1; page 48; caption: A Roman Sacrifice
- images/matasovic-2009-reader-comparative-ie-mythology-p48-fig2.png; p48 fig2; page 48; caption: The Gundestrup Cauldron with Celtic deities
- images/matasovic-2009-reader-comparative-ie-mythology-p49-fig1.png; p49 fig1; page 49; caption: Taranis (Jupiter) from Châtelet
- images/matasovic-2009-reader-comparative-ie-mythology-p49-fig2.png; p49 fig2; page 49; caption: Thórr
- images/matasovic-2009-reader-comparative-ie-mythology-p50-fig1.png; p50 fig1; page 50; caption: A pagan Slavic idol
