# Handoff: Session D — Dangwa-Era Reconcile Archaeology

**Date:** 2026-05-16  
**Priority:** Low — do after Sessions A–C  
**Scope:** Assess `vocab/archive/lexicon-reconcile.tsv` (248 rows) to determine how many of the 173 "probable new entry" and 74 "probable merge" items are already in the current lexicon, and how many represent genuine gaps.

---

## Context

`lexicon-reconcile.tsv` was generated during an earlier project phase when the language was still called "Dangwa" (column names include "DW0", "DW1-F", etc.). It was a bulk intake/deduplication run against an older version of the lexicon. It has been archived to `vocab/archive/` and is no longer authoritative, but it may contain vocabulary candidates that never made it into the current lexicon.

The current lexicon is in NocoDB (localhost:8080, `ghandwa-db/`), 716 rows × 50 columns.

---

## Column key for lexicon-reconcile.tsv

The column names are non-standard. Key ones:

| Column | Meaning |
|---|---|
| `merged_term` | The candidate Ghandwa form |
| `narGloss` | Gloss |
| `intake_bucket` | `probable_new_entry` / `probable_merge` / `already_represented` |
| `review_flag` | `REVIEW:gloss-match`, `REVIEW:old1-only`, `REVIEW:possible-split` |
| `best_current_lemma` | Closest match found in the lexicon at time of reconciliation |
| `best_current_status` | Status of that match: `canonical`, `unresolved`, `candidate` |
| `best_match_score` | Fuzzy match score |
| `pos` | Part of speech |
| `PIE Root` | PIE source if known |

---

## Distribution

| Bucket | Count |
|---|---|
| probable_new_entry | 173 |
| probable_merge | 74 |
| already_represented | 1 |

Review flags set:
- `REVIEW:gloss-match` — 26 (fuzzy match on gloss only; form differs)
- `REVIEW:old1-only` — 23 (appeared in only one source list)
- `REVIEW:possible-split` — 2 (one source entry may cover multiple concepts)

---

## Suggested workflow

1. Export current lexicon from NocoDB as TSV (or use the Filesystem MCP to read it directly)
2. For each row in `lexicon-reconcile.tsv` where `intake_bucket = probable_new_entry`:
   - NFC-normalize and check `merged_term` against current lexicon lemmas
   - If not found: assess whether it's a genuine gap or a Dangwa-era artifact that no longer applies
   - Flag genuine gaps for lexicon entry
3. For `probable_merge` rows: check whether the merge target is still in the lexicon and whether the candidate form adds anything
4. Discard rows where `best_current_status = canonical` and the match is solid

**Do not attempt to batch-process this mechanically** — many Dangwa-era forms used different orthographic conventions (ğ instead of ɣ, inconsistent accent marking) and will generate false negatives on string matching. Human review of ambiguous cases is required.

---

## Key files

| File | Path |
|---|---|
| Reconcile file (archived) | `vocab/archive/lexicon-reconcile.tsv` |
| Lexicon (authoritative) | NocoDB localhost:8080 |
| Notation conventions | `docs/notation.md` |
