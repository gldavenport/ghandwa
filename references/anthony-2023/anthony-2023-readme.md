# anthony-2023 Markdown extraction package

This package contains a clean, corpus-ready Markdown extraction of David W. Anthony's 2023 article “Ten Constraints that Limit the Late PIE Homeland to the Steppes.”

## Files

- `anthony-2023.md` — main clean Markdown extraction, now with the bibliography normalized to one reference per paragraph.
- `anthony-2023-extracted-forms.md` — companion list of reconstructed forms and glosses.
- `anthony-2023-bibliography-source-style.md` — cleaned source-style bibliography with repeated-author dashes preserved.
- `anthony-2023-bibliography-normalized.md` — lookup-oriented bibliography with repeated-author dashes expanded.
- `anthony-2023-bibliography-audit.md` — notes on bibliography cleanup and unresolved source-internal citation mismatches.
- `anthony-2023-extraction-notes.md` — pass history, limitations, and further-pass assessment.

## Extraction approach

The PDF text layer was used as the base. Printed line numbers, page numbers, and running headers were removed. Page anchors were retained as hidden HTML comments where they did not interrupt words or sentences; in the bibliography, internal page-anchor comments were removed during the bibliography pass because they interrupted reference-list readability.

The extraction was cleaned for structure, paragraph joins, page-boundary continuations, line-break hyphenation artifacts, reconstructed forms, and bibliography readability.
