---
title: "Syntactic Reconstruction and Proto-Germanic"
author: "George Walkden"
date: "2014"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "walkden-2014-syntactic-reconstruction-proto-germanic.pdf"
chunk: "extraction report"
---
# Extraction report — Walkden 2014

## Source type

Born-digital PDF with a machine-readable text layer. The PDF uses several embedded custom fonts, and some special glyphs in the text layer required contextual repair. Raw text, not visual rendering, was used as primary input; visual/page rendering was used for figure extraction and for spot-checking custom-glyph cases.

## Corrections applied

- Repaired common ligatures: `ﬁ` → `fi`, `ﬂ` → `fl`.
- Repaired custom-font control-glyph mappings contextually: `` as `×`, `±`, or `Ø`; `` as `Ø`, `Øystein`, or `Tromsø`, according to context.
- Repaired extracted arrow glyphs in formula lines: `!` → `→`.
- Rejoined obvious line-break hyphenation in prose blocks.
- Normalized starred Proto-Germanic `*hw-` forms to `*hʷ-` where the source text layer flattened superscript `w`.
- Converted figure captions to Markdown image references and rasterized the corresponding page regions into `images/`.

## Unresolved issues list

- No inline `[unclear]` markers were inserted. This should not be taken as a guarantee of character-perfect output.
- Tables are preserved mainly as caption plus preformatted text blocks, not fully reconstructed Markdown tables. Dense statistical tables should be checked against the PDF if numerical precision is critical.
- Figure crops are page-region rasterizations rather than fully isolated vector-object exports. They preserve visual reference value but may include some surrounding figure labels/caption material.
- Italic/bold styling from the PDF was not systematically retained because the text layer uses custom embedded font names and the extraction prioritized character fidelity and searchable text.
- No residual non-tab/newline ASCII control characters were detected in the Markdown outputs.

## Confusion-pair report

- `h₁ h₂ h₃`: no subscript-laryngeal forms were detected in the output; this source primarily concerns Proto-Germanic syntax rather than PIE laryngeal reconstruction.
- Macron vowels: approximate output counts are reported below; they were not visually verified exhaustively.
- `ʰ ʷ`: starred Proto-Germanic `*hw-` was repaired to `*hʷ-` where detected; other superscript/modifier-letter cases were not exhaustively verified.
- `ə`, underdot letters, acute consonants, asterisks, daggers: approximate counts/absence only; not certified.
- Custom-font glyphs: the highest-risk items were `×`, `±`, `Ø`, `ø`, and `→`; these were contextually repaired but should be spot-checked in formulas and tables.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 2,
  "macron_e": 60,
  "macron_i": 25,
  "macron_o": 14,
  "macron_u": 13,
  "schwa": 1,
  "greek_chars": 324,
  "combining_diacritics": 0,
  "dagger": 0
}
```

## Structural integrity check

- Chapter and top-level section files follow the source structure. Chapter 5 is split at §§5.1–5.4 because the chapter exceeds 50 pages.
- Bibliography and indexes are separate files.
- Page anchors are included as HTML comments.
- Running headers and page-number headers were removed from body extraction where detected.
- Tables, interlinear examples, and tree/diagram material are generally preserved in fenced `text` blocks when prose joining would damage alignment.

## Image inventory

| File | Source figure | Printed page | Caption |
|---|---:|---:|---|
| `images/walkden-2014-fig1-1.png` | Figure 1.1 | 9 | The Germanic family tree |
| `images/walkden-2014-fig2-1.png` | Figure 2.1 | 32 | The Z-model of Andersen (1973: 767) |
| `images/walkden-2014-fig3-1.png` | Figure 3.1 | 75 | Percentage of V1, V2, V3, and V-later main clauses in ON pre-1300 |
| `images/walkden-2014-fig3-2.png` | Figure 3.2 | 82 | Percentage of V1/V2 vs. V-later main vs. subordinate clauses in the Heliand |
| `images/walkden-2014-fig4-1.png` | Figure 4.1 | 127 | Percentage of V1/V2 vs. V-later huat-clauses vs. non-huat clauses in the Heliand |
| `images/walkden-2014-fig4-2.png` | Figure 4.2 | 129 | Percentage of V1/V2 vs. V-later hwæt-clauses vs. non-hwæt clauses in the OE Bede |
| `images/walkden-2014-fig4-3.png` | Figure 4.3 | 131 | Percentage of V1/V2 vs. V-later hwæt-clauses vs. non-hwæt clauses in Ælfric’s Lives of Saints |
| `images/walkden-2014-fig5-1.png` | Figure 5.1 | 161 | Referential pronominal subjects in the Gothic Gospel of Matthew, by clause type |
| `images/walkden-2014-fig5-2.png` | Figure 5.2 | 162 | Referential pronominal subjects in the Gothic Gospel of Matthew, by person and number |
| `images/walkden-2014-fig5-3.png` | Figure 5.3 | 167 | Referential pronominal subjects in Old Icelandic ﬁnite clauses in IcePaHC 0.9.1, by text |
| `images/walkden-2014-fig5-4.png` | Figure 5.4 | 169 | Referential pronominal subjects in ﬁnite clauses in the First Grammatical Treatise, by person and number |
| `images/walkden-2014-fig5-5.png` | Figure 5.5 | 170 | Referential pronominal subjects in ﬁnite clauses in the Morkinskinna, by person and number |
| `images/walkden-2014-fig5-6.png` | Figure 5.6 | 177 | Referential null subjects in OE ﬁnite indicative clauses in the YCOE and YCOEP, by text |
| `images/walkden-2014-fig5-7.png` | Figure 5.7 | 180 | Referential null subjects in ﬁnite indicative clauses in the Lindisfarne Gospels and Rushworth Glosses, by person and number |
| `images/walkden-2014-fig5-8.png` | Figure 5.8 | 182 | Referential null subjects in ﬁnite indicative clauses in Beowulf, Bald’s Leechbook, Bede, and MS E of the Chronicle, by person and number |
| `images/walkden-2014-fig5-9.png` | Figure 5.9 | 186 | Referential null subjects in OHG ﬁnite clauses, by text and clause type |
| `images/walkden-2014-fig5-10.png` | Figure 5.10 | 189 | Referential null subjects in main clauses in OHG, by person and number |
| `images/walkden-2014-fig5-11.png` | Figure 5.11 | 191 | Referential pronominal subjects in the OS Heliand, by clause type |
| `images/walkden-2014-fig5-12.png` | Figure 5.12 | 194 | Referential pronominal subjects in the OS Heliand, by person and number |
| `images/walkden-2014-fig5-13.png` | Figure 5.13 | 224 | Frankish dominance and the main clause constraint in Romance |

## Caveat

This pass is corpus-ready for search and ordinary reference, but it is not a certified diplomatic or character-authoritative edition. Consistently mis-mapped custom glyphs can evade automated checks.
