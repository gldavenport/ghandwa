---
title: "Lexical Dataset Notes — Bennett 1969"
source_title: "Pre-Germanic /p/ for Indo-European /kʷ/"
source_author: "William H. Bennett"
source_year: 1969
source_file: "bennet-1969.pdf"
extraction_date: "2026-05-02"
---

# Lexical Dataset Notes

This pass extracted a separate lexical-form dataset from Bennett 1969 and rechecked dense form sequences against the page images.

## Scope

Included:

- Attested forms cited in the article body.
- Reconstructed, expected, hypothetical, and stem-like forms cited in the article body.
- Glosses where Bennett supplies them.
- Language/stage labels as Bennett gives them, with an expanded language/stage column.
- Role in Bennett’s argument: p-form, q-form, expected comparator, borrowing example, contamination example, or analogy.

Excluded:

- Bibliography-title forms unless they are also part of Bennett’s argument in the article body.
- Pure phoneme references such as /p/, /kʷ/, /gʷh/ unless attached to a lexical form.
- Proper names and titles such as Germania, La Tène, Cotini, and author names.

## Character-level corrections integrated in the v2 Markdown

The dataset pass exposed several places where the previous clean Markdown had simplified or misread dense forms. The v2 Markdown corrects these against page images:

- `*wlkʷos` → `*wl̥kʷos`
- `*wlpos` → `*wl̥pos`
- `*ljekʷrt` → `*ljekʷr̥t`
- `*sekʷnis` → `*sekʷnís`
- `*bajtā` → `*bajtá`
- `baitē` → `baítē`
- `ipnos` → `ipnós` where the Greek oven form is accented in the source
- `*penkʷe` → `*péŋkʷe`
- `*penkʷtrós` → `*peŋkʷrós`
- `*wlkʷ-` → `*wl̥kʷ-`
- `*wlp-` → `*wl̥p-`

## File recommendations

- Use the TSV for corpus or database import; it avoids comma ambiguity in glosses and notes.
- Use the CSV for spreadsheet software.
- Use the JSONL for scripting and downstream transformation.
- Use the Markdown file only as a readable preview.
