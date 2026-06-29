# §1 Introduction — Notation Conventions

---
last_updated: 2026-06-18T00:00-04:00
changelog:
  - 2026-05-22T00:00-04:00 | — | Split from `docs/notation.md`. Grammar-relevant content (script, transliteration, IPA, letter inventory, labiovelar notation, glide/semivowel conventions, Sharpscript long vowels) moved here as §1 of the grammar volume. Workflow content (entry status pipeline, lexicon field conventions, document conventions, transformer I/O conventions) remains in `docs/notation.md`.
---

This chapter documents the three-layer representation system used throughout the grammar, the letter inventory, and the orthographic and IPA conventions referenced in all subsequent chapters.

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

There is no letter for [z]. [z] is a fully predictable, non-phonemic realization of /s/ (see Grammar §4.2.2.3); orthographic ⟨s⟩ covers both values, and the distinction is resolved only in IPA transcription.

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

*Note: §7 is the Lexicon Entry Status Pipeline. It lives in `docs/notation.md` (workflow conventions) rather than here.*
