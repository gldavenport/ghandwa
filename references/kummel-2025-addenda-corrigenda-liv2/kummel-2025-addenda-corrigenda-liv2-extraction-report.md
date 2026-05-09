# Extraction report — Addenda und Corrigenda zu LIV²

- Source file: `kümmel-2025-addenda-corrigenda-liv2.pdf`
- Source type: born-digital PDF (machine-readable text layer present)
- Extraction timestamp: 2026-05-07T23:18:58Z
- Pages: 96
- Output package: `kummel-2025-addenda-corrigenda-liv2.zip`

## Corrections applied

- Used the PDF text layer as primary input, with Poppler `pdftotext -raw` as the base extraction because it preserved line continuity better than PyMuPDF for lexical entries.
- Used PyMuPDF as a secondary glyph check and inserted glyphs omitted by Poppler where page-level text alignment made the omission clear. The main systematic correction was palatovelar `k̑`: PyMuPDF exposed this as `kҮ`, which was corrected to `k̑`; approximately 187 such source-glyph cases were encountered.
- Also imported one omitted `Ƶ` in `(SƵB)` from secondary extraction.
- Repaired one clear ligature/text-map artifact `Suf ix` → `Suffix`.
- Removed repeated running headers, page numbers, and copyright footers from pages 2–96.
- Conservatively repaired selected line-break hyphenation while avoiding section/entry boundaries.
- Added page anchors as HTML comments (`<!-- p. N -->`) for later checking.
- No embedded figures or image-only tables were detected by `pdfimages -list`; no `images/` directory was produced.

## Unresolved issues list

- No `[unclear]` passages were inserted during this pass.
- The systematic `k̑` correction should be spot-checked in later QA because it depends on a source-specific font/text-map artifact. Inline `[?]` markers were not inserted for all corrected cases to keep the corpus usable; this is the main known review item.
- Some paragraph lineation remains close to the PDF text layer to avoid damaging dense lexical notation. Later passes could further reflow prose if desired.
- Secondary-glyph alignment produced a small number of unresolved page-level differences that were not imported automatically; first examples follow.
  - Page 34: 1 unresolved alignment difference(s), examples: `[('insert-unhandled?', '', 'ޖ')]`
  - Page 37: 1 unresolved alignment difference(s), examples: `[('insert-unhandled?', '', 'ޒ')]`
  - Page 53: 2 unresolved alignment difference(s), examples: `[('insert-unhandled?', '', 'ǂ'), ('insert-unhandled?', '', 'ǂ')]`
  - Page 54: 1 unresolved alignment difference(s), examples: `[('insert-unhandled?', '', 'ǂ')]`
  - Page 58: 1 unresolved alignment difference(s), examples: `[('insert-unhandled?', '', 'ϐ')]`
  - Page 71: 1 unresolved alignment difference(s), examples: `[('insert-unhandled?', '', 'ǂ')]`

## Confusion-pair report

| Item | Approximate status |
|---|---|
| `h₁ h₂ h₃` vs. ASCII `h1 h2 h3` | Subscript laryngeals retained; approximate counts h₁=429, h₂=525, h₃=196. ASCII sequences were not globally normalized because they may occur in citations or ordinary text. |
| macron vowels | Precomposed macron vowels retained where present; approximate counts ā=367, ē=119, ī=101, ō=100, ū=46. |
| `ʰ ʷ` vs. plain `h w` | Modifier letters retained where extracted; not exhaustively verified against rendering. |
| `ə` vs. `e/9` | Schwa retained where extracted; approximate count 123. |
| underdot letters `ṛ ḷ ṃ ṇ` | Retained where extracted; not exhaustively verified against rendering. |
| `ǵ ḱ` / palatovelar notation | Source mainly uses `g̑` and `k̑`; missing `k̑` combining marks from Poppler were restored from secondary extraction. |
| asterisk before reconstructed forms | Asterisks retained. No global claim of completeness. |
| dagger `†` | Approximate dagger count is 4. |

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 429,
    "h2": 525,
    "h3": 196
  },
  "macron_a": 367,
  "macron_e": 119,
  "macron_i": 101,
  "macron_o": 100,
  "macron_u": 46,
  "schwa": 123,
  "greek_chars": 1873,
  "combining_diacritics": 1965,
  "dagger": 4,
  "combining_inverted_breve": 351,
  "source_specific_k_inverted_breve": 190,
  "source_specific_z_with_stroke": 1
}
```

## Structural integrity check

- Headings were chunked according to the source’s own root-initial sections rather than arbitrary page ranges.
- The “Neue Literatur” abbreviation/literature list was extracted as the bibliography file.
- No separate index was detected; the opening “Übersicht” is retained in the front-matter file rather than emitted as an index file.
- Footnotes/annotations beginning with `Anm.` are retained inline with the relevant lexical entries.
- Dense lexical entry structure was left largely line-oriented to reduce risk of character loss in reconstructed forms.

## Image inventory

- No embedded images detected; no image placeholders used.
