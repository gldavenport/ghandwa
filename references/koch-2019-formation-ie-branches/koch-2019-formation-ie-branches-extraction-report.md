---
title: "Formation of the Indo-European branches in the light of the Archaeogenetic Revolution — Extraction Report"
author: "John T. Koch"
date: "Draft [19-iii-2019]; paper read 13-14 December 2018"
source_type: born-digital
extraction_date: 2026-05-07
source_file: "koch-2019-formation-ie-branches.pdf"
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The raw extracted text was used as the primary input. Rendered pages were used to verify figure placement, visible figure captions, and several high-risk linguistic notation items.

## Corrections applied

- Removed running headers, printed source page numbers, and decorative page furniture.
- Rejoined line-wrapped paragraphs and repaired routine line-break hyphenation.
- Extracted six figures as raster PNG crops into `images/` and inserted Markdown image references at the corresponding logical positions.
- Separated the bibliography into `koch-2019-formation-ie-branches-bibliography.md`.
- Converted the consonant inventories on source page 16 into Markdown tables.
- Normalized text-layer `satǝm` to `satəm` because the project instruction block treats U+0259 schwa as the target character.
- Corrected visible high-risk technical forms in the main text, including `*ḱm̥tóm`, `*kʷ`, `*gʷ`, `*gʷʰ`, `*ḱ`, `*ǵ`, `*ǵʰ`, and `*Dreu̯entiH₂-`.
- Applied conservative proper-name and sentence-initial capitalization repairs where the PDF text layer mapped capital letters inconsistently, especially `Ringe`, `RUKI`, `Reich`, `Renfrew`, `Rathlin`, `Rakhigarhi`, `Olalde`, `Oxford`, and `Oxbow`.

## Unresolved issues list

- The bibliography is retained as a separate file, but its dense two-column layout and several cross-column continuations make it the least reliable part of this pass. It should receive a dedicated bibliography audit if this source is to be used for citation extraction.
- Some capitalization in names beginning with R/O may remain wrong in the bibliography because the PDF text layer systematically mapped some capitals to lower-case letters.
- Inline numerical citations were preserved mainly as extracted rather than normalized into Markdown footnotes. Superscript styling is not exhaustively reconstructed.
- Italics and bold in running prose were not exhaustively reconstructed, except where they are obvious in headings, captions, quotations, and tables.
- The source itself contains probable typos such as `instrusive`, `rsulting`, and `inmdigenous`; these were preserved rather than silently corrected.
- Figure crops are raster extractions from rendered PDF pages rather than underlying vector/object extraction.

## Confusion-pair report

- `h₁ h₂ h₃`: no ordinary laryngeal-index series appears in the main text; `H₂` occurs in `*Dreu̯entiH₂-`. Further verification of subscript-laryngeal usage was not needed beyond that instance.
- Macron vowels `ā ē ī ō ū`: approximate counts are low; no dense paradigms or index sections were present. Bibliography names/titles with macrons may still warrant audit.
- Superscript modifier letters `ʰ ʷ`: corrected in the main technical consonant paragraph and consonant tables. Remaining bibliography instances were not exhaustively audited.
- Schwa `ə`: normalized from text-layer `ǝ` in `satəm`.
- Underdot letters: `m̥` in `*ḱm̥tóm` was retained. No broad Indic paradigm data present.
- Acute consonants `ǵ ḱ`: corrected in the main technical paragraph.
- Asterisk `*`: reconstructed-form asterisks were preserved where extracted.
- Dagger `†`: none observed.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 1,
  "macron_e": 0,
  "macron_i": 0,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 6,
  "greek_chars": 11,
  "combining_diacritics": 4,
  "dagger": 0
}
```

## Structural integrity check

- Headings were normalized into Markdown heading levels.
- Figure captions are represented as Markdown image alt text and listed in the manifest.
- The consonant inventories were converted into Markdown tables.
- No index section is present in the source.
- References are separated, but bibliography structure should be considered provisional pending a targeted reference-pass audit.

## Image inventory

- Figure 1: `images/koch-2019-formation-ie-branches-fig1.png` — page 2; Figure 1. August Schleicher’s 1861 tree model of the Indo-European language family.
- Figure 2: `images/koch-2019-formation-ie-branches-fig2.png` — page 2; Figure 2. Simplified version of Ringe et al. 2002, Fig. 8, ‘one of the best trees with Germanic omitted’, to which is added labels for the nodes PIE 1–6 as explained in this essay. The bracketed position of Germanic in the tree model is that indicated in the passage quoted from Ringe et al. 2002.
- Figure 3: `images/koch-2019-formation-ie-branches-fig3.png` — page 9; Figure 3. Zones of pre-Roman Indo-European and non-Indo-European names in the Iberian Peninsula: the dashed green line shows the divide, pointing out group names with ‘Celt-’ and the diagnostically Celtic -briga ‘hill, hillfort, major town’, contrasting with non-IE il(t)i. Some IE (mostly Celtic) outliers are shown in green.
- Figure 4: `images/koch-2019-formation-ie-branches-fig4.png` — page 9; Figure 4. Map illustrating the mutually exclusive distributions of metalwork of the Atlantic Late Bronze Age and evidence for ancient non-Indo-European languages around the western Mediterranean.
- Figure 5: `images/koch-2019-formation-ie-branches-fig5.png` — page 11; Figure 5. Map showing developments before ~4500 BP: 1) primary outward migration from Yamnaya on the Pontic–Caspian steppe, bringing with it the genetic steppe component and PIE 2 speech to found CWC in northern Europe and Afanasievo in the Siberian Altai; 2) the Proto-Beaker package spreads by sea from its origin in the Tagus estuary to Brittany and Mediterranean France. In Figures 5 and 6, straight sans-serif type indicates archaeological cultures, italic sans-serif type indicates linguistic stages, and straight serif type indicates genetic structure.
- Figure 6: `images/koch-2019-formation-ie-branches-fig6.png` — page 12; Figure 6. Map showing developments after ~4500 BP: 1) reflux of from north-eastern Europe bringing with it Proto-Indo-Iranian from PIE 6 and a genetic signature with ~68% steppe component and ~24% MNE; this genetic signature and Indo-Iranian speech subsequently spread from the Sintashta culture eastward to the Andronovo horizon and thence to South Asia; 2) the reflux of the Bell Beaker Complex westward from west-central Europe, bringing with it a form of Indo-European speech, probably Pre-Italo-Celtic.
