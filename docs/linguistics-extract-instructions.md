Extract this source to clean, corpus-ready Markdown.

> *Character fidelity is the primary constraint. Structure is secondary. When they conflict, preserve the character.*

Do not summarize unless explicitly asked. Extract and transcribe the source text into clean Markdown.

---

## Source type

Identify the source type before proceeding:

- **Born-digital PDF (machine-readable text layer present):** The raw extracted text — not the visual rendering — is the primary input. Treat visual inference as a fallback only for characters the text layer cannot resolve (corrupted glyphs, figures, tables rendered as images).
- **Scanned-only PDF:** Character inference from visual rendering is required. Flag this at the top of the extraction report, and flag every character that required inference with `[?]` inline.

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

---

## Structure

- Preserve the source's logical structure: title, author/source metadata, sections, subsections, lists, tables, quotations, notes, captions, appendices, bibliography, indexes, and lexical entries.
- Prioritize intellectual structure over visual layout. Ignore columns, page geometry, running headers, footers, page numbers, catchwords, blank pages, and decorative layout.
- **Exception:** Multi-column layouts that carry semantic meaning (e.g., cognate comparison tables, parallel text, side-by-side paradigms) should be preserved as Markdown tables, not collapsed into prose.
- Preserve meaningful formatting: italics, bold, small caps, underlining, block quotations, captions, footnotes/endnotes, and source-critical notation where they affect interpretation.
- Preserve dense paradigms, sound-law tables, forms lists, abbreviation lists, and lexical datasets in readable Markdown tables or fenced blocks when prose Markdown would damage the structure.
- For indexes and Index Verborum sections, preserve one headword entry per line. Do not collapse multiple entries onto a single line or reformat entry-page-number alignment; collapsing introduces drop risk for diacritics in dense entries.
- Keep page anchors or source-location markers where useful for later citation or source-critical checking.
- Use readable headings and consistent Markdown structure even when the source is visually irregular.

---

## OCR and scanned sources

- Correct obvious OCR errors while preserving original wording, spelling, notation, and meaning.
- Reconstruct paragraphs, headings, lists, quotations, footnotes/endnotes, captions, tables, and lexical entries for readability.
- Repair broken lineation, hyphenation across line breaks, column-order problems, page-boundary breaks, and split words.
- Remove OCR artifacts, repeated running headers/footers, page numbers, scanning noise, duplicated continuation text, stray control characters, and corrupted markup.
- Preserve original spelling, archaic usage, transliteration, scholarly notation, and technical terminology; do not modernize or silently normalize.
- If a word, character, name, form, date, citation, or passage is unreadable or uncertain, mark it with `[unclear]` or a short bracketed note rather than guessing.
- If charts, images, maps, plates, figures, stemmata, diagrams, or photo-only pages appear, include accessible descriptions rather than interpretive summaries.
- If tables, paradigms, indexes, or lexical entries are too damaged to reconstruct confidently, preserve readable content and add a brief note explaining the uncertainty.

---

## YAML front matter

Add YAML front matter to the main Markdown file containing basic source metadata only. QC notes and corrections belong in the extraction report, not here.

```yaml
title:
author:
date:
source_type:          # born-digital | scanned | mixed | unknown
extraction_date:
source_file:
```

---

## Deliverables

Every extraction produces a ZIP containing exactly three files:

### 1. `{source}.md` — Main extraction

Clean corpus-ready Markdown with YAML front matter. No QC content, no correction notes, no unresolved-issues lists. This file is the corpus deliverable.

### 2. `{source}-extraction-report.md` — Extraction report

Human-readable QC record. Include:

**Corrections applied.** List corrections made (e.g., ligature repairs, laryngeal normalization, paragraph rejoins). Be specific about what was changed and how.

**Unresolved-issues list.** Enumerate every location where a character, form, or passage required inference, guessing, or produced uncertainty. This list is for human review. Do not suppress uncertain items.

**Confusion-pair report.** For each item in the known high-risk confusion table, report: (a) any instances in the output that may be wrong, and (b) any that could not be verified. Do not claim the list was fully checked.

**Codepoint inventory.** Report approximate counts for cross-pass comparison. Label all counts as approximate.

**Structural integrity check.** Note whether headings are consistent, footnotes are attached, tables are well-formed, and no continuation text appears lost at page boundaries.

The QC pass cannot catch errors made consistently throughout the extraction. Do not assert correctness. Assert uncertainty.

### 3. `manifest.json` — Machine-readable metrics

```json
{
  "source_file": "",
  "source_type": "",
  "extraction_date": "",
  "output_files": [],
  "corrections_applied": {
    "ligature_repairs": "count or unknown",
    "laryngeal_normalization": "applied | not applied | unknown",
    "paragraph_rejoins": "count or unknown"
  },
  "markers_inserted": {
    "unclear": 0,
    "inferred_char": 0
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

All counts in `approximate_counts` are approximate. Their value is detecting regressions between passes, not certifying accuracy. Add source-specific fields as needed.

---

Use kebab-case filenames throughout.
