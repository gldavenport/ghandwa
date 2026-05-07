# Extraction Report: *The Reflexes of the Proto-Indo-European Laryngeals in Celtic*

## Source type

Born-digital PDF with a machine-readable text layer. The body text was extracted primarily from the PDF text layer with `pdftotext -layout`. The cover is the only detected raster image and is represented in the main extraction by an accessible description.

## Corrections applied

- Repaired PDF text-layer ligature artifacts: `fif` → `fi` approximately 656 times and `flf` → `fl` approximately 549 times.
- Repaired laryngeal index mapping where the visual/source form uses subscript indices: `h1/h2/h3/h4` and `H1/H2/H3/H4` → `h₁/h₂/h₃/h₄` and `H₁/H₂/H₃/H₄` approximately 2765 times; slash-following laryngeal digits were subscripted approximately 89 times.
- Rejoined line-break hyphenation approximately 1064 times. Ordinary hyphenated compounds were retained where the continuation began with an uppercase letter.
- Removed repeated running headers, printed page numbers, and form-feed artifacts.
- Converted the abbreviations section to a Markdown table where the PDF text layer exposed a two-column list.
- Decolumnized the Index Verborum so entries are one headword per output line where the text layer exposed multiple columns on a single line.
- Repaired two corrupted occurrences of Greek `ἵεμαι` by contextual/visual inference and marked them with `[?]` inline.

## Unresolved issues list

The following locations contain explicit uncertainty markers or inferred-character markers in the main extraction:

- output line 1615: `*h₂u̯ eh₁-tV- (Joseph 1980: 50–51), with shortening. However, it is possible that there was a root *h₂u̯ et- of similar meaning (Gk. Hesych. ἀετμόν· τὸ πνεῦμα, Gk. ᾱ[unclear glyph]τμος ‘smoke, vapour’; IEW 82). 4. OIr. `
- output line 1625: `LIV 107; see OIr. dían p. 229). However, the alternative connection with Lat. bonus ‘good’ < *du̯ eno- is formally unproblematic and semantically better. Consequently, den is not firm evidence for *CIHC-. 6. OIr. dron (o`
- output line 1667: `1. Lat. dūrus ‘hard, harsh’ < *duh₂-ró- *‘enduring, long-lasting’ (dūrāre ‘extend’ shows the older meaning; Fortson 2007: 87); cf. Skt. dūráḥ ‘far, long’, Gk. Hom. δηρός, Dor. δᾱρός ‘long (of time)’. 2. Lat. fĕrus ‘wild`
- output line 2311: `§ 150. *-eI̯HV-1. Gaul. Boii (tribal name) is most likely to come from *bhoi̯h₂-o-, from *bhei̯h₂-‘strike’ (LIV 72); *gwoi̯h₃-o-, from *gwi̯eh₃- ‘live’ (LIV 215–216) is also possible (Bammesberger 1997). For other less l`
- output line 7026: `## ᾱ[unclear glyph]τμος`
- output line 7161: `ῑς[unclear glyph] — 217`

Additional limitations:

- The extraction is a text-layer pass with automated structural cleanup. It cannot certify that every Greek, IPA, reconstructed form, or diacritic survived the PDF text mapping correctly.
- The text layer contains a small number of non-Unicode Brill glyph mappings. Four remaining such glyphs were not silently guessed and are marked `[unclear glyph]` in the output.
- Page-boundary continuation checks were automated, but a human source-critical pass would still be warranted before treating this as a character-authoritative edition.

## Confusion-pair report

This report records automated checks and likely-risk areas. It does not certify that every instance is correct.

| Confusion pair | Automated status |
|---|---|
| `h₁ h₂ h₃` vs `h1 h2 h3` | ASCII laryngeal indices from the text layer were converted to subscript forms. Residual ASCII `h1/h2/h3` should be manually checked if discovered in a later pass. |
| Macron vowels dropped in dense sections | Macron counts are recorded below for regression checks. Index pages were decolumnized to reduce dense-section drop risk. |
| `ʰ ʷ` vs `h w` | Not exhaustively verified. Superscript modifier letters remain only where the text layer exposed them. |
| `ə` vs `e` or `9` | Approximate schwa counts recorded below; no exhaustive visual verification. |
| `ṛ ḷ ṃ ṇ` vs plain letters | Not exhaustively verified. Underdot codepoints were retained where present in the text layer. |
| `ǵ ḱ` vs apostrophe forms | Acute consonants were retained where present in the text layer; no exhaustive visual verification. |
| `*` before reconstructed forms | Asterisks were preserved from the text layer; no claim of exhaustive verification. |
| `†` dagger vs plus/absence | Approximate dagger count recorded below; no exhaustive visual verification. |
| Greek breathing/combined diacritic glyphs | Six nonstandard glyph mappings were found. Two were contextually repaired as `ἵεμαι[?]`; four remain `[unclear glyph]`. |

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "laryngeals": {
    "h1": 860,
    "h2": 1419,
    "h3": 484
  },
  "macron_a": 1170,
  "macron_e": 325,
  "macron_i": 538,
  "macron_o": 332,
  "macron_u": 334,
  "schwa": 84,
  "greek_chars": 6845,
  "combining_diacritics": 5420,
  "dagger": 0
}
```

Selected non-ASCII and combining codepoints in output:

- U+00A7 SECTION SIGN: approx. 795
- U+00B7 MIDDLE DOT: approx. 165
- U+00C1 LATIN CAPITAL LETTER A WITH ACUTE: approx. 2
- U+00C9 LATIN CAPITAL LETTER E WITH ACUTE: approx. 51
- U+00D3 LATIN CAPITAL LETTER O WITH ACUTE: approx. 19
- U+00D6 LATIN CAPITAL LETTER O WITH DIAERESIS: approx. 4
- U+00DC LATIN CAPITAL LETTER U WITH DIAERESIS: approx. 3
- U+00DF LATIN SMALL LETTER SHARP S: approx. 4
- U+00E0 LATIN SMALL LETTER A WITH GRAVE: approx. 23
- U+00E1 LATIN SMALL LETTER A WITH ACUTE: approx. 750
- U+00E2 LATIN SMALL LETTER A WITH CIRCUMFLEX: approx. 17
- U+00E3 LATIN SMALL LETTER A WITH TILDE: approx. 13
- U+00E4 LATIN SMALL LETTER A WITH DIAERESIS: approx. 124
- U+00E5 LATIN SMALL LETTER A WITH RING ABOVE: approx. 6
- U+00E6 LATIN SMALL LETTER AE: approx. 16
- U+00E7 LATIN SMALL LETTER C WITH CEDILLA: approx. 3
- U+00E8 LATIN SMALL LETTER E WITH GRAVE: approx. 12
- U+00E9 LATIN SMALL LETTER E WITH ACUTE: approx. 382
- U+00EA LATIN SMALL LETTER E WITH CIRCUMFLEX: approx. 14
- U+00EB LATIN SMALL LETTER E WITH DIAERESIS: approx. 13
- U+00EC LATIN SMALL LETTER I WITH GRAVE: approx. 47
- U+00ED LATIN SMALL LETTER I WITH ACUTE: approx. 389
- U+00EE LATIN SMALL LETTER I WITH CIRCUMFLEX: approx. 10
- U+00EF LATIN SMALL LETTER I WITH DIAERESIS: approx. 6
- U+00F0 LATIN SMALL LETTER ETH: approx. 1
- U+00F1 LATIN SMALL LETTER N WITH TILDE: approx. 67
- U+00F2 LATIN SMALL LETTER O WITH GRAVE: approx. 3
- U+00F3 LATIN SMALL LETTER O WITH ACUTE: approx. 286
- U+00F4 LATIN SMALL LETTER O WITH CIRCUMFLEX: approx. 3
- U+00F5 LATIN SMALL LETTER O WITH TILDE: approx. 8
- U+00F6 LATIN SMALL LETTER O WITH DIAERESIS: approx. 35
- U+00F8 LATIN SMALL LETTER O WITH STROKE: approx. 16
- U+00F9 LATIN SMALL LETTER U WITH GRAVE: approx. 49
- U+00FA LATIN SMALL LETTER U WITH ACUTE: approx. 279
- U+00FB LATIN SMALL LETTER U WITH CIRCUMFLEX: approx. 6
- U+00FC LATIN SMALL LETTER U WITH DIAERESIS: approx. 147
- U+00FD LATIN SMALL LETTER Y WITH ACUTE: approx. 25
- U+00FE LATIN SMALL LETTER THORN: approx. 38
- U+0101 LATIN SMALL LETTER A WITH MACRON: approx. 1170
- U+0103 LATIN SMALL LETTER A WITH BREVE: approx. 235
- U+0105 LATIN SMALL LETTER A WITH OGONEK: approx. 2
- U+0107 LATIN SMALL LETTER C WITH ACUTE: approx. 91
- U+010C LATIN CAPITAL LETTER C WITH CARON: approx. 1
- U+010D LATIN SMALL LETTER C WITH CARON: approx. 16
- U+0110 LATIN CAPITAL LETTER D WITH STROKE: approx. 2
- U+0111 LATIN SMALL LETTER D WITH STROKE: approx. 59
- U+0112 LATIN CAPITAL LETTER E WITH MACRON: approx. 39
- U+0113 LATIN SMALL LETTER E WITH MACRON: approx. 286
- U+0114 LATIN CAPITAL LETTER E WITH BREVE: approx. 14
- U+0115 LATIN SMALL LETTER E WITH BREVE: approx. 44
- U+0117 LATIN SMALL LETTER E WITH DOT ABOVE: approx. 35
- U+0119 LATIN SMALL LETTER E WITH OGONEK: approx. 7
- U+011B LATIN SMALL LETTER E WITH CARON: approx. 15
- U+011D LATIN SMALL LETTER G WITH CIRCUMFLEX: approx. 206
- U+0129 LATIN SMALL LETTER I WITH TILDE: approx. 11
- U+012A LATIN CAPITAL LETTER I WITH MACRON: approx. 58
- U+012B LATIN SMALL LETTER I WITH MACRON: approx. 480
- U+012C LATIN CAPITAL LETTER I WITH BREVE: approx. 49
- U+012D LATIN SMALL LETTER I WITH BREVE: approx. 110
- U+013C LATIN SMALL LETTER L WITH CEDILLA: approx. 5
- U+0142 LATIN SMALL LETTER L WITH STROKE: approx. 12
- U+0144 LATIN SMALL LETTER N WITH ACUTE: approx. 3
- U+014D LATIN SMALL LETTER O WITH MACRON: approx. 332
- U+014F LATIN SMALL LETTER O WITH BREVE: approx. 26
- U+0155 LATIN SMALL LETTER R WITH ACUTE: approx. 9
- U+015B LATIN SMALL LETTER S WITH ACUTE: approx. 67
- U+0160 LATIN CAPITAL LETTER S WITH CARON: approx. 1
- U+0161 LATIN SMALL LETTER S WITH CARON: approx. 103
- U+0169 LATIN SMALL LETTER U WITH TILDE: approx. 11
- U+016B LATIN SMALL LETTER U WITH MACRON: approx. 334
- U+016D LATIN SMALL LETTER U WITH BREVE: approx. 114
- U+0177 LATIN SMALL LETTER Y WITH CIRCUMFLEX: approx. 1
- U+017E LATIN SMALL LETTER Z WITH CARON: approx. 40
- U+0195 LATIN SMALL LETTER HV: approx. 2
- U+01DD LATIN SMALL LETTER TURNED E: approx. 36
- U+01E3 LATIN SMALL LETTER AE WITH MACRON: approx. 14
- U+01EB LATIN SMALL LETTER O WITH OGONEK: approx. 35
- U+01F0 LATIN SMALL LETTER J WITH CARON: approx. 5
- U+0201 LATIN SMALL LETTER A WITH DOUBLE GRAVE: approx. 9
- U+0209 LATIN SMALL LETTER I WITH DOUBLE GRAVE: approx. 15
- U+0211 LATIN SMALL LETTER R WITH DOUBLE GRAVE: approx. 2
- U+0215 LATIN SMALL LETTER U WITH DOUBLE GRAVE: approx. 4
- U+0229 LATIN SMALL LETTER E WITH CEDILLA: approx. 2
- U+022B LATIN SMALL LETTER O WITH DIAERESIS AND MACRON: approx. 1
- U+0233 LATIN SMALL LETTER Y WITH MACRON: approx. 4
- U+0254 LATIN SMALL LETTER OPEN O: approx. 2
- U+0259 LATIN SMALL LETTER SCHWA: approx. 48
- U+026A LATIN LETTER SMALL CAPITAL I: approx. 1
- U+0281 LATIN LETTER SMALL CAPITAL INVERTED R: approx. 1
- U+0289 LATIN SMALL LETTER U BAR: approx. 2
- U+0292 LATIN SMALL LETTER EZH: approx. 2
- U+02A2 LATIN LETTER REVERSED GLOTTAL STOP WITH STROKE: approx. 4
- U+0301 COMBINING ACUTE ACCENT: approx. 297
- U+0302 COMBINING CIRCUMFLEX ACCENT: approx. 210
- U+0303 COMBINING TILDE: approx. 33
- U+0304 COMBINING MACRON: approx. 170
- U+0305 COMBINING OVERLINE: approx. 3
- U+0306 COMBINING BREVE: approx. 127
- U+0307 COMBINING DOT ABOVE: approx. 33
- U+030A COMBINING RING ABOVE: approx. 2
- U+0311 COMBINING INVERTED BREVE: approx. 1
- U+0313 COMBINING COMMA ABOVE: approx. 3
- U+0325 COMBINING RING BELOW: approx. 1504
- U+0326 COMBINING COMMA BELOW: approx. 2
- U+0328 COMBINING OGONEK: approx. 3
- U+032C COMBINING CARON BELOW: approx. 137
- U+032F COMBINING INVERTED BREVE BELOW: approx. 2894
- U+0331 COMBINING MACRON BELOW: approx. 1
- U+0391 GREEK CAPITAL LETTER ALPHA: approx. 2
- U+0392 GREEK CAPITAL LETTER BETA: approx. 2
- U+0393 GREEK CAPITAL LETTER GAMMA: approx. 5
- U+0395 GREEK CAPITAL LETTER EPSILON: approx. 5
- U+0397 GREEK CAPITAL LETTER ETA: approx. 1
- U+0399 GREEK CAPITAL LETTER IOTA: approx. 8
- U+039A GREEK CAPITAL LETTER KAPPA: approx. 4
- U+039B GREEK CAPITAL LETTER LAMDA: approx. 8
- U+039C GREEK CAPITAL LETTER MU: approx. 2
- U+039D GREEK CAPITAL LETTER NU: approx. 2
- U+039F GREEK CAPITAL LETTER OMICRON: approx. 6
- U+03A0 GREEK CAPITAL LETTER PI: approx. 5
- U+03A1 GREEK CAPITAL LETTER RHO: approx. 1
- U+03A3 GREEK CAPITAL LETTER SIGMA: approx. 3
- U+03A4 GREEK CAPITAL LETTER TAU: approx. 5
- U+03A5 GREEK CAPITAL LETTER UPSILON: approx. 1
- U+03A9 GREEK CAPITAL LETTER OMEGA: approx. 1
- U+03B1 GREEK SMALL LETTER ALPHA: approx. 545
- U+03B2 GREEK SMALL LETTER BETA: approx. 74
- U+03B3 GREEK SMALL LETTER GAMMA: approx. 142
- U+03B4 GREEK SMALL LETTER DELTA: approx. 92
- U+03B5 GREEK SMALL LETTER EPSILON: approx. 218
- U+03B6 GREEK SMALL LETTER ZETA: approx. 33
- U+03B7 GREEK SMALL LETTER ETA: approx. 141
- U+03B8 GREEK SMALL LETTER THETA: approx. 103
- U+03B9 GREEK SMALL LETTER IOTA: approx. 295
- U+03BA GREEK SMALL LETTER KAPPA: approx. 198
- U+03BB GREEK SMALL LETTER LAMDA: approx. 373
- U+03BC GREEK SMALL LETTER MU: approx. 322
- U+03BD GREEK SMALL LETTER NU: approx. 431
- U+03BE GREEK SMALL LETTER XI: approx. 28
- U+03BF GREEK SMALL LETTER OMICRON: approx. 373
- U+03C0 GREEK SMALL LETTER PI: approx. 147
- U+03C1 GREEK SMALL LETTER RHO: approx. 412
- U+03C2 GREEK SMALL LETTER FINAL SIGMA: approx. 455
- U+03C3 GREEK SMALL LETTER SIGMA: approx. 196
- U+03C4 GREEK SMALL LETTER TAU: approx. 289
- U+03C5 GREEK SMALL LETTER UPSILON: approx. 161
- U+03C6 GREEK SMALL LETTER PHI: approx. 97
- U+03C7 GREEK SMALL LETTER CHI: approx. 67
- U+03C9 GREEK SMALL LETTER OMEGA: approx. 215
- U+03DD GREEK SMALL LETTER DIGAMMA: approx. 14
- U+044A CYRILLIC SMALL LETTER HARD SIGN: approx. 53
- U+044C CYRILLIC SMALL LETTER SOFT SIGN: approx. 30
- U+1E17 LATIN SMALL LETTER E WITH MACRON AND ACUTE: approx. 2
- U+1E1E LATIN CAPITAL LETTER F WITH DOT ABOVE: approx. 1
- U+1E1F LATIN SMALL LETTER F WITH DOT ABOVE: approx. 1
- U+1E25 LATIN SMALL LETTER H WITH DOT BELOW: approx. 320
- U+1E2A LATIN CAPITAL LETTER H WITH BREVE BELOW: approx. 1
- U+1E2B LATIN SMALL LETTER H WITH BREVE BELOW: approx. 3
- U+1E43 LATIN SMALL LETTER M WITH DOT BELOW: approx. 2
- U+1E47 LATIN SMALL LETTER N WITH DOT BELOW: approx. 57
- U+1E59 LATIN SMALL LETTER R WITH DOT ABOVE: approx. 9
- U+1E5B LATIN SMALL LETTER R WITH DOT BELOW: approx. 2
- U+1E61 LATIN SMALL LETTER S WITH DOT ABOVE: approx. 2
- U+1E63 LATIN SMALL LETTER S WITH DOT BELOW: approx. 58
- U+1E6D LATIN SMALL LETTER T WITH DOT BELOW: approx. 94
- U+1EAF LATIN SMALL LETTER A WITH BREVE AND ACUTE: approx. 1
- U+1EBD LATIN SMALL LETTER E WITH TILDE: approx. 16
- U+1EF9 LATIN SMALL LETTER Y WITH TILDE: approx. 2
- U+1F00 GREEK SMALL LETTER ALPHA WITH PSILI: approx. 89
- U+1F04 GREEK SMALL LETTER ALPHA WITH PSILI AND OXIA: approx. 55
- U+1F05 GREEK SMALL LETTER ALPHA WITH DASIA AND OXIA: approx. 5
- U+1F0C GREEK CAPITAL LETTER ALPHA WITH PSILI AND OXIA: approx. 3
- U+1F10 GREEK SMALL LETTER EPSILON WITH PSILI: approx. 50
- U+1F11 GREEK SMALL LETTER EPSILON WITH DASIA: approx. 8
- U+1F14 GREEK SMALL LETTER EPSILON WITH PSILI AND OXIA: approx. 44
- U+1F15 GREEK SMALL LETTER EPSILON WITH DASIA AND OXIA: approx. 3
- U+1F18 GREEK CAPITAL LETTER EPSILON WITH PSILI: approx. 2
- U+1F20 GREEK SMALL LETTER ETA WITH PSILI: approx. 4
- U+1F21 GREEK SMALL LETTER ETA WITH DASIA: approx. 1
- U+1F24 GREEK SMALL LETTER ETA WITH PSILI AND OXIA: approx. 4
- U+1F25 GREEK SMALL LETTER ETA WITH DASIA AND OXIA: approx. 1
- U+1F30 GREEK SMALL LETTER IOTA WITH PSILI: approx. 8
- U+1F31 GREEK SMALL LETTER IOTA WITH DASIA: approx. 5
- U+1F34 GREEK SMALL LETTER IOTA WITH PSILI AND OXIA: approx. 10
- U+1F35 GREEK SMALL LETTER IOTA WITH DASIA AND OXIA: approx. 9
- U+1F36 GREEK SMALL LETTER IOTA WITH PSILI AND PERISPOMENI: approx. 2
- U+1F37 GREEK SMALL LETTER IOTA WITH DASIA AND PERISPOMENI: approx. 2
- U+1F38 GREEK CAPITAL LETTER IOTA WITH PSILI: approx. 2
- U+1F40 GREEK SMALL LETTER OMICRON WITH PSILI: approx. 45
- U+1F41 GREEK SMALL LETTER OMICRON WITH DASIA: approx. 4
- U+1F44 GREEK SMALL LETTER OMICRON WITH PSILI AND OXIA: approx. 38
- U+1F45 GREEK SMALL LETTER OMICRON WITH DASIA AND OXIA: approx. 4
- U+1F50 GREEK SMALL LETTER UPSILON WITH PSILI: approx. 9
- U+1F51 GREEK SMALL LETTER UPSILON WITH DASIA: approx. 9
- U+1F54 GREEK SMALL LETTER UPSILON WITH PSILI AND OXIA: approx. 2
- U+1F55 GREEK SMALL LETTER UPSILON WITH DASIA AND OXIA: approx. 4
- U+1F56 GREEK SMALL LETTER UPSILON WITH PSILI AND PERISPOMENI: approx. 8
- U+1F57 GREEK SMALL LETTER UPSILON WITH DASIA AND PERISPOMENI: approx. 5
- U+1F60 GREEK SMALL LETTER OMEGA WITH PSILI: approx. 17
- U+1F64 GREEK SMALL LETTER OMEGA WITH PSILI AND OXIA: approx. 2
- U+1F65 GREEK SMALL LETTER OMEGA WITH DASIA AND OXIA: approx. 2
- U+1F70 GREEK SMALL LETTER ALPHA WITH VARIA: approx. 1
- U+1F71 GREEK SMALL LETTER ALPHA WITH OXIA: approx. 131
- U+1F73 GREEK SMALL LETTER EPSILON WITH OXIA: approx. 146
- U+1F75 GREEK SMALL LETTER ETA WITH OXIA: approx. 98
- U+1F77 GREEK SMALL LETTER IOTA WITH OXIA: approx. 95
- U+1F78 GREEK SMALL LETTER OMICRON WITH VARIA: approx. 1
- U+1F79 GREEK SMALL LETTER OMICRON WITH OXIA: approx. 228
- U+1F7B GREEK SMALL LETTER UPSILON WITH OXIA: approx. 59
- U+1F7D GREEK SMALL LETTER OMEGA WITH OXIA: approx. 26
- U+1FA0 GREEK SMALL LETTER OMEGA WITH PSILI AND YPOGEGRAMMENI: approx. 3
- U+1FB6 GREEK SMALL LETTER ALPHA WITH PERISPOMENI: approx. 11
- U+1FC6 GREEK SMALL LETTER ETA WITH PERISPOMENI: approx. 26
- U+1FC7 GREEK SMALL LETTER ETA WITH PERISPOMENI AND YPOGEGRAMMENI: approx. 4
- U+1FD3 GREEK SMALL LETTER IOTA WITH DIALYTIKA AND OXIA: approx. 5
- U+1FD6 GREEK SMALL LETTER IOTA WITH PERISPOMENI: approx. 35
- U+1FE5 GREEK SMALL LETTER RHO WITH DASIA: approx. 10
- U+1FE6 GREEK SMALL LETTER UPSILON WITH PERISPOMENI: approx. 18
- U+1FF6 GREEK SMALL LETTER OMEGA WITH PERISPOMENI: approx. 10
- U+2013 EN DASH: approx. 1493
- U+2014 EM DASH: approx. 5331
- U+2018 LEFT SINGLE QUOTATION MARK: approx. 4168
- U+2019 RIGHT SINGLE QUOTATION MARK: approx. 4621
- U+201C LEFT DOUBLE QUOTATION MARK: approx. 42
- U+201D RIGHT DOUBLE QUOTATION MARK: approx. 42
- U+2022 BULLET: approx. 1
- U+2026 HORIZONTAL ELLIPSIS: approx. 3
- U+2081 SUBSCRIPT ONE: approx. 860
- U+2082 SUBSCRIPT TWO: approx. 1432
- U+2083 SUBSCRIPT THREE: approx. 560
- U+2084 SUBSCRIPT FOUR: approx. 2
- U+2190 LEFTWARDS ARROW: approx. 16
- U+2192 RIGHTWARDS ARROW: approx. 30

## Structural integrity check

- Headings: converted major title, chapter, section, numbered-section, reference, and index headings where detected automatically.
- Footnotes: preserved in page-local reading order as exposed by the text layer; footnote markers were not normalized.
- Tables: abbreviation lists were converted to a Markdown table. No other raster/image tables were detected.
- Index: decolumnized so each detected headword entry is on its own output line.
- Page anchors: `<!-- pdf-page: n -->` comments were inserted before extracted page content to support source-location checking.
- Continuation text: line-break hyphenation was repaired automatically, but no claim is made that every page-boundary continuation is perfect.

## Approximate correction metrics

```json
{
  "fif_to_fi": 656,
  "flf_to_fl": 549,
  "h_digit_to_subscript": 2765,
  "slash_digit_to_subscript_after_laryngeal": 89,
  "private_use_glyph_unclear": 4,
  "greek_iemai_inferred": 2,
  "hyphenation_rejoins": 1064
}
```
