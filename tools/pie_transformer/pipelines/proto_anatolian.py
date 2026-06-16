"""
Proto-Anatolian historical pipeline.

Rule ordering follows PIE → Proto-Anatolian sound changes v0.8:

  1.  Palatal-velar merger: ḱ→k, ǵ→g, ǵʰ→gʰ.                             [pa.1.1]
        (toggle: enable-centum-merger, default False)
        Whether this merger occurred at PA stage or later (Hittite-specific)
        is contested. Default: palatovelars pass through unchanged.
  2.  Accent preserved; mobile paradigms inherited.
  3.  Laryngeal realization: h₂→H₂ or χ, h₃→H₃ or χʷ; h₁ retained. [pa.2.1]
        (toggle: enable-laryngeal-realization, default False → abstract H₂/H₃)
  4.  Laryngeal coloring: H₂/χ → a-color, H₃/χʷ → o-color. [pa.3.1]
        Works in both abstract and concrete mode.
  5.  Laryngeal-cluster assimilation (individually togglable):
        VRχV, VRχʷV → VRRV  (toggle: enable-vrhv-assimilation, default True)  [pa.4.1]
        sχ, sχʷ → ss         (toggle: enable-sh-assimilation,   default False) [pa.4.2]
        Tχ, Tχʷ → TT        (toggle: enable-th-assimilation,   default False) [pa.4.3]
      h₁ cluster assimilation (toggle: enable-h1-cluster-assimilation, default False): [pa.4.4]
        VRh₁V → VRRV; sh₁ → ss; Th₁ → TT
  6.  e-lowering: e→a / _Rχ, _Rχʷ, _{r,n}{T,#}
        (toggle: enable-e-lowering, default False)                              [pa.5.1]
  7.  h₁ loss and compensatory lengthening:                                    [pa.6.1]
        eh₁ → ǣ  (special case, fires before general rule)
        Vh₁ → V̄
        h₁ → ∅ elsewhere
      Toggle: enable-initial-h1-glottal-stop (default False)
        h₁ → ʔ / #_V
  8.  Syllabic resonants:                                                       [pa.7.1]
        Default mode: R̥ preserved abstractly.
          wR̥ → uR    (toggle: enable-w-syl-repair,  default True)
          kʷR̥ → kuR  (toggle: enable-kw-syl-repair, default True)
        Full-vocalization mode (toggle: enable-syllabic-vocalization, default False):
          r̥→ar, l̥→al, m̥→am, n̥→an (supersedes specific repairs when active)
  9.  Voiced aspirates merge with voiced stops: Dʰ→D.                         [pa.8.1]
        Also catches gʰ produced by centum merger (step 1 ǵʰ→gʰ→g here).
  10. Dental-yod affrication: ty→ts.                                           [pa.9.1]
  11. Prosodic stop voicing (toggle; default False):                           [pa.10.1]
        T→D / prosodically weak position.
        T = {p, t, k, ḱ, kʷ} (ḱ merged to k only when enable-centum-merger is on); ts, s, χ, χʷ immune.
      Toggle: enable-prosodic-stop-voicing

Context options (pass via Context.options dict):
  enable-laryngeal-realization    bool  default False
  enable-centum-merger             bool  default False
  enable-vrhv-assimilation         bool  default True
  enable-sh-assimilation           bool  default False
  enable-th-assimilation           bool  default False
  enable-h1-cluster-assimilation   bool  default False
  enable-e-lowering                bool  default False
  enable-initial-h1-glottal-stop   bool  default False   [changed from True in v0.7]
  enable-w-syl-repair              bool  default True
  enable-kw-syl-repair             bool  default True
  enable-syllabic-vocalization     bool  default False
  enable-prosodic-stop-voicing     bool  default False

Notes:
  - H₂/H₃ are the default output for h₂/h₃ (abstract mode). Set
    enable-laryngeal-realization=True for χ/χʷ concrete output.
    Laryngeal coloring and cluster assimilation operate on both representations.
  - ǣ is a distinct PA output symbol; daughter rules decide its fate.
  - enable-initial-h1-glottal-stop changed to default False (was True in v0.7).
    Initial h₁→ʔ is a phonological interpretation (Kloekhorst-like profile),
    not a base PIE→PA sound change.
  - Tχ→TT and sχ→ss default False (was mandatory in v0.7 as part of
    ASSIMILATION_CORE). VRχV→VRRV kept default True (Sturtevant-type;
    better-attested as a PA-level change).
  - e-lowering default False (was mandatory in v0.7).
  - enable-centum-merger default False: palatovelar → plain velar merger is
    attested in Hittite but may be Hittite-specific rather than PA-level. The
    PA branching likely predates the centum-satem isogloss. Enable for profiles
    committed to the merger (e.g. a Hittite-like output).
  - Missing base rules (tracked for future implementation): diphthong outcomes,
    PIE *o/*a treatment, final-position behavior, initial *y/*w behavior,
    long-vowel normalization, abstract H₂/H₃ layer. Current code passes these
    through unchanged (abstract preservation by default).
  - Step 10 (ty→ts) must precede step 11 (T→D): ts is immune to prosodic voicing.
  - Prosodic voicing uses coda-biased syllabification: look right for next
    vowel stopping at any boundary; if boundary intervenes, look left.
    A consonant is protected only if its syllable nucleus == accent_index.
"""

from __future__ import annotations

from ..rule import Rule, Context, scan
from pie_core.tokens import (
    SHORTEN, LENGTHEN, DEASPIRATE,
    is_vowel, is_laryngeal, is_syl_res, is_dental, is_consonant,
    is_sonorant, is_boundary, is_nasal, is_liquid,
    lengthen, shorten,
)
from ._common import make_rule as _rule


# ── Category helpers ──────────────────────────────────────────────────────────

# ḱ included: if enable-centum-merger is off, ḱ may still be present at step 11.
# Prosodic voicing of ḱ → ǵ is unlikely to be PA-appropriate, but it is
# included here for completeness; the toggle keeps it off by default anyway.
_VOICE_TARGETS: frozenset[str] = frozenset(['p', 't', 'k', 'ḱ', 'kʷ'])
_VOICE_MAP: dict[str, str] = {'p': 'b', 't': 'd', 'k': 'g', 'ḱ': 'ǵ', 'kʷ': 'gʷ'}

_RESONANTS: frozenset[str] = frozenset(['r', 'l', 'm', 'n', 'w', 'y', 'j',
                                         'r̥', 'l̥', 'm̥', 'n̥'])

_H2_TYPE: frozenset[str] = frozenset(['χ', 'H₂'])   # h₂-type: a-coloring
_H3_TYPE: frozenset[str] = frozenset(['χʷ', 'H₃'])  # h₃-type: o-coloring
_UVULAR:  frozenset[str] = _H2_TYPE | _H3_TYPE      # all post-h₁ laryngeals, abstract or concrete

_SYL_RES_MAP: dict[str, str] = {'r̥': 'r', 'l̥': 'l', 'm̥': 'm', 'n̥': 'n'}


# ── Step 1: Palatal-velar merger (toggle) ────────────────────────────────────

_CENTUM_MAP: dict[str, str] = {
    'ḱ':  'k',
    'ǵ':  'g',
    'ǵʰ': 'gʰ',  # loses palatalization; gʰ then caught by step 9 (Dʰ→D) → g
}

def _centum_merger(toks: list[str], ctx: Context) -> list[str]:
    """
    ḱ→k, ǵ→g, ǵʰ→gʰ. Toggle: enable-centum-merger (default False).
    When off, palatovelars pass through unchanged (abstract preservation).
    When on, merges with plain velars; gʰ then caught by step 9 Dʰ→D.
    """
    if not ctx.options.get('enable-centum-merger', False):
        return toks
    return [_CENTUM_MAP.get(t, t) for t in toks]

_CENTUM = _rule(
    'pa.1.1',
    'Palatal-velar merger: ḱ→k, ǵ→g, ǵʰ→gʰ (toggle: enable-centum-merger)',
    'Dorsals',
    _centum_merger,
)


# ── Step 2: Laryngeal realization ─────────────────────────────────────────────

def _h_realize(toks: list[str], ctx: Context) -> list[str]:
    """
    Abstract mode (enable-laryngeal-realization=False, default): h₂→H₂, h₃→H₃.
    Concrete mode (enable-laryngeal-realization=True):           h₂→χ,  h₃→χʷ.
    h₁ unchanged in both modes.
    """
    concrete = ctx.options.get('enable-laryngeal-realization', False)
    out = []
    for tok in toks:
        if tok == 'h₂':
            out.append('χ' if concrete else 'H₂')
        elif tok == 'h₃':
            out.append('χʷ' if concrete else 'H₃')
        else:
            out.append(tok)
    return out

_H_REALIZE = _rule(
    'pa.2.1',
    'Laryngeal realization: h₂→H₂/χ, h₃→H₃/χʷ (toggle: enable-laryngeal-realization)',
    'Laryngeals',
    _h_realize,
)


# ── Step 3: Laryngeal coloring ────────────────────────────────────────────────

def _h_color(toks: list[str], ctx: Context) -> list[str]:
    """
    H₂-type (H₂ or χ) colors adjacent e → a.
    H₃-type (H₃ or χʷ) colors adjacent e → o.
    Works in both abstract and concrete mode.
    Forward pass: laryngeal colors following e.
    Backward pass: laryngeal colors preceding e.
    """
    t = list(toks)

    def _target(h: str) -> str:
        return 'a' if h in _H2_TYPE else 'o'

    for i in range(len(t) - 1):
        if t[i] in _UVULAR and t[i + 1] == 'e':
            t[i + 1] = _target(t[i])

    for i in range(len(t) - 1, 0, -1):
        if t[i] in _UVULAR and t[i - 1] == 'e':
            t[i - 1] = _target(t[i])

    return t

_H_COLOR = _rule(
    'pa.3.1',
    'Laryngeal coloring: H₂/χ→a-color, H₃/χʷ→o-color (works in abstract and concrete mode)',
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


def _assimilation_vrhv(toks: list[str], ctx: Context) -> list[str]:
    if not ctx.options.get('enable-vrhv-assimilation', True):
        return toks
    return _VRHV_CORE.apply(toks, ctx)

_ASSIMILATION_VRHV = _rule(
    'pa.4.1',
    'VRχV→VRRV: resonant-laryngeal assimilation (toggle: enable-vrhv-assimilation)',
    'Assimilation',
    _assimilation_vrhv,
)


def _assimilation_sh(toks: list[str], ctx: Context) -> list[str]:
    if not ctx.options.get('enable-sh-assimilation', False):
        return toks
    return _SH_SS_CORE.apply(toks, ctx)

_ASSIMILATION_SH = _rule(
    'pa.4.2',
    'sχ→ss: sibilant-laryngeal assimilation (toggle: enable-sh-assimilation)',
    'Assimilation',
    _assimilation_sh,
)


def _assimilation_th(toks: list[str], ctx: Context) -> list[str]:
    if not ctx.options.get('enable-th-assimilation', False):
        return toks
    return _TH_TT_CORE.apply(toks, ctx)

_ASSIMILATION_TH = _rule(
    'pa.4.3',
    'Tχ→TT: obstruent-laryngeal assimilation (toggle: enable-th-assimilation)',
    'Assimilation',
    _assimilation_th,
)


def _assimilation_h1(toks: list[str], ctx: Context) -> list[str]:
    if not ctx.options.get('enable-h1-cluster-assimilation', False):
        return toks
    toks = _VRHV_H1.apply(toks, ctx)
    toks = _SH_SS_H1.apply(toks, ctx)
    toks = _TH_TT_H1.apply(toks, ctx)
    return toks

_ASSIMILATION_H1 = _rule(
    'pa.4.4',
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
    Toggle: enable-e-lowering (default False).
    Not mandatory base: environment-conditioning is contested for Common PA.
    """
    if not ctx.options.get('enable-e-lowering', False):
        return toks

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
    'pa.5.1',
    'e-lowering: e→a / _Rχ, _Rχʷ, _{r,n}{T,#} (toggle: enable-e-lowering)',
    'Vowels',
    _e_lower,
)


# ── Step 6: h₁ loss ───────────────────────────────────────────────────────────

def _h1_loss(toks: list[str], ctx: Context) -> list[str]:
    """
    eh₁ → ǣ          (special case; checked before general rule)
    Vh₁ → V̄          (V ≠ e)
    h₁ → ʔ / #_V     (toggle: enable-initial-h1-glottal-stop, default False)
    h₁ → ∅ elsewhere

    ǣ is a distinct PA output; not normalized to ē at this stage.
    Default changed False (was True in v0.7): initial h₁→ʔ is phonological
    interpretation (Kloekhorst-like profile), not a base PIE→PA sound change.
    """
    glottal = ctx.options.get('enable-initial-h1-glottal-stop', False)
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
    'pa.6.1',
    'h₁ loss: eh₁→ǣ, Vh₁→V̄, h₁→∅ (toggle: enable-initial-h1-glottal-stop → #h₁V→ʔV)',
    'Laryngeals',
    _h1_loss,
)


# ── Step 7: Syllabic resonants ────────────────────────────────────────────────

def _syl_res_handler(toks: list[str], ctx: Context) -> list[str]:
    """
    Three modes, checked in priority order:

    1. enable-syllabic-vocalization (default False):
         r̥→ar, l̥→al, m̥→am, n̥→an. Full PA-level vocalization; supersedes
         specific repairs below. Accent moves to inserted 'a' if accent was
         on R̥; shifts right by one for each R̥ expanded before it.

    2. Specific repairs (default mode):
         wR̥ → uR   (toggle: enable-w-syl-repair,  default True)
         kʷR̥ → kuR (toggle: enable-kw-syl-repair, default True)
         All other R̥ preserved abstractly.

    Accent index updated for all token-count changes.
    """
    if ctx.options.get('enable-syllabic-vocalization', False):
        # Full vocalization: each R̥ expands to two tokens ('a' + consonant).
        out: list[str] = []
        shift = 0
        new_accent: int | None = None
        for j, tok in enumerate(toks):
            if tok in _SYL_RES_MAP:
                if ctx.accent_index is not None:
                    if j == ctx.accent_index:
                        new_accent = len(out)   # accent on inserted 'a'
                    elif j < ctx.accent_index:
                        shift += 1
                out.append('a')
                out.append(_SYL_RES_MAP[tok])
            else:
                out.append(tok)
        if ctx.accent_index is not None:
            ctx.accent_index = (
                new_accent if new_accent is not None
                else ctx.accent_index + shift
            )
        return out

    # Default: specific context-repairs only.
    w_repair  = ctx.options.get('enable-w-syl-repair',  True)
    kw_repair = ctx.options.get('enable-kw-syl-repair', True)
    out = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None

        if w_repair and tok == 'w' and nxt and nxt in _SYL_RES_MAP:
            out.extend(['u', _SYL_RES_MAP[nxt]])
            i += 2
        elif kw_repair and tok == 'kʷ' and nxt and nxt in _SYL_RES_MAP:
            insert_at = len(out)
            out.extend(['k', 'u', _SYL_RES_MAP[nxt]])
            if ctx.accent_index is not None and ctx.accent_index > insert_at:
                ctx.accent_index += 1
            i += 2
        else:
            out.append(tok)
            i += 1
    return out

_SYL_RES = _rule(
    'pa.7.1',
    'Syllabic resonants: wR̥→uR (enable-w-syl-repair), kʷR̥→kuR (enable-kw-syl-repair), '
    'full vocalization r̥→ar etc. (enable-syllabic-vocalization)',
    'Syllabics',
    _syl_res_handler,
)


# ── Step 8: Voiced aspirates → voiced stops ───────────────────────────────────

_ASPIRATES = _rule(
    'pa.8.1',
    'Dʰ→D: voiced aspirates merge with voiced stops (catches gʰ from centum step pa.1.1)',
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

_TY_TS = _rule('pa.9.1', 'ty→ts: dental-yod affrication', 'Affricates', _ty_ts)


# ── Step 10: Prosodic stop voicing (toggle, default off) ──────────────────────

def _prosodic_voice(toks: list[str], ctx: Context) -> list[str]:
    """
    T→D / prosodically weak position. Toggle: enable-prosodic-stop-voicing.
    T = {p, t, k, ḱ, kʷ} (ḱ merged to k only when enable-centum-merger is on); ts, s, χ, χʷ immune.

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
    'pa.10.1',
    'T→D / prosodically weak position (toggle: enable-prosodic-stop-voicing)',
    'Voicing',
    _prosodic_voice,
    requires=['accent'],
)


# ── Pipeline ──────────────────────────────────────────────────────────────────

RULES: list[Rule] = [
    _CENTUM,              # 1:  ḱ→k, ǵ→g, ǵʰ→gʰ  (toggle: enable-centum-merger, default False)
    _H_REALIZE,           # 2:  h₂→χ, h₃→χʷ
    _H_COLOR,             # 3:  laryngeal coloring
    _ASSIMILATION_VRHV,   # 4a: VRχV→VRRV (toggle: enable-vrhv-assimilation, default True)
    _ASSIMILATION_SH,     # 4b: sχ→ss    (toggle: enable-sh-assimilation,   default False)
    _ASSIMILATION_TH,     # 4c: Tχ→TT    (toggle: enable-th-assimilation,   default False)
    _ASSIMILATION_H1,     # 4d: h₁ cluster assimilation (toggle: enable-h1-cluster-assimilation)
    _E_LOWER,             # 5:  e-lowering (toggle: enable-e-lowering, default False)
    _H1_LOSS,             # 6:  h₁ loss; eh₁→ǣ, Vh₁→V̄
    _SYL_RES,             # 7:  syllabic resonant handling
    _ASPIRATES,           # 8:  Dʰ→D (catches gʰ from step 1 when enable-centum-merger is on)
    _TY_TS,               # 9:  ty→ts
    _PROSODIC_VOICE,      # 10: prosodic voicing (toggle: enable-prosodic-stop-voicing)
]
