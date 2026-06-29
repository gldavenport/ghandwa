# pdr_shapegen.py — "Shape-Alike" Proto-Dravidian Root Generator

last_updated: 2026-06-28

## What it does

`pdr_shapegen.py` generates phonologically well-formed but entirely invented
root and word shapes that follow Proto-Dravidian's phonotactics, for use as
raw material for the substrate/wanderword donor language. It is not a
Dravidian lexicon, a reconstruction tool, or a borrowing pipeline — it only
produces candidate shapes. Gloss assignment and linguistic review (the
ChatGPT-bulk / Claude-validate split discussed when this tool was built)
happen downstream, before anything from this tool is eligible for the
Ghandwa lexicon.

Nothing emitted by default is a real attested or reconstructed Dravidian
form. A hardcoded `ATTESTED` set excludes every real form gathered while
sourcing the phonological system (Southworth's 2005 crop vocabulary,
Krishnamurti's basic-vocabulary list, *cinki-wēr "ginger," etc.) so generated
output can't accidentally collide with them.

---

## Sourcing

The phonological system encoded here synthesizes Subrahmanyam (1983),
Zvelebil (1990), and Krishnamurti (2003) — the cumulative mainstream
Proto-Dravidian reconstruction, not a contested alternative. It deliberately
does **not** encode the genuinely disputed margins (nasal count, the
disputed laryngeal *H, anything Northern-branch/Brahui-Kurukh-Malto–specific)
— the generator only ever used the safe common core, which is why collapsing
the earlier separate "PSD1" variant of this tool back into one PDr-based
generator (see Decay layer, below) lost nothing.

Specific facts encoded:
- 10 vowels, no diphthongs (the *ai/*au sequences are *ay/*av).
- Consonant inventory by series (stops/nasals/laterals/rhotics/glides).
- Word-initial ban on alveolars and retroflexes.
- Root-final ban on *ñ.
- No gemination for *r/*ɻ.
- Krishnamurti's root-shape typology: V, CV, VC, CVC, each with short or
  long vowel (covering all eight of his root types).
- No prefixes or infixes — every root may itself already be a complete word;
  grammatical relations are added by suffixation, not modeled here.

---

## Invocation

From `tools/`:

```
python3 pdr_shapegen.py [options]
```

| Option | Description |
|---|---|
| `--n N` | Number of bare roots to generate (default 12) |
| `--template {V,CV,VC,CVC,all}` | Root-shape template, or `all` to mix (default `all`) |
| `--seed SEED` | RNG seed, for reproducible output |
| `--decay-stage {0,1,2,3}` | Apply the *c decay chain to this stage on any output containing *c (0=none, 3=full loss) |
| `--psd1` | Shorthand: apply both PSD1-defining changes (*c loss, *ṯ>*r) to all output |
| `--compounds N` | Also generate N root+classifier compounds |

---

## Reading the output

Bare roots print one per line. If a decay option changed the form, both the
underlying and surfaced forms are shown:

```
  ciw  ->  iw
  tuṯ  ->  tur
```

Compounds (`--compounds N`) print as `root-classifier`, structurally in the
role of *mām-kāy "mango" or *cinki-wēr "ginger root" — a specific root plus
a generated, equally novel generic classifier element.

---

## Decay layer (contact-stratum modeling)

`decay_c()`, `decay_t_hat()`, and `to_psd1()` are not corrections to the base
generator — they're an optional layer applied per item, used to simulate
*when* a borrowing happened relative to the donor language's own internal
sound changes:

- **stage 0** (no change): conservative donor, earliest plausible contact.
- **stage 1** (*c>s): donor mid-decay.
- **stage 2** (*c>s>h): donor further along.
- **stage 3** / `--psd1`: donor has completed the SD I shift (*c fully lost,
  *ṯ merged into *r) — the Telugu/South-Central branch is the empirically
  motivated place to model stage 1–2 as a stable, non-transitional donor
  dialect rather than just an intermediate step, since Krishnamurti notes
  the *c shift is completed in SD I but still in progress in SD II.

Generating the same root at multiple stages and treating them as separate
borrowing-wave doublets (rather than picking one "correct" donor form) is
the intended usage — see the *kinki-/sinki-/inki- discussion this tool grew
out of.

---

## Known limitations

- Sampling is uniform across each consonant/vowel class, and the long-vowel
  bias (0.35) is an arbitrary default, not derived from real frequency data.
  Both should be re-weighted once real distributions can be pulled from
  DEDR.
- The *ṯ/*r gemination contrast that some daughters (Malayalam) actually
  preserve is collapsed into a flat *ṯ→*r substitution for simplicity.
- No weapon vocabulary exists yet to validate against — neither Southworth's
  agricultural reconstruction nor Krishnamurti's basic-vocabulary list covers
  tools or weapons. That gap needs a direct DEDR lookup, not this generator.
- No NocoDB or lexicon write-back, and none is planned — see "What it does."
- One root/word per invocation's worth of output; no batch-file input.
