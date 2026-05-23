# Ghandwa: Notation — Workflow and Project Conventions

---
last_updated: 2026-05-22T00:00-04:00
changelog:
  - 2026-05-22T00:00-04:00 | — | Split file. Grammar-relevant content (§§1–6, 8–9: script layers, diacritics, letter inventory, worked examples, labiovelar notation, glide/semivowel conventions, Sharpscript long vowels) moved to `docs/grammar/ch1-introduction/notation.md`. This file retains workflow and project conventions only (§§7, 10–15).
  - 2026-05-15T00:00-04:00 | — | Added §14 (Transformer Input Normalization). Added §15 (Ghandwa Orthographic Conventions in Transformer Output).
  - 2026-05-05T00:00-04:00 | stub sections added | Added §12 TODO stub (doublets/dialectal variants framework) and §13 TODO stub (Sophomore list gap analysis).
  - 2026-04-13T00:00-04:00 | 204 lines | Added §8–§11.
  - 2026-03-22T18:00-04:00 | 139 lines | Added §7 Lexicon Entry Status Pipeline.
  - 2026-03-14 | 129 lines | Converted from `ghandwa_notation.docx`.
---

> **Script, transliteration, IPA, and orthographic conventions** (letter inventory, diacritics, labiovelar notation, glide/semivowel conventions, Sharpscript long vowels) are in `docs/grammar/ch1-introduction/notation.md`.

Working reference document — workflow conventions for lexicon management, document authoring, and transformer I/O.

---

## 7. Lexicon Entry Status Pipeline

Every entry in the lexicon TSV carries an `entry_status` value. The four values form a pipeline with one side lane:

```
stub → draft → canon
           ↘ hold → canon
```

### stub

A gloss reservation. `lemma_1` is blank — no Ghandwa surface form has been proposed. May have: a PIE root (`lemma_1_pre_root`), a Swadesh/literary-text tag, a `note` sketching candidates. Purpose: track that the concept is needed and prevent duplicate work.

### draft

Has a Ghandwa surface form (`lemma_1` + `lemma_1_ipa`). The form is plausible but has not been fully vetted. No known open problems with the form itself. Typical profile: recently added, may be missing etymology backfill (`pre_root`, `pre_ety`), cognates, or full semantic classification. Most new entries enter at this tier.

Minimum fields: `lemma_1`, `lemma_1_ipa`, `pos`, `gloss`, `entry_status`.

### hold

Has a Ghandwa surface form — often more complete than a draft entry — but an **identified open question** blocks promotion to canon. Reasons include: competing stems, paradigm uncertainty, phonological ambiguity, semantic distribution conflict, or a known naming collision.

The `note` field should state what is unresolved. Exiting hold: resolve the question, then promote to canon (or demote back to draft if the form changes).

Minimum fields: same as draft, plus `note` explaining the hold reason.

### canon

The form is settled and usable in text. All core metadata is populated. An entry at this tier can appear in inscriptions, paradigm tables, and cross-references without caveat.

Minimum fields for all entries: `lemma_1`, `lemma_1_ipa`, `lemma_1_ipa_status`, `pos`, `gloss`, `semantic_field`, `semantic_subfield`, `entry_status`. Additional minimums by POS: nouns require `nom_stem_class` + `noun_gender`; verbs require `verb_thematicity` + `verb_stem_type`.

### Label history

Prior to 2026-03-22, the labels were: `stub`, `candidate` (now draft), `unresolved` (now hold), `canonical` (now canon).

---

## 10. Lexicon Field Conventions

Conventions for values in `lexicon.tsv` columns. Column schema itself is authoritative in the TSV header row.

**Verb citation form.** Verbs are cited in the 3sg present active indicative (e.g., *tékseti*, *ɣénti*). Not the bare root, not the infinitive, not the full paradigm.

**Provenance.** Two values:

- `PIE` — inherited from Proto-Indo-European.
- `PGh` — Proto-Ghandwa innovation; a form or formation that arose within the Ghandwa branch after divergence from PIE.

**`pre_root` asterisk convention.** The `lemma_1_pre_root` field stores the PIE root *without* the leading `*`. Rendering conventions (in markdown tables, prose, etc.) add the `*` back. Example: the field stores `tek-`; output renders `*tek-`.

---

## 11. Markdown and Document Conventions

**Italicization.** All Ghandwa forms (script renderings and transliterations) are italicized in running prose: *ékvos*, *ɣvḗr*. IPA, glosses, and PIE reconstructions are **not** italicized. Example:

> The word *ékvos* /ˈe.kʷos/ 'horse' derives from PIE \*h₁éḱwos.

**Cognate column formatting.** In markdown tables listing cognates, the asterisk distinguishes reconstructed from attested forms:

- Reconstructed proto-forms: escaped asterisk, no italics. `\*kurną` renders as `*kurną`.
- Attested forms: italics via surrounding asterisks. `*equus*` renders as *equus*.

**PIE reconstructions in prose.** Use escaped asterisk: `\*h₁éḱwos` → `*h₁éḱwos`. Not italicized.

---

## 12. Doublets and Dialectal Variants

<!-- TODO: Write this section. -->

**Status:** Stub. Content to be drafted.

**Scope:** Conventions for when two reflexes of the same PIE root may coexist as separate canon entries in the lexicon, versus when one is a variant to be documented inline.

**Criteria to formalize:**
- Different stress environment at the syllabic resonant vocalization stage, producing distinct surface forms (e.g. *udṓr* vs. *vódar*)
- Different dialect stratum within the pre-Ghandwa continuum (geographic split)
- Different register (archaic/learned vs. vernacular)
- Contact borrowing from Crotonian or another branch

**Worked example to develop:** *udṓr* / *vódar* — two water words currently on hold.

**See also:** `docs/alt-phonologies.md` §6 (Crotonian) for the borrowing scenario that generates contact doublets.

---

## 13. Sophomore List Gap Analysis

<!-- TODO: Execute this analysis when verb system is settled. -->

**Status:** Stub. Task to be executed, not a convention to document.

**What it is:** Rosenfelder's *Language Construction Kit* (2011) ~350-word "Sophomore list" — semantic extension of Swadesh 207. Task: run against current lexicon; output gap report in `docs/lexicon-gaps.md`.

**When to do it:** After the verb system is settled.

**Delegation:** Suitable for ChatGPT batch pass once the lexicon TSV is stable.

---

## 14. Transformer Input Normalization: Palatals vs. Accent

The `normalize.py` module in `pie_transformer/` distinguishes two uses of U+0301 (combining acute accent) in PIE input strings:

**Lexical pitch accent** — combining acute on a **vowel** or **syllabic resonant** (identified by U+0325 ring-below in the cluster). The accent is stripped from the input and recorded as `accent_char_pos` for downstream use by accent-sensitive rules.

**Palatalization diacritic** — combining acute on a **consonant** (e.g. `ǵ` = g+U+0301, `ḱ` = k+U+0301). This is a PIE notation convention for palatal stops, not a prosodic mark. The diacritic is kept in the normalized string and passed to the centumization rule (`ǵ→g`, `ḱ→k`, `ǵʰ→gʰ`).

**Input convention for PIE preforms in the lexicon:** Palatal stops should always be written with the precomposed forms (`ǵ`, `ḱ`, `ǵʰ`) or their NFC-normalized equivalents, not as plain `g` or `k`.

---

## 15. Ghandwa Orthographic Conventions in Transformer Output

The `render.py` module in `pie_transformer/` applies the following token-level substitutions when producing orthographic (surface) output. IPA output uses tokens directly without substitution.

| Token (IPA) | Orthography | Notes |
|---|---|---|
| `kʷ` | `kv` | Labiovelar stop |
| `gʷ` | `gv` | Labiovelar stop |
| `ɣʷ` | `ɣv` | Labiovelar fricative (from \*gʷʰ) |
| `j` | `i` | Palatal glide (see §8 in grammar notation) |
| `w` | `v` | Labial glide (onset position; see §8 in grammar notation) |
| all others | unchanged | — |

`ˀ` (surviving laryngeal / glottal stop) passes through unchanged in both output modes. It is a **diagnostic tracer** — its presence signals a laryngeal not consumed by any rule, flagging a gap in the rule inventory. It should never appear in a canon entry's `lemma_1_ipa` or `gh_lemma_1_orth` fields.
