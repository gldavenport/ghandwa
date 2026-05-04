---
title: "Cleanup pass 2 stress-test report — The Language Construction Kit"
source_file: "rosenfelder-language-construction-kit.epub"
extraction_date: "2026-05-03"
---

# Cleanup pass 2 stress-test report

## Scope

This pass targeted the issues found in the previous stress test: Contents formatting, one dropped inline image reference, inline-image spacing, and exact-form searchability where EPUB style spans divided words or linguistic examples.

## Changes made

- Converted the generated Contents page into a real `## Contents` heading with a Markdown bullet list.
- Restored the missing `images/00007.jpeg` sidebar image reference.
- Added spaces around inline images embedded in running prose.
- Removed inline `<em>` / `<strong>` markup only where the tag boundary fell inside a word or linguistic form.
- Applied targeted repairs for obvious EPUB span-boundary spacing defects such as `chrepresent`, `scan represent`, `Czechorthography`, `Latinand`, `Chinesespeakers`, `phaticparticles`, `prototypeU`, `whileunder`, `likeḣyvu`, and the `Caďinor &lt;h&gt;` line.
- Updated front matter, image index, and this report.

## File metrics after pass

| Metric | Value |
| --- | ---: |
| Characters | 456,514 |
| Lines | 7,492 |
| Words | 0 |
| Markdown image references in main file | 58 |
| Image files in package | 58 |
| Unreferenced image files from main Markdown | 0 |
| Replacement characters `�` | 0 |
| Suspicious `</em>/<strong>` boundary followed by word char | 0 |
| Suspicious word char followed by `<em>/<strong>` boundary | 0 |

## Exact-form / artifact search tests

| Search string | Count |
| --- | ---: |
| `pǔ-tōng-huà` | 1 |
| `Měi-guó` | 1 |
| `wǒhěn hǎo` | 1 |
| `nèixiōng` | 1 |
| `diànhuà` | 1 |
| `psukhē` | 1 |
| `nāviculārius` | 1 |
| `formōsus` | 2 |
| `fùqin` | 1 |
| `père` | 1 |
| `Czech orthography` | 1 |
| `ch represent` | 3 |
| `images/00007.jpeg` | 1 |
| `Sumerian ![` | 3 |
| `formed ![` | 1 |
| `Cheap ’n easy language families` | 1 |
| `Caďinor &lt;h&gt;` | 1 |
| `something like ḣ ś ź` | 1 |
| `like ḣyvu` | 1 |
| `prototype U` | 1 |
| `sans serif U` | 1 |
| `while under` | 1 |

## Known artifact checks

| Pattern | Count |
| --- | ---: |
| `replacement_character` | 0 |
| `cheap_no_space_heading` | 0 |
| `sumerian_image_no_space` | 0 |
| `formed_image_no_space` | 0 |
| `chrepresent` | 0 |
| `scan represent` | 0 |
| `Czechorthography` | 0 |
| `Latinand` | 0 |
| `Chinesespeakers` | 0 |
| `phaticparticles` | 0 |
| `Caď<em>inor` | 0 |
| `likeḣ` | 0 |
| `šorR` | 0 |
| `prototypeU` | 0 |
| `serifU` | 0 |
| `whileunder` | 0 |

## Remaining limitations

- The EPUB itself contains many style-span boundaries and a few probable source-level missing spaces. This pass repairs the high-confidence cases found by stress testing, but it does not claim to be a character-authoritative edition.
- Some inline emphasis was intentionally removed where it damaged exact word/form searchability. Whole-word italics and bold remain elsewhere.
- The remaining suspicious inline-style boundary counts are now zero by the boundary test used here. That does not prove every source-level spacing issue is gone; it means the specific broken-inline-formatting artifact class found in the stress test has been cleared.

## Recommendation

A further pass would be useful only if you want a more aggressive source-level cleanup of all probable EPUB span-boundary spacing defects. For normal corpus use, this pass fixes the main practical search and structure issues identified in the stress test.
