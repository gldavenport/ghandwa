---
title: "Instructions & Filesystem Audit — Handoff"
last_updated: 2026-06-06
session: "Full instructions review against live filesystem; all decisions recorded below."
---

# Instructions & Filesystem Audit — Handoff

Audit conducted 2026-06-06. Covers `docs/ghandwa-project-instructions-claude.md` against the
live filesystem at `/Users/g_/Documents/GitHub/ghandwa/`. All items resolved in-session unless
marked **PENDING**.

---

## Completed This Session

| Item | Action taken |
|---|---|
| B: `sources/` → `references/` | Renamed. `references/` confirmed live. |
| A2: `tools/README.md` | Deleted. |
| D1: `docs/daughters.md` | Deleted. |
| D2: `_inbox/README.md` | Moved to `docs/reference-notes/crotonian.md`. |
| D2: `_inbox/` (repo root) | Now empty (`.DS_Store` only); delete. |
| D2: `corpus/_inbox/` | Image removed; now empty; delete. |
| Image: UUID.png | Renamed `ash-gatherer-and-old-woman.png`, moved to `world/`. |

---

## A. Immediate Fixes to Instructions (path corrections)

### A1. `corpus/lore.md` → `world/lore.md`
**Section 3 table, corpus row.** `corpus/` contains only `inscriptions.md`. `lore.md` lives at
`world/lore.md` (repo root). `file-map.md` has a pending migration of it to `docs/world/`, not yet
executed. Update instructions to `world/lore.md` now; update again after migration lands.

### A2. `tools/README.md` — delete and update pointer
`tools/README.md` is self-described as stale ("covers only the old JSX transformer and does not
mention the Python package"). **Gary to delete it.** Instructions §6 pointer ("See `tools/README.md`")
should be updated to `tools/docs/pie_transformer/ARCHITECTURE.md`.

### A3. Section 5 lexicon TSV convention
Section 5 currently says "TSV exports to `vocab/lexicon.tsv` happen at milestones for Git version
history." This is wrong in two ways: (a) `lexicon.tsv` is archived at `vocab/archive/`; (b) the
export format is CSV not TSV.

**Correct convention:** `vocab/archive/lexicon-YYYY-MM-DD.csv` is exported periodically for
convenient access when NocoDB is unavailable. There is no regular export schedule otherwise;
NocoDB is the canonical lexicon.

---

## B. `sources/` → `references/` rename  ✅ COMPLETE

Renamed in-session. Unblocks C6. Remaining follow-up:
- Update `sources-index.py` hardcoded paths (if any) — verify before next use
- Update `sources-lookup.md` path prefix header (still says `sources/{dir}/{file}`)
- Log in `file-map.md`

---

## C. Instructions Table Additions

Items to add to the §3 source-of-truth table once the above fixes are applied.

### C1. `vertenda/` — translation benchmarks corpus
> | Translation corpus (benchmarks, lexicon audit) | `vertenda/` |

`vertenda/` contains 10 translation exercises (Schleicher, Beowulf, Catullus 5, Nāsadīya, etc.)
plus a lexicon audit (`vertenda/README.md`) that maps directly to `lexicon-gaps.md`. Last audited
2026-05-23 against 615-entry export. This directory drives gap-filling work and is a major project
resource not currently mentioned anywhere in the instructions.

### C2. `tools/docs/pie_deriver/` — derivational generator
> | PIE derivational generator — spec, handoff, tool doc | `tools/docs/pie_deriver/` |

Files: `derive-spec.md`, `derive-handoff.md`, `pie_deriver.md` (last updated 2026-06-02).
Companion script: `tools/pie_deriver.py`. The deriver generates attested PIE derivational
candidates from verbal roots; output is PIE-only (no surface Ghandwa forms). Active enough to
have its own spec directory.

### C3. `tools/pie_core/` — shared tokenizer/normalizer
> | Shared tokenizer, normalizer, token definitions (used by transformer and deriver) | `tools/pie_core/` |

Note in table: not invoked standalone; consumed by `pie_transformer` and `pie_deriver`.

### C4. Active `vocab/` working files
> | Active lexicon working files (staging, gaps, notes, pre-root backfill) | `vocab/lexicon-staging.md`, `vocab/lexicon-gaps.md`, `vocab/lexicon-notes.md`, `vocab/pre-root-backfill.tsv` |

These are temporary working files; they will go away as the lexicon matures. List them now for
discoverability. `pre-root-backfill.tsv` has 189 entries with a ChatGPT work order pending.

### C5. `docs/reference-notes/` — working reference notes
> | Working reference notes (alt phonologies, Ringe ordered changes, verbal system sources) | `docs/reference-notes/` |

Files: `alt-phonologies.md`, `ringe-ordered-changes.md`, `ghandwa-verbal-system-source-list.md`.
Migration from `docs/` root was listed as pending in `file-map.md` but is already complete.
Update `file-map.md` to reflect completed status.

### C6. Bibliography index — **PENDING rename (see B)**
> | Bibliography index and speed-lookup | `references/references-index.tsv`, `references/references-lookup.md` |

Do not add to instructions until `sources/` → `references/` rename is complete.

### C8. `_inbox/` directories — add note to §10

Add a brief note under §10 (Technical Patterns) or §7 (Document Conventions):

> `_inbox/` directories (repo root and `corpus/`) are intentional staging drop zones for
> incoming files. They are not orphans when empty.

### C7. Swanenvleugel in §3 / §9
`docs/comparanda.md` row in §3 currently mentions "Swanenvleugel" without introduction.
Swanenvleugel does not appear in §9 (Reference Works). For now, add a brief gloss in §9:

> Swanenvleugel — working title for a comparative phonology rule inventory consulted during
> development of `comparanda.md`; will be formalized or retired as comparanda work matures.

*(Adjust wording once the actual work's status is clearer.)*

---

## D. Filesystem Cleanup

### D1. Already tracked in `file-map.md` — incomplete  **PENDING: Gary to execute**

| File/Path | Action |
|---|---|
| `docs/daughters.md` | **Delete.** Superseded in full by `docs/grammar/ch5-daughters/` (2026-05-27). Retained as read-only archive; confirmed for deletion. |
| `docs/handoff-central-daughter-pipeline.md` (root of `docs/`) | **Delete or move to `docs/handoffs/`.** Superseded by dated version `docs/handoffs/handoff-central-daughter-pipeline-2026-05-31.md`. |
| `world/lore.md`, `world/science.md` | **Migrate to `docs/world/`.** `docs/world/` exists and is empty. After move, delete root `world/` directory. Note: `file-map.md` lists source paths as `docs/science.md` and `corpus/lore.md` — both are wrong; actual paths are `world/science.md` and `world/lore.md`. Correct `file-map.md` when logging the migration. |
| `docs/reference-notes/` migration | Listed as pending in `file-map.md`; files are already there. **Mark complete in `file-map.md`.** |

### D2. Not tracked — need disposition decisions

| File/Path | Status | Recommended action |
|---|---|---|
| `grammar/` (repo root) | Unresolved | **Audit needed.** See §E below. |
| `tools/README.md` | ✅ Deleted | — |
| `_inbox/` (repo root) | Empty; `.DS_Store` only | **Keep.** Intentional staging drop zone. |
| `_inbox/README.md` | ✅ Moved to `docs/reference-notes/crotonian.md` | — |
| `corpus/_inbox/` | Empty | **Keep.** Intentional staging drop zone. |
| `corpus/_inbox/` image | ✅ Moved to `world/ash-gatherer-and-old-woman.png` | — |
| `ghandwa-noco-2026-06-05.db.zip` | Unresolved | Add to `.gitignore` or move to `backups/`; binary blob at repo root is noise. |
| `docs/world/` | Empty; destination for pending `world/` migration | No action until D1 migration executed. |

---

## E. Audit Required — `grammar/` at Repo Root  **PENDING**

Three files exist at `grammar/` that are not mentioned in the instructions and whose relationship
to `docs/grammar/ch4-ghandwa/verbs.md` is unverified:

- `grammar/verb-eval-template.md` — Memory notes: "6 of 7 flagged verbs now in lexicon; staleness
  flag partially resolved." Status uncertain post-reconciliation.
- `grammar/verbal-system.md` — Relationship to `docs/grammar/ch4-ghandwa/verbs.md` unknown.
- `grammar/verbs-worksheet.md` — Memory notes: "has paradigms for only 6 verbs; 20+ verbs lack
  paradigm work." Still active working file.

**Recommended next session action:** open all three against `docs/grammar/ch4-ghandwa/verbs.md`
and diff for content overlap. For each file: (a) superseded → log in `file-map.md` and delete;
(b) active but unintegrated → decide whether to migrate or keep as scratch; (c) fully active
working file → add to §3 instructions table.

---

## F. Instructions Update Sequence

| Step | Item | Status |
|---|---|---|
| 1 | `sources/` → `references/` rename | ✅ Done |
| 2 | Apply A1, A2, A3 fixes to instructions | PENDING |
| 3 | Apply C1–C5 table additions | PENDING |
| 4 | Apply C6 (bibliography row) and C7 (Swanenvleugel) | PENDING |
| 5 | Delete empty `_inbox/` dirs; execute D1 cleanup; update `file-map.md` | PENDING |
| 6 | Execute E audit; resolve `grammar/` disposition | PENDING |
| 7 | Final pass on instructions to confirm all paths live | PENDING |

---

## G. Items Not Requiring Instructions Changes

- `docs/ghandwa-project-instructions-claude.md` — the instructions file itself in the repo. No
  action needed; it's Gary's to maintain.
- `docs/infra/nocodb-mcp-setup.md` — infrastructure setup; not a §3 table item (operational,
  not linguistic reference).
- `docs/ling489-syllabus.md` — course syllabus; reference material only.
- `docs/linguistics-extract-instructions.md` — ChatGPT extraction instructions; operational.
- `docs/ref-works-outstanding.md` — acquisition list; not a §3 table item.
- `docs/handoffs/` contents — per-session records; no §3 entry needed.
- `ghandwa-noco-2026-06-05.db.zip` — see D2; no instructions change needed, just repo hygiene.
