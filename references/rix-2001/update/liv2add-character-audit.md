---
title: 'Character audit for liv2add extraction'
source_file: 'liv2add.pdf'
extraction_date: '2026-04-29'
source_type: 'companion audit'
pass_status: 'first extraction plus targeted cleanup, character-audit pass, and additional character-accuracy pass'
---

# Character audit

## Character-accuracy passes applied

### Pass 1: high-risk extraction glyphs

- Replaced PyMuPDF's mis-mapped `Ү` after `k` with `k̑` (`k` + U+0311 COMBINING INVERTED BREVE), based on page-image spot checks against the source notation.
- Raw PyMuPDF `Ү` count before correction: 187.
- Removed running headers, page numbers, and copyright footers from the main extraction.

### Pass 2: private-use and replacement-character audit

- Scanned the cleaned Markdown for U+FFFD replacement characters, U+FFFE, private-use characters, and leftover `Ү`.
- Result after correction: no U+FFFD, U+FFFE, private-use characters, or leftover `Ү` remain in `liv2add.md`.
- Resolved two occurrences of source/private-use U+F023 in the Greek forms under `*pi̯eh₂-`.
  - `ἔπταξα` → `ἔπτᾱ̆ξα`
  - `πτάσσω` → `πτά̄̆σσω`
- This correction is contextual: the same entry explicitly discusses `*ptē̆-/ptā̆-`, so the private-use glyph was converted to standard Unicode combining macron + breve.

### Pass 3: stray combining-mark audit

- Scanned for combining marks attached to punctuation or whitespace rather than a letter/sign.
- Removed one spurious combining dot above after a citation period:
  - `SCHUMACHER l.c. 44f.̇;` → `SCHUMACHER l.c. 44f.;`

## Residual extraction risks

- This is now cleaner for character-level corpus use, but it is still not a diplomatic transcription.
- Lithuanian accent marks, Greek with multiple combining marks, and dense reconstructed forms should still be checked against the page image before publication-quality quotation.
- Italic/small-caps styling is not exhaustively represented; the extraction prioritizes structure and character fidelity.
- Entry headings were detected from font size and lexical-heading patterns; the companion index is useful for navigation but should not be treated as a formally curated lexical database.

## Automated post-pass checks

| Check | Result |
|---|---|
| U+FFFD replacement character | 0 |
| U+FFFE / noncharacter artifacts | 0 |
| Private-use characters | 0 |
| Leftover `Ү` | 0 |
| Stray combining marks after punctuation/space | 0 |

## Selected character counts in `liv2add.md`

| Character | Count | Unicode note |
|---|---:|---|
| `₁` | 395 | SUBSCRIPT ONE |
| `₂` | 454 | SUBSCRIPT TWO |
| `₃` | 193 | SUBSCRIPT THREE |
| `ʰ` | 707 | MODIFIER LETTER SMALL H |
| `ʷ` | 275 | MODIFIER LETTER SMALL W |
| `ʱ` | 25 | MODIFIER LETTER SMALL H WITH HOOK |
| `̯` | 1101 | COMBINING INVERTED BREVE BELOW |
| `̑` | 338 | COMBINING INVERTED BREVE |
| `̥` | 213 | COMBINING RING BELOW |
| `̄` | 15 | COMBINING MACRON |
| `̆` | 17 | COMBINING BREVE |
| `ɣ` | 36 | LATIN SMALL LETTER GAMMA |
| `θ` | 64 | GREEK SMALL LETTER THETA |
| `δ` | 55 | GREEK SMALL LETTER DELTA |
| `ə` | 117 | LATIN SMALL LETTER SCHWA |
| `ǫ` | 22 | LATIN SMALL LETTER O WITH OGONEK |
| `ā` | 367 | LATIN SMALL LETTER A WITH MACRON |
| `ē` | 100 | LATIN SMALL LETTER E WITH MACRON |
| `ī` | 86 | LATIN SMALL LETTER I WITH MACRON |
| `ō` | 93 | LATIN SMALL LETTER O WITH MACRON |
| `ū` | 47 | LATIN SMALL LETTER U WITH MACRON |
| `á` | 129 | LATIN SMALL LETTER A WITH ACUTE |
| `é` | 362 | LATIN SMALL LETTER E WITH ACUTE |
| `í` | 38 | LATIN SMALL LETTER I WITH ACUTE |
| `ó` | 87 | LATIN SMALL LETTER O WITH ACUTE |
| `ú` | 13 | LATIN SMALL LETTER U WITH ACUTE |
| `æ` | 41 | LATIN SMALL LETTER AE |
| `ð` | 16 | LATIN SMALL LETTER ETH |
| `þ` | 9 | LATIN SMALL LETTER THORN |
| `φ` | 37 | GREEK SMALL LETTER PHI |
| `χ` | 28 | GREEK SMALL LETTER CHI |
| `β` | 57 | GREEK SMALL LETTER BETA |
| `γ` | 15 | GREEK SMALL LETTER GAMMA |
| `κ` | 43 | GREEK SMALL LETTER KAPPA |
| `λ` | 105 | GREEK SMALL LETTER LAMDA |
| `μ` | 92 | GREEK SMALL LETTER MU |
| `ν` | 85 | GREEK SMALL LETTER NU |
| `ο` | 87 | GREEK SMALL LETTER OMICRON |
| `π` | 62 | GREEK SMALL LETTER PI |
| `ρ` | 68 | GREEK SMALL LETTER RHO |
| `σ` | 69 | GREEK SMALL LETTER SIGMA |
| `τ` | 96 | GREEK SMALL LETTER TAU |
| `υ` | 26 | GREEK SMALL LETTER UPSILON |
| `ω` | 81 | GREEK SMALL LETTER OMEGA |
| `ᾱ` | 8 | GREEK SMALL LETTER ALPHA WITH MACRON |

## Remaining stray combining-mark candidates

None found after the additional pass.


## Structured lexical dataset pass — 2026-04-29

Generated companion lexical datasets from the cleaned Markdown extraction:

- lexical/root entries: 379
- stem/building statements: 444
- reconstructed-form occurrences: 2394
- heading-level cross-reference rows: 70

Automated character checks on the structured rows found:

- replacement characters: 0
- private-use characters: 0
- leftover U+04AE/U+04AF palatovelar-artifact candidates: 0

Rows containing Greek, combining marks, or subscript numerals are flagged in `char_flags` for downstream import caution; these are expected in this source and are not treated as errors.
