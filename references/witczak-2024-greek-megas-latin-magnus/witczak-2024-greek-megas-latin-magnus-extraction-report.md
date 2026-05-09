# Extraction report — witczak-2024-greek-megas-latin-magnus

## Source type

Born-digital PDF. A machine-readable text layer is present. The raw extracted text was used as the primary input, with rendered-page inspection used for systematic character verification where the text layer flattened visual subscript laryngeal digits or split combining marks.

## Corrections applied

- Removed running headers, page numbers, and page-break artifacts.
- Rejoined paragraph lineation and repaired page-boundary continuation text.
- Repaired line-break hyphenation and source-layout splits, including Indo-European compounds, section headings split from following text, and forms split across page/line boundaries.
- Split the bibliography into `witczak-2024-greek-megas-latin-magnus-bibliography.md` as required by the project instructions.
- Converted printed footnotes to Markdown footnote references and definitions.
- Applied laryngeal normalization after rendered-page checks: `h1`, `h2`, `h3` in laryngeal contexts were rendered as `h₁`, `h₂`, `h₃`; vocalic laryngeals were rendered as `h̥₁`, `h̥₂`, `h̥₃` where appropriate.
- Preserved source-specific notation such as `*megA-`, `*magA-`, `*mėĝh₂-`, `*sm̥Ho-`, Greek forms, macrons, underdots, and combining inverted breve below.
- No images, figures, diagrams, maps, plates, or image-rendered tables were detected by embedded-image extraction or rendered-page inspection.

## Unresolved-issues list

- No `[unclear]` markers were inserted.
- The PDF text layer systematically encoded visually subscript laryngeal indices as baseline ASCII digits. These were normalized to Unicode subscripts based on rendered-page verification and recurring scholarly context. A later pass could still compare every laryngeal-bearing form against the rendered PDF.
- Italics were not exhaustively reconstructed for every cited lexical item. The extraction prioritizes character fidelity over typographic restoration.
- The order of combining marks in `*meĝh̥́₂-no-s` follows a normalized readable Unicode sequence (`h` + ring below + acute + subscript two), based on rendered-page inspection of §3.12.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: laryngeal contexts were normalized to subscript digits. Remaining ASCII digit sequences such as `a2` were retained where they appear to be non-laryngeal notation.
- Macron vowels: macron-bearing Latin/Sanskrit/Baltic forms were retained where detected. Dense bibliography entries and notes were checked, but not certified as exhaustively verified.
- `ʰ ʷ`: the source uses `*ĝh` in the text layer but the rendered page shows aspirated notation in at least one context. This extraction uses `*ĝʰ` in the §3.1 aspiration formula; a later character-authoritative pass could verify every aspirated-stop context.
- `ə`: schwa was retained in footnotes as `*ə₂` and `*ə̯₂`.
- Underdot/ring-below characters: forms such as `m̥`, `r̥`, `h̥`, `ṣ`, `ṇ`, `ṃ`-type notation were preserved where present; exact coverage is not certified.
- `ǵ ḱ`: no `ǵ` was detected; `ḱ` appears in the poetic phrase in note 4 and was retained.
- `*`: reconstructed-form asterisks were retained as literal U+002A characters.
- `†`: no dagger was detected.

## Codepoint inventory

Approximate counts:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 1,
    "h2": 71,
    "h3": 0
  },
  "macron_a": 32,
  "macron_e": 0,
  "macron_i": 8,
  "macron_o": 3,
  "macron_u": 0,
  "schwa": 2,
  "greek_chars": 132,
  "combining_diacritics": 48,
  "dagger": 0
}
```

## Structural integrity check

- Article-level headings and numbered subsections 1–4, 2.1–2.12, and 3.1–3.16 were preserved.
- Footnotes 1–7 are attached as Markdown footnotes.
- The bibliography is separate from the main text.
- No index is present in the source.
- No semantic tables were present.
- No continuation text appears intentionally omitted at page boundaries, but a later pass could compare every page boundary against the rendered PDF.

## Image inventory

No images extracted; no `[image-only...]` placeholders used.
