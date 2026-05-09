---
title: "PIE > Celtic: implications of new evidence for an updated working hypothesis"
author: "John T. Koch"
date: 2025
source_type: born-digital
extraction_date: 2026-05-07
source_file: "koch-2025-pie-celtic-implications.pdf"
chunk: extraction-report
---

# Extraction report

## Source type

Born-digital PDF. The file has a machine-readable text layer; the raw extracted text was used as the primary input. Visual rendering and PDF HTML extraction were used only to verify or repair specialized glyphs, superscripts, and embedded figures.

## Corrections applied

- Removed running page-number markers and the initial word-count marker.
- Reflowed line-wrapped prose and repaired hyphenated line breaks where a word or compound was split across PDF lineation.
- Separated the end bibliography into `koch-2025-pie-celtic-implications-bibliography.md`.
- Extracted eight embedded figure images into `images/` and replaced manuscript figure placeholders with Markdown image references and captions.
- Corrected PDF text-layer glyph substitutions: `VȖ` → `V̆`; `Vȑ` → `V̄`; `porkǻos` → `porḱos`.
- Restored superscript/modifier-letter forms from PDF HTML/visual rendering: `*gw` → `*gʷ`; `anbaatiia` → `anbᵃatᶦia`; `tiirtoos` → `tᶦirtᵒos`; `taarnekukuun` → `tᵃarnekᵘkᵘun`.
- Converted the two printed endnote markers into Markdown footnotes, preserving the endnote text.
- Repaired two extraction-induced missing spaces around technical forms: `Indo-European*porḱos` → `Indo-European *porḱos`; `form*arganto-` → `form *arganto-`.
- Converted two bibliography instances of `M.a` with superscript `a` to `M.ª`.

## Unresolved issues list

- No `[unclear]` or `[?]` markers were inserted in the Markdown.
- The corrected `V̆` and `V̄` notation on the Proto-Celtic sound-law line was visually verified, but because it involved a text-layer glyph substitution, it remains a high-value target for a future character-fidelity pass.
- The `*porḱos` corrections were visually inferred from the rendered PDF and the zero-width glyph behavior in the PDF text layer. These should be rechecked in any later character-authoritative pass.
- Figure map labels were preserved as images rather than transcribed individually. A later figure-label audit could transcribe internal map labels if needed for full-text search.
- Italic/bold formatting was preserved selectively rather than exhaustively; the extraction prioritizes character fidelity and searchable clean text over fully diplomatic styling.

## Confusion-pair report

- **h₁ h₂ h₃:** No subscript-laryngeal instances detected in the output.
- **ā ē ī ō ū:** Macron counts approximate: ā=3, ē=9, ī=1, ō=4, ū=1.
- **ʰ ʷ:** One superscript w in *gʷ was restored from the PDF HTML/visual rendering. No superscript aspiration signs were detected; the source text appears to use *bh, *dh, *gh baseline notation.
- **ə:** No schwa instances detected.
- **ṛ ḷ ṃ ṇ:** No precomposed underdot Indic letters detected. Syllabic r/l are represented as r̥ and l̥ using combining ring below, following the PDF text layer.
- **ǵ ḱ:** Two source-layer mis-mapped instances of *porkǻos were corrected to *porḱos after visual inspection. No ǵ instances detected.
- ***:** Asterisks before reconstructed forms were retained as literal source characters.
- **†:** No dagger instances detected.

Residual suspicious patterns in the generated Markdown: none detected for the checked source-specific patterns.

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
  "macron_a": 3,
  "macron_e": 9,
  "macron_i": 1,
  "macron_o": 4,
  "macron_u": 1,
  "schwa": 0,
  "greek_chars": 62,
  "combining_diacritics": 7,
  "dagger": 0
}
```

## Structural integrity check

- Headings were normalized to Markdown headings for the article/chapter structure; a follow-up patch split headings that the first reflow pass had fused to following prose.
- Bibliography was separated from the main extraction and organized as one reference entry per paragraph using the PDF's hanging-indent line structure.
- The source has no index.
- The main text contains the acknowledgements and the two end notes; QC notes are confined to this report.
- The extracted figure images are referenced from the main Markdown file and listed in the manifest.
- No continuation text was intentionally omitted at page boundaries; several obvious page-boundary paragraph splits were repaired, but references and body paragraphs that continue over a page break should remain priority candidates for later QA.

## Image inventory

- Figure X.1 (p. 2): `images/koch-2025-pie-celtic-implications-figx-1.png` — Figure X.1. The distribution of the Ancient Celtic languages as attested by the evidence of inscriptions and references by the Greek and Roman authors, also showing the location of Keltoi ‘Celts’ according to Herodotus (§2.34 and §4.48). The areas with horizontal stripes are known to have received Celtic expansions during the La Tène period (mid 5th century BC onward), either from historical accounts and/or archaeology.
- Figure X.2 (p. 6): `images/koch-2025-pie-celtic-implications-figx-2.png` — Figure X.2. ‘Schematic Bell Beaker distribution in Europe’ (Heyd 2013, Fig.28)
- Figure X.3 (p. 8): `images/koch-2025-pie-celtic-implications-figx-3.jpg` — Figure X.3. Formative areas, as implied by dense genomic attestation, for the three migrations in the background of Celtic Europe (McColl et al. 2025b): 1) Bell Beaker in orange, 2) French/Iberian Bronze Age ancestry shown in yellow, and 3) the LBA Knovíz Urnfield Culture. The territory of the Argar Culture ~2200–1550 BC is marked with horizontal stripes.
- Figure X.4 (p. 11): `images/koch-2025-pie-celtic-implications-figx-4.png` — Figure X.4. An Indo-European family tree based on Ringe et al. 2002. The phenomena of Celto-Germanic and North-West Indo-European shared vocabulary are represented as reflecting layers of contact between separating branches.
- Figure X.5 (p. 15): `images/koch-2025-pie-celtic-implications-figx-5.png` — Figure X.5. Percentages of genetic outliers in southern Britain ~2450 BC–AD 43 from Patterson et al. 2022 with this author’s first-glance linguistic implications inserted.
- Figure X.6 (p. 21): `images/koch-2025-pie-celtic-implications-figx-6.jpg` — Figure X.6. Approximate dates for the adoption of high-tin bronze as the standard material for tools, weapons and ornaments (based on Pare 2000; cf. Koch 2013).
- Figure X.7 (p. 23): `images/koch-2025-pie-celtic-implications-figx-7.jpg` — Figure X.7. Places in Wales and the Marches mentioned in the chapter.
- Figure X.8 (p. 27): `images/koch-2025-pie-celtic-implications-figx-8.jpg` — Figure X.8. The Irulegi hand and a romanized edition of the engraved text.
