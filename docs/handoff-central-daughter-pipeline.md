# Handoff — Central Daughter Pipeline Review
**Date:** 2026-05-27

---

## What Was Accomplished This Session

### Linguistics
- Worked through the complete Central daughter (B) voiced fricative system environment by environment, mining the lexicon for attested cases at each stage.
- Decided rules in this order:
  - N_ → hardening (β→b, ð→d, ɣ→g, ɣʷ→gʷ) — typologically strongest
  - ɣʷ → w / N_ already resolved; ɣʷ → w / _V (all prevocalic)
  - #_R → hardening (β→b, ð→d, ɣ→g) — onset fortition, attestationally parallel to PIt frater, PG brōþēr
  - β → w / _V and _C (all non-final, after N_ and #_R resolved)
  - ð → r / {V,R}_V — rhotacism; liquids transparent
  - ɣ → w / {V,R}_V — gliding; liquids transparent
  - _C (non-liquid): ð→θ, ɣ→x (β already w)
  - Default devoicing: ð→θ, ɣ→x / elsewhere (#_V, word-final)
  - Word-final: unspecified, unattested, comment only
  - R_ vacuous in non-_V contexts; liquid transparent for all voiced fricatives

### Files Updated (all written to local, pushed to GitHub)
- `tools/pie_transformer/pipelines/daughter_b.py` — fully rewritten (rules 2B.1–2B.7)
- `tools/pie_transformer/pipelines/daughter_c.py` — docstring fix only (#s>z initial rule noted as dropped)
- `docs/grammar/ch5-daughters/` — new directory with 6 files migrated from `docs/daughters.md`:
  - `ch5-01-overview.md`
  - `ch5-02-late-common-ghandwa.md`
  - `ch5-03-comparative-phonology.md` (2B fully rewritten, 2C corrected)
  - `ch5-04-comparative-morphology.md`
  - `ch5-05-lexicon-testing.md`
  - `ch5-appendices.md`
- `docs/file-map.md` — updated with 2026-05-27 migrations
- `docs/daughters.md` — superseded, retained as archive pending deletion confirmation

---

## Open Issue: Central Daughter Pipeline May Over-Lenite

At end of session, discovered that \*bʰr̥ǵʰús → Ghandwa *βargus* → Central *wawwus* (or similar) under the new pipeline. The cumulative effect of β→w/_V (initial) plus rɣ→rw (internal, rule 2B.5) produces a form too far from the source.

The problem is likely **β→w broadly in _V** — the rule may be too aggressive at word-initial position (#_V), and/or the R_ transparency for ɣ produces too much internal lenition.

### Options Identified (not yet decided)

| Option | β #_V | R_ɣ_V | *βargus* result |
|---|---|---|---|
| 1 | ɸ | w | *ɸarwus* |
| 2 | w | x | *warxus* |
| 3 | ɸ | x | *ɸarxus* |
| 4 | w (keep current) | w | *wawwus* |
| 5 | ɸ (after voiced C only → w) | w | *ɸarwus* |

Other affected test cases to evaluate:
- *βarðos* (beard, \*bʰerdʰ-o-): β initial + rð internal
- *βraːteːr* (brother, \*bʰréh₂tēr): #_R → b (rule 2B.3, unaffected by this issue)
- *margus* (brief, \*mr̥ǵʰús): no initial β; rɣ→rw internal — *marwus*
- *warðom* (word, \*wordʰom): initial w already, rð internal → *warrðos* → *warros*

---

## Immediate Next Session Tasks

1. **Decide the β #_V question** — Option 1 (ɸ) is probably most defensible typologically (cf. Italic *f-*). Option 3 (ɸ + ɣ devoices after liquid) is most conservative.

2. **Verify `_is_word_initial` is importable from `_common.py`** — it's used in the new `daughter_b.py` (rule 2B.3) but was only confirmed present in `daughter_c.py` imports. Check before running the pipeline.

3. **Run test forms through updated `daughter_b.py`** — once the β #_V question is resolved and any import issues fixed. Key test forms:
   - *βargus*, *βarðos*, *βraːteːr* (initial β cases)
   - *melðoː*, *warðom* (R_ cases)
   - *margus* (rɣ internal)
   - *alβos* (lβ internal)

4. **Pre-form population** — deferred until pipeline is verified. Several test entries have null `lemma_1_pre_ipa`; do not populate until surface forms are confirmed correct.

5. **melðoː pre-form** — null in lexicon; needs formation type confirmed before a pre-form can be derived.

---

## Key Decisions Still Open

- β → w / #_V vs. β → ɸ / #_V (central to the over-lenition problem)
- Whether R_ɣ_V → w or x (feeds into option choice above)
- Central labiovelar conditioned-reduction triggers (Appendix I.B, long-standing)
- Word-final voiced fricatives: unspecified, unattested; flag any new entries
