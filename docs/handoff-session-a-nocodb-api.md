# Handoff: Session A — NocoDB API Patch Script

**Date:** 2026-05-16  
**Scope:** Write and test a general-purpose script for merging ChatGPT-returned TSVs back into NocoDB. Use it immediately for the `pre-root-backfill.tsv` work order.

---

## Context

The lexicon is now in NocoDB (SQLite, localhost:8080), installed at `/Users/g_/Documents/GitHub/ghandwa/ghandwa-db/`. The database has a single merged table with 716 rows × 50 columns. NocoDB exposes a REST API.

Work sent externally to ChatGPT (cognate mining, column backfill, etc.) comes back as a TSV with `entry_id` + changed columns. There is no native NocoDB "import over existing data" — updates must go through the API row by row.

---

## Immediate deliverable: `tools/noco-patch.py`

A Python script that:

1. Takes as input:
   - A TSV file path (the returned work order)
   - A NocoDB API token
   - A list of column names to update (to avoid accidentally overwriting untouched columns)
2. For each row in the TSV:
   - Looks up the NocoDB row by `entry_id`
   - PATCHes only the specified columns
3. Reports: rows updated, rows skipped (entry_id not found), rows with no change

**API pattern:**
```
GET  http://localhost:8080/api/v1/db/data/noco/{baseId}/{tableId}?where=(entry_id,eq,{id})
PATCH http://localhost:8080/api/v1/db/data/noco/{baseId}/{tableId}/{rowId}
```

Headers: `xc-token: {API_TOKEN}`

To get `baseId` and `tableId`: NocoDB UI → table → URL contains both, or GET `/api/v1/db/meta/projects/` to list bases.

---

## First use: `pre-root-backfill.tsv`

File: `/Users/g_/Documents/GitHub/ghandwa/vocab/pre-root-backfill.tsv`  
Rows: 189  
Column to update: `lemma_1_pre_root`  
Status: 0/189 filled — this is the pending ChatGPT work order defined in `vocab/handoff-pre-root-backfill.md`

Once ChatGPT returns a filled TSV, run:
```bash
python3 tools/noco-patch.py \
  --tsv vocab/pre-root-backfill-filled.tsv \
  --columns lemma_1_pre_root \
  --token {API_TOKEN}
```

---

## Also do in this session

- Update `grammar/verb-eval-template.md` staleness flag:
  - Current flag says 7 verbs never entered into TSV
  - 6 of 7 are now in the lexicon
  - *dédōti* vs. *dídōti* discrepancy resolved: lexicon *dídōti* (i-reduplication) is correct; template had wrong e-reduplication, contaminated by Latin *dedī*
  - Update the changelog entry in the template header to reflect this

---

## Key file locations

| File | Path |
|---|---|
| NocoDB install | `ghandwa-db/` (renamed from `democratic_quelea/`) |
| NocoDB database | `ghandwa-db/noco.db` |
| Pre-root backfill work order | `vocab/pre-root-backfill.tsv` |
| Backfill handoff doc | `vocab/handoff-pre-root-backfill.md` |
| Verb eval template | `grammar/verb-eval-template.md` |

---

## Setup note

To get the API token: NocoDB UI → Team & Settings → API Tokens → generate one. To get `baseId` and `tableId` for the script: check the URL when viewing the table in NocoDB, or hit `GET /api/v1/db/meta/projects/` with the token.
