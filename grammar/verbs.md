# Ghandwa Verbal Morphology

---
last_updated: 2026-03-14
session: "Reconciliation pass — lexicon verb inventory now documented; open questions updated with new evidence from entries 379–400"
changelog:
  - 2026-03-14 | 207 lines | Added §Lexicon Verb Inventory (22 entries, organized by present stem class); updated open questions §5 (middle/passive: *mariétor* now exists as first deponent), §6 (*-éye/o-* causatives: *moldéieti, moréieti, nokéieti* now attested), §Sievers: noted *βarkiéti* as test case. Updated scope note.
  - 2026-03-11T22:00:00Z | 138 lines | Initial creation from working notes. Established design philosophy, present stem inventory (4 classes), broader system categories, deferred items, and open questions.
---

Working document for Ghandwa's verbal system. Companion to `ghandwa-prompt.md` (phonology and nominal morphology) and `ghandwa_lexicon.tsv` (canonical lexicon). Material here is architectural — paradigm tables and surface forms will be added as the system is fleshed out.

**Citation convention:** Verbs are cited in the 3rd person singular present active indicative (e.g. *arketi*, not bare roots).

---

## Design Philosophy

The verbal system follows the same principles as Ghandwa's phonology and nominal morphology:

**Inheritance, not innovation.** The system is built from what Proto-Italic, Proto-Celtic, and Proto-Germanic (the 3sl) share. Where all three agree on a formation, that is the Ghandwa formation. Where they diverge through independent innovation, Ghandwa stays at the PIE-inherited form rather than following any single branch. Proto-Balto-Slavic (making the 4sl) is consulted where it supports broad overlap, but held at arm's length due to satem changes and structural divergences.

**Only partly regularized.** Ghandwa preserves enough inherited class diversity to force later daughter-level remodeling. The verb system is not a clean grid — it is a late-PIE-derived, western-leaning inventory of formations at varying degrees of productivity. Some classes are large and regular; others are small, irregular, or semantically opaque. This is deliberate. A daughter language that wants a tidy four-conjugation system (like Latin) or a strong/weak split (like Germanic) must do the tidying itself.

**Semantic underspecification.** Where PIE did not grammaticalize a uniform semantic contrast between formations, Ghandwa does not invent one. Root-specific semantic tendencies are permitted; system-wide oppositions are not imposed.

**Common material as base checklist.** The inventory below is treated as safe shared material across the 3sl (with 4sl confirmation where available), not as a reconstructed proto-language. The question of whether a given feature is retention or shared innovation is not prioritized at this stage.

**Celtic's role.** Proto-Celtic confirms inherited morphology at the older/common level but is deprioritized as a structural model due to the comparative messiness of its later verbal system. It is a witness, not a template.

---

## Present Stem Classes

Four present-tense stem classes, all justified by 3sl inheritance:

### 1. Plain thematic presents

The broad default present class. Root + thematic vowel *-e/o-* + primary endings. The most populous class and the one into which new formations are most likely to be drawn by analogy.

Not a single semantically uniform category — includes statives, activities, punctuals, and other Aktionsart types depending on the root. The plain thematic present is defined morphologically, not semantically.

### 2. *-ye/o-* thematic presents

A distinct thematic present formation, formally characterized by the suffix *-ye/o-* between root and primary endings. Well attested across the 3sl: Proto-Germanic weak presents, Proto-Italic present-stem classes, Proto-Celtic *-ye/o-* presents, and Proto-Balto-Slavic class morphology all continue this formation.

Semantic tendencies (root-specific, not system-wide):
- Causative / transitivizing (the strongest and most widespread tendency)
- Atelic / non-directed / distributive / iterative (attested in some roots or branches)

These tendencies are real but not grammaticalized into a rule. A *-ye/o-* present may be causative for one root and iterative for another; the formation carries a family resemblance, not a uniform function. Where a root has both a plain thematic and a *-ye/o-* present, the semantic relationship between them is root-specific.

### 3. Nasal presents

An inherited mixed class characterized by a nasal element (*-n-* infix or *-ne/o-* suffix) in the present stem. Two subtypes are attested across the 3sl:

**Athematic nasal presents** — the older type. Root with nasal infix, athematic endings. PIE pattern: *\*li-ne-kʷ-ti* (full grade infix in strong forms, zero grade in weak). Small, archaic, possibly already shrinking.

**Thematicized nasal presents** — the remodeled type. Originally athematic nasal presents that acquired a thematic vowel. The thematicization is well attested across branches as independent but convergent remodeling.

🔲 **Open question:** Are both subtypes living (if small) classes in Ghandwa, or is the athematic subtype already fossilizing? The athematic type is archaic across all branches, but it is *preserved* across all of them too, at least residually. Decision deferred — needs concrete verb inventory to evaluate.

### 4. Residual athematic presents

A small, closed set of high-frequency verbs that retain athematic present inflection. These are lexical relics, not a productive class. Every branch of the 3sl (and the 4sl) preserves a residue of athematic verbs rather than leveling everything into thematic conjugations. The canonical members include 'to be', 'to give', 'to eat', and a handful of others.

These verbs are expected to show irregular or suppletive behavior and to resist analogical pressure. They are the verbs that daughters must individually decide how to handle — some will thematicize them, some will preserve them, some will replace them with new formations.

---

## Broader System Architecture

Beyond the present stem classes, the following categories are established as part of Ghandwa's verbal system based on 3sl (and where noted, 4sl) overlap:

### Established categories

**Finite person-number inflection.** Verbs inflect for person (1st, 2nd, 3rd) and number (singular, plural). Dual is not posited — it is a PIE archaism not robustly shared across the 3sl as a productive verbal category.

**Present / non-past indicative.** The central finite category. The repository of the present stem classes described above.

**Imperative.** A normal finite category, not marginal. Present imperative at minimum; further imperative types (e.g. future imperative) are deferred.

**At least one non-indicative mood.** All branches preserve modal morphology of some kind (subjunctive, optative, or material derived from them). The specific inventory and morphology of Ghandwa's moods are deferred for a dedicated session — what is established is that the system is not indicative-only.

**A marked past / preterite category.** All branches have a distinct past-tense formation, but they do not build it the same way (Germanic preterite ≠ Italic perfect ≠ Celtic syncretic preterite ≠ Slavic aorist). What is safe: Ghandwa has a morphologically marked past. What is not yet decided: how it is formed.

**Stem classes matter.** The verbal system is not flat. Multiple present-stem classes coexist (as detailed above), and the system resists reduction to a single conjugation pattern.

**Derived verbal stems with semantic load.** Formations involving *-ye/o-* and *-eye/o-* carry derivational semantics (causative, factitive, iterative) and are not merely inflectional variants. Proto-Germanic weak class 1 (*-éye/o-*), Italic iterative-causatives, and parallel formations in Celtic and Balto-Slavic all continue this pattern.

**Infinitive or verbal noun.** At least one non-finite form functioning as a verbal noun / infinitive. All branches are comfortable with this category. Specific morphology deferred.

**Participles.** A regular part of the verbal system. Two participles are especially well supported across branches:
- Present active participle (*-ont-* / *-nt-*) — attested in Italic, Germanic, and Balto-Slavic
- Past / resultative participle (*-to-*) — attested across all four branches as a past participial adjective

### Deferred categories

The following are explicitly placed outside the initial system and reserved for later sessions:

- **Subjunctive / optative specifics** — mood morphology and distribution
- **Productive middle voice** — the old middle is not the main engine of the system in any of the 3sl; Ghandwa's voice system is fundamentally active, with middle/passive as at most residual or secondary
- **Future tense** — no shared future formation across the 3sl
- **Specific past/preterite morphology** — "there is a past" is established; "how it is built" is not
- **Branch-specific hallmarks** — Italic *-r* passive, Germanic dental weak preterite, Celtic absolute/conjunct, Slavic obligatory aspect pairing: none of these are part of the Ghandwa base layer

---

## Lexicon Verb Inventory

As of the 2026-03-14 TSV (409 lines), 22 verbs are attested in the lexicon. Organized by present stem class:

### Class 1 — Plain thematic presents

| ID | Citation form | Gloss | Preform |
|---|---|---|---|
| 325 | *édeti* ~ *édonti* | to eat | \*h₁édeti |
| 328 | *gvémeti* ~ *gvémonti* | to come; to step | \*gʷémeti |
| 329 | *sékveti* ~ *sékvonti* | to follow | \*sékʷeti |
| 334 | *tekseti* ~ *teksonti* | to weave; to craft | \*tékseti |
| 326 | *véideti* ~ *véidonti* | to see; to know | \*weydeti |
| 327 | *βúeti* ~ *βúonti* | to become; to be | \*bʰúHeti |
| 373 | *píboti* ~ *píbonti* | to drink | \*piph₃éti (reduplicated thematic) |

Note: *píboti* is listed here as thematic despite its reduplicated stem because it takes thematic endings. It could also be classified as a distinct reduplicated subtype.

### Class 2 — *-ye/o-* and *-éye/o-* presents

| ID | Citation form | Gloss | Preform | Subtype |
|---|---|---|---|---|
| 313 | *βarkiéti* | to cram, crowd | \*bʰr̥kʷyéti | *-ye/o-* |
| 380 | *moldéieti* ~ *moldéionti* | (cause to) melt | \*moldéyeti | *-éye/o-* causative |
| 400 | *moréieti* ~ *moréionti* | kill (make die) | \*moréyeti | *-éye/o-* causative |
| 399 | *nokéieti* ~ *nokéionti* | kill (make disappear) | \*noḱéyeti | *-éye/o-* causative |

*moldéieti*, *moréieti*, and *nokéieti* are the first *-éye/o-* causatives in the lexicon — see open question §6 below.

### Class 3 — Nasal presents

| ID | Citation form | Gloss | Preform |
|---|---|---|---|
| 130 | *klíneti* ~ *klínenti* | to be leaning, sloping | \*ḱlíneti (nasal infix) |

Single attested member. See open question on the athematic/thematic nasal split.

### Class 4 — Residual athematic presents

| ID | Citation form | Gloss | Preform |
|---|---|---|---|
| 61 | *ésti* ~ *sénti* | is | \*h₁ésti |
| 322 | *éiti* ~ *iénti* | to go | \*h₁éyti |
| 333 | *ðḗti* ~ *ðánti* | to put, place; to dedicate | \*dʰéh₁ti |
| 323 | *stā́ti* ~ *stā́nti* | to stand | \*stéh₂ti |
| 324 | *βérti* ~ *βarénti* | to carry | \*bʰérti |
| 387 | *vélti* | to wish, want | \*wélh₁ti |

*vélti* (387) is a recent addition expanding this class. Note: the 3pl form for *vélti* is listed as *valénti* in the TSV.

### Middle/deponent

| ID | Citation form | Gloss | Preform |
|---|---|---|---|
| 398 | *mariétor* ~ *marióntor* | to die | \*mr̥yétor |

First and only deponent in the lexicon — see open question §5 below.

### Unclassified / stubs

| ID | Citation form | Gloss | Notes |
|---|---|---|---|
| 379 | *méldeti* ~ *méldonti* | melt, smelt | IPA blank; thematic root? |
| 383 | *sēieti* | (gloss pending) | preform \*séh₁yeti; stub |
| 388 | *voléieti* | (gloss pending) | preform \*wolh₁éyeti; stub; presumably causative of *vélti* |

---

## Open Questions

🔲 **Nasal present split.** Are athematic nasal presents a living (if small) class, or already fossils? See §3 above. Only one nasal present (*klíneti*) is attested so far — not enough data to decide.

🔲 **Past/preterite formation.** Morphology entirely unspecified. Needs its own session — the question is large and consequential for the whole system.

🔲 **Mood inventory.** At least one non-indicative mood exists. Which one(s), and with what morphology?

🔲 **Infinitive/verbal noun morphology.** Category is established; form is not.

🔲 **Middle/passive residue.** How much of the old middle survives, if any? Deponent-like verbs? Medio-passive endings on a handful of roots? **Update (2026-03-14):** *mariétor* (398, 'to die', \*mr̥yétor) is now in the lexicon as a middle deponent — the first and so far only verb with medio-passive morphology. Its partner *moréieti* (400, 'to kill/make die') is a thematic *-éye/o-* causative, giving a clean active/middle pair: *moréieti* 'kills' (active causative) vs. *mariétor* 'dies' (middle deponent). This confirms at least a residual middle survives. Open: is *mariétor* a lonely fossil, or are there more candidates?

🔲 ***-éye/o-* causatives.** Distinct from *-ye/o-* presents — a dedicated causative/factitive formation. Needs its own treatment: productive or lexicalized? Separate conjugation class or subtype of *-ye/o-*? **Update (2026-03-14):** Three *-éye/o-* causatives now attested: *moldéieti* (380, 'cause to melt'), *moréieti* (400, 'kill/make die'), *nokéieti* (399, 'kill/make disappear'). All three are transparently derived from base verbs (*méldeti* 379, *mariétor* 398). The pattern is productive enough to warrant treatment as a subclass of Class 2 rather than a handful of lexicalized forms.

🔲 **Sievers' Law.** Deferred in the phonological prompt doc pending verbal morphology. Now relevant — glide alternations (*-ye/o-* ~ *-iye/o-*) conditioned by syllable weight of the preceding syllable will affect the surface forms of *-ye/o-* presents. **Note:** *βarkiéti* (313, \*bʰr̥kʷyéti) is a test case — the *-ye/o-* suffix appears after a heavy syllable.

🔲 **Verb citation forms in lexicon.** Convention is 3sg present active indicative. Once paradigms exist, the lexicon will need a verbal entry format (parallel to the nom ~ gen format for nouns). Design pending.

🔲 **Transformer support.** The phonological transformer currently handles nom ~ gen noun pairs. Verbal forms will need to be runnable through the transformer. Whether this requires a new input mode or just feeding individual forms through the existing single-form mode is TBD.

---

## Methodology Notes

These notes record the reasoning behind the design framework and are preserved for continuity across sessions.

The goal is not to reconstruct a single proto-language or to prove a shared clade among the western/northern IE branches. Similarities among the 3sl (and 4sl) are treated as overlap from late dialect-continuum inheritance, useful as design material regardless of their historical explanation.

The present active indicative of Italic, Celtic, and Germanic looks very similar, especially in the simple thematic present. This similarity is treated as useful common material without requiring a verdict on retention vs. innovation.

The task was deliberately narrowed: enumerate common features first, then design the system. The inventory above is the enumeration; paradigm-building is the next phase.
