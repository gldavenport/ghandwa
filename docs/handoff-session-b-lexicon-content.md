# Handoff: Session B — Lexicon Content: Pending Flags & Water Words

**Date:** 2026-05-16  
**Scope:** Linguistic judgment session. Resolve or advance five flagged lexicon items and four verb stubs.

---

## Context

The lexicon is in NocoDB (localhost:8080, `ghandwa-db/`), 716 rows × 50 columns. Entry status pipeline: stub → draft → hold → canon. Items below are either `hold` or missing entirely.

Primary references: Ringe 2017 (PIE to Proto-Germanic), Kroonen EDPG, de Vaan EDL, Rix + Kümmel LIV². Ghandwa is a conservative western centum branch: aspirates → voiced fricatives (bʰ→β, dʰ→ð, gʰ→ɣ, gʷʰ→ɣv); syllabic resonants → CaRC (r̥→ar, l̥→al, m̥→am, n̥→an). See `docs/notation.md` for full conventions, `docs/phonological-history.md` for sound change rules.

---

## Item 1 — *óngvan ~ angʷéns*

**Status:** `hold` — stem class and full etymology pending.

PIE source is *h₂engʷʰ- / *h₂ongʷʰ- 'snake, serpent' (cf. Lat. *anguis*, Lith. *angìs*, OIr. *escung* 'eel'). The Ghandwa forms suggest an n-stem or r/n heteroclite but the paradigm hasn't been worked out. Questions:

- Is this an n-stem (*h₂ongʷʰ-en-) or a root noun with n-extension?
- Does the aspiration produce ɣv- (from gʷʰ) in Ghandwa? Expected: *h₂ongʷʰ-en-s → óngvan (nom.), angʷéns (gen.) — but the gʷʰ behavior in the oblique needs checking against the transformer.
- Cross-reference with *angʷis* (the i-stem snake word, if separately entered).

---

## Item 2 — *udṓr ~ udnós* / *vódar ~ udéns*

**Status:** `hold` — two water words exist; relationship and dialectal distribution unresolved.

PIE has two heteroclitic paradigms for 'water':
- Acrostatic: *wódr̥ (nom.) ~ *wédns (gen.) — o-grade nom., e-grade gen.
- Proterokinetic: *wódr̥ (nom.) ~ *udéns (gen.) — o-grade nom., zero-grade gen.

Ghandwa appears to have inherited both, surfacing as:
- *udṓr ~ udnós* — collective/mass form (the great water, the sea)?
- *vódar ~ udéns* — singular/countable (a body of water)?

Questions to resolve:
- Which ablaut pattern does each form reflect?
- Is the distinction singular vs. collective, or dialectal?
- How does this interact with the existing entry *vodán* (if present)?
- Check `lexicon-staging.md` §r/n heteroclites for the full staged paradigm options.

---

## Item 3 — *svézōr*

**Status:** draft — missing `nom_stem_class`.

PIE *swésōr 'sister'. Ghandwa *svézōr is regular (s→sv via w-glide, z from *s between vowels). This is an r-stem (or -r̥/-r heteroclite). Nom_stem_class should be set — probably `r-stem` or `r/n-stem`. Check paradigm against `grammar/paradigms-nominal.md` and set the field in NocoDB.

---

## Item 4 — *véstrom*

**Status:** flagged for collision with Westeros/fantasy conlang associations.

The form is phonologically regular from PIE *wes-tro-m or similar. The question is whether the gloss ('place, location, site') and form together create an unacceptable association. Options:
- Keep as-is (the connection is superficial and the etymology is sound)
- Regloss to something less generic
- Replace with a different derivational strategy for 'place/location'

Bring your own judgment — this is an aesthetic/design call more than a linguistic one.

---

## Item 5 — Four verb stubs

From `lexicon-gaps.md` Tier 3. All exist only as blank-lemma stubs in NocoDB. Use `grammar/verb-eval-template.md` to evaluate each.

| Gloss | PIE root candidates | Notes |
|---|---|---|
| hold / grasp (stative) | *\*seǵʰ-* or *\*kap-* | *kapiéti* already covers "take/seize"; need stative "hold" |
| run / flow | *\*srew-* | *dā́nu* is noun only; no motion verb |
| throw | *\*h₁yeh₁-* or *\*gʷelh₁-* | — |
| cut | *\*sek-* | Basic technology verb |

For each: run the decision logic in `verb-eval-template.md` §1, choose a stem type, derive the Ghandwa form, verify against the transformer (`tools/pie-2-ghandwa.jsx`).

---

## Key files

| File | Purpose |
|---|---|
| `docs/notation.md` | Orthography, field conventions |
| `docs/phonological-history.md` | Sound change rules |
| `grammar/paradigms-nominal.md` | Nominal paradigms |
| `grammar/verbs.md` | Verb classification schema |
| `grammar/verb-eval-template.md` | Verb adoption decision framework |
| `vocab/lexicon-staging.md` | §r/n heteroclites has water word paradigm options |
| `tools/pie-2-ghandwa.jsx` | Transformer — authoritative for surface forms |
