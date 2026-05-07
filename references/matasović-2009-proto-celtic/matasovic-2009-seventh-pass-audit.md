# Seventh-Pass Targeted Cleanup Audit

This pass addressed the residual issues identified after the sixth pass: the last explicit uncertainty marker, remaining `fJ` OCR artifacts, false lexical headings that were actually continuation lines, and several high-risk forms checked against rendered page images.

## Actions

- Resolved the final explicit `[unclear: ...]` marker on PDF page 336 by restoring `senyo 'milking vessel'`.
- Removed all remaining `fJ` artifacts in the main Markdown.
  - Bracketed grammar labels such as `[m and fJ]`, `[a fJ]`, and `[ia fJ]` were corrected to closing `]`.
  - Page-image-checked Breton forms were corrected, including `biruiff`, `berwiñ`, `deuff`, `deuñv`, `euaff`, `gouaff`, `gouañv`, `queffuer`, `keñver`, `nezaff`, and `nezañ`.
  - Avestan `bafJra-` was corrected to `baβra-`.
- Repaired false level-3 headings created from page-boundary continuation lines on pages 69, 96, 118, 163, 240, 421, 424, 437, and 442.
- Corrected selected page-image-verified forms in those same regions, including `*h₁erbʰ-`, `*lāto-`, `*h₁widh-`, and `*meh₁-`.
- Regenerated the entry index after removing false headings; the index now contains 1467 rows.
- Regenerated extraction statistics and current pattern counts.

## Current pattern counts

| Pattern class | Remaining count |
|---|---:|
| `~` OCR symbol in main Markdown | 0 |
| `[unclear]` / `[unclear: ...]` markers in main Markdown | 0 |
| `fJ` OCR artifact | 0 |
| `PlE` OCR artifact | 0 |
| `GOlD` OCR artifact | 0 |
| stray currency/symbol OCR characters `¢ § € £` | 0 |
| malformed class closers `[Noun)`, `[Adj)`, `[Vb)`, `[Prep)` | 0 |

## Current top non-ASCII characters

| Character | Unicode name | Count |
|---|---|---:|
| `ʰ` | MODIFIER LETTER SMALL H | 578 |
| `ʷ` | MODIFIER LETTER SMALL W | 564 |
| `₂` | SUBSCRIPT TWO | 516 |
| `₁` | SUBSCRIPT ONE | 221 |
| `₃` | SUBSCRIPT THREE | 183 |
| `ā` | LATIN SMALL LETTER A WITH MACRON | 88 |
| `ć` | LATIN SMALL LETTER C WITH ACUTE | 81 |
| `ī` | LATIN SMALL LETTER I WITH MACRON | 57 |
| `ü` | LATIN SMALL LETTER U WITH DIAERESIS | 33 |
| `ó` | LATIN SMALL LETTER O WITH ACUTE | 22 |
| `á` | LATIN SMALL LETTER A WITH ACUTE | 20 |
| `ē` | LATIN SMALL LETTER E WITH MACRON | 14 |
| `•` | BULLET | 12 |
| `ñ` | LATIN SMALL LETTER N WITH TILDE | 7 |
| `ṣ` | LATIN SMALL LETTER S WITH DOT BELOW | 6 |
| `ę` | LATIN SMALL LETTER E WITH OGONEK | 6 |
| `é` | LATIN SMALL LETTER E WITH ACUTE | 6 |
| `ō` | LATIN SMALL LETTER O WITH MACRON | 3 |
| `ū` | LATIN SMALL LETTER U WITH MACRON | 3 |
| `ś` | LATIN SMALL LETTER S WITH ACUTE | 2 |
| `š` | LATIN SMALL LETTER S WITH CARON | 2 |
| `č` | LATIN SMALL LETTER C WITH CARON | 2 |
| `́` | COMBINING ACUTE ACCENT | 1 |
| `í` | LATIN SMALL LETTER I WITH ACUTE | 1 |
| `Ó` | LATIN CAPITAL LETTER O WITH ACUTE | 1 |
| `̥` | COMBINING RING BELOW | 1 |
| `β` | GREEK SMALL LETTER BETA | 1 |
| `ь` | CYRILLIC SMALL LETTER SOFT SIGN | 1 |
| `ъ` | CYRILLIC SMALL LETTER HARD SIGN | 1 |
| `ṇ` | LATIN SMALL LETTER N WITH DOT BELOW | 1 |

## Remaining limitations

- This pass removed the known explicit uncertainty marker and the false-heading artifacts found by index audit, but it is not a full character-by-character verification of all 460 PDF pages.
- Greek, Sanskrit, Avestan, Old Irish, Breton, and reconstructed PIE/PCelt. forms should still be checked against the page image before exact scholarly citation.
- Some remaining suspicious-looking strings may be legitimate source notation, abbreviations, or variables rather than OCR errors.
