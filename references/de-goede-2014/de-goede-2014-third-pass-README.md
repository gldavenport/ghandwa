# de-goede-2014 third-pass extraction

Source: `de-goede-2014.pdf`  
Work: Tim de Goede, *Derivational Morphology: New Perspectives on the Italo-Celtic Hypothesis* (2014).

## Files

- `de-goede-2014-third-pass.md` — clean Markdown extraction with page comments and Markdown footnote definitions.
- `de-goede-2014-suffix-dataset.tsv` — structured table of suffix overview entries from chapter 2.
- `de-goede-2014-suffix-dataset.json` — JSON version of the suffix dataset.
- `de-goede-2014-bibliography-normalized.tsv` — parsed bibliography table with raw entry retained.
- `de-goede-2014-bibliography-normalized.md` — human-readable bibliography companion.
- `de-goede-2014-third-pass-README.md` — this file.

## Third-pass corrections

This pass corrects the recurring character-mapping errors that remained after the second pass:

- glide notation: `i̭` was normalized to `i̯`; `ṷ` was normalized to `u̯`;
- short/uncertain vowel notation: caron-vowels were normalized to breve-vowels, e.g. `ā̌` -> `ā̆`, `ǒ` -> `ŏ`;
- recurring text-layer artifacts in the bibliography/abbreviations were lightly corrected where obvious;
- the suffix overview was parsed into a reusable dataset for reference/querying.

## Remaining caveat

This is clean reference Markdown, not a diplomatic transcription. It is designed for research use, searching, and downstream linguistic reference. Exact PDF line breaks, indentation, and page layout are intentionally not preserved. Isolated bibliography typography may still require checking against the PDF if used for formal citation export.
