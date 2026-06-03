"""
Unit tests for tokenize.py.

Run immediately after tokenize.py is implemented per spec implementation order §3a.
"""

import unittest

from ..tokenize import tokenize, accent_char_pos_to_token_index, tokens_to_string
from ..normalize import normalize


class TestLongestMatch(unittest.TestCase):
    """Multi-character symbols must be recognized as single tokens."""

    def test_gw_aspirate(self):
        tokens, _ = tokenize('gʷʰ')
        self.assertEqual(tokens, ['gʷʰ'])

    def test_labiovelar_kw(self):
        tokens, _ = tokenize('kʷ')
        self.assertEqual(tokens, ['kʷ'])

    def test_labiovelar_gw(self):
        tokens, _ = tokenize('gʷ')
        self.assertEqual(tokens, ['gʷ'])

    def test_laryngeal_h2(self):
        tokens, _ = tokenize('h₂')
        self.assertEqual(tokens, ['h₂'])

    def test_syl_res_r(self):
        tokens, _ = tokenize('r̥')
        self.assertEqual(tokens, ['r̥'])

    def test_syl_res_n(self):
        tokens, _ = tokenize('n̥')
        self.assertEqual(tokens, ['n̥'])

    def test_long_vowel(self):
        tokens, _ = tokenize('ā')
        self.assertEqual(tokens, ['ā'])

    def test_gw_not_split(self):
        # gʷ must be one token, not ['g', 'ʷ']
        tokens, _ = tokenize('gʷ')
        self.assertEqual(len(tokens), 1)

    def test_h2_not_split(self):
        tokens, _ = tokenize('h₂')
        self.assertEqual(len(tokens), 1)


class TestBoundaryTokens(unittest.TestCase):
    """Boundary marks are preserved as tokens."""

    def test_morpheme_boundary(self):
        tokens, _ = tokenize('bʰer-')
        self.assertIn('-', tokens)

    def test_syllable_boundary(self):
        tokens, _ = tokenize('bʰer.eti')
        self.assertIn('.', tokens)

    def test_boundary_not_deleted(self):
        tokens, _ = tokenize('a-bʰ')
        self.assertEqual(tokens, ['a', '-', 'bʰ'])


class TestWholeWords(unittest.TestCase):
    """Verify tokenization of complete normalized forms."""

    def test_wlkwos(self):
        # *wĺ̥kʷos normalized (accent stripped): wl̥kʷos
        norm = normalize('*wĺ̥kʷos')
        tokens, _ = tokenize(norm.clean)
        self.assertIn('kʷ', tokens)
        self.assertIn('l̥', tokens)

    def test_ph2ter(self):
        norm = normalize('*ph₂tḗr')
        tokens, _ = tokenize(norm.clean)
        self.assertIn('h₂', tokens)

    def test_gndweh2(self):
        norm = normalize('*ǵʰn̥dwéh₂s')
        tokens, _ = tokenize(norm.clean)
        # After normalization: ǵʰ → gʰ (in pipeline, not norm), but norm gives 'ǵʰ'
        # Actually normalization does NOT do centumization; that's a pipeline rule.
        self.assertIn('ǵʰ', tokens)
        self.assertIn('n̥', tokens)
        self.assertIn('h₂', tokens)

    def test_simple_word(self):
        norm = normalize('*patēr')
        tokens, offsets = tokenize(norm.clean)
        self.assertEqual(tokens_to_string(tokens), norm.clean)


class TestAccentMapping(unittest.TestCase):
    """accent_char_pos → token index mapping."""

    def test_accent_on_first_vowel(self):
        # *pátēr — accent on 'a' (first vowel)
        norm = normalize('*pátēr')
        tokens, offsets = tokenize(norm.clean)
        accent_idx = accent_char_pos_to_token_index(norm.accent_char_pos, tokens, offsets)
        self.assertIsNotNone(accent_idx)
        self.assertEqual(tokens[accent_idx], 'a')

    def test_accent_on_later_vowel(self):
        # *patḗr — accent on ē (second vowel)
        norm = normalize('*patḗr')
        tokens, offsets = tokenize(norm.clean)
        accent_idx = accent_char_pos_to_token_index(norm.accent_char_pos, tokens, offsets)
        self.assertIsNotNone(accent_idx)
        self.assertEqual(tokens[accent_idx], 'ē')

    def test_no_accent(self):
        norm = normalize('*pater')
        tokens, offsets = tokenize(norm.clean)
        accent_idx = accent_char_pos_to_token_index(norm.accent_char_pos, tokens, offsets)
        self.assertIsNone(accent_idx)

    def test_accent_on_syl_res(self):
        # *wĺ̥kʷos — accent on syllabic l̥
        norm = normalize('*wĺ̥kʷos')
        tokens, offsets = tokenize(norm.clean)
        accent_idx = accent_char_pos_to_token_index(norm.accent_char_pos, tokens, offsets)
        self.assertIsNotNone(accent_idx)
        # Should point to 'l̥'
        self.assertEqual(tokens[accent_idx], 'l̥')


class TestRoundTrip(unittest.TestCase):
    """tokens_to_string(tokenize(s)) == s for clean inputs."""

    def test_roundtrip(self):
        for s in ['patēr', 'kʷekʷlos', 'h₂ekʷeh₂', 'bʰer', 'wl̥kʷos']:
            tokens, _ = tokenize(s)
            self.assertEqual(tokens_to_string(tokens), s,
                             f'Round-trip failed for {s!r}')


if __name__ == '__main__':
    unittest.main()
