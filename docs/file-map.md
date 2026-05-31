# File Map — Supersedences and Migrations

---
last_updated: 2026-05-27T00:00-04:00
---

Tracks file renames, moves, merges, and deletions across the project. When a file is superseded, the old path is listed here with its new location.

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
