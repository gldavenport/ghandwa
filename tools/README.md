# Ghandwa Tools

---
last_updated: 2026-04-13T00:00-04:00
changelog:
  - 2026-04-13T00:00-04:00 | 66 lines | Initial creation. Documents pie-2-ghandwa.jsx: authority status, headless execution recipe, known gaps. Content absorbed from project instructions §6.
---

## `pie-2-ghandwa.jsx`

PIE-to-Ghandwa phonological transformer. React JSX, but the core logic is plain JavaScript and can be run headless for batch verification.

### Authority

The transformer is **authoritative for surface forms**. Hand-derived Ghandwa forms must be verified against it. Interactions between Osthoff's Law, laryngeal coloring, and devoicing rules produce non-obvious outputs that are easy to miss by hand — e.g.:

- \*nṓman → *noman* (Osthoff shortens ō before mn̥)
- \*gʷʰ devoices to *kʷ* before *s*
- \*pípoti → *píboti* via h₃-triggered voicing adjacent to voiceless stop

When a hand-derived form disagrees with the transformer, the transformer is right unless a specific bug is identified and documented below.

### File structure

| Lines | Contents |
|---|---|
| 1–537 | Tokenizer, rule definitions, rule application machinery |
| 538–738 | `transformSingle(raw)` — the transformer entry point |
| 739–end | React component (`App`) — UI wrapper |

### Headless execution

The React component is a UI wrapper around pure-JS logic. To run the transformer from a Node.js CLI:

1. Extract lines 1–738 (everything before the React `App` component).
2. Strip the `import { useState } from "react";` line at the top.
3. Append a small CLI runner that reads input and calls `transformSingle`:

```javascript
const input = process.argv[2];
const result = transformSingle(input);
console.log(JSON.stringify(result, null, 2));
```

`transformSingle(input)` returns an object with:

- `.final` — the surface form after all rules have applied.
- `.steps` — an array of `{rule, before, after}` entries giving the rule-by-rule derivation.

Use `.steps` when a derivation disagrees with expectation, to identify which rule produced the surprise.

### Known gaps

**Glide respelling fires unconditionally.** The `y → j` rule (corresponding to §5.5 of `phonological-history.md`) does not distinguish diphthong contexts. Correct behavior:

- Pre-consonantal \*ey (diphthong) → transliteration ⟨ei⟩, IPA /ej/
- Pre-vocalic \*ey (glide before vowel) → transliteration ⟨i⟩, IPA /j/

Current transformer output may show ⟨j⟩ in positions where ⟨i⟩ is correct. Post-process or hand-correct as needed.

**h₃ voicing adjacent to voiceless stops** is implemented but edge cases exist. Verify outputs involving h₃ + stop clusters against worked examples in `phonological-history.md` §10.

### Related files

- `docs/phonological-history.md` — the ordered rule inventory the transformer implements.
- `docs/comparanda.md` — rule-by-rule tracking against Ringe 2017, De Vaan, Swanenvleugel.

---

## `pie-2-crotonian.jsx` *(planned — not yet implemented)*

**Status:** Deferred. Dependencies not yet met.

**Purpose:** PIE-to-Crotonian phonological transformer, parallel in architecture to `pie-2-ghandwa.jsx`. Takes a PIE preform as input, applies the Garnier & Sagot (2017) Crotonian rule inventory in chronological order, and outputs a Crotonian surface form. A second adaptation layer then maps that form to its shape as a loanword in Ghandwa.

**Use case:** Generating Crotonian-sourced borrowings for the Ghandwa lexicon. Entries derived via this transformer would carry `provenance` = `Crotonian` in the TSV. Doublet pairs — inherited Ghandwa form vs. Crotonian loanword from the same PIE root — are the primary output.

**Rule inventory source:** Garnier, Romain & Benoît Sagot. 2017. "A shared substrate between Greek and Italic." *Indogermanische Forschungen* 122(1): 29–60. Table 1 (p. 57), 12 chronologically ordered rules. Article is in `references/garnier-2017/`. Garnier & Sagot implemented the same rule set computationally; their test cases (~100 Greek, ~20 Latin/Proto-Romance etymologies) serve as verification suite.

**Dependencies before implementation:**
1. Verb system settled (Ghandwa-internal infrastructure must be stable first)
2. Crotonian phone inventory decided — specifically the fortis/lenis distinction (Garnier's cover symbols \*P, \*B, \*T need concrete phonetic values) and the realization of the Verner-like alternation
3. Ghandwa borrowing adaptation layer specified — how Crotonian phones map to Ghandwa phones on contact (e.g. Crotonian fortis \*P → Ghandwa plain voiceless stop; Crotonian \*ur from syllabic resonants vs. Ghandwa \*ar)

**Known issue to resolve:** Rule 11 asymmetry — \*#pr- → \*#br- (voicing) vs. \*#tr- → \*#Tr- (fortition) is typologically unexplained by Garnier. Implement \*#tr- → \*#Tr- as low-confidence; flag outputs using it.

**See also:** `docs/alt-phonologies.md` §6 for the Crotonian rule inventory summary and divergence table relative to Ghandwa.

---

## `pie-2-crotonian.jsx` *(planned — not yet implemented)*

**Status:** Deferred. Dependencies not yet met.

**Purpose:** PIE-to-Crotonian phonological transformer, parallel in architecture to `pie-2-ghandwa.jsx`. Takes a PIE preform as input, applies the Garnier & Sagot (2017) Crotonian rule inventory in chronological order, and outputs a Crotonian surface form. A second adaptation layer then maps that form to its shape as a loanword in Ghandwa.

**Use case:** Generating Crotonian-sourced borrowings for the Ghandwa lexicon. Entries derived via this transformer would carry `provenance` = `Crotonian` in the TSV. Doublet pairs — inherited Ghandwa form vs. Crotonian loanword from the same PIE root — are the primary output.

**Rule inventory source:** Garnier, Romain & Benoît Sagot. 2017. "A shared substrate between Greek and Italic." *Indogermanische Forschungen* 122(1): 29–60. Table 1 (p. 57), 12 chronologically ordered rules. Article is in `references/garnier-2017/`. Garnier & Sagot implemented the same rule set computationally; their test cases (~100 Greek, ~20 Latin/Proto-Romance etymologies) serve as verification suite.

**Dependencies before implementation:**
1. Verb system settled (Ghandwa-internal infrastructure must be stable first)
2. Crotonian phone inventory decided — specifically the fortis/lenis distinction (Garnier's cover symbols \*P, \*B, \*T need concrete phonetic values) and the realization of the Verner-like alternation
3. Ghandwa borrowing adaptation layer specified — how Crotonian phones map to Ghandwa phones on contact (e.g. Crotonian fortis \*P → Ghandwa plain voiceless stop; Crotonian \*ur from syllabic resonants vs. Ghandwa \*ar)

**Known issue to resolve:** Rule 11 asymmetry — \*#pr- → \*#br- (voicing) vs. \*#tr- → \*#Tr- (fortition) is typologically unexplained by Garnier. Implement \*#tr- → \*#Tr- as low-confidence; flag outputs using it.

**See also:** `docs/alt-phonologies.md` §6 for the Crotonian rule inventory summary and divergence table relative to Ghandwa.
