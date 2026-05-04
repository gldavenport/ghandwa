# Palmér et al. 2021 extraction package

Files:

- `palmer-et-al-2021-proto-indo-european-fox.md` — main clean Markdown extraction.
- `palmer-et-al-2021-extracted-forms.md` — selected companion form index for search/corpus navigation.
- `palmer-et-al-2021-third-pass-audit.md` — notes on the additional audit pass.
- `palmer-2021-raw-pdftotext-layout.txt` — raw text-layer extraction retained for audit.

Pass notes:

1. First pass: text-layer extraction from the born-digital PDF.
2. Second pass: removed running headers, page numbers, download footer, and decorative layout; added YAML front matter; repaired major line-break and hyphenation artifacts; converted small paradigm/table blocks to Markdown tables; preserved footnotes as Markdown footnotes.
3. Targeted character audit: spot-checked principal reconstructed forms, Greek forms, laryngeals, ḱ, accented vowels, bibliography start/end, small tables, and footnote preservation against rendered PDF pages.
4. Third pass: repaired residual heading/citation punctuation artifacts, combining-mark splits, Section 4.1 list structure, high-value reconstructed forms, and companion-index status.

Remaining limitations:

- The PDF text layer encodes typographic small caps as lowercase in many places; the main extraction generally preserves those text-layer abbreviations rather than forcing global normalization.
- Italics are not exhaustively encoded because doing so would reduce readability and can interfere with search over reconstructed forms.
- A further pass could improve exhaustive typographic markup and catch residual hyphenation artifacts in the bibliography, but the current file should be usable for corpus search and linguistic reference. A final targeted patch repaired inline footnote blocks and restored the References heading.
