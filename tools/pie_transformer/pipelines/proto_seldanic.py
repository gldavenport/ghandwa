"""
Proto-Seldanic historical pipeline.

Rule ordering follows tools/pie_transformer/docs/proto-seldanic-pipeline.md.

Key features:
  - Dʰ > Tʰ (voiced aspirates devoice, retaining aspiration)
  - CHC > CaC (uniform; no high-vowel conditioning)
  - R̥ > aR generally; KʷR̥ > KʷuR > KuR (labiovelar exception feeds delabialization)
  - TT > ss / ssC > sC (dental clusters, same as Ghandwa, ordered before CHC)
  - Kʷ class covers all labiovelars regardless of aspiration (kʷ, gʷ, kʷʰ)
  - No Grimm's Law; no p-loss; no s > z; no final-syllable erosion
  - No accent dependency; fully implementable without accent tracking
"""

from ..rule import Rule, Context, scan
from pie_core.tokens import (
    is_vowel, is_laryngeal, is_syl_res, is_dental, is_consonant, is_boundary,
    lengthen,
)
from ._common import (
    make_rule as _rule,
    UW,
    laryngeal_color as _laryngeal_color,
    centumize_rule,
)


# ── Category helpers (Seldanic-local) ─────────────────────────────────────────

LABIOVELARS = ('kʷ', 'gʷ', 'kʷʰ', 'gʷʰ')
DELAB_MAP   = {'kʷ': 'k', 'gʷ': 'g', 'kʷʰ': 'kʰ', 'gʷʰ': 'gʰ'}
SYL_RES_MAP = {'r̥': 'r', 'l̥': 'l', 'm̥': 'm', 'n̥': 'n'}


# ── Rule 1: Adjacent laryngeal coloring ───────────────────────────────────────

def _h_color(toks: list[str], ctx: Context) -> list[str]:
    """H-1: h₂/h₃ color adjacent e → a/o."""
    t = list(toks)
    for i in range(len(t) - 1):
        if is_laryngeal(t[i]) and is_vowel(t[i + 1]):
            t[i + 1] = _laryngeal_color(t[i], t[i + 1])
    for i in range(len(t) - 1, 0, -1):
        if is_laryngeal(t[i]) and is_vowel(t[i - 1]):
            t[i - 1] = _laryngeal_color(t[i], t[i - 1])
    return t

_H_COLOR = _rule('sel.1.1', 'H-1: Laryngeal coloring — h₂/h₃ color adjacent e', 'Laryngeals', _h_color)


# ── Rule 2: Postvocalic laryngeal lengthening ─────────────────────────────────

def _h_vh(toks: list[str], ctx: Context) -> list[str]:
    """H-2: VH → V̄ before consonant or word boundary."""
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        if is_laryngeal(tok) and out:
            prev = out[-1]
            nxt  = toks[i + 1] if i + 1 < len(toks) else None
            if is_vowel(prev) and (nxt is None or not is_vowel(nxt)):
                out.pop()
                out.append(lengthen(prev))
                if ctx.accent_index is not None and ctx.accent_index > len(out):
                    ctx.accent_index -= 1
                i += 1
                continue
        out.append(tok)
        i += 1
    return out

_H_VH = _rule('sel.2.1', 'H-2: VH → V̄ — postvocalic laryngeal lengthening', 'Laryngeals', _h_vh)


# ── Rule 3: Voiced obstruent → voiceless before t/s ──────────────────────────

def _voiced_before_ts(toks: list[str], ctx: Context) -> list[str]:
    """Voiced obstruent → voiceless before t or s (Core IE).

    Runs before dental cluster simplification so that the feeding chain
    *dt > tt > ss is fully ordered: devoicing feeds TT > ss.
    Voiced aspirates are still present at this stage; they devoice to plain
    voiceless stops (aspiration lost in this environment).
    """
    def _fn(tok: str, i: int, ts: list[str]) -> str:
        nxt = ts[i + 1] if i + 1 < len(ts) else None
        if not nxt or nxt not in ('t', 's'):
            return tok
        if tok in ('b', 'bʰ'):          return 'p'
        if tok in ('d', 'dʰ'):          return 't'
        if tok in ('g', 'gʰ'):          return 'k'
        if tok in ('gʷ', 'gʷʰ'):        return 'kʷ'
        return tok
    return scan(toks, _fn)

_VOICED_BTS = _rule('sel.2.2', 'Voiced obstruent → voiceless before t/s (Core IE)', 'Consonants', _voiced_before_ts)


# ── Rule 4: Dental clusters ───────────────────────────────────────────────────

def _tt_ss(toks: list[str], ctx: Context) -> list[str]:
    """TT → ss: dental before dental → geminate ss."""
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if is_dental(tok) and nxt and is_dental(nxt):
            out.extend(['s', 's'])
            i += 2
        else:
            out.append(tok)
            i += 1
    return out

_TT_SS = _rule('sel.3.1', 'TT → ss: dental + dental → geminate ss', 'Dentals', _tt_ss)


def _ssc_simplify(toks: list[str], ctx: Context) -> list[str]:
    """ssC → sC: geminate ss simplifies before consonant."""
    out: list[str] = []
    i = 0
    while i < len(toks):
        if (toks[i] == 's' and
                i + 1 < len(toks) and toks[i + 1] == 's' and
                i + 2 < len(toks) and is_consonant(toks[i + 2])):
            out.append('s')
            if ctx.accent_index is not None and ctx.accent_index > i:
                ctx.accent_index -= 1
            i += 2
        else:
            out.append(toks[i])
            i += 1
    return out

_SSC = _rule('sel.3.2', 'ssC → sC: geminate ss simplifies before consonant', 'Dentals', _ssc_simplify)


# ── Rule 5: Interconsonantal laryngeals (CHC → CaC) ───────────────────────────

def _chc_repair(toks: list[str], ctx: Context) -> list[str]:
    """H-3: CHC → CaC — uniform a-repair.

    Ordered after dental cluster simplification (rule 4) so clusters are
    resolved before CHC vocalization. Ordered before centum merger and
    aspirate devoicing so laryngeals are still consonantal.

    KʷHC sequences become KʷaC; the labiovelar then precedes a vowel and
    is not caught by the later delabialization rule (rule 9).
    """
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        if is_laryngeal(tok):
            prev = out[-1] if out else None
            nxt  = toks[i + 1] if i + 1 < len(toks) else None
            if (prev and is_consonant(prev) and not is_syl_res(prev) and
                    nxt and is_consonant(nxt) and not is_syl_res(nxt)):
                out.append('a')
                # Replaced 1 laryngeal with 1 'a': net token count unchanged
                i += 1
                continue
        out.append(tok)
        i += 1
    return out

_CHC = _rule('sel.4.1', 'H-3: CHC → CaC — uniform interconsonantal laryngeal repair', 'Laryngeals', _chc_repair)


# ── Rule 6: Centum merger ─────────────────────────────────────────────────────

_CENTUM = centumize_rule('sel.5.1', stage='Centum')  # sel.5.1


# ── Rule 7: Voiced aspirates devoice, retaining aspiration ───────────────────

_DEASPIRATE_VOICE = _rule(
    'sel.6.1', 'Dʰ → Tʰ: bʰ→pʰ, dʰ→tʰ, gʰ→kʰ, gʷʰ→kʷʰ', 'Aspirates',
    lambda toks, ctx: scan(toks, lambda t, i, ts:
        'pʰ'  if t == 'bʰ'  else
        'tʰ'  if t == 'dʰ'  else
        'kʰ'  if t == 'gʰ'  else
        'kʷʰ' if t == 'gʷʰ' else t
    )
)


# ── Rule 8: Syllabic resonants ────────────────────────────────────────────────

def _syl_res(toks: list[str], ctx: Context) -> list[str]:
    """R̥ vocalization: KʷR̥ → KʷuR (runs first), then R̥ → aR.

    Kʷ class covers all labiovelars (kʷ, gʷ, kʷʰ), including kʷʰ created
    from gʷʰ via rules 5–6. The KʷuR output feeds rule 8 (delabialization).
    """
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        if is_syl_res(tok):
            res    = SYL_RES_MAP[tok]
            prev   = out[-1] if out else None
            # KʷR̥ → KʷuR
            if prev in LABIOVELARS:
                out.extend(['u', res])
            else:
                # R̥ → aR
                out.extend(['a', res])
            # Replaced 1 syllabic resonant with 2 tokens: update accent
            if ctx.accent_index is not None and ctx.accent_index > i:
                ctx.accent_index += 1
            i += 1
        else:
            out.append(tok)
            i += 1
    return out

_SYL_RES = _rule('sel.7.1', 'Syllabic resonants: KʷR̥→KʷuR, R̥→aR', 'Syllabics', _syl_res)


# ── Rule 9: Labiovelar delabialization ────────────────────────────────────────

def _delab(toks: list[str], ctx: Context) -> list[str]:
    """Kʷ → K / _C and / _{u,ū,w} and / {u,ū,w}_.

    Covers all labiovelars (kʷ, gʷ, kʷʰ). Catches KʷuR output of rule 8
    via the _{u} environment. KʷaC sequences (from rule 5) are NOT caught
    here; Kʷ before a vowel does not delabialized.
    """
    out: list[str] = []
    for i, tok in enumerate(toks):
        if tok in LABIOVELARS:
            prev = out[-1] if out else None
            nxt  = toks[i + 1] if i + 1 < len(toks) else None
            prev_triggers = prev in UW
            nxt_triggers  = (nxt in UW or
                             (nxt is not None and
                              is_consonant(nxt) and
                              not is_syl_res(nxt) and
                              not is_boundary(nxt)))
            if prev_triggers or nxt_triggers:
                out.append(DELAB_MAP[tok])
            else:
                out.append(tok)
        else:
            out.append(tok)
    return out

_DELAB = _rule('sel.8.1', 'Kʷ → K / _C and /{u,ū,w}_ and /_{u,ū,w}', 'Labiovelars', _delab)


# ── Remaining laryngeals → ∅ ──────────────────────────────────────────────────

def _h_drop(toks: list[str], ctx: Context) -> list[str]:
    """H → ∅: delete any surviving laryngeals after all laryngeal rules."""
    out: list[str] = []
    for i, tok in enumerate(toks):
        if is_laryngeal(tok):
            if ctx.accent_index is not None and ctx.accent_index > len(out):
                ctx.accent_index -= 1
        else:
            out.append(tok)
    return out

_H_DROP = _rule('sel.9.1', 'H → ∅: remaining laryngeals deleted', 'Laryngeals', _h_drop)


# ── Pipeline (ordered flat list) ──────────────────────────────────────────────

RULES: list[Rule] = [
    # Rule 1: laryngeal coloring
    _H_COLOR,
    # Rule 2: postvocalic laryngeal lengthening
    _H_VH,
    # Rule 3: voiced obstruents devoice before t/s (feeds TT > ss)
    _VOICED_BTS,
    # Rule 4: dental clusters (after devoicing)
    _TT_SS,
    _SSC,
    # Rule 5: interconsonantal laryngeals
    _CHC,
    # Rule 6: centum merger
    _CENTUM,
    # Rule 7: voiced aspirates devoice
    _DEASPIRATE_VOICE,
    # Rule 8: syllabic resonants (KʷR̥ → KʷuR first, then R̥ → aR)
    _SYL_RES,
    # Rule 9: labiovelar delabialization
    _DELAB,
    # Cleanup: drop any surviving laryngeals
    _H_DROP,
]
