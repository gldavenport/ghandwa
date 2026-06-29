# `pie_transformer` — Internals

**Last updated:** 2026-06-17  
**Package location:** `tools/pie_transformer/`  
**Entry point:** `python3 -m pie_transformer`

---

## Overview

`pie_transformer` is a Python 3.10+ CLI package that takes a PIE preform as input and applies chronologically ordered phonological rules to produce output for Ghandwa, its daughters, and the Wékʷos/Seldanic/Anatolian proto-language pipelines. It replaces the earlier `pie-2-ghandwa.jsx` as the authoritative transformer.

The pipeline is:

```
raw string
  → normalize()        strip *, expand shorthands, extract accent position
  → tokenize()          split into phoneme tokens
  → run()                apply ordered rules, track context (accent index)
  → render()            convert tokens to orth / citation / IPA output
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
Registry, hierarchy, and chaining logic for named pipelines.

- `ALL_PIPELINES` — list of valid pipeline names: `ghandwa`, `ghandwa-daughter-a`, `ghandwa-daughter-b`, `ghandwa-daughter-c`, `proto-anatolian`, `proto-seldanic`, `wekwos-old`, `wekwos-neo`.
- `run(name, tokens, context, input_form, trace_mode)` — dispatches to the correct pipeline module.
- **`PIPELINE_PARENTS`** — `dict[str, str | None]` mapping each pipeline to its mother language, or `None` for roots. Drives both pipeline chaining (which upstream pipeline's tokens feed a downstream pipeline) and the `--all` display tree.
- **`PIPELINE_IS_RECONSTRUCTION`** — `dict[str, bool]`. `True` for proto-languages (Wékʷos, Seldanic, Anatolian); `False` for Ghandwa and its daughters. Drives the default `*`-prefixing behaviour of citation-mode rendering.
- **`pipeline_display_order()`** — returns `(pipeline_name, depth)` pairs in tree order (root, then its children at depth 1) for `--all` display. Roots are listed in a fixed order (`ghandwa`, `proto-anatolian`, `proto-seldanic`, `wekwos-old`); children are alphabetized under each root.
- Chaining (`_run_chained`): Wékʷos-Neo is downstream of Wékʷos-Old; daughters A/B/C are downstream of `ghandwa`. The upstream pipeline's final token stream feeds the downstream pipeline directly — re-tokenization does not occur. Traces from both legs are concatenated.

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

### `pipelines/wekwos_old.py`, `pipelines/wekwos_neo.py`
Provisional. Rule lists exist but have not been verified against expected outputs. Wékʷos-Neo runs downstream of Wékʷos-Old.

### `pipelines/daughter_a.py`, `pipelines/daughter_b.py`, `pipelines/daughter_c.py`
Daughter pipelines, downstream of `ghandwa`. A and B implement Stage 2 only (Stage 3 unspecified). C implements Stage 2C and Stage 3C fully.

### `render.py`
Converts a final token list to output strings, in three independent tiers:

| Tier | Mode | Present for | Absent for |
|---|---|---|---|
| Orthography | `orth` | attested/constructed languages with a designed script: `ghandwa` and its daughters | proto-languages (`wekwos-old`, `wekwos-neo`, `proto-seldanic`, `proto-anatolian`) — returns `None` |
| Citation | `citation` | all pipelines | — |
| IPA | `ipa` | all pipelines with a syllabifiable token stream | `proto-anatolian` (provisional; returns raw token join, not syllabified) |

`render(pipeline, mode, tokens, accent_index, star=None)` is the dispatcher. `mode` is one of `orth`, `citation`, `ipa`, `tokens`. Returns `str | None` — `None` signals the tier is absent for that pipeline; callers display `—`.

**`apply_accent_mark(tokens, accent_index)`** — inserts U+0301 combining acute on the token at `accent_index`, NFC-normalizes (so `a+´→á`). Called before any tier-specific rendering.

**Orthographic renderers** are pipeline-specific conversion tables applied to the token stream after boundary-stripping:

| Pipeline | Conversions |
|---|---|
| `ghandwa` | `kʷ→kv`, `gʷ→gv`, `ɣʷ→ɣv`, `j→i`, `w→v` |
| `ghandwa-daughter-a` | `ɸ→f`, `θ→þ`, `x→h`, `xʷ→hv`, `j→i`, `w→v` |
| `ghandwa-daughter-b` | inherits Ghandwa orthography wholesale (delegates to `_ghandwa_orth`) |
| `ghandwa-daughter-c` | `ʁ→ŕ`, `j→i`, `w→v` (labiovelars already resolved by Stage 2C) |

`ˀ` (surviving laryngeal) passes through unchanged in orth/citation — it is a diagnostic tracer, not a real surface segment.

**Citation renderer** (`_citation_render`) is shared across all pipelines: converts labiovelar digraphs (`kʷ→kw`, `gʷ→gw`, `ɣʷ→ɣw`) and leaves everything else (β, ð, ɣ, j, w, vowels) unchanged. Prefixes `*` when `star=True` (or when `star=None` and `PIPELINE_IS_RECONSTRUCTION[pipeline]` is `True`). This is the Germanic-citation-style convention shared by most IE proto-language scholarship — easy to type, easy to search, distinct from both the orthography and the IPA.

**IPA renderer** (`_ipa_syllabified`) is shared across all pipelines except `proto-anatolian`: onset-maximization syllabification (`_syllabify` in `pipelines/_common.py`), syllables joined with `.`, stressed syllable prefixed with `ˈ`, wrapped in `/…/`. Phonological, not phonetic (`/n/` stays `/n/` before velars).

**`get_warnings(tokens)`** — returns warning strings for the token stream. Checks for: unresolved `ˀ`; CCC consonant cluster (glides excluded from the count, as post-vocalic `j`/`w` are vocalic).

### `reports.py`
Formats `DerivationResult` objects for output. All three tiers (orth, citation, ipa) are computed and shown regardless of the `mode` parameter — `mode` is currently accepted but unused (see Known Gaps).

- `format_terminal()` — compact mode (`--all`): one line per pipeline, indented by tree depth, with fixed-width orth/citation columns followed by IPA (`—` for absent orth). Non-compact mode: a labeled three-line block (`orth:` / `citation:` / `ipa:`) plus pipeline name, status, and optional derivation trace.
- `format_markdown()` — Markdown block per result with `**Orth:**` (omitted if absent), `**Citation:**`, `**IPA:**`, and an optional derivation trace table.
- `result_to_tsv_row()` — flat dict for TSV output. Computes `orth_match` and `ipa_match` by NFC-comparing generated forms against `expected_orth`/`expected_ipa`.
- `result_to_jsonl()` — JSON line with `generated_orth`, `generated_citation`, `generated_ipa`.

### `tsv_io.py`
Reads and writes the transformer-ready TSV format.

- `read_lexicon()` — reads the human lexicon TSV (`vocab/lexicon.tsv`). CRLF-safe, NFC-normalizes all fields, resolves columns dynamically by name. Source form precedence: `lemma_1_pre_ety` > `lemma_1_pre_root`.
- `read_transformer_tsv()` / `write_transformer_tsv()` — reads/writes the intermediate transformer format (separate from the human lexicon).
- `TRANSFORMER_HEADER` — canonical column list: `item_id`, `source_form`, `pipeline`, `expected_orth`, `expected_ipa`, `notes`, `generated_orth`, `generated_citation`, `generated_ipa`, `generated_tokens`, `result_status`, `orth_match`, `ipa_match`, `blocked_stage`, `blocked_rule`, `blocked_form`, `trace_path`.

### `cli.py`
Four subcommands:

- **`form`** — transform a single PIE string. Clears the screen by default (`--no-clear` to suppress). Optional `--trace changed` or `--trace full` to show the derivation. `--pipeline` selects the target; `--all` runs every pipeline using `pipeline_display_order()` so daughters/Wékʷos-Neo display indented under their mothers. `--mode` chooses among `orth`, `citation`, `ipa`, `tokens` (default `orth`) — see Known Gaps re: vestigial behaviour in compact/markdown display.
- **`batch`** — transform a transformer-ready TSV. Writes output TSV, optional Markdown report and JSONL.
- **`paradigm`** — generate a noun paradigm table from nominative/genitive singular forms.
- **`extract-lexicon`** — reads the human lexicon TSV, extracts source forms and expected forms, writes a transformer-ready TSV for use with `batch`.

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
  render('ghandwa', 'orth')     →  apply_accent → 'wálkʷos' → orthographic → 'válkvos'
  render('ghandwa', 'citation') →  apply_accent → 'wálkʷos' → digraph     → 'wálkwos'
  render('ghandwa', 'ipa')      →  apply_accent → 'wálkʷos' → syllabified → '/ˈwal.kʷos/'
```

For a proto-language pipeline (e.g. `wekwos-old`), `render(pipeline, 'orth', …)` returns `None` — there is no script — and citation carries the `*` prefix: `*wlákwos`.

---

## Known Gaps

- IPA renderer for `proto-anatolian` is provisional: returns the raw token join, not syllabified. Vocalism in that pipeline (e.g. unresolved `l̥`) is not yet stable enough to syllabify reliably.
- Wékʷos-Old/Wékʷos-Neo pipelines provisional and untested.
- Daughter pipelines A and B: Stage 3 not yet specified. Daughter C: Stage 3 implemented.
- `pyproject.toml` not written; package must be run in-place.
- `--mode` flag is parsed and passed to `format_terminal`/`format_markdown`, but both functions currently ignore it and always display all three tiers (orth, citation, ipa). The flag is reserved for a future single-tier display mode.
- **Accent-tracking:** Five distinct hand-rolled accent-index patterns exist across pipeline rules; no shared API. Refactor deferred pending test coverage. See `docs/handoff-accent-tracking-v2.md` for pattern catalog, equivalence proofs, proposed `shift_for_change`/`relocate` API, and required test suite.
