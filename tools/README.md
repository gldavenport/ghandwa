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
