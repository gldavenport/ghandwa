"""
Daughter language pipelines.

Daughter A is currently implemented (Stage 2A + Stage 3A).
Daughters B and C remain stubs.

Input token stream: Daughter A chains downstream of the Ghandwa pipeline.
It receives the final Ghandwa token stream and applies daughter-level rules.
This is the same chaining pattern as neo-wekwos -> old-wekwos.

Rule ordering authority: docs/daughter-a-stage-3a-pipeline.md

Open questions preserved as inline comments. Do not silently resolve.
"""

from ..rule import Rule, Context, scan
from ..tokens import is_vowel, is_short_vowel, is_long_vowel, lengthen


# -- Rule-building helper -------------------------------------------------------

def _rule(id_: str, name: str, stage: str, apply_fn) -> Rule:
    return Rule(id=id_, name=name, stage=stage, requires=[], apply=apply_fn)


# ==============================================================================
# DAUGHTER A
# ==============================================================================

# -- Stage 2A rules ------------------------------------------------------------

# 2A.1  Voiced fricatives devoice: beta->phi, eth->theta, gamma->x, gammaw->xw
_DEVOICE_MAP = {'β': 'ɸ', 'ð': 'θ', 'ɣ': 'x', 'ɣʷ': 'xʷ'}

_2A_DEVOICE = _rule(
    'da.2a.devoice',
    'Voiced fricatives devoice: β→ɸ, ð→θ, ɣ→x, ɣʷ→xʷ',
    'Stage 2A',
    lambda toks, ctx: scan(toks, lambda t, i, ts: _DEVOICE_MAP.get(t, t)),
)

# 2A.2  z devoices to s (part of general devoicing; eliminates /z/ entirely in A)
_2A_Z_DEVOICE = _rule(
    'da.2a.z_devoice',
    'z → s (general devoicing)',
    'Stage 2A',
    lambda toks, ctx: scan(toks, lambda t, i, ts: 's' if t == 'z' else t),
)

# 2A.3  Labiovelars delabialized: kw->k, gw->g
# xw (from yw above) is handled in Stage 3A.5 after the compensatory-
# lengthening window has closed.
_LABIOVELAR_MAP = {'kʷ': 'k', 'gʷ': 'g'}

_2A_DELABIALIZE = _rule(
    'da.2a.delabialize',
    'kʷ → k, gʷ → g',
    'Stage 2A',
    lambda toks, ctx: scan(toks, lambda t, i, ts: _LABIOVELAR_MAP.get(t, t)),
)

# 2A.4  Cluster spirantization before /s/: ks->xs, ps->phis
# Open: does this apply across morpheme boundaries?
# Current implementation: fires only when tokens are directly adjacent.
def _next_phoneme(toks: list, i: int):
    """Return the next non-boundary token after index i, or None."""
    for j in range(i + 1, len(toks)):
        if toks[j] not in ('-', '.'):
            return toks[j]
    return None


def _cluster_spirantize(toks: list, ctx: Context) -> list:
    # Looks through morpheme/syllable boundaries: p-s and k-s both trigger.
    out = []
    for i, t in enumerate(toks):
        nxt = _next_phoneme(toks, i)
        if t == 'k' and nxt == 's':
            out.append('x')
        elif t == 'p' and nxt == 's':
            out.append('ɸ')
        else:
            out.append(t)
    return out

_2A_CLUSTER_SPIRANT = _rule(
    'da.2a.cluster_spirant',
    'Cluster spirantization before s: ks → xs, ps → ɸs',
    'Stage 2A',
    _cluster_spirantize,
)

# 2A.5  Initial stress
# Resets accent_index to the first vowel token.
# Ordered last in Stage 2A so token-deleting rules above have settled first.
def _initial_stress(toks: list, ctx: Context) -> list:
    for i, t in enumerate(toks):
        if is_vowel(t):
            ctx.accent_index = i
            break
    return toks

_2A_STRESS = _rule(
    'da.2a.stress',
    'Stress → initial syllable',
    'Stage 2A',
    _initial_stress,
)


# -- Stage 3A rules ------------------------------------------------------------

# 3A.1 and 3A.2 share compensatory-lengthening logic.
# Vphis, Vxs -> V:s  (3A.1)
# Vphit, Vxt -> V:t  (3A.2)
#
# Open: morpheme-boundary scope -- rule fires only for directly adjacent tokens.
# Open: long-vowel input -- rule restricted to short vowels; long vowels do not trigger.
# Open: sonorant-mediated clusters (rphis, nphis) -- do not trigger.

def _compensatory_lengthen(fricatives: frozenset, following: frozenset):
    """
    Delete a fricative between a vowel and a following coronal, lengthening
    the vowel if short. If the vowel is already long, the fricative is still
    deleted (same surface output; phonological for short vowels, analogically
    reinforced for long vowels by the dominant root-noun nom.sg. pattern).
    """
    def apply(toks: list, ctx: Context) -> list:
        out = []
        deletions_before_accent = 0
        for i, t in enumerate(toks):
            nxt = _next_phoneme(toks, i)
            prev_is_vowel = out and (is_short_vowel(out[-1]) or is_long_vowel(out[-1]))
            if (
                t in fricatives
                and prev_is_vowel
                and nxt in following
            ):
                if is_short_vowel(out[-1]):
                    out[-1] = lengthen(out[-1])  # compensatory lengthening
                # long vowel: no change needed; fricative deleted either way
                if ctx.accent_index is not None and i < ctx.accent_index:
                    deletions_before_accent += 1
                # fricative deleted -- do not append
            else:
                out.append(t)
        if ctx.accent_index is not None:
            ctx.accent_index -= deletions_before_accent
        return out
    return apply

_3A_COMPENSATE_S = _rule(
    'da.3a.1',
    'Vɸs, Vxs → Vːs (compensatory lengthening before s)',
    'Stage 3A',
    _compensatory_lengthen(frozenset({'ɸ', 'x'}), frozenset({'s'})),
)

_3A_COMPENSATE_T = _rule(
    'da.3a.2',
    'Vɸt, Vxt → Vːt (compensatory lengthening before t)',
    'Stage 3A',
    _compensatory_lengthen(frozenset({'ɸ', 'x'}), frozenset({'t'})),
)

# 3A.3  Coronal assimilation: thetas->ss, thetat->tt
# No compensatory lengthening; direct assimilation.
def _coronal_assimilate(toks: list, ctx: Context) -> list:
    out = []
    for i, t in enumerate(toks):
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if t == 'θ' and nxt in ('s', 't'):
            out.append(nxt)  # theta replaced by following coronal; geminate resolved by 3A.4
        else:
            out.append(t)
    return out

_3A_CORONAL_ASSIM = _rule(
    'da.3a.3',
    'θs → ss, θt → tt (coronal assimilation)',
    'Stage 3A',
    _coronal_assimilate,
)

# 3A.4  Geminate simplification: ss->s, tt->t
# Open: currently restricted to s/t geminates only.
# Does not apply to geminates from other sources.
def _degeminate(toks: list, ctx: Context) -> list:
    out = []
    for t in toks:
        if out and t == out[-1] and t in ('s', 't'):
            pass  # skip second of geminate
        else:
            out.append(t)
    return out

_3A_DEGEMINATE = _rule(
    'da.3a.4',
    'ss → s, tt → t (geminate simplification)',
    'Stage 3A',
    _degeminate,
)

# 3A.5  Late delabialization: xw->x
# kw and gw already handled in Stage 2A.
# xw (from yw devoicing) delayed until after compensatory-lengthening window.
_3A_DELABIALIZE_XW = _rule(
    'da.3a.5',
    'xʷ → x (late delabialization)',
    'Stage 3A',
    lambda toks, ctx: scan(toks, lambda t, i, ts: 'x' if t == 'xʷ' else t),
)


# -- Daughter A ordered rule list ----------------------------------------------

RULES_A: list = [
    _2A_DEVOICE,
    _2A_Z_DEVOICE,
    _2A_DELABIALIZE,
    _2A_CLUSTER_SPIRANT,
    _2A_STRESS,
    _3A_COMPENSATE_S,
    _3A_COMPENSATE_T,
    _3A_CORONAL_ASSIM,
    _3A_DEGEMINATE,
    _3A_DELABIALIZE_XW,
]


# ==============================================================================
# DAUGHTERS B AND C -- stubs
# ==============================================================================

RULES_B: list = []
RULES_C: list = []

NOT_IMPLEMENTED_B = True
NOT_IMPLEMENTED_C = True
