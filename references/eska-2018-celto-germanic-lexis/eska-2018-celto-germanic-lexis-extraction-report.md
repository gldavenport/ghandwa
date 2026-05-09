---
title: "Celto-Germanic Lexis in Light of Laryngeal Realism — Extraction Report"
author: "Joseph F. Eska"
date: 2018
source_type: scanned
extraction_date: 2026-05-08
source_file: eska-2018-celto-germanic-lexis.pdf
chunk: extraction-report
---

# Extraction Report

## Source type

Scanned-only PDF. No usable machine-readable text layer was present. The extraction was based on page rendering, OCR, and targeted manual correction. Because the whole source is scanned, every character is ultimately inferential; inline `[unclear]` markers were reserved for forms or readings that remained materially uncertain rather than marking every character.

## Corrections applied

- Reconstructed paragraphs from OCR output and removed running headers, page numbers, line-break hyphenation, and OCR blank-line fragmentation.
- Split the article into main text and bibliography files according to project instructions.
- Preserved Figure 1 as a cropped PNG in `images/` and linked it at the original figure location.
- Applied targeted character normalization for obvious OCR confusions: `Wamow` → `Warnow`, `Genmanic` → `Germanic`, `Celto-Genmanic` → `Celto-Germanic`, `Phanet-ics` → `Phonetics`, `fii/fiir` → `für`, and other prose-level repairs.
- Repaired many recurring linguistic glyph confusions by context: θ/þ/x/φ, macron vowels, IPA aspiration marks, laryngeal subscript digits, and angle brackets used for orthography.

## Unresolved issues list

The scan quality is adequate for prose but weak for dense phonological and lexical notation. The following areas remain high-risk and need a targeted second pass before treating this as character-authoritative:

1. §6 list item 5d: PGmc. form before `istiz` remains unresolved.
2. §9 table (2) and §9 expanded table (3): the stop-series tables were too glyph-dense for reliable recovery from this scan. They were preserved as structured summaries with explicit notes.
3. §13 table (6) and §14 table (7): the stop-series tables were too glyph-dense for reliable recovery from this scan. They were preserved as structured summaries with explicit notes.
4. Footnote 5: the Old Irish feminine form glossed “bondwoman; concubine” was not recovered confidently.
5. §12(5a): the Celtiberian form after `SDAnm` should be checked against the page image and MLH K.6.1.
6. §15–§19 lexical forms: forms containing `φ`, `θ`, `þ`, `x`, `h₂`, `h₃`, superscript aspiration, and labiovelar marks were normalized by context but not fully certifiable from the scanned glyphs.
7. Bibliography entries were cleaned from OCR, but several titles with Welsh, German, Spanish, and Italian diacritics should be checked against external bibliographic records.

## Confusion-pair report

- `h₁ h₂ h₃`: present in output where context strongly suggested laryngeal notation; not fully verified from scan.
- Macron vowels `ā ē ī ō ū`: normalized to precomposed macron vowels where read or inferred; not fully verified across all lexical forms.
- Superscript `ʰ ʷ`: used in phonological notation where visible/inferable; all table occurrences remain high-risk.
- `ə`: no confirmed source instances recovered.
- Underdot letters `ṛ ḷ ṃ ṇ`: no confirmed source instances recovered.
- `ǵ ḱ`: limited use in reconstructed forms; not fully verified.
- Asterisk `*`: preserved before reconstructed forms where visible/inferable; dense table occurrences remain high-risk.
- Dagger `†`: no confirmed source instances recovered.
- Source-specific high-risk pairs: `þ/θ`, `φ/f`, `x/h`, `w/y`, `OIcel./OIr.`, `LIDC/LIH`, and `CIL/CII/CI`.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

- `h₁`: 4
- `h₂`: 3
- `h₃`: 2
- `ā`: 19
- `ē`: 17
- `ī`: 41
- `ō`: 13
- `ū`: 10
- `ə`: 0
- Greek-range characters: 20
- Combining diacritics: 1
- `†`: 0

## Structural integrity check

- Main headings are consistent.
- Main text and bibliography were separated.
- Footnotes were attached as Markdown footnotes.
- Figure 1 was extracted and linked.
- Dense sound-law tables were not fully reconstructed; they require a targeted table pass.
- No index is present in the source.

## Image inventory

| Filename | Source label | Page | Caption |
|---|---:|---:|---|
| `images/eska-2018-celto-germanic-lexis-fig1.png` | Figure 1 | 29 | Indo-European family tree (after Labov 2007:345) |
