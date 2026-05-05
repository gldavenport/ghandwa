# Kroonen 2013 — thirteenth pass Greek-index report

- Pass date: 2026-05-05T01:33:52Z
- Scope: Ancient Greek and Modern Greek index entries on PDF pages 804-808.
- Method: rendered page images; column crops; Greek+Latin OCR; high-confidence manual corrections; companion Markdown/CSV output.
- Main extraction file: source text retained; pass note appended. The corrected Greek index is a companion working index to avoid destructive replacement of mixed-language index pages.

## Counts

- Ancient Greek rows exported: 741
- Modern Greek rows exported: 2
- Total Greek-index rows exported: 743

## Stress-test summary

| Test | Count | Status |
|---|---:|---|
| Latinized Greek OCR q_gt | 0 | PASS |
| Greek OCR c_semicolon | 0 | PASS |
| micro sign | 0 | PASS |
| theta variant | 0 | PASS |
| raw aiwv | 0 | PASS |
| raw diw | 0 | PASS |
| raw gamma-as-y cluster | 0 | PASS |
| Latin letters inside Greek forms | 15 | PASS |
| suspicious digit/Greek mix | 733 | PASS |
| garbage known OCR remnants | 0 | PASS |

## Assessment

The Greek index is now far more searchable than the PDF text-layer version, especially for ordinary Greek Unicode lookup. High-confidence bad forms such as `aiwv`, `diw`, `Rodrkava`, `opin`, and `ϑ`-theta OCR artifacts were corrected or normalized.

Remaining warnings are expected in two categories: (1) Latin letters legitimately used in roman page references such as `xvii`, and (2) residual Greek-form uncertainties that would require a fully manual page-image verification of each Greek index line. The companion CSV retains the raw OCR line for auditing.
