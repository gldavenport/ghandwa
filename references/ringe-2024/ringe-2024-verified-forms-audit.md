# Ringe 2024 verified-forms audit

This pass targeted reconstructed forms and Greek forms rather than general prose cleanup. It used the PDF's rendered/XML glyph positions to distinguish ordinary letters from raised and lowered glyphs, especially superscript aspiration/labiovelarity and subscript laryngeal numerals.

## What was checked

- Reconstructed forms with `∗`.
- Laryngeals and uncertain laryngeals: `h₁`, `h₂`, `h₃`, `H`.
- Raised aspiration/labiovelarity: `ʰ`, `ʷ`.
- Greek tokens and mixed Greek/Latin extraction artifacts, especially Latin `o` where the source glyph is Greek omicron.
- Dense PIE/Greek examples in the early phonology chapters and later Greek-development sections.
- Tables and paradigmatic material to the extent that the PDF XML preserves the visual glyph positions.

## Method

1. Render-sensitive XML was generated from the PDF with Poppler.
2. Raised small `h`/`w` glyphs were reconstructed as `ʰ`/`ʷ`.
3. Lowered laryngeal digits were reconstructed as `₁`, `₂`, `₃`.
4. Greek tokens with obvious Latin-omicron extraction artifacts were normalized page-locally.
5. The existing clean Markdown was patched page-by-page only where the visual-text form and the Markdown form shared the same plain matching key.

## Summary

- PDF pages processed: 415.
- Token-level page-local replacements made during the patch run: 612.
- Main output file: `ringe-2024-the-linguistic-roots-of-ancient-greek-clean-character-fidelity-verified-forms.md`.
- Visual-text reference file: `ringe-2024-visual-text-reference-high-risk-pass.txt`.

## Important finding

The source itself often uses raised `h` not only in reconstructed PIE forms but also in some cited scholarly transliterations. For example, the PDF XML for page 19 encodes Skt. `ágrabʰīt` with a visually raised `h`. That means the earlier apparent issue was not automatically an error: the correction rule must follow the source glyph positions, not external normalization expectations.

## Remaining limitation

This is a clean extraction with targeted form verification. It is not a fully manual, page-by-page scholarly edition of every form in the book. The companion uncertainty file lists areas where future manual image checking would still add value.
