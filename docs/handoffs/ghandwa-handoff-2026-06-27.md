---
title: "Ghandwa Handoff — 2026-06-27"
last_updated: 2026-06-27
session: "References intake (7 works) + comparanda.md citation/comparandum work. Remaining items below."
---

# Ghandwa Handoff — 2026-06-27

## Completed This Session (context only — no action needed)

- Moved 7 works from `references/_inbox/` into `references/`: Deuffic 2021, Fulk 2018 (renamed from `fulk-2008-`), Kroonen 2013 (EDPG), Matasović 2009 (EDPC), Stuart-Smith 2004, Swanenvleugel 2021, de Vaan 2008 (EDL).
- Extended `sources-index.py`/`sources-index.tsv`/`sources-lookup.md` to 200 rows; added `etymological-dictionary` tag and quality-tier markers (`⚠OCR`/`⚠mixed/OCR`/`⚠glyph`).
- Destaled `references/sources-handoff.md` and fixed two Ghandwa-specific commentary leaks in `references/README.md` (modularity cleanup).
- Resolved the `comparanda.md` "De Vaan 2009" citation (was a year-slip for the 2008 EDL's introduction; de Vaan's actual 2009 publication is an unrelated ἵππος/ἱππεύς article — read in full, archived note added to `davenport-2026-working-bib.md`).
- `comparanda.md`: added StSm (Stuart-Smith) and Deuf (Deuffic) as sources; added StSm citation to the aspirates→fricatives entry (Part I); added Deuf citations to the "Already in Ghandwa" table and two new candidate-pool entries (*gʷ>*b, *Dʰ>D) in Part II; corrected and sharpened the syllabic-resonant "Key divergence" note (fixed an order/quality conflation, replaced a vague Celtic hedge with Deuf §4.1/§4.2-sourced specifics).
- Confirmed `docs/grammar/ch3-development/sec3-2-sound-changes/sec3-2-3-stage2.md` (§3.2.3.1) already frames CaRC accurately as a Celtic-quality/Germanic-order hybrid — no grammar-file edit was needed. The looser "unattested in any NWIE daughter" framing lives only in this chat's project instructions, not in any repo file.

---

## A. `references/` Indexing — Remaining Work

### A1. Deuf21 / Swan21 — split into subsection-level rows

Both are currently indexed as a single row each in `sources-index.tsv` (`pages: n/a`), despite having substantial internal structure directly relevant to Ghandwa's defining features. Full chapter/section TOCs already extracted this session — no further source reading needed before drafting.

**Deuffic 2021 TOC (relevant sections):** §1 Laryngeals (1.1–1.8), §2 Stops (2.1–2.11, incl. 2.5 *gʷ>*b, 2.6 *Dʰ>D), §3 Fricative *s (3.1–3.2), §4 Resonants (4.1 *CLT>*CLiT, 4.2 *R̥>*aR, 4.3–4.5), §5 Vowels (5.1–5.8).

**Swanenvleugel 2021 sections:** obstruents (incl. mediae aspiratae), vocalic resonants, laryngeals, vowels, stress, verbal TAM categories (tense/mood/aspect) for Italic and Celtic.

**Plan:** ~15–20 min solo drafting (assign per-subsection tags from the existing tag vocabulary, no new tags needed); show the proposed row breakdown for review before writing into `sources-index.py`; regenerate `sources-index.tsv`/`sources-lookup.md`; update row count in `references/README.md` and `references/sources-handoff.md`.

### A2. `_inbox/` batch — 16 items, deferred to a separate session

Current contents of `references/_inbox/`:

1. `byrd-2015-ie-syllable`
2. `clayton-2022-labiovelar-loss`
3. `cooper-2015-reconciling-ie-syllabification`
4. `coppock-2019-quantity-superlatives-germanic`
5. `derksen-2008-slavic-inherited-lexicon` (EDSIL — closes the Balto-Slavic tag gap once processed)
6. `derksen-2015-baltic-inherited-lexicon` (EDBIL — same)
7. `fortson-2010-indo-european-language-culture`
8. `hchiel` (unidentified — check contents before processing; doesn't follow the `{author}-{year}-{title}` naming convention)
9. `klimp-2013-remnants-r-n-stem`
10. `klimp-linguistics-residues-steppe`
11. `olander-ed-2022-ie-language-family`
12. `piwowarczyk-2023-development-pie`
13. `vaan-2009-ἵππος` — see A3, called out separately
14. `woodhouse-2017-delabialization-after-u`
15. `yates-2019-phonology-phonetics-diachrony`
16. `yates-2022-new-prosodic-reconstruction`

No work done on any of these beyond #13 (read in full for an unrelated reason, see below). Standard intake process applies: verify extraction quality, assign tags from existing tag vocabulary (add new tags only if genuinely needed), determine row granularity (single-row vs. subsection-level) per source type, update all three index files + `README.md` + `sources-handoff.md`.

### A3. `vaan-2009-ἵππος` — already read, not yet indexed

This one's already been engaged with substantively this session (read in full to resolve the "De Vaan 2009" citation question in `comparanda.md`) but not yet given a row in `sources-index.tsv`. Title: "The derivational history of Greek ἵππος and ἱππεύς." Content: EPIE u-stem reconstruction of *h₁éku- 'horse', thematization, hysterodynamic genitive/hypostasis mechanics, the *-eu-/-éw- agent-noun suffix. Born-digital, clean (per manifest: 4 unresolved markers).

Also flagged as directly relevant to the in-progress `davenport-2026` paper on *h₂ékʷeh₂/*h₂engʷʰis (see note already added to `davenport-2026-working-bib.md`) — *h₁éku- 'horse' is the same EPIE u-stem-to-thematic-derivation mechanism Proposal A needs for *h₂éḱ-u-eh₂, though the roots are not cognate (different laryngeal, different meaning — purely a structural/methodological parallel).

### A4. Pre-existing backlog (not raised this session, still open per `sources-handoff.md`)

- R1996 (Ringe 1996, Tocharian) OCR quality pass — targeted visual QA on Ch2 (laryngeals) and Ch5 (syllabic resonants) against the source PDF.
- Content-read tag refinement for R2024 — same method just applied to R2017 this session (see new section D below); R2017 is done, R2024 is next.

---

## B. `docs/file-map.md` — not updated this session (gap found, not yet acted on)

Per project convention, `file-map.md` tracks file renames/moves/supersedences. Two events from this session were never logged there:

1. **Fulk rename**: `fulk-2008-comparative-grammar-early-germanic/` (+ 19 files within it) → `fulk-2018-comparative-grammar-early-germanic/`, correcting a filename-date error (uploaded PDF filename said 2008; actual publication is 2018).
2. **7-work batch move**: `references/_inbox/{deuffic-2021,fulk-2018,kroonen-2013,matasovic-2009,stuart-smith-2004,swanenvleugel-2021,vaan-2008}` → `references/{same}`.

Neither is strictly a "supersedence" in the sense `file-map.md` usually tracks (no old content is superseded — these are new acquisitions plus one rename), so it's a judgment call whether either belongs there at all, or whether `file-map.md`'s scope should stay limited to genuine supersedences. Flagging for a decision rather than logging unilaterally.

---

## C. Checked, no action needed

- `docs/ref-works-outstanding.md` — checked against today's 7 acquisitions; it's a lore/mythology acquisition list (Benveniste, Dumézil, Lincoln, Polomé, Puhvel) entirely unrelated to this session's phonology/etymology works. No overlap, no update needed.

---

## D. R2017 content-read tag refinement + Matasović Letter-I fix (this session, continued)

**Matasović Letter-I page range — resolved.** Corrected `49-178` to `176-178`. The extraction's own embedded `<!-- pdf-page: N -->` anchors settle it: the I-chunk shows sequential anchors 176→177→178→179 (the 179-anchor entry being K's actual first entry, which leaked into the I-chunk file); G's chunk independently ends at page 175 with no further entries; K's frontmatter independently declares `179-236`. Fixed in `sources-index.py`, `sources-index.tsv`, the letter-I file's own frontmatter, and the directory `README.md`.

**R2017 content-read tag refinement — done, all 41 sections.** Read the full text of every section (not just titles) and refined tags to surface subtopics and named phenomena the structural tags missed. Added 11 tags to the controlled vocabulary, using a `law-` prefix for named sound laws (e.g. `law-Grimm`, not `Grimm`) to distinguish discussion of *the law itself* from incidental citations of the scholar's other work — existing `Grimm`/`Verner`/`Sievers` tags were renamed to match, including their occurrences in Fulk18. New tags: `law-Grimm`, `law-Verner`, `law-Sievers`, `law-Lindeman`, `law-Szemerenyi`, `law-Stang`, `law-Bartholomae`, `law-Pinault`, `law-Cowgill`, `law-Osthoff`, `law-Kluge`, `Auslautgesetze`, `Caland`, `n-stem`. Full per-section deltas and the naming rationale are now in `references/sources-handoff.md`.

**Outstanding from this sub-task:** none — `sources-lookup.md` has been regenerated locally (`python3 sources-index.py`, ran clean) and is now in sync with `sources-index.py`/`.tsv`.

**Next step:** R2024 content-read tag refinement, same method, fresh session.
