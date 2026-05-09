---
title: "European prehistory between Celtic and Germanic: the Celto-Germanic isoglosses revisited — Extraction Report"
author: "Paulus van Sluis, Anders Richardt Jørgensen, and Guus Kroonen"
date: 2023
source_type: born-digital
extraction_date: 2026-05-07
source_file: sluis-2023-european-history-celtic-germanic.pdf
chunk: extraction-report
---

# Extraction Report

## Source Type

Born-digital PDF with a machine-readable text layer. The raw text layer was used as the primary input. Embedded figure images were extracted directly from the PDF where available.

## Output Files

- `sluis-2023-european-history-celtic-germanic.md` — main text and appendix, excluding bibliography
- `sluis-2023-european-history-celtic-germanic-bibliography.md` — references section
- `sluis-2023-european-history-celtic-germanic-extraction-report.md` — this report
- `manifest.json` — machine-readable manifest
- `images/` — extracted figure images

## Corrections Applied

- Repaired common typographic ligatures exposed in the text layer: `fi`, `fl`, `ff`, `ffi`, `ffl`, `st`.
- Normalized lowercase laryngeal text-layer forms `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃` because the rendered source uses subscript digits for laryngeals in linguistic forms.
- Removed repeated running headers, running footers, DOI footer lines, and isolated page numbers.
- Rejoined line-broken words and common hyphenation artifacts from the two-column PDF text layer.
- Split the bibliography into a separate Markdown file.
- Extracted Figures 13.1, 13.2, and 13.3 into `images/` and inserted Markdown image links at their caption locations.

## Unresolved Issues List

- No specific unreadable passages were identified in this pass.
- Inline italics and bold from the PDF were not exhaustively reconstructed; headings and figure placement were represented structurally in Markdown.
- Footnote markers and footnote text are preserved as text-layer content, but they were not converted into normalized Markdown footnote syntax.
- The appendix is dense and character-sensitive. This pass applies global normalization and line repair, but it should not be treated as character-certified without a further targeted visual pass against high-risk reconstructed forms.
- The extraction process cannot catch errors that are present consistently throughout the machine-readable text layer.

## Confusion-Pair Report

| Correct target | Status in this extraction |
|---|---|
| h₁ h₂ h₃ | Laryngeal ASCII sequences `h1`, `h2`, `h3` from the machine text layer were normalized to subscript-digit forms where they occurred as lowercase `h` + 1/2/3. This is a systematic repair, not a certified visual check of every instance. |
| ā ē ī ō ū | Macron vowels were preserved from the text layer. Ligature repairs were applied separately. |
| macrons in dense sections | Appendix and bibliography were included in the same normalization/count pass; dense appendix entries were not visually checked item by item. |
| ʰ ʷ | Modifier letters were preserved where exposed by the text layer. |
| ə | No schwa instances counted in output. |
| ṛ ḷ ṃ ṇ | Underdot characters were preserved where exposed by the text layer. |
| ǵ ḱ | Precomposed acute consonants were preserved where exposed by the text layer. |
| * | Asterisks before reconstructed forms were preserved from the text layer. |
| † | No dagger instances counted in output. |


## Codepoint Inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 71,
    "h2": 98,
    "h3": 22
  },
  "macron_a": 192,
  "macron_e": 84,
  "macron_i": 173,
  "macron_o": 157,
  "macron_u": 95,
  "schwa": 12,
  "greek_chars": 397,
  "combining_diacritics": 44,
  "dagger": 0
}
```

## Structural Integrity Check

- Headings were converted to Markdown heading levels according to the source section hierarchy.
- Bibliography was separated from the main file.
- Appendix lexical entries were preserved with headword-style headings and PC/PG/REF/isogloss/interpretation fields retained.
- Figures 13.1–13.3 were extracted and linked in the main Markdown file.
- No index section was present in the source.
- No `[unclear]` or `[?]` markers were inserted in this pass.

## Image Inventory

| File | Source label | Source page | Caption |
|---|---:|---:|---|
| `images/sluis-2023-european-history-celtic-germanic-fig13-1.png` | Figure 13.1 | 197 | Schematic representation of the main temporal strata of Celtic and Germanic. |
| `images/sluis-2023-european-history-celtic-germanic-fig13-2.jpg` | Figure 13.2 | 203 | Distribution range of the common yew (Taxus baccata). Data from Caudullo et al. (2017) CC-BY |
| `images/sluis-2023-european-history-celtic-germanic-fig13-3.jpg` | Figure 13.3 | 206 | The spread of silver in Europe. Map data from Mallory and Huld (1984). |
