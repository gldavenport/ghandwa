# Ringe 2017 Chapter 2 — Third-Pass Targeted Technical Cleanup Report

Source PDF: `ringe-pie-to-proto-germanic-2nd-ed.pdf`

Input Markdown: `ringe-2017-chapter-2-proto-indo-european-second-pass.md`

Output Markdown: `ringe-2017-chapter-2-proto-indo-european-third-pass.md`

## Scope

Chapter 2, printed pp. 5-83 / PDF pp. 16-94.

This pass targeted the sections flagged after the second pass:

- 2.2.1-2.2.4 PIE phonology, especially inventories, ablaut patterns, laryngeal notation, and syllabic resonants.
- 2.3.3 Proto-Central IE verb paradigms, especially the large sample paradigms on printed pp. 44-49.
- 2.3.4 PIE noun inflection, especially large nominal paradigm tables on printed pp. 50-63.
- Greek phonemic transcriptions where the PDF text layer displaced accent marks, colons, or spaces.

## Changes made

- Rebuilt the PIE phonological inventory as a clean fenced table instead of leaving the whole prose introduction inside a code block.
- Split the root-syllable constraint passage so only the three-row stop-combination table remains fenced.
- Restored the ablaut pattern as a two-line block rather than a flattened inline sequence.
- Unwrapped additional prose-heavy fenced blocks in 2.2.3-2.2.4 and in the introductory material around 2.3.3/2.3.4.
- Repaired selected Greek phonemic transcription artifacts, including `/oktɔ́:/`, `/khthɔ́:n/`, and `/gignɔ́:ske:n/`.
- Repaired obvious broken superscript/raised-letter artifacts in the sample verb paradigms, especially `leykʷ-`, `dʰeh₁-`, `gʷem-`, and `weǵʰ-` tables.
- Repaired obvious broken superscript/raised-letter artifacts in the noun paradigms, including rows for `gʷen-`, `dn̥ǵʰuh₂-`, and selected inst./acc. plural forms.
- Expanded and separated footnotes 25 and 26, which had been partially displaced into main text/code blocks by the PDF text layer.

## Diagnostics after third pass

- `h₁`: 732
- `h₂`: 621
- `h₃`: 50
- `kʷ`: 228
- `gʷ`: 206
- `gʷʰ`: 13
- `bʰ`: 200
- `dʰ`: 414
- `gʰ`: 19
- `ḱ`: 194
- `ǵ`: 188
- fenced `text` blocks: 45
- footnote blocks: 0
- remaining isolated `w`/`h` suspect lines: 0

## Remaining limitations

This is still a corpus/search edition, not a fully diplomatic scholarly edition. The third pass substantially improves the targeted high-risk sections, but some large paradigm tables should still be checked against page images before formal quotation or citation. The PDF text layer sometimes separates superscript-like `w`, aspiration `h`, and accent marks from their base characters; this pass repaired the obvious cases found in the targeted sections but does not guarantee that every such case in Chapter 2 is eliminated.

## Remaining suspect isolated-marker lines

No suspect isolated-marker lines remain after the final patch, except the legitimate `w` in the phonological inventory.