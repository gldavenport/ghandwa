---
title: Ghandwa Daughter B — Phonological Pipeline
file: docs/ghandwa-daughter-b.md
last_updated: 2026-05-18T00:00-04:00
status: Stage 2B specified and implemented; Stage 3B pending
changelog:
  - 2026-05-18T00:00-04:00 | 132 lines | Initial creation. Stage 2B non-sibilant
    fricative pipeline fully specified and implemented in
    tools/pie_transformer/pipelines/daughter_b.py. Transformer verified against
    six test forms. Language name established as xandwā.
---

# Ghandwa Daughter B (*xandwā*)

## 1. Identity and Character

Daughter B descends from regional common Ghandwa via the Dark Ages dialectalization
(Stage 2). It is the central, conservative branch — slower to innovate than A
(full devoicing) or C (full hardening). Its defining character is the conditioning
of fricative outcomes by phonological environment: the same inherited fricative
produces different results depending on what surrounds it.

**Language name:** *xandwā* — the daughter-internal reflex of Ghandwa *ɣandwā*,
from PIE \**gʰándweh₂*. Word-initial *ɣ* is not intervocalic and falls through
to default devoicing: ɣ → x.

**Mutual unintelligibility targets:**
- vs. Daughter A (*xandwā* surface same, but systematic A/B divergence in
  post-liquid environments: A *álɸos* vs. B *álwos*; intervocalic: A *néɸos*
  vs. B *néwos*)
- vs. Daughter C (C *ándwā* via full hardening and stop-merger; B retains x
  where C has ∅ or stop)
- vs. Ghandwa (Gh *ɣandwā* vs. B *xandwā*; Gh *alβós* vs. B *álwos*)

---

## 2. Stage 1: Late Common Ghandwa (shared)

Rules 1.1–1.3 apply uniformly across all daughter branches before Stage 2
divergence. See `docs/daughters.md` §2.1.

---

## 3. Stage 2B: Dark Ages Innovations

### 3.1 Stress

B retains bounded nonfinal stress from the Stage 1 accent retraction rule.
A penultimate default develops gradually through Stage 2B but is not yet
implemented as a discrete rule. A and C both innovate initial stress; B does not.

### 3.2 Non-sibilant voiced fricatives

Resolved by a five-step ordered pipeline. Rules apply in order; each rule
bleeds subsequent rules on its outputs.

#### Rule ordering

**2B.1 Homorganic nasal assimilation** *(bleeds 2B.2–5)*

Place assimilation triggered by following homorganic nasal. Fires only when
the fricative is post-vocalic.

| Sequence | Output | Motivation |
|---|---|---|
| Vβm | Vmm | Full labial identity; geminate created |
| Vðn | Vnn | Full coronal identity; geminate created |
| VɣʷmV | VwmV | Partial: labial feature wins, velar lost; no gemination; requires V on both sides |
| VɣnV | no change | No place overlap; falls through to 2B.2 |

Note: geminates from 2B.1 are retained at this stage. Simplification is a
possible Stage 3+ development.

**2B.2 Post-nasal hardening**

β ð ɣ ɣʷ → b d g gʷ / N\_

Nasals trigger hardening in both directions (pre-nasal assimilation in 2B.1;
post-nasal hardening here). Voiced fricatives directly following any nasal
(m or n) become the corresponding voiced stop.

**2B.3 Post-liquid**

β ɣʷ → w / R\_ *(labial identity wins)*
ð ɣ  → θ x / R\_ *(devoice; no labial feature to drive sonorantization)*

Post-liquid environment is split by place: labial fricatives sonorantize to w,
coronal and velar fricatives devoice.

**2B.4 Intervocalic sonorantization**

β ɣʷ → w / V\_V
ɣ    → j / V\_V
ð    → r / V\_V

The core defining innovation of B. All voiced fricatives sonorantize between
vowels. ð → r is direct rhotacism (skipping the z intermediate stage seen
in some other IE daughters). ɣ → j is velar weakening.

**2B.5 Default devoicing**

β→ɸ  ð→θ  ɣ→x  ɣʷ→xʷ / elsewhere

Covers: word-initial position, pre-consonantal, word-final, and any voiced
fricative not consumed by 2B.1–4.

#### Rule summary

| Environment | β | ð | ɣ | ɣʷ |
|---|---|---|---|---|
| Vβm, Vðn (homorganic pre-nasal) | m (+ geminate) | n (+ geminate) | — | — |
| VɣʷmV | — | — | — | w (no geminate) |
| N\_ (post-nasal) | b | d | g | gʷ |
| R\_ (post-liquid, labial) | w | — | — | w |
| R\_ (post-liquid, other) | — | θ | x | — |
| V\_V (intervocalic) | w | r | j | w |
| elsewhere (default) | ɸ | θ | x | xʷ |

#### Key rule interactions

*Post-sonorant bleed:* Post-nasal (2B.2) and post-liquid (2B.3) rules fire
before intervocalic (2B.4). A fricative after a sonorant does not reach the
intervocalic check even if a vowel follows the fricative. E.g., *anβrís*:
β is post-nasal → hardens to b (2B.2); intervocalic rule never applies.

*Homorganic bleed:* 2B.1 removes β/ð before their respective nasals. The
nasal itself remains; post-nasal hardening (2B.2) therefore does not apply
to the position where β/ð stood (it has been replaced by a nasal consonant,
not a voiced fricative).

*Open question:* The sequence NβmV (post-nasal β before m) creates a conflict
between 2B.1 (Vβm assimilation, requires preceding vowel) and 2B.2 (post-nasal
hardening, requires preceding nasal). The preceding context is N, not V, so
2B.1 does not fire; 2B.2 applies (β → b). This is the expected resolution but
requires transformer verification.

### 3.3 /z/

Inherited Ghandwa /z/ (~55 lemmas across intervocalic, pre-consonantal, and
post-liquid environments) is preserved unchanged. The voicing rule that created
/z/ in Ghandwa is not productive in B — no new VsV contacts produce /z/.

After the non-sibilant pipeline eliminates β ð ɣ ɣʷ, /z/ is the **sole
surviving voiced fricative** in B — a systemic orphan with no voicing partner
for /s/. This instability drives Stage 3B resolution (not yet specified;
partial rhotacism by environment is expected).

### 3.3 Stress (continued): Stage 3B candidate

**Antepenultimate stress** is the candidate Stage 3B crystallization. Rationale:
- Stage 1 bans final accent; Stage 2B develops penultimate tendency but never
  fully locks in
- Antepenultimate is a natural stopping point for systems with residual
  quantity-sensitivity (cf. Greek, Latin manus rule)
- Creates a meaningful three-way typological spread across daughters:
  A/C anchor initial (left edge); B anchors antepenultimate (one syllable
  further right) — different right-edge erosion profiles follow

If B retains syllable-weight sensitivity at Stage 3, a heavy-final-syllable
exception (penultimate stress when final syllable is heavy) is plausible
before full antepenultimate leveling.

**Decision deferred.** Stress comparison across all three daughters is the
appropriate context for finalizing this. Do not implement until A, C stress
trajectories are reviewed together with B.

### 3.4 Labiovelars

Conditioned reduction in specific environments. Exact triggers not yet settled.
See `docs/daughters.md` Appendix I §I.B.

---

## 4. Stage 2B Exit Profile

B exits Stage 2 with:
- No β ð ɣ ɣʷ (fully resolved)
- New w from: intervocalic β/ɣʷ, post-liquid β/ɣʷ, and VɣʷmV assimilation
- New r from: intervocalic ð
- New j from: intervocalic ɣ
- Geminates mm/nn from homorganic assimilation (not yet simplified)
- Voiceless fricatives ɸ θ x xʷ in non-sonorantizing environments
- /z/ orphaned as sole voiced fricative
- Characteristic instability: /z/ without a voicing partner

---

## 5. Verified Test Cases

All forms verified against `tools/pie_transformer/pipelines/daughter_b.py`.

| PIE | Ghandwa | Daughter B | Rule(s) fired |
|---|---|---|---|
| \**gʰándweh₂* | *ɣándwā* | *xándwā* | 2B.5 (initial ɣ→x) |
| \**albʰós* | *álβos* | *álwos* | 2B.3 (post-liquid β→w) |
| \**nebʰós* | *néβos* | *néwos* | 2B.4 (intervocalic β→w) |
| \**médʰjos* | *méðjos* | *méθjos* | 2B.5 (pre-consonantal ð→θ) |
| \**gʰóstis* | *ɣóstis* | *xóstis* | 2B.5 (initial ɣ→x) |
| \**gʷʰéndʰ-* | *ɣʷénð-* | *xʷénd-* | 2B.2 (post-nasal ð→d); 2B.5 (initial ɣʷ→xʷ) |

Contrast with Daughter A on the same inputs:

| PIE | Daughter A | Daughter B | Divergence |
|---|---|---|---|
| \**albʰós* | *álɸos* | *álwos* | post-liquid: A devoices, B sonorantizes |
| \**nebʰós* | *néɸos* | *néwos* | intervocalic: A devoices, B sonorantizes |

---

## 6. Open Questions

- **NβmV interaction:** sequence is post-nasal β (→ b by 2B.2) before m;
  2B.1 does not fire (preceding context is N, not V); expected output is bm.
  Needs a test case with a lexicon form containing this sequence.
- **Stage 3B /z/ resolution:** partial rhotacism by environment expected;
  pre-consonantal and post-liquid environments still open.
- **Labiovelar conditioned reduction:** triggers not yet specified.
- **Stage 3B stress crystallization:** antepenultimate is the candidate; possibly
  with heavy-final exception before full leveling. Defer until A/C stress
  trajectories reviewed together. See §3.3.
- **Geminate simplification:** mm/nn from 2B.1 retained at this stage;
  Stage 3+ fate undecided.

---

## 7. Implementation

Transformer pipeline: `tools/pie_transformer/pipelines/daughter_b.py`
Pipeline name: `daughter-b`
Chaining: downstream of `ghandwa` pipeline

```bash
python3 -m pie_transformer form "*gʰándweh₂" --pipeline daughter-b --trace changed
```
