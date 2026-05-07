# Sixth-Pass Targeted Cleanup Audit

This pass addressed the remaining tilde OCR artifacts identified in the fifth-pass audit and rechecked the small set of suspicious starred headings. It is still not a full character-by-character manual edition of all 460 PDF pages.

## Actions

- Removed or resolved all `~` OCR artifacts from the main Markdown.
- Repaired heavily corrupted OCR blocks on PDF pages 92, 288, 323, and 438.
- Rechecked the six suspicious starred headings from the fifth-pass audit. Most were confirmed as intentional; two were corrected (`*kē`, `*up(p)u`).
- Cleaned the final explicit `[unclear]` placeholders that could be resolved from context or page text: the *bu-yo-, *buzdo-, *dekam, *dīro-, *dow-ant-, and *druko- lines.
- Regenerated the entry index and extraction stats.

## Remaining pattern counts

| Pattern class | Remaining count |
|---|---:|
| `~` OCR symbol in main Markdown | 0 |
| `[unclear]` markers in main Markdown | 1 |

## Rechecked suspicious headings

| PDF page | Markdown line | Heading | Pass-six status |
|---:|---:|---|---|
| 131 | 6352 | `*fatar / Gen. *fatanos, *fetnos 'wing, bird' [Noun]` | confirmed against page image; intentional genitive form in heading |
| 208 | 10289 | `*ki / *koy / *kē [Demonstrative Particle or pronoun]` | corrected to `*kē`; Particle capitalization restored |
| 253 | 12587 | `*Lugu- 'god Lug', perhaps originally 'the shiny one' [Noun]` | confirmed intentional theonymic capital L |
| 296 | 14773 | `*Nowdont- [Theonym]` | confirmed intentional theonym heading |
| 300 | 14959 | `*Ogmiyo- 'a mythological name'` | confirmed intentional mythological-name heading |
| 403 | 20228 | `*up(p)u 'ouch' [Exclamation]` | corrected lowercase parenthetical p |

## Remaining explicit uncertainty

The following explicit uncertainty markers remain in the main Markdown:

| Markdown line | Text |
|---:|---|
| 16798 | `[unclear: Fr. dial. form] 'milking vessel' (FEW 11: 183). The comparison with Gr. stenion` |

## Notes

- Several additional high-confidence OCR repairs were made around affected lines, but the source remains OCR-derived and the page image should control for citation-critical forms.
