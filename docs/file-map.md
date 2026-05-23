# File Map — Supersedences and Migrations

---
last_updated: 2026-05-22T00:00-04:00
---

Tracks file renames, moves, merges, and deletions across the project. When a file is superseded, the old path is listed here with its new location.

---

## Completed Migrations (2026-05-22)

| Old path | New path | Notes |
|---|---|---|
| `docs/phonological-history.md` | `docs/grammar/ch3-development/phonological-history.md` | Moved into grammar volume as ch3 (Development). Old path deleted. |
| `grammar/verbs.md` | `docs/grammar/ch4-ghandwa/verbs.md` | Moved into grammar volume as ch4 synchronic Ghandwa. Old path deleted. |
| `grammar/paradigms-nominal.md` | `docs/grammar/ch4-ghandwa/paradigms-nominal.md` | Moved into grammar volume as ch4 synchronic Ghandwa. Old path deleted. |
| `docs/notation.md` (§§1–6, 8–9) | `docs/grammar/ch1-introduction/notation.md` | Grammar/script content split out. `docs/notation.md` retains workflow content (§§7, 10–15). |

---

## Planned Future Migrations

| File | Destination | Condition |
|---|---|---|
| `grammar/verb-eval-template.md` | Retire | After all 7 flagged verbs are in the lexicon and the template is no longer needed as a working document |
| `grammar/verbs-worksheet.md` | Retire | After verb paradigm work is complete for the 20+ verbs currently lacking paradigms |
| `grammar/verbal-system.md` | Retire; verify no content survives that isn't in `docs/grammar/ch4-ghandwa/verbs.md` | Before deletion |
| `grammar/` directory | Delete | After all three files above are retired |

---

## Previously Completed Supersedences

| Old path | Status | Notes |
|---|---|---|
| `ghandwa_comparanda_ringe_pgmc.md` | Merged → `docs/comparanda.md` | 2026-03-14 |
| `ghandwa_comparanda_pic.md` | Merged → `docs/comparanda.md` | 2026-03-14 |
| `lexicon-core.tsv` | Deprecated | Superseded by NocoDB as authoritative source |
| `lexicon-ref.tsv` | Deprecated | Superseded by NocoDB |
| `vocab/lexicon.tsv` | Archived → `vocab/archive/` | Periodic TSV exports from NocoDB; not the live source |
| `vocab/lexicon-reconcile.tsv` | Archived → `vocab/archive/` | |
