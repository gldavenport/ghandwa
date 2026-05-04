---
title: "Final validation report — The Language Construction Kit"
source_file: "rosenfelder-language-construction-kit.epub"
validation_date: "2026-05-03"
pass_status: "final validation with targeted repairs"
---

# Final validation report — The Language Construction Kit

## Scope

This pass performed the five requested checks: exact-search testing, table fidelity audit, image-reference audit, footnote/endnote audit, and random source-vs-Markdown spot checks. It also applied targeted repairs where validation found high-confidence conversion artifacts.

## Targeted repairs applied

- Converted the Contents block to a real `## Contents` heading with a bullet list.
- Restored the omitted `images/00007.jpeg` reference in the “But I’m …!” sidebar.
- Copied the full image directory back into the extracted package directory so local Markdown image links resolve outside the ZIP.
- Inserted spaces where inline image syntax had collided with preceding words.
- Repaired high-confidence span-boundary artifacts that harmed exact searchability, including Mandarin examples, `psukhē`, `nāviculārius`, `formōsus`, `nèixiōng`, `père`, `fùqin`, `Czech orthography`, `phatic particles`, `prototype U`, and the `Caďinor &lt;h&gt;` line.
- Adjusted three headerless data tables so the first data row is not promoted to a Markdown header row.

## 1. Exact-search test suite

Exact searches run: 50. Passing terms with count > 0: 50.

| Search string | Count |
| --- | ---: |
| `The Language Construction Kit` | 3 |
| `Mark Rosenfelder` | 6 |
| `A naming language` | 2 |
| `Phonetic notation` | 1 |
| `pǔ-tōng-huà` | 1 |
| `Měi-guó` | 1 |
| `wǒhěn hǎo` | 1 |
| `wó hén hǎo` | 1 |
| `nèixiōng` | 1 |
| `psukhē` | 1 |
| `psukho-` | 1 |
| `nāviculārius` | 1 |
| `formōsus` | 2 |
| `fùqin` | 1 |
| `père` | 1 |
| `Czech orthography` | 1 |
| `č</strong> for ch` | 1 |
| `š</strong> for sh` | 1 |
| `Caďinor &lt;h&gt;` | 1 |
| `ḣ ś ź` | 1 |
| `prototype U` | 1 |
| `sans serif U` | 1 |
| `while under` | 1 |
| `phatic particles` | 1 |
| `Chinese speakers` | 1 |
| `Latin and` | 4 |
| `Sumerian ![` | 3 |
| `formed ![` | 1 |
| `images/00007.jpeg` | 1 |
| `Cheap ’n easy language families` | 1 |
| `Kebreni` | 88 |
| `Meṫaiun` | 17 |
| `Aḣimba` | 1 |
| `wényán` | 2 |
| `ŋap` | 1 |
| `Láadan` | 2 |
| `Pirahã` | 3 |
| `Tlön` | 1 |
| `Rōmānus` | 1 |
| `Mē augurem nōmināvērunt` | 1 |
| `Senātus Populusque` | 1 |
| `Caoimhghín` | 1 |
| `Brāhmī` | 2 |
| `Devanāgarī` | 1 |
| `Xīnchéng` | 1 |
| `Yànméi` | 1 |
| `Ḣazum` | 7 |
| `boḣtu` | 2 |
| `eḣc` | 22 |
| `zhoon’yaa` | 1 |

## 2. Table fidelity audit

- Source and Markdown both contain 28 tables.
- 1. part0000_split_005.html#1 source 1 semantic rows/3 max cols → Markdown line 325 1 semantic rows/3 max cols: ok. First row: lug | n | tower
- 2. part0000_split_005.html#2 source 9 semantic rows/6 max cols → Markdown line 431 9 semantic rows/6 max cols: ok. First row:  | Roots |  |  |  | 
- 3. part0000_split_008.html#1 source 6 semantic rows/2 max cols → Markdown line 1296 6 semantic rows/2 max cols: ok. First row: mundus | subject or NOMINATIVE : the world (is, does, ...)
- 4. part0000_split_008.html#2 source 15 semantic rows/3 max cols → Markdown line 1314 15 semantic rows/3 max cols: ok. First row: kirja | NOMINATIVE | book (subject)
- 5. part0000_split_008.html#3 source 7 semantic rows/5 max cols → Markdown line 1471 7 semantic rows/5 max cols: ok. First row:  | French | Hungarian | Quechua | Swahili
- 6. part0000_split_008.html#4 source 4 semantic rows/3 max cols → Markdown line 1621 4 semantic rows/3 max cols: ok. First row:  | s | p
- 7. part0000_split_008.html#5 source 4 semantic rows/3 max cols → Markdown line 1629 4 semantic rows/3 max cols: ok. First row:  | s | p
- 8. part0000_split_008.html#6 source 8 semantic rows/7 max cols → Markdown line 1671 8 semantic rows/7 max cols: ok. First row:  | query | this | that | some | none | every
- 9. part0000_split_009.html#1 source 3 semantic rows/3 max cols → Markdown line 2598 3 semantic rows/3 max cols: ok. First row: HEAVY IS IMPORTANT | heavy (matters, prose) | light ( subjects, banter)
- 10. part0000_split_009.html#2 source 3 semantic rows/3 max cols → Markdown line 2694 3 semantic rows/3 max cols: ok. First row:  | Nouns | Verbs
- 11. part0000_split_009.html#3 source 19 semantic rows/3 max cols → Markdown line 2794 19 semantic rows/3 max cols: ok. First row: standard | colloquial | meaning
- 12. part0000_split_011.html#1 source 7 semantic rows/5 max cols → Markdown line 3921 7 semantic rows/5 max cols: ok. First row: Caďinor | Verdurian | Ismaîn | Barakhinei | gloss
- 13. part0000_split_011.html#2 source 7 semantic rows/4 max cols → Markdown line 3960 7 semantic rows/4 max cols: ok. First row: Verdurian | Ismaîn | Barakhinei | gloss
- 14. part0000_split_011.html#3 source 6 semantic rows/2 max cols → Markdown line 4596 6 semantic rows/2 max cols: ok. First row: yon i ŋ | I speak
- 15. part0000_split_011.html#4 source 5 semantic rows/21 max cols → Markdown line 4714 5 semantic rows/21 max cols: ok. First row: P-W | p | t | k | kw | b | d | g | gw | kš | f | s | x | xw | w | r | l | m | n | ñ | ñw
- 16. part0000_split_011.html#5 source 5 semantic rows/8 max cols → Markdown line 4732 5 semantic rows/8 max cols: ok. First row: P-W | i | e | ê | a | ô | o | u
- 17. part0000_split_011.html#6 source 24 semantic rows/5 max cols → Markdown line 4755 24 semantic rows/5 max cols: ok. First row: P-W | Nanese | Omeguese | K’aitani | Moa
- 18. part0000_split_011.html#7 source 5 semantic rows/5 max cols → Markdown line 4874 5 semantic rows/5 max cols: ok. First row:  | Old English | English | Old High German | German
- 19. part0000_split_011.html#8 source 2 semantic rows/2 max cols → Markdown line 4885 2 semantic rows/2 max cols: ok. First row: s tā n | s tā nas
- 20. part0000_split_011.html#9 source 2 semantic rows/2 max cols → Markdown line 4892 2 semantic rows/2 max cols: ok. First row: stone | stones
- 21. part0000_split_012.html#1 source 11 semantic rows/5 max cols → Markdown line 5178 11 semantic rows/5 max cols: ok. First row: あ a | い i | う u | え e | お o
- 22. part0000_split_012.html#2 source 7 semantic rows/6 max cols → Markdown line 5199 7 semantic rows/6 max cols: ok. First row:  | labial | dental | palatal | velar | glottal
- 23. part0000_split_013.html#1 source 27 semantic rows/7 max cols → Markdown line 5659 27 semantic rows/7 max cols: ok. First row:  | see | work | call | kick | command | not
- 24. part0000_split_013.html#2 source 5 semantic rows/7 max cols → Markdown line 5694 5 semantic rows/7 max cols: ok; irregular source column counts. First row:  | pejorative | ordinary | deferential
- 25. part0000_split_013.html#3 source 4 semantic rows/4 max cols → Markdown line 5745 4 semantic rows/4 max cols: ok. First row: fyn | none | fynte | nothing, no one
- 26. part0000_split_013.html#4 source 14 semantic rows/4 max cols → Markdown line 6498 14 semantic rows/4 max cols: ok. First row: brynu | bry | facing, before, about | keda bryunte ‘in front of the house’, kriidi bryunte ‘about books’
- 27. part0000_split_013.html#5 source 32 semantic rows/3 max cols → Markdown line 6829 32 semantic rows/3 max cols: ok. First row: CC → C |  | treggeur → treḣyr
- 28. part0000_split_013.html#6 source 28 semantic rows/4 max cols → Markdown line 6906 28 semantic rows/4 max cols: ok. First row: Kebreni | Meṫaiun | Cat | Gloss

### Table audit assessment

The table count matches the source. Most tables retain row/column shape. One source table has irregular source column counts because of merged cells/colspan behavior; this remains worth manual review if exact typographic table reconstruction is required. Three obvious headerless data tables were repaired with blank Markdown headers to preserve row semantics.

## 3. Image-reference audit

- Source inline image refs: 59 refs / 57 unique source image files.
- Markdown image refs: 60 refs / 58 unique image files, plus cover if counted separately.
- Missing source image refs in Markdown: none.
- Markdown refs with missing files: none.
- Source/Markdown image sequence matches: yes.

### Image audit assessment

All source image references are now represented in Markdown, including repeated glyph images and the previously omitted `00007.jpeg`. The Markdown also includes the EPUB cover image, which is expected. Image descriptions remain intentionally brief; a later image-caption pass would only be useful if richer accessibility descriptions are desired.

## 4. Footnote/endnote audit

- Markdown footnote refs: 6 total / 3 unique; definitions: 3.
- Undefined refs: none.
- Unused definitions: none.
- Source HTML note-anchor string hits: 13 (low-level heuristic only).

### Footnote audit assessment

The Markdown footnotes are internally consistent: all detected references have definitions and no definitions are orphaned. The source contains only a small note set in this EPUB extraction.

## 5. Random source-vs-Markdown spot checks

| # | Type | Source file | Result | Checked snippet |
| ---: | --- | --- | --- | --- |
| 1 | targeted | `part0000_split_006.html` | pass | `ble for naïve English speakers and for ASCII applications, such as the early web. (In the` |
| 2 | targeted | `part0000_split_006.html` | pass | `e each other. For example, Mandarin’s third tone changes to second before another third to` |
| 3 | targeted | `part0000_split_001.html` | pass | `All rights reserved, including the right to reproduce this book or portions thereof in any` |
| 4 | targeted | `part0000_split_007.html` | pass | `nèidì younger brother of wife dàbó elder brother of husband x iǎ os hū younger brother of` |
| 5 | targeted | `part0000_split_009.html` | pass | `If you have a parent language worked out, you can borrow from it— but only if your people’` |
| 6 | targeted | `part0000_split_012.html` | pass | `We very likely have a prototype U that we compare these to— perhaps something like a sans` |
| 7 | random | `part0000_split_009.html` | pass | `ns prefer to deal with sentences, abstract statements without context. The optimist hopes` |
| 8 | random | `part0000_split_003.html` | pass | `an artificial language, after all, you have to know a lot about real languages.` |
| 9 | random | `part0000_split_012.html` | pass | `We’re so used to writing left to right, top to bottom that we may forget that there are al` |
| 10 | random | `part0000_split_015.html` | pass | `Anne Karpf , The Human Voice: How this extraordinary instrument reveals essential clues ab` |
| 11 | random | `part0000_split_013.html` | pass | `The conjunction is considered to modify the first (X) clause. To second clause can however` |
| 12 | random | `part0000_split_006.html` | pass | `You know about vowels and consonants— though the distinction between them isn’t as airtigh` |
| 13 | random | `part0000_split_006.html` | pass | `If the rule is absolutely regular, you don’t need to indicate stress orthographically. If` |
| 14 | random | `part0000_split_008.html` | pass | `It’s easy and diverting to regularize the table, although natural languages generally leav` |
| 15 | random | `part0000_split_013.html` | pass | `A syntactic alternative, to use the verb tasu ‘do’, is extremely productive, especially fo` |
| 16 | random | `part0000_split_003.html` | pass | `nd a free translation. I recommend this for your grammars as well— it makes it much easier` |
| 17 | random | `part0000_split_005.html` | pass | `Some people are terribly worried about people stealing their languages. But frankly, unles` |
| 18 | random | `part0000_split_005.html` | pass | `When I was a lad, it was foolish to expect anyone to be interested in your conlang, except` |
| 19 | random | `part0000_split_009.html` | pass | `The existence of basic categories answers Willard Quine’s objection to ostension— e.g. tha` |
| 20 | random | `part0000_split_010.html` | pass | `OSE which ensures that neither party has more to add, and the actual closing.` |
| 21 | random | `part0000_split_008.html` | pass | `Many languages offer ways of suggesting the answer to the question. For instance, the Lati` |

### Spot-check assessment

All selected targeted and random spot checks passed after normalization and the targeted repairs above.

## Artifact regression checks

| Pattern | Count after pass |
| --- | ---: |
| `replacement character �` | 0 |
| `Cheap’n easy` | 0 |
| `Czechorthography` | 0 |
| `<strong>ch</strong>represent` | 0 |
| `<strong>s</strong>can represent` | 0 |
| `Sumerian![` | 0 |
| `formed![` | 0 |
| `prototypeU` | 0 |
| `serifU` | 0 |
| `whileunder` | 0 |
| `Latinand` | 0 |
| `Chinesespeakers` | 0 |
| `phaticparticles` | 0 |
| `Caď<em>inor` | 0 |
| `likeḣ` | 0 |

## Final assessment

The extraction is ready for normal corpus use. The remaining worthwhile improvement would be a manual accessibility/caption enhancement pass for small glyph images, or a manual table-typography pass if exact visual reproduction of merged cells is needed. Another broad automated pass is not justified.
