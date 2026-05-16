# Handoff: Session E — Grammar Paradigms into NocoDB

**Date:** 2026-05-16  
**Priority:** Medium — after Session A (API script), since bulk import will use the same patch tooling  
**Scope:** Design and populate NocoDB tables for nominal and verbal paradigms. This is a multi-pass project, not a single import.

---

## Rationale

Paradigm tables are inherently relational:
- Each lexicon entry has a `nom_stem_class` (e.g. `o-stem-m`, `u-stem`, `r-stem`) or `verb_stem_type`
- Each stem class has a fixed set of case/number cells
- The ending for each cell is the same across all entries in the class

Storing this in NocoDB allows: querying all forms of a given stem class, cross-referencing from lexicon entries to their paradigm, and tracking which paradigm cells are still gaps (marked `—` in the current markdown).

**What stays in markdown:** the prose notes (sound change derivations, analogical explanations, comparative remarks). The `grammar/paradigms-nominal.md` file remains the authoritative explanatory document. NocoDB holds the structured data; markdown holds the reasoning.

---

## Proposed schema

### Table: `paradigm_endings`

One row per paradigm cell. Columns:

| Column | Type | Notes |
|---|---|---|
| `paradigm_id` | AutoNumber | PK |
| `stem_class` | SingleSelect | Controlled vocabulary (see below) |
| `pos` | SingleSelect | `noun`, `adj`, `verb` |
| `gender` | SingleSelect | `m`, `f`, `n`, `m/f`, `—` |
| `case` | SingleSelect | `nom`, `voc`, `acc`, `gen`, `dat`, `ins`, `loc` |
| `number` | SingleSelect | `sg`, `pl`, `du` (du not yet attested) |
| `ending_orth` | SingleLineText | Surface ending, orthographic (e.g. `-os`, `-ās`) |
| `ending_ipa` | SingleLineText | IPA of ending only (e.g. `os`, `aːs`) |
| `pie_source` | SingleLineText | PIE ending it derives from |
| `status` | SingleSelect | `established`, `pending`, `gap` |
| `notes` | LongText | Cell-level notes |

### Controlled vocabulary: `stem_class`

From `paradigms-nominal.md` and `grammar/verbs.md`:

**Nominal:**
- `ā-stem` (fem)
- `o-stem-m` (masc)
- `o-stem-n` (neut)
- `i-stem`
- `u-stem-mf` (masc/fem)
- `u-stem-n` (neut)
- `ī-stem` (fem; currently folded into ā-stem)
- `cons-stem` (root nouns)
- `r-stem` (kinship)
- `n-stem` / `men-stem`
- `s-stem-n` (neut)
- `r/n-heteroclite`

**Adjectival:**
- `adj-o/ā`
- `adj-u`
- `adj-i`
- `adj-cons`

**Verbal (present active — add others as needed):**
- `verb-thematic`
- `verb-athematic-root`
- `verb-reduplicated-thematic`
- `verb-reduplicated-athematic`
- `verb-nasal-infix`
- `verb-causative-eye`
- `verb-ye`

### Table: `paradigm_examples`

Links a stem class to attested lexicon entries used as examples.

| Column | Type | Notes |
|---|---|---|
| `example_id` | AutoNumber | PK |
| `stem_class` | SingleSelect | FK to stem_class vocabulary |
| `entry_id` | Number | FK to lexicon table |
| `lemma` | SingleLineText | Denormalized for readability |
| `is_primary` | Checkbox | Primary example for the class |

---

## Current state of `paradigms-nominal.md`

Stem classes and fill status:

| Stem class | Sg filled | Pl filled | Notes |
|---|---|---|---|
| ā-stem | ✅ all 7 cases | ✅ all 7 | Complete |
| o-stem-m | ✅ all 7 | ✅ all 7 | Complete |
| o-stem-n | ✅ 7 (nom/acc/voc merged) | ✅ | Complete |
| i-stem | ✅ all 7 | partial (nom/acc only) | Pl mostly gaps |
| u-stem-mf | ✅ all 7 | ✅ all 7 | Complete |
| u-stem-n | ✅ 7 | ✅ | Complete |
| ī-stem | partial (nom, gen, dat) | all gaps | Explicitly deferred — folds into ā-stem |
| cons-stem | partial (nom, acc, gen, dat, loc) | partial (nom, gen) | IPA pending throughout |
| r-stem | all gaps | all gaps | Not yet established |
| n/men-stem | all gaps | all gaps | Not yet established |
| s-stem-n | ✅ all 7 | ✅ all 7 | Complete; IPA complete |
| r/n-heteroclite | partial (nom, gen) | all gaps | Pending water word resolution (Session B) |
| adj-o/ā | — (follows o-stem/ā-stem) | — | Not a separate table needed |
| adj-u | nom only | all gaps | Mostly pending |
| adj-i | all gaps | all gaps | Not yet established |
| adj-cons | all gaps | all gaps | Not yet established |

Verbal paradigms: in `grammar/verbs-worksheet.md`, 6 verbs done. Session C covers expansion.

---

## Suggested workflow

**Phase 1 — Nominal endings table (this session)**
1. Create `paradigm_endings` table in NocoDB with the schema above
2. Set SingleSelect options for all controlled vocabulary fields
3. Populate from `paradigms-nominal.md` — start with the five complete stem classes (ā, o-m, o-n, u-mf, u-n, s-n)
4. Mark gaps as `status = gap` rather than leaving them blank
5. Create `paradigm_examples` table and link primary examples from the lexicon

**Phase 2 — Verbal endings table (Session C or after)**
1. Same schema, `pos = verb`
2. Verbal cells are: person (1/2/3) × number (sg/pl) × mood (ind/subj/opt/imp) × voice (act/mid)
3. Populate as `verbs-worksheet.md` fills in (coordinate with Session C)

**Phase 3 — Gap-filling passes**
- r-stem, n/men-stem, consonant stem IPA, adj paradigms — fill as linguistic work allows
- Cross-reference with Session B (r/n heteroclite pending water word resolution)

---

## Link to lexicon

Once `paradigm_endings` exists, add a **Links** field in the lexicon table pointing to `paradigm_examples`. This lets you open any lexicon entry and see its full paradigm from the record view.

This requires the API patch script from Session A if you want to auto-populate the links for all 716 entries at once rather than clicking through them manually.

---

## Key files

| File | Purpose |
|---|---|
| `grammar/paradigms-nominal.md` | Source of truth for endings and notes — keep in sync |
| `grammar/verbs-worksheet.md` | Source for verbal paradigms |
| `grammar/verbs.md` | Verb stem type classification |
| `docs/notation.md` | Orthographic conventions |
| Session A handoff | API patch script — needed for bulk lexicon→paradigm linking |
| Session B handoff | Resolves r/n heteroclite before that paradigm can be completed |
| Session C handoff | Fills verbal paradigms to populate verbal endings table |
