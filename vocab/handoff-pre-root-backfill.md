# Handoff: `lemma_1_pre_root` Backfill

**Date:** 2026-05-15  
**Input file:** `pre-root-backfill.tsv` (attached)  
**Entries to fill:** 189

---

## The Field

`lemma_1_pre_root` stores the PIE root underlying a Ghandwa lemma — **without** the leading `*`. Examples:

- PIE `*bʰer-` → field value `bʰer-`
- PIE `*h₃nebʰ-` → field value `h₃nebʰ-`

The value must match standard notation in LIV² (Rix 2001 / Kümmel 2023) for verbal roots, or the standard nominal/adjectival root used in EDPG (Kroonen 2013) and EDL (de Vaan 2008).

---

## Input File Columns

| Column | Content |
|---|---|
| `entry_id` | Unique ID — **do not change** |
| `lemma_1_gh_orth` | Ghandwa surface form |
| `gloss` | English gloss |
| `pos` | Part of speech |
| `entry_status` | `draft`, `hold`, or `canon` |
| `lemma_1_pre_orth` | PIE preform if known (41 entries have this) |
| `lemma_1_pre_root` | **← FILL THIS** |

---

## Two Tiers

### Tier 1 — `lemma_1_pre_orth` is populated (41 entries)

The PIE preform is known. Extract the root from the preform by stripping inflectional endings and derivational suffixes, reducing to the bare root with thematic vowel or zero-grade as appropriate.

Examples:
- `h₃nobʰeh₂` → `h₃nebʰ-`
- `suh₂l` → `sh₂ul-` (check LIV/EDPG for exact form)
- `kʷetwr̥ǵʰimos` → `kʷetwṓr` (ordinal; root is the cardinal numeral base)

### Tier 2 — no `lemma_1_pre_orth` (148 entries)

No preform is given. Identify the PIE root from the Ghandwa form and gloss using EDPG, EDL, LIV², Pokorny, or Wiktionary reconstruction pages.

Work the Ghandwa form backward through these correspondence rules:

| Ghandwa | PIE source |
|---|---|
| `v-` initial | `*w-` |
| `β-` | `*bʰ-` |
| `ð-` | `*dʰ-` |
| `ɣ-` | `*gʰ-` |
| `ɣv-` | `*gʷʰ-` |
| `-kv-` / `-gv-` | `*-kʷ-` / `*-gʷ-` |
| `-i-` in onset position | `*-j-` (glide) |
| internal `-ar-`/`-al-`/`-am-`/`-an-` | syllabic resonant `*r̥`/`*l̥`/`*m̥`/`*n̥` |
| long vowels (`ā`, `ē`, etc.) | may reflect laryngeal lengthening — check EDPG cognates |

---

## Special Categories

**`noun (name)` entries (58)** — proper names and epithets, many of them transparent compounds. Decompose to constituent roots; record as semicolon-delimited if two roots (e.g. `men-;bʰer-`). If the name is clearly a PGh innovation with no single PIE root, write `PGh`.

**Pronouns and particles (13)** — look up in Dunkel *LIPP* or Fortson §5 paradigm tables.

**Numerals (11)** — PIE numeral bases are well-attested; use standard reconstructions.

---

## Output Requirements

Return the same TSV with `lemma_1_pre_root` filled. Also add a `confidence` column with one of: `high` / `medium` / `low` / `uncertain`.

**Rules:**
- Leave `lemma_1_pre_root` blank if genuinely uncertain — do not guess.
- If a form is a transparent internal compound or PGh derivation with no single PIE root, write `compound` or `PGh`.
- Do not change `entry_id`, `lemma_1_gh_orth`, or any other existing column.
- Do not add or remove rows.

---

## Primary References

Kroonen EDPG, de Vaan EDL, Rix + Kümmel LIV², Matasović EDPC. Wiktionary PIE reconstructions are acceptable for cross-checking but not as sole source.
