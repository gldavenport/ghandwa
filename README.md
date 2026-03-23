# Ghandwa

---
last_updated: 2026-03-19T18:20-04:00
session: "GitHub prep — rewritten from notes/prompt.md as repo-level README"
changelog:
  - 2026-03-19T18:20-04:00 | 129 lines | Rewritten from prompt.md (319 lines). Restructured as repo orientation: project overview, linguistic positioning, repo map with file descriptions, key references. Transformer pipeline details, code architecture, and tested examples are covered by phonological-history.md and comparanda.md. Original prompt.md deleted (all content covered by living docs).
  - 2026-03-14 | 319 lines | (as prompt.md) Added metadata header; updated scope statement to acknowledge verbal morphology in progress.
---

## What is Ghandwa?

Ghandwa is a constructed Proto-Indo-European (PIE) daughter language — a conlang built with historical-linguistic methodology. It occupies the position of a conservative western centum branch of the IE family, designed to sit alongside Proto-Germanic, Proto-Italic, and Proto-Celtic as a plausible sister language.

The project includes a growing lexicon (~520 entries), a phonological transformer that derives Ghandwa surface forms from PIE inputs, grammatical paradigms, a worldbuilding/lore layer, and a developing daughter-language framework.

Primary reference: **Ringe 2017** — *From Proto-Indo-European to Proto-Germanic*, 2nd ed.

---

## Ghandwa's position in the IE family

- **Centum** language — no satemization
- **Voiced fricatives from aspirates**: PIE \*bʰ dʰ gʰ gʷʰ → Ghandwa β ð ɣ ɣʷ
- **a-vocalism for syllabic resonants**: PIE \*r̥ l̥ m̥ n̥ → ar al am an (Celtic-like vowel quality, Germanic metathesis order)
- **Preserves labiovelars**: no \*gʷ → b (Celtic, Greek) or \*k ʷ →p (Gaulish, Sabellic, Greek) mergers
- **Preserves o/a distinction**: no Germanic-style merger
- **Preserves word-final -m**

### Comparanda hierarchy

1. **Proto-Germanic (PGmc)** — computational backbone; Ringe's PIE→PGmc derivation is the scaffolding
2. **Proto-Italic (PIt) and Proto-Celtic (PC)** — close comparanda, consulted on equal footing
3. **Proto-Balto-Slavic (PBS)** — consulted but held at arm's length due to satemization and nominal paradigm divergences

When all three western branches (PGmc + PIt + PC, the "WIE") share an inherited form, that is the Ghandwa form. When they diverge through independent innovation, Ghandwa picks one, makes one up, or preserves the PIE-inherited state.

---

## Phonological inventory

**Stops**: p b t d k g kʷ gʷ
**Fricatives**: s z β ð ɣ ɣʷ
**Nasals**: m n
**Liquids**: l r
**Glides**: w y
**Vowels (short)**: a e i o u
**Vowels (long)**: ā ē ī ō ū

Stress is free/lexical. Orthographic conventions: /β/ /ð/ /ɣ/ written ⟨β⟩ ⟨ð⟩ ⟨ɣ⟩; /j/ in IPA only, ⟨i⟩ in transliteration; /w/ written ⟨v⟩ in orthography. The Ghandwa script is modeled on Old Italic (Unicode Old Italic block).

---

## Grammatical scope

- **3 genders**: masculine, feminine, neuter
- **8 cases**: nominative, accusative, genitive, dative, ablative, instrumental, locative, vocative
- **Nominal morphology**: largely complete — see `grammar/paradigms-nominal.md`
- **Verbal morphology**: in progress — 4 present stem classes established; see `grammar/verbs.md`
- **Verb citation form**: 3sg present active indicative (e.g. *tékseti*, not bare root)

---

## Design philosophy

A central principle is that **not every phonological instability is resolved at the parent-language stage**. Clusters, sequences, and allomorphies are left as deliberate unresolved tensions for daughter languages to resolve differently. Current tensions include: kt clusters, labiovelar stem allomorphy, voiced fricatives, labiovelars before vowels, nasal clusters (no assimilation), and VV hiatus from laryngeal loss.

---

## Repo structure

```
ghandwa/
├── README.md                          ← this file
├── docs/
│   ├── comparanda.md                  Comparative evidence across branches
│   ├── daughters.md                   Daughter-language framework (A/B/C stages)
│   ├── inscriptions.md                Inscription formulae and working sentences
│   ├── lore.md                        Worldbuilding, theology, naming, culture
│   ├── phonological-history.md        Ordered PIE→Ghandwa sound change inventory
│   └── science.md                     Science/nature vocabulary domain
├── grammar/
│   ├── notation.md                    Notation and formatting conventions
│   ├── paradigms-nominal.md           Nominal declension paradigm tables
│   ├── verb-eval-template.md          Verb adoption evaluation methodology
│   ├── verbs-worksheet.md             Working verb paradigm tables
│   └── verbs.md                       Verbal morphology architecture
├── tools/
│   └── pie-2-ghandwa.jsx             PIE→Ghandwa phonological transformer
└── vocab/
    ├── alphabet-notes.md              Alphabet and grapheme notes
    ├── alphabet.tsv                   Alphabet table (Old Italic mappings)
    ├── lexicon-gaps.md                Tracked lexical gaps (~21 items)
    ├── lexicon-reconcile.tsv          Reconciliation workspace (in progress)
    ├── lexicon-staging.md             Staging notes for candidate entries
    ├── lexicon.md                     Lexicon changelog
    └── lexicon.tsv                    Primary lexicon (~520 entries, 68 columns)
```

---

## Key files

**`vocab/lexicon.tsv`** — the primary artifact. Hand-edited in Apple Numbers on macOS. 68 tab-separated columns covering lemma forms, IPA, glosses, stem classes, PIE preforms, cognates across 4 branches, semantic fields, cross-references, and transformer test columns. Companion changelog in `vocab/lexicon.md`.

**`tools/pie-2-ghandwa.jsx`** — the phonological transformer. A React JSX artifact that takes PIE input forms and derives Ghandwa surface forms through an ordered rule pipeline. Authoritative for surface forms — hand-derived forms must be verified against it. Can be run headlessly via Node.js.

**`docs/phonological-history.md`** — the narrative companion to the transformer. Full rule inventory with formal statements, examples, ordering arguments, and design rationale.

**`docs/daughters.md`** — the daughter-language framework. Staged A/B/C branch model with landed sound changes and morphological directions. Appendices contain provisional material from earlier sessions (7-zone dialect geography, CS register decisions).

---

## References

- Ringe, Don. 2017. *From Proto-Indo-European to Proto-Germanic*. 2nd ed. Oxford.
- Ringe, Don. 2024. *A Linguistic History of Greek*.
- Kroonen, Guus. *Etymological Dictionary of Proto-Germanic* (EDPG).
- De Vaan, Michiel. *Etymological Dictionary of Latin and the Other Italic Languages* (EDL).
- Matasović, Ranko. *Etymological Dictionary of Proto-Celtic* (EDPC).

---

## Conventions

- Ghandwa forms are *italicized*. IPA/pronunciation is non-italic.
- Cross-references between lexicon entries use `lemma_1` strings, not numeric IDs.
- All `.md` files carry a YAML-style changelog header with ISO 8601 timestamps and line counts.
- The `.tsv` lexicon's changelog lives in a companion `.md` file with the same base name.
