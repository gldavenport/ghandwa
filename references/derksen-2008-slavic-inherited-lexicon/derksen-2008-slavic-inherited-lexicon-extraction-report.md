# Derksen 2008 Slavic inherited lexicon — extraction report

## Source identification
Born-digital PDF with a machine-readable text layer. The PDF uses custom embedded fonts and incomplete/nonstandard ToUnicode mappings for many philological characters. The raw text layer was therefore used as the primary input, with font-aware repair of repeated high-confidence glyphs and explicit inline markers for unresolved custom glyphs.

## Corrections applied
- Removed InDesign artifact lines and most running headers/folios by coordinate position.
- Repaired common ligature codes in roman text: fi, fl, ff, ffi, ft.
- Repaired common Slavic/IE characters in repeated contexts, including č, ć, Č, ń, ż, Đ, ł, ъ, ь, ǫ, ʔ, ʰ, ʷ, and frequent macron vowels.
- Normalized PDF text-layer laryngeal placeholders `h&` and `h'` to h₁ and h₂; capital H analogues also normalized. h₃ appears only where the custom subscript glyph could be mapped with confidence.
- Preserved page anchors as HTML comments for later source checking.

## Unresolved issues
- Inline unresolved glyph markers inserted: approximately 6267. These are concentrated in Greek forms, dense Slovincian/Serbo-Croatian accent notation, and index pages.
- Greek is not character-authoritative in this pass; many Greek glyphs remain marked as unresolved because the embedded font maps Greek to non-Unicode glyph codes.
- Some Proto-Slavic long/intoned vowel combinations in bold headwords are only partly repaired. A second pass should prioritize the bold headword glyph table.
- The bibliography and index are structurally extracted but not character-authoritative; dense index pages retain more unresolved glyph markers.

## Confusion-pair report
- h₁/h₂/h₃: h₁ and h₂ were normalized from recurrent text-layer placeholders; h₃ was only normalized when represented by the mapped custom subscript code. Other laryngeal-index contexts may remain unresolved.
- Macron vowels: common macrons were repaired in many contexts, but not all custom macron-bearing glyphs were decoded.
- ʰ/ʷ: mapped in repeated italic PIE contexts; unverified elsewhere.
- ə and underdot characters: partially mapped; unverified in dense dialect material.
- ǵ/ḱ: ǵ mapped in repeated italic contexts; other acute consonants not fully verified.
- Asterisks and daggers: asterisks are preserved from the text layer; dagger is preserved where ToUnicode supplied it.

## Codepoint inventory
Approximate counts for cross-pass comparison only:
- h1: 68
- h2: 119
- h3: 112
- macron_a: 586
- macron_e: 927
- macron_i: 668
- macron_o: 259
- macron_u: 533
- schwa: 499
- greek_chars: 0
- combining_diacritics: 600
- dagger: 1

## Structural integrity check
- Source chunked as an etymological dictionary: frontmatter/introduction, one file per detected letter section, bibliography, and index.
- Footnotes remain near the page/section where extracted; continuation text may require manual audit around page boundaries.
- Tables and form lists are line-preserved rather than converted to Markdown tables where conversion risked character loss.
- No figures, maps, stemmata, or plates requiring image extraction were identified in this pass; decorative cover art was not extracted.

## Applied glyph repairs by font
- EOMinion-Italic U+0003 → 'č': 2344
- EOMinion-Italic U+0004 → 'ł': 1033
- EOMinion U+0007 → 'Č': 897
- EOMinion-Bold U+0002 → 'ъ': 885
- EOMinion-Italic U+0018 → 'ȃ': 797
- EOMinion-Italic U+0019 → 'ê': 770
- EOMinion-Bold U+0003 → 'ь': 694
- EOMinion-Italic U+0012 → 'ī': 643
- EOMinion-Italic U+001D → 'ʰ': 602
- EOMinion-Italic U+0010 → 'ā': 568
- EOMinion-Italic U+008B → 'ʔ': 502
- EOMinion-Italic U+008A → 'ə': 499
- EOMinion-Italic U+0006 → 'ē': 498
- EOMinion-Italic U+0095 → 'ŕ': 465
- EOMinion-Italic U+0017 → 'ȗ': 459
- EOMinion-Italic U+0097 → 'é': 458
- EOMinion-Italic U+001A → 'ȁ': 451
- EOMinion-Italic U+0091 → 'a': 420
- EOMinion-Italic U+000F → 'ū': 360
- EOMinion U+0003 → 'č': 349
- EOMinion-Italic U+000D → 'ẽ': 305
- EOMinion-Italic U+000E → 'ą': 305
- EOMinion U+0098 → 'ē': 264
- EOMinion-Italic U+0007 → 'ō': 259
- EOMinion-Italic U+001B → 'ȋ': 216
- EOMinion-Italic U+001F → '̯': 199
- EOMinion-Italic U+0014 → 'ʷ': 197
- EOMinion U+0082 → 'ę': 190
- EOMinion-Italic U+0005 → 'ń': 168
- EOMinion-Italic U+008F → 'ǝ': 157
- EOMinion-Italic U+009A → 'ṣ': 148
- EOMinion-Bold U+0004 → 'ę': 139
- EOMinion-Italic U+001C → 'ǵ': 129
- EOMinion-Italic U+0015 → '₃': 120
- EOMinion-Italic U+0011 → 'á': 116
- EOMinion-Italic U+0013 → 'ē': 110
- EOMinion-Italic U+0008 → 'ė': 101
- EOMinion-Italic U+000B → 'ū': 101
- EOMinion-Italic U+0088 → 'ȧ̃': 84
- EOMinion-Italic U+0089 → 'o': 84
- EOMinion-Italic U+0092 → 'ci': 84
- EOMinion U+0005 → 'fi': 71
- EOMinion-Bold U+0016 → 'ǫ': 70
- EOMinion U+0008 → 'ū': 69
- EOMinion-Italic U+0016 → 'ĺ': 69
- EOMinion-Italic U+008D → 'ỹ': 68
- EOMinion-Bold U+000E → 'ē': 55
- EOMinion U+0004 → 'fl': 51
- EOMinion-Bold U+0012 → 'ľ': 41
- EOMinion U+0002 → 'ft': 33
- EOMinion U+009C → 'ja': 30
- EOMinion-Italic U+0099 → 'š': 26
- EOMinion U+001F → 'ī': 25
- EOMinion-Bold U+0010 → 'ě': 24
- EOMinion U+0006 → 'ff': 23
- EOMinion U+0019 → 'ń': 21
- EOMinion U+0084 → 'ě̄': 20
- EOMinion-Bold U+0008 → 'ě̄': 18
- EOMinion-Bold U+000B → 'ā': 18
- EOMinion U+0011 → 'ć': 17
- EOMinion-Bold U+0005 → 'ȃ': 15
- EOMinion-Italic U+000C → 'ų': 13
- EOMinion-Italic U+0002 → 'È': 12
- EOMinion-Bold U+0007 → '̄': 12
- EOMinion U+0083 → '̄': 11
- EOMinion-Bold U+001C → 'ě': 11
- EOMinion U+0010 → 'ffi': 10
- EOMinion U+001C → 'ʔ': 7
- EOMinion U+001B → 'Đ': 4
- TimesNewRoman U+0003 → 'č': 4
- EOMinion U+001A → 'ż': 2
- TimesNewRoman U+0002 → 'Bū': 1
- TimesNewUnicodePSMT U+0002 → 'Bū': 1
- TimesNewRoman,Italic U+0002 → 'Bū': 1

## Unmapped glyph inventory by font
- EOMinion-Italic U+009B: 922
- EOMinion-Italic U+009F: 725
- EOMinion U+0015: 347
- EOMinion U+000F: 328
- EOMinion U+0018: 292
- EOMinion U+000D: 291
- EOMinion U+000C: 280
- EOMinion U+0095: 226
- EOMinion U+0013: 190
- EOMinion U+0080: 179
- EOMinion U+000B: 171
- EOMinion-Italic U+008E: 169
- EOMinion-Bold U+0014: 167
- EOMinion U+0017: 164
- EOMinion U+000E: 163
- EOMinion U+0016: 144
- EOMinion-Italic U+0094: 118
- EOMinion-Italic U+0098: 116
- EOMinion U+008C: 116
- EOMinion U+0091: 115
- EOMinion U+0012: 108
- EOMinion-Italic U+0093: 96
- EOMinion U+0096: 81
- EOMinion-Bold U+0006: 76
- EOMinion U+0014: 72
- EOMinion U+0089: 71
- EOMinion U+0087: 70
- EOMinion-Bold U+0015: 44
- EOMinion-Bold U+001A: 40
- EOMinion U+008A: 33
- EOMinion-Italic U+0096: 30
- EOMinion-Bold U+000C: 26
- EOMinion-Bold U+0019: 26
- EOMinion U+009B: 25
- EOMinion U+009F: 25
- EOMinion-Bold U+0017: 25
- EOMinion U+009A: 23
- EOMinion U+0088: 19
- EOMinion-Bold U+0018: 17
- EOMinion-Bold U+000D: 15
- EOMinion-Bold U+001F: 14
- EOMinion-Bold U+0013: 13
- EOMinion-Italic U+001E: 11
- EOMinion U+0093: 11
- EOMinion-Bold U+0011: 11
- EOMinion-Bold U+001D: 10
- EOMinion U+0086: 7
- EOMinion U+0094: 7
- EOMinion U+001E: 6
- EOMinion U+001D: 5
- EOMinion-Bold U+001E: 5
- EOMinion U+0001: 5
- SymbolMT U+0002: 4
- EOMinion-Bold U+000F: 4
- EOMinion-Italic U+0001: 3
- EOMinion-Italic U+0087: 2
- EOMinion U+0092: 2
- EOMinion U+008B: 1
- EOMinion-Bold U+001B: 1

## Post-processing note

After the first extraction, the dictionary file was split at detected letter markers into 22 letter-section files: A, B, C, D, E, G, X, I, J, K, L, M, N, O, P, R, S, Š, T, U, V, Z.
