---
title: "Comparative Indo-European Linguistics: An Introduction — Extraction report"
author: "Robert S. P. Beekes; revised and corrected by Michiel de Vaan"
date: "2011"
source_type: born-digital
extraction_date: 2026-05-07
source_file: "beekes-2011-comparative-ie-linguistics.pdf"
chunk: "extraction-report"
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The raw text layer was the primary input; rendered page images were used for spot checks and for the maps/illustrations pages.

## Corrections applied

- Repaired page-level lineation and many line-break hyphenations in running prose.
- Removed running headers, top folios, and standalone page-number lines where detected.
- Normalized laryngeal notation from ASCII `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃` throughout extracted Markdown.
- Normalized `k´`/`g´` to `ḱ`/`ǵ`; NFC normalization was applied after glyph substitutions.
- Preserved page anchors as HTML comments of the form `<!-- pdf-page: N -->`.
- Rendered cover, maps, and illustrations pages as PNG files in `images/` and inserted Markdown image references.
- Applied source-specific private-use glyph substitutions. Approximate substitution inventory:

  - `\u0131\ue034->ī́`: 13
  - `\u0269\ue034->ī́`: 7
  - `\u205c\u6e20->‑`: 40
  - `\u5c6e->[unclear-private-glyph]`: 21
  - `\ue188->̣`: 2
  - `\ue308->̣`: 26
  - `\uf6d6->[unclear-private-glyph]`: 4
  - `\uf8fc\uf8fd\uf8fe->[unclear-private-glyphs]`: 1
  - `\x07->`: 47
  - `\x08->`: 24
  - `a\ue033->ā́`: 1
  - `a\ue034->ā́`: 100
  - `a\ue034\u0304->ā́`: 1
  - `e\ue02b->ė́`: 23
  - `e\ue034->ḗ`: 1
  - `e\ue035->ė`: 2
  - `o\ue033->ṓ`: 1
  - `o\ue034->ṓ`: 1
  - `u\ue01f->ǖ`: 2
  - `u\ue032->ū́`: 1
  - `u\ue034->ū́`: 21

## Unresolved issues

- The PDF text layer uses several custom/private glyphs for composed diacritics. Common high-confidence substitutions were applied, but the result should not be treated as character-authoritative without a second pass against rendered page images.
- Dense paradigms and multi-column tables were preserved as line-oriented blocks rather than fully reconstructed Markdown tables. Some column alignment may remain imperfect.
- Several paradigm pages contain corrupted extracted symbols (`[unclear-private-glyph]` / `[unclear-private-glyphs]`) where the text layer could not be confidently resolved automatically. These require visual review.
- Footnotes are generally preserved in reading order but have not been manually audited one-by-one for attachment to the corresponding anchor.
- Italics/bold/small caps are not exhaustively represented; the extraction prioritizes characters and text content over typographic markup.

## Confusion-pair report

- `h₁ h₂ h₃` vs `h1 h2 h3`: laryngeal normalization applied; approximate remaining ASCII laryngeal-like sequences: 12.
- Precomposed macrons vs decomposed macrons: NFC normalization applied; remaining combining macron count: 24.
- Superscript `ʰ`/`ʷ`: preserved where present in extracted text; not exhaustively verified visually.
- Schwa `ə`: approximate count 103; not exhaustively verified visually.
- Underdot characters: private dot-below glyphs were mapped to Unicode combining dot below and NFC-normalized where possible; not exhaustively verified.
- `ǵ`/`ḱ`: acute consonant forms normalized where extraction produced `g´`/`k´`; not exhaustively verified.
- Asterisk before reconstructed forms: preserved from text layer; not exhaustively verified.
- Dagger `†`: approximate count 0; no global correction applied.
- Remaining private-use characters: 0; remaining raw control characters: 1.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 515,
    "h2": 689,
    "h3": 138
  },
  "macron_a": 1259,
  "macron_e": 895,
  "macron_i": 457,
  "macron_o": 1006,
  "macron_u": 326,
  "schwa": 103,
  "greek_chars": 163,
  "combining_diacritics": 760,
  "dagger": 0
}
```

## Structural integrity check

- Chapter-level chunking follows the PDF outline and source table of contents.
- Bibliography and index were separated into standalone files.
- README lists all output files and page ranges.
- Maps and illustrations are represented both as rendered page images and as extracted caption/text-layer content where available.
- No claim of full correctness is made; a second pass should focus on private glyphs, tables/paradigms, and the index.

## Image inventory

- `images/beekes-2011-comparative-ie-linguistics-pdf1-cover.png` — cover, page 1: Cover
- `images/beekes-2011-comparative-ie-linguistics-p343-map.png` — Maps p. 343, page 343: Map 1. The Indo-European languages. — Anatolian (Hittite and its relatives) has died out, as did
- `images/beekes-2011-comparative-ie-linguistics-p344-map.png` — Maps p. 344, page 344: Map 2. Countries where an Indo-European language is spoken, either as the first or as an officially
- `images/beekes-2011-comparative-ie-linguistics-p345-map.png` — Maps p. 345, page 345: Map 3. The Iranian languages. — The Iranian languages at the time of their greatest expansion. Ver-
- `images/beekes-2011-comparative-ie-linguistics-p346-map.png` — Maps p. 346, page 346: Map 4. The Anatolian languages — This group probably arrived from the north-west, across the
- `images/beekes-2011-comparative-ie-linguistics-p347-map.png` — Maps p. 347, page 347: Map 5. The Slavic languages — Note the position of Sorbian in east Germany. Rumanian is a
- `images/beekes-2011-comparative-ie-linguistics-p348-map.png` — Maps p. 348, page 348: Map 6. The Thracian tribes — The Thracians lived mostly in present-day Bulgaria. Serdica is now
- `images/beekes-2011-comparative-ie-linguistics-p349-map.png` — Maps p. 349, page 349: Map 7. Italy — Etruscan is a non-Indo-European language that came from the Aegean area. Greek
- `images/beekes-2011-comparative-ie-linguistics-p350-map.png` — Maps p. 350, page 350: Map 8. The expansion of the Celts — The Celts can be traced back to central Europe, from where
- `images/beekes-2011-comparative-ie-linguistics-p351-map.png` — Maps p. 351, page 351: Map 9. The Celtic tribes in Britain — The whole of England, and Ireland, was Celtic at the time of
- `images/beekes-2011-comparative-ie-linguistics-p352-map.png` — Maps p. 352, page 352: Map 10. The Jastorf culture — This culture (nr. 1) is the oldest stage which we can confidently
- `images/beekes-2011-comparative-ie-linguistics-p353-map.png` — Maps p. 353, page 353: Map 11. The Sredny Stog culture — The latest research has confirmed the old view that the Indo-Europeans originated from the south Russian steppes,
- `images/beekes-2011-comparative-ie-linguistics-p354-map.png` — Maps p. 354, page 354: Map 12. The Yamnaya (Pit Grave) culture — This complex, that stretched out over a very great area, developed out of the Sredny Stog culture. (The
- `images/beekes-2011-comparative-ie-linguistics-p355-map.png` — Maps p. 355, page 355: Map 12a. An Indo-European burial — A burial with the dead with flexed legs, a position which
- `images/beekes-2011-comparative-ie-linguistics-p356-map.png` — Maps p. 356, page 356: Map 12b. Wheels in the Yamnaya (Pit Grave) culture. — During this culture the first evidence for
- `images/beekes-2011-comparative-ie-linguistics-p357-map.png` — Maps p. 357, page 357: Map 13. The Corded Ware complex — This complex of cultures (among them the Battle-Axe
- `images/beekes-2011-comparative-ie-linguistics-p358-map.png` — Maps p. 358, page 358: Map 14. The first Indo-Europeans in Asia — The Tocharians, in Xinjiang, may be a continuation of
- `images/beekes-2011-comparative-ie-linguistics-p359-illustration.png` — Illustrations p. 359, page 359: Illustration 1. Sanskrit, devanāgarī-script. — A strophe from the Rigveda (II 12,1). Indra is one of
- `images/beekes-2011-comparative-ie-linguistics-p360-illustration.png` — Illustrations p. 360, page 360: Illustration 2. Avestan script, to be read from right to left. A passage from the Gatha-Avesta of
- `images/beekes-2011-comparative-ie-linguistics-p361-illustration.png` — Illustrations p. 361, page 361: Illustration 3. Old Persian cuneiform writing — The inscription from Behistun (Bīsotūn, ancient
- `images/beekes-2011-comparative-ie-linguistics-p362-illustration.png` — Illustrations p. 362, page 362: Illustration 4. Old Persian cuneiform writing. — A stela of king Darius from Egypt in which he
- `images/beekes-2011-comparative-ie-linguistics-p363-illustration.png` — Illustrations p. 363, page 363: Illustration 5. Tocharian. — Most manuscripts date from the sixth to eighth centuries A.D. from
- `images/beekes-2011-comparative-ie-linguistics-p364-illustration.png` — Illustrations p. 364, page 364: Illustrations, printed p. 364
- `images/beekes-2011-comparative-ie-linguistics-p365-illustration.png` — Illustrations p. 365, page 365: Illustration 7. Hittite clay tablet, with cuneiform writing, found in Boghazköy, the old capital Hat-
- `images/beekes-2011-comparative-ie-linguistics-p366-illustration.png` — Illustrations p. 366, page 366: Illustrations, printed p. 366
- `images/beekes-2011-comparative-ie-linguistics-p367-illustration.png` — Illustrations p. 367, page 367: Illustration 8. Hieroglyphic Luwian — An inscription in Luwian hieroglyphs. It is a proclamatian of
- `images/beekes-2011-comparative-ie-linguistics-p368-illustration.png` — Illustrations p. 368, page 368: Illustration 9. An inscription in Old Phrygian on a façade cut in the rock. The inscription probably
- `images/beekes-2011-comparative-ie-linguistics-p369-illustration.png` — Illustrations p. 369, page 369: Illustration 10. Old Church Slavonic in glagolitic script — Old Church Slavonic is handed down in
- `images/beekes-2011-comparative-ie-linguistics-p370-illustration.png` — Illustrations p. 370, page 370: Illustration 11. Old Russian text written on birch bark, from the beginning of the 14th century,
- `images/beekes-2011-comparative-ie-linguistics-p371-illustration.png` — Illustrations p. 371, page 371: Illustration 12. Thracian — The gold ring with inscription from Ezerovo, dating from the fifth
- `images/beekes-2011-comparative-ie-linguistics-p372-illustration.png` — Illustrations p. 372, page 372: Illustrations, printed p. 372
- `images/beekes-2011-comparative-ie-linguistics-p373-illustration.png` — Illustrations p. 373, page 373: Illustration 13. Mycenaean clay tablets, two in the shape of palm leaves. They are written in the Lin-
- `images/beekes-2011-comparative-ie-linguistics-p374-illustration.png` — Illustrations p. 374, page 374: Illustrations, printed p. 374
- `images/beekes-2011-comparative-ie-linguistics-p375-illustration.png` — Illustrations p. 375, page 375: Illustration 14. Greek. Manuscript page (above) with a passage from Homer’s Iliad (T 76ff). This
- `images/beekes-2011-comparative-ie-linguistics-p376-illustration.png` — Illustrations p. 376, page 376: Illustration 15. Messapian inscription, from Galatina, second century B.C. Messapian was an inde-
- `images/beekes-2011-comparative-ie-linguistics-p377-illustration.png` — Illustrations p. 377, page 377: Illustration 16. The oldest inscription but one in Latin, or rather a closely related dialect, from ca.
- `images/beekes-2011-comparative-ie-linguistics-p378-illustration.png` — Illustrations p. 378, page 378: Illustrations, printed p. 378
- `images/beekes-2011-comparative-ie-linguistics-p379-illustration.png` — Illustrations p. 379, page 379: Illustration 17. Umbrian. Plate Vb of the Tabulae Iguvinae, large bronze tables found in Iguvium
- `images/beekes-2011-comparative-ie-linguistics-p380-illustration.png` — Illustrations p. 380, page 380: Illustration 18. South Picene — The inscription from
- `images/beekes-2011-comparative-ie-linguistics-p381-illustration.png` — Illustrations p. 381, page 381: Illustration 19. A Gaulish inscription. — The inscription from Todi, in Umbria, Italy. It is a bilingual
- `images/beekes-2011-comparative-ie-linguistics-p382-illustration.png` — Illustrations p. 382, page 382: Illustrations, printed p. 382
- `images/beekes-2011-comparative-ie-linguistics-p383-illustration.png` — Illustrations p. 383, page 383: Illustration 20. The first Celtiberian inscription from Botorrita, near Zaragoza (Spain), found in 1970;
- `images/beekes-2011-comparative-ie-linguistics-p384-illustration.png` — Illustrations p. 384, page 384: Illustration 23. Old Irish manuscript, from the Book of Leinster, from ca. 1160. The text is from the
- `images/beekes-2011-comparative-ie-linguistics-p385-illustration.png` — Illustrations p. 385, page 385: Illustration 24. The Germanic runes, with their reconstructed names. This script is called the
- `images/beekes-2011-comparative-ie-linguistics-p386-illustration.png` — Illustrations p. 386, page 386: Illustration 25. The Gothic alphabet. It is largely based on the Greek alphabet, but h, r and s are
