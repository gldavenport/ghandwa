---
title: "Sources Index — Handoff"
last_updated: "2026-05-31"
---

# Sources Index Handoff

## What was built

Two files, now in `sources/`:

- `sources-index.tsv` — 105 rows, canonical record; columns: `work | dir | file | section | pages | title | tags | quality`
- `sources-lookup.md` — speed lookup organized by tag group; grep with `grep -A 20 '## tag-name' sources-lookup.md`

Tags derived from README section titles only — not from content reading. Coverage is structural, not granular.

## Tag vocabulary (58 tags)

**PIE Phonology & Reconstruction:** `phonology`, `PIE-phonology`, `PIE-reconstruction`, `laryngeals`, `syllabic-resonants`, `labiovelars`, `stops`, `sonorants`, `fricatives`, `accent`, `ablaut`, `thorn-clusters`

**PIE Morphology:** `PIE-inflection`, `PIE-syntax`, `PIE-lexicon`, `noun-inflection`, `verb-inflection`, `adjective-inflection`, `thematic-stems`, `athematic-stems`, `present-stems`, `perfect`, `aorist`, `nasal-infix`, `mood`, `aspect`, `personal-endings`, `o-stem`, `s-stem`, `root-nouns`, `athematic-nouns`, `pronouns`, `numerals`, `paradigms`, `derivational-morphology`, `word-formation`, `compounding`

**Sound Changes & Chronology:** `sound-changes`, `sound-change-chronology`, `Grimm`, `Verner`, `Sievers`

**Languages & Branches:** `Proto-Germanic`, `Proto-Greek`, `Tocharian`, `Germanic`, `Greek`, `Italic`, `Celtic`, `Balto-Slavic`

**Comparative & Theoretical:** `comparative-reconstruction`, `subgrouping`, `phylogeny`, `cladistics`, `dialect-geography`, `borrowing`, `historical-linguistics-theory`, `syntax`, `lexicon`

## Action items

### High priority
- **Content-read R2017 for tag refinement** — R2017 is the primary reference and has the finest section granularity. Many sections currently carry only structural tags. Read each section file and add subtopic tags (e.g., which specific sound changes are in §3.2.3, which stem classes are in §4.3.3). Do one work per session; start here.
- **Content-read R2024 for tag refinement** — Same pass for the Greek volume; particularly useful for thorn clusters, Proto-Greek *h, and dialect geography sections.

### Medium priority
- **Add missing branch tags** — `Italic`, `Celtic`, `Balto-Slavic`, `Germanic` are in the vocabulary but currently unassigned (no section in these four works focuses on those branches exclusively). Tag sections where those branches appear as secondary comparanda during content-read passes.
- **R1996 OCR quality pass** — The Tocharian volume is scanned OCR with known fidelity issues. Before relying on it for character-level data, do a targeted visual QA pass on the sections most relevant to active work (Ch2 laryngeals, Ch5 syllabic resonants).
- **Fifth source onboarding** — When a new source is added to `sources/`, extend `sources-index.tsv` and rebuild `sources-lookup.md` using the same Python script (`sources-index.py`, currently in Claude's working environment only — consider committing it to `tools/` or `sources/`).

### Low priority
- **Cross-index the per-work back-matter indices** — The existing `*-index.md` files are page-reference indices (form → page). A future pass could invert these into a cross-source PIE-form lookup (form → {R2017 page, R2024 page}) for rapid comparative citation. Probably a ChatGPT bulk job.
- **Commit the build script** — `sources-index.py` is the source of truth for regenerating both files. Commit to `sources/` or `tools/`.

## Known gaps
- Tags reflect section titles, not content; topics discussed as subtopics within a section are not yet indexed
- R1996 character fidelity unreliable for technical data; use for structural/argumentative reference only
- No cross-source form index yet (see low priority above)
