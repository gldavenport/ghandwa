# Handoff — Worldbuilding Content from Noodling Handoff + Open Sociolinguistic Items

**Date:** 2026-06-08
**Source session:** Sociolinguistic model development and integration
**Priority:** Low — no blocking dependencies

---

## Context

`docs/handoffs/ghandwa-noodling-2026-05-24.md` contains worldbuilding content that predates the current `docs/world/` structure and has not been canonically placed. The sociolinguistic framing in that file is superseded by `docs/world/ghandwa-historical-sociolinguistic-model.md`. The linguistic content (daughter branch formulations) reflects earlier decisions since updated in `docs/grammar/ch5-daughters/`.

What remains potentially useful: geographic model, named place, and ethnonym material.

---

## Task 1 — Mine the noodling handoff for unplaced worldbuilding content

File: `docs/handoffs/ghandwa-noodling-2026-05-24.md`

Sections to extract and place in `docs/world/`:

**§2 Geographic Model** — Core settlement pattern (delta/coastal zone, river expansion), shoreline + river economy. Check whether any of this conflicts with or duplicates the geographic model implied by the Koch interaction-sphere framing in the sociolinguistic model. If compatible, extract to a new file `docs/world/geography.md`.

**Septakvās** — Named confluence metropolis; prestige center of Common Ghandwa; cosmopolitan Bronze Age river-maritime city. Currently only in the noodling handoff and mentioned in `docs/world/lore.md` (ch5-02 background). Should have a canonical entry in `docs/world/geography.md` or a dedicated `docs/world/septakvas.md`.

**§9 Ethnonyms** — *teutā treies akvās* ("the people of the three rivers"), *treiakvaskōs* ("Three-Rivers person"). Check whether these are already in NocoDB. If not, flag for lexicon entry.

**§8 Material / Metal Lexicon** — *argantóm* (silver), *auzantom* (gold), *santóm* (iron). Cross-check against NocoDB — most likely already entered. The conceptual material (copper/twilight, iron/blood, gold/dawn) is relevant to `docs/world/science.md` which already has the *engman* gradient in metals section. Add cross-references if not already present.

**Stale content to ignore** — The sociolinguistic framing (§§1, 3–7, 10), A/B/C naming discussion, Central voiced fricative formulation: all superseded. Do not migrate.

---

## Task 2 — Open items from sociolinguistic model integration (low priority)

These were deferred during the 2026-06-08 session. Neither is blocking.

**Item 4.3 — Stage 1 pan-dialectal vs. convergent ambiguity**

Location: `docs/grammar/ch5-daughters/ch5-02-late-common-ghandwa.md`

The file says Stage 1 changes were pan-dialectal "either originating early enough to spread through the full dialect continuum, **or phonetically natural enough to arise convergently across it**." The second option makes some Stage 1 changes `status: parallel-innovation` rather than `status: pan-Ghandwa` in the YAML schema, which affects how the generator treats them.

Resolution options:
- Resolve per change (nasal assimilation, prosodic restructuring, trimoraic regularization each tagged individually)
- Mark the hedge as intentionally unresolved: "distinction has no practical effect on daughter outputs"

**Item 4.4 — Neo-Ghandwa gap in sociolinguistic model**

`docs/world/ghandwa-historical-sociolinguistic-model.md` covers Stages 0–4 in the stage table but has no prose section on Stage 3 Neo-Ghandwa specifically. `docs/grammar/ch5-daughters/ch5-03-comparative-phonology.md` §3.1 has the substantive description: priestly-scholarly recovery, merchant-warrior koine, common tongues. The sociolinguistic model should eventually get a Stage 3 section that:
- Characterizes Neo-Ghandwa explicitly as a koine (post-divergence, contact-leveled, artificially spread) — the term deliberately avoided for Stage 0–1
- References ch5-03 §3.1 for linguistic detail
- Connects to the Religious Landscape section of `docs/world/lore.md` (the priestly class maintaining the synthesis is the same class behind Neo-Ghandwa)
