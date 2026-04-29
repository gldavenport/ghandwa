# Character-audit notes for clackson-2013

## Pass purpose

This pass focused on high-risk character fidelity issues rather than general prose cleanup. It targeted inscriptional forms, reconstructed forms, diacritics, dotless-i notation, laryngeal notation, labialized velars, voiced aspirates, and bibliography accents.

## Corrections applied

- Rechecked high-density linguistic sections against rendered page images, especially sections 3.2.1, 3.3.2-3.3.4, and 3.5.2-3.5.6.
- Fixed remaining page-break seams that interrupted paragraphs or headings.
- Removed remaining obvious page-break seams where PDF page boundaries split a continuous sentence or paragraph.
- Corrected several South Picene/Oscan/Umbrian forms and reconstructed forms, including `iúkúh:ko`, `lúvkis`, `*gʷītām`, `*kom-gʷened`, `*dhēsnā-`, and `kduú`.
- Corrected the South Picene 3PL marker from `-üh` to `-úh`.
- Regularized selected reconstructed voiced aspirates with Unicode superscript `ʰ` where the source uses raised `h` notation, for example `*dʰ`, `*bʰ`, `*gʰ`, `*medʰyo-`, `*rudʰro-`, and `*gʰortos`.
- Fixed obvious bibliography extraction artifacts including `Harrassowitz`, `Einleitung und Quellen`, `lingüístico`, `nç-/-nś`, and `ō-perfect`.
- Added `normalized-bibliography.md` as a companion file while preserving the main bibliography in the article Markdown.

## Remaining limitations

- The result is still clean Markdown, not diplomatic transcription.
- Some source-level typographic distinctions, especially italics and small caps, are not exhaustively represented because the embedded text stream does not reliably preserve styling.
- A publication-grade audit would require checking every line against rendered page images. This pass instead targeted high-risk forms and the bibliography.

## Recommendation

For corpus use, this fifth-pass package is the best stopping point unless the article itself becomes a publication-critical source requiring full diplomatic proofing.
