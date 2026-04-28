# Appendix cell-verification report

Third-pass scope: Appendix Tables A.1-A.42 were checked as structured sidecar data against the embedded text layer and targeted rendered-page inspection for anomalous cells. The second-pass row counts were retained because they match the source table sequence: 479 innovation rows and 479 feature-occurrence rows.

## Innovation dataset value profile

| Value | Cell count |
| --- | ---: |
| `0` | 1992 |
| `1` | 976 |
| `?` | 861 |
| `3` | 3 |

Total innovation cells checked: 3832. Binary/unknown cells: 3829. Non-binary cells: 3.

## Non-binary cells preserved from the source

These are not extraction errors introduced by the sidecar table: the rendered pages show the same value. Because the Appendix is nominally binary/unknown, they are flagged for scholarly review rather than normalized away.

| Row | Table | Book page | PDF page | Innovation | Column | Source value | Third-pass action |
| ---: | --- | ---: | ---: | --- | --- | --- | --- |
| 296 | A.13 | 233 | 252 | `p, ∗t, ∗k > pf, ʒ, hh` | OHG | `3` | preserved and flagged |
| 419 | A.19 | 239 | 258 | `-æs, -æ, -um` | OE | `3` | preserved and flagged |
| 422 | A.19 | 239 | 258 | `∗-z- ~ ∗-s-; ∗-d- ~ ∗-þ-` | OE | `3` | preserved and flagged |

## Feature-occurrence table check

- Feature-occurrence rows checked: 479.

- Numeric field parsing failures: 2395.


| Row | Book page | Feature | Field | Value |
| ---: | ---: | --- | --- | --- |
| 1 | 242 | `∗ē > ∗ā/ [+stress]` | mean | `None` |
| 1 | 242 | `∗ē > ∗ā/ [+stress]` | sd | `None` |
| 1 | 242 | `∗ē > ∗ā/ [+stress]` | lower_89ci | `None` |
| 1 | 242 | `∗ē > ∗ā/ [+stress]` | higher_89ci | `None` |
| 1 | 242 | `∗ē > ∗ā/ [+stress]` | hdi_range | `None` |
| 2 | 242 | `∗-ī > ∗-i / _#` | mean | `None` |
| 2 | 242 | `∗-ī > ∗-i / _#` | sd | `None` |
| 2 | 242 | `∗-ī > ∗-i / _#` | lower_89ci | `None` |
| 2 | 242 | `∗-ī > ∗-i / _#` | higher_89ci | `None` |
| 2 | 242 | `∗-ī > ∗-i / _#` | hdi_range | `None` |
| 3 | 242 | `∗-ō > ∗-u/ [-stress] _#` | mean | `None` |
| 3 | 242 | `∗-ō > ∗-u/ [-stress] _#` | sd | `None` |
| 3 | 242 | `∗-ō > ∗-u/ [-stress] _#` | lower_89ci | `None` |
| 3 | 242 | `∗-ō > ∗-u/ [-stress] _#` | higher_89ci | `None` |
| 3 | 242 | `∗-ō > ∗-u/ [-stress] _#` | hdi_range | `None` |
| 4 | 242 | `∗-wū > ∗-u` | mean | `None` |
| 4 | 242 | `∗-wū > ∗-u` | sd | `None` |
| 4 | 242 | `∗-wū > ∗-u` | lower_89ci | `None` |
| 4 | 242 | `∗-wū > ∗-u` | higher_89ci | `None` |
| 4 | 242 | `∗-wū > ∗-u` | hdi_range | `None` |
| 5 | 242 | `∗a > ∗u/ _∗m` | mean | `None` |
| 5 | 242 | `∗a > ∗u/ _∗m` | sd | `None` |
| 5 | 242 | `∗a > ∗u/ _∗m` | lower_89ci | `None` |
| 5 | 242 | `∗a > ∗u/ _∗m` | higher_89ci | `None` |
| 5 | 242 | `∗a > ∗u/ _∗m` | hdi_range | `None` |
| 6 | 242 | `∗a > ∗i / [-stress] _ n` | mean | `None` |
| 6 | 242 | `∗a > ∗i / [-stress] _ n` | sd | `None` |
| 6 | 242 | `∗a > ∗i / [-stress] _ n` | lower_89ci | `None` |
| 6 | 242 | `∗a > ∗i / [-stress] _ n` | higher_89ci | `None` |
| 6 | 242 | `∗a > ∗i / [-stress] _ n` | hdi_range | `None` |
| 7 | 242 | `∗ai > ∗ē` | mean | `None` |
| 7 | 242 | `∗ai > ∗ē` | sd | `None` |
| 7 | 242 | `∗ai > ∗ē` | lower_89ci | `None` |
| 7 | 242 | `∗ai > ∗ē` | higher_89ci | `None` |
| 7 | 242 | `∗ai > ∗ē` | hdi_range | `None` |
| 8 | 242 | `∗u > ∗[o]/ ]σ [-high]` | mean | `None` |
| 8 | 242 | `∗u > ∗[o]/ ]σ [-high]` | sd | `None` |
| 8 | 242 | `∗u > ∗[o]/ ]σ [-high]` | lower_89ci | `None` |
| 8 | 242 | `∗u > ∗[o]/ ]σ [-high]` | higher_89ci | `None` |
| 8 | 242 | `∗u > ∗[o]/ ]σ [-high]` | hdi_range | `None` |
| 9 | 242 | `∗ō > ∗ū / _ [σ` | mean | `None` |
| 9 | 242 | `∗ō > ∗ū / _ [σ` | sd | `None` |
| 9 | 242 | `∗ō > ∗ū / _ [σ` | lower_89ci | `None` |
| 9 | 242 | `∗ō > ∗ū / _ [σ` | higher_89ci | `None` |
| 9 | 242 | `∗ō > ∗ū / _ [σ` | hdi_range | `None` |
| 10 | 242 | `∗V1V2 > ∗V̄ 3` | mean | `None` |
| 10 | 242 | `∗V1V2 > ∗V̄ 3` | sd | `None` |
| 10 | 242 | `∗V1V2 > ∗V̄ 3` | lower_89ci | `None` |
| 10 | 242 | `∗V1V2 > ∗V̄ 3` | higher_89ci | `None` |
| 10 | 242 | `∗V1V2 > ∗V̄ 3` | hdi_range | `None` |

## Notes on the three source anomalies

- Table A.13, row 296, `p, *t, *k > pf, ʒ, hh`, column OHG, value `3`: visually checked on the rendered page; the cell is printed as `3`.

- Table A.19, row 419, `-æs, -æ, -um`, column OE, value `3`: visually checked on the rendered page; the cell is printed as `3`.

- Table A.19, row 422, `*-z- ~ *-s-; *-d- ~ *-þ-`, column OE, value `3`: visually checked on the rendered page; the cell is printed as `3`.


## Recommended computational handling

For statistical reuse, do not silently coerce the three `3` values to binary. Use one of these explicit policies: preserve as source-coded non-binary values; recode as missing with a logged transformation; or manually decide a correction from external evidence.
