# QA Report

Source: `friedman-2025.pdf`

## Pass summary

- Second pass: reflowed hard-wrapped prose, repaired common line-break hyphenation, converted wrapped section headings, removed residual Cambridge footer noise where detected, and formatted page-bottom notes as blockquoted footnotes.
- Third pass: generated structured indexes for headings, tables, figures, numbered examples, and footnotes; extracted table blocks into a separate Markdown file; produced a QA count report.

## Counts

| Item | Count |
|---|---:|
| PDF page anchors | 1088 |
| PDF pages without retained text anchors | 1, 2, 18, 40 |
| Expected PDF pages | 1092 |
| Headings detected | 777 |
| Tables detected | 85 |
| Tables converted by wide-space normalization | 37 |
| Numbered examples indexed | 566 |
| Figures indexed | 3 |
| Footnotes indexed | 1784 |
| Cambridge footer fragments remaining | 0 |

## Character scan

```json
{
  "�": 0,
  "￾": 0,
  "ﬁ": 0,
  "ﬂ": 0
}
```

## Remaining limitations

Pages 1, 2, 18, and 40 do not have retained page anchors because they are cover/blank or contain no useful extractable text after cleanup.

The extraction is good for corpus/search use and ordinary reading. It is not a fully diplomatic edition. Complex tables, multi-line examples, and figures should still be checked against the PDF page image before being used as citable data.

A further pass is not needed unless you want one of these narrower deliverables:

1. a fully normalized table dataset;
2. a hand-verified linguistic-example database;
3. figure redrawing or image-level figure descriptions;
4. citation/bibliographic normalization from the Cambridge companion web resources.
