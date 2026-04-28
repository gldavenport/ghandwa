# Next-pass handoff: Van Sluis / Jørgensen / Kroonen clean extraction upgrade

Use this if someday upgrading the extraction from `complete-working` to `complete-clean`.

## Goal

Improve the existing standalone package while keeping it a clean, readable Markdown extraction. Do not make it diplomatic.

## Priority checks

1. Appendix entry audit
   - Check all 80 compelling isogloss rows against the PDF appendix.
   - Check all 50 doubtful isogloss rows against the PDF appendix.
   - Spot-check rejected entries, especially rows whose references wrapped across lines.

2. Form-level notation audit
   - Check PC and PG forms involving laryngeals, labiovelars, syllabic resonants, Verner/Grimm-related consonants, and long vowels.
   - Preserve authorial source notation; do not force Deuffic or Swanenvleugel conventions onto this article.

3. Classification audit
   - Confirm RT/MO/SM/LX labels.
   - Confirm interpretation labels: IE, IE(?), IE?, L, 3L, ML, CGL, GCL.
   - Confirm temporal strata, especially ranges such as I-II and uncertain strata.

4. Markdown polish
   - Improve bibliography formatting if needed.
   - Convert footnotes only if needed for readability.
   - Confirm major section headings and page anchors.

5. Optional analytical extension
   - Create a semantic-domain table.
   - Create a directionality summary table.
   - Create a comparison crosswalk against Koch 2020 and Hyllested.

## Done criteria

- TSV rows match source appendix at the level needed for clean comparative use.
- Classification/stratum fields are verified.
- Notes clearly mark uncertain readings and wrapped-reference artifacts.

## Filename base

Continue using `van-sluis-et-al-2023` for all revised files.
