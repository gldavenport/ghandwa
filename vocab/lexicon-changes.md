# Ghandwa Lexicon Changelog

Companion changelog for `lexicon.tsv`. Keeping last 3 entries only.

---
last_updated: 2026-05-08T00:00-04:00
session: "File renamed from lexicon.md to lexicon-changes.md for disambiguation (lexicon.md was ambiguous between 'a markdown version of the lexicon' and 'a changelog for the lexicon'). No content changes."
changelog:
  - 2026-05-08T00:00-04:00 | 22 lines | Renamed from lexicon.md → lexicon-changes.md. README.md updated to match. No content changes.
---

## Change Log

| Timestamp (ISO 8601) | Lines | Changes |
|---|---|---|
| 2026-04-26T00:00-04:00 | 711 | **15 new entries + 5 hygiene fixes.** Gary added offline: numerals 11–19 (*undekam* through *nevandekam*, all draft); *áusteros* 'east' (o/ā adj, draft); *arktiiós* 'bear-like' (stub); *mélðō* 'the one who smashes' (ō/nés m., draft); *parí* 'in front of' (adp, draft). Renames detected: *akmṓ*→*ákmō* (root-syllable accent correction), *waltós* (w→v orthographic normalization). Hygiene: fixed stale xrefs *akmṓ*→*ákmō* in *grā́wō*.cross_references and *targóm*.synonyms; set *arktiiós* entry_status→stub; set *mélðō* entry_status→draft and cross_references→*melðániios*. |
| 2026-03-24T12:00-04:00 | 689 | **Data hygiene pass (37 edits across 29 entries).** Verb classification: *kéleti*, *skéleti* → thematic, simple thematic present. Gender fills: *akmṓ* → m, *ɣvérō* → m, *skvónɣvom* → n. Stem class: *ɣvérō* → ō/nés, *skvónɣvom* → o, *léuðertūts* → ts/tés, 9 -rḗks name compounds root → root noun. Semantic field/subfield for 19 draft entries. IPA status: *keitís*, *keivís*, *ovióm* review_lemma_accent → complete. |
| 2026-03-24T12:00-04:00 | 691 | **Verb category normalization (42 edits on 42 entries) + new column.** Added `verb_derivation` (col 75). Normalized `verb_stem_type` values across 7 categories. True reclassifications: *ganṓti* root→nasal-infix, *talnā́ti* root→nasal-infix, *rogéieti* causative→\*-éye/o-, *skélieti* root→\*-ye/o-. Filled `verb_derivation: causative` for 7 \*-éye/o- entries. Schema defined in `verbs.md` §TSV Column Schema. |
