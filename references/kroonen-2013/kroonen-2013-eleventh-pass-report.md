# Kroonen 2013 eleventh-pass report

Scope: targeted pass on `kroonen-2013-tenth-pass.md`, limited to residual `/J`/`fJ`-type artifacts, control characters, unresolved markers, and selected high-risk angle-bracket/diacritic artifacts.

## Verification basis

Page-image checks were used for pages 40, 58, 61, 64, 83, 146, 165, 166, 182, 191, 194, 310, 347, 436, 596, 804, 805, and 808. Some pattern-limited replacements were also applied to reconstructed verbal endings where the OCR pattern was unambiguous.

## Result summary

| Artifact class | Before | After | Change |
|---|---:|---:|---:|
| `control_characters` | 1 | 0 | -1 |
| `unclear_markers` | 10 | 0 | -10 |
| `malformed_thorn_sequences` | 171 | 142 | -29 |
| `angle_bracket_latin_clusters` | 583 | 572 | -11 |
| `replacement_character` | 0 | 0 | 0 |
| `starred_uppercase_P_forms` | 0 | 0 | 0 |

- Correction rules with at least one hit: 89.
- Actual replacements: 98.
- Remaining source-text `[unclear]` markers: 0.
- Remaining control characters: 0.
- Regenerated lexical dataset rows: 2859.

## Main corrected zones

- Resolved all remaining source-text `[unclear]` markers in the index pages that had been left by previous OCR passes.
- Removed the final control character in the `*þwerha-` entry.
- Corrected page-image-verified residual thorn/eth artifacts in entries including `*abuha-`, `*alda-`, `*aljan-`, `*awi-`, `*awidja-`, `*falþan-`, `*finþan-`, `*fōþra-`, `*inþera-`, and `*paþa-`.
- Corrected selected high-visibility angle-bracket/diacritic artifacts such as `OE m<Eger` → `OE mæger`, `ON <Er` → `ON ær`, and `OE <Ewisc` → `OE æwisc`.

## Remaining issues

Residual `/J`/`fJ`-class hits remain, but the remaining set is mixed: index material, Sanskrit/Avestan/Greek OCR, slash-as-slash notation, and uncertain special characters. I did not blanket-replace these because that would reduce character accuracy. The largest remaining class is still angle-bracket and Greek/Indic OCR damage, especially in the index and in dense comparanda. A later pass should be either a Greek/Indic index pass or a dedicated angle-bracket/diacritic pass, not a broad cleanup.

## Stress-test table

| Test | Before | After | Status | Note |
|---|---:|---:|---|---|
| `pdf_page_anchors` |  | 833 | PASS | missing=0; duplicates=0 |
| `lexical_dataset_rows` |  | 2859 | INFO | conservative regenerated entry-like rows |
| `malformed_thorn_sequences` | 171 | 142 | WARN |  |
| `control_characters` | 1 | 0 | PASS |  |
| `unclear_markers` | 10 | 0 | PASS |  |
| `angle_bracket_latin_clusters` | 583 | 572 | WARN |  |
| `replacement_character` | 0 | 0 | PASS |  |
| `starred_uppercase_P_forms` | 0 | 0 | PASS |  |
| `search_[unclear]` |  | 0 | INFO | literal smoke search |
| `search_/J` |  | 54 | INFO | literal smoke search |
| `search_fJ` |  | 34 | INFO | literal smoke search |
| `search_jJ` |  | 0 | INFO | literal smoke search |
| `search_j:J` |  | 0 | INFO | literal smoke search |
| `search_/p` |  | 54 | INFO | literal smoke search |
| `search_m<Eger` |  | 0 | INFO | literal smoke search |
| `search_Verschii` |  | 0 | INFO | literal smoke search |
| `search_Verschärfung` |  | 11 | INFO | literal smoke search |
| `search_\*paþa-` |  | 2 | INFO | literal smoke search |
| `search_\*finþan-` |  | 4 | INFO | literal smoke search |
| `search_\*falþan-` |  | 1 | INFO | literal smoke search |
| `search_\*fōþra-` |  | 1 | INFO | literal smoke search |
| `search_φάρυγξ` |  | 2 | INFO | literal smoke search |
| `search_τέτραξ` |  | 1 | INFO | literal smoke search |
| `search_awe/Ji` |  | 0 | INFO | literal smoke search |
| `search_finpan` |  | 0 | INFO | literal smoke search |
| `search_fanpjan` |  | 0 | INFO | literal smoke search |
| `search_papa-` |  | 1 | INFO | literal smoke search |
