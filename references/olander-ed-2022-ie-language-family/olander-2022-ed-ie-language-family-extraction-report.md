# Extraction Report — olander-2022-ed-ie-language-family

## Source identification

- Source file: `olander-2022-ed-ie-language-family.pdf`
- Source type: born-digital PDF with machine-readable text layer.
- Pages in source PDF: 316
- Extraction date: 2026-05-07
- Chunking: one Markdown file for front matter, one per chapter, one bibliography file per chapter with a References section, one index file, plus README, manifest, and extracted figure crops.

## Corrections applied

- Removed Cambridge Core download/terms footer text and running page headers/page numbers from extraction output.
- Rejoined paragraph line breaks and repaired many line-break hyphenations. Hyphenated compounds were preserved when the same hyphenated token appeared elsewhere in the source or matched common source-specific compound patterns.
- Repaired common Unicode ligatures from the text layer: `ﬁ`, `ﬂ`, `ﬀ`, `ﬃ`, `ﬄ`, `ﬅ`, and `ﬆ`.
- Normalized Unicode to NFC, preserving combining marks where no precomposed Unicode character exists.
- Converted text-layer laryngeal sequences `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃` because the PDF stores visually subscript laryngeal indices as baseline ASCII digits in many contexts.
- Repaired separated diaeresis in visible names where the text layer emitted `e¨`/`u¨` sequences, especially `Michaël` and `Kümmel`.
- Removed spacing before combining marks and some spacing after combining breve/candrabindu marks when they occurred inside technical forms.
- Extracted figure crops as PNGs and inserted Markdown image references at figure-caption locations.

## Unresolved issues list

- No `[unclear]` markers were inserted during this pass. This does not certify that all characters are correct.
- Figures are raster crops from vector/text diagrams. Crop boundaries were selected programmatically from page coordinates and should be visually checked if these figures will be used as archival image assets.
- Italic and bold formatting were partially preserved using inline HTML tags where the PDF font names exposed italic/bold distinctions. This pass did not attempt a full diplomatic style reconstruction.
- Tables were retained from the PDF text layer. Some dense tables may benefit from a later dedicated table-reconstruction pass if they are intended for structured data use.
- Line-break hyphenation repair is heuristic. A later pass could audit residual false joins or false retained hyphens in technical compounds.
- The index was extracted as text with one block/paragraph per surviving text block. A later index-specific pass could improve one-entry-per-line normalization and page-number alignment.
- Laryngeal conversion was applied globally for `h1`, `h2`, and `h3`. This is almost certainly correct for the technical notation in this source, but the pass did not manually verify every instance against page renderings.

## Confusion-pair report

- `h₁ h₂ h₃` vs. `h1 h2 h3`: normalization applied globally; not every instance manually verified.
- Macron vowels: NFC normalization applied; counts are included below. Some figure labels originally stored macrons as combining sequences or spacing macron artifacts and are preserved mainly in the raster images.
- Superscript modifier letters `ʰ` and `ʷ`: preserved where present in the text layer; not every instance manually verified.
- Schwa `ə`: preserved where present in text layer; not every instance manually verified.
- Underdotted Indic-style letters: preserved where present in text layer; not every instance manually verified.
- `ǵ`/`ḱ` and related palatal notation: preserved from text layer with NFC normalization; not every instance manually verified.
- Reconstruction asterisk `*`: preserved where present in text layer; not every instance manually verified.
- Dagger `†`: preserved where present in text layer; not every instance manually verified.

## Codepoint inventory

Approximate counts across generated Markdown corpus files:

```json
{
  "laryngeals": {
    "h1": 168,
    "h2": 280,
    "h3": 66
  },
  "macron_a": 423,
  "macron_e": 167,
  "macron_i": 144,
  "macron_o": 194,
  "macron_u": 88,
  "schwa": 82,
  "greek_chars": 3620,
  "combining_diacritics": 1061,
  "dagger": 5,
  "note": "All counts are approximate and for cross-pass comparison only."
}
```

## Structural integrity check

- Headings: chapter headings were generated from the source table of contents; numbered subsection headings were detected from extracted text and formatted as Markdown headings where possible.
- Footnotes: retained inline/as bottom-of-page text blocks according to the source text layer; not renumbered or converted to Markdown footnote syntax.
- Bibliographies: split into separate per-chapter bibliography files when a `References` heading was present.
- Page anchors: included as HTML comments with printed page and PDF page identifiers.
- Continuation text: page-boundary text was retained, but no exhaustive page-boundary audit was performed.
- Images: 18 figure crops were extracted into `images/`.

## Image inventory

| File | Source label | Page | Caption |
|---|---:|---:|---|
| `images/olander-2022-ed-ie-language-family-fig1-1.png` | Figure 1.1 | 5 | The “neo-traditional” model |
| `images/olander-2022-ed-ie-language-family-fig1-2.png` | Figure 1.2 | 6 | Binary-branching model (Ringe group) |
| `images/olander-2022-ed-ie-language-family-fig1-3.png` | Figure 1.3 | 6 | Binary-branching model (Gray group; Chang et al. 2015) |
| `images/olander-2022-ed-ie-language-family-fig2-1.png` | Figure 2.1 | 19 | Family tree of the ABC language family |
| `images/olander-2022-ed-ie-language-family-fig2-2.png` | Figure 2.2 | 20 | Schleicher’s tree diagram (Schleicher 1861: 7). |
| `images/olander-2022-ed-ie-language-family-fig4-1.png` | Figure 4.1 | 53 | Outgroup analysis of PGmc. *tūna- and PCelt. *dūn . . . |
| `images/olander-2022-ed-ie-language-family-fig5-1.png` | Figure 5.1 | 70 | The Luwic sub-branch of Anatolian |
| `images/olander-2022-ed-ie-language-family-fig5-2.png` | Figure 5.2 | 76 | Tree model of the Anatolian languages |
| `images/olander-2022-ed-ie-language-family-fig6-1.png` | Figure 6.1 | 89 | The position of Tocharian |
| `images/olander-2022-ed-ie-language-family-fig7-1.png` | Figure 7.1 | 109 | Tentative tree showing the position of Italo-Celtic |
| `images/olander-2022-ed-ie-language-family-fig8-1.png` | Figure 8.1 | 115 | The Italic languages |
| `images/olander-2022-ed-ie-language-family-fig9-1.png` | Figure 9.1 | 143 | The Celtic languages |
| `images/olander-2022-ed-ie-language-family-fig10-1.png` | Figure 10.1 | 160 | A tree model illustrating a binary split of Proto-Germanic into North-West vs. East Germanic |
| `images/olander-2022-ed-ie-language-family-fig10-2.png` | Figure 10.2 | 160 | A unified tree-wave model of the Germanic dialect continuum |
| `images/olander-2022-ed-ie-language-family-fig11-1.png` | Figure 11.1 | 190 | The Greek dialects |
| `images/olander-2022-ed-ie-language-family-fig12-1.png` | Figure 12.1 | 209 | The position of Armenian |
| `images/olander-2022-ed-ie-language-family-fig13-1.png` | Figure 13.1 | 241 | The position of Albanian |
| `images/olander-2022-ed-ie-language-family-fig14-1.png` | Figure 14.1 | 255 | The Indo-Iranian languages |
