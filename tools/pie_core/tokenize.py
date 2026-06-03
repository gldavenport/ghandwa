"""
Tokenization: converts a normalized pre-token string into a token stream.

Rules:
  - Longest-match scanning: complex symbols (gʷʰ, h₂, r̥, …) are recognized as
    single tokens before their component characters.
  - Boundary marks are preserved as tokens: '-' = morpheme boundary, '.' = syllable boundary.
  - Re-tokenization occurs only on raw string input. Pipeline chaining passes token
    streams directly (no re-tokenization).

Accent mapping:
  After tokenization, the char-offset of the accented character (from normalize.py)
  is mapped to a token index. The token index is stored in context.accent_index.
"""

from .tokens import PHONEME_PATTERNS, BOUNDARIES


def tokenize(s: str) -> tuple[list[str], list[int]]:
    """
    Tokenize a normalized string using longest-match scanning.

    Returns:
        tokens: list of token strings
        char_offsets: list of char offsets (start position in s) for each token

    char_offsets[i] is the start char position of tokens[i] in s.
    Pass char_offsets to accent_char_pos_to_token_index() to find accent_index.
    """
    tokens: list[str] = []
    char_offsets: list[int] = []
    i = 0

    while i < len(s):
        matched = False

        # Try each phoneme pattern (already in longest-first order)
        for pattern in PHONEME_PATTERNS:
            plen = len(pattern)
            if s[i:i + plen] == pattern:
                char_offsets.append(i)
                tokens.append(pattern)
                i += plen
                matched = True
                break

        if not matched:
            # Single character fallthrough: boundary tokens, plain ASCII, etc.
            char_offsets.append(i)
            tokens.append(s[i])
            i += 1

    return tokens, char_offsets


def accent_char_pos_to_token_index(
    char_pos: int | None,
    tokens: list[str],
    char_offsets: list[int],
) -> int | None:
    """
    Map a character offset (from normalize.py) to a token index.

    Returns the index of the token whose span contains char_pos,
    or None if char_pos is None or no matching token is found.
    """
    if char_pos is None:
        return None

    for ti, (tok, offset) in enumerate(zip(tokens, char_offsets)):
        # The token occupies chars [offset, offset + len(tok))
        if offset <= char_pos < offset + len(tok):
            return ti

    # Fallback: find token with closest start offset
    best = None
    best_dist = float('inf')
    for ti, offset in enumerate(char_offsets):
        dist = abs(offset - char_pos)
        if dist < best_dist:
            best_dist = dist
            best = ti
    return best


def tokens_to_string(tokens: list[str]) -> str:
    """Join a token stream into a display string (for trace output)."""
    return ''.join(tokens)
