# Ghandwa Verbal System

*Last updated: 2026-05-16. Line count: see changelog.*

---

## §1. Overview

The Ghandwa verbal system is organized around a conservative Western Indo-European core. The default finite verb is a thematic root present. A small set of inherited athematic and reduplicated presents survives as a relic class, confined largely to high-frequency lexical items. Derived present stems in *-ye/o-* and *-éye/o-* are productive. Nasal-infix presents exist but are limited and classifiable. The middle/mediopassive survives as a relic category in *-r*; active voice is the default. The past system is organized around a single broad preterite, with a subset of lexically listed reduplicated or root-aorist forms for common inherited verbs. There is no dental preterite at the Ghandwa level; that is left to daughter-language development.

The system is set by Italic–Germanic consensus. Where the two branches diverge, decisions have been made case by case; the basis for each choice is documented in §§2–8 and in the design notes at the end of this file.

---

## §2. Verb classification

Ghandwa verbs fall into the following classes on the basis of present-stem formation:

**I. Thematic root presents.** The default class. An unaffixed root with thematic vowel *-e/o-* and primary active endings. Root is e-grade throughout the present. The large majority of inherited and newly derived verbs belong here.

**II. Derived thematic presents.**

- **IIA. *-ye/o-* presents.** Root or nominal stem plus the suffix *-ye/o-*. Denominative, inchoative, and some present-forming functions. Productive/semi-productive.
- **IIB. *-éye/o-* presents.** O-grade root plus *-éye/o-*. Causative, factitive, iterative. Productive.

**III. Athematic root presents.** Zero-grade root (full grade in sg. active) with primary endings added directly to the root. Relic class: confined to high-frequency inherited verbs ('be', 'go', 'give', 'stand', 'do/put', 'know').

**IV. Nasal presents.** Root with a nasal infix or suffix in the present stem only; zero-grade root. Subclasses: nasal infix, nasal suffix, *-néw/nu-* type, nasal-remodeled. [*Subclass paradigms open: see §8.*]

**V. Reduplicated presents.** Root reduplication plus present stem. Relic class; lexically enumerated. [*Inventory open: see §8.*]

**VI. Middle/deponent.** Mediopassive *-r* endings. Relic category; not a productive class.

---

## §3. The present system

### §3.1 Thematic root present — active indicative

The thematic vowel is *-e-* before single consonants and in the singular, *-o-* before *-m-* and *-nt-* (i.e. in 1pl and 3pl). The 2sg ending *-ezi* reflects regular intervocalic *\*s > z* (PIE \*-esi > Ghandwa \*-ezi).

Example root: *leg-* 'gather, speak' (3sg citation form *légeti*).

| Person | Ending | Form |
|---|---|---|
| 1sg | *-ō* | *légō* |
| 2sg | *-ezi* | *légezi* |
| 3sg | *-eti* | *légeti* |
| 1pl | *-omos* | *légomos* |
| 2pl | *-ete* | *légete* |
| 3pl | *-onti* | *légonti* |

### §3.2 Derived presents

#### *-ye/o-* presents (Class IIA)

Suffix *-ye/o-* is added to a nominal stem or zero-grade root. Function: denominative, inchoative, and productive present formation. The suffix surfaces as *-ie-* in most environments (3sg *-ieti*).

Example: *voléieti* 'wishes, wants' (from the root for 'will/wish').

#### *-éye/o-* presents (Class IIB)

O-grade root plus *-éye/o-*. Causative and factitive function. The suffix carries accent, hence the consistent accentuation pattern.

| Base | Derived causative | Gloss pair |
|---|---|---|
| *sédeti* 'sits' | *sodéieti* | 'sits' / 'seats, sets' |
| *légeti* 'gathers' | *logéieti* | 'gathers' / 'causes to gather, collects' |
| *éiti* 'goes' | *oyéieti* | 'goes' / 'sends, causes to go' |

Not every verb requires a derived causative. Ghandwa preserves inherited pairs and builds new ones; overgeneralizing *-éieti* to all verbs is avoided.

### §3.3 Athematic root present (Class III)

Athematic presents are confined to a small set of high-frequency inherited verbs. Full-grade root in the singular active; zero-grade elsewhere. Primary endings are added directly to the root.

Example: *es-* 'be'.

| Person | Ending | Form |
|---|---|---|
| 1sg | *-mi* | *esmi* |
| 2sg | *-zi* | *ezi* |
| 3sg | *-ti* | *esti* |
| 1pl | *-mos* | *esmos* |
| 2pl | *-te* | *este* |
| 3pl | *-nti* | *santi* |

The 3pl athematic zero-grade cluster (*\*h₁snti* for 'be') resolves to *santi* by two convergent paths: (a) CHC > CaC (laryngeal between consonants vocalizes), or (b) laryngeal disappears and syllabic *\*n̥* vocalizes by CaRC (*an*). Both paths yield the same output. The same resolution applies across the athematic relic class: *\*h₁ei-* 'go' → 3pl *yanti*; *\*deh₃-* 'give' → *danti*; *\*steh₂-* 'stand' → *stanti*. **Note:** the transformer does not yet handle CHC + syllabic nasal clusters correctly; hand-derive these forms until that gap is closed.

### §3.4 Nasal presents (Class IV)

[*Open. At least four subtypes are attested in the lexicon (nasal-infix, nasal-suffix, *-néw/nu-*, nasal-remodeled). Subclass paradigms to be drafted when inventory is confirmed. See §8.*]

### §3.5 Reduplicated presents (Class V)

[*Open. Inventory to be enumerated. Confirmed: *dídōti* 'gives', *píboti* 'drinks'. See §8.*]

---

## §4. Middle/mediopassive

Ghandwa preserves the Italic-type *-r* mediopassive as a relic category. It is not a productive voice in the core system; default verbal behavior is active. Lexicalized middle/deponent verbs exist (cf. *sékvetor* 'follows') and are marked `verb_voice_behavior = deponent` in the lexicon.

The 2pl and 3sg middle endings are syncretic (*-etor* for both); this is an inherited PIE feature and is not corrected.

Example: mediopassive paradigm of *leg-*.

| Person | Ending | Form |
|---|---|---|
| 1sg | *-or* | *légor* |
| 2sg | *-ezor* | *légezor* |
| 3sg | *-etor* | *légetor* |
| 1pl | *-omor* | *légomor* |
| 2pl | *-etor* | *légetor* (= 3sg) |
| 3pl | *-ontor* | *légontor* |

---

## §5. The mood system

### §5.1 Subjunctive

Formed with a long thematic vowel (*-ō/ē-*) plus primary endings. The long vowel creates syncretism with the indicative at 1sg, 1pl, and 3pl; this is expected and not remedied.

| Person | Ending | Form |
|---|---|---|
| 1sg | *-ō* | *légō* (= indic.) |
| 2sg | *-ēzi* | *légēzi* |
| 3sg | *-ēti* | *légēti* |
| 1pl | *-ōmos* | *légōmos* (= indic.) |
| 2pl | *-ēte* | *légēte* |
| 3pl | *-ōnti* | *légōnti* (= indic.) |

Semantic value: projection, expectation. Formally distinct from the optative.

Athematic subjunctive (e.g. *es-*): thematization of the root is the expected strategy (e.g. *esō*, *esēti*, *esōnti*). Full paradigm deferred pending confirmation that thematization is consistent across all athematic roots. [*Open: see §8.*]

### §5.2 Optative

Formed with *-oy-* plus secondary endings. The *-oy-* suffix is the thematic optative formant (PIE \*-oi- + \*-h₁-).

| Person | Ending | Form |
|---|---|---|
| 1sg | *-oyom* | *légoyom* |
| 2sg | *-oyes* | *légoyes* |
| 3sg | *-oyet* | *légoyet* |
| 1pl | *-oyome* | *légoyome* |
| 2pl | *-oyete* | *légoyete* |
| 3pl | *-oyont* | *légoyont* |

Semantic value: wish, potential. Formally distinct from the subjunctive.

### §5.3 Imperative

Ghandwa retains the conservative long-imperative (*-tōd*) type, following Italic (cf. Latin *-tō*). The 2pl imperative is syncretic with the indicative 2pl; the 2sg is the bare thematic stem.

| Person | Ending | Form |
|---|---|---|
| 2sg | *-e* (bare stem) | *lége* |
| 3sg | *-etōd* | *légetōd* |
| 2pl | *-ete* | *légete* (= indic.) |
| 3pl | *-ontōd* | *légontōd* |

---

## §6. Non-finite forms

### §6.1 Infinitive

Ghandwa formalizes the accusative of the *-tu-* verbal noun as the infinitive. The suffix is *-tum*, added to the zero-grade root.

Example: *légeti* → infinitive *légtum*.

This parallels the Latin *-tum* supine in origin but functions as a general infinitive in Ghandwa. The *-an* infinitive of Germanic is a different formation and is not adopted.

### §6.2 Participles

**Active participle:** suffix *-ont-* (PIE \*-ont-). Added to the thematic present stem.

Example: *légonts* (nom.sg.), stem *légont-*.

**Passive/result participle:** suffix *-to-* (PIE \*-to-). Added to the zero-grade root.

Example: *légtos* 'gathered'.

### §6.3 Verbal nouns

Three inherited verbal noun suffixes are maintained:

| Suffix | Origin | Function |
|---|---|---|
| *-tum* | PIE \*-tu- (acc.) | Infinitive/purpose (see §6.1) |
| *-ti-* | PIE \*-ti- | Abstract action noun |
| *-men-* | PIE \*-men- | Result noun, instrument noun |

Example (*leg-*): *légts* (action of gathering), *légmen* (collection, lore).

---

## §7. The past system

### §7.1 Organization

Ghandwa has a single preterite category absorbing the functions of the PIE aorist and perfect. There is no semantic split preserved between eventive past and stative/resultative past, though a small number of inherited reduplicated or root-aorist forms retain conservative morphology. There is no dental preterite at the Ghandwa level; that formation is left to daughter-language development.

Three sub-formations are distinguished:

| Formation | Source | Applies to |
|---|---|---|
| Thematic preterite | PIE imperfect | Thematic and derived verbs; the default |
| Root preterite | PIE root aorist | Inherited irregular verbs; lexically listed |
| Reduplicated preterite | PIE perfect | High-frequency relics; lexically enumerated |

### §7.2 Thematic preterite

O-grade root plus thematic vowel plus secondary endings. For most thematic verbs the preterite stem is the o-grade counterpart of the e-grade present stem.

Example: *leg-* present → *log-* preterite stem.

| Person | Ending | Form |
|---|---|---|
| 1sg | *-om* | *légom* |
| 2sg | *-es* | *léges* |
| 3sg | *-et* | *léget* |
| 1pl | *-ome* | *légome* |
| 2pl | *-ete* | *légete* (= pres. indic. 2pl) |
| 3pl | *-ont* | *légont* |

The 2pl syncretism with the present indicative is unavoidable without further innovation; disambiguation is left to context and daughters.

### §7.3 Root preterite

Zero-grade root plus secondary endings directly (no thematic vowel). Confined to inherited verbs where a root aorist is reconstructable. Lexically listed.

Confirmed: *dṓt* '(he/she) gave' — root preterite 3sg of the verb 'give'. Whether this represents a productive class or a lexicalized relic is not yet decided; it is currently classified as a relic root preterite.

### §7.4 Reduplicated preterite

[*Open. Inventory to be enumerated. Minimum: 'give', probably 'be', 'do', 'go'. See §8.*]

---

## §8. Open questions

The following issues are documented but unresolved. No settled decision should depend on them until they are closed.

| Issue | Blocking |
|---|---|
| Reduplicated preterite verb inventory | §7.4; lexical enumeration |
| Nasal-present subclassing paradigms | §3.4; at least four subtypes need worked examples |
| Athematic subjunctive paradigm | §5.1; thematization strategy needs confirmation across all athematic roots |

---

## Design notes

These notes record the basis (Italic, Germanic, or both) for non-obvious decisions, for future comparanda documentation.

| Decision | Basis |
|---|---|
| Intervocalic \*s > z (2sg *-ezi*) | Germanic (Italic keeps *-s*) |
| 1pl *-omos* | PIE \*-mos (both branches, regular reflexes) |
| Long imperative *-tōd* | Italic (Latin *-tō*; Germanic *-þau* marginal) |
| *-r* mediopassive | Italic (Germanic has no productive *-r* middle) |
| *-tum* infinitive | Italic (Latin *-tum* supine; Germanic *-an* is different) |
| Thematic preterite from PIE imperfect | Italic (Germanic does not preserve PIE imperfect) |
| Single preterite (aorist + perfect collapsed) | Germanic-leaning (Italic keeps perfect formally distinct) |
| No dental preterite at Ghandwa level | Germanic-informed; left to daughters |
| *-ye/o-* denominatives productive | Germanic-primary (Gothic/OHG *-jan*; Italic more restricted) |
| Middle/deponent marginalized | Germanic-leaning (Italic keeps deponents heavily) |
| Subjunctive, optative, active participle, passive participle, verbal nouns *-men-*, *-éye/o-* causatives | Both / PIE inheritance |

---

## Changelog

| Date | Version | Lines | Description |
|---|---|---|---|
| 2026-05-16 | 0.1 | ~220 | Initial draft. Settled decisions through §7.3 documented. Four open items listed in §8. Design notes added. |
| 2026-05-16 | 0.2 | ~225 | Athematic 3pl resolved: *santi* (CHC > CaC / CaRC convergence). Transformer gap noted. §8 reduced to three open items. |
