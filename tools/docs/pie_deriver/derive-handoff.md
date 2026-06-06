# Derivator — Implementation Handoff

last_updated: 2026-06-01

Authoritative design: **`derive-spec.md`** (read it first; this note only sequences the work).

---

## State

Spec is complete and reviewed. Both ChatGPT queries (Tier 2 input restrictions; Yates on m-stems) are **resolved and folded into the spec** — no pending data. Tier 1 is ready to build. Tier 2 is implemented in a second phase (table now re-tiered to attested bases; §5).

Final m-stem cluster (Tier 1): `MenNounR` (neuter *-mn̥*, root full grade, root accent), `MenNounAnim` (ID *-mōn-*, mobile), `MonNounPrim` (primary deverbal *-món-*, zero-grade, suffix accent). The old `MenNounS` was dropped per Yates.

---

## First action: extract `pie_core` (spec §11)

One atomic refactor. **Re-pull and re-grep before acting** — the inventory below was gathered from a possibly-stale clone; treat it as a guide, not gospel. Filesystem MCP targets `/Users/g_/Documents/GitHub/ghandwa/`; the local working copy is authoritative and may have uncommitted changes to preserve.

Steps:
1. Create `tools/pie_core/` with `tokens.py`, `tokenize.py`, `normalize.py` moved verbatim, plus `__init__.py`. (`tokenize.py`'s internal `from .tokens import …` stays relative within `pie_core`.)
2. Redirect transformer import sites (below) from `.tokens`/`.tokenize`/`.normalize` to `pie_core.…`.
3. Decide test placement: move `test_tokenize.py` / `test_normalize.py` to `pie_core/tests/` (cleaner) or leave them and redirect their imports. Either way, fix the absolute-import lines in `test_pipelines.py`.
4. Run the suite → confirm green: `python3 -m unittest discover tools/pie_transformer/tests` (and `pie_core/tests` if moved).
5. Build `tools/derive.py` (Tier 1) against `pie_core`.

Test, then write back only verified files. Gary commits — Claude cannot push.

### Import sites to redirect (verified against clone; re-grep to confirm)

```
cli.py:24        from .normalize import normalize
cli.py:25        from .tokenize import tokenize, accent_char_pos_to_token_index, tokens_to_string
rule.py:106      from .tokenize import tokens_to_string          # local, avoids circular import
render.py:21     from .tokenize import tokens_to_string
render.py:318    from .tokens import is_consonant, is_glottal, GLIDES
interactive.py:126  from .normalize import normalize
interactive.py:127  from .tokenize import tokenize, accent_char_pos_to_token_index
reports.py:19    from .tokenize import tokens_to_string
pipeline.py:25   from .tokenize import tokens_to_string
tests/test_tokenize.py:9-10    from ..tokenize / ..normalize
tests/test_normalize.py:10     from ..normalize import normalize, NormalizeResult
tests/test_pipelines.py:23-24, 80, 85   from ..tokenize / ..normalize (relative)
tests/test_pipelines.py:379-380, 392-393   from pie_transformer.tokenize / .normalize (ABSOLUTE — must redirect to pie_core)
tokenize.py:16   from .tokens import PHONEME_PATTERNS, BOUNDARIES   # stays internal to pie_core
```

Also check `tsv_io.py` for `strip_crlf` (defined in `normalize.py`); did not surface in the import grep — verify directly.

`render.py` needs `is_consonant`, `is_glottal`, `GLIDES` from `pie_core.tokens` — confirm those exports survive the move (they exist in current `tokens.py`).

---

## Then: build Tier 1 `derive.py`

Per spec §2–§7. Key points that bit us during design, so the implementer doesn't relitigate:

- **Input** via `pie_core.normalize` → `pie_core.tokenize`; operate on the token list, not the string (§3.1).
- **Zero grade** is sonority-based on the post-deletion token sequence: liquid/nasal → syllabic; glide → vowel (w→u, y/j→i); no resonant → bare cluster (valid, don't flag); flag only genuine ambiguity (§3.2). This was the single biggest error in earlier drafts — onset-cluster resonants (*ǵneh₃-* → *ǵn̥h₃-*) and glide vocalization must work.
- **Reduplication**: present = i-reduplication (`C₁i-`); perfect = e-reduplication (`C₁e-`). Don't conflate (§3.3).
- **Stem vs. citation**: every pattern emits both; vowel-initial suffix on a thematic stem deletes the thematic vowel (§3.6).
- **Accent placement** by `accent_type` label; single acute per form, encoded as `pie_core.normalize` expects so forms round-trip later (§3.7).
- **Semantics** = flat function-label lookup + chain display; no slot-filling (§7).
- Output PIE only; markdown export to `lexicon/derivata/{sanitized-egrade}-derivata.md`.

`MonNounPrim` is part of the final Tier 1 m-stem cluster (zero-grade root + *-món-*, suffix accent); `MenNounR` is root full grade, not zero-grade — don't regress it.

---

## After Tier 1 ships

Build Tier 2 from the re-tiered §5 table (adjective-input vs. nominal-input bases already resolved). High-yield default + `--all`. `ComparativeTero` and `SuperlativeMm̥o` are catalog-only — do not generate them.
