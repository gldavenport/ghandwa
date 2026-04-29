# Extraction notes for clackson-2013

## Source

- Source file: `clackson-2013.pdf`
- Article: James Clackson, “Subgrouping in the Sabellian Branch of Indo-European,” *Transactions of the Philological Society* 00 (2013), 1-34.
- DOI: 10.1111/1467-968X.12034

## Passes performed

1. **First pass:** extracted embedded PDF text and reconstructed article structure in clean Markdown.
2. **Second pass:** removed running headers, ordinary page numbers, publisher footer text, and layout-only line breaks; converted section titles to Markdown headings; moved page footnotes into Markdown footnote definitions.
3. **Third pass:** audited character fidelity for ligatures, acute/macron/caron/grave encoding artifacts, German umlaut artifacts in German titles, c-cedilla forms, and dense linguistic notation. Spot-checked pages with dense South Picene/Umbrian notation and bibliography pages against rendered page images.
4. **Fifth targeted cleanup / bibliography normalization / character audit pass:** fixed missed footnote markers, removed accidental footnote-marker conversions in laryngeal notation and `CIL I²`, repaired the split heading at 3.2.2, joined a few remaining page-break seams, cleaned `Imag. Ital.` punctuation artifacts, and corrected a small set of high-value bibliography/notation artifacts.

## Known limitations

- The extraction is intended as clean corpus Markdown, not diplomatic transcription.
- Italics/small-caps from the PDF are not exhaustively represented where the embedded text stream did not expose styling.
- Dense epigraphic and reconstructed forms were cleaned, but a full diplomatic character-by-character proof against every page image would still be the next quality tier if publication-grade accuracy were required.
- No charts, maps, diagrams, or photo-only pages were present.

## Further-pass value

No further pass is needed for corpus research use. A future pass would be useful only for publication-grade proofing against every page image or for exhaustive recovery of italics/small caps not exposed by the embedded PDF text.


## Fifth-pass addendum

A further specialized pass was run after the fourth-pass package. This pass added:

- a normalized bibliography companion file;
- a targeted character audit against rendered page images and extracted PDF text;
- corrections to remaining high-risk linguistic notation and bibliography artifacts;
- an explicit character-audit notes file.

The main Markdown remains a clean extraction, not diplomatic transcription.
