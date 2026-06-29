---
title: "Extraction report: Woodhouse 2017, Delabialization after *u"
source_file: "woodhouse-2017-delabialization-after-u.pdf"
extraction_date: "2026-05-26"
---

# Extraction report

## Source assessment

- **Source type:** born-digital PDF article extracted from an edited volume.
- **Article pages extracted:** source PDF pages 8-82, corresponding to printed pages 845-919.
- **Preliminary pages:** PDF pages 1-7 contain anthology cover/copyright/table-of-contents material and were not included in the main corpus Markdown except for source metadata.
- **Text-layer quality:** mostly reliable for reading order and ordinary characters, but not character-authoritative. The embedded text layer drops parts of ligatures (`Th`, `fi`, `ff`, `ft`, `tt`, etc.) and uses private-use glyphs for some phonetic/philological symbols.
- **Layout complexity:** mostly single-column scholarly prose with footnotes, one small phoneme table, many cited forms, Sanskrit/Vedic transliteration, Greek, Cyrillic, and Indo-European reconstructions.
- **High-risk zones:** phonological symbols, subscript/superscript notation, Vedic accent marks, Greek, Cyrillic, bibliography, and the appendix list of roots.

## Corrections applied

- Removed running headers and page numbers from continuation pages.
- Rejoined line-broken paragraphs and repaired ordinary hyphenation where clear.
- Preserved the article abstract, keywords, section numbering, appendix heading, references, and footnote text.
- Moved footnote blocks to a final `## Footnotes` section to prevent page-bottom note continuations from interrupting body prose.
- Applied source-specific ligature repairs where the text layer systematically dropped characters, for example `ater` -> `after`, `irst` -> `first`, `suix` -> `suffix`, `relex` -> `reflex`, `atested` -> `attested`, `diferent` -> `different`, `hese` -> `These` in sentence-initial contexts, and comparable recurring forms.
- Converted common laryngeal and author-specific tectal indices from text-layer forms like `h2`, `k1`, `g2` to subscripted forms such as `h₂`, `k₁`, `g₂` where the context indicated technical notation.
- Replaced recurrent private-use glyphs where visual inspection/context made the reading clear, including several Vedic long-vowel+acute glyphs, syllabic resonant/nasal glyphs, and author-specific tectal symbols.

## Source-specific glyph/confusion map

High-confidence or contextually strong mappings used in the main extraction include:

```text
U+F001 -> ᵘ
U+F00A -> n̥
U+F00C -> r̥
U+F00D -> ŕ̥
U+F00F -> ū
U+F018 -> ā́
U+F01A -> ī́
U+F01D -> ṱ
U+F032 -> ė
U+F036 -> ũ
U+F045 -> ĝ
U+F046 -> k̂
U+F04B -> ŭ
U+F050 -> K̂
U+F051 -> ę
U+F052 -> á
U+F053 -> ṙ
U+F054 -> á
U+F055 -> ŕ̥
U+F056 -> ē
U+F059 -> ă
U+F05B -> ū
U+F05C -> ū
U+F05D -> ē
```

Lower-confidence context-based mappings were also applied for a few rare glyphs. One especially rare glyph was retained as `[unclear-glyph]` rather than guessed.

## Linguistics QC checks performed

- Visual spot-checks against rendered pages 845, 846, 852, 878, 919.
- Private-use glyph inventory and sample visual glyph sheet.
- Search/replacement pass for common dropped-ligature failures.
- Laryngeal/index normalization pass for `h₁ h₂ h₃`, `k₁ k₂`, and `g₁ g₂` notation.
- Bibliography pass for gross line-joining and running-header removal.
- Search for remaining private-use characters after mapped substitutions.

## Unresolved issues

- This extraction is suitable for corpus search and ordinary AI parsing, but it is not fully character-authoritative for every cited linguistic form.
- Some rare private-use glyphs in Lithuanian/Latvian/Avestan/Sanskrit examples were mapped by context but should be checked visually before quotation or derivational use.
- Italic/cited-form styling was not exhaustively converted to Markdown code spans. The text is prioritized for readability and searchability.
- The initial phoneme table was preserved in readable text order, but it was not fully rebuilt as a formal Markdown table.
- The article’s bibliography was preserved in sequence, but individual entries were not manually verified character-by-character.

## Further-pass recommendation

A targeted second pass would add value if this article will be used for exact quotation or formal derivation. Best next checks:

1. Verify all appendix root entries against the PDF rendering.
2. Verify all Vedic/Sanskrit accent-bearing forms.
3. Verify all private-use glyph mappings in Lithuanian, Latvian, Avestan, and Old Prussian examples.
4. Rebuild the §1 tectal table as a Markdown table after visual verification.
5. Add code-span wrapping around italicized cited forms if strict Markdown style consistency is required.


## Targeted second pass, 2026-05-26

A targeted character-authority pass was completed after the initial extraction. This pass did not re-extract the whole article; it focused on the high-risk zones identified in the first report.

### Areas checked and revised

- Rebuilt the §1 tectal-inventory display as a Markdown table after visual comparison with the PDF rendering.
- Replaced the appendix block with a cleaner structured version: numbered root entries, explicit cross-reference lines, preserved footnotes 56-57, a readable language-group index, and a Markdown summary table.
- Visually checked the appendix pages against rendered pages 906-912, with special attention to reconstructed roots, Lithuanian/Latvian forms, Avestan forms, Old Prussian forms, and Vedic/Sanskrit accent-bearing forms appearing there.
- Corrected the first-pass overmapping of U+F00F from `ū́` to `ū`.
- Corrected the first-pass overmapping of U+F04B from `ū` to `ŭ` in forms such as `*bhŭg₁o-s` and `*mŭk₂-`.
- Verified appendix-specific private-use glyphs: U+F00F = `ū`; U+F018 = `ā́`; U+F01D = `ṱ`; U+F032 = `ė`; U+F036 = `ũ`; U+F045 = `ĝ`; U+F04B = `ŭ`; U+F05F = `ā`.
- Rechecked the numerical summary table from the appendix and restored the row/column relationships lost in the first extraction.

### Remaining limitations after second pass

- The article is substantially improved for corpus search and form lookup, especially in the appendix, but it is still not a full diplomatic or character-authoritative edition of every form in the running text.
- The pass did not exhaustively convert every italic cited form in the article to Markdown code spans. Code-span cleanup remains stylistic rather than evidentiary.
- The bibliography was not character-verified entry by entry; only obvious lingering dropped-ligature artifacts encountered during the pass were repaired.
- Exact quotation of dense linguistic notation outside the checked zones should still be verified against the PDF rendering.

### Further-pass recommendation

No further general cleanup pass is necessary for ordinary corpus use. A future third pass would only be worthwhile for a narrow purpose: bibliography character audit, exhaustive code-span styling, or quote-authoritative verification of selected paragraphs/forms outside the appendix.
