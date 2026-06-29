---
title: "Extraction report: The phonology, phonetics, and diachrony of Sturtevant’s Law"
author: "Anthony D. Yates"
date: 2019
source_type: "born-digital PDF article"
extraction_date: 2026-05-26
source_file: "yates-2019-phonology-phonetics-diachrony.pdf"
---

# Extraction report: Yates 2019, "The phonology, phonetics, and diachrony of Sturtevant’s Law"

## Source assessment

- **Source type:** born-digital PDF article.
- **Length:** 67 PDF pages, journal pages 241–307.
- **Text-layer quality:** mostly reliable for ordinary prose and Greek, but not character-authoritative for all linguistic notation. The Brill font text layer extracts visible subscript laryngeal digits as baseline `h1`, `h2`, `h3`.
- **Layout complexity:** single-column scholarly article with many numbered examples, rule statements, feature notation, OT tableaux, footnotes, and a bibliography.
- **High-risk zones:** reconstructed PIE/Anatolian forms, laryngeals, Greek, phonological feature matrices, OT tableaux, and bibliography entries.

## Corrections and normalization applied

- Removed repeated running headers, journal footer, page numbers, Brill download stamps, and repeated access lines.
- Reconstructed article-level Markdown hierarchy: title, abstract, keywords, numbered sections/subsections, footnotes, and references.
- Preserved complex examples, rules, and tableaux as fenced text blocks where Markdown table syntax would risk mangling notation or alignment.
- Reflowed ordinary prose, footnotes, and bibliography entries while repairing line-break hyphenation.
- Moved extracted footnotes into a consolidated `## Footnotes` section before the bibliography, so page-bottom notes do not interrupt body paragraphs.
- Added YAML front matter with source metadata.

## Character-risk assessment

The embedded text layer was not treated as character-authoritative for laryngeal notation. Visual comparison was made against pages with dense notation and tableaux, including pages 3, 5, 6, 39, and 42. The recurring confirmed problem was font/ToUnicode flattening of laryngeal subscript digits.

## Source-specific glyph and confusion map

- Extracted `h1`, `h2`, `h3` corrected to `h₁`, `h₂`, `h₃` where the visible PDF uses subscript laryngeal digits.
- Other notation such as `kw`, `gw`, `bh`, `dh`, and `gh` was preserved as extracted unless corrected by the laryngeal rule. This avoids over-normalizing the author’s notation into a different convention.
- Greek characters and diacritics appeared substantially reliable in sampled pages and were preserved from the text layer.
- Phonological symbols such as `χ`, `ʁ`, `ɡ`, `ː`, `ə`, `ʔ`, `∅`, `→`, `⇐`, `☞`, `⟨ ⟩`, and combining marks were preserved where present in the text layer.

## Linguistics QC checks performed

- Laryngeal search for residual baseline `h1`, `h2`, `h3`.
- Search for replacement characters and form feeds.
- Search for Brill download/footer artifacts.
- Visual spot-checks of dense notation pages and OT-tableau pages against rendered PDF images.
- Bibliography parsing and page-furniture removal check.
- Footnote continuity check for missing note numbers.

## QC search results

```json
{
  "replacement_char": 0,
  "baseline_h1": 0,
  "baseline_h2": 0,
  "baseline_h3": 0,
  "spaced_h_subscript": 0,
  "unclear_markers": 0,
  "downloaded_stamp": 0,
  "via_free_access": 0,
  "form_feeds": 0,
  "remaining_footer_lines": 0,
  "footnotes_extracted": 82,
  "missing_footnote_numbers": [],
  "reference_entries_estimate": 161
}
```

## Unresolved issues and cautions

- This is suitable for ordinary corpus search and AI parsing.
- It should not be treated as character-authoritative for quotation of a specific reconstructed form until that form is checked against the PDF image or a reliable text layer.
- Italics were not exhaustively converted to Markdown backticks for every cited form. The extraction prioritizes character fidelity and logical/searchable structure over full typographic reconstruction.
- Some complex tableaux are preserved as fenced text blocks rather than fully normalized Markdown tables; this better protects the notation but may not be ideal for tabular data extraction.
- Because the PDF text layer flattens some glyph information, superscript/modifier notation beyond laryngeal subscripts may still need targeted verification before derivational use.

## Targeted laryngeal-notation cleanup pass

Performed a focused pass for residual baseline or spaced laryngeal notation after the initial extraction. The pass searched the main Markdown for `h1`, `h2`, `h3`, `h 1`, `h 2`, and `h 3`, then corrected only linguistic-form contexts supported by the source PDF extraction pattern.

Corrections applied:

- Corrected seven residual spaced laryngeals in PIE forms from `h 1` to `h₁`.
- Left non-linguistic `h + digit` sequences in bibliography/reference prose untouched, e.g. journal titles such as *Language and Speech 29 (1)*.
- Re-ran laryngeal QC searches after correction.

Updated laryngeal QC results:

```json
{
  "baseline_h1": 0,
  "baseline_h2": 0,
  "baseline_h3": 0,
  "spaced_laryngeal_h1_actual_contexts": 0,
  "spaced_laryngeal_h2_actual_contexts": 0,
  "spaced_laryngeal_h3_actual_contexts": 0,
  "subscript_h1": 26,
  "subscript_h2": 33,
  "subscript_h3": 14,
  "all_subscript_laryngeals": 73,
  "generic_h_space_digit_remaining": 7
}
```

Remaining generic `h\s+[123]` hits are bibliography/reference artifacts, not laryngeal notation.

## Further-pass recommendation

A targeted second pass would add value if this extraction will be used for direct quotation or derivational work. The highest-value pass would be a form-notation audit over all numbered examples and tableaux, checking laryngeals, possible modifier/superscript notation, palatovelar notation, syllabic resonants, and bracket/slash notation against the rendered PDF.
