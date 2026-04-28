# References

This directory holds extracted and structured versions of reference works used in the Ghandwa project. Each work lives in its own subdirectory containing the markdown extraction, structured TSVs, and notes. Source PDFs are stored locally alongside the subdirectories but are gitignored (`references/**/*.pdf`).

---

## Role taxonomy

Each reference is tagged with one or more roles:

| Tag | Meaning |
|---|---|
| `LEX` | Lexical / etymological — for looking up individual roots, cognate sets, and comparanda |
| `DIAC` | Diachronic phonology — sound change rules, relative chronology, rule ordering |
| `SUB` | Subgrouping / isoglosses — evidence for branch relationships, contact, and shared innovations |

Works that serve multiple roles are tagged accordingly. The tags determine which references to consult for a given task, not how to cite them.

---

## Reference inventory

### Ringe 2017 — `ringe-2017/`
**Don Ringe, *From Proto-Indo-European to Proto-Germanic*, 2nd ed. Oxford University Press.**  
Roles: `DIAC`  
Extraction: complete, QA-reviewed (three passes). Structured index (4,802 rows: PIE protoforms + attested forms with page references). Chapters 1–4 in markdown. See `ringe-2017/README.md` for full bundle details.  
Primary use: sound change ordering and relative chronology for PGmc; PIE morphology reference (Ch. 2); structured index for root lookup.  
Known gaps: paradigm cells in Chs. 2 and 4 need spot-check against PDF before citation; prose-in-fence artifacts and paradigm cell spacing artifacts pending cleanup (see `ringe-2017-cleanup-handoff.md` in repo root).

---

### Swanenvleugel 2021 — `swanenvleugel-2021/`
**Swanenvleugel, PhD thesis, Proto-Italo-Celtic phonology and TAM.**  
Roles: `DIAC` `SUB`  
Extraction: complete-working. Markdown + 4 structured TSVs: PIC sound changes, obstruent systems, PIC phoneme inventory, TAM summary. Appendices A–C cleaned against PDF.  
Primary use: PIC phonology as comparanda for Ghandwa sound changes; TAM morphology reference; PIC unity argument (subgrouping).

---

### Deuffic 2021 — `deuffic-2021/`
**Deuffic, PhD thesis, relative chronology PIE to Proto-Celtic.**  
Roles: `DIAC` `SUB`  
Extraction: complete-working (targeted cleanup pass). Markdown + 4 structured TSVs including dependency edges (`deuffic-relative-chronology-edges.tsv`). Staged chronology: Late Indo-European / Italo-Celtic / Proto-Celtic.  
Primary use: rule-ordering model for Ghandwa phonological history; dependency-graph approach to chronology (partial order rather than flat numbered list); PC sound change inventory for comparison.  
Known gaps: superscript aspirates and some combining diacritics need checking before use as canonical forms. See `deuffic-2021/notes.md`.

---

### Van Sluis, Jørgensen & Kroonen 2023 — `van-sluis-et-al-2023/`
**Paulus van Sluis, Anders Richardt Jørgensen, Guus Kroonen. "European Prehistory between Celtic and Germanic: the Celto-Germanic Isoglosses Revisited." In Kristiansen & Willerslev (eds.), *The Indo-European Puzzle Revisited*. Cambridge University Press.**  
Roles: `LEX` `SUB`  
Extraction: complete-working. Markdown + 7 structured TSVs: full isogloss table, compelling isoglosses (80), doubtful isoglosses (50), rejected isoglosses (140), classification schema (RT/MO/SM/LX × IE/loan categories), temporal strata (0–IV), contact mechanisms.  
Primary use: determining whether a Ghandwa lexical item reflects NWIE inheritance, Celto-Germanic shared innovation, or contact; strata model for dating isoglosses relative to PC and PGmc sound laws; classification schema for lexical evidence.

---

### Eska 2018 — `eska-2018/`
**Joseph F. Eska. "Laryngeal Realism and the Prehistory of Celtic." *Transactions of the Philological Society* 116/3: 320–331.**  
Roles: `DIAC` `SUB`  
Extraction: complete, second pass. See `eska-2018/eska-2018.md`.  
Primary use: laryngeal methodology as applied to the Celtic branch; argues from laryngeal evidence for a specific model of Celtic prehistory relevant to NWIE reconstruction. Cross-reference with Deuffic and Swanenvleugel on the Celtic phonological history side.

---

### Hyllested 2010 — `hyllested-2010/`
**Adam Hyllested. "Precursors to Celtic and Germanic."**  
Roles: `SUB`  
Extraction: PDF only (Xerox scan, 22 pp., landscape, rotated). ChatGPT extraction in progress. See `hyllested-2010/notes.md`.  
Primary use: direct argument for the NWIE subgrouping question — what Celtic and Germanic share before either set of branch-specific innovations. Directly bears on Ghandwa's position in the family.

---

### Matasović 2009 — `matasovic-2009/`
**Ranko Matasović, *Etymological Dictionary of Proto-Celtic*. Brill.**  
Roles: `LEX`  
Extraction: front matter and introduction only (PDF pages 1–27). Dictionary proper not yet extracted. See `matasovic-2009/matasovic-2009-frontmatter.md`.  
Primary use: PC cognates and etymologies for lexicon comparanda columns. The introduction covers PC phonology and morphology, useful as orientation.

---

### Weiss 2020 — `weiss-2020/`
**Michael Weiss, *Outline of the Historical and Comparative Grammar of Latin*, 2nd ed. Beech Stave Press.**  
Roles: `LEX` `DIAC`  
Extraction: targeted — pp. 175–179 only (Ch. 29, athematic nominal suffixes, n-stems). Full extraction pending (bad scan; OCR quality is a risk for diacritic-heavy notation). See `weiss-2020/weiss-2020-p175-179.md`.  
Primary use: Latin/Italic comparanda; Italic sound changes for comparison with Ghandwa; nominal derivation (the extracted section covers n-stems directly relevant to open lexicon entries).

---

### Witczak 2024 — `witczak-2024/`
**Krzysztof Tomasz Witczak. "Greek *Megas* and Latin *Magnus* 'Great, Big, Large': A New Contribution to the Laryngeal Theory." *Linguistica Silesiana* 45/1: 7–20.**  
Roles: `LEX`  
Extraction: complete, second pass. See `witczak-2024/witczak-2024.md`.  
Primary use: specific etymology for PIE \*méǵh₂- 'great'; laryngeal argument relevant to the *magnus* family and secondary *a*-vocalism. Narrow scope — consult when working on this root or adjacent laryngeal questions.

---

## Pending / planned

| Work | Roles | Status |
|---|---|---|
| Ringe 2024, *A Linguistic History of Greek* | `DIAC` | Not yet acquired |
| Kroonen 2013, *Etymological Dictionary of Proto-Germanic* | `LEX` | Not yet extracted |
| De Vaan 2008, *Etymological Dictionary of Latin* | `LEX` | Not yet extracted |
| Derksen 2008, *Etymological Dictionary of the Slavic Inherited Lexicon* | `LEX` | Not yet acquired |
| Derksen 2015, *Etymological Dictionary of the Baltic Inherited Lexicon* | `LEX` | Not yet acquired |
| Beekes 2010, *Etymological Dictionary of Greek* | `LEX` | Not yet acquired |
| LIV = Rix et al. 2001, *Lexikon der indogermanischen Verben*, 2nd ed. | `LEX` `DIAC` | Not yet acquired |
| Schrijver, Italo-Celtic linguistic unity | `DIAC` `SUB` | Not yet acquired — verify format (may be article, not monograph) |
| Olander (ed.) 2023, *The Indo-European Language Family* | `SUB` | Not yet acquired |
| Fortson 2010, *Indo-European Language and Culture*, 2nd ed. | `DIAC` `SUB` | Not yet acquired |
| Dunkel 2014, *Lexikon der indogermanischen Partikeln und Pronominalstämme* | `LEX` | Not yet acquired |

---

## Changelog

| Date | Change |
|---|---|
| 2026-04-27 | Restructured into per-work subdirectories. Added .gitignore rule for PDFs. Added `hyllested-2010/notes.md` stub. Updated README paths. Initial inventory as of commit `07d7540`. |
