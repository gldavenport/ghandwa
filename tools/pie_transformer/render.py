"""
Output rendering.

Output modes:
  surface  — pipeline's language-specific display form / orthography
  ipa      — pipeline's pronunciation rendering
  tokens   — internal token notation joined for debugging

render.py is a thin dispatcher. It receives a pipeline identifier, an output mode,
and a final token stream, and calls the appropriate pipeline-specific renderer.

The `tokens` mode renderer is shared across all pipelines.

If a pipeline has no implemented surface renderer, returns 'renderer_missing'.
If a pipeline has no implemented IPA renderer, returns 'renderer_missing'.
"""

from __future__ import annotations

import unicodedata
from pie_core.tokenize import tokens_to_string
from .pipelines._common import (
    _base_form, _has_accent, _is_ipa_vowel,
    _valid_onset, _onset_split, _syllabify,
)


# ── Accent application ─────────────────────────────────────────────────────────

def apply_accent_mark(tokens: list[str], accent_index: int | None) -> list[str]:
    """
    Return a copy of tokens with U+0301 (combining acute) appended to the token
    at accent_index.  NFC-normalizes the result so precomposed forms are used
    where they exist (á, é, í, ó, ú).  No-op if accent_index is None or
    out of range.
    """
    if accent_index is None or accent_index >= len(tokens):
        return list(tokens)
    out = list(tokens)
    out[accent_index] = unicodedata.normalize('NFC', out[accent_index] + '\u0301')
    return out


# ── Tokens mode (shared) ───────────────────────────────────────────────────────

def render_tokens(tokens: list[str]) -> str:
    """Join the token stream as-is. Shared across all pipelines."""
    return tokens_to_string(tokens)


# ── Ghandwa renderers ──────────────────────────────────────────────────────────

# Ghandwa orthographic conversions from token form.
# Tokens not listed pass through unchanged.
_GH_ORTH = {
    'kʷ': 'kv',
    'gʷ': 'gv',
    'ɣʷ': 'ɣv',
    'j':  'i',
    'w':  'v',
}

# IPA tokens are identical to Ghandwa tokens except labiovelars,
# which are already in correct IPA form (kʷ, gʷ, ɣʷ).
# j is correct IPA. No conversion needed — tokens ARE the IPA.


def _ghandwa_surface(tokens: list[str]) -> str:
    """
    Ghandwa orthographic form.  Wrapped in ⟨ ⟩.
    Conversions: kʷ→kv, gʷ→gv, ɣʷ→ɣv, j→i.
    Boundary tokens stripped. ˀ preserved as diagnostic tracer.
    """
    body = ''.join(_GH_ORTH.get(t, t) for t in tokens if t not in ('-', '.'))
    return body




def _ghandwa_ipa(tokens: list[str]) -> str:
    """
    Ghandwa IPA form with syllabification and stress mark.

    - Boundary tokens stripped.
    - Onset-maximization syllabifier applied.
    - Accented token (carrying U+0301) has its acute stripped; IPA ˈ is
      placed immediately before the onset of that syllable.
    - Syllables separated by '.'.
    - Wrapped in /…/.

    Phonological (not phonetic): /n/ is written /n/ even before velars.
    """
    toks = [t for t in tokens if t not in ('-', '.')]

    if not toks:
        return '//'

    syllables = _syllabify(toks)

    # Find which syllable contains the accented token; strip the acute there.
    accent_syl: int | None = None
    accent_tok: int | None = None

    for si, syl in enumerate(syllables):
        for ti, t in enumerate(syl):
            if _has_accent(t):
                syllables[si][ti] = _base_form(t)
                accent_syl = si
                accent_tok = ti
                break
        if accent_syl is not None:
            break

    # Render syllables as strings, prefixing the stressed syllable with ˈ.
    parts: list[str] = []
    for si, syl in enumerate(syllables):
        s = ''.join(syl)
        if si == accent_syl:
            s = 'ˈ' + s
        parts.append(s)

    return '/' + '.'.join(parts) + '/'


# ── Proto-Seldanic renderers ───────────────────────────────────────────────────
# No surface/orthographic form. IPA only: tokens joined, wrapped in /…/.

def _proto_seldanic_ipa(tokens: list[str]) -> str:
    """Proto-Seldanic IPA form. Tokens joined, boundary marks stripped, wrapped in /…/."""
    body = ''.join(t for t in tokens if t not in ('-', '.'))
    return '/' + body + '/'


# ── Old Wékʷos renderers ───────────────────────────────────────────────────────

def _old_wekwos_surface(tokens: list[str]) -> str:
    """Old Wékʷos surface form. Provisional: joins tokens, strips boundary marks."""
    return ''.join(t for t in tokens if t not in ('-', '.'))


def _old_wekwos_ipa(tokens: list[str]) -> str:
    return 'renderer_missing'


# ── Neo-Wékʷos renderers ───────────────────────────────────────────────────────

def _neo_wekwos_surface(tokens: list[str]) -> str:
    """Neo-Wékʷos surface form. Provisional."""
    return ''.join(t for t in tokens if t not in ('-', '.'))


def _neo_wekwos_ipa(tokens: list[str]) -> str:
    return 'renderer_missing'


# ── Provisional renderer (shared) ────────────────────────────────────────────

def _provisional_surface(tokens: list[str]) -> str:
    """Provisional surface renderer: joins tokens, strips boundary marks.
    Used for pipelines without a designed orthography yet."""
    return ''.join(t for t in tokens if t not in ('-', '.'))


# ── Daughter A renderers ───────────────────────────────────────────────────────

_DA_ORTH: dict[str, str] = {
    'ɸ':  'f',
    'θ':  'þ',
    'x':  'h',
    'xʷ': 'hv',
    'j':  'i',
    'w':  'v',
}

def _daughter_a_surface(tokens: list[str]) -> str:
    """Daughter A orthographic surface form.
    ɸ→f, θ→þ, x→h, xʷ→hv, j→i, w→v. Boundary tokens stripped.
    kʷ/gʷ already delabialized to k/g by Stage 2A; no further conversion needed.
    """
    return ''.join(_DA_ORTH.get(t, t) for t in tokens if t not in ('-', '.'))


def _daughter_a_ipa(tokens: list[str]) -> str:
    """Daughter A IPA form. Tokens are already phonological symbols.
    Boundary tokens stripped, wrapped in /…/.
    """
    body = ''.join(t for t in tokens if t not in ('-', '.'))
    return '/' + body + '/'


# ── Daughter B renderers ───────────────────────────────────────────────────────
# Orthography inherited from Ghandwa (conservative scribal tradition).
# Surface renderer delegates to _ghandwa_surface for now; divergence expected
# as Stage 3B phonology is specified and the orth/IPA/token mapping changes.

def _daughter_b_surface(tokens: list[str]) -> str:
    """Daughter B surface form. Inherits Ghandwa orthography wholesale.
    Replace delegation when B orthography diverges from Ghandwa.
    """
    return _ghandwa_surface(tokens)


def _daughter_b_ipa(tokens: list[str]) -> str:
    """Daughter B IPA form. Provisional: tokens joined, boundary marks stripped.
    Replace with proper IPA mapping when Stage 3B phonology is committed.
    """
    body = ''.join(t for t in tokens if t not in ('-', '.'))
    return '/' + body + '/'


# ── Daughter C renderers ───────────────────────────────────────────────────────

_DC_ORTH: dict[str, str] = {
    'ʁ': 'ŕ',
    'j': 'i',
    'w': 'v',
}

def _daughter_c_surface(tokens: list[str]) -> str:
    """Daughter C orthographic surface form.
    ʁ→ŕ, j→i, w→v. Boundary tokens stripped.
    kʷ→p and gʷ→b already resolved by Stage 2C; labiovelars absent.
    β ð ɣ ɣʷ already hardened to b d g gʷ then resolved; absent at surface.
    Note: ŕ is unambiguous in C orthography — lexical acute is not used
    (stress is fixed initial); ŕ marks the rhotacism-origin rhotic only.
    """
    return ''.join(_DC_ORTH.get(t, t) for t in tokens if t not in ('-', '.'))


def _daughter_c_ipa(tokens: list[str]) -> str:
    """Daughter C IPA form. Tokens are phonological symbols; ʁ is valid IPA.
    Boundary tokens stripped, wrapped in /…/.
    """
    body = ''.join(t for t in tokens if t not in ('-', '.'))
    return '/' + body + '/'


# ── Dispatch table ─────────────────────────────────────────────────────────────

_SURFACE: dict[str, callable] = {
    'ghandwa':         _ghandwa_surface,
    'old-wekwos':      _old_wekwos_surface,
    'neo-wekwos':      _neo_wekwos_surface,
    # Provisional — orthography not yet designed; tokens rendered as-is
    'proto-anatolian':    _provisional_surface,
    'proto-seldanic':     _provisional_surface,
    'ghandwa-daughter-a': _daughter_a_surface,
    'ghandwa-daughter-b': _daughter_b_surface,
    'ghandwa-daughter-c': _daughter_c_surface,
}

_IPA: dict[str, callable] = {
    'ghandwa':            _ghandwa_ipa,
    'old-wekwos':         _old_wekwos_ipa,
    'neo-wekwos':         _neo_wekwos_ipa,
    'proto-seldanic':     _proto_seldanic_ipa,
    # Provisional — tokens are already IPA-like
    'proto-anatolian':    tokens_to_string,
    'ghandwa-daughter-a': _daughter_a_ipa,
    'ghandwa-daughter-b': _daughter_b_ipa,
    'ghandwa-daughter-c': _daughter_c_ipa,
}


# ── Main dispatch function ─────────────────────────────────────────────────────

def render(pipeline: str, mode: str, tokens: list[str],
           accent_index: int | None = None) -> str:
    """
    Render a token stream for a given pipeline and output mode.

    mode: 'surface' | 'ipa' | 'tokens'
    accent_index: if provided, the acute accent is applied to that token before rendering.
    Returns a string. Returns 'renderer_missing' if the renderer is not implemented.
    """
    accented = apply_accent_mark(tokens, accent_index)

    if mode == 'tokens':
        return render_tokens(accented)

    if mode == 'surface':
        renderer = _SURFACE.get(pipeline)
        if renderer is None:
            return 'renderer_missing'
        return renderer(accented)

    if mode == 'ipa':
        renderer = _IPA.get(pipeline)
        if renderer is None:
            return 'renderer_missing'
        result = renderer(accented)
        # Enforce /…/ wrapping uniformly regardless of renderer implementation.
        if result and result not in ('renderer_missing',):
            result = result.strip()
            if not result.startswith('/'):
                result = '/' + result
            if not result.endswith('/'):
                result = result + '/'
        return result

    return f'unknown_mode:{mode}'


def has_unresolved_laryngeal(tokens: list[str]) -> bool:
    """True if the output contains the glottal stop diagnostic marker."""
    return 'ˀ' in tokens


def get_warnings(tokens: list[str]) -> list[str]:
    """Return a list of warning strings for the output token stream."""
    warnings: list[str] = []
    if has_unresolved_laryngeal(tokens):
        warnings.append('unresolved ˀ (surviving laryngeal)')

    # Check for triple consonant cluster (CCC).
    # Glides (j, w) are excluded: post-vocalic j/w form diphthongs and
    # do not count as onset/coda consonants for cluster purposes.
    from pie_core.tokens import is_consonant, is_glottal, GLIDES
    run = 0
    for t in tokens:
        if t in ('-', '.'):
            run = 0
            continue
        if t in GLIDES:
            run = 0          # glide resets the count — treated as vocalic
            continue
        if (is_consonant(t) or is_glottal(t)):
            run += 1
            if run >= 3:
                warnings.append('CCC cluster')
                break
        else:
            run = 0

    return warnings
