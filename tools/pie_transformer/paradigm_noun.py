"""
Noun paradigm generator for Ghandwa.

Supported stem classes (auto-detected from nom.sg + gen.sg pair):
  a_stem    — ā-stem (feminine)
  o_stem_m  — o-stem (masculine)
  o_stem_n  — o-stem (neuter)
  i_stem    — i-stem
  u_stem_mf — u-stem (masculine/feminine)
  u_stem_n  — u-stem (neuter)
  s_stem    — s-stem (neuter)

Detection is unambiguous for all seven classes from the (nom.sg, gen.sg) pair.
Use stem_class_override to force a class when auto-detection fails.

Accent note: accent is fixed from the nom.sg form. Mobile accent alternations
(e.g. hysterokinetic r/n-stems) are not modeled. Deferred stem classes (r, n/men,
r/n heteroclite, root nouns) are not yet implemented.

Source of truth: grammar/paradigms-nominal.md
"""

from __future__ import annotations
import unicodedata

CASES = ['nom', 'voc', 'acc', 'gen', 'dat', 'ins', 'loc']
NUMBERS = ['sg', 'pl']
GAP = '—'


# ── Paradigm tables ────────────────────────────────────────────────────────────
# dict[(case, number)] = (orth_ending, ipa_ending)
# Endings are relative to the nom-stem (nom.sg with nom ending stripped).
# GAP = not yet established in paradigms-nominal.md.

_A_STEM: dict[tuple[str, str], tuple[str, str]] = {
    ('nom', 'sg'): ('ā',    'aː'),
    ('voc', 'sg'): ('a',    'a'),
    ('acc', 'sg'): ('ām',   'aːm'),
    ('gen', 'sg'): ('ās',   'aːs'),
    ('dat', 'sg'): ('āi',   'aːj'),
    ('ins', 'sg'): ('ā',    'aː'),
    ('loc', 'sg'): ('āi',   'aːj'),
    ('nom', 'pl'): ('ās',   'aːs'),
    ('voc', 'pl'): ('ās',   'aːs'),
    ('acc', 'pl'): ('āns',  'aːns'),
    ('gen', 'pl'): ('ām',   'aːm'),
    ('dat', 'pl'): ('āmos', 'aː.mos'),
    ('ins', 'pl'): ('āmis', 'aː.mis'),
    ('loc', 'pl'): ('āzu',  'aː.zu'),
}

_O_STEM_M: dict[tuple[str, str], tuple[str, str]] = {
    ('nom', 'sg'): ('os',    'os'),
    ('voc', 'sg'): ('e',     'e'),
    ('acc', 'sg'): ('om',    'om'),
    ('gen', 'sg'): ('ozio',  'o.z͡jo'),
    ('dat', 'sg'): ('ōi',    'oːj'),
    ('ins', 'sg'): ('ō',     'oː'),
    ('loc', 'sg'): ('oi',    'oj'),
    ('nom', 'pl'): ('ōs',    'oːs'),
    ('voc', 'pl'): ('ōs',    'oːs'),
    ('acc', 'pl'): ('ons',   'ons'),
    ('gen', 'pl'): ('ōm',    'oːm'),
    ('dat', 'pl'): ('oimos', 'oj.mos'),
    ('ins', 'pl'): ('ōis',   'oːjs'),
    ('loc', 'pl'): ('oizu',  'oj.zu'),
}

_O_STEM_N: dict[tuple[str, str], tuple[str, str]] = {
    ('nom', 'sg'): ('om',    'om'),
    ('voc', 'sg'): ('e',     'e'),
    ('acc', 'sg'): ('om',    'om'),
    ('gen', 'sg'): ('ozio',  'o.z͡jo'),
    ('dat', 'sg'): ('ōi',    'oːj'),
    ('ins', 'sg'): ('ō',     'oː'),
    ('loc', 'sg'): ('oi',    'oj'),
    ('nom', 'pl'): ('ā',     'aː'),
    ('voc', 'pl'): ('ā',     'aː'),
    ('acc', 'pl'): ('ā',     'aː'),
    ('gen', 'pl'): ('ōm',    'oːm'),
    ('dat', 'pl'): ('oimos', 'oj.mos'),
    ('ins', 'pl'): ('ōis',   'oːjs'),
    ('loc', 'pl'): ('oizu',  'oj.zu'),
}

_I_STEM: dict[tuple[str, str], tuple[str, str]] = {
    ('nom', 'sg'): ('is',   'is'),
    ('voc', 'sg'): ('i',    'i'),
    ('acc', 'sg'): ('im',   'im'),
    ('gen', 'sg'): ('eis',  'e͡js'),
    ('dat', 'sg'): ('eiei', 'e.je͡j'),
    ('ins', 'sg'): ('iiē',  'i.jeː'),
    ('loc', 'sg'): ('eii',  'e͡j.i'),
    ('nom', 'pl'): ('eies', 'e.jes'),
    ('voc', 'pl'): ('eies', 'e.jes'),
    ('acc', 'pl'): ('ins',  'ins'),
    ('gen', 'pl'): (GAP,    ''),
    ('dat', 'pl'): (GAP,    ''),
    ('ins', 'pl'): (GAP,    ''),
    ('loc', 'pl'): (GAP,    ''),
}

_U_STEM_MF: dict[tuple[str, str], tuple[str, str]] = {
    ('nom', 'sg'): ('us',   'us'),
    ('voc', 'sg'): ('u',    'u'),
    ('acc', 'sg'): ('um',   'um'),
    ('gen', 'sg'): ('ous',  'o͡ws'),
    ('dat', 'sg'): ('evei', 'e.we͡j'),
    ('ins', 'sg'): ('ū',    'uː'),
    ('loc', 'sg'): ('evi',  'e.wi'),
    ('nom', 'pl'): ('eves', 'e.wes'),
    ('voc', 'pl'): ('eves', 'e.wes'),
    ('acc', 'pl'): ('uns',  'uns'),
    ('gen', 'pl'): ('evōm', 'e.woːm'),
    ('dat', 'pl'): ('umos', 'u.mos'),
    ('ins', 'pl'): ('umis', 'u.mis'),
    ('loc', 'pl'): ('uzu',  'u.zu'),
}

_U_STEM_N: dict[tuple[str, str], tuple[str, str]] = {
    ('nom', 'sg'): ('u',    'u'),
    ('voc', 'sg'): ('u',    'u'),
    ('acc', 'sg'): ('u',    'u'),
    ('gen', 'sg'): ('ous',  'o͡ws'),
    ('dat', 'sg'): ('evei', 'e.we͡j'),
    ('ins', 'sg'): ('ū',    'uː'),
    ('loc', 'sg'): ('evi',  'e.wi'),
    ('nom', 'pl'): ('evā',  'e.waː'),
    ('voc', 'pl'): ('evā',  'e.waː'),
    ('acc', 'pl'): ('evā',  'e.waː'),
    ('gen', 'pl'): ('evōm', 'e.woːm'),
    ('dat', 'pl'): ('umos', 'u.mos'),
    ('ins', 'pl'): ('umis', 'u.mis'),
    ('loc', 'pl'): ('uzu',  'u.zu'),
}

_S_STEM: dict[tuple[str, str], tuple[str, str]] = {
    # Oblique stem = nom-stem + 'ez'; endings in this table include 'ez' so
    # plain concatenation with the nom-stem works throughout.
    ('nom', 'sg'): ('os',    'os'),
    ('voc', 'sg'): ('e',     'e'),
    ('acc', 'sg'): ('os',    'os'),
    ('gen', 'sg'): ('ezos',  'e.zos'),
    ('dat', 'sg'): ('ezei',  'e.zej'),
    ('ins', 'sg'): ('ezē',   'e.zeː'),
    ('loc', 'sg'): ('ezi',   'e.zi'),
    ('nom', 'pl'): ('ā',     'aː'),
    ('voc', 'pl'): ('ā',     'aː'),
    ('acc', 'pl'): ('ā',     'aː'),
    ('gen', 'pl'): ('ezōm',  'e.zoːm'),
    ('dat', 'pl'): ('ezmos', 'e.zmos'),
    ('ins', 'pl'): ('ezmis', 'e.zmis'),
    ('loc', 'pl'): ('ezu',   'e.zu'),
}

# Registry
_TABLES: dict[str, dict[tuple[str, str], tuple[str, str]]] = {
    'a_stem':    _A_STEM,
    'o_stem_m':  _O_STEM_M,
    'o_stem_n':  _O_STEM_N,
    'i_stem':    _I_STEM,
    'u_stem_mf': _U_STEM_MF,
    'u_stem_n':  _U_STEM_N,
    's_stem':    _S_STEM,
}

_LABELS: dict[str, str] = {
    'a_stem':    'ā-stem (feminine)',
    'o_stem_m':  'o-stem (masculine)',
    'o_stem_n':  'o-stem (neuter)',
    'i_stem':    'i-stem',
    'u_stem_mf': 'u-stem (m/f)',
    'u_stem_n':  'u-stem (neuter)',
    's_stem':    's-stem (neuter)',
}

# Nominative singular endings — used to strip nom-stem from input
_NOM_ENDINGS: dict[str, str] = {
    'a_stem':    'ā',
    'o_stem_m':  'os',
    'o_stem_n':  'om',
    'i_stem':    'is',
    'u_stem_mf': 'us',
    'u_stem_n':  'u',
    's_stem':    'os',
}

# Gaps that carry a note in the output
_PARTIAL_CLASSES = {'i_stem'}


# ── Core functions ─────────────────────────────────────────────────────────────

def _nfc(s: str) -> str:
    return unicodedata.normalize('NFC', s.strip())


def _bare(s: str) -> str:
    """Strip combining marks (accents) for pattern-matching only.
    In NFC all precomposed chars have the same byte-length as their
    unaccented counterparts, so stripping N chars from the original form
    is safe after a bare-form endswith() check.
    """
    nfd = unicodedata.normalize('NFD', s)
    stripped = ''.join(c for c in nfd if unicodedata.category(c) != 'Mn')
    return unicodedata.normalize('NFC', stripped)


def detect_class(nom_sg: str, gen_sg: str) -> str:
    """
    Detect stem class from nom.sg and gen.sg pair.
    Returns a class ID (key in _TABLES).
    Raises ValueError if the pair is unrecognized.
    """
    nom  = _bare(_nfc(nom_sg))
    gen  = _bare(_nfc(gen_sg))

    # Order matters: check -om before -os to avoid masking o_stem_n
    if nom.endswith('a') and gen.endswith('as'):      # ā-stem (bare: ā→a, ās→as)
        return 'a_stem'
    if nom.endswith('om') and gen.endswith('ozio'):
        return 'o_stem_n'
    if nom.endswith('os') and gen.endswith('ozio'):
        return 'o_stem_m'
    if nom.endswith('is') and gen.endswith('eis'):
        return 'i_stem'
    # u-stem neut: nom ends -u (not -us), gen ends -ous
    if not nom.endswith('us') and nom.endswith('u') and gen.endswith('ous'):
        return 'u_stem_n'
    if nom.endswith('us') and gen.endswith('ous'):
        return 'u_stem_mf'
    if nom.endswith('os') and gen.endswith('ezos'):
        return 's_stem'

    raise ValueError(
        f'Cannot detect stem class from nom.sg={nom_sg!r}, gen.sg={gen_sg!r}.\n'
        f'Supported: ā-stem, o-stem m/n, i-stem, u-stem m/f/n, s-stem.\n'
        f'Use --stem-class to override.'
    )


def derive_stem(nom_sg: str, stem_class: str) -> str:
    """Strip the nominative ending from nom_sg to get the base stem.
    Uses accent-insensitive matching (both nom and ending are bare-compared).
    In NFC, precomposed chars have the same codepoint-length as their bare
    counterparts, so slicing by bare-ending length preserves stem accents.
    """
    nom      = _nfc(nom_sg)
    nom_bare = _bare(nom)
    ending   = _NOM_ENDINGS[stem_class]
    end_bare = _bare(ending)
    if end_bare and nom_bare.endswith(end_bare):
        return nom[: -len(end_bare)]
    raise ValueError(
        f'nom.sg {nom_sg!r} does not end with expected -{ending!r} '
        f'for class {stem_class!r}.'
    )


class ParadigmResult:
    """Holds a fully generated paradigm."""

    def __init__(self, lemma: str, stem: str, stem_class: str) -> None:
        self.lemma = lemma
        self.stem = stem
        self.stem_class = stem_class
        self.label = _LABELS.get(stem_class, stem_class)
        self.is_partial = stem_class in _PARTIAL_CLASSES
        # cells[(case, number)] = (orth_form, ipa_ending)
        self.cells: dict[tuple[str, str], tuple[str, str]] = {}


def generate(
    nom_sg: str,
    gen_sg: str,
    stem_class_override: str | None = None,
) -> ParadigmResult:
    """
    Generate a full noun paradigm.

    Args:
        nom_sg: Nominative singular (Ghandwa orthography, accent marked).
        gen_sg: Genitive singular (used for class detection).
        stem_class_override: Force a specific stem class; skips auto-detection.

    Returns:
        ParadigmResult with all case forms populated.
    """
    stem_class = stem_class_override or detect_class(nom_sg, gen_sg)
    if stem_class not in _TABLES:
        raise ValueError(
            f'Unknown stem class {stem_class!r}. Known: {sorted(_TABLES)}'
        )

    stem = derive_stem(nom_sg, stem_class)
    table = _TABLES[stem_class]
    result = ParadigmResult(lemma=_nfc(nom_sg), stem=stem, stem_class=stem_class)

    for (case, num), (ending, ipa) in table.items():
        form = GAP if ending == GAP else stem + ending
        result.cells[(case, num)] = (form, ipa)

    # Preserve user-provided forms for nom.sg and gen.sg (accent marks intact)
    nom_ipa = table.get(('nom', 'sg'), ('', ''))[1]
    gen_ipa = table.get(('gen', 'sg'), ('', ''))[1]
    result.cells[('nom', 'sg')] = (_nfc(nom_sg), nom_ipa)
    result.cells[('gen', 'sg')] = (_nfc(gen_sg), gen_ipa)

    # For neuter stems where nom.sg = acc.sg by paradigm, propagate the
    # user-provided form so the table is internally consistent.
    _NOM_EQ_ACC_SG = {'o_stem_n', 'u_stem_n', 's_stem'}
    if stem_class in _NOM_EQ_ACC_SG:
        result.cells[('acc', 'sg')] = result.cells[('nom', 'sg')]
    # u-stem neuter also has nom = acc = voc in sg
    if stem_class == 'u_stem_n':
        result.cells[('voc', 'sg')] = result.cells[('nom', 'sg')]

    return result


# ── Formatters ─────────────────────────────────────────────────────────────────

def format_table(result: ParadigmResult, show_ipa: bool = False) -> str:
    """Terminal-friendly paradigm table."""
    lines: list[str] = []
    lines.append(f'  {result.lemma}  ·  {result.label}')
    lines.append(f'  stem: {result.stem}-')
    lines.append('')

    sg_forms = [result.cells.get((c, 'sg'), (GAP, ''))[0] for c in CASES]
    pl_forms = [result.cells.get((c, 'pl'), (GAP, ''))[0] for c in CASES]

    w_case = max(len(c) for c in CASES)
    w_sg   = max(len(f) for f in sg_forms)
    w_pl   = max(len(f) for f in pl_forms)

    if show_ipa:
        sg_ipas = [result.cells.get((c, 'sg'), (GAP, ''))[1] for c in CASES]
        pl_ipas = [result.cells.get((c, 'pl'), (GAP, ''))[1] for c in CASES]
        w_sg_ipa = max((len(i) for i in sg_ipas), default=4)
        w_pl_ipa = max((len(i) for i in pl_ipas), default=4)
        sg_head = f"{'singular':<{w_sg}}  {'(ending IPA)':<{w_sg_ipa + 2}}"
        pl_head = f"{'plural':<{w_pl}}  {'(ending IPA)':<{w_pl_ipa + 2}}"
    else:
        sg_head = f"{'singular':<{w_sg}}"
        pl_head = f"{'plural':<{w_pl}}"

    pad = ' ' * (w_case + 2)
    lines.append(f'  {pad}{sg_head}  {pl_head}')
    lines.append(f'  {pad}{"-" * len(sg_head)}  {"-" * len(pl_head)}')

    for case in CASES:
        sg_form, sg_ipa = result.cells.get((case, 'sg'), (GAP, ''))
        pl_form, pl_ipa = result.cells.get((case, 'pl'), (GAP, ''))

        if show_ipa:
            sg_col = f'{sg_form:<{w_sg}}  [{sg_ipa}]'
            pl_col = (f'{pl_form:<{w_pl}}  [{pl_ipa}]'
                      if pl_form != GAP else GAP)
        else:
            sg_col = f'{sg_form:<{w_sg}}'
            pl_col = f'{pl_form:<{w_pl}}'

        lines.append(f'  {case:<{w_case}}  {sg_col}  {pl_col}')

    lines.append('')
    lines.append('  ⚠ Accent fixed from nom.sg; mobile alternations not modeled.')
    if result.is_partial:
        lines.append('  ⚠ Some cells not yet established in paradigms-nominal.md (—).')

    return '\n'.join(lines)


def format_markdown(result: ParadigmResult) -> str:
    """Markdown paradigm table, matching paradigms-nominal.md style."""
    lines: list[str] = []
    lines.append(f'## *{result.lemma}*  ({result.label})')
    lines.append(f'Stem: *{result.stem}-*')
    lines.append('')
    lines.append('|     | sing-orth | plur-orth |')
    lines.append('|-----|-----------|-----------|')
    for case in CASES:
        sg_form, _ = result.cells.get((case, 'sg'), (GAP, ''))
        pl_form, _ = result.cells.get((case, 'pl'), (GAP, ''))
        lines.append(f'| {case} | {sg_form} | {pl_form} |')
    lines.append('')
    lines.append('> ⚠ Accent fixed from nom.sg; mobile alternations not modeled.')
    if result.is_partial:
        lines.append('> ⚠ Some cells not yet established in paradigms-nominal.md (—).')
    return '\n'.join(lines)
