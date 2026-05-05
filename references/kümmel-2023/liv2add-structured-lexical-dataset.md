---
title: 'Structured lexical dataset for Addenda und Corrigenda zu LIV²'
source_file: 'liv2add.pdf'
source_markdown: 'liv2add.md'
source_type: 'companion structured dataset'
extraction_date: '2026-04-29'
pass_status: 'structured lexical dataset pass with character-audit checks'
---

# Structured lexical dataset

This companion dataset is source-faithful rather than interpretively normalized. It preserves the LIV² addenda notation in the entry headings, stem statements, and reconstructed-form contexts. The rows are intended for sorting, filtering, search, and later manual normalization.

## Files

- `liv2add-lexical-entries.csv` / `.jsonl`: one row per detected lexical/root entry. JSONL includes the full `body_markdown` field and is safer for programmatic import than CSV when multiline body text matters.
- `liv2add-stem-statements.csv` / `.jsonl`: one row per detected stem-building statement such as Präsens, Aorist, Perfekt, Desiderativ, Kausativ, Iterativ, and Neubildungen.
- `liv2add-reconstructed-forms.csv`: occurrence index of star-prefixed reconstructed forms found in headings and entry bodies, with short source contexts.
- `liv2add-crossrefs.csv` / `.jsonl`: entries whose headings contain redirects, see-references, removals, alternatives, or related cross-reference signals.

## Summary counts

| Measure | Count |
|---|---:|
| lexical/root entries | 379 |
| stem/building statements | 444 |
| reconstructed-form occurrences | 2394 |
| cross-reference-style headings | 70 |
| entries marked Neu | 58 |
| entries marked uncertain | 53 |

## Field notes

- `primary_headword` is the first star-prefixed form detected in the heading; it is not silently normalized.
- `target_headword` is filled only when a heading-level redirect or see-reference exposes a second star-prefixed form.
- `heading_gloss` preserves quoted gloss material from the heading when present.
- `statement_markdown` preserves source wording for each detected stem statement. These rows are intentionally not reduced to a single language/form/gloss schema because many entries contain compound arguments, alternatives, and notes.
- `char_flags` mark high-risk character contexts, including Greek, combining marks, subscript numerals, and any unresolved replacement/private-use characters. Presence of a flag does not mean an error; it means the row is worth care in downstream import.

## Character-audit result

| Check | Count |
|---|---:|
| replacement-character | 0 |
| private-use | 0 |
| cyrillic-straight-u-possible-palatovelar-artifact | 0 |

## Sample lexical-entry rows

| entry_id | pdf_page_range | section | heading | primary_headword | target_headword | heading_gloss | heading_relation_tags |
| --- | --- | --- | --- | --- | --- | --- | --- |
| liv2add-0001 | 10-11 | *bʰ- | *bʰag- | *bʰag- |  |  |  |
| liv2add-0002 | 11 | *bʰ- | *bʰeh₁g̑- | *bʰeh₁g̑- |  |  |  |
| liv2add-0003 | 11 | *bʰ- | 1.*bʰeh₂- | *bʰeh₂- |  |  |  |
| liv2add-0004 | 11 | *bʰ- | *bʰei̯d- | *bʰei̯d- |  |  |  |
| liv2add-0005 | 11 | *bʰ- | *bʰend- | *bʰend- |  |  |  |
| liv2add-0006 | 11 | *bʰ- | *bʰer- | *bʰer- |  |  |  |
| liv2add-0007 | 11-12 | *bʰ- | *bʰerg̑- | *bʰerg̑- |  |  |  |
| liv2add-0008 | 12 | *bʰ- | *bʰergʰ- | *bʰergʰ- |  |  |  |
| liv2add-0009 | 12 | *bʰ- | *bʰerH- | *bʰerH- |  |  |  |
| liv2add-0010 | 12 | *bʰ- | Neu: ?1.*bʰers- ‘eilen?’ | *bʰers- |  | eilen? | new; uncertain |
| liv2add-0011 | 12 | *bʰ- | Neu: 2.*bʱers-1 ‘hervorbrechen, bersten’2 | *bʱers-1 |  | hervorbrechen, bersten | new |
| liv2add-0012 | 12 | *bʰ- | *bʰeru̯- | *bʰeru̯- |  |  |  |

## Sample stem-statement rows

| statement_id | primary_headword | statement_type | reconstructed_forms_in_statement | glosses_in_statement |
| --- | --- | --- | --- | --- |
| liv2add-0001-s01 | *bʰag- | Aorist | *bʰag-; *baɣ-; *g | zuteilen; weiht, stiftet; bringen |
| liv2add-0003-s01 | *bʰeh₂- | Präsens | *bʰi-bʰéh₂-/bʰh₂-; *wi-bibā-; *bibā-; *bibā-sa-; *β(ə)βās-; *apa-bibā-sa-; *apa-bāsa-? | scheinen; die Farbe wechseln; bleich werden |
| liv2add-0006-s01 | *bʰer- | Zum Präsens | *bʰer-e- | sollen bringen; verliert, büßt ein; fließt, ergießt sich |
| liv2add-0006-s02 | *bʰer- | Zum Iterativ |  | tragen; halten |
| liv2add-0007-s01 | *bʰerg̑- | Präsens | *bʰr̥(g̑)-sg̑ó- | röstet |
| liv2add-0008-s01 | *bʰergʰ- | Präsens | *bʰḗrgʰ-/bʰérgʰ-; *berga- | bergen, verwahren; vernachlässigen; schauen, spähen |
| liv2add-0009-s01 | *bʰerH- | Zum Nasalpräsens | *bər-n°; *brī- | schneiden; werden gebrochen |
| liv2add-0010-s01 | *bʰers- | Präsens | *bʰérs-/bʰr̥s- | flieht |
| liv2add-0011-s01 | *bʱers-1 | Aorist | *bʱérs-/bʱr̥s- | breche |
| liv2add-0011-s02 | *bʱers-1 | Präsens | *bʱr̥s-i̯é- | bricht |
| liv2add-0012-s01 | *bʰeru̯- | Präsens | *barwa-; *warba-; *ferw- | sieden, wallen |
| liv2add-0013-s01 | *bʰes- | Präsens | *uz-baha-; *uz-bāhaya-; *bʰos-éi̯e- | überdrüssig werden; sich überessen; verdrießen |

## Further normalization recommendations

For a database-grade lexicon, the next step should be manual schema mapping, not further automated extraction. Recommended manual fields would include `root_normalized`, `root_sort_key`, `liv2_status`, `stem_type_normalized`, `language`, `attested_form`, `gloss_normalized`, `source_reference`, and `confidence`. The current dataset supplies the source-faithful evidence needed for that mapping without flattening ambiguous source statements.
