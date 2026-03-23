# Ghandwa Daughter Languages

---
last_updated: 2026-03-19T18:10-04:00
session: "GitHub prep — consolidated daughters-framework.md + daughters-sprachbund.md + decisions-cs-dialects.md into single file"
changelog:
  - 2026-03-19T18:10-04:00 | 657 lines | Consolidated three files into one. A/B/C staged framework (from daughters-framework.md, 2026-03-18) is primary content. Seven-zone dialect geography (from daughters-sprachbund.md, 2026-03-08 ChatGPT export) demoted to Appendix A as provisional historical notes. CS/dialect decisions (from decisions_summary_utf8.pdf, 2026-03-01 ChatGPT export) placed in Appendix B as provisional notes. Both appendices flagged for future harvesting/reconciliation with the A/B/C framework.
---

This document records the daughter-language framework for Ghandwa. All rules here operate on Ghandwa surface forms — they are post-Ghandwa, not part of the parent-language derivation.

The primary framework (§§1–9) uses a staged A/B/C branch model. Provisional material from earlier sessions is preserved in the appendices for future harvesting.

---

## 1. Current overall framing

The daughter-language project is a staged historical framework with three main daughter branches.

### Preferred structure

- **Stage 0 = Ghandwa**
- **Stage 1 = Late Common Ghandwa**
- **Stage 2 = early daughter divergence into A / B / C**
- **Stage 3 = later branch-specific developments**

The project is now being thought of as a **3 x 3 matrix**:

- **three common late-Ghandwa changes**
- **three domains of divergent A/B/C response**
- **three branch-specific later developments**

The current preference is to refer to the three main daughters simply as:

- **A**
- **B**
- **C**

Possible later subbranches can be labeled in a nested way, for example:

- **AA, AB**
- **BA, BB, BC**
- **CA, CB**

or in a stage-sensitive way if needed later.

---

## 2. Stage 1: Late Common Ghandwa

These are the currently landed-on **shared** changes.

### 1.1 Prosodic restructuring

This is being treated as one change with two linked aspects:

- **pitch accent becomes more stress-like**
- **final-syllable accent is banned**
- if accent would have fallen on the final syllable, it retracts one syllable left

### 1.2 Nasal-obstruent assimilation

Current formulation:

- **n > m / _ {p b ɸ β}**
- **m > n / _ {t d θ ð s k g ɣ kʷ gʷ ɣʷ}**

### 1.3 Trimoraic glide-sequence regularization

Current formulation:

- **Vːj > Vj**
- **Vːw > Vw**

And, **if such sequences ever arise**:

- **Vjː > Vj**
- **Vwː > Vw**

Interpretation:

- trimoraic tautosyllabic vowel+glide sequences are simplified to ordinary bimoraic diphthongs
- this rule is meant to apply only to **tautosyllabic** sequences

### Summary of Stage 1

```text
Stage 1: Late Common Ghandwa

1.1  pitch accent > stress-like prominence
     final-syllable accent prohibited
     final accent retracts one syllable left

1.2  nasal-obstruent assimilation
     n > m / _ {p b ɸ β}
     m > n / _ {t d θ ð s k g ɣ kʷ gʷ ɣʷ}

1.3  trimoraic glide-sequence regularization
     Vːj > Vj
     Vːw > Vw
     and, if such sequences arise:
     Vjː > Vj
     Vwː > Vw
```

---

## 3. Stage 2: Early divergent A / B / C responses

This is now the main daughter-defining stage.

The core idea is that the same inherited problem set is resolved in **different ways** across A, B, and C.

### Stage 2 matrix

| Domain | A | B | C |
|---|---|---|---|
| **2.1 Stress** | **initial stress** | **bounded nonfinal stress**, tending penultimate | **initial stress** |
| **2.2 Fricatives** | voiced fricatives resolve by **devoicing** | fricatives resolve **by environment**, not uniformly | voiced fricatives resolve by **hardening** |
| **2.3 Labiovelars** | labiovelars **delabialize** | labiovelars reduce only in **conditioned environments** | labiovelars **develarize** to labials |

### 2A current formulation

- **stress > initial**
- **β > ɸ**
- **ð > θ**
- **ɣ > x**
- **ɣʷ > xʷ** (in practice often treated in running tests as leading to **x** in A)
- **kʷ > k**
- **gʷ > g**

### 2B current formulation

B is explicitly the **slower, central, intermediate branch**.

#### Stress
- **bounded nonfinal stress**
- tends toward **penultimate** as a default, but not necessarily in a fully categorical way at this stage

#### Non-sibilant fricatives
Current working concept:
- after nasals: they may harden
- in stronger positions: they may remain fricatives longer
- in weaker positions: they may weaken or disappear

#### /z/ as a separate instability channel
This has been singled out as important and should **not** be buried inside the general fricative rules.

Current working idea:
- preserved in strong positions
- affricates after nasals
- devoices before voiceless consonants
- may later yield **z / s / r / ∅** in different B-descendants

#### Labiovelars
- reduced only in **specific conditioned environments**
- exact triggers are not yet fully settled

### 2C current formulation

- **stress > initial**
- **β > b**
- **ð > d**
- **ɣ > g**
- **ɣʷ > gʷ** and in practical testing often continues to **b** under develarization
- **kʷ > p**
- **gʷ > b**

### Summary of Stage 2

```text
Stage 2

2A
  1. stress > initial
  2. β ð ɣ ɣʷ > ɸ θ x xʷ
  3. kʷ gʷ > k g

2B
  1. bounded nonfinal stress, tending penultimate
  2. fricatives resolve by environment
  3. labiovelars reduce only under conditioned environments

2C
  1. stress > initial
  2. β ð ɣ ɣʷ > b d g gʷ
  3. kʷ gʷ > p b
```

---

## 4. Stage 3: later branch-specific developments

This is the stage where the daughters no longer simply respond differently to the same pressures, but begin developing branch-specific histories.

### 3A current direction

Current landed decisions:

1. **cluster spirantization only before s**
   - not before t
   - practical examples:
     - **ks > xs**
     - **ps > ɸs**

2. **later loss/simplification of x, ɸ in some of those clusters with compensatory lengthening**
   - not necessarily fully general or immediate
   - example:
     - **kréps > kreɸs > kreːs** (possible later development)

3. **no rhoticism**

### 3B current direction

B remains the least fixed, but the following broad profile is now in place:

1. **/z/ becomes the main unstable channel**
2. more conservative/mixed accentual residues survive
3. bridge-zone mergers and mixed local reflexes develop

### 3C current direction

Current landed decisions:

1. **rhoticism**
2. **final-vowel shortening and later apocope**
3. **right-edge morphological erosion**

C is expected to sound heavier and more clipped at the right edge than A.

---

## 5. Broad morphological directions now adopted

Phonology alone is not enough. The daughters should also remodel grammar differently.

### A: conservative stems, reduced case system, more analytic syntax

Current direction:

- A retains many older **consonant stems**
- A does **not** aggressively regularize everything into a few productive stem classes
- instead, the **case system collapses**
- grammatical work shifts to:
  - **determiners**
  - **particles**
  - **adpositions**
- A therefore becomes more **analytic** in syntax

Compact characterization:

> **A preserves many old stems but loses most cases in favor of determiners/adpositions.**

### B: mixed retention and mixed regularization

Current direction:

- B preserves more inherited irregularity than either edge branch
- it should keep:
  - more case morphology than A
  - more stem diversity than C
- but it should also show analogical leveling
- B is the true intermediate branch, both phonologically and morphologically

### C: strong paradigm regularization into productive stem classes

Current direction:

- C is likely to remodel nouns heavily into **o-stems** and **ā / a-stems**
- consonant stems may be absorbed analogically into these productive classes
- endings are shortened
- example given:
  - **walpos > walps**
- another likely direction:
  - **-ā > -a**
  - then former consonant stems may be pulled into **a-stems**

Compact characterization:

> **C regularizes stem classes hard, especially into o- and ā/a-type nouns, while shortening endings and eroding the right edge.**

### Useful summary contrast

- **A**: old stems survive; case marking weakens; syntax becomes more analytic
- **B**: mixed retention and mixed leveling
- **C**: old stem classes collapse into productive paradigms; short clipped endings survive

---

## 6. Lexicon testing already done

A first pass of test forms has already been run for A and C. This matters because the project has now reached a point where the transformations are **actionable**, not merely speculative.

### Good test forms identified

Useful probes included:

- *ðéɣveti* 'to burn, blaze, consume with fire'
- *ðeɣvís* 'fire, blaze, conflagration'
- *alβós* 'white'
- *anðér* 'under'
- *ékvos* 'horse'
- *gvéitom* 'food'
- *rḗks* 'king'
- *svéks* 'six'
- *kréps* 'body'
- *ðrāks* 'dregs, debris'

### Sample A outcomes already observed

Examples:

- *ðéɣveti* > /ˈθe.xe.ti/
- *ðeɣvís* > /ˈθe.xis/
- *alβós* > /ˈal.ɸos/
- *ékvos* > /ˈe.kos/
- *kréps* > /ˈkreɸs/, with later possible /ˈkreːs/

### Sample C outcomes already observed

Examples:

- *ðéɣveti* > /ˈde.be.ti/
- *ðeɣvís* > /ˈde.bis/
- *alβós* > /ˈal.bos/
- *ékvos* > /ˈe.pos/
- *kréps* > /ˈkreps/

This confirms that A and C are already becoming clearly distinct in sound.

---

## 7. Pending decisions

The following decisions remain open and should be continued in the next chat.

### A. Stage 2.B fricative environments
This is the biggest open phonological task.

Need to decide:

- exact environments for hardening
- exact environments for retention
- exact environments for deletion
- exact behavior of **/z/**
- whether any intervocalic **z > r** belongs in common B or only later B subbranches

### B. Stage 2.B labiovelar triggers
Need to decide exactly what counts as a conditioning environment for labiovelar reduction in B.

### C. Exact treatment of ɣʷ in A and C
In practical testing:
- A has often been treated as **ɣʷ > xʷ > x**
- C has often been treated as **ɣʷ > gʷ > b**

These practical results are useful, but the exact formal statement still needs to be locked down.

### D. Exact shape of Stage 2.B stress
Current wording is:

- bounded nonfinal stress
- tending penultimate

Need to decide how much older lexical accent survives in B.

### E. Stage 3B morphology
Need to decide whether B:
- keeps a modest case system
- partly regularizes stem classes
- preserves more consonant stems than C
- develops any determiner system like A

### F. A morphology in detail
The direction is clear, but details are still open:

- which cases survive longest
- what the determiner system looks like
- whether analytic marking first appears in nouns, adjectives, or both

### G. C morphology in detail
Need to decide:

- exact pathway of consonant stems into o- and ā/a-stems
- exact fate of endings such as:
  - **-os**
  - **-om**
  - **-ā**
- degree of case preservation after remodeling

### H. Whether Vjː and Vwː actually occur
Stage 1.3 currently includes them **if such sequences arise**, but their actual existence in the system is still unconfirmed.

### I. Additional sound changes considered but not adopted
These should be remembered as possibilities, but are **not** currently part of the landed system unless decided later.

1. **3A-stage cluster spirantization before t**
   - earlier broader idea: spirantization in **_{s,t}**
   - current landed system narrows this to **_s only**

2. **Blanket daughter-wide initial stress**
   - earlier idea: all daughters shift to initial stress
   - current landed system rejects this in favor of:
     - A = initial
     - B = bounded nonfinal / tending penultimate
     - C = initial

3. **More fully regular penultimate B**
   - possible future choice, but not yet adopted
   - current preference leaves more mixed or residual accent in B

4. **Categorical /z/ developments in common B**
   - e.g. universal **z > r** intervocalically
   - not currently adopted as a common B-wide rule

5. **Generalized 3A compensatory lengthening**
   - possible later extension, but not yet landed as fully automatic across all relevant clusters

### J. Additional lexicon testing
Need to test more items, especially:
- forms with **ɣʷ**
- forms with **kʷ / gʷ**
- forms with **ps / ks**
- longer polysyllables
- forms with **z**

---

## 8. Best immediate next steps

Recommended next tasks:

1. lock down **2B fricative environments**, especially **/z/**
2. lock down **B morphology**
3. write one or two **sample noun paradigms** through A, B, and C
4. test more lexical items through all stages

---

## 9. Short project status statement

The project is now at a useful turning point:

- Stage 1 is **solid enough to treat as fixed**
- Stage 2 is **mostly fixed**, with B still needing detail
- Stage 3 is **directionally clear**, especially for A and C
- the sound changes are already **actionable**
- morphology has started to differentiate in a historically meaningful way

That is enough structure to continue productively in a new chat without starting over.

---
---

# Appendices — Provisional Notes

The material below comes from earlier ChatGPT sessions and uses a different organizational model (seven dialect zones rather than three staged branches). It is retained as a source of ideas to harvest — individual rules and decisions may be adopted into the A/B/C framework above, at which point they should be removed from here. **Nothing in these appendices is canonical unless it also appears in §§1–9 above.**

---

## Appendix A: Seven-Zone Dialect Geography (2026-03-08)

Source: ChatGPT export, 2026-03-08. This predates the A/B/C framework and uses a finer-grained geographic model. Some rules here (nasal assimilation, fricative resolution, labiovelar resolution) overlap with the staged framework but are formulated differently. The zone labels may eventually map onto A/B/C subbranches or be retired entirely.

### Dialect Zones

Seven zones, ordered west to east:

| Code | Label |
|------|-------|
| W | West |
| WC | West-Central |
| C | Central |
| CS | Central-South |
| CC | Central-Central |
| EC | East-Central |
| E | East |

Zone labels are provisional — geographic/genealogical interpretation TBD.

### Rule Application Order

Rules are ordered and applied sequentially. Later rules may feed or bleed earlier ones depending on dialect.

### Rule 1 — Nasal-Obstruent Assimilation

**Scope**: all dialects (W WC C CS CC EC E)

| Subrule | Target | Change | Environment |
|---------|--------|--------|-------------|
| 1a | n | n → m | \_{p, b, ɸ, β} |
| 1b | m | m → n | \_{t, d, θ, ð, s, k, g, ɣ, kʷ, gʷ, ɣʷ} |

Note: this rule is explicitly marked as **not a Ghandwa rule** in the parent project. Ghandwa preserves nasal clusters without assimilation. This is a daughter-level innovation shared across all dialect zones.

### Rule 2 — Fricative Resolution

The voiced fricatives β ð ɣ ɣʷ (stable in Ghandwa) resolve differently by dialect zone. Rules are ordered within each zone; subrule 2e takes priority for CS before 2f–2n apply.

#### W and WC — wholesale devoicing

| Subrule | Target | Change | Environment |
|---------|--------|--------|-------------|
| 2a | β | β → ɸ | everywhere |
| 2b | ð | ð → θ | everywhere |
| 2c | ɣ | ɣ → x | everywhere |
| 2d | ɣʷ | ɣʷ → xʷ | everywhere |

#### CS — special ɣʷ rule, then devoicing elsewhere

| Subrule | Target | Change | Environment | Note |
|---------|--------|--------|-------------|------|
| 2e | ɣʷ | ɣʷ → w | V\_V | CS-only; takes priority; applies before 2n |
| 2f | β | β → b | N\_ | after m or n |
| 2g | ð | ð → d | N\_ | after m or n |
| 2h | ɣ | ɣ → g | N\_ | after m or n |
| 2i | ɣʷ | ɣʷ → gʷ | N\_ | after m or n |
| 2j | β | β → ɸ | elsewhere | |
| 2k | ð | ð → θ | elsewhere | |
| 2l | ɣ | ɣ → x | elsewhere | |
| 2n | ɣʷ | ɣʷ → xʷ | elsewhere | |

#### CC — same as CS minus the 2e override

| Subrule | Target | Change | Environment |
|---------|--------|--------|-------------|
| 2f | β | β → b | N\_ |
| 2g | ð | ð → d | N\_ |
| 2h | ɣ | ɣ → g | N\_ |
| 2i | ɣʷ | ɣʷ → gʷ | N\_ |
| 2j | β | β → ɸ | elsewhere |
| 2k | ð | ð → θ | elsewhere |
| 2l | ɣ | ɣ → x | elsewhere |
| 2n | ɣʷ | ɣʷ → xʷ | elsewhere |

#### EC and E — wholesale hardening to stops

| Subrule | Target | Change | Environment |
|---------|--------|--------|-------------|
| 2o | β | β → b | everywhere |
| 2p | ð | ð → d | everywhere |
| 2q | ɣ | ɣ → g | everywhere |
| 2r | ɣʷ | ɣʷ → gʷ | everywhere |

### Rule 3 — Labiovelar Resolution

Ghandwa labiovelars kʷ gʷ (and xʷ from rule 2) resolve as follows:

#### CS and CC — conditioned dissimilation

| Subrule | Target | Change | Environment | Note |
|---------|--------|--------|-------------|------|
| 3a | kʷ | kʷ → k | triggered | trigger: another Lʷ within 1 syllable; Lʷ = {kʷ, gʷ, xʷ, w} |
| 3b | gʷ | gʷ → g | triggered | same trigger |
| 3c | xʷ | xʷ → w | \_V AND triggered | only before vowel when trigger holds |

#### EC — wholesale delabialization

| Subrule | Target | Change |
|---------|--------|--------|
| 3d | kʷ | kʷ → k |
| 3e | gʷ | gʷ → g |

#### E — labiovelars shift to labials

| Subrule | Target | Change |
|---------|--------|--------|
| 3f | kʷ | kʷ → p |
| 3g | gʷ | gʷ → b |

W, WC, C: no labiovelar resolution rule specified (labiovelars preserved or handled by Rule 4).

### Rule 4 — Cluster Spirantization

Stops spirantize before s or t in western dialects only.

#### W — before s or t

| Subrule | Target | Change | Environment |
|---------|--------|--------|-------------|
| 4a | p | p → ɸ | \_{s, t} |
| 4b | t | t → θ | \_{s, t} |
| 4c | k | k → x | \_{s, t} |

#### WC — before s only

| Subrule | Target | Change | Environment |
|---------|--------|--------|-------------|
| 4d | p | p → ɸ | \_s |
| 4e | t | t → θ | \_s |
| 4f | k | k → x | \_s |

### Rule 5 — Accent Regression

**Scope**: all dialects

Stress shifts to initial syllable. Ghandwa stress is free/lexical; daughters regularize to initial.

### Rule 6 — Final-Syllable Vowel Shortening

**Scope**: CC, EC, E

Long vowels shorten in the final syllable, blocked when the word has only one vowel nucleus (i.e. monosyllables are exempt).

| Subrule | Target | Change | Environment |
|---------|--------|--------|-------------|
| 6a | Vː | Vː → V | final syllable, word has ≥2 vowel nuclei |

### Rule 7 — Initial x-Debuccalization

**Scope**: W, WC, CC

| Subrule | Target | Change | Environment |
|---------|--------|--------|-------------|
| 7a | x | x → h | #\_V (word-initially before vowel) |

### Summary Table by Dialect Zone

| Rule | W | WC | C | CS | CC | EC | E |
|------|---|----|---|----|----|----|---|
| 1 Nasal assim. | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 Fric. resolution | devoice all | devoice all | devoice all | N\_→stop, V\_V ɣʷ→w, else devoice | N\_→stop, else devoice | harden all | harden all |
| 3 Labiovelar res. | — | — | — | dissim. triggered | dissim. triggered | delabialize | →labials |
| 4 Cluster spirant. | \_s,t | \_s | — | — | — | — | — |
| 5 Accent regression | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 6 Final Vː short. | — | — | — | — | ✓ | ✓ | ✓ |
| 7 x-debuccal. | ✓ | ✓ | — | — | ✓ | — | — |

### Open Questions (from 7-zone model)

- Geographic/genealogical identity of each zone not yet assigned to named daughter languages
- Rule ordering interactions between 2 and 4 in W/WC not fully specified (does 2 devoice first, then 4 spirantizes the result, or vice versa?)
- C zone: no unique rules assigned — may just be a conservative dialect or a placeholder
- Nasal assimilation scope note: overview table marks CS as "n/a" for rule 1, but detailed rules mark it as applying to all zones — discrepancy TBD

---

## Appendix B: CS / Dialect / -ln- Decisions (2026-03-01)

Source: ChatGPT session export, 2026-03-01T21:54:32Z. These are point decisions from an early session. Some may already be reflected in the A/B/C framework or Appendix A; others are not yet captured anywhere else.

- Dialectal outcomes for *-ln-*: West: -ln- > -ll-; East: -ln- > -nn-; Central (C): -Vln- > -Vwn-.

- Dialect geography model: innovations spread inward from the edges; the center becomes a mixed-isogloss zone; later, edge dialects also develop incomplete isoglosses and split into subdialects.

- CS status/label: CS is treated as a codified high register (a supradialectal, normed variety), not a purely geographic dialect.

- CS phonological profile (vowels): CS retains vowel 'shape' conservatively (keeps two-part vocalism such as V+glide sequences, even if component qualities drift).

- CS phonological profile (glides): CS retains glides and can acquire additional glides in ways other dialects do not.

- CS glide-creation (morphology example): for s-stem-like material, genitive -ezos > -ejos; hypothetical -oze- > -owe- (environment-driven z > j / z > w).

- Representation choice: all IPA diphthongs were replaced with Vj/Vw pairs (e.g., oi > oj; ei > ej) as the working representation.

- Design stance on interactions: any knock-on interactions from the Vj/Vw rewrite are acceptable; rule ordering/rules will be adjusted if outputs are undesirable, and such interactions may be desirable for naturalism.

- Palatals: palatal consonants may arise allophonically at first (with optional later phonologization).
