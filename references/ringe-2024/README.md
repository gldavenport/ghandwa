# Ringe 2024 clean character-fidelity verified-forms package

This package supersedes the previous clean character-fidelity extraction for the purpose of reconstructed-form and Greek-form accuracy. It is not a diplomatic transcription. It keeps clean Markdown structure while correcting high-risk notation using visual-text glyph positioning from the supplied PDF.

## Files

- `ringe-2024-the-linguistic-roots-of-ancient-greek-clean-character-fidelity-verified-forms.md` — main clean Markdown extraction after targeted form verification.
- `ringe-2024-verified-forms-audit.md` — method, summary, and cautions.
- `ringe-2024-remaining-uncertain-forms.md` — residual candidates for future manual image checking.
- `ringe-2024-extracted-high-risk-forms-index.tsv` — page-anchored high-risk forms extracted from the visual-text pass.
- `ringe-2024-visual-text-reference-high-risk-pass.txt` — line-oriented reference extracted from PDF XML with superscript/subscript reconstruction; an audit aid, not the main clean extraction.

## Main correction principle

Do not normalize forms to outside conventions. Use the source image/PDF glyph positions. If the source uses raised `h` in a Sanskrit or other cited form, this package preserves that raised `h`.
