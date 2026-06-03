"""
Daughter B (Central) phonological pipeline.

Input: output of the ghandwa pipeline (Ghandwa surface form tokens),
after the shared Late Common Ghandwa (Stage 1) rules.

This pipeline is registered as downstream of 'ghandwa' in pipeline.py.

Stages:
  Stage 1 — Late Common Ghandwa (shared; imported from late_common_ghandwa.py)
  Stage 2B — Daughter B (Central) Dark Ages innovations

Stage 2B non-sibilant fricative pipeline (ordered):

  2B.1  Homorganic nasal assimilation (bleeds rules 2B.2–2B.6)
          Vβm   → Vmm    (full place identity; geminate retained)
          Vðn   → Vnn    (full place identity; geminate retained)
          VɣʷmV → VwmV   (partial: labial feature wins, velar lost; no gemination)
          VɣnV  → falls through to 2B.2 (no place overlap; hardens post-nasally)

  2B.2  Post-nasal hardening (bleeds 2B.3–2B.6)
          β ð ɣ ɣʷ → b d g gʷ / N_

  2B.3  Word-initial pre-liquid hardening (bleeds 2B.4–2B.6)
          β ð ɣ → b d g / #_R
          (ɣʷ in this environment is vacuous in the current lexicon; handled
           as gʷ for completeness. Onset cluster fortition motivation: #βr →
           #br parallel to PIt frater, PG brōþēr; #ðr, #ɣr similarly.)

  2B.4  β and ɣʷ gliding (bleeds 2B.5–2B.6 for these segments)
          β  → w / _V   (prevocalic; all environments after 2B.1–2B.3)
          β  → w / _C   (pre-consonantal; vacuous in current lexicon after
                          2B.1–2B.3 resolve attested #βR and Nβ cases, but
                          specified for completeness)
          ɣʷ → w / _V   (prevocalic; all environments)
          (β word-finally: unspecified; no attested cases in current lexicon.
           Flag any word-final β for review.)

  2B.5  ð and ɣ in sonorant-flanked environment
          ð → r / {V,R}_V   (after vowel or liquid, before vowel; rhotacism)
          ɣ → w / {V,R}_V   (after vowel or liquid, before vowel; gliding)
          (Liquid is transparent: R_V patterns with V_V for these segments.
           Typological motivation: ɣ → w is the natural weakening trajectory
           for a back/velar fricative in voiced flanking context; ð → r is
           well-attested cross-linguistically in this environment.)

  2B.6  Default devoicing (elsewhere)
          ð  → θ
          ɣ  → x
          ɣʷ → xʷ  (vacuous in current lexicon; retained as fallback)
          (Covers: word-initial #_V for ð and ɣ; pre-consonantal ð_C and ɣ_C;
           word-final (unattested). β is fully resolved by 2B.4.)

  2B.7  Labiovelar dissimilation (OCP-[+round]) — unchanged from prior version

Rule interaction summary:
  2B.1 bleeds 2B.2–2B.6. E.g., *VβmV*: homorganic assimilation fires first
  (→ VmmV); β never reaches post-nasal or gliding rules.

  NβmV interaction (post-nasal β before m): unresolved edge case. 2B.2 would
  harden β → b first; 2B.1 is already bled. Flag output for review.

  Ordering of 2B.3 before 2B.4 ensures #βr → #br (not #wr): onset fortition
  takes precedence over prevocalic gliding for word-initial clusters.

  R_ transparency (2B.5): liquids do not trigger hardening of ð or ɣ. Instead
  R_V patterns with V_V — the following vowel is the dominant conditioning
  factor, the liquid is transparent. Confirmed by lexicon: all attested R_
  cases are R_V; R_C and R_# are vacuous.

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

Source: docs/grammar/ch5-daughters/ch5-03-comparative-phonology.md §2B.

Open questions (do not silently resolve):
  - NβmV interaction: post-nasal hardening vs. homorganic assimilation.
  - Stage 3B: /z/ resolution by environment (partial rhotacism likely).
  - Labiovelar detail: exact conditioned-reduction triggers not yet settled.
  - Geminate simplification: geminates from 2B.1 retained; Stage 3+ development.
  - Word-final voiced fricatives: unattested in current lexicon; unspecified.
    Flag any word-final β ð ɣ ɣʷ in new entries for review.
"""

from ..rule import Rule, Context, scan
from pie_core.tokens import is_vowel, VOWELS, NASALS, LIQUIDS, BOUNDARIES
from .late_common_ghandwa import RULES_LCG
from ._common import (
    make_rule as _rule,
    prev_seg as _prev_seg,
    next_seg as _next_seg,
    is_word_initial as _is_word_initial,
    _syllabify,
)


# ── Category sets ──────────────────────────────────────────────────────────────

_VOICED_FRICATIVES = frozenset(['β', 'ð', 'ɣ', 'ɣʷ'])
_BOUNDARIES        = frozenset(['-', '.', None])


def _is_consonant(t) -> bool:
    """True if t is a non-vowel, non-boundary segment (i.e. a consonant or glide)."""
    return t is not None and t not in VOWELS and t not in BOUNDARIES


# ── Stage 2B rule implementations ─────────────────────────────────────────────

def _homorganic_nasal_assim(toks: list[str], ctx: Context) -> list[str]:
    """2B.1: Homorganic nasal assimilation.

    Vβm   → Vmm   (β assimilates fully to following m; geminate retained)
    Vðn   → Vnn   (ð assimilates fully to following n; geminate retained)
    VɣʷmV → VwmV  (ɣʷ partially assimilates: labial feature wins, no gemination;
                    requires vowel on both sides of the ɣʷm sequence)

    VɣnV: no place overlap; ɣ does not assimilate before n.
           Falls through to post-nasal hardening (2B.2).
    """
    out = []
    for i, t in enumerate(toks):
        prev, _ = _prev_seg(toks, i)
        nxt, _  = _next_seg(toks, i)

        if t == 'β' and prev in VOWELS and nxt == 'm':
            out.append('m')   # Vβm → Vmm

        elif t == 'ð' and prev in VOWELS and nxt == 'n':
            out.append('n')   # Vðn → Vnn

        elif t == 'ɣʷ' and prev in VOWELS and nxt == 'm':
            # VɣʷmV: requires vowel after m too
            _, m_pos = _next_seg(toks, i)
            after_m, _ = _next_seg(toks, m_pos) if m_pos is not None else (None, None)
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
            prev, _ = _prev_seg(ts, i)
            if prev in NASALS:
                return _harden[t]
        return t

    return scan(toks, fn)


def _initial_liquid_harden(toks: list[str], ctx: Context) -> list[str]:
    """2B.3: Word-initial pre-liquid hardening. β ð ɣ (ɣʷ) → b d g (gʷ) / #_R

    Onset fortition: #βr → br, #ðr → dr, #ɣr → gr, #βl → bl, #ɣl → gl.
    Parallel to PIt frater, PG brōþēr for β; analogous for ɣ and ð.
    Typological basis: onset clusters prefer stops over fricatives; initial
    position is a strong (fortition) environment.

    ɣʷ in this environment is vacuous in the current lexicon but specified for
    completeness: ɣʷ → gʷ / #_R.
    """
    _harden = {'β': 'b', 'ð': 'd', 'ɣ': 'g', 'ɣʷ': 'gʷ'}

    def fn(t, i, ts):
        if t in _VOICED_FRICATIVES:
            nxt, _ = _next_seg(ts, i)
            if _is_word_initial(ts, i) and nxt in LIQUIDS:
                return _harden[t]
        return t

    return scan(toks, fn)


def _labial_glide(toks: list[str], ctx: Context) -> list[str]:
    """2B.4: β and ɣʷ gliding.

    β  → w / _V   (prevocalic: all environments after 2B.1–2B.3)
    β  → w / _C   (pre-consonantal: vacuous in current lexicon but specified)
    ɣʷ → w / _V   (prevocalic: all environments)

    β word-finally: unspecified; no attested cases. Flag for review.
    ɣʷ in _C: vacuous; falls to default devoicing (2B.6) as xʷ if encountered.
    """
    def fn(t, i, ts):
        if t not in _VOICED_FRICATIVES:
            return t
        nxt, _ = _next_seg(ts, i)

        if t == 'β':
            if nxt in VOWELS or _is_consonant(nxt):
                return 'w'

        elif t == 'ɣʷ':
            if nxt in VOWELS:
                return 'w'

        return t

    return scan(toks, fn)


def _sonorant_flanked(toks: list[str], ctx: Context) -> list[str]:
    """2B.5: ð and ɣ in sonorant-flanked environment.

    ð → r / {V,R}_V   (rhotacism: after vowel or liquid, before vowel)
    ɣ → w / {V,R}_V   (gliding: after vowel or liquid, before vowel)

    Liquids are transparent: R_V patterns with V_V. The following vowel is the
    dominant conditioning factor. Confirmed by lexicon: all attested R_ cases
    for ð and ɣ are R_V; R_C and R_# are vacuous.

    Examples from lexicon:
      alβos (white): lβ → lw (β handled by 2B.4)
      melðoː (hammer name): lð → lr (this rule)
      βarðos (beard): rð → rr (this rule; geminate may simplify at Stage 3)
      βargus (high): rɣ → rw (this rule)
    """
    def fn(t, i, ts):
        if t not in _VOICED_FRICATIVES:
            return t
        prev, _ = _prev_seg(ts, i)
        nxt, _  = _next_seg(ts, i)
        prev_is_sonorant = prev in VOWELS or prev in LIQUIDS
        nxt_is_vowel     = nxt in VOWELS

        if t == 'ð' and prev_is_sonorant and nxt_is_vowel:
            return 'r'
        if t == 'ɣ' and prev_is_sonorant and nxt_is_vowel:
            return 'w'
        return t

    return scan(toks, fn)


def _default_devoice(toks: list[str], ctx: Context) -> list[str]:
    """2B.6: Default devoicing for remaining ð and ɣ.

    ð  → θ  (covers: #_V, _C, word-final)
    ɣ  → x  (covers: #_V, _C, word-final)
    ɣʷ → xʷ (vacuous in current lexicon; retained as fallback)

    β is fully resolved by 2B.4 and should not appear here. If β reaches
    this rule, it indicates an unhandled environment; output is flagged.
    """
    _devoice = {'ð': 'θ', 'ɣ': 'x', 'ɣʷ': 'xʷ'}
    return scan(toks, lambda t, i, ts: _devoice.get(t, t))


# ── Stage 2B.7: Labiovelar dissimilation ──────────────────────────────────────

def _labiovelar_dissim(toks: list[str], ctx: Context) -> list[str]:
    """2B.7: Labiovelar dissimilation (OCP-[+round]).

    If two adjacent syllables each contain a member of Lʷ = {kʷ, gʷ, xʷ, w},
    the labiovelar stop or fricative (kʷ, gʷ, xʷ) in each affected syllable
    delabializes. /w/ is immune as a target (it is only a trigger).

    Examples:
      wál.kʷos → wál.kos   (w triggers; kʷ delabializes)
      wón.gʷom → wón.gom   (w triggers; gʷ delabializes)

    Direction: symmetric. Either syllable may carry /w/ as trigger.
    If both syllables carry a labiovelar stop/fricative, both delabielize.

    Syllabification: onset maximization via _common._syllabify.
    Morpheme boundaries (-) are stripped before syllabification and reattached
    after; this rule does not cross morpheme boundaries (edge case; flag if seen).
    """
    _LW       = frozenset(['kʷ', 'gʷ', 'xʷ', 'w'])
    _DELAB    = {'kʷ': 'k', 'gʷ': 'g', 'xʷ': 'x'}
    _MORPHEME = '-'

    clean     = [t for t in toks if t != _MORPHEME]
    morph_pos = [i for i, t in enumerate(toks) if t == _MORPHEME]

    if not clean:
        return toks

    syllables = _syllabify(clean)
    has_lw    = [any(t in _LW for t in syl) for syl in syllables]

    result_sylls: list[list[str]] = []
    for i, syl in enumerate(syllables):
        prev_has_lw = i > 0 and has_lw[i - 1]
        if has_lw[i] and prev_has_lw:
            result_sylls.append([_DELAB.get(t, t) for t in syl])
        else:
            result_sylls.append(list(syl))

    flat = [t for syl in result_sylls for t in syl]
    for pos in morph_pos:
        flat.insert(pos, _MORPHEME)

    return flat


# ── Rule list ──────────────────────────────────────────────────────────────────

RULES_STAGE2B: list[Rule] = [
    _rule('db.2.1', 'Homorganic nasal assimilation: Vβm→Vmm, Vðn→Vnn, VɣʷmV→VwmV',
          'Stage 2 (Daughter B)', _homorganic_nasal_assim),
    _rule('db.2.2', 'Post-nasal hardening: β ð ɣ ɣʷ → b d g gʷ / N_',
          'Stage 2 (Daughter B)', _post_nasal_harden),
    _rule('db.2.3', 'Word-initial pre-liquid hardening: β ð ɣ (ɣʷ) → b d g (gʷ) / #_R',
          'Stage 2 (Daughter B)', _initial_liquid_harden),
    _rule('db.2.4', 'β/ɣʷ gliding: β→w / _V,_C; ɣʷ→w / _V',
          'Stage 2 (Daughter B)', _labial_glide),
    _rule('db.2.5', 'ð/ɣ sonorant-flanked: ð→r, ɣ→w / {V,R}_V',
          'Stage 2 (Daughter B)', _sonorant_flanked),
    _rule('db.2.6', 'Default devoicing: ð→θ, ɣ→x, ɣʷ→xʷ / elsewhere',
          'Stage 2 (Daughter B)', _default_devoice),
    _rule('db.2.7', 'Labiovelar dissimilation (OCP-[+round]): kʷ gʷ xʷ → k g x / adj. syl. has Lʷ',
          'Stage 2 (Daughter B)', _labiovelar_dissim),
]

# Full Daughter B rule list: Stage 1 (shared) + Stage 2B (branch-specific)
RULES_B: list[Rule] = RULES_LCG + RULES_STAGE2B
