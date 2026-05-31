# sources/

Extracted Markdown editions of reference works used in the Ghandwa project. Each work lives in its own subdirectory alongside its index and metadata files. A cross-source tag index covers all four works.

---

## Works

| Dir | Work | Type | Primary use |
|---|---|---|---|
| `ringe-1996-chronology-sound-changes-tocharian/` | Ringe 1996 — *On the Chronology of Sound Changes in Tocharian* | Scanned OCR ⚠ | Sound change chronology methodology; Tocharian comparanda |
| `ringe-2013-historical-linguistics/` | Ringe & Eska 2013 — *Historical Linguistics: Toward a Twenty-First Century Reintegration* | Born-digital | Theory, reconstruction methodology, subgrouping, cladistics |
| `ringe-2017-pie-to-proto-germanic-2nd/` | Ringe 2017 — *From Proto-Indo-European to Proto-Germanic*, 2nd ed. | Born-digital | **Primary reference.** PIE phonology, morphology, sound changes to PGmc |
| `ringe-2024-linguistic-roots-ancient-greek/` | Ringe 2024 — *The Linguistic Roots of Ancient Greek* | Born-digital | PIE phonology cross-check; thorn clusters; Proto-Greek comparanda |

⚠ R1996 is scanned OCR with known fidelity issues. Use for structural and argumentative reference; verify character-level data against the original PDF.

---

## Index files

| File | Purpose | Use |
|---|---|---|
| `sources-index.tsv` | Canonical record — 105 rows × 8 cols (`work\|dir\|file\|section\|pages\|title\|tags\|quality`) | grep/awk/script-based lookup; authoritative tag record |
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

58 tags in five groups — see `sources-lookup.md` group headers for the full list. Tags currently reflect section titles, not full content; refine with content-read passes (R2017 first).

---

## Per-work file structure

Each work directory contains:

- `{work}-ch{N}.md` or `{work}-ch{N}-sec{N}-{N}.md` — chapter/section content
- `{work}-index.md` — back-matter index (form → page reference)
- `{work}-bibliography.md` — references
- `{work}-front-matter.md` / `{work}-frontmatter.md` — front matter
- `{work}-extraction-report.md` — extraction QA notes
- `manifest.json` — source metadata, correction counts, character statistics
- `README.md` — file table with page ranges

---

## _inbox/

Staging directory for new sources before extraction and indexing.

---

## Adding a new source

1. Extract to a new subdirectory following the naming convention `{author}-{year}-{short-title}/`
2. Add entries to `sources-index.py` following the existing pattern
3. Run `python3 sources-index.py` from this directory — regenerates `sources-index.tsv` and `sources-lookup.md`
4. Commit all four files
