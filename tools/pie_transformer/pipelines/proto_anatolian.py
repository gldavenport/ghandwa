"""
Proto-Anatolian historical pipeline.

Rule ordering follows PIE → Proto-Anatolian sound changes v0.7:

  1.  Accent preserved; mobile paradigms inherited.
  2.  Laryngeal realization: h₂→χ, h₃→χʷ; h₁ retained for now.
  3.  Laryngeal coloring: χe/eχ→χa/aχ; χʷe/eχʷ→χʷo/oχʷ.
  4.  Laryngeal-cluster assimilation (core: χ/χʷ only):
        VRχV, VRχʷV → VRRV
        sχ, sχʷ → ss
        Tχ, Tχʷ → TT
      Toggle: enable-h1-cluster-assimilation (default off)
        VRh₁V → VRRV; sh₁ → ss; Th₁ → TT
  5.  e-lowering: e→a / _Rχ, _Rχʷ, _{r,n}{T,#}
  6.  h₁ loss and compensatory lengthening:
        eh₁ → ǣ  (special case, fires before general rule)
        Vh₁ → V̄
        h₁ → ∅ elsewhere
      Toggle: enable-initial-h1-glottal-stop (default True)
        h₁ → ʔ / #_V
  7.  Syllabic resonants retained; wR̥→uR; kʷR̥→kuR.
  8.  Voiced aspirates merge with voiced stops: Dʰ→D.
  9.  Dental-yod affrication: ty→ts.
  10. Prosodic stop voicing (flagged; default off):
        T→D / prosodically weak position
        T = p, t, ḱ, k, kʷ; not ts, s, χ, χʷ
      Toggle: enable-prosodic-stop-voicing

Context options (pass via Context.options dict):
  enable-h1-cluster-assimilation   bool  default False
  enable-initial-h1-glottal-stop   bool  default True
  enable-prosodic-stop-voicing     bool  default False

Notes:
  - χ/χʷ survive into Proto-Anatolian; only h₁ is deleted.
  - ǣ is a distinct PA output symbol; daughter rules decide its fate.
  - Step 9 must precede step 10: ty→ts before T→D; ts immune to step 10.
  - Prosodic voicing uses coda-biased syllabification: look right for next
    vowel stopping at any boundary; if boundary intervenes, look left.
    A consonant is protected only if its syllable nucleus == accent_index.
"""

from __future__ import annotations

from ..rule import Rule, Context, scan
from ..tokens import (
    SHORTEN, LENGTHEN, DEASPIRATE,
    is_vowel, is_laryngeal, is_syl_res, is_dental, is_consonant,
    is_sonorant, is_boundary, is_nasal, is_liquid,
    lengthen, shorten,
)


# ── Rule-building helper ───────────────────────────────────────────────────────

def _rule(id_: str, name: str, stage: str, apply_fn, requires=None) -> Rule:
    return Rule(
        id=id_,
        name=name,
        stage=stage,
        requires=requires or [],
        apply=apply_fn,
    )


# ── Category helpers ──────────────────────────────────────────────────────────

_VOICE_TARGETS: frozenset[str] = frozenset(['p', 't', 'k', 'ḱ', 'kʷ'])
_VOICE_MAP: dict[str, str] = {'p': 'b', 't': 'd', 'k': 'g', 'ḱ': 'ǵ', 'kʷ': 'gʷ'}

_RESONANTS: frozenset[str] = frozenset(['r', 'l', 'm', 'n', 'w', 'y', 'j',
                                         'r̥', 'l̥', 'm̥', 'n̥'])

_UVULAR: frozenset[str] = frozenset(['χ', 'χʷ'])


# ── Step 2: Laryngeal realization ─────────────────────────────────────────────

def _h_realize(toks: list[str], ctx: Context) -> list[str]:
    """h₂→χ, h₃→χʷ. h₁ unchanged."""
    out = []
    for tok in toks:
        if tok == 'h₂':
            out.append('χ')
        elif tok == 'h₃':
            out.append('χʷ')
        else:
            out.append(tok)
    return out

_H_REALIZE = _rule(
    'pa.h_realize',
    'Laryngeal realization: h₂→χ, h₃→χʷ',
    'Laryngeals',
    _h_realize,
)


# ── Step 3: Laryngeal coloring ────────────────────────────────────────────────

def _h_color(toks: list[str], ctx: Context) -> list[str]:
    """
    χe/eχ → χa/aχ; χʷe/eχʷ → χʷo/oχʷ.
    Forward pass: χ/χʷ colors following e.
    Backward pass: χ/χʷ colors preceding e.
    """
    t = list(toks)

    def _target(h: str) -> str:
        return 'a' if h == 'χ' else 'o'

    for i in range(len(t) - 1):
        if t[i] in _UVULAR and t[i + 1] == 'e':
            t[i + 1] = _target(t[i])

    for i in range(len(t) - 1, 0, -1):
        if t[i] in _UVULAR and t[i - 1] == 'e':
            t[i - 1] = _target(t[i])

    return t

_H_COLOR = _rule(
    'pa.h_color',
    'Laryngeal coloring: χe/eχ→χa/aχ, χʷe/eχʷ→χʷo/oχʷ',
    'Laryngeals',
    _h_color,
)


# ── Step 4: Laryngeal-cluster assimilation ────────────────────────────────────

def _build_assimilation(H_set: frozenset[str], id_suffix: str, label: str):
    """Build VRHV, sH, TH assimilation functions for a given laryngeal set."""

    def _vrhv(toks: list[str], ctx: Context) -> list[str]:
        out: list[str] = []
        i = 0
        while i < len(toks):
            if (i + 3 <= len(toks) - 1 and
                    is_vowel(toks[i]) and
                    toks[i + 1] in _RESONANTS and
                    toks[i + 2] in H_set and
                    is_vowel(toks[i + 3])):
                res = toks[i + 1]
                out.extend([toks[i], res, res])
                if ctx.accent_index is not None and ctx.accent_index > len(out) - 1:
                    ctx.accent_index -= 1
                i += 3
            else:
                out.append(toks[i])
                i += 1
        return out

    def _sh_ss(toks: list[str], ctx: Context) -> list[str]:
        out: list[str] = []
        i = 0
        while i < len(toks):
            if toks[i] == 's' and i + 1 < len(toks) and toks[i + 1] in H_set:
                out.extend(['s', 's'])
                i += 2
            else:
                out.append(toks[i])
                i += 1
        return out

    def _th_tt(toks: list[str], ctx: Context) -> list[str]:
        out: list[str] = []
        i = 0
        while i < len(toks):
            tok = toks[i]
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            if is_consonant(tok) and not is_sonorant(tok) and nxt and nxt in H_set:
                out.extend([tok, tok])
                i += 2
            else:
                out.append(tok)
                i += 1
        return out

    return (
        _rule(f'pa.vrhv{id_suffix}', f'VRχV→VRRV {label}', 'Assimilation', _vrhv),
        _rule(f'pa.sh_ss{id_suffix}', f'sχ→ss {label}', 'Assimilation', _sh_ss),
        _rule(f'pa.th_tt{id_suffix}', f'Tχ→TT {label}', 'Assimilation', _th_tt),
    )

_VRHV_CORE, _SH_SS_CORE, _TH_TT_CORE = _build_assimilation(_UVULAR, '', '(χ/χʷ)')
_VRHV_H1, _SH_SS_H1, _TH_TT_H1 = _build_assimilation(frozenset(['h₁']), '_h1', '(h₁)')


def _assimilation_core(toks: list[str], ctx: Context) -> list[str]:
    toks = _VRHV_CORE.apply(toks, ctx)
    toks = _SH_SS_CORE.apply(toks, ctx)
    toks = _TH_TT_CORE.apply(toks, ctx)
    return toks

_ASSIMILATION_CORE = _rule(
    'pa.assimilation_core',
    'Cluster assimilation: VRχV→VRRV, sχ→ss, Tχ→TT (χ/χʷ)',
    'Assimilation',
    _assimilation_core,
)


def _assimilation_h1(toks: list[str], ctx: Context) -> list[str]:
    if not ctx.options.get('enable-h1-cluster-assimilation', False):
        return toks
    toks = _VRHV_H1.apply(toks, ctx)
    toks = _SH_SS_H1.apply(toks, ctx)
    toks = _TH_TT_H1.apply(toks, ctx)
    return toks

_ASSIMILATION_H1 = _rule(
    'pa.assimilation_h1',
    'h₁ cluster assimilation: VRh₁V→VRRV, sh₁→ss, Th₁→TT (toggle: enable-h1-cluster-assimilation)',
    'Assimilation',
    _assimilation_h1,
)


# ── Step 5: e-lowering ────────────────────────────────────────────────────────

def _e_lower(toks: list[str], ctx: Context) -> list[str]:
    """
    e → a in three environments:
      (a) e _ R χ/χʷ
      (b) e _ {r,n} {T, #}
    """
    RN = frozenset(['r', 'n'])

    def _is_obstruent(t: str) -> bool:
        return is_consonant(t) and not is_sonorant(t)

    out = list(toks)
    for i in range(len(out)):
        if out[i] != 'e':
            continue
        rest = out[i + 1:]

        if len(rest) >= 2 and rest[0] in _RESONANTS and rest[1] in _UVULAR:
            out[i] = 'a'
            continue

        if rest and rest[0] in RN:
            after = rest[1] if len(rest) >= 2 else None
            if after is None or _is_obstruent(after) or is_boundary(after):
                out[i] = 'a'
                continue

    return out

_E_LOWER = _rule(
    'pa.e_lower',
    'e-lowering: e→a / _Rχ, _Rχʷ, _{r,n}{T,#}',
    'Vowels',
    _e_lower,
)


# ── Step 6: h₁ loss ───────────────────────────────────────────────────────────

def _h1_loss(toks: list[str], ctx: Context) -> list[str]:
    """
    eh₁ → ǣ          (special case; checked before general rule)
    Vh₁ → V̄          (V ≠ e)
    h₁ → ʔ / #_V     (toggle: enable-initial-h1-glottal-stop, default True)
    h₁ → ∅ elsewhere

    ǣ is a distinct PA output; not normalized to ē at this stage.
    """
    glottal = ctx.options.get('enable-initial-h1-glottal-stop', True)
    out: list[str] = []
    i = 0
    word_initial = True

    while i < len(toks):
        tok = toks[i]

        if tok == 'h₁':
            nxt = toks[i + 1] if i + 1 < len(toks) else None

            if out and is_vowel(out[-1]):
                # Compensatory lengthening: eh₁→ǣ, Vh₁→V̄
                if out[-1] == 'e':
                    out[-1] = 'ǣ'
                else:
                    out[-1] = lengthen(out[-1])
                if ctx.accent_index is not None and ctx.accent_index >= i:
                    ctx.accent_index -= 1
            elif glottal and word_initial and nxt and is_vowel(nxt):
                # #h₁V → ʔV (replaces h₁ in place; count unchanged)
                out.append('ˀ')
            else:
                # h₁ → ∅
                if ctx.accent_index is not None and ctx.accent_index >= i:
                    ctx.accent_index -= 1

            i += 1
            word_initial = False

        else:
            if is_boundary(tok):
                word_initial = True
            out.append(tok)
            i += 1

    return out

_H1_LOSS = _rule(
    'pa.h1_loss',
    'h₁ loss: eh₁→ǣ, Vh₁→V̄, h₁→∅ (toggle: enable-initial-h1-glottal-stop → #h₁V→ʔV)',
    'Laryngeals',
    _h1_loss,
)


# ── Step 7: Syllabic resonant repairs ────────────────────────────────────────

def _syl_res_repair(toks: list[str], ctx: Context) -> list[str]:
    """
    R̥ retained except:
      wR̥ → uR
      kʷR̥ → kuR  (net +1 token; accent_index updated)
    """
    RES = {'r̥': 'r', 'l̥': 'l', 'm̥': 'm', 'n̥': 'n'}
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None

        if tok == 'w' and nxt and nxt in RES:
            out.extend(['u', RES[nxt]])
            i += 2
        elif tok == 'kʷ' and nxt and nxt in RES:
            insert_at = len(out)
            out.extend(['k', 'u', RES[nxt]])
            if ctx.accent_index is not None and ctx.accent_index > insert_at:
                ctx.accent_index += 1
            i += 2
        else:
            out.append(tok)
            i += 1
    return out

_SYL_RES = _rule(
    'pa.syl_res',
    'Syllabic resonant repairs: wR̥→uR, kʷR̥→kuR; others retained',
    'Syllabics',
    _syl_res_repair,
)


# ── Step 8: Voiced aspirates → voiced stops ───────────────────────────────────

_ASPIRATES = _rule(
    'pa.aspirates',
    'Dʰ→D: voiced aspirates merge with voiced stops',
    'Stops',
    lambda toks, ctx: scan(toks, lambda t, i, ts: DEASPIRATE.get(t, t)),
)


# ── Step 9: Dental-yod affrication ───────────────────────────────────────────

def _ty_ts(toks: list[str], ctx: Context) -> list[str]:
    """ty → ts. Fires before prosodic voicing so ts is immune to T→D."""
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if tok == 't' and nxt in ('y', 'j'):
            out.extend(['t', 's'])
            i += 2
        else:
            out.append(tok)
            i += 1
    return out

_TY_TS = _rule('pa.ty_ts', 'ty→ts: dental-yod affrication', 'Affricates', _ty_ts)


# ── Step 10: Prosodic stop voicing (toggle, default off) ──────────────────────

def _prosodic_voice(toks: list[str], ctx: Context) -> list[str]:
    """
    T→D / prosodically weak position. Toggle: enable-prosodic-stop-voicing.
    T = {p, t, k, ḱ, kʷ}; ts, s, χ, χʷ immune.

    Coda-biased syllabification: look right for next vowel/syl_res stopping
    at any boundary. If boundary intervenes, look left. Protect only if
    nucleus == accent_index.
    """
    if not ctx.options.get('enable-prosodic-stop-voicing', False):
        return toks
    if ctx.accent_index is None:
        return toks

    accent = ctx.accent_index

    def _nucleus(i: int) -> int | None:
        for j in range(i + 1, len(toks)):
            if is_boundary(toks[j]):
                break
            if is_vowel(toks[j]) or is_syl_res(toks[j]):
                return j
        for j in range(i - 1, -1, -1):
            if is_vowel(toks[j]) or is_syl_res(toks[j]):
                return j
        return None

    out = list(toks)
    for i, tok in enumerate(toks):
        if tok not in _VOICE_TARGETS:
            continue
        if _nucleus(i) != accent:
            out[i] = _VOICE_MAP[tok]
    return out

_PROSODIC_VOICE = _rule(
    'pa.prosodic_voice',
    'T→D / prosodically weak position (toggle: enable-prosodic-stop-voicing)',
    'Voicing',
    _prosodic_voice,
    requires=['accent'],
)


# ── Pipeline ──────────────────────────────────────────────────────────────────

RULES: list[Rule] = [
    _H_REALIZE,           # 2: h₂→χ, h₃→χʷ
    _H_COLOR,             # 3: coloring
    _ASSIMILATION_CORE,   # 4a: χ/χʷ cluster assimilation (core)
    _ASSIMILATION_H1,     # 4b: h₁ cluster assimilation (toggle)
    _E_LOWER,             # 5: e-lowering
    _H1_LOSS,             # 6: h₁ loss; eh₁→ǣ, Vh₁→V̄
    _SYL_RES,             # 7: syllabic resonant repairs
    _ASPIRATES,           # 8: Dʰ→D
    _TY_TS,               # 9: ty→ts
    _PROSODIC_VOICE,      # 10: prosodic voicing (toggle)
]
