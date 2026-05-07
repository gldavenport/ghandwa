# Extraction report — Ringe, *From Proto-Indo-European to Proto-Germanic*

## Source assessment

- Source file: `ringe-pie-to-proto-germanic-2nd-ed.pdf`
- Source type used for this pass: born-digital PDF with a machine-readable text layer.
- Noted exception: PDF page 1 is an image-only cover; it was represented with a brief accessible cover description.
- Primary extraction path: `pdftotext -layout`, followed by deterministic Unicode cleanup and Markdown structuring.

## Corrections applied

- Converted the PDF text layer's private-use oldstyle numerals to ASCII digits 0–9.
- Converted the PDF text layer's private-use small-cap letters to uppercase Latin letters.
- Replaced typographic ligatures `ﬁ` and `ﬂ` with `fi` and `fl`.
- Normalized laryngeal indices from text-layer `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃`.
- Normalized common acute palatal spellings such as `k´`/`g´` and decomposed acute consonants where Unicode normalization allowed it.
- Repaired common spaces before combining diacritics introduced by extraction.
- Applied a conservative token-level normalization of superscript `ʷ` and `ʰ` in marked linguistic forms and isolated table cells.
- Removed some running-header lines when they matched recognizable page-header patterns.
- Added page anchors in the form `<a id="pdf-page-N"></a>` and `<!-- pdf-page: N -->` for source-location reference.
- Promoted recognizable section headings to Markdown headings.

## Unresolved-issues list

This pass did not insert inline `[unclear]` markers from visual uncertainty except for the cover description, because the extraction relied on the born-digital text layer. Remaining issues are systematic rather than tied to single visually unreadable places:

1. Superscript `ʷ` and `ʰ` conversion was rule-based. Some linguistic tokens may still contain plain `w` or `h` where the visual source has superscript glyphs, and a small number of ordinary tokens could theoretically have been over-normalized.
2. Dense paradigms and comparison tables are preserved largely by layout spacing rather than hand-built Markdown tables. They are corpus-usable as text but not guaranteed to render as aligned tables in every Markdown viewer.
3. Footnotes are preserved as extracted page text, but this pass did not hand-verify every footnote anchor-to-note pairing.
4. Greek, Indic, IPA, and reconstructed-form characters were normalized mechanically and spot-checked only by automated probes; this does not constitute a character-authoritative edition.
5. Remaining private-use characters after cleanup: none detected.
6. Remaining `ﬁ`/`ﬂ` ligatures after cleanup: none detected.

## Confusion-pair report

The following checks are approximate automated probes, not proof of correctness.

| Confusion pair | Probe result |
|---|---|
| `h₁ h₂ h₃` vs `h1 h2 h3` | Normalization applied. Remaining ASCII probes: {'h1': 0, 'h2': 0, 'h3': 0}. |
| precomposed macrons vs decomposed macrons | Unicode NFC applied. Counts below distinguish precomposed macron vowels, but combining macrons may remain where the source uses stacked or nonstandard scholarly marks. |
| macrons in body/notes/index | Not fully verified across all sections. Automated counts are available for regression comparison. |
| `ʰ ʷ` vs plain `h w` | Conservative token-level normalization applied. Remaining isolated plain labiovelar probes: 0; remaining isolated aspirate probes: 236. Contextual plain `h/w` inside tokens was not exhaustively verified. |
| `ə` vs `e` or `9` | `ə` count recorded below; no exhaustive visual verification. |
| underdot/syllabic marks | Unicode normalization and spacing repair applied; no exhaustive visual verification. |
| `ǵ ḱ` vs `g' k'` or `g´ k´` | Acute-consonant cleanup applied where detectable; no exhaustive visual verification. |
| `*` before reconstructed forms | Asterisks preserved from text layer; no exhaustive visual verification for dropped asterisks. |
| `†` dagger | Dagger count recorded below; no exhaustive visual verification. |

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "h1": 1176,
  "h2": 1414,
  "h3": 176,
  "macron_a": 1028,
  "macron_e": 1155,
  "macron_i": 953,
  "macron_o": 2000,
  "macron_u": 401,
  "schwa": 188,
  "greek_chars": 4762,
  "combining_diacritics": 1640,
  "dagger": 0
}
```

## Structural integrity check

- Headings: recognizable chapter and section headings were promoted to Markdown headings.
- Footnotes: retained in page-local order as extracted text.
- Tables/paradigms: retained in layout-preserving text blocks where possible, not hand-converted to full Markdown tables.
- Page boundaries: page anchors were inserted for every PDF page.
- Continuation text: no page-boundary loss was detected by script, but continuation integrity was not manually verified page by page.

## Assessment

This is a usable first-pass corpus extraction from a born-digital PDF text layer. It is not yet a character-authoritative edition. The likely next beneficial pass would be a targeted character-authority pass over superscript `ʷ/ʰ`, Greek/Indic forms, dense paradigms, references, and the index.
