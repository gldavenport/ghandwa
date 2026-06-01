# Handoff — Central Daughter Pipeline, Session 2026-05-31

---

## What Was Accomplished This Session

This session was entirely analytical — no files were edited. All implementation is deferred until Gary is back on his home system with Filesystem MCP live. Decisions were made on the Central daughter (B) voiced fricative ruleset, resolving the over-lenition problem identified at the end of the previous session. New test forms were added to the suite, exposing upstream transformer dependencies and a previously undocumented Ghandwa-stage rule.

---

## Detailed Summary: Voiced Fricative System — Journey to Decisions

### The Over-Lenition Problem (Carried from Previous Session)

The previous session ended with the discovery that \*bʰr̥ǵʰús → Ghandwa *βargus* → Central *wawwus* (or similar) under the then-current pipeline. Two independent rules were both firing:

1. **β → w / #\_V** — initial labial voiced fricative before vowel glides to w
2. **ɣ → w / {V,R}\_V** — velar voiced fricative glides to w after vowel or liquid

The compound effect was total obliteration of the source form's phonological identity. Neither rule was individually indefensible, but their interaction was the problem.

### Rule 1: β → w / #\_V

The issue with this rule is typological. In Italic — the primary comparandum for initial bʰ — the outcome is *f-* (voiceless labial fricative), not *w-*. Latin *frāter*, *ferre*, *fīlius* all reflect PIt \*bʰ → f / #\_. Germanic keeps *b-* via Grimm. No major IE branch gives *w-* word-initially from \*bʰ-. An additional problem: β→w word-initially produces merger with inherited *w-* roots, destroying a lexical distinction.

**Decision: β → ɸ / #\_.** Motivated by Italic parallel and lexical distinctiveness. This also has the desirable property of giving Central a word-initial labial fricative distinct from both inherited w- and the internal β→w reflex.

### Rule 2: ɣ → w / {V,R}\_V

This rule was identified as typologically unsound. The natural lenition path for a voiced velar fricative is not to a labio-velar glide — that requires a rounding source. The w outcome is motivated for **ɣʷ** (labiovelar loses the stop, keeps rounding), not for plain ɣ. The rule appeared to have been extended from ɣʷ→w by analogy, which is the error.

The natural outcomes of VɣV cross-linguistically, ranked:
1. **∅ (+ compensatory lengthening)** — most common; Spanish *lago* [laɣo] → deletion in fast speech; Greek laryngeal/fricative loss between vowels
2. **j** — before/after front vowels
3. **h** — debuccalization
4. **w** — unnatural from plain ɣ without rounding source
5. **g** — reversal of lenition; requires conditioning trigger

The **R\_V context** is different from plain V\_V. Sonorants (N and R) can condition fortition — post-nasal hardening (2B.1) is already in the system on exactly this logic. Extending the fortition trigger to liquids is the same phonological argument, just expanding the conditioning class from {N} to {N, liquid}. ɣ→g / R\_V is therefore defensible: the liquid is doing work, just as the nasal does in 2B.1.

For **V\_V (plain intervocalic)**, ɣ→g has no trigger and is typologically a marked reversal. The honest answer is ∅ + lengthening. Gary accepted this but noted that heterovocalic hiatus resolution from VɣV deletion should not be specified yet — there are no attested cases to constrain it. Decisions:

- **VɣV (same vowel):** coalescence → V̄. Uncontroversial.
- **VɣV (different vowels):** deletion → VV hiatus. Resolution deferred.

### Rule Ordering Tightening

The previous handoff's 11-rule table had two redundancies:

1. 2B.7 was stated as {N,R}\_V, but N\_ɣ is already covered by 2B.1. The N specification in 2B.7 was redundant.
2. 2B.10 and 2B.11 were separate rules with the same output (ð,ɣ → θ,x) in different environments. Collapsed into one elsewhere rule.

Result: 11 rules → 9 rules, no content change.

### New Test Forms — Transformer Dependencies Exposed

Four new forms were added to the test suite. Two of them exposed that hand-derivation at the daughter stage was incorrect because upstream PIE-stage rules apply first:

- **\*dʰgʷʰitís** — initial cluster; thorn metathesis fires before daughter rules. Hand-tracing the initial cluster as a daughter-stage problem was wrong.
- **\*snígʷʰs** — gʷʰs → ks is a PIE-stage cluster reduction; the daughter pipeline never sees ɣʷ here. The "gap" flagged in 2B was vacuous.

This confirmed that the transformer must be run before any further rule analysis on forms with potential upstream interactions.

- **\*h₂éngʷʰis** — N\_ɣʷ context; 2B.1 applies (gʷ result), not 2B.2. First confirmed case for both 2B.1 (ɣʷ column) and the 2B.1 < 2B.2 ordering being non-vacuous.
- **\*h₁ógʷʰis** — V\_ɣʷ\_V context; 2B.2 applies (w result). First confirmed case for 2B.2. Note: Central *owis is formally identical to the expected reflex of \*h₃éwis 'sheep' — potential merger, flagged.
- **\*negʷʰrós** — ɣʷ\_R context; no rule covers this. Genuine gap, but upstream rules may resolve it; transformer must be run first.

### New Ghandwa-Stage Rule Identified

Thorn metathesis on \*dʰgʷʰitís produces an initial cluster \*ɣʷð- in Ghandwa. No existing rule handles this. The typologically natural resolution is initial dorsal drop: ɣʷð- → ð-. This is a **Ghandwa-specific rule not currently in any documentation.** The conditioning needs to be verified: is it specifically ɣ(ʷ) before a dental fricative at #\_, or broader? Since thorn metathesis is the only PIE source sequence that can produce this cluster in Ghandwa, the rule may be statable narrowly as a thorn-cluster resolution rule.

---

## Full Revised 2B Ruleset (Decided, Not Yet Implemented)

| Rule | Input | Environment | Output | Notes |
|---|---|---|---|---|
| 2B.1 | β, ð, ɣ, ɣʷ | N\_ | b, d, g, gʷ | Post-nasal hardening |
| 2B.2 | ɣʷ | \_V | w | Labiovelar prevocalic gliding; must follow 2B.1 |
| 2B.3 | β, ð, ɣ | #\_R | b, d, g | Onset fortition before sonorant |
| 2B.4 | β | #\_ | ɸ | Initial labial fricative; cf. Italic f-; must follow 2B.3 |
| 2B.5 | β | \_V, \_C (non-initial, non-final) | w | Labial gliding, non-initial |
| 2B.6 | ð | {V,R}\_V | r | Rhotacism; liquids transparent |
| 2B.7 | ɣ | R\_V | g | Sonorant fortition (R only; N covered by 2B.1) |
| 2B.8 | ɣ | V\_V (same vowel) | V̄ | Coalescence |
| 2B.9 | ɣ | V\_V (diff. vowels) | ∅ | Deletion; hiatus unresolved |
| 2B.10 | ð, ɣ | elsewhere | θ, x | Default devoicing |

**Required ordering:** 2B.1 < 2B.2; 2B.3 < 2B.4 < 2B.5; {2B.6, 2B.7, 2B.8, 2B.9} < 2B.10.

**Feed warning:** if 2B.6 (ð→r) creates a new liquid adjacent to ɣ\_V, it feeds 2B.7. No attested case yet; flag if encountered.

**Provisional rules (no attested feeding cases):** 2B.8, 2B.9. Mark as provisional in documentation.

---

## Updated Test Suite

| PIE form | Ghandwa input | Key rule(s) | Expected Central output | Notes |
|---|---|---|---|---|
| \*bʰr̥ǵʰús | *βargus | 2B.4, 2B.7 | *ɸargus | Original over-lenition test case |
| \*bʰerdʰ-o- | *βarðos | 2B.4, 2B.6 | *ɸarros | Initial β + rð internal |
| \*bʰréh₂tēr | *βraːteːr | 2B.3 | *braːteːr | #\_R; unaffected by β #\_V question |
| \*mr̥ǵʰús | *margus | 2B.7 | *margus | rɣ→rg; no initial β |
| \*wordʰom | *warðom | 2B.6 | — | rð internal; run transformer |
| *melðoː | *melðoː | 2B.6 | — | Pre-form null; formation type unconfirmed |
| *alβos | *alβos | 2B.5 | *alwos | lβ internal |
| \*h₂éngʷʰis | *anɣʷis | 2B.1 | *angʷis | First 2B.1 ɣʷ case; confirms 2B.1 < 2B.2 ordering |
| \*h₁ógʷʰis | *oɣʷis | 2B.2 | *owis | First 2B.2 case; merger risk with \*h₃éwis reflex |
| \*negʷʰrós | *neɣʷros | — | **run transformer** | ɣʷ\_R gap; may be resolved upstream |
| \*snóygʷʰos | *snóyɣʷos | 2B.2 | *snóywos | 2B.2 confirmed in glide context |
| \*snígʷʰs | — | PIE-stage: gʷʰs→ks | **run transformer** | Gap was vacuous; upstream rule applies |
| \*dʰgʷʰitís | — | PIE-stage: thorn metathesis | **run transformer** | Upstream; also triggers new Ghandwa rule (see below) |

---

## Decisions Made This Session

1. β → ɸ / #\_ (replaces β → w / #\_V; typologically motivated by Italic)
2. ɣ → g / R\_V (sonorant fortition; same logic as existing N\_ hardening)
3. VɣV same vowel → V̄ (coalescence)
4. VɣV different vowels → ∅ + hiatus (resolution deferred)
5. 2B.7 N\_ specification dropped (redundant with 2B.1)
6. 2B.10/2B.11 collapsed into single elsewhere rule
7. New test forms added: \*h₂éngʷʰis, \*h₁ógʷʰis, \*negʷʰrós, \*snóygʷʰos, \*snígʷʰs, \*dʰgʷʰitís
8. Ghandwa initial dorsal drop rule identified: ɣ(ʷ)ð- → ð- / #\_ (post-thorn-metathesis cluster resolution)

---

## Open Items and Blockers

### Blocking: Transformer Must Run First

The following cannot be decided until transformer output is in hand:

- \*negʷʰrós — is ɣʷ\_R a real gap or vacuous after upstream rules?
- \*snígʷʰs — confirm gʷʰs→ks fires at PIE stage
- \*dʰgʷʰitís — confirm thorn metathesis output before applying Ghandwa dorsal drop rule
- \*warðom, \*melðoː — run through pipeline to confirm rð behavior

### Blocking: Implementation Deferred (Home System Required)

- `tools/pie_transformer/pipelines/daughter_b.py` — **file exists with old (over-leniting) ruleset** written in the 2026-05-27 session; needs rewriting with the revised 2B ruleset above, not creating from scratch
- `_is_word_initial` import check in `daughter_b.py` (carried from previous handoff)
- `docs/grammar/ch5-daughters/ch5-03-comparative-phonology.md` — **file exists with old 2B section** written in the 2026-05-27 session; needs rewriting with revised 2B rules, not creating from scratch
- New Ghandwa rule (initial dorsal drop) to be added to `docs/grammar/ch3-development/sec3-2-sound-changes/`
- `docs/daughters.md` deletion confirmation (carried from previous handoff)

### Explicitly Deferred (No Blocker, Low Priority)

- VɣV heterovocalic hiatus resolution — no attested cases, defer to later stage or sub-daughter
- Central labiovelar conditioned-reduction triggers — Appendix I.B, long-standing
- Word-final voiced fricatives — unspecified, unattested; flag any new entries
- Pre-form population — blocked on pipeline verification
- \*melðoː pre-form — formation type unconfirmed

### Deferred by Design

- Typological audit of full 2B voiced fricative system against natural language comparables — planned for after implementation and test run

---

## Carried Forward from Previous Handoff (Unchanged)

- `_is_word_initial` import check in `daughter_b.py` (rule 2B.3 depends on it)
- `docs/daughters.md` superseded; retained as archive pending deletion confirmation
- Daughter A and B Stage 3 phonology unspecified
- Daughter B renderer: confirm `_ghandwa_surface` implementation
- 2B.8 and 2B.9 provisional — no attested feeding cases

---

## Implementation Sequence (When Back on Home System)

1. Run transformer on all **run transformer** test forms
2. Resolve any upstream surprises before touching `daughter_b.py`
3. Rewrite `daughter_b.py` with revised 2B ruleset
4. Check `_is_word_initial` import
5. Run full test suite through updated pipeline
6. Add Ghandwa initial dorsal drop rule to sound changes doc
7. Rewrite `ch5-03-comparative-phonology.md`
8. Typological audit
9. Confirm and delete `docs/daughters.md`
