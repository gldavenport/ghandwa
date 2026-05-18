"""
Daughter C phonological pipeline.

Input: output of the ghandwa pipeline (Ghandwa surface form tokens).
This pipeline is registered as downstream of 'ghandwa' in pipeline.py.

Stages:
  Stage 1 — Late Common Ghandwa (shared; imported from late_common_ghandwa.py)
  Stage 2 — Daughter C Dark Ages innovations
  Stage 3 — Daughter C Dawn Age: z-resolution and rhotacism

Stage 2C rule ordering:
  2C.1   Stress → initial
  2C.2   s > z word-finally: / V_#, N_#, R_#
         NOTE: 2C.2a (#s > z / _[+voiced]) dropped — initial position is a
         fortition environment, not a lenition one.
  2C.3a  β ð ɣ ɣʷ > b d g gʷ (voiced fricative hardening, everywhere)
  2C.3b  z > d / N_  (post-nasal z hardens; only sibilant participation in hardening)
  2C.4   kʷ > p, gʷ > b
         (must follow 2C.3a: ɣʷ > gʷ feeds gʷ > b here)

  Ordering constraint: s-voicing (2C.2) precedes hardening (2C.3). All edge
  s-voicing fires while voiced fricatives are still present in the system.
  Hardening then resolves all voiced fricatives in one pass.
  Result: massive /z/ inventory (time bomb for Stage 3).

Stage 3C rule ordering:
  3C.1  #z > #d  [DORMANT: vacuous — no word-initial /z/ exists after dropping
                  2C.2a; retained as backstop in case upstream changes]
  3C.2  RzV > RV  (post-liquid z before vowel deletes, no lengthening;
                   historically -RzV- > -RRV- > -RV-, pipeline outputs final form)
  3C.3  VzC > V̄C  (pre-consonantal z: z deletes, preceding vowel lengthens;
                   C includes glides j, w — covers gen.sg. -ozjo > -ōjo)
  3C.4  VRzC > V̄RC  (post-liquid pre-consonantal: z deletes, preceding vowel
                      lengthens; historically -VRzN- > -VRRN- > -V̄RN-)
  3C.5  z > ʁ   (rhotacism: all remaining /z/ → uvular fricative ʁ)
  3C.6  Rʁ# > ʁ#  (liquid drops before word-final ʁ; resolves VRs# chain:
                    VRs [Stage 2] > VRz > VRʁ [3C.5] > Vʁ [this rule])
  3C.7  ʁ > r / r_  (ʁ merges immediately with adjacent inherited /r/ only)

New token introduced: 'ʁ' (voiced uvular fricative). Stable in Stage 3; merges
adjacent to /r/ immediately, elsewhere deferred to Stage 4 or sub-daughters.

Open (Stage 4 or sub-daughter):
  - ʁ > r in all remaining environments
  - Final-vowel shortening and apocope
  - Right-edge morphological erosion
  - Paradigm repair: suppletive pairs widened by Stage 2C (e.g. kʷṓ > pṓ ~ kunés > kunéʁ)

Source: docs/daughters.md §§2.2 (2C), 3.1 (3C); docs/ghandwa-daughter-c.md.
"""

from ..rule import Rule, Context, scan
from ..tokens import (
    is_vowel, is_short_vowel, is_long_vowel, lengthen,
    LIQUIDS, NASALS, GLIDES,
)
from .late_common_ghandwa import RULES_LCG


# ── Rule-building helper ───────────────────────────────────────────────────────

def _rule(id_: str, name: str, stage: str, apply_fn, requires=None) -> Rule:
    return Rule(id=id_, name=name, stage=stage, requires=requires or [], apply=apply_fn)


# ── Category sets ──────────────────────────────────────────────────────────────

# Non-sibilant voiced fricatives → voiced stops (Stage 2C hardening)
_HARDEN_C: dict[str, str] = {
    'β':  'b',
    'ð':  'd',
    'ɣ':  'g',
    'ɣʷ': 'gʷ',  # intermediate: gʷ > b handled by 2C.4 after hardening pass
}

# Labiovelar stops → labials
_LABIOVELARS_C: dict[str, str] = {
    'kʷ': 'p',
    'gʷ': 'b',
}

# Tokens treated as consonants for VzC / VRzC environment checks.
# Includes glides (j, w) — covers gen.sg. -ozjo > -ōjo.
_CONSONANTS_C: frozenset[str] = frozenset([
    'p', 'b', 't', 'd', 'k', 'g', 'kʷ', 'gʷ',
    's', 'z', 'ʁ',
    'm', 'n', 'r', 'l',
    'j', 'w',
    'ɸ', 'θ', 'x', 'xʷ',
    'β', 'ð', 'ɣ', 'ɣʷ',
])

_BOUNDARY: frozenset[str] = frozenset(['-', '.'])


# ── Internal helpers ───────────────────────────────────────────────────────────

def _prev_seg(toks: list[str], i: int) -> tuple[str | None, int | None]:
    """Return (token, index) of the previous non-boundary token before i, or (None, None)."""
    for j in range(i - 1, -1, -1):
        if toks[j] not in _BOUNDARY:
            return toks[j], j
    return None, None


def _next_seg(toks: list[str], i: int) -> tuple[str | None, int | None]:
    """Return (token, index) of the next non-boundary token after i, or (None, None)."""
    for j in range(i + 1, len(toks)):
        if toks[j] not in _BOUNDARY:
            return toks[j], j
    return None, None


def _is_word_final(toks: list[str], i: int) -> bool:
    """True if the token at i is the last non-boundary token in the stream."""
    nxt, _ = _next_seg(toks, i)
    return nxt is None


def _is_word_initial(toks: list[str], i: int) -> bool:
    """True if the token at i is the first non-boundary token in the stream."""
    prv, _ = _prev_seg(toks, i)
    return prv is None


# ── Stage 2C: rule implementations ────────────────────────────────────────────

def _stress_initial_c(toks: list[str], ctx: Context) -> list[str]:
    """2C.1: Stress shifts to the initial syllable (first vowel position)."""
    for i, t in enumerate(toks):
        if is_vowel(t):
            ctx.accent_index = i
            break
    return toks


def _s_voice_final(toks: list[str], ctx: Context) -> list[str]:
    """2C.2: s > z / {V, N, R}_#  — word-final s voices after vowels, nasals, and liquids.

    2C.2b  s > z / V_#   (word-final after vowel)
    2C.2c  s > z / N_#   (word-final after nasal; feeds post-nasal hardening 2C.3b)
    2C.2d  s > z / R_#   (word-final after liquid; feeds Stage 3 VRz# chain)

    Blocked in all non-final positions and before voiceless stops at word-initial
    (2C.2a dropped: initial position is fortition environment, not lenition).
    """
    out = list(toks)
    for i, t in enumerate(out):
        if t != 's' or not _is_word_final(out, i):
            continue
        prev, _ = _prev_seg(out, i)
        if prev is not None and (is_vowel(prev) or prev in NASALS or prev in LIQUIDS):
            out[i] = 'z'
    return out


def _harden_fricatives_c(toks: list[str], ctx: Context) -> list[str]:
    """2C.3a: β→b, ð→d, ɣ→g, ɣʷ→gʷ — voiced fricative hardening everywhere.

    /z/ is not subject to hardening here (sibilant excluded from the general
    hardening pass). Post-nasal /z/ is handled separately by 2C.3b.
    """
    return scan(toks, lambda t, i, ts: _HARDEN_C.get(t, t))


def _harden_postnasal_z(toks: list[str], ctx: Context) -> list[str]:
    """2C.3b: z > d / N_ — post-nasal z hardens to stop.

    Must follow 2C.2: word-final -Ns > -Nz (2C.2c) feeds this rule.
    The one environment where the sibilant participates in hardening.
    e.g. -Vns > -Vnz (2C.2c) > -Vnd (this rule).
    """
    def fn(t, i, ts):
        if t == 'z':
            prev, _ = _prev_seg(ts, i)
            if prev is not None and prev in NASALS:
                return 'd'
        return t
    return scan(toks, fn)


def _labiovelars_c(toks: list[str], ctx: Context) -> list[str]:
    """2C.4: kʷ→p, gʷ→b.

    Must follow 2C.3a: ɣʷ→gʷ (hardening) feeds gʷ→b here.
    Catches both original Ghandwa gʷ and gʷ produced by ɣʷ hardening.
    """
    return scan(toks, lambda t, i, ts: _LABIOVELARS_C.get(t, t))


# ── Stage 3C: rule implementations ────────────────────────────────────────────

def _initial_fortition_dormant(toks: list[str], ctx: Context) -> list[str]:
    """3C.1: #z > #d  [DORMANT].

    Vacuous: 2C.2a was dropped, so no word-initial /z/ is created by Stage 2C,
    and Ghandwa had none. Retained as a backstop; do not remove silently.
    If a future upstream rule creates initial /z/, this fires correctly.
    """
    def fn(t, i, ts):
        if t == 'z' and _is_word_initial(ts, i):
            return 'd'
        return t
    return scan(toks, fn)


def _liq_z_before_vowel(toks: list[str], ctx: Context) -> list[str]:
    """3C.2: RzV > RV — post-liquid z before a vowel deletes (no lengthening).

    Historically: -RzV- > -RRV- > -RV- (z assimilates to preceding liquid,
    geminate simplifies). Pipeline outputs the final form directly.
    Must precede 3C.3 (VzC) to avoid incorrect lengthening in this environment.
    """
    out = list(toks)
    i = 0
    deletions_before_accent = 0
    while i < len(out):
        t = out[i]
        if t == 'z':
            prev, _ = _prev_seg(out, i)
            nxt, _ = _next_seg(out, i)
            if prev in LIQUIDS and nxt is not None and is_vowel(nxt):
                out.pop(i)
                if ctx.accent_index is not None and i < ctx.accent_index:
                    deletions_before_accent += 1
                continue  # recheck same index after deletion
        i += 1
    if ctx.accent_index is not None:
        ctx.accent_index -= deletions_before_accent
    return out


def _vz_before_cons(toks: list[str], ctx: Context) -> list[str]:
    """3C.3: VzC > V̄C — pre-consonantal z deletes, preceding vowel lengthens.

    Preceding token must be a vowel (not a liquid — RzC is handled by 3C.4).
    C is any consonant including glides (j, w): this covers gen.sg. -ozjo > -ōjo
    (tie-bar z͡j treated as sequence zj; j is the following consonant).

    If the preceding vowel is already long, it remains long (rule still fires;
    the length is vacuously maintained).
    """
    out = list(toks)
    i = 0
    deletions_before_accent = 0
    while i < len(out):
        t = out[i]
        if t == 'z':
            prev, pi = _prev_seg(out, i)
            nxt, _ = _next_seg(out, i)
            if (prev is not None and is_vowel(prev)
                    and nxt is not None and nxt in _CONSONANTS_C):
                if is_short_vowel(out[pi]):
                    out[pi] = lengthen(out[pi])
                out.pop(i)
                if ctx.accent_index is not None and i < ctx.accent_index:
                    deletions_before_accent += 1
                continue
        i += 1
    if ctx.accent_index is not None:
        ctx.accent_index -= deletions_before_accent
    return out


def _rlz_before_cons(toks: list[str], ctx: Context) -> list[str]:
    """3C.4: VRzC > V̄RC — post-liquid pre-consonantal z deletes, vowel before R lengthens.

    Historically: -VRzC- > -VRRC- > -V̄RC- (z assimilates to preceding liquid,
    geminate compensates as vowel lengthening). Pipeline outputs final form.

    Covers: pérznā > pērnā, karznóm > kārnóm.

    Preceding token must be a liquid (R); the token before the liquid must be
    a vowel. This is mutually exclusive with 3C.3 (which requires the token
    before z to be a vowel, not a liquid).
    """
    out = list(toks)
    i = 0
    deletions_before_accent = 0
    while i < len(out):
        t = out[i]
        if t == 'z':
            prev, pi = _prev_seg(out, i)
            nxt, _ = _next_seg(out, i)
            if (prev is not None and prev in LIQUIDS
                    and nxt is not None and nxt in _CONSONANTS_C):
                # find the vowel before the liquid
                vow, vi = _prev_seg(out, pi)
                if vow is not None and is_vowel(vow):
                    if is_short_vowel(out[vi]):
                        out[vi] = lengthen(out[vi])
                    out.pop(i)
                    if ctx.accent_index is not None and i < ctx.accent_index:
                        deletions_before_accent += 1
                    continue
        i += 1
    if ctx.accent_index is not None:
        ctx.accent_index -= deletions_before_accent
    return out


def _rhotacism(toks: list[str], ctx: Context) -> list[str]:
    """3C.5: z > ʁ — rhotacism of all remaining /z/.

    Fires after 3C.2, 3C.3, 3C.4 have consumed their environments.
    Remaining /z/ environments at this point:
      - VzV  (intervocalic; inherited from Ghandwa)
      - Vz#  (word-final after vowel; from 2C.2b)
      - Rz#  (word-final after liquid; from 2C.2d — feeds 3C.6)

    Introduces the new token 'ʁ' (voiced uvular fricative).
    """
    return scan(toks, lambda t, i, ts: 'ʁ' if t == 'z' else t)


def _liquid_final_simplify(toks: list[str], ctx: Context) -> list[str]:
    """3C.6: Rʁ# > ʁ# — word-final liquid drops before ʁ.

    Resolves the VRs# chain:
      Stage 2: -VRs# > -VRz#  (2C.2d: s voices after liquid)
      Stage 3: -VRz# > -VRʁ#  (3C.5: rhotacism)
              -VRʁ# > -Vʁ#   (this rule: liquid lost)

    The liquid is deleted; ʁ survives. If ʁ is then adjacent to an inherited
    /r/, 3C.7 will merge it. If the liquid was /r/, that triggers 3C.7
    immediately — effectively -Vrʁ# > -Vrr# > -Vr# (via 3C.6 + 3C.7).
    If the liquid was /l/, ʁ survives as-is (lʁ does not trigger 3C.7).
    """
    out = list(toks)
    i = 0
    deletions_before_accent = 0
    while i < len(out):
        t = out[i]
        if t in LIQUIDS:
            nxt, ni = _next_seg(out, i)
            if nxt == 'ʁ' and _is_word_final(out, ni):
                out.pop(i)
                if ctx.accent_index is not None and i < ctx.accent_index:
                    deletions_before_accent += 1
                continue
        i += 1
    if ctx.accent_index is not None:
        ctx.accent_index -= deletions_before_accent
    return out


def _rho_merge(toks: list[str], ctx: Context) -> list[str]:
    """3C.7: ʁ > r / r_ — ʁ merges immediately with adjacent inherited /r/.

    Only /r/ triggers merger, not /l/. ʁ adjacent to /l/ is stable at this stage.
    Merger is bidirectional (ʁr or rʁ both fire).
    All other ʁ environments are deferred to Stage 4 or sub-daughters.
    """
    def fn(t, i, ts):
        if t == 'ʁ':
            prev, _ = _prev_seg(ts, i)
            nxt, _ = _next_seg(ts, i)
            if prev == 'r' or nxt == 'r':
                return 'r'
        return t
    return scan(toks, fn)


# ── Rule lists ─────────────────────────────────────────────────────────────────

RULES_STAGE2C: list[Rule] = [
    _rule('dc.2.1',  'Stress → initial',
          'Stage 2 (Daughter C)', _stress_initial_c),
    _rule('dc.2.2',  's > z / V_#, N_#, R_# (word-final voicing)',
          'Stage 2 (Daughter C)', _s_voice_final),
    _rule('dc.2.3a', 'β→b, ð→d, ɣ→g, ɣʷ→gʷ (voiced fricative hardening)',
          'Stage 2 (Daughter C)', _harden_fricatives_c),
    _rule('dc.2.3b', 'z > d / N_ (post-nasal hardening)',
          'Stage 2 (Daughter C)', _harden_postnasal_z),
    _rule('dc.2.4',  'kʷ→p, gʷ→b (labiovelars)',
          'Stage 2 (Daughter C)', _labiovelars_c),
]

RULES_STAGE3C: list[Rule] = [
    _rule('dc.3.1',  '#z > #d [DORMANT: vacuous after dropping 2C.2a]',
          'Stage 3 (Daughter C)', _initial_fortition_dormant),
    _rule('dc.3.2',  'RzV > RV (post-liquid z before vowel: delete)',
          'Stage 3 (Daughter C)', _liq_z_before_vowel),
    _rule('dc.3.3',  'VzC > V̄C (pre-consonantal z: delete + lengthen)',
          'Stage 3 (Daughter C)', _vz_before_cons),
    _rule('dc.3.4',  'VRzC > V̄RC (post-liquid pre-consonantal z: delete + lengthen)',
          'Stage 3 (Daughter C)', _rlz_before_cons),
    _rule('dc.3.5',  'z > ʁ (rhotacism)',
          'Stage 3 (Daughter C)', _rhotacism),
    _rule('dc.3.6',  'Rʁ# > ʁ# (liquid drops before word-final ʁ)',
          'Stage 3 (Daughter C)', _liquid_final_simplify),
    _rule('dc.3.7',  'ʁ > r / r_ (ʁ merges with adjacent inherited /r/)',
          'Stage 3 (Daughter C)', _rho_merge),
]

# Full Daughter C rule list: Stage 1 (shared) + Stage 2C + Stage 3C
RULES_C: list[Rule] = RULES_LCG + RULES_STAGE2C + RULES_STAGE3C
