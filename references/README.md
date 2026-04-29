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

### Van Sluis, Jørgensen & Kroonen 2023 — `sluis-2023/`
**Paulus van Sluis, Anders Richardt Jørgensen, Guus Kroonen. "European Prehistory between Celtic and Germanic: the Celto-Germanic Isoglosses Revisited." In Kristiansen & Willerslev (eds.), *The Indo-European Puzzle Revisited*. Cambridge University Press.**  
Roles: `LEX` `SUB`  
Extraction: complete-working. Markdown + 7 structured TSVs: full isogloss table, compelling isoglosses (80), doubtful isoglosses (50), rejected isoglosses (140), classification schema (RT/MO/SM/LX × IE/loan categories), temporal strata (0–IV), contact mechanisms.  
Primary use: determining whether a Ghandwa lexical item reflects NWIE inheritance, Celto-Germanic shared innovation, or contact; strata model for dating isoglosses relative to PC and PGmc sound laws; classification schema for lexical evidence.

---

### Eska 2018a — `eska-2018-laryngeal-realism/`
**Joseph F. Eska. "Laryngeal Realism and the Prehistory of Celtic." *Transactions of the Philological Society* 116/3: 320–331.**  
Roles: `DIAC` `SUB`  
Extraction: complete, second pass. See `eska-2018-laryngeal-realism/eska-2018-laryngeal-realism.md`.  
Primary use: laryngeal methodology as applied to the Celtic branch; argues from laryngeal evidence for a specific model of Celtic prehistory relevant to NWIE reconstruction. Cross-reference with Deuffic and Swanenvleugel on the Celtic phonological history side.

---

### Eska 2018b — `eska-2018-celto-germanic-lexis/`
**Joseph F. Eska. "Celto-Germanic Lexis in Light of Laryngeal Realism." In Goldstein, Jamison & Vine (eds.), *Proceedings of the 29th Annual UCLA Indo-European Conference*. Bremen: Hempen. pp. 29–45.**  
Roles: `LEX` `SUB` `DIAC`  
Extraction: in progress (second-pass OCR cleanup exists in directory but not yet finalized). Raw OCR and first-pass retained for audit.  
Primary use: applies the laryngeal realism framework to shared Celtic-Germanic lexical material; directly relevant to Ghandwa's WIE positioning and to lexical items in the van Sluis isogloss set.

---

### Eska 2023 — `eska-2023/`
**Joseph F. Eska. "Grounding Celtic diachronic phonology II." *Die Sprache: Zeitschrift für Sprachwissenschaft* 55 (2022/2023): 1–21.**  
Roles: `DIAC`  
Extraction: in progress.  
Primary use: part of Eska's laryngeal realism / Celtic phonology series (alongside 2018a, 2018b, 2024). Covers \*/j/ > /ð/ in proto-Brittonic, \*-/nthL/- > -/θL/- in Old Welsh, and \*/lthr/ evolution in Welsh — relevant as comparanda for Ghandwa consonant cluster outcomes.

---

### Eska 2024 — `eska-2024/`
**Joseph F. Eska. "Celtic in Greek characters and implications for Greek and Celtic phonology." *Indogermanische Forschungen* (2024): 199–212. DOI: 10.1515/if-2024-0009.**  
Roles: `DIAC` `SUB`  
Extraction: in progress.  
Primary use: fourth item in the Eska laryngeal realism series. Uses Transalpine Celtic inscriptions in Greek characters to argue for [spread glottis] vs. [voice] feature specification in proto-Celtic — has indirect implications for Ghandwa's aspiration treatment and the voiced fricative outcomes of PIE aspirates.

---

### Höfler 2024 — `hofler-2024/`
**Stefan Höfler. "Linnaean linguistics: 'Bear', 'horse', 'wolf' and the Indo-European phylogeny from a zoographical perspective." In Larsson, Olander & Jørgensen (eds.), *Indo-European Interfaces: Integrating Linguistics, Mythology and Archaeology*. Stockholm University Press. pp. 57–90.**  
Roles: `LEX` `SUB`  
Extraction: complete, second pass (2026-04-28).  
Primary use: phylogenetic argumentation from fauna vocabulary (bear, horse, wolf taboo terms and their replacements); relevant to Ghandwa animal lexicon entries and to subgrouping evidence from semantic shift patterns.

---

### Hyllested 2010 — `hyllested-2010/`
**Adam Hyllested. "Precursors to Celtic and Germanic." In Sørensen (ed.), *Per Aspera ad Asteriscos*. 22 pp.**  
Roles: `SUB`  
Extraction: in progress (Xerox WorkCentre scan, landscape A4, rotated 270°; rotation correction required before OCR).  
Primary use: direct argument for the NWIE subgrouping question — shared innovations that precede both PC and PGmc branch-defining sound changes. Directly bears on Ghandwa's position in the family and on how to classify shared lexical material.

---

### Klimp 2013 — `klimp-2013/`
**J. Klimp. *Remnants of \*r/n-stem Heteroclite Inflection in Germanic*. MA thesis (Research Master Linguistics), University of Groningen. Supervisors: G. Kroonen, J.-W. Zwart.**  
Roles: `DIAC` `LEX`  
Extraction: in progress (third-pass draft exists in directory but not yet finalized).  
Primary use: r/n-stem heteroclitic inflection in Germanic, supervised by Kroonen and methodologically aligned with EDPG; relevant to Ghandwa's nominal morphology for neuters with nom./acc. \*-r ~ oblique \*-n-, and to the \*-mn̥ > -man suffix entries.

---

### Koch 2019 — `koch-2019/`
**John T. Koch. "Formation of the Indo-European branches in the light of the Archaeogenetic Revolution." Conference paper, Austrian Academy of Sciences, Vienna, December 2018. Draft dated 19 March 2019.**  
Roles: `SUB`  
Extraction: in progress.  
Primary use: IE branch formation integrating archaeogenetic data; background for the cultural and historical framing in `daughters.md`. Lower priority than the lexical and phonological works.

---

### Koch 2024 — `koch-2024/`
**John T. Koch. "Celto-Germanic and North-West Indo-European vocabulary: Resonances in myth and rock art iconography." Ch. 10 in Larsson, Olander & Jørgensen (eds.), *Indo-European Interfaces: Integrating Linguistics, Mythology and Archaeology*. Stockholm University Press.**  
Roles: `LEX` `SUB`  
Extraction: complete, second pass (2026-04-28). Figures (7) copied from EPUB source and linked. Page anchors from PDF added.  
Primary use: NWIE shared vocabulary with mythological and iconographic comparanda; relevant to Ghandwa lexical strata and to `lore.md` cultural content.

---

### Kroonen, Wigman & Thorsø 2021 — `kroonen-2021/`
**Guus Kroonen, Andrew Wigman & Rasmus Thorsø. "Proto-Indo-European \*sneigʷʰ- 'to fall down; to snow'." *Historische Sprachforschung / Historical Linguistics* 134/1: 214–224. DOI: 10.13109/hisp.2021.134.1.214.**  
Roles: `LEX` `DIAC`  
Extraction: in progress.  
Primary use: reconstruction and cross-branch comparanda for a labiovelar root — directly relevant since Ghandwa preserves labiovelars. Part of the Kroonen–Wigman–Thorsø research cluster alongside Kroonen et al. 2022 and Wigman 2023.

---

### Kroonen et al. 2022 — `kroonen-2022/`
**Guus Kroonen, Anthony Jakob, Axel I. Palmér, Paulus van Sluis & Andrew Wigman. "Indo-European cereal terminology suggests a Northwest Pontic homeland for the core Indo-European languages." *PLOS ONE* (2022).**  
Roles: `LEX` `SUB`  
Extraction: in progress (third-pass draft with structured tables exists in directory but not yet finalized).  
Primary use: agricultural/cereal vocabulary comparanda and reconstruction depth; Northwest Pontic homeland argument. Two uses: (1) grain vocabulary comparanda in the Ghandwa lexicon; (2) cultural-historical framing for `daughters.md`.

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

### Wigman 2023 — `wigman-2023-prehistory-italic/`
**A. M. Wigman. *Unde vēnistī? The Prehistory of Italic through its Loanword Lexicon*. PhD thesis, Leiden University, November 2023.**  
Roles: `LEX` `SUB`  
Extraction: in progress (second-pass + automated third-pass drafts exist in directory but not yet finalized).  
Primary use: Italic branch prehistory through its loanword stratum — distinguishes inherited NWIE/PIt material from substrate and contact loans. Complements Weiss 2020 (sound changes); high priority for LEX work once de Vaan is extracted.

---

### Witczak 2024 — `witczak-2024/`
**Krzysztof Tomasz Witczak. "Greek *Megas* and Latin *Magnus* 'Great, Big, Large': A New Contribution to the Laryngeal Theory." *Linguistica Silesiana* 45/1: 7–20.**  
Roles: `LEX`  
Extraction: complete, second pass. See `witczak-2024/witczak-2024.md`.  
Primary use: specific etymology for PIE \*méǵh₂- 'great'; laryngeal argument relevant to the *magnus* family and secondary *a*-vocalism. Narrow scope — consult when working on this root or adjacent laryngeal questions.

---

## _inbox — stubs not yet processed

| Dir | Work | Status |
|---|---|---|
| `clackson-2007` | Clackson 2007 | Stub only |
| `de-goede-2014` | de Goede 2014 | Stub only |
| `keydana-hock-widmer-eds` | Keydana, Hock & Widmer (eds.) | Stub only |
| `koch-2020` | Koch 2020 | Stub only |
| `kroonen-2012` | Kroonen 2012 | Stub only |
| `kroonen-2016` | Kroonen 2016 | Stub only |
| `matasovic-2010` | Matasović 2010 | Stub only |

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
| 2026-04-28 | Added `references-index.tsv` — 50-row lookup index with `roles`, `extraction_status`, `keywords_source`, `keywords_parsed`, and `ghandwa_notes` for all current sources. |
| 2026-04-28 | Added 10 missing entries (Eska 2018b, Eska 2023, Eska 2024, Höfler 2024, Klimp 2013, Koch 2019, Koch 2024, Kroonen et al. 2021, Kroonen et al. 2022, Wigman 2023). Corrected two wrong paths: `eska-2018/` → split into `eska-2018-laryngeal-realism/` and `eska-2018-celto-germanic-lexis/`; `van-sluis-et-al-2023/` → `sluis-2023/`. Added _inbox table. Marked in-progress extractions correctly. Moved 9 stale notes.md files to `_delete/`. |
| 2026-04-27 | Restructured into per-work subdirectories. Added .gitignore rule for PDFs. Added `hyllested-2010/notes.md` stub. Updated README paths. Initial inventory as of commit `07d7540`. |
