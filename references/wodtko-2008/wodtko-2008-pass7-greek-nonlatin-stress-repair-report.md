---
title: "Nomina im Indogermanischen Lexikon — pass-7 Greek/non-Latin stress-repair report"
source_file_name: "wodtko-2008.pdf"
extraction_date: "2026-05-03T21:57:28Z"
pass_status: "seventh-pass Greek/non-Latin target stress-test and repair layer"
---

# Wodtko 2008 — pass-7 Greek/non-Latin stress-test + repair report

## Scope

This pass targets the **704** pass-6 candidates that were explicitly separated as Greek/non-Latin or opaque script-surrogate cases. It does not silently overwrite the readable source Markdown. It creates a pass-7 lookup/collation layer with the pass-6 source candidate, pass-7 normalized form, confidence flag, repair action, and issue bucket side by side.

The main practical repair in this pass is the recurrent OCR confusion of long-vowel/macron notation in lexical forms: `ä → ā`, `ö/Ö/O → ō`, and `ü/Ü → ū`, applied only to lexical-form candidates without opaque Greek/script-surrogate characters, uppercase anomalies, embedded glosses, or candidate-boundary noise. Opaque Greek/custom-font OCR strings are kept unresolved unless a safe image-collated repair was available.

## Counts

- Pass-6 Greek/non-Latin target rows re-tested: **704**
- Rows repaired, trimmed, or image-collated in pass 7: **404**
- Rows still unresolved after pass 7: **300**
- Full internal lexical-form rows carried forward in pass-7 TSV: **9,300**
- Unique pass-7 lookup strings: **8,048**

## Pass-7 target classes

| class                                  |   count |
|:---------------------------------------|--------:|
| latin-script-macron-surrogate          |     349 |
| greek-or-opaque-script-surrogate       |     185 |
| nonlatin-unresolved-other              |     115 |
| candidate-boundary-noise-with-nonlatin |      54 |
| greek-script-image-collated            |       1 |

## Pass-7 confidence distribution for target rows

| confidence                           |   count |
|:-------------------------------------|--------:|
| medium-repaired-greek-nonlatin-pass7 |     349 |
| low-greek-or-nonlatin-surrogate      |     300 |
| filtered-noise-fragment              |      54 |
| high-image-collated                  |       1 |

## Pass-7 action distribution for target rows

| action                                                                     |   count |
|:---------------------------------------------------------------------------|--------:|
| repaired_latin_macron_surrogates                                           |     349 |
| kept_unresolved_opaque_script_surrogate                                    |     185 |
| kept_unresolved_nonlatin_other                                             |     115 |
| trimmed_obvious_nonlexical_tail_for_lookup;marked_candidate_boundary_noise |      54 |
| image_collated_greek_line_repair                                           |       1 |

## Stress-test results

| search_term   |   pass6_hits |   pass7_hits |   delta | assessment            |
|:--------------|-------------:|-------------:|--------:|:----------------------|
| *bōk          |            0 |            6 |       6 | improved              |
| *bōk-ō-       |            0 |            4 |       4 | improved              |
| bōk           |            0 |            6 |       6 | improved              |
| *barzdā       |            0 |            2 |       2 | improved              |
| *baidā        |            0 |            2 |       2 | improved              |
| *baidō        |            0 |            2 |       2 | improved              |
| *-bʰā         |            0 |            0 |       0 | no_change             |
| *-lōā         |            0 |            2 |       2 | improved              |
| *bʰer-ās      |            0 |            2 |       2 | improved              |
| *bʰrū         |            0 |            0 |       0 | no_change             |
| *bʰruH-ōn-    |            0 |            2 |       2 | improved              |
| *-tā-         |            0 |            4 |       4 | improved              |
| *dōm          |            0 |            2 |       2 | improved              |
| *-ōn-         |            0 |            6 |       6 | improved              |
| *-ōm          |            0 |            4 |       4 | improved              |
| *gʷdʰōm       |            0 |            0 |       0 | no_change             |
| *φακτῆρες     |            0 |            2 |       2 | improved              |
| φακτῆρες      |            0 |            2 |       2 | improved              |
| *qxx~         |            2 |            0 |      -2 | reduced_old_surrogate |
| *bOk          |            4 |            2 |      -2 | reduced_old_surrogate |
| *bök          |            4 |            0 |      -4 | reduced_old_surrogate |
| *ö            |           28 |            2 |     -26 | reduced_old_surrogate |
| *ä            |           38 |           10 |     -28 | reduced_old_surrogate |

## Manual/image-collated repair

- PDF page 79 / printed page 1: the source text-layer candidate `*qxx~)` was collated against the visible page image as `*φακτῆρες`. This is included as a high-confidence Greek repair in the pass-7 target file.

## Remaining limitations

This pass improves lookup for Latin-script non-Latin/macron forms and separates opaque Greek/custom-font surrogates more cleanly. It does **not** make every Greek form character-authoritative. Exact Greek recovery still requires manual image collation or a custom OCR workflow with systematic review, because the embedded OCR layer frequently represents Greek as Latin-like surrogate strings.
