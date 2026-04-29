# Extraction notes for anthony-2023

## Passes completed

1. **First extraction:** extracted the PDF text layer into Markdown, removed printed line numbers, page numbers, and running headers, and added YAML front matter.
2. **Second pass:** repaired section structure, footnote placement, page-boundary continuations, paragraph joins, and common line-break hyphenation artifacts.
3. **Third pass:** audited reconstructed forms, combining diacritics, laryngeal notation, non-ASCII names, and bibliography-heavy sections.
4. **Additional targeted pass:** created a companion extracted-form list because the article contains a compact but high-value set of reconstructed PIE/LPIE forms.
5. **Bibliography pass:** rebuilt the references section as one reference per paragraph, removed page anchors from inside the bibliography, added source-style and expanded-author bibliography companions, and documented source-internal citation mismatches.

## Further-pass assessment

For ordinary corpus use, the current extraction should be sufficient. The bibliography is now cleaned for readability and lookup. A further pass would add value mainly if the goal is to resolve source-internal mismatches through external bibliographic checking or to convert the bibliography to CSL JSON/BibTeX.

## Known limitations

- Italic/bold font styling was not systematically reconstructed from the PDF text layer.
- The bibliography has been normalized for Markdown readability but not converted into a formal citation database.
- Source-internal citation mismatches are documented in `anthony-2023-bibliography-audit.md` rather than silently corrected.
- Hidden page anchors are retained as HTML comments in the body where they do not interrupt words or sentences; bibliography-internal page anchors were removed for readability.
