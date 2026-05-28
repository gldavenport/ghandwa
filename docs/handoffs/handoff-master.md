# Master Handoff

**Consolidated:** 2026-05-23
**Sources:** `handoff-verbal-system.md`, `handoff-verb-paradigms.md`, `handoff-lexicon-content.md`, `handoff-catch-all.md`, `ghandwa-syntax-handoff.md`, `handoff-syntax-benchmark.md`, `handoff-paradigms-db.md`, `handoff-transformer-cleanup.md`, `handoff-dangwa-reconcile.md`

Sections are ordered by dependency: verbal system decisions inform verb paradigm work; lexicon gaps block syntax benchmarks; syntax decisions depend on vocabulary; paradigm DB population depends on paradigm content; transformer and reconcile work are independent.

---

## §1 — Verbal System

### §1.1 — Decisions from Session A

**Source:** `handoff-verbal-system.md`
**Output file:** `grammar/verbal-system.md` (v0.5, 309 lines)
**Status:** §8 substantively closed; two TBD present forms remain as lexicon tasks, not blocking.

#### Governing design principle

The Ghandwa verbal system is built from **Italic–Germanic consensus**, used as a positive inclusion heuristic — not a blanket rule. Italic–Germanic agreement is strong evidence for adoption; it does not automatically include shared losses or reductions. Where branches diverge, decisions are made case by case and documented in the Design Notes section of `verbal-system.md`.

#### Verb classification

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

#### Present system

- Thematic root present paradigm fully established (*légō*, *légezi*, *légeti*, *légomos*, *légete*, *légonti*)
- Intervocalic *\*s > z* established as regular sound change (Germanic-sourced); produces 2sg *-ezi*, *-zi* (athematic)
- Athematic 3pl resolved: *\*h₁snti* → *santi* by CHC > CaC or CaRC convergence; same pattern across all athematics (*yanti*, *danti*, *stanti*). **Transformer does not yet handle this correctly; hand-derive.**
- Nasal presents: two active subclasses — `nasal-infix` (attested ×4: *ganṓti*, *talnā́ti*, *iunékti*, *kalnéiti*) and `nasal-suffix` (supported, unattested, deferred to verb generator). *-néw/nu-* type dropped for insufficient WIE support. Laryngeal coloring within `nasal-infix` is phonological, not morphological.
- Reduplicated presents: relic class; confirmed *dídōti* 'give', *píboti* 'drink'

#### Mood system

- **Subjunctive:** long-vowel thematic (*-ō/ē-*) + primary endings; athematic verbs thematize (*esēti*, *eyēti*, *dōēti*, *stāēti*). Long-vowel hiatus sequences (*dōēti*, *stāēti*) not contracted at Ghandwa level — left to daughters
- **Optative:** *-oy-* + secondary endings
- **Imperative:** 2sg bare stem, 3sg *-etōd*, 2pl *-ete* (syncretic), 3pl *-ontōd*; long imperative type following Italic

#### Non-finites

- Infinitive: accusative of *-tu-* stem → suffix *-tum* (Italic-parallel)
- Active participle: *-ont-*
- Passive/result participle: *-to-*
- Verbal nouns: *-tum*, *-ti-*, *-men-*

#### Middle/mediopassive

Italic-type *-r* endings; relic category. 2pl/3sg syncretic (*-etor*); inherited, not corrected. Full paradigm in `verbal-system.md` §4.

#### Past system

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

**Decision by Gary:** Ghandwa should inherit all PIE reduplicated preterites that appear in both Proto-Italic and Proto-Germanic. Flag for action the next time this section is reviewed.

#### Still open (verbal system)

**Minor / lexicon tasks (not blocking):**
- 'Do/put' and 'carry' need present forms established in the lexicon before their reduplicated preterite rows are complete
- `nasal-suffix` subclass has no lexicon attestation; deferred to verb generator session

**Substantive agenda for future sessions:**

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

### §1.2 — Verb Evaluation & Paradigm Work Order

**Source:** `handoff-verb-paradigms.md`
**Scope:** Two-part verb session. Priority 0: evaluate and derive four stub verbs that have glosses but no lemma. Priority 1–4: fill missing paradigms in `docs/grammar/ch4-ghandwa/verbs-worksheet.md` for the 20+ verbs that already have lemmas.

**Context:** The lexicon (NocoDB) has ~95+ verb entries. `verbs-worksheet.md` currently has full paradigms for only 6 verbs. `verb-eval-template.md` §1 has the adoption decision logic; §4 has a quick-reference of PIE present stem types and their Ghandwa reflexes. `verbs.md` has the full classification schema.

#### Priority 0 — Evaluate and derive four stub verbs

These stubs exist in NocoDB with glosses but no lemma, PIE source, or stem class. For each: run the decision logic in `verb-eval-template.md` §1, choose a stem type, derive the Ghandwa 3sg present, verify against the transformer, and update the NocoDB record.

| Gloss | PIE root candidates | Notes |
|---|---|---|
| hold / grasp (stative) | *\*seǵʰ-* or *\*kap-* | *kapiéti* already covers "take/seize"; need stative "hold" — *\*seǵʰ-* is the better candidate |
| run / flow | *\*ḱers-* or *\*h₁ret-* | No motion verb in lexicon; *dā́nu* is noun only. Also blocks benchmark sentences 10, 21, 26, 30 (see §2.4) |
| throw | *\*h₁yeh₁-* or *\*gʷelh₁-* | — |
| cut | *\*sek-* | Basic technology verb; straightforward thematic |

#### Priority 1 — Athematic root presents

Pattern: full-grade root + zero ending in sg.; zero-grade root + thematic vowel in pl.

Candidates (from lexicon `verb_thematicity = athematic`, `verb_stem_type = root`):
- *ɣvénti ~ ɣvanénti* — strike, kill (*\*gʷʰen-*)
- *βā́ti ~ βánti* — speak authoritatively (*\*bʰeh₂-*)
- *stā́ti* — stand (*\*steh₂-*)
- *éiti* — go (*\*h₁ey-*) — check if already done
- *ésti* — is (*\*h₁es-*) — check if already done

Note: athematic 3pl uses *-anti* (< *\*h₁snti* → *santi* by CHC > CaC or CaRC convergence); same pattern across all athematics (*yanti*, *danti*, *stanti*). **Transformer does not yet handle this correctly; hand-derive.**

#### Priority 2 — Thematic root presents

Pattern: full-grade root + thematic vowel throughout; 3sg *-eti*, 3pl *-onti*.

Candidates: *édeti* (eat), *véideti* (see/know), *sékveti* (follow), *gvéteti* (say), *ðéɣveti* (burn), *kléveti* (hear), *wérteti* (turn), *skéleti* (split), *méldeti* (melt), *régeti* (straighten).

#### Priority 3 — Reduplicated presents

- *dídōti ~ didónti* — give (reduplicated athematic; i-reduplication, not e-)
- *píboti ~ píponti* — drink (reduplicated thematic; *h₃* voicing pending resolution)
- *ðḗti ~ ðánti* — put/place (reduplicated athematic)

#### Priority 4 — Derived presents

- *éye-causatives*: *ðoɣvéieti*, *sodéieti*, *moldéieti*, *voléieti*, *rogéieti*, *moréieti*, *nokéieti*
- Nasal infix: *kalnéuti*, *kalnéiti*, *iunékti* — some may already be done
- *ye-presents*: *βarkiéti*, *sjūjéti*

#### Format for paradigm work

Read `verbs-worksheet.md` at session start to confirm which 6 verbs are done and use them as models. For each new verb include at minimum: PIE preform → Ghandwa derivation (transformer-verified); present active 1sg–3pl; ablaut pattern; any transformer gaps or hand-corrections flagged.

#### Key files (verbal work)

| File | Purpose |
|---|---|
| `docs/grammar/ch4-ghandwa/verbs-worksheet.md` | Target file — add paradigms here |
| `docs/grammar/ch4-ghandwa/verbs.md` | Classification schema and stem type definitions |
| `docs/grammar/ch4-ghandwa/verb-eval-template.md` | Decision logic and worked examples |
| `tools/pie_transformer/` | Transformer — authoritative for surface forms |
| `docs/grammar/ch3-development/phonological-history.md` | Sound change rules for manual derivations |

---

## §2 — Lexicon Content & Gaps

### §2.1 — Etymology: *udṓr ~ udnós* / *vódar ~ udéns*

**Source:** `handoff-lexicon-content.md` Item 2
**Status:** `hold` — two water words exist; relationship and dialectal distribution unresolved.

PIE has two heteroclitic paradigms for 'water':
- Acrostatic: *wódr̥* (nom.) ~ *wédns* (gen.) — o-grade nom., e-grade gen.
- Proterokinetic: *wódr̥* (nom.) ~ *udéns* (gen.) — o-grade nom., zero-grade gen.

Ghandwa appears to have inherited both, surfacing as:
- *udṓr ~ udnós* — collective/mass form (the great water, the sea)?
- *vódar ~ udéns* — singular/countable (a body of water)?

Questions to resolve: which ablaut pattern does each form reflect; is the distinction singular vs. collective, or dialectal; how does this interact with the existing entry *vodán* (if present). Check `vocab/lexicon-staging.md` §r/n heteroclites for the full staged paradigm options.

---

### §2.3 — Lexicon Quick Edits

**Source:** `handoff-catch-all.md` C1, C2, C10

#### *svézōr* `nom_stem_class` (~10 min)

Set the `nom_stem_class` field in the NocoDB record for *svézōr* 'sister'. PIE *swésōr is an r-stem (or r/n heteroclite, but the nom. -r without alternation suggests treating it as a pure r-stem for now). Value: `r-stem`. Check paradigm against `docs/grammar/ch4-ghandwa/paradigms-nominal.md` before writing, and confirm IPA is consistent.

#### *véstrom* — keep or replace (~15 min)

Decide whether to keep *véstrom* 'place, location, site'. The form is phonologically regular (< PIE *\*wes-tro-m* or similar). The flagged concern is superficial Westeros/fantasy association. Options: keep as-is (association is incidental; etymology is sound); regloss to something less generic ('dwelling site', 'encampment', 'settlement territory'); replace with a different derivation for the 'place/location' semantic slot. Call at your discretion — no further linguistic research needed.

---

### §2.4 — Lexical Gaps (Merged)

**Sources:** `handoff-lexicon-content.md` §3, `handoff-syntax-benchmark.md` "Lexical Gaps"

These items block multiple sentences in the 38-sentence syntax benchmark corpus (§3.2). For each: identify PIE source, derive Ghandwa form using `docs/grammar/ch3-development/phonological-history.md`, verify against the transformer, and add to NocoDB.

#### Nouns / pronouns

| Gloss | PIE candidate | Sentences blocked | Notes |
|---|---|---|---|
| child | *\*gʷelbʰ-* (womb/young) or *\*peh₂w-* (small) | 4, 7, 12, 16, 23, 25 | Check EDPG/EDL for best WIE form. Core Swadesh item. |
| bread | *\*peh₂-* ('feed, protect') or denominative from grain word | 4, 7, 16, 35 | *iévos* 'grain/cereal' exists; check whether a derived 'bread' form is better than a separate root |
| who (anim. interrog.) | *\*kʷis* | 20 | *kvód* (inanimate 'what') already exists; need animate counterpart |

#### Verbs

| Gloss | PIE candidate | Sentences blocked | Notes |
|---|---|---|---|
| run | *\*ḱers-* or *\*h₁ret-* | 10, 21, 26, 30 | *éiti* 'go' currently substituted; dedicated run verb needed. Also a Priority 0 stub in §1.2. |
| flee | *\*bʰewg-* | 25, 38 | Noun *βugā́* 'flight' already exists; derive verb from same root |
| rejoice | — | 24 | No entry. |
| cry / weep | *\*ḱley-* or *\*gʷʰley-* | 23 | Lower priority; single sentence |

#### Particles / adverbs

These require reference to Dunkel *LIPP* or Fortson §5 paradigm tables for particle reconstruction.

| Gloss | PIE candidate | Sentences blocked | Notes |
|---|---|---|---|
| where | *\*kʷu* or *\*kʷo-dhé* | 22 | Standard PIE locative interrogative |
| when (subordinator) | *\*kʷe* + temporal particle | 24 | Check whether *kve* conflicts with the conjunctive *kve* if it exists |
| because | *\*eti* or periphrastic | 25 | May require a calque or particle compound |
| if (conditional) | *\*sey* or *\*kʷe* | 26 | *néi* = 'if not / unless' — not the affirmative conditional |
| yesterday | *\*dʰǵʰyes-* | 14 | *péruti* = 'last year' — wrong scale; 'yesterday' is a separate form |
| never | *\*ne* + temporal particle | 38 | May be compositional; check what temporal adverbs exist |
| up (preverb) | — | 33–34 | No established preverb inventory |

#### Key files (lexicon content)

| File | Purpose |
|---|---|
| `docs/notation.md` | Orthography, field conventions |
| `docs/grammar/ch3-development/phonological-history.md` | Sound change rules |
| `docs/grammar/ch4-ghandwa/paradigms-nominal.md` | Nominal paradigms |
| `docs/grammar/ch4-ghandwa/verbs.md` | Verb classification schema |
| `vocab/lexicon-staging.md` | §r/n heteroclites has water word paradigm options |
| `tools/pie_transformer/` | Transformer — authoritative for surface forms |

---

## §3 — Syntax

### §3.1 — Design Framework

**Source:** `ghandwa-syntax-handoff.md` (benchmark sentences removed; see §3.2 for translations)

#### Source and typological motivation

These recommendations are motivated by the general profile of older Indo-European languages and by Proto-Germanic/Germanic syntactic reconstruction work, especially: Walkden *Syntactic Reconstruction and Proto-Germanic* (2014); Fortson *Indo-European Language and Culture* (2010); *The Cambridge Handbook of Germanic Linguistics*; HCHIEL Germanic and Indo-European background chapters.

The guiding logic is that Ghandwa should not simply copy Latin, nor should it already behave like later Germanic. It should occupy an earlier IE-like stage where rich case morphology and discourse-driven order are still central, while some Germanic-like finite-verb placement patterns may be emerging.

#### High-level recommendation

> A shallow post-PIE language with rich case morphology, noun-adjective noun phrases, optional subject pronouns, discourse-driven constituent order, second-position clitics, inherited correlative relative clauses, and an emerging but not obligatory V2-like main-clause pattern.

Key principle:

> **Case endings mark grammatical roles; word order marks discourse.**

#### Already-decided project constraints

- Ghandwa is shallow post-PIE, not a late daughter language.
- Ghandwa retains enough inherited morphology that syntax need not be rigidly English-like.
- Noun phrase order is generally **noun-adjective**.
- Possessive pronouns, determiners, and numerals may precede the noun, but this remains unresolved.
- Ghandwa should leave room for later daughters to diverge substantially.
- Translation work should use IPA-style or normalized Ghandwa forms consistently, depending on the layer being tested.

#### Core syntactic profile

| Domain | Recommendation | Status |
|---|---|---|
| Alignment | nominative-accusative | recommended default |
| Argument marking | primarily by case | recommended default |
| Subject pronouns | optional unless contrastive/emphatic | recommended |
| Object pronouns | droppable if recoverable/topical | recommended but test in benchmarks |
| NP order | noun-adjective | already decided |
| Possessive pronouns | probably pre-nominal | unresolved |
| Lexical genitives | probably post-nominal by default | recommended |
| Main-clause order | topic/focus first, finite verb early | recommended |
| V2 | available/emerging, not absolute | recommended |
| Subordinate clauses | more verb-late/conservative | recommended |
| Wh-questions | wh-fronting with finite verb early | recommended |
| Imperatives | verb-initial or verb-early | recommended |
| Relatives | correlative in archaic/formal style; later postnominal relatives possible | recommended |
| Clitics | second-position clitic slot | recommended |
| Preverbs | semi-independent in older/high style; more bound in ordinary style | recommended |
| Negation | preverbal particle, exact placement unresolved | unresolved |

#### Clause order

Ghandwa should not be assigned a single rigid basic order. It should have **several licensed clause templates** whose distribution depends on register, clause type, and information structure.

**Template 1 — Conservative/archaic neutral declarative:**
`Subject-NOM Object-ACC Verb`
Use for older, formal, poetic, legal, or inherited-style Ghandwa.

**Template 2 — Ordinary assertive main clause:**
`Topic / Subject – finite verb – remaining arguments`
Recommended everyday/prose main-clause structure. Allows a Germanic-like V2 tendency without making V2 fully obligatory.

**Template 3 — Subordinate clause:**
`Subordinator – Subject-NOM Object-ACC Verb`
Subordinate clauses prefer conservative verb-late order.

**Template 4 — Fronted adverbial main clause:**
`Adverbial – finite verb – subject – object`
Useful benchmark for whether Ghandwa has an early V2-like main-clause left edge.

**Template 5 — Verb-initial clause:**
`Verb – subject – object`
Use for imperatives, narrative surprise, presentational/existential clauses, or elevated/marked style.

#### Information structure

Ghandwa should be treated as **discourse-configurational** rather than "free word order."

| Order type | Function |
|---|---|
| Subject-first | neutral topic continuity |
| Object-first | topicalization or contrast |
| Adverbial-first | scene-setting, temporal/logical frame |
| Verb-first | command, dramatic narration, existential/presentational, marked assertion |
| Verb-late | conservative, subordinate, formal, poetic, or non-assertive |

Practical rule for translation: if a constituent is moved to the front, assume it is topical, contrastive, emphatic, or scene-setting unless the construction is specifically marked as neutral.

#### Noun phrase syntax

Default order: `Noun – Adjective`. Already decided.

Adjectives agree in gender, number, and case. Do **not** assume a full Proto-Germanic-style strong/weak adjective system; a definiteness-sensitive adjective distinction could emerge in daughters.

Genitive placement — recommended default: `Noun possessed – lexical possessor-GEN`. But pronominal possessors may be pre-nominal: `my horse`, `our city`. Status: unresolved but recommended.

Determiners and numerals — unresolved. Provisional: `Determiner / numeral – noun – adjective`.

#### Pronoun syntax

Subject pronouns optional when verbal agreement makes the subject recoverable. Use explicit subject pronouns for: contrast, emphasis, topic shift, disambiguation, coordination, formal clarity.

Allow recoverable object pronouns to be omitted in discourse, but treat this as more context-sensitive than subject omission.

#### Clitics and particles

Second-position clitic slot: `First stressed constituent = clitic(s) – rest of clause`

Possible clitic categories: connective "and / but / then" particles; weak pronouns; discourse particles such as "indeed," "also," "even"; modal particles; possibly negation.

Open issue: decide which particles are true clitics and which are independent adverbs/conjunctions.

#### Negation

Unresolved. Provisional: `NEG – finite verb`, or in V2-like clauses `Topic – NEG/finite-verb complex – subject/object`.

Open questions: Is the basic negator pre-verbal? Can negation occupy the second-position clitic slot? Is there a separate negative polarity particle for "never," "not yet," or "no one"? Does negation trigger special word order?

#### Questions

**Yes/no:** verb-initial default; particle-marked and intonation-only options available.

**Wh-questions:** `WH-phrase – finite verb – subject – remaining arguments`. Early Germanic wh-questions strongly support wh-fronting and finite-verb movement.

#### Relative clauses

Two strategies:

1. **Archaic/formal correlative:** `Which X ..., that X ...` — deeply Indo-European; for liturgy, law, epic, learned prose.
2. **Ordinary postnominal relative:** `Noun – relative clause` — later/ordinary option; exact relative particle/pronoun is unresolved.

#### Subordination

Subordinate clauses should be more conservative than main clauses: `Subordinator – subject – object/adverbials – verb`.

#### Complement clauses and reported speech

Unresolved. Provisional: finite complement clauses rather than Latin-style AcI. Open issue: whether Ghandwa also has an infinitival complement strategy.

#### Preverbs and adpositions

Preverbs: semi-independent in older/high style. Both separated and verb-adjacent forms depending on register.

Adpositions: unresolved whether mostly prepositions, postpositions, or case-governed adverbs. Provisional: prepositions/adverbs with case government, allowing older bare case usage where inherited.

#### Case syntax

| Case | Core syntactic use |
|---|---|
| nominative | subject, predicate nominal |
| accusative | direct object, goal/extent in some uses |
| genitive | possession, partitive, source-like relations |
| dative | recipient, indirect object, experiencer, location-like uses |
| instrumental | means, accompaniment, manner, possibly agent in some constructions |
| vocative | direct address |

Open issue: whether instrumental is robust, residual, or being replaced by adpositional phrases.

#### Register model

**Conservative/high/formal:** more verb-late order; more correlative relatives; more overt morphology; fewer reduced pronouns; more separated preverbs; more second-position particles. Use for: liturgy, law, epic/poetry, official inscriptions, learned prose.

**Ordinary prose/speech:** topic-first with early finite verb; subject pronouns omitted when obvious; postnominal relatives increasingly available; preverbs more often adjacent to/bound with verb; case still active. Use for: narrative prose, dialogue, ordinary translation benchmarks.

**Late/regional/daughter-leaning:** stronger V2 in some regions; stronger SVO in others; erosion or restructuring of case functions; generalized postnominal relatives; more fixed negation patterns; clitic systems simplifying. Use for: daughter-language development, dialectal variation.

#### Implementation advice

Keep these layers separate: (1) morphology, (2) phrase syntax, (3) clause syntax, (4) discourse, (5) clitic/particle, (6) register/dialect. Do not collapse into a single "word order" rule.

#### Near-term decisions still needed (syntax framework)

1. Decide the ordinary position of possessive pronouns.
2. Decide whether lexical genitives are mostly postnominal.
3. Decide whether numerals and demonstratives precede nouns by default.
4. Decide the basic negator and its placement.
5. Decide whether negation is a clitic, particle, or independent adverb.
6. Decide the main relative pronoun/particle inventory.
7. Decide whether ordinary prose uses correlative relatives frequently or only in high style.
8. Decide whether Ghandwa has a productive infinitive and how it handles complement clauses.
9. Decide how robust the instrumental case is syntactically.
10. Decide how separable preverbs are in ordinary prose.
11. Decide whether V2 is optional, preferred, or strongly regular in main clauses.
12. Decide whether daughter languages inherit different registers as different grammatical baselines.

#### Recommended immediate working standard

1. **Noun phrases:** noun-adjective; preposed possessive pronouns/determiners/numerals allowed provisionally.
2. **Main clauses:** topic/subject first, finite verb early; V2-like but not obligatory.
3. **Subordinate clauses:** verb-late preferred.
4. **Questions:** wh-fronting plus early finite verb.
5. **Relatives:** correlative in formal/archaic style; postnominal relative clauses allowed in ordinary prose but not yet fully specified.
6. **Pronouns:** omit subject pronouns when agreement is clear; use pronouns for emphasis or contrast.
7. **Particles:** reserve a second-position clitic slot.
8. **Preverbs:** allow both separated and verb-adjacent forms depending on register.
9. **Word order:** treat deviations from neutral order as meaningful, not random.

---

### §3.2 — Benchmark Translations

**Source:** `handoff-syntax-benchmark.md`
**Convention adopted:** all sentences rendered in present tense throughout. Past tense is deferred pending aorist/past paradigm work.

Ordinary prose order (topic-first, V2-like) is the default. Conservative (SOV) shown where it differs.
`[GAP]` = no lexicon entry. `[run]` etc. = specific missing verb.

#### Basic clauses

**1. The man sees the horse.**
*virós véideti ékvom.*
`man.NOM see.3SG horse.ACC`
Cons: *virós ékvom véideti.*

**2. The woman sees the river.**
*gvénā véideti ákvām.*
`woman.NOM see.3SG river.ACC`
River lexeme fixed as *ákvā* (ā-stem f).

**3. The king kills the wolf.**
*rḗks nokéieti válkvom.*
`king.NOM kill.3SG wolf.ACC`
⚑ See §3.3 D1.

**4. The child eats bread.**
[child.NOM] *édeti* [bread.ACC]
[GAP: child, bread]

**5. I know the name.**
*véidō nóman.* (pro-drop) / *ég véidō nóman.* (with subject)
`know.1SG name.ACC`
⚑ See §3.3 D2. *ganṓti* (know/recognize) also available but nasal-infix; 1sg form unresolved.

**6. We hear the word.**
*véi klevomos várðom.*
`we.NOM hear.1PL word.ACC`

#### Case and valency

**7. The king gives bread to the child.**
*rḗks dídōti* [child.DAT] [bread.ACC]
[GAP: child, bread]

**8. The warrior strikes the wolf with a spear.**
*koriovirós ɣoizō ɣvéneti válkvom.*
`warrior.NOM spear.INS strike.3SG wolf.ACC`
Cons: *koriovirós ɣoizō válkvom ɣvéneti.*

**9. The man comes from the city.**
*virós gvémeti véikezos.*
`man.NOM come.3SG settlement.GEN(=ABL)`
⚑ See §3.3 D3.

**10. The horse runs to the river.**
*ékvos éiti ákvām.*
`horse.NOM go.3SG river.ACC`
[GAP: run verb; *éiti* 'go' substituted]

**11. The woman stands before the house.**
*gvénā stā́ti parí kóimom.*
`woman.NOM stand.3SG before home.ACC`
⚑ See §3.3 D4. Static position may prefer LOC (*kóimoi*).

**12. The child sleeps in the house.**
[child.NOM] *svépeti kóimoi.*
`sleep.3SG home.LOC`
[GAP: child]

#### Information structure

**13. The wolf, the king kills.**
*válkvom nokéieti rḗks.*
`wolf.ACC(TOP) kill.3SG king.NOM`
Object-fronted = topicalized/contrastive; V2 order.

**14. Yesterday the king kills the wolf.**
[yesterday] *nokéieti rḗks válkvom.*
[GAP: 'yesterday']

**15. This I know.**
*tód véidō.*
`this.ACC.N know.1SG`
*tód* in topic position → V2; subject pro-dropped.

**16. Bread the woman gives to the child.**
[bread.ACC(TOP)] *gvénā dídōti* [child.DAT]
[GAP: bread, child]

**17. To the king comes the warrior.**
*regéi gvémeti koriovirós.*
`king.DAT come.3SG warrior.NOM`
Fronted dative, V2, subject last. Presentational/existential pattern.

**18. Great is the city.**
*megvom ésti véikos.*
`great.NOM.N be.3SG city.NOM.N`
V-initial = marked/emphatic. Neutral: *véikos ésti megvom.*

#### Questions

**19. What does the man see?**
*kvód véideti virós?*
`what.ACC see.3SG man.NOM`

**20. Who kills the wolf?**
[who.NOM] *nokéieti válkvom?*
[GAP: animate interrogative 'who']

**21. Which horse runs to the river?**
*iós ékvos éiti ákvām?*
`which.NOM horse.NOM go.3SG river.ACC`
[GAP: run; *éiti* substituted]

**22. Where does the king stand?**
[where] *stā́ti rḗks?*
[GAP: 'where']

**23. Why does the child cry?**
[why] [child.NOM] [cry.3SG]?
[GAP: child, cry/weep, why]

#### Subordinate clauses

**24. When the king comes, the people rejoice.**
[when] *rḗks gvémeti, teutā́* [rejoice.3SG]
[GAP: 'when' subordinator, rejoice]

**25. Because the wolf comes, the child flees.**
[because] *válkvos gvémeti,* [child.NOM] [flee.3SG]
[GAP: because, child, flee]

**26. If the horse runs, the warrior follows.**
[if] *ékvos éiti, koriovirós sékveti.*
[GAP: 'if'; *éiti* for run]

**27. The man says that the king comes.**
*virós gvéteti tód rḗks gvémeti.*
`man.NOM say.3SG COMP king.NOM come.3SG`
*tód* as complementizer (standard PIE demonstrative-to-comp. pathway).

**28. I know that the woman sees the river.**
*véidō tód gvénā ákvām véideti.*
`know.1SG COMP woman.NOM river.ACC see.3SG`
Subordinate clause verb-late (SOV). Main/sub contrast visible.

#### Relatives

**29. Which man comes, that man I see.**
*iós virós gvémeti, tóm viróm véidō.*
`which.NOM man.NOM come.3SG, that.ACC man.ACC see.1SG`
Correlative strategy. ⚑ See §3.3 D5.

**30. Which horse the king chooses, that horse runs.**
*ióm ékvom rḗks voléieti, tóm ékvom* [run.3SG]
[GAP: run] ⚑ See §3.3 D5.

**31. I see the man who kills the wolf.**
*véidō viróm iós válkvom nokéieti.*
`see.1SG man.ACC REL.NOM.M wolf.ACC kill.3SG`
Postnominal relative. *iós* as relative pronoun, agreeing with head in gender/number.

**32. The city that the king builds is great.**
*véikos iód rḗks tékseti ésti megvom.*
`city.NOM REL.NOM.N king.NOM make.3SG be.3SG great.NOM.N`
⚑ See §3.3 D5. *tékseti* ('fashion/make') used for 'build' — semantic stretch.

#### Preverbs, particles, negation

**33. The warrior goes up to the city.**
*koriovirós éiti* [up] *véikos.*
`warrior.NOM go.3SG [up] city.ACC`
[GAP: 'up' preverb]

**34. Up goes the warrior to the city.**
[up] *éiti koriovirós véikos.*
V-initial (marked narrative). Same gap.

**35. The king then gives bread to the child.**
*rḗks éti dídōti* [child.DAT] [bread.ACC]
`king.NOM also/then.2P give.3SG`
*éti* in 2P clitic slot after *rḗks*. ⚑ See §3.3 D6.
[GAP: bread, child]

**36. This too I know.**
*tód éti véidō.*
`this.ACC also.2P know.1SG`
Clean 2P clitic demonstration: topic → 2P clitic → verb.

**37. The man does not see the wolf.**
*virós né véideti válkvom.*
`man.NOM NEG see.3SG wolf.ACC`
*né* preverbal; also satisfies 2P reading after topic *virós*.

**38. The king never flees.**
*rḗks* [never] [flee.3SG]
[GAP: flee; *néi* = 'not indeed / if not' ≠ never]

#### New entry from this session

| field | value |
|---|---|
| entry_id | 99900 |
| lemma_1 | *koriovirós* |
| lemma_2 | *koriovirózio* |
| gloss | warrior, fighting man |
| pos | noun |
| stem | o-stem |
| gender | m |
| status | draft |
| formation | compound (PGh innovation) |
| note | *kórios* 'army, troops' + *virós* 'man'; accent on second element per compounding rules; IPA pending (see §2.3) |
| cross_refs | kórios; virós |

#### Morphological gaps surfaced

- **Past tense / aorist**: deferred by design. Blocks ~60% of the original benchmark. Next tense session needs at minimum a 3sg s-aorist or root aorist convention.
- **Nasal-infix verb 1sg**: *ganṓti* — alternative to *véideti* for sentence 5 — but its 1sg form requires athematic nasal-infix paradigm work not yet done.
- **Full *to-* / *io-* paradigms**: see §3.3 D5.
- **Thematic verb 1pl confirmed** as *-omos* (e.g., *klevomos*) — consistent with dat.pl pattern and PIE *-omes*.

#### Vocabulary confirmed this session

| Form | Gloss | Stem | Source |
|---|---|---|---|
| *virós* | man | o-stem m | lexicon |
| *gvénā* | woman | ā-stem f | lexicon |
| *rḗks ~ regés* | king | root noun m | lexicon |
| *válkvos* | wolf | o-stem m | lexicon |
| *ékvos* | horse | o-stem m | lexicon |
| *nóman ~ naméns* | name | man/mén-stem n | lexicon |
| *várðom* | word | o-stem n | lexicon |
| *ɣoizós* | spear | o-stem m | lexicon |
| *kórios* | army, troops | o-stem m | lexicon |
| *ákvā ~ ákvās* | river | ā-stem f | lexicon |
| *kóimos* | home, camp, settlement | o-stem m | lexicon |
| *véikos ~ véikezos* | settlement, city | s-stem n | lexicon |
| *teutā́* | people, tribe | ā-stem f | lexicon |
| *megvos* | great, big, mighty | o/ā adj | lexicon |
| *ég* | I (nom, unemphatic) | pronoun | lexicon |
| *egóm* | I (nom, emphatic) | pronoun | lexicon |
| *véi* | we (nom) | pronoun | lexicon |
| *tū* | you (2sg) | pronoun | lexicon |
| *ís ~ ízio* | he (3sg m) | pronoun | lexicon |
| *tód ~ tózio* | that/this; COMP | det | lexicon |
| *iós ~ iózio* | which; REL | det | lexicon |
| *kvód* | what | interrog | lexicon |
| *éti* | and, also; (weak: then) | conj | lexicon |
| *né* | not | particle | lexicon |
| *parí* | before, in front of | adp | lexicon |
| *véideti* | see; know | verb | lexicon |
| *kléveti* | hear | verb | lexicon |
| *gvéteti* | say, speak | verb | lexicon |
| *gvémeti* | come, arrive | verb | lexicon |
| *éiti* | go | verb | lexicon |
| *stā́ti* | stand | verb | lexicon |
| *svépeti* | sleep | verb | lexicon |
| *édeti* | eat | verb | lexicon |
| *ɣvéneti* | strike, beat | verb | lexicon |
| *nokéieti* | kill (make disappear) | verb | lexicon |
| *moréieti* | kill (make die) | verb | lexicon |
| *dídōti* | give | verb | lexicon |
| *sékveti* | follow | verb | lexicon |
| *voléieti* | choose | verb | lexicon |
| *tékseti* | fashion, make | verb | lexicon |
| *ésti* | be (3sg) | verb | lexicon |
| *koriovirós* | warrior | o-stem m | new entry 725 |

---

### §3.3 — Open Syntax Decisions

**Sources:** `handoff-catch-all.md` C4–C9, `handoff-syntax-benchmark.md` D1–D6 (merged; catch-all versions provide expanded actionable detail)

#### D1 — Default 'kill' verb (~10 min)

Pick the default verb for 'kill' and note it in the lexicon or grammar.

Options established: *moréieti* (causative of 'die' — transparent, semantically neutral) vs. *nokéieti* (causative of 'disappear/perish' — more 'eliminate'). Both are in the lexicon. Recommend *moréieti* as the default transitive 'kill'; *nokéieti* for 'eliminate/make disappear'. Update gloss fields in NocoDB if the current glosses are ambiguous.

#### D2 — Pro-drop convention (~15 min)

Write one paragraph in `docs/grammar/ch4-ghandwa/sec4-5-syntax.md` stating the pro-drop policy.

Working decision: drop subject pronoun when person/number is unambiguous from the verb ending; retain for contrast or topic-shift. (See benchmark sentences 5 and 15.)

#### D3 — Ablative source: *eks* vs. bare genitive (~20–30 min for Option B; ~5 min for Option A)

Decide whether to add *eks* (< PIE *\*h₁eǵʰs* 'out of') as an ablative/source particle.

Option A: bare genitive already functions as ablative-of-source (sentence 9 works). No new entry needed.
Option B: lexicalize *eks* as a particle; adds an unambiguous ablative marker and enables cleaner sentences 9, 33–34.

*\*h₁eǵʰs* is directly reconstructible: Lat. *ex*, OIr. *ess-*, Goth. *us*. Ghandwa form would be *eks* (regular: *\*h₁* → zero, *g* → *k* word-finally? — check phonological history before committing). If Option B, add to NocoDB as a particle entry.

#### D4 — *parí* case government (~10 min)

Confirm and document the case split for *parí* in `docs/grammar/ch4-ghandwa/sec4-5-syntax.md` or the adposition's NocoDB entry.

PIE *\*peri*: ACC for motion-toward, LOC for static position. 'Stand before the house' = static → *parí kóimoi* (LOC), not ACC. This is the standard PIE split and requires no new decision, just documentation.

#### D5 — *to-/io-* paradigm formalization (~45 min)

Establish the full paradigm of the demonstrative/complementizer *to-* and the relative/interrogative *io-*, and add the needed forms to NocoDB or a paradigm table.

Currently attested: *tód* (n.nom/acc), *tózio* (gen?), *iós* (m.nom), *iózio* (gen?). Needed for the benchmark corpus: m.acc *tóm/ióm*, f.nom *tā/iā*, f.acc *tām/iām*, n.nom *iód*. All derivable by regular analogy from PIE *\*to-/\*yo-* with Ghandwa's established nominal endings.

Approach: build a small paradigm table (nom/acc × m/f/n × sg/pl) for both stems, verify each cell against the nominal endings in `docs/grammar/ch4-ghandwa/paradigms-nominal.md`, and add the new forms to NocoDB.

#### D6 — Temporal 'then' (~15 min decision; +30 min if new entry)

Decide whether to add a dedicated temporal adverb or leave *éti* ('and, also') as the weak substitute.

*éti* covers 'furthermore / and then' loosely. Options: add a new particle (*nu*, *tá*, or similar from PIE temporal adverbs) or leave the slot empty and note the gap. Low priority unless corpus work requires it.

---

## §4 — Paradigm Database

**Source:** `handoff-paradigms-db.md`
**Priority:** Medium
**Scope:** Design and populate NocoDB tables for nominal and verbal paradigms. Multi-pass project.

### §4.1 — Rationale

Paradigm tables are inherently relational: each lexicon entry has a `nom_stem_class` or `verb_stem_type`; each stem class has a fixed set of case/number cells; the ending for each cell is the same across all entries in the class.

Storing this in NocoDB allows: querying all forms of a given stem class, cross-referencing from lexicon entries to their paradigm, and tracking which paradigm cells are still gaps.

**What stays in markdown:** the prose notes (sound change derivations, analogical explanations, comparative remarks). `docs/grammar/ch4-ghandwa/paradigms-nominal.md` remains the authoritative explanatory document. NocoDB holds the structured data; markdown holds the reasoning.

### §4.2 — Proposed schema

#### Table: `paradigm_endings`

One row per paradigm cell.

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

#### Controlled vocabulary: `stem_class`

**Nominal:** `ā-stem` (fem), `o-stem-m` (masc), `o-stem-n` (neut), `i-stem`, `u-stem-mf` (masc/fem), `u-stem-n` (neut), `ī-stem` (fem; currently folded into ā-stem), `cons-stem` (root nouns), `r-stem` (kinship), `n-stem` / `men-stem`, `s-stem-n` (neut), `r/n-heteroclite`.

**Adjectival:** `adj-o/ā`, `adj-u`, `adj-i`, `adj-cons`.

**Verbal (present active — add others as needed):** `verb-thematic`, `verb-athematic-root`, `verb-reduplicated-thematic`, `verb-reduplicated-athematic`, `verb-nasal-infix`, `verb-causative-eye`, `verb-ye`.

#### Table: `paradigm_examples`

Links a stem class to attested lexicon entries used as examples.

| Column | Type | Notes |
|---|---|---|
| `example_id` | AutoNumber | PK |
| `stem_class` | SingleSelect | FK to stem_class vocabulary |
| `entry_id` | Number | FK to lexicon table |
| `lemma` | SingleLineText | Denormalized for readability |
| `is_primary` | Checkbox | Primary example for the class |

### §4.3 — Current state of `paradigms-nominal.md`

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
| r/n-heteroclite | partial (nom, gen) | all gaps | Mark as `status = gap`; fill when water word paradigm is resolved (§2.2) |
| adj-o/ā | — (follows o-stem/ā-stem) | — | Not a separate table needed |
| adj-u | nom only | all gaps | Mostly pending |
| adj-i | all gaps | all gaps | Not yet established |
| adj-cons | all gaps | all gaps | Not yet established |

Verbal paradigms: in `verbs-worksheet.md`, 6 verbs done; more to follow (§1.2). Populate verbal endings from what is established there; mark unestablished classes as `status = gap`.

### §4.4 — Suggested workflow

**Phase 1 — Nominal endings table:**
1. Create `paradigm_endings` table in NocoDB with the schema above
2. Set SingleSelect options for all controlled vocabulary fields
3. Populate from `paradigms-nominal.md` — start with the five complete stem classes (ā, o-m, o-n, u-mf, u-n, s-n)
4. Mark gaps as `status = gap` rather than leaving them blank
5. Create `paradigm_examples` table and link primary examples from the lexicon

**Phase 2 — Verbal endings table:**
1. Same schema, `pos = verb`
2. Verbal cells are: person (1/2/3) × number (sg/pl) × mood (ind/subj/opt/imp) × voice (act/mid)
3. Populate from `verbs-worksheet.md` as currently established; mark unestablished classes as `status = gap`

**Phase 3 — Gap-filling passes:**
r-stem, n/men-stem, consonant stem IPA, adj paradigms — fill as linguistic work allows. r/n-heteroclite: leave as `status = gap`; add after water word etymology is resolved (§2.2).

**Linking paradigm_examples to the lexicon:**
Once `paradigm_endings` exists, add a Links field in the lexicon table pointing to `paradigm_examples`. To auto-populate links, write a Python script using the NocoDB API (`localhost:8080/api/v1/meta/tables/{table_id}/records`). Otherwise, link manually.

### §4.5 — Key files (paradigm DB)

| File | Purpose |
|---|---|
| `docs/grammar/ch4-ghandwa/paradigms-nominal.md` | Source of truth for endings and notes — keep in sync |
| `docs/grammar/ch4-ghandwa/verbs-worksheet.md` | Source for verbal paradigms |
| `docs/grammar/ch4-ghandwa/verbs.md` | Verb stem type classification |
| `docs/notation.md` | Orthographic conventions |

---

## §5 — Transformer Cleanup

**Source:** `handoff-transformer-cleanup.md`
**Scope:** `tools/pie_transformer/`
**Status:** Ready to execute. No edits made yet.

### §5.1 — Context

The PIE transformer (Python package at `tools/pie_transformer/`, superseded the JSX file in 2026-05-15) has accumulated three classes of debt:

1. **A stale duplicate Daughter A implementation** is the one currently being called. The newer `daughter_a.py` is dead code.
2. **Seven helper functions and constants are duplicated across pipeline files**, with subtly different signatures.
3. **Accent-index tracking has at least five hand-rolled patterns in use**, some equivalent, some with off-by-one boundary differences that aren't covered by tests.

Phases 1 and 2 are mechanical and can ship together. Phase 3 (accent-tracking refactor) is specced in a separate document and executed in a future session. Phase 4 is cosmetic and can be done piecemeal.

### §5.2 — Decisions already made (do not relitigate)

| # | Decision | Rationale |
|---|---|---|
| 1 | `pipelines/daughter_a.py` is canonical. Delete `pipelines/daughters.py`. | Daughter A new model: LCG Stage 1 shared + per-daughter Stage 2; Stage 3 deferred until phonology settles. Matches `daughter_b.py` / `daughter_c.py`. |
| 2 | Accent-on-deleted-token policy: the rule that consumes the accented token specifies where the accent now lives. | Generalization of existing `_syl_res_vocalize` behavior. |
| 3 | Consolidate shared helpers into a new `pipelines/_common.py`. | Scopes pipeline-specific helpers separately from the rule engine (`rule.py`) and token inventory (`tokens.py`). |
| 4 | Accent-tracking refactor is deferred to a future session. This session preserves accent code verbatim. | Risk-bounded scope. Accent refactor requires test coverage to land first. |
| 5 | Rule IDs use `<prefix>.<stage>.<position>` numerical doc-mirror convention. | IDs anchor runner rules to their source documents. |

### §5.3 — Open decision

**D1. Daughter A Stage 3A tests.** `pipelines/daughters.py` had a Stage 3A (compensatory lengthening, coronal assimilation, geminate simplification, late xʷ-delabialization). `pipelines/daughter_a.py` does not — Stage 3A is explicitly deferred per the docstring. Two tests exercise Stage 3A behavior:

- `TestDaughterA::test_compensatory_lengthening_across_boundary`
- `TestDaughterA::test_cluster_spirant_ks` (asserts `'ē'` in output — only Stage 3A produces long vowels)

Options:
- **(a)** Delete the tests outright.
- **(b)** Move to dormant section (`@unittest.skip`) with comment pointing at `docs/daughters.md §3.1, 3A`. Preserves work; doesn't block CI; surfaces gap.
- **(c)** Leave them failing as a visible TODO.

Recommendation: **(b)**.

### §5.4 — Phase 1: Fix Daughter A breakage

**Risk:** Low (mechanical).
**Verification:** Full test suite passes after.

#### File operations
- Delete `tools/pie_transformer/pipelines/daughters.py`.
- Delete `tools/pie_transformer/pipelines/README.md`. (Byte-for-byte copy of `daughter_c.py`. Verify with `diff` before deleting. If a real README is wanted later, write separately.)

#### Routing fix
In `tools/pie_transformer/pipeline.py` (line 53–54):

```python
# Current:
if name == 'ghandwa-daughter-a':
    from .pipelines.daughters import RULES_A
    return RULES_A

# Change to:
if name == 'ghandwa-daughter-a':
    from .pipelines.daughter_a import RULES_A
    return RULES_A
```

#### Test updates
- `TestNotImplemented::test_daughter_b` and `test_daughter_c`: B and C are now implemented. Either delete these tests or rewrite to assert `status == 'ok'`.
- `TestDaughterA`: Per D1, resolve the Stage 3A tests.
- Verify remaining Daughter A tests align with `daughter_a.py` rule list (LCG + 2A.1 stress, 2A.2 devoicing, 2A.3 z→s, 2A.4 delab, 2A.5 cluster-spirant). The new `daughter_a.py` orders **stress first**, where `daughters.py` ordered it last — tests inspecting `accent_index` at intermediate states need updating.

#### Verification
```bash
cd tools && python3 -m unittest pie_transformer.tests.test_pipelines
```

#### Acceptance criteria
- `daughters.py` and `pipelines/README.md` removed.
- `pipeline.py:53` imports from `daughter_a`.
- Test suite green.
- `python3 -m pie_transformer form "*wĺ̥kʷos" --all` shows same eight pipelines; Daughter A output reflects LCG-then-Stage-2A.

---

### §5.5 — Phase 2: Extract `pipelines/_common.py`

**Risk:** Low-to-moderate (mechanical refactor, touches every pipeline file).
**Precondition:** Phase 1 complete and green.

#### Create `_common.py`

| Symbol | Source | Notes |
|---|---|---|
| `make_rule(id_, name, stage, apply_fn, requires=None)` | Any of the 9 copies (identical) | Replaces local `_rule` |
| `next_seg(toks, i) -> tuple[str \| None, int \| None]` | `daughter_c.py::_next_seg` | Tuple form replaces 5 single-return variants |
| `prev_seg(toks, i) -> tuple[str \| None, int \| None]` | `daughter_c.py::_prev_seg` | Same |
| `is_word_initial(toks, i)` | `daughter_c.py` | Useful for B and wékʷos |
| `is_word_final(toks, i)` | `daughter_c.py` | Same |
| `laryngeal_color(h, v) -> str` | `ghandwa.py` (byte-identical to `old_wekwos.py` and `proto_seldanic.py`) | Anatolian's version stays local |
| `centumize_rule(prefix)` factory | `ghandwa.py::_CENTUMIZE`'s body | Returns a `Rule` |
| `labiovelarize(toks, ctx)` | `ghandwa.py` (byte-identical to `old_wekwos.py`) | Preserve accent code verbatim |
| `UW: frozenset[str]` | `frozenset({'u', 'ū', 'w'})` | Replaces 3 inline definitions |

#### Move `_syllabify` from `render.py` to `_common.py`

Currently `daughter_b.py::_labiovelar_dissim` imports `_syllabify` from `..render` — wrong-direction dependency. Move `_syllabify`, `_valid_onset`, `_onset_split`, `_is_ipa_vowel`, `_base_form`, `_has_accent` to `_common.py`. `render.py` and `daughter_b.py` import from there. Local `from .tokens import VOWELS` imports become top-level.

#### Update each pipeline file

For each of 9 pipeline files: replace local `_rule` with `make_rule`; replace local next/prev helpers with tuple-returning imports; replace local `_laryngeal_color` with import; replace inline boundary sets with `tokens.BOUNDARIES`; replace inline `{'u', 'ū', 'w'}` with `_common.UW`.

#### Clean up dead bindings
- `ghandwa.py::_BOUKÓLOS` (line 148): defined but never placed in `RULES`. Either delete or change `_STAND_BOK_1`/`_STAND_BOK_2` to use it.

#### Daughter C consonant set
`daughter_c.py::_CONSONANTS_C`: hardcoded local list. Replace with derivation from `tokens.py` category sets. Verify resulting set is identical before committing.

#### Verification
```bash
cd tools && python3 -m unittest pie_transformer.tests.test_pipelines
python3 -m pie_transformer form "*wĺ̥kʷos" --all
python3 -m pie_transformer form "*ph₂tḗr" --all
python3 -m pie_transformer form "*ǵʰoysós" --all
python3 -m pie_transformer form "*h₁ésti" --all
python3 -m pie_transformer form "*nṓmn̥" --all
```
Output must be byte-identical to pre-refactor snapshot.

#### Acceptance criteria
- `_common.py` exists with listed symbols.
- No pipeline file defines a local `_rule`, boundary set, `_next_*`, `_prev_*`, `_laryngeal_color`, or `UW`.
- `_syllabify` lives in `_common.py`; `render.py` and `daughter_b.py` import from there.
- Test suite green.
- `--all` output unchanged on five smoke-test forms.

---

### §5.6 — Phase 3: Accent-tracking refactor

**Status: Spec complete.** See `tools/pie_transformer/docs/handoff-accent-tracking-v2.md`.

Execute after Phases 1–2. Covers: pattern catalog (A–E) with equivalence proofs, `shift_for_change`/`relocate` API, required test coverage, and per-file migration order. No code changes until test suite in §4 of that doc is written and passing.

---

### §5.7 — Phase 4: Rule ID migration

**Risk:** Low (cosmetic; only affects trace dumps and tests matching on `rule_id`).

Convention: `<prefix>.<stage>.<position>[<subletter>]`

**Already conforming:** `lcg.*`, `db.*`, `dc.*`, `da.*`. `nwk.*` optionally reformat (`nwk.41` → `nwk.4.1`).

**Needs migration — `ghandwa.py` (`gh.*`):**

| Current | Proposed | Source ref |
|---|---|---|
| `gh.centum` | `gh.0.1` | Pre-stage |
| `gh.lv_merge` | `gh.0.2` | Pre-stage |
| `gh.pie_delab` | `gh.0.3` | Pre-stage |
| `gh.tts` | `gh.1.1` | Stage 1 dentals |
| `gh.ssc` | `gh.1.2` | Stage 1 dentals |
| `gh.thorn` | `gh.1.3` | Stage 1 dentals |
| `gh.h_a` | `gh.1.4` | Stage 1 laryngeals |
| `gh.h_b1` | `gh.1.5` | |
| `gh.h_b2` | `gh.1.6` | |
| `gh.h_b3` | `gh.1.7` | |
| `gh.h_b4` | `gh.1.8` | |
| `gh.h_b5` | `gh.1.9` | |
| `gh.h_survive` | `gh.1.10` | |
| `gh.voi_bts` | `gh.1.11` | Stage 1 consonants |
| `gh.osthoff` | `gh.1.12` | Stage 1 vowels |
| `gh.ew_ow` | `gh.1.13` | Stage 1 vowels |
| `gh.pretonic` | `gh.1.14` | Pretonic |
| `gh.stand_lv_1` | `gh.1.15` | Standing post-S1 |
| `gh.stand_bok_1` | `gh.1.16` | Standing post-S1 |
| `gh.syl_res` | `gh.2.1` | Stage 2 syllabics |
| `gh.juwankos` | `gh.2.2` | Stage 2 fricatives |
| `gh.aspirates` | `gh.2.3` | Stage 2 fricatives |
| `gh.s_voice` | `gh.2.4` | Stage 2 fricatives |
| `gh.y_j` | `gh.2.5` | Stage 2 glides |
| `gh.stand_lv_2` | `gh.2.6` | Standing post-S2 |
| `gh.stand_bok_2` | `gh.2.7` | Standing post-S2 |

Verify against `docs/grammar/ch3-development/phonological-history.md` section numbers before committing.

**Other pipelines:** `old_wekwos.py` (`wk.*`), `proto_anatolian.py` (`pa.*` — module docstring numbers steps 1–10, migrate to `pa.1.1` etc.), `proto_seldanic.py` (`sel.*` — module docstring references `docs/proto-seldanic-pipeline.md` for rules 1–9).

#### Verification
- `grep -r "rule_id\s*==\s*['\"]" tools/pie_transformer/tests/` — update matching tests.
- `--all` trace output shows new IDs.
- Test suite green.

---

### §5.8 — Duplication catalog (grep targets for Phase 2)

- `_rule` constructor: 9 files.
- Boundary-skipping lookup: 5 variants across `daughters.py` (deleted Phase 1), `late_common_ghandwa.py`, `daughter_b.py` (2), `daughter_c.py` (2), plus inline in `ghandwa.py::_voiced_before_ts`.
- Boundary-set constant: `tokens.BOUNDARIES` exists; redefined or inlined in 6 places.
- `_laryngeal_color`: byte-identical in `ghandwa.py`, `old_wekwos.py`, `proto_seldanic.py`.
- `_labiovelarize`: byte-identical in `ghandwa.py`, `old_wekwos.py`.
- Centumize lambda: near-identical in `ghandwa.py`, `old_wekwos.py`, `proto_seldanic.py`.
- `{u, ū, w}` set: 3 definitions plus inline literals.
- `_syllabify`: in `render.py`, imported (wrong direction) by `daughter_b.py`.

### §5.9 — Explicitly out of scope

- Accent-tracking refactor (Phase 3; future session).
- Resurrecting Daughter A Stage 3A.
- Any behavior change to rules. Phases 1, 2, and 4 are pure refactor/cleanup.
- Touching `pie-2-ghandwa.jsx` (superseded, retained for reference).

---

## §6 — Dangwa-Era Reconcile Archaeology

**Source:** `handoff-dangwa-reconcile.md`
**Priority:** Low — do after all other sections.
**Scope:** Assess `vocab/archive/lexicon-reconcile.tsv` (248 rows) to determine how many of the 173 "probable new entry" and 74 "probable merge" items are already in the current lexicon, and how many represent genuine gaps.

### §6.1 — Context

`lexicon-reconcile.tsv` was generated during an earlier phase when the language was still called "Dangwa." It was a bulk intake/deduplication run against an older lexicon version. It has been archived to `vocab/archive/` and is no longer authoritative, but may contain vocabulary candidates that never made it into the current lexicon.

### §6.2 — Column key

| Column | Meaning |
|---|---|
| `merged_term` | The candidate Ghandwa form |
| `narGloss` | Gloss |
| `intake_bucket` | `probable_new_entry` / `probable_merge` / `already_represented` |
| `review_flag` | `REVIEW:gloss-match`, `REVIEW:old1-only`, `REVIEW:possible-split` |
| `best_current_lemma` | Closest match found in the lexicon at time of reconciliation |
| `best_current_status` | Status of that match |
| `best_match_score` | Fuzzy match score |
| `pos` | Part of speech |
| `PIE Root` | PIE source if known |

### §6.3 — Distribution

| Bucket | Count |
|---|---|
| probable_new_entry | 173 |
| probable_merge | 74 |
| already_represented | 1 |

Review flags: `REVIEW:gloss-match` (26), `REVIEW:old1-only` (23), `REVIEW:possible-split` (2).

### §6.4 — Suggested workflow

1. Export current lexicon from NocoDB as TSV (or use the Filesystem MCP to read it directly)
2. For each row where `intake_bucket = probable_new_entry`: NFC-normalize and check `merged_term` against current lexicon lemmas. If not found: assess whether it's a genuine gap or a Dangwa-era artifact. Flag genuine gaps for entry.
3. For `probable_merge` rows: check whether the merge target is still in the lexicon and whether the candidate form adds anything.
4. Discard rows where `best_current_status = canonical` and the match is solid.

**Do not batch-process mechanically** — many Dangwa-era forms used different orthographic conventions (ğ instead of ɣ, inconsistent accent marking) and will generate false negatives on string matching. Human review of ambiguous cases is required.

### §6.5 — Key files

| File | Path |
|---|---|
| Reconcile file (archived) | `vocab/archive/lexicon-reconcile.tsv` |
| Lexicon (authoritative) | NocoDB localhost:8080 |
| Notation conventions | `docs/notation.md` |

---

## §7 — File Corrections

**Source:** `handoff-catch-all.md` C3

### `docs/comparanda.md` line 111 (~5 min)

The line currently reads `[Ghandwa: *kantom]`. This was the pre-rename label; the rule is now the Boukólos rule. Update to the correct label. Verify current rule name in `docs/grammar/ch3-development/phonological-history.md` before editing.
