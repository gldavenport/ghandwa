"""
Token notation constants and category predicates.

The token notation system is the internal machine-working representation.
It is mostly IPA-like but not strict IPA and includes PIE-reconstructive symbols.
"""

# ── Token types ────────────────────────────────────────────────────────────────

MORPHEME_BOUNDARY = '-'
SYLLABLE_BOUNDARY = '.'

# ── Phoneme pattern list (longest-match order) ─────────────────────────────────
# Must be checked longest-first to ensure multi-character symbols are recognized
# as single tokens. Used by tokenize.py.

PHONEME_PATTERNS: list[str] = [
    # Labiovelar aspirate first (longest)
    'gʷʰ',
    # Palatal aspirate
    'ǵʰ',
    # Labiovelars (including voiceless fricative labiovelar produced by daughter devoicing)
    'gʷ', 'kʷ', 'xʷ',
    # Plain aspirates
    'gʰ', 'bʰ', 'dʰ',
    # Palatals
    'ǵ', 'ḱ',
    # Laryngeals
    'h₁', 'h₂', 'h₃',
    # Syllabic resonants
    'r̥', 'l̥', 'm̥', 'n̥',
    # Voiceless uvular fricatives (Proto-Anatolian retained laryngeals)
    'χʷ', 'χ',
    # Voiced fricatives (Ghandwa outputs)
    'ɣʷ', 'β', 'ð', 'ɣ',
    # Long vowels
    'ā', 'ē', 'ī', 'ō', 'ū', 'ǣ',
    # Nasal vowels (defined for completeness; not generated unless a rule requires)
    'ā̃', 'ē̃', 'ī̃', 'ō̃', 'ū̃',
    'ã', 'ẽ', 'ĩ', 'õ', 'ũ',
    # Other multi-char symbols
    'tː',
    # Glottal stop (laryngeal diagnostic)
    'ˀ',
    # Unspecified laryngeal (bare H; neutral, no coloring)
    'H',
]
# Single ASCII characters are handled by fallthrough in the tokenizer.

# ── Category sets ──────────────────────────────────────────────────────────────

LARYNGEALS: frozenset[str] = frozenset(['h₁', 'h₂', 'h₃', 'H'])

VOWELS: frozenset[str] = frozenset([
    'a', 'e', 'i', 'o', 'u',
    'ā', 'ē', 'ī', 'ō', 'ū', 'ǣ',
    # nasal vowels
    'ã', 'ẽ', 'ĩ', 'õ', 'ũ',
    'ā̃', 'ē̃', 'ī̃', 'ō̃', 'ū̃',
])

SHORT_VOWELS: frozenset[str] = frozenset(['a', 'e', 'i', 'o', 'u'])
LONG_VOWELS: frozenset[str] = frozenset(['ā', 'ē', 'ī', 'ō', 'ū', 'ǣ'])

SYL_RES: frozenset[str] = frozenset(['r̥', 'l̥', 'm̥', 'n̥'])

DENTALS: frozenset[str] = frozenset(['t', 'd', 'dʰ'])

PLAIN_VELARS: frozenset[str] = frozenset(['k', 'g', 'gʰ'])

LIQUIDS: frozenset[str] = frozenset(['r', 'l'])

NASALS: frozenset[str] = frozenset(['m', 'n'])

GLIDES: frozenset[str] = frozenset(['w', 'j', 'y'])

SONORANTS: frozenset[str] = frozenset(['r', 'l', 'm', 'n', 'w', 'y', 'j'])

UVULAR_FRICATIVES: frozenset[str] = frozenset(['χ', 'χʷ'])

VOICELESS_FRICATIVES: frozenset[str] = frozenset(['ɸ', 'θ', 'x', 'xʷ', 's'])

# Voiced consonants (for s→z voicing rule)
VOICED_C: frozenset[str] = frozenset([
    'b', 'd', 'g', 'gʷ', 'β', 'ð', 'ɣ', 'ɣʷ',
    'm', 'n', 'l', 'r', 'w', 'y', 'j', 'v', 'z',
])

BOUNDARIES: frozenset[str] = frozenset([MORPHEME_BOUNDARY, SYLLABLE_BOUNDARY])

# ── Helper maps ────────────────────────────────────────────────────────────────

LENGTHEN: dict[str, str] = {'a': 'ā', 'e': 'ē', 'i': 'ī', 'o': 'ō', 'u': 'ū'}
SHORTEN:  dict[str, str] = {'ā': 'a', 'ē': 'e', 'ī': 'i', 'ō': 'o', 'ū': 'u'}

# Voiced aspirate → voiceless stop
DEVOICE: dict[str, str] = {'bʰ': 'p', 'dʰ': 't', 'gʰ': 'k', 'gʷʰ': 'kʷ'}

# Voiced aspirate → plain voiced stop (deaspirate without devoicing)
DEASPIRATE: dict[str, str] = {'bʰ': 'b', 'dʰ': 'd', 'gʰ': 'g', 'gʷʰ': 'gʷ'}

NASALIZE: dict[str, str] = {
    'a': 'ã', 'e': 'ẽ', 'i': 'ĩ', 'o': 'õ', 'u': 'ũ',
    'ā': 'ā̃', 'ē': 'ē̃', 'ī': 'ī̃', 'ō': 'ō̃', 'ū': 'ū̃',
}

# ── Predicate functions ────────────────────────────────────────────────────────

def is_vowel(t: str) -> bool:
    return t in VOWELS

def is_short_vowel(t: str) -> bool:
    return t in SHORT_VOWELS

def is_long_vowel(t: str) -> bool:
    return t in LONG_VOWELS

def is_laryngeal(t: str) -> bool:
    return t in LARYNGEALS

def is_glottal(t: str) -> bool:
    return t == 'ˀ'

def is_syl_res(t: str) -> bool:
    return t in SYL_RES

def is_dental(t: str) -> bool:
    return t in DENTALS

def is_plain_velar(t: str) -> bool:
    return t in PLAIN_VELARS

def is_liquid(t: str) -> bool:
    return t in LIQUIDS

def is_nasal(t: str) -> bool:
    return t in NASALS

def is_glide(t: str) -> bool:
    return t in GLIDES

def is_sonorant(t: str) -> bool:
    return t in SONORANTS

def is_boundary(t: str) -> bool:
    return t in BOUNDARIES

def is_uvular_fricative(t: str) -> bool:
    return t in UVULAR_FRICATIVES

def is_voiceless_fricative(t: str) -> bool:
    return t in VOICELESS_FRICATIVES

def is_consonant(t: str) -> bool:
    """Any segment that is not a vowel, laryngeal, glottal stop, or boundary."""
    return not is_boundary(t) and not is_vowel(t) and not is_laryngeal(t) and t != 'ˀ'

def is_voiced(t: str) -> bool:
    """True for voiced consonants and all vowels."""
    return t in VOICED_C or is_vowel(t)

def lengthen(v: str) -> str:
    return LENGTHEN.get(v, v)

def shorten(v: str) -> str:
    return SHORTEN.get(v, v)

def nasalize(v: str) -> str:
    return NASALIZE.get(v, v)
