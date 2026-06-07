# Extraction report: Ringe 1996 Tocharian

## Source type

Scanned-only PDF. The extraction was made from embedded page-scan images; no machine-readable text layer was available for direct extraction.

## Process

- Extracted the PDF's embedded page images.
- Cropped page images to text-bearing regions where possible.
- Ran OCR with Tesseract English at the page level.
- Re-ran failed/empty OCR pages manually where the page was not blank.
- Removed obvious running headers and page-only lines in chunk files.
- Repaired obvious line-break hyphenation in prose where a lower-case word was split across a line break.
- Chunked the monograph by the source's own chapters, with bibliography and indexes as separate files.
- Added PDF-page and printed-page anchors as HTML comments.

## Corrections applied

- Ligature repairs: unknown; handled only where OCR emitted ordinary characters.
- Laryngeal normalization: not applied. The source uses Ringe's own notation; OCR treatment of laryngeal-related symbols and superscripts is not reliable enough for silent normalization.
- Paragraph rejoins: partial. Hyphenated line-break repairs were applied conservatively; prose lineation remains closer to OCR line output than to a fully reflowed edition.
- Running headers/footers: obvious running headers and page-only lines were removed where detected.

## Unresolved issues

- This is a first-pass OCR extraction from a scanned source. Technical forms, Tocharian transcription, PIE reconstructions, Sanskrit/Greek material, superscripts, subscripts, macrons, breve-like marks, and index entries remain high-risk.
- The instruction to mark every visually inferred scanned character with `[?]` was not applied literally because every character in a scanned-only PDF is visually inferred; applying `[?]` after every character would make the corpus unusable. `[?]` is therefore not a comprehensive inference marker in this pass.
- Dense tables, sound-law lists, the contents pages, abbreviations, and the four indexes need visual second-pass checking.
- Italics, small caps, and other typography are mostly not preserved by this OCR pass.
- Some source page images that are blank separator pages were intentionally omitted from chunk text.
- No claim is made that the character inventory is correct. The counts below are only regression-check aids.

## Confusion-pair report

Not fully checked. Known high-risk confusions remain, especially:

- subscript/superscript notation vs. baseline ASCII characters;
- macron vowels vs. unmarked vowels;
- schwa-like symbols vs. e, a, o, or numerals;
- Tocharian letters such as ñ, ś, ṣ, ä, and related OCR approximations;
- Greek letters misread as Latin lookalikes;
- asterisk/dagger/prime marks and quotation marks;
- dense index headwords and page references.

## Codepoint inventory (approximate)

```json
{
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
}
```

## Structural integrity check

- Output is chunked by the book's major source structure: front matter/introduction, Chapters 1-10, bibliography, and indexes.
- Bibliography and indexes are separate from the main chapter files.
- Page anchors are included as comments before extracted page text.
- Headings are partially normalized, but numbered section headings should be checked against the contents during a second pass.
- Tables and paradigms were not fully reconstructed into Markdown tables in this pass; they are preserved primarily as OCR line blocks.
- Footnote attachment is uncertain and should be checked visually in a second pass.

## Image inventory

No non-page figure, map, plate, or diagram files were extracted. The PDF consists of scanned page images; no separate content figures were identified in this pass.
