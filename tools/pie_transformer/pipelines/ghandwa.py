"""
Ghandwa historical pipeline.

Rule ordering follows docs/phonological-history.md and the JSX prototype
(tools/pie-2-ghandwa.jsx). Stage labels match the phonological-history sections.

Key departures from the JSX architecture (per spec):
  - No shared pre-branch transformation block. Centumization, labiovelarization,
    Boukólos, and KʷC→K are defined here, inside the Ghandwa pipeline.
  - Rules are flat objects; no subclass hierarchy or global language flags.
  - Standing rules (labiovelarization, Boukólos, KʷC→K) appear as ordinary rules
    at the positions where the JSX ran them to stability. One pass is placed after
    Stage 1 laryngeals and one after Stage 2. For practical PIE inputs, one pass
    per position is equivalent to the JSX's "run to stability" (max 10 passes).
  - Pretonic shortening requires accent in context (blocks derivation if absent).
  - y→j is handled in normalization (spec §Normalization shorthand table).
    The rule is retained here as a historical note but is a no-op after normalization.
"""

from ..rule import Rule, Context, scan
from ..tokens import (
    SHORTEN, LENGTHEN, DEVOICE, DEASPIRATE,
    is_vowel, is_laryngeal, is_glottal, is_syl_res, is_dental,
    is_plain_velar, is_consonant, is_voiced, is_sonorant, is_boundary,
    lengthen, shorten,
)


# ── Rule-building helper ───────────────────────────────────────────────────────

def _rule(id_: str, name: str, stage: str, apply_fn, requires=None) -> Rule:
    return Rule(
        id=id_,
        name=name,
        stage=stage,
        requires=requires or [],
        apply=apply_fn,
    )


# ── Category helpers (Ghandwa-local) ──────────────────────────────────────────

def _laryngeal_color(h: str, v: str) -> str:
    """h₂ colors adjacent e→a, h₃ colors adjacent e→o. h₁ and H are neutral."""
    if v != 'e':
        return v
    if h == 'h₂':
        return 'a'
    if h == 'h₃':
        return 'o'
    return v  # h₁, H are neutral



# ── Pre-stage: centum merger and labiovelar normalization ─────────────────────
# (Ghandwa-internal; not shared with Wékʷos pipelines per spec)

_CENTUMIZE = _rule(
    'gh.centum', 'Centumization: ḱ→k, ǵ→g, ǵʰ→gʰ', 'Pre-stage',
    lambda toks, ctx: scan(toks, lambda t, i, ts:
        'k' if t == 'ḱ' else
        'g' if t == 'ǵ' else
        'gʰ' if t == 'ǵʰ' else t
    )
)

def _labiovelarize(toks: list[str], ctx: Context) -> list[str]:
    """K+w → Kʷ (sequence merge).

    Each merge reduces the token list by 1.  For every merge whose first token
    is strictly before ctx.accent_index, the accent shifts left by 1.
    """
    out: list[str] = []
    merges_before_accent = 0
    i = 0
    while i < len(toks):
        tok, nxt = toks[i], toks[i + 1] if i + 1 < len(toks) else None
        merged = False
        if tok == 'k' and nxt == 'w':
            out.append('kʷ'); i += 2; merged = True
        elif tok == 'g' and nxt == 'w':
            out.append('gʷ'); i += 2; merged = True
        elif tok == 'gʰ' and nxt == 'w':
            out.append('gʷʰ'); i += 2; merged = True
        else:
            out.append(tok); i += 1
        if merged and ctx.accent_index is not None and (i - 2) < ctx.accent_index:
            merges_before_accent += 1
    if ctx.accent_index is not None:
        ctx.accent_index -= merges_before_accent
    return out

_LABIOVELARIZE = _rule('gh.lv_merge', 'Labiovelarization: K+w → Kʷ', 'Pre-stage', _labiovelarize)

def _pie_delab(toks: list[str], ctx: Context) -> list[str]:
    """PIE-internal delabialization: Kʷ → K / {u,ū,w} _ and Kʷ → K / _ {u,ū,w}.

    Bidirectional, narrow environment. This is a pre-branch PIE change that
    cleans up the input before any Ghandwa-specific rules fire.  Runs once
    at pre-stage; does NOT recur as a standing rule (its environments are
    exhausted before laryngeal loss or syllabic vocalization create new ones).
    """
    LABIOVELARS = ('kʷ', 'gʷ', 'gʷʰ')
    DELAB = {'kʷ': 'k', 'gʷ': 'g', 'gʷʰ': 'gʰ'}
    UW = {'u', 'ū', 'w'}

    out: list[str] = []
    for i, tok in enumerate(toks):
        prev = out[-1] if out else None
        nxt  = toks[i + 1] if i + 1 < len(toks) else None
        if tok in LABIOVELARS and ((prev and prev in UW) or (nxt and nxt in UW)):
            out.append(DELAB[tok])
        else:
            out.append(tok)
    return out

_PIE_DELAB = _rule('gh.pie_delab',
                   'PIE delab: Kʷ→K / {u,ū,w}_ and _{u,ū,w}',
                   'Pre-stage', _pie_delab)

def _boukólos(toks: list[str], ctx: Context) -> list[str]:
    """Ghandwa Boukólos: Kʷ → K / _ {C, w, u, ū}.

    Forward-only, broader than the PIE-internal rule.  Covers environments
    created by laryngeal loss and syllabic vocalization; runs as a standing
    rule after Stage 1 and Stage 2 only — not at pre-stage.
    Syllabic resonants and boundaries do not trigger.
    """
    LABIOVELARS = ('kʷ', 'gʷ', 'gʷʰ')
    DELAB = {'kʷ': 'k', 'gʷ': 'g', 'gʷʰ': 'gʰ'}
    TRIGGER_VOWELS = {'u', 'ū'}

    def _triggers(t: str) -> bool:
        return (t in TRIGGER_VOWELS or t == 'w' or
                (is_consonant(t) and not is_syl_res(t) and not is_boundary(t)))

    out: list[str] = []
    for i, tok in enumerate(toks):
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if tok in LABIOVELARS and nxt is not None and _triggers(nxt):
            out.append(DELAB[tok])
        else:
            out.append(tok)
    return out

# Note: _BOUKÓLOS is intentionally NOT placed in the pre-stage pipeline list.
# It appears only as standing rules _STAND_BOK_1 and _STAND_BOK_2.
_BOUKÓLOS = _rule('gh.boukólos', 'Boukólos: Kʷ→K / _{C,w,u,ū} (Ghandwa innovation)',
                  'Standing', _boukólos)


# ── Stage 1: dental clusters ───────────────────────────────────────────────────

def _tts(toks: list[str], ctx: Context) -> list[str]:
    """TT → ss: dental before dental → geminate ss.
    Note: dental+s is NOT covered here; *ds → ts via the voiced-before-ts
    devoicing rule, and Ghandwa preserves ts (does not reduce to ss).
    """
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if is_dental(tok) and nxt and is_dental(nxt):
            out.extend(['s', 's'])
            # Two tokens replaced two tokens; accent_index unchanged
            i += 2
        else:
            out.append(tok)
            i += 1
    return out

_TTS = _rule('gh.tts', 'TT→ss: dental+dental → geminate ss', 'Dentals', _tts)

def _ssc_simplify(toks: list[str], ctx: Context) -> list[str]:
    """ssC → sC: geminate ss simplifies before consonant."""
    out: list[str] = []
    i = 0
    while i < len(toks):
        if (toks[i] == 's' and
            i + 1 < len(toks) and toks[i + 1] == 's' and
            i + 2 < len(toks) and is_consonant(toks[i + 2])):
            out.append('s')
            # One token deleted; update accent if it was after position i
            if ctx.accent_index is not None and ctx.accent_index > i:
                ctx.accent_index -= 1
            i += 2
        else:
            out.append(toks[i])
            i += 1
    return out

_SSC = _rule('gh.ssc', 'ssC→sC: geminate simplifies before consonant', 'Dentals', _ssc_simplify)

def _thorn(toks: list[str], ctx: Context) -> list[str]:
    """TK → KT: thorn metathesis word-internally (plain velars only; labiovelars excluded)."""
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        # Word-initial position excluded (i == 0)
        if i != 0 and is_dental(tok) and nxt and is_plain_velar(nxt):
            out.extend([nxt, tok])  # swap; no change in count → accent_index unchanged
            i += 2
        else:
            out.append(tok)
            i += 1
    return out

_THORN = _rule('gh.thorn', 'Thorn metathesis: TK→KT word-internally', 'Dentals', _thorn)


# ── Stage 1: laryngeals ────────────────────────────────────────────────────────

def _h_color(toks: list[str], ctx: Context) -> list[str]:
    """H-A: Laryngeal coloring — h₂/h₃ color adjacent e."""
    t = list(toks)
    # Forward pass: H colors following vowel
    for i in range(len(t) - 1):
        if is_laryngeal(t[i]) and is_vowel(t[i + 1]):
            t[i + 1] = _laryngeal_color(t[i], t[i + 1])
    # Backward pass: H colors preceding vowel
    for i in range(len(t) - 1, 0, -1):
        if is_laryngeal(t[i]) and is_vowel(t[i - 1]):
            t[i - 1] = _laryngeal_color(t[i], t[i - 1])
    return t

_H_COLOR = _rule('gh.h_a', 'H-A: Laryngeal coloring — h₂/h₃ color adjacent e', 'Laryngeals', _h_color)

def _h_vhv(toks: list[str], ctx: Context) -> list[str]:
    """H-B1: VHV → V̄ — identical vowels across laryngeal contract; laryngeal lost."""
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        if is_laryngeal(tok) and out and i + 1 < len(toks):
            prev = out[-1]
            nxt = toks[i + 1]
            if is_vowel(prev) and is_vowel(nxt) and prev == nxt:
                out.pop()
                out.append(lengthen(prev))
                # Deleted laryngeal + next vowel: net -1 token before position i+1
                if ctx.accent_index is not None and ctx.accent_index > len(out):
                    ctx.accent_index -= 1
                i += 2
                continue
        out.append(tok)
        i += 1
    return out

_H_VHV = _rule('gh.h_b1', 'H-B1: VHV→V̄ — identical vowels contract across laryngeal', 'Laryngeals', _h_vhv)

def _h_vh(toks: list[str], ctx: Context) -> list[str]:
    """H-B2: VH → V̄ — vowel before laryngeal (before C or #) lengthens; laryngeal lost."""
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        if is_laryngeal(tok) and out:
            prev = out[-1]
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            if is_vowel(prev) and (nxt is None or not is_vowel(nxt)):
                out.pop()
                out.append(lengthen(prev))
                # Replaced laryngeal with length on previous vowel: net -1
                if ctx.accent_index is not None and ctx.accent_index > len(out):
                    ctx.accent_index -= 1
                i += 1
                continue
        out.append(tok)
        i += 1
    return out

_H_VH = _rule('gh.h_b2', 'H-B2: VH→V̄ — vowel before laryngeal lengthens', 'Laryngeals', _h_vh)

def _h_adj_v(toks: list[str], ctx: Context) -> list[str]:
    """H-B3: H adjacent to vowel → ∅ — covers #HV and CHV (coloring already applied)."""
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        if is_laryngeal(tok):
            prev = out[-1] if out else None
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            if (prev and is_vowel(prev)) or (nxt and is_vowel(nxt)):
                # Delete laryngeal
                if ctx.accent_index is not None and ctx.accent_index > len(out):
                    ctx.accent_index -= 1
                i += 1
                continue
        out.append(tok)
        i += 1
    return out

_H_ADJ_V = _rule('gh.h_b3', 'H-B3: H adjacent to vowel → ∅', 'Laryngeals', _h_adj_v)

def _h_initial_c(toks: list[str], ctx: Context) -> list[str]:
    """H-B4: #H before consonant → ∅ (word-initial laryngeal before consonant deleted)."""
    if len(toks) > 1 and is_laryngeal(toks[0]) and is_consonant(toks[1]):
        if ctx.accent_index is not None and ctx.accent_index > 0:
            ctx.accent_index -= 1
        return toks[1:]
    return toks

_H_INIT_C = _rule('gh.h_b4', 'H-B4: #HC → C — initial laryngeal before consonant deleted', 'Laryngeals', _h_initial_c)

def _h_btw_c(toks: list[str], ctx: Context) -> list[str]:
    """H-B5: H between consonants → a (initial syllable) / ∅ (elsewhere)."""
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        if is_laryngeal(tok):
            prev = toks[i - 1] if i > 0 else None
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            if (prev and is_consonant(prev) and not is_syl_res(prev) and
                    nxt and is_consonant(nxt) and not is_syl_res(nxt)):
                has_vowel_before = any(is_vowel(t) for t in out)
                if not has_vowel_before:
                    out.append('a')  # schwa vocalization in initial syllable
                # else: laryngeal deleted (no vowel insertion)
                if ctx.accent_index is not None:
                    # If we inserted 'a', net change = 0 (replaced 1 with 1)
                    # If we deleted, net = -1
                    if has_vowel_before and ctx.accent_index > len(out):
                        ctx.accent_index -= 1
                i += 1
                continue
        out.append(tok)
        i += 1
    return out

_H_BTW_C = _rule('gh.h_b5', 'H-B5: CHC → Ca (initial) / C∅C (elsewhere)', 'Laryngeals', _h_btw_c)

def _h_surviving(toks: list[str], ctx: Context) -> list[str]:
    """H→ˀ: surviving laryngeals become glottal stop (diagnostic marker)."""
    return scan(toks, lambda t, i, ts: 'ˀ' if is_laryngeal(t) else t)

_H_SURV = _rule('gh.h_survive', 'H→ˀ: surviving laryngeals → glottal stop (diagnostic)', 'Laryngeals', _h_surviving)


# ── Stage 1: consonantal changes ──────────────────────────────────────────────

def _voiced_before_ts(toks: list[str], ctx: Context) -> list[str]:
    """Voiced obstruent → voiceless before t or s (Core IE)."""
    def _fn(tok: str, i: int, ts: list[str]) -> str:
        nxt = ts[i + 1] if i + 1 < len(ts) else None
        if not nxt or nxt not in ('t', 's'):
            return tok
        if tok in ('b', 'bʰ'):
            return 'p'
        if tok in ('d', 'dʰ'):
            return 't'
        if tok in ('g', 'gʰ'):
            return 'k'
        if tok in ('gʷ', 'gʷʰ'):
            return 'kʷ'
        return tok
    return scan(toks, _fn)

_VOICED_BTS = _rule('gh.voi_bts', 'Voiced obstruent → voiceless before t/s (Core IE)', 'Consonants', _voiced_before_ts)


# ── Stage 1: vowel changes ─────────────────────────────────────────────────────

def _osthoff(toks: list[str], ctx: Context) -> list[str]:
    """Osthoff's Law: V̄RC → VRC (long vowel before sonorant + consonant shortens)."""
    return scan(toks, lambda tok, i, ts: (
        shorten(tok)
        if SHORTEN.get(tok) and
           i + 1 < len(ts) and is_sonorant(ts[i + 1]) and
           i + 2 < len(ts) and is_consonant(ts[i + 2])
        else tok
    ))

_OSTHOFF = _rule('gh.osthoff', "Osthoff's Law: V̄RC → VRC", 'Vowels', _osthoff)

def _ew_ow(toks: list[str], ctx: Context) -> list[str]:
    """ew → ow: tautosyllabic e+w in coda (w before consonant or word-finally)."""
    out = list(toks)
    for i in range(len(out) - 1):
        if out[i] == 'e' and out[i + 1] == 'w':
            after = out[i + 2] if i + 2 < len(out) else None
            # w is in coda if followed by consonant or word boundary/end
            w_in_coda = (after is None or
                         (is_consonant(after) and not is_syl_res(after)) or
                         is_boundary(after))
            if w_in_coda:
                out[i] = 'o'
    return out

_EW_OW = _rule('gh.ew_ow', 'ew→ow: tautosyllabic e+w in coda', 'Vowels', _ew_ow)


# ── Pretonic shortening (accent-dependent) ────────────────────────────────────

def _pretonic_shorten(toks: list[str], ctx: Context) -> list[str]:
    """
    Pretonic shortening: long vowel on first syllable shortens when accent
    falls on a later syllable.

    Requires accent_index in context. Uses accent_index to determine whether
    there is a vowel before the accented position (= accent on later syllable).
    """
    if ctx.accent_index is None:
        return toks  # should not reach here due to requires=['accent'] guard

    # Find first vowel token
    first_vowel_idx = next(
        (i for i, t in enumerate(toks) if is_vowel(t)), None
    )
    if first_vowel_idx is None:
        return toks

    # Is there any vowel before the accented token? If so, accent is on a later syllable.
    any_vowel_before_accent = any(
        is_vowel(toks[j]) for j in range(min(ctx.accent_index, len(toks)))
    )

    if not any_vowel_before_accent:
        # Accent is on first syllable (or the accented token IS the first vowel)
        return toks

    # Accent is later: shorten the first vowel
    out = list(toks)
    if out[first_vowel_idx] in SHORTEN:
        out[first_vowel_idx] = shorten(out[first_vowel_idx])
    return out

_PRETONIC = _rule(
    'gh.pretonic', 'Pretonic shortening: V̄ → V on unaccented first syllable', 'Vowels',
    _pretonic_shorten,
    requires=['accent'],
)


# ── Standing rules (post-Stage 1 pass) ────────────────────────────────────────

_STAND_LV_1  = _rule('gh.stand_lv_1',  'Kw→kʷ (standing, post S1)',          'Standing', _labiovelarize)
_STAND_BOK_1 = _rule('gh.stand_bok_1', 'Boukólos (standing, post S1)',        'Standing', _boukólos)


# ── Stage 2: syllabic resonant vocalization ───────────────────────────────────

def _syl_res_vocalize(toks: list[str], ctx: Context) -> list[str]:
    """Syllabic resonants → aR: r̥→ar, l̥→al, m̥→am, n̥→an. Adjacent glottal ˀ consumed."""
    RES = {'r̥': 'r', 'l̥': 'l', 'm̥': 'm', 'n̥': 'n'}
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        if is_syl_res(tok):
            res = RES[tok]
            prev = out[-1] if out else None
            nxt = toks[i + 1] if i + 1 < len(toks) else None

            # Consume adjacent glottal stop (laryngeal residue)
            if is_glottal(prev):
                out.pop()
                # Deleted one token before current → adjust accent if needed
                if ctx.accent_index is not None:
                    insert_at = len(out)  # position where 'a' will go
                    if ctx.accent_index > insert_at:
                        ctx.accent_index -= 1  # net: removed ˀ, +1 'a' = net 0 delta at this pos

            if nxt and is_glottal(nxt):
                i += 1  # skip following glottal
                # Will insert 'a' + res = +2 for the resonant, -1 for glottal = net +1
                if ctx.accent_index is not None and ctx.accent_index > len(out) + 1:
                    ctx.accent_index += 1

            # Insert 'a' + resonant (replace syllabic with two tokens)
            insert_at = len(out)
            out.extend(['a', res])

            # Update accent_index: if it pointed to this syllabic resonant,
            # it now points to the 'a' (the new nucleus)
            if ctx.accent_index is not None:
                if ctx.accent_index == i:
                    ctx.accent_index = insert_at  # points to 'a'
                elif ctx.accent_index > i:
                    ctx.accent_index += 1  # one extra token inserted

            i += 1
        else:
            out.append(tok)
            i += 1
    return out

_SYL_RES = _rule('gh.syl_res', 'Syllabic resonants → aR: r̥→ar, l̥→al, m̥→am, n̥→an', 'Syllabics', _syl_res_vocalize)


# ── Stage 2: glide changes ────────────────────────────────────────────────────

def _juwankos(toks: list[str], ctx: Context) -> list[str]:
    """ū → uw before vowel (Juwankos rule; hiatus glide insertion)."""
    out: list[str] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if tok == 'ū' and nxt and is_vowel(nxt):
            out.extend(['u', 'w'])
            # Inserted one extra token; update accent if after this position
            if ctx.accent_index is not None and ctx.accent_index > i:
                ctx.accent_index += 1
        else:
            out.append(tok)
        i += 1
    return out

_JUWANKOS = _rule('gh.juwankos', 'ū→uw before vowel (Juwankos / hiatus glide)', 'Fricatives', _juwankos)


# ── Stage 2: aspirate shift ───────────────────────────────────────────────────

_ASPIRATES = _rule(
    'gh.aspirates', 'Aspirates → voiced fricatives: bʰ→β, dʰ→ð, gʰ→ɣ, gʷʰ→ɣʷ', 'Fricatives',
    lambda toks, ctx: scan(toks, lambda t, i, ts:
        'β' if t == 'bʰ' else
        'ð' if t == 'dʰ' else
        'ɣ' if t == 'gʰ' else
        'ɣʷ' if t == 'gʷʰ' else t
    )
)


# ── Stage 2: s→z voicing ──────────────────────────────────────────────────────

def _s_voice(toks: list[str], ctx: Context) -> list[str]:
    """s → z between voiced sounds."""
    return scan(toks, lambda tok, i, ts: (
        'z' if tok == 's' and
               i > 0 and is_voiced(ts[i - 1]) and
               i + 1 < len(ts) and is_voiced(ts[i + 1])
        else tok
    ))

_S_VOICE = _rule('gh.s_voice', 's→z between voiced sounds', 'Fricatives', _s_voice)


# ── Stage 2: y→j (historical note; y normalized to j in normalize.py) ─────────

_Y_J = _rule(
    'gh.y_j', 'y→j: PIE palatal glide → Ghandwa j (note: applied in normalization)', 'Glides',
    lambda toks, ctx: scan(toks, lambda t, i, ts: 'j' if t == 'y' else t)
)


# ── Standing rules (post-Stage 2 pass) ────────────────────────────────────────

_STAND_LV_2  = _rule('gh.stand_lv_2',  'Kw→kʷ (standing, post S2)',  'Standing', _labiovelarize)
_STAND_BOK_2 = _rule('gh.stand_bok_2', 'Boukólos (standing, post S2)', 'Standing', _boukólos)


# ── Pipeline (ordered flat list) ──────────────────────────────────────────────

RULES: list[Rule] = [
    # Pre-stage
    _CENTUMIZE,
    _LABIOVELARIZE,
    _PIE_DELAB,
    # Stage 1: dentals
    _TTS,
    _SSC,
    _THORN,
    # Stage 1: laryngeals
    _H_COLOR,
    _H_VHV,
    _H_VH,
    _H_ADJ_V,
    _H_INIT_C,
    _H_BTW_C,
    _H_SURV,
    # Stage 1: consonants
    _VOICED_BTS,
    # Stage 1: vowels
    _OSTHOFF,
    _EW_OW,
    # Pretonic shortening (accent-dependent)
    _PRETONIC,
    # Standing filter (post Stage 1)
    _STAND_LV_1,
    _STAND_BOK_1,
    # Stage 2: syllabics
    _SYL_RES,
    # Stage 2: fricatives
    _JUWANKOS,
    _ASPIRATES,
    _S_VOICE,
    # Stage 2: glides (historical note)
    _Y_J,
    # Standing filter (post Stage 2)
    _STAND_LV_2,
    _STAND_BOK_2,
]
