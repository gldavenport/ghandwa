# Notes — Deuffic chronology PIE to Proto-Celtic

## Extraction status

Targeted-cleanup-pass extraction from the born-digital PDF. Text extraction was generally good, but the source contains dense notation, superscripts, combining diacritics, and footnotes; this package should be treated as usable for corpus search and first-pass analysis, not as a final diplomatic edition.

## Files

- `deuffic-chronology-pie-proto-celtic.md` — full Markdown extraction with YAML front matter and page anchors.
- `deuffic-sound-changes.tsv` — structured list of the sound changes discussed in the thesis.
- `deuffic-relative-chronology.tsv` — tabular transcription of the final staged chronology in section II.
- `deuffic-relative-chronology-edges.tsv` — extracted before/after dependency edges useful for graphing or rule-order comparison.
- `notes.md` — this file.

## Page-anchor policy

Page anchors use PDF page order:

```markdown
<!-- page: 45 -->
```

The thesis also has printed page numbers. Those were not used as anchors because the repository cover page shifts the numbering.

## Known extraction issues to review later

- Superscript aspirates in forms such as `bh`, `dh`, `gh`, and `gwh` may appear as plain inline `h` or as separated line fragments in a few places.
- Combining diacritics such as syllabic marks, macrons, breves, and acute accents should be checked before using a form as canonical data.
- Some footnotes are retained inline near the bottom of source pages rather than normalized into Markdown footnotes.
- The mathematical section was preserved as text, but formula layout should be checked if it becomes analytically important.
- Section 5.4 has notation differences between the section heading and the final relative chronology table; the TSV notes flag this case.
- The final chronology distinguishes `a.q.` and `p.q.` rows. These are preserved as `qualifier` values rather than interpreted aggressively.

## Ghandwa relevance

Most useful tables for Ghandwa work:

1. `deuffic-sound-changes.tsv` — model for daughter-language sound-law inventory.
2. `deuffic-relative-chronology-edges.tsv` — model for dependency-based ordering rather than a single linear chronology.
3. `deuffic-relative-chronology.tsv` — staged period model: Late Indo-European / Italo-Celtic / Proto-Celtic.

The main transferable design lesson is that a Ghandwa daughter-language sound history should probably be represented as a partial order of dependencies, not merely a numbered list.


## Targeted cleanup pass

Applied on 2026-04-28T00:25:00Z.

Changes made:

- Corrected seven obvious `Olr.` OCR artifacts to `OIr.`.
- Normalized missing reconstructed-output asterisks in the final chronology where the source heading or surrounding notation supports it, e.g. `*#HC > *#C`, `*CLT > *CLiT`, `*ē > *ī`, and `*pn > *u̥n`.
- Standardized Deuffic's `*u̥n` notation where OCR had `*un`, bare `u̥n`, or related inconsistent forms.
- Normalized selected `*eie > ...` sound-change labels to `*ei̯e > ...` while leaving lexical suffix strings such as `*-eie-` alone.
- Corrected the mathematical notation `8,22.1033` to `8,22·10^33` after visual verification against the rendered PDF page.
- Added a `table_status` column to `deuffic-relative-chronology-edges.tsv` marking it as a derived analytical table rather than a direct source table.

### Note on `*u̥n`

The source itself uses the notation `*u̥n` in the headings and final chronology. In section 2.10, Deuffic explains the rule in relation to Matasović's formulation `*pN > *wN` after back vowels and McCone's formulation `p > w` between a back vowel and `n`. Therefore `*u̥n` should be treated here as Deuffic's notation for a Celtic-stage labial glide/sonorant outcome before `n`, roughly comparable in function to `*wn` in the cited formulations. It is not being normalized here into a standard PIE phoneme `*u̥`.

## Future quality pass

A separate future-quality handoff has been added as `next-pass-handoff.md`. It records optional next-pass work for upgrading this package from `complete-working` to `complete-clean` without turning it into a diplomatic transcription project.
