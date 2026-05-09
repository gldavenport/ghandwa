---
title: "Derivational Morphology: New Perspectives on the Italo-Celtic Hypothesis — extraction report"
author: "Tim de Goede"
date: "2014"
source_type: born-digital
extraction_date: "2026-05-07"
source_file: "goede-2014-derivational-morphology.pdf"
chunk: "extraction-report"
---

# Extraction report

## Source type

Born-digital PDF. A machine-readable text layer is present, but several embedded Identity-H Times New Roman font mappings in the PDF map many visible glyphs to spaces or wrong characters. The final extraction therefore uses the PDF text objects plus embedded TrueType `cmap` recovery for those malformed font spans. No OCR text was used in the final Markdown.

## Deliverables

- `goede-2014-derivational-morphology.md` — main text through the conclusion, including title page and table of contents.
- `goede-2014-derivational-morphology-bibliography.md` — bibliography section.
- `goede-2014-derivational-morphology-abbreviations.md` — abbreviation list.
- `manifest.json` — machine-readable metrics.
- `images/` — extracted cover-page image/logo.

## Corrections applied

- Recovered malformed Type0 font text using embedded TrueType cmap data, especially italic linguistic forms otherwise extracted as blanks.
- Recovered high-byte punctuation and diacritics in simple-font spans where the PDF exporter used glyph-code-like values for quotation marks, dashes, and characters such as `ü`.
- Rejoined line-broken prose heuristically.
- Normalized `h1`, `h2`, and `h3` laryngeal indices to `h₁`, `h₂`, and `h₃` after extraction.
- Removed printed page numbers while preserving page anchors as HTML comments.
- Split bibliography and abbreviations into separate Markdown files.

## Unresolved issues

- The source PDF's font mappings are defective; although embedded cmap recovery substantially improves character fidelity, the extraction cannot be certified as character-authoritative.
- The combining mark used in many glide forms is preserved as recovered from the embedded font (`i̭`, U+032D COMBINING CIRCUMFLEX BELOW). This may require human review if the intended notation was visually closer to another nonsyllabic marker.
- Footnote markers and footnote bodies are preserved in-line/plain form rather than converted into fully cross-linked Markdown footnotes.
- Paragraph reflow was heuristic. Some suffix-overview entries may be better represented as definition-list/table structures in a later pass.
- Unknown CID markers inserted: 0.
- Unknown byte markers inserted: 0.

## Unknown glyph inventory

- Unique unresolved CIDs sampled: `[]`
- Unique unresolved bytes sampled: `[]`

## Confusion-pair report

- `h₁ h₂ h₃` vs `h1 h2 h3`: baseline forms were normalized to subscript indices; residual baseline forms were not exhaustively human-verified.
- Macron vowels: precomposed macron vowels were preserved or recovered where available. Decomposed macron sequences were not intentionally introduced.
- `ʰ ʷ`: superscript modifier letters are recovered where present in embedded font maps, but not exhaustively visually checked.
- `ə`: no systematic source-wide visual verification was performed.
- `ṛ ḷ ṃ ṇ`: underdot characters are preserved where recovered; no source-wide visual certification.
- `ǵ ḱ`: acute consonants are preserved where recovered; no source-wide visual certification.
- `*`: asterisks before reconstructed forms were preserved from the text objects.
- `†`: no dagger instances were detected in the final output.

Potential residual issues detected automatically: none detected by simple pattern checks.

## Codepoint inventory

Approximate counts only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 26,
    "h2": 50,
    "h3": 12
  },
  "macron_a": 289,
  "macron_e": 46,
  "macron_i": 125,
  "macron_o": 129,
  "macron_u": 98,
  "schwa": 1,
  "greek_chars": 180,
  "combining_diacritics": 232,
  "dagger": 0
}
```

## Structural integrity check

- Headings: converted to Markdown headings by numbered-section pattern; table of contents lines are preserved as source lines.
- Bibliography: separated into `goede-2014-derivational-morphology-bibliography.md`.
- Abbreviations: separated into `goede-2014-derivational-morphology-abbreviations.md`.
- Tables/overview entries: preserved as reflowed text, not formal Markdown tables.
- Footnotes: preserved as plain text lines near their source locations; not cross-linked.
- Page anchors: preserved as `<!-- p. N -->` comments for source-location checking.

## Image inventory

- `goede-2014-derivational-morphology-p1-fig1.jpeg` — p. 1 unnumbered image; [no caption in source] cover-page image/logo

