"""
Daughter B phonological pipeline.

Input: output of the ghandwa pipeline (Ghandwa surface form tokens),
after the shared Late Common Ghandwa (Stage 1) rules.

This pipeline is registered as downstream of 'ghandwa' in pipeline.py.

Stages:
  Stage 1 — Late Common Ghandwa (shared; imported from late_common_ghandwa.py)
  Stage 2B — Daughter B Dark Ages innovations

Stage 2B non-sibilant fricative pipeline (ordered):

  2B.1  Homorganic nasal assimilation (bleeds rules 2–5)
          Vβm  → Vmm   (full place identity; geminate created; not yet simplified)
          Vðn  → Vnn   (full place identity; geminate created; not yet simplified)
          VɣʷmV → VwmV  (partial: labial feature wins, velar lost; no gemination)
          VɣnV → falls through to 2B.2 (no place overlap; hardens post-nasally)

  2B.2  Post-nasal hardening
          β ð ɣ ɣʷ → b d g gʷ / N_

  2B.3  Post-liquid (R_)
          β ɣʷ → w     (labial identity wins)
          ð ɣ  → θ x   (devoice; no labial feature to preserve)

  2B.4  Intervocalic sonorantization (V_V)
          β ɣʷ → w
          ɣ    → j
          ð    → r

  2B.5  Default devoicing (word-initial, pre-consonantal, word-final)
          β→ɸ, ð→θ, ɣ→x, ɣʷ→xʷ

Rule interaction note:
  2B.1 bleeds 2B.2–5. E.g., *VβmV*: β is post-vocalic and pre-nasal, but
  homorganic assimilation fires first, producing *VmmV*; β never reaches the
  intervocalic or post-nasal rules.

  The interaction of 2B.1 and 2B.2 in the sequence *NβmV* (post-nasal β
  before m) is unresolved — edge case for transformer testing. Not stipulated
  here; flag output for review.

/z/ handling:
  Inherited Ghandwa /z/ is preserved unchanged in Stage 2B. The voicing rule
  that created /z/ in Ghandwa is not productive in B. After the non-sibilant
  pipeline eliminates β ð ɣ ɣʷ, /z/ is the sole surviving voiced fricative —
  a systemic orphan. Stage 3B resolution not yet specified.

Stress:
  B retains bounded nonfinal stress from Stage 1 (Late Common Ghandwa accent
  retraction). A penultimate default develops gradually in Stage 2B. Full
  penultimate stress rule not yet implemented; Stage 1 accent retraction
  already handles the primary instability.

Source: docs/ghandwa-daughter-b.md; docs/daughters.md §2.2 (2B).

Open questions (do not silently resolve):
  - NβmV interaction: post-nasal hardening vs. homorganic assimilation.
  - Stage 3B: /z/ resolution by environment (partial rhotacism likely).
  - Labiovelar detail: exact conditioned-reduction triggers not yet settled.
  - Geminate simplification: geminates from 2B.1 are retained at this stage;
    simplification is a possible Stage 3+ development.
"""

from ..rule import Rule, Context, scan
from ..tokens import is_vowel, VOWELS, NASALS, LIQUIDS
from .late_common_ghandwa import RULES_LCG


# ── Category sets ──────────────────────────────────────────────────────────────

_VOICED_FRICATIVES = frozenset(['β', 'ð', 'ɣ', 'ɣʷ'])
_BOUNDARIES = frozenset(['-', '.'])


# ── Helper functions ───────────────────────────────────────────────────────────

def _prev_phoneme(toks: list[str], i: int) -> str | None:
    """Return the nearest preceding non-boundary token, or None."""
    for j in range(i - 1, -1, -1):
        if toks[j] not in _BOUNDARIES:
            return toks[j]
    return None


def _next_phoneme(toks: list[str], i: int) -> str | None:
    """Return the nearest following non-boundary token, or None."""
    for j in range(i + 1, len(toks)):
        if toks[j] not in _BOUNDARIES:
            return toks[j]
    return None


def _next_phoneme_pos(toks: list[str], i: int) -> int | None:
    """Return the index of the nearest following non-boundary token, or None."""
    for j in range(i + 1, len(toks)):
        if toks[j] not in _BOUNDARIES:
            return j
    return None


# ── Rule-building helper ───────────────────────────────────────────────────────

def _rule(id_: str, name: str, stage: str, apply_fn, requires=None) -> Rule:
    return Rule(id=id_, name=name, stage=stage, requires=requires or [], apply=apply_fn)


# ── Stage 2B rule implementations ─────────────────────────────────────────────

def _homorganic_nasal_assim(toks: list[str], ctx: Context) -> list[str]:
    """2B.1: Homorganic nasal assimilation.

    Vβm  → Vmm  (β assimilates fully to following m; geminate retained)
    Vðn  → Vnn  (ð assimilates fully to following n; geminate retained)
    VɣʷmV → VwmV (ɣʷ partially assimilates: labial feature wins, no gemination;
                   requires vowel on both sides of the ɣʷm sequence)

    VɣnV: no place overlap; ɣ does not assimilate before n.
           Falls through to post-nasal hardening (2B.2).
    """
    out = []
    for i, t in enumerate(toks):
        prev = _prev_phoneme(toks, i)
        nxt  = _next_phoneme(toks, i)

        if t == 'β' and prev in VOWELS and nxt == 'm':
            out.append('m')   # Vβm → Vmm

        elif t == 'ð' and prev in VOWELS and nxt == 'n':
            out.append('n')   # Vðn → Vnn

        elif t == 'ɣʷ' and prev in VOWELS and nxt == 'm':
            # VɣʷmV: requires vowel after m too
            m_pos = _next_phoneme_pos(toks, i)
            after_m = _next_phoneme(toks, m_pos) if m_pos is not None else None
            if after_m in VOWELS:
                out.append('w')   # VɣʷmV → VwmV
            else:
                out.append(t)     # no change (V not present after m)

        else:
            out.append(t)

    return out


def _post_nasal_harden(toks: list[str], ctx: Context) -> list[str]:
    """2B.2: Post-nasal hardening. β ð ɣ ɣʷ → b d g gʷ / N_"""
    _harden = {'β': 'b', 'ð': 'd', 'ɣ': 'g', 'ɣʷ': 'gʷ'}

    def fn(t, i, ts):
        if t in _VOICED_FRICATIVES:
            prev = _prev_phoneme(ts, i)
            if prev in NASALS:
                return _harden[t]
        return t

    return scan(toks, fn)


def _post_liquid(toks: list[str], ctx: Context) -> list[str]:
    """2B.3: Post-liquid.
    β ɣʷ → w / R_   (labial identity wins)
    ð ɣ  → θ x / R_  (devoice)
    """
    _liq_labial  = {'β': 'w', 'ɣʷ': 'w'}
    _liq_other   = {'ð': 'θ', 'ɣ': 'x'}

    def fn(t, i, ts):
        if t in _VOICED_FRICATIVES:
            prev = _prev_phoneme(ts, i)
            if prev in LIQUIDS:
                if t in _liq_labial:
                    return _liq_labial[t]
                elif t in _liq_other:
                    return _liq_other[t]
        return t

    return scan(toks, fn)


def _intervocalic_sonorize(toks: list[str], ctx: Context) -> list[str]:
    """2B.4: Intervocalic sonorantization.
    β ɣʷ → w / V_V
    ɣ    → j / V_V
    ð    → r / V_V
    """
    _sonorize = {'β': 'w', 'ɣʷ': 'w', 'ɣ': 'j', 'ð': 'r'}

    def fn(t, i, ts):
        if t in _VOICED_FRICATIVES:
            prev = _prev_phoneme(ts, i)
            nxt  = _next_phoneme(ts, i)
            if prev in VOWELS and nxt in VOWELS:
                return _sonorize[t]
        return t

    return scan(toks, fn)


def _default_devoice(toks: list[str], ctx: Context) -> list[str]:
    """2B.5: Default devoicing. β→ɸ ð→θ ɣ→x ɣʷ→xʷ / elsewhere."""
    _devoice = {'β': 'ɸ', 'ð': 'θ', 'ɣ': 'x', 'ɣʷ': 'xʷ'}
    return scan(toks, lambda t, i, ts: _devoice.get(t, t))


# ── Rule list ──────────────────────────────────────────────────────────────────

RULES_STAGE2B: list[Rule] = [
    _rule('db.2.1', 'Homorganic nasal assimilation: Vβm→Vmm, Vðn→Vnn, VɣʷmV→VwmV',
          'Stage 2 (Daughter B)', _homorganic_nasal_assim),
    _rule('db.2.2', 'Post-nasal hardening: β ð ɣ ɣʷ → b d g gʷ / N_',
          'Stage 2 (Daughter B)', _post_nasal_harden),
    _rule('db.2.3', 'Post-liquid: β ɣʷ → w / R_; ð ɣ → θ x / R_',
          'Stage 2 (Daughter B)', _post_liquid),
    _rule('db.2.4', 'Intervocalic sonorantization: β ɣʷ → w, ɣ → j, ð → r / V_V',
          'Stage 2 (Daughter B)', _intervocalic_sonorize),
    _rule('db.2.5', 'Default devoicing: β→ɸ, ð→θ, ɣ→x, ɣʷ→xʷ / elsewhere',
          'Stage 2 (Daughter B)', _default_devoice),
]

# Full Daughter B rule list: Stage 1 (shared) + Stage 2B (branch-specific)
RULES_B: list[Rule] = RULES_LCG + RULES_STAGE2B
