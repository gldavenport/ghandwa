---
title: "Fourth-pass extraction notes for Bjørn 2017"
source_pdf: "bjørn-2017.pdf"
extraction_date: "2026-04-29"
pass_status: "fourth pass complete"
---

# Fourth-pass extraction notes

## What changed

- Rebuilt the main Markdown from the PDF text layer using a cleaner text flow than the prior raw extraction.
- Reconstructed systematic linguistic notation in reconstructed forms: aspirates as `ʰ`, labiovelars as `ʷ`, and laryngeals as `h₁`, `h₂`, `h₃`.
- Reflowed broken line wraps and reduced word-join artifacts from the prior raw extraction.
- Preserved PDF page anchors as HTML comments.
- Kept the table of contents in a fenced text block so it does not pollute the Markdown heading hierarchy.
- Added a normalized bibliography companion while preserving the extracted bibliography separately.
- Regenerated the lexical dataset from the fourth-pass Markdown and validated item coverage.

## Lexical dataset validation

- Numbered lexical items extracted: 135
- Expected numbered items: 135
- Missing item numbers: none
- Duplicate item numbers: none

## Character audit counts

- unicode aspirate ʰ: 124
- unicode labialization ʷ: 131
- laryngeal h₁: 133
- laryngeal h₂: 226
- laryngeal h₃: 80
- Greek codepoint count: 1541
- replacement character �: 0

## Suspicious-pattern check

- possible separated aspirate pattern (*b h etc.): 0
- raw mojibake M- artifact: 0

## Remaining caveats

- Some table-like appendix material is still constrained by the PDF text layer and should be checked against the original page image for source-critical use.
- Italic/bold styling is not exhaustively preserved; the pass prioritizes text, structure, and linguistic character fidelity.
- A fully manual proofread could improve individual entries, but would be substantially slower and is unlikely to change ordinary corpus usability.
