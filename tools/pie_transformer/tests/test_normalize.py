"""
Unit tests for normalize.py.

Run immediately after normalize.py is implemented per spec implementation order §2a.
"""

import unicodedata
import unittest

from ..normalize import normalize, NormalizeResult


class TestNFCNormalization(unittest.TestCase):
    """NFC normalization is the mandatory first step."""

    def test_nfc_applied(self):
        # NFD input (Apple Numbers export): a + combining acute
        nfd_acute = 'a\u0301'
        result = normalize(nfd_acute)
        # Result should be NFC
        self.assertEqual(result.clean, unicodedata.normalize('NFC', result.clean))

    def test_nfc_precomposed_passes(self):
        result = normalize('á')
        # accent stripped, result is 'a'
        self.assertEqual(result.clean, 'a')
        self.assertIsNotNone(result.accent_char_pos)


class TestLeadingStar(unittest.TestCase):
    def test_star_stripped(self):
        result = normalize('*wlkwos')
        self.assertFalse(result.clean.startswith('*'))
        self.assertTrue(result.had_star)

    def test_no_star(self):
        result = normalize('wlkwos')
        self.assertFalse(result.had_star)


class TestAccentExtraction(unittest.TestCase):
    def test_acute_on_vowel(self):
        # *wĺ̥kʷos — accent on l̥ (or in normalized form, on preceding char)
        result = normalize('*wĺ̥kʷos')
        self.assertIsNotNone(result.accent_char_pos)

    def test_no_accent(self):
        result = normalize('*wlkwos')
        self.assertIsNone(result.accent_char_pos)

    def test_precomposed_acute(self):
        result = normalize('*pátēr')
        self.assertIsNotNone(result.accent_char_pos)
        # Accent is on 'a'; it should be near the start
        self.assertGreater(result.accent_char_pos, -1)

    def test_accent_stripped_from_clean(self):
        result = normalize('*pátēr')
        # No acute combining character in result
        nfd = unicodedata.normalize('NFD', result.clean)
        self.assertNotIn('\u0301', nfd)


class TestShorthandExpansion(unittest.TestCase):
    def test_longvowel_colon(self):
        result = normalize('a:')
        self.assertIn('ā', result.clean)

    def test_laryngeal_digits(self):
        self.assertIn('h₁', normalize('H1').clean)
        self.assertIn('h₂', normalize('H2').clean)
        self.assertIn('h₃', normalize('H3').clean)
        self.assertIn('h₁', normalize('h1').clean)

    def test_laryngeal_subscript(self):
        self.assertIn('h₁', normalize('h₁').clean)
        self.assertIn('h₂', normalize('h₂').clean)
        self.assertIn('h₃', normalize('h₃').clean)

    def test_labiovelar_kw(self):
        self.assertIn('kʷ', normalize('kw').clean)

    def test_labiovelar_gw(self):
        self.assertIn('gʷ', normalize('gw').clean)

    def test_labiovelar_gwh(self):
        self.assertIn('gʷʰ', normalize('gwh').clean)

    def test_aspirate_bh(self):
        self.assertIn('bʰ', normalize('bh').clean)

    def test_aspirate_dh(self):
        self.assertIn('dʰ', normalize('dh').clean)

    def test_aspirate_gh(self):
        # gh not followed by laryngeal subscript
        self.assertIn('gʰ', normalize('gh').clean)

    def test_gh_not_in_h2(self):
        # 'gh₂' should NOT convert 'gh' before subscript
        result = normalize('gh₂')
        # After laryngeal expansion, h₂ stays; the 'g' should remain 'g'
        # (gh before ₂ should not be consumed as 'gʰ')
        self.assertNotIn('gʰ', result.clean)

    def test_syl_res_underscore(self):
        self.assertIn('r̥', normalize('r_').clean)
        self.assertIn('l̥', normalize('l_').clean)
        self.assertIn('m̥', normalize('m_').clean)
        self.assertIn('n̥', normalize('n_').clean)

    def test_y_to_j(self):
        # y → j in normalization
        result = normalize('yod')
        self.assertIn('j', result.clean)
        self.assertNotIn('y', result.clean)

    def test_i_breve_to_j(self):
        result = normalize('i\u032fod')
        self.assertIn('j', result.clean)

    def test_leading_star_then_expand(self):
        result = normalize('*bher')
        self.assertTrue(result.had_star)          # star was present
        self.assertNotIn('*', result.clean)        # star stripped from clean
        self.assertEqual(result.clean, 'bʰer')    # bh → bʰ in normalization; β is pipeline

    def test_bh_expands_then_no_star(self):
        result = normalize('*bher')
        self.assertNotIn('*', result.clean)
        self.assertIn('bʰ', result.clean)  # bh → bʰ in normalize; β only in pipeline

    def test_bh_expands_to_bph(self):
        result = normalize('*bher')
        self.assertIn('bʰ', result.clean)


class TestCRLF(unittest.TestCase):
    def test_crlf_in_input(self):
        # normalize should handle input with \r
        result = normalize('*patér\r')
        self.assertNotIn('\r', result.clean)


if __name__ == '__main__':
    unittest.main()
