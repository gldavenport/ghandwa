"""
Late Common Ghandwa (Stage 1) shared rules.

These rules apply uniformly to all daughter branches (A, B, C).
Input: Ghandwa surface form tokens (output of the ghandwa pipeline).

Rule ordering:
  1.1a  n > m / _labial
  1.1b  m > n / _non-labial
  1.2   Final-syllable accent retraction
  1.3   Trimoraic glide shortening: Vː+{j,w} > V+{j,w}

Source: docs/daughters.md §2.1 Stage 1: Late Common Ghandwa.

Notes:
  - ɸ and θ appear in the environments of 1.1a/b per spec, but do not yet exist
    in the Ghandwa token stream at this stage. Included for completeness; vacuous.
  - Accent retraction (1.2) is blocked if ctx.accent_index is None.
  - Trimoraic shortening checks adjacency only; tautosyllabic qualification is
    implicit (long vowel + glide bigram is always tautosyllabic in Ghandwa).
"""

from ..rule import Rule, Context, scan
from pie_core.tokens import is_vowel, is_long_vowel, shorten
from ._common import make_rule as _rule, next_seg as _next_seg

# ── Category sets ──────────────────────────────────────────────────────────────

_LABIALS = frozenset(['p', 'b', 'ɸ', 'β'])
_NON_LABIALS = frozenset(['t', 'd', 'θ', 'ð', 's', 'z', 'k', 'g', 'ɣ', 'kʷ', 'gʷ', 'ɣʷ'])
_GLIDES = frozenset(['j', 'w'])


# ── Rule implementations ───────────────────────────────────────────────────────

def _nasal_assim_n(toks: list[str], ctx: Context) -> list[str]:
    """1.1a: n > m / _ {p, b, ɸ, β} (looks past internal morpheme boundaries)."""
    def fn(t, i, ts):
        if t == 'n':
            nxt, _ = _next_seg(ts, i)
            if nxt is not None and nxt in _LABIALS:
                return 'm'
        return t
    return scan(toks, fn)


def _nasal_assim_m(toks: list[str], ctx: Context) -> list[str]:
    """1.1b: m > n / _ {t, d, θ, ð, s, z, k, g, ɣ, kʷ, gʷ, ɣʷ} (looks past boundaries)."""
    def fn(t, i, ts):
        if t == 'm':
            nxt, _ = _next_seg(ts, i)
            if nxt is not None and nxt in _NON_LABIALS:
                return 'n'
        return t
    return scan(toks, fn)


def _final_accent_retract(toks: list[str], ctx: Context) -> list[str]:
    """1.2: Final-syllable accent retraction.

    If the accented vowel is the last vowel in the form, retract the accent
    to the penultimate vowel position.  No-op for monosyllables.
    """
    if ctx.accent_index is None:
        return toks
    vowel_positions = [i for i, t in enumerate(toks) if is_vowel(t)]
    if len(vowel_positions) < 2:
        return toks  # monosyllable: no retraction possible
    if ctx.accent_index == vowel_positions[-1]:
        ctx.accent_index = vowel_positions[-2]
    return toks


def _trimoraic_shorten(toks: list[str], ctx: Context) -> list[str]:
    """1.3: Vː + {j, w} > V + {j, w}: trimoraic glide-sequence regularization."""
    out = list(toks)
    for i in range(len(out) - 1):
        if is_long_vowel(out[i]) and out[i + 1] in _GLIDES:
            # Accent remains on the (now shortened) vowel; index unchanged
            out[i] = shorten(out[i])
    return out


# ── Rule list ──────────────────────────────────────────────────────────────────

RULES_LCG: list[Rule] = [
    _rule('lcg.1.1a', 'Nasal assimilation: n > m / _labial',
          'Stage 1 (Late Common Ghandwa)', _nasal_assim_n),
    _rule('lcg.1.1b', 'Nasal assimilation: m > n / _non-labial',
          'Stage 1 (Late Common Ghandwa)', _nasal_assim_m),
    _rule('lcg.1.2',  'Final-syllable accent retraction',
          'Stage 1 (Late Common Ghandwa)', _final_accent_retract,
          requires=['accent']),
    _rule('lcg.1.3',  'Trimoraic glide shortening: Vː{j,w} > V{j,w}',
          'Stage 1 (Late Common Ghandwa)', _trimoraic_shorten),
]
