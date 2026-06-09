# File Map — Supersedences and Migrations

---
last_updated: 2026-06-08
---

Tracks file renames, moves, merges, and deletions across the project. When a file is superseded, the old path is listed here with its new location.

---

## Moved / Created (2026-06-08)

| Action | Path | Notes |
|---|---|---|
| Created | `docs/world/ghandwa-historical-sociolinguistic-model.md` | Historical-sociolinguistic model: dialect pool, stage taxonomy (stage-0 through stage-4), YAML metadata schema for sound changes, literacy model |
| Moved | `world/lore.md` → `docs/world/lore.md` | Worldbuilding: mythology, cosmology, Agnis theology |
| Moved | `world/science.md` → `docs/world/science.md` | Worldbuilding: natural philosophy, *engman* gradient |
| Moved | `world/ash-gatherer-and-old-woman.png` → `docs/world/ash-gatherer-and-old-woman.png` | Illustration |

Gary to delete: `world/` directory at repo root (now empty).

---

## Moved / Created (2026-06-07)

| Action | Path | Notes |
|---|---|---|
| Created | `docs/infra/nocodb-backup.md` | Infrastructure doc: Ubuntu systemd backup + Mac launchd pull; supersedes `docs/handoffs/handoff-nocodb-backup.md` |
| Created | `tools/mac/pull-ghandwa-db-backups.sh` | Mac rsync pull script (source of truth; live copy at `~/Library/Scripts/`) |
| Created | `tools/mac/local.ghandwa-db-backup-pull.plist` | launchd plist (source of truth; live copy at `~/Library/LaunchAgents/`) |

Gary to delete: `docs/handoffs/handoff-nocodb-backup.md`.

---

## Moved / Created (2026-06-06)

| Action | Path | Notes |
|---|---|---|
| Moved | `docs/crotonian-rules.md` → `tools/docs/pie_transformer/crotonian-rules.md` | Operational wékʷos/Crotonian transformer spec; belongs with pipeline docs |
| Moved | `docs/numeral-suffixes.md` → `docs/grammar/ch4-ghandwa/sec4-4-word-formation/numeral-suffixes.md` | Active grammar content; migrated to ch4 word-formation |
| Created | `docs/handoffs/pipeline-spec-gaps.md` | Flags transformer pipelines lacking standalone spec docs |

Gary to delete originals: `docs/crotonian-rules.md`, `docs/numeral-suffixes.md`.

Pending (directories created, files not yet moved — Gary to move and delete originals):
- `docs/reference-notes/` — will receive: `docs/alt-phonologies.md`, `docs/ringe-ordered-changes.md`, `docs/ghandwa-verbal-system-source-list.md`
- `docs/world/` — ✅ completed 2026-06-08 (source was `world/` at repo root, not `docs/science.md`/`corpus/lore.md` as originally noted)
- `docs/ghandwa-daughter-b.md` — superseded by `docs/grammar/ch5-daughters/ch5-03-comparative-phonology.md` + `tools/pie_transformer/pipelines/daughter_b.py`; retire to `docs/handoffs/` or delete

---

## Created (2026-05-31)

| New path | Notes |
|---|---|
| `docs/grammar/preface.md` | Grammar preface: Italo-Germanic default, dialect continuum premise, phonological tensions, PIE framework. Design reasoning confined here (and forthcoming epilogue) rather than inline in grammar chapters. |

---

## Completed Migrations (2026-05-30)

| Old path | New path | Notes |
|---|---|---|
| `docs/grammar/ch3-development/phonological-history.md` (§§0, 2) | `docs/grammar/ch3-development/sec3-1-introduction.md` | Chapter intro: comparative position, scope, notation pointer |
| `docs/grammar/ch3-development/phonological-history.md` (§§3–5, 8–10) | `docs/grammar/ch3-development/sec3-2-sound-changes/` | Sound change rules distributed across 6 files by stage/function |
| `docs/grammar/ch3-development/phonological-history.md` (§§1, 6, 7) | `docs/grammar/ch4-ghandwa/sec4-2-phonology/sec4-2-phonology.md` | Synchronic inventory, Boukólos standing rule, deliberate tensions |

`docs/grammar/ch3-development/phonological-history.md` is superseded in full and deleted.

---

## Completed Migrations (2026-05-27)

| Old path | New path | Notes |
|---|---|---|
| `docs/daughters.md` | `docs/grammar/ch5-daughters/ch5-01-overview.md` | §1 Cultural and Historical Framing |
| `docs/daughters.md` | `docs/grammar/ch5-daughters/ch5-02-late-common-ghandwa.md` | §2.1 Late Common Ghandwa (Stage 1) |
| `docs/daughters.md` | `docs/grammar/ch5-daughters/ch5-03-comparative-phonology.md` | §§2.2–3 Stages 2–4 comparative phonology; 2B fully rewritten (2026-05-27); 2C #s>z initial rule corrected |
| `docs/daughters.md` | `docs/grammar/ch5-daughters/ch5-04-comparative-morphology.md` | §4 Morphological directions |
| `docs/daughters.md` | `docs/grammar/ch5-daughters/ch5-05-lexicon-testing.md` | §§5–6 Lexicon testing and status |
| `docs/daughters.md` | `docs/grammar/ch5-daughters/ch5-appendices.md` | All appendices |

`docs/daughters.md` is superseded in full. Retained at old path as read-only archive until confirmed for deletion. Daughters renamed throughout: A = Western, B = Central, C = Eastern.

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
