# Ringe 2013 Historical Linguistics — extraction report

## Source identification

- Source type: born-digital PDF with machine-readable text layer.
- Primary input used: PDF text layer via PyMuPDF span extraction, with visual rendering used for figure cropping and spot-checks.
- Extraction target: clean, chunked, corpus-ready Markdown with bibliography and index separated.

## Corrections applied

- Running heads and page numbers were removed from body text.
- Line-break hyphenation was repaired conservatively during paragraph reflow outside index and bibliography sections.
- Ligatures were normalized where exposed by the text layer (`ﬁ` → `fi`, `ﬂ` → `fl`).
- Laryngeal indices were normalized to subscript digits where the PDF text layer exposed them as smaller lowered spans or ASCII digits: `h₁`, `h₂`, `h₃`.
- Superscript `h` and `w` in common PIE notation were normalized to `ʰ` and `ʷ` where the PDF exposed them as smaller raised spans.
- Some macron sequences exposed as base-letter plus overbar were normalized to precomposed macron vowels where straightforward (`ā ē ī ō ū`).
- All figures listed in the source were rasterized from the PDF into `images/` and referenced at caption locations.

## Unresolved issues

- This is a high-quality first extraction, not a character-authoritative final edition. Dense tables, paradigms, Greek/polytonic passages, and phonological notation should receive targeted second-pass audit before being treated as definitive.
- The PDF uses custom fonts without full Unicode mappings. Some combining marks over consonants, Greek, and IPA may require visual verification, especially in tables and examples.
- Italic and bold span markup was preserved in many places via HTML tags, but source-style preservation should be spot-checked where markup interacts with linguistic forms.
- Bibliography and index were preserved line-by-line to reduce drop risk; they were not reflowed into prose.
- No `[?]` inferred-character markers were inserted because the source was treated as born-digital and characters were taken from the text layer or deterministic span-position mapping. This does not imply all characters are correct.

## Confusion-pair report

- ASCII laryngeals h1/h2/h3 remaining: approximate remaining matches = 0; sample values = none observed in automated scan.
- possible unsuperscripted PIE labiovelars/aspirates: approximate remaining matches = 0; sample values = none observed in automated scan.
- macron-as-spacing-overbar sequences: approximate remaining matches = 0; sample values = none observed in automated scan.
- replacement/control characters: approximate remaining matches = 0; sample values = none observed in automated scan.
- Known high-risk pairs from the instruction sheet were checked by automated scan only; this does not certify full correctness.

## Codepoint inventory

All counts are approximate and intended for cross-pass comparison, not certification.

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 8,
    "h2": 30,
    "h3": 3
  },
  "macron_a": 257,
  "macron_e": 168,
  "macron_i": 164,
  "macron_o": 112,
  "macron_u": 93,
  "schwa": 461,
  "greek_chars": 5,
  "combining_diacritics": 86,
  "dagger": 69
}
```

## Structural integrity check

- Output is chunked by the source’s own top-level structure: front matter, Introduction, Chapters 1–11, Appendix, References, and Indexes.
- Every content chunk has YAML front matter with chunk and source page range.
- The README lists all output files, page ranges, and coverage.
- Figures have been extracted as PNGs and inserted in the relevant chapter files.
- Tables were extracted as text. A table-specific pass is recommended for Markdown-table normalization and character verification.
- Footnotes were retained in textual order; a footnote-specific pass is recommended if exact note anchoring is required.

## Image inventory

- Figure 5.1: `images/ringe-2013-historical-linguistics-fig5-1.png`; source page 84; caption: Typical lenition paths of long /t:/
- Figure 5.2: `images/ringe-2013-historical-linguistics-fig5-2.png`; source page 86; caption: Gestural score of the syllable [ta]
- Figure 5.3: `images/ringe-2013-historical-linguistics-fig5-3.png`; source page 86; caption: Gestural score of the syllable [tʰa]
- Figure 6.1: `images/ringe-2013-historical-linguistics-fig6-1.png`; source page 106; caption: First assimilation of Old English gædeling
- Figure 6.2: `images/ringe-2013-historical-linguistics-fig6-2.png`; source page 106; caption: Second assimilation of Old English gædeling
- Figure 6.3: `images/ringe-2013-historical-linguistics-fig6-3.png`; source page 109; caption: Second compensatory lengthening in Ancient Greek
- Figure 6.4: `images/ringe-2013-historical-linguistics-fig6-4.png`; source page 120; caption: Early southern Middle English vowels
- Figure 7.1: `images/ringe-2013-historical-linguistics-fig7-1.png`; source page 159; caption: Syntactic structure of the word arrivals
- Figure 8.1: `images/ringe-2013-historical-linguistics-fig8-1.png`; source page 169; caption: Ionic dialect ‘say’ before reanalysis
- Figure 8.2: `images/ringe-2013-historical-linguistics-fig8-2.png`; source page 169; caption: Ionic dialect ‘say’ after reanalysis
- Figure 8.3: `images/ringe-2013-historical-linguistics-fig8-3.png`; source page 176; caption: Morphological structure of menness in the dialect of the Orrmulum

## Recommended further passes

1. Character-fidelity pass for laryngeals, superscript aspiration/labialization, syllabic marks, IPA, Greek, and combining diacritics.
2. Table/paradigm pass for Chapters 5–11, especially dense sound-law and reconstruction tables.
3. Bibliography/index pass for page references, names with diacritics, and line-entry integrity.
4. Figure caption and figure-reference pass to confirm image crops and captions against rendered pages.
