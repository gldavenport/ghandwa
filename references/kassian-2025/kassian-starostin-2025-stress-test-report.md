---
source_file: kassian-starostin-2025-language-trees-sampled-ancestors-hybrid-model-second-pass.md
report_date: 2026-05-04
report_type: extraction stress-test report
---

# Stress-test report: Kassian & Starostin 2025 extraction

## File tested

`kassian-starostin-2025-language-trees-sampled-ancestors-hybrid-model-second-pass.md`

## Automated artifact checks

- Replacement characters: 0
- PDF hyphen/private-use artifacts: 0
- Soft hyphen/object replacement/control-character artifacts: 0
- `[unclear]` markers: 0
- Page anchors: 10
- Figure captions: 2
- Markdown table rows: 6
- Remaining obvious page-break hyphenation patterns checked: no hits for `Eur-`, `classifi-`, `lexico-`, `phylo-`, `recon-`, `corres-`, `Supple-`.
- Raw URL/DOI extraction: 33 URL-like strings; main DOI and reference DOIs are present. A few sentence-final URLs are followed by punctuation in prose, which is acceptable for readable Markdown but could be regularized if link-parsing is a priority.

## Searchability tests

Representative exact searches succeeded for:

- `derivational drift`
- `semantic specification`
- `IE-CoR protocols`
- `puˈli`, `πουλί`, `πουλλίον`, `ποῦλλος`
- `ˈko̞kale̞`, `σύγνοφο`, `tʃʰu`
- `woḍon`, `kʰaṛā`, `ḍulomɨ`
- `kr̥ṣṇá`, `áśman`
- `kʷekʷlo`, `kʷelh1`
- `majority rule consensus`

## Character-audit findings

The second-pass file is clean enough for ordinary corpus use and technical search. The main residual character issue is not corruption but source/Unicode interpretation:

- The PDF text layer encodes the first character of Iranian `*car-ta` as Cyrillic small es (`с`, U+0441), while the rendered page image is visually indistinguishable from Latin `c`. The second-pass Markdown currently uses Latin `c` for searchability. For stricter source-character fidelity, this should either be restored to `*сar-ta` with a QA note or left as Latin `*car-ta` with an explicit note that the PDF text layer mapped it as Cyrillic.
- NFC normalization changes Greek oxia `ί` to tonos `ί` and changes mathematical angle brackets `〈〉` to Unicode angle brackets `〈〉`. These are not errors, but they mean exact Unicode searches may differ depending on normalization.
- The Hittite `u̯`/`uu̯` forms, Tsakonian lowering marks, Kashmiri/Sanskrit dot-below forms, and PIE `kʷ` forms passed spot checks against the PDF text layer and/or rendered image.

## Further-pass value

A third pass would be useful only for character-authoritative polish, not for general readable Markdown. Best targets:

1. Decide and document treatment of PDF-text-layer Cyrillic `с` in `*car-ta`.
2. Optionally add a short Unicode-normalization/search note for Greek oxia/tonos and angle-bracket variants.
3. Optionally regularize sentence-final URLs so URL parsers do not absorb trailing punctuation.
4. Optionally transcribe more of Fig. 1 terminal labels from the dense tree image, if figure-label searchability matters.

Recommendation: run a light third pass only if this file is intended to be a character-authoritative reference or used for exact-form search across a larger normalized corpus. Otherwise, the second pass is sufficient.
