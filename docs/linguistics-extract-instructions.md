Extract this source to clean, corpus-ready Markdown.

> *Character fidelity is the primary constraint. Structure is secondary. When they conflict, preserve the character.*

Do not summarize unless explicitly asked. Extract and transcribe the source text into clean Markdown. Use kebab-case filenames throughout.

---

## Source type

Identify the source type before proceeding:

- **Born-digital PDF (machine-readable text layer present):** The raw extracted text — not the visual rendering — is the primary input. Treat visual inference as a fallback only for characters the text layer cannot resolve (corrupted glyphs, figures, tables rendered as images).
- **Scanned-only PDF:** Character inference from visual rendering is required. Flag this at the top of the extraction report, and flag every character that required inference with `[?]` inline. For image handling, see the Images section below.
- **EPUB:** The source is a structured archive with an embedded HTML text layer and discrete image files. The text layer is always machine-readable; use it directly. Images are already discrete files within the EPUB's internal directory structure. For image handling, see the Images section below.

If source type is uncertain, note it in the extraction report and treat the source as scanned.

---

## Character fidelity

Exact characters, diacritics, reconstructed forms, Greek, IPA, laryngeals, and scholarly notation take priority over all other concerns. Structure, layout, and readability are secondary.

- Preserve the author's notation system without silent normalization: PIE, Proto-Celtic, Proto-Germanic, Proto-Italic, Sanskrit, Greek, Gothic, Old Irish, Old Norse, Latin, and all other languages and scripts.
- Preserve distinctions among asterisks, daggers, superscripts, subscripts, macrons, breves, acute/grave/circumflex accents, underdots, over-rings, aspiration marks, syllabic markers, palatalization marks, and laryngeal indices.
- Do not normalize technical notation, phonological symbols, accent marks, vowel length, root notation, inflectional labels, segmented morphology, or etymological conventions.
- For etymological dictionaries or lexical studies, preserve headwords, reconstructed forms, glosses, language labels, derivational notes, cognate sets, bibliography keys, cross-references, and index references with special care.

**Known high-risk confusions — verify each:**

| Correct | Wrong |
|---|---|
| h₁ h₂ h₃ (U+2081–2083, subscript digits) | h1 h2 h3 (ASCII digits) |
| ā ē ī ō ū (precomposed macrons) | a + combining macron U+0304 (unless source uses decomposed) |
| Macron vowels consistent across body text, footnotes, and index sections | Macron silently dropped in dense or reformatted sections (indexes, paradigm tables, reference lists) |
| ʰ ʷ (U+02B0, U+02B7 superscript modifier letters) | h w |
| ə (U+0259 schwa) | e or 9 |
| ṛ ḷ ṃ ṇ (underdot, e.g. U+1E5B) | r l m n |
| ǵ ḱ (precomposed acute on consonant) | g' k' or g´ k´ |
| * (asterisk U+002A before reconstructed forms) | ✱ × or absent |
| † (dagger U+2020, unattested or uncertain) | + or absent |

This list covers common confusions for Indo-European linguistics sources. Add source-specific confusions as they are identified. When a character required visual inference rather than direct reading, flag it with `[?]` inline.

Laryngeal normalization must apply within inline HTML markup spans (`<i>`, `<em>`, `<b>`, `<sup>`, `<sub>`) as well as plain text. Do not skip normalization because a form is italicized.

---

## Structure

- Preserve the source's logical structure: title, author/source metadata, sections, subsections, lists, tables, quotations, notes, captions, appendices, and lexical entries. Bibliographies and indexes are extracted as separate files; see Deliverables.
- Prioritize intellectual structure over visual layout. Ignore columns, page geometry, running headers, footers, page numbers, catchwords, blank pages, and decorative layout.
- **Exception:** Multi-column layouts that carry semantic meaning (e.g., cognate comparison tables, parallel text, side-by-side paradigms) should be preserved as Markdown tables, not collapsed into prose.
- Preserve meaningful formatting: italics, bold, small caps, underlining, block quotations, captions, footnotes/endnotes, and source-critical notation where they affect interpretation.
- Preserve dense paradigms, sound-law tables, forms lists, abbreviation lists, and lexical datasets in readable Markdown tables or fenced blocks when prose Markdown would damage the structure.
- For indexes and Index Verborum sections, preserve one headword entry per line. Do not collapse multiple entries onto a single line or reformat entry-page-number alignment; collapsing introduces drop risk for diacritics in dense entries.
- Keep page anchors or source-location markers where useful for later citation or source-critical checking.
- Use readable headings and consistent Markdown structure even when the source is visually irregular.

### Chunking

A single large Markdown file is unwieldy for navigation and reference lookup. Apply the following rules based on source type:

| Source type | Threshold | Default granularity |
|---|---|---|
| Running prose monograph | > 100 pages | One file per chapter |
| Running prose monograph | Any chapter > 50 pages | Split that chapter at its top-level numbered sections |
| Etymological dictionary | Any length | One file per letter section (A, B, C…) |
| Journal article or book chapter | Any length | Single file |

**Bibliography and index are always separate files** regardless of source type, length, or whether the rest of the work is chunked:

- If the work has a single end bibliography: `{source}-bibliography.md`
- If bibliographies appear per-section (per chapter, per part, per letter, or any other division): produce one bibliography file per section, named to match the section identifier used for that chunk — e.g., `{source}-bibliography-{chunk}.md`. Use whatever chunk label the source provides; do not impose chapter-specific naming if the source uses a different division.
- If the work has both per-section bibliographies and a master bibliography: produce both
- If references appear only as footnotes with no bibliography section, keep them inline; do not produce a bibliography file
- Index: `{source}-index.md` if present; omit if the source has no index

**Matching the source's own sectioning:** Use the source's actual chapter and section labels as the basis for chunking and filenames wherever possible. If the source labels sections as §2.1, §2.2, §2.3, use those labels. If it uses named subsections (e.g., "2.3 The Laryngeals," "2.4 The Stops"), use those names. Do not impose an arbitrary structure; mirror the source's hierarchy. If a chapter has no internal numbered sections, treat it as a single file regardless of length.

**Secondary splits:** If a top-level section is itself very long (> 30 pages), split at the next level of the source's own hierarchy (e.g., §2.3.1, §2.3.2). Do not split below the source's own labeled divisions.

**Filenames for chunked outputs** should reflect the source's labels:
- Chapter-level: `{source}-ch2.md`, `{source}-ch3.md`
- Section-level within a chapter: `{source}-ch2-sec2-3.md` (for §2.3)
- Letter-section for dictionaries: `{source}-letter-a.md`, `{source}-letter-b.md`
- Per-section bibliography: `{source}-bibliography-{chunk}.md`, where `{chunk}` matches the section identifier used for the corresponding content file

For chunked outputs:
- Each file gets its own YAML front matter including `chunk:` and `pages:` fields.
- All chunked outputs require a `README.md` index listing every output file with its title, source label (chapter/section number as it appears in the book), page range, and section coverage.
- The README is part of the ZIP alongside the extraction report and manifest.
- Do not mix QC content into chapter or section files. All QC belongs in the extraction report only.

---

## Images

Extract all figures, diagrams, tables rendered as images, stemmata, maps, and plates into a subdirectory named `images/` within the ZIP.

**EPUB sources:** Images are already discrete files inside the EPUB archive. Copy them directly from the EPUB's internal image directory into `images/`. Rename using the shared conventions below; do not re-encode or recompress.

**EPUB inline character glyphs:** Some EPUBs store individual characters as inline PNG images rather than Unicode — typically rare or composed characters the publisher could not encode. These are distinct from figures and tables; they appear embedded in running text and linguistic forms. When encountered:
- If the character has a Unicode equivalent (e.g., `i_Mac.png` → ī, `u_Mac.png` → ū, `teta.png` → θ), substitute the Unicode character directly and record the substitution.
- If no Unicode equivalent exists (e.g., ε̃, æ̃, ə̆), preserve the image reference and add a `[image-glyph: description]` annotation inline.
- List all substitutions and unresolvable instances in the extraction report under a dedicated image-glyph inventory.

If binary image copying is unavailable in the extraction environment, use the fallback placeholder format in the Markdown body:

```
[image-only {type}: {source_filename}] Caption text
```

where `{type}` is one of `figure`, `table`, `map`, `plate`, or `other`, and `{source_filename}` is the EPUB-internal filename (e.g., `c03t001.jpg`). When using this fallback, include a complete image inventory in the extraction report (see Extraction report contents below).

**PDF sources (born-digital or scanned):** Extract embedded images where possible. For scanned sources where figures are part of the page image rather than discrete embedded objects, rasterize the relevant page region and save as PNG. If a figure cannot be extracted cleanly, use the standard unavailable placeholder below.

**Shared conventions for all source types:**
- Filename: `{source}-fig{N}.ext` where N is the figure number as labeled in the source (e.g., `ringe-2017-fig3-2.png`). If the source does not number figures, use `{source}-p{page}-fig{n}.ext`.
- In the Markdown file, use `![Figure 3.2: Caption text](images/{filename})` at the image location. Preserve the source's caption text exactly. Use the standard `![]()` reference only when the image file exists in `images/`; use the `[image-only...]` fallback when it does not.
- If an image cannot be extracted cleanly, insert: `![Figure N: Caption](images/unavailable)` followed by a bracketed note describing what the figure contains based on surrounding text and any visible content.
- List all extracted images in the manifest under `"images"` with filename, source figure label, page, and caption. Omit the `"images"` key or use `[]` if the source has no images.

---

## OCR and scanned sources

- Correct obvious OCR errors while preserving original wording, spelling, notation, and meaning.
- Reconstruct paragraphs, headings, lists, quotations, footnotes/endnotes, captions, tables, and lexical entries for readability.
- Repair broken lineation, hyphenation across line breaks, column-order problems, page-boundary breaks, and split words.
- Remove OCR artifacts, repeated running headers/footers, page numbers, scanning noise, duplicated continuation text, stray control characters, and corrupted markup.
- Preserve original spelling, archaic usage, transliteration, scholarly notation, and technical terminology; do not modernize or silently normalize.
- If a word, character, name, form, date, citation, or passage is unreadable or uncertain, mark it with `[unclear]` or a short bracketed note rather than guessing.
- For image-only figures, maps, and plates in scanned sources, see the Images section above.
- If tables, paradigms, indexes, or lexical entries are too damaged to reconstruct confidently, preserve readable content and add a brief note explaining the uncertainty.

---

## YAML front matter

Add YAML front matter to each Markdown file containing basic source metadata only. QC notes and corrections belong in the extraction report, not here.

For single-file extractions and standalone files (bibliography, index):

```yaml
title:
author:
date:
source_type:          # born-digital | scanned | mixed | unknown
extraction_date:
source_file:
chunk:                # bibliography | index | omit for single-file main text
```

For chunked extractions, add to each content file:

```yaml
title:
author:
date:
source_type:
extraction_date:
source_file:
chunk:                # source label as it appears in the book, e.g., "Chapter 2" or "§2.3"
pages:                # e.g., 45-112
```

For per-section bibliography files, use `chunk: bibliography-{chunk}` where `{chunk}` matches the section identifier of the corresponding content file.

---

## Deliverables

Every extraction produces a ZIP.

**Single-file extraction (articles, short monographs):**
1. `{source}.md` — clean corpus Markdown (main text only)
2. `{source}-bibliography.md` — if a bibliography section is present
3. `{source}-index.md` — if an index is present
4. `{source}-extraction-report.md` — QC record
5. `manifest.json` — machine-readable metrics
6. `images/` — subdirectory of extracted figures (omit if source has no images)

**Chunked extraction (long monographs, etymological dictionaries):**
1. `{source}-{chunk}.md` per chapter or letter section — clean corpus Markdown, one file each
2. `{source}-bibliography.md` and/or `{source}-bibliography-{chunk}.md` — per bibliography structure
3. `{source}-index.md` — if an index is present
4. `README.md` — index of all output files with source labels, page ranges, and section coverage
5. `{source}-extraction-report.md` — single QC record covering the whole extraction
6. `manifest.json` — machine-readable metrics; `output_files` lists all files
7. `images/` — subdirectory of extracted figures (omit if source has no images)

The main extraction files must be clean corpus Markdown only. No QC content, no correction notes, no unresolved-issues lists anywhere except the extraction report.

### Extraction report contents

**Corrections applied.** List corrections made (e.g., ligature repairs, laryngeal normalization, paragraph rejoins). Be specific about what was changed and how.

**Unresolved-issues list.** Enumerate every location where a character, form, or passage required inference, guessing, or produced uncertainty. This list is for human review. Do not suppress uncertain items.

**Confusion-pair report.** For each item in the known high-risk confusion table, report: (a) any instances in the output that may be wrong, and (b) any that could not be verified. Do not claim the list was fully checked.

**Codepoint inventory.** Report approximate counts for cross-pass comparison. Label all counts as approximate.

**Structural integrity check.** Note whether headings are consistent, footnotes are attached, tables are well-formed, and no continuation text appears lost at page boundaries.

**Image inventory** (required when the `[image-only...]` fallback format was used): complete list of every placeholder with source filename, type, chapter or page location, and caption. This inventory is the canonical reference for later image collation.

The QC pass cannot catch errors made consistently throughout the extraction. Do not assert correctness. Assert uncertainty.

### Manifest schema

```json
{
  "source_file": "",
  "source_type": "",
  "extraction_date": "",
  "output_files": [],
  "images": [
    {
      "filename": "",
      "source_label": "",
      "page": 0,
      "caption": ""
    }
  ],
  "corrections_applied": {
    "ligature_repairs": "count or unknown",
    "laryngeal_normalization": "applied | not applied | unknown",
    "paragraph_rejoins": "count or unknown"
  },
  "markers_inserted": {
    "unclear": 0,
    "inferred_char": 0,
    "image_glyphs_substituted": 0,
    "image_glyphs_unresolved": 0
  },
  "approximate_counts": {
    "note": "All counts are approximate and for cross-pass comparison only.",
    "laryngeals": {
      "h1": 0,
      "h2": 0,
      "h3": 0
    },
    "macron_a": 0,
    "macron_e": 0,
    "macron_i": 0,
    "macron_o": 0,
    "macron_u": 0,
    "schwa": 0,
    "greek_chars": 0,
    "combining_diacritics": 0,
    "dagger": 0
  },
  "unresolved_count": 0,
  "notes": ""
}
```

Omit the `"images"` key or use `[]` if the source has no images. All counts in `approximate_counts` are approximate; their value is detecting regressions between passes, not certifying accuracy. Add source-specific fields as needed.
