---
title: "Wodtko 2008 — use-now and future-revisit note"
source_file_name: "wodtko-2008.pdf"
extraction_date: "2026-05-03T22:15:05Z"
pass_status: "post-pass-7 readiness and future-collation note"
---

# Wodtko 2008 — use-now and future-revisit note

## Current status

The pass-7 bundle is suitable for present use as a machine-assisted, searchable corpus/search edition of *Nomina im Indogermanischen Lexikon*.

It is not a fully character-authoritative edition of every lexical form. The main Markdown remains a readable extraction; the companion TSV files carry the corrected, normalized, unresolved, and stress-tested lookup/collation layers.

## Why it is good enough to use now

The extraction has gone through multiple targeted passes after the initial Markdown conversion:

1. structure and general OCR cleanup;
2. headword, index, and reconstructed-form audit;
3. internal lexical-form candidate extraction;
4. stress-test and repair of reconstructed-form candidates;
5. targeted Greek/non-Latin stress-test and repair.

The final pass-7 layer includes 9,300 internal lexical-form candidate rows and 8,048 unique lookup strings. It also separates unresolved Greek/non-Latin or opaque script-surrogate rows so they do not silently masquerade as verified forms.

## What has been documented elsewhere in the bundle

- `wodtko-2008-pass7-notes.md` lists all pass-7 deliverables and states that pass-7 repairs are editorial lookup aids rather than silent normalization of the source text.
- `wodtko-2008-pass7-greek-nonlatin-stress-repair-report.md` documents the Greek/non-Latin pass, including the 704 target rows, 404 repaired/trimmed/image-collated rows, 300 unresolved rows, and the stress-test results.
- `wodtko-2008-internal-lexical-forms-pass7.tsv` is the full pass-7 candidate layer.
- `wodtko-2008-greek-nonlatin-target-pass7.tsv` records the pass-7 classification of all Greek/non-Latin target rows.
- `wodtko-2008-greek-nonlatin-repaired-pass7.tsv` records rows repaired, trimmed, or image-collated in pass 7.
- `wodtko-2008-greek-nonlatin-unresolved-pass7.tsv` records rows still requiring manual collation.
- `wodtko-2008-unique-lookup-forms-pass7.tsv` provides deduplicated lookup strings after pass 7.
- `wodtko-2008-pass7-greek-nonlatin-stress-test.tsv` preserves the stress-test terms and hit counts.

Earlier pass reports also remain useful as provenance:

- pass 5 documents the internal lexical-form character-audit method and the original unresolved/high-risk candidate layer;
- pass 6 documents the larger reconstructed-form stress-test and mechanical repair layer;
- pass 7 documents the Greek/non-Latin follow-up.

## Remaining limitations

The remaining weaknesses are not ordinary Markdown-cleanup issues. They come from the source PDF text layer and OCR/font encoding:

- Greek forms sometimes appear as custom-font garbage or opaque Latin-like surrogate strings.
- Dense index material remains vulnerable to column-order and small-type extraction errors.
- Some reconstructed forms require visual confirmation of laryngeals, palatovelars, labiovelars, syllabics, accents, macrons, underdots, superscripts, and note-level notation.
- Exact Greek recovery still requires manual image collation or a custom OCR/font-aware workflow with systematic review.

## Future-revisit workflow

A future improvement pass should not start with a general reread. It should begin from the unresolved/collation files:

1. Open `wodtko-2008-greek-nonlatin-unresolved-pass7.tsv`.
2. For each row, inspect the corresponding page image or a high-resolution crop.
3. Replace the unresolved surrogate with a verified Unicode reading.
4. Preserve the original source-layer candidate in a separate column.
5. Mark the repair as image-collated and include the page number.
6. Re-run exact-search stress tests only on the corrected subset.

A second future target, after Greek/non-Latin collation, would be the non-Greek low-confidence/high-risk reconstructed-form rows from pass 6.

## Recommendation

Use the pass-7 bundle now for corpus search, lexical lookup, and exploratory Indo-European work. Treat the TSV lookup layers as the best current machine-assisted index, and treat unresolved rows as an explicit invitation for future manual image collation rather than as a defect that blocks use.
