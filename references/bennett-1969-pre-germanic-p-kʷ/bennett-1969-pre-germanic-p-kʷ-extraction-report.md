---
title: "Pre-Germanic /p/ for Indo-European /kʷ/ — Extraction Report"
author: "William H. Bennett"
date: "1969-06"
source_type: mixed
extraction_date: "2026-05-07"
source_file: "bennet-1969-pre-germanic-p-kʷ.pdf"
chunk: extraction-report
---

# Extraction Report

## Source type

Mixed PDF: scanned page images with a machine-readable text layer. The text layer was usable as a base but contained substantial OCR/text-layer corruption in names, diacritics, Germanic symbols, superscript labiovelar notation, macron vowels, and bibliography entries. Visual page rendering was used as a fallback for technical forms and visibly corrupted words.

## Corrections applied

- Removed JSTOR cover-page boilerplate, download notice, running headers, page numbers, and footer text from the corpus files.
- Rejoined line-broken and hyphenated prose into continuous paragraphs.
- Separated the references into `bennett-1969-pre-germanic-p-kʷ-bibliography.md`.
- Repaired visible OCR/text-layer corruption including, but not limited to: `WIL,TIAM` → `William`; `/kw/`, `/gw/`, `/gwh/` in technical contexts → `/kʷ/`, `/gʷ/`, `/gʷʰ/`; `kc-forms` → `kʷ-forms`; `lpnos`/`ipnds`-type errors → `ipnós`; `lopdsa-` → `lopāśa-`; `La Tbne` → `La Tène`; `aijba`/`wilbeis`-type errors → `*ajþa-`, `aiþs`, `wilþeis`; bibliography errors such as `W6rterbuch`, `Tiibingen`, `Triibner`, and `Bull` → `Wörterbuch`, `Tübingen`, `Trübner`, and `Brill`.
- Restored macrons and other diacritics where visually supported: e.g. `bōs`, `*vōs`, `pād`, `pēda`, `dūn`, `tūn`, `fidwōr`, `*xʷeðwōrez`, `*feðwōrez`, `*fīxʷe`, `*wḷkʷ-`, `*wḷp-`, `*ljekʷṛt`.
- Preserved user-visible annotation as non-source: the yellow highlight on page 246 was not transcribed as source formatting.

## Unresolved-issues list

1. The source appears to use a raised `wh` cluster for IE /gʷʰ/. The output represents this as `/gʷʰ/` and `gʷʰ`; a later pass may prefer `/gʷh/` if matching older typographic convention more narrowly.
2. The exact accent/length interpretation of `*kʷet-wóres`, `-wóres`, and `*pet-wóres` was visually checked but remains a high-value review target because the scan is small and the forms are central to the argument.
3. `*bajtā (baité in Herodotus)` was restored from the visual page; the final vowel/accent in both forms should be reviewed against a cleaner source if available.
4. The sequence `PGmc. *fiŋxʷe > *fīxʷe > Go. *feilv` was restored from the page image; it remains worth checking because the text layer was heavily corrupted in this line.
5. The sequence `IE *peŋkʷrós > PGmc. *fiŋg(w)raz > Go. figgrs` was restored from the page image; it remains worth checking because the text layer was heavily corrupted in this line.

## Confusion-pair report

- `h₁ h₂ h₃`: no laryngeal-index forms detected.
- `ā ē ī ō ū`: macron vowels restored where visually supported. Approximate counts are in the codepoint inventory; no combining macrons were intentionally used.
- Superscript `ʰ ʷ`: labiovelar notation restored with `ʷ`; IE /gʷʰ/ represented with both `ʷ` and `ʰ`, with the caveat noted above.
- `ə`: no schwa detected.
- `ṛ ḷ ṃ ṇ`: `ṛ` and `ḷ` restored in `*ljekʷṛt`, `*wḷkʷos`, `*wḷpos`, `*wḷkʷ-`, and `*wḷp-`. No `ṃ` or `ṇ` detected.
- `ǵ ḱ`: no instances detected.
- `*`: reconstructed-form asterisks preserved in running text. Markdown emphasis may affect display in some renderers, but the raw Markdown retains the literal asterisk characters.
- `†`: no instances detected.

## Codepoint inventory

All counts are approximate and for cross-pass comparison only.

```json
{
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 3,
  "macron_e": 1,
  "macron_i": 1,
  "macron_o": 8,
  "macron_u": 2,
  "schwa": 0,
  "greek_chars": 0,
  "combining_diacritics": 0,
  "dagger": 0
}
```

Additional source-specific approximate counts:

- `ʷ`: 40
- `ʰ`: 4
- `ƀ`: 4
- `þ`: 3
- `ð`: 2
- `ŋ`: 3
- `ḷ`: 4
- `ṛ`: 1

## Structural integrity check

- Main article extracted as one corpus file, as appropriate for a journal article.
- Bibliography extracted as a separate file.
- Footnotes 1 and 2 are attached in the main file using Markdown footnote syntax.
- No tables, figures, maps, plates, or image-only content were detected.
- No index was present.
- Page-boundary continuation was repaired into continuous prose; no known continuation text was intentionally omitted.

## Image inventory

No figures, maps, plates, stemmata, or tables rendered as images were detected. No `images/` directory was created.
