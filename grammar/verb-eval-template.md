# Ghandwa Verb Adoption Evaluation Template

---
last_updated: 2026-03-14
session: "Added metadata header; ğ→ɣ normalization applied (12 instances); staleness flag added"
changelog:
  - 2026-03-14 | 611 lines | Added metadata header. Applied ğ→ɣ normalization (12 instances: ğvénti→ɣvénti, ğvanénti→ɣvanénti, ğandvā́→ɣandvā́, etc.). **Staleness flag:** 7 verbs adopted here never entered into the canonical TSV: *dédōti* (\*deh₃-), *ɣvénti* (\*gʷʰen-), *βā́ti* (\*bʰeh₂-), *gvéteti* (\*gʷet-), *ðéɣveti* (\*dʰegʷʰ-), *ðoɣvéieti* (\*dʰogʷʰ-éye-), and *kléveti* (\*ḱlew-, rejected as present but adopted as *klíneti* in TSV #130). Also: TSV *píboti* (373) reflects h₃ voicing (p→b) that this template flagged as pending under *pípoti*. A dedicated session is needed to reconcile this file with the TSV. See also inline changelog table at end of file.
---

## How to use this template

Copy the blank evaluation block (§2) for each verb under consideration. Fill in sections top to bottom — the structure forces you through the comparative evidence before reaching a decision. The decision logic (§1) is a reference; don't skip steps.

---

## §1 — Decision Logic

### Step 1: Root survival

For each of the four sisters (PGmc, PItal, PC, PBS), answer: **did the branch keep the root as a verb at all?**

- **Kept** — the root continued as an active verb (even if the stem formation changed)
- **Demoted** — the root survived but shifted to a derived/stative/nominal role (e.g. \*ḱlew- → Latin *cluēre* stative)
- **Lost** — the root's verbal reflex was replaced by an innovation from a different root
- **Uncertain** — evidence is ambiguous or fragmentary

Count the result: if 3–4 branches kept it, the root is inherited and Ghandwa should keep it. If 2 kept and 2 lost/demoted, the root is probably inherited but worth examining whether the losses share a motivation. If only 1 or 0 kept it as a verb, something may have been wrong with the formation — investigate before adopting.

### Step 2: Present stem formation

For each branch that **kept** the root, identify the present stem type:

| Type | Notation | Example |
|---|---|---|
| Thematic root present | \*CéC-e-ti | \*bʰér-e-ti |
| Athematic root present | \*CéC-ti | \*h₁és-ti |
| Reduplicated thematic | \*Ci-CC-é-ti | \*pi-ph₃-é-ti |
| Reduplicated athematic | \*Ci-CéC-ti | \*dé-deh₃-ti |
| Nasal infix | \*C-né-C-ti / \*C-n-C-énti | \*li-né-kʷ-ti |
| Nasal suffix | \*CC-n-é-ti | — |
| yé-present (intransitive) | \*CC-yé-ti | \*bʰr̥kʷ-yé-ti |
| éye-present (causative) | \*CoC-éye-ti | \*mon-éye-ti |
| ské-present (inchoative) | \*CC-sḱé-ti | \*gn̥h₃-sḱé-ti |
| Stative (ēh₁) | \*CC-éh₁-ti | \*ḱlu-éh₁-ti |
| Other / unclear | describe | — |

**Convergence test:** Do the branches that kept the root agree on the stem type?

- **Same type across ≥2 branches** → that is the inherited formation; Ghandwa should use it
- **Each branch has a different type** → look for the most archaic (least derived) formation; check Sanskrit/Greek/Hittite as tiebreakers if needed
- **One branch innovated, others agree** → go with the agreeing branches

### Step 3: Ablaut and accent

Note the root vowel grade and accent position for the present stem. For Ghandwa, accent matters for pretonic shortening and the transformer pipeline.

- Full grade root (\*CéC-) is the default for thematic presents
- Zero grade root (\*CC-) is typical for reduplicated presents, nasal infixes, and yé-presents
- o-grade (\*CoC-) signals a causative or iterative

### Step 4: Ghandwa decision

Apply the standard decision rule:

1. If PGmc, PItal, and PC agree on root + stem type → that is the Ghandwa form
2. If they diverge through independent innovation → Ghandwa stays at the PIE form
3. If all three independently replaced the verb → the PIE form may have been unstable; adopt with caution and note the concern

### Step 5: Transformer check

Run the chosen PIE input through the transformer. Note:

- Does the output match the expected Ghandwa surface form?
- Any surviving ˀ (laryngeal leakage)?
- Any problematic clusters (CCC)?
- Does the 3sg ~ 3pl pair show the expected ablaut pattern?

---

## §2 — Blank Evaluation Block

```
### ROOT: *___- "___"

**PIE reconstruction:** *___
**Semantic field:** ___
**Motivation for inclusion:** ___

#### Comparative evidence

| Branch | Status | Verb form | Present stem type | Notes |
|--------|--------|-----------|-------------------|-------|
| PGmc   |        |           |                   |       |
| PItal  |        |           |                   |       |
| PC     |        |           |                   |       |
| PBS    |        |           |                   |       |

**Tiebreaker witnesses (if needed):**
- Sanskrit: ___
- Greek: ___
- Hittite: ___

#### Convergence

- Root survival: _/4 kept, _/4 demoted, _/4 lost
- Stem type consensus: ___
- Ablaut/accent: ___

#### Ghandwa decision

- **Adopt / Reject / Defer**: ___
- **Chosen present stem:** *___ → Ghandwa ___
- **3sg ~ 3pl:** *___ ~ *___ → ___ ~ ___
- **Verb class (for lexicon):** ___
- **Rationale:** ___

#### Transformer output

- Input: `___`
- Output: ___
- Warnings: ___

#### Cross-references

- Existing lexicon entries derived from this root: ___
- Lore/theological connections: ___
```

---

## §3 — Worked Examples

### ROOT: \*peh₃- "drink"

**PIE reconstruction:** \*pi-ph₃-é-ti ~ \*pi-ph₃-ó-nti (reduplicated thematic)
**Semantic field:** food/drink; ritual; sacred
**Motivation for inclusion:** pōklom (drinking cup) already in lexicon; méðu (mead) present; libation central to ritual; core daily verb

#### Comparative evidence

| Branch | Status | Verb form | Present stem type | Notes |
|--------|--------|-----------|-------------------|-------|
| PGmc | Lost | replaced by \*drinkaną | — | nominal derivatives survived (\*pōkla-) |
| PItal | Kept | \*bibō (Latin) | reduplicated thematic | dissimilatory voicing p...p → b...b |
| PC | Kept | \*ib-e-ti (OIr *ibid*) | reduplicated thematic | p-loss destroyed both p's |
| PBS | Kept | \*pi-ti (Lith *gerti* replaced; but OCS *piti*) | root present (simplified) | reduplication lost early in Slavic |

**Tiebreaker witnesses:**
- Sanskrit: *píbati* — reduplicated thematic, b-dissimilation (parallel to Italic)
- Greek: — (replaced by πίνω, nasal infix from different root sense)
- Hittite: — (not clearly attested)

#### Convergence

- Root survival: 3/4 kept, 0/4 demoted, 1/4 lost (PGmc)
- Stem type consensus: PItal + PC + Sanskrit agree on **reduplicated thematic**; PGmc irrelevant (lost)
- Ablaut/accent: zero-grade root in reduplication (\*pi-pH₃-é-), o-grade thematic vowel confirmed by Latin/Sanskrit

#### Ghandwa decision

- **Adopt**
- **Chosen present stem:** \*pi-ph₃-é-ti (reduplicated thematic)
- **3sg ~ 3pl:** \*pi-ph₃-é-ti ~ \*pi-ph₃-ó-nti → pípoti ~ píponti
- **Verb class:** reduplicated thematic
- **Rationale:** 3/4 branches kept the root; 2/4 (+ Sanskrit) agree on reduplicated thematic present; PGmc replacement is an isolated innovation; formation is archaic and well-reconstructed

#### Transformer output

- 3sg input: `píph₃eti`
  - H-A: h₃ colors following e → o: píph₃oti
  - H-B3: h₃ adjacent to vowel → drops: pípoti
  - **Output: pípoti** ✓
- 3pl input: `píph₃onti`
  - H-A: h₃ adjacent to o — already o, no change
  - H-B3: h₃ adjacent to vowel → drops: píponti
  - **Output: píponti** ✓
- Warnings: none — clean derivation both ways

#### Cross-references

- Existing: pōklom (#219, drinking cup, from same root via \*péh₃-tl-om)
- Lore: libation in ritual contexts; Agnis consumes offerings, community drinks méðu; fire-and-drink symmetry

---

### ROOT: \*ḱlew- "hear"

**PIE reconstruction:** \*ḱléw-e-ti ~ \*ḱléw-o-nti (thematic root present)
**Semantic field:** perception; fame/renown; knowledge
**Motivation for inclusion:** klévos, klutom, klutós already in lexicon; perception pair with véideti (see/know); IE poetic tradition: fame is "what is heard"

#### Comparative evidence

| Branch | Status | Verb form | Present stem type | Notes |
|--------|--------|-----------|-------------------|-------|
| PGmc | Lost | replaced by \*hauzijaną (from \*h₂ḱows- "ear") | — | nominal derivatives survived: \*hlūda- "loud", \*hleuma- |
| PItal | Demoted | Latin *cluēre* "be reputed" | stative (ēh₁) | shifted to stative "be heard"; active "hear" replaced by *audiō* |
| PC | Kept | OIr *ro·cluinethar*, Welsh *clywed* | possibly nasal suffix (rebuilt) | sole western branch to keep it as active "hear" |
| PBS | Kept | Lith *klausýti*, OCS *slušati* | éye-causative (rebuilt) | satemized; root kept but stem rebuilt to causative |

**Tiebreaker witnesses:**
- Sanskrit: *śṛṇóti* — nasal infix present from same root (\*ḱl̥-né-w-ti), satemized
- Greek: *κλύω* — thematic present (root present or secondary thematic), active "hear"
- Hittite: — (not clearly attested for this root)

#### Convergence

- Root survival: 2/4 kept, 1/4 demoted (PItal), 1/4 lost (PGmc)
- Stem type consensus: **no agreement on stem type** — PC rebuilt (nasal?), PBS rebuilt (causative), PItal narrowed (stative), PGmc lost it. Sanskrit has nasal infix; Greek has thematic. The simplest archaic formation is the **thematic root present** \*ḱléw-e-ti, which Greek *κλύω* may reflect
- Ablaut/accent: full-grade root expected for thematic present

#### Ghandwa decision

- **Adopt**
- **Chosen present stem:** \*ḱléw-e-ti (thematic root present)
- **3sg ~ 3pl:** \*ḱléw-e-ti ~ \*ḱléw-o-nti → kléveti ~ klévonti
- **Verb class:** thematic root
- **Rationale:** root is clearly inherited (3/4 retained it in some form); each branch independently rebuilt or replaced the stem, meaning no single innovation is shared — Ghandwa stays at the PIE level; thematic root present is the simplest formation consistent with Greek evidence; feeds existing klévos/klutom/klutós family

#### Transformer output

- Input: `ḱléweti ~ ḱléwonti`
- Output: kléveti ~ klévonti (centumization ḱ→k; no other rules fire)
- Warnings: none

#### Cross-references

- Existing: klévos (#130), klutom (#133), klutós (#134), klíneti (#131, different root but similar semantic field)
- Lore: perception-pair with véideti; "hearing" as channel of fame and tradition; danwiweits "well-watcher" is the sight-based guardian — a hearing-based complement may exist in priestly vocabulary

---

### ROOT: \*deh₃- "give"

**PIE reconstruction:** \*dé-deh₃-ti ~ \*di-dh₃-énti (reduplicated athematic)
**Semantic field:** ritual; social/legal; core transitive
**Motivation for inclusion:** dṓnom (#44, gift) already in lexicon from \*deh₃-no-m; dapnóm (#33, sacrifice) from same root via \*dh₂p-; core verb for oath-giving, offering to Agnis, βoiðā́ contract-making; no language works without "give"

#### Comparative evidence

| Branch | Status | Verb form | Present stem type | Notes |
|--------|--------|-----------|-------------------|-------|
| PGmc | Lost | replaced by \*gebaną (from \*gʰebʰ-) | — | total loss — no verbal or nominal reflex; even "gift" replaced |
| PItal | Kept | Latin *dō, dare, dedī, datum* | present rebuilt (short-vowel root pres.); perfect *dedī* preserves reduplication | primary "give" verb throughout Italic; Oscan *deded* confirms |
| PC | Kept (partially) | Welsh *rhoddi* < *ro-* + \*dā-; OIr *dán* "gift" | unclear (preverbed in Goidelic; Brythonic clearer) | Goidelic partially displaced by \*bʰer- compounds (*do-beir* "gives") |
| PBS | Kept | Lith *dúoti*, OCS *dati*, *damь* | athematic (reduplication lost) | primary "give" verb throughout; OCS *damь* athematic 1sg |

**Tiebreaker witnesses:**
- Sanskrit: *dádāti* ~ *dádati* — reduplicated athematic, canonical; confirms PIE formation unambiguously
- Greek: *δίδωμι* — reduplicated athematic (with innovative ω-grade in sg.); confirms independently
- Hittite: *dāi* "takes" — same root but semantic shift to "take"; root antiquity goes back to Anatolian split

#### Convergence

- Root survival: 3/4 kept, 0/4 demoted, 1/4 lost (PGmc)
- Stem type consensus: no agreement across western branches — PItal rebuilt present, PC preverbed, PBS dropped reduplication. But Sanskrit *dádāti* and Greek *δίδωμι* both independently confirm **reduplicated athematic** as the PIE formation. Western simplifications are all independent innovations.
- Ablaut/accent: full-grade root in 3sg (\*dé-deh₃-), zero-grade in 3pl (\*di-dh₃-); accent on reduplication syllable in sg, on ending in pl — standard athematic pattern

#### Ghandwa decision

- **Adopt**
- **Chosen present stem:** \*dé-deh₃-ti ~ \*di-dh₃-énti (reduplicated athematic)
- **3sg ~ 3pl:** \*dédeh₃ti ~ \*didh₃énti → dédōti ~ didónti
- **Verb class:** reduplicated athematic
- **Rationale:** 3/4 branches kept the root; reduplicated athematic confirmed by Sanskrit and Greek independently; every western branch simplified differently (PItal rebuilt present, PC preverbed, PBS dropped reduplication), meaning no simplification is inherited — Ghandwa stays at the PIE level. Structurally parallel to ðḗti ~ ðánti (\*dʰéh₁-ti), forming a natural class of reduplicated athematic presents. PGmc's total loss is an isolated innovation.

#### Transformer output

- 3sg input: `dédeh₃ti`
  - h₃ colors preceding e → o: dédoh₃ti
  - VH→V̄ (o before h₃, h₃ before C): dédōti
  - **Output: dédōti** ✓
- 3pl input: `didh₃énti`
  - h₃ colors following é → ó: didh₃ónti
  - H-B3 (h₃ adjacent to vowel, drops): didónti
  - **Output: didónti** ✓
- Warnings: none — clean derivation both ways

#### Notes

First Ghandwa verb with overt reduplication in the present tense (ðḗti lost its historical reduplication). The sg/pl vowel alternation dédōti ~ didónti (ō vs. o, full-grade vs. zero-grade root, plus i-reduplication in pl.) defines what "reduplicated athematic" looks and sounds like in Ghandwa. Pairs with ðḗti ~ ðánti as a natural paradigmatic class.

#### Cross-references

- Existing: dṓnom (#44, gift, from \*deh₃-no-m); dapnóm (#33, sacrifice, from \*dh₂p-nóm — same root, zero-grade with p-suffix)
- Lore: ritual offering to Agnis; oath-giving in the Woman in the Well covenant; βoiðā́ contract formalization; the Ash-Gatherer's gift economy (tests through generosity/withholding)

---

### ROOT: \*gʷʰen- "strike, kill"

**PIE reconstruction:** \*gʷʰén-ti ~ \*gʷʰn̥-énti (root athematic)
**Semantic field:** violence; smithing; sacred
**Motivation for inclusion:** Every blow of melðanjos is this verb. martís/martus (death/dead) from \*mr̥- are in the lexicon but that root means "die" — there's no word for the act of striking or killing. Core transitive for warfare (katús, kórios), sacrifice (dapnóm), and the forge cosmogony.

#### Comparative evidence

| Branch | Status | Verb form | Present stem type | Notes |
|--------|--------|-----------|-------------------|-------|
| PGmc | Lost | replaced by \*slahaną "strike", \*daudijaną "kill" | — | nominals survived: \*banō "killer" (OE *bana*), \*gunþō "battle" (OE *gūþ*, ON *gunnr*) from zero-grade \*gʷʰn̥- |
| PItal | Partially kept | Latin *-fendō* (in *dēfendō*, *offendō*) | dental extension \*gʷʰen-d- | simplex lost; "kill" replaced by *occīdō*, *necō*, *interficiō* |
| PC | Kept | OIr *gonaim* "I wound, slay"; Welsh *gwanu* "to stab" | o-grade thematic (rebuilt) | root kept as active verb; stem rebuilt from athematic to o-grade |
| PBS | Kept (shifted) | OCS *ženǫ* "I drive"; Lith *genù* "I drive" | thematic (rebuilt) | semantic shift "strike" → "drive, chase"; stem rebuilt |

**Tiebreaker witnesses:**
- Sanskrit: *hánti* ~ *ghnánti* — root athematic, canonical; full-grade sg., zero-grade pl.; confirms PIE formation unambiguously
- Greek: *θείνω* "I strike" (rebuilt thematic); *φόνος* "murder" < \*gʷʰón-os; *ἔπεφνον* (redupl. aorist) — root preserved, present rebuilt
- Hittite: *kuenzi* "he kills" — root athematic (\*gʷʰén-ti with Hittite -zi ending); independent Anatolian confirmation

#### Convergence

- Root survival: 2/4 kept (PC, PBS), 1/4 partially kept (PItal), 1/4 lost (PGmc)
- Stem type consensus: no western branch preserved the root athematic — PC rebuilt to o-grade, PBS rebuilt to thematic, PItal extended with dental. But Sanskrit *hánti* and Hittite *kuenzi* both independently confirm **root athematic** as the PIE formation, from opposite ends of the family tree. Every western innovation is independent.
- Ablaut/accent: full-grade root \*gʷʰén- in sg., zero-grade \*gʷʰn̥- in pl.; accent on root in sg., on ending in pl. — textbook root athematic, identical to βérti ~ βarénti

#### Ghandwa decision

- **Adopt**
- **Chosen present stem:** \*gʷʰén-ti ~ \*gʷʰn̥-énti (root athematic)
- **3sg ~ 3pl:** \*gʷʰénti ~ \*gʷʰn̥énti → ɣvénti ~ ɣvanénti
- **Verb class:** athematic root
- **Rationale:** Root clearly inherited — attested from Anatolian to Indo-Iranian to Celtic to Balto-Slavic. Root athematic confirmed by Sanskrit and Hittite independently (both major first-order branches). Every western branch rebuilt or replaced independently; no innovation is inherited. Ghandwa stays at the PIE level. Joins the existing athematic root class (ésti, éiti, stā́ti, βérti, ðḗti); first with labiovelar aspirate onset, giving distinctive ɣv- surface.

#### Transformer output

- 3sg input: `gʷʰénti`
  - No laryngeals or clusters to resolve in Stage 1
  - Stage 2: gʷʰ → ɣʷ (aspirate fricativization)
  - **Output: ɣʷénti** → orthographic **ɣvénti** ✓
- 3pl input: `gʷʰn̥énti`
  - Stage 2: n̥ → an (syllabic resonant vocalization)
  - Stage 2: gʷʰ → ɣʷ (aspirate fricativization)
  - **Output: ɣʷanénti** → orthographic **ɣvanénti** ✓
- Warnings: none — clean derivation both ways

#### Notes

The 3sg ~ 3pl pair ɣvénti ~ ɣvanénti shows textbook athematic ablaut: full-grade root with accent in the singular, zero-grade root with accent on the ending in the plural — the same pattern as βérti ~ βarénti. The syllabic nasal vocalization (n̥ → an) in the plural parallels βr̥ → βar. These two verbs form a minimal pair illustrating how different root-initial consonants interact with the same athematic ablaut pattern.

The Hittite confirmation is worth emphasizing — *kuenzi* is the only tiebreaker witness in any evaluation so far that reaches into Anatolian, making \*gʷʰen- the most securely reconstructed root athematic present in the template.

#### Cross-references

- Existing: martís (#165, death), martus (#166, dead) — from \*mr̥-, the intransitive "die"; ɣvénti supplies the transitive counterpart "strike, kill." Also katús (#124, battle), kórios (#136, army), meltrom (#358, hammer), melðanjos (#359, divine hammer), dapnóm (#33, sacrifice)
- Lore: Agnis melðanjṓ ɣvénti — "Agnis strikes with Melðanjos" (SOV; instrumental); the forging of the world; every forge-blow recapitulates creation; sacrifice as ritually striking the offering. The verb is the action behind the entire smith theology.

---

### ROOT: \*bʰeh₂- "speak (authoritatively)"

**PIE reconstruction:** \*bʰéh₂-ti ~ \*bʰh₂-énti (root athematic)
**Semantic field:** speech; sacred; legal
**Motivation for inclusion:** no "speak" verb in lexicon; this root fills the sacred/authoritative register — prophecy, oath-formula, ritual declaration. Complements \*gʷet- for everyday speech.

#### Comparative evidence

| Branch | Status | Verb form | Present stem type | Notes |
|--------|--------|-----------|-------------------|-------|
| PGmc | Lost (verb) | no verb; \*bōnō "prayer" nominal only | — | root survived nominally |
| PItal | Kept (defective) | Latin *for, fārī* | root present (deponent, defective) | restricted to sacred/legal register; hugely productive nominals: *fāma*, *fātum*, *fābula*, *fās* |
| PC | Lost | no clear verbal reflex | — | — |
| PBS | Uncertain | OCS *bajati* "tell, enchant" | debated | semantic shift; connection questioned |

**Tiebreaker witnesses:**
- Sanskrit: — (not clearly attested as independent verb)
- Greek: φημί ~ φαμέν — **root athematic, canonical**; full-grade φη- (\*bʰéh₂-) in sg., zero-grade φα- (\*bʰh₂-) in pl.; strongest witness
- Hittite: — (not attested)

#### Convergence

- Root survival: 1/4 kept (PItal, defective), 0/4 demoted, 2/4 lost, 1/4 uncertain
- Stem type consensus: weak across 4sl. Greek φημί independently confirms **root athematic**. Latin deponent *fārī* is consistent with athematic origin (deponent reflexes of old athematics are common in Latin).
- Ablaut/accent: full-grade \*bʰéh₂- in sg., zero-grade \*bʰh₂- in pl. H₂ colors and lengthens in sg.; vocalizes to *a* in pl. zero-grade cluster.

#### Ghandwa decision

- **Adopt**
- **Chosen present stem:** \*bʰéh₂-ti ~ \*bʰh₂-énti (root athematic)
- **3sg ~ 3pl:** \*bʰéh₂ti ~ \*bʰh₂énti → βā́ti ~ βánti
- **Verb class:** athematic root
- **Register:** sacred/formal — prophecy, oath, ritual declaration. Contrasts with gvéteti (everyday "say").
- **Rationale:** Greek φημί independently confirms root athematic. Latin *fārī* restricted to sacred/legal register, which Ghandwa preserves as a register distinction. Weak 4sl convergence acknowledged, but the root is clearly PIE and the formation is confirmed by the best single witness available (Greek). Adopted alongside thematic \*gʷet- to create a productive register split.

#### Transformer output

- 3sg input: `bʰéh₂ti`
  - H-A: h₂ colors preceding é → á: bʰáh₂ti
  - H-B2: VH→V̄ (á before h₂, h₂ before C): bʰā́ti, h₂ drops
  - Stage 2: bʰ → β
  - **Output: βā́ti** ✓
- 3pl input: `bʰh₂énti`
  - H-A: h₂ colors following é → á: bʰh₂ánti
  - H-B3: h₂ adjacent to vowel → drops: bʰánti
  - Stage 2: bʰ → β
  - **Output: βánti** ✓
- Warnings: none

#### Notes

The sg/pl ablaut βā́ti ~ βánti is clean: long ā in the singular (from laryngeal coloring + compensatory lengthening), short a in the plural (from h₂ coloring é→á then dropping). Joins the athematic class alongside ðḗti ~ ðánti — both laryngeal roots with the same kind of long/short vowel alternation between sg. and pl. Register: sacred, prophetic, legal. Latin *fātum* "fate" = "that which has been spoken (by βā́ti)" — the Ghandwa cognate would be a productive source for legal/theological vocabulary.

#### Cross-references

- Existing: varðom (#296, word), vāt- family (#372–375, poet/lyric/inspiration/frenzy — different root \*weh₂t-), βoiðā́ (#325, oath/pledge), ɣandvā́ (#67, tongue/language)
- Lore: oath formulae; Strasbourg oath; ritual invocation of Agnis; the danwiweits pronouncing sanctuary boundaries

---

### ROOT: \*gʷet- "say, tell"

**PIE reconstruction:** \*gʷét-e-ti ~ \*gʷét-o-nti (thematic root present)
**Semantic field:** speech; everyday
**Motivation for inclusion:** everyday "say/tell" verb; complements βā́ti (sacred register). Needed for ordinary dialogue, narrative, reported speech.

#### Comparative evidence

| Branch | Status | Verb form | Present stem type | Notes |
|--------|--------|-----------|-------------------|-------|
| PGmc | Kept | \*kweþaną (Gothic *qiþan*, OE *cweþan*) | thematic (strong V) | primary "say" verb in early Germanic |
| PItal | Lost | — | — | "say" replaced by *dīcō* (\*deyk-) |
| PC | Lost | — | — | "say" replaced by *as-beir* (compound of \*bʰer-) |
| PBS | Lost | — | — | no clear reflex |

**Tiebreaker witnesses:**
- Sanskrit: — (no clear reflex)
- Greek: — (no clear reflex)
- Hittite: — (no clear reflex)

#### Convergence

- Root survival: 1/4 kept (PGmc only), 0/4 demoted, 3/4 lost
- Stem type consensus: PGmc alone; thematic root present. No independent confirmation.
- Ablaut/accent: e-grade root, thematic vowel. Straightforward.

#### Ghandwa decision

- **Adopt (with caveat)**
- **Chosen present stem:** \*gʷét-e-ti ~ \*gʷét-o-nti (thematic root present)
- **3sg ~ 3pl:** \*gʷéteti ~ \*gʷétonti → gvéteti ~ gvétonti
- **Verb class:** thematic root
- **Register:** everyday speech — ordinary saying, telling, narrating. Contrasts with βā́ti (sacred/formal).
- **Rationale:** weakest 4sl support of any adopted verb — PGmc only. But the root is phonologically clean PIE (\*gʷet- has good PIE shape), the thematic formation is the default unmarked type, and the semantic need is acute. The fact that every branch *replaced* the "say" verb independently (each with a different semantic shift: point, carry, lip-move) suggests the *slot* was volatile, not that this particular root was defective. PGmc's retention may be conservative. Caveat noted: this is the one adoption driven more by need than by comparative convergence.

#### Transformer output

- 3sg input: `gʷéteti`
  - No laryngeals, no clusters
  - **Output: gvéteti** ✓ (gʷ → gv orthographically)
- 3pl input: `gʷétonti`
  - No laryngeals, no clusters
  - **Output: gvétonti** ✓
- Warnings: none — trivially clean

#### Notes

Phonologically the simplest verb in the entire template — nothing fires except the orthographic gʷ → gv. Joins the thematic root class alongside édeti, véideti, sékveti, etc. The register pairing βā́ti (sacred) / gvéteti (everyday) parallels Latin *fārī* / *dīcō* and may be one of the oldest semantic distinctions in the Ghandwa speech-verb vocabulary.

#### Cross-references

- Existing: varðom (#296, word), ɣandvā́ (#67, tongue/language), βā́ti (sacred speech counterpart)
- Lore: everyday narrative; reported speech in myths; quotative frame verb ("he said")

---

### ROOT: \*dʰegʷʰ- "burn"

**PIE reconstruction:** \*dʰégʷʰ-e-ti ~ \*dʰégʷʰ-o-nti (thematic root present)
**Semantic field:** fire; sacred; cosmology
**Motivation for inclusion:** ðéɣvis (#35, fire) from same root; Agnis's fundamental action; "to burn" is the core verb of the entire theology

#### Comparative evidence

| Branch | Status | Verb form | Present stem type | Notes |
|--------|--------|-----------|-------------------|-------|
| PGmc | Lost | replaced by \*brinnaną / \*brennijaną | — | possible nominal \*dagaz "day" (debated) |
| PItal | Lost | replaced by *ūrō*, *cremō*, *incendō* | — | nominal *focus* possibly related (debated) |
| PC | Lost | no clear verbal reflex | — | — |
| PBS | Kept | Lith *dègti*, OCS *žegǫ* | thematic | primary "burn" verb; satemized |

**Tiebreaker witnesses:**
- Sanskrit: *dáhati* — thematic root present, canonical; primary "burn" verb
- Avestan: *dažaiti* — thematic root present, independently confirms Sanskrit
- Albanian: *djeg* "I burn" — kept the verb

#### Convergence

- Root survival: 1/4 kept (PBS), 3/4 lost
- Stem type consensus: weak across 4sl. Sanskrit + Avestan + PBS agree on **thematic root present**. Three independent confirmations outside the western branches.
- Ablaut/accent: e-grade root, thematic vowel. Straightforward.

#### Ghandwa decision

- **Adopt**
- **Chosen present stem:** \*dʰégʷʰ-e-ti ~ \*dʰégʷʰ-o-nti (thematic root present)
- **3sg ~ 3pl:** \*dʰégʷʰeti ~ \*dʰégʷʰonti → ðéɣveti ~ ðéɣvonti
- **Verb class:** thematic root
- **Rationale:** weak 4sl support (1/4), but Sanskrit + Avestan + Albanian independently confirm thematic root present. Root is clearly PIE and theologically indispensable — ðéɣvis is already in the lexicon. The western losses are independent replacements (each branch chose a different substitute), suggesting the slot was volatile but the root was viable.

#### Transformer output

- 3sg input: `dʰégʷʰeti`
  - Stage 2: dʰ → ð, gʷʰ → ɣʷ
  - **Output: ðéɣveti** ✓
- 3pl input: `dʰégʷʰonti`
  - Stage 2: dʰ → ð, gʷʰ → ɣʷ
  - **Output: ðéɣvonti** ✓
- Warnings: none

#### Present active participle

\*dʰegʷʰ-ó-nt-s → ðeɣvónts (nom.sg.m.), gen. ðeɣvantés. Standard thematic present participle. Basis for Agnis epithets:

- *ðeɣvóntios* — "pertaining to the blazing one"; solemn/hymnic epithet
- *ðeɣvontiskos* — "the little blazing one"; folk/affectionate diminutive for Baby Agnis

#### Cross-references

- Existing: ðéɣvis (#35, fire, from same root); pūr (#224, fire); agnís (#1, fire deity); engman (#356, sacred fire-nature)
- Lore: Agnis ðéɣveti — "Agnis burns"; the inherent, divine state. The basic verb of the entire theology.

---

### ROOT: \*dʰogʷʰ-éye- "cause to burn, kindle, ignite" (causative of \*dʰegʷʰ-)

**PIE reconstruction:** \*dʰogʷʰ-éye-ti ~ \*dʰogʷʰ-éye-nti (éye-causative)
**Semantic field:** fire; ritual; smithing
**Motivation for inclusion:** causative counterpart to ðéɣveti; "kindle, ignite" is the human ritual action — the priest kindles the offering, the smith kindles the forge. First éye-causative in Ghandwa.

#### Comparative evidence

| Branch | Status | Verb form | Present stem type | Notes |
|--------|--------|-----------|-------------------|-------|
| PGmc | Lost | — | — | — |
| PItal | Lost | — | — | — |
| PC | Lost | — | — | — |
| PBS | Uncertain | — | — | causative not clearly attested separately |

**Tiebreaker witnesses:**
- Sanskrit: *dāháyati* "causes to burn" — éye-causative, canonical; independently confirms the formation
- Avestan: parallel causative attested

#### Convergence

- Root survival: 0/4 clearly kept as a separate causative
- Stem type consensus: Sanskrit *dāháyati* independently confirms **éye-causative** as a PIE formation. The o-grade + -éye- is the standard productive PIE causative — not an innovation but the regular derivation.
- Ablaut: o-grade root (\*dʰogʷʰ-), accent on -éye- suffix

#### Ghandwa decision

- **Adopt**
- **Chosen present stem:** \*dʰogʷʰ-éye-ti ~ \*dʰogʷʰ-éye-nti (éye-causative)
- **3sg ~ 3pl:** \*dʰogʷʰéyeti ~ \*dʰogʷʰéyenti → ðoɣvéieti ~ ðoɣvéienti
- **Verb class:** éye-causative
- **Rationale:** regular PIE causative formation from an adopted root. Sanskrit confirms independently. First éye-causative in Ghandwa — fills the last empty slot in the verb class inventory. Semantically distinct from basic ðéɣveti: ðéɣveti = "burns" (state/action), ðoɣvéieti = "kindles, ignites, sets on fire" (deliberate causation).

#### Transformer output

- 3sg input: `dʰogʷʰéyeti`
  - Stage 2: dʰ → ð, gʷʰ → ɣʷ, y → j (but éye → éie in orthography)
  - **Output: ðoɣvéieti** ✓
- 3pl input: `dʰogʷʰéyenti`
  - Same processes
  - **Output: ðoɣvéienti** ✓
- Warnings: none

#### Notes

Semantic split with ðéɣveti: the basic verb is the divine state (Agnis ðéɣveti — "Agnis burns, inherently"); the causative is the human ritual action (a smith or priest ðoɣvéieti — "kindles the forge/offering"). This parallels the Catholic distinction between eternal light and the act of lighting a candle. First éye-causative in the lexicon.

Agent noun for "fire-starter" epithet: pending formation decision (options include \*-tor agent suffix, compound with pūr, etc.).

#### Cross-references

- Existing: ðéɣveti (basic verb counterpart); ðéɣvis (#35, fire); meltrom (#358, hammer); dapnóm (#33, sacrifice)
- Lore: the smith ðoɣvéieti the forge; the priest ðoɣvéieti the offering; fire-starter epithet for Agnis (pending)

---

## §4 — Quick-Reference: PIE Present Stem Types

For convenience when filling in evaluations. This is not exhaustive — just the types most commonly encountered in western IE verb adoption.

**Primary (underived):**
- **Root athematic:** \*CéC-ti ~ \*CC-énti — the oldest type; Ghandwa examples: ésti, éiti, stā́ti, βérti, ðḗti, ɣvénti, βā́ti
- **Root thematic:** \*CéC-e-ti ~ \*CéC-o-nti — very common; Ghandwa examples: édeti, véideti, sékveti, gvéteti, ðéɣveti
- **Reduplicated thematic:** \*Ci-CC-é-ti — archaic; often with zero-grade root; Ghandwa example: pípoti
- **Reduplicated athematic:** \*Ci-CéC-ti — mostly for \*deh₃- "give" (dédōti) and \*dʰeh₁- "put" (ðḗti)

**Derived (suffixed):**
- **Nasal infix:** \*C-né-C-ti ~ \*C-n-C-énti — transitivizer; klíneti is the only Ghandwa example so far
- **yé-present:** \*CC-yé-ti — intransitive/stative/denominal; βarkiéti is the only example
- **éye-causative:** \*CoC-éye-ti — causative/factitive; Ghandwa example: ðoɣvéieti
- **ské-inchoative:** \*CC-sḱé-ti — becoming/beginning; none yet in Ghandwa

**When in doubt:** the thematic root present is the default "unmarked" type. If the comparative evidence is messy and no stem type has clear majority support, a thematic root present is the safest Ghandwa choice — it's productive, phonologically transparent, and doesn't commit to any branch-specific innovation.

---

## Change Log

| Timestamp (ISO 8601) | Lines | Changes |
|---|---|---|
| 2026-03-10T05:25:05-04:00 | 244 | Initial creation. Decision logic (§1), blank template (§2), worked examples for \*peh₃- and \*ḱlew- (§3), PIE present stem quick-reference (§4). |
| 2026-03-10T05:35:00-04:00 | 301 | Added \*deh₃- "give" worked example to §3. Decision: **adopted** as reduplicated athematic dédōti ~ didónti. Updated §4 quick-reference. |
| 2026-03-10T05:45:00-04:00 | 361 | Added \*gʷʰen- "strike, kill" worked example to §3. Decision: **adopted** as athematic root ɣvénti ~ ɣvanénti. Hittite tiebreaker. Updated §4 quick-reference. |
| 2026-03-10T05:50:00-04:00 | 363 | Fixed \*gʷʰen- cross-references: corrected example sentence to SOV word order (Agnis melðanjṓ ɣvénti) and instrumental case (melðanjṓ, not accusative melðanjom). |
| 2026-03-10T06:10:00-04:00 | 480 | Added \*bʰeh₂- "speak (authoritatively)" and \*gʷet- "say, tell" worked examples to §3. Both adopted: βā́ti ~ βánti (athematic root, sacred register) and gvéteti ~ gvétonti (thematic root, everyday register). Updated §4 quick-reference. |
| 2026-03-10T06:15:00-04:00 | 480 | Fixed \*bʰeh₂- 3pl: βanénti → βánti. H-B3 (H adjacent to vowel) applies, not H-B5 (H between consonants). Corrected transformer derivation and notes. |
| 2026-03-10T06:25:00-04:00 | 487 | Confirmed \*peh₃- transformer output: pípoti ~ píponti ✓. Updated from pending to confirmed. Updated §4 quick-reference. |
| 2026-03-10T06:45:00-04:00 | 602 | Added \*dʰegʷʰ- "burn" (thematic root, ðéɣveti ~ ðéɣvonti) and \*dʰogʷʰ-éye- "kindle" (éye-causative, ðoɣvéieti ~ ðoɣvéienti) to §3. First causative in lexicon. Participle ðeɣvónts + epithet candidates noted. Updated §4 quick-reference. |
