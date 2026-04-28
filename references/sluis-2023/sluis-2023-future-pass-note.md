# Future-pass note: van-sluis-et-al-2023

## Current status

```yaml
extraction_status: "complete-clean"
review_status: "isogloss-tables-second-pass-complete"
canonical_form_level: "structured-tables"
```

No further pass is needed for ordinary comparative use, Ghandwa lexical-strata work, or later corpus standardization. The structured appendix tables have already received a targeted second pass and should be treated as the clean working data for this article.

## Useful future passes, if higher quality is ever needed

### 1. Body-text evidence expansion

The current TSVs are appendix-centered. A later pass could extract body-text discussions into a separate evidence table with columns such as:

```text
headword	section	claim_type	pc_form	pg_form	other_ie_forms	example_forms	classification_argument	chronology_argument	page_anchor	notes
```

This would be useful if the goal becomes a searchable argument database rather than a structured appendix extraction.

### 2. Lexical-field normalization

The current isogloss tables preserve source-style entry text. A later pass could split entries more aggressively into:

```text
headword	gloss	pc_form	pg_form	celtic_attestations	germanic_attestations	other_attestations	typology	interpretation_category	stratum	references	notes
```

This should wait until several comparable works have been extracted, because the normalization scheme should align with Koch 2020, Hyllested, and any later Ghandwa lexical database.

### 3. Crosswalk against Koch 2020 and Hyllested

A later corpus-level pass should map each Van Sluis et al. entry against Koch's CG/ICG/CGBS/ANW corpus and Hyllested's earlier list. This would be useful for identifying:

- agreements
- rejections
- downgraded/doubtful items
- classification differences
- chronology differences
- entries unique to one author/work

### 4. Footnotes and bibliography polish

This is not needed for current use. It would only improve readability if the Markdown is used as a polished reading edition.

### 5. Full form-level audit

Only needed if the extraction becomes a citation-grade source for exact forms. This would require checking every starred form, macron, laryngeal, syllabic resonant, and special character against the PDF. The structured appendix tables are already good enough for clean comparative use.

## Do not do unless project goals change

- Do not make a diplomatic transcription.
- Do not silently normalize Celtic, Germanic, and PIE notation to Deuffic or Swanenvleugel conventions.
- Do not collapse source categories such as `IE`, `IE(?)`, `IE?`, `L`, `3L`, `ML`, `CGL`, and `GCL`.
- Do not collapse temporal strata ranges such as `I-II` into a single stage.

## Recommendation

Treat this package as done. Revisit only during a later multi-work standardization pass or if building a normalized Celto-Germanic / Ghandwa lexical-strata database.
