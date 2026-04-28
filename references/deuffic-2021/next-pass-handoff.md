---
title: "Next-pass handoff: Deuffic chronology PIE to Proto-Celtic"
source_work: "Maël Deuffic, The relative chronology of sound changes from Proto-Indo-European to Proto-Celtic"
package: "deuffic-chronology-pie-proto-celtic"
current_status: "complete-working"
next_pass_goal: "clean analytical extraction, not diplomatic transcription"
created_utc: "2026-04-28T00:33:00Z"
---

# Next-pass handoff: Deuffic chronology PIE to Proto-Celtic

## Current state

This package is complete as a working extraction. It is suitable for search, comparative use, Ghandwa sound-law planning, and future corpus integration.

The package currently contains:

- `deuffic-chronology-pie-proto-celtic.md`
- `deuffic-sound-changes.tsv`
- `deuffic-relative-chronology.tsv`
- `deuffic-relative-chronology-edges.tsv`
- `notes.md`

The intended standard is **clean extraction**, not diplomatic transcription. Do not spend a future pass reproducing every visual feature of the PDF. Preserve structure, linguistic notation, examples, and arguments; ignore layout unless it affects meaning.

## Recommended future pass

Run this only if the Deuffic package is going to be used as a high-quality reference for Ghandwa rule design or as a model for later corpus-wide sound-change tables.

### 1. Clean Markdown structure

Promote all numbered subsections to proper Markdown headings where this improves navigation.

Examples:

```markdown
### 1.1.1. *h1/2/3 > *e / a / o
### 1.3.1.1. *eh1 > *ē(H)
```

Do not force over-nesting if the result becomes visually noisy. The goal is readable navigation, not perfect formal hierarchy.

### 2. Convert footnotes enough to be usable

Convert page-bottom notes into Markdown footnotes only where they interrupt the main text or obscure examples. It is not necessary to create a fully diplomatic footnote apparatus.

Preferred style:

```markdown
Text with citation marker.[^12]

[^12]: Zair (2012), p. 109.
```

If a footnote belongs to a dense example list and the mapping is unclear, leave it inline and add a local `<!-- review-footnote -->` comment.

### 3. Add an examples table if needed

The current `deuffic-sound-changes.tsv` is a rule inventory. A later pass could add a separate evidence table:

`deuffic-examples.tsv`

Suggested fields:

```text
change_id	section	pie_or_preform	intermediate_forms	proto_celtic_or_branch_form	attested_reflexes	gloss	comparanda	notes	page_anchor
```

This table would be more useful for Ghandwa construction than adding more prose cleanup. It would allow queries such as “all examples involving laryngeals before resonants” or “all examples where Deuffic uses Italic comparanda.”

### 4. Review only high-risk notation

Do not perform a line-by-line diplomatic notation audit. Instead, spot-check forms likely to matter for reusable sound-law data:

- laryngeal indices: `h1`, `h2`, `h3`; ideally normalize to `h₁`, `h₂`, `h₃` if the surrounding file already uses subscript style consistently
- syllabic resonants: `R̥`, `L̥`, `N̥`, `m̥`, `n̥`, `r̥`, `l̥`
- glides: `i̯`, `u̯`
- long/short marks: `V̄`, `V̆`, `ā`, `ē`, `ī`, `ō`, `ū`
- labiovelars and aspirates: `kw`, `gw`, `gwh`, `bh`, `dh`, `gh`
- special Deuffic notation: `*u̥n`

Important: `*u̥n` should remain as source-specific Deuffic notation unless a later analytical table explicitly maps it to another representation. It should not be generalized as a standard PIE phoneme. In context, Deuffic’s `*pn > *u̥n` and `*u̥n > *bn` appear to represent a Celtic-stage treatment comparable to `*wN` / `*wn`, not ordinary PIE `*u̥`.

### 5. Keep source notation separate from normalized analytical notation

For future Ghandwa use, consider adding parallel fields where necessary:

```text
source_change	normalized_change	analysis_note
```

Example:

```text
*pn > *u̥n	*pn > *wn?	Deuffic notation; value uncertain; compare Matasović *pN > *wN
```

Do not silently replace Deuffic’s notation in the main Markdown. If normalizing for analysis, do it in tables with notes.

### 6. Improve relative chronology tables

The current relative chronology tables are usable. A future quality pass could make them cleaner by adding:

- `source_directness`: `explicit`, `inferred`, `editorial`
- `relation_type`: `precedes`, `follows`, `same_stage`, `terminus_ante_quem`, `terminus_post_quem`
- `confidence`: `high`, `medium`, `low`
- `reason_type`: `transitivity`, `blocking`, `category-exclusion`, `periodization`, `synchronic-system`, `unclear`

This matters because Deuffic’s chronology is a partial order, not a single sequence. The edge table should remain explicitly analytical.

### 7. Add short rule summaries for Ghandwa reuse

For each sound change, optionally add a short plain analytical note in the TSV or a new file:

`deuffic-ghandwa-use-notes.tsv`

Suggested fields:

```text
change_id	change	ghandwa_relevance	potential_use	cautions
```

Example uses:

- “good model for early laryngeal coloring before loss”
- “useful relative-ordering example; not necessarily a Ghandwa rule”
- “avoid copying as-is; Celtic-specific outcome”

### 8. Bibliography cleanup only if packaging for public sharing

The bibliography is searchable and good enough for internal corpus work. Clean it only if the package will be shared as a polished artifact.

Minimum cleanup:

- one item per paragraph or bullet
- preserve author/date/title/publisher/page data
- do not reformat into CSL unless needed

## Things not worth doing

Do not spend time on:

- reproducing page layout
- preserving line breaks from the PDF
- matching indentation or table-of-contents dot leaders
- making the Markdown visually identical to the source
- exhaustive diplomatic checking of every page
- manually correcting every citation format unless it affects meaning

## Completion criteria for a future high-quality clean pass

Consider the package upgraded from `complete-working` to `complete-clean` when:

1. all major headings and subsection headings are navigable;
2. obvious OCR/extraction artifacts are removed;
3. high-risk linguistic notation has been spot-checked;
4. the sound-change table distinguishes source notation from analytical normalization where needed;
5. the relative chronology edge table is clearly marked as analytical;
6. any unresolved notation issues are listed in `notes.md` or `unresolved-readings.md`.

Suggested future YAML update:

```yaml
extraction_status: "complete-clean"
review_status: "targeted-clean-pass-complete"
canonical_form_level: false
corpus_ready: true
```
