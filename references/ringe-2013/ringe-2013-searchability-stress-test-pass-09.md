# Ringe 2013 searchability and retrieval stress test — pass 09

Working Markdown tested: `ringe-2013-historical-linguistics-pass-07.md`

## Search term counts

| Query | Hits | Assessment |
|---|---:|---|
| `laryngeal` | 8 | usable |
| `PIE` | 152 | usable |
| `Proto-Indo-European` | 13 | usable |
| `Tocharian` | 52 | usable |
| `PToch.` | 11 | usable |
| `Greek` | 189 | usable |
| `Old Irish` | 23 | usable |
| `sound change` | 266 | usable |
| `analogy` | 11 | usable |
| `subgrouping` | 13 | usable |
| `Mánśi` | 11 | usable |
| `functional load` | 15 | usable |
| `Verner` | 3 | usable |
| `Grimm` | 7 | usable |
| `Table 8.17` | 3 | usable |
| `Table 9.3` | 3 | usable |
| `Table 9.4` | 2 | usable |
| `Table 11.1` | 6 | usable |
| `Table 11.3` | 2 | usable |
| `Table 11.6` | 3 | usable |
| `hypergeometric` | 6 | usable |
| `epitetrápʰatai` | 2 | usable |
| `*h₁dʰí` | 1 | usable |
| `*gʷémeti` | 2 | usable |
| `Pān.ini` | 1 | usable |
| `do-periphrasis` | 18 | usable |
| `Central Sierra Miwok` | 4 | usable |
| `Proto-Baltic Finnic` | 4 | usable |
| `x ≠ y` | 1 | usable |
| `São Paulo` | 1 | usable |
| `twenty-seven` | 1 | usable |
| `pre-Eastern-Miwok` | 1 | usable |

## Structural checks

```json
{
  "code_fence_marker_count": 434,
  "code_fence_even": true,
  "table_caption_lines": 81,
  "figure_caption_lines": 13,
  "false_bold_table_reference_patterns": 0,
  "replacement_character": 0,
  "fffe_artifact": 0,
  "unclear_markers": 0,
  "no_space_pp_dot_digit": 0,
  "or_dot_decimal": 0,
  "pre_hyphen_space": 0,
  "warnings": [],
  "ringe-2013-table-inventory-pass-08.tsv_exists": true,
  "ringe-2013-table-inventory-pass-08.tsv_lines": 82,
  "ringe-2013-numbered-examples-pass-08.tsv_exists": true,
  "ringe-2013-numbered-examples-pass-08.tsv_lines": 315,
  "ringe-2013-extracted-forms-pass-08.tsv_exists": true,
  "ringe-2013-extracted-forms-pass-08.tsv_lines": 2591,
  "ringe-2013-language-label-hits-pass-08.tsv_exists": true,
  "ringe-2013-language-label-hits-pass-08.tsv_lines": 1596
}
```

## Assessment

Pass 07 is the best current working-corpus Markdown. The major retrieval checks now resolve, table/example boundaries are cleaner, and companion TSV files make the text more usable for corpus mining. Remaining limitations are not general Markdown cleanup issues; they would require line-by-line page-image collation or external bibliography normalization.
