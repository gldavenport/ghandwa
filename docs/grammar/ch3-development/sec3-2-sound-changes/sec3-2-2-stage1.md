---
title: "§3.2.2 Stage 1: PIE to Late Western IE"
last_updated: 2026-06-09T00:00-04:00
chapter: ch3-development
section: sec3-2-sound-changes
supersedes: "docs/grammar/ch3-development/phonological-history.md (§4)"
---

# §3.2.2 Stage 1: PIE to Late Western IE

Stage 1 comprises the changes shared broadly across the western IE branches: dental cluster simplification, thorn metathesis, laryngeal elimination, obstruent devoicing before voiceless consonants, Osthoff's Law, the *ew* → *ow* diphthong shift, and pretonic shortening. None of these individually characterizes Ghandwa — each has reflexes in one or more sister branches — but taken together they define the pre-Ghandwa stage from which Stage 2 innovations emerge.

The standing Boukólos rule (§3.2.1.4) applies after this stage.

## §3.2.2.1 Dental Cluster Simplification

> T + T → ss (dental before dental → geminate ss)

Two adjacent dental stops merge into a geminate *ss*. **This rule covers dental+dental only.** Dental+s sequences are handled separately: the devoicing rule (§3.2.2.4) converts voiced dental+s to *ts*, which Ghandwa preserves as *ts* without further reduction (unlike Latin, which reduces *ts* → *ss*).

> ss → s / _C

Geminate *ss* simplifies to single *s* before a following consonant.

**Examples:**
- \*widstós 'known' → widstos → wissos (TT: ds → ss) — cf. PGmc \*(ga)wissaz, OE ġewiss
- \*sedstós 'seated' → sedstos → sessos — cf. PGmc \*sessaz, ON sess
- \*gʰáyds 'goat' → ɣájts (ds → ts via devoicing §3.2.2.4; *not* → ss)

**Ordering:** Must precede thorn metathesis (§3.2.2.2), since dental+dental clusters are resolved before dental+velar clusters are reordered.

## §3.2.2.2 Thorn Metathesis

> TK → KT (word-internally; voicing and aspiration of each segment preserved)

A dental stop followed by a plain velar stop undergoes metathesis: the velar moves before the dental. Labiovelars are excluded (they have already been simplified before consonants by the Ghandwa Boukólos rule, §3.2.1.4). Word-initial position is excluded.

This follows Jasanoff 2018 (via Ringe 2024) in treating the outcome as metathesis (Greek-type *kt*) rather than the assibilation path that fed PGmc (TK → KS → K after Grimm's Law).

**Examples:**
- \*h₂ŕ̥tḱos 'bear': after centumization → h₂r̥tkos; thorn metathesis → h₂r̥ktos → … → *arktos*
  (cf. Greek ἄρκτος; PGmc replaced the inherited form with the euphemism \*berō)

**Design note:** The metathesized cluster *kt* is left stable in Ghandwa. It constitutes a deliberate phonological tension: daughter languages may simplify it variously (assibilation, loss of one member, fricativization, etc.). See §4.2 (*sec4-2-phonology/sec4-2-phonology.md*).

## §3.2.2.3 Laryngeal Changes

The PIE laryngeals (h₁, h₂, h₃) are resolved in a multi-step sequence. All substeps must be ordered as given; each feeds the next.

### §3.2.2.3a Laryngeal Coloring

> h₂ colors adjacent \*e → a
> h₃ colors adjacent \*e → o
> h₁ is neutral (no coloring)

Coloring operates bidirectionally: both HV and VH sequences are affected. Only \*e is colored; \*a, \*o, \*i, \*u are immune.

**Examples:**
- \*h₂éḱweh₂ 'water' → h₂akwah₂ (both e's colored by adjacent h₂)
- \*h₃réǵs 'king' → h₃regs (h₃ does not color non-e vowels) → … → *rēks*

**Ordering:** Coloring must precede all laryngeal deletion rules, since the vowel quality established here is the permanent reflex.

### §3.2.2.3b Word-Initial Laryngeal Coloring Before Syllabic Resonants

> #h₁R̥ → eR
> #h₃R̥ → oR

When a word-initial laryngeal immediately precedes a syllabic resonant, it provides quality coloring to the vocalic nucleus before being deleted: h₁ yields *e*-quality, h₃ yields *o*-quality. The syllabic resonant is simultaneously desyllabified. The result is a non-syllabic resonant preceded by a short colored vowel.

The h₂ case is not listed separately. *#h₂R̥* yields *aR* by the general route: h₂ is deleted word-initially (§3.2.2.3e) and the residual syllabic resonant vocalizes to *aR* via the CaRC rule (§3.2.3.1) — the same surface output that a dedicated coloring rule would produce.

**Examples:**
- *h₃r̥bʰ-* 'deprived, orphaned' → *orβ-* (h₃ colors r̥ → or; cf. Latin *orbus*, Greek *ὀρφανός*)

**Ordering:** Feeds §3.2.2.3e (word-initial laryngeal deletion), which would otherwise delete the laryngeal without a trace and leave a bare syllabic resonant to vocalize as *aR*. Must follow §3.2.2.3a (laryngeal coloring of adjacent vowels), which does not see syllabic resonants.

### §3.2.2.3c Contraction across Laryngeal

> VHV → V̄ (when both vowels are identical after coloring)

Two identical vowels separated by a laryngeal contract into a single long vowel; the laryngeal is lost.

When the flanking vowels are not identical after coloring, the laryngeal is not resolved at this stage. It surfaces as a diagnostic glottal stop ˀ in the output, flagging the form for manual review.

**Design note:** Ringe posits trimoric (overlong) vowels from certain VHV contractions in PGmc. Ghandwa does not maintain a trimoric distinction; all contractions yield ordinary long vowels.

### §3.2.2.3d Pre-consonantal and Word-Final Laryngeal Loss with Compensatory Lengthening

> VH → V̄ / _{C, #}

A vowel immediately preceding a laryngeal lengthens; the laryngeal is lost. This applies both before consonants and at word boundaries.

**Examples:**
- \*séh₁mn̥ 'seed' → sēmn̥ (eH → ē) → … → *sēman*
- \*bʰráh₂tēr 'brother' → βrātēr (aH → ā) → … → *βrātēr*
- \*dʰéh₁ti- 'act of putting' → ðēti- (eH → ē)
- \*h₂éḱweh₂ → akwah₂ → akwā (word-final aH → ā) → *akʷā*

This rule applies to both high and low vowels. The lengthening of high vowels before laryngeals (\*iH → ī, \*uH → ū) is a Ghandwa design decision.

### §3.2.2.3e Word-Initial Laryngeal Loss

> #H → ∅ (before consonants or at the absolute beginning of a word)

Word-initial laryngeals are deleted without trace.

**Examples:**
- \*h₁ésti 'is' → esti → *esti*
- \*h₁éd- 'eat' → ed- → *ed-*
- \*h₂ŕ̥tḱos 'bear' → (after coloring) ar̥tkos (h₂ deleted word-initially)

### §3.2.2.3f Interconsonantal Laryngeal Resolution

> CHC → CaC (in the initial syllable, i.e. when no vowel has yet appeared)
> CHC → CC (post-vocalically, i.e. when a vowel already precedes)

A laryngeal caught between two consonants (neither of which is a syllabic resonant) is resolved as *a* in the first syllable of the word, and deleted silently in subsequent syllables.

**Examples:**
- \*ph₂tḗr 'father' → patēr (h₂ between p and t in initial syllable → a) → *patēr*
  (cf. PGmc \*fadēr < \*pətēr, with the same epenthesis)

### §3.2.2.3g Residual Laryngeal Diagnostic

> H → ˀ (any surviving laryngeal)

Any laryngeal that has not been resolved by the preceding rules surfaces as a glottal stop ˀ in the output. This is an intentional diagnostic: it flags an environment not yet covered by the rule set for manual review. It is not a Ghandwa phoneme.

## §3.2.2.4 Obstruent Devoicing before Voiceless Consonants

> {b, bʰ} → p / _{t, s}
> {d, dʰ} → t / _{t, s}
> {g, gʰ} → k / _{t, s}
> {gʷ, gʷʰ} → kʷ / _{t, s}

Voiced and breathy-voiced obstruents are devoiced immediately before \*t or \*s. This is a core western IE process shared with PGmc and PIt. The rule covers all voiced obstruents including dentals — \*d and \*dʰ devoice to \*t before \*t or \*s.

**Examples:**
- \*dʰugh₂tḗr 'daughter' → dugh₂tēr → dugtēr (h₂ lost post-vocalically) → duktēr (g devoiced before t) → *ðuktēr*
- \*gʰáyds 'goat' → ɣájds → ɣájts (d devoiced before s) → *ɣájts*

**Design note:** Ringe defers voicing assimilation to individual daughter branches. Ghandwa applies it at the parent stage as a shared western development, following the evidence from PIt and PC.

**Ordering:** Must follow laryngeal resolution (§3.2.2.3), since laryngeal loss can create new obstruent+t/s clusters. Must precede aspirate fricativization (§3.2.3.3), since the rule references bʰ, dʰ, gʰ, gʷʰ as inputs that become β, ð, ɣ, ɣʷ after fricativization — at which point the rule would no longer reach them.

## §3.2.2.5 Osthoff's Law

> V̄RC → VRC (long vowel shortens before sonorant + consonant)

A long vowel is shortened when followed by a sonorant (r, l, m, n, w, y) and then a consonant in the same word. This is a PIE-era or early Core IE rule with reflexes across multiple branches.

**Examples:**
- \*h₁nḗh₃mn̥ 'name': h₁ deleted initially → nēh₃mn̥; h₃ colors ē → ō → nōmn̥; Osthoff fires (ō before m + C) → nomn̥ → … → *noman*
  (cf. PGmc \*namô, Goth. namo, OE nama — same Osthoff shortening, different resonant vocalism)

- \*h₂yúHn̥ḱos 'young' → (h₂ lost initially) yūn̥kos (uH → ū) → (Osthoff: ū before n̥+k) yun̥kos → … → *juwankos*
  (cf. PGmc \*jungaz, Goth. juggs — same shortening)

- \*h₂wéh₁n̥ts 'wind' → (h₂ lost) wéh₁n̥ts → (VH → V̄) wēn̥ts → (Osthoff: ē before n̥+t) wen̥ts → … → *wants*
  (cf. PGmc \*windaz — same shortening, different vocalism)

## §3.2.2.6 Tautosyllabic *ew* → *ow*

> e͡w → o͡w (where *e* and *w* are tautosyllabic, i.e. *w* is in coda)

When \*e and \*w belong to the same syllable — that is, when \*w stands before a consonant or at word end and thus occupies the coda — the diphthong \*e͡w becomes *o͡w*. Heterosyllabic sequences, where \*w is the onset of the following syllable (e.g. \*e.wi), are not affected.

This is a shared western IE innovation. The tautosyllabic condition explains why the rule applies in some morphological environments but not others within the same paradigm: in the u-stem genitive \*-ews, the *w* is in coda before *s*, so the rule fires and the genitive surfaces as *-ows*; in the u-stem dative \*-ewi, the *w* is onset of the next syllable, and the *e* is preserved.

**Examples:**
- u-stem gen.sg. \*-ews → *-ows* (w in coda before s; tautosyllabic; rule fires)
- u-stem dat.sg. \*-ewi → *-ewi* (syllabified e.wi; w is onset; heterosyllabic; rule does not fire)
- \*newos 'new' → *newos* (syllabified ne.wos; w is onset before vowel; heterosyllabic; rule does **not** fire)

**Orthographic note:** Coda *w* is written ⟨u⟩ in Ghandwa transliteration (as in Greek αυ, ευ and Latin au). Thus the genitive ending /ows/ is transliterated *-ous*, even though the phonological representation is /ows/. The IPA layer resolves the ambiguity; the transliteration layer reflects the script convention that glides in coda position are written as their corresponding vowel letters.

**Design note:** PGmc continued this change further (ow → aw → awz in certain environments). Ghandwa stops at *ow*.

**Ordering:** Must follow laryngeal resolution (§3.2.2.3), since laryngeal loss can expose new *ew* sequences.

## §3.2.2.7 Pretonic Shortening

> V̄ → V / in the first syllable, when the accent falls on a later syllable

A long vowel in the first syllable of a word is shortened if the word accent falls on a non-initial syllable. This is a western IE innovation.

**Examples:**
- \*wih₁rós 'man' (if accent on second syllable): wīros (iH → ī) → wiros (pretonic shortening: ī in first syllable, accent on -ós) → *wiros*

When the accent position is not marked on the input form, the rule does not fire and the form is flagged with a warning. This is a computational safeguard, not a phonological claim.

**Ordering:** Must follow laryngeal resolution (§3.2.2.3) and Osthoff's Law (§3.2.2.5), since both create the long vowels that feed pretonic shortening. Osthoff's Law and pretonic shortening both belong to Stage 1 but do not interact: Osthoff's Law is conditioned by syllable structure (\*V̄RC), pretonic shortening by accent position. The stage grouping is a notational convenience, not a chronological claim.
