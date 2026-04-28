# Special-character and reconstructed-form audit

This sidecar is a third-pass audit aid. It does not replace philological review, but it surfaces high-risk Unicode and reconstructed-form material for targeted checking.

## Character inventory of non-ASCII/significant symbols

| Character | Code point | Unicode name | Count |
| --- | --- | --- | ---: |
| `±` | U+00B1 | PLUS-MINUS SIGN | 6 |
| `É` | U+00C9 | LATIN CAPITAL LETTER E WITH ACUTE | 1 |
| `Ö` | U+00D6 | LATIN CAPITAL LETTER O WITH DIAERESIS | 1 |
| `Ü` | U+00DC | LATIN CAPITAL LETTER U WITH DIAERESIS | 2 |
| `Þ` | U+00DE | LATIN CAPITAL LETTER THORN | 4 |
| `ß` | U+00DF | LATIN SMALL LETTER SHARP S | 3 |
| `à` | U+00E0 | LATIN SMALL LETTER A WITH GRAVE | 1 |
| `á` | U+00E1 | LATIN SMALL LETTER A WITH ACUTE | 11 |
| `ã` | U+00E3 | LATIN SMALL LETTER A WITH TILDE | 1 |
| `ä` | U+00E4 | LATIN SMALL LETTER A WITH DIAERESIS | 31 |
| `æ` | U+00E6 | LATIN SMALL LETTER AE | 29 |
| `ç` | U+00E7 | LATIN SMALL LETTER C WITH CEDILLA | 13 |
| `é` | U+00E9 | LATIN SMALL LETTER E WITH ACUTE | 16 |
| `ê` | U+00EA | LATIN SMALL LETTER E WITH CIRCUMFLEX | 2 |
| `ë` | U+00EB | LATIN SMALL LETTER E WITH DIAERESIS | 1 |
| `í` | U+00ED | LATIN SMALL LETTER I WITH ACUTE | 3 |
| `ð` | U+00F0 | LATIN SMALL LETTER ETH | 24 |
| `ó` | U+00F3 | LATIN SMALL LETTER O WITH ACUTE | 12 |
| `ô` | U+00F4 | LATIN SMALL LETTER O WITH CIRCUMFLEX | 8 |
| `ö` | U+00F6 | LATIN SMALL LETTER O WITH DIAERESIS | 29 |
| `ø` | U+00F8 | LATIN SMALL LETTER O WITH STROKE | 24 |
| `ú` | U+00FA | LATIN SMALL LETTER U WITH ACUTE | 6 |
| `ü` | U+00FC | LATIN SMALL LETTER U WITH DIAERESIS | 37 |
| `þ` | U+00FE | LATIN SMALL LETTER THORN | 83 |
| `ā` | U+0101 | LATIN SMALL LETTER A WITH MACRON | 51 |
| `ă` | U+0103 | LATIN SMALL LETTER A WITH BREVE | 1 |
| `ą` | U+0105 | LATIN SMALL LETTER A WITH OGONEK | 8 |
| `ē` | U+0113 | LATIN SMALL LETTER E WITH MACRON | 100 |
| `ġ` | U+0121 | LATIN SMALL LETTER G WITH DOT ABOVE | 7 |
| `ī` | U+012B | LATIN SMALL LETTER I WITH MACRON | 66 |
| `ń` | U+0144 | LATIN SMALL LETTER N WITH ACUTE | 1 |
| `ō` | U+014D | LATIN SMALL LETTER O WITH MACRON | 96 |
| `ū` | U+016B | LATIN SMALL LETTER U WITH MACRON | 31 |
| `ű` | U+0171 | LATIN SMALL LETTER U WITH DOUBLE ACUTE | 2 |
| `ǣ` | U+01E3 | LATIN SMALL LETTER AE WITH MACRON | 2 |
| `ǫ` | U+01EB | LATIN SMALL LETTER O WITH OGONEK | 11 |
| `ɔ` | U+0254 | LATIN SMALL LETTER OPEN O | 6 |
| `ɛ` | U+025B | LATIN SMALL LETTER OPEN E | 2 |
| `ʋ` | U+028B | LATIN SMALL LETTER V WITH HOOK | 4 |
| `ʒ` | U+0292 | LATIN SMALL LETTER EZH | 2 |
| `ˉ` | U+02C9 | MODIFIER LETTER MACRON | 2 |
| `ː` | U+02D0 | MODIFIER LETTER TRIANGULAR COLON | 1 |
| `̂` | U+0302 | COMBINING CIRCUMFLEX ACCENT | 1 |
| `̄` | U+0304 | COMBINING MACRON | 24 |
| `̨` | U+0328 | COMBINING OGONEK | 2 |
| `Δ` | U+0394 | GREEK CAPITAL LETTER DELTA | 3 |
| `α` | U+03B1 | GREEK SMALL LETTER ALPHA | 48 |
| `β` | U+03B2 | GREEK SMALL LETTER BETA | 22 |
| `γ` | U+03B3 | GREEK SMALL LETTER GAMMA | 7 |
| `δ` | U+03B4 | GREEK SMALL LETTER DELTA | 9 |
| `ε` | U+03B5 | GREEK SMALL LETTER EPSILON | 14 |
| `λ` | U+03BB | GREEK SMALL LETTER LAMDA | 3 |
| `μ` | U+03BC | GREEK SMALL LETTER MU | 65 |
| `ν` | U+03BD | GREEK SMALL LETTER NU | 3 |
| `ρ` | U+03C1 | GREEK SMALL LETTER RHO | 6 |
| `ς` | U+03C2 | GREEK SMALL LETTER FINAL SIGMA | 1 |
| `σ` | U+03C3 | GREEK SMALL LETTER SIGMA | 37 |
| `τ` | U+03C4 | GREEK SMALL LETTER TAU | 1 |
| `χ` | U+03C7 | GREEK SMALL LETTER CHI | 4 |
| `ϕ` | U+03D5 | GREEK PHI SYMBOL | 3 |
| `ӯ` | U+04EF | CYRILLIC SMALL LETTER U WITH MACRON | 3 |
| `Ṽ` | U+1E7C | LATIN CAPITAL LETTER V WITH TILDE | 3 |
| `–` | U+2013 | EN DASH | 511 |
| `—` | U+2014 | EM DASH | 61 |
| `’` | U+2019 | RIGHT SINGLE QUOTATION MARK | 173 |
| `“` | U+201C | LEFT DOUBLE QUOTATION MARK | 129 |
| `”` | U+201D | RIGHT DOUBLE QUOTATION MARK | 129 |
| `ℝ` | U+211D | DOUBLE-STRUCK CAPITAL R | 2 |
| `→` | U+2192 | RIGHTWARDS ARROW | 13 |
| `∅` | U+2205 | EMPTY SET | 92 |
| `∗` | U+2217 | ASTERISK OPERATOR | 886 |

## High-risk observations

- The main extraction uses `∗` (U+2217 ASTERISK OPERATOR) for reconstructed forms, matching the PDF text layer and previous passes.

- The Appendix contains three printed non-binary `3` values in otherwise binary/unknown columns; these are source anomalies, not automatic extraction substitutions.

- Rare marks such as `ʒ`, `ʋ`, combining macron/tilde marks, and ogonek-bearing forms are indexed in `reconstructed-forms-index.tsv` for manual review.

- Names with diacritics in the references were normalized in the reference sidecars where the text layer made that safe, e.g. `für`, `Tübingen`, `Jörg`, `Höhna`, `Björn`, `vorrömische`.


## Token index

See `reconstructed-forms-index.tsv` for a frequency-sorted list of reconstructed-form and special-character tokens.
