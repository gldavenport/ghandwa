# Fourth-pass extraction notes

Source: `EDBIL.pdf`  
Generated: 2026-04-28T18:55:29Z

## Scope of this pass

This was a targeted fourth pass, not a full diplomatic re-OCR. It focused on:

1. entry-boundary verification and repair;
2. false heading removal where discussion text had been misread as a dictionary entry;
3. a normalized references file;
4. a regenerated field-level CSV;
5. a reconstructed-form audit CSV for BSL, PSL, PIE, IE, Slavic, Baltic, and Old Prussian form fields.

## Entry-boundary changes

- False discussion headings repaired: 30
- Lemma case fixes: 1
- Duplicate running heads removed: 1
- Additional OCR field-label repairs: 4
- Remaining suspicious entry headings in audit: 0

The main repaired problem was a third-pass artifact where sentences beginning with words such as “The”, “This”, “For”, or “If” were accidentally promoted to `####` dictionary-entry headings.

## Dataset outputs

- `derksen-2015-edbil-entry-index-fourth-pass.csv`: regenerated entry list with line and page anchors.
- `derksen-2015-edbil-fields-fourth-pass.csv`: regenerated field-level extraction.
- `derksen-2015-edbil-reconstructed-forms-fourth-pass.csv`: field rows with extracted star-forms and automated risk flags.
- `derksen-2015-edbil-form-audit.csv`: rows most likely to need human checking.
- `derksen-2015-edbil-entry-boundary-audit.csv`: remaining heading-level anomalies.
- `derksen-2015-edbil-entry-boundary-fixes.csv`: changes made in this pass.

## Remaining limitations

The PDF was produced with Adobe ClearScan/OCR. This pass improves structure and identifies risk zones, but it does not make every reconstructed form citation-grade. The highest-risk material remains:

- Greek forms;
- Sanskrit transliteration;
- Slavic/Baltic accent marks;
- laryngeal notation and subscript/superscript-like symbols;
- bibliography diacritics, URLs, and journal abbreviations;
- fields where multiple labels were fused by OCR or by previous cleanup.

For formal citation or reuse in a lexical database, use `derksen-2015-edbil-form-audit.csv` as the checklist for page-image verification.
