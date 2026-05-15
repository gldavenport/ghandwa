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
from .tokenize import tokens_to_string


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
    Ghandwa IPA form.  Wrapped in /…/.
    Tokens are already IPA symbols; only boundaries are stripped.
    """
    body = ''.join(t for t in tokens if t not in ('-', '.'))
    return f'/{body}/'


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


# ── Dispatch table ─────────────────────────────────────────────────────────────

_SURFACE: dict[str, callable] = {
    'ghandwa':    _ghandwa_surface,
    'old-wekwos': _old_wekwos_surface,
    'neo-wekwos': _neo_wekwos_surface,
}

_IPA: dict[str, callable] = {
    'ghandwa':    _ghandwa_ipa,
    'old-wekwos': _old_wekwos_ipa,
    'neo-wekwos': _neo_wekwos_ipa,
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
        return renderer(accented)

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
    from .tokens import is_consonant, is_glottal, GLIDES
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
