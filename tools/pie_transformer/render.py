"""
Output rendering.

Three output tiers:
  orth      — orthographic form (attested/constructed languages only; None for proto-languages)
  citation  — conventional scholarly shorthand derivable from tokens; universal
              proto-language reconstructions prefixed with *
  ipa       — syllabified phonological IPA with stress mark; universal
  tokens    — raw token join for debugging; universal

render.py is a thin dispatcher. It receives a pipeline identifier, a mode,
and a final token stream, and calls the appropriate renderer.

Returns str | None. None signals that the requested tier is absent for this pipeline
(e.g. orth for a proto-language). Callers should display '—' for None.
"""

from __future__ import annotations

import unicodedata
from pie_core.tokenize import tokens_to_string
from .pipelines._common import (
    _base_form, _has_accent, _is_ipa_vowel,
    _valid_onset, _onset_split, _syllabify,
)
from .pipeline import PIPELINE_IS_RECONSTRUCTION


# ── Accent application ─────────────────────────────────────────────────────────

def apply_accent_mark(tokens: list[str], accent_index: int | None) -> list[str]:
    """
    Return a copy of tokens with U+0301 (combining acute) appended to the token
    at accent_index. NFC-normalizes so precomposed forms are used (á, é, í, ó, ú).
    No-op if accent_index is None or out of range.
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


# ── Shared IPA renderer ────────────────────────────────────────────────────────

def _ipa_syllabified(tokens: list[str]) -> str:
    """Shared IPA renderer: onset-maximization syllabification with ˈ stress mark.

    Used by all pipelines whose token stream is phonologically interpretable as-is.
    Boundary tokens stripped. Accent mark (U+0301) must already be applied to the
    relevant token before calling (via apply_accent_mark in render()).

    - Syllables separated by '.'.
    - Stressed syllable prefixed with ˈ.
    - Wrapped in /…/.
    - Phonological, not phonetic (/n/ before velars stays /n/, etc.).
    """
    toks = [t for t in tokens if t not in ('-', '.')]
    if not toks:
        return '//'
    syllables = _syllabify(toks)
    accent_syl: int | None = None
    for si, syl in enumerate(syllables):
        for ti, t in enumerate(syl):
            if _has_accent(t):
                syllables[si][ti] = _base_form(t)
                accent_syl = si
                break
        if accent_syl is not None:
            break
    parts: list[str] = []
    for si, syl in enumerate(syllables):
        s = ''.join(syl)
        if si == accent_syl:
            s = 'ˈ' + s
        parts.append(s)
    return '/' + '.'.join(parts) + '/'


# ── Shared citation renderer ───────────────────────────────────────────────────

# Labiovelar digraph substitutions for citation form.
# Boundary tokens stripped; everything else passes through unchanged.
_CIT_SUBS: dict[str, str] = {
    'kʷ': 'kw',
    'gʷ': 'gw',
    'ɣʷ': 'ɣw',
}


def _citation_render(tokens: list[str], star: bool) -> str:
    """Shared citation renderer.

    Converts labiovelars to digraphs (kʷ→kw, gʷ→gw, ɣʷ→ɣw).
    Everything else — β, ð, ɣ, j, w, all vowels — passes through unchanged.
    Prepends * for reconstructions. Boundary tokens stripped.
    """
    body = ''.join(_CIT_SUBS.get(t, t) for t in tokens if t not in ('-', '.'))
    return ('*' if star else '') + body


# ── Ghandwa orthographic renderer ─────────────────────────────────────────────

_GH_ORTH: dict[str, str] = {
    'kʷ': 'kv',
    'gʷ': 'gv',
    'ɣʷ': 'ɣv',
    'j':  'i',
    'w':  'v',
}


def _ghandwa_orth(tokens: list[str]) -> str:
    """Ghandwa orthographic form.
    Conversions: kʷ→kv, gʷ→gv, ɣʷ→ɣv, j→i, w→v.
    Boundary tokens stripped. ˀ preserved as diagnostic tracer.
    """
    return ''.join(_GH_ORTH.get(t, t) for t in tokens if t not in ('-', '.'))


def _ghandwa_ipa(tokens: list[str]) -> str:
    """Ghandwa IPA form. Delegates to shared syllabifier."""
    return _ipa_syllabified(tokens)


# ── Proto-Seldanic IPA ─────────────────────────────────────────────────────────

def _proto_seldanic_ipa(tokens: list[str]) -> str:
    """Proto-Seldanic IPA form."""
    return _ipa_syllabified(tokens)


# ── Wékʷos IPA ────────────────────────────────────────────────────────────────

def _wekwos_old_ipa(tokens: list[str]) -> str:
    """Wékʷos-Old IPA form."""
    return _ipa_syllabified(tokens)


def _wekwos_neo_ipa(tokens: list[str]) -> str:
    """Wékʷos-Neo IPA form."""
    return _ipa_syllabified(tokens)


# ── Daughter A ─────────────────────────────────────────────────────────────────

_DA_ORTH: dict[str, str] = {
    'ɸ':  'f',
    'θ':  'þ',
    'x':  'h',
    'xʷ': 'hv',
    'j':  'i',
    'w':  'v',
}


def _daughter_a_orth(tokens: list[str]) -> str:
    """Daughter A orthographic form.
    ɸ→f, θ→þ, x→h, xʷ→hv, j→i, w→v. Boundary tokens stripped.
    """
    return ''.join(_DA_ORTH.get(t, t) for t in tokens if t not in ('-', '.'))


def _daughter_a_ipa(tokens: list[str]) -> str:
    """Daughter A IPA form."""
    return _ipa_syllabified(tokens)


# ── Daughter B ─────────────────────────────────────────────────────────────────

def _daughter_b_orth(tokens: list[str]) -> str:
    """Daughter B orthographic form. Inherits Ghandwa orthography wholesale."""
    return _ghandwa_orth(tokens)


def _daughter_b_ipa(tokens: list[str]) -> str:
    """Daughter B IPA form. Provisional."""
    return _ipa_syllabified(tokens)


# ── Daughter C ─────────────────────────────────────────────────────────────────

_DC_ORTH: dict[str, str] = {
    'ʁ': 'ŕ',
    'j': 'i',
    'w': 'v',
}


def _daughter_c_orth(tokens: list[str]) -> str:
    """Daughter C orthographic form.
    ʁ→ŕ, j→i, w→v. Boundary tokens stripped.
    kʷ→p and gʷ→b resolved by Stage 2C; β ð ɣ ɣʷ hardened and resolved.
    """
    return ''.join(_DC_ORTH.get(t, t) for t in tokens if t not in ('-', '.'))


def _daughter_c_ipa(tokens: list[str]) -> str:
    """Daughter C IPA form. ʁ is valid IPA; treated as plain consonant by syllabifier."""
    return _ipa_syllabified(tokens)


# ── Dispatch tables ────────────────────────────────────────────────────────────

# Only attested/constructed languages with a designed script.
# Proto-languages are absent; render() returns None for them in orth mode.
_ORTH: dict[str, callable] = {
    'ghandwa':            _ghandwa_orth,
    'ghandwa-daughter-a': _daughter_a_orth,
    'ghandwa-daughter-b': _daughter_b_orth,
    'ghandwa-daughter-c': _daughter_c_orth,
}

# Citation is universal — handled by _citation_render() with PIPELINE_IS_RECONSTRUCTION.
# No dispatch table needed.

_IPA: dict[str, callable] = {
    'ghandwa':            _ghandwa_ipa,
    'wekwos-old':         _wekwos_old_ipa,
    'wekwos-neo':         _wekwos_neo_ipa,
    'proto-seldanic':     _proto_seldanic_ipa,
    # Provisional — syllabification unverified for proto-anatolian
    'proto-anatolian':    tokens_to_string,
    'ghandwa-daughter-a': _daughter_a_ipa,
    'ghandwa-daughter-b': _daughter_b_ipa,
    'ghandwa-daughter-c': _daughter_c_ipa,
}


# ── Main dispatch function ─────────────────────────────────────────────────────

def render(
    pipeline: str,
    mode: str,
    tokens: list[str],
    accent_index: int | None = None,
    star: bool | None = None,
) -> str | None:
    """
    Render a token stream for a given pipeline and output mode.

    mode: 'orth' | 'citation' | 'ipa' | 'tokens'

    accent_index: if provided, acute accent applied to that token before rendering.

    star: for citation mode — True prefixes *, False omits it, None uses
          PIPELINE_IS_RECONSTRUCTION[pipeline] (default behaviour).

    Returns str | None. None means the tier is absent for this pipeline
    (currently only orth for proto-languages). Callers display '—' for None.
    """
    accented = apply_accent_mark(tokens, accent_index)

    if mode == 'tokens':
        return render_tokens(accented)

    if mode == 'orth':
        renderer = _ORTH.get(pipeline)
        if renderer is None:
            return None
        return renderer(accented)

    if mode == 'citation':
        use_star = PIPELINE_IS_RECONSTRUCTION.get(pipeline, True) if star is None else star
        return _citation_render(accented, use_star)

    if mode == 'ipa':
        renderer = _IPA.get(pipeline)
        if renderer is None:
            return None
        result = renderer(accented)
        if result and result != 'renderer_missing':
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

    from pie_core.tokens import is_consonant, is_glottal, GLIDES
    run = 0
    for t in tokens:
        if t in ('-', '.'):
            run = 0
            continue
        if t in GLIDES:
            run = 0
            continue
        if is_consonant(t) or is_glottal(t):
            run += 1
            if run >= 3:
                warnings.append('CCC cluster')
                break
        else:
            run = 0

    return warnings
