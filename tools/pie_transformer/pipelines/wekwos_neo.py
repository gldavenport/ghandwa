"""
Wékʷos-Neo historical pipeline.

Status: PROVISIONAL. The Wékʷos-Neo rule list is unstable and likely to change.
All test cases for this pipeline should be marked provisional.

Wékʷos-Neo is downstream of Wékʷos-Old. Its input token stream comes from
the final output of the Wékʷos-Old pipeline (pipeline chaining via pipeline.py).
Re-tokenization does not occur; the token stream passes directly.

Ported from tools/pie-transformer.jsx (WK_NEO).
"""

from ..rule import Rule, Context, scan
from pie_core.tokens import (
    SHORTEN, is_vowel, is_nasal, is_liquid, is_consonant, is_long_vowel,
    shorten, nasalize,
)
from ._common import make_rule as _rule


# ── Syllabification helper (for final-syllable shortening) ───────────────────

def _get_last_nucleus_range(toks: list[str]) -> tuple[int, int] | None:
    """
    Find the start and end indices of the last nucleus (vowel or diphthong).
    Returns (start, end) or None if no vowel found.
    """
    GLIDES = frozenset(['w', 'j', 'y'])
    nuclei: list[tuple[int, int]] = []
    i = 0
    while i < len(toks):
        t = toks[i]
        if is_long_vowel(t):
            nuclei.append((i, i)); i += 1
        elif is_vowel(t):
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            after_nxt = toks[i + 2] if i + 2 < len(toks) else None
            is_diph = (nxt and nxt in GLIDES and
                       (not after_nxt or is_consonant(after_nxt)))
            if is_diph:
                nuclei.append((i, i + 1)); i += 2
            else:
                nuclei.append((i, i)); i += 1
        else:
            i += 1
    return nuclei[-1] if nuclei else None


def _is_polysyllabic(toks: list[str]) -> bool:
    """True if the token stream has at least two nuclei."""
    count = 0
    i = 0
    GLIDES = frozenset(['w', 'j', 'y'])
    while i < len(toks):
        t = toks[i]
        if is_long_vowel(t):
            count += 1; i += 1
        elif is_vowel(t):
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            after_nxt = toks[i + 2] if i + 2 < len(toks) else None
            is_diph = (nxt and nxt in GLIDES and
                       (not after_nxt or is_consonant(after_nxt)))
            count += 1
            i += 2 if is_diph else 1
        else:
            i += 1
        if count >= 2:
            return True
    return False


# ── Rules ─────────────────────────────────────────────────────────────────────

# 4.1: Barytonesis — stress retracts to initial syllable
# No token-level change; feeds 4.4 by demoting final-syllable prominence.
_BARYTONESIS = _rule(
    'nwk.41', 'Neo 4.1: Barytonesis — stress retracts to initial syllable', 'Prosody',
    lambda toks, ctx: toks,  # no-op on token stream
)

# Initial x+liquid+vowel → k+liquid+vowel
def _x_liquid(toks, ctx):
    """Neo: #xLV → #kLV — initial laryngeal residue fortifies before liquid+vowel."""
    if (len(toks) >= 3 and toks[0] == 'x' and
            is_liquid(toks[1]) and is_vowel(toks[2])):
        return ['k'] + toks[1:]
    return toks

_X_LV = _rule('nwk.xlv', 'Neo: #xLV → #kLV — initial laryngeal residue fortifies', 'Laryngeals', _x_liquid)

# #wlV and #mlV → #blV
def _wl_ml_initial(toks, ctx):
    """Neo: #wlV and #mlV → #blV — initial w/m before liquid+vowel → b."""
    if (len(toks) >= 3 and toks[0] in ('w', 'm') and
            is_liquid(toks[1]) and is_vowel(toks[2])):
        return ['b'] + toks[1:]
    return toks

_WL_ML_INIT = _rule('nwk.wlml', 'Neo: #wlV/#mlV → #blV — initial w/m before liquid+vowel → b', 'Consonants', _wl_ml_initial)

# 4.2: Collapse of homorganic diphthongs
def _homorganic_collapse(toks, ctx):
    """Neo 4.2: ey/ej → ī, ow → ū."""
    out = []; i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if tok == 'e' and nxt in ('j', 'y'):
            out.append('ī'); i += 2
        elif tok == 'o' and nxt == 'w':
            out.append('ū'); i += 2
        else:
            out.append(tok); i += 1
    return out

_HOMO_COLLAPSE = _rule('nwk.42', 'Neo 4.2: ey/ej→ī, ow→ū — homorganic diphthong collapse', 'Vowels', _homorganic_collapse)

# 4.3: Harmonization of heterorganic diphthongs
def _hetero_harmonize(toks, ctx):
    """Neo 4.3: ew → ow, oy/oj → ey."""
    out = []; i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if tok == 'e' and nxt == 'w':
            out.extend(['o', 'w']); i += 2
        elif tok == 'o' and nxt in ('j', 'y'):
            out.extend(['e', 'j']); i += 2
        else:
            out.append(tok); i += 1
    return out

_HETERO_HARM = _rule('nwk.43', 'Neo 4.3: ew→ow, oy→ey — heterorganic diphthong harmonization', 'Vowels', _hetero_harmonize)

# 4.4: Long vowels in final syllable shorten (polysyllables only)
def _final_shorten(toks, ctx):
    """Neo 4.4: Long vowels in final syllable shorten (polysyllables only)."""
    if not _is_polysyllabic(toks):
        return toks
    last = _get_last_nucleus_range(toks)
    if last is None:
        return toks
    out = list(toks)
    start, end = last
    for i in range(start, end + 1):
        if out[i] in SHORTEN:
            out[i] = shorten(out[i])
    return out

_FINAL_SHORTEN = _rule('nwk.44', 'Neo 4.4: Long vowels in final syllable shorten (polysyllables)', 'Vowels', _final_shorten)

# 4.5: o → a (short only)
_O_A = _rule(
    'nwk.45', 'Neo 4.5: o→a — short o merges with a', 'Vowels',
    lambda toks, ctx: scan(toks, lambda t, i, ts: 'a' if t == 'o' else t)
)

# 10.3: s → z between V/R and V/R (ordered after o→a)
def _s_voice(toks, ctx):
    """Neo 10.3: s → z / {V,R}_{V,R}."""
    def vr(t):
        return t is not None and (is_vowel(t) or is_nasal(t) or is_liquid(t))
    return scan(toks, lambda tok, i, ts: (
        'z' if tok == 's' and vr(ts[i - 1] if i > 0 else None) and vr(ts[i + 1] if i + 1 < len(ts) else None)
        else tok
    ))

_S_VOICE = _rule('nwk.103', 'Neo 10.3: s→z / V_V — intervocalic voicing', 'Fricatives', _s_voice)

# 10.4: VN# → Ṽ# — final nasal nasalizes preceding vowel, nasal drops
def _final_nasal_drop(toks, ctx):
    """Neo 10.4: VN# → Ṽ# — final nasal nasalizes preceding vowel, nasal drops."""
    if len(toks) < 2:
        return toks
    last = toks[-1]
    if not is_nasal(last):
        return toks
    prev = toks[-2]
    if not is_vowel(prev):
        return toks
    nas = nasalize(prev)
    if nas == prev:
        return toks
    return list(toks[:-2]) + [nas]

_NASAL_DROP = _rule('nwk.104', 'Neo 10.4: VN# → Ṽ# — final nasal nasalizes vowel and drops', 'Nasals', _final_nasal_drop)

# 11.1: Word-final obstruent voicing
def _final_voice(toks, ctx):
    """Neo 11.1: p,t,k,kʷ,s → b,d,g,gʷ,z word-finally."""
    VF = {'p': 'b', 't': 'd', 'k': 'g', 'kʷ': 'gʷ', 's': 'z'}
    if not toks:
        return toks
    out = list(toks)
    if out[-1] in VF:
        out[-1] = VF[out[-1]]
    return out

_FINAL_VOICE = _rule('nwk.111', 'Neo 11.1: word-final obstruent voicing p/t/k/kʷ/s → b/d/g/gʷ/z', 'Consonants', _final_voice)

# 11.2: Kʷ → K — labiovelar delabialization
_KW_DEL = _rule(
    'nwk.112', 'Neo 11.2: Kʷ→K — labiovelar delabialization', 'Consonants',
    lambda toks, ctx: scan(toks, lambda t, i, ts:
        'k' if t == 'kʷ' else 'g' if t == 'gʷ' else t)
)

# 11.3: l → r / _# — final lateral rhotacism
def _final_rhotacism(toks, ctx):
    """Neo 11.3: l → r word-finally."""
    if not toks:
        return toks
    out = list(toks)
    if out[-1] == 'l':
        out[-1] = 'r'
    return out

_FINAL_RHOT = _rule('nwk.113', 'Neo 11.3: l→r / _# — final lateral rhotacism', 'Consonants', _final_rhotacism)


# ── Pipeline ──────────────────────────────────────────────────────────────────

RULES: list[Rule] = [
    _BARYTONESIS,
    _X_LV,
    _HOMO_COLLAPSE,
    _HETERO_HARM,
    _FINAL_SHORTEN,
    _O_A,
    _S_VOICE,
    _NASAL_DROP,
    _FINAL_VOICE,
    _WL_ML_INIT,
    _KW_DEL,
    _FINAL_RHOT,
]
