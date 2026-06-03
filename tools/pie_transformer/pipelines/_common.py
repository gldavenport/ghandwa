"""
Shared helpers for all pie_transformer pipeline modules.

Imported by: ghandwa, old_wekwos, neo_wekwos, proto_anatolian, proto_seldanic,
             late_common_ghandwa, daughter_a, daughter_b, daughter_c.
Also imported by render.py (..pipelines._common) for syllabification utilities.

Accent-tracking code is preserved verbatim in every pipeline rule that touches
it.  The accent refactor (shift_for_change / relocate API) is deferred to a
future session; see docs/handoff-accent-tracking-v2.md.

Contents
--------
make_rule         Rule constructor factory (replaces local _rule in every pipeline)
UW                frozenset({'u', 'ū', 'w'}) — labiovelar trigger vowel+glide set
laryngeal_color   h₂/h₃ e→a/o coloring (PIE flavor; NOT Anatolian χ/χʷ version)
labiovelarize     K+w → Kʷ sequence merge with accent tracking
centumize_rule    factory: centumization Rule for a given pipeline prefix
prev_seg          (token, index) of previous non-boundary token
next_seg          (token, index) of next non-boundary token
is_word_initial   True if token at i is the first non-boundary token
is_word_final     True if token at i is the last non-boundary token
_base_form        strip U+0301 acute from a token
_has_accent       True if token carries U+0301 acute
_is_ipa_vowel     True if token is a vowel (with or without accent)
_valid_onset      True if consonant cluster is a valid Ghandwa onset
_onset_split      onset-maximization split point for an inter-nuclear cluster
_syllabify        onset-maximization syllabifier for Ghandwa IPA tokens
"""

from __future__ import annotations

import unicodedata

from ..rule import Rule, Context, scan
from pie_core.tokens import BOUNDARIES, VOWELS, LIQUIDS, GLIDES


# ── Rule-building helper ───────────────────────────────────────────────────────

def make_rule(id_: str, name: str, stage: str, apply_fn, requires=None) -> Rule:
    return Rule(id=id_, name=name, stage=stage, requires=requires or [], apply=apply_fn)


# ── Shared constants ───────────────────────────────────────────────────────────

#: PIE labiovelar trigger set used in delabialization and dissimilation rules.
UW: frozenset[str] = frozenset({'u', 'ū', 'w'})


# ── Laryngeal coloring (PIE / WIE flavor) ─────────────────────────────────────

def laryngeal_color(h: str, v: str) -> str:
    """h₂ colors adjacent e→a, h₃ colors adjacent e→o.  h₁ and H are neutral.

    This is the PIE / WIE flavor used by Ghandwa, Old Wékʷos, and Proto-Seldanic.
    Proto-Anatolian's χ/χʷ coloring is kept local to proto_anatolian.py.
    """
    if v != 'e':
        return v
    if h == 'h₂':
        return 'a'
    if h == 'h₃':
        return 'o'
    return v


# ── Labiovelarization: K+w → Kʷ ──────────────────────────────────────────────

def labiovelarize(toks: list[str], ctx: Context) -> list[str]:
    """K+w → Kʷ (sequence merge) with accent-index tracking.

    Each merge reduces the token list by 1.  For every merge whose first
    token is strictly before ctx.accent_index, the accent shifts left by 1.
    Accent code preserved verbatim (pre-refactor).
    """
    out: list[str] = []
    merges_before_accent = 0
    i = 0
    while i < len(toks):
        tok, nxt = toks[i], toks[i + 1] if i + 1 < len(toks) else None
        merged = False
        if tok == 'k' and nxt == 'w':
            out.append('kʷ'); i += 2; merged = True
        elif tok == 'g' and nxt == 'w':
            out.append('gʷ'); i += 2; merged = True
        elif tok == 'gʰ' and nxt == 'w':
            out.append('gʷʰ'); i += 2; merged = True
        else:
            out.append(tok); i += 1
        if merged and ctx.accent_index is not None and (i - 2) < ctx.accent_index:
            merges_before_accent += 1
    if ctx.accent_index is not None:
        ctx.accent_index -= merges_before_accent
    return out


# ── Centumization rule factory ────────────────────────────────────────────────

def centumize_rule(id_: str, stage: str = 'Pre-stage') -> Rule:
    """Return a centumization Rule with the given id.

    Centumization: ḱ→k, ǵ→g, ǵʰ→gʰ.
    """
    def _apply(toks: list[str], ctx: Context) -> list[str]:
        return scan(toks, lambda t, i, ts:
            'k'  if t == 'ḱ'  else
            'g'  if t == 'ǵ'  else
            'gʰ' if t == 'ǵʰ' else t
        )
    return make_rule(
        id_,
        'Centumization: ḱ→k, ǵ→g, ǵʰ→gʰ',
        stage,
        _apply,
    )


# ── Boundary-skipping navigation ──────────────────────────────────────────────

def prev_seg(toks: list[str], i: int) -> tuple[str | None, int | None]:
    """Return (token, index) of the previous non-boundary token before i.
    Returns (None, None) if there is no such token.
    """
    for j in range(i - 1, -1, -1):
        if toks[j] not in BOUNDARIES:
            return toks[j], j
    return None, None


def next_seg(toks: list[str], i: int) -> tuple[str | None, int | None]:
    """Return (token, index) of the next non-boundary token after i.
    Returns (None, None) if there is no such token.
    """
    for j in range(i + 1, len(toks)):
        if toks[j] not in BOUNDARIES:
            return toks[j], j
    return None, None


def is_word_initial(toks: list[str], i: int) -> bool:
    """True if the token at i is the first non-boundary token in the stream."""
    prv, _ = prev_seg(toks, i)
    return prv is None


def is_word_final(toks: list[str], i: int) -> bool:
    """True if the token at i is the last non-boundary token in the stream."""
    nxt, _ = next_seg(toks, i)
    return nxt is None


# ── Syllabification utilities (shared with render.py) ─────────────────────────
# render.py imports these as: from .pipelines._common import _syllabify, ...

def _base_form(t: str) -> str:
    """Strip U+0301 combining acute from a token, preserving other diacritics."""
    nfd = unicodedata.normalize('NFD', t)
    return unicodedata.normalize('NFC', ''.join(c for c in nfd if c != '\u0301'))


def _has_accent(t: str) -> bool:
    """True if token carries U+0301 combining acute (lexical pitch accent)."""
    return '\u0301' in unicodedata.normalize('NFD', t)


def _is_ipa_vowel(t: str) -> bool:
    """True if token is a vowel (with or without accent mark)."""
    return _base_form(t) in VOWELS


_ONSET_STOPS: frozenset[str] = frozenset([
    'p', 'b', 't', 'd', 'k', 'g', 'kʷ', 'gʷ',
    'bʰ', 'dʰ', 'gʰ', 'gʷʰ',
])


def _valid_onset(cluster: list[str]) -> bool:
    """True if cluster is a valid complex onset for Ghandwa.
    Valid: empty, single consonant, stop+liquid, s+stop.
    """
    n = len(cluster)
    if n == 0:
        return True
    if n == 1:
        return True
    if n == 2:
        c1, c2 = cluster
        if c1 in _ONSET_STOPS and c2 in LIQUIDS:   # stop + liquid: pr, kr, gl …
            return True
        if c1 == 's' and c2 in _ONSET_STOPS:        # s + stop: st, sp, sk
            return True
        return False
    return False   # no 3-consonant onsets


def _onset_split(inter: list[str]) -> int:
    """Given a consonant sequence between two nuclei, return the index where
    the onset of the right syllable begins (onset maximization).
    """
    for start in range(len(inter)):
        if _valid_onset(inter[start:]):
            return start
    # Fallback: unreachable when single-consonant onset is always valid
    return len(inter) - 1


def _syllabify(toks: list[str]) -> list[list[str]]:
    """Onset-maximization syllabifier for Ghandwa IPA tokens.

    Returns a list of syllables; each syllable is a list of tokens.

    Rules:
    - Vowels are nuclei.
    - Post-vocalic j/w form diphthongs and remain in the preceding syllable.
    - Consonant sequences between nuclei are split by onset maximization.
    - Consonants before the first nucleus → initial onset of first syllable.
    - Consonants after the last nucleus → final coda.
    - Geminates split naturally: CC is not a valid single-onset type.
    """
    if not toks:
        return []

    labels: list[str] = []
    for i, t in enumerate(toks):
        if _is_ipa_vowel(t):
            labels.append('N')
        elif t in GLIDES and labels and labels[-1] in ('N', 'D'):
            labels.append('D')   # diphthong glide: part of preceding nucleus
        else:
            labels.append('C')

    nuc_positions = [i for i, lb in enumerate(labels) if lb == 'N']

    if not nuc_positions:
        return [list(toks)]  # no vowels — return as single unit

    syllables: list[list[str]] = []
    current: list[str] = list(toks[:nuc_positions[0]])

    for k, nuc_idx in enumerate(nuc_positions):
        current.append(toks[nuc_idx])

        pos = nuc_idx + 1
        while pos < len(toks) and labels[pos] == 'D':
            current.append(toks[pos])
            pos += 1

        if k + 1 < len(nuc_positions):
            next_nuc = nuc_positions[k + 1]
            inter = toks[pos:next_nuc]
            split = _onset_split(inter)
            current.extend(inter[:split])
            syllables.append(current)
            current = list(inter[split:])
        else:
            current.extend(toks[pos:])
            syllables.append(current)

    return syllables
