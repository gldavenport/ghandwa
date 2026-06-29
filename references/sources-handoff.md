---
title: "Sources Index — Handoff"
last_updated: "2026-06-27"
---

# Sources Index Handoff

## What was built

Two files, now in `sources/`:

- `sources-index.tsv` — 200 rows, canonical record; columns: `work | dir | file | section | pages | title | tags | quality`
- `sources-lookup.md` — speed lookup organized by tag group; grep with `grep -A 20 '## tag-name' sources-lookup.md`

Tagging methodology differs by source. R2017 has now had a full content-read pass (see below); R2024 still reflects README section titles only — not content reading. The three etymological dictionaries (Kroon13, Matas09, Vaan08) are tagged generically at letter-range granularity — one row per letter, same four tags repeated (branch + `lexicon` + `etymological-dictionary` + `comparative-reconstruction`) — since dictionary letter-ranges have no finer structure without a content read. The two MA theses (Deuf21, Swan21) were tagged from a full table-of-contents/header scan rather than README titles, giving more topic-specific tags per row than the structural works, but each is still a single row for the whole document.

**R2017 content-read pass (2026-06-27):** all 41 sections read in full; tags refined to surface named sound laws and subtopics that section-title tagging missed (e.g. §2.2 now carries six named PIE-internal laws plus thorn-clusters and Auslautgesetze, not just the broad PIE-phonology/laryngeals/ablaut tags it had before). Added 11 tags to the vocabulary in the process (see below). R2024 is the natural next target, using the same method.

## Tag vocabulary (71 tags)

**PIE Phonology & Reconstruction:** `phonology`, `PIE-phonology`, `PIE-reconstruction`, `laryngeals`, `syllabic-resonants`, `labiovelars`, `stops`, `sonorants`, `fricatives`, `accent`, `ablaut`, `thorn-clusters`

**PIE Morphology:** `PIE-inflection`, `PIE-syntax`, `PIE-lexicon`, `noun-inflection`, `verb-inflection`, `adjective-inflection`, `thematic-stems`, `athematic-stems`, `present-stems`, `perfect`, `aorist`, `nasal-infix`, `mood`, `aspect`, `personal-endings`, `o-stem`, `s-stem`, `n-stem`, `root-nouns`, `athematic-nouns`, `pronouns`, `numerals`, `paradigms`, `derivational-morphology`, `word-formation`, `compounding`, `Caland`

**Sound Changes & Chronology:** `sound-changes`, `sound-change-chronology`, `Auslautgesetze`, `law-Grimm`, `law-Verner`, `law-Sievers`, `law-Lindeman`, `law-Szemerenyi`, `law-Stang`, `law-Bartholomae`, `law-Pinault`, `law-Cowgill`, `law-Osthoff`, `law-Kluge`

**Languages & Branches:** `Proto-Germanic`, `Proto-Greek`, `Tocharian`, `Germanic`, `Greek`, `Italic`, `Celtic`, `Balto-Slavic`

**Comparative & Theoretical:** `comparative-reconstruction`, `etymological-dictionary`, `subgrouping`, `phylogeny`, `cladistics`, `dialect-geography`, `borrowing`, `historical-linguistics-theory`, `syntax`, `lexicon`

**Naming convention for named sound laws:** `law-` prefix + capitalized name (e.g. `law-Grimm`, not `Grimm`), to distinguish discussion of *the law itself* from incidental citations of the scholar's other work. `law-Cowgill` in particular should be reserved for rows discussing Cowgill's Law specifically — Cowgill is cited constantly elsewhere in R2017 for unrelated points. `Auslautgesetze` (word-final sound-law category) and `Caland` (the Caland derivational system) are left unprefixed since they're categories/systems, not single named laws. `n-stem` is lowercase to match the existing `o-stem`/`s-stem` convention.

## Action items

### High priority
- **Content-read R2024 for tag refinement** — same method just applied to R2017 (read all sections, surface named phenomena and subtopics). Particularly useful for thorn clusters, Proto-Greek *h, and dialect geography sections, and for catching any named Greek-specific sound laws the structural tags miss.

### Medium priority
- **Balto-Slavic branch tag still unassigned** — `Italic`, `Celtic`, `Germanic` are now in active use (Deuf21, Fulk18, Matas09, StSm04, Swan21, Vaan08). `Balto-Slavic` remains the only branch tag with zero entries. Two Derksen works (EDSIL 2008, EDBIL 2015) are in `_inbox/` awaiting processing — once indexed, this gap closes.
- **R1996 OCR quality pass** — The Tocharian volume is scanned OCR with known fidelity issues. Before relying on it for character-level data, do a targeted visual QA pass on the sections most relevant to active work (Ch2 laryngeals, Ch5 syllabic resonants). The same caution now applies more broadly: Kroon13, Matas09, Vaan08 (mixed/scanned) and Fulk18 (born-digital, glyph-corrupted) carry their own quality flags in `sources-index.tsv`.

### Resolved this session
- **Matasović Letter-I page range** — was `49-178` (internally inconsistent: D ends 117, K begins 179). Corrected to `176-178`, confirmed via the embedded `<!-- pdf-page: N -->` anchors already present in the extraction itself (176/177/178/179 sequential within the I-chunk; G's chunk independently ends at 175; K's frontmatter independently declares `179-236`). Fixed in `sources-index.py`/`.tsv`, the letter-I file's own frontmatter, and the directory README.

### Low priority
- **Cross-index the per-work back-matter indices** — The existing `*-index.md` files are page-reference indices (form → page). A future pass could invert these into a cross-source PIE-form lookup (form → {R2017 page, R2024 page, ...}) for rapid comparative citation. Probably a ChatGPT bulk job.
- **Subsection-level rows for Deuf21 and Swan21** — Both are currently indexed as a single row each despite having substantial internal structure directly relevant to Ghandwa (e.g. Deuffic's dedicated subsections on *gʷ>*b and *R̥>*aR). Splitting into subsection-level rows, matching the granularity given to the R-works, would make these two more usable.

## Known gaps
- R2024 (and all sources except R2017) still reflect section/letter/chapter titles, not content; topics discussed as subtopics within a section are not yet indexed
- R1996, Kroon13, Matas09, Vaan08 character fidelity unreliable to varying degrees (see `quality` column); use for structural/argumentative reference only until verified against the source PDF
- No cross-source form index yet (see low priority above)
