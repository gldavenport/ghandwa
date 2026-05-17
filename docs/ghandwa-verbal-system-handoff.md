# Ghandwa Verbal System Handoff

Date: 2026-05-16  
Scope: notes extracted from the current chat on using Italic–Germanic overlap as the core model for Ghandwa verbal grammar.

## Governing design decision

Ghandwa verbal grammar should be built from **features shared by Italic and Germanic**, regardless of whether the shared material is inherited, innovative, areal, or conservative.

The operative filter is:

> Is this feature plausibly present in both Italic and Germanic?

Not:

> Is this feature a diagnostic shared innovation?

This matters because Ghandwa is being modeled as a **shallow post-PIE / early Western Indo-European layer**, closer to something like pre-Italic / pre-Germanic / early WIE than to a fully differentiated daughter language.

## Current verbal-system profile

The emerging Ghandwa verbal system should have:

| Domain | Current working choice |
|---|---|
| Present system | Conservative PIE-like present system |
| Default finite class | Thematic root presents |
| Citation form | Usually 3sg present active |
| Productive derived presents | *-ye/o-* and *-éye/o-* |
| Archaic/relic class | Athematic/root presents, mostly high-frequency verbs |
| Nasal presents | Present, but limited and classifiable |
| Reduplicated presents | Relic/high-frequency class |
| Middle/deponent | Present but secondary, not central |
| Past system | Not yet settled; likely simplified preterite zone |
| Participles | Active *-nt-* and result/passive *-to-* |
| Verbal nouns | *-tu-*, *-ti-*, *-men-* |
| Preverbs | Productive, but not Old Irish-style structurally dominant |

## Thematic root present

The Ghandwa thematic root present is the inherited *-e/o-* type.

Current Old Ghandwa present indicative active endings:

| Person | Ending |
|---|---|
| 1sg | *-ō* |
| 2sg | *-ezi* |
| 3sg | *-eti* |
| 1pl | *-omos* |
| 2pl | *-ete* |
| 3pl | *-onti* |

Useful shorthand:

> The thematic root present is the **-e- / -on- pattern**.

Example:

| Person | Example |
|---|---|
| 3sg | *légeti* |
| 3pl | *légonti* |

This is compatible with the Italic–Germanic standard because it preserves the transparent thematic architecture that later daughters can reduce, level, or remodel.

## Derived *-ye/o-* and *-éye/o-* verbs

The chat settled that *-ye/o-* and *-éye/o-* verbs should **not** be treated only as inherited debris. Italic and Germanic both support keeping the pattern alive as a productive or semi-productive derivational mechanism.

Working rule:

> Ghandwa preserves inherited *-ye/o-* and *-éye/o-* present formations and continues to use them productively to derive secondary verbs, especially causatives, factitives, transitives, denominatives, and some iterative/intensive verbs.

### Functional split

| Type | Shape | Function | Ghandwa status |
|---|---|---|---|
| Simple thematic | root + *-e/o-* | Basic action/state | default |
| Plain *-ye/o-* | root/stem + *-ye/o-* | denominative, inchoative, present-forming | productive/semi-productive |
| Accented *-éye/o-* | often o-grade/root + *-éye/o-* | causative, factitive, iterative | productive |
| Later Germanic target | *jan*-type verbs | weak/derived/transitive | daughter-language development |
| Later Italic target | factitives/remodeled classes | make/cause/become | daughter-language development |

### Examples discussed

| Base / inherited verb | Derived verb | Meaning contrast |
|---|---|---|
| *sedeti* | *sodéieti* | “sits” vs. “sets, seats” |
| *stā́ti* | *stādéieti* or similar | “stands” vs. “sets upright” |
| *legeti* | *logéieti* | “gathers/speaks” vs. “causes to gather, collects” |
| *éiti* | *oyéieti* | “goes” vs. “sends, causes to go” |

Important caution:

> Do not make every derived verb *-éieti*. Ghandwa should preserve a mix of inherited and newly derived verbs.

## Inherited vs. Ghandwa-derived verbs

A useful lexical distinction should be added:

| Type | Source | Expected feel |
|---|---|---|
| inherited verb | PIE/root-level verb continued into Ghandwa | older, basic, sometimes irregular |
| Ghandwa-derived verb | built inside Ghandwa using living morphology | transparent, regular, often transitive/causative/specialized |

Likely contrasts:

| Domain | Inherited verb | Ghandwa-derived verb |
|---|---|---|
| Morphology | root present, nasal present, reduplicated, athematic, etc. | usually regular thematic or *-ye/o-*, *-éye/o-* |
| Semantics | basic action/state | causative, factitive, denominative, iterative |
| Regularity | more likely irregular or ablauting | more likely regular |
| Register | core/basic vocabulary | productive, technical, administrative, or transparent |
| Daughter outcomes | can diverge unpredictably | likely regularized as weak/derived verbs |

Suggested fields:

```tsv
verb_derivation_origin = inherited | ghandwa-derived | uncertain
verb_derivation_type = root-present | thematic | nasal-present | causative-éye | denominative-ye | relic-athematic
```

## Celtic comparison

Celtic is relevant as WIE context but should not dictate the Ghandwa verbal core.

Celtic is similar in preserving:
- thematic presents
- old present stem classes
- *-nt-* participles
- *-to-* participles
- verbal nouns
- preverbs

But Celtic differs by developing:
- a much stronger r-mediopassive / deponent system
- heavy preverb restructuring
- absolute vs. conjunct verbal endings
- central verbal-noun syntax
- later initial-mutation-triggering verbal particles

Ghandwa should therefore use Celtic mostly as a comparison layer, while the verbal core is set by Italic–Germanic overlap.

## Current compliance of the lexicon

The uploaded `lexicon-core.tsv` appears mostly compliant with the nascent Italic–Germanic verbal standard.

The lexicon already contains about **95 verb entries** and shows useful clusters:

| Present class | Examples noted |
|---|---|
| thematic root presents | *léigeti*, *ðéɣveti*, *wérteti*, *káneti*, *légeti*, *ɣvéneti* |
| *-ye/o-* presents | *βarkiéti*, *rogéieti*, *moldéieti*, *sodéieti*, *voléieti* |
| nasal presents | *ganṓti* |
| reduplicated presents | *dídōti*, *píboti* |
| root aorist/relic past material | *dṓt* |
| mediopassive/deponent-looking material | *sékvetor* |

Assessment:

> The lexicon is not structurally noncompliant. Its problems are mostly standardization and metadata gaps.

## Where the lexicon/system is lacking

Main gaps identified in the chat:

| Gap | Current state | Why it matters |
|---|---|---|
| 30 verb stubs | gloss only; no lemma/preform/class/IPA | cannot test the verbal system |
| no past-system field | only *dṓt* is explicitly past-like | preterite strategy not defined |
| no person/number paradigm field | lemmas are mostly 3sg citation forms | need predictable inflection generation |
| no voice-behavior field | middle/deponent forms exist but are not systematized | need active vs. middle/deponent distinction |
| no ablaut field | root/nasal/reduplicated classes exist but ablaut is not controlled | needed for relic/strong verbs |
| no productivity/status field | verb classes exist but are not marked productive/relic/fossilized | needed for diachronic modeling |
| causatives marked unevenly | *-éye/o-* verbs exist but other derivations are not labeled consistently | need cleaner derivational metadata |
| no conjugation class ID | `verb_stem_type` exists but not a script-friendly paradigm ID | needed for transformer/pipeline work |
| no regularity flag | archaic/irregular forms are not flagged | needed for generation and auditing |

Minimum proposed columns:

```tsv
verb_class_id
verb_present_class
verb_past_formation
verb_voice_behavior
verb_ablaut_type
verb_productivity
verb_regular_status
```

Additional useful columns:

```tsv
verb_derivation_origin
verb_derivation_type
```

## Past system: main unresolved issue

The biggest substantive open question is the **preterite/past system**.

Current direction:

> Ghandwa should probably have a simplified preterite zone absorbing older aorist and perfect functions, while preserving a few archaic reduplicated or stative perfect-like relics in common verbs.

Open decisions:

1. Should Ghandwa have one generalized preterite, or multiple inherited past formations?
2. Should a dental preterite already exist at the Ghandwa level, or should it be left for daughters?
3. How many reduplicated/stative perfects should be preserved?
4. Should *dṓt* “gave” represent a productive class, a relic aorist, or a fossilized irregular?
5. Should past stems be generated from roots by ablaut, by suffix, or by suppletion/lexical listing?
6. Should Ghandwa preserve any semantic split between old perfect/stative and eventive past?

Recommended conservative answer for now:

- one broad **preterite** category
- a few relic irregular/reduplicated/stative forms
- no fully Germanic-style weak dental preterite as the default at the Ghandwa layer unless later explicitly chosen
- allow daughter languages to develop stronger dental/weak preterite systems independently

## Middle/deponent policy

Forms like *sékvetor* and *mariétor* are compatible with conservative Indo-European material, but the Italic–Germanic core should not make middle/deponent voice central.

Working policy:

> Middle/deponent verbs are allowed as conservative relics or lexicalized classes, but default verbal behavior is active thematic.

Needed metadata:

```tsv
verb_voice_behavior = active | middle | deponent | active-middle | uncertain
```

## Athematic policy

Athematic presents should exist, but not become the default.

Working policy:

> Keep athematic/root presents mainly for old, high-frequency verbs.

Possible core athematic/relic verbs to preserve:
- “be”
- “go”
- “give”
- “stand”
- “put/do”
- “know”
- maybe “eat/drink” depending on lexical evidence

Open issue:

> Some current 3sg forms may look too athematic if overextended. Review non-basic athematics and convert or mark them as relics.

## Nasal-present policy

Nasal presents are acceptable but need clearer subclassing.

Current issue:

> The lexicon has nasal-like verbs, but their patterns differ and are not consistently classified.

Needed distinctions:

```tsv
nasal-infix
nasal-suffix
*-néw-/*-nu-
nasal-remodeled
```

Examples noted:
- *ganṓti*
- *talnā́ti*
- *iunékti*
- *kalnéiti*

## Lexicon stub-fill pass

A first-pass table was generated for the 30 blank verb lemmas:

- `lexicon-core-verb-stub-fill-candidates.md`
- `lexicon-core-verb-stub-fill-candidates.tsv`

Results:

| Status | Count |
|---|---:|
| fillable candidate | 26 |
| possible but verify | 3 |
| leave blank/planned | 1 |

The one recommended to leave blank/planned for now:

- “to play”

Best immediate fill candidates from that pass:

| Gloss | Suggested Ghandwa |
|---|---|
| sit | *sédeti* |
| cut | *séketi* |
| dig | *βéðeti* |
| float | *pléweti* |
| flow | *sréweti* |
| hold | *séɣeti* |
| pull | *sélketi* |
| vomit | *wḗmeti* |
| wash | *lowéieti* |

Important note:

> These were suggestions, not canonized lexicon edits.

## Suggested next workflow

1. Add verbal metadata fields to the lexicon.
2. Classify all existing non-stub verbs by present class, voice behavior, productivity, and regularity.
3. Apply the 26 high/medium-confidence stub fills only after review.
4. Leave “to play” blank/planned unless a better inherited or culturally marked source is chosen.
5. Define the Ghandwa preterite before adding many past forms.
6. Build 6–10 model paradigms:
   - thematic “carry/bear”
   - thematic “sit”
   - athematic “be”
   - athematic/reduplicated “give”
   - nasal-present verb
   - *-ye/o-* denominative/inchoative
   - *-éye/o-* causative
   - middle/deponent relic
   - “go”
   - “stand”

## Working statement for the grammar

Ghandwa uses Italic–Germanic agreement to define the default finite verbal core: thematic presents with conservative primary endings, residual athematic presents for high-frequency inherited verbs, productive *-ye/o-* and *-éye/o-* presents, limited nasal presents, relic reduplicated presents, and a non-central middle/deponent category. The past system remains to be standardized.
