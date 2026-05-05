# Kroonen 2013 — Fourteenth pass: angle-bracket/diacritic cleanup

Scope: targeted high-confidence cleanup of residual angle-bracket OCR artifacts and diacritic damage, using the thirteenth-pass Greek-index Markdown as the base. This was not a full page-by-page verification pass.

## Summary counts

| Artifact class | Before | After |
|---|---:|---:|
| <E artifacts | 131 | 0 |
| <i! artifacts | 10 | 0 |
| <l! artifacts | 20 | 16 |
| Latin-cluster angle artifacts | 491 | 349 |
| replacement character | 0 | 0 |
| control characters | 0 | 0 |

## Applied correction rules with hits

| Find | Replace | Hits | Note |
|---|---|---:|---|
| `<E` | `æ` | 131 | OCR artifact for æ in Old English/Old Norse/phonetic [æ] and index forms |
| `<i!` | `ǣ` | 10 | OCR artifact for ǣ in Old English forms |
| `OEf<est` | `OE fæst` | 1 | High-confidence exact angle/diacritic artifact correction |
| `f<et` | `fæt` | 1 | High-confidence exact angle/diacritic artifact correction |
| `b<l!c` | `bæc` | 1 | High-confidence exact angle/diacritic artifact correction |
| `ON r<l!na` | `ON ræna` | 1 | High-confidence exact angle/diacritic artifact correction |
| `ON s<l!r` | `ON sær` | 1 | High-confidence exact angle/diacritic artifact correction |
| `ON k<l!sa` | `ON kæsa` | 1 | High-confidence exact angle/diacritic artifact correction |
| `fj<ir` | `fjár` | 1 | High-confidence exact angle/diacritic artifact correction |
| `d<io` | `dáð` | 2 | High-confidence exact angle/diacritic artifact correction |
| `g<itt` | `gátt` | 2 | High-confidence exact angle/diacritic artifact correction |
| `t<ittur` | `táttur` | 2 | High-confidence exact angle/diacritic artifact correction |
| `bh<irati` | `bhárati` | 3 | High-confidence exact angle/diacritic artifact correction |
| `d<idhiiti` | `dádhāti` | 2 | High-confidence exact angle/diacritic artifact correction |
| `d<ihati` | `dáhati` | 1 | High-confidence exact angle/diacritic artifact correction |
| `p<lr$ɣi-` | `pārṣṇi-` | 1 | High-confidence exact angle/diacritic artifact correction |
| `p<irdate` | `párdate` | 1 | High-confidence exact angle/diacritic artifact correction |
| `t<irati` | `tárati` | 2 | High-confidence exact angle/diacritic artifact correction |

## Assessment

The pass removed the highest-confidence `<E` and `<i!` classes and selected exact Germanic/Indic angle artifacts. Remaining angle-bracket hits are mixed: many are PIE relation symbols or uncertain OCR for laryngeals, Greek, Indic transliteration, or notation. They should not be blanket-normalized.
