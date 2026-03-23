# Ghandwa Alphabet — Naming System Notes

---
last_updated: 2026-03-20T03:00:00Z
session: "Resolved rektús/leiðra open question"
changelog:
  - 2026-03-20T03:00:00Z | 95 lines (MD) | Removed rektús/leiðra open question (both added to lexicon offline).
  - 2026-03-20T02:00:00Z | 21 lines (TSV), 96 lines (MD) | Filled 33 new register slots from lexicon. New Sacred: ðubnióm, éngman, ɣostís, némos, óngvōl, sakrós, térman, vektís, βātus. New Martial: akús, ðarzús, glúptrom, iugóm, kórios, méltrom, nḗr, óitos, panktís, rektós, santóm, táuros, virós, βā́gos. New Nature: anβrís, ðeɣvís, gelús, ɣidós, miɣlā, néβos, ógnos, régvos, βlṓtus. New Life: báktrom, dónts, élkos, gentís, iuvantā́, klutom, nóman, ovióm, patḗr. Remaining gaps: /b/ (3 empty), /z/ (4 empty), /i/ and /l/ (2 empty each), scattered singles. No Alt columns touched. Updated open questions.
  - 2026-03-20T01:00:00Z | 91 lines | Added Orthographic Conventions section documenting labiovelar digraphs (⟨kv⟩, ⟨gv⟩, ⟨ɣv⟩) and long vowel marking (doubled characters in Sharpscript → diacritical descendants). Removed incorrect /z/ open question (𐌆 is confirmed as its own letter). Added /b/ to unnamed-letter list with note on PIE *b-gap. Added ampsinþa ⟨þ⟩ problem to open questions.
  - 2026-03-20T00:00:00Z | 76 lines | Normalized all letter-name forms to match lexicon lemma_1 with accent marks. Fixed: agnís, deivós, ékvos, ɣoizós, pérkus, teutā́, mā́tēr, ðúktēr, dervís, agnós, sunús. Corrected fratēr → βrā́tēr, vēks → véiks (form and gloss). Fixed ɣoios → ɣoizós and sān → sā́val in register examples. Removed sullā (no lexicon entry). rektús, leiðra, ampsinþa flagged for later resolution.
  - 2026-03-14 | 76 lines | Added metadata header. No content changes.
---

## Script Names

### Sharpscript
The older, monumental writing tradition. Recognized in post-Ghandwa daughter cultures as the "sharp script" based on the physical reality of how most surviving inscriptions were made — incised with a sharp instrument (knife, axe, chisel) into hard materials: wood, stone, clay. This produces naturally angular letterforms with few curves. The Old Italic Unicode block is used as the closest available visual approximation in modern rendering.

### Softscript
A later development, presumably pen-and-ink or brush-based, producing more cursive or rounded forms. Details TBD.

**Note:** Both script traditions will eventually have names in the daughter languages. TBD.

---

## The Naming Register System

Each letter of the Ghandwa alphabet carries multiple names drawn from different registers of cultural life. This functions similarly to the runic tradition (where each rune has a name that is also a word), but is more elaborate: rather than a single name per letter, Ghandwa has a **set of names**, one per register, allowing the alphabet to serve as a structured teaching tool for children.

Children learning to read are simultaneously learning a taxonomy of the world — each letter is an entry point into a different domain of knowledge and value. Each register also carries **alternate names** to include and honor gendered terms, ensuring no letter's cultural domain is represented by only one gender's experience.

---

## Registers

The register system is built on **Dumézil's trifunctional hypothesis** — the three social functions reconstructed for Proto-Indo-European society — plus a fourth register for the natural world.

### 1. Sacred
Corresponds to Dumézil's **first function**: sovereignty, the sacred, divine law, priesthood. Dumézil's first function has two aspects — the magical/charismatic (Odin, Varuna) and the juridical/rational (Tyr, Mitra) — making it naturally receptive to gendered alternates. Names drawn from theology, cosmology, and divine order. Examples: *agnís* 'god', *deivós* 'deity'.

### 2. Martial
Corresponds to Dumézil's **second function**: martial virtue, the warrior class, conflict, heroism, protection of the community. Figures like Thor and Indra. Names drawn from weapons, battle, and warrior culture. Example: *ɣoizós* 'spear'.

### 3. Nature
Sits outside the trifunctional scheme proper — the raw world within which all three functions operate. Names drawn from plants, animals, celestial bodies, landscape. Examples: *pérkus* 'oak', *sā́val* 'sun', *ampsinþa* 'catnip', *ékvos* 'horse'.

### 4. Life
Corresponds to Dumézil's **third function**: fertility, agriculture, domestic life, the household, kinship, craft, abundance. The most explicitly gendered of the three functions in IE cultures — family pairs (mother/father, son/daughter) live most naturally here. Names drawn from family, home, community, and the rhythms of ordinary life. Examples: *mā́tēr* 'mother', *teutā́* 'people', *véiks* 'village, household', *sunús* 'son'.

---

## TSV Structure

The companion TSV (ghandwa_alphabet.tsv) has the following columns:

| Column | Notes |
|---|---|
| Phoneme | IPA phoneme value(s) |
| Sharpscript | Old Italic Unicode character |
| Transliteration | Latin letter rendering |
| Sacred | Primary name, Sacred register |
| Sacred Alt | Alternate/gendered name, Sacred register |
| Martial | Primary name, Martial register |
| Martial Alt | Alternate/gendered name, Martial register |
| Nature | Primary name, Nature register |
| Nature Alt | Alternate/gendered name, Nature register |
| Life | Primary name, Life register |
| Life Alt | Alternate/gendered name, Life register |

Softscript is not currently a separate column — it does not yet diverge from the Transliteration column. A Softscript column will be added when the cursive tradition is developed.

---

## Orthographic Conventions

### Labiovelars

The labiovelar phonemes /kʷ/, /gʷ/, /ɣʷ/ are written as digraphs in both Sharpscript and transliteration: ⟨kv⟩, ⟨gv⟩, ⟨ɣv⟩. They do not have dedicated alphabet characters. In Sharpscript, the velar letter is followed by 𐌖 (the /u/~/w/ letter).

### Long Vowels

Vowel length is phonemically distinctive in Ghandwa. In Sharpscript, long vowels are written by doubling the vowel character (e.g. 𐌀𐌀 for /ā/). Over time, the doubled characters were written one on top of the other for economy, which then resolved variously by tradition and geography into diacritical marks: a dot above or below the letter, or a horizontal line (macron) above or below. All of these notational descendants represent the same underlying convention of marking length.

In transliteration, long vowels are written with a macron: ā, ē, ī, ō, ū.

---

## Open Questions

- How many registers will there be in total? The current four (Sacred, Martial, Nature, Life) map cleanly to Dumézil plus the natural world. A fifth register has not been ruled out.
- /b/ has only one name (Life: *báktrom* 'staff') due to the PIE *b-gap — genuine *b-initial words in any western IE language are extremely rare. Three register slots remain empty.
- /z/ has no names in any register. No z-initial words exist in the lexicon, since /z/ arises only from intervocalic s-voicing. A non-initial example or a special solution is needed.
- Scattered single-register gaps remain across /d/ Martial, /e/ Martial, /g/ Sacred, /i/ Sacred and Nature, /k/ Sacred, /l/ Sacred/Martial/Nature, /m/ Sacred, /p/ Sacred, /r/ Sacred, /t/ Nature, /u/ Nature.
- No Alt (gendered alternate) names have been populated yet in any register.
- *ampsinþa* 'catnip' uses ⟨þ⟩, which is not in the Ghandwa phonological inventory. Form needs revision.
