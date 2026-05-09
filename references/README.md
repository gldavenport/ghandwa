# References

This directory holds extracted and structured versions of reference works used in the Ghandwa project. Each work lives in its own subdirectory containing the markdown extraction, structured TSVs, and notes. Source PDFs are stored locally alongside the subdirectories but are gitignored (`references/**/*.pdf`).

---

## Role taxonomy

Each reference is tagged with one or more roles drawn from the axes below. Tags are lowercase, hyphenated where multi-word. A source receives only the tags for which it is a *primary* resource on that axis — not every branch or subfield it mentions in passing. Tags are the structured filter layer; `keywords_parsed` in the TSV is the free-text search layer. These two are complementary, not redundant.

**Subfield**

| Tag | Meaning |
|---|---|
| `lexical` | Etymological and lexical — root lookup, cognate sets, comparanda |
| `diachronic` | Diachronic phonology — sound change rules, relative chronology, rule ordering |
| `phonology` | Phonological description or reconstruction — inventory, alternations, prosody (synchronic or diachronic) |
| `morphology` | Morphological description or reconstruction — nominal/verbal paradigms, derivation, inflectional categories |
| `prosody` | Accent, ablaut, tone, and stress patterns |
| `phylogeny` | Branch relationships, subgrouping, isoglosses, shared innovations |
| `contact` | Language contact, substrate analysis, loanword stratigraphy |
| `epigraphy` | Inscription analysis, decipherment, epigraphic methodology |
| `computational` | Computational or statistical phylogenetics and quantitative methods |
| `reconstruction` | Reconstruction methodology — primarily about *how* to reconstruct, not just outputs |

**Branch**

| Tag | Meaning |
|---|---|
| `italic` | Italic branch (Latin, Oscan, Umbrian, Venetic, Faliscan, Lusitanian) |
| `celtic` | Celtic branch (Gaulish, Celtiberian, Brittonic, Goidelic, Lepontic) |
| `germanic` | Germanic branch |
| `balto-slavic` | Baltic and Slavic branches |
| `greek` | Greek branch |
| `anatolian` | Anatolian branch (Hittite, Luwian, Lycian, Lydian) |
| `indo-iranian` | Indo-Iranian branch |

**Culture / Lore**

| Tag | Meaning |
|---|---|
| `myth` | Comparative mythology — narrative structure, tale types, mythological motifs |
| `ritual` | Ritual practice, cult organization, sacred space, sacrifice terminology |
| `theonymy` | Divine name formation, cult epithets, theonymic distribution |
| `material-culture` | Culturally-loaded vocabulary — metals, grains, tools, animals as domesticates |
| `formulaic` | Reconstructed poetic formulae, epithets, and collocations |

**Output type**

| Tag | Meaning |
|---|---|
| `corpus` | Models inscription types, formulaic registers, or pragmatic text patterns for Ghandwa corpus composition |
| `onomastics` | Personal, place, ethnic, and divine name formation patterns for the Ghandwa onomastic register |

**Note on source_id convention:** `references-index.tsv` source_id values are ASCII-normalized (umlauts and diacritics dropped). Directory names preserve Unicode. This is intentional.

---

## Reference inventory

### Ringe 2017 — `ringe-2017/`
**Don Ringe, *From Proto-Indo-European to Proto-Germanic*, 2nd ed. Oxford University Press.**  
Roles: `diachronic` `phonology` `morphology` `germanic`  
Extraction: complete, QA-reviewed (three passes). Structured index (4,802 rows: PIE protoforms + attested forms with page references). Chapters 1–4 in markdown. See `ringe-2017/README.md` for full bundle details.  
Primary use: sound change ordering and relative chronology for PGmc; PIE morphology reference (Ch. 2); structured index for root lookup.  
Known gaps: paradigm cells in Chs. 2 and 4 need spot-check against PDF before citation; prose-in-fence artifacts and paradigm cell spacing artifacts pending cleanup (see `ringe-2017-cleanup-handoff.md` in repo root).

---

### Ringe 2024 — `ringe-2024/`
**Don Ringe, *The Linguistic Roots of Ancient Greek*. Oxford University Press.**  
Roles: `diachronic` `phonology` `greek`  
Extraction: complete. Character-fidelity-verified extraction with high-risk form index TSV and visual-text reference file. See `ringe-2024/README.md`.  
Primary use: thorn-cluster outcomes; Greek phonological history as comparanda for Ghandwa; laryngeal evidence from Greek. Previously listed as "not yet acquired" — present and extracted.

---

### Swanenvleugel 2021 — `swanenvleugel-2021/`
**Swanenvleugel, PhD thesis, Proto-Italo-Celtic phonology and TAM.**  
Roles: `diachronic` `phonology` `morphology` `phylogeny` `italic` `celtic`  
Extraction: complete-working. Markdown + 4 structured TSVs: PIC sound changes, obstruent systems, PIC phoneme inventory, TAM summary. Appendices A–C cleaned against PDF.  
Primary use: PIC phonology as comparanda for Ghandwa sound changes; TAM morphology reference; PIC unity argument (subgrouping).

---

### Deuffic 2021 — `deuffic-2021/`
**Deuffic, PhD thesis, relative chronology PIE to Proto-Celtic.**  
Roles: `diachronic` `phonology` `phylogeny` `celtic`  
Extraction: complete-working (targeted cleanup pass). Markdown + 4 structured TSVs including dependency edges (`deuffic-relative-chronology-edges.tsv`). Staged chronology: Late Indo-European / Italo-Celtic / Proto-Celtic.  
Primary use: rule-ordering model for Ghandwa phonological history; dependency-graph approach to chronology (partial order rather than flat numbered list); PC sound change inventory for comparison.  
Known gaps: superscript aspirates and some combining diacritics need checking before use as canonical forms. See `deuffic-2021/notes.md`.

---

### Van Sluis, Jørgensen & Kroonen 2023 — `sluis-2023/`
**Paulus van Sluis, Anders Richardt Jørgensen, Guus Kroonen. "European Prehistory between Celtic and Germanic: the Celto-Germanic Isoglosses Revisited." In Kristiansen & Willerslev (eds.), *The Indo-European Puzzle Revisited*. Cambridge University Press.**  
Roles: `lexical` `phylogeny` `contact` `celtic` `germanic`  
Extraction: complete-working. Markdown + 7 structured TSVs: full isogloss table, compelling isoglosses (80), doubtful isoglosses (50), rejected isoglosses (140), classification schema (RT/MO/SM/LX × IE/loan categories), temporal strata (0–IV), contact mechanisms.  
Primary use: determining whether a Ghandwa lexical item reflects NWIE inheritance, Celto-Germanic shared innovation, or contact; strata model for dating isoglosses relative to PC and PGmc sound laws; classification schema for lexical evidence.

---

### Eska 2018a — `eska-2018-laryngeal-realism/`
**Joseph F. Eska. "Laryngeal Realism and the Prehistory of Celtic." *Transactions of the Philological Society* 116/3: 320–331.**  
Roles: `diachronic` `phonology` `phylogeny` `celtic`  
Extraction: complete, second pass. See `eska-2018-laryngeal-realism/eska-2018-laryngeal-realism.md`.  
Primary use: laryngeal methodology as applied to the Celtic branch; argues from laryngeal evidence for a specific model of Celtic prehistory relevant to NWIE reconstruction. Cross-reference with Deuffic and Swanenvleugel on the Celtic phonological history side.

---

### Eska 2018b — `eska-2018-celto-germanic-lexis/`
**Joseph F. Eska. "Celto-Germanic Lexis in Light of Laryngeal Realism." In Goldstein, Jamison & Vine (eds.), *Proceedings of the 29th Annual UCLA Indo-European Conference*. Bremen: Hempen. pp. 29–45.**  
Roles: `lexical` `diachronic` `phonology` `phylogeny` `celtic` `germanic`  
Extraction: in progress (second-pass OCR cleanup exists in directory but not yet finalized). Raw OCR and first-pass retained for audit.  
Primary use: applies the laryngeal realism framework to shared Celtic-Germanic lexical material; directly relevant to Ghandwa's WIE positioning and to lexical items in the van Sluis isogloss set.

---

### Eska 2023 — `eska-2023/`
**Joseph F. Eska. "Grounding Celtic diachronic phonology II." *Die Sprache: Zeitschrift für Sprachwissenschaft* 55 (2022/2023): 1–21.**  
Roles: `diachronic` `phonology` `celtic`  
Extraction: in progress.  
Primary use: part of Eska's laryngeal realism / Celtic phonology series (alongside 2018a, 2018b, 2024). Covers \*/j/ > /ð/ in proto-Brittonic, \*-/nthL/- > -/θL/- in Old Welsh, and \*/lthr/ evolution in Welsh — relevant as comparanda for Ghandwa consonant cluster outcomes.

---

### Eska 2024 — `eska-2024/`
**Joseph F. Eska. "Celtic in Greek characters and implications for Greek and Celtic phonology." *Indogermanische Forschungen* (2024): 199–212. DOI: 10.1515/if-2024-0009.**  
Roles: `diachronic` `phonology` `phylogeny` `celtic` `greek`  
Extraction: in progress.  
Primary use: fourth item in the Eska laryngeal realism series. Uses Transalpine Celtic inscriptions in Greek characters to argue for [spread glottis] vs. [voice] feature specification in proto-Celtic — has indirect implications for Ghandwa's aspiration treatment and the voiced fricative outcomes of PIE aspirates.

---

### Höfler 2024 — `hofler-2024/`
**Stefan Höfler. "Linnaean linguistics: 'Bear', 'horse', 'wolf' and the Indo-European phylogeny from a zoographical perspective." In Larsson, Olander & Jørgensen (eds.), *Indo-European Interfaces: Integrating Linguistics, Mythology and Archaeology*. Stockholm University Press. pp. 57–90.**  
Roles: `lexical` `phylogeny` `myth` `material-culture`  
Extraction: complete, second pass (2026-04-28).  
Primary use: phylogenetic argumentation from fauna vocabulary (bear, horse, wolf taboo terms and their replacements); relevant to Ghandwa animal lexicon entries and to subgrouping evidence from semantic shift patterns.

---

### Hyllested 2010 — `hyllested-2010/`
**Adam Hyllested. "Precursors to Celtic and Germanic." In Sørensen (ed.), *Per Aspera ad Asteriscos*. 22 pp.**  
Roles: `phylogeny` `celtic` `germanic`  
Extraction: in progress (Xerox WorkCentre scan, landscape A4, rotated 270°; rotation correction required before OCR).  
Primary use: direct argument for the NWIE subgrouping question — shared innovations that precede both PC and PGmc branch-defining sound changes. Directly bears on Ghandwa's position in the family and on how to classify shared lexical material.

---

### Klimp 2013 — `klimp-2013/`
**J. Klimp. *Remnants of \*r/n-stem Heteroclite Inflection in Germanic*. MA thesis (Research Master Linguistics), University of Groningen. Supervisors: G. Kroonen, J.-W. Zwart.**  
Roles: `diachronic` `lexical` `morphology` `germanic`  
Extraction: in progress (third-pass draft exists in directory but not yet finalized).  
Primary use: r/n-stem heteroclitic inflection in Germanic, supervised by Kroonen and methodologically aligned with EDPG; relevant to Ghandwa's nominal morphology for neuters with nom./acc. \*-r ~ oblique \*-n-, and to the \*-mn̥ > -man suffix entries.

---

### Koch 2019 — `koch-2019/`
**John T. Koch. "Formation of the Indo-European branches in the light of the Archaeogenetic Revolution." Conference paper, Austrian Academy of Sciences, Vienna, December 2018. Draft dated 19 March 2019.**  
Roles: `phylogeny`  
Extraction: in progress.  
Primary use: IE branch formation integrating archaeogenetic data; background for the cultural and historical framing in `daughters.md`. Lower priority than the lexical and phonological works.

---

### Koch 2024 — `koch-2024/`
**John T. Koch. "Celto-Germanic and North-West Indo-European vocabulary: Resonances in myth and rock art iconography." Ch. 10 in Larsson, Olander & Jørgensen (eds.), *Indo-European Interfaces: Integrating Linguistics, Mythology and Archaeology*. Stockholm University Press.**  
Roles: `lexical` `phylogeny` `myth` `formulaic` `celtic` `germanic`  
Extraction: complete, second pass (2026-04-28). Figures (7) copied from EPUB source and linked. Page anchors from PDF added.  
Primary use: NWIE shared vocabulary with mythological and iconographic comparanda; relevant to Ghandwa lexical strata and to `lore.md` cultural content.

---

### Kroonen, Wigman & Thorsø 2021 — `kroonen-2021/`
**Guus Kroonen, Andrew Wigman & Rasmus Thorsø. "Proto-Indo-European \*sneigʷʰ- 'to fall down; to snow'." *Historische Sprachforschung / Historical Linguistics* 134/1: 214–224. DOI: 10.13109/hisp.2021.134.1.214.**  
Roles: `lexical` `diachronic` `phonology` `germanic`  
Extraction: in progress.  
Primary use: reconstruction and cross-branch comparanda for a labiovelar root — directly relevant since Ghandwa preserves labiovelars. Part of the Kroonen–Wigman–Thorsø research cluster alongside Kroonen et al. 2022 and Wigman 2023.

---

### Kroonen et al. 2022 — `kroonen-2022/`
**Guus Kroonen, Anthony Jakob, Axel I. Palmér, Paulus van Sluis & Andrew Wigman. "Indo-European cereal terminology suggests a Northwest Pontic homeland for the core Indo-European languages." *PLOS ONE* (2022).**  
Roles: `lexical` `phylogeny` `material-culture`  
Extraction: in progress (third-pass draft with structured tables exists in directory but not yet finalized).  
Primary use: agricultural/cereal vocabulary comparanda and reconstruction depth; Northwest Pontic homeland argument. Two uses: (1) grain vocabulary comparanda in the Ghandwa lexicon; (2) cultural-historical framing for `daughters.md`.

---

### Matasović 2009 — `matasovic-2009/`
**Ranko Matasović, *Etymological Dictionary of Proto-Celtic*. Brill.**  
Roles: `lexical` `celtic`  
Extraction: front matter and introduction only (PDF pages 1–27). Dictionary proper not yet extracted. See `matasovic-2009/matasovic-2009-frontmatter.md`.  
Primary use: PC cognates and etymologies for lexicon comparanda columns. The introduction covers PC phonology and morphology, useful as orientation.

---

### Weiss 2020 — `weiss-2020/`
**Michael Weiss, *Outline of the Historical and Comparative Grammar of Latin*, 2nd ed. Beech Stave Press.**  
Roles: `lexical` `diachronic` `phonology` `morphology` `italic`  
Extraction: targeted — pp. 175–179 only (Ch. 29, athematic nominal suffixes, n-stems). Full extraction pending (bad scan; OCR quality is a risk for diacritic-heavy notation). See `weiss-2020/weiss-2020-p175-179.md`.  
Primary use: Latin/Italic comparanda; Italic sound changes for comparison with Ghandwa; nominal derivation (the extracted section covers n-stems directly relevant to open lexicon entries).

---

### Wigman 2023 — `wigman-2023-prehistory-italic/`
**A. M. Wigman. *Unde vēnistī? The Prehistory of Italic through its Loanword Lexicon*. PhD thesis, Leiden University, November 2023.**  
Roles: `lexical` `phylogeny` `contact` `italic`  
Extraction: in progress (second-pass + automated third-pass drafts exist in directory but not yet finalized).  
Primary use: Italic branch prehistory through its loanword stratum — distinguishes inherited NWIE/PIt material from substrate and contact loans. Complements Weiss 2020 (sound changes); high priority for LEX work once de Vaan is extracted.

---

### Witczak 2024 — `witczak-2024/`
**Krzysztof Tomasz Witczak. "Greek *Megas* and Latin *Magnus* 'Great, Big, Large': A New Contribution to the Laryngeal Theory." *Linguistica Silesiana* 45/1: 7–20.**  
Roles: `lexical` `diachronic` `phonology` `greek` `italic`  
Extraction: complete, second pass. See `witczak-2024/witczak-2024.md`.  
Primary use: specific etymology for PIE \*méǵh₂- 'great'; laryngeal argument relevant to the *magnus* family and secondary *a*-vocalism. Narrow scope — consult when working on this root or adjacent laryngeal questions.

---

### Kroonen 2013 — `kroonen-2013/`
**Guus Kroonen, *Etymological Dictionary of Proto-Germanic*. Brill.**  
Roles: `lexical` `germanic`  
Extraction: complete (seventh combined targeted pass). Structured lexical dataset (CSV + Markdown), correction ledger, headword-line verification, residual audit. See `kroonen-2013/README.md`.  
Primary use: PGmc cognates and etymologies for lexicon `cog_Germanic` column backfill; primary PGmc etymological dictionary alongside Orel 2003. Previously listed as "not yet extracted" — present and extracted.

---

### LIV² — `LIV²/`
**Helmut Rix et al., *Lexikon der indogermanischen Verben*, 2nd ed. Reichert.**  
Roles: `lexical` `diachronic` `morphology`  
Extraction: complete for the addenda/corrigenda (LIV²add). Structured dataset (CSV + JSONL): lexical entries, stem statements, reconstructed forms index, cross-references. Main dictionary body not separately extracted. See `LIV²/README.md`.  
Primary use: verbal root inventory and stem-type coverage; addenda/corrigenda cover roots revised or added after the first edition. Cross-reference with Ghandwa lexicon `verb_stem_type` and `lemma_1_pre_root` columns. Full dictionary body actively sought.

---

### Olander 2022 — `olander-2022/`
**Thomas Olander, ed. *The Indo-European Language Family: A Phylogenetic Perspective*. Cambridge University Press.**  
Roles: `diachronic` `phylogeny`  
Extraction: complete (fourth pass). Full-volume Markdown + chapter-by-chapter files + figures/tables companion + character audit. See `olander-2022/README.md`.  
Primary use: IE phylogeny from multiple disciplinary angles; subgrouping evidence relevant to Ghandwa's WIE position; chapter-level extraction enables targeted lookup.  
Note: previously listed in Pending as "Olander 2023, not yet acquired" — year is 2022; present and extracted.

---

### West 2007 — `west-2007/`
**M. L. West, *Indo-European Poetry and Myth*. Oxford University Press.**  
Roles: `lexical` `corpus` `myth` `ritual` `formulaic`  
Extraction: complete (third pass). Main Markdown + structural outline + extraction notes. See `west-2007/README.md`.  
Primary use: comparative IE poetic and mythological formulae; directly feeds `lore.md` religious/ritual vocabulary and `corpus/` composition. High priority for CORP and ONOM tasks. Caution: verify Greek, Vedic, and PIE reconstructions against page images before citation.

---

### Bjørn 2017 — `bjørn-2017/`
**Rasmus Gudmundsen Bjørn, "Foreign elements in the Proto-Indo-European vocabulary: A Comparative Loanword Study." Prize paper / MA thesis (2017).**  
Roles: `lexical` `phylogeny` `contact`  
Extraction: complete (fourth pass). Main Markdown + structured lexical dataset (135 items, CSV + Markdown) + normalized bibliography. See `bjørn-2017/README.md`.  
Primary use: systematic catalog of non-PIE-inherited vocabulary (substrate candidates, Wanderwörter); methodology for distinguishing inherited vs. borrowed in the Ghandwa lexicon. Cross-reference with van Sluis 2023 and Wigman 2023.

---

### Clackson 2007 — `clackson-2007/`
**James Clackson, *Indo-European Linguistics: An Introduction*. Cambridge University Press.**  
Roles: `diachronic` `phonology` `morphology` `phylogeny`  
Extraction: complete (fourth pass). Main Markdown + character audit + heading and table audit + extraction notes. See `clackson-2007/README.md`.  
Primary use: standard IE linguistics textbook; broad phonological and morphological reference for all branches; useful orientation for sound rule application and branch-level survey. Tables and indexes are text-extraction artifacts — verify layout from PDF for source-critical use.

---

### Clackson 2013 — `clackson-2013/`
**James Clackson, "Subgrouping in the Sabellian Branch of Indo-European." *Transactions of the Philological Society* (2013). DOI: 10.1111/1467-968X.12034.**  
Roles: `diachronic` `phonology` `phylogeny` `italic`  
Extraction: complete (fifth pass). Main Markdown + normalized bibliography + character audit. See `clackson-2013/README.md`.  
Primary use: Sabellian internal subgrouping evidence (Oscan, Umbrian, South Picene); Italic sub-branch isoglosses as comparanda for Ghandwa's Proto-Italic positioning.

---

### Fagiolo et al. 2024 — `fagiolo-2024/`
**Virna Fagiolo, Daniel Ayora Estevan & Esteban Ngomo Fernández. "Snakes, dragons, and hydras: the Indo-European terminology for serpent." *Cuadernos de Filología Clásica. Estudios griegos e indoeuropeos* 34 (2024): 17–28. DOI: 10.5209/cfcg.91438.**  
Roles: `lexical` `myth` `material-culture`  
Extraction: complete (fourth pass). Main Markdown + extracted forms index. See `fagiolo-2024/README.md`.  
Primary use: cross-branch reconstruction of IE serpent/dragon vocabulary; relevant to Ghandwa fauna lexicon entries and `lore.md` mythological content.

---

### Graça da Silva & Tehrani 2016 — `graça-da-silva-2016/`
**Sara Graça da Silva & Jamshid J. Tehrani. "Comparative phylogenetic analyses uncover the ancient roots of Indo-European folktales." *Royal Society Open Science* 3 (2016): 150645. DOI: 10.1098/rsos.150645.**  
Roles: `phylogeny` `myth` `computational`  
Extraction: complete. Main Markdown + Figure 4 ancestral-tale-corpora CSV + confidence/character/bibliography audits. See `graça-da-silva-2016/README.md`.  
Primary use: phylogenetic analysis of IE folktale distribution; background methodology for `daughters.md` mythology-subgrouping claims. Lower priority than linguistic sources.

---

### Mikhailova 2021 — `mikhailova-2021/`
**Tatyana A. Mikhailova. "Night-mare: on the origin of a trope in Celtic and Germanic (a response to Stephen Pax Leonard)." *Journal of Language Relationship* 19/1 (2021): 15–24.**  
Roles: `lexical` `phylogeny` `myth` `celtic` `germanic`  
Extraction: complete (third pass). Main Markdown + extracted forms table + extraction notes. See `mikhailova-2021/README.md`.  
Primary use: Celtic-Germanic shared trope in the night-mare complex; NWIE vocabulary with mythological comparanda for Ghandwa fauna/mythology vocabulary and `lore.md`.

---

### Anthony 2013 — `anthony-2013/`
**David W. Anthony. "Two IE phylogenies, three PIE migrations, and four kinds of steppe pastoralism." *Journal of Language Relationship* 9 (2013): 1–21.**  
Roles: `phylogeny`  
Extraction: complete (third pass). Main Markdown. See `anthony-2013/README.md`.  
Primary use: IE phylogeny and steppe migration model; background for `daughters.md` cultural-historical framing. Lower priority than linguistic sources.

---

### Anthony 2023 — `anthony-2023/`
**David W. Anthony. "Ten Constraints that Limit the Late PIE Homeland to the Steppes." (2023).**  
Roles: `phylogeny`  
Extraction: complete. Main Markdown + extracted forms companion + bibliography files. See `anthony-2023/anthony-2023-readme.md`.  
Primary use: systematic constraint model for PIE steppe homeland; background for `daughters.md` cultural framing. Lower priority than linguistic sources.

---

### Clackson et al. 2020 — `clackson-ed-2020/`
**James Clackson (ed.), *Migration, Mobility and Language Contact in and around the Ancient Mediterranean*. Cambridge University Press.**  
Roles: `phylogeny` `contact` `corpus` `onomastics` `italic`  
Extraction: complete. Front matter, Chapters 1–11, bibliography, index. See `clackson-ed-2020-migration-mobility-language-contact/README.md`.  
Primary use: chapters on Oscan alphabet origins (Ch. 5), Etruscan onomastics (Ch. 2), multilingualism in Delos (Ch. 8), and migration in the city of Rome (Ch. 11) are relevant to Ghandwa CORP and ONOM tasks; Ch. 7 (Mamertini) provides a model for mercenary-register language contact scenarios usable in `corpus/`.

---

### Fortson 2010 — `fortson-2010/`
**Benjamin W. Fortson IV, *Indo-European Language and Culture: An Introduction*, 2nd ed. Wiley-Blackwell.**  
Roles: `diachronic` `phonology` `morphology` `phylogeny` `italic` `celtic` `germanic`  
Extraction: complete. Full chapter-level extraction (20 chapters + glossary + bibliography + index). Page ranges not encoded in EPUB. See `fortson-2010-indo-european-language-culture/README.md`.  
Primary use: comprehensive IE branch survey and PIE phonology/morphology reference; Chs. 13–15 (Italic, Celtic, Germanic) are direct reference points for Ghandwa WIE positioning; Ch. 3 (PIE phonology) and Ch. 6 (nominal morphology) for PIE reconstruction orientation. Previously listed in Pending as "not yet acquired" — present and extracted.

---

### Kapović 2017 — `kapovic-ed-2017/`
**Mate Kapović (ed.), *The Indo-European Languages*, 2nd ed. Routledge.**  
Roles: `diachronic` `phonology` `morphology` `phylogeny` `italic` `celtic` `germanic` `balto-slavic`  
Extraction: complete. Full chapter-level extraction (12 parts, 45+ chapters) with bibliographies separated by chapter. See `kapovic-ed-2017-ie-languages-2nd/README.md`.  
Primary use: comprehensive multi-author IE language reference; PIE phonology (Part 1 Ch. 1), PIE morphology (Part 1 Ch. 2), Italic (Part 6), Celtic (Part 7), and Germanic (Part 8) are primary WIE reference chapters for Ghandwa comparanda; Baltic and Slavic (Part 11) for eastern comparanda.

---

### Putnam 2020 — `putnam-ed-2020/`
**Michael Putnam (ed.), *The Cambridge Handbook of Germanic Linguistics*. Cambridge University Press.**  
Roles: `diachronic` `phonology` `morphology` `phylogeny` `germanic`  
Extraction: complete. 35 chapters covering phonology, morphology, syntax, semantics, contact, and dialects. Extraction date 2026-05-07. See `putnam-ed-2020-cambridge-handbook-germanic/README.md`.  
Primary use: comprehensive Germanic branch reference; Ch. 6 (laryngeal phonetics/phonology), Ch. 9 (verbal inflectional morphology), and Ch. 10 (nominal inflection) provide PGmc comparanda directly relevant to Ghandwa's WIE positioning.

---

### Schrijver 2014 — `schrijver-2014/`
**Peter Schrijver, *Language Contact and the Origins of the Germanic Languages*. Routledge.**  
Roles: `diachronic` `phonology` `phylogeny` `contact` `germanic` `celtic`  
Extraction: complete. Front matter, Chapters I–VI, notes, bibliography, index. Extraction date 2026-05-07. See `schrijver-2014-language-contact-germanic/README.md`.  
Primary use: argues for a contact-origin model of Germanic via non-IE substrate populations; substrate phonology and mechanisms of Celtic-Germanic contact; relevant to Ghandwa's WIE positioning and substrate questions for the lexicon. Ch. V ("Beginnings") covers the pre-Germanic period most directly.  
Note: previously listed in Pending as "Schrijver, Italo-Celtic linguistic unity" — wrong work. That entry has been removed. No Italo-Celtic unity monograph by Schrijver is in the collection.

---

### Woodard 2006 — `woodard-2006/`
**Roger D. Woodard, *Indo-European Sacred Space: Vedic and Roman Cult*. University of Illinois Press.**  
Roles: `corpus` `lexical` `ritual` `theonymy` `myth` `italic`  
Extraction: complete. Front matter, Chs. 1–5 (Chs. 1 and 4 split by numbered sections), postscript, abbreviations, bibliography, index. See `woodard-2006-indo-european-sacred-space/README.md`.  
Primary use: Dumézilian three-function analysis of Roman and Vedic sacred space (Capitoline triad, fire altars, boundary rites); directly relevant to Ghandwa `lore.md` for divine function vocabulary, ritual terminology, and triadic mythological structure.

---

### Zair 2012 — `zair-2012/`
**Nicholas Zair, *The Reflexes of the Proto-Indo-European Laryngeals in Celtic*. Brill.**  
Roles: `diachronic` `phonology` `celtic`  
Extraction: complete. Front matter, Chs. I–VIII (Ch. III split by laryngeal environment), bibliography, index verborum. See `zair-2012-reflexes-pie-laryngeals-celtic/README.md`.  
Primary use: systematic environment-by-environment analysis of PIE laryngeal reflexes in Celtic; comprehensive secondary source for any Ghandwa derivation where laryngeal treatment is uncertain; CaRC vocalism comparanda especially in the CR̥HC cluster sections.

---

## _inbox — stubs and works needing narrative entries

| Dir | Work | Notes |
|---|---|---|
| `de-goede-2014` | de Goede 2014 — PhD thesis, derivational morphology as PIC evidence | Complete (third pass); suffix dataset (TSV + JSON) extracted. Needs narrative entry. TSV row present and marked complete. |
| `kroonen-2012` | Kroonen 2012 — substrate root-noun candidates in PGmc | Complete (second pass); lexical dataset (CSV) extracted. Needs narrative entry. TSV row present and marked complete. |
| `kroonen-2016` | Kroonen 2016 — etymology of 'apple', Wanderwort methodology | Complete (third pass); lexical comparanda (CSV) extracted. Needs narrative entry. TSV row present and marked complete. |
| `matasovic-2010` | Matasović 2010 — "The etymology of Latin *focus* and the devoicing of final stops before \*s in PIE," *Historische Sprachforschung* 123: 212–216 | Third-pass extraction present. TSV status listed as stub — correct to complete. |
| `koch-2020` | Koch 2020 | Extraction status unknown — check directory. |

---

## Pending / planned

| Work | Roles | Status |
|---|---|---|
| Kroonen 2013 (*EDPG*) | `LEX` | **Complete** — seventh-pass in `kroonen-2013/` |
| Ringe 2024 | `DIAC` | **Complete** — in `ringe-2024/` |
| LIV² — full dictionary body | `LEX` `DIAC` | Addenda/corrigenda complete (see `LIV²/`); full dictionary body not yet acquired — actively sought |
| Olander 2022 | `DIAC` `SUB` | **Complete** — fourth-pass in `olander-2022/` (was listed as "Olander 2023") |
| Derksen 2015 (*EDBIL*) | `LEX` | **Complete** — fourth-pass in `derksen-2015/` |
| De Vaan 2008 (*EDL*) | `LEX` | PDF in `vaan-2008/` — extraction in progress (multiple passes) — incoming |
| Matasović 2009 (*EDPC*) | `LEX` | Extraction in progress (multiple passes) — incoming |
| Derksen 2008 (*EDLIL*) | `LEX` | PDF in `derksen-2008/` — extraction in progress (multiple passes) — incoming |
| Beekes 2010 (*EDG*) | `LEX` | PDF in `beekes-2010/` — extraction in progress (multiple passes) — incoming |
| Schrijver, Italo-Celtic linguistic unity | `DIAC` `SUB` | Removed — wrong work; see Schrijver 2014 entry above |
| Fortson 2010, *Indo-European Language and Culture*, 2nd ed. | `DIAC` `SUB` | **Complete** — in `fortson-2010-indo-european-language-culture/` |
| Dunkel 2014, *Lexikon der indogermanischen Partikeln und Pronominalstämme* | `LEX` | Not yet acquired |

---

## Changelog

| Date | Change |
|---|---|
| 2026-05-07 | Role taxonomy overhaul. Replaced 5-tag uppercase system with 24-tag lowercase system across four axes: subfield (lexical, diachronic, phonology, morphology, prosody, phylogeny, contact, epigraphy, computational, reconstruction), branch (italic, celtic, germanic, balto-slavic, greek, anatolian, indo-iranian), culture/lore (myth, ritual, theonymy, material-culture, formulaic), output type (corpus, onomastics). Updated all narrative Roles: lines in README and all roles fields in TSV. |
| 2026-05-07 | Filesystem audit. Added narrative entries and TSV rows for 7 newly extracted works: Clackson et al. 2020, Fortson 2010, Kapović 2017, Putnam 2020, Schrijver 2014, Woodard 2006, Zair 2012. Updated Pending: Fortson 2010 marked complete; Schrijver "Italo-Celtic linguistic unity" entry replaced with note (wrong work, now corrected). Note: `_inbox/clackson-2014` is an empty directory — delete manually. |
| 2026-05-02 | Filesystem audit. Added narrative entries for 13 previously undocumented or misclassified works: Ringe 2024, Kroonen 2013, LIV², Olander 2022, West 2007, Bjørn 2017, Clackson 2007, Clackson 2013, Fagiolo et al. 2024, Graça da Silva & Tehrani 2016, Mikhailova 2021, Anthony 2013, Anthony 2023. Updated _inbox: de-goede-2014, kroonen-2012, kroonen-2016 are complete (not stubs); matasović-2008 flagged as unconfirmed; keydana-hock-widmer-eds removed (no directory). Updated Pending table. Noted five etymological dictionaries extraction in progress. LIV² full body actively sought. Added source_id ASCII-normalization note. |
| 2026-04-28 | Added `ONOM` and `CORP` role codes to taxonomy; updated 15 Prósper rows in `references-index.tsv`. |
| 2026-04-28 | Added `references-index.tsv` — 50-row lookup index with `roles`, `extraction_status`, `keywords_source`, `keywords_parsed`, and `ghandwa_notes` for all current sources. |
| 2026-04-28 | Added 10 missing entries (Eska 2018b, Eska 2023, Eska 2024, Höfler 2024, Klimp 2013, Koch 2019, Koch 2024, Kroonen et al. 2021, Kroonen et al. 2022, Wigman 2023). Corrected two wrong paths: `eska-2018/` → split into `eska-2018-laryngeal-realism/` and `eska-2018-celto-germanic-lexis/`; `van-sluis-et-al-2023/` → `sluis-2023/`. Added _inbox table. Marked in-progress extractions correctly. Moved 9 stale notes.md files to `_delete/`. |
| 2026-04-27 | Restructured into per-work subdirectories. Added .gitignore rule for PDFs. Added `hyllested-2010/notes.md` stub. Updated README paths. Initial inventory as of commit `07d7540`. |
