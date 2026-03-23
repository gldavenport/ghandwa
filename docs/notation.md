# Ghandwa: Notation System

---
last_updated: 2026-03-22T18:00-04:00
session: "Added §7 Lexicon Entry Status Pipeline — formal definitions for entry_status values (stub, draft, hold, canon)"
changelog:
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
