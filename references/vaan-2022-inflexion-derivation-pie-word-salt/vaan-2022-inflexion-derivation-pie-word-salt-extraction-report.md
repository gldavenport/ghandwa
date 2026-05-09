---
title: "From inflexion to derivation: The PIE word for ‘salt’ — extraction report"
author: "Michiel de Vaan"
date: "2022"
source_type: born-digital
extraction_date: 2026-05-07
source_file: "vaan-2022-inflexion-derivation-pie-word-salt.pdf"
---

# Extraction report

## Source type

Born-digital PDF. A machine-readable text layer was present and used as the primary input. Visual/layout inference was not used except for basic verification of source type and page structure. No embedded images were detected.

## Deliverables produced

- `vaan-2022-inflexion-derivation-pie-word-salt.md` — main article text, including English abstract, Russian abstract, numbered sections, footnote, and abbreviations.
- `vaan-2022-inflexion-derivation-pie-word-salt-bibliography.md` — bibliography split into a separate file.
- `vaan-2022-inflexion-derivation-pie-word-salt-extraction-report.md` — this QC record.
- `manifest.json` — machine-readable metrics.

No index file was produced because the source has no index. No `images/` directory was produced because no figures, plates, maps, or embedded images were present.

## Corrections applied

- Rejoined paragraphs broken by PDF lineation and page boundaries.
- Removed running headers, running page numbers, page-only metadata, and decorative layout artifacts.
- Repaired line-break hyphenation in English and Russian prose where the source text layer split words at line endings.
- Split the bibliography into its own Markdown file as required by the extraction instructions.
- Converted the single source footnote to a Markdown footnote and attached it to the relevant occurrence of `*sʕald`.
- Preserved source-location comments such as `<!-- source p. 417 -->` for later source-critical checking.
- Repaired high-risk text-layer artifacts observed during extraction, including `LIV2` → `LIV²`, the broken spacing in `sā̀ls`, and retained the line-break compound hyphen in Russian `балто-славянских`.
- Preserved laryngeals as subscript digits where present: `h₁`, `h₂`, `h₃`.

## Unresolved-issues list

No `[unclear]` or `[?]` markers were inserted. The source was machine-readable and short enough for a full structural pass, but the QC pass cannot guarantee that every combining accent and specialty character matches the PDF image. Items worth spot-checking in any later character-authoritative pass:

- `Latv. sā̀ls` — contains a combining grave after macron-a.
- `*sā́l-d` — contains a combining acute after macron-a.
- `*deḱḿt` and `*dekḿd` — contain combining acute after consonantal `m`.
- `yakŕ̥t` — contains r with below mark plus combining acute.
- `[g]e-nu-t꞊` — contains the modifier letter short equals sign `꞊`.

## Confusion-pair report

This report is approximate and should not be treated as a certification of full correctness.

| Confusion item | Output status |
|---|---|
| `h₁ h₂ h₃` vs. `h1 h2 h3` | Subscript laryngeal digits retained where present. ASCII `h1`, `h2`, `h3` were not found in the output. |
| Macron vowels | Macron vowels retained in body and bibliography where visible in the text layer. Combining-accent sequences remain in `sā̀ls`, `*sā́l-d`, and related forms. |
| `ʰ ʷ` vs. `h w` | Superscript modifier letters retained in forms such as `gʰs-ér-t`, `kʷod`, and `kʷid`. |
| `ə` vs. `e` or `9` | No schwa `ə` detected in the output. |
| `ṛ ḷ ṃ ṇ` | `r̥` appears as `r` plus combining ring below/diacritic sequence in `yakŕ̥t`; this should be spot-checked if a later pass normalizes Indic notation. |
| `ǵ ḱ` | `ḱ` retained in `*deḱḿt` and `*deḱmtós`; no `ǵ` detected. |
| Asterisk before reconstructed forms | Asterisks retained. |
| Dagger `†` | No dagger detected. |

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "h1": 2,
  "h2": 32,
  "h3": 2,
  "macron_a": 12,
  "macron_e": 1,
  "macron_i": 4,
  "macron_o": 2,
  "macron_u": 3,
  "schwa": 0,
  "greek_chars": 0,
  "combining_diacritics": 6,
  "dagger": 0
}
```

## Structural integrity check

- Headings are consistent: title, abstracts, numbered sections 1–7, abbreviations, and separate references.
- The bibliography contains approximately 61 reference entries.
- The single source footnote was preserved and attached as Markdown footnote `[^1]`.
- Page anchors/comments were added at source page transitions.
- No tables or figures were present.
- No continuation text appears intentionally omitted at page boundaries, but a later diff pass against rendered page images could still catch character-level errors missed by text-layer extraction.

## Image inventory

No image-only figures, maps, plates, diagrams, or tables were detected. No image placeholders were inserted.
