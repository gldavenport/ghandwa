# Ghandwa Project Handoff
**Date:** 2026-05-15  
**Scope:** Python transformer (`tools/pie_transformer/`) + outstanding repo work  
**Preceding session:** Built Python transformer from scratch, ran and debugged against live lexicon

---

## 1. Spec Situation

The original spec (`pie-transformer-handoff-spec-v2.md`, ChatGPT-authored) is **stale**. The implementation diverged from it during this session in several significant ways. The code is currently the source of truth. `tools/README.md` covers only the old JSX transformer and does not mention the Python package.

**Action needed:** Either update the spec to match the code, or write a new `tools/pie_transformer/README.md` documenting current architecture. The latter is probably cleaner. See §4 for what needs to be documented.

---

## 2. Python Transformer: Outstanding Implementation

All files are in `tools/pie_transformer/` on the local filesystem (also committed to repo at `github.com/gldavenport/ghandwa`).

### 2.1 IPA Syllabifier + Stress Mark
**Handoff doc:** `tools/pie_transformer/docs/handoff-ipa-syllabifier.md`  
**File to edit:** `render.py` → `_ghandwa_ipa()`  
**Current state:** Stub. Returns `/joined-tokens/` with no syllable boundaries or stress mark.  
**What's needed:** Onset-maximization syllabifier + replace U+0301 acute on accented token with IPA `ˈ` before the syllable onset. Both must be done together. See the handoff doc for full spec, algorithm sketch, and test cases.

### 2.2 Provisional Test Suite Expected Outputs
**File:** `tests/test_pipelines.py`  
**Current state:** 14 starter test inputs run but mismatches only log to stderr and `REVIEW_LOG`; they don't assert. Expected outputs are not filled in.  
**Action:** Run each starter form through the pipeline, verify the output is linguistically correct, then fill in the `expected` values and convert from provisional logging to hard assertions.

Starter inputs (from original spec):
`wĺ̥kʷos, ǵʰoysós, h₂éymō, gʰórdʰos, dʰuh₂mós, ph₂tḗr, bʰréh₂tēr, gʷeneh₂, h₂ékʷeh₂, dn̥ǵʰwéh₂s, ǵʰn̥dwéh₂s`  
Plus two exploratory forms: `méǵh₂-s` and `mǵh₂-és`.

### 2.3 Old/Neo Wékʷos Pipelines
**Files:** `pipelines/old_wekwos.py`, `pipelines/neo_wekwos.py`  
**Current state:** Marked `PROVISIONAL`. Rule lists were written but not tested against any expected outputs.  
**Action:** Define expected outputs for a small test set, run, debug. Neo-Wékʷos chains downstream of Old-Wékʷos via `_run_chained()` in `pipeline.py`.

### 2.4 Daughter Language Pipelines
**File:** `pipelines/daughters.py`  
**Current state:** Stubs only. `NOT_IMPLEMENTED = True`. Three daughters (A, B, C) defined in `docs/daughters.md` with phonological histories.  
**Action:** Deferred until daughter phonology is fully settled. Not a transformer priority now.

### 2.5 `pyproject.toml`
Not written. Currently the package runs only via `python3 -m pie_transformer` from within `tools/pie_transformer/`. Adding a `pyproject.toml` would allow `pip install -e .` for system-wide use. Low priority but easy.

### 2.6 Minor CLI Issues
- `--no-clear` flag was added to `form` command only; `batch` command does not have it (less relevant there, but worth noting)
- `--mode` flag in `form` command is parsed but currently ignored — both orthographic and IPA are always shown in terminal output. Either enforce `--mode` to select one, or drop the flag and always show both. Decision needed.

---

## 3. Design Decisions Made This Session Not Yet in Repo Docs

These were implemented in code but not reflected in `docs/phonological-history.md`, `docs/comparanda.md`, or `docs/notation.md`. They need to be added before those files drift further out of sync.

### 3.1 Two-Rule Boukólos Split
**Where to document:** `docs/phonological-history.md`, `docs/comparanda.md`

Two distinct rules now in the pipeline:

**Rule 1 — PIE-internal delabialization** (`pipelines/ghandwa.py`: `_PIE_DELAB`):  
`Kʷ → K / {u, ū, w} _` AND `Kʷ → K / _ {u, ū, w}`  
Bidirectional. Narrow environment. Pre-stage, fires once. Does not recur.

**Rule 2 — Ghandwa Boukólos** (`pipelines/ghandwa.py`: `_BOUKÓLOS`):  
`Kʷ → K / _ {C, w, u, ū}`  
Forward-only. Broader (includes any following consonant). Fires as a standing rule post-S1 and post-S2 only — not at pre-stage. Catches environments created by laryngeal loss and syllabic vocalization.

Rationale: Rule 1 cleans up PIE input; Rule 2 is a Ghandwa innovation that applies to derived environments. Syllabic resonants do not trigger Rule 2. The two rules were confirmed against lexicon spot-checks (`*h₁ln̥gʷʰús` → Rule 1; `*h₃ékʷs`, `*gʷríHw` → Rule 2).

### 3.2 TT→ss Restricted to Dental+Dental Only
**Where to document:** `docs/phonological-history.md`

The rule T{T,s}→ss (dental before dental-or-s → geminate ss) was restricted to **dental+dental only** (`TT→ss`). The dental+s case is NOT handled by this rule. Instead:
- `*ds` → devoicing rule → `ts` (preserved, not reduced to ss)
- Ghandwa does not reduce `ts` → `ss` (unlike Latin)

### 3.3 Dental Devoicing Rule Fixed
**Where to document:** `docs/phonological-history.md`

The "voiced obstruent → voiceless before t or s" rule was missing dentals (`d`, `dʰ`). Fixed: `d → t`, `dʰ → t` before `t` or `s`. Confirmed against `*gʰáyds` → `ɣájts`.

### 3.4 Normalize: Palatals vs. Accents
**Where to document:** `docs/notation.md`

`normalize.py`'s `_extract_accent()` now distinguishes:
- U+0301 (combining acute) on a **vowel** or **syllabic resonant** (U+0325) → lexical pitch accent; stripped and recorded as `accent_char_pos`
- U+0301 on a **consonant** (e.g. `ǵ`, `ḱ`) → palatalization diacritic; kept, not treated as accent

This means palatal notation (`ǵʰ`, `ḱ`) survives normalization intact and is handled by the centumization pipeline rule.

### 3.5 Ghandwa Orthographic Conventions
**Where to document:** `docs/notation.md`

Orthographic output (`render.py` `_ghandwa_surface()`):

| Token (IPA) | Orthography |
|---|---|
| `kʷ` | `kv` |
| `gʷ` | `gv` |
| `ɣʷ` | `ɣv` |
| `j` | `i` |
| `w` | `v` |
| all others | pass through |

IPA output uses token stream directly (tokens are already IPA), wrapped in `/…/`.  
No brackets or italics on either output mode.  
Surviving `ˀ` is a diagnostic tracer indicating a laryngeal that wasn't consumed — indicates a rule gap, not a real surface segment.

---

## 4. tools/README.md Needs Updating

Currently describes only `pie-2-ghandwa.jsx`. Should add a section for `pie_transformer/` covering:
- How to run (`python3 -m pie_transformer form "*wĺ̥kʷos" --pipeline ghandwa`)
- `--trace changed` flag
- `--no-clear` flag
- Pipeline names: `ghandwa`, `old-wekwos`, `neo-wekwos`
- Authority status (replacing JSX as authoritative transformer)
- Known gaps (IPA syllabifier, Wékʷos pipelines provisional, daughters not implemented)

---

## 5. Pre-Existing Lexicon Debt (Not This Session)

Listed for completeness; none of these were touched this session.

| Item | Scope | File |
|---|---|---|
| `lemma_1_pre_root` missing | ~174 non-stub entries | `vocab/lexicon.tsv` |
| `pos_subtype` unpopulated | all entries | `vocab/lexicon.tsv` |
| `_ety`/`_inp` backfill | ~500+ entries | `vocab/lexicon.tsv` |
| Mixed-normalization lemmas | *akmṓ*, *iṓr*, *sēmṓ* | `vocab/lexicon.tsv` |
| `svézōr` missing `nom_stem_class` | 1 entry | `vocab/lexicon.tsv` |
| 7 adopted verbs not in TSV | *dédōti*, *ɣvénti*, *βā́ti*, *gvéteti*, *ðéɣveti*, *ðoɣvéieti*, *kléveti* | `grammar/verb-eval-template.md` → TSV |
| 20+ TSV verbs lack paradigm work | — | `grammar/verbs-worksheet.md` |

---

## 6. Recommended Next Session Order

1. Fill in test suite expected outputs (§2.2) — validates current rule set before further changes
2. Document design decisions in repo files (§3) — before they're forgotten
3. Update `tools/README.md` (§4)
4. IPA syllabifier (§2.1) — use the handoff doc
5. Wékʷos pipeline verification (§2.3)
6. Lexicon batch run — extract pre_roots, run transformer, compare against `gh_lemma_1_orth`

---

# Ghandwa Tools

---
last_updated: 2026-05-15T00:00-04:00
changelog:
  - 2026-04-13T00:00-04:00 | 66 lines | Initial creation. Documents pie-2-ghandwa.jsx: authority status, headless execution recipe, known gaps. Content absorbed from project instructions §6.
  - 2026-05-15T00:00-04:00 | — | Prepended project handoff. Added pie_transformer/ internals doc (ARCHITECTURE.md). Updated last_updated.
---

## `pie-2-ghandwa.jsx`

PIE-to-Ghandwa phonological transformer. React JSX, but the core logic is plain JavaScript and can be run headless for batch verification.

### Authority

The transformer is **authoritative for surface forms**. Hand-derived Ghandwa forms must be verified against it. Interactions between Osthoff's Law, laryngeal coloring, and devoicing rules produce non-obvious outputs that are easy to miss by hand — e.g.:

- \*nṓman → *noman* (Osthoff shortens ō before mn̥)
- \*gʷʰ devoices to *kʷ* before *s*
- \*pípoti → *píboti* via h₃-triggered voicing adjacent to voiceless stop

When a hand-derived form disagrees with the transformer, the transformer is right unless a specific bug is identified and documented below.

### File structure

| Lines | Contents |
|---|---|
| 1–537 | Tokenizer, rule definitions, rule application machinery |
| 538–738 | `transformSingle(raw)` — the transformer entry point |
| 739–end | React component (`App`) — UI wrapper |

### Headless execution

The React component is a UI wrapper around pure-JS logic. To run the transformer from a Node.js CLI:

1. Extract lines 1–738 (everything before the React `App` component).
2. Strip the `import { useState } from "react";` line at the top.
3. Append a small CLI runner that reads input and calls `transformSingle`:

```javascript
const input = process.argv[2];
const result = transformSingle(input);
console.log(JSON.stringify(result, null, 2));
```

`transformSingle(input)` returns an object with:

- `.final` — the surface form after all rules have applied.
- `.steps` — an array of `{rule, before, after}` entries giving the rule-by-rule derivation.

Use `.steps` when a derivation disagrees with expectation, to identify which rule produced the surprise.

### Known gaps

**Glide respelling fires unconditionally.** The `y → j` rule (corresponding to §5.5 of `phonological-history.md`) does not distinguish diphthong contexts. Correct behavior:

- Pre-consonantal \*ey (diphthong) → transliteration ⟨ei⟩, IPA /ej/
- Pre-vocalic \*ey (glide before vowel) → transliteration ⟨i⟩, IPA /j/

Current transformer output may show ⟨j⟩ in positions where ⟨i⟩ is correct. Post-process or hand-correct as needed.

**h₃ voicing adjacent to voiceless stops** is implemented but edge cases exist. Verify outputs involving h₃ + stop clusters against worked examples in `phonological-history.md` §10.

### Related files

- `docs/phonological-history.md` — the ordered rule inventory the transformer implements.
- `docs/comparanda.md` — rule-by-rule tracking against Ringe 2017, De Vaan, Swanenvleugel.

---

## `pie-2-crotonian.jsx` *(planned — not yet implemented)*

**Status:** Deferred. Dependencies not yet met.

**Purpose:** PIE-to-Crotonian phonological transformer, parallel in architecture to `pie-2-ghandwa.jsx`. Takes a PIE preform as input, applies the Garnier & Sagot (2017) Crotonian rule inventory in chronological order, and outputs a Crotonian surface form. A second adaptation layer then maps that form to its shape as a loanword in Ghandwa.

**Use case:** Generating Crotonian-sourced borrowings for the Ghandwa lexicon. Entries derived via this transformer would carry `provenance` = `Crotonian` in the TSV. Doublet pairs — inherited Ghandwa form vs. Crotonian loanword from the same PIE root — are the primary output.

**Rule inventory source:** Garnier, Romain & Benoît Sagot. 2017. "A shared substrate between Greek and Italic." *Indogermanische Forschungen* 122(1): 29–60. Table 1 (p. 57), 12 chronologically ordered rules. Article is in `references/garnier-2017/`. Garnier & Sagot implemented the same rule set computationally; their test cases (~100 Greek, ~20 Latin/Proto-Romance etymologies) serve as verification suite.

**Dependencies before implementation:**
1. Verb system settled (Ghandwa-internal infrastructure must be stable first)
2. Crotonian phone inventory decided — specifically the fortis/lenis distinction (Garnier's cover symbols \*P, \*B, \*T need concrete phonetic values) and the realization of the Verner-like alternation
3. Ghandwa borrowing adaptation layer specified — how Crotonian phones map to Ghandwa phones on contact (e.g. Crotonian fortis \*P → Ghandwa plain voiceless stop; Crotonian \*ur from syllabic resonants vs. Ghandwa \*ar)

**Known issue to resolve:** Rule 11 asymmetry — \*#pr- → \*#br- (voicing) vs. \*#tr- → \*#Tr- (fortition) is typologically unexplained by Garnier. Implement \*#tr- → \*#Tr- as low-confidence; flag outputs using it.

**See also:** `docs/alt-phonologies.md` §6 for the Crotonian rule inventory summary and divergence table relative to Ghandwa.

---

## `pie-2-crotonian.jsx` *(planned — not yet implemented)*

**Status:** Deferred. Dependencies not yet met.

**Purpose:** PIE-to-Crotonian phonological transformer, parallel in architecture to `pie-2-ghandwa.jsx`. Takes a PIE preform as input, applies the Garnier & Sagot (2017) Crotonian rule inventory in chronological order, and outputs a Crotonian surface form. A second adaptation layer then maps that form to its shape as a loanword in Ghandwa.

**Use case:** Generating Crotonian-sourced borrowings for the Ghandwa lexicon. Entries derived via this transformer would carry `provenance` = `Crotonian` in the TSV. Doublet pairs — inherited Ghandwa form vs. Crotonian loanword from the same PIE root — are the primary output.

**Rule inventory source:** Garnier, Romain & Benoît Sagot. 2017. "A shared substrate between Greek and Italic." *Indogermanische Forschungen* 122(1): 29–60. Table 1 (p. 57), 12 chronologically ordered rules. Article is in `references/garnier-2017/`. Garnier & Sagot implemented the same rule set computationally; their test cases (~100 Greek, ~20 Latin/Proto-Romance etymologies) serve as verification suite.

**Dependencies before implementation:**
1. Verb system settled (Ghandwa-internal infrastructure must be stable first)
2. Crotonian phone inventory decided — specifically the fortis/lenis distinction (Garnier's cover symbols \*P, \*B, \*T need concrete phonetic values) and the realization of the Verner-like alternation
3. Ghandwa borrowing adaptation layer specified — how Crotonian phones map to Ghandwa phones on contact (e.g. Crotonian fortis \*P → Ghandwa plain voiceless stop; Crotonian \*ur from syllabic resonants vs. Ghandwa \*ar)

**Known issue to resolve:** Rule 11 asymmetry — \*#pr- → \*#br- (voicing) vs. \*#tr- → \*#Tr- (fortition) is typologically unexplained by Garnier. Implement \*#tr- → \*#Tr- as low-confidence; flag outputs using it.

**See also:** `docs/alt-phonologies.md` §6 for the Crotonian rule inventory summary and divergence table relative to Ghandwa.
