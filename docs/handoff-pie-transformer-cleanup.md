# PIE Transformer Cleanup — Phased Handoff

**Date:** 2026-05-19
**Scope:** `tools/pie_transformer/`
**Status:** Ready to execute. No edits made yet.
**Preceding session:** Code review of pipeline consistency and internal logic.

---

## 1. Context

The PIE transformer (Python package at `tools/pie_transformer/`, superseded the JSX file in 2026-05-15) has accumulated three classes of debt:

1. **A stale duplicate Daughter A implementation** is the one currently being called. The newer `daughter_a.py` is dead code.
2. **Seven helper functions and constants are duplicated across pipeline files**, with subtly different signatures.
3. **Accent-index tracking has at least five hand-rolled patterns in use**, some equivalent, some with off-by-one boundary differences that aren't covered by tests.

This handoff splits the work into four phases. Phases 1 and 2 are mechanical and can ship together. Phase 3 is a spec deliverable. Phase 4 is cosmetic and can be done piecemeal.

---

## 2. Decisions already made (do not relitigate)

| # | Decision | Rationale |
|---|---|---|
| 1 | `pipelines/daughter_a.py` is canonical. Delete `pipelines/daughters.py`. | Daughter A new model: LCG Stage 1 shared + per-daughter Stage 2; Stage 3 deferred until phonology settles. Matches `daughter_b.py` / `daughter_c.py`. |
| 2 | Accent-on-deleted-token policy: the rule that consumes the accented token specifies where the accent now lives. | Generalization of existing `_syl_res_vocalize` behavior (accented `r̥` → vocalizes → accent moves to new `a`). |
| 3 | Consolidate shared helpers into a new `pipelines/_common.py`. | Scopes pipeline-specific helpers separately from the rule engine (`rule.py`) and token inventory (`tokens.py`). |
| 4 | Accent-tracking refactor is deferred to a future session. This session preserves accent code verbatim. | Risk-bounded scope. Accent refactor requires test coverage to land first. |
| 5 | Rule IDs use `<prefix>.<stage>.<position>` numerical doc-mirror convention. | IDs anchor runner rules to their source documents. Daughter pipelines and Neo-Wékʷos already use this. Ghandwa and Proto-Anatolian migrate. |

---

## 3. Open decisions (resolve at start of Phase 1)

**D1. Daughter A Stage 3A tests.** `pipelines/daughters.py` had a Stage 3A (compensatory lengthening, coronal assimilation, geminate simplification, late xʷ-delabialization). `pipelines/daughter_a.py` does not — Stage 3A is explicitly deferred per the docstring. The current test suite has tests that exercise Stage 3A behavior:

- `TestDaughterA::test_compensatory_lengthening_across_boundary`
- `TestDaughterA::test_cluster_spirant_ks` (asserts `'ē'` in output — only Stage 3A produces long vowels)

Three options:
- **(a)** Delete the tests outright.
- **(b)** Move them to a clearly-marked dormant section (commented out or skipped with `@unittest.skip`) for when Stage 3A is specified.
- **(c)** Leave them failing as a visible TODO.

Recommendation: **(b)** with a comment pointing at `docs/daughters.md §3.1, 3A`. Preserves the work; doesn't block CI; surfaces the gap.

---

## 4. Phase 1 — Fix Daughter A breakage

**Risk:** Low (mechanical).
**Verification:** Full test suite passes after.

### 4.1 File operations
- Delete `tools/pie_transformer/pipelines/daughters.py`.
- Delete `tools/pie_transformer/pipelines/README.md`. (It is a byte-for-byte copy of `daughter_c.py`. Verify with `diff` before deleting. If a real README is wanted later, write a new one separately.)

### 4.2 Routing fix
In `tools/pie_transformer/pipeline.py`:

```python
# Line 53–54, current:
if name == 'ghandwa-daughter-a':
    from .pipelines.daughters import RULES_A
    return RULES_A

# Change to:
if name == 'ghandwa-daughter-a':
    from .pipelines.daughter_a import RULES_A
    return RULES_A
```

### 4.3 Test updates
In `tools/pie_transformer/tests/test_pipelines.py`:

- `TestNotImplemented::test_daughter_b` and `test_daughter_c`: B and C are now implemented. Either delete these tests or rewrite them to assert `status == 'ok'` for a known input.
- `TestDaughterA`: Per D1 above, resolve the Stage 3A tests.
- Verify the remaining Daughter A tests align with `daughter_a.py` rule list (LCG + 2A.1 stress, 2A.2 devoicing, 2A.3 z→s, 2A.4 delab, 2A.5 cluster-spirant). Note that the new `daughter_a.py` orders **stress first**, where `daughters.py` ordered it last — any test inspecting `accent_index` at an intermediate state will need updating.

### 4.4 Verification
```bash
cd tools && python3 -m unittest pie_transformer.tests.test_pipelines
```
All tests pass. No `FAIL` or `ERROR`.

### 4.5 Acceptance criteria
- `daughters.py` and `pipelines/README.md` removed.
- `pipeline.py:53` imports from `daughter_a`.
- Test suite green.
- `python3 -m pie_transformer form "*wĺ̥kʷos" --all` shows the same eight pipelines and Daughter A output now reflects LCG-then-Stage-2A (specifically: LCG rules fire before Daughter A devoicing).

---

## 5. Phase 2 — Extract `pipelines/_common.py`

**Risk:** Low-to-moderate (mechanical refactor, but touches every pipeline file).
**Precondition:** Phase 1 complete and green.
**Verification:** Full test suite passes; `--all` output is byte-identical to pre-refactor on a small smoke-test corpus.

### 5.1 Create `tools/pie_transformer/pipelines/_common.py`

Contents to move, with their canonical source noted:

| Symbol | Source | Notes |
|---|---|---|
| `make_rule(id_, name, stage, apply_fn, requires=None)` | Any of the 9 copies — they are identical except `daughters.py` which is deleted in Phase 1. | Replaces local `_rule` in all pipelines. |
| `next_seg(toks, i) -> tuple[str \| None, int \| None]` | `daughter_c.py::_next_seg` | Tuple form is strictly more general; replaces the 5 single-return variants. Callers needing only the token discard the index. |
| `prev_seg(toks, i) -> tuple[str \| None, int \| None]` | `daughter_c.py::_prev_seg` | Same. |
| `is_word_initial(toks, i)` | `daughter_c.py` | Currently daughter-C only; useful for B and wékʷos. |
| `is_word_final(toks, i)` | `daughter_c.py` | Same. |
| `laryngeal_color(h, v) -> str` | `ghandwa.py::_laryngeal_color` (byte-identical to `old_wekwos.py` and `proto_seldanic.py` copies) | PIE flavor (`h₂`/`h₃` color `e`). Anatolian's `χ`/`χʷ` version stays in `proto_anatolian.py` — it's a different stage. |
| `centumize_rule(prefix)` factory | `ghandwa.py::_CENTUMIZE`'s body | Returns a `Rule` with `id=f'{prefix}.centum'`. Used by `ghandwa.py`, `old_wekwos.py`, `proto_seldanic.py`. |
| `labiovelarize(toks, ctx)` | `ghandwa.py::_labiovelarize` (byte-identical to `old_wekwos.py` copy) | Preserves the accent-tracking loop verbatim. Do NOT refactor the accent code in this phase. |
| `UW: frozenset[str]` | New constant `frozenset({'u', 'ū', 'w'})` | Replaces 3 inline definitions. |

### 5.2 Move `_syllabify` from `render.py` to `_common.py`

Currently `daughter_b.py::_labiovelar_dissim` imports `_syllabify` from `..render`. This is wrong-direction dependency (a rule reaching into the renderer).

- Move `_syllabify`, `_valid_onset`, `_onset_split`, `_is_ipa_vowel`, `_base_form`, `_has_accent` to `_common.py` (or a new `pipelines/syllabify.py` if you prefer; both work).
- `render.py` imports them from there.
- `daughter_b.py` imports them from there.

`_is_ipa_vowel` and `_base_form` currently do local imports inside the function body (`from .tokens import VOWELS`). Those should become top-level imports once moved.

### 5.3 Update each pipeline file
For each of: `ghandwa.py`, `old_wekwos.py`, `neo_wekwos.py`, `proto_anatolian.py`, `proto_seldanic.py`, `late_common_ghandwa.py`, `daughter_a.py`, `daughter_b.py`, `daughter_c.py`:

- Replace local `_rule` with import of `make_rule` from `._common`.
- Replace local `_next_phoneme` / `_next_segment` / `_next_seg` / `_prev_phoneme` / `_prev_seg` with the tuple-returning forms from `._common`. Adjust callers that only used the token to unpack `tok, _ = next_seg(...)`.
- Replace local `_laryngeal_color` (where applicable) with the import.
- Replace inline `('-', '.')` and `_BOUNDARIES` / `_BOUNDARY` with `tokens.BOUNDARIES`.
- Replace inline `{'u', 'ū', 'w'}` with `_common.UW`.

### 5.4 Clean up dead bindings
- `ghandwa.py::_BOUKÓLOS` (line 148) is defined but never placed in `RULES`. The two standing-rule entries reference the underlying function `_boukólos` directly. Either delete `_BOUKÓLOS` or change `_STAND_BOK_1` and `_STAND_BOK_2` to be built from it. Either works; pick one for consistency.

### 5.5 Daughter C local consonant set
`daughter_c.py::_CONSONANTS_C` is a hardcoded local list. Replace with a derivation from `tokens.py` category sets so it doesn't drift when new tokens are added. Suggested:

```python
_CONSONANTS_C = (frozenset(['p','b','t','d','k','g'])
                 | LABIOVELAR_STOPS  # define in tokens.py
                 | LIQUIDS | NASALS | GLIDES
                 | VOICELESS_FRICATIVES | UVULAR_FRICATIVES
                 | frozenset(['β','ð','ɣ','ɣʷ','z','ʁ']))
```

Verify the resulting set is identical to the current hardcoded list before committing.

### 5.6 Verification
After all moves:
```bash
cd tools && python3 -m unittest pie_transformer.tests.test_pipelines
python3 -m pie_transformer form "*wĺ̥kʷos" --all
python3 -m pie_transformer form "*ph₂tḗr" --all
python3 -m pie_transformer form "*ǵʰoysós" --all
python3 -m pie_transformer form "*h₁ésti" --all
python3 -m pie_transformer form "*nṓmn̥" --all
```

Output must be byte-identical to a pre-refactor snapshot. Capture the snapshot before starting Phase 2.

### 5.7 Acceptance criteria
- `_common.py` exists with the listed symbols.
- No pipeline file defines a local `_rule`, boundary set, `_next_*`, `_prev_*`, `_laryngeal_color`, or `UW`/`_adj_uw`.
- `_syllabify` lives in `_common.py` (or `syllabify.py`); `render.py` and `daughter_b.py` import from there.
- Test suite green.
- `--all` smoke-test output unchanged on the five forms above.

---

## 6. Phase 3 — Accent-tracking spec (deferred-session prerequisite)

**Risk:** None (documentation only).
**Deliverable:** `tools/pie_transformer/docs/handoff-accent-tracking-v2.md`.

**Note:** `outputs/handoff-accent-tracking.md` already exists per project memory. This is its successor. Decide whether to supersede or append.

### 6.1 Contents the doc must cover

**§1. Catalog of current patterns.** Enumerate the five hand-rolled patterns observed across the codebase with file:function pointers:

- Pattern A: `insert_at = len(out)` + case-split (`==` move, `>` shift). Source: `ghandwa.py::_syl_res_vocalize`.
- Pattern B: Same as A but check ordered before extend. Source: `old_wekwos.py::_syl_res_vocalize`.
- Pattern C: `> len(out)` after pop+append. Source: `ghandwa.py::_h_vhv`, `_h_vh`, `_h_adj_v`.
- Pattern D: `>= i` after `i += 1`. Source: `old_wekwos.py::_h_vh`.
- Pattern E: `deletions_before_accent` counter, decrement at loop end. Source: `daughter_c.py` (five rules).

Identify which are equivalent and which are not. Specifically: confirm whether Pattern C and Pattern D produce the same accent index for accent-on-vowel-before-laryngeal inputs.

**§2. The model.** The rule that consumes the accented token decides where the accent goes. Generalize from the syllabic-resonant case:

- `r̥` carries accent → vocalizes → accent moves to the new `a`. ✓ implemented.
- `H` carries accent (rare; usually H doesn't bear accent in PIE reconstruction, but stipulate the policy): on VHV→V̄, accent moves to the surviving long vowel.
- Accented vowel deleted via VzC→V̄C: accent moves to the preceding lengthened vowel.

Rules whose changes don't touch the accented token simply shift the index for tokens inserted/deleted before it.

**§3. Proposed API.**

```python
def shift_for_change(ctx: Context, position: int, delta: int) -> None:
    """Adjust ctx.accent_index for a net `delta` token-count change at `position`.
    Used by rules whose changes do not touch the accented token itself.
    `delta` can be positive (insertions) or negative (deletions).
    """
    if ctx.accent_index is None: return
    if position < ctx.accent_index:
        ctx.accent_index += delta

def relocate(ctx: Context, new_position: int) -> None:
    """Move the accent to `new_position`. Used by rules that consume the
    accented token and know where the accent should land phonologically.
    """
    if ctx.accent_index is None: return
    ctx.accent_index = new_position
```

Open question to resolve in spec: what if a rule deletes the accented token *without* a phonological landing site (e.g. a stray accented boundary marker)? Options: error out, drop to None, fall back to preceding vowel.

**§4. Test coverage required before refactor.** Before any rule's accent code is touched, the following tests must exist and pass:

- Accent on syllabic resonant → vocalizes → accent on new `a`. (`*wĺ̥kʷos`, `*ḱm̥tóm`)
- Accent on vowel before lost laryngeal → accent on lengthened vowel. (`*ph₂tḗr` if the accent ever sits there; construct synthetic if needed.)
- Accent on vowel deleted by compensatory-lengthening rule (Daughter C 3C.3) → accent on preceding vowel.
- Accent on first vowel of `kʷ + w → kʷ` labiovelar merge → unchanged.
- Cross-pipeline equivalence: `ghandwa._h_vh` and `old_wekwos._h_vh` on a form whose accent sits on the lengthened vowel should produce the same accent index. (Currently they may not.)

**§5. Refactor order.** When the future session executes this:
1. Add the API to `rule.py` or `_common.py`.
2. Land the test suite from §4.
3. Migrate rules one file at a time, leaving accent code byte-identical until all tests pass, then refactor to use the API. Each file is a green-to-green commit.

### 6.2 Acceptance criteria
- Doc file exists in `tools/pie_transformer/docs/`.
- Cross-referenced from `tools/pie_transformer/docs/ARCHITECTURE.md` in the "Known Gaps" section.
- No code changes in this phase.

---

## 7. Phase 4 — Rule ID migration to `<prefix>.<stage>.<position>`

**Risk:** Low (cosmetic; only affects trace dumps and any tests that match on `rule_id`).
**Can be done:** Piecemeal (one pipeline at a time) or in one pass.

### 7.1 Convention

`<prefix>.<stage>.<position>[<subletter>]`

- `<prefix>`: pipeline identifier. Existing: `gh`, `wk`, `nwk`, `pa`, `sel`, `lcg`, `da`, `db`, `dc`.
- `<stage>`: integer matching the stage number in the pipeline's source document (`docs/phonological-history.md` for Ghandwa, `docs/daughters.md` for daughters, etc.). Pre-stage rules use `0`.
- `<position>`: integer within stage, in execution order.
- `<subletter>`: optional lowercase letter for sub-rules (`a`, `b`, `c`).

### 7.2 Migration tables

**Already conforming, no changes:**
- `lcg.*` — `lcg.1.1a`, `lcg.1.1b`, `lcg.1.2`, `lcg.1.3`.
- `db.*` — `db.2.1` through `db.2.6`.
- `dc.*` — `dc.2.1` through `dc.3.7`.
- `da.*` (in new `daughter_a.py`) — `da.2.1` through `da.2.5`.
- `nwk.*` — `nwk.41`, `nwk.42`, etc. (Already numerical; consider re-formatting `nwk.41` → `nwk.4.1` for consistency. Optional.)

**Needs migration:**

`ghandwa.py` (`gh.*`):
| Current | Proposed | Source ref |
|---|---|---|
| `gh.centum` | `gh.0.1` | Pre-stage |
| `gh.lv_merge` | `gh.0.2` | Pre-stage |
| `gh.pie_delab` | `gh.0.3` | Pre-stage |
| `gh.tts` | `gh.1.1` | Stage 1 dentals |
| `gh.ssc` | `gh.1.2` | Stage 1 dentals |
| `gh.thorn` | `gh.1.3` | Stage 1 dentals |
| `gh.h_a` | `gh.1.4` | Stage 1 laryngeals (subletters if doc splits H-A/B1/B2…) |
| `gh.h_b1` | `gh.1.5` | etc. |
| `gh.h_b2` | `gh.1.6` | |
| `gh.h_b3` | `gh.1.7` | |
| `gh.h_b4` | `gh.1.8` | |
| `gh.h_b5` | `gh.1.9` | |
| `gh.h_survive` | `gh.1.10` | |
| `gh.voi_bts` | `gh.1.11` | Stage 1 consonants |
| `gh.osthoff` | `gh.1.12` | Stage 1 vowels |
| `gh.ew_ow` | `gh.1.13` | Stage 1 vowels |
| `gh.pretonic` | `gh.1.14` | Pretonic |
| `gh.stand_lv_1` | `gh.1.15` | Standing post-S1 |
| `gh.stand_bok_1` | `gh.1.16` | Standing post-S1 |
| `gh.syl_res` | `gh.2.1` | Stage 2 syllabics |
| `gh.juwankos` | `gh.2.2` | Stage 2 fricatives |
| `gh.aspirates` | `gh.2.3` | Stage 2 fricatives |
| `gh.s_voice` | `gh.2.4` | Stage 2 fricatives |
| `gh.y_j` | `gh.2.5` | Stage 2 glides |
| `gh.stand_lv_2` | `gh.2.6` | Standing post-S2 |
| `gh.stand_bok_2` | `gh.2.7` | Standing post-S2 |

Verify against `docs/phonological-history.md` section numbers before committing — if the doc itself uses different numbering, mirror the doc, not this table.

`old_wekwos.py` (`wk.*`): analogous migration; verify against the source doc (currently no dedicated doc — rule order is from the JSX prototype). Numbering can start from §1 of `docs/comparanda.md` if a Wékʷos rule inventory exists there, or be assigned 0/1/2/… by execution order if not.

`proto_anatolian.py` (`pa.*`): the module docstring already numbers steps 1–10. Migrate to `pa.1.1`, `pa.2.1`, etc., where step-number = stage.

`proto_seldanic.py` (`sel.*`): module docstring references `docs/proto-seldanic-pipeline.md` for rule numbers 1–9. Migrate to `sel.1.1` through `sel.9.1` mirroring the doc.

### 7.3 Verification
- `grep -r "rule_id\s*==\s*['\"]" tools/pie_transformer/tests/` to find any tests that match rule IDs literally. Update those.
- Run `--all` and inspect trace output to confirm IDs are present and readable.
- Test suite green.

### 7.4 Acceptance criteria
- All rule IDs follow `<prefix>.<stage>.<position>[<sub>]`.
- IDs map cleanly to source-doc section numbers (verify the doc itself if needed).
- Tests pass.

---

## 8. Explicitly out of scope

- Accent-tracking refactor (Phase 3 specs it; future session executes).
- Resurrecting Daughter A Stage 3A (intentionally dropped per D1).
- Any behavior change to rules. Phases 1, 2, and 4 are pure refactor/cleanup; Phase 3 is doc.
- Touching `pie-2-ghandwa.jsx` (superseded, retained for reference only).

---

## 9. Suggested execution order if split across sessions

- **Session 1:** Phase 1 + Phase 2 + Phase 3. Phases 1 and 2 ship together as one commit set; Phase 3 is a separate doc commit. Estimated 2–3 hours.
- **Session 2:** Phase 4 in one pass, or piecemeal as time allows. Estimated 1–2 hours for the full migration.
- **Session 3+:** Accent-tracking refactor per Phase 3's spec. Estimated longer — test coverage first, then per-file rule migration.

---

## 10. Reference: full duplication catalog (from the review)

For Phase 2 grep-targets:

- `_rule` constructor: defined in 9 files (`ghandwa.py`, `old_wekwos.py`, `neo_wekwos.py`, `proto_anatolian.py`, `proto_seldanic.py`, `late_common_ghandwa.py`, `daughter_a.py`, `daughter_b.py`, `daughter_c.py`).
- Boundary-skipping lookup: 5 variants across `daughters.py`, `late_common_ghandwa.py`, `daughter_b.py` (2), `daughter_c.py` (2), plus inline in `ghandwa.py::_voiced_before_ts`.
- Boundary-set constant: `tokens.BOUNDARIES` exists; redefined or inlined in 6 places.
- `_laryngeal_color`: byte-identical in `ghandwa.py`, `old_wekwos.py`, `proto_seldanic.py`.
- `_labiovelarize`: byte-identical in `ghandwa.py`, `old_wekwos.py`.
- Centumize lambda: near-identical in `ghandwa.py`, `old_wekwos.py`, `proto_seldanic.py`.
- `{u, ū, w}` set: 3 definitions plus inline literals.
- `_syllabify`: in `render.py`, imported (wrong direction) by `daughter_b.py`.

---

last_updated: 2026-05-19T23:50-04:00
changelog:
  - 2026-05-19T23:50-04:00 | initial | Phased handoff for PIE transformer cleanup. Phase 1 fixes Daughter A routing breakage and removes stale `daughters.py` + duplicate `pipelines/README.md`. Phase 2 extracts shared helpers to `pipelines/_common.py` and moves `_syllabify` out of `render.py`. Phase 3 specs the accent-tracking refactor as a future-session prerequisite. Phase 4 migrates rule IDs to `<prefix>.<stage>.<position>` doc-mirror convention. Decisions D1–D5 captured. One open decision flagged for Phase 1 (Daughter A Stage 3A test disposition).
