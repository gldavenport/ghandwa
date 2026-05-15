# Handoff: Ghandwa IPA Syllabifier and Stress Renderer

**File to edit:** `tools/pie_transformer/render.py`  
**Function to replace:** `_ghandwa_ipa(tokens)`  
**Status:** stub — currently returns `/joined-tokens/` with no syllable boundaries or stress mark  
**Depends on:** `accent_index` already applied to token stream before render is called (i.e. the accented token already carries U+0301)

---

## What needs to be built

Two things that must be done together:

1. **Syllabifier** — insert `.` boundaries between syllables in the token stream
2. **Stress mark** — replace the acute accent on the accented vowel with IPA `ˈ` placed *before* the syllable containing that vowel

Current output: `/wálkʷos/`  
Target output: `/ˈwal.kʷos/`

---

## Ghandwa phonology relevant to syllabification

**Segment classes** (see `tokens.py` for the canonical sets):

| Class | Members |
|---|---|
| Vowels | `a e i o u ā ē ī ō ū` |
| Glides | `j w` — syllabic only as nucleus; otherwise treated as onset/coda consonants |
| Liquids | `r l` |
| Nasals | `m n` |
| Fricatives | `β ð ɣ ɣʷ s z` |
| Stops | `p b t d k g kʷ gʷ` |

Sonority hierarchy (low to high): stops < fricatives < nasals < liquids < glides < vowels

**Syllable structure:** CV(C), with onset maximization. No complex onsets beyond stop+liquid or fricative+stop (st-, sp-, sk-); all else is split.

**Diphthongs:** `aj aw ej ew oj ow` — the glide is part of the nucleus, not the onset of the next syllable. Post-vocalic `j` and `w` do NOT trigger a new syllable.

**Geminates:** split across syllable boundary: `ss` → `s.s`, `ll` → `l.l`, etc.

**Accent:** the accented token is identified by U+0301 (combining acute). The `ˈ` mark goes immediately before the onset consonant(s) of the syllable containing that token, not immediately before the vowel itself.

---

## Algorithm sketch

```python
def _ghandwa_ipa(tokens: list[str]) -> str:
    # 1. Strip boundary tokens
    toks = [t for t in tokens if t not in ('-', '.')]

    # 2. Find accented token index (has U+0301 in its codepoints)
    accent_syl = None  # will be set to syllable index after syllabification

    # 3. Syllabify → list of syllables, each a list of tokens
    syllables = _syllabify(toks)

    # 4. Find which syllable contains the accented token
    #    (scan for token containing U+0301)

    # 5. Strip U+0301 from the accented token (ˈ replaces it)

    # 6. Render: join syllables with '.', prefix accented syllable with 'ˈ'

    # 7. Wrap in /…/
    return f'/{body}/'


def _syllabify(toks: list[str]) -> list[list[str]]:
    # Onset maximization with the constraints above.
    # Returns list of syllables, each a list of tokens.
    ...
```

---

## Test cases

| Input tokens (post-pipeline) | Expected IPA |
|---|---|
| `w á l kʷ o s` (accent on `a`) | `/ˈwal.kʷos/` |
| `p a t ē r` (accent on `ē`) | `/paˈtēr/` |
| `β a r ɣ ú s` (accent on `u`) | `/βarˈɣus/` |
| `ɣ á j t s` (accent on `a`) | `/ˈɣajts/` |
| `ó j u` (accent on `o`) | `/ˈoju/` |
| `a n ɣ ʷ i s` (accent on `a`) | `/ˈaŋɣʷis/` |

---

## Notes

- The accented token already has U+0301 applied by `apply_accent_mark()` before the renderer is called. The renderer must detect it, strip it, and use `ˈ` instead.
- Diphthongs: `aj`, `aw` etc. count as one nucleus. Post-vocalic glide is part of the same syllable as the preceding vowel.
- Geminates split: `ss` → `s.s`; the first half closes the preceding syllable.
- Syllable-final position: Ghandwa allows CVC(C) but not CVCC unless the cluster is a valid coda (nasal+stop, liquid+stop, s+stop).
- The orthographic renderer `_ghandwa_surface` does NOT need syllabification — plain join with orthographic substitutions is correct there.
- IPA slashes and stress mark are IPA conventions only; they do not appear in surface orthography.

---

## Changelog

- 2026-05-15: handoff created; `_ghandwa_ipa` left as plain token-join stub pending syllabifier implementation
