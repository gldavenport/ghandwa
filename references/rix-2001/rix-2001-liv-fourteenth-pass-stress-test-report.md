---
source_title: "LIV fourteenth-pass targeted source-image collation report"
source_file_name: "rix-lexikon-indogermanischen verben.pdf"
extraction_date: "2026-05-05T02:29:54Z"
pass_status: "targeted source-image collation over thirteenth pass"
---

# LIV fourteenth-pass targeted source-image collation report

## Scope

This pass used the thirteenth-pass unresolved audit as a punch list. It focused on remaining Greek/pseudo-Greek rows and dense index-zone rows. It did not run a broad automatic cleanup. Corrections were either supported by rendered page OCR/page-image collation or were narrow high-confidence repairs of obvious Greek OCR artifacts in already-flagged rows. Unresolved rows remain in the audit files.

## Repair summary

| Item | Count |
|---|---:|
| targeted corrections attempted | 138 |
| targeted corrections applied | 135 |
| page-image/OCR-supported applied corrections | 34 |
| manual high-confidence applied corrections | 101 |
| attempted but not found in current text | 3 |

## Stress-test counts

| Check | thirteenth pass | fourteenth pass |
|---|---:|---:|
| page anchors | 828 | 828 |
| Greek/pseudo-Greek risk rows, same detector as thirteenth pass | 159 | 47 |
| dense-index risk rows, same detector as thirteenth pass | 14 | 3 |
| Greek/pseudo-Greek risk rows, expanded fourteenth-pass detector | 348 | 251 |
| dense-index risk rows, expanded fourteenth-pass detector | 22 | 13 |

The expanded detector is intentionally broader, so its absolute count is not comparable to the thirteenth-pass report count. Its purpose is to surface the next punch list after the easier Greek repairs.


## Targeted search probes

| Query | Hits |
|---|---:|
| `πορφύρει` | 1 |
| `φρίσσει` | 1 |
| `ἔφριξε` | 1 |
| `φρέαρ` | 1 |
| `ἀπ-έδρᾶν` | 1 |
| `ἀπο-διδράσκω` | 1 |
| `ἀπο-δράσομαι` | 1 |
| `ἔφθισα` | 3 |
| `φθει-/φθι-` | 1 |
| `ψινοντος` | 1 |
| `ἐγράψη` | 1 |
| `κλέος ἄφθιτον` | 1 |
| `φθίει νόσῳ` | 1 |
| `τραπέω` | 1 |
| `ἔτραπον` | 1 |
| `τρέπω` | 2 |
| `τροπέω` | 1 |
| `τρέψαι` | 1 |
| `φθάνω` | 2 |
| `φθείρω` | 2 |
| `φθίμενος` | 1 |
| `φῖτυ` | 3 |
| `φοβέομαι` | 2 |
| `δρέπω` | 1 |
| `δείδω` | 1 |
| `δείσομαι` | 1 |
| `τέτροφεν` | 1 |
| `τρέχω` | 1 |
| `τράχω` | 1 |
| `ὀΐφω` | 1 |
| `κρεμῶ` | 1 |
| `κύπτω` | 1 |
| `κρίνω` | 1 |
| `πείσομαι` | 1 |
| `συννέφει` | 1 |
| `πέσσω` | 1 |
| `πέττω` | 1 |
| `πίμπλημι` | 1 |
| `πέτομαι` | 1 |
| `πείρω` | 1 |
| `πίμπρημι` | 1 |
| `σφίγγω` | 1 |
| `στρέφω` | 1 |
| `ἔτεκον` | 1 |
| `τιτρώσκω` | 1 |
| `τρώγω` | 2 |
| `τρίβω` | 1 |
| `ὑφαίνω` | 1 |
| `ἰδεῖν` | 2 |

## Assessment

The fourteenth pass reduced the original unresolved Greek/pseudo-Greek risk set from 159 to 47 under the same detector used for the thirteenth pass, and reduced dense-index risk rows from 14 to 3 under that same detector. It also created a stricter expanded audit for the next pass; that file intentionally contains more rows because it catches additional damaged Greek-like patterns that the earlier detector ignored. Further useful work should continue from the audit list by page-by-page verification, not by broad whole-document substitution.

