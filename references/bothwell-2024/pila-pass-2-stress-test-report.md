---
source_title: "PILA: A Historical-Linguistic Dataset of Proto-Italic and Latin"
source_file_name: "2404.16341v1.pdf"
extraction_file: "pila-historical-linguistic-dataset-proto-italic-latin-pass-2.md"
report_date: "2026-05-04"
report_type: "stress-test report"
---

# PILA pass-2 Markdown stress-test report

## Scope

This stress test targeted the second-pass Markdown extraction for:

- searchability of core technical terms and forms;
- residual PDF/OCR artifacts;
- special-character coverage;
- Markdown structure;
- footnote consistency;
- table integrity and values;
- selected visual spot checks against rendered PDF pages.

## File-level checks

- Characters: 55,803
- Lines: 480
- Approximate word tokens: 8,357
- Unique non-ASCII characters: 38
- Suspicious control/artifact characters: 0
- Replacement characters: 0
- U+FFFE/U+FFFF-style PDF artifacts: 0
- `[unclear]` / `[illegible]` markers: 0

## Non-ASCII / special-character findings

Expected characters are present, including:

- typographic quotation marks and dashes: `‘ ’ “ ” – —`;
- source symbols: `†`, arrows `→ ← ↓`, `±`, `·`, `×`;
- formal notation: `⊆`, `∈`, `∩`, `≠`, `∅`;
- linguistic characters: `ŋ`, `ð`, `β`, `ʷ`;
- accented names and words: `Zürich`, `Mahé`, `Sébastien`, `Łukasz`, `İlhan`, `Antônio`, `Náhuatl`, `Yañez`.

No obvious residual PDF extraction artifacts were found.

## Structural checks

All major headings are present:

- Abstract
- 1. Introduction
- 2. Background
- 3. Related Work
- 4. PILA: Proto-Italic to Latin Dataset
- 4.1. Overview
- 4.2. Development
- 4.2.1–4.2.6 subsections
- 5. Applications
- 5.1. Sample Tasks
- 5.2. Dataset Compatibility
- 6. Conclusion
- 7. Acknowledgements
- 8. Bibliographical References
- 9. Language Resource References
- Footnotes

Tables 1–9 are present as Markdown tables. Algorithm 1 is present as a fenced text block.

Footnotes 1–6 have matching inline references and definitions.

## Search sentinel tests

Search tests passed for the main source-critical items:

- dataset and structure terms: `CLDF`, `languages.csv`, `forms.csv`, `cognates.csv`, `lemmata.csv`, `glosses.csv`, `tags.csv`, `overlaps.csv`;
- key stages: `Pre-Latin Proto-Italic`, `Ciceronian Latin`, `Proto-Italo-Celtic`;
- Table 1 forms: `*fragelis`, `*takslos`, `ta:lus`, `*a:zide:jo:`, `a:rdeo:`, `*pauros`;
- reconstruction examples: `*awide:o:`, `*awiðos`, `audeo:`, `avidus`, `aevita:s`, `aeta:s`, `genimen`, `ti:bur`;
- normalization examples: `*nomezos`, `*nomesos`, `*faβer`, `maŋnus`, `fraŋgo:`, `maiior`, `cuiius`;
- inflection examples: `fefelli:`, `ru:pi:`, `scri:psi:`, `ama:vi:`, `monui:`, `*monawai`, `*to`, `pultus`, `pulta:re`, `cru:s`, `cru:ris`, `flo:s`, `flo:ris`, `*osyo`, `*ejes`, `fe:li:x`;
- model/evaluation notation: `C ⊆ E × R`, `e ∈ E`, `r ∈ R`, `WER`, `PER`, `$d_{model}$`, `L²`, `bos`, `eos`, `[−0.01, 0.01]`;
- algorithm notation: `LSA(scores)`, `first[i]∩second[j] ≠ ∅`;
- later-source names: `Collatinus`, `UNIDIA`, `PBase`.

## Visual spot-check findings

Rendered-page checks confirm the following high-risk items:

- Page 5: `*faβer`, `(*f)`, `(*β)` are correctly rendered in the Markdown.
- Page 9: Table 9 values match the source, including the source's apparent percentage oddity `31 (0.1%)` for Ciobanu and Dinu (2014). This should be preserved unless making an editorial correction note.
- Page 10: The source visibly reads `Lateinsche Laut- Und Formenlehre`; the Markdown preserves that reading rather than silently correcting it to the expected German title.

## Issues found

### Minor capitalization issue

Several table occurrences of the dataset name `JAMBU` appear in the source in all caps. The pass-2 Markdown currently has `Jambu` in Tables 2, 3, and 9, plus a few prose occurrences. The bibliography title already has `JAMBU`.

Recommended correction:

- In Tables 2, 3, and 9, use `JAMBU` instead of `Jambu`.
- In running prose, either preserve the source's capitalization if visually checked, or leave `Jambu` if the source uses sentence-style capitalization there.

### Figure-description compression

Figure 1’s visual `Spanish French Italian · · ·` is paraphrased as “Spanish, French, Italian, and others.” This is acceptable for accessible description, but a character-authoritative figure caption pass could include the literal `Spanish, French, Italian, · · ·` inside the description.

### Source formatting intentionally not preserved

Table 1’s bold/underlined affected phones and color distinctions are described in prose rather than encoded inside the Markdown table. This matches clean-Markdown priorities, but a character-authoritative scholarly edition could encode bold/underline if desired.

## Recommendation

A full third pass is not warranted. The current pass is structurally strong and searchable, with no detected residual PDF-artifact characters and good coverage of the high-risk linguistic notation.

The only useful further work would be a very small targeted cleanup pass:

1. Correct table acronym capitalization for `JAMBU`.
2. Optionally adjust Figure 1’s accessible description to include the literal ellipsis marks `· · ·`.
3. Optionally encode Table 1’s bold/underline affected phones, if the Markdown is meant to be visually source-critical rather than clean corpus text.

For corpus/search use, the file is already usable. For a character-authoritative edition, do the small targeted cleanup above, then stop.
