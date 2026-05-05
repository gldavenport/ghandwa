# Kroonen 2013 — Twelfth pass Greek/Indic character audit

## Scope

This pass targeted high-confidence OCR artifacts in Greek forms and Indic/Sanskrit/Indo-Iranian transliteration in the eleventh-pass Markdown. It did not attempt wholesale normalization of every Greek or Indic token, especially in the index, because many residual hits require page-image verification.

## Outputs

- `kroonen-2013-twelfth-pass-greek-indic.md`
- `kroonen-2013-lexical-dataset-twelfth-pass.csv`
- `kroonen-2013-twelfth-pass-greek-indic-correction-ledger.csv`
- `kroonen-2013-twelfth-pass-greek-indic-residual-audit.csv`
- `kroonen-2013-twelfth-pass-greek-indic-stress-test-results.csv`
- `kroonen-2013-twelfth-pass-greek-indic-stress-test-contexts.md`

## Correction summary

- Correction rules with hits: **65**
- Actual replacements: **88**
- Greek correction replacements: **51**
- Indic correction replacements: **37**

## Stress-test summary

- `bad_exact_token_hits`: 52 → 0
- `suspicious_greek_indic_context_lines_nonindex`: 1192 → 1192
- `suspicious_greek_indic_context_lines_total`: 1213 → 1213
- `dollar_sign_total`: 175 → 167
- `pound_sign_total`: 187 → 179
- `replacement_character`: 0 → 0

## Residual audit categories

- angle-bracket-in-greek-indic-context: 1167
- latin-ocr-cluster-in-greek-indic-context: 829
- digit-letter-token-in-greek-indic-context: 734
- pound-sign-in-greek-indic-context: 76
- dollar-sign-in-greek-indic-context: 60
- nonlatin-ocr-remnant: 1

## Assessment

The pass improves the highest-confidence Greek and Indic/Sanskrit transliteration failures, especially in the introduction and repeated dictionary contexts. The remaining residual list is still substantial because the index and dense etymological lines contain many mixed OCR artifacts. Those should not be resolved by blanket replacement: many require direct page-image checking. The best next pass would be a dedicated Greek-index pass or a page-block pass for the pages with the densest Greek/Indic residuals.
