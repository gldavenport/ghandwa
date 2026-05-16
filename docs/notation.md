# Ghandwa: Notation System

---
last_updated: 2026-05-15T00:00-04:00
session: "Added §§8–11: glide/semivowel conventions, Sharpscript long vowels, lexicon field conventions (verb citation, provenance, pre_root), and markdown document conventions (italicization, cognate column formatting). Absorbed content previously living only in project instructions."
changelog:
  - 2026-05-15T00:00-04:00 | — | Added §14 (Transformer Input Normalization: Palatals vs. Accent — U+0301 on consonants kept as palatalization diacritic; U+0301 on vowels/syllabic resonants extracted as accent_char_pos). Added §15 (Ghandwa Orthographic Conventions in Transformer Output — token substitution table: kʷ→kv, gʷ→gv, ɣʷ→ɣv, j→i, w→v; ˀ diagnostic tracer note).
  - 2026-05-05T00:00-04:00 | stub sections added | Added §12 TODO stub (doublets/dialectal variants framework) and §13 TODO stub (Sophomore list gap analysis). Changelog and last_updated updated.
  - 2026-04-13T00:00-04:00 | 204 lines | Added §8 Glide and Semivowel Conventions (/j/ → ⟨i⟩; /w/ onset ⟨v⟩ vs coda ⟨u⟩). Added §9 Sharpscript Long Vowels (vowel doubling in script). Added §10 Lexicon Field Conventions (verb citation form = 3sg pres act ind; provenance PIE/PGh; pre_root asterisk convention). Added §11 Markdown and Document Conventions (italicization rule; cognate column `\*form-` vs `*form*`). Added normalization rule to §3 (ğ → ɣ in output).
  - 2026-03-22T18:00-04:00 | 139 lines | Added §7 Lexicon Entry Status Pipeline. Four tiers: stub (gloss reservation, no form), draft (has form, awaiting vetting), hold (has form, blocked on open question), canon (settled, usable in text). Minimum field requirements defined for each tier. Replaces prior ad-hoc labels (candidate→draft, unresolved→hold, canonical→canon).
  - 2026-03-14 | 129 lines | Converted from `ghandwa_notation.docx` to proper markdown. Reformatted all tables from whitespace-aligned to pipe-delimited markdown. Added metadata header. Content unchanged.
---

Working reference document — notation conventions for Ghandwa script, transliteration, and IPA transcription.

---

## 1. The Three-Layer System

Ghandwa linguistic data is represented in three layers:

**1. Native script.** Rendered in Old Italic Unicode as a 1:1 stand-in. The actual Ghandwa script was visually similar but not identical to Old Italic; the Unicode block is used as the closest available approximation.

**2. Transliteration.** Latin alphabet rendering. This is a script-to-script conversion (not phonetic). It adds information not present in the original inscription, including vowel length (macron), pitch accent (acute), and editorial notation. The convention is based on the high-register scholarly tradition of a daughter culture that preserved and formalized the notation.

**3. IPA transcription.** Phonetic transcription in the International Phonetic Alphabet. This is where phonemic ambiguities present in the script and transliteration are resolved.

---

## 2. Diacritic Conventions (Transliteration)

| Diacritic | Example | Meaning |
|---|---|---|
| Macron | ē | Vowel length (long vowel) |
| Acute | é | Pitch accent (reconstructed; not marked in original script) |
| Macron + acute | ḗ | Long vowel with pitch accent |

---

## 3. Author Shorthand vs. Formal Transliteration

A distinction exists between the formal Ghandwa transliteration and the author's practical typing shorthand:

| Old Italic | Formal Transliteration | Author Shorthand (typed) | IPA |
|---|---|---|---|
| 𐌘 | β | β | β |
| 𐌈 | ð | ð | ð |
| 𐌙 | ɣ | ğ (typed via press-and-hold) | ɣ |

ğ is the author's input convenience for ɣ, accessible via macOS press-and-hold on 'g'. It does not appear in formal notation. The fricative series (β, ð, ɣ) borrows IPA symbols directly into transliteration, as no clean press-and-hold Latin alternatives exist for these sounds on macOS.

ð is accessible via press-and-hold on 'd' on macOS.

**Normalize ğ → ɣ in all generated output.** ğ is an input-time convenience only; any file, table, or quoted form produced by tools or assistants should use ɣ.

---

## 4. Letter Inventory

Letters marked 'extrapolated' are predicted from the phonological system but not yet attested in worked examples.

| Old Italic | Transliteration | IPA | Notes |
|---|---|---|---|
| 𐌀 | a | a | |
| 𐌁 | b | b | *extrapolated* |
| 𐌂 | g | g | |
| 𐌃 | d | d | *extrapolated* |
| 𐌄 | e | e | |
| 𐌉 | i | i | *extrapolated* |
| 𐌊 | k | k | |
| 𐌋 | l | l | |
| 𐌌 | m | m | |
| 𐌍 | n | n | |
| 𐌏 | o | o | |
| 𐌐 | p | p | *extrapolated* |
| 𐌓 | r | r | |
| 𐌔 | s | s | |
| 𐌕 | t | t | *extrapolated* |
| 𐌖 | v | ʷ / w | labiovelarization modifier; ambiguous between labiovelarization and /w/ |
| 𐌘 | β | β | voiced bilabial fricative; see author shorthand note |
| 𐌈 | ð | ð | voiced dental fricative |
| 𐌙 | ɣ | ɣ | voiced velar fricative; see author shorthand note |

---

## 5. Worked Examples

| Old Italic | Transliteration | IPA | Meaning | Etymology |
|---|---|---|---|---|
| 𐌙𐌖𐌄𐌄𐌓 | *ɣvḗr* | ˈɣʷeːr | wild animal, beast | PIE \*ǵʰwḗr; cf. Gk. θήρ, Lat. fera |
| 𐌂𐌀𐌓𐌍𐌏𐌌 | *garnom* | ˈgar.nom | grain | PIE \*ǵr̥h₂nóm > \*gr̥nóm > \*garnóm; cf. PGmc \*kurną, Lat. grānum |
| 𐌂𐌖𐌀𐌋𐌏𐌌 | *gválom* | ˈgʷa.lom | coal | cf. OE col, PGmc \*kulą; \*l̥ > al |
| 𐌄𐌊𐌖𐌏𐌔 | *ékvos* | ˈe.kʷos | horse | PIE \*h₁éḱwos; cf. Lat. equus, Gk. ἵππος |

---

## 6. Labiovelar Notation

The letter 𐌖 (transliterated v) functions as a labiovelarization modifier when following a consonant. Like Latin v, the script does not distinguish between labiovelarization (/ʷ/) and the consonant /w/. This ambiguity is preserved in transliteration and only resolved in IPA transcription.

| Cluster (script) | Transliteration | IPA | Description |
|---|---|---|---|
| 𐌙𐌖 | ɣv | ɣʷ | voiced labiovelar fricative |
| 𐌂𐌖 | gv | gʷ | voiced labiovelar stop |
| 𐌊𐌖 | kv | kʷ | voiceless labiovelar stop |

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

Has a Ghandwa surface form — often more complete than a draft entry — but an **identified open question** blocks promotion to canon. Reasons include: competing stems (e.g. *smérus* direct vs. oblique-derived), paradigm uncertainty (e.g. *βúeti*), phonological ambiguity (e.g. *snéikos*/*snóiɣvos*), semantic distribution conflict (e.g. *udṓr*/*vódar*), or a known naming collision.

The `note` field should state what is unresolved. Exiting hold: resolve the question, then promote to canon (or demote back to draft if the form changes).

Minimum fields: same as draft, plus `note` explaining the hold reason.

### canon

The form is settled and usable in text. All core metadata is populated. An entry at this tier can appear in inscriptions, paradigm tables, and cross-references without caveat.

Minimum fields for all entries: `lemma_1`, `lemma_1_ipa`, `lemma_1_ipa_status`, `pos`, `gloss`, `semantic_field`, `semantic_subfield`, `entry_status`. Additional minimums by POS: nouns require `nom_stem_class` + `noun_gender`; verbs require `verb_thematicity` + `verb_stem_type`.

### Label history

Prior to 2026-03-22, the labels were: `stub`, `candidate` (now draft), `unresolved` (now hold), `canonical` (now canon). Old labels may appear in changelog entries predating the rename; these are historical record.

---

## 8. Glide and Semivowel Conventions

**/j/ (palatal glide).** Appears only in IPA transcription. In transliteration it is written ⟨i⟩. There is no ⟨j⟩ in Ghandwa transliteration.

**/w/ (labial glide).** Two transliteration values depending on syllable position:

| Position | Transliteration | Example |
|---|---|---|
| Onset (syllable-initial) | v | *vódar* /ˈwo.dar/ |
| Coda (syllable-final) | u | *néu* /new/ |

This parallels the convention of Latin orthography and is distinct from the ⟨v⟩ that serves as a labiovelarization modifier after a consonant (see §6).

---

## 9. Sharpscript Long Vowels

In the native writing system (Sharpscript, rendered here in Old Italic Unicode), long vowels are written by doubling the vowel character. The macron is a transliteration-layer diacritic only.

| Script | Transliteration | IPA |
|---|---|---|
| 𐌄𐌄 | ē | eː |
| 𐌏𐌏 | ō | oː |
| 𐌀𐌀 | ā | aː |
| 𐌉𐌉 | ī | iː |

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

Conventions for prose documents, tables, and generated output across the project.

**Italicization.** All Ghandwa forms (script renderings and transliterations) are italicized in running prose: *ékvos*, *ɣvḗr*. IPA, glosses, and PIE reconstructions are **not** italicized. Example:

> The word *ékvos* /ˈe.kʷos/ 'horse' derives from PIE \*h₁éḱwos.

**Cognate column formatting.** In markdown tables listing cognates, the asterisk distinguishes reconstructed from attested forms:

- Reconstructed proto-forms: escaped asterisk, no italics. `\*kurną` renders as `*kurną`.
- Attested forms: italics via surrounding asterisks. `*equus*` renders as *equus*.

This applies to `cog_Celtic`, `cog_Germanic`, `cog_Italic`, and the other `cog_*` columns when their contents are rendered into documentation.

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
- Contact borrowing from Crotonian or another branch producing a form that diverges systematically from the inherited Ghandwa reflex (see `provenance` = `Crotonian` in lexicon schema)

**Worked example to develop:** *udṓr* / *vódar* — two water words currently on hold; their relationship and distribution are unresolved. This pair should be the primary example once the criteria above are settled.

**See also:** `docs/alt-phonologies.md` §6 (Crotonian) for the borrowing scenario that generates contact doublets.

---

## 13. Sophomore List Gap Analysis

<!-- TODO: Execute this analysis when verb system is settled. -->

**Status:** Stub. Task to be executed, not a convention to document.

**What it is:** Rosenfelder's *Language Construction Kit* (2011) includes a ~350-word "Sophomore list" — a semantic extension of Swadesh 207 organized by domain (emotions, social/political structure, religion, material culture, cognitive verbs, speech act verbs, modals, seasons, time divisions). Swadesh 207 is the floor; the Sophomore list maps the next layer of coverage.

**Task:** Run the Sophomore list against the current lexicon. For each item: (a) covered by a canon or draft entry, (b) covered by a stub, (c) not present. Output as a gap report in `docs/lexicon-gaps.md`.

**When to do it:** After the verb system is settled, so that verbal entries (cognitive verbs, speech act verbs, modals) can be generated alongside nominals in the same pass.

**Delegation:** Suitable for ChatGPT batch pass once the lexicon TSV is stable.

---

## 14. Transformer Input Normalization: Palatals vs. Accent

The `normalize.py` module in `pie_transformer/` distinguishes two uses of U+0301 (combining acute accent) in PIE input strings:

**Lexical pitch accent** — combining acute on a **vowel** or **syllabic resonant** (identified by U+0325 ring-below in the cluster, e.g. *ĺ̥*, *ŕ̥*). The accent is stripped from the input and recorded as `accent_char_pos` for downstream use by accent-sensitive rules (pretonic shortening, etc.).

**Palatalization diacritic** — combining acute on a **consonant** (e.g. `ǵ` = g+U+0301, `ḱ` = k+U+0301). This is a PIE notation convention for palatal stops, not a prosodic mark. The diacritic is kept in the normalized string and passed to the centumization rule (`ǵ→g`, `ḱ→k`, `ǵʰ→gʰ`).

The practical consequence: input strings like `*ǵʰn̥dwéh₂s` are normalized correctly — the acute on `ǵʰ` survives, while the acute on `é` is extracted as the accent position. The centumization rule then applies to the surviving `ǵʰ` token in the pipeline.

**Input convention for PIE preforms in the lexicon:** Palatal stops should always be written with the precomposed forms (`ǵ`, `ḱ`, `ǵʰ`) or their NFC-normalized equivalents, not as plain `g` or `k`. The transformer relies on these diacritics to identify palatals for centumization.

---

## 15. Ghandwa Orthographic Conventions in Transformer Output

The `render.py` module in `pie_transformer/` applies the following token-level substitutions when producing orthographic (surface) output. IPA output uses tokens directly without substitution.

| Token (IPA) | Orthography | Notes |
|---|---|---|
| `kʷ` | `kv` | Labiovelar stop |
| `gʷ` | `gv` | Labiovelar stop |
| `ɣʷ` | `ɣv` | Labiovelar fricative (from \*gʷʰ) |
| `j` | `i` | Palatal glide (see §8) |
| `w` | `v` | Labial glide (onset position; see §8) |
| all others | unchanged | — |

These substitutions are applied after accent marking. Accent marks (acute) appear in orthographic output on the accented segment.

`ˀ` (surviving laryngeal / glottal stop) passes through unchanged in both output modes. It is a **diagnostic tracer**, not a real surface segment — its presence indicates a laryngeal that was not consumed by any rule, signalling a gap in the rule inventory. It should never appear in a canon entry's `lemma_1_ipa` or `gh_lemma_1_orth` fields.
