# Nomina im Indogermanischen Lexikon — extraction report

## Source assessment

- Source file: `wodtko-2008-nil.pdf`
- Assessed source type: `mixed/scanned-with-ocr-text-layer`
- PDF pages: 908
- Extraction date: 2026-05-07

This PDF is not a clean born-digital text source. It is a scanned page-image PDF with an OCR/text layer produced before this extraction. The text layer is usable for broad corpus search and structure, but it contains systematic encoding/OCR damage in technical notation. The extraction therefore preserves the text-layer content with conservative cleanup and records unresolved character-fidelity risk rather than silently over-normalizing.

## Corrections applied

- Removed form-feed page breaks from `pdftotext` output and replaced them with explicit HTML source-location anchors.
- Removed trailing whitespace and leading OCR-layout indentation that would otherwise create unintended Markdown code blocks.
- Removed stray non-text control characters and normalized Unicode to NFC only, avoiding compatibility normalization.
- Repaired line-initial OCR substitutions where `•` or `·` appeared in the place of a source asterisk at the start of an entry/form line.
- Bibliography and index were separated from the main dictionary files.
- Main dictionary was split by initial letter section using source page ranges derived from the table of contents.
- Cover page was rasterized as a single plate image in `images/`; ordinary scanned page images were not duplicated.

## Unresolved issues

1. Superscript aspiration is not reliably encoded in the OCR/text layer. Examples include OCR-like sequences such as `bb` where the source image visibly has `bʰ` in forms such as `*bʰer-`. These were not globally normalized because the mapping is context-dependent.
2. Superscript labialization is not reliably encoded. Examples include candidates such as `gP`, where visual checking suggests source notation like `gʷ` in some contexts.
3. Laryngeal indices are not reliably encoded. The text layer contains a mixture of ASCII digits, punctuation-like substitutes, and damaged forms; no global conversion to `h₁ h₂ h₃` was applied.
4. Greek text is OCR-damaged in places. Greek passages and pseudo-Greek line noise should be checked against page images before citation-critical use.
5. Dense index entries preserve one source line per OCR line where possible, but some column breaks and diacritics are probably damaged by the source OCR.
6. PDF page 809 appears to contain scan/OCR noise with no recoverable text content and was excluded from the index file.
7. Footnotes are preserved in page order, but the extraction does not guarantee perfect reattachment of footnote markers to every note.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: unresolved. The output contains ASCII/damaged laryngeal candidates and should not be treated as normalized.
- Macron vowels: unresolved. Some macron vowels survive, but the OCR/text layer also confuses macrons with umlauts or drops marks, especially in dense lexical material.
- `ʰ ʷ` vs. `h w`: unresolved. Superscript aspiration and labialization are a major systematic weak spot in this extraction.
- `ə` vs. `e` or `9`: unresolved; no reliable global check was possible.
- Underdot consonants/vowels: unresolved; source OCR may drop or substitute combining marks.
- `ǵ ḱ`: unresolved; palatal/acute consonant distinctions may be damaged.
- `*` vs. absent/bullet substitutes: partially repaired only at line starts; internal asterisk substitutions may remain.
- `†`: unresolved; no full visual verification was performed.

## Codepoint inventory (approximate)

All counts are approximate and intended only for cross-pass comparison, not certification.

```json
{
  "laryngeals": {
    "h1": 76,
    "h2": 846,
    "h3": 164
  },
  "macron_a": 6471,
  "macron_e": 0,
  "macron_i": 0,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 0,
  "greek_chars": 0,
  "combining_diacritics": 0,
  "dagger": 0
}
```

## Additional probe counts (approximate)

```json
{
  "replacement_char": 0,
  "form_feed": 0,
  "private_use": 0,
  "line_initial_bullet_repaired_or_remaining": 65,
  "ocr_garbled_superscript_candidates_bb": 835,
  "ocr_garbled_labial_candidates_gP": 63,
  "ascii_laryngeal_candidates_h1_h2_h3": 1086
}
```

## Structural integrity check

- Headings and YAML front matter were added consistently to each file.
- Page anchors were inserted throughout the extraction.
- Bibliography and index are separate files.
- The main dictionary is chunked by initial letter section.
- Tables and dense paradigms were not deeply reconstructed into Markdown tables in this pass; the extraction favors line-level preservation over structural normalization because character fidelity is the primary constraint.
- No claim is made that page-boundary continuation text is fully repaired.

## Image inventory

- `wodtko-2008-nil-p1-plate1.png` — cover plate / Umschlagbild, PDF page 1; caption: Fragment einer karischen Inschrift aus Saqqāra (cover image; rasterized full cover page)
