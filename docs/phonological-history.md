# From Proto-Indo-European to Ghandwa

---
last_updated: 2026-03-17T00:00:00Z
status: draft — first complete pass; examples to be expanded as lexicon grows
related: ghandwa-prompt.md, ghandwa_comparanda.md, pie_2_ghandwa.jsx
changelog:
  - 2026-03-17T01:00:00Z | 556 lines | Replaced §5.2 Juwankos rule (narrow ū→uw/_V) with general hiatus glide insertion rule (i→ij/_V, u→uw/_V). Rewrote §4.6 (ew→ow) to clarify tautosyllabic condition, add u-stem paradigm examples, and document coda-w orthographic convention (⟨u⟩ for /w/ in coda). Fixed *newos* example: ne.wos is heterosyllabic (w is onset before vowel), so rule does not fire — was incorrectly shown as firing. Updated §9 rule summary, §10.6 worked example, and §7 tension inventory accordingly.
  - 2026-03-17T00:00:00Z | 565 lines | Initial creation. Full rule inventory from transformer and comparanda; staged presentation with formal statements, examples, ordering arguments, and design rationale. Standing rules treated as synchronic surface constraints.
---

This chapter presents the phonological derivation from Proto-Indo-European (PIE) to Ghandwa as an ordered sequence of sound changes. The chapter is designed so that any entry in the dictionary can be checked: given a PIE preform, a reader should be able to walk through the rules below and arrive at the Ghandwa surface form.

The primary structural model is Ringe 2017 (*From Proto-Indo-European to Proto-Germanic*, 2nd ed.), supplemented by Ringe 2024 (*A Linguistic History of Greek*) for the treatment of thorn clusters. The rule inventory is also implemented computationally in a transformer tool (`pie_2_ghandwa.jsx`), which serves as a verification device for the derivations given in individual dictionary entries.

---

## 0. Ghandwa's Position

Ghandwa is a centum language of the western Indo-European group. Its two defining innovations relative to PIE are:

1. **Voiced fricatives from aspirates.** The PIE breathy-voiced stops \*bʰ, \*dʰ, \*gʰ, \*gʷʰ surface as voiced fricatives β, ð, ɣ, ɣʷ — not as voiceless fricatives (as in Germanic via Grimm's Law) and not as plain voiced stops (as in Italic and Celtic).

2. **CaRC syllabic resonant vocalism.** The PIE syllabic resonants \*r̥, \*l̥, \*m̥, \*n̥ vocalize with an *a*-colored epenthetic vowel in the order *aR*: \*r̥ → *ar*, \*l̥ → *al*, \*m̥ → *am*, \*n̥ → *an*. This aligns with Celtic in vowel quality (*a*, not Germanic *u*) and with Germanic in metathesis order (*aR*, not Italic *Ra*).

The comparative framework draws primarily on Proto-Germanic (PGmc), Proto-Italic (PIt), and Proto-Celtic (PC) — "Western Indo-European" (WIE). Where all three share an inherited form, that is the Ghandwa form. Where they diverge through independent innovation, Ghandwa preserves the PIE-inherited state rather than following any single branch. Proto-Balto-Slavic (PBS) is consulted as a fourth witness but held at arm's length due to satemization and structural divergences in nominal morphology.

Ghandwa explicitly does *not* undergo two major innovations attested in sister branches:

- **\*gʷ → b** (Celtic-specific). Ghandwa preserves \*gʷ.
- **p-loss** (Celtic-specific). Ghandwa preserves \*p.
- **o/a merger** (Germanic-specific). Ghandwa preserves the PIE o/a distinction.
- **Grimm's Law** (Germanic-specific). Ghandwa does not shift voiceless stops to fricatives.
- **Verner's Law** (Germanic-specific). Ghandwa's *s* → *z* rule is conditioned by voicing environment, not accent position.

---

## 1. Phonological Inventory

The Ghandwa surface-stage inventory, as derived by the rules below:

**Stops:** p  b  t  d  k  g  kʷ  gʷ
**Fricatives:** s  z  β  ð  ɣ  ɣʷ
**Nasals:** m  n
**Liquids:** l  r
**Glides:** w  j
**Short vowels:** a  e  i  o  u
**Long vowels:** ā  ē  ī  ō  ū

Vowel length is phonemically distinctive. Stress is free and lexical. Labiovelars kʷ, gʷ are preserved before vowels other than *u*; they delabialized before *u*, *ū*, *w*, and before consonants (see Standing Rules, §6).

---

## 2. Conventions

Throughout this chapter, PIE forms are given with the conventional asterisk and standard PIE notation: \*bʰer- 'carry', \*ph₂tḗr 'father'. Ghandwa forms are given in italics: *βer-*, *patēr*. Intermediate stages are unmarked.

The arrow → indicates a diachronic development. The notation "C" means any consonant, "V" any vowel, "R" any sonorant (r, l, m, n, w, y), "T" any dental stop (t, d, dʰ), "K" any velar stop (k, g, gʰ), "Kʷ" any labiovelar (kʷ, gʷ, gʷʰ), "H" any laryngeal (h₁, h₂, h₃), and "#" a word boundary.

---

## 3. Pre-Stage: Centum Merger and Labiovelar Normalization

These changes are shared by all centum IE languages and are presupposed by every subsequent rule. They are not Ghandwa innovations but features of the centum node from which Ghandwa descends.

### 3.1. Centumization

> \*ḱ → k, \*ǵ → g, \*ǵʰ → gʰ

The PIE palatal series merges unconditionally with the plain velars. After this rule, no subsequent rule ever sees a palatovelar.

**Examples:**
- \*ḱr̥h₂nóm 'horn (acc.)' → kr̥h₂nom → … → *karnom*
- \*ḱm̥tóm 'hundred' → km̥tom → … → *kantom*
- \*déḱm̥ 'ten' → dekm̥ → … → *dekam*
- \*h₂ŕ̥tḱos 'bear' → h₂r̥tkos → … → *arktos*

### 3.2. Labiovelar Absorption

> Kw → Kʷ (velar + w sequences merge with inherited labiovelars)

Any sequence of a plain velar followed immediately by \*w is treated as a single labiovelar segment. This rule collapses the distinction between inherited labiovelars (\*kʷ, \*gʷ, \*gʷʰ) and surface-identical sequences arising from morpheme boundaries or compounding.

### 3.3. Boukólos Rule

> Kʷ → K / adjacent to u, ū, or w

Labiovelars lose their labialization next to rounded segments. This is a surface constraint shared with PGmc (Ringe §2.2.3(ii)).

**Examples:**
- \*gʷr̥h₂ús 'heavy' → … gr̥h₂us (labiovelar delabializes before u)

### 3.4. Labiovelar Delabialization before Consonants

> Kʷ → K / _C (before any consonant other than a syllabic resonant)

Labiovelars simplify to plain velars before obstruents, nasals, and liquids.

**Examples:**
- \*nókʷts 'night' → nokts (kʷ → k before t) → *nokts*

**Ordering:** The Boukólos rule (§3.3) and KʷC delabialization (§3.4) must follow labiovelar absorption (§3.2), since absorption creates new labiovelars that then feed both simplification rules. All three also function as standing rules (§6), reapplying after every subsequent stage.

---

## 4. Stage 1: PIE to Late Western Indo-European

These rules represent shared developments of the western IE node — changes that Ghandwa shares with some combination of PGmc, PIt, and PC. They are ordered relative to one another as specified below.

### 4.1. Dental Cluster Simplification

> T + {T, s} → ss

Any dental stop immediately followed by another dental stop or by \*s merges into a geminate *ss*. This feeds the subsequent simplification rule.

> ss → s / _C

Geminate *ss* simplifies to single *s* before a following consonant.

**Examples:**
- \*widstós 'known' → widstos → wissos (TTs → ss) — cf. PGmc \*(ga)wissaz, OE ġewiss
- \*sedstós 'seated' → sedstos → sessos — cf. PGmc \*sessaz, ON sess

**Ordering:** Must precede thorn metathesis (§4.2), since dental+dental clusters are resolved before dental+velar clusters are reordered.

### 4.2. Thorn Metathesis

> TK → KT (word-internally; voicing and aspiration of each segment preserved)

A dental stop followed by a plain velar stop undergoes metathesis: the velar moves before the dental. Labiovelars are excluded (they have already been simplified before consonants by §3.4). Word-initial position is excluded.

This follows Jasanoff 2018 (via Ringe 2024) in treating the outcome as metathesis (Greek-type *kt*) rather than the assibilation path that fed PGmc (TK → KS → K after Grimm's Law).

**Examples:**
- \*h₂ŕ̥tḱos 'bear': after centumization → h₂r̥tkos; thorn metathesis → h₂r̥ktos → … → *arktos*
  (cf. Greek ἄρκτος; PGmc replaced the inherited form with the euphemism \*berō)

**Design note:** The metathesized cluster *kt* is left stable in Ghandwa. It constitutes a deliberate phonological tension: daughter languages may simplify it variously (assibilation, loss of one member, fricativization, etc.).

### 4.3. Laryngeal Changes

The PIE laryngeals (h₁, h₂, h₃) are resolved in a multi-step sequence. All substeps must be ordered as given; each feeds the next.

#### 4.3.1. Laryngeal Coloring

> h₂ colors adjacent \*e → a
> h₃ colors adjacent \*e → o
> h₁ is neutral (no coloring)

Coloring operates bidirectionally: both HV and VH sequences are affected. Only \*e is colored; \*a, \*o, \*i, \*u are immune.

**Examples:**
- \*h₂éḱweh₂ 'water' → h₂akwah₂ (both e's colored by adjacent h₂)
- \*h₃réǵs 'king' → h₃regs (h₃ does not color non-e vowels) → … → *rēks*

**Ordering:** Coloring must precede all laryngeal deletion rules, since the vowel quality established here is the permanent reflex.

#### 4.3.2. Contraction across Laryngeal

> VHV → V̄ (when both vowels are identical after coloring)

Two identical vowels separated by a laryngeal contract into a single long vowel; the laryngeal is lost.

When the flanking vowels are *not* identical after coloring, the laryngeal is not resolved at this stage. It surfaces as a diagnostic glottal stop ˀ in the output, flagging the form for manual review.

**Design note:** Ringe posits trimoric (overlong) vowels from certain VHV contractions in PGmc. Ghandwa does not maintain a trimoric distinction; all contractions yield ordinary long vowels.

#### 4.3.3. Pre-consonantal and Word-Final Laryngeal Loss with Compensatory Lengthening

> VH → V̄ / _{C, #}

A vowel immediately preceding a laryngeal lengthens; the laryngeal is lost. This applies both before consonants and at word boundaries.

**Examples:**
- \*séh₁mn̥ 'seed' → sēmn̥ (eH → ē) → … → *sēman*
- \*bʰráh₂tēr 'brother' → βrātēr (aH → ā) → … → *βrātēr*
- \*dʰéh₁ti- 'act of putting' → ðēti- (eH → ē)
- \*h₂éḱweh₂ → akwah₂ → akwā (word-final aH → ā) → *akʷā*

This rule applies to both high and low vowels. The lengthening of high vowels before laryngeals (\*iH → ī, \*uH → ū) is a Ghandwa design decision; some reconstructions restrict compensatory lengthening to non-high vowels.

#### 4.3.4. Word-Initial Laryngeal Loss

> #H → ∅ (before consonants or at the absolute beginning of a word)

Word-initial laryngeals are deleted without trace.

**Examples:**
- \*h₁ésti 'is' → esti → *esti*
- \*h₁éd- 'eat' → ed- → *ed-*
- \*h₂ŕ̥tḱos 'bear' → (after coloring) ar̥tkos (h₂ deleted word-initially)

#### 4.3.5. Interconsonantal Laryngeal Resolution

> CHC → CaC (in the initial syllable, i.e. when no vowel has yet appeared)
> CHC → CC (post-vocalically, i.e. when a vowel already precedes)

A laryngeal caught between two consonants (neither of which is a syllabic resonant) is resolved as *a* in the first syllable of the word, and deleted silently in subsequent syllables. This accounts for the "schwa indogermanicum" reflex without positing an intermediate reduced vowel.

**Examples:**
- \*ph₂tḗr 'father' → patēr (h₂ between p and t in initial syllable → a) → *patēr*
  (cf. PGmc \*fadēr < \*pətēr, with the same epenthesis)

#### 4.3.6. Residual Laryngeal Diagnostic

> H → ˀ (any surviving laryngeal)

Any laryngeal that has not been resolved by the preceding rules surfaces as a glottal stop ˀ in the output. This is an intentional diagnostic: it signals an environment not yet covered by the rule set and flags the form for manual review. It is not a Ghandwa phoneme.

### 4.4. Obstruent Devoicing before Voiceless Consonants

> {b, bʰ} → p / _{t, s}
> {g, gʰ} → k / _{t, s}
> {gʷ, gʷʰ} → kʷ / _{t, s}

Voiced and breathy-voiced obstruents are devoiced immediately before \*t or \*s. This is a core western IE process shared with PGmc and PIt.

**Examples:**
- \*dʰugh₂tḗr 'daughter' → dugh₂tēr → dugtēr (h₂ lost post-vocalically) → duktēr (g devoiced before t) → *ðuktēr*

**Design note:** Ringe defers voicing assimilation to individual daughter branches. Ghandwa applies it at the parent stage as a shared western development, following the evidence from PIt and PC.

**Ordering:** Must follow laryngeal resolution (§4.3), since laryngeal loss can create new obstruent+t/s clusters. Must precede aspirate fricativization (§5.3), since the rule references bʰ, gʰ, gʷʰ as inputs.

### 4.5. Osthoff's Law

> V̄RC → VRC (long vowel shortens before sonorant + consonant)

A long vowel is shortened when followed by a sonorant (r, l, m, n, w, y) and then a consonant in the same word. This is a PIE-era or early Core IE rule with reflexes across multiple branches.

**Examples:**
- \*h₁nḗh₃mn̥ 'name': h₁ deleted initially → nēh₃mn̥; h₃ colors ē → ō → nōmn̥; Osthoff fires (ō before m + C) → nomn̥ → … → *noman*
  (cf. PGmc \*namô, Goth. namo, OE nama — same Osthoff shortening, different resonant vocalism)

- \*h₂yúHn̥ḱos 'young' → (h₂ lost initially) yūn̥kos (uH → ū) → (Osthoff: ū before n̥+k) yun̥kos → … → *juwankos*
  (cf. PGmc \*jungaz, Goth. juggs — same shortening)

- \*h₂wéh₁n̥ts 'wind' → (h₂ lost) wéh₁n̥ts → (VH → V̄) wēn̥ts → (Osthoff: ē before n̥+t) wen̥ts → … → *wants*
  (cf. PGmc \*windaz — same shortening, different vocalism)

### 4.6. Tautosyllabic *e͡w* → *o͡w*

> e͡w → o͡w (where *e* and *w* are tautosyllabic, i.e. *w* is in coda)

When \*e and \*w belong to the same syllable — that is, when \*w stands before a consonant or at word end and thus occupies the coda — the diphthong \*e͡w becomes *o͡w*. Heterosyllabic sequences, where \*w is the onset of the following syllable (e.g. \*e.wi), are not affected.

This is a shared western IE innovation. The tautosyllabic condition explains why the rule applies in some morphological environments but not others within the same paradigm: in the u-stem genitive \*-ews, the *w* is in coda before *s*, so the rule fires and the genitive surfaces as *-ows*; in the u-stem dative \*-ewi, the *w* is onset of the next syllable, and the *e* is preserved.

**Examples:**
- u-stem gen.sg. \*-ews → *-ows* (w in coda before s; tautosyllabic; rule fires)
- u-stem dat.sg. \*-ewi → *-ewi* (syllabified e.wi; w is onset; heterosyllabic; rule does not fire)
- \*newos 'new' → *newos* (syllabified ne.wos; w is onset before vowel; heterosyllabic; rule does **not** fire)

**Orthographic note:** Coda *w* is written ⟨u⟩ in Ghandwa transliteration (as in Greek αυ, ευ and Latin au). Thus the genitive ending /ows/ is transliterated *-ous*, even though the phonological representation is /ows/. The IPA layer resolves the ambiguity; the transliteration layer reflects the script convention that glides in coda position are written as their corresponding vowel letters.

**Design note:** PGmc continued this change further (ow → aw → awz in certain environments). Ghandwa stops at *o͡w*.

**Ordering:** Must follow laryngeal resolution, since laryngeal loss can expose new *ew* sequences.

### 4.7. Pretonic Shortening

> V̄ → V / in the first syllable, when the accent falls on a later syllable

A long vowel in the first syllable of a word is shortened if the word accent falls on a non-initial syllable. This is a western IE innovation.

**Examples:**
- \*wih₁rós 'man' (if accent on second syllable): wīros (iH → ī) → wiros (pretonic shortening: ī in first syllable, accent on -ós) → *wiros*

When the accent position is not marked on the input form, the rule does not fire and the form is flagged with a warning. This is a computational safeguard, not a phonological claim.

**Ordering:** Must follow laryngeal resolution (§4.3) and Osthoff's Law (§4.5), since both create the long vowels that feed pretonic shortening.

**Design note on staging:** Osthoff's Law (§4.5) and pretonic shortening (§4.7) are both vowel-shortening rules placed in the same stage. They share no historical relationship — Osthoff's Law is conditioned by syllable structure (\*V̄RC), pretonic shortening by accent position. Both are placed after laryngeal resolution because both require resolved vowel length as input. They do not interact: Osthoff's Law shortens before sonorant+consonant regardless of accent; pretonic shortening shortens unaccented initial syllables regardless of following segments. The stage grouping is a notational convenience, not a chronological claim.

---

## 5. Stage 2: Late Western IE to Ghandwa

These rules are the innovations that define Ghandwa as a distinct branch. None are shared in their entirety with any single attested IE language, though each has partial parallels.

### 5.1. Syllabic Resonant Vocalization

> r̥ → ar, l̥ → al, m̥ → am, n̥ → an

The PIE syllabic resonants vocalize with an epenthetic *a* preceding the resonant. If a residual glottal stop ˀ (from an unresolved laryngeal) is adjacent to the syllabic resonant, it is consumed silently during vocalization.

**Examples:**
- \*ḱm̥tóm 'hundred' → km̥tom (centumization) → *kantom*
  (cf. PGmc \*hundą with u-vocalism; PC \*kantom with a-vocalism — Ghandwa aligns with Celtic)
- \*déḱm̥ 'ten' → dekm̥ → *dekam*
  (cf. PGmc \*tehun; Latin decem)
- \*wĺ̥kʷos 'wolf' → wl̥kʷos → *walkʷos*
  (cf. PGmc \*wulfaz with u-vocalism)
- \*ḱr̥h₂nóm 'horn (acc.)' → kr̥ˀnom (h₂ between consonants post-vocalically → ∅, leaving ˀ consumed by adjacent r̥) → *karnom*
  (cf. PGmc \*hurną; Latin cornū)
- \*n̥- (negative prefix) → *an-*
  (cf. PGmc \*un-; Greek ἀ(ν)-, Latin in-)

**Comparative note:** The three major western outcomes for syllabic resonants are:
- PGmc: \*uR (vowel before resonant, u-quality): \*m̥ → um, \*r̥ → ur
- PIt: \*eR or \*aR (vowel before resonant, variable quality): \*m̥ → em/am
- PC: \*aR (vowel after resonant in some analyses, a-quality): \*m̥ → am

Ghandwa's *aR* outcome is closest to Celtic in vowel quality and partially aligns with Germanic in having the vowel precede the resonant (CaRC, not CRaC). This hybrid outcome is phonetically natural — *a* is the cross-linguistically most common epenthetic vowel — and does not require positing that Ghandwa inherited from or imitated any single branch.

### 5.2. Hiatus Glide Insertion

> i → ij / _V (high front vowel inserts homorganic glide before a following vowel)
> u → uw / _V (high back vowel inserts homorganic glide before a following vowel)

When a high vowel (*i* or *u*, short or long) stands immediately before another vowel, a homorganic glide is inserted to break the hiatus: *j* after *i*, *w* after *u*. If the high vowel is long, it shortens as part of the same process (the length is, in effect, absorbed into the inserted glide).

This is a general hiatus-resolution rule with transparent phonetic motivation — high vowels in hiatus cross-linguistically tend to develop an on-glide into the following syllable.

**Examples:**
- \*h₂yúHn̥ḱos 'young': … yun̥kos → yuankos (syllabic resonant, §5.1) → yuwankos (u before a → u.wa) → *juwankos*
- Any -i.V- morpheme juncture (e.g. in verbal suffixes) → -ij.V-

**Ordering:** Must follow syllabic resonant vocalization (§5.1), since resonant vocalization creates new V.V hiatus sequences (e.g. u.n̥ → u.an → u.wan). Should precede s-voicing (§5.4), since the inserted glide is voiced and participates in the voicing environment.

### 5.3. Aspirate Fricativization

> bʰ → β, dʰ → ð, gʰ → ɣ, gʷʰ → ɣʷ

The PIE breathy-voiced (aspirated) stops become voiced fricatives. This is Ghandwa's most typologically distinctive innovation.

**Examples:**
- \*bʰer- 'carry' → *βer-*
- \*bʰráh₂tēr 'brother' → brātēr (laryngeals resolved) → *βrātēr*
- \*dʰéh₁ti- 'act of putting' → ðēti-
- \*dʰéǵʰōm 'earth' → dʰegʰōm (centumization) → *ðeɣōm*
- \*gʰóstis 'stranger, guest' → *ɣostis*
- \*gʷʰen- 'strike, kill' → *ɣʷen-*

**Comparative note:** The initial step — breathy-voiced stops becoming voiced fricatives — is the same as the third component of Grimm's Law in PGmc. Germanic then continued with a full chain shift (voiceless stops → voiceless fricatives, voiced stops → voiceless stops), while Ghandwa stops after this single change. The result is that Ghandwa has voiced fricatives where Germanic has them (from aspirates), but preserves the plain voiceless and voiced stops unchanged — a system that looks, in its stop inventory, more archaic than any attested western branch.

PIt and PC also shifted aspirates, but to plain voiced stops (merging with inherited \*b, \*d, \*g) — or, in word-initial position in some Celtic analyses, to voiceless fricatives. Ghandwa's voiced-fricative outcome is distinct from both.

**Ordering:** Must follow obstruent devoicing (§4.4), which references bʰ, gʰ, gʷʰ as inputs that devoice before \*t and \*s. After fricativization, these segments are β, ɣ, ɣʷ and would no longer be caught by the devoicing rule. The ordering is:

1. \*dʰugh₂tḗr → (laryngeals resolved) dugh₂tēr → dugtēr (h₂ lost between consonants post-vocalically) → duktēr (g devoiced before t, §4.4)
2. Then: duktēr → *ðuktēr* (dʰ → ð, §5.3; but the medial g has already been devoiced to k and is not affected)

If the order were reversed, fricativization would produce ðuɣtēr, and devoicing (which targets voiced obstruents, not fricatives) would miss the ɣ, yielding incorrect \*ðuɣtēr.

### 5.4. Intervocalic s-Voicing

> s → z / [+voiced]_[+voiced]

The voiceless fricative \*s becomes voiced *z* when flanked by voiced sounds (vowels, sonorants, or voiced obstruents).

**Examples:**
- \*wirósyo (gen.sg. of 'man') → wirosjo (y → j) → wiro**z**jo → *wirozio*
- \*snusós 'daughter-in-law' → snusos → snu**z**os → *snuzos*

**Comparative note:** The PGmc parallel is Verner's Law, which conditions *s*-voicing on PIE accent position rather than on the voicing of adjacent segments. The two rules often produce the same surface result — *s* between vowels becomes *z* in both systems — but the conditioning is formally different. Ghandwa's rule is simpler (purely phonotactic) and makes no reference to accent.

### 5.5. Glide Respelling

> y → j (orthographic)

The palatal glide, inherited as PIE \*y, is respelled as *j* in Ghandwa orthography. This is a writing convention, not a sound change; the phonetic value remains [j].

---

## 6. Standing Rules: Synchronic Surface Constraints

Three rules function as standing surface constraints rather than diachronic changes. They apply after every stage and run in a convergence loop (reapplying until no further changes occur), ensuring that the surface phonotactics of labiovelars are maintained regardless of what intermediate forms are produced by the diachronic rules.

### 6.1. Labiovelar Absorption (standing)

> Kw → Kʷ

Identical to §3.2. Any surface sequence of velar + w is treated as a labiovelar.

### 6.2. Labiovelar Delabialization before Consonants (standing)

> Kʷ → K / _C

Identical to §3.4. Ensures that no labiovelar ever surfaces before a consonant, even if one is created by a preceding rule's output.

### 6.3. Boukólos Rule (standing)

> Kʷ → K / adjacent to u, ū, w

Identical to §3.3. Ensures that no labiovelar ever surfaces next to a rounded segment.

**Interaction example:** The o-stem noun \*perkʷus ~ \*perkʷéws 'oak' illustrates the standing rules in action. In the nominative, \*kʷ stands before \*u and delabializes (Boukólos): *perkus*. In the genitive, \*kʷ stands before \*e and is preserved: *perkʷews*. The result is a stem alternation kʷ ~ k conditioned by the following vowel — a deliberate unresolved tension that daughter languages may level in either direction.

---

## 7. Deliberate Tensions and Deferred Resolutions

A central design principle of Ghandwa is that not every phonological instability is resolved at the parent-language stage. The following features are left as tensions that daughter languages are expected to resolve independently:

- **kt clusters** (from thorn metathesis, §4.2): stable in Ghandwa; daughters may simplify
- **Labiovelar stem allomorphy** (from standing rules, §6): alternations like kʷ ~ k within paradigms are not leveled
- **Voiced fricatives** β, ð, ɣ, ɣʷ: stable; daughters may devoice, stop, or merge them
- **Labiovelars** kʷ, gʷ before front vowels: preserved; daughters may palatalize, labialize, or simplify
- **Nasal + obstruent clusters** (np, nk, nt, etc.): no nasal assimilation; daughters may assimilate
- **Non-high VV hiatus** from laryngeal loss: hiatus involving high vowels is resolved by glide insertion (§5.2), but hiatus between non-high vowels (e.g. *a.o*, *e.a*) remains unresolved; daughters may contract, insert glides, or tolerate
- **sr clusters**: preserved; daughters may dissimilate (sr → θr, as in Italic/Celtic)
- **βu- onset**: flagged as a likely site of phonological mutation in daughter languages

---

## 8. Rules Not Applied

The following rules attested in sister branches are explicitly not part of Ghandwa's derivation. They are listed here to clarify the limits of the system.

| Rule | Attested in | Reason for exclusion |
|---|---|---|
| Grimm's Law (full chain shift) | PGmc | Germanic-specific; Ghandwa applies only the aspirate → fricative step |
| Verner's Law (accent-conditioned s-voicing) | PGmc | Replaced by phonotactic s-voicing (§5.4) |
| o/a merger | PGmc | Germanic-specific; Ghandwa preserves the distinction |
| gʷ → b | PC | Celtic-specific |
| p-loss | PC | Celtic-specific |
| Auslautgesetze (word-final -m → -n → ∅) | PGmc | Ghandwa preserves word-final -m |
| Sievers' Law (glide ~ vowel+glide alternations) | Deferred | Not yet decided; see `ghandwa_verbs.md` |
| Szemerényi's Law (compensatory lengthening in nom.sg.) | Pre-PIE | Applied to input forms before they enter the transformer; not a Ghandwa-stage rule |
| p…kʷ → kʷ…kʷ labial-labiovelar dissimilation | PIt, PC | Deferred to daughter languages |
| nw → nn, ln → ll assimilation | PGmc | Deferred to daughter languages |
| sr → θr sibilant dissimilation | PIt, PC | Deferred to daughter languages |

---

## 9. Summary of Rule Ordering

The complete derivation, in order:

**Pre-Stage (§3):**
1. Centumization: ḱ → k, ǵ → g, ǵʰ → gʰ
2. Labiovelar absorption: Kw → Kʷ
3. Boukólos rule: Kʷ → K / adj. u, ū, w
4. Labiovelar delabialization: Kʷ → K / _C

**Stage 1 — PIE to Late Western IE (§4):**
5. Dental simplification: T{T,s} → ss; ssC → sC
6. Thorn metathesis: TK → KT (word-internally)
7. Laryngeal coloring: h₂ → a, h₃ → o (adjacent to e)
8. VHV contraction: VHV → V̄ (identical vowels)
9. VH lengthening: VH → V̄ (before C or #)
10. HV deletion: H → ∅ (adjacent to vowel, after coloring)
11. H-initial deletion: #H → ∅
12. Interconsonantal H: CHC → CaC (initial) / CC (elsewhere)
13. Residual H → ˀ
14. Obstruent devoicing: voiced obstruent → voiceless / _{t, s}
15. Osthoff's Law: V̄RC → VRC
16. Tautosyllabic e͡w → o͡w
17. Pretonic shortening: V̄ → V (unaccented first syllable)

*Standing rules apply (§6)*

**Stage 2 — Late Western IE to Ghandwa (§5):**
18. Syllabic resonant vocalization: R̥ → aR
19. Hiatus glide insertion: i → ij / _V; u → uw / _V
20. Aspirate fricativization: bʰ → β, dʰ → ð, gʰ → ɣ, gʷʰ → ɣʷ
21. Intervocalic s-voicing: s → z / [+voiced]_[+voiced]
22. Glide respelling: y → j

*Standing rules apply (§6)*

---

## 10. Worked Examples

### 10.1. \*wirós ~ \*wirósyo 'man' (o-stem, masc.)

| Step | Nominative | Genitive |
|---|---|---|
| Input | wiros | wirosyo |
| y → j (§5.5) | — | wirosjo |
| s → z (§5.4) | — | wirozjo |
| **Output** | ***wiros*** | ***wirozio*** |

A transparent derivation: no laryngeals, no syllabic resonants, no clusters. The only changes are Stage 2 voicing of intervocalic *s* and the orthographic *y* → *j*.

### 10.2. \*h₂ŕ̥tḱos 'bear' (o-stem, masc.)

| Step | Form |
|---|---|
| Input | h₂r̥tḱos |
| Centumization (§3.1) | h₂r̥tkos |
| H-initial deletion (§4.3.4) | r̥tkos |
| Thorn metathesis (§4.2) | r̥ktos |
| Syllabic resonant (§5.1) | arktos |
| **Output** | ***arktos*** |

Centumization feeds thorn metathesis by converting ḱ to k, creating the TK sequence that undergoes metathesis. The initial laryngeal is lost without trace (no preceding vowel to color or lengthen). The syllabic resonant vocalizes in Stage 2 to give the characteristic Ghandwa *ar*.

### 10.3. \*ph₂tḗr 'father' (r-stem, masc.)

| Step | Form |
|---|---|
| Input | ph₂tēr |
| CHC → CaC (§4.3.5) | patēr |
| **Output** | ***patēr*** |

The laryngeal h₂ is caught between two consonants (p and t) in the initial syllable and resolves to *a*. No further rules apply. Cf. PGmc \*fadēr < \*pətēr, with the same epenthetic vowel (later lowered in Germanic).

### 10.4. \*h₁nḗh₃mn̥ 'name' (men-stem, neut.)

| Step | Form |
|---|---|
| Input | h₁nēh₃mn̥ |
| H-initial deletion (§4.3.4) | nēh₃mn̥ |
| Laryngeal coloring (§4.3.1) | nōmn̥ (h₃ colors ē → ō) |
| VH → V̄ (§4.3.3) | nōmn̥ (ō already long; h₃ deleted) |
| Osthoff's Law (§4.5) | nomn̥ (ō shortens before m + C) |
| Syllabic resonant (§5.1) | noman |
| **Output** | ***noman*** |

This form demonstrates the interaction of laryngeal coloring, compensatory lengthening, and Osthoff's Law. The h₃ first colors the adjacent vowel (ē → ō), then is deleted with compensatory lengthening (but the vowel is already long, so the length is redundant). Osthoff's Law then shortens the long ō before the cluster mn̥. Finally, the syllabic nasal vocalizes in Stage 2.

### 10.5. \*dʰugh₂tḗr 'daughter' (r-stem, fem.)

| Step | Form |
|---|---|
| Input | dʰugh₂tēr |
| CHC → CC (§4.3.5) | dʰugtēr (h₂ between g and t, post-vocalic → ∅) |
| Obstruent devoicing (§4.4) | dʰuktēr (g → k before t) |
| Aspirate fricativization (§5.3) | ðuktēr |
| **Output** | ***ðuktēr*** |

The ordering of devoicing before fricativization is critical here. The medial *g* must devoice to *k* before *t* (§4.4) while it is still a stop. Then the initial *dʰ* fricativizes to *ð* (§5.3). If fricativization applied first, the *gʰ* (which has already been stripped of aspiration by laryngeal resolution) would remain *g* and incorrectly survive as a voiced stop before *t*.

### 10.6. \*h₂yúHn̥ḱos 'young' (o-stem, masc.)

| Step | Form |
|---|---|
| Input | h₂yúHn̥ḱos |
| Centumization (§3.1) | h₂yuHn̥kos |
| H-initial deletion (§4.3.4) | yuHn̥kos |
| VH → V̄ (§4.3.3) | yūn̥kos |
| Osthoff's Law (§4.5) | yun̥kos (ū before n̥ + k → u) |
| Syllabic resonant (§5.1) | yuankos |
| Hiatus glide insertion (§5.2) | yuwankos (u before a → u.wa) |
| y → j (§5.5) | juwankos |
| **Output** | ***juwankos*** |

The *uw* sequence arises from hiatus glide insertion (§5.2), not from the *ū* itself. After Osthoff's Law shortens *ū* to *u*, syllabic resonant vocalization produces the sequence *u.a* (from *un̥* → *uan*), which creates a hiatus environment. The glide insertion rule then resolves it: *u.a* → *u.wa*. The derivation thus passes through three distinct stages: long *ū* (from compensatory lengthening), short *u* (from Osthoff), and *uw* (from hiatus resolution).

### 10.7. \*kʷekʷlos 'wheel' (o-stem, masc.)

| Step | Form |
|---|---|
| Input | kʷekʷlos |
| KʷC → K (§3.4) | kʷeklos (second kʷ delabializes before l) |
| **Output** | ***kʷeklos*** |

The second labiovelar stands before the liquid *l* — a consonant — and delabializes by §3.4. The first labiovelar, before the vowel *e*, is preserved. This is a minimal illustration of labiovelar distribution in Ghandwa: preserved before vowels, simplified before consonants.

---

*This chapter will be expanded as the lexicon grows and additional worked examples become available. Forms from inscription work and verbal paradigms will be added as those systems are finalized.*
