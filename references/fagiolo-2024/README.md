# Fagiolo 2024 extraction package

## Source

- `fagiolo-2024.pdf`
- Article: Virna Fagiolo, Daniel Ayora Estevan, and Esteban Ngomo Fernández, “Snakes, dragons, and hydras: the Indo-European terminology for serpent,” *Cuadernos de Filología Clásica. Estudios griegos e indoeuropeos* 34 (2024): 17-28.
- DOI: 10.5209/cfcg.91438

## Files

- `fagiolo-2024.md` — clean/corpus-oriented Markdown extraction with YAML metadata, section headings, page anchors, bibliography, and normalized Markdown footnotes.
- `fagiolo-2024-extracted-forms.md` — companion index of major roots, lexical forms, and serpent/dragon terms discussed in the article.
- `README.md` — this package note.

## Fourth-pass cleanup

This pass targeted the issue identified in the prior package: the source PDF’s text layer splices page-bottom footnotes into the body flow, especially around the long Aeneid, Iliad, Euripides, and scholion quotations.

Changes made:

- Moved footnotes 1–52 into standard Markdown footnote definitions.
- Removed page-spliced footnote fragments from the main text.
- Restored the affected body-text joins around sections 2.1.1–2.2.4.
- Reformatted the main quoted passages as Markdown block quotes where the text layer made that practical.
- Kept page anchors as HTML comments for later source-critical lookup.
- Retained escaped leading asterisks in reconstructed forms so PIE-style notation displays literally.

## Remaining limitations

This is still a clean corpus extraction, not a diplomatic edition. The source has dense scholarly notation and some characters whose PDF text-layer representation is not ideal. The main remaining possible improvement would be a character-only audit against page images for every reconstructed form and every Greek/Sanskrit/Albanian form. That would improve source-critical confidence, but the fourth-pass file is substantially cleaner than the prior version because footnotes no longer interrupt the body text.
