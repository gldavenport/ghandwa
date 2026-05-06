---
source_title: "A shared substrate between Greek and Italic"
author_creator: "Romain Garnier; Benoît Sagot"
date_year: 2017
source_file_name: "garnier-2017.pdf"
audit_date: "2026-05-06"
audit_type: "second character-authority pass"
pass_status: "completed"
---

# Garnier & Sagot 2017 — character-authority audit

## Scope

This pass targeted character authority rather than physical layout. It focused on reconstructed forms, Greek, laryngeals, superscripts, combining diacritics, footnote/citation collisions, abbreviation characters, and broken joins around technical forms.

## Rendered/source checks used

- Re-rendered the PDF pages locally for page-image verification.
- Spot-checked the recurring private-use glyph extracted as `U+E727` against rendered pages. It represents non-syllabic `u̯`, so the Markdown keeps `u̯` using Unicode `u` + combining inverted breve below.
- Checked contexts on pages with dense technical material, especially article pages 36, 44, 49, 53, 55, and 57.
- Re-ran a technical-token audit against PDF text extraction after normalizing `U+E727` to `u̯`.

## Repairs made in this pass

- Confirmed no remaining `U+E727`, object replacement characters, PDF soft-hyphen artifacts, or `�` replacement characters in the main Markdown.
- Repaired `DLG[^2]` misreadings to `DLG²`.
- Repaired false Markdown footnote conversions inside citations: `112–113¹⁵`, `215⁵`, and `208⁵⁶` are now preserved as superscript citation-note digits rather than document footnotes.
- Repaired the missed document footnote sequence after “three-mora law” to `[^20][^21]`.
- Escaped linguistic double-asterisk forms so Markdown does not treat them as bold markup, e.g. `\*\*τυπέω`, `\*\*kəluβo-`, `\*\*tiurba`, `\*\*pers-`.
- Repaired broken technical-form joins, including:
  - `*brówko-/*bréwko-/*brúko- ‘jumping animal’`
  - `*pryg- ‘to jump’`
  - `Welsh bref- ‘to low, bleat, bray’`
  - `*bʰléǵ-u̯-on- with`
  - `*su̯é-tro- < PIE`
  - `PIE *ḱ is reflected as k`
- Removed several spacing artifacts around `∼`, `ϝ`, short/long-vowel notation, and gloss quotes.
- Rebuilt the abbreviations and bibliography sections into separated Markdown entries while preserving characters, diacritics, and source order.

## Residual notes

- The PDF’s embedded text maps one recurrent special glyph to private-use `U+E727`; rendered-page checking supports `u̯` as the intended scholarly character.
- Italics remain selectively encoded, especially in bibliography and major source-title fields. The pass prioritized character authority and searchable scholarly notation over exhaustive formatting replication.
- Some visually indistinguishable Latin/Greek `o` cases in mixed forms remain governed by the extracted source text and were not aggressively normalized.
- Further passes could still improve paragraph structure in the body, but the most obvious character-authority issues found in this pass have been repaired.

## QA counts after this pass

- Remaining `U+E727`: 0
- Remaining `�`: 0
- Remaining object replacement characters: 0
- Remaining `DLG[^2]`: 0
- Remaining `law.20,21`: 0
- Remaining false Markdown note conversions for `112–113`, `215`, `208`: 0
- Remaining `∼*` spacing artifacts: 0


## Stress-test addendum — 2026-05-06

A subsequent stress test checked artifact residues, footnote integrity, Markdown continuity, page-break word splits, and searchability of high-risk linguistic strings. Minor repairs were applied to the main Markdown:

- `*Trī´ps` was corrected to `*Trī́ps`.
- `*hxi̯...` forms in footnote 13 were corrected to `*hₓi̯...`.
- `Skt bhr̥ṣṭi` was corrected to stem-form `Skt bhr̥ṣṭi-`.
- Residual page-break splits were repaired: `borrowed`, `Finally`, `subsequent`, `< PIE`, and `χurđíz > OHG hurd`.
- Section 5.7 was restored as a numbered list.

Post-repair counts: private-use glyphs 0; replacement characters 0; `U+FFFF` 0; `U+00B4` 0; missing footnotes 0; orphan footnotes 0; hyphenated word before page anchor 0.
