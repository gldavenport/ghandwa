---
source_title: "A shared substrate between Greek and Italic"
author_creator: "Romain Garnier; Benoît Sagot"
date_year: 2017
source_file_name: "garnier-2017.pdf"
report_date: "2026-05-06"
report_type: "stress-test report"
pass_status: "completed; minor repairs applied"
---

# Garnier & Sagot 2017 — stress-test report

## Scope

Stress-testing focused on whether the latest Markdown extraction is robust as a searchable, corpus-ready linguistic text. Tests targeted character authority, technical notation, page-break artifacts, footnote integrity, Greek/PIE form searchability, abbreviation/bibliography integrity, and residual OCR/PDF extraction artifacts.

## Tests run

### 1. Artifact scan

Checked for:

- private-use glyphs, especially the former `U+E727` artifact;
- replacement characters `�` and `U+FFFF`;
- object/box glyphs;
- control characters other than normal line breaks/tabs;
- residual `[unclear]` / `[illegible]` markers;
- acute-accent artifact `U+00B4` used as a spacing accent rather than a combining mark.

Result after repair:

- private-use glyphs: 0
- replacement characters: 0
- `U+FFFF`: 0
- `U+00B4`: 0
- `[unclear]`: 0
- `[illegible]`: 0

### 2. Footnote and Markdown integrity

Checked that all Markdown footnote references have definitions and that no definitions are orphaned.

Result:

- unique footnote references: 64
- footnote definitions: 64
- missing definitions: 0
- orphan definitions: 0
- code-fence imbalance: 0 code fences present, so no imbalance

### 3. Page-break and line-break stress test

Checked for residual page-break joins that interrupt words or technical operators.

Repairs applied:

- `bor-` + page break + `rowed` → `borrowed`
- `Fi-` + page break + `nally` → `Finally`
- `sub-` + page break + `sequent` → `subsequent`
- `<` + page break + `PIE` repaired so the searchable string `< PIE` is not split
- `χurđíz` + paragraph break + `> OHG hurd` repaired into a continuous etymological expression

Result after repair:

- hyphenated word before page anchor: 0
- `<` operator before page anchor: 0
- same-line page-anchor/text collisions: 0

Residual note: page anchors still interrupt some sentences at original PDF page boundaries. That is intentional enough for page-level checking, but a later AI-parsing pass could move all page anchors to paragraph boundaries if maximum phrase-search continuity is preferred over approximate page-position fidelity.

### 4. Technical-token and character spot tests

Searched for core forms and high-risk strings.

Confirmed searchable after repair:

- `*Cu̯r̥C > *CurC`
- `*#Dʰ > Substr. *#T`
- `*Trī́ps`
- `*hₓi̯`
- `Skt bhr̥ṣṭi-`
- `DLG²`
- `Κρότων`
- `βροῦκος`
- `Tĭbĕris`
- `μέλαθρον`
- `πέλεθρον`
- `borrowed in Greek as pʰ`
- `Finally, a zero-grade abstract noun`
- `probably subsequent) anticipation`

### 5. Search-behavior probes

Probe counts in the final Markdown:

| Query | Count |
|---|---:|
| `Pre-Greek` | 15 |
| `Pelasgian` | 23 |
| `Crotonian` | 1 |
| `*Cu̯r̥C > *CurC` | 5 |
| `*#Dʰ > Substr. *#T` | 2 |
| `*Trī́ps` | 1 |
| `*hₓi̯` | 4 |
| `Skt bhr̥ṣṭi-` | 1 |
| `DLG²` | 3 |
| `Κρότων` | 2 |
| `βροῦκος` | 4 |
| `Tĭbĕris` | 2 |
| `μέλαθρον` | 5 |
| `πέλεθρον` | 3 |

## Repairs made from stress-test findings

- Replaced the spacing acute artifact in `*Trī´ps` with a combining acute over the macron-bearing vowel: `*Trī́ps`.
- Repaired Nikolaev laryngeal notation from `*hxi̯...` to `*hₓi̯...` in footnote 13.
- Restored the Sanskrit stem hyphen in `Skt bhr̥ṣṭi-`.
- Repaired residual page-break word splits and etymological-operator splits.
- Recast Section 5.7’s three examples as a numbered Markdown list, matching the source’s logical structure and improving search/parse behavior without changing the text.

## Assessment

The extraction is now strong for character authority in the areas this stress test targeted: PIE forms, Greek forms, laryngeals, `u̯`, superscripts/subscripts, abbreviation characters, and footnote linkage. The most important residual weakness is not character-level accuracy but corpus ergonomics: page anchors still occur mid-sentence where the PDF page break falls inside a paragraph. This preserves approximate page-position information but can interrupt exact phrase searches across page boundaries.

A further pass would be useful only if the goal is to optimize AI-agent parsing and phrase-search continuity by relocating page anchors to paragraph boundaries and lightly restructuring long dense paragraphs, especially Section 4. For character authority alone, this stress test found only minor residual defects, and those were repaired.
