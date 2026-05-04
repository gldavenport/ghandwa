# Ringe 2013 extraction notes — pass 07

Source: `ringe-2013.pdf`

Pass 07 scope:

- Targeted table/example audit after the pass-06 character-hotspot repairs.
- Repaired false bolded table-reference lines that were actually running prose.
- Repaired split captions for selected tables whose titles had been pushed into code blocks.
- Repaired Table 9.3 and Table 9.4 code-block boundaries so prose no longer sits inside the table block.
- Cleaned Table 11.1 by removing underline-artifact rows while preserving searchable wordlist entries.
- Added a note to Table 11.1 that source underlining/dotted underlining is meaningful but exact underline placement is not reproduced in the code block.

Table/figure inventory after pass 07:

```json
{
  "tables": 81,
  "figures": 13,
  "numbered_examples": 115
}
```

Recommended use:

- Use `ringe-2013-historical-linguistics-pass-07.md` as the current working Markdown corpus.
- Use the pass-08 TSV files for corpus mining and targeted lookup.
