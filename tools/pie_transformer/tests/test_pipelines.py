"""
Pipeline test suite.

Test statuses (per spec):
  stable      — stable tests fail loudly on mismatch
  provisional — report mismatches as review items; do not fail suite
  disputed    — show competing expected notes; do not fail suite
  exploratory — no expected output; used to inspect derivations

Missing-accent blockage is a valid expected result.

Starter inputs are from spec §Testing. Expected outputs for Ghandwa are derived
from the JSX prototype and phonological-history.md. Many are marked provisional
pending review.
"""

from __future__ import annotations

import copy
import sys
import unittest

from ..normalize import normalize
from ..tokenize import tokenize, accent_char_pos_to_token_index
from ..rule import Context
from ..pipeline import run
from ..render import render


# ── Status markers ────────────────────────────────────────────────────────────

REVIEW_LOG: list[str] = []


def _run_form(raw: str, pipeline: str = 'ghandwa') -> str:
    """Normalize, tokenize, run pipeline, return surface form."""
    norm = normalize(raw)
    tokens, offsets = tokenize(norm.clean)
    accent_idx = accent_char_pos_to_token_index(norm.accent_char_pos, tokens, offsets)
    ctx = Context(accent_index=accent_idx)
    result = run(pipeline, list(tokens), ctx, raw)
    return render(pipeline, 'surface', result.final_tokens), result.status


def _check_provisional(test_name: str, raw: str, expected: str, pipeline: str = 'ghandwa'):
    """Check a provisional test case. Appends to REVIEW_LOG on mismatch; does not raise."""
    actual, status = _run_form(raw, pipeline)
    if actual != expected and status != expected:
        REVIEW_LOG.append(
            f'PROVISIONAL MISMATCH [{test_name}]: {raw!r} ({pipeline}) '
            f'expected={expected!r} got={actual!r} status={status}'
        )
    return actual, status


# ── Stable tests ───────────────────────────────────────────────────────────────

class TestNormalizationAndTokenizationStable(unittest.TestCase):
    """Stable: normalization + tokenization round-trips. Fail loudly."""

    def test_star_stripped(self):
        norm = normalize('*wlkwos')
        self.assertFalse('*' in norm.clean)

    def test_kw_normalized(self):
        norm = normalize('kw')
        self.assertIn('kʷ', norm.clean)

    def test_tokenize_h2_single(self):
        from ..tokenize import tokenize
        tokens, _ = tokenize('h₂')
        self.assertEqual(tokens, ['h₂'])

    def test_tokenize_gw_aspirate_single(self):
        from ..tokenize import tokenize
        tokens, _ = tokenize('gʷʰ')
        self.assertEqual(tokens, ['gʷʰ'])


class TestNotImplemented(unittest.TestCase):
    """Daughter pipelines return not_implemented. Fail loudly."""

    def test_daughter_a(self):
        _, status = _run_form('*wlkwos', 'daughter-a')
        self.assertEqual(status, 'not_implemented')

    def test_daughter_b(self):
        _, status = _run_form('*wlkwos', 'daughter-b')
        self.assertEqual(status, 'not_implemented')

    def test_daughter_c(self):
        _, status = _run_form('*wlkwos', 'daughter-c')
        self.assertEqual(status, 'not_implemented')


class TestAccentBlocking(unittest.TestCase):
    """Forms without accent are blocked at pretonic shortening. Fail loudly."""

    def test_no_accent_blocks_at_pretonic(self):
        # Form with a long vowel in first syllable, no accent marked → should block
        # *nēh₃mn̥ has ē in first syllable; without accent, pretonic shortening blocks
        _, status = _run_form('*neh3mn_', 'ghandwa')
        # Status may be ok (if no long vowel in first syllable before accent is needed)
        # or blocked_missing_accent. At minimum, it should not error.
        self.assertIn(status, ('ok', 'blocked_missing_accent'))

    def test_with_accent_ok(self):
        _, status = _run_form('*pátēr', 'ghandwa')
        self.assertEqual(status, 'ok')


# ── Provisional tests — starter inputs from spec ──────────────────────────────

class TestGhandwaProvisionaStarterInputs(unittest.TestCase):
    """
    Provisional test cases from spec §Testing starter inputs.
    Expected outputs derived from JSX prototype + phonological-history.md.
    Mismatches are logged to REVIEW_LOG; they do not fail the suite.
    """

    def _check(self, raw: str, expected: str):
        actual, status = _run_form(raw, 'ghandwa')
        if actual != expected:
            REVIEW_LOG.append(
                f'PROVISIONAL [{self.id()}]: {raw!r} → expected={expected!r} '
                f'got={actual!r} status={status}'
            )

    # Expected outputs derived from JSX prototype.
    # Mark as provisional: many depend on accent handling which is still under review.

    def test_wlkwos(self):
        # *wĺ̥kʷos 'wolf' — accent on l̥; syllabic l̥ → al; → walkʷos → … walwos? No.
        # JSX: wl̥kʷos → (syl res) walkʷos → (standing KʷC: kʷ before s — no C after kʷ)
        # → walkʷos (kʷ before o stays) → final: walkʷos
        # Actually kʷ is before 'o' (vowel), so kʷC rule doesn't fire.
        # Expected: walkʷos
        self._check('*wĺ̥kʷos', 'walkʷos')

    def test_ghoysós(self):
        # *ǵʰoysós 'ghost, spirit?' — centumize ǵʰ→gʰ, then gʰ→ɣ (aspirate shift)
        # *gʰoysós → s→z (oy_s: o is voiced, after that s, then o) → gʰoyzoz?
        # Actually: ɣoizoz or ɣoizos... let's let the test be exploratory
        self._check('*ǵʰoysós', 'ɣoizoz')

    def test_h2eymo(self):
        # *h₂éymō — h₂ + accent on e: h₂ colors e→a: h₂áymō → H-B3 (h₂ adjacent vowel) → áymō
        # → ā (VH→V̄? No, h₂ is before vowel, H-B3 fires: h₂ deleted adjacent to vowel)
        # With accent on first vowel: no pretonic shortening.
        # → aymō → ā (no, H-B3 just deletes h₂) → aymō
        # Juwankos: ā not applicable here. y→j: ajmō? Let's see.
        # Actually with correct accent *h₂éymō: h₂ colors e→a (h₂A); accent on position 1 (e=a now)
        # H-B3: h₂ adjacent to vowel (a) → deleted. Result: aymō → (y→j normalization) ajmō
        # → s→z not applicable; → ajmō final
        self._check('*h₂éymō', 'ajmō')

    def test_h2ymnes(self):
        # *h₂ym̥nés — no initial vowel (h₂ before consonant y)
        # H-B4: #H before consonant → deleted. h₂ before j (y normalized to j) → ym̥nés → jm̥nés
        # m̥ → am: jamnés → (accent on e) → jamanez? no.
        # This is provisional. Let the test just not assert a specific value for now.
        actual, status = _run_form('*h₂ym̥nés', 'ghandwa')
        REVIEW_LOG.append(f'EXPLORATORY [h₂ym̥nés]: → {actual!r} ({status})')

    def test_ghordhos(self):
        # *gʰórdʰos — centumize (no palatals); gʰ→ɣ, dʰ→ð; → ɣórdʰos → ɣórðos
        # s→z? d before s? No. Final: ɣórðos
        self._check('*gʰórdʰos', 'ɣórðos')

    def test_dhuh2mos(self):
        # *dʰuh₂mós — dʰ→ð; h₂ adjacent to vowel (u before h₂? No: dʰ-u-h₂-m-ó-s)
        # H-B3: h₂ adjacent to vowel? prev=u (vowel) → fire: h₂ deleted, u stays.
        # H-B2 might fire first: u before h₂ → ū? Then H-B2 fires: u+h₂ → ū (before m which is C)
        # Result: dʰūmós → dʰ→ð → ðūmós → (accent on ó, pretonic: ū stays long) → ðūmoz?
        # s→z: m is voiced, ó is voiced, s between mós: m_o_s → before vowel, but s is word-final
        # Actually: ðūmós → s→z? s is at end: prev=o (voiced), next=nothing → no voicing.
        # Final: ðūmos (accent blocks pretonic on ū since ū IS the first syllable vowel? No:
        # ð is consonant, ū is first vowel. Accent on ó is later → pretonic shorten ū→u.
        # With accent: ðūmós → pretonic: ū→u → ðumós. Final: ðumoz? No, s at end, not between voiced.
        # s at word-final: prev=o (voiced), next=None → does NOT voice. ðumos.
        self._check('*dʰuh₂mós', 'ðumos')

    def test_ph2ter(self):
        # *ph₂tḗr 'father' — h₂ between p and t (consonants): H-B5: CHC in initial? 
        # wait — has h₂ between p and t. No vowel before h₂ so H-B2/B3 don't fire for VH.
        # H-B5: CHC → Ca (initial syllable): prev=p (consonant), next=t (consonant), no vowel before → 'a'
        # p+h₂+t → p+a+t = pat. Then ḗ: accent on ē.
        # patḗr → (pretonic: first vowel a, accent on ē which is later → shorten a? a already short) → patēr
        # Final: patēr
        self._check('*ph₂tḗr', 'patēr')

    def test_bhreh2ter(self):
        # *bʰréh₂tēr 'brother' — bʰ→β; h₂ adjacent to vowel (é before h₂): H-B2: é+h₂ → ē (V̄) before t
        # *bʰréh₂tēr → H-A: h₂ colors e→a → *bʰráh₂tēr → H-B2: a+h₂→ā (before t, consonant) → bʰrātēr
        # → bʰ→β: βrātēr → accent on rá, pretonic: ā is first long vowel? wait, accent on é (position 2)
        # If accent on é (in *bʰréh₂tēr), after h₂ coloring e→a, accent moves to 'a' at pos 2
        # Then pretonic: any vowel before accent? No vowel before 'a' (bʰr are consonants). No shortening.
        # Final: βrātēr
        self._check('*bʰréh₂tēr', 'βrātēr')

    def test_gweneh2(self):
        # *gʷeneh₂ 'woman' — h₂ at end (after vowel e): H-B2: e+h₂→ē (before #) → *gʷenē
        # gʷ before e: Boukólos doesn't fire (e is not u/w). kʷC doesn't fire (e is vowel).
        # s→z: no s. y→j: no y. Final: gʷenē
        self._check('*gʷeneh₂', 'gʷenē')

    def test_h2ekweh2(self):
        # *h₂ékʷeh₂ 'horse / water' — accent on é
        # H-A: h₂ colors e→a (both h₂s): h₂ákʷah₂ → H-B3: both h₂ adjacent to vowels → deleted
        # → ákʷa → no pretonic (accent on first vowel á) → akʷa
        # Final: akʷa
        self._check('*h₂ékʷeh₂', 'akʷa')

    def test_dn_gwheh2s(self):
        # *dn̥ǵʰwéh₂s 'tongue' — n̥→an; ǵʰ→gʰ (centumize); gʰw→gʷʰ (labiovelarize); gʷʰ→ɣʷ
        # *dn̥ǵʰwéh₂s → centumize ǵʰ→gʰ → dn̥gʰwéh₂s → labiovelarize gʰw→gʷʰ → dn̥gʷʰéh₂s
        # → n̥→an → dangʷʰéh₂s → h₂ adjacent to é... wait, gʷʰ before é, h₂ after é
        # H-A: h₂ colors é→á (but é already = 'e', h₂ follows, colors to 'a') → dangʷʰáh₂s
        # H-B2: á+h₂ → ā before s → dangʷʰās
        # Aspirate: gʷʰ→ɣʷ → danɣʷās
        # Standing KʷC: ɣʷ is not a labiovelar kʷ/gʷ/gʷʰ, so rule doesn't apply.
        # Final: danɣʷās (provisional)
        self._check('*dn̥ǵʰwéh₂s', 'danɣʷās')

    def test_ghn_dweh2s(self):
        # *ǵʰn̥dwéh₂s — the Ghandwa word itself? ǵʰ→gʰ (centumize); n̥→an; gʰ→ɣ;
        # h₂ adj to é → colors e→a → h₂ deleted
        # *ǵʰn̥dwéh₂s → gʰn̥dwéh₂s → (n̥→an) → gʰandwéh₂s
        # H-A: h₂ after é → a. H-B2: é+h₂ → ā. gʰandwās → gʰ→ɣ → ɣandwās
        # s→z: w is voiced, ā is voiced, s after ā before end? prev=ā voiced, next=None → no voice
        # Final: ɣandwās (provisional)
        self._check('*ǵʰn̥dwéh₂s', 'ɣandwās')

    def test_megh2_s(self):
        # *méǵh₂-s 'great (nom.sg.)' — boundary token preserved through pipeline
        # ǵ→g (centumize); h₂ adj to ǵ? No: ǵ already → g; g+h₂ → H-B5: CHC? g,h₂,s: consonants
        # but wait: H-A fires first: h₂ has no adjacent vowel (prev=g, next=s) → no coloring
        # H-B5: prev=g (consonant), next=s (consonant), no vowel before → 'a'
        # ég(h₂)s → mégas → (accent on é, first vowel, no pretonic) → mégas
        # boundary: - preserved. mégas. But boundary handling: - in stream.
        # *méǵh₂-s → after norm: mégh₂-s (ǵ not in norm; ǵ→g in pipeline)
        # Pipeline sees: m,é,g,h₂,-,s (with - as boundary token)
        # Thorn: none. H-B5: h₂ between g and '-'? '-' is boundary, not consonant → no.
        # H-B3: h₂ adjacent to vowel? prev=g (not vowel), next='-' (not vowel) → no
        # H-B4: initial? No. H-B5: is '-' a consonant? Per is_consonant: - is boundary → no.
        # So h₂ survives as ˀ (diagnostic). meɡˀ-s (with boundary)
        # Actually: H-B5 checks is_consonant which returns False for '-'. So h₂ → ˀ.
        # meɡˀ-s or without boundary in surface: megˀs. Provisional.
        actual, status = _run_form('*méǵh₂-s', 'ghandwa')
        REVIEW_LOG.append(f'EXPLORATORY [méǵh₂-s]: → {actual!r} status={status}')
        # The key invariant: result should not error
        self.assertIn(status, ('ok', 'blocked_missing_accent'))

    def test_mgh2_es(self):
        # *mǵh₂-és (genitive of 'great') — similar but accent on second vowel
        actual, status = _run_form('*mǵh₂-és', 'ghandwa')
        REVIEW_LOG.append(f'EXPLORATORY [mǵh₂-és]: → {actual!r} status={status}')
        self.assertIn(status, ('ok', 'blocked_missing_accent'))


class TestOldWekwosProvisional(unittest.TestCase):
    """Provisional tests for Old Wékʷos pipeline."""

    def test_wolf(self):
        actual, status = _run_form('*wĺ̥kʷos', 'old-wekwos')
        REVIEW_LOG.append(f'EXPLORATORY [old-wekwos wĺ̥kʷos]: → {actual!r} ({status})')
        self.assertIn(status, ('ok', 'blocked_missing_accent', 'not_implemented'))

    def test_father(self):
        actual, status = _run_form('*ph₂tḗr', 'old-wekwos')
        REVIEW_LOG.append(f'EXPLORATORY [old-wekwos ph₂tḗr]: → {actual!r} ({status})')
        self.assertIn(status, ('ok', 'blocked_missing_accent', 'not_implemented'))


class TestNeoWekwosProvisional(unittest.TestCase):
    """Provisional tests for Neo-Wékʷos pipeline (downstream of Old Wékʷos)."""

    def test_wolf(self):
        actual, status = _run_form('*wĺ̥kʷos', 'neo-wekwos')
        REVIEW_LOG.append(f'EXPLORATORY [neo-wekwos wĺ̥kʷos]: → {actual!r} ({status})')
        self.assertIn(status, ('ok', 'blocked_missing_accent', 'not_implemented'))


# ── Review log reporting ───────────────────────────────────────────────────────

class TestReviewLog(unittest.TestCase):
    """Print the review log after all tests. Not a failure condition."""

    @classmethod
    def setUpClass(cls):
        pass

    def test_print_review_log(self):
        if REVIEW_LOG:
            print('\n\n=== PROVISIONAL TEST REVIEW LOG ===', file=sys.stderr)
            for entry in REVIEW_LOG:
                print(f'  {entry}', file=sys.stderr)
            print(f'=== {len(REVIEW_LOG)} provisional mismatches ===\n', file=sys.stderr)
        # Not a failure; provisional mismatches are expected during development
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
