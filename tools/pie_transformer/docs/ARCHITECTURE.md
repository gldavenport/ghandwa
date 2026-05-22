# `pie_transformer` — Internals

**Last updated:** 2026-05-15  
**Package location:** `tools/pie_transformer/`  
**Entry point:** `python3 -m pie_transformer`

---

## Overview

`pie_transformer` is a Python 3.10+ CLI package that takes a PIE preform as input and applies chronologically ordered phonological rules to produce surface forms for Ghandwa and (provisionally) Wékʷos. It replaces the earlier `pie-2-ghandwa.jsx` as the authoritative transformer.

The pipeline is:

```
raw string
  → normalize()        strip *, expand shorthands, extract accent position
  → tokenize()         split into phoneme tokens
  → run()              apply ordered rules, track context (accent index)
  → render()           convert tokens to orthographic / IPA output
```

---

## Module Reference

### `tokens.py`
Defines the token inventory and category sets used throughout the package. A token is a string representing one phonological segment: single characters (`a`, `t`, `s`) or multi-character symbols (`kʷ`, `gʷʰ`, `h₂`, `r̥`, `ɣʷ`, etc.).

Key exports:
- `PHONEME_PATTERNS` — ordered list of multi-character tokens, longest first. Used by the tokenizer for longest-match scanning.
- Category sets: `VOWELS`, `SHORT_VOWELS`, `LONG_VOWELS`, `SYL_RES`, `DENTALS`, `PLAIN_VELARS`, `LIQUIDS`, `NASALS`, `GLIDES`, `SONORANTS`, `VOICED_C`, `LARYNGEALS`, `BOUNDARIES`
- Predicate functions: `is_vowel()`, `is_consonant()`, `is_dental()`, etc.
- Helper maps: `LENGTHEN`, `SHORTEN`, `DEVOICE`, `DEASPIRATE`, `NASALIZE`

`is_consonant()` is defined negatively: anything that is not a vowel, laryngeal, glottal stop (`ˀ`), or boundary.

### `normalize.py`
Prepares a raw PIE string for tokenization.

Steps in order:
1. **NFC normalization** — mandatory first step; Apple Numbers exports NFD.
2. **Strip leading `*`** — records `had_star=True` on the result.
3. **Extract accent** — walks the NFD decomposition looking for combining acute (U+0301), grave (U+0300), or circumflex (U+0302). Records the NFC character offset of the accented segment as `accent_char_pos`. Strips the diacritic from the clean string. Combining acute on a **consonant** (e.g. `ǵ`, `ḱ`) is treated as a palatalization diacritic and kept. Only combining acute on a **vowel** or **syllabic resonant** (identified by U+0325 ring-below in the cluster) is treated as lexical accent.
4. **Expand shorthands** — converts input notation conventions to token-ready strings: long vowels (`aa→ā`), laryngeals (`H1→h₁`), digraphs (`bh→bʰ`, `dh→dʰ`, `gh→gʰ`, `gwh→gʷʰ`), labiovelars (`kw→kʷ`, `gw→gʷ`), syllabic resonants (`r_→r̥` etc.), glides (`y→j`, `i̯→j`).

Returns a `NormalizeResult` dataclass with fields `clean`, `accent_char_pos`, `had_star`.

### `tokenize.py`
Splits a normalized string into a list of tokens using longest-match against `PHONEME_PATTERNS`, falling back to single characters.

Also produces `char_offsets`: a parallel list mapping each token to its starting character position in the input string. Used by `accent_char_pos_to_token_index()` to convert the character-level accent position from `normalize()` into a token-level index.

### `rule.py`
Defines the rule and pipeline execution model.

- **`Context`** — mutable object carrying `accent_index: int | None` (zero-based token index of the accented segment). Passed to every rule function; rules that change the token count must update it.
- **`Rule`** — dataclass with `id`, `name`, `stage`, `requires`, and `apply`. `apply` is a function `(tokens, context) → tokens`. `requires=["accent"]` causes the rule to be skipped (status `blocked_missing_accent`) if `context.accent_index is None`.
- **`run_pipeline()`** — iterates the rule list, applies each rule, records a `TraceRow` for each step where the token stream changed. Catches exceptions per-rule. Returns a `DerivationResult`.
- **`DerivationResult`** — holds `status`, `final_tokens`, `trace`, `final_accent_index`, and fields for error/blockage reporting.
- **`scan()`** — helper for rule functions that apply a per-token transformation: iterates tokens, calls a function `(token, index, token_list) → token`, returns the modified list.

### `pipeline.py`
Registry and dispatcher for named pipelines.

- `ALL_PIPELINES` — list of valid pipeline names: `ghandwa`, `old-wekwos`, `neo-wekwos`, `daughter-a`, `daughter-b`, `daughter-c`.
- `run(name, tokens, context, input_form, trace_mode)` — dispatches to the correct pipeline module.
- Neo-Wékʷos chains downstream of Old-Wékʷos: `run()` calls `_run_chained()` which runs Old-Wékʷos first, then feeds its output tokens and context into the Neo-Wékʷos rule list.
- Daughter pipelines return `not_implemented` status immediately.

### `pipelines/ghandwa.py`
The Ghandwa rule list. Rules are flat objects in chronological order:

| Stage | Rules |
|---|---|
| Pre-stage | Centumize palatals; labiovelarize `Kw→Kʷ`; PIE-internal delabialization `Kʷ→K / {u,ū,w}_ and _{u,ū,w}` |
| Stage 1: Dentals | `TT→ss`; `ssC→sC`; thorn clusters `TK→KT` |
| Stage 1: Laryngeals | H coloring (A/B/C rules); H loss in various environments; surviving H → `ˀ` |
| Stage 1: Consonants | Voiced obstruent → voiceless before `t`/`s` (covers b, d, g, gʷ and aspirated variants) |
| Stage 1: Vowels | Osthoff's Law; `ew→ow` |
| Stage 1: Accent | Pretonic shortening (requires accent) |
| Standing ×1 post-S1 | `Kw→Kʷ`; Ghandwa Boukólos `Kʷ→K / _{C,w,u,ū}` |
| Stage 2: Syllabics | `r̥→ar`, `l̥→al`, `m̥→am`, `n̥→an`; accent index updated |
| Stage 2: Fricatives | Juwankos (`ū→uw/_V`); aspirates → voiced fricatives (`bʰ→β`, `dʰ→ð`, `gʰ→ɣ`, `gʷʰ→ɣʷ`); `s→z` between voiced segments |
| Stage 2: Glides | `y→j` (no-op after normalization) |
| Standing ×1 post-S2 | Same as post-S1 |

**Boukólos:** Two distinct rules cover labiovelar delabialization. The PIE-internal rule fires once at pre-stage and is bidirectional. The Ghandwa Boukólos fires only as a standing rule (post-S1, post-S2), is forward-only, and has a broader environment including any following consonant. Syllabic resonants do not trigger the Ghandwa rule.

**Dental clusters:** `TT→ss` covers dental+dental only. Dental+s goes through the voiced-before-ts devoicing rule instead, yielding `ts` (not `ss`).

### `pipelines/old_wekwos.py`, `pipelines/neo_wekwos.py`
Provisional. Rule lists exist but have not been verified against expected outputs. Neo-Wékʷos runs downstream of Old-Wékʷos.

### `pipelines/daughters.py`
Stubs only. Returns `not_implemented` for all three daughter pipelines (A, B, C).

### `render.py`
Converts a final token list to a display string.

**`apply_accent_mark(tokens, accent_index)`** — inserts U+0301 combining acute on the token at `accent_index`, NFC-normalizes (so `a+´→á`). Called before rendering.

**`render(pipeline, mode, tokens, accent_index)`** — dispatcher. Modes:
- `surface` — orthographic form. For Ghandwa: applies the conversion table below, strips boundaries.
- `ipa` — IPA form. For Ghandwa: tokens joined and wrapped in `/…/`. Syllabification and `ˈ` stress mark are not yet implemented (see `handoff-ipa-syllabifier.md`).
- `tokens` — raw token join for debugging.

**Ghandwa orthographic conversions:**

| Token | Orthography |
|---|---|
| `kʷ` | `kv` |
| `gʷ` | `gv` |
| `ɣʷ` | `ɣv` |
| `j` | `i` |
| `w` | `v` |
| all others | unchanged |

`ˀ` (surviving laryngeal) passes through in both modes — it is a diagnostic tracer, not a real surface segment.

**`get_warnings(tokens)`** — returns warning strings for the token stream. Checks for: unresolved `ˀ`; CCC consonant cluster (glides excluded from the count, as post-vocalic `j`/`w` are vocalic).

### `reports.py`
Formats `DerivationResult` objects for output.

- `format_terminal()` — single-line header showing orthographic and IPA forms side by side, followed by pipeline name, blockage/error info if any, and optional derivation trace.
- `format_markdown()` — Markdown table format for report documents.
- `result_to_tsv_row()` — flat dict for TSV output. Computes `surface_match` by NFC-comparing generated surface against `expected_surface`.
- `result_to_jsonl()` — JSON line for machine-readable output.

### `tsv_io.py`
Reads and writes the transformer-ready TSV format.

- `read_lexicon()` — reads the human lexicon TSV (`vocab/lexicon.tsv`). CRLF-safe, NFC-normalizes all fields, resolves columns dynamically by name. Source form precedence: `lemma_1_pre_root` > `lemma_1_pre_ety`.
- `read_transformer_tsv()` / `write_transformer_tsv()` — reads/writes the intermediate transformer format (separate from the human lexicon).
- `TRANSFORMER_HEADER` — the canonical column list for transformer TSV output.

### `cli.py`
Three subcommands:

- **`form`** — transform a single PIE string. Clears the screen by default (`--no-clear` to suppress). Optional `--trace changed` or `--trace full` to show the derivation. `--pipeline` selects the target; `--all` runs all pipelines.
- **`batch`** — transform a transformer-ready TSV. Writes output TSV, optional Markdown report and JSONL.
- **`extract-lexicon`** — reads the human lexicon TSV, extracts source forms and expected surfaces, writes a transformer-ready TSV for use with `batch`.

---

## Data Flow: Single Form

```
"*wĺ̥kʷos"
  normalize()  →  clean='wl̥kʷos', accent_char_pos=1, had_star=True
  tokenize()   →  ['w', 'l̥', 'kʷ', 'o', 's'], char_offsets=[0,1,3,…]
                  accent_index=1  (token 'l̥' at char 1)
  Context(accent_index=1)
  run('ghandwa', tokens, ctx, …)
    pre-stage:   labiovelarize → ['w','l̥','kʷ','o','s']
    stage 2:     l̥→al → ['w','a','l','kʷ','o','s'], accent_index→2 ('a')
  DerivationResult(final_tokens=['w','á','l','kʷ','o','s'], final_accent_index=2)
  render('surface') →  apply_accent → 'wálkʷos' → orthographic → 'válkʷos'
  render('ipa')     →  apply_accent → 'wálkʷos' → '/wálkʷos/'
```

---

## Known Gaps

- IPA syllabifier and `ˈ` stress mark not implemented. See `docs/handoff-ipa-syllabifier.md`.
- Old/Neo Wékʷos pipelines provisional and untested.
- Daughter pipelines A and B: Stage 3 not yet specified. Daughter C: Stage 3 implemented.
- IPA renderers for Wékʷos return `renderer_missing`.
- `pyproject.toml` not written; package must be run in-place.
- `--mode` flag parsed but ignored in `form` command; both output modes always shown.
- **Accent-tracking:** Five distinct hand-rolled accent-index patterns exist across pipeline rules; no shared API. Refactor deferred pending test coverage. See `docs/handoff-accent-tracking-v2.md` for pattern catalog, equivalence proofs, proposed `shift_for_change`/`relocate` API, and required test suite.
