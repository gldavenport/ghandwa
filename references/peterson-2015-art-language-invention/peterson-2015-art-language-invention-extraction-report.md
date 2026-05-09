# The Art of Language Invention — Extraction Report

## Source identification

- Source type: EPUB.
- Primary input used: machine-readable XHTML text layer inside the EPUB archive.
- Image handling: EPUB image files copied directly to `images/` without re-encoding; filenames normalized to kebab-case sequential names.

## Corrections applied

- Converted EPUB XHTML to Markdown using Pandoc after preprocessing noisy styling spans.
- Preserved italics, bold, underlining, small caps where mechanically recoverable from HTML tags/classes.
- Removed generated pagebreak spans from the running text; page ranges are recorded in YAML front matter and README.
- Rewrote image paths to copied `images/` assets.
- Did not perform laryngeal normalization; no normalization pass was needed for this EPUB extraction beyond preserving the text layer.

## Unresolved issues

- Inline image-glyphs unresolved: 588 occurrences. These are preserved as Markdown image references with `image-glyph:` alt text rather than guessed as Unicode. Full location inventory is in `peterson-2015-art-language-invention-image-glyph-inventory.tsv`.
- Because many IPA/transcription/conlang examples are image-only in the EPUB, the corresponding text is not fully searchable until manually decoded or OCR/collation is performed.
- No `[?]` inline inferred-character markers were inserted because the extraction did not visually infer characters from glyph images.

## Confusion-pair report

- h₁ h₂ h₃: no item-by-item manual verification performed; mechanically preserved where present in the XHTML text layer. Inline image-glyph occurrences may hide additional instances.
- ā ē ī ō ū: no item-by-item manual verification performed; mechanically preserved where present in the XHTML text layer. Inline image-glyph occurrences may hide additional instances.
- ʰ ʷ: no item-by-item manual verification performed; mechanically preserved where present in the XHTML text layer. Inline image-glyph occurrences may hide additional instances.
- ə: no item-by-item manual verification performed; mechanically preserved where present in the XHTML text layer. Inline image-glyph occurrences may hide additional instances.
- ṛ ḷ ṃ ṇ: no item-by-item manual verification performed; mechanically preserved where present in the XHTML text layer. Inline image-glyph occurrences may hide additional instances.
- ǵ ḱ: no item-by-item manual verification performed; mechanically preserved where present in the XHTML text layer. Inline image-glyph occurrences may hide additional instances.
- * before reconstructed forms: no item-by-item manual verification performed; mechanically preserved where present in the XHTML text layer. Inline image-glyph occurrences may hide additional instances.
- †: no item-by-item manual verification performed; mechanically preserved where present in the XHTML text layer. Inline image-glyph occurrences may hide additional instances.

## Codepoint inventory

Approximate counts for cross-pass comparison:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 11,
  "macron_e": 10,
  "macron_i": 3,
  "macron_o": 3,
  "macron_u": 3,
  "schwa": 0,
  "greek_chars": 19,
  "combining_diacritics": 0,
  "dagger": 0
}
```

## Structural integrity check

- Headings are preserved from source `<h1>`–`<h6>` elements.
- Bibliography: no separate bibliography section identified in the EPUB.
- Index: extracted separately to `peterson-2015-art-language-invention-index.md`.
- Tables rendered as EPUB images were copied as image assets and left in place as Markdown image links; they were not manually transcribed into Markdown tables.
- Footnotes/endnotes: no separate footnote/endnote apparatus detected in the XHTML files during automated inspection.
- Page-boundary continuation text was not reconstructed because the EPUB source is already reflowable XHTML.

## Image-glyph inventory summary

- `peterson-2015-art-language-invention-ch1-sounds.md`: 243 unresolved inline image-glyphs
- `peterson-2015-art-language-invention-ch2-words.md`: 151 unresolved inline image-glyphs
- `peterson-2015-art-language-invention-ch4-written-word.md`: 76 unresolved inline image-glyphs
- `peterson-2015-art-language-invention-ch3-evolution.md`: 71 unresolved inline image-glyphs
- `peterson-2015-art-language-invention-front-matter.md`: 46 unresolved inline image-glyphs
- `peterson-2015-art-language-invention-introduction.md`: 1 unresolved inline image-glyphs

## Full unresolved image-glyph inventory

1. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116842.jpg` → `images/peterson-2015-art-language-invention-img-0003-116842.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
2. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116840.jpg` → `images/peterson-2015-art-language-invention-img-0004-116840.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
3. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116838.jpg` → `images/peterson-2015-art-language-invention-img-0005-116838.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
4. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116836.jpg` → `images/peterson-2015-art-language-invention-img-0006-116836.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
5. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116834.jpg` → `images/peterson-2015-art-language-invention-img-0007-116834.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
6. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116832.jpg` → `images/peterson-2015-art-language-invention-img-0008-116832.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
7. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116830.jpg` → `images/peterson-2015-art-language-invention-img-0009-116830.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
8. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116828.jpg` → `images/peterson-2015-art-language-invention-img-0010-116828.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
9. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116826.jpg` → `images/peterson-2015-art-language-invention-img-0011-116826.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
10. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116824.jpg` → `images/peterson-2015-art-language-invention-img-0012-116824.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
11. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116821.jpg` → `images/peterson-2015-art-language-invention-img-0013-116821.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
12. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116819.jpg` → `images/peterson-2015-art-language-invention-img-0014-116819.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
13. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116817.jpg` → `images/peterson-2015-art-language-invention-img-0015-116817.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
14. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116814.jpg` → `images/peterson-2015-art-language-invention-img-0016-116814.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
15. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116812.jpg` → `images/peterson-2015-art-language-invention-img-0017-116812.jpg`; classes `h1em`; context: Phonetics Oral Physiology Consonants Vowels Phonology Sound Systems Phonotactics Allophony Intonation Pragmatic Intonation Stress Tone Contour Tone Languages Register Tone Language
16. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116810.jpg` → `images/peterson-2015-art-language-invention-img-0018-116810.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
17. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116808.jpg` → `images/peterson-2015-art-language-invention-img-0019-116808.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
18. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116806.jpg` → `images/peterson-2015-art-language-invention-img-0020-116806.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
19. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116804.jpg` → `images/peterson-2015-art-language-invention-img-0021-116804.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
20. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116802.jpg` → `images/peterson-2015-art-language-invention-img-0022-116802.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
21. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116800.jpg` → `images/peterson-2015-art-language-invention-img-0023-116800.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
22. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116798.jpg` → `images/peterson-2015-art-language-invention-img-0024-116798.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
23. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116796.jpg` → `images/peterson-2015-art-language-invention-img-0025-116796.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
24. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116794.jpg` → `images/peterson-2015-art-language-invention-img-0026-116794.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
25. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116792.jpg` → `images/peterson-2015-art-language-invention-img-0027-116792.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
26. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116790.jpg` → `images/peterson-2015-art-language-invention-img-0028-116790.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
27. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116787.jpg` → `images/peterson-2015-art-language-invention-img-0029-116787.jpg`; classes `h1em`; context: Key Concepts Allomorphy Nominal Inflection Nominal Number Grammatical Gender Noun Case Nominal Inflection Exponence Verbal Inflection Agreement Tense, Modality, Aspect Valency Word
28. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116785.jpg` → `images/peterson-2015-art-language-invention-img-0030-116785.jpg`; classes `h1em`; context: Phonological Evolution Lexical Evolution Grammatical Evolution
29. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116783.jpg` → `images/peterson-2015-art-language-invention-img-0031-116783.jpg`; classes `h1em`; context: Phonological Evolution Lexical Evolution Grammatical Evolution
30. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116781.jpg` → `images/peterson-2015-art-language-invention-img-0032-116781.jpg`; classes `h1em`; context: Orthography Types of Orthographies Alphabet Abjad Abugida Syllabary Complex Systems Using a System Drafting a Proto-System Evolving a Modern System Typography
31. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116779.jpg` → `images/peterson-2015-art-language-invention-img-0033-116779.jpg`; classes `h1em`; context: Orthography Types of Orthographies Alphabet Abjad Abugida Syllabary Complex Systems Using a System Drafting a Proto-System Evolving a Modern System Typography
32. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116777.jpg` → `images/peterson-2015-art-language-invention-img-0034-116777.jpg`; classes `h1em`; context: Orthography Types of Orthographies Alphabet Abjad Abugida Syllabary Complex Systems Using a System Drafting a Proto-System Evolving a Modern System Typography
33. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116775.jpg` → `images/peterson-2015-art-language-invention-img-0035-116775.jpg`; classes `h1em`; context: Orthography Types of Orthographies Alphabet Abjad Abugida Syllabary Complex Systems Using a System Drafting a Proto-System Evolving a Modern System Typography
34. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116773.jpg` → `images/peterson-2015-art-language-invention-img-0036-116773.jpg`; classes `h1em`; context: Orthography Types of Orthographies Alphabet Abjad Abugida Syllabary Complex Systems Using a System Drafting a Proto-System Evolving a Modern System Typography
35. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116771.jpg` → `images/peterson-2015-art-language-invention-img-0037-116771.jpg`; classes `h1em`; context: Orthography Types of Orthographies Alphabet Abjad Abugida Syllabary Complex Systems Using a System Drafting a Proto-System Evolving a Modern System Typography
36. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116768.jpg` → `images/peterson-2015-art-language-invention-img-0038-116768.jpg`; classes `h1em`; context: Orthography Types of Orthographies Alphabet Abjad Abugida Syllabary Complex Systems Using a System Drafting a Proto-System Evolving a Modern System Typography
37. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116765.jpg` → `images/peterson-2015-art-language-invention-img-0039-116765.jpg`; classes `h1em`; context: Orthography Types of Orthographies Alphabet Abjad Abugida Syllabary Complex Systems Using a System Drafting a Proto-System Evolving a Modern System Typography
38. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116763.jpg` → `images/peterson-2015-art-language-invention-img-0040-116763.jpg`; classes `h1em`; context: Orthography Types of Orthographies Alphabet Abjad Abugida Syllabary Complex Systems Using a System Drafting a Proto-System Evolving a Modern System Typography
39. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116761.jpg` → `images/peterson-2015-art-language-invention-img-0041-116761.jpg`; classes `h1em`; context: Orthography Types of Orthographies Alphabet Abjad Abugida Syllabary Complex Systems Using a System Drafting a Proto-System Evolving a Modern System Typography
40. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116759.jpg` → `images/peterson-2015-art-language-invention-img-0042-116759.jpg`; classes `h1em`; context: Dothraki High Valyrian Shiväisith Castithan Irathient Indojisnen Kamakawi Væyne Zaanics
41. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116757.jpg` → `images/peterson-2015-art-language-invention-img-0043-116757.jpg`; classes `h1em`; context: Dothraki High Valyrian Shiväisith Castithan Irathient Indojisnen Kamakawi Væyne Zaanics
42. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116755.jpg` → `images/peterson-2015-art-language-invention-img-0044-116755.jpg`; classes `h1em`; context: Dothraki High Valyrian Shiväisith Castithan Irathient Indojisnen Kamakawi Væyne Zaanics
43. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116753.jpg` → `images/peterson-2015-art-language-invention-img-0045-116753.jpg`; classes `h1em`; context: Dothraki High Valyrian Shiväisith Castithan Irathient Indojisnen Kamakawi Væyne Zaanics
44. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116751.jpg` → `images/peterson-2015-art-language-invention-img-0046-116751.jpg`; classes `h1em`; context: Dothraki High Valyrian Shiväisith Castithan Irathient Indojisnen Kamakawi Væyne Zaanics
45. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116749.jpg` → `images/peterson-2015-art-language-invention-img-0047-116749.jpg`; classes `h1em`; context: Dothraki High Valyrian Shiväisith Castithan Irathient Indojisnen Kamakawi Væyne Zaanics
46. `peterson-2015-art-language-invention-front-matter.md` page n/a: `OEBPS/image/116747.jpg` → `images/peterson-2015-art-language-invention-img-0048-116747.jpg`; classes `h1em`; context: Dothraki High Valyrian Shiväisith Castithan Irathient Indojisnen Kamakawi Væyne Zaanics
47. `peterson-2015-art-language-invention-introduction.md` page 22: `OEBPS/image/115295.jpg` → `images/peterson-2015-art-language-invention-img-0051-115295.jpg`; classes `h1em`; context: 
48. `peterson-2015-art-language-invention-ch1-sounds.md` page 27: `OEBPS/image/115299.jpg` → `images/peterson-2015-art-language-invention-img-0053-115299.jpg`; classes `h1em`; context: 
49. `peterson-2015-art-language-invention-ch1-sounds.md` page 27: `OEBPS/image/121677.jpg` → `images/peterson-2015-art-language-invention-img-0054-121677.jpg`; classes `h1em`; context: In English, we use a number of sounds to convey meaning. Sometimes, though, the same sound will be pronounced differently, even if we’re completely unaware of it. Try this test out
50. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/hindi_teak.jpg` → `images/peterson-2015-art-language-invention-img-0055-hindi-teak.jpg`; classes `h1em`; context: 
51. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/115301.jpg` → `images/peterson-2015-art-language-invention-img-0056-115301.jpg`; classes `h1em`; context: 
52. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/hindi_okay.jpg` → `images/peterson-2015-art-language-invention-img-0057-hindi-okay.jpg`; classes `h1em`; context: 
53. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/115304.jpg` → `images/peterson-2015-art-language-invention-img-0058-115304.jpg`; classes `h1em`; context: 
54. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/115306.jpg` → `images/peterson-2015-art-language-invention-img-0059-115306.jpg`; classes `h1em`; context: 
55. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/115310.jpg` → `images/peterson-2015-art-language-invention-img-0060-115310.jpg`; classes `h1em`; context: 
56. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/115312.jpg` → `images/peterson-2015-art-language-invention-img-0061-115312.jpg`; classes `h1em`; context: 
57. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/115314.jpg` → `images/peterson-2015-art-language-invention-img-0062-115314.jpg`; classes `h1em`; context: 
58. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/116275.jpg` → `images/peterson-2015-art-language-invention-img-0063-116275.jpg`; classes `h1em`; context: 
59. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/118058.jpg` → `images/peterson-2015-art-language-invention-img-0064-118058.jpg`; classes `h1em`; context: 
60. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/115316.jpg` → `images/peterson-2015-art-language-invention-img-0065-115316.jpg`; classes `h1em`; context: 
61. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/115318.jpg` → `images/peterson-2015-art-language-invention-img-0066-115318.jpg`; classes `h1em`; context: 
62. `peterson-2015-art-language-invention-ch1-sounds.md` page 28: `OEBPS/image/121677.jpg` → `images/peterson-2015-art-language-invention-img-0054-121677.jpg`; classes `h1em`; context: Notice that the phonemic transcription (which is always given between forward slashes) leaves off the aspiration marker . This is because it’s considered to be a predictable pronun
63. `peterson-2015-art-language-invention-ch1-sounds.md` page 29: `OEBPS/image/115320.jpg` → `images/peterson-2015-art-language-invention-img-0067-115320.jpg`; classes `h1em`; context: 
64. `peterson-2015-art-language-invention-ch1-sounds.md` page 29: `OEBPS/image/115322.jpg` → `images/peterson-2015-art-language-invention-img-0068-115322.jpg`; classes `h1em`; context: 
65. `peterson-2015-art-language-invention-ch1-sounds.md` page 34: `OEBPS/image/115324.jpg` → `images/peterson-2015-art-language-invention-img-0072-115324.jpg`; classes `h1em`; context: 
66. `peterson-2015-art-language-invention-ch1-sounds.md` page 35: `OEBPS/image/115328.jpg` → `images/peterson-2015-art-language-invention-img-0073-115328.jpg`; classes `h1em`; context: 
67. `peterson-2015-art-language-invention-ch1-sounds.md` page 35: `OEBPS/image/115332.jpg` → `images/peterson-2015-art-language-invention-img-0074-115332.jpg`; classes `h1em`; context: 
68. `peterson-2015-art-language-invention-ch1-sounds.md` page 35: `OEBPS/image/115334.jpg` → `images/peterson-2015-art-language-invention-img-0075-115334.jpg`; classes `h1em`; context: 
69. `peterson-2015-art-language-invention-ch1-sounds.md` page 35: `OEBPS/image/115336.jpg` → `images/peterson-2015-art-language-invention-img-0077-115336.jpg`; classes `h1em`; context: 
70. `peterson-2015-art-language-invention-ch1-sounds.md` page 35: `OEBPS/image/115338.jpg` → `images/peterson-2015-art-language-invention-img-0078-115338.jpg`; classes `h1em`; context: 
71. `peterson-2015-art-language-invention-ch1-sounds.md` page 36: `OEBPS/image/115340.jpg` → `images/peterson-2015-art-language-invention-img-0079-115340.jpg`; classes `h1em`; context: Second, you’ll notice that the post-alveolar symbols and don’t appear on the chart above. This is because the fricatives are the only major sounds that are produced at that point o
72. `peterson-2015-art-language-invention-ch1-sounds.md` page 36: `OEBPS/image/115342.jpg` → `images/peterson-2015-art-language-invention-img-0080-115342.jpg`; classes `h1em`; context: Second, you’ll notice that the post-alveolar symbols and don’t appear on the chart above. This is because the fricatives are the only major sounds that are produced at that point o
73. `peterson-2015-art-language-invention-ch1-sounds.md` page 36: `OEBPS/image/115344.jpg` → `images/peterson-2015-art-language-invention-img-0081-115344.jpg`; classes `h1em`; context: 
74. `peterson-2015-art-language-invention-ch1-sounds.md` page 36: `OEBPS/image/115346.jpg` → `images/peterson-2015-art-language-invention-img-0082-115346.jpg`; classes `h1em`; context: 
75. `peterson-2015-art-language-invention-ch1-sounds.md` page 36: `OEBPS/image/115349.jpg` → `images/peterson-2015-art-language-invention-img-0083-115349.jpg`; classes `h1em`; context: 
76. `peterson-2015-art-language-invention-ch1-sounds.md` page 36: `OEBPS/image/115351.jpg` → `images/peterson-2015-art-language-invention-img-0085-115351.jpg`; classes `h1em`; context: 
77. `peterson-2015-art-language-invention-ch1-sounds.md` page 36: `OEBPS/image/115353.jpg` → `images/peterson-2015-art-language-invention-img-0087-115353.jpg`; classes `h1em`; context: 
78. `peterson-2015-art-language-invention-ch1-sounds.md` page 36: `OEBPS/image/115355.jpg` → `images/peterson-2015-art-language-invention-img-0088-115355.jpg`; classes `h1em`; context: 
79. `peterson-2015-art-language-invention-ch1-sounds.md` page 37: `OEBPS/image/115357.jpg` → `images/peterson-2015-art-language-invention-img-0089-115357.jpg`; classes `h1em`; context: 
80. `peterson-2015-art-language-invention-ch1-sounds.md` page 37: `OEBPS/image/115359.jpg` → `images/peterson-2015-art-language-invention-img-0090-115359.jpg`; classes `h1em`; context: 
81. `peterson-2015-art-language-invention-ch1-sounds.md` page 38: `OEBPS/image/115361.jpg` → `images/peterson-2015-art-language-invention-img-0094-115361.jpg`; classes `h1em`; context: 
82. `peterson-2015-art-language-invention-ch1-sounds.md` page 38: `OEBPS/image/115365.jpg` → `images/peterson-2015-art-language-invention-img-0095-115365.jpg`; classes `h1em`; context: 
83. `peterson-2015-art-language-invention-ch1-sounds.md` page 38: `OEBPS/image/115373.jpg` → `images/peterson-2015-art-language-invention-img-0096-115373.jpg`; classes `h1em`; context: 
84. `peterson-2015-art-language-invention-ch1-sounds.md` page 38: `OEBPS/image/115375.jpg` → `images/peterson-2015-art-language-invention-img-0097-115375.jpg`; classes `h1em`; context: 
85. `peterson-2015-art-language-invention-ch1-sounds.md` page 38: `OEBPS/image/115378.jpg` → `images/peterson-2015-art-language-invention-img-0098-115378.jpg`; classes `h1em`; context: 
86. `peterson-2015-art-language-invention-ch1-sounds.md` page 38: `OEBPS/image/115380.jpg` → `images/peterson-2015-art-language-invention-img-0099-115380.jpg`; classes `h1em`; context: 
87. `peterson-2015-art-language-invention-ch1-sounds.md` page 38: `OEBPS/image/115382.jpg` → `images/peterson-2015-art-language-invention-img-0100-115382.jpg`; classes `h1em`; context: 
88. `peterson-2015-art-language-invention-ch1-sounds.md` page 38: `OEBPS/image/115384.jpg` → `images/peterson-2015-art-language-invention-img-0101-115384.jpg`; classes `h1em`; context: ,
89. `peterson-2015-art-language-invention-ch1-sounds.md` page 38: `OEBPS/image/115386.jpg` → `images/peterson-2015-art-language-invention-img-0102-115386.jpg`; classes `h1em`; context: 
90. `peterson-2015-art-language-invention-ch1-sounds.md` page 38: `OEBPS/image/115388.jpg` → `images/peterson-2015-art-language-invention-img-0103-115388.jpg`; classes `h1em`; context: 
91. `peterson-2015-art-language-invention-ch1-sounds.md` page 38: `OEBPS/image/115392.jpg` → `images/peterson-2015-art-language-invention-img-0104-115392.jpg`; classes `h1em`; context: 
92. `peterson-2015-art-language-invention-ch1-sounds.md` page 39: `OEBPS/image/115394.jpg` → `images/peterson-2015-art-language-invention-img-0105-115394.jpg`; classes `h1em`; context: 
93. `peterson-2015-art-language-invention-ch1-sounds.md` page 39: `OEBPS/image/115396.jpg` → `images/peterson-2015-art-language-invention-img-0106-115396.jpg`; classes `h1em`; context: 
94. `peterson-2015-art-language-invention-ch1-sounds.md` page 39: `OEBPS/image/115398.jpg` → `images/peterson-2015-art-language-invention-img-0107-115398.jpg`; classes `h1em`; context: 
95. `peterson-2015-art-language-invention-ch1-sounds.md` page 39: `OEBPS/image/116277.jpg` → `images/peterson-2015-art-language-invention-img-0108-116277.jpg`; classes `h1em`; context: 
96. `peterson-2015-art-language-invention-ch1-sounds.md` page 39: `OEBPS/image/116279.jpg` → `images/peterson-2015-art-language-invention-img-0109-116279.jpg`; classes `h1em`; context: 
97. `peterson-2015-art-language-invention-ch1-sounds.md` page 39: `OEBPS/image/115401.jpg` → `images/peterson-2015-art-language-invention-img-0110-115401.jpg`; classes `h1em`; context: 
98. `peterson-2015-art-language-invention-ch1-sounds.md` page 41: `OEBPS/image/115403.jpg` → `images/peterson-2015-art-language-invention-img-0112-115403.jpg`; classes `h1em`; context: 
99. `peterson-2015-art-language-invention-ch1-sounds.md` page 41: `OEBPS/image/115405.jpg` → `images/peterson-2015-art-language-invention-img-0113-115405.jpg`; classes `h1em`; context: 
100. `peterson-2015-art-language-invention-ch1-sounds.md` page 41: `OEBPS/image/115407.jpg` → `images/peterson-2015-art-language-invention-img-0114-115407.jpg`; classes `h1em`; context: 
101. `peterson-2015-art-language-invention-ch1-sounds.md` page 41: `OEBPS/image/115409.jpg` → `images/peterson-2015-art-language-invention-img-0115-115409.jpg`; classes `h1em`; context: 
102. `peterson-2015-art-language-invention-ch1-sounds.md` page 41: `OEBPS/image/115411.jpg` → `images/peterson-2015-art-language-invention-img-0116-115411.jpg`; classes `h1em`; context: 
103. `peterson-2015-art-language-invention-ch1-sounds.md` page 42: `OEBPS/image/115413.jpg` → `images/peterson-2015-art-language-invention-img-0117-115413.jpg`; classes `h1em`; context: 
104. `peterson-2015-art-language-invention-ch1-sounds.md` page 42: `OEBPS/image/115415.jpg` → `images/peterson-2015-art-language-invention-img-0118-115415.jpg`; classes `h1em`; context: 
105. `peterson-2015-art-language-invention-ch1-sounds.md` page 42: `OEBPS/image/115417.jpg` → `images/peterson-2015-art-language-invention-img-0119-115417.jpg`; classes `h1em`; context: 
106. `peterson-2015-art-language-invention-ch1-sounds.md` page 42: `OEBPS/image/115419.jpg` → `images/peterson-2015-art-language-invention-img-0120-115419.jpg`; classes `h1em`; context: 
107. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115421.jpg` → `images/peterson-2015-art-language-invention-img-0122-115421.jpg`; classes `h1em`; context: 
108. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115424.jpg` → `images/peterson-2015-art-language-invention-img-0123-115424.jpg`; classes `h1em`; context: With that inventory in mind, all the other vowels can basically be described in reference to English. For example, [y ] , , [ø], [œ] and are simply the vowels [i] , , [e], , and pr
109. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115426.jpg` → `images/peterson-2015-art-language-invention-img-0124-115426.jpg`; classes `h1em`; context: 
110. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115428.jpg` → `images/peterson-2015-art-language-invention-img-0125-115428.jpg`; classes `h1em`; context: ,
111. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115430.jpg` → `images/peterson-2015-art-language-invention-img-0126-115430.jpg`; classes `h1em`; context: With that inventory in mind, all the other vowels can basically be described in reference to English. For example, [y ] , , [ø], [œ] and are simply the vowels [i] , , [e], , and pr
112. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115432.jpg` → `images/peterson-2015-art-language-invention-img-0127-115432.jpg`; classes `h1em`; context: 
113. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115434.jpg` → `images/peterson-2015-art-language-invention-img-0128-115434.jpg`; classes `h1em`; context: 
114. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115436.jpg` → `images/peterson-2015-art-language-invention-img-0129-115436.jpg`; classes `h1em`; context: 
115. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115438.jpg` → `images/peterson-2015-art-language-invention-img-0130-115438.jpg`; classes `h1em`; context: 
116. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115443.jpg` → `images/peterson-2015-art-language-invention-img-0131-115443.jpg`; classes `h1em`; context: 
117. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115445.jpg` → `images/peterson-2015-art-language-invention-img-0132-115445.jpg`; classes `h1em`; context: ,
118. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115448.jpg` → `images/peterson-2015-art-language-invention-img-0133-115448.jpg`; classes `h1em`; context: 
119. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115450.jpg` → `images/peterson-2015-art-language-invention-img-0134-115450.jpg`; classes `h1em`; context: 
120. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115452.jpg` → `images/peterson-2015-art-language-invention-img-0135-115452.jpg`; classes `h1em`; context: 
121. `peterson-2015-art-language-invention-ch1-sounds.md` page 43: `OEBPS/image/115454.jpg` → `images/peterson-2015-art-language-invention-img-0136-115454.jpg`; classes `h1em`; context: 
122. `peterson-2015-art-language-invention-ch1-sounds.md` page 44: `OEBPS/image/115458.jpg` → `images/peterson-2015-art-language-invention-img-0137-115458.jpg`; classes `h1em`; context: 
123. `peterson-2015-art-language-invention-ch1-sounds.md` page 44: `OEBPS/image/115460.jpg` → `images/peterson-2015-art-language-invention-img-0138-115460.jpg`; classes `h1em`; context: 
124. `peterson-2015-art-language-invention-ch1-sounds.md` page 44: `OEBPS/image/115462.jpg` → `images/peterson-2015-art-language-invention-img-0139-115462.jpg`; classes `h1em`; context: 
125. `peterson-2015-art-language-invention-ch1-sounds.md` page 44: `OEBPS/image/115466.jpg` → `images/peterson-2015-art-language-invention-img-0140-115466.jpg`; classes `h1em`; context: 
126. `peterson-2015-art-language-invention-ch1-sounds.md` page 45: `OEBPS/image/115468.jpg` → `images/peterson-2015-art-language-invention-img-0141-115468.jpg`; classes `h1em`; context: 
127. `peterson-2015-art-language-invention-ch1-sounds.md` page 45: `OEBPS/image/115470.jpg` → `images/peterson-2015-art-language-invention-img-0142-115470.jpg`; classes `h1em`; context: 
128. `peterson-2015-art-language-invention-ch1-sounds.md` page 45: `OEBPS/image/115473.jpg` → `images/peterson-2015-art-language-invention-img-0143-115473.jpg`; classes `h1em`; context: 
129. `peterson-2015-art-language-invention-ch1-sounds.md` page 45: `OEBPS/image/115475.jpg` → `images/peterson-2015-art-language-invention-img-0144-115475.jpg`; classes `h1em`; context: 
130. `peterson-2015-art-language-invention-ch1-sounds.md` page 46: `OEBPS/image/115477.jpg` → `images/peterson-2015-art-language-invention-img-0145-115477.jpg`; classes `h1em`; context: 
131. `peterson-2015-art-language-invention-ch1-sounds.md` page 47: `OEBPS/image/115479.jpg` → `images/peterson-2015-art-language-invention-img-0147-115479.jpg`; classes `h1em`; context: 
132. `peterson-2015-art-language-invention-ch1-sounds.md` page 47: `OEBPS/image/115481.jpg` → `images/peterson-2015-art-language-invention-img-0148-115481.jpg`; classes `h1em`; context: 
133. `peterson-2015-art-language-invention-ch1-sounds.md` page 47: `OEBPS/image/115483.jpg` → `images/peterson-2015-art-language-invention-img-0150-115483.jpg`; classes `h1em`; context: 
134. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/hindi_bard.jpg` → `images/peterson-2015-art-language-invention-img-0151-hindi-bard.jpg`; classes `h1em`; context: 
135. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/115490.jpg` → `images/peterson-2015-art-language-invention-img-0152-115490.jpg`; classes `h1em`; context: 
136. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/hindi_washerman.jpg` → `images/peterson-2015-art-language-invention-img-0153-hindi-washerman.jpg`; classes `h1em`; context: 
137. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/115492.jpg` → `images/peterson-2015-art-language-invention-img-0154-115492.jpg`; classes `h1em`; context: 
138. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/hindi_shield.jpg` → `images/peterson-2015-art-language-invention-img-0155-hindi-shield.jpg`; classes `h1em`; context: 
139. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/115494.jpg` → `images/peterson-2015-art-language-invention-img-0156-115494.jpg`; classes `h1em`; context: 
140. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/hindi_chime.jpg` → `images/peterson-2015-art-language-invention-img-0157-hindi-chime.jpg`; classes `h1em`; context: 
141. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/115496.jpg` → `images/peterson-2015-art-language-invention-img-0158-115496.jpg`; classes `h1em`; context: 
142. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/hindi_hour.jpg` → `images/peterson-2015-art-language-invention-img-0159-hindi-hour.jpg`; classes `h1em`; context: 
143. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/115498.jpg` → `images/peterson-2015-art-language-invention-img-0160-115498.jpg`; classes `h1em`; context: 
144. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/115500.jpg` → `images/peterson-2015-art-language-invention-img-0161-115500.jpg`; classes `h1em`; context: 
145. `peterson-2015-art-language-invention-ch1-sounds.md` page 49: `OEBPS/image/115502.jpg` → `images/peterson-2015-art-language-invention-img-0162-115502.jpg`; classes `h1em`; context: 
146. `peterson-2015-art-language-invention-ch1-sounds.md` page 50: `OEBPS/image/121708.jpg` → `images/peterson-2015-art-language-invention-img-0163-121708.jpg`; classes `h1em`; context: ð, ]
147. `peterson-2015-art-language-invention-ch1-sounds.md` page 50: `OEBPS/image/116281.jpg` → `images/peterson-2015-art-language-invention-img-0164-116281.jpg`; classes `h1em`; context: 
148. `peterson-2015-art-language-invention-ch1-sounds.md` page 50: `OEBPS/image/115504.jpg` → `images/peterson-2015-art-language-invention-img-0165-115504.jpg`; classes `h1em`; context: 
149. `peterson-2015-art-language-invention-ch1-sounds.md` page 50: `OEBPS/image/115506.jpg` → `images/peterson-2015-art-language-invention-img-0166-115506.jpg`; classes `h1em`; context: ]
150. `peterson-2015-art-language-invention-ch1-sounds.md` page 51: `OEBPS/image/115508.jpg` → `images/peterson-2015-art-language-invention-img-0167-115508.jpg`; classes `h1em`; context: 
151. `peterson-2015-art-language-invention-ch1-sounds.md` page 51: `OEBPS/image/115510.jpg` → `images/peterson-2015-art-language-invention-img-0168-115510.jpg`; classes `h1em`; context: 
152. `peterson-2015-art-language-invention-ch1-sounds.md` page 52: `OEBPS/image/115512.jpg` → `images/peterson-2015-art-language-invention-img-0169-115512.jpg`; classes `h1em`; context: 
153. `peterson-2015-art-language-invention-ch1-sounds.md` page 52: `OEBPS/image/115514.jpg` → `images/peterson-2015-art-language-invention-img-0170-115514.jpg`; classes `h1em`; context: 
154. `peterson-2015-art-language-invention-ch1-sounds.md` page 52: `OEBPS/image/115516.jpg` → `images/peterson-2015-art-language-invention-img-0171-115516.jpg`; classes `h1em`; context: 
155. `peterson-2015-art-language-invention-ch1-sounds.md` page 52: `OEBPS/image/115519.jpg` → `images/peterson-2015-art-language-invention-img-0172-115519.jpg`; classes `h1em`; context: 
156. `peterson-2015-art-language-invention-ch1-sounds.md` page 52: `OEBPS/image/115521.jpg` → `images/peterson-2015-art-language-invention-img-0173-115521.jpg`; classes `h1em`; context: 
157. `peterson-2015-art-language-invention-ch1-sounds.md` page 53: `OEBPS/image/115525.jpg` → `images/peterson-2015-art-language-invention-img-0174-115525.jpg`; classes `h1em`; context: 
158. `peterson-2015-art-language-invention-ch1-sounds.md` page 53: `OEBPS/image/115527.jpg` → `images/peterson-2015-art-language-invention-img-0175-115527.jpg`; classes `h1em`; context: 
159. `peterson-2015-art-language-invention-ch1-sounds.md` page 53: `OEBPS/image/115529.jpg` → `images/peterson-2015-art-language-invention-img-0176-115529.jpg`; classes `h1em`; context: 
160. `peterson-2015-art-language-invention-ch1-sounds.md` page 53: `OEBPS/image/115533.jpg` → `images/peterson-2015-art-language-invention-img-0177-115533.jpg`; classes `h1em`; context: 
161. `peterson-2015-art-language-invention-ch1-sounds.md` page 53: `OEBPS/image/115535.jpg` → `images/peterson-2015-art-language-invention-img-0178-115535.jpg`; classes `h1em`; context: 
162. `peterson-2015-art-language-invention-ch1-sounds.md` page 53: `OEBPS/image/115538.jpg` → `images/peterson-2015-art-language-invention-img-0179-115538.jpg`; classes `h1em`; context: 
163. `peterson-2015-art-language-invention-ch1-sounds.md` page 54: `OEBPS/image/115540.jpg` → `images/peterson-2015-art-language-invention-img-0181-115540.jpg`; classes `h1em`; context: 
164. `peterson-2015-art-language-invention-ch1-sounds.md` page 54: `OEBPS/image/115542.jpg` → `images/peterson-2015-art-language-invention-img-0182-115542.jpg`; classes `h1em`; context: 
165. `peterson-2015-art-language-invention-ch1-sounds.md` page 54: `OEBPS/image/115545.jpg` → `images/peterson-2015-art-language-invention-img-0183-115545.jpg`; classes `h1em`; context: 
166. `peterson-2015-art-language-invention-ch1-sounds.md` page 54: `OEBPS/image/115547.jpg` → `images/peterson-2015-art-language-invention-img-0184-115547.jpg`; classes `h1em`; context: 
167. `peterson-2015-art-language-invention-ch1-sounds.md` page 54: `OEBPS/image/115549.jpg` → `images/peterson-2015-art-language-invention-img-0185-115549.jpg`; classes `h1em`; context: 
168. `peterson-2015-art-language-invention-ch1-sounds.md` page 55: `OEBPS/image/115551.jpg` → `images/peterson-2015-art-language-invention-img-0186-115551.jpg`; classes `h1em`; context: 
169. `peterson-2015-art-language-invention-ch1-sounds.md` page 55: `OEBPS/image/115553.jpg` → `images/peterson-2015-art-language-invention-img-0187-115553.jpg`; classes `h1em`; context: 
170. `peterson-2015-art-language-invention-ch1-sounds.md` page 55: `OEBPS/image/115555.jpg` → `images/peterson-2015-art-language-invention-img-0188-115555.jpg`; classes `h1em`; context: 
171. `peterson-2015-art-language-invention-ch1-sounds.md` page 55: `OEBPS/image/115557.jpg` → `images/peterson-2015-art-language-invention-img-0189-115557.jpg`; classes `h1em`; context: 
172. `peterson-2015-art-language-invention-ch1-sounds.md` page 56: `OEBPS/image/115561.jpg` → `images/peterson-2015-art-language-invention-img-0190-115561.jpg`; classes `h1em`; context: 
173. `peterson-2015-art-language-invention-ch1-sounds.md` page 56: `OEBPS/image/115563.jpg` → `images/peterson-2015-art-language-invention-img-0191-115563.jpg`; classes `h1em`; context: 
174. `peterson-2015-art-language-invention-ch1-sounds.md` page 56: `OEBPS/image/115565.jpg` → `images/peterson-2015-art-language-invention-img-0192-115565.jpg`; classes `h1em`; context: 
175. `peterson-2015-art-language-invention-ch1-sounds.md` page 56: `OEBPS/image/115567.jpg` → `images/peterson-2015-art-language-invention-img-0193-115567.jpg`; classes `h1em`; context: 
176. `peterson-2015-art-language-invention-ch1-sounds.md` page 56: `OEBPS/image/115569.jpg` → `images/peterson-2015-art-language-invention-img-0194-115569.jpg`; classes `h1em`; context: ,
177. `peterson-2015-art-language-invention-ch1-sounds.md` page 56: `OEBPS/image/Image70139.jpg` → `images/peterson-2015-art-language-invention-img-0195-image70139.jpg`; classes `h1em`; context: 
178. `peterson-2015-art-language-invention-ch1-sounds.md` page 56: `OEBPS/image/115571.jpg` → `images/peterson-2015-art-language-invention-img-0196-115571.jpg`; classes `h1em`; context: 
179. `peterson-2015-art-language-invention-ch1-sounds.md` page 56: `OEBPS/image/115573.jpg` → `images/peterson-2015-art-language-invention-img-0197-115573.jpg`; classes `h1em`; context: 
180. `peterson-2015-art-language-invention-ch1-sounds.md` page 57: `OEBPS/image/115575.jpg` → `images/peterson-2015-art-language-invention-img-0198-115575.jpg`; classes `h1em`; context: 
181. `peterson-2015-art-language-invention-ch1-sounds.md` page 57: `OEBPS/image/115577.jpg` → `images/peterson-2015-art-language-invention-img-0199-115577.jpg`; classes `h1em`; context: 
182. `peterson-2015-art-language-invention-ch1-sounds.md` page 57: `OEBPS/image/115579.jpg` → `images/peterson-2015-art-language-invention-img-0200-115579.jpg`; classes `h1em`; context: 
183. `peterson-2015-art-language-invention-ch1-sounds.md` page 57: `OEBPS/image/115582.jpg` → `images/peterson-2015-art-language-invention-img-0201-115582.jpg`; classes `h1em`; context: 
184. `peterson-2015-art-language-invention-ch1-sounds.md` page 57: `OEBPS/image/115584.jpg` → `images/peterson-2015-art-language-invention-img-0202-115584.jpg`; classes `h1em`; context: 
185. `peterson-2015-art-language-invention-ch1-sounds.md` page 57: `OEBPS/image/115591.jpg` → `images/peterson-2015-art-language-invention-img-0203-115591.jpg`; classes `h1em`; context: 
186. `peterson-2015-art-language-invention-ch1-sounds.md` page 59: `OEBPS/image/115593.jpg` → `images/peterson-2015-art-language-invention-img-0204-115593.jpg`; classes `h1em`; context: 
187. `peterson-2015-art-language-invention-ch1-sounds.md` page 59: `OEBPS/image/116284.jpg` → `images/peterson-2015-art-language-invention-img-0205-116284.jpg`; classes `h1em`; context: 
188. `peterson-2015-art-language-invention-ch1-sounds.md` page 59: `OEBPS/image/116286.jpg` → `images/peterson-2015-art-language-invention-img-0206-116286.jpg`; classes `h1em`; context: 
189. `peterson-2015-art-language-invention-ch1-sounds.md` page 59: `OEBPS/image/115595.jpg` → `images/peterson-2015-art-language-invention-img-0207-115595.jpg`; classes `h1em`; context: 
190. `peterson-2015-art-language-invention-ch1-sounds.md` page 59: `OEBPS/image/116287.jpg` → `images/peterson-2015-art-language-invention-img-0208-116287.jpg`; classes `h1em`; context: 
191. `peterson-2015-art-language-invention-ch1-sounds.md` page 60: `OEBPS/image/115597.jpg` → `images/peterson-2015-art-language-invention-img-0209-115597.jpg`; classes `h1em`; context: 
192. `peterson-2015-art-language-invention-ch1-sounds.md` page 66: `OEBPS/image/115621.jpg` → `images/peterson-2015-art-language-invention-img-0214-115621.jpg`; classes `h1em`; context: 
193. `peterson-2015-art-language-invention-ch1-sounds.md` page 66: `OEBPS/image/115624.jpg` → `images/peterson-2015-art-language-invention-img-0215-115624.jpg`; classes `h1em`; context: 
194. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115626.jpg` → `images/peterson-2015-art-language-invention-img-0216-115626.jpg`; classes `h1em`; context: 
195. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115628.jpg` → `images/peterson-2015-art-language-invention-img-0217-115628.jpg`; classes `h1em`; context: 
196. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115630.jpg` → `images/peterson-2015-art-language-invention-img-0218-115630.jpg`; classes `h1em`; context: 
197. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115632.jpg` → `images/peterson-2015-art-language-invention-img-0219-115632.jpg`; classes `h1em`; context: 
198. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115634.jpg` → `images/peterson-2015-art-language-invention-img-0220-115634.jpg`; classes `h1em`; context: 
199. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115636.jpg` → `images/peterson-2015-art-language-invention-img-0221-115636.jpg`; classes `h1em`; context: 
200. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115638.jpg` → `images/peterson-2015-art-language-invention-img-0222-115638.jpg`; classes `h1em`; context: 
201. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115640.jpg` → `images/peterson-2015-art-language-invention-img-0223-115640.jpg`; classes `h1em`; context: 
202. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115642.jpg` → `images/peterson-2015-art-language-invention-img-0224-115642.jpg`; classes `h1em`; context: 
203. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115644.jpg` → `images/peterson-2015-art-language-invention-img-0225-115644.jpg`; classes `h1em`; context: 
204. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115646.jpg` → `images/peterson-2015-art-language-invention-img-0226-115646.jpg`; classes `h1em`; context: 
205. `peterson-2015-art-language-invention-ch1-sounds.md` page 67: `OEBPS/image/115648.jpg` → `images/peterson-2015-art-language-invention-img-0227-115648.jpg`; classes `h1em`; context: 
206. `peterson-2015-art-language-invention-ch1-sounds.md` page 68: `OEBPS/image/115655.jpg` → `images/peterson-2015-art-language-invention-img-0228-115655.jpg`; classes `h1em`; context: 
207. `peterson-2015-art-language-invention-ch1-sounds.md` page 68: `OEBPS/image/115657.jpg` → `images/peterson-2015-art-language-invention-img-0229-115657.jpg`; classes `h1em`; context: 
208. `peterson-2015-art-language-invention-ch1-sounds.md` page 68: `OEBPS/image/115659.jpg` → `images/peterson-2015-art-language-invention-img-0230-115659.jpg`; classes `h1em`; context: 
209. `peterson-2015-art-language-invention-ch1-sounds.md` page 69: `OEBPS/image/115661.jpg` → `images/peterson-2015-art-language-invention-img-0232-115661.jpg`; classes `h1em`; context: 
210. `peterson-2015-art-language-invention-ch1-sounds.md` page 69: `OEBPS/image/115663.jpg` → `images/peterson-2015-art-language-invention-img-0233-115663.jpg`; classes `h1em`; context: 
211. `peterson-2015-art-language-invention-ch1-sounds.md` page 69: `OEBPS/image/115665.jpg` → `images/peterson-2015-art-language-invention-img-0234-115665.jpg`; classes `h1em`; context: 
212. `peterson-2015-art-language-invention-ch1-sounds.md` page 69: `OEBPS/image/115667.jpg` → `images/peterson-2015-art-language-invention-img-0235-115667.jpg`; classes `h1em`; context: 
213. `peterson-2015-art-language-invention-ch1-sounds.md` page 70: `OEBPS/image/115669.jpg` → `images/peterson-2015-art-language-invention-img-0236-115669.jpg`; classes `h1em`; context: 
214. `peterson-2015-art-language-invention-ch1-sounds.md` page 70: `OEBPS/image/115671.jpg` → `images/peterson-2015-art-language-invention-img-0237-115671.jpg`; classes `h1em`; context: 
215. `peterson-2015-art-language-invention-ch1-sounds.md` page 70: `OEBPS/image/115673.jpg` → `images/peterson-2015-art-language-invention-img-0238-115673.jpg`; classes `h1em`; context: 
216. `peterson-2015-art-language-invention-ch1-sounds.md` page 70: `OEBPS/image/115675.jpg` → `images/peterson-2015-art-language-invention-img-0239-115675.jpg`; classes `h1em`; context: 
217. `peterson-2015-art-language-invention-ch1-sounds.md` page 70: `OEBPS/image/115677.jpg` → `images/peterson-2015-art-language-invention-img-0240-115677.jpg`; classes `h1em`; context: 
218. `peterson-2015-art-language-invention-ch1-sounds.md` page 70: `OEBPS/image/115679.jpg` → `images/peterson-2015-art-language-invention-img-0241-115679.jpg`; classes `h1em`; context: 
219. `peterson-2015-art-language-invention-ch1-sounds.md` page 70: `OEBPS/image/115681.jpg` → `images/peterson-2015-art-language-invention-img-0242-115681.jpg`; classes `h1em`; context: 
220. `peterson-2015-art-language-invention-ch1-sounds.md` page 71: `OEBPS/image/115683.jpg` → `images/peterson-2015-art-language-invention-img-0245-115683.jpg`; classes `h1em`; context: 
221. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/118962.jpg` → `images/peterson-2015-art-language-invention-img-0247-118962.jpg`; classes `h1em`; context: 
222. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/115687.jpg` → `images/peterson-2015-art-language-invention-img-0248-115687.jpg`; classes `h1em`; context: 
223. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/119870.jpg` → `images/peterson-2015-art-language-invention-img-0249-119870.jpg`; classes `h1em`; context: 
224. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/115689.jpg` → `images/peterson-2015-art-language-invention-img-0250-115689.jpg`; classes `h1em`; context: 
225. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/119872.jpg` → `images/peterson-2015-art-language-invention-img-0251-119872.jpg`; classes `h1em`; context: 
226. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/ma.jpg` → `images/peterson-2015-art-language-invention-img-0252-ma.jpg`; classes `h1em`; context: or [ma214] “horse”
227. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/115691.jpg` → `images/peterson-2015-art-language-invention-img-0253-115691.jpg`; classes `h1em`; context: 
228. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/119874.jpg` → `images/peterson-2015-art-language-invention-img-0254-119874.jpg`; classes `h1em`; context: 
229. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/115693.jpg` → `images/peterson-2015-art-language-invention-img-0255-115693.jpg`; classes `h1em`; context: 
230. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/115695.jpg` → `images/peterson-2015-art-language-invention-img-0256-115695.jpg`; classes `h1em`; context: 
231. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/115697.jpg` → `images/peterson-2015-art-language-invention-img-0257-115697.jpg`; classes `h1em`; context: 
232. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/115699.jpg` → `images/peterson-2015-art-language-invention-img-0258-115699.jpg`; classes `h1em`; context: 
233. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/115701.jpg` → `images/peterson-2015-art-language-invention-img-0259-115701.jpg`; classes `h1em`; context: 
234. `peterson-2015-art-language-invention-ch1-sounds.md` page 73: `OEBPS/image/115703.jpg` → `images/peterson-2015-art-language-invention-img-0260-115703.jpg`; classes `h1em`; context: 
235. `peterson-2015-art-language-invention-ch1-sounds.md` page 74: `OEBPS/image/115705.jpg` → `images/peterson-2015-art-language-invention-img-0261-115705.jpg`; classes `h1em`; context: 
236. `peterson-2015-art-language-invention-ch1-sounds.md` page 74: `OEBPS/image/115707.jpg` → `images/peterson-2015-art-language-invention-img-0262-115707.jpg`; classes `h1em`; context: “paddy field”
237. `peterson-2015-art-language-invention-ch1-sounds.md` page 74: `OEBPS/image/115710.jpg` → `images/peterson-2015-art-language-invention-img-0263-115710.jpg`; classes `h1em`; context: 
238. `peterson-2015-art-language-invention-ch1-sounds.md` page 74: `OEBPS/image/115737.jpg` → `images/peterson-2015-art-language-invention-img-0264-115737.jpg`; classes `h1em`; context: “nickname (i.e. this is someone in particular’s nickname)”
239. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/115739.jpg` → `images/peterson-2015-art-language-invention-img-0265-115739.jpg`; classes `h1em`; context: 
240. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/115741.jpg` → `images/peterson-2015-art-language-invention-img-0266-115741.jpg`; classes `h1em`; context: “face”
241. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/115743.jpg` → `images/peterson-2015-art-language-invention-img-0267-115743.jpg`; classes `h1em`; context: 
242. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/115745.jpg` → `images/peterson-2015-art-language-invention-img-0268-115745.jpg`; classes `h1em`; context: “maternal aunt”
243. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/115747.jpg` → `images/peterson-2015-art-language-invention-img-0269-115747.jpg`; classes `h1em`; context: 
244. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/115749.jpg` → `images/peterson-2015-art-language-invention-img-0270-115749.jpg`; classes `h1em`; context: “thick”
245. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/118964.jpg` → `images/peterson-2015-art-language-invention-img-0271-118964.jpg`; classes `h1em`; context: 
246. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/ni.jpg` → `images/peterson-2015-art-language-invention-img-0272-ni.jpg`; classes `h1em`; context: 
247. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/118966.jpg` → `images/peterson-2015-art-language-invention-img-0273-118966.jpg`; classes `h1em`; context: 
248. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/hao.jpg` → `images/peterson-2015-art-language-invention-img-0274-hao.jpg`; classes `h1em`; context: [ni214] “you” + [hao214] “good” = ní [ni35.hao21] “hello”
249. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/115751.jpg` → `images/peterson-2015-art-language-invention-img-0275-115751.jpg`; classes `h1em`; context: 
250. `peterson-2015-art-language-invention-ch1-sounds.md` page 75: `OEBPS/image/hao.jpg` → `images/peterson-2015-art-language-invention-img-0274-hao.jpg`; classes `h1em`; context: ní
251. `peterson-2015-art-language-invention-ch1-sounds.md` page 76: `OEBPS/image/115753.jpg` → `images/peterson-2015-art-language-invention-img-0276-115753.jpg`; classes `h1em`; context: 
252. `peterson-2015-art-language-invention-ch1-sounds.md` page 76: `OEBPS/image/115755.jpg` → `images/peterson-2015-art-language-invention-img-0277-115755.jpg`; classes `h1em`; context: 
253. `peterson-2015-art-language-invention-ch1-sounds.md` page 76: `OEBPS/image/115758.jpg` → `images/peterson-2015-art-language-invention-img-0278-115758.jpg`; classes `h1em`; context: 
254. `peterson-2015-art-language-invention-ch1-sounds.md` page 76: `OEBPS/image/116290.jpg` → `images/peterson-2015-art-language-invention-img-0279-116290.jpg`; classes `h1em`; context: 
255. `peterson-2015-art-language-invention-ch1-sounds.md` page 76: `OEBPS/image/115760.jpg` → `images/peterson-2015-art-language-invention-img-0280-115760.jpg`; classes `h1em`; context: 
256. `peterson-2015-art-language-invention-ch1-sounds.md` page 76: `OEBPS/image/115762.jpg` → `images/peterson-2015-art-language-invention-img-0281-115762.jpg`; classes `h1em`; context: 
257. `peterson-2015-art-language-invention-ch1-sounds.md` page 77: `OEBPS/image/115764.jpg` → `images/peterson-2015-art-language-invention-img-0282-115764.jpg`; classes `h1em`; context: 
258. `peterson-2015-art-language-invention-ch1-sounds.md` page 77: `OEBPS/image/115766.jpg` → `images/peterson-2015-art-language-invention-img-0283-115766.jpg`; classes `h1em`; context: 
259. `peterson-2015-art-language-invention-ch1-sounds.md` page 77: `OEBPS/image/115768.jpg` → `images/peterson-2015-art-language-invention-img-0284-115768.jpg`; classes `h1em`; context: 
260. `peterson-2015-art-language-invention-ch1-sounds.md` page 77: `OEBPS/image/115774.jpg` → `images/peterson-2015-art-language-invention-img-0285-115774.jpg`; classes `h1em`; context: 
261. `peterson-2015-art-language-invention-ch1-sounds.md` page 77: `OEBPS/image/115776.jpg` → `images/peterson-2015-art-language-invention-img-0286-115776.jpg`; classes `h1em`; context: 
262. `peterson-2015-art-language-invention-ch1-sounds.md` page 77: `OEBPS/image/115778.jpg` → `images/peterson-2015-art-language-invention-img-0287-115778.jpg`; classes `h1em`; context: 
263. `peterson-2015-art-language-invention-ch1-sounds.md` page 77: `OEBPS/image/115780.jpg` → `images/peterson-2015-art-language-invention-img-0288-115780.jpg`; classes `h1em`; context: 
264. `peterson-2015-art-language-invention-ch1-sounds.md` page 78: `OEBPS/image/115783.jpg` → `images/peterson-2015-art-language-invention-img-0289-115783.jpg`; classes `h1em`; context: 
265. `peterson-2015-art-language-invention-ch1-sounds.md` page 78: `OEBPS/image/115785.jpg` → `images/peterson-2015-art-language-invention-img-0290-115785.jpg`; classes `h1em`; context: 
266. `peterson-2015-art-language-invention-ch1-sounds.md` page 78: `OEBPS/image/Image71178.jpg` → `images/peterson-2015-art-language-invention-img-0291-image71178.jpg`; classes `h2em`; context: Wa (L) tekaané yáá (H). “I saw you.”
267. `peterson-2015-art-language-invention-ch1-sounds.md` page 78: `OEBPS/image/115789.jpg` → `images/peterson-2015-art-language-invention-img-0292-115789.jpg`; classes `h1em`; context: 
268. `peterson-2015-art-language-invention-ch1-sounds.md` page 78: `OEBPS/image/Image71188.jpg` → `images/peterson-2015-art-language-invention-img-0293-image71188.jpg`; classes `h2em`; context: 
269. `peterson-2015-art-language-invention-ch1-sounds.md` page 78: `OEBPS/image/115791.jpg` → `images/peterson-2015-art-language-invention-img-0294-115791.jpg`; classes `h1em`; context: 
270. `peterson-2015-art-language-invention-ch1-sounds.md` page 90: `OEBPS/image/115793.jpg` → `images/peterson-2015-art-language-invention-img-0299-115793.jpg`; classes `h1em`; context: 
271. `peterson-2015-art-language-invention-ch1-sounds.md` page 91: `OEBPS/image/115795.jpg` → `images/peterson-2015-art-language-invention-img-0300-115795.jpg`; classes `h1em`; context: 
272. `peterson-2015-art-language-invention-ch1-sounds.md` page 91: `OEBPS/image/115797.jpg` → `images/peterson-2015-art-language-invention-img-0301-115797.jpg`; classes `h1em`; context: 
273. `peterson-2015-art-language-invention-ch1-sounds.md` page 91: `OEBPS/image/115799.jpg` → `images/peterson-2015-art-language-invention-img-0302-115799.jpg`; classes `h1em`; context: 
274. `peterson-2015-art-language-invention-ch1-sounds.md` page 91: `OEBPS/image/115805.jpg` → `images/peterson-2015-art-language-invention-img-0303-115805.jpg`; classes `h1em`; context: 
275. `peterson-2015-art-language-invention-ch1-sounds.md` page 91: `OEBPS/image/115807.jpg` → `images/peterson-2015-art-language-invention-img-0304-115807.jpg`; classes `h1em`; context: 
276. `peterson-2015-art-language-invention-ch1-sounds.md` page 92: `OEBPS/image/115809.jpg` → `images/peterson-2015-art-language-invention-img-0307-115809.jpg`; classes `h1em`; context: 
277. `peterson-2015-art-language-invention-ch1-sounds.md` page 92: `OEBPS/image/115811.jpg` → `images/peterson-2015-art-language-invention-img-0308-115811.jpg`; classes `h1em`; context: 
278. `peterson-2015-art-language-invention-ch1-sounds.md` page 92: `OEBPS/image/115813.jpg` → `images/peterson-2015-art-language-invention-img-0309-115813.jpg`; classes `h1em`; context: 
279. `peterson-2015-art-language-invention-ch1-sounds.md` page 92: `OEBPS/image/115815.jpg` → `images/peterson-2015-art-language-invention-img-0310-115815.jpg`; classes `h1em`; context: 
280. `peterson-2015-art-language-invention-ch1-sounds.md` page 93: `OEBPS/image/115818.jpg` → `images/peterson-2015-art-language-invention-img-0311-115818.jpg`; classes `h1em`; context: 
281. `peterson-2015-art-language-invention-ch1-sounds.md` page 93: `OEBPS/image/115820.jpg` → `images/peterson-2015-art-language-invention-img-0312-115820.jpg`; classes `h1em`; context: 
282. `peterson-2015-art-language-invention-ch1-sounds.md` page 93: `OEBPS/image/115822.jpg` → `images/peterson-2015-art-language-invention-img-0313-115822.jpg`; classes `h1em`; context: 
283. `peterson-2015-art-language-invention-ch1-sounds.md` page 93: `OEBPS/image/115824.jpg` → `images/peterson-2015-art-language-invention-img-0314-115824.jpg`; classes `h1em`; context: 
284. `peterson-2015-art-language-invention-ch1-sounds.md` page 93: `OEBPS/image/115826.jpg` → `images/peterson-2015-art-language-invention-img-0315-115826.jpg`; classes `h1em`; context: 
285. `peterson-2015-art-language-invention-ch1-sounds.md` page 93: `OEBPS/image/115829.jpg` → `images/peterson-2015-art-language-invention-img-0316-115829.jpg`; classes `h1em`; context: 
286. `peterson-2015-art-language-invention-ch1-sounds.md` page 93: `OEBPS/image/115831.jpg` → `images/peterson-2015-art-language-invention-img-0317-115831.jpg`; classes `h1em`; context: 
287. `peterson-2015-art-language-invention-ch1-sounds.md` page 93: `OEBPS/image/115833.jpg` → `images/peterson-2015-art-language-invention-img-0318-115833.jpg`; classes `h1em`; context: 
288. `peterson-2015-art-language-invention-ch1-sounds.md` page 93: `OEBPS/image/115835.jpg` → `images/peterson-2015-art-language-invention-img-0319-115835.jpg`; classes `h1em`; context: 
289. `peterson-2015-art-language-invention-ch1-sounds.md` page 93: `OEBPS/image/115838.jpg` → `images/peterson-2015-art-language-invention-img-0320-115838.jpg`; classes `h1em`; context: 
290. `peterson-2015-art-language-invention-ch1-sounds.md` page 94: `OEBPS/image/115840.jpg` → `images/peterson-2015-art-language-invention-img-0322-115840.jpg`; classes `h1em`; context: 
291. `peterson-2015-art-language-invention-ch2-words.md` page 102: `OEBPS/image/115842.jpg` → `images/peterson-2015-art-language-invention-img-0323-115842.jpg`; classes `h1em`; context: 
292. `peterson-2015-art-language-invention-ch2-words.md` page 103: `OEBPS/image/115844.jpg` → `images/peterson-2015-art-language-invention-img-0325-115844.jpg`; classes `h1em`; context: 
293. `peterson-2015-art-language-invention-ch2-words.md` page 103: `OEBPS/image/115846.jpg` → `images/peterson-2015-art-language-invention-img-0326-115846.jpg`; classes `h1em`; context: 
294. `peterson-2015-art-language-invention-ch2-words.md` page 103: `OEBPS/image/115848.jpg` → `images/peterson-2015-art-language-invention-img-0327-115848.jpg`; classes `h1em`; context: 
295. `peterson-2015-art-language-invention-ch2-words.md` page 104: `OEBPS/image/115850.jpg` → `images/peterson-2015-art-language-invention-img-0328-115850.jpg`; classes `h1em`; context: 
296. `peterson-2015-art-language-invention-ch2-words.md` page 104: `OEBPS/image/115856.jpg` → `images/peterson-2015-art-language-invention-img-0329-115856.jpg`; classes `h1em`; context: 
297. `peterson-2015-art-language-invention-ch2-words.md` page 106: `OEBPS/image/115858.jpg` → `images/peterson-2015-art-language-invention-img-0330-115858.jpg`; classes `h1em`; context: 
298. `peterson-2015-art-language-invention-ch2-words.md` page 106: `OEBPS/image/115860.jpg` → `images/peterson-2015-art-language-invention-img-0331-115860.jpg`; classes `h1em`; context: Daenerys Jelmāzmo aō naejot dēmas . . .
299. `peterson-2015-art-language-invention-ch2-words.md` page 108: `OEBPS/image/115862.jpg` → `images/peterson-2015-art-language-invention-img-0332-115862.jpg`; classes `h1em`; context: 
300. `peterson-2015-art-language-invention-ch2-words.md` page 108: `OEBPS/image/115864.jpg` → `images/peterson-2015-art-language-invention-img-0333-115864.jpg`; classes `h1em`; context: 
301. `peterson-2015-art-language-invention-ch2-words.md` page 108: `OEBPS/image/115866.jpg` → `images/peterson-2015-art-language-invention-img-0334-115866.jpg`; classes `h1em`; context: 
302. `peterson-2015-art-language-invention-ch2-words.md` page 108: `OEBPS/image/115868.jpg` → `images/peterson-2015-art-language-invention-img-0335-115868.jpg`; classes `h1em`; context: 
303. `peterson-2015-art-language-invention-ch2-words.md` page 108: `OEBPS/image/davidy.jpg` → `images/peterson-2015-art-language-invention-img-0336-davidy.jpg`; classes `h1em`; context: 
304. `peterson-2015-art-language-invention-ch2-words.md` page 108: `OEBPS/image/115870.jpg` → `images/peterson-2015-art-language-invention-img-0337-115870.jpg`; classes `h1em`; context: 
305. `peterson-2015-art-language-invention-ch2-words.md` page 108: `OEBPS/image/115872.jpg` → `images/peterson-2015-art-language-invention-img-0338-115872.jpg`; classes `h1em`; context: 
306. `peterson-2015-art-language-invention-ch2-words.md` page 108: `OEBPS/image/115874.jpg` → `images/peterson-2015-art-language-invention-img-0339-115874.jpg`; classes `h1em`; context: 
307. `peterson-2015-art-language-invention-ch2-words.md` page 108: `OEBPS/image/davidy.jpg` → `images/peterson-2015-art-language-invention-img-0336-davidy.jpg`; classes `h1em`; context: kēli dēmas
308. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/121915.jpg` → `images/peterson-2015-art-language-invention-img-0341-121915.jpg`; classes `h1em`; context: • No Marking : Some languages make no morphological distinction between singular and plural outside of a couple instances. Nouns in Mandarin Chinese are neither singular nor plural
309. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/121917.jpg` → `images/peterson-2015-art-language-invention-img-0342-121917.jpg`; classes `h1em`; context: 
310. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/wo.jpg` → `images/peterson-2015-art-language-invention-img-0343-wo.jpg`; classes `h1em`; context: • No Marking : Some languages make no morphological distinction between singular and plural outside of a couple instances. Nouns in Mandarin Chinese are neither singular nor plural
311. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/121919.jpg` → `images/peterson-2015-art-language-invention-img-0344-121919.jpg`; classes `h1em`; context: 
312. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/ni.jpg` → `images/peterson-2015-art-language-invention-img-0272-ni.jpg`; classes `h1em`; context: • No Marking : Some languages make no morphological distinction between singular and plural outside of a couple instances. Nouns in Mandarin Chinese are neither singular nor plural
313. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/121921.jpg` → `images/peterson-2015-art-language-invention-img-0345-121921.jpg`; classes `h1em`; context: 
314. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/115876.jpg` → `images/peterson-2015-art-language-invention-img-0346-115876.jpg`; classes `h1em`; context: 
315. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/women.jpg` → `images/peterson-2015-art-language-invention-img-0347-women.jpg`; classes `h1em`; context: • No Marking : Some languages make no morphological distinction between singular and plural outside of a couple instances. Nouns in Mandarin Chinese are neither singular nor plural
316. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/115878.jpg` → `images/peterson-2015-art-language-invention-img-0348-115878.jpg`; classes `h1em`; context: 
317. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/nimen.jpg` → `images/peterson-2015-art-language-invention-img-0349-nimen.jpg`; classes `h1em`; context: • No Marking : Some languages make no morphological distinction between singular and plural outside of a couple instances. Nouns in Mandarin Chinese are neither singular nor plural
318. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/115880.jpg` → `images/peterson-2015-art-language-invention-img-0350-115880.jpg`; classes `h1em`; context: 
319. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/Image72465.jpg` → `images/peterson-2015-art-language-invention-img-0351-image72465.jpg`; classes `h1em`; context: 
320. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/115883.jpg` → `images/peterson-2015-art-language-invention-img-0352-115883.jpg`; classes `h1em`; context: 
321. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/Image72475.jpg` → `images/peterson-2015-art-language-invention-img-0353-image72475.jpg`; classes `h1em`; context: 
322. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/115885.jpg` → `images/peterson-2015-art-language-invention-img-0354-115885.jpg`; classes `h1em`; context: 
323. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/Image72489.jpg` → `images/peterson-2015-art-language-invention-img-0355-image72489.jpg`; classes `h1em`; context: 
324. `peterson-2015-art-language-invention-ch2-words.md` page 109: `OEBPS/image/115891.jpg` → `images/peterson-2015-art-language-invention-img-0356-115891.jpg`; classes `h1em`; context: 
325. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/Image72498.jpg` → `images/peterson-2015-art-language-invention-img-0357-image72498.jpg`; classes `h1em`; context: 
326. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115893.jpg` → `images/peterson-2015-art-language-invention-img-0358-115893.jpg`; classes `h1em`; context: 
327. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/Image72511.jpg` → `images/peterson-2015-art-language-invention-img-0359-image72511.jpg`; classes `h1em`; context: 
328. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115895.jpg` → `images/peterson-2015-art-language-invention-img-0360-115895.jpg`; classes `h1em`; context: 
329. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/Image72525.jpg` → `images/peterson-2015-art-language-invention-img-0361-image72525.jpg`; classes `h1em`; context: 
330. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115897.jpg` → `images/peterson-2015-art-language-invention-img-0362-115897.jpg`; classes `h1em`; context: 
331. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/Image72538.jpg` → `images/peterson-2015-art-language-invention-img-0363-image72538.jpg`; classes `h1em`; context: 
332. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115899.jpg` → `images/peterson-2015-art-language-invention-img-0364-115899.jpg`; classes `h1em`; context: 
333. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115901.jpg` → `images/peterson-2015-art-language-invention-img-0365-115901.jpg`; classes `h1em`; context: 
334. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115903.jpg` → `images/peterson-2015-art-language-invention-img-0366-115903.jpg`; classes `h1em`; context: 
335. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115905.jpg` → `images/peterson-2015-art-language-invention-img-0367-115905.jpg`; classes `h1em`; context: 
336. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115907.jpg` → `images/peterson-2015-art-language-invention-img-0368-115907.jpg`; classes `h1em`; context: 
337. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115909.jpg` → `images/peterson-2015-art-language-invention-img-0369-115909.jpg`; classes `h1em`; context: 
338. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115914.jpg` → `images/peterson-2015-art-language-invention-img-0370-115914.jpg`; classes `h1em`; context: 
339. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/Image72553.jpg` → `images/peterson-2015-art-language-invention-img-0371-image72553.jpg`; classes `h1em`; context: 
340. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115916.jpg` → `images/peterson-2015-art-language-invention-img-0372-115916.jpg`; classes `h1em`; context: 
341. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/Image72563.jpg` → `images/peterson-2015-art-language-invention-img-0373-image72563.jpg`; classes `h1em`; context: 
342. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115918.jpg` → `images/peterson-2015-art-language-invention-img-0374-115918.jpg`; classes `h1em`; context: 
343. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115920.jpg` → `images/peterson-2015-art-language-invention-img-0375-115920.jpg`; classes `h1em`; context: 
344. `peterson-2015-art-language-invention-ch2-words.md` page 110: `OEBPS/image/115923.jpg` → `images/peterson-2015-art-language-invention-img-0376-115923.jpg`; classes `h1em`; context: 
345. `peterson-2015-art-language-invention-ch2-words.md` page 113: `OEBPS/image/115925.jpg` → `images/peterson-2015-art-language-invention-img-0381-115925.jpg`; classes `h1em`; context: 
346. `peterson-2015-art-language-invention-ch2-words.md` page 113: `OEBPS/image/115927.jpg` → `images/peterson-2015-art-language-invention-img-0382-115927.jpg`; classes `h1em`; context: 
347. `peterson-2015-art-language-invention-ch2-words.md` page 113: `OEBPS/image/115929.jpg` → `images/peterson-2015-art-language-invention-img-0383-115929.jpg`; classes `h1em`; context: 
348. `peterson-2015-art-language-invention-ch2-words.md` page 119: `OEBPS/image/115931.jpg` → `images/peterson-2015-art-language-invention-img-0387-115931.jpg`; classes `h1em`; context: 
349. `peterson-2015-art-language-invention-ch2-words.md` page 119: `OEBPS/image/115935.jpg` → `images/peterson-2015-art-language-invention-img-0388-115935.jpg`; classes `h1em`; context: 
350. `peterson-2015-art-language-invention-ch2-words.md` page 119: `OEBPS/image/115937.jpg` → `images/peterson-2015-art-language-invention-img-0389-115937.jpg`; classes `h1em`; context: 2. Gender + Number : In Swahili, every noun has a prefix that tells you its gender and number, for example, mgeni “stranger” versus wageni “strangers” (compare kigeni “strangeness”
351. `peterson-2015-art-language-invention-ch2-words.md` page 121: `OEBPS/image/115939.jpg` → `images/peterson-2015-art-language-invention-img-0391-115939.jpg`; classes `h1em`; context: 
352. `peterson-2015-art-language-invention-ch2-words.md` page 121: `OEBPS/image/115941.jpg` → `images/peterson-2015-art-language-invention-img-0392-115941.jpg`; classes `h1em`; context: 
353. `peterson-2015-art-language-invention-ch2-words.md` page 123: `OEBPS/image/hindi_man_saw_laborer.jpg` → `images/peterson-2015-art-language-invention-img-0395-hindi-man-saw-laborer.jpg`; classes `h1em`; context: 
354. `peterson-2015-art-language-invention-ch2-words.md` page 123: `OEBPS/image/115943.jpg` → `images/peterson-2015-art-language-invention-img-0396-115943.jpg`; classes `h1em`; context: 
355. `peterson-2015-art-language-invention-ch2-words.md` page 123: `OEBPS/image/hindi_laborer_saw_man.jpg` → `images/peterson-2015-art-language-invention-img-0397-hindi-laborer-saw-man.jpg`; classes `h1em`; context: 
356. `peterson-2015-art-language-invention-ch2-words.md` page 123: `OEBPS/image/115945.jpg` → `images/peterson-2015-art-language-invention-img-0398-115945.jpg`; classes `h1em`; context: 
357. `peterson-2015-art-language-invention-ch2-words.md` page 124: `OEBPS/image/115947.jpg` → `images/peterson-2015-art-language-invention-img-0399-115947.jpg`; classes `h1em`; context: 
358. `peterson-2015-art-language-invention-ch2-words.md` page 124: `OEBPS/image/115949.jpg` → `images/peterson-2015-art-language-invention-img-0400-115949.jpg`; classes `h1em`; context: 
359. `peterson-2015-art-language-invention-ch2-words.md` page 124: `OEBPS/image/115951.jpg` → `images/peterson-2015-art-language-invention-img-0401-115951.jpg`; classes `h1em`; context: 
360. `peterson-2015-art-language-invention-ch2-words.md` page 124: `OEBPS/image/115953.jpg` → `images/peterson-2015-art-language-invention-img-0402-115953.jpg`; classes `h1em`; context: 
361. `peterson-2015-art-language-invention-ch2-words.md` page 124: `OEBPS/image/115956.jpg` → `images/peterson-2015-art-language-invention-img-0403-115956.jpg`; classes `h1em`; context: 
362. `peterson-2015-art-language-invention-ch2-words.md` page 124: `OEBPS/image/115958.jpg` → `images/peterson-2015-art-language-invention-img-0404-115958.jpg`; classes `h1em`; context: 
363. `peterson-2015-art-language-invention-ch2-words.md` page 124: `OEBPS/image/115961.jpg` → `images/peterson-2015-art-language-invention-img-0405-115961.jpg`; classes `h1em`; context: 
364. `peterson-2015-art-language-invention-ch2-words.md` page 124: `OEBPS/image/115963.jpg` → `images/peterson-2015-art-language-invention-img-0406-115963.jpg`; classes `h1em`; context: 
365. `peterson-2015-art-language-invention-ch2-words.md` page 124: `OEBPS/image/115965.jpg` → `images/peterson-2015-art-language-invention-img-0407-115965.jpg`; classes `h1em`; context: 
366. `peterson-2015-art-language-invention-ch2-words.md` page 124: `OEBPS/image/115967.jpg` → `images/peterson-2015-art-language-invention-img-0408-115967.jpg`; classes `h1em`; context: 
367. `peterson-2015-art-language-invention-ch2-words.md` page 124: `OEBPS/image/115969.jpg` → `images/peterson-2015-art-language-invention-img-0409-115969.jpg`; classes `h1em`; context: 
368. `peterson-2015-art-language-invention-ch2-words.md` page 126: `OEBPS/image/Art_377_AOLI.jpg` → `images/peterson-2015-art-language-invention-img-0412-art-377-aoli.jpg`; classes `h1em`; context: 
369. `peterson-2015-art-language-invention-ch2-words.md` page 126: `OEBPS/image/Art_378_AOLI.jpg` → `images/peterson-2015-art-language-invention-img-0413-art-378-aoli.jpg`; classes `h1em`; context: 
370. `peterson-2015-art-language-invention-ch2-words.md` page 127: `OEBPS/image/Image73369.jpg` → `images/peterson-2015-art-language-invention-img-0416-image73369.jpg`; classes `h1em`; context: 
371. `peterson-2015-art-language-invention-ch2-words.md` page 127: `OEBPS/image/Image73382.jpg` → `images/peterson-2015-art-language-invention-img-0417-image73382.jpg`; classes `h1em`; context: 
372. `peterson-2015-art-language-invention-ch2-words.md` page 128: `OEBPS/image/Image73396.jpg` → `images/peterson-2015-art-language-invention-img-0418-image73396.jpg`; classes `h1em`; context: 
373. `peterson-2015-art-language-invention-ch2-words.md` page 128: `OEBPS/image/115971.jpg` → `images/peterson-2015-art-language-invention-img-0419-115971.jpg`; classes `h1em`; context: 
374. `peterson-2015-art-language-invention-ch2-words.md` page 128: `OEBPS/image/Image73411.jpg` → `images/peterson-2015-art-language-invention-img-0420-image73411.jpg`; classes `h1em`; context: 
375. `peterson-2015-art-language-invention-ch2-words.md` page 128: `OEBPS/image/115973.jpg` → `images/peterson-2015-art-language-invention-img-0421-115973.jpg`; classes `h1em`; context: 
376. `peterson-2015-art-language-invention-ch2-words.md` page 128: `OEBPS/image/Art_379_AOLI.jpg` → `images/peterson-2015-art-language-invention-img-0422-art-379-aoli.jpg`; classes `h1em`; context: 
377. `peterson-2015-art-language-invention-ch2-words.md` page 128: `OEBPS/image/115975.jpg` → `images/peterson-2015-art-language-invention-img-0423-115975.jpg`; classes `h1em`; context: 
378. `peterson-2015-art-language-invention-ch2-words.md` page 128: `OEBPS/image/Art_380_AOLI.jpg` → `images/peterson-2015-art-language-invention-img-0424-art-380-aoli.jpg`; classes `h1em`; context: 
379. `peterson-2015-art-language-invention-ch2-words.md` page 128: `OEBPS/image/115977.jpg` → `images/peterson-2015-art-language-invention-img-0425-115977.jpg`; classes `h1em`; context: 
380. `peterson-2015-art-language-invention-ch2-words.md` page 129: `OEBPS/image/Art_381_AOLI.jpg` → `images/peterson-2015-art-language-invention-img-0426-art-381-aoli.jpg`; classes `h1em`; context: 
381. `peterson-2015-art-language-invention-ch2-words.md` page 129: `OEBPS/image/115981.jpg` → `images/peterson-2015-art-language-invention-img-0427-115981.jpg`; classes `h1em`; context: 
382. `peterson-2015-art-language-invention-ch2-words.md` page 129: `OEBPS/image/Image73431.jpg` → `images/peterson-2015-art-language-invention-img-0428-image73431.jpg`; classes `h1em`; context: 
383. `peterson-2015-art-language-invention-ch2-words.md` page 129: `OEBPS/image/115983.jpg` → `images/peterson-2015-art-language-invention-img-0429-115983.jpg`; classes `h1em`; context: 
384. `peterson-2015-art-language-invention-ch2-words.md` page 130: `OEBPS/image/Image73526.jpg` → `images/peterson-2015-art-language-invention-img-0431-image73526.jpg`; classes `h2em`; context: 
385. `peterson-2015-art-language-invention-ch2-words.md` page 130: `OEBPS/image/115985.jpg` → `images/peterson-2015-art-language-invention-img-0432-115985.jpg`; classes `h1em`; context: Koraksut arkonyu chewtlen . ( arkon “boat,” absolutive)
386. `peterson-2015-art-language-invention-ch2-words.md` page 130: `OEBPS/image/Art_382_AOLI.jpg` → `images/peterson-2015-art-language-invention-img-0433-art-382-aoli.jpg`; classes `h1em`; context: 
387. `peterson-2015-art-language-invention-ch2-words.md` page 130: `OEBPS/image/115987.jpg` → `images/peterson-2015-art-language-invention-img-0434-115987.jpg`; classes `h1em`; context: 
388. `peterson-2015-art-language-invention-ch2-words.md` page 131: `OEBPS/image/115989.jpg` → `images/peterson-2015-art-language-invention-img-0435-115989.jpg`; classes `h1em`; context: 
389. `peterson-2015-art-language-invention-ch2-words.md` page 131: `OEBPS/image/115991.jpg` → `images/peterson-2015-art-language-invention-img-0436-115991.jpg`; classes `h1em`; context: 
390. `peterson-2015-art-language-invention-ch2-words.md` page 131: `OEBPS/image/Art_383_AOLI.jpg` → `images/peterson-2015-art-language-invention-img-0437-art-383-aoli.jpg`; classes `h1em`; context: 
391. `peterson-2015-art-language-invention-ch2-words.md` page 131: `OEBPS/image/115993.jpg` → `images/peterson-2015-art-language-invention-img-0438-115993.jpg`; classes `h1em`; context: 
392. `peterson-2015-art-language-invention-ch2-words.md` page 131: `OEBPS/image/Art_384_AOLI.jpg` → `images/peterson-2015-art-language-invention-img-0439-art-384-aoli.jpg`; classes `h1em`; context: 
393. `peterson-2015-art-language-invention-ch2-words.md` page 131: `OEBPS/image/115995.jpg` → `images/peterson-2015-art-language-invention-img-0440-115995.jpg`; classes `h1em`; context: 
394. `peterson-2015-art-language-invention-ch2-words.md` page 132: `OEBPS/image/Art_385_AOLI.jpg` → `images/peterson-2015-art-language-invention-img-0441-art-385-aoli.jpg`; classes `h1em`; context: 
395. `peterson-2015-art-language-invention-ch2-words.md` page 132: `OEBPS/image/115997.jpg` → `images/peterson-2015-art-language-invention-img-0442-115997.jpg`; classes `h1em`; context: 
396. `peterson-2015-art-language-invention-ch2-words.md` page 146: `OEBPS/image/Image74518.jpg` → `images/peterson-2015-art-language-invention-img-0458-image74518.jpg`; classes `h1em`; context: Ka lalau ei ie hate aeiu kava. / PST throw 1SG OBJ -DEF onion into fire/
397. `peterson-2015-art-language-invention-ch2-words.md` page 146: `OEBPS/image/Image74527.jpg` → `images/peterson-2015-art-language-invention-img-0459-image74527.jpg`; classes `h1em`; context: 
398. `peterson-2015-art-language-invention-ch2-words.md` page 146: `OEBPS/image/Image74540.jpg` → `images/peterson-2015-art-language-invention-img-0460-image74540.jpg`; classes `h1em`; context: 
399. `peterson-2015-art-language-invention-ch2-words.md` page 146: `OEBPS/image/Image74554.jpg` → `images/peterson-2015-art-language-invention-img-0461-image74554.jpg`; classes `h1em`; context: 
400. `peterson-2015-art-language-invention-ch2-words.md` page 147: `OEBPS/image/Image74567.jpg` → `images/peterson-2015-art-language-invention-img-0462-image74567.jpg`; classes `h1em`; context: 
401. `peterson-2015-art-language-invention-ch2-words.md` page 147: `OEBPS/image/Image74582.jpg` → `images/peterson-2015-art-language-invention-img-0463-image74582.jpg`; classes `h1em`; context: 
402. `peterson-2015-art-language-invention-ch2-words.md` page 147: `OEBPS/image/Image74597.jpg` → `images/peterson-2015-art-language-invention-img-0464-image74597.jpg`; classes `h1em`; context: 
403. `peterson-2015-art-language-invention-ch2-words.md` page 147: `OEBPS/image/Image74610.jpg` → `images/peterson-2015-art-language-invention-img-0465-image74610.jpg`; classes `h1em`; context: 
404. `peterson-2015-art-language-invention-ch2-words.md` page 147: `OEBPS/image/Image74623.jpg` → `images/peterson-2015-art-language-invention-img-0466-image74623.jpg`; classes `h1em`; context: 
405. `peterson-2015-art-language-invention-ch2-words.md` page 147: `OEBPS/image/Image74638.jpg` → `images/peterson-2015-art-language-invention-img-0467-image74638.jpg`; classes `h1em`; context: 
406. `peterson-2015-art-language-invention-ch2-words.md` page 147: `OEBPS/image/Image74653.jpg` → `images/peterson-2015-art-language-invention-img-0468-image74653.jpg`; classes `h1em`; context: 
407. `peterson-2015-art-language-invention-ch2-words.md` page 151: `OEBPS/image/Image74864.jpg` → `images/peterson-2015-art-language-invention-img-0472-image74864.jpg`; classes `h1em`; context: 
408. `peterson-2015-art-language-invention-ch2-words.md` page 151: `OEBPS/image/Image74878.jpg` → `images/peterson-2015-art-language-invention-img-0473-image74878.jpg`; classes `h1em`; context: 
409. `peterson-2015-art-language-invention-ch2-words.md` page 151: `OEBPS/image/Image74891.jpg` → `images/peterson-2015-art-language-invention-img-0474-image74891.jpg`; classes `h1em`; context: 
410. `peterson-2015-art-language-invention-ch2-words.md` page 154: `OEBPS/image/116002.jpg` → `images/peterson-2015-art-language-invention-img-0476-116002.jpg`; classes `h1em`; context: Zahon hudi zvoshakte
411. `peterson-2015-art-language-invention-ch2-words.md` page 154: `OEBPS/image/116002.jpg` → `images/peterson-2015-art-language-invention-img-0476-116002.jpg`; classes `h1em`; context: 
412. `peterson-2015-art-language-invention-ch2-words.md` page 154: `OEBPS/image/116002.jpg` → `images/peterson-2015-art-language-invention-img-0476-116002.jpg`; classes `h1em`; context: 
413. `peterson-2015-art-language-invention-ch2-words.md` page 155: `OEBPS/image/116006.jpg` → `images/peterson-2015-art-language-invention-img-0477-116006.jpg`; classes `h1em`; context: 
414. `peterson-2015-art-language-invention-ch2-words.md` page 155: `OEBPS/image/116008.jpg` → `images/peterson-2015-art-language-invention-img-0478-116008.jpg`; classes `h1em`; context: 
415. `peterson-2015-art-language-invention-ch2-words.md` page 155: `OEBPS/image/116011.jpg` → `images/peterson-2015-art-language-invention-img-0480-116011.jpg`; classes `h1em`; context: 
416. `peterson-2015-art-language-invention-ch2-words.md` page 156: `OEBPS/image/116013.jpg` → `images/peterson-2015-art-language-invention-img-0481-116013.jpg`; classes `h1em`; context: 
417. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75257.jpg` → `images/peterson-2015-art-language-invention-img-0485-image75257.jpg`; classes `h1em`; context: 
418. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75272.jpg` → `images/peterson-2015-art-language-invention-img-0486-image75272.jpg`; classes `h1em`; context: 
419. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75292.jpg` → `images/peterson-2015-art-language-invention-img-0487-image75292.jpg`; classes `h1em`; context: 
420. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75306.jpg` → `images/peterson-2015-art-language-invention-img-0488-image75306.jpg`; classes `h1em`; context: 
421. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75319.jpg` → `images/peterson-2015-art-language-invention-img-0489-image75319.jpg`; classes `h1em`; context: 
422. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75333.jpg` → `images/peterson-2015-art-language-invention-img-0490-image75333.jpg`; classes `h1em`; context: 
423. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75346.jpg` → `images/peterson-2015-art-language-invention-img-0491-image75346.jpg`; classes `h1em`; context: 
424. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75361.jpg` → `images/peterson-2015-art-language-invention-img-0492-image75361.jpg`; classes `h1em`; context: 
425. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75376.jpg` → `images/peterson-2015-art-language-invention-img-0493-image75376.jpg`; classes `h1em`; context: 
426. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75389.jpg` → `images/peterson-2015-art-language-invention-img-0494-image75389.jpg`; classes `h1em`; context: 
427. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75402.jpg` → `images/peterson-2015-art-language-invention-img-0495-image75402.jpg`; classes `h1em`; context: 
428. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75416.jpg` → `images/peterson-2015-art-language-invention-img-0496-image75416.jpg`; classes `h1em`; context: 
429. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75431.jpg` → `images/peterson-2015-art-language-invention-img-0497-image75431.jpg`; classes `h1em`; context: 
430. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75450.jpg` → `images/peterson-2015-art-language-invention-img-0498-image75450.jpg`; classes `h1em`; context: 
431. `peterson-2015-art-language-invention-ch2-words.md` page 157: `OEBPS/image/Image75464.jpg` → `images/peterson-2015-art-language-invention-img-0499-image75464.jpg`; classes `h1em`; context: 
432. `peterson-2015-art-language-invention-ch2-words.md` page 158: `OEBPS/image/Image75477.jpg` → `images/peterson-2015-art-language-invention-img-0500-image75477.jpg`; classes `h1em`; context: 
433. `peterson-2015-art-language-invention-ch2-words.md` page 158: `OEBPS/image/Image75491.jpg` → `images/peterson-2015-art-language-invention-img-0501-image75491.jpg`; classes `h1em`; context: 
434. `peterson-2015-art-language-invention-ch2-words.md` page 158: `OEBPS/image/Image75504.jpg` → `images/peterson-2015-art-language-invention-img-0502-image75504.jpg`; classes `h1em`; context: 
435. `peterson-2015-art-language-invention-ch2-words.md` page 158: `OEBPS/image/Image75519.jpg` → `images/peterson-2015-art-language-invention-img-0503-image75519.jpg`; classes `h1em`; context: 
436. `peterson-2015-art-language-invention-ch2-words.md` page 158: `OEBPS/image/116015.jpg` → `images/peterson-2015-art-language-invention-img-0504-116015.jpg`; classes `h1em`; context: 
437. `peterson-2015-art-language-invention-ch2-words.md` page 158: `OEBPS/image/Image75534.jpg` → `images/peterson-2015-art-language-invention-img-0505-image75534.jpg`; classes `h1em`; context: 
438. `peterson-2015-art-language-invention-ch2-words.md` page 158: `OEBPS/image/Image75547.jpg` → `images/peterson-2015-art-language-invention-img-0506-image75547.jpg`; classes `h1em`; context: 
439. `peterson-2015-art-language-invention-ch2-words.md` page 158: `OEBPS/image/Image75560.jpg` → `images/peterson-2015-art-language-invention-img-0507-image75560.jpg`; classes `h1em`; context: 
440. `peterson-2015-art-language-invention-ch2-words.md` page 158: `OEBPS/image/Image75574.jpg` → `images/peterson-2015-art-language-invention-img-0508-image75574.jpg`; classes `h1em`; context: 
441. `peterson-2015-art-language-invention-ch2-words.md` page 158: `OEBPS/image/Image75590.jpg` → `images/peterson-2015-art-language-invention-img-0509-image75590.jpg`; classes `h1em`; context: 
442. `peterson-2015-art-language-invention-ch3-evolution.md` page 159: `OEBPS/image/116017.jpg` → `images/peterson-2015-art-language-invention-img-0510-116017.jpg`; classes `h1em`; context: 
443. `peterson-2015-art-language-invention-ch3-evolution.md` page 159: `OEBPS/image/116019.jpg` → `images/peterson-2015-art-language-invention-img-0511-116019.jpg`; classes `h1em`; context: 
444. `peterson-2015-art-language-invention-ch3-evolution.md` page 160: `OEBPS/image/116021.jpg` → `images/peterson-2015-art-language-invention-img-0512-116021.jpg`; classes `h1em`; context: 
445. `peterson-2015-art-language-invention-ch3-evolution.md` page 160: `OEBPS/image/116023.jpg` → `images/peterson-2015-art-language-invention-img-0513-116023.jpg`; classes `h1em`; context: 
446. `peterson-2015-art-language-invention-ch3-evolution.md` page 160: `OEBPS/image/116024.jpg` → `images/peterson-2015-art-language-invention-img-0514-116024.jpg`; classes `h1em`; context: 
447. `peterson-2015-art-language-invention-ch3-evolution.md` page 160: `OEBPS/image/116027.jpg` → `images/peterson-2015-art-language-invention-img-0515-116027.jpg`; classes `h1em`; context: 
448. `peterson-2015-art-language-invention-ch3-evolution.md` page 160: `OEBPS/image/116029.jpg` → `images/peterson-2015-art-language-invention-img-0516-116029.jpg`; classes `h1em`; context: 
449. `peterson-2015-art-language-invention-ch3-evolution.md` page 160: `OEBPS/image/116031.jpg` → `images/peterson-2015-art-language-invention-img-0517-116031.jpg`; classes `h1em`; context: 
450. `peterson-2015-art-language-invention-ch3-evolution.md` page 160: `OEBPS/image/116037.jpg` → `images/peterson-2015-art-language-invention-img-0518-116037.jpg`; classes `h1em`; context: 
451. `peterson-2015-art-language-invention-ch3-evolution.md` page 160: `OEBPS/image/116039.jpg` → `images/peterson-2015-art-language-invention-img-0519-116039.jpg`; classes `h1em`; context: 
452. `peterson-2015-art-language-invention-ch3-evolution.md` page 160: `OEBPS/image/116042.jpg` → `images/peterson-2015-art-language-invention-img-0520-116042.jpg`; classes `h1em`; context: 
453. `peterson-2015-art-language-invention-ch3-evolution.md` page 160: `OEBPS/image/Image75610.jpg` → `images/peterson-2015-art-language-invention-img-0521-image75610.jpg`; classes `h1em`; context: 
454. `peterson-2015-art-language-invention-ch3-evolution.md` page 160: `OEBPS/image/116044.jpg` → `images/peterson-2015-art-language-invention-img-0522-116044.jpg`; classes `h1em`; context: 
455. `peterson-2015-art-language-invention-ch3-evolution.md` page 161: `OEBPS/image/116046.jpg` → `images/peterson-2015-art-language-invention-img-0523-116046.jpg`; classes `h1em`; context: 
456. `peterson-2015-art-language-invention-ch3-evolution.md` page 161: `OEBPS/image/Image75624.jpg` → `images/peterson-2015-art-language-invention-img-0524-image75624.jpg`; classes `h1em`; context: 
457. `peterson-2015-art-language-invention-ch3-evolution.md` page 161: `OEBPS/image/116048.jpg` → `images/peterson-2015-art-language-invention-img-0525-116048.jpg`; classes `h1em`; context: 
458. `peterson-2015-art-language-invention-ch3-evolution.md` page 162: `OEBPS/image/116050.jpg` → `images/peterson-2015-art-language-invention-img-0526-116050.jpg`; classes `h1em`; context: 
459. `peterson-2015-art-language-invention-ch3-evolution.md` page 162: `OEBPS/image/116052.jpg` → `images/peterson-2015-art-language-invention-img-0527-116052.jpg`; classes `h1em`; context: 
460. `peterson-2015-art-language-invention-ch3-evolution.md` page 162: `OEBPS/image/Image75637.jpg` → `images/peterson-2015-art-language-invention-img-0528-image75637.jpg`; classes `h1em`; context: 
461. `peterson-2015-art-language-invention-ch3-evolution.md` page 164: `OEBPS/image/116054.jpg` → `images/peterson-2015-art-language-invention-img-0529-116054.jpg`; classes `h1em`; context: 
462. `peterson-2015-art-language-invention-ch3-evolution.md` page 164: `OEBPS/image/116056.jpg` → `images/peterson-2015-art-language-invention-img-0530-116056.jpg`; classes `h1em`; context: 
463. `peterson-2015-art-language-invention-ch3-evolution.md` page 164: `OEBPS/image/116058.jpg` → `images/peterson-2015-art-language-invention-img-0531-116058.jpg`; classes `h1em`; context: 
464. `peterson-2015-art-language-invention-ch3-evolution.md` page 165: `OEBPS/image/116060.jpg` → `images/peterson-2015-art-language-invention-img-0533-116060.jpg`; classes `h1em`; context: 
465. `peterson-2015-art-language-invention-ch3-evolution.md` page 165: `OEBPS/image/116062.jpg` → `images/peterson-2015-art-language-invention-img-0534-116062.jpg`; classes `h1em`; context: 
466. `peterson-2015-art-language-invention-ch3-evolution.md` page 166: `OEBPS/image/116064.jpg` → `images/peterson-2015-art-language-invention-img-0535-116064.jpg`; classes `h1em`; context: 
467. `peterson-2015-art-language-invention-ch3-evolution.md` page 166: `OEBPS/image/116066.jpg` → `images/peterson-2015-art-language-invention-img-0536-116066.jpg`; classes `h1em`; context: 
468. `peterson-2015-art-language-invention-ch3-evolution.md` page 167: `OEBPS/image/116068.jpg` → `images/peterson-2015-art-language-invention-img-0537-116068.jpg`; classes `h1em`; context: 
469. `peterson-2015-art-language-invention-ch3-evolution.md` page 167: `OEBPS/image/116070.jpg` → `images/peterson-2015-art-language-invention-img-0538-116070.jpg`; classes `h1em`; context: 
470. `peterson-2015-art-language-invention-ch3-evolution.md` page 167: `OEBPS/image/116074.jpg` → `images/peterson-2015-art-language-invention-img-0539-116074.jpg`; classes `h1em`; context: 
471. `peterson-2015-art-language-invention-ch3-evolution.md` page 167: `OEBPS/image/116077.jpg` → `images/peterson-2015-art-language-invention-img-0540-116077.jpg`; classes `h1em`; context: 
472. `peterson-2015-art-language-invention-ch3-evolution.md` page 167: `OEBPS/image/116079.jpg` → `images/peterson-2015-art-language-invention-img-0541-116079.jpg`; classes `h1em`; context: 
473. `peterson-2015-art-language-invention-ch3-evolution.md` page 167: `OEBPS/image/116081.jpg` → `images/peterson-2015-art-language-invention-img-0542-116081.jpg`; classes `h1em`; context: 
474. `peterson-2015-art-language-invention-ch3-evolution.md` page 167: `OEBPS/image/116083.jpg` → `images/peterson-2015-art-language-invention-img-0543-116083.jpg`; classes `h1em`; context: 
475. `peterson-2015-art-language-invention-ch3-evolution.md` page 167: `OEBPS/image/116085.jpg` → `images/peterson-2015-art-language-invention-img-0544-116085.jpg`; classes `h1em`; context: 
476. `peterson-2015-art-language-invention-ch3-evolution.md` page 167: `OEBPS/image/116087.jpg` → `images/peterson-2015-art-language-invention-img-0545-116087.jpg`; classes `h1em`; context: 
477. `peterson-2015-art-language-invention-ch3-evolution.md` page 168: `OEBPS/image/116089.jpg` → `images/peterson-2015-art-language-invention-img-0546-116089.jpg`; classes `h1em`; context: 
478. `peterson-2015-art-language-invention-ch3-evolution.md` page 168: `OEBPS/image/116091.jpg` → `images/peterson-2015-art-language-invention-img-0547-116091.jpg`; classes `h1em`; context: 
479. `peterson-2015-art-language-invention-ch3-evolution.md` page 168: `OEBPS/image/116093.jpg` → `images/peterson-2015-art-language-invention-img-0548-116093.jpg`; classes `h1em`; context: 
480. `peterson-2015-art-language-invention-ch3-evolution.md` page 168: `OEBPS/image/116095.jpg` → `images/peterson-2015-art-language-invention-img-0549-116095.jpg`; classes `h1em`; context: 
481. `peterson-2015-art-language-invention-ch3-evolution.md` page 168: `OEBPS/image/V.jpg` → `images/peterson-2015-art-language-invention-img-0551-v.jpg`; classes `h1em`; context: ]
482. `peterson-2015-art-language-invention-ch3-evolution.md` page 169: `OEBPS/image/V.jpg` → `images/peterson-2015-art-language-invention-img-0551-v.jpg`; classes `h1em`; context: [v, ð, ]
483. `peterson-2015-art-language-invention-ch3-evolution.md` page 169: `OEBPS/image/116097.jpg` → `images/peterson-2015-art-language-invention-img-0553-116097.jpg`; classes `h1em`; context: 
484. `peterson-2015-art-language-invention-ch3-evolution.md` page 169: `OEBPS/image/116099.jpg` → `images/peterson-2015-art-language-invention-img-0555-116099.jpg`; classes `h1em`; context: 
485. `peterson-2015-art-language-invention-ch3-evolution.md` page 169: `OEBPS/image/116101.jpg` → `images/peterson-2015-art-language-invention-img-0556-116101.jpg`; classes `h1em`; context: 
486. `peterson-2015-art-language-invention-ch3-evolution.md` page 169: `OEBPS/image/116103.jpg` → `images/peterson-2015-art-language-invention-img-0557-116103.jpg`; classes `h1em`; context: 
487. `peterson-2015-art-language-invention-ch3-evolution.md` page 170: `OEBPS/image/116105.jpg` → `images/peterson-2015-art-language-invention-img-0560-116105.jpg`; classes `h1em`; context: 
488. `peterson-2015-art-language-invention-ch3-evolution.md` page 171: `OEBPS/image/116107.jpg` → `images/peterson-2015-art-language-invention-img-0563-116107.jpg`; classes `h1em`; context: 
489. `peterson-2015-art-language-invention-ch3-evolution.md` page 173: `OEBPS/image/116109.jpg` → `images/peterson-2015-art-language-invention-img-0566-116109.jpg`; classes `h1em`; context: 
490. `peterson-2015-art-language-invention-ch3-evolution.md` page 176: `OEBPS/image/116111.jpg` → `images/peterson-2015-art-language-invention-img-0570-116111.jpg`; classes `h1em`; context: 
491. `peterson-2015-art-language-invention-ch3-evolution.md` page 176: `OEBPS/image/116113.jpg` → `images/peterson-2015-art-language-invention-img-0572-116113.jpg`; classes `h1em`; context: 
492. `peterson-2015-art-language-invention-ch3-evolution.md` page 177: `OEBPS/image/116120.jpg` → `images/peterson-2015-art-language-invention-img-0574-116120.jpg`; classes `h1em`; context: 
493. `peterson-2015-art-language-invention-ch3-evolution.md` page 180: `OEBPS/image/Image77140.jpg` → `images/peterson-2015-art-language-invention-img-0576-image77140.jpg`; classes `h1em`; context: 
494. `peterson-2015-art-language-invention-ch3-evolution.md` page 180: `OEBPS/image/Image77154.jpg` → `images/peterson-2015-art-language-invention-img-0577-image77154.jpg`; classes `h1em`; context: 
495. `peterson-2015-art-language-invention-ch3-evolution.md` page 181: `OEBPS/image/Image77167.jpg` → `images/peterson-2015-art-language-invention-img-0578-image77167.jpg`; classes `h1em`; context: 
496. `peterson-2015-art-language-invention-ch3-evolution.md` page 181: `OEBPS/image/Image77182.jpg` → `images/peterson-2015-art-language-invention-img-0579-image77182.jpg`; classes `h1em`; context: 
497. `peterson-2015-art-language-invention-ch3-evolution.md` page 182: `OEBPS/image/Image77197.jpg` → `images/peterson-2015-art-language-invention-img-0580-image77197.jpg`; classes `h1em`; context: 
498. `peterson-2015-art-language-invention-ch3-evolution.md` page 182: `OEBPS/image/Image77210.jpg` → `images/peterson-2015-art-language-invention-img-0581-image77210.jpg`; classes `h1em`; context: 
499. `peterson-2015-art-language-invention-ch3-evolution.md` page 182: `OEBPS/image/Image77223.jpg` → `images/peterson-2015-art-language-invention-img-0582-image77223.jpg`; classes `h1em`; context: 
500. `peterson-2015-art-language-invention-ch3-evolution.md` page 182: `OEBPS/image/Image77237.jpg` → `images/peterson-2015-art-language-invention-img-0583-image77237.jpg`; classes `h1em`; context: 
501. `peterson-2015-art-language-invention-ch3-evolution.md` page 182: `OEBPS/image/Image77252.jpg` → `images/peterson-2015-art-language-invention-img-0584-image77252.jpg`; classes `h1em`; context: 
502. `peterson-2015-art-language-invention-ch3-evolution.md` page 182: `OEBPS/image/Image77271.jpg` → `images/peterson-2015-art-language-invention-img-0585-image77271.jpg`; classes `h1em`; context: 
503. `peterson-2015-art-language-invention-ch3-evolution.md` page 188: `OEBPS/image/116123.jpg` → `images/peterson-2015-art-language-invention-img-0586-116123.jpg`; classes `h1em`; context: 
504. `peterson-2015-art-language-invention-ch3-evolution.md` page 188: `OEBPS/image/116125.jpg` → `images/peterson-2015-art-language-invention-img-0587-116125.jpg`; classes `h1em`; context: 
505. `peterson-2015-art-language-invention-ch3-evolution.md` page 188: `OEBPS/image/116127.jpg` → `images/peterson-2015-art-language-invention-img-0588-116127.jpg`; classes `h1em`; context: 
506. `peterson-2015-art-language-invention-ch3-evolution.md` page 188: `OEBPS/image/116129.jpg` → `images/peterson-2015-art-language-invention-img-0589-116129.jpg`; classes `h1em`; context: 
507. `peterson-2015-art-language-invention-ch3-evolution.md` page 191: `OEBPS/image/Image77859.jpg` → `images/peterson-2015-art-language-invention-img-0593-image77859.jpg`; classes `h1em`; context: 
508. `peterson-2015-art-language-invention-ch3-evolution.md` page 196: `OEBPS/image/Image78233.jpg` → `images/peterson-2015-art-language-invention-img-0603-image78233.jpg`; classes `h1em`; context: 
509. `peterson-2015-art-language-invention-ch3-evolution.md` page 196: `OEBPS/image/Image78248.jpg` → `images/peterson-2015-art-language-invention-img-0604-image78248.jpg`; classes `h1em`; context: 
510. `peterson-2015-art-language-invention-ch3-evolution.md` page 196: `OEBPS/image/Image78263.jpg` → `images/peterson-2015-art-language-invention-img-0605-image78263.jpg`; classes `h1em`; context: 
511. `peterson-2015-art-language-invention-ch3-evolution.md` page 207: `OEBPS/image/116133.jpg` → `images/peterson-2015-art-language-invention-img-0613-116133.jpg`; classes `h1em`; context: 
512. `peterson-2015-art-language-invention-ch3-evolution.md` page 207: `OEBPS/image/116135.jpg` → `images/peterson-2015-art-language-invention-img-0614-116135.jpg`; classes `h1em`; context: 
513. `peterson-2015-art-language-invention-ch4-written-word.md` page 211: `OEBPS/image/116137.jpg` → `images/peterson-2015-art-language-invention-img-0619-116137.jpg`; classes `h1em`; context: 
514. `peterson-2015-art-language-invention-ch4-written-word.md` page 212: `OEBPS/image/116139.jpg` → `images/peterson-2015-art-language-invention-img-0620-116139.jpg`; classes `h1em`; context: It’s important to distinguish these key terms as their functions should be quite different. For example, have you ever been reading a book with a “fictional” people in it and gotte
515. `peterson-2015-art-language-invention-ch4-written-word.md` page 212: `OEBPS/image/116141.jpg` → `images/peterson-2015-art-language-invention-img-0621-116141.jpg`; classes `h1em`; context: 
516. `peterson-2015-art-language-invention-ch4-written-word.md` page 214: `OEBPS/image/116143.jpg` → `images/peterson-2015-art-language-invention-img-0626-116143.jpg`; classes `h1em`; context: 
517. `peterson-2015-art-language-invention-ch4-written-word.md` page 214: `OEBPS/image/116145.jpg` → `images/peterson-2015-art-language-invention-img-0627-116145.jpg`; classes `h1em`; context: 
518. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116152.jpg` → `images/peterson-2015-art-language-invention-img-0628-116152.jpg`; classes `h1em`; context: 
519. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116154.jpg` → `images/peterson-2015-art-language-invention-img-0629-116154.jpg`; classes `h1em`; context: 
520. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116156.jpg` → `images/peterson-2015-art-language-invention-img-0630-116156.jpg`; classes `h1em`; context: 
521. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116158.jpg` → `images/peterson-2015-art-language-invention-img-0631-116158.jpg`; classes `h1em`; context: 
522. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116160.jpg` → `images/peterson-2015-art-language-invention-img-0632-116160.jpg`; classes `h1em`; context: 
523. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116162.jpg` → `images/peterson-2015-art-language-invention-img-0633-116162.jpg`; classes `h1em`; context: 
524. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116164.jpg` → `images/peterson-2015-art-language-invention-img-0634-116164.jpg`; classes `h1em`; context: 
525. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116166.jpg` → `images/peterson-2015-art-language-invention-img-0635-116166.jpg`; classes `h1em`; context: 
526. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116169.jpg` → `images/peterson-2015-art-language-invention-img-0636-116169.jpg`; classes `h1em`; context: 
527. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116171.jpg` → `images/peterson-2015-art-language-invention-img-0637-116171.jpg`; classes `h1em`; context: 
528. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116198.jpg` → `images/peterson-2015-art-language-invention-img-0638-116198.jpg`; classes `h1em`; context: 
529. `peterson-2015-art-language-invention-ch4-written-word.md` page 215: `OEBPS/image/116200.jpg` → `images/peterson-2015-art-language-invention-img-0639-116200.jpg`; classes `h1em`; context: 
530. `peterson-2015-art-language-invention-ch4-written-word.md` page 217: `OEBPS/image/Image78711.jpg` → `images/peterson-2015-art-language-invention-img-0640-image78711.jpg`; classes `h2em`; context: 
531. `peterson-2015-art-language-invention-ch4-written-word.md` page 217: `OEBPS/image/Image79051.jpg` → `images/peterson-2015-art-language-invention-img-0642-image79051.jpg`; classes `h1em`; context: 
532. `peterson-2015-art-language-invention-ch4-written-word.md` page 217: `OEBPS/image/116202.jpg` → `images/peterson-2015-art-language-invention-img-0643-116202.jpg`; classes `h1em`; context: 
533. `peterson-2015-art-language-invention-ch4-written-word.md` page 217: `OEBPS/image/116204.jpg` → `images/peterson-2015-art-language-invention-img-0644-116204.jpg`; classes `h1em`; context: 
534. `peterson-2015-art-language-invention-ch4-written-word.md` page 218: `OEBPS/image/116206.jpg` → `images/peterson-2015-art-language-invention-img-0646-116206.jpg`; classes `h1em`; context: 
535. `peterson-2015-art-language-invention-ch4-written-word.md` page 218: `OEBPS/image/116208.jpg` → `images/peterson-2015-art-language-invention-img-0647-116208.jpg`; classes `h1em`; context: 
536. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/116210.jpg` → `images/peterson-2015-art-language-invention-img-0651-116210.jpg`; classes `h1em`; context: 
537. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/121886.jpg` → `images/peterson-2015-art-language-invention-img-0654-121886.jpg`; classes `h1em`; context: 
538. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/121888.jpg` → `images/peterson-2015-art-language-invention-img-0655-121888.jpg`; classes `h1em`; context: 
539. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/121896.jpg` → `images/peterson-2015-art-language-invention-img-0656-121896.jpg`; classes `h1em`; context: 
540. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/121894.jpg` → `images/peterson-2015-art-language-invention-img-0657-121894.jpg`; classes `h1em`; context: 
541. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/121892.jpg` → `images/peterson-2015-art-language-invention-img-0658-121892.jpg`; classes `h1em`; context: 
542. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/121890.jpg` → `images/peterson-2015-art-language-invention-img-0659-121890.jpg`; classes `h1em`; context: 
543. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/121898.jpg` → `images/peterson-2015-art-language-invention-img-0660-121898.jpg`; classes `h1em`; context: 
544. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/121901.jpg` → `images/peterson-2015-art-language-invention-img-0661-121901.jpg`; classes `h1em`; context: 
545. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/121903.jpg` → `images/peterson-2015-art-language-invention-img-0662-121903.jpg`; classes `h1em`; context: 
546. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/121905.jpg` → `images/peterson-2015-art-language-invention-img-0663-121905.jpg`; classes `h1em`; context: 
547. `peterson-2015-art-language-invention-ch4-written-word.md` page 220: `OEBPS/image/121911.jpg` → `images/peterson-2015-art-language-invention-img-0664-121911.jpg`; classes `h1em`; context: 
548. `peterson-2015-art-language-invention-ch4-written-word.md` page 222: `OEBPS/image/118970.jpg` → `images/peterson-2015-art-language-invention-img-0665-118970.jpg`; classes `h1em`; context: 
549. `peterson-2015-art-language-invention-ch4-written-word.md` page 222: `OEBPS/image/116214.jpg` → `images/peterson-2015-art-language-invention-img-0666-116214.jpg`; classes `h1em`; context: 
550. `peterson-2015-art-language-invention-ch4-written-word.md` page 222: `OEBPS/image/118972.jpg` → `images/peterson-2015-art-language-invention-img-0667-118972.jpg`; classes `h1em`; context: 
551. `peterson-2015-art-language-invention-ch4-written-word.md` page 222: `OEBPS/image/116217.jpg` → `images/peterson-2015-art-language-invention-img-0668-116217.jpg`; classes `h1em`; context: 
552. `peterson-2015-art-language-invention-ch4-written-word.md` page 223: `OEBPS/image/Image79625.jpg` → `images/peterson-2015-art-language-invention-img-0670-image79625.jpg`; classes `h2em`; context: 
553. `peterson-2015-art-language-invention-ch4-written-word.md` page 223: `OEBPS/image/Image79639.jpg` → `images/peterson-2015-art-language-invention-img-0671-image79639.jpg`; classes `h2em`; context: 
554. `peterson-2015-art-language-invention-ch4-written-word.md` page 223: `OEBPS/image/Image79648.jpg` → `images/peterson-2015-art-language-invention-img-0672-image79648.jpg`; classes `h2em`; context: 
555. `peterson-2015-art-language-invention-ch4-written-word.md` page 223: `OEBPS/image/Image79656.jpg` → `images/peterson-2015-art-language-invention-img-0673-image79656.jpg`; classes `h2em`; context: 
556. `peterson-2015-art-language-invention-ch4-written-word.md` page 223: `OEBPS/image/Image79665.jpg` → `images/peterson-2015-art-language-invention-img-0674-image79665.jpg`; classes `h2em`; context: 
557. `peterson-2015-art-language-invention-ch4-written-word.md` page 223: `OEBPS/image/Image79673.jpg` → `images/peterson-2015-art-language-invention-img-0675-image79673.jpg`; classes `h2em`; context: 
558. `peterson-2015-art-language-invention-ch4-written-word.md` page 223: `OEBPS/image/Image79665.jpg` → `images/peterson-2015-art-language-invention-img-0674-image79665.jpg`; classes `h1em`; context: 
559. `peterson-2015-art-language-invention-ch4-written-word.md` page 223: `OEBPS/image/Image79693.jpg` → `images/peterson-2015-art-language-invention-img-0676-image79693.jpg`; classes `h2em`; context: 
560. `peterson-2015-art-language-invention-ch4-written-word.md` page 223: `OEBPS/image/Image79701.jpg` → `images/peterson-2015-art-language-invention-img-0677-image79701.jpg`; classes `h2em`; context: 
561. `peterson-2015-art-language-invention-ch4-written-word.md` page 226: `OEBPS/image/116219.jpg` → `images/peterson-2015-art-language-invention-img-0684-116219.jpg`; classes `h1em`; context: 
562. `peterson-2015-art-language-invention-ch4-written-word.md` page 229: `OEBPS/image/116221.jpg` → `images/peterson-2015-art-language-invention-img-0687-116221.jpg`; classes `h1em`; context: 
563. `peterson-2015-art-language-invention-ch4-written-word.md` page 229: `OEBPS/image/116223.jpg` → `images/peterson-2015-art-language-invention-img-0688-116223.jpg`; classes `h1em`; context: The Proto-Sinaitic system utilized pictographs, and Canaanite speakers were happy with that system. When the Phoenicians got hold of it, they took some of those pictographs and for
564. `peterson-2015-art-language-invention-ch4-written-word.md` page 230: `OEBPS/image/Image80314.jpg` → `images/peterson-2015-art-language-invention-img-0691-image80314.jpg`; classes `h1em`; context: It was a long, blunted reed called a stylus that had a triangular end. If that was your implement and you were making impressions into wet clay, you should be able to see why it’d 
565. `peterson-2015-art-language-invention-ch4-written-word.md` page 234: `OEBPS/image/n.jpg` → `images/peterson-2015-art-language-invention-img-0695-n.jpg`; classes `h1em`; context: Enjoy the whole thing, but just look at some of the incredible changes! Look at the column headed by . In the third century BCE, the thing was basically a capital I, and now it loo
566. `peterson-2015-art-language-invention-ch4-written-word.md` page 234: `OEBPS/image/squiggle.jpg` → `images/peterson-2015-art-language-invention-img-0696-squiggle.jpg`; classes `h1em`; context: Enjoy the whole thing, but just look at some of the incredible changes! Look at the column headed by . In the third century BCE, the thing was basically a capital I, and now it loo
567. `peterson-2015-art-language-invention-ch4-written-word.md` page 234: `OEBPS/image/t.jpg` → `images/peterson-2015-art-language-invention-img-0697-t.jpg`; classes `h1em`; context: Enjoy the whole thing, but just look at some of the incredible changes! Look at the column headed by . In the third century BCE, the thing was basically a capital I, and now it loo
568. `peterson-2015-art-language-invention-ch4-written-word.md` page 234: `OEBPS/image/stop.jpg` → `images/peterson-2015-art-language-invention-img-0698-stop.jpg`; classes `h1em`; context: Enjoy the whole thing, but just look at some of the incredible changes! Look at the column headed by . In the third century BCE, the thing was basically a capital I, and now it loo
569. `peterson-2015-art-language-invention-ch4-written-word.md` page 234: `OEBPS/image/hoove.jpg` → `images/peterson-2015-art-language-invention-img-0699-hoove.jpg`; classes `h1em`; context: Enjoy the whole thing, but just look at some of the incredible changes! Look at the column headed by . In the third century BCE, the thing was basically a capital I, and now it loo
570. `peterson-2015-art-language-invention-ch4-written-word.md` page 235: `OEBPS/image/116239.jpg` → `images/peterson-2015-art-language-invention-img-0700-116239.jpg`; classes `h1em`; context: 
571. `peterson-2015-art-language-invention-ch4-written-word.md` page 236: `OEBPS/image/Image80521.jpg` → `images/peterson-2015-art-language-invention-img-0701-image80521.jpg`; classes `h1em`; context: All the font programs I’ve worked with make use of the traditional U.S. letterboard (though most are now updating to Unicode, which is a good thing). The first step in creating a f
572. `peterson-2015-art-language-invention-ch4-written-word.md` page 237: `OEBPS/image/Image80851.jpg` → `images/peterson-2015-art-language-invention-img-0703-image80851.jpg`; classes `h1em`; context: A mapping like this makes Sondiv look like an alphabet, even though it’s an abjad. It also ignores the fact that is only ever used in foreign words, is just a rarely used ligature,
573. `peterson-2015-art-language-invention-ch4-written-word.md` page 237: `OEBPS/image/Image80860.jpg` → `images/peterson-2015-art-language-invention-img-0704-image80860.jpg`; classes `h1em`; context: A mapping like this makes Sondiv look like an alphabet, even though it’s an abjad. It also ignores the fact that is only ever used in foreign words, is just a rarely used ligature,
574. `peterson-2015-art-language-invention-ch4-written-word.md` page 237: `OEBPS/image/Image80868.jpg` → `images/peterson-2015-art-language-invention-img-0705-image80868.jpg`; classes `h1em`; context: A mapping like this makes Sondiv look like an alphabet, even though it’s an abjad. It also ignores the fact that is only ever used in foreign words, is just a rarely used ligature,
575. `peterson-2015-art-language-invention-ch4-written-word.md` page 243: `OEBPS/image/116241.jpg` → `images/peterson-2015-art-language-invention-img-0715-116241.jpg`; classes `h1em`; context: 
576. `peterson-2015-art-language-invention-ch4-written-word.md` page 243: `OEBPS/image/116247.jpg` → `images/peterson-2015-art-language-invention-img-0716-116247.jpg`; classes `h1em`; context: 
577. `peterson-2015-art-language-invention-ch4-written-word.md` page 243: `OEBPS/image/116249.jpg` → `images/peterson-2015-art-language-invention-img-0717-116249.jpg`; classes `h1em`; context: 
578. `peterson-2015-art-language-invention-ch4-written-word.md` page 244: `OEBPS/image/116251.jpg` → `images/peterson-2015-art-language-invention-img-0718-116251.jpg`; classes `h1em`; context: 
579. `peterson-2015-art-language-invention-ch4-written-word.md` page 250: `OEBPS/image/116255.jpg` → `images/peterson-2015-art-language-invention-img-0724-116255.jpg`; classes `h1em`; context: 
580. `peterson-2015-art-language-invention-ch4-written-word.md` page 250: `OEBPS/image/116257.jpg` → `images/peterson-2015-art-language-invention-img-0725-116257.jpg`; classes `h1em`; context: 
581. `peterson-2015-art-language-invention-ch4-written-word.md` page 251: `OEBPS/image/116259.jpg` → `images/peterson-2015-art-language-invention-img-0727-116259.jpg`; classes `h1em`; context: 
582. `peterson-2015-art-language-invention-ch4-written-word.md` page 251: `OEBPS/image/116263.jpg` → `images/peterson-2015-art-language-invention-img-0728-116263.jpg`; classes `h1em`; context: 
583. `peterson-2015-art-language-invention-ch4-written-word.md` page 251: `OEBPS/image/116265.jpg` → `images/peterson-2015-art-language-invention-img-0730-116265.jpg`; classes `h1em`; context: 
584. `peterson-2015-art-language-invention-ch4-written-word.md` page 251: `OEBPS/image/Image81861.jpg` → `images/peterson-2015-art-language-invention-img-0731-image81861.jpg`; classes `h1em`; context: 
585. `peterson-2015-art-language-invention-ch4-written-word.md` page 251: `OEBPS/image/116267.jpg` → `images/peterson-2015-art-language-invention-img-0732-116267.jpg`; classes `h1em`; context: 
586. `peterson-2015-art-language-invention-ch4-written-word.md` page 254: `OEBPS/image/116269.jpg` → `images/peterson-2015-art-language-invention-img-0740-116269.jpg`; classes `h1em`; context: 
587. `peterson-2015-art-language-invention-ch4-written-word.md` page 254: `OEBPS/image/116271.jpg` → `images/peterson-2015-art-language-invention-img-0742-116271.jpg`; classes `h1em`; context: 
588. `peterson-2015-art-language-invention-ch4-written-word.md` page 254: `OEBPS/image/116273.jpg` → `images/peterson-2015-art-language-invention-img-0743-116273.jpg`; classes `h1em`; context: 
