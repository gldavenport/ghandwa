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
**Status: COMPLETE as of 2026-05-15.**  
`render.py` → `_ghandwa_ipa()` now implements onset-maximization syllabifier with stress mark. See `docs/handoff-ipa-syllabifier.md` (marked implemented).

### 2.2 Provisional Test Suite Expected Outputs
**Status: COMPLETE as of 2026-05-15.**  
44 stable tests passing. All starter inputs verified and hardened to hard assertions. IPA test class added.

### 2.3 Old/Neo Wékʷos Pipelines
**Status: COMPLETE as of 2026-05-15.**  
6 stable test cases each, verified against expected outputs. Accent_index tracking fixed in `_syl_res_vocalize` and `_liquid_metathesis`. `#wlV/#mlV→#blV` rule added to Neo. "Substrate" stage label renamed to "Cluster Assimilation".

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

**Status: COMPLETE as of 2026-05-15.** All five design decisions documented in `docs/phonological-history.md`, `docs/comparanda.md`, and `docs/notation.md`.

---

## 4. tools/README.md Needs Updating

**Status: COMPLETE as of 2026-05-15.** `pie_transformer/` section added; JSX marked superseded; duplicate Crotonian removed.

---

## 5. Pre-Existing Lexicon Debt (Not This Session)

Listed for completeness; none of these were touched this session.

| Item | Scope | File |
|---|---|---|
| `lemma_1_pre_root` missing | ~174 non-stub entries | `vocab/lexicon-core.tsv` |
| `pos_subtype` unpopulated | all entries | `vocab/lexicon-core.tsv` |
| `_ety`/`_inp` backfill | ~500+ entries | `vocab/lexicon-core.tsv` |
| Mixed-normalization lemmas | *akmṓ*, *iṓr*, *sēmṓ* | `vocab/lexicon-core.tsv` |
| `svézōr` missing `nom_stem_class` | 1 entry | `vocab/lexicon-core.tsv` |
| 7 adopted verbs not in TSV | *dédōti*, *ɣvénti*, *βā́ti*, *gvéteti*, *ðéɣveti*, *ðoɣvéieti*, *kléveti* | `grammar/verb-eval-template.md` → TSV |
| 20+ TSV verbs lack paradigm work | — | `grammar/verbs-worksheet.md` |

---

## 6. Lexicon Restructuring (This Session)

`vocab/lexicon.tsv` split into two files:

- **`vocab/lexicon-core.tsv`** (26 columns) — lemma, POS, gloss, stem class, verb fields, entry_status, formation/historical type, source. Working file for hygiene passes in Numbers.
- **`vocab/lexicon-ref.tsv`** (29 columns) — cognates, notes, cross-references, semantic fields, register, lit/swadesh tags. Joined on `entry_id`.

Column renames applied: `gh_lemma_1_orth→lemma_1_gh_orth`, `gh_lemma_1_ipa→lemma_1_gh_ipa`, same for lemma_2; `lemma_1_pre_ety→lemma_1_pre_orth`, same for lemma_2/3.

Dropped columns (22): `gh_lemma_1_ipa_test`, `gh_lemma_2_ipa_test`, `sound_changes`, all `r0-*`/`r1-*`/`r2-*`.

---

# Ghandwa Tools

---
last_updated: 2026-05-15T00:00-04:00
changelog:
  - 2026-04-13T00:00-04:00 | 66 lines | Initial creation. Documents pie-2-ghandwa.jsx: authority status, headless execution recipe, known gaps. Content absorbed from project instructions §6.
  - 2026-05-15T00:00-04:00 | — | Prepended project handoff. Added pie_transformer/ internals doc (ARCHITECTURE.md). Updated last_updated.
  - 2026-05-15T00:00-04:00 | — | Added pie_transformer/ section. Marked pie-2-ghandwa.jsx superseded. Removed duplicate Crotonian entry. Added Phonological Adaptation Layer planned section. Updated handoff §§2-4 completion status.
---

## `pie_transformer/`

Python 3 CLI package. **Authoritative transformer** as of 2026-05-15, superseding `pie-2-ghandwa.jsx`.

Full internals documentation: `tools/pie_transformer/docs/ARCHITECTURE.md`.

### Running

From `tools/pie_transformer/` (the package must be run as a module from within `tools/`):

```bash
# Single form — Ghandwa pipeline
python3 -m pie_transformer form "*wĺ̥kʷos" --pipeline ghandwa

# Show derivation trace (changed steps only)
python3 -m pie_transformer form "*wĺ̥kʷos" --trace changed

# Full trace (all rule evaluations)
python3 -m pie_transformer form "*wĺ̥kʷos" --trace full

# Suppress screen clear (useful when piping or in a shell session)
python3 -m pie_transformer form "*wĺ̥kʷos" --no-clear

# Run all pipelines against a single form
python3 -m pie_transformer form "*wĺ̥kʷos" --all

# Batch mode — transformer-ready TSV in, results TSV out
python3 -m pie_transformer batch input.tsv --out results.tsv --report results.md

# Extract source forms from the human lexicon TSV
python3 -m pie_transformer extract-lexicon ../../vocab/lexicon-core.tsv --out transformer-input.tsv
```

### Pipeline names

| Name | Status |
|---|---|
| `ghandwa` | Stable. Primary pipeline. |
| `old-wekwos` | Provisional. Rule list written; 6 verified test cases. |
| `neo-wekwos` | Provisional. Chains downstream of `old-wekwos`; 6 verified test cases. |
| `daughter-a`, `daughter-b`, `daughter-c` | Not implemented. Returns `not_implemented`. |

### Authority

The transformer is **authoritative for surface forms**. Hand-derived Ghandwa forms must be verified against it when non-obvious rule interactions are in play. When a hand-derived form disagrees with the transformer output, the transformer is right unless a specific bug is identified and documented in `ARCHITECTURE.md § Known Gaps`.

Surviving `ˀ` in output is a diagnostic tracer, not a real surface segment — it indicates a laryngeal that was not consumed by any rule, signalling a rule gap.

### Known gaps

- **Wékʷos pipelines provisional.** Rule lists exist and have verified test cases, but the phonological history is not fully settled. Additional test cases should be added as the phonology is refined.
- **Daughter pipelines not implemented.**
- **`--mode` flag ignored** in `form` command. Both orthographic and IPA are always shown regardless of `--mode` value.
- **`pyproject.toml` not written.** Package must be run in-place via `python3 -m pie_transformer`. `pip install -e .` not available.

---

## `pie-2-ghandwa.jsx`

> **Superseded.** `pie_transformer/` is now authoritative. This file is retained for reference. Do not use it to generate or verify surface forms.

PIE-to-Ghandwa phonological transformer. React JSX, but the core logic is plain JavaScript and can be run headless for batch verification.

### Authority (historical)

~~The transformer is **authoritative for surface forms**.~~ As of 2026-05-15, `pie_transformer/` supersedes this file. Interactions between Osthoff's Law, laryngeal coloring, and devoicing rules produce non-obvious outputs that are easy to miss by hand — e.g.:

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

- `docs/grammar/ch3-development/phonological-history.md` — the ordered rule inventory the transformer implements.
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

## Phonological Adaptation Layer *(planned — not yet designed)*

**Status:** Deferred. Concept established; design not started.

**Purpose:** A generalizable pipeline for adapting loanwords from non-PIE-derived source forms into Ghandwa. Where the PIE transformer takes a reconstruction and applies diachronic rules, the adaptation layer takes a synchronic surface form in a source language and applies contact-era correspondence rules to produce the Ghandwa loanword shape.

**Architecture:** Same pipeline structure as existing transformers — a source-language normalizer, a correspondence rule list, and a render pass. The source-language normalizer accepts the source language's own notation rather than PIE. Each source language would be a separate pipeline (e.g. `crotonian-to-ghandwa`, `substrate-x-to-ghandwa`).

**Relationship to Crotonian transformer:** The planned `pie-2-crotonian.jsx` produces a Crotonian surface form from a PIE reconstruction. The adaptation layer is the second stage — Crotonian surface → Ghandwa loanword. Together they form a two-stage pipeline: PIE → Crotonian → Ghandwa. The adaptation layer generalizes this second stage to arbitrary source languages.

**Borrowing workflow without this tool:** Enter `lemma_1_gh_orth` and `lemma_1_gh_ipa` by hand; leave `lemma_1_pre_orth` blank; set `entry_formation_type` to borrowing/loanword. The transformer batch run skips entries with no `lemma_1_pre_orth`. For source forms that can be plausibly written in PIE notation without triggering destructive rules (no laryngeals, aspirates, palatals, or syllabic resonants), running through the standard PIE pipeline is also acceptable.

**Dependencies before design:**
1. Crotonian transformer implemented and verified
2. At least one source language's phonological inventory and Ghandwa correspondence rules specified
3. Borrowing layer notation convention decided (how to mark entry-point stage in the pipeline)
