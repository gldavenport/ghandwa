---
title: Vertenda — Index
description: Index of translation benchmarks for Ghandwa, with status tracking and aggregate lexical gap table
last_updated: 2026-05-23
---

# Vertenda

Translation benchmarks for Ghandwa. Each text is held in its own file. Translations test lexical coverage, grammatical completeness, and register range across the trifunctional system (Sacred, Martial, Nature, Life).

---

## Index

| File | Text | Register | Translation status |
|---|---|---|---|
| `one-ring-verse.md` | The One Ring Verse (Tolkien, 1954) | Sacred / Martial | pending |
| `schleicher-fable.md` | Schleicher's Fable (*h₂óuis h₁eḱuōs-kʷe*, 1868) | Nature / Life | pending |
| `king-and-god.md` | The King and the God (Sen 1994) | Sacred | pending |
| `strasbourg-oaths.md` | The Strasbourg Oaths (842 AD) | Sacred / Legal | pending |
| `agni-hymn-rv1-1.md` | RV 1.1 — First Agni Hymn | Sacred | pending |
| `merseburg-charm.md` | Second Merseburg Charm (OHG, ~842) | Sacred / Nature | pending |
| `catullus-5.md` | Catullus 5 (*Vivamus mea Lesbia*) | Life | pending |
| `beowulf-opening.md` | Beowulf, ll. 1–11 | Martial | pending |
| `nasadiya-rv10-129.md` | Nāsadīya (*RV* 10.129) | Sacred / Cosmological | pending |
| `fables-narrative.md` | Fables / narrative prose (TBD) | Nature / Life | unspecified |

**Translation status values:** pending · in progress · draft · complete

---

## Lexicon Audit

*Last audited: 2026-05-23 against `ghandwa_-_lexicon__LexiconMergedCsv__2026-05-23_10-22.csv` (615 entries with lemma filled).*

### Housekeeping flags (NocoDB)

Two entries have blank `entry_status` — assign before next audit:

| Lemma | Gloss |
|---|---|
| *ɣeslám* | thousand |
| *ɣvénti* | to be striking, beating, killing |

### Readiness notes by text

- **King and the God** — one lexical gap: "best/finest" (no superlative attested). Syntax is the remaining challenge: question formation and future/prospective verb form for *dídōti*.
- **Schleicher's Fable** — 17/30 concepts covered. Missing basic verbs: flee, pull, drive, grieve.
- **Merseburg Charm** — blocked by three `hold`-status entries: *svézōr* (sister), *pṓts* (foot), *iunékti* (join/yoke). Resolving those unblocks the charm. Also needs physiological "blood" — *kvoinā́* is "blood-money" only.
- **Catullus 5** — *svépeti* (sleep) is `hold`; blocks the central *nox perpetua* construction. *ɣeslám* (thousand) has blank status.
- **Nāsadīya** — lowest priority; copula (exist/be) is a deep structural gap the hymn pivots on.

### Cross-text notes

- **Two stone words**: *targóm* [draft] and *ákmō* [draft] — distribution unresolved.
- **Two water words**: *udṓr* [draft] and *vódar* [draft] — distribution unresolved.
- **Two shadow words**: *skátus* [hold] and *skṓī* [canon] — *skṓī* preferred for Ring Verse context.
- **Generic king**: *rḗks* [canon] confirmed. *ekvorḗks* and other *-rḗks* compounds are epithets built on it.
- **God**: *deivós* [canon] is the generic term; *agnís* [canon] is fire-god specifically.
- **Copula**: no plain exist/be verb attested — deepest structural gap across the corpus.
- **Light (illumination)**: *lanɣús* [canon] is "light of weight" — gap for luminous sense.
- **Heat/warmth**: *ɣvérō* [draft] is an Agnis epithet — gap for common noun.
- **Blood (physiological)**: *kvoinā́* [canon] is "blood-money" — gap for physiological sense.

---

## Aggregate Lexical Gaps

Confirmed gaps across one or more texts as of 2026-05-23 audit. Merge into `lexicon-gaps.md` when stub work begins. Sorted by number of texts requiring the concept.

| Concept | PoS | Texts |
|---|---|---|
| sky / heaven | n | Ring Verse, Beowulf, Nāsadīya |
| day | n | Agni, Beowulf, Nāsadīya |
| hall | n | Ring Verse, Beowulf |
| love (noun) | n | Strasbourg, Catullus |
| love (verb) | v | Catullus |
| heat / warmth (n) | n | Agni, Nāsadīya |
| light (illumination) | n | Agni, Catullus |
| grow / increase | v | Agni, Beowulf |
| limb / joint | n | Merseburg, Nāsadīya |
| land / territory | n | Ring Verse |
| throne | n | Ring Verse |
| mortal | adj | Ring Verse |
| find | v | Ring Verse |
| bring | v | Ring Verse |
| bind (verb) | v | Ring Verse |
| doomed / fated | adj | Ring Verse |
| sheep | n | Schleicher |
| flee (verb) | v | Schleicher |
| pull / drag | v | Schleicher |
| pain / grieve | v | Schleicher |
| wagon | n | Schleicher |
| plain | n | Schleicher |
| warm (general adj) | adj | Schleicher |
| salvation / safety | n | Strasbourg |
| save / help | v | Strasbourg |
| knowledge | n | Strasbourg |
| ability / power | n | Strasbourg |
| aid (v/n) | v/n | Strasbourg |
| never | adv | Strasbourg |
| our | pro | Strasbourg |
| forest / wood (place) | n | Merseburg |
| ride (verb) | v | Merseburg |
| foal | n | Merseburg |
| sprain | v | Merseburg |
| charm (verb) | v | Merseburg |
| blood (physiological) | n | Merseburg |
| kiss | n/v | Catullus |
| envy | v | Catullus |
| eternal / perpetual | adj | Catullus |
| noble / prince | n | Beowulf |
| enemy / foe | n | Beowulf |
| fear / terror | n | Beowulf |
| sea (open water) | n | Beowulf |
| yield / submit | v | Beowulf |
| tribute | n | Beowulf |
| exist / be (copula) | v | Nāsadīya |
| breathe | v | Nāsadīya |
| create | v | Nāsadīya |
| immortality | n | Nāsadīya |
| praise (verb) | v | Agni |
| invoke | v | Agni |
| shine / be bright | v | Agni |
| homage / reverence | n | Agni |
