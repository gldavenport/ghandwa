# Extraction Report: Migration, Mobility and Language Contact in and around the Ancient Mediterranean

## Source type
EPUB. The source is a structured archive with XHTML text and discrete image files. The XHTML text layer was used directly; no OCR was performed.

## Corrections applied
- Ligature repairs: approximately 0.
- Laryngeal normalization: applied during recursive inline conversion, including inside inline formatting spans (`<i>`, `<em>`, `<b>`, `<sup>`, `<sub>`). The detected `h` + `<sub>2</sub>` sequence was rendered as `h₂`.
- Superscript/subscript conversion: HTML superscript/subscript text was converted to Unicode where possible; footnote references were converted to Markdown footnote references.
- Paragraph rejoins: unknown; paragraph boundaries were inherited from XHTML paragraph elements rather than OCR lineation.
- Non-icon EPUB image assets were copied directly into `images/` without recompression. EPUB font files were not included.

## Unresolved-issues list
- `5` `[?]` inferred-character marker(s) present.

## Confusion-pair report
- h₁ h₂ h₃ vs h1 h2 h3: automated scan found 0 possible ASCII-laryngeal hits.
- Precomposed macrons vs combining macron: automated scan found 7 U+0304 combining macron instances.
- Macron consistency across body, notes, and index: not exhaustively verifiable by automated scan; no certification asserted.
- ʰ ʷ vs h w: not exhaustively verifiable by automated scan; no certification asserted.
- ə vs e or 9: automated scan did not certify possible plain-letter confusions.
- ṛ ḷ ṃ ṇ vs plain r l m n: not exhaustively verifiable by automated scan; no certification asserted.
- ǵ ḱ vs g/k plus apostrophe: automated scan found 0 possible hits.
- * before reconstructed forms vs alternate glyphs: automated scan found 7 alternate asterisk/multiplication glyph hits.
- † vs plus/absent: not exhaustively verifiable by automated scan; no certification asserted.
- The QC pass cannot detect errors made consistently throughout the extraction.

## Codepoint inventory
All counts are approximate and for cross-pass comparison only.

```json
{
  "laryngeals": {
    "h1": 0,
    "h2": 1,
    "h3": 0
  },
  "macron_a": 9,
  "macron_e": 3,
  "macron_i": 8,
  "macron_o": 23,
  "macron_u": 1,
  "schwa": 1,
  "greek_chars": 9886,
  "combining_diacritics": 139,
  "dagger": 0
}
```

## Structural integrity check
- Output is chunked into front matter, abbreviations, eleven chapter files, bibliography, and combined index.
- Footnote references converted: approximately 658; footnote bodies converted: approximately 0.
- Page anchors preserved: approximately 376.
- Markdown image references detected: approximately 11.
- Markdown table rows detected: approximately 178.
- XHTML tables were converted to Markdown tables. Rowspan/colspan geometry is not fully representable in Markdown, so very complex tables should be spot-checked if physical table geometry matters.
- Index entries are preserved one entry per line where XHTML `index-entry` divisions were present; continuation entries are indented.

## Image inventory
No `[image-only...]` fallback format was required. Copied image assets:
- `images/clackson-ed-2020-migration-mobility-language-contact-fig3-1.png` — Figure 3.1; caption: Figure 3.1 Journeys in three plays of Plautus as depicted on a conventional modern map: Curculio, Persa, Poenulus
- `images/clackson-ed-2020-migration-mobility-language-contact-fig4-1.png` — Figure 4.1; caption: Figure 4.1 Plasos’signature
- `images/clackson-ed-2020-migration-mobility-language-contact-fig4-2.png` — Figure 4.2; caption: Figure 4.2 Dish with Plator’s signature
- `images/clackson-ed-2020-migration-mobility-language-contact-fig4-3.png` — Figure 4.3; caption: Figure 4.3 Plator’s signature
- `images/clackson-ed-2020-migration-mobility-language-contact-fig4-4.png` — Figure 4.4; caption: Figure 4.4 L. H. Jeffery’s drawing of Kalon’s signature and Glaukies’dedication
- `images/clackson-ed-2020-migration-mobility-language-contact-fig6-1.png` — Figure 6.1; caption: Figure 6.1 The Oscan vowel system
- `images/clackson-ed-2020-migration-mobility-language-contact-fig8-1.png` — Figure 8.1; caption: Figure 8.1 Network of associations within a group of seals
- `images/clackson-ed-2020-migration-mobility-language-contact-fig8-2.png` — Figure 8.2; caption: Figure 8.2 Graffito of the ‘Maison du Théâtre’
- `images/clackson-ed-2020-migration-mobility-language-contact-fig8-3.png` — Figure 8.3; caption: Figure 8.3 Graffito from an altar in the Agora des Italiens
- `images/clackson-ed-2020-migration-mobility-language-contact-table10-1.png` — Table 10.1; caption: [none in XHTML]
- `images/clackson-ed-2020-migration-mobility-language-contact-table10-2.png` — Table 10.2; caption: [none in XHTML]
- `images/clackson-ed-2020-migration-mobility-language-contact-table10-4.png` — Table 10.4; caption: [none in XHTML]
- `images/clackson-ed-2020-migration-mobility-language-contact-table2-1.png` — Table 2.1; caption: [none in XHTML]
- `images/clackson-ed-2020-migration-mobility-language-contact-table8-1.png` — Table 8.1; caption: Table 8.1 The Delian population in the public and funerary inscriptions
- `images/clackson-ed-2020-migration-mobility-language-contact-table8-2.png` — Table 8.2; caption: Table 8.2 Delian documents containing Latin names
- `images/clackson-ed-2020-migration-mobility-language-contact-table8-3.png` — Table 8.3; caption: [none in XHTML]
- `images/clackson-ed-2020-migration-mobility-language-contact-table9-1.png` — Table 9.1; caption: [none in XHTML]
- `images/clackson-ed-2020-migration-mobility-language-contact-table9-2.png` — Table 9.2; caption: [none in XHTML]
- `images/clackson-ed-2020-migration-mobility-language-contact-table9-3.png` — Table 9.3; caption: [none in XHTML]
- `images/clackson-ed-2020-migration-mobility-language-contact-cover.jpg` — Cover; caption: Cover
- `images/clackson-ed-2020-migration-mobility-language-contact-logo.png` — Logo; caption: Cambridge University Press logo
- `images/clackson-ed-2020-migration-mobility-language-contact-logo1.png` — Logo; caption: Cambridge University Press logo

## Image-glyph inventory
- No inline character glyph images were detected in the XHTML body. All `<img>` elements encountered were cover/logo/figure images; additional table images were present as discrete but unreferenced EPUB assets and were copied into `images/`.
