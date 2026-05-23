# Ghandwa Verbal Morphology

---
last_updated: 2026-03-24
changelog:
  - 2026-03-24 | 430 lines | Merged verb-categories.md into this file. Added §TSV Column Schema (defines allowed values for `verb_thematicity`, `verb_stem_type`, new `verb_derivation` col 75). Added §Ringe 2017 Reference Mapping (full PIE inventory keyed to TSV values). Added §Pending Reclassifications (42 edits for Apple Numbers). Added §Dictionary Extraction Notes. Updated §Present Stem Classes to reference value table. Updated §Lexicon Verb Inventory to 94 verbs (49 classified, 45 blank). Resolved *-éye/o-* causatives open question (§6) — now covered by schema.
  - 2026-03-14 | 207 lines | Added §Lexicon Verb Inventory (22 entries, organized by present stem class); updated open questions §5 (middle/passive: *mariétor* now exists as first deponent), §6 (*-éye/o-* causatives: *moldéieti, moréieti, nokéieti* now attested), §Sievers: noted *βarkiéti* as test case. Updated scope note.
  - 2026-03-11T22:00:00Z | 138 lines | Initial creation from working notes. Established design philosophy, present stem inventory (4 classes), broader system categories, deferred items, and open questions.
---

Working document for Ghandwa's verbal system. Companion to `lexicon.tsv` (canonical lexicon), `verb-eval-template.md` (adoption decision framework), and `verbs-worksheet.md` (paradigm scratch work).

**Citation convention:** Verbs are cited in the 3rd person singular present active indicative (e.g. *tékseti*, not bare roots).

---

## Design Philosophy

The verbal system follows the same principles as Ghandwa's phonology and nominal morphology:

**Inheritance, not innovation.** The system is built from what Proto-Italic, Proto-Celtic, and Proto-Germanic (WIE) share. Where all three agree on a formation, that is the Ghandwa formation. Where they diverge through independent innovation, Ghandwa stays at the PIE-inherited form rather than following any single branch. Proto-Balto-Slavic (making NWIE) is consulted where it supports broad overlap, but held at arm's length due to satem changes and structural divergences.

**Only partly regularized.** Ghandwa preserves enough inherited class diversity to force later daughter-level remodeling. The verb system is not a clean grid — it is a late-PIE-derived, western-leaning inventory of formations at varying degrees of productivity. Some classes are large and regular; others are small, irregular, or semantically opaque. This is deliberate. A daughter language that wants a tidy four-conjugation system (like Latin) or a strong/weak split (like Germanic) must do the tidying itself.

**Semantic underspecification.** Where PIE did not grammaticalize a uniform semantic contrast between formations, Ghandwa does not invent one. Root-specific semantic tendencies are permitted; system-wide oppositions are not imposed.

**Common material as base checklist.** The inventory below is treated as safe shared material across WIE (with NWIE confirmation where available), not as a reconstructed proto-language. The question of whether a given feature is retention or shared innovation is not prioritized at this stage.

**Celtic's role.** Proto-Celtic confirms inherited morphology at the older/common level but is deprioritized as a structural model due to the comparative messiness of its later verbal system. It is a witness, not a template.

---

## TSV Column Schema

Three columns in `lexicon.tsv` classify verbs. The first two are existing; the third is new.

### `verb_thematicity` (col 12)

| Value | Meaning |
|---|---|
| `athematic` | Endings attach directly to stem (no thematic vowel) |
| `thematic` | Stem includes thematic vowel \*-e/o- before endings |
| *(blank)* | Non-verb entry |

### `verb_stem_type` (col 13)

Single column covering all three stem domains (present, aorist, perfect). Domain is inferred from context: citation-form entries are present stems; aorist entries like *dṓt* are identified by gloss and entry structure.

**Present stems (imperfective):**

| Value | Ringe category | Thematicity | Typical ablaut |
|---|---|---|---|
| `root` | Root present (ath.) / simple thematic present (th.) | either | e or ē |
| `Ce-reduplicated` | Ce-reduplicated present | athematic | e or zero |
| `Ci-reduplicated` | Ci-reduplicated present | either | zero |
| `nasal-infix` | Nasal-infixed present (\*-né-/\*-n-) | athematic | zero |
| `*-néw-/-nu-` | nu-present (\*-néw-/\*-nu-) | athematic | zero |
| `*-ye/o-` | \*-yé/ó- and \*-ye/o- presents | thematic | e or zero |
| `*-éye/o-` | Causative-iterative in \*-éye/o- | thematic | o |
| `*-ské/ó-` | Iterative/imperfective in \*-ské/ó- | thematic | zero |
| `*-se/o-` | Desiderative in \*-se/o- | thematic | e |
| `*-éh₁-` | Stative in \*-éh₁- | athematic | zero |
| `*-h₂-` | Factitive in \*-h₂- | athematic | — |

**Notes on `root`:** Unified label for affixless presents regardless of thematicity. An athematic root present (*ésti*) and a simple thematic present (*tékseti*) both get `root`. `verb_thematicity` disambiguates. This keeps the value set small and dictionary extraction simple.

**Notes on `*-ye/o-` accent split:** Ringe distinguishes root-accented \*-ye/o- (e-grade root: *kléieti, sēieti*) from suffix-accented \*-yé/ó- (zero-grade root: *βarkiéti, kapiéti, mariétor*). Both are `*-ye/o-` in `verb_stem_type`. The accent/ablaut difference is visible in the preform and surface form and does not need a separate column.

**Aorist stems (perfective):**

| Value | Ringe category | Thematicity | Typical ablaut |
|---|---|---|---|
| `root` | Root aorist | athematic | e or zero |
| `s-aorist` | Sigmatic aorist | athematic | ē or e |
| `thematic` | Simple thematic aorist | thematic | zero |
| `Ci-reduplicated` | Reduplicated thematic aorist | thematic | zero |

**Perfect stems (stative):**

| Value | Ringe category | Typical ablaut |
|---|---|---|
| `root` | Root perfect | o ~ zero |
| `reduplicated` | Reduplicated perfect | o ~ zero |

Currently only *dṓt* (root aorist) is attested outside the present. Aorist/perfect system design is deferred; values are reserved.

### `verb_derivation` (col 75, new — append at end)

Blank for basic (primary) verbs. Populated only when the verb is synchronically derived from another verb or nominal in the lexicon.

| Value | Meaning | Typical formation |
|---|---|---|
| `causative` | Derived causative ("make X happen") | \*-éye/o- with o-grade root |
| `iterative` | Derived iterative ("do X repeatedly") | \*-éye/o- with o-grade root |
| `factitive` | Derived factitive from adjective ("make X-adj") | \*-éye/o- or \*-h₂- |
| `denominative` | Derived from nominal | \*-ye/o- |
| `desiderative` | Derived desiderative ("want to X") | \*-se/o- or \*-sye/o- |
| `stative` | Derived stative ("be in state X") | \*-éh₁- |
| *(blank)* | Basic/primary verb, or non-verb |

When `verb_derivation` is populated, the base verb or nominal should appear in `cross_references`.

**Causative vs. iterative:** Both use \*-éye/o-. The distinction is semantic and root-specific, not morphological. Default to `causative` unless iterative semantics are clear from the gloss.

---

## Present Stem Classes — Architectural Notes

The following prose sections expand on the value table above with notes on productivity, typological behavior, and open design questions. The value table in §TSV Column Schema is authoritative for classification; this section is commentary.

### Root presents (`root`)

The broad default class. Thematic root presents are the most populous class and the one into which new formations are most likely to be drawn by analogy. Not a single semantically uniform category — includes statives, activities, punctuals, and other Aktionsart types depending on the root. Defined morphologically, not semantically.

Athematic root presents are a small, closed set of high-frequency verbs that retain athematic inflection. These are lexical relics, not a productive class. Every branch of WIE (and NWIE) preserves a residue of athematic verbs rather than leveling everything into thematic conjugations. The canonical members include 'be', 'give', 'carry', 'go', and a handful of others. These verbs are expected to show irregular or suppletive behavior and to resist analogical pressure.

### \*-ye/o- presents (`*-ye/o-`)

A distinct thematic formation. Well attested across WIE: Proto-Germanic weak presents, Proto-Italic present-stem classes, Proto-Celtic \*-ye/o- presents, and Proto-Balto-Slavic class morphology all continue this formation.

Semantic tendencies (root-specific, not system-wide): causative/transitivizing (the strongest and most widespread tendency), atelic/non-directed/distributive/iterative (attested in some roots or branches). These tendencies are real but not grammaticalized into a rule. A \*-ye/o- present may be causative for one root and iterative for another; the formation carries a family resemblance, not a uniform function.

### \*-éye/o- causative-iteratives (`*-éye/o-`)

Distinct from \*-ye/o- presents — a dedicated causative/factitive formation with o-grade root. Seven attested in the lexicon: *moldéieti, moréieti, nokéieti, sodéieti, voléieti, rogéieti, ðoɣvéieti*. All are transparently derived from base verbs and take `verb_derivation: causative`. The pattern is productive enough to warrant treatment as a live derivational class, not a handful of lexicalized fossils.

### Nasal presents (`nasal-infix`, `*-néw-/-nu-`)

An inherited mixed class characterized by a nasal element in the present stem. Two formation types are attested:

**Nasal-infix presents** (`nasal-infix`) — root with infix \*-né-/\*-n-, athematic endings. PIE pattern: \*li-né-kʷ-ti. Four attested: *iunékti, kalnéiti, ganṓti, talnā́ti*.

**Nu-presents** (`*-néw-/-nu-`) — suffix \*-néw-/\*-nu-, athematic endings. One attested: *kalnéuti*.

🔲 **Open question:** Are both subtypes living (if small) classes in Ghandwa, or is the athematic type already fossilizing? The athematic type is archaic across all branches, but it is *preserved* across all of them too, at least residually. Decision deferred — needs more data.

### Reduplicated presents (`Ce-reduplicated`, `Ci-reduplicated`)

Two reduplication patterns distinguished by the reduplicant vowel:

**Ce-reduplicated** — \*Ce- reduplicant, typically athematic. One attested: *dídōti* (\*dé-deh₃-ti).

**Ci-reduplicated** — \*Ci- reduplicant, typically thematic. Two attested: *píboti* (\*pi-ph₃-é-ti), *sízdeti* (\*si-sd-e/o-ti).

---

## Broader System Architecture

Beyond the present stem classes, the following categories are established as part of Ghandwa's verbal system based on WIE (and where noted, NWIE) overlap:

### Established categories

**Finite person-number inflection.** Verbs inflect for person (1st, 2nd, 3rd) and number (singular, plural). Dual is not posited — it is a PIE archaism not robustly shared across WIE as a productive verbal category.

**Present / non-past indicative.** The central finite category. The repository of the present stem classes described above.

**Imperative.** A normal finite category, not marginal. Present imperative at minimum; further imperative types (e.g. future imperative) are deferred.

**At least one non-indicative mood.** All branches preserve modal morphology of some kind (subjunctive, optative, or material derived from them). The specific inventory and morphology of Ghandwa's moods are deferred for a dedicated session — what is established is that the system is not indicative-only.

**A marked past / preterite category.** All branches have a distinct past-tense formation, but they do not build it the same way (Germanic preterite ≠ Italic perfect ≠ Celtic syncretic preterite ≠ Slavic aorist). What is safe: Ghandwa has a morphologically marked past. What is not yet decided: how it is formed.

**Stem classes matter.** The verbal system is not flat. Multiple present-stem classes coexist (as detailed above), and the system resists reduction to a single conjugation pattern.

**Derived verbal stems with semantic load.** Formations involving \*-ye/o- and \*-éye/o- carry derivational semantics (causative, factitive, iterative) and are not merely inflectional variants. Tracked in `verb_derivation`.

**Infinitive or verbal noun.** At least one non-finite form functioning as a verbal noun / infinitive. All branches are comfortable with this category. Specific morphology deferred.

**Participles.** A regular part of the verbal system. Two participles are especially well supported across branches: present active participle (\*-ont-/\*-nt-) attested in Italic, Germanic, and Balto-Slavic; past/resultative participle (\*-to-) attested across all four branches as a past participial adjective.

### Deferred categories

The following are explicitly placed outside the initial system and reserved for later sessions:

- **Subjunctive / optative specifics** — mood morphology and distribution
- **Productive middle voice** — the old middle is not the main engine of the system in any of WIE; Ghandwa's voice system is fundamentally active, with middle/passive as at most residual or secondary
- **Future tense** — no shared future formation across WIE
- **Specific past/preterite morphology** — "there is a past" is established; "how it is built" is not
- **Branch-specific hallmarks** — Italic \*-r passive, Germanic dental weak preterite, Celtic absolute/conjunct, Slavic obligatory aspect pairing: none of these are part of the Ghandwa base layer

---

## Ringe 2017 Reference Mapping

Full inventory from Ringe ch. 2, §2.1.3.2, showing which PIE formations map to which `verb_stem_type` value. Categories not yet attested in Ghandwa are included for completeness.

### Present (imperfective) stems

**Basic presents:**

| Ringe type | PIE pattern | → `verb_stem_type` | → `verb_thematicity` |
|---|---|---|---|
| Athematic root present | \*CéC-ti ~ \*CC-énti | `root` | `athematic` |
| Ce-reduplicated athematic | \*Cé-CeC-ti ~ \*Cé-CC-enti | `Ce-reduplicated` | `athematic` |
| Ci-reduplicated athematic | \*Cí-CeC-ti ~ \*Cí-CC-enti | `Ci-reduplicated` | `athematic` |
| Nasal-infixed | \*C-né-C-ti ~ \*C-n-C-énti | `nasal-infix` | `athematic` |
| nu-present | \*C-néw-ti ~ \*C-nu-énti | `*-néw-/-nu-` | `athematic` |
| Simple thematic present | \*CéC-e/o-ti | `root` | `thematic` |
| Ci-reduplicated thematic | \*Cí-CC-e/o-ti | `Ci-reduplicated` | `thematic` |
| \*-ské/ó- present | \*CC-ské/ó-ti | `*-ské/ó-` | `thematic` |
| \*-yé/ó- present (suffix-acc.) | \*CC-yé/ó-ti | `*-ye/o-` | `thematic` |
| \*-ye/o- present (root-acc.) | \*CéC-ye/o-ti | `*-ye/o-` | `thematic` |
| \*-se/o- present | \*CéC-se/o-ti | `*-se/o-` | `thematic` |

**Derived presents:**

| Ringe type | PIE pattern | → `verb_stem_type` | → `verb_derivation` |
|---|---|---|---|
| Stative in \*-éh₁- | \*CC-éh₁-ti | `*-éh₁-` | `stative` |
| Factitive in \*-h₂- | \*CéCo-h₂-ti | `*-h₂-` | `factitive` |
| Causative-iterative | \*CoC-éye/o-ti | `*-éye/o-` | `causative` or `iterative` |
| Denominative in \*-yé/ó- | \*CéCos-yé/ó-ti | `*-ye/o-` | `denominative` |
| Desiderative in \*-se/o- | \*CéC-se/o-ti | `*-se/o-` | `desiderative` |
| Factitive in \*-yé/ó- | \*CéCero-yé/ó-ti | `*-ye/o-` | `factitive` |

### Aorist (perfective) stems

| Ringe type | PIE pattern | → `verb_stem_type` | → `verb_thematicity` |
|---|---|---|---|
| Root aorist | \*CéC- ~ \*CC- | `root` | `athematic` |
| s-aorist | \*CēC-s- ~ \*CéC-s- | `s-aorist` | `athematic` |
| Simple thematic aorist | \*CC-é/ó- | `thematic` | `thematic` |
| Ci-reduplicated thematic | \*Cé-CC-e/o- | `Ci-reduplicated` | `thematic` |

### Perfect (stative) stems

| Ringe type | PIE pattern | → `verb_stem_type` |
|---|---|---|
| Root perfect | \*CóC- ~ \*CC- | `root` |
| Reduplicated perfect | \*Ce-CóC- ~ \*Ce-CC- | `reduplicated` |

---

## Lexicon Verb Inventory

As of 2026-03-24: 94 verb entries in the TSV. 49 have `verb_thematicity` + `verb_stem_type` populated; 45 are blank in both. The inventory below covers the 49 classified verbs, organized by `verb_stem_type` using the new normalized labels. See §Pending Reclassifications for the edits needed to bring the TSV in line with this schema.

### `root` — athematic

| Citation form | Gloss | Preform |
|---|---|---|
| *ésti* ~ *sénti* | is | \*h₁ésti |
| *éiti* ~ *iénti* | go | \*h₁éyti |
| *déukti* | lead | — |
| *vḗsti* | graze, consume | — |
| *ðḗti* ~ *ðánti* | put, place; dedicate | \*dʰéh₁ti |
| *βérti* ~ *βarénti* | carry | \*bʰérti |
| *stā́ti* ~ *stā́nti* | stand | \*stéh₂ti |
| *vélti* ~ *valénti* | want, wish | \*wélh₁ti |
| *βā́ti* | pronounce, declare | \*bʰéh₂ti |

### `root` — thematic

| Citation form | Gloss | Preform |
|---|---|---|
| *édeti* ~ *édonti* | eat | \*h₁édeti |
| *gvémeti* ~ *gvémonti* | come; step | \*gʷémeti |
| *gvéteti* | say, speak | \*gʷéteti |
| *kléveti* | hear, listen | \*ḱléweti |
| *kéleti* | hide, conceal | \*ḱéleti |
| *légeti* | gather, collect | \*léǵeti |
| *méldeti* ~ *méldonti* | melt, smelt | \*(s)méldeti |
| *plékteti* | plait, weave | \*pléḱteti |
| *skéleti* ~ *skélonti* | split, cleave | \*skélHeti |
| *svépeti* | sleep | — |
| *sékveti* ~ *sékvonti* | follow | \*sékʷeti |
| *sékvetor* | be following | — |
| *tékseti* ~ *téksonti* | weave, craft | \*téḱseti |
| *véideti* ~ *véidonti* | see; know | \*wéydeti |
| *ðéɣveti* | burn, blaze | \*dʰégʷʰeti |
| *ɣvéneti* | strike, beat | \*gʷʰéneti |
| *βúeti* ~ *βúonti* | become; be | \*bʰúHeti |
| *régeti* ~ *régonti* | guide, set upright | \*h₃réǵeti |

### `Ce-reduplicated` — athematic

| Citation form | Gloss | Preform |
|---|---|---|
| *dídōti* | give | \*dé-deh₃-ti |

### `Ci-reduplicated` — thematic

| Citation form | Gloss | Preform |
|---|---|---|
| *píboti* ~ *píbonti* | drink | \*pi-ph₃-é-ti |
| *sízdeti* | be sitting | \*si-sd-e/o-ti |

### `nasal-infix` — athematic

| Citation form | Gloss | Preform |
|---|---|---|
| *iunékti* | join, yoke | \*yu-né-g-ti |
| *kalnéiti* | lean, incline | \*kl̥-né-y-ti |
| *ganṓti* | know, recognize | \*ǵn̥-né-h₃-ti |
| *talnā́ti* | bear, lift, endure | \*tl̥-né-h₂-ti |

### `*-néw-/-nu-` — athematic

| Citation form | Gloss | Preform |
|---|---|---|
| *kalnéuti* | hearken, attend | \*ḱl̥-néw-ti |

### `*-ye/o-` — thematic

| Citation form | Gloss | Preform |
|---|---|---|
| *βarkiéti* ~ *βarkiónti* | cram, crowd | \*bʰr̥kʷ-yé-ti |
| *kapiéti* ~ *kapiónti* | take, seize | \*kap-yé-ti |
| *mariétor* ~ *marióntor* | die (middle/deponent) | \*mr̥-yé-tor |
| *kléieti* ~ *kléionti* | lean, incline | \*ḱléy-ye/o-ti |
| *sēieti* ~ *sēionti* | sow | \*séh₁-ye/o-ti |
| *skélieti* ~ *skélionti* | split, cleave | \*skélH-ye/o-ti |

### `*-éye/o-` — thematic

All take `verb_derivation: causative`.

| Citation form | Gloss | Preform | Base verb |
|---|---|---|---|
| *moldéieti* ~ *moldéionti* | melt (cause to) | \*(s)mold-éye-ti | *méldeti* |
| *moréieti* ~ *moréionti* | kill (make die) | \*mor-éye-ti | *mariétor* |
| *nokéieti* ~ *nokéionti* | kill (make disappear) | \*noḱ-éye-ti | *(base not in lexicon)* |
| *sodéieti* | seat, cause to sit | \*sod-éye-ti | *sízdeti* |
| *voléieti* | choose, cause to want | \*wol-h₁-éye-ti | *vélti* |
| *rogéieti* | straighten, make straight | \*h₃roǵ-éye-ti | *régeti* |
| *ðoɣvéieti* | kindle, set on fire | \*dʰogʷʰ-éye-ti | *ðéɣveti* |

### `root` — athematic (aorist)

| Citation form | Gloss | Preform |
|---|---|---|
| *dṓt* | gave | \*déh₃-t |

---

## Open Questions

🔲 **Nasal present split.** Are athematic nasal presents a living (if small) class, or already fossils? Four nasal-infix presents now attested (*iunékti, kalnéiti, ganṓti, talnā́ti*) plus one nu-present (*kalnéuti*). Still not enough data to decide on productivity.

🔲 **Past/preterite formation.** Morphology entirely unspecified. Needs its own session — the question is large and consequential for the whole system.

🔲 **Mood inventory.** At least one non-indicative mood exists. Which one(s), and with what morphology?

🔲 **Infinitive/verbal noun morphology.** Category is established; form is not.

🔲 **Middle/passive residue.** How much of the old middle survives, if any? *mariétor* (die, \*mr̥yétor) is the first and so far only verb with medio-passive morphology. Its partner *moréieti* (kill/make die) gives a clean active/middle pair. Open: is *mariétor* a lonely fossil, or are there more candidates?

🔲 **Sievers' Law.** Glide alternations (\*-ye/o- ~ \*-iye/o-) conditioned by syllable weight of the preceding syllable will affect the surface forms of \*-ye/o- presents. *βarkiéti* (313, \*bʰr̥kʷyéti) is a test case — the \*-ye/o- suffix appears after a heavy syllable.

🔲 **Verb citation forms in lexicon.** Convention is 3sg present active indicative. Once paradigms exist, the lexicon will need a verbal entry format (parallel to the nom ~ gen format for nouns). Design pending.

🔲 **Transformer support.** The phonological transformer currently handles nom ~ gen noun pairs. Verbal forms will need to be runnable through the transformer. Whether this requires a new input mode or just feeding individual forms through the existing single-form mode is TBD.

---

## Pending Reclassifications

**Status:** Action items for Apple Numbers. Remove this section after edits are applied.

### Label normalizations (31 entries)

Value changes only — the old and new labels describe the same formation.

| Current `verb_stem_type` | New `verb_stem_type` | Entries |
|---|---|---|
| `simple thematic present` | `root` | *édeti, gvémeti, gvéteti, kléveti, kéleti, légeti, méldeti, plékteti, skéleti, svépeti, sékveti, sékvetor, tékseti, véideti, ðéɣveti, ɣvéneti, βúeti* (17) |
| `root present` | `root` | *ésti, éiti, déukti, vḗsti, ðḗti, βérti, stā́ti, vélti, βā́ti, régeti* (10) |
| `reduplicated present` | `Ce-reduplicated` | *dídōti* (1) |
| `reduplicated thematic present` | `Ci-reduplicated` | *píboti, sízdeti* (2) |
| `*-nu- / -neu-* present` | `*-néw-/-nu-` | *kalnéuti* (1) |

### True reclassifications (4 entries)

| Entry | Current | New `verb_stem_type` | New `verb_derivation` | Reason |
|---|---|---|---|---|
| *ganṓti* | `root present` | `nasal-infix` | *(blank)* | PIE \*ǵn̥-né-h₃-ti; confirmed nasal infix |
| *talnā́ti* | `root present` | `nasal-infix` | *(blank)* | PIE \*tl̥-né-h₂-ti; confirmed nasal infix |
| *rogéieti* | `causative` | `*-éye/o-` | `causative` | Formation is \*-éye/o-; function moves to `verb_derivation` |
| *skélieti* | `simple thematic present` | `*-ye/o-` | *(blank)* | Surface -ieti; coexists with *skéleti* (the root present) |

### New `verb_derivation` values (7 entries)

No `verb_stem_type` change — only adding the new column value.

| Entry | `verb_derivation` | Base verb |
|---|---|---|
| *moldéieti* | `causative` | *méldeti* |
| *moréieti* | `causative` | *mariétor* |
| *nokéieti* | `causative` | *(base \*neḱ- verb not in lexicon)* |
| *sodéieti* | `causative` | *sízdeti* |
| *voléieti* | `causative` | *vélti* |
| *ðoɣvéieti* | `causative` | *ðéɣveti* |
| *rogéieti* | `causative` | *régeti* |

**Note:** *rogéieti* appears in both the reclassification and new-derivation tables because it needs both a `verb_stem_type` change (causative → \*-éye/o-) and a `verb_derivation` fill.

**Gap flagged:** *nokéieti* has `verb_derivation: causative` but its base verb (a basic \*neḱ- root present) is not yet in the lexicon.

---

## Dictionary Extraction Notes

A verb's classification string for dictionary-making is assembled from the three columns:

    {verb_thematicity} {verb_stem_type} {verb_derivation}

Examples:

| Entry | Columns | Dictionary string |
|---|---|---|
| *tékseti* | `thematic` `root` | thematic root present |
| *ésti* | `athematic` `root` | athematic root present |
| *iunékti* | `athematic` `nasal-infix` | athematic nasal-infix present |
| *moréieti* | `thematic` `*-éye/o-` `causative` | thematic causative in \*-éye/o- |
| *dídōti* | `athematic` `Ce-reduplicated` | athematic Ce-reduplicated present |
| *dṓt* | `athematic` `root` | root aorist |

The `verb_derivation` value, when present, carries the semantic function label that a dictionary entry needs. The `verb_stem_type` value carries the morphological formation. Together they give a complete classification without needing to look anything up.

---

## Methodology Notes

These notes record the reasoning behind the design framework and are preserved for continuity across sessions.

The goal is not to reconstruct a single proto-language or to prove a shared clade among the western/northern IE branches. Similarities among WIE (and NWIE) are treated as overlap from late dialect-continuum inheritance, useful as design material regardless of their historical explanation.

The present active indicative of Italic, Celtic, and Germanic looks very similar, especially in the simple thematic present. This similarity is treated as useful common material without requiring a verdict on retention vs. innovation.

The task was deliberately narrowed: enumerate common features first, then design the system. The inventory above is the enumeration; paradigm-building is the next phase.
