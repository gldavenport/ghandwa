#!/usr/bin/env python3
"""
PIE Derivational Generator — Primary Derivations.

Takes a PIE verbal root and generates primary derivations (operating directly on
the root or an ablaut grade of it). PIE forms only. See tools/docs/pie_deriver.md.

Secondary derivations (operating on primary outputs) are deferred; the
screen/markdown output prints a deferred placeholder for them.

Shared primitives come from pie_core (normalize, tokenize, token inventory). This
tool does not depend on pie_transformer.

Usage:
    python3 tools/derive.py ROOT [--zero Z] [--lengthened L] [--gloss G]
                            [--reduplication B] [--nasal-infix B] [--export]
"""

from __future__ import annotations

import os
import argparse
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

from pie_core.normalize import normalize
from pie_core.tokenize import tokenize, tokens_to_string
from pie_core.tokens import (
    LIQUIDS, NASALS, GLIDES, SYL_RES, VOWELS,
    is_vowel, is_syl_res,
)

ACUTE = '\u0301'

# Zero-grade resolution maps (spec §3.2 / §3.5)
_SYLLABIFY = {'r': 'r̥', 'l': 'l̥', 'm': 'm̥', 'n': 'n̥'}   # liquids/nasals → syllabic
_VOCALIZE  = {'w': 'u', 'y': 'i', 'j': 'i'}               # glides → vowel


# ── Accent helpers ────────────────────────────────────────────────────────────

def _base(t: str) -> str:
    """Strip a combining acute (U+0301) from a token; leave other diacritics."""
    nfd = unicodedata.normalize('NFD', t)
    return unicodedata.normalize('NFC', ''.join(c for c in nfd if c != ACUTE))


def _is_nucleus(t: str) -> bool:
    """A token that can bear the accent: a vowel or a syllabic resonant."""
    b = _base(t)
    return b in VOWELS or b in SYL_RES


def _accent(tok: str) -> str:
    """Apply the combining acute to a token; NFC so precomposed forms are used."""
    return unicodedata.normalize('NFC', _base(tok) + ACUTE)


def _place_root_accent(tokens: list[str], root_len: int) -> int | None:
    """Accent the (last) nucleus within the root portion tokens[:root_len].
    Returns the accented index, or None if the root has no nucleus."""
    for i in range(root_len - 1, -1, -1):
        if _is_nucleus(tokens[i]):
            tokens[i] = _accent(tokens[i])
            return i
    return None


def _place_suffix_accent(tokens: list[str], root_len: int) -> int | None:
    """Accent the first nucleus in the suffix portion tokens[root_len:]."""
    for i in range(root_len, len(tokens)):
        if _is_nucleus(tokens[i]):
            tokens[i] = _accent(tokens[i])
            return i
    return None


# ── PIE display ────────────────────────────────────────────────────────────────

def _pie(tokens: list[str]) -> str:
    """Render tokens as a PIE citation string: drop boundary marks; the internal
    palatal glide token j is shown as PIE y (the consonantal glide). Vocalized
    glides are already 'i'/'u'. Wrapped by caller in *…*."""
    body = ''.join(t for t in tokens if t not in ('-', '.'))
    return body.replace('j', 'y')


def _pie_stem(tokens: list[str]) -> str:
    """Stem display: like _pie but with a trailing morpheme hyphen."""
    return _pie(tokens) + '-'


# ── Root + ablaut grades (spec §3.1, §3.2) ────────────────────────────────────

@dataclass
class Root:
    raw: str
    egrade: list[str]                      # root tokens, boundary stripped
    e_count: int
    ograde: list[str] | None = None
    zerograde: list[str] | None = None
    zero_reason: str | None = None         # why zero grade is unavailable
    lengthened: list[str] | None = None
    notes: list[str] = field(default_factory=list)

    @property
    def onset(self) -> list[str]:
        """Leading consonant tokens before the first nucleus (the root's onset)."""
        out: list[str] = []
        for t in self.egrade:
            if _is_nucleus(t):
                break
            out.append(t)
        return out


def build_root(raw: str, zero_override: str | None, leng_override: str | None) -> Root:
    norm = normalize(raw)
    tokens, _ = tokenize(norm.clean)
    egrade = [t for t in tokens if t not in ('-', '.')]
    e_idxs = [i for i, t in enumerate(egrade) if t == 'e']
    e_count = len(e_idxs)

    r = Root(raw=raw, egrade=egrade, e_count=e_count)

    if e_count != 1:
        r.notes.append('ambiguous root vowel — supply e-grade '
                       '(o/zero/lengthened grades unavailable)')
        # Only e-grade-as-supplied patterns can fire.
    else:
        ei = e_idxs[0]
        r.ograde     = egrade[:ei] + ['o'] + egrade[ei + 1:]
        r.lengthened = egrade[:ei] + ['ē'] + egrade[ei + 1:]
        r.zerograde, r.zero_reason = _zero_grade(egrade, ei)

    # Overrides win outright (spec §3.2).
    if zero_override:
        zt, _ = tokenize(normalize(zero_override).clean)
        r.zerograde = [t for t in zt if t not in ('-', '.')]
        r.zero_reason = None
    if leng_override:
        lt, _ = tokenize(normalize(leng_override).clean)
        r.lengthened = [t for t in lt if t not in ('-', '.')]

    return r


def _zero_grade(egrade: list[str], ei: int) -> tuple[list[str] | None, str | None]:
    """Sonority-based zero grade (spec §3.2). Operates on the post-deletion
    token sequence. Right-of-site (offglide / post-vocalic resonant) takes
    priority; an onset-cluster resonant before the site syllabifies only when
    the right neighbour is not itself a nucleus candidate.

    Returns (tokens, None) on success, or (None, reason) if it must be flagged.
    """
    toks = egrade[:ei] + egrade[ei + 1:]
    # After deletion the two segments flanking the old vowel are:
    #   left  = toks[ei-1]   (was immediately before e)
    #   right = toks[ei]     (was immediately after e)
    left  = toks[ei - 1] if ei - 1 >= 0 else None
    right = toks[ei]     if ei < len(toks) else None

    def syllabify_or_vocalize(seg: str) -> str:
        if seg in GLIDES:
            return _VOCALIZE[seg]
        return _SYLLABIFY[seg]          # liquid or nasal

    # Priority 1: the post-vocalic segment (offglide / coda resonant).
    if right is not None and (right in GLIDES or right in LIQUIDS or right in NASALS):
        toks[ei] = syllabify_or_vocalize(right)
        return toks, None

    # Priority 2: no nucleus candidate to the right → an onset-cluster resonant
    # immediately before the site syllabifies (e.g. *ǵneh₃- → *ǵn̥h₃-).
    if left is not None and (left in GLIDES or left in LIQUIDS or left in NASALS):
        toks[ei - 1] = syllabify_or_vocalize(left)
        return toks, None

    # Priority 3: no resonant/glide adjacent → bare consonant cluster is the zero
    # grade (e.g. *sed- → *sd-). Valid; not flagged.
    return toks, None


# ── Reduplication & nasal infix (spec §3.3, §3.4) ─────────────────────────────

def reduplicant(root: Root, vowel: str) -> tuple[list[str] | None, str | None]:
    """Return ([C₁, vowel], None) or (None, reason). vowel is 'i' (present) or
    'e' (perfect). Predictable only when the onset is a single atomic consonant
    (not a laryngeal, not an s+C cluster, not a multi-consonant cluster)."""
    if not root.egrade:
        return None, 'empty root'
    first = root.egrade[0]
    if first in {'h₁', 'h₂', 'h₃', 'H'}:
        return None, 'laryngeal onset colours the reduplication vowel'
    onset = root.onset
    if len(onset) >= 2:
        if onset[0] == 's':
            return None, 's+C onset — copy ambiguous (s-mobile)'
        return None, 'complex onset — copy ambiguous'
    return [first, vowel], None


def nasal_infix(zerograde: list[str] | None) -> tuple[list[str] | None, str | None]:
    """Insert né before the final coda consonant of the zero grade (strong stem).
    Predictable only when a single atomic consonant follows the nucleus."""
    if zerograde is None:
        return None, 'zero grade unavailable'
    # Find the nucleus, then the consonants after it.
    nuc = next((i for i, t in enumerate(zerograde) if _is_nucleus(t)), None)
    if nuc is None:
        return None, 'no nucleus in zero grade'
    coda = zerograde[nuc + 1:]
    if len(coda) == 0:
        return None, 'no coda consonant to host the infix'
    if len(coda) > 1:
        return None, 'complex coda — infix site ambiguous'
    # Insert n + é before the single final consonant.
    out = zerograde[:nuc + 1] + ['n', 'é'] + coda
    return out, None


# ── Built-form container ──────────────────────────────────────────────────────

@dataclass
class Built:
    label: str
    accent_type: str
    citation: list[str] | None = None      # accented tokens
    stem: list[str] | None = None          # accented tokens (display adds '-')
    secondary: str | None = None           # e.g. 'obl. *deh₃-tór-*'
    note: str | None = None
    skip: str | None = None                # if set, pattern could not generate


# ── Generic builders ──────────────────────────────────────────────────────────

def _grade_tokens(root: Root, grade: str) -> tuple[list[str] | None, str | None]:
    if grade == 'e':
        return list(root.egrade), None
    if grade == 'o':
        return (list(root.ograde), None) if root.ograde else (None, 'o-grade unavailable')
    if grade == 'zero':
        if root.zerograde is None:
            return None, (root.zero_reason or 'zero grade unavailable')
        return list(root.zerograde), None
    if grade == 'leng':
        return (list(root.lengthened), None) if root.lengthened else (None, 'lengthened grade unavailable')
    raise ValueError(grade)


def affix(root: Root, label: str, grade: str, suffix: list[str], accent: str,
          stem_trim: int = 0, note: str | None = None) -> Built:
    """Build grade + suffix, place accent ('root'|'suffix'), derive stem by
    trimming `stem_trim` tokens from the end of the citation."""
    g, reason = _grade_tokens(root, grade)
    if g is None:
        return Built(label, accent, skip=reason)
    root_len = len(g)
    toks = g + list(suffix)
    if accent == 'root':
        if _place_root_accent(toks, root_len) is None:
            # zero grade with no nucleus (bare cluster) — accent the suffix instead
            _place_suffix_accent(toks, root_len)
    elif accent == 'suffix':
        if _place_suffix_accent(toks, root_len) is None:
            _place_root_accent(toks, root_len)
    stem = toks[:len(toks) - stem_trim] if stem_trim else list(toks)
    return Built(label, accent, citation=toks, stem=stem, note=note)


# ── Primary derivation registry ─────────────────────────────────────────────
# Each builder returns a Built (or a list of Built for `variable` patterns that
# emit two accent variants).

def tier1(root: Root, redup_override: str | None,
          nasal_override: str | None) -> list[Built]:
    out: list[Built] = []
    A = lambda *a, **k: out.append(affix(root, *a, **k))

    # ── Verbal: presents ───────────────────────────────────────────────────
    # RootPres (mobile): sg onset-é-coda-ti / pl onset-∅-coda-énti
    rp = affix(root, 'RootPres', 'e', ['t', 'i'], 'root')
    if rp.skip is None and root.zerograde is not None:
        pl = affix(root, 'RootPres', 'zero', ['e', 'n', 't', 'i'], 'suffix')
        if pl.citation:
            rp.secondary = '3pl. *' + _pie(pl.citation) + '*'
    out.append(rp)

    # ThemPres: onset-é-coda-e-ti (root accent), stem = …-e-
    A('ThemPres', 'e', ['e', 't', 'i'], 'root', stem_trim=2)

    # RedupPres: C₁i- + é-grade root + ti (root accent)
    out.append(_redup_present(root, redup_override))

    # NasalPres: zero grade + né infix + ti (suffix accent on infix é)
    out.append(_nasal_present(root, nasal_override))

    # NasalSuf: zero grade + néw + ti (suffix accent); weak …-nu-énti noted
    ns = affix(root, 'NasalSuf', 'zero', ['n', 'e', 'w', 't', 'i'], 'suffix', stem_trim=2)
    if ns.citation and root.zerograde is not None:
        # Weak stem: zero root + -nu- + stressed ending -énti.
        weak_tokens = list(root.zerograde) + ['n', 'u', _accent('e'), 'n', 't', 'i']
        ns.secondary = 'weak *' + _pie(weak_tokens) + '*'
    out.append(ns)

    # SkePres / YePres: zero grade + suffix (suffix accent)
    A('SkePres', 'zero', ['s', 'ḱ', 'e', 't', 'i'], 'suffix', stem_trim=2)
    A('YePres',  'zero', ['j', 'e', 't', 'i'],      'suffix', stem_trim=2)

    # CausIter: o-grade + éye-ti (suffix accent)
    A('CausIter', 'o', ['e', 'j', 'e', 't', 'i'], 'suffix', stem_trim=2)

    # Perfect: C₁e- + ó-grade root + e (root accent)
    out.append(_perfect(root, redup_override))

    # ── Verbal: aorists ────────────────────────────────────────────────────
    A('RootAor', 'e',    ['t'],      'root')           # onset-é-coda-t (3sg)
    A('SigAor',  'leng', ['s', 't'], 'root')           # lengthened-s-t (3sg)

    # ── Root nouns ─────────────────────────────────────────────────────────
    A('RootNounAcro', 'e', [], 'root')
    rnm = affix(root, 'RootNounMob', 'e', ['s'], 'root', stem_trim=1)   # nom.sg -s
    if rnm.citation:
        obl = affix(root, 'RootNounMob', 'zero', ['e', 's'], 'suffix')
        if obl.citation:
            rnm.secondary = 'obl. *' + _pie_stem(obl.citation) + '*'
    out.append(rnm)

    # ── Thematic nouns ─────────────────────────────────────────────────────
    A('ThemNounR',  'o',    ['o', 's'], 'root',   stem_trim=1)   # *bʰóros, stem *bʰóro-
    A('ThemNounS',  'o',    ['o', 's'], 'suffix', stem_trim=1)   # *bʰorós
    A('ThemNounZR', 'zero', ['o', 's'], 'root',   stem_trim=1)
    A('ThemNounZS', 'zero', ['o', 's'], 'suffix', stem_trim=1)

    # ── Verbal adjectives / state adjectives ───────────────────────────────
    A('VerbAdjTo', 'zero', ['t', 'o', 's'], 'suffix', stem_trim=1)
    A('VerbAdjNo', 'zero', ['n', 'o', 's'], 'suffix', stem_trim=1)
    A('AdjRo',     'zero', ['r', 'o', 's'], 'suffix', stem_trim=1)
    A('AdjLo',     'e',    ['l', 'o', 's'], 'suffix', stem_trim=1,
      note='grade root-specific; e-grade assumed')

    # ── Action nouns ───────────────────────────────────────────────────────
    A('ActNounTi', 'zero', ['t', 'i', 's'], 'suffix', stem_trim=1)
    A('ActNounTu', 'zero', ['t', 'u', 's'], 'suffix', stem_trim=1)

    # ── m-stem cluster (Yates; handoff) ────────────────────────────────────
    # MenNounR: é-grade root + -mn̥ (root accent, fixed root stress)
    A('MenNounR', 'e', ['m', 'n̥'], 'root')
    # MonNounPrim: zero grade + -món- (suffix accent)
    A('MonNounPrim', 'zero', ['m', 'o', 'n'], 'suffix')
    # MenNounAnim: é-grade root + -mōn (mobile; strong stem-final stress on ō)
    mna = affix(root, 'MenNounAnim', 'e', ['m', 'ō', 'n'], 'suffix')
    if mna.citation:
        # Weak stem is é-grade root + -mn-, with stress on the case ending
        # (Yates). -mn- has no nucleus, so the stem itself is left unaccented.
        weak_tokens = list(root.egrade) + ['m', 'n']
        mna.secondary = 'weak *' + _pie_stem(weak_tokens) + '* (ending-stressed)'
    out.append(mna)

    # ── Agent nouns ────────────────────────────────────────────────────────
    ae = affix(root, 'AgentNounE', 'e', ['t', 'ō', 'r'], 'root')   # *bʰértōr
    if ae.citation:
        obl = affix(root, 'AgentNounE', 'e', ['t', 'o', 'r'], 'suffix')
        if obl.citation:
            ae.secondary = 'obl. *' + _pie_stem(obl.citation) + '*'
    out.append(ae)
    A('AgentNounR', 'zero', ['t', 'ē', 'r'], 'suffix')             # *…tḗr

    # ── s-stem ─────────────────────────────────────────────────────────────
    out.append(_sstem(root))

    # ── u-/i-stems ─────────────────────────────────────────────────────────
    A('UStemC', 'zero', ['u', 's'], 'suffix', stem_trim=1)
    A('UStemM', 'zero', ['u', 's'], 'root',   stem_trim=1)
    out.extend(_variable(root, 'IStem', 'e', ['i', 's'], stem_trim=1))

    # ── Primary feminine event/result noun ─────────────────────────────────
    A('FemEventNoun', 'o', ['e', 'h₂'], 'suffix')                  # o-grade + -éh₂

    # ── Instrument / thematic suffix nouns (variable: two accent variants) ──
    out.extend(_variable(root, 'InstrNounTro', 'e', ['t', 'r', 'o', 'm'], stem_trim=1,
                         note='grade root-specific; e-grade assumed'))
    out.extend(_variable(root, 'InstrNounTlo', 'e', ['t', 'l', 'o', 'm'], stem_trim=1,
                         note='grade root-specific; e-grade assumed'))
    out.extend(_variable(root, 'LoNoun', 'e', ['l', 'o', 's'], stem_trim=1,
                         note='grade root-specific; e-grade assumed'))
    out.extend(_variable(root, 'MoNoun', 'e', ['m', 'o', 's'], stem_trim=1,
                         note='grade root-specific; e-grade assumed'))
    out.extend(_variable(root, 'NoNoun', 'e', ['n', 'o', 's'], stem_trim=1,
                         note='grade root-specific; e-grade assumed'))

    return out


def _variable(root: Root, label: str, grade: str, suffix: list[str],
              stem_trim: int = 0, note: str | None = None) -> list[Built]:
    """`variable` accent_type: emit a root-accent and a suffix-accent row."""
    r = affix(root, label, grade, suffix, 'root', stem_trim=stem_trim, note=note)
    s = affix(root, label, grade, suffix, 'suffix', stem_trim=stem_trim, note=note)
    if r.skip:
        return [r]
    r.accent_type = 'variable (root-accent)'
    s.accent_type = 'variable (suffix-accent)'
    return [r, s]


def _redup_present(root: Root, override: str | None) -> Built:
    if override:
        ot, _ = tokenize(normalize(override).clean)
        toks = [t for t in ot if t not in ('-', '.')]
        _place_root_accent(toks, len(toks))
        return Built('RedupPres', 'root', citation=toks, stem=toks)
    redup, reason = reduplicant(root, 'i')
    if redup is None:
        return Built('RedupPres', 'root', skip=reason)
    toks = redup + list(root.egrade) + ['t', 'i']
    # Accent the root nucleus (after the reduplicant).
    root_lo = len(redup)
    for i in range(root_lo + len(root.egrade) - 1, root_lo - 1, -1):
        if _is_nucleus(toks[i]):
            toks[i] = _accent(toks[i])
            break
    return Built('RedupPres', 'root', citation=toks, stem=toks[:-2])


def _perfect(root: Root, override: str | None) -> Built:
    redup, reason = reduplicant(root, 'e')
    if redup is None and override is None:
        return Built('Perfect', 'root', skip=reason)
    if root.ograde is None:
        return Built('Perfect', 'root', skip='o-grade unavailable')
    if override:
        ot, _ = tokenize(normalize(override).clean)
        redup = [t for t in ot if t not in ('-', '.')]
    toks = list(redup) + list(root.ograde) + ['e']
    root_lo = len(redup)
    for i in range(root_lo + len(root.ograde) - 1, root_lo - 1, -1):
        if _is_nucleus(toks[i]):
            toks[i] = _accent(toks[i])
            break
    return Built('Perfect', 'root', citation=toks, stem=toks[:-1])


def _nasal_present(root: Root, override: str | None) -> Built:
    if override:
        ot, _ = tokenize(normalize(override).clean)
        base = [t for t in ot if t not in ('-', '.')]
        toks = base + ['t', 'i']
        _place_suffix_accent(toks, 0) or _place_root_accent(toks, len(toks))
        return Built('NasalPres', 'suffix', citation=toks, stem=base)
    infixed, reason = nasal_infix(root.zerograde)
    if infixed is None:
        return Built('NasalPres', 'suffix', skip=reason)
    # Accent the infixed é.
    toks = list(infixed) + ['t', 'i']
    for i, t in enumerate(toks):
        if t == 'é':
            break
    else:
        i = None
    if i is not None:
        toks[i] = _accent('e')   # already 'é'; normalise
    return Built('NasalPres', 'suffix', citation=toks, stem=list(infixed))


def _sstem(root: Root) -> Built:
    g, reason = _grade_tokens(root, 'e')
    if g is None:
        return Built('SStem', 'root', skip=reason)
    toks = g + ['e', 's']
    _place_root_accent(toks, len(g))
    # s-stem cites the bare oblique stem with a trailing hyphen.
    return Built('SStem', 'root', citation=toks, stem=toks)


# ── Output ────────────────────────────────────────────────────────────────────

def load_functions() -> dict[str, str]:
    path = Path(__file__).resolve().parent / 'pie_core' / 'derivation-functions.tsv'
    funcs: dict[str, str] = {}
    if path.exists():
        for line in path.read_text(encoding='utf-8').splitlines()[1:]:
            if '\t' in line:
                label, fn = line.split('\t', 1)
                funcs[label.strip()] = fn.strip()
    return funcs


def _chain(gloss: str | None, func: str) -> str:
    if gloss:
        return f'"{gloss}" → [{func}]'
    return f'[{func}]'


def _display_len(s: str) -> int:
    """Character count excluding zero-width combining marks (e.g. combining acute)."""
    return sum(1 for c in s if unicodedata.category(c) != 'Mn')


def _ljust(s: str, width: int) -> str:
    """Left-justify s to display width, accounting for combining marks."""
    pad = max(0, width - _display_len(s))
    return s + ' ' * pad


def _render_row(b: Built, funcs: dict[str, str], gloss: str | None,
               form_width: int = 22) -> str:
    func = funcs.get(b.label, b.label)
    # For variable patterns two rows share the same label; append accent qualifier.
    if b.accent_type.startswith('variable'):
        qualifier = 'root-accent' if 'root' in b.accent_type else 'suffix-accent'
        display_label = f'{func} ({qualifier})'
    else:
        display_label = func
    if b.skip:
        return f'  {display_label}   (skipped: {b.skip})'
    if b.label == 'SStem' or (b.citation and b.citation[-1] in ('-',)):
        form = _pie_stem(b.citation)
    else:
        form = _pie(b.citation)
    line = f'  {_ljust(form, form_width)}   {display_label}'
    if gloss:
        line += f'   "{gloss}"'
    tail = []
    if b.secondary:
        tail.append(b.secondary)
    if b.note:
        tail.append(f'({b.note})')
    if tail:
        line += '   ' + '; '.join(tail)
    return line


def _grades_line(root: Root) -> str:
    parts = []
    if root.zerograde is not None:
        parts.append('zero *' + _pie_stem(root.zerograde) + '*')
    elif root.zero_reason:
        parts.append('zero —')
    if root.ograde:
        parts.append('o-grade *' + _pie_stem(root.ograde) + '*')
    if root.lengthened:
        parts.append('lengthened *' + _pie_stem(root.lengthened) + '*')
    grades = ('  (' + '  '.join(parts) + ')') if parts else ''
    return f'ROOT: *{_pie_stem(root.egrade)}*{grades}'


_POS_GROUP: dict[str, str] = {
    'RootPres':  'Verbs', 'ThemPres':  'Verbs', 'RedupPres': 'Verbs',
    'NasalPres': 'Verbs', 'NasalSuf':  'Verbs', 'SkePres':   'Verbs',
    'YePres':    'Verbs', 'CausIter':  'Verbs', 'Perfect':   'Verbs',
    'RootAor':   'Verbs', 'SigAor':    'Verbs',
    'VerbAdjTo': 'Adjectives', 'VerbAdjNo': 'Adjectives',
    'AdjRo':     'Adjectives', 'AdjLo':     'Adjectives',
    'UStemC':    'Adjectives',
}  # everything else → 'Nouns'
_GROUP_ORDER = ['Verbs', 'Adjectives', 'Nouns']


def render_screen(root: Root, built: list[Built], funcs: dict[str, str],
                  gloss: str | None) -> str:
    lines: list[str] = []
    head = _grades_line(root)
    if gloss:
        head += f'   gloss: "{gloss}"'
    lines.append(head)
    for n in root.notes:
        lines.append(f'  ⚠ {n}')
    lines.append('')
    lines.append('# Primary Derivations')
    groups: dict[str, list[Built]] = {g: [] for g in _GROUP_ORDER}
    for b in built:
        groups[_POS_GROUP.get(b.label, 'Nouns')].append(b)
    # Compute form column width from all non-skipped forms.
    form_width = max(
        (_display_len(_pie_stem(b.citation) if (b.label == 'SStem' or
            (b.citation and b.citation[-1] in ('-',))) else _pie(b.citation))
         for b in built if not b.skip and b.citation),
        default=20,
    )
    for group in _GROUP_ORDER:
        members = groups[group]
        if not members:
            continue
        lines.append('')
        lines.append(f'## {group}')
        lines.append('')
        for b in members:
            lines.append(_render_row(b, funcs, gloss, form_width))
    lines.append('')
    lines.append('# Secondary Derivations')
    lines.append('')
    lines.append('  (deferred)')
    return '\n'.join(lines)


def _sanitize(egrade: list[str]) -> str:
    s = _pie(egrade)
    repl = {'ʰ': 'h', 'ʷ': 'w', 'ǵ': "g'", 'ḱ': "k'", 'ē': 'e:', 'ō': 'o:',
            'ī': 'i:', 'ā': 'a:', 'ū': 'u:', 'h₁': 'h1', 'h₂': 'h2', 'h₃': 'h3'}
    for k, v in repl.items():
        s = s.replace(k, v)
    nfd = unicodedata.normalize('NFD', s)
    out = []
    for c in nfd:
        if c == '\u0325':            # combining ring below (syllabic)
            out.append('0')
        elif c == '\u0301':          # acute — drop in filenames
            continue
        elif ord(c) < 128:
            out.append(c)
        # else: drop other non-ASCII
    return unicodedata.normalize('NFC', ''.join(out)) or 'root'


def render_markdown(root: Root, built: list[Built], funcs: dict[str, str],
                    gloss: str | None, datestamp: str) -> str:
    lines: list[str] = []
    lines.append(f'# Derivata — *{_pie_stem(root.egrade)}*'
                 + (f' "{gloss}"' if gloss else ''))
    lines.append('')
    lines.append(f'_generated {datestamp}_')
    lines.append('')
    lines.append('Grades: ' + _grades_line(root).replace('ROOT: ', ''))
    for n in root.notes:
        lines.append(f'> ⚠ {n}')
    lines.append('')
    lines.append('## Primary Derivations')
    lines.append('')
    lines.append('| Label | Form | Accent | Function | Notes |')
    lines.append('|-------|------|--------|----------|-------|')
    for b in built:
        func = funcs.get(b.label, b.label)
        if b.skip:
            lines.append(f'| {b.label} | — | {b.accent_type} | {func} | skipped: {b.skip} |')
            continue
        if b.label == 'SStem':
            form = '*' + _pie_stem(b.citation) + '*'
        else:
            form = '*' + _pie(b.citation) + '*'
        notes = '; '.join(x for x in (b.secondary, b.note) if x)
        lines.append(f'| {b.label} | {form} | {b.accent_type} | {func} | {notes} |')
    lines.append('')
    lines.append('## Secondary Derivations')
    lines.append('')
    lines.append('_Deferred — see derive-spec.md §5._')
    lines.append('')
    return '\n'.join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog='pie_deriver.py',
        description='PIE derivation generator — primary derivations (see tools/docs/pie_deriver/pie_deriver.md).',
    )
    p.add_argument('root', help='e-grade root, e.g. "bʰer-" (shorthand ok: bher-, g\'neh3-)')
    p.add_argument('--zero', help='zero-grade override')
    p.add_argument('--lengthened', help='lengthened-grade override')
    p.add_argument('--gloss', help='root gloss in English, e.g. "carry"')
    p.add_argument('--reduplication', help='reduplicated base override')
    p.add_argument('--nasal-infix', dest='nasal_infix', help='nasal-infix base override')
    p.add_argument('--export', action='store_true',
                   help='write markdown to lexicon/derivata/{egrade}-derivata.md')
    args = p.parse_args(argv)

    root = build_root(args.root, args.zero, args.lengthened)
    built = tier1(root, args.reduplication, args.nasal_infix)
    funcs = load_functions()

    os.system('clear')
    print(render_screen(root, built, funcs, args.gloss))

    if args.export:
        from datetime import date
        datestamp = date.today().isoformat()
        md = render_markdown(root, built, funcs, args.gloss, datestamp)
        out_dir = Path('lexicon') / 'derivata'
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f'{_sanitize(root.egrade)}-derivata.md'
        out_path.write_text(md, encoding='utf-8')
        print(f'\nMarkdown written to {out_path}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
