# Accent-Tracking Refactor — Spec Handoff

**Date:** 2026-05-21
**Scope:** `tools/pie_transformer/` — accent-index tracking across all pipeline rules
**Status:** Spec only. No code changes in this document.
**Prerequisite for:** a future session that will add tests, then migrate rules one file at a time.
**Supersedes:** `outputs/handoff-accent-tracking.md` (never committed; this is the authoritative spec).

---

## 1. Catalog of current patterns

Five distinct hand-rolled accent-tracking patterns appear across the codebase.
File and function pointers are as of 2026-05-21 post-Phase-2 refactor.

---

### Pattern A — `insert_at` + case-split on `==` / `>`

**Source:** `pipelines/ghandwa.py :: _syl_res_vocalize`

```python
# Insert 'a' + resonant (replace syllabic with two tokens)
insert_at = len(out)
out.extend(['a', res])

if ctx.accent_index is not None:
    if ctx.accent_index == i:
        ctx.accent_index = insert_at  # accent was on this syllabic → moves to 'a'
    elif ctx.accent_index > i:
        ctx.accent_index += 1         # one extra token inserted before accent
```

**Semantics:** Correct for the simple two-arm case. Accent on the syllabic resonant itself gets relocated to the new 'a'. Accent after the resonant shifts right by 1 (because an extra token was inserted before it). Accent before the resonant is unaffected.

**Complication:** The same function has earlier glottal-consumption branches that apply *their own* partial accent adjustments before reaching the main block, making the overall function multi-stage and hard to audit. The `insert_at` variable is computed, then recomputed lower in the function, which adds noise.

---

### Pattern B — Same as A, but the `==` check fires before `extend`

**Source:** `pipelines/wekwos_old.py :: _syl_res_vocalize`

```python
if ctx.accent_index is not None:
    if ctx.accent_index == i:
        ctx.accent_index = len(out)   # accent was on syllabic → moves to 'a'
    elif ctx.accent_index > i:
        ctx.accent_index += 1         # extra token inserted
out.extend(['a', RES[tok]])
```

**Difference from A:** The check happens before `extend`, so `len(out)` at the time of the `==` arm equals `insert_at` in Pattern A (they compute the same value). Functionally identical to A for the simple case. Wékʷos-Old does not have the glottal-consumption branches, so Pattern B is simpler and easier to audit.

**Equivalence verdict:** A ≅ B for all practical PIE inputs. The numerical difference (check before vs. after extend) is immaterial because the `==` arm relocates to `len(out)` which is the same value either way.

---

### Pattern C — `> len(out)` after pop+append

**Source:** `pipelines/ghandwa.py :: _h_vhv`, `_h_vh`, `_h_adj_v`  
(Also `pipelines/proto_seldanic.py :: _h_vh`)

Representative — `_h_vh`:

```python
out.pop()
out.append(lengthen(prev))
# Replaced laryngeal with length on previous vowel: net -1
if ctx.accent_index is not None and ctx.accent_index > len(out):
    ctx.accent_index -= 1
i += 1
continue
```

**Semantics:** After the pop+append, `len(out)` equals the index of the lengthened vowel + 1 — equivalently, the position *the consumed laryngeal occupied* in the original token stream. The condition `accent_index > len(out)` fires if and only if the accent was on a token strictly *after* the laryngeal. Accent on the pre-laryngeal vowel (which remains in place as a long vowel) is unaffected.

**Edge case:** Accent on the laryngeal itself (`accent_index == original_H_position`). At the time of the check, `len(out) = original_H_position`. The condition `== len(out)` is false (condition is `>`), so the accent is not adjusted. The laryngeal is gone; `accent_index` now points to the token that follows the long vowel in the output. This is technically wrong but accent on a laryngeal is not a valid PIE input, so it is vacuous in practice.

---

### Pattern D — `>= i` after `i += 1`

**Source:** `pipelines/wekwos_old.py :: _h_vh`

```python
out.pop(); out.append(lengthen(prev)); i += 1
# H deleted: accent shifts left if it was beyond this position
if ctx.accent_index is not None and ctx.accent_index >= i:
    ctx.accent_index -= 1
continue
```

**Semantics:** `i` has been incremented past the laryngeal, so `i` at this point equals `original_H_position + 1`. The condition `accent_index >= i` fires if the accent was on a token at or after `original_H_position + 1`, i.e., strictly after the laryngeal. This is the same logical condition as Pattern C.

**Equivalence verdict: Pattern C ≡ Pattern D** for all practical inputs. Both shift the accent if and only if it was on a token strictly after the laryngeal. They produce the same `accent_index` output for all well-formed PIE inputs (where the accent is never on a laryngeal). The edge case (accent on the laryngeal) differs in implementation detail but is unreachable with real data.

**Implication for refactor:** `ghandwa._h_vhv`, `_h_vh`, `_h_adj_v` and `wekwos_old._h_vh` can all be migrated to the same `shift_for_change(ctx, position, delta=-1)` call without behavioral difference on any live input.

---

### Pattern E — `deletions_before_accent` counter, decremented at loop end

**Source:** `pipelines/daughter_c.py :: _liq_z_before_vowel`, `_vz_before_cons`, `_rlz_before_cons`, `_liquid_final_simplify`, and one rule in `_rhotacism` (vacuous — rhotacism is 1:1, no deletions)

Representative — `_liq_z_before_vowel`:

```python
out = list(toks)
i = 0
deletions_before_accent = 0
while i < len(out):
    t = out[i]
    if t == 'z':
        ...
        out.pop(i)
        if ctx.accent_index is not None and i < ctx.accent_index:
            deletions_before_accent += 1
        continue   # recheck same index after in-place deletion
    i += 1
if ctx.accent_index is not None:
    ctx.accent_index -= deletions_before_accent
```

**Semantics:** The rules mutate `out` in-place (using `list.pop`). The counter accumulates the number of deletions that occurred at positions *before* the accent. At the end, `accent_index` is adjusted once. This is correct because each deletion before the accent position shifts the accent left by 1, and the counter defers the adjustment until after the loop.

**Why it differs:** These rules operate on a mutable output list (pop-in-place), whereas Patterns A–D operate on a freshly built `out` list (append-only). The counter pattern is the natural fit for pop-in-place; the `len(out)` threshold pattern is the natural fit for append-only.

**Cross-pattern interaction:** Daughter C rules run *after* Ghandwa rules (Pattern A/C). The `accent_index` entering Daughter C's rules has already been updated by Pattern A/C, so there is no cross-pattern consistency issue — each pattern is self-consistent within its rule's scope.

---

## 2. The model

The invariant that all patterns are approximating:

> **The rule that consumes the accented token decides where the accent now lives. All other rules merely shift the index by the net token delta for any changes made before the accented position.**

This generalizes directly from the syllabic-resonant case, which is the best-implemented instance in the codebase:

| Input state | Rule action | Accent outcome |
|---|---|---|
| `r̥` carries accent | Vocalizes to `a` + `r` (net +1) | Accent moves to new `a` (explicit relocation) |
| `H` is consumed (VH→V̄) | H deleted, preceding vowel lengthened (net -1) | Accent shifts left by 1 if it was after H; unchanged if it was on the vowel before H |
| Token deleted, not accented | Deletion before accent (net -1 at that position) | Accent shifts left by 1 |
| Tokens inserted, not accented | Insertion before accent (net +1 at that position) | Accent shifts right by 1 |
| Accented token deleted with no phonological landing site | Not currently handled | **Open policy question** (see below) |

**Open policy question:** What if a rule deletes the accented token without a phonological landing site? Three options:

- **(a) Error out.** Status `error`; propagate to DerivationResult. Safest for catching bugs.
- **(b) Drop to `None`.** Accent lost; downstream rules see `None`. May cause silent failures.
- **(c) Fall back to preceding vowel.** Implicit relocation; may be phonologically wrong.

**Recommendation: (a), error out.** A well-formed PIE input should never have the accent on a token that gets deleted without compensation. If this fires, it indicates either a bad input or a rule logic bug. Surfacing it as an error is preferable to silently corrupting the accent index. Implement as a guard in `relocate()` when `new_position` is `None`.

---

## 3. Proposed API

Two functions to be added to `rule.py` (or `pipelines/_common.py`; `rule.py` is preferable since `Context` lives there).

```python
def shift_for_change(ctx: Context, position: int, delta: int) -> None:
    """Adjust ctx.accent_index for a net `delta` token-count change at `position`.

    Used by rules whose changes do NOT touch the accented token itself.
    `delta` is positive for net insertions, negative for net deletions.
    The adjustment fires if and only if `position < ctx.accent_index`
    (i.e., the change is strictly before the accent).

    Args:
        ctx:      Pipeline context. No-op if ctx.accent_index is None.
        position: The token index where the change occurred, measured in
                  the token stream BEFORE the change (for deletions) or
                  AFTER the change (for insertions). Convention: use the
                  index of the first token affected.
        delta:    Net token count change. -1 for a single deletion,
                  +1 for a single insertion, etc.
    """
    if ctx.accent_index is None:
        return
    if position < ctx.accent_index:
        ctx.accent_index += delta


def relocate(ctx: Context, new_position: int | None) -> None:
    """Move the accent to `new_position`.

    Used by rules that consume the accented token and know where the accent
    should land phonologically (e.g., syllabic resonant vocalizes, accent
    moves to the new 'a').

    Args:
        ctx:          Pipeline context. No-op if ctx.accent_index is None.
        new_position: The new token index in the output stream. If None,
                      the rule is asserting there is no phonological landing
                      site, which is an error condition (see §2).

    Raises:
        ValueError: If new_position is None (accent lost with no landing site).
    """
    if ctx.accent_index is None:
        return
    if new_position is None:
        raise ValueError(
            "relocate() called with new_position=None: accented token was "
            "consumed with no phonological landing site. Check rule logic."
        )
    ctx.accent_index = new_position
```

### Migration examples

**Replacing Pattern B** (`wekwos_old._syl_res_vocalize`, simple case):

```python
# Before
if ctx.accent_index is not None:
    if ctx.accent_index == i:
        ctx.accent_index = len(out)
    elif ctx.accent_index > i:
        ctx.accent_index += 1
out.extend(['a', RES[tok]])

# After
insert_at = len(out)
out.extend(['a', RES[tok]])
if ctx.accent_index == i:
    relocate(ctx, insert_at)
else:
    shift_for_change(ctx, insert_at, delta=+1)
```

**Replacing Pattern C** (`ghandwa._h_vh`):

```python
# Before
out.pop()
out.append(lengthen(prev))
if ctx.accent_index is not None and ctx.accent_index > len(out):
    ctx.accent_index -= 1
i += 1

# After
consumed_at = len(out)   # position of the consumed laryngeal in output coordinates
out.pop()
out.append(lengthen(prev))
shift_for_change(ctx, consumed_at, delta=-1)
i += 1
```

Note: `consumed_at = len(out)` must be computed *before* the pop, not after — the pop moves `len(out)` down by 1. The formula above captures the position of the H in output coordinates (= the position after the lengthened vowel).

**Replacing Pattern E** (`daughter_c._liq_z_before_vowel` and siblings):

```python
# Before
deletions_before_accent = 0
while i < len(out):
    ...
    out.pop(i)
    if ctx.accent_index is not None and i < ctx.accent_index:
        deletions_before_accent += 1
    continue
if ctx.accent_index is not None:
    ctx.accent_index -= deletions_before_accent

# After
while i < len(out):
    ...
    shift_for_change(ctx, i, delta=-1)
    out.pop(i)
    continue
```

The deferred-counter is replaced by an immediate `shift_for_change` call before each deletion. Both produce the same result; the immediate form is simpler and consistent with the API.

---

## 4. Test coverage required before any code changes

The following tests must exist and pass before any rule's accent code is modified. All tests should be added to `pie_transformer/tests/test_pipelines.py` in a `TestAccentTracking` class.

**4.1 Syllabic resonant vocalization (Pattern A/B)**
- Accent on syllabic resonant → vocalizes → accent on new 'a'.
  - `*wĺ̥kʷos`: `accent_index` after `_syl_res` rule should point to the 'a' in `[..., 'a', 'l', ...]`.
  - `*ḱm̥tóm`: accent on `m̥` → moves to 'a' in `[..., 'a', 'm', ...]`.
- Accent on vowel after syllabic resonant → accent index shifts right by 1.
  - `*ǵn̥h₁tós`: accent on `ó`; after `n̥→an`, accent_index increments by 1.

**4.2 Laryngeal loss with lengthening (Pattern C/D)**
- Accent on vowel before lost laryngeal → accent index unchanged (long vowel inherits it).
  - `*ph₂tḗr`: accent on `ē`; H-B5 inserts `a` before `t`, not a laryngeal loss affecting this accent; verify `accent_index` after full pipeline.
  - Synthetic: `*séh₂l` — accent on `e` at index 1, H-B2 fires: VH→V̄, H deleted. Accent stays at 1 (now pointing to `ē`).
- Accent on vowel after lost laryngeal → accent index shifts left by 1.
  - Synthetic: `*neh₂wós` — accent on `o`; after H-B2, `accent_index` decrements by 1.

**4.3 Cross-pipeline equivalence: `ghandwa._h_vh` vs. `wekwos_old._h_vh` (C ≡ D)**
- Same form through both pipelines; assert `final_accent_index` is identical.
  - Use `*bʰréh₂tēr`: accent on `e` which colors to `a` then lengthens. Run through both `ghandwa` and a hypothetical isolated `wekwos_old._h_vh` rule; confirm same `accent_index`.
  - This test documents the equivalence proved in §1; it should remain green after refactor.

**4.4 Daughter C deletion patterns (Pattern E)**
- Accent on vowel deleted by `VzC→V̄C` (3C.3) → accent on preceding lengthened vowel.
  - Construct a form where the *accented* short vowel feeds `VzC→V̄C`. After the rule, the accent should be on the new long vowel at the same position.
  - Example: form with `*óz` + consonant where `ó` is accented → `ōC`, accent still at the position of `ō`.
- Accent after a deletion that precedes it → accent shifts left by 1.
  - Daughter C form where `z` is deleted before the accent; verify `accent_index` decrements.

**4.5 Labiovelar merge (accent before merge position)**
- `*ǵn̥h₁tós` with `kw` sequence not involving accent: verify merge does not corrupt accent.
- `*wĺ̥kʷos`: `kʷ` is already merged by tokenizer; verify `labiovelarize` is a no-op and accent is correct.

---

## 5. Refactor order

Execute in a future session, after all tests in §4 are written and passing.

1. **Add API to `rule.py`.** Add `shift_for_change` and `relocate` as module-level functions. No rule code touched yet. Run test suite: should still be green.

2. **Land §4 test suite.** Write `TestAccentTracking` in `test_pipelines.py`. All tests must pass before any rule migration.

3. **Migrate rules one file at a time, green-to-green.**
   - Recommended order: `wekwos_old.py` (Pattern B+D, simpler glottal handling) → `ghandwa.py` (Pattern A+C, complex glottal branches) → `proto_seldanic.py` (Pattern C) → `daughter_c.py` (Pattern E, five rules).
   - For each file: replace accent code in each rule function with API calls, run full suite, commit.
   - **Do not refactor accent code in a rule if its test (§4) is missing or failing.** Skipped tests (Stage 3A) are acceptable; missing tests are not.

4. **Leave `daughter_a.py` and `daughter_b.py` last.** Daughter A's `_stress_initial` sets `accent_index` unconditionally to the first vowel — this is a `relocate` call, not a `shift_for_change`. Daughter B has no internal accent arithmetic beyond what it inherits from LCG.

5. **Do not touch `late_common_ghandwa.py` accent code.** The only rule with accent dependency is `_final_accent_retract`, which directly reads and writes `vowel_positions` and `ctx.accent_index` as an explicit phonological operation. It is not bookkeeping — it's the rule's output. Leave as-is.

---

## 6. Known non-issues (do not refactor)

- `_tts` (`gh.tts`): two dentals replaced by two `s` tokens; net count unchanged; accent untouched. ✓
- `_ssc_simplify` (`gh.ssc`): one `s` deleted; uses `ctx.accent_index > i` shift. This is Pattern-C-adjacent but correct. Migrate opportunistically if Pattern C migration is in progress.
- `_thorn`: two tokens swapped; net count unchanged; accent untouched. ✓
- `_h_initial_c` (both files): initial H deleted; uses `ctx.accent_index > 0` shift (Pattern C). Migrate with `shift_for_change(ctx, 0, -1)`.
- `wekwos_neo.py`: no accent arithmetic in rules (barytonesis is a no-op on tokens; other rules are pure token transforms). No migration needed.
- `proto_anatolian.py`: `_syl_res_repair` (kʷR̥→kuR, net +1) and `_h1_loss` use hand-rolled `>= i` pattern (Pattern D variant). Include in the D-to-API migration pass.

---

last_updated: 2026-05-21T00:00-04:00
changelog:
  - 2026-05-21 | initial | Accent-tracking refactor spec. Catalogs five patterns (A–E) with file:function pointers; proves C ≡ D for all practical PIE inputs; specifies shift_for_change/relocate API; lists required test coverage; gives per-file migration order. Supersedes uncommitted outputs/handoff-accent-tracking.md.
