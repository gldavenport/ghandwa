"""
pdr_shapegen.py -- "Shape-alike" Proto-Dravidian-style root generator.

Encodes the PDr phonological/phonotactic facts established in the chat
session that produced this tool: vowel system, consonant inventory, and
root-shape typology per Subrahmanyam 1983 / Zvelebil 1990 / Krishnamurti
2003 (via Wikipedia's synthesis and Britannica's summary of Krishnamurti's
root-shape typology). See tools/docs/pdr_shapegen/pdr_shapegen.md for
sourcing detail, known limitations, and the contact-stratum design intent.

Produces NOVEL phonological shapes only -- nothing emitted by default is a
real attested or reconstructed Dravidian form. Real forms gathered during
development are hardcoded into ATTESTED and actively excluded so output
can't accidentally collide with them.

This is a generation/exploration aid, not a lexicon pipeline. Output is
unvetted candidate shapes -- gloss assignment and linguistic review happen
downstream, before anything from this tool is eligible for the lexicon.
"""

import argparse
import random

VOWELS_SHORT = ['a', 'i', 'u', 'e', 'o']
VOWELS_LONG  = ['ā', 'ī', 'ū', 'ē', 'ō']

STOPS    = {'labial': 'p', 'dental': 't', 'alveolar': 'ṯ', 'retroflex': 'ʈ', 'palatal': 'c', 'velar': 'k'}
NASALS   = {'labial': 'm', 'dental': 'n', 'alveolar': 'ṉ', 'retroflex': 'ɳ', 'palatal': 'ɲ'}
LATERALS = {'dental': 'l', 'retroflex': 'ɭ'}
RHOTICS  = {'alveolar': 'r', 'retroflex': 'ɻ'}
GLIDES   = {'labial': 'w', 'palatal': 'y'}

ALL_CONSONANTS = list(STOPS.values()) + list(NASALS.values()) + list(LATERALS.values()) \
                 + list(RHOTICS.values()) + list(GLIDES.values())

# Word-initial: alveolars and retroflexes excluded (Krishnamurti 2003)
RESTRICTED_INITIAL = {'ṯ', 'ʈ', 'ɳ', 'ɭ', 'ɻ', 'ṉ'}
INITIAL_CONSONANTS = [c for c in ALL_CONSONANTS if c not in RESTRICTED_INITIAL]

# Root-final: *ñ excluded (Krishnamurti's root-shape typology)
RESTRICTED_FINAL = {'ɲ'}
FINAL_CONSONANTS = [c for c in ALL_CONSONANTS if c not in RESTRICTED_FINAL]

# Gemination: *r and *ɻ occur only singly, never geminate
NO_GEMINATE = {'r', 'ɻ'}

ROOT_TEMPLATES = ['V', 'CV', 'VC', 'CVC']

# Real forms gathered during development -- excluded from "novel" output
ATTESTED = {
    'koḷ', 'pacVṯ', 'pacVl', 'uẓuntu', 'min', 'avarai', 'tuvar', 'connal', 'kotV',
    'ārVk', 'arVk', 'kampu', 'irak', 'kūli', 'wariñci', 'cuv', 'ñēral', 'pīr',
    'akVce', 'parutti', 'cīntu', 'uḷḷi', 'waẓVtV', 'nūv', 'cetVkk', 'boyVl',
    'cintta', 'tuḷacV', 'maran', 'kāy', 'kān', 'kāṭu', 'pul', 'mā', 'kurVc',
    'puli', 'eli', 'pāmpu', 'naHay', 'mīn', 'cinki', 'wēr', 'ūr',
}


# NOTE: sampling below is uniform across each consonant/vowel class, and
# long_bias=0.35 is an arbitrary default -- neither is derived from real
# Dravidian frequency data. Re-weight both once real distributions can be
# pulled from DEDR (Burrow & Emeneau); see Known Limitations in
# tools/docs/pdr_shapegen/pdr_shapegen.md.

def pick_vowel(long_bias=0.35):
    return random.choice(VOWELS_LONG if random.random() < long_bias else VOWELS_SHORT)


def gen_root(template=None, allow_geminate=True):
    template = template or random.choice(ROOT_TEMPLATES)
    v = pick_vowel()
    if template == 'V':
        return v
    if template == 'CV':
        return random.choice(INITIAL_CONSONANTS) + v
    if template == 'VC':
        return v + random.choice(FINAL_CONSONANTS)
    if template == 'CVC':
        c1 = random.choice(INITIAL_CONSONANTS)
        c2 = random.choice(FINAL_CONSONANTS)
        if allow_geminate and c2 not in NO_GEMINATE and random.random() < 0.15:
            return f"{c1}{v}{c2}{c2}"
        return f"{c1}{v}{c2}"


def generate_batch(n=10, template=None, seen=None):
    """template=None or 'all' mixes templates randomly per item."""
    seen = seen if seen is not None else set()
    tmpl = None if template in (None, 'all') else template
    out = []
    tries = 0
    while len(out) < n and tries < n * 50:
        tries += 1
        r = gen_root(tmpl)
        key = r.lower()
        if key in ATTESTED or key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


# ---------------------------------------------------------------------------
# Optional decay layer: apply selectively, per item, to simulate which
# contact stratum a given borrowing reflects -- not a fixed target stage.
# ---------------------------------------------------------------------------

def decay_c(form, stage):
    """
    *c decay chain (PDr > SD I/PSD1, completed; still in progress in SD II
    per Krishnamurti). stage 0 = conservative *c (no change), 1 = *c>s,
    2 = *c>s>h, 3 = *c>s>h>zero (the SD I / PSD1 endpoint).
    """
    chain = {0: 'c', 1: 's', 2: 'h', 3: ''}
    return form.replace('c', chain[stage])


def decay_t_hat(form):
    """*ṯ > *r merger -- the other PSD1-defining change."""
    return form.replace('ṯ', 'r')


def to_psd1(form):
    """Convenience: apply both PSD1-defining changes at once."""
    return decay_t_hat(decay_c(form, 3))


def main():
    p = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    p.add_argument('--n', type=int, default=12, help='number of bare roots to generate (default 12)')
    p.add_argument('--template', choices=['V', 'CV', 'VC', 'CVC', 'all'], default='all',
                    help="root-shape template, or 'all' to mix (default all)")
    p.add_argument('--seed', type=int, default=None, help='RNG seed, for reproducible output')
    p.add_argument('--decay-stage', type=int, choices=[0, 1, 2, 3], default=0,
                    help='apply the *c decay chain to this stage on output containing *c '
                         '(0=none, 3=PSD1 endpoint; --psd1 is shorthand for both changes at once)')
    p.add_argument('--psd1', action='store_true',
                    help='apply both PSD1-defining changes (*c loss, *ṯ>*r) to all output')
    p.add_argument('--compounds', type=int, default=0,
                    help='also generate N root+classifier compounds (role of *mām-kāy / *cinki-wēr)')
    args = p.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    seen = set()
    roots = generate_batch(args.n, args.template, seen)

    def apply_stage(form):
        if args.psd1:
            return to_psd1(form)
        if args.decay_stage:
            return decay_c(form, args.decay_stage)
        return form

    print(f"=== {args.n} candidate roots (template={args.template}) ===")
    for r in roots:
        out = apply_stage(r)
        print(f"  {r}" + (f"  ->  {out}" if out != r else ""))

    if args.compounds:
        classifiers = generate_batch(max(4, args.compounds // 2), 'CV', seen)
        compound_roots = generate_batch(args.compounds, 'CVC', seen)
        print(f"\n=== {args.compounds} candidate root+classifier compounds ===")
        for r in compound_roots:
            cl = random.choice(classifiers)
            r_out, cl_out = apply_stage(r), apply_stage(cl)
            print(f"  {r_out}-{cl_out}")


if __name__ == '__main__':
    main()
