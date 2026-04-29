# LIV² addenda/corrigenda Markdown extraction

## Contents

- `liv2add.md` — main clean Markdown extraction.
- `liv2add-entry-index.md` — detected headings/root-entry index with PDF page numbers.
- `liv2add-character-audit.md` — targeted character notes, automated-fix summary, and additional character-accuracy pass log.

## Extraction approach

The PDF has embedded text, so OCR was not used. Text was extracted with PyMuPDF, then cleaned to remove running page headers, page numbers, and footers. Page anchors were retained as hidden Markdown/HTML comments (`<!-- page: N -->`) for citation and later checking.

The extraction follows the uploaded linguistics-source instructions: clean Markdown rather than diplomatic transcription; preservation of logical structure; high attention to Indo-Europeanist characters, laryngeals, combining marks, Greek, and scholarly notation.

## Character-accuracy passes

This package now includes the initial extraction, targeted cleanup, the first character audit, and an additional character-accuracy pass. The added pass checked for replacement characters, private-use characters, leftover `Ү`, and combining marks attached to punctuation. It also corrected the two private-use Greek quantity-mark cases in the `*pi̯eh₂-` entry and one stray combining-dot artifact in a citation.

## Known limitations

This package does not claim exhaustive visual verification of every individual form. For lexicographic import or publication-quality quotation, run a further character-by-character verification pass against page images, especially for Lithuanian accents, Greek with stacked diacritics, and dense reconstructed forms.

## Suggested further pass

Another pass would add value only if the file will be used as a structured lexical dataset or quoted at publication quality. The highest-value additional work would be: verify every root heading against page images; verify all forms with combining marks; and normalize bibliography entries into a companion structured list while leaving the source bibliography unchanged in the main Markdown.

## Structured lexical dataset pass

This package now includes a source-faithful structured lexical dataset for downstream lexicographic work:

- `liv2add-structured-lexical-dataset.md` — dataset overview, field notes, summary counts, and sample rows.
- `liv2add-lexical-entries.csv` and `liv2add-lexical-entries.jsonl` — one row per detected lexical/root entry.
- `liv2add-stem-statements.csv` and `liv2add-stem-statements.jsonl` — detected stem-building statements under entries.
- `liv2add-reconstructed-forms.csv` — occurrence index of star-prefixed reconstructed forms with context.
- `liv2add-crossrefs.csv` and `liv2add-crossrefs.jsonl` — heading-level redirects, see-references, alternatives, and removal-style entries.

Dataset rows preserve source notation rather than normalizing it into a single reconstructed root schema. This is deliberate: many entries contain alternatives, redirects, uncertain proposals, and stem-type arguments that should not be flattened automatically.
