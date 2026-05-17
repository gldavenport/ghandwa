# Handoff: Verbal System Session A

Date: 2026-05-16  
Output file: `grammar/verbal-system.md` (v0.5, 309 lines)  
Status: §8 substantively closed; two TBD present forms remain as lexicon tasks, not blocking

---

## What was decided this session

### Governing design principle

The Ghandwa verbal system is built from **Italic–Germanic consensus**, used as a positive inclusion heuristic — not a blanket rule. Italic–Germanic agreement is strong evidence for adoption; it does not automatically include shared losses or reductions. Where branches diverge, decisions are made case by case and documented in the Design Notes section of `verbal-system.md`.

### Verb classification

Six present-stem classes established:

| Class | Label | Status |
|---|---|---|
| I | Thematic root present | Default; productive |
| IIA | *-ye/o-* present | Productive/semi-productive |
| IIB | *-éye/o-* causative/factitive | Productive |
| III | Athematic root present | Relic; high-frequency inherited verbs only |
| IV | Nasal present | Limited; two subclasses |
| V | Reduplicated present | Relic; lexically enumerated |
| VI | Middle/deponent | Relic; not productive |

### Present system

- Thematic root present paradigm fully established (*légō*, *légezi*, *légeti*, *légomos*, *légete*, *légonti*)
- Intervocalic *\*s > z* established as regular sound change (Germanic-sourced); produces 2sg *-ezi*, *-zi* (athematic)
- Athematic 3pl resolved: *\*h₁snti* → *santi* by CHC > CaC or CaRC convergence; same pattern across all athematics (*yanti*, *danti*, *stanti*). **Transformer does not yet handle this correctly; hand-derive.**
- Nasal presents: two active subclasses — `nasal-infix` (attested ×4: *ganṓti*, *talnā́ti*, *iunékti*, *kalnéiti*) and `nasal-suffix` (supported, unattested, deferred to verb generator). *-néw/nu-* type dropped for insufficient WIE support. Laryngeal coloring within `nasal-infix` is phonological, not morphological.
- Reduplicated presents: relic class; confirmed *dídōti* 'give', *píboti* 'drink'

### Mood system

- **Subjunctive:** long-vowel thematic (*-ō/ē-*) + primary endings; athematic verbs thematize (*esēti*, *eyēti*, *dōēti*, *stāēti*). Long-vowel hiatus sequences (*dōēti*, *stāēti*) not contracted at Ghandwa level — left to daughters
- **Optative:** *-oy-* + secondary endings
- **Imperative:** 2sg bare stem, 3sg *-etōd*, 2pl *-ete* (syncretic), 3pl *-ontōd*; long imperative type following Italic

### Non-finites

- Infinitive: accusative of *-tu-* stem → suffix *-tum* (Italic-parallel)
- Active participle: *-ont-*
- Passive/result participle: *-to-*
- Verbal nouns: *-tum*, *-ti-*, *-men-*

### Middle/mediopassive

Italic-type *-r* endings; relic category. 2pl/3sg syncretic (*-etor*); inherited, not corrected. Full paradigm in `verbal-system.md` §4.

### Past system

Single preterite absorbing aorist and perfect functions. Three sub-formations:

| Formation | Source | Default for |
|---|---|---|
| Thematic preterite | PIE imperfect | Thematic and derived verbs |
| Root preterite | PIE root aorist | Inherited irregular verbs; lexically listed |
| Reduplicated preterite | PIE perfect | High-frequency relics; lexically enumerated |

No dental preterite at the Ghandwa level; left to daughters.

**Reduplicated preterite inventory (initial):**

| Gloss | Present | PIE perfect | Pret. 3sg |
|---|---|---|---|
| give | *dídōti* | *\*de-dóh₃-* | *dedṓt* |
| stand | *stā́ti* | *\*ste-stóh₂-* | *stestṓt* |
| do/put | TBD | *\*dhe-dhóh₁-* | *ðeðṓt* |
| drink | *píboti* | *\*pi-ph₃-* | *pipṓt* |
| carry | TBD | *\*bhe-bhór-* | *βeβṓrt* |

'Be' and 'go' are suppletive; no reduplicated preterites. 'Know' → preterite-present class (next session). Standard for future additions: PIE reduplicated perfect reconstructable + verb is high-frequency or basic.

**Key insight:** reduplicated preterites are PIE residue, not an Italic–Germanic consensus item. Both branches independently retained different subsets with little crossover. Ghandwa retains them by conservatism, not branch agreement.

---

## What is still open

### Minor / lexicon tasks (not blocking)

- 'Do/put' and 'carry' need present forms established in the lexicon before their reduplicated preterite rows are complete
- `nasal-suffix` subclass has no lexicon attestation; deferred to verb generator session

### Substantive agenda for next session(s)

These are the remaining Italic–Germanic items and system-level decisions not yet addressed:

| Topic | Notes |
|---|---|
| Preterite-present verbs | 'Know' (*ganṓti*) feeds this class; 'see' also. Need inventory and paradigm |
| Past subjunctive and optative | Not yet defined; both branches have them |
| Past middle/mediopassive | Endings not yet established |
| Ablaut in root and reduplicated preterites | O-grade/zero-grade distribution not fully specified |
| Verbal accent | Italic and Germanic diverge sharply; needs a decision |
| Preverb–verb accent interaction | Depends on accent decision |
| Full athematic paradigms | 'Be', 'go', 'give', 'stand' — present + past in one place |
| Suppletive verbs | 'Be' and 'go' need suppletive preterite stems established |
| *nasal-suffix* paradigm | Deferred to verb generator |

---

## Files touched this session

| File | Action |
|---|---|
| `grammar/verbal-system.md` | Created and updated to v0.5 |
| `vocab/archive/lexicon.tsv` | Read-only; used to identify nasal-present entries and PIE preforms |

---

## Changelog

| Date | Version | Description |
|---|---|---|
| 2026-05-16 | 1.0 | Initial handoff covering verbal system session A |
