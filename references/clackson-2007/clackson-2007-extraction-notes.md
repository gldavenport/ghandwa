# clackson-2007 extraction notes — second and third passes

## Source

- Source PDF: `clackson-2007.pdf`
- Base extraction: first-pass Markdown from `clackson-2007-markdown-first-pass.zip`
- Second/third pass date: 2026-04-28

## Second pass: structural cleanup

Actions performed:

- Replaced the front-matter Contents, Figures, and Tables sections with clean Markdown lists.
- Removed ordinary front-matter page labels and the blank-page text marker where it carried no corpus value.
- Demoted 113 false Markdown headings caused by table/example line starts and accidental numeric headings, then repaired 9 broken table-heading joins identified by the heading audit.
- Normalized obvious Markdown inconsistencies and excessive blank-line runs.
- Preserved PDF page anchors as HTML comments because they remain useful for citation and later verification.
- Kept dense comparative tables primarily as line-oriented Markdown rather than forcing lossy table normalization.

## Third pass: character and scholarly-notation audit

Actions performed:

- Targeted the transliteration-conventions section first, since it contains the highest concentration of IPA and diacritic mapping errors.
- Repaired high-confidence glyphs including IPA [ɟ], [ʒ], [ɫ], [ɖ], [ɦ], [ɲ], [ɨ], vowel-length [ː], ogonek vowels, ḫ, and ṛ/r̩.
- Repaired recurring high-value names where the PDF text layer dropped a special character, especially Kuryłowicz, Möller, and Szemerényi.
- Created `clackson-2007-character-audit.md` with remaining uncertainty markers and line contexts.
- Created `clackson-2007-heading-audit.md` and `clackson-2007-table-exercise-audit.md` as future cleanup aids.

## Remaining limitations

- This is now substantially cleaner than the first pass, but it is still not a fully hand-verified edition.
- Some comparative tables remain line-oriented because the source PDF uses dense scholarly tables and custom fonts.
- Fourth pass supersedes the third-pass uncertainty count; bracketed uncertainty markers were resolved or removed as artifacts where source checks allowed.
- A full bibliography-normalization pass would still add value, but the original bibliography has been preserved in the main Markdown rather than silently regularized.

## Further-pass recommendation

No broad fourth pass is necessary for ordinary corpus use. A narrow fourth pass would add value only if you want exact searchable lexical forms from the tables and indexes; that pass should target the remaining uncertainty markers and the Word Index rather than rereading the whole book.


## Fourth pass note

A fourth character-fidelity pass was applied after the second/third-pass package. The goal was not broad table reconstruction, but maximal restoration of special characters in the existing clean Markdown. The pass used: PDF text-layer extraction, PyPDF glyph-name output such as `/underring` and `/halfringleftsubscript`, and selected rendered page images for high-value uncertain forms.

Bracketed uncertainty markers from the third pass were resolved or removed when they were page-artifacts rather than recoverable characters. The remaining limitation is not unresolved bracketed glyphs, but the inherited line-oriented structure of several dense tables and index pages.
