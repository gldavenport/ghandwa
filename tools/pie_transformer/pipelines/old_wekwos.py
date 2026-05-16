"""
Old Wékʷos historical pipeline.

Status: PROVISIONAL. The Old Wékʷos rule list is unstable and likely to change.
All test cases for this pipeline should be marked provisional.

Ported from tools/pie-transformer.jsx (WK_OLD + SHARED_PRE + GH_PRE for the
pre-stage subset applicable to Wékʷos). Per spec, no shared pre-branch block;
centumization and labiovelarization are defined here.

Key differences from Ghandwa:
  - Voiced aspirates devoice (not → voiced fricatives)
  - Laryngeal residue: h₂/h₃ → x (consonantal residue), h₁/H → ∅
  - Liquid metathesis and cluster assimilation rules
  - No Ghandwa-specific KʷC→K delabialization rule
"""

from ..rule import Rule, Context, scan
from ..tokens import (
    SHORTEN, LENGTHEN, DEVOICE, DEASPIRATE,
    is_vowel, is_laryngeal, is_consonant, is_syl_res,
    is_liquid, is_nasal, is_plain_velar,
    lengthen, shorten,
)


def _rule(id_: str, name: str, stage: str, apply_fn, requires=None) -> Rule:
    return Rule(id=id_, name=name, stage=stage, requires=requires or [], apply=apply_fn)


# ── Laryngeal color helper ─────────────────────────────────────────────────────

def _laryngeal_color(h: str, v: str) -> str:
    if v != 'e':
        return v
    if h == 'h₂':
        return 'a'
    if h == 'h₃':
        return 'o'
    return v


def _adj_uw(t: str) -> bool:
    return t in ('u', 'ū', 'w')


# ── Pre-stage (Wékʷos-internal) ───────────────────────────────────────────────

_CENTUMIZE = _rule(
    'wk.centum', 'Centumization: ḱ→k, ǵ→g, ǵʰ→gʰ', 'Pre-stage',
    lambda toks, ctx: scan(toks, lambda t, i, ts:
        'k' if t == 'ḱ' else 'g' if t == 'ǵ' else 'gʰ' if t == 'ǵʰ' else t)
)

def _labiovelarize(toks, ctx):
    out = []
    merges_before_accent = 0
    i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
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

_LABIOVELARIZE = _rule('wk.lv_merge', 'Labiovelarization: K+w → Kʷ', 'Pre-stage', _labiovelarize)

def _boukólos(toks, ctx):
    out = []
    for i, tok in enumerate(toks):
        prev = out[-1] if out else None
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if tok in ('kʷ', 'gʷ', 'gʷʰ') and (
            (prev and _adj_uw(prev)) or (nxt and _adj_uw(nxt))
        ):
            out.append('k' if tok == 'kʷ' else 'g' if tok == 'gʷ' else 'gʰ')
        else:
            out.append(tok)
    return out

_BOUKÓLOS = _rule('wk.boukólos', 'Boukólos: Kʷ→K adjacent to u/ū/w', 'Pre-stage', _boukólos)


# ── Laryngeals ────────────────────────────────────────────────────────────────

def _h_color(toks, ctx):
    t = list(toks)
    for i in range(len(t) - 1):
        if is_laryngeal(t[i]) and is_vowel(t[i + 1]):
            t[i + 1] = _laryngeal_color(t[i], t[i + 1])
    for i in range(len(t) - 1, 0, -1):
        if is_laryngeal(t[i]) and is_vowel(t[i - 1]):
            t[i - 1] = _laryngeal_color(t[i], t[i - 1])
    return t

_H_COLOR = _rule('wk.h_a', 'H-A: Laryngeal coloring — h₂/h₃ color adjacent e', 'Laryngeals', _h_color)

def _h_vhv(toks, ctx):
    out = []; i = 0
    while i < len(toks):
        tok = toks[i]
        if is_laryngeal(tok) and out and i + 1 < len(toks):
            prev, nxt = out[-1], toks[i + 1]
            if is_vowel(prev) and is_vowel(nxt) and prev == nxt:
                out.pop(); out.append(lengthen(prev)); i += 2; continue
        out.append(tok); i += 1
    return out

_H_VHV = _rule('wk.h_b1', 'H-B1: VHV→V̄ — identical vowels contract across laryngeal', 'Laryngeals', _h_vhv)

def _h_vh(toks, ctx):
    out = []; i = 0
    while i < len(toks):
        tok = toks[i]
        if is_laryngeal(tok) and out:
            prev = out[-1]
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            if is_vowel(prev) and (nxt is None or not is_vowel(nxt)):
                out.pop(); out.append(lengthen(prev)); i += 1
                # H deleted: accent shifts left if it was beyond this position
                if ctx.accent_index is not None and ctx.accent_index >= i:
                    ctx.accent_index -= 1
                continue
        out.append(tok); i += 1
    return out

_H_VH = _rule('wk.h_b2', 'H-B2: VH→V̄ — vowel before laryngeal lengthens', 'Laryngeals', _h_vh)

def _h_c_prevocalic(toks, ctx):
    """H-C: Pre-vocalic h₂/h₃ → x (laryngeal coloring residue)."""
    out = []; i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if tok in ('h₂', 'h₃') and nxt and is_vowel(nxt):
            out.append('x')
        else:
            out.append(tok)
        i += 1
    return out

_H_C = _rule('wk.h_c', 'H-C: Pre-vocalic h₂/h₃ → x (laryngeal residue)', 'Laryngeals', _h_c_prevocalic)

def _h_d_prevocalic(toks, ctx):
    """H-D: Pre-vocalic h₁/H → ∅ (no residue)."""
    out = []; i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if tok in ('h₁', 'H') and nxt and is_vowel(nxt):
            if ctx.accent_index is not None and ctx.accent_index > i:
                ctx.accent_index -= 1
            i += 1; continue  # deleted
        out.append(tok); i += 1
    return out

_H_D = _rule('wk.h_d', 'H-D: Pre-vocalic h₁/H → ∅', 'Laryngeals', _h_d_prevocalic)

def _h_btw_c(toks, ctx):
    """Old 2.2: CHC → Ca — laryngeal between consonants vocalizes as a."""
    out = []; i = 0
    while i < len(toks):
        tok = toks[i]
        if is_laryngeal(tok):
            prev = out[-1] if out else None
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            if (prev and is_consonant(prev) and not is_syl_res(prev) and
                    nxt and is_consonant(nxt) and not is_syl_res(nxt)):
                out.append('a'); i += 1; continue
        out.append(tok); i += 1
    return out

_H_BTW_C = _rule('wk.h_22', 'Old 2.2: CHC → Ca — laryngeal between consonants → a', 'Laryngeals', _h_btw_c)

def _h_initial_c(toks, ctx):
    """Old 2.4: #HC → C — initial laryngeal before consonant deleted."""
    if len(toks) > 1 and is_laryngeal(toks[0]) and is_consonant(toks[1]):
        if ctx.accent_index is not None and ctx.accent_index > 0:
            ctx.accent_index -= 1
        return toks[1:]
    return toks

_H_INIT_C = _rule('wk.h_24', 'Old 2.4: #HC → C — initial laryngeal deleted', 'Laryngeals', _h_initial_c)

def _h_remaining(toks, ctx):
    """Remaining H → x (coloring residue marker)."""
    return scan(toks, lambda t, i, ts: 'x' if is_laryngeal(t) else t)

_H_REMAINING = _rule('wk.h_rem', 'Remaining H → x (laryngeal residue)', 'Laryngeals', _h_remaining)


# ── Syllabic resonants ────────────────────────────────────────────────────────

def _syl_res_vocalize(toks, ctx):
    """Syllabic resonants → aR: r̥→ar, l̥→al, m̥→am, n̥→an."""
    RES = {'r̥': 'r', 'l̥': 'l', 'm̥': 'm', 'n̥': 'n'}
    out = []; i = 0
    while i < len(toks):
        tok = toks[i]
        if tok in RES:
            if ctx.accent_index is not None:
                if ctx.accent_index == i:
                    ctx.accent_index = len(out)  # accent moves to 'a'
                elif ctx.accent_index > i:
                    ctx.accent_index += 1         # one extra token inserted before accent
            out.extend(['a', RES[tok]])
        else:
            out.append(tok)
        i += 1
    return out

_SYL_RES = _rule('wk.syl_res', 'Syllabic resonants → aR: r̥→ar, l̥→al, m̥→am, n̥→an', 'Syllabics', _syl_res_vocalize)


# ── Aspirate treatment (devoicing, unlike Ghandwa's fricativization) ──────────

def _aspirate_before_liquid(toks, ctx):
    """Old 4.1: DʰL → DL — aspirate before liquid loses aspiration."""
    return scan(toks, lambda tok, i, ts: (
        DEASPIRATE[tok] if DEASPIRATE.get(tok) and i + 1 < len(ts) and is_liquid(ts[i + 1])
        else tok
    ))

_ASP_LIQUID = _rule('wk.asp_liq', 'Old 4.1: DʰL → DL — aspirate before liquid deaspirates', 'Aspirates', _aspirate_before_liquid)

def _aspirate_devoice(toks, ctx):
    """Old 4.2: Dʰ → T — remaining voiced aspirates devoice."""
    return scan(toks, lambda t, i, ts: DEVOICE.get(t, t))

_ASP_DEVOICE = _rule('wk.asp_dev', 'Old 4.2: Dʰ → T — aspirates devoice', 'Aspirates', _aspirate_devoice)


# ── Cluster assimilation ───────────────────────────────────────────────────────

def _liquid_metathesis(toks, ctx):
    """Old 5.1: CVLC → CLVC — liquid metathesis.

    Token count is unchanged (3 consumed, 3 emitted per firing).
    Only the vowel moves: from position i+1 to len(out)+2 in output.
    Positions after the block are unaffected.
    """
    out = []; i = 0
    while i < len(toks):
        a = toks[i] if i < len(toks) else None
        b = toks[i + 1] if i + 1 < len(toks) else None
        c = toks[i + 2] if i + 2 < len(toks) else None
        d = toks[i + 3] if i + 3 < len(toks) else None
        if (a and is_consonant(a) and not is_liquid(a) and
                b and is_vowel(b) and
                c and is_liquid(c) and
                d and is_consonant(d)):
            if ctx.accent_index is not None and ctx.accent_index == i + 1:
                ctx.accent_index = len(out) + 2  # vowel moves to third output slot
            out.extend([a, c, b])
            i += 3
        else:
            out.append(toks[i]); i += 1
    return out

_LIQ_META = _rule('wk.liq_meta', 'Old 5.1: CVLC → CLVC — liquid metathesis', 'Cluster Assimilation', _liquid_metathesis)

def _stop_before_nasal(toks, ctx):
    """5.1b: VTNV → VNDV — voiceless stop before nasal voices."""
    VS = {'p': 'b', 't': 'd', 'k': 'g', 'kʷ': 'gʷ'}
    out = []; i = 0
    while i < len(toks):
        a = toks[i]
        b = toks[i + 1] if i + 1 < len(toks) else None
        c = toks[i + 2] if i + 2 < len(toks) else None
        d = toks[i + 3] if i + 3 < len(toks) else None
        if (a and is_vowel(a) and
                b and VS.get(b) and
                c and is_nasal(c) and
                d and is_vowel(d)):
            out.extend([a, c, VS[b]])
            i += 3
        else:
            out.append(toks[i]); i += 1
    return out

_STOP_NASAL = _rule('wk.stop_nas', 'Old 5.1b: VTNV → VNDV — stop before nasal voices', 'Cluster Assimilation', _stop_before_nasal)

def _initial_pr_voice(toks, ctx):
    """Old 5.3: #pr → #br — initial labial+r voices."""
    if len(toks) >= 2 and toks[0] == 'p' and toks[1] == 'r':
        return ['b'] + toks[1:]
    return toks

_INIT_PR = _rule('wk.init_pr', 'Old 5.3: #pr → #br — initial labial+r voices', 'Cluster Assimilation', _initial_pr_voice)


# ── Pipeline ──────────────────────────────────────────────────────────────────

RULES: list[Rule] = [
    # Pre-stage
    _CENTUMIZE,
    _LABIOVELARIZE,
    _BOUKÓLOS,
    # Laryngeals
    _H_COLOR,
    _H_VHV,
    _H_VH,
    _H_C,
    _H_D,
    _H_BTW_C,
    _H_INIT_C,
    _H_REMAINING,
    # Syllabic resonants
    _SYL_RES,
    # Aspirates
    _ASP_LIQUID,
    _ASP_DEVOICE,
    # Cluster assimilation
    _LIQ_META,
    _STOP_NASAL,
    _INIT_PR,
]
