---
title: "Ghandwa Handoff — Derivational Suffix Lemma Entries — 2026-06-30"
last_updated: 2026-06-30
session: "Examined three candidate derivational suffixes for NocoDB lemma-entry status (-man/-méns, -el-, -dékes~-dékā). Settled the man/men paradigm fully. Surfaced the POS-tagging/table-architecture question as the actual blocker for all three. -el- and -dékes~-dékā remain unexamined beyond initial framing."
---

# Ghandwa Handoff — Derivational Suffix Lemma Entries — 2026-06-30

## Completed This Session

### 1. man/men paradigm — fully settled, written up

The *-man* suffix (PIE \**-mn̥* ~ \**-mén-*, Yates and Ringe amphikinetic neuter) is now fully resolved and documented. Key decisions:

- **Naming convention:** refer to this as the **man/men paradigm** in NocoDB and lexical records generally — neither *-man* nor *-méns*/*-menés* alone names the alternation.
- **Genitive singular split, both forms retained as register variants** (not adjudicated to a single winner):
  - *-méns* (full-grade *-mén-* + bare *-s*) — older/archaic, mapped to **Layer 1**
  - *-menés* (full-grade *-mén-* + *-és*) — later/generalized, mapped to **Layer 2**
- **Rationale for retaining both:** comparative evidence is genuinely split across every WIE witness, each resolving the inherited alternation differently rather than converging — Italic preserves it most transparently (Lat. *nōmen* ~ *nōminis*, though *nōmen*'s long vowel is likely analogical after *cognōmen*); Celtic leveled to a single stem (PCelt \**anman*, same strategy as 'nail' \**anglna*); Germanic replaced the formation outright with an *-ō-* n-stem (PGmc \**namō-*, same reanalysis-of-collective pattern as 'water'/'fire'); Greek absorbed it into an unexplained *t*-extended class (*-ματ-*, gen. ὀνόματος). No branch hands down a clean, unremodeled form — so rather than pick one, Ghandwa keeps the PIE-internal diachronic variation itself as productive register variation. This is now framed in `preface.md` as a general principle for handling this kind of comparative split, not a one-off.
- **Scope explicitly limited:** this resolution applies to the man/men paradigm only. The general question of the genitive singular ending for Ghandwa consonant stems as a class is still open and was *not* resolved or generalized from this.
- **Open thread, not pursued further this session:** Matasović glosses PCelt \**anman* as "derived from the oblique cases" (i.e. from \**h₃nmen-*), but the form's actual vocalism is better explained by the regular pan-Celtic \**m̥/n̥* > \**am/an* sound law than by a full-grade oblique reflex. Tried to explain the mismatch as an OCR artifact — correctly rejected (OCR can mangle a diacritic, not fabricate an interpretive clause). Unresolved; next step if pursued is McCone 1996 (*Towards a Relative Chronology of Ancient and Medieval Celtic Sound Change*), which is **not currently in the reference corpus**.

**Files modified (written directly to local repo via Filesystem MCP):**
- `docs/grammar/ch4-ghandwa/sec4-4-word-formation/derivational-suffixes.md` — *-man* section rewritten under "the man/men paradigm" heading; full comparative survey added; changelog entry added.
- `docs/grammar/preface.md` — new section "The man/men Paradigm Genitive Split" added before "PIE Reconstruction Framework"; `last_updated` bumped to 2026-06-30.

### 2. -el- (diminutive) — confirmed, not re-litigated this session

Underlying form is full-grade *-elo-* (Lat. *-ulus*, PGmc *-ila-*, both < *-elo-* + thematic), not zero-grade *-l̥-*. CaRC does not apply (the *e* is an inherited full-grade vowel with no syllabic resonant environment). This was settled earlier in conversation, already reflected in the existing `derivational-suffixes.md` entry — no file changes needed this session.

### 3. -dékes ~ -dékā (numeral suffixes) — NOT examined this session

Flagged at the start of the session as needing the same kind of scrutiny as *-man*, but the conversation went deep on *-man* and never returned to this. Treat as fully open — no etymological or comparative work done on it in this session.

---

## A. The Actual Blocker: POS Tagging / Table Architecture for Suffix Entries

This is the live decision blocking NocoDB row creation for **all three** suffix candidates (man/men, *-el-*, *-dékes~-dékā*), not just one. Surfaced two sub-questions, neither resolved:

### A1. What do the reference dictionaries do?

Checked all three model EDx dictionaries in `references/` (de Vaan EDL, Kroonen EDPG, Matasović EDPC): **none of them give derivational suffixes independent headword/lemma entries with their own POS tag.** Suffixes only ever appear embedded in the etymological prose of a full lexeme entry that bears them (e.g. Matasović discusses \**-smn̥-* inside the *garman* entry, not as its own lemma). De Vaan's bracket-tag convention (*[n.]*, *[f.]*, *[adj.]*) is never applied to a bare suffix. LIV² and NIL are not in the reference corpus, so their conventions (if different) are unchecked.

**Implication:** treating suffixes as independent NocoDB rows with a POS field is a Ghandwa-project-specific departure from the reference dictionary tradition, not something inherited from a precedent. Worth being explicit about that when documenting the decision, whichever way it goes.

### A2. Same table vs. separate table — not decided

Two live options, weighed but not chosen:

**Option 1 — same table, new `pos` value(s).**
- Pros: free use of existing `entry_status` pipeline (stub/draft/hold/canon), existing `_ety` field conventions, and — most valuably — lets `cross_references`/`derived_forms` on ordinary lemma rows point at suffix rows directly, instead of relying on prose mentions the way the reference dictionaries do. One export, one NFC/lookup workflow.
- Cons: `notation.md` §7 ties POS to required-minimum-field rules at canon tier (nouns need `nom_stem_class`+`noun_gender`; verbs need `verb_thematicity`+`verb_stem_type`). A suffix POS needs its own minimum-field rule — something like PIE source, allomorph set, attaches-to category, productivity — not stem-class fields, which don't apply.
- A two-value split (nominal der. suf. / verbal der. suf.) doesn't cleanly cover everything already drafted — *-dékes~-dékā* is a numeral suffix, neither. **Suggested resolution if Option 1 is chosen:** single `pos` value (e.g. "der. suf."), and let the already-unpopulated `pos_subtype` field carry the nominal/verbal/numeral distinction. This would resolve two open lexicon items at once (suffix POS tagging + the long-unpopulated `pos_subtype` field) rather than one.

**Option 2 — separate table.**
- Pros: no retrofitting the noun/verb schema; design exactly the columns a suffix entry needs (allomorph pair, PIE source, attaches-to, productivity, paradigm name like "man/men paradigm", comparanda summary) without empty noun/verb fields. Maps cleanly onto a literal dictionary-appendix export unit.
- Cons: new schema to design now; a second TSV in the bulk-analysis workflow; cross-referencing from word entries back to suffix entries becomes cross-table (need to decide: formal linked field, or just prose in `_ety` as today).

### A3. Scale consideration

This is not a 3-row decision. `derivational-suffixes.md` already has several more suffixes drafted in prose beyond the three actively discussed this session — at minimum the Caland instrument suffixes, an agentive nt-stem doublet, and a *-ēs ~ -ezos* onomastic suffix; *-sman-* (PIE \**-smn̥-*, confirmed via 6 independent Celtic etyma in Matasović — *garsman-*, *kanxsman-*, *lanxsman-*, *luxsman-*, *be-sman*, *braxsman-* — but not yet checked against de Vaan/Kroonen for Italic/Germanic support) is a plausible additional candidate, structurally distinct from plain *-man*, not yet decided whether to pursue as its own entry. Once all currently-drafted suffixes are formalized, this is closer to a ten-plus-row decision — worth weighing in favor of designing the right structure now rather than retrofitting later.

**No decision was made on A1/A2/A3 this session.** This is the recommended starting point for the next session on this thread.

---

## B. Suggested Next-Session Order

1. Decide table architecture (A2) and POS/`pos_subtype` convention (A1 resolution sketch above) before creating any rows.
2. Examine *-dékes ~ -dékā* with the same rigor as *-man* got this session (underlying PIE form, comparative check across Italic/Celtic/Germanic, any Ghandwa-specific phonological wrinkles).
3. If time remains: decide whether *-sman-* warrants its own candidate-suffix treatment, and whether to pursue the McCone 1996 acquisition for the still-open Celtic *anman* vocalism question (§1 above).
4. Once architecture is settled, draft and propose (not write — Gary reviews before NocoDB commit) rows for man/men, *-el-*, and whichever others are ready.
