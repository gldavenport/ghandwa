"""
Normalization: converts raw human input into a canonical pre-token string plus metadata.

This is not a historical transformation. It runs before tokenization.

Steps:
  1. NFC normalization (mandatory; Apple Numbers exports are NFD)
  2. Leading * removal
  3. Accent extraction (records char offset before stripping)
  4. Shorthand expansion (ASCII approximations → canonical symbols)

Note on y→j: PIE *y is the palatal glide. Some sources use 'j', some 'y'.
Normalization treats input 'y' as the palatal glide (= 'j' in this system),
consistent with the spec shorthand table. The Ghandwa Stage 2 rule documenting
the PIE *y → Ghandwa j outcome is then a linguistic note (no-op in tokens).
The character 'i̯' (i + combining inverted breve below) is also accepted.
"""

import re
import unicodedata
from dataclasses import dataclass


@dataclass
class NormalizeResult:
    """Output of normalize()."""
    clean: str           # normalized string, accent stripped, ready for tokenization
    accent_char_pos: int | None  # char offset in `clean` of the accented character; None if no accent
    had_star: bool       # True if input began with *


def normalize(raw: str) -> NormalizeResult:
    """
    Normalize a raw PIE input string.

    Returns NormalizeResult with:
      - clean: canonical string without accent diacritics, ready for tokenization
      - accent_char_pos: index in `clean` of the accented segment (or None)
      - had_star: whether the input had a leading *
    """
    # ── Step 1: NFC (mandatory first step) ────────────────────────────────────
    s = unicodedata.normalize('NFC', raw.strip())

    # ── Step 2: Strip leading * ────────────────────────────────────────────────
    had_star = s.startswith('*')
    if had_star:
        s = s[1:]

    # ── Step 3: Extract accent before stripping ────────────────────────────────
    clean, accent_char_pos = _extract_accent(s)

    # ── Step 4: Shorthand expansions ───────────────────────────────────────────
    clean = _expand_shorthands(clean)

    return NormalizeResult(clean=clean, accent_char_pos=accent_char_pos, had_star=had_star)


def _extract_accent(s: str) -> tuple[str, int | None]:
    """
    Find the first acute accent in s, record the position of the accented
    character in the resulting clean string, then return (clean, pos).

    Handles precomposed forms (á = U+00E1) and decomposed forms (a + U+0301).
    Strips acute, grave, and circumflex ONLY when they are lexical pitch accents,
    i.e. when the marked grapheme cluster is:
      - a vowel (a e i o u, upper or lower)
      - a syllabic resonant (l̥ r̥ m̥ n̥ — identified by containing U+0325)
    On consonants without U+0325 (e.g. ǵ, ḱ), combining acute marks
    palatalization and is kept as a diacritic.
    """
    nfd = unicodedata.normalize('NFD', s)

    ACCENT_MARKS = {'\u0301', '\u0300', '\u0302'}   # acute, grave, circumflex
    VOWEL_BASES  = set('aeiouAEIOU')
    SYL_RES_MARK = '\u0325'                          # combining ring below

    out_nfd: list[str] = []
    accent_base_nfd_pos: int | None = None  # position in out_nfd of accented base char

    i = 0
    while i < len(nfd):
        ch = nfd[i]
        if ch in ACCENT_MARKS:
            # Find the most recent combining-class-0 base char
            base_pos = len(out_nfd) - 1
            while base_pos >= 0 and unicodedata.combining(out_nfd[base_pos]) != 0:
                base_pos -= 1
            base_ch = out_nfd[base_pos] if base_pos >= 0 else None
            # Check whether the grapheme cluster is a vowel or syllabic resonant
            cluster = out_nfd[base_pos:] if base_pos >= 0 else []
            is_lexical = (base_ch in VOWEL_BASES) or (SYL_RES_MARK in cluster)
            if is_lexical:
                if accent_base_nfd_pos is None:
                    accent_base_nfd_pos = base_pos
                i += 1
                continue
            # Palatalization diacritic — keep it
            out_nfd.append(ch)
            i += 1
            continue
        out_nfd.append(ch)
        i += 1

    clean_nfc = unicodedata.normalize('NFC', ''.join(out_nfd))

    if accent_base_nfd_pos is None:
        return clean_nfc, None

    # Map NFD base position → NFC position.
    prefix_nfc = unicodedata.normalize('NFC', ''.join(out_nfd[:accent_base_nfd_pos]))
    accent_nfc_pos = len(prefix_nfc)

    return clean_nfc, accent_nfc_pos


def _expand_shorthands(s: str) -> str:
    """
    Expand ASCII/shorthand notations to canonical token-notation symbols.
    Order matters: longer patterns must be substituted before shorter substrings.
    """
    # Long vowels (colon notation)
    s = s.replace('a:', 'ā').replace('e:', 'ē').replace('i:', 'ī') \
         .replace('o:', 'ō').replace('u:', 'ū')

    # Laryngeals — order: H3/h3 before H2/h2 before H1/h1 to avoid partial matches
    # Also handle subscript digit variants
    s = re.sub(r'[Hh]3|[Hh]₃', 'h₃', s)
    s = re.sub(r'[Hh]2(?![₃3])|[Hh]₂', 'h₂', s)
    s = re.sub(r'[Hh]1(?![₂₃23])|[Hh]₁', 'h₁', s)
    # Bare H (unspecified laryngeal) left as-is if not caught above

    # Labiovelar aspirate — must precede gw and gh
    s = re.sub(r'gʷh|gwh', 'gʷʰ', s)
    s = re.sub(r"g[´'`]h", 'ǵʰ', s)

    # gh — must precede g alone; avoid matching h₁ etc.
    s = re.sub(r'gh(?![₁₂₃123])', 'gʰ', s)
    s = s.replace('bh', 'bʰ').replace('dh', 'dʰ')

    # Palatals
    s = re.sub(r"g[´'`](?!ʰ)", 'ǵ', s)
    s = re.sub(r"k[´'`]", 'ḱ', s)

    # Labiovelars
    s = s.replace('kw', 'kʷ')
    s = re.sub(r'gw(?!ʰ)', 'gʷ', s)

    # Syllabic resonants (underscore notation)
    s = s.replace('r_', 'r̥').replace('l_', 'l̥') \
         .replace('m_', 'm̥').replace('n_', 'n̥')

    # Palatal glide: i̯ (i + combining inverted breve below U+032F) and bare y
    # y is treated as the PIE palatal glide (= j in this system's orthography)
    s = s.replace('i\u032f', 'j')
    s = s.replace('y', 'j')

    return s


def strip_crlf(field: str) -> str:
    """Strip Windows carriage return from a TSV field. Use in tsv_io.py."""
    return field.rstrip('\r')
