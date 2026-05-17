# Handoff: Session C — Verb Paradigm Debt

**Date:** 2026-05-16  
**Scope:** Fill missing paradigms in `grammar/verbs-worksheet.md` for the 20+ verbs in the lexicon that lack paradigm work.

---

## Context

The lexicon (NocoDB, localhost:8080) has ~95 verb entries. `grammar/verbs-worksheet.md` currently has full paradigms for only 6 verbs. The goal of this session is to work through as many of the remaining verbs as time allows, prioritizing by verb class (so paradigms within each class are consistent).

`grammar/verb-eval-template.md` §4 has a quick-reference of PIE present stem types and their Ghandwa reflexes. `grammar/verbs.md` has the full classification schema (`verb_thematicity`, `verb_stem_type`, `verb_derivation` fields).

---

## Verbs with paradigms already in verbs-worksheet.md

(Do not redo these — use them as models for the same class.)

From memory, the 6 done are likely: *ésti*, *éiti*, *βérti*, *ðḗti*, *kalnéuti*, and one thematic. Confirm by reading `verbs-worksheet.md` at session start.

---

## Priority order for new paradigms

Work class by class — one full class done is more useful than scattered entries.

### Priority 1 — Athematic root presents

Pattern: full-grade root + zero ending in sg.; zero-grade root + thematic in pl.  
Model: *βérti ~ βarénti* (if in worksheet), *ɣvénti ~ ɣvanénti*

Candidates (from lexicon `verb_thematicity = athematic`, `verb_stem_type = root`):
- *ɣvénti ~ ɣvanénti* — strike, kill (*\*gʷʰen-*)
- *βā́ti ~ βánti* — speak authoritatively (*\*bʰeh₂-*)
- *stā́ti* — stand (*\*steh₂-*)
- *éiti* — go (*\*h₁ey-*) — may already be done
- *ésti* — is (*\*h₁es-*) — may already be done

### Priority 2 — Thematic root presents

Pattern: full-grade root + thematic vowel throughout; 3sg -eti, 3pl -onti.  
Model: use any confirmed thematic already in the worksheet.

Candidates:
- *édeti* — eat
- *véideti* — see/know
- *sékveti* — follow
- *gvéteti* — say
- *ðéɣveti* — burn
- *kléveti* — hear
- *wérteti* — turn
- *skéleti* — split
- *méldeti* — melt
- *régeti* — straighten

### Priority 3 — Reduplicated presents

- *dídōti ~ didónti* — give (reduplicated athematic; note i-reduplication, not e-)
- *píboti ~ píponti* — drink (reduplicated thematic; note lexicon has *píboti* not *pípoti* — h₃ voicing pending resolution)
- *ðḗti ~ ðánti* — put/place (reduplicated athematic)

### Priority 4 — Derived presents

- *éye-causatives*: *ðoɣvéieti*, *sodéieti*, *moldéieti*, *voléieti*, *rogéieti*, *moréieti*, *nokéieti*
- *Nasal infix*: *kalnéuti*, *kalnéiti*, *iunékti* — some may already be done
- *ye-presents*: *βarkiéti*, *sjūjéti*

---

## Format

Follow the existing paradigm format in `verbs-worksheet.md`. For each verb include at minimum:

- PIE preform → Ghandwa derivation (transformer-verified)
- Present active: 1sg, 2sg, 3sg, 1pl, 2pl, 3pl
- Note ablaut pattern (where it applies)
- Flag any transformer gaps or hand-corrections needed

---

## Key files

| File | Purpose |
|---|---|
| `grammar/verbs-worksheet.md` | Target file — add paradigms here |
| `grammar/verbs.md` | Classification schema and stem type definitions |
| `grammar/verb-eval-template.md` | Decision logic and worked examples |
| `tools/pie-2-ghandwa.jsx` | Transformer — run inputs to verify surface forms |
| `docs/phonological-history.md` | Sound change rules for manual derivations |
