"""
Daughter A phonological pipeline.

Input: output of the ghandwa pipeline (Ghandwa surface form tokens).
This pipeline is registered as downstream of 'ghandwa' in pipeline.py.

Stages:
  Stage 1 — Late Common Ghandwa (shared; imported from late_common_ghandwa.py)
  Stage 2 — Daughter A Dark Ages innovations

Stage 2A rule ordering:
  2A.1  Stress → initial (accent_index set to first vowel)
  2A.2  Devoicing: β→ɸ, ð→θ, ɣ→x, ɣʷ→xʷ
  2A.3  z → s
  2A.4  Labiovelar delabialization: kʷ→k, gʷ→g
  2A.5  Cluster spirantization before s: k→x / _s, p→ɸ / _s
        (must follow 2A.4: kʷ→k feeds ks→xs when kʷ precedes s)

Stage 3 rules: NOT IMPLEMENTED.
  Direction: voiceless fricative instability (ɸ→f, θ→t/s, x→h), cluster
  simplification with compensatory lengthening. Not yet specified precisely
  enough to pipeline. See docs/daughters.md §3.1, 3A.

Source: docs/daughters.md §§2.2 (2A), 3.1 (3A).
"""

from ..rule import Rule, Context, scan
from pie_core.tokens import is_vowel
from .late_common_ghandwa import RULES_LCG
from ._common import make_rule as _rule


# ── Stage 2A: category sets ────────────────────────────────────────────────────

# Non-sibilant voiced fricatives → voiceless counterparts
_DEVOICE_A: dict[str, str] = {
    'β':  'ɸ',
    'ð':  'θ',
    'ɣ':  'x',
    'ɣʷ': 'xʷ',  # xʷ survives to Stage 3; simplification to x not yet committed
}

# Labiovelar stops → plain velars
_DELAB_A: dict[str, str] = {
    'kʷ': 'k',
    'gʷ': 'g',
}

# Stops that spirantize before /s/
_SPIRANT_BEFORE_S: dict[str, str] = {
    'k': 'x',
    'p': 'ɸ',
}


# ── Stage 2A: rule implementations ────────────────────────────────────────────

def _stress_initial(toks: list[str], ctx: Context) -> list[str]:
    """2A.1: Stress shifts to the initial syllable (first vowel position)."""
    for i, t in enumerate(toks):
        if is_vowel(t):
            ctx.accent_index = i
            break
    return toks


def _devoice(toks: list[str], ctx: Context) -> list[str]:
    """2A.2: β→ɸ, ð→θ, ɣ→x, ɣʷ→xʷ (general devoicing of non-sibilant fricatives)."""
    return scan(toks, lambda t, i, ts: _DEVOICE_A.get(t, t))


def _z_to_s(toks: list[str], ctx: Context) -> list[str]:
    """2A.3: z → s (z devoices as part of general devoicing; eliminates /z/ entirely)."""
    return scan(toks, lambda t, i, ts: 's' if t == 'z' else t)


def _delab(toks: list[str], ctx: Context) -> list[str]:
    """2A.4: kʷ→k, gʷ→g (labiovelar delabialization)."""
    return scan(toks, lambda t, i, ts: _DELAB_A.get(t, t))


def _cluster_spirant(toks: list[str], ctx: Context) -> list[str]:
    """2A.5: k→x / _s, p→ɸ / _s (cluster spirantization before /s/ only).

    Fires after 2A.4, so kʷ has already become k. Any kʷ-before-s
    is thus correctly handled as kʷ→k (2A.4) then k→x (2A.5).
    """
    def fn(t, i, ts):
        if i + 1 < len(ts) and ts[i + 1] == 's':
            return _SPIRANT_BEFORE_S.get(t, t)
        return t
    return scan(toks, fn)


# ── Rule lists ─────────────────────────────────────────────────────────────────

RULES_STAGE2A: list[Rule] = [
    _rule('da.2.1', 'Stress → initial',
          'Stage 2 (Daughter A)', _stress_initial),
    _rule('da.2.2', 'Devoicing: β→ɸ, ð→θ, ɣ→x, ɣʷ→xʷ',
          'Stage 2 (Daughter A)', _devoice),
    _rule('da.2.3', 'z → s',
          'Stage 2 (Daughter A)', _z_to_s),
    _rule('da.2.4', 'Labiovelar delabialization: kʷ→k, gʷ→g',
          'Stage 2 (Daughter A)', _delab),
    _rule('da.2.5', 'Cluster spirantization: k→x / _s, p→ɸ / _s',
          'Stage 2 (Daughter A)', _cluster_spirant),
]

# Full Daughter A rule list: Stage 1 (shared) + Stage 2A (branch-specific)
RULES_A: list[Rule] = RULES_LCG + RULES_STAGE2A
