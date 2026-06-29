# sources/

Extracted Markdown editions of reference works used in the Ghandwa project. Each work lives in its own subdirectory alongside its index and metadata files. A cross-source tag index covers all eleven works.

---

## Works

| Dir | Work | Type | Primary use |
|---|---|---|---|
| `ringe-1996-chronology-sound-changes-tocharian/` | Ringe 1996 — *On the Chronology of Sound Changes in Tocharian* | Scanned OCR ⚠ | Sound change chronology methodology; Tocharian comparanda |
| `ringe-2013-historical-linguistics/` | Ringe & Eska 2013 — *Historical Linguistics: Toward a Twenty-First Century Reintegration* | Born-digital | Theory, reconstruction methodology, subgrouping, cladistics |
| `ringe-2017-pie-to-proto-germanic-2nd/` | Ringe 2017 — *From Proto-Indo-European to Proto-Germanic*, 2nd ed. | Born-digital | **Primary reference.** PIE phonology, morphology, sound changes to PGmc |
| `ringe-2024-linguistic-roots-ancient-greek/` | Ringe 2024 — *The Linguistic Roots of Ancient Greek* | Born-digital | PIE phonology cross-check; thorn clusters; Proto-Greek comparanda |
| `deuffic-2021-relative-chronology-sound-change/` | Deuffic 2021 — *The Relative Chronology of Sound Changes from PIE to Proto-Celtic* (Leiden MA thesis) | Born-digital | Direct PIE→Celtic comparandum: syllabic-resonant vocalism, *gʷ>*b, aspirate-stop loss |
| `fulk-2018-comparative-grammar-early-germanic/` | Fulk 2018 — *A Comparative Grammar of the Early Germanic Languages* | Born-digital, glyph-corrupted ⚠ | Full Germanic comparative grammar — phonology through verb inflection |
| `kroonen-2013-proto-germanic/` | Kroonen 2013 — *Etymological Dictionary of Proto-Germanic* (EDPG) | Mixed/scanned ⚠ | **Core reference.** Germanic etymological dictionary model |
| `matasovic-2009-proto-celtic/` | Matasović 2009 — *Etymological Dictionary of Proto-Celtic* (EDPC) | Mixed/scanned ⚠ | **Core reference.** Celtic etymological dictionary model |
| `stuart-smith-2004-phonetics-phonology/` | Stuart-Smith 2004 — *Phonetics and Philology: Sound Change in Italic* | Scanned OCR ⚠ | Phonetic/philological treatment of the PIE voiced-aspirate-to-fricative shift in Italic |
| `swanenvleugel-2021-reconstructing-proto-italo-celtic/` | Swanenvleugel 2021 — *Reconstructing Proto-Italo-Celtic* (Leiden MA thesis) | Born-digital | Italo-Celtic phonemic system (mediae aspiratae, vocalic resonants, laryngeals) and TAM categories |
| `vaan-2008-latin-italic-dialects/` | de Vaan 2008 — *Etymological Dictionary of Latin and the Other Italic Languages* (EDL) | Mixed/scanned ⚠ | **Core reference.** Italic etymological dictionary model |

⚠ R1996, StSm04 are scanned OCR; Kroon13, Matas09, Vaan08 are mixed/scanned with unresolved character-fidelity risk; Fulk18 is born-digital but has unresolved inline-glyph corruption. All five quality tiers are usable for structural and argumentative reference — verify character-level data (diacritics, laryngeal subscripts, exact forms) against the original PDF before quoting or deriving forms.

Fulk18's directory/filenames were renamed from the uploaded PDF's filename date (2008) to the actual publication date (2018) at index time; `manifest.json` retains the original uploaded filename as `source_file` for provenance.

Matas09's Letter-I entry has a page range (`49-178`) that is internally inconsistent with the surrounding alphabetical sequence — flagged in `sources-index.tsv`, not corrected, pending verification against the source PDF.

---

## Index files

| File | Purpose | Use |
|---|---|---|
| `sources-index.tsv` | Canonical record — 200 rows × 8 cols (`work\|dir\|file\|section\|pages\|title\|tags\|quality`) | grep/awk/script-based lookup; authoritative tag record |
| `sources-lookup.md` | Speed lookup — sections grouped by tag | Fast in-session navigation; see usage below |
| `sources-index.py` | Build script — regenerates both files above | Run after adding a new source or updating tags |

### Searching sources-lookup.md

Extract a full tag block with awk (handles tags with many entries):

```bash
awk '/^## labiovelars$/{p=1} p && /^## / && !/^## labiovelars$/{p=0} p' sources-lookup.md
```

Cross-field TSV search (e.g., PGmc verb inflection sections only):

```bash
grep "Proto-Germanic" sources-index.tsv | grep "verb-inflection" | awk -F'\t' '{print $1, $4, $6}'
```

### Tag vocabulary

60 tags in five groups — see `sources-lookup.md` group headers for the full list. Tags currently reflect section/chapter/letter titles, not full content; refine with content-read passes (R2017 first). The three etymological dictionaries (Kroon13, Matas09, Vaan08) are tagged at letter-range granularity — one row per letter, generic branch + `lexicon` + `etymological-dictionary` + `comparative-reconstruction` tags — since dictionary letter-ranges carry no finer topical structure without a content read.

`Germanic`, `Italic`, `Celtic`, and `Balto-Slavic` branch tags are now in active use (previously defined but unassigned in the vocabulary). `Proto-Germanic` is reserved for PGmc-stage reconstruction content; `Germanic` for comparative/attested-stage content spanning the daughter languages — same distinction applies to `Proto-Greek`/`Greek`.

---

## Per-work file structure

Each work directory contains:

- `{work}-ch{N}.md` or `{work}-ch{N}-sec{N}-{N}.md` — chapter/section content (or `{work}-letter-{x}.md` for the three dictionaries)
- `{work}-index.md` / `{work}-index-of-words.md` / `{work}-general-index.md` — back-matter index (form → page reference)
- `{work}-bibliography.md` / `{work}-references.md` — references (not indexed in `sources-index.tsv`)
- `{work}-front-matter.md` / `{work}-frontmatter.md` — front matter
- `{work}-extraction-report.md` — extraction QA notes
- `manifest.json` — source metadata, correction counts, character statistics
- `README.md` — file table with page ranges

Bibliography/references files, `manifest.json`, `README.md`, and purely mechanical artifacts (e.g. Fulk18's inline-image-glyph-audit, back-cover) are not given rows in `sources-index.tsv`.

---

## Images

Figure files are not stored in the repo. Figures referenced in content files should be consulted in the original PDF.

---

## _inbox/

Staging directory for new sources before extraction and indexing.

---

## Adding a new source

1. Extract to a new subdirectory following the naming convention `{author}-{year}-{short-title}/`
2. Add entries to `sources-index.py` following the existing pattern
3. Run `python3 sources-index.py` from this directory — regenerates `sources-index.tsv` and `sources-lookup.md`
4. Commit all four files
