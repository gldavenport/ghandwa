# Extraction report — Zair 2012

## Source type

Born-digital PDF. A machine-readable text layer is present. The raw text layer was the primary input; visual/image extraction was used only for the cover image and for spot-checking source character problems.

## Corrections applied

- Re-extracted/repackaged as a chunked monograph extraction under the updated instructions.
- Split the running text into front matter, chapter files, separate Chapter III environment chunks, a separate bibliography, and a separate Index Verborum file.
- Added a README index for navigation and a manifest with machine-readable counts.
- Extracted the embedded cover image as `images/zair-2012-reflexes-pie-laryngeals-celtic-p1-fig1.png` and inserted a Markdown image reference in the frontmatter file.
- Repaired systematic PDF text-layer ligature artifacts: `fif` → `fi`, `ffif` → `ffi`, and `flf` → `fl` where produced by the text layer.
- Normalized ASCII laryngeal indices in extracted text to subscript digits: `h1 h2 h3` → `h₁ h₂ h₃`; the same normalization was applied after Markdown cleanup.
- Repaired the source-specific palatovelar artifact `k̂` to `ḱ` where the PDF text layer used `k` plus combining circumflex for the palatovelar.
- Repaired common spacing artifacts around Hittite `h̬`, non-syllabic `i̯/u̯`, and section headings glued to numbered lexical/example entries.

## Unresolved-issues list

- No `[unclear]` markers were inserted in this pass because the source is born-digital and the text layer was available throughout.
- The extraction remains vulnerable to consistent text-layer errors that cannot be discovered by automated normalization alone.
- Some footnotes and dense example lists may still have imperfect paragraph boundaries, especially where page-bottom notes were merged by the source text layer.
- Index Verborum entries were normalized to one entry per line from the text-layer/index extraction, but dense two-column alignment may still hide ordering or association errors.
- The output does not claim a fully verified diplomatic character-authoritative edition; it is a cleaned corpus extraction with uncertainty retained in this report.

## Confusion-pair report

| Confusion pair | Approximate status in output |
|---|---|
| h₁ h₂ h₃ vs h1 h2 h3 | Subscript normalization applied. Approximate remaining ASCII laryngeal matches: 0 (not all automatically classifiable). |
| precomposed macron vowels vs decomposed macrons | Precomposed macron vowels are preserved where present; decomposed Greek/Indic/tone combinations also remain where the source text layer supplied combining marks. Not fully visually verified. |
| macrons in body, footnotes, index | Macron counts were measured across all Markdown files; dense index macrons were preserved from the index extraction. Not fully visually verified. |
| ʰ ʷ vs h w | Modifier-letter aspiration/labialization were not globally inferred where absent from the text layer; remaining risks not fully verified. |
| ə vs e or 9 | Approximate schwa count: 48. No full visual verification. |
| ṛ ḷ ṃ ṇ vs plain r/l/m/n | Underdot and syllabic-marker characters were preserved where present in the text layer. No full visual verification. |
| ǵ ḱ vs g/k apostrophe or accent artifacts | `k̂` artifact normalization was applied; remaining `k̂` count: 0. Other palatovelar characters were not exhaustively verified visually. |
| asterisk before reconstructed forms | Asterisks were preserved from the text layer; no global inference of missing asterisks was attempted. |
| dagger † vs plus/absence | Approximate dagger count: 0. No full visual verification. |

## Codepoint inventory

All counts are approximate and intended for cross-pass regression comparison only.

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 858,
    "h2": 1415,
    "h3": 479
  },
  "macron_a": 1170,
  "macron_e": 286,
  "macron_i": 480,
  "macron_o": 332,
  "macron_u": 334,
  "schwa": 48,
  "greek_chars": 6845,
  "combining_diacritics": 5235,
  "dagger": 0
}
```

## Structural integrity check

- Chunking follows the updated instructions: monograph-level chunking, Chapter III subdivided by source environment headings, separate bibliography, separate Index Verborum, and README navigation file.
- Headings are normalized to Markdown, but the source’s dense technical headings are preserved rather than silently renamed.
- Footnotes are retained in the relevant chunks; attachment quality is uncertain where the PDF text layer placed note material at page bottoms.
- Tables are not a major structural feature of this source; dense lists and Index Verborum entries are preserved as text rather than forced into Markdown tables.
- No continuation text is known to be omitted at page boundaries, but page-boundary repairs were not exhaustively checked visually.

## Image inventory

- `images/zair-2012-reflexes-pie-laryngeals-celtic-p1-fig1.png` — page 1, cover/plate image. Caption/source note from the book: “Cover illustration: Folio 78v of The Red Book of Hergest (Jesus MS.111), The Principal and Fellows of Jesus College, Oxford.”
