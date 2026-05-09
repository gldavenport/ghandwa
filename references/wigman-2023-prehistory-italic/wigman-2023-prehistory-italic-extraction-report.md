---
title: "Unde vēnistī? — Extraction Report"
author: "Andrew Michael Wigman"
date: "2023-11-01"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "wigman-2023-prehistory-italic.pdf"
chunk: "wigman-2023-prehistory-italic-extraction-report"
---

# Extraction Report

## Source classification

Source type: **born-digital PDF**. A machine-readable text layer is present through the main text and was used as the primary input. Visual rendering was used only to verify figure pages and crop figure images.

## Corrections applied

- Replaced discretionary-hyphen/control glyphs emitted by the text layer (`U+FFFE`/soft-hyphen class) with hyphens where present. Approximate count: 0.
- Replaced private-use bullet glyphs with Markdown-compatible hyphen bullets where present. Approximate count: 16.
- Removed object-replacement characters where present. Approximate count: 0.
- Applied Unicode NFC normalization to compose canonically equivalent precomposed characters where Unicode provides them, especially macron vowels, while leaving non-composable scholarly notation intact.
- Normalized residual ASCII laryngeal indices h1/h2/h3 to h₁/h₂/h₃ in extracted content.
- Removed recurring running headers and page-number-only header lines from the text stream.
- Added source-page anchors as HTML comments at page boundaries for later checking.
- Converted source numbered headings to Markdown headings in content chunks.
- Reflowed ordinary running prose in Chapters 1 and 3-8, the Dutch summary, and the curriculum vitae. Dense lexical-data chunks and bibliography were kept line-preserving to avoid damaging reconstructed forms, table-like entry structures, and dense citation lines.
- Extracted/cropped figures to `images/` and inserted Markdown image references at caption locations where practical.

## Unresolved issues and human-review targets

1. Inline italics/bold/small caps from the PDF font layer were not exhaustively converted to Markdown because adding Markdown delimiters around reconstructed forms and scholarly notation can corrupt searchable character strings. Character fidelity was prioritized.
2. Some paragraph rejoining remains conservative at page anchors; page-boundary paragraphs may remain split where the anchor is inserted.
3. Chapter 2 lexical entries retain much of the source lineation. This is intentional for character and entry-structure safety, but it is less prose-clean than the running chapters.
4. Figure captions on pages 357-365 repeat labels 4.4-4.8, while the List of Figures identifies the corresponding later figures as 4.8-4.12. Captions are preserved as they appear on the figure pages; image filenames disambiguate duplicates.
5. The extraction did not include a full manual character-by-character audit against rendered pages. Counts below are approximate and intended for regression testing, not certification.

## Confusion-pair report

The known high-risk confusion list was spot-checked by codepoint inventory and targeted text inspection, but not fully verified manually. Residual ASCII h1/h2/h3 in extracted content was normalized to h₁/h₂/h₃; no broader normalization from ASCII to subscript/superscript forms was applied.

- h₁ h₂ h₃ vs. h1 h2 h3: possible isolated errors remain; not certified as fully checked.
- macron vowels ā ē ī ō ū vs. dropped or decomposed macrons: possible isolated errors remain; not certified as fully checked.
- superscript ʰ ʷ vs. plain h/w: possible isolated errors remain; not certified as fully checked.
- schwa ə vs. e/9: possible isolated errors remain; not certified as fully checked.
- underdot characters ṛ ḷ ṃ ṇ: possible isolated errors remain; not certified as fully checked.
- acute consonants ǵ ḱ: possible isolated errors remain; not certified as fully checked.
- asterisk before reconstructed forms: possible isolated errors remain; not certified as fully checked.
- dagger †: possible isolated errors remain; not certified as fully checked.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 174,
    "h2": 451,
    "h3": 53
  },
  "macron_a": 727,
  "macron_e": 427,
  "macron_i": 567,
  "macron_o": 639,
  "macron_u": 365,
  "schwa": 32,
  "greek_chars": 13102,
  "combining_diacritics": 849,
  "dagger": 0
}
```

## Structural integrity check

- Headings: converted from source numbered headings where detected; front matter and bibliography headings retained.
- Footnotes: retained inline in page-flow order from the text layer. No separate footnote apparatus was rebuilt.
- Tables and dense lexical structures: preserved primarily as source lineation rather than aggressively converted to Markdown tables, to reduce character-loss risk.
- Bibliography: extracted separately and kept line-preserving. Further bibliography-specific cleanup could improve entry wrapping, but may risk damaging diacritics and citation strings.
- Continuation text: no obvious systematic page-boundary loss detected in automated pass; not manually certified.

## Image inventory

| File | Source label | Source page | Caption |
|---|---:|---:|---|
| `images/wigman-2023-prehistory-italic-fig1-1.png` | Figure 1.1 | 2 | The linguistic diversity of the Italian peninsula represented by sites of inscriptions |
| `images/wigman-2023-prehistory-italic-fig4-1.png` | Figure 4.1 | 338 | Latin words of loanword origin distributed by existence of comparanda in Celtic, Germanic, and Greek |
| `images/wigman-2023-prehistory-italic-fig4-2.png` | Figure 4.2 | 339 | The transmission of Lat. cupressus and its comparanda |
| `images/wigman-2023-prehistory-italic-fig4-3.png` | Figure 4.3 | 348 | Overlapping irregular alternations between words with a Mediterranean distribution. (Words in gray are restricted to Italic) |
| `images/wigman-2023-prehistory-italic-fig4-4-rhamnus-alaternus.png` | Figure 4.4 | 350 | Range of Rhamnus alaternus (Based on Bolòs & Vigo 1984-2001) |
| `images/wigman-2023-prehistory-italic-fig4-5-ficus-carica.png` | Figure 4.5 | 350 | Range of Ficus carica (Based on Zohary, Hopf & Weiss 2012: 129) |
| `images/wigman-2023-prehistory-italic-fig4-6-buxus-sempervirens.png` | Figure 4.6 | 350 | Range of Buxus sempervirens (https://commons.wikimedia.org/wiki/File: Buxus_sempervirens_range.svg with refs.) |
| `images/wigman-2023-prehistory-italic-fig4-7-cupressus-sempervirens.png` | Figure 4.7 | 350 | Range of Cupressus sempervirens (https://commons.wikimedia.org/wiki/File:Cupressus_sempervirens_range.svg with refs.) |
| `images/wigman-2023-prehistory-italic-fig4-4-contact-situations-p357.png` | Figure 4.4 | 357 | Separate contact situations suggested by the distribution of non-inherited lexemes |
| `images/wigman-2023-prehistory-italic-fig4-5-italo-celtic-p359.png` | Figure 4.5 | 359 | One interpretation of contact incorporating Italo-Celtic considerations |
| `images/wigman-2023-prehistory-italic-fig4-6-early-italo-celtic-p360.png` | Figure 4.6 | 360 | An alternative scenario with an early Italo-Celtic split and later close contact |
| `images/wigman-2023-prehistory-italic-fig4-7-pca-loose-p364.png` | Figure 4.7 | 364 | PCA of loose analysis |
| `images/wigman-2023-prehistory-italic-fig4-8-pca-strict-p365.png` | Figure 4.8 | 365 | PCA of strict analysis |

## Output manifest summary

- Markdown files: 25
- Extracted images: 13
- Approximate unresolved count: 5

