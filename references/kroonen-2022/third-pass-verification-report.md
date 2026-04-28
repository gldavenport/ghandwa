# Third-pass verification report: Kroonen et al. 2022

## Scope

This pass targeted two items from the second-pass handoff:

1. Character-level verification of reconstructed forms.
2. Bibliography normalization into external structured files.

## Reconstructed forms

The PDF was re-extracted from character-level spans. Smaller glyphs were compared to the line baseline and mapped to Unicode where the PDF placed them as superscript or subscript characters. Examples:

- `*b` + superscript `h` → `*bʰ`
- `*g` + superscript `w` → `*gʷ`
- `h` + subscript `2` → `h₂`
- `h` + subscript `a` → `hₐ`

The audit detected **1010** star-marked form occurrences and **842** unique displayed star-marked forms. Both all-occurrence and unique-form CSVs are included in `tables/`.

## Bibliography

The bibliography was normalized into Markdown, CSV, and BibTeX-style exports. **232** source references were parsed. DOI and PMID fields were extracted where supplied in the printed source. For references without identifiers, normalization is heuristic and source-derived.

## Residual limitations

- Table 1 and Table 2 preserve their printed table notation, which uses plain `h2`, `h3`, and separate accent marks in places where the running prose uses typographic subscripts or precomposed accents.
- The bibliography was not externally authority-matched against Crossref, WorldCat, or publisher metadata. The output is structured and cleaned, but not a guarantee of canonical metadata for every undoi'd book/chapter.
- Some source asterisks occur after Tocharian forms or other non-PIE tokens. They remain in the audit because this pass intentionally captured all source star-marked tokens rather than guessing which ones to suppress.
