# Extraction Report

## Source identification

- Source file: `putnam-ed-2020-cambridge-handbook-germanic.epub.zip`
- Source type: EPUB (structured archive with XHTML text layer and discrete image files).
- Extraction date: 2026-05-07
- Controlling instruction file: `linguistics-extract-instructions.md`

## Corrections applied

- Parsed EPUB XHTML text directly rather than applying OCR.
- Converted page anchors such as `page_193` to inline `[[page 193]]` markers.
- Converted HTML superscript/subscript digits and common modifier letters to Unicode equivalents where direct one-to-one mappings were available. This includes laryngeal-style `h` + subscript digit sequences across inline markup spans.
- Replaced the EPUB inline image fallback `42186inline27_1.png` with the Unicode MathML text-layer equivalent `⇍` and recorded it in the image-glyph inventory.
- Preserved small-caps spans as inline HTML `<span class="sc">…</span>` rather than changing case.
- Converted XHTML tables to tab-delimited fenced `tsv` blocks to reduce alignment loss in dense linguistic examples.
- Separated per-chapter reference lists into bibliography files and separated the index into its own file.
- Copied EPUB image assets into `images/` without re-encoding.

## Unresolved-issues list

- `[?]` inferred-character markers present: 1.

## Confusion-pair report

- h₁ h₂ h₃ vs h1 h2 h3: no issue-pattern instances found by automated regex scan; not fully verified against a publisher PDF or page images.
- precomposed macrons vs combining macrons: 2 possible issue-pattern instance(s) found for human review.
- superscript ʰ ʷ vs plain h w: no issue-pattern instances found by automated regex scan; not fully verified against a publisher PDF or page images.
- ə vs e or 9: 183 possible issue-pattern instance(s) found for human review.
- underdot letters ṛ ḷ ṃ ṇ vs plain: no issue-pattern instances found by automated regex scan; not fully verified against a publisher PDF or page images.
- ǵ ḱ vs g'/k': 168 possible issue-pattern instance(s) found for human review.
- asterisk before reconstructed forms vs absent/corrupt: 18 possible issue-pattern instance(s) found for human review.
- dagger † vs + or absent: 5 possible issue-pattern instance(s) found for human review.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 6,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 1,
  "macron_e": 14,
  "macron_i": 8,
  "macron_o": 29,
  "macron_u": 0,
  "schwa": 234,
  "greek_chars": 193,
  "combining_diacritics": 109,
  "dagger": 0
}
```

## Structural integrity check

- Output files listed in manifest: 55 Markdown/JSON/report files plus image assets.
- Bibliography files created: 1.
- XHTML-referenced figures/images rendered in Markdown: 87.
- Headings were derived from the source XHTML hierarchy. Chapter files, part files, front matter, bibliography files, and index are separated.
- Footnotes remain with their corresponding chapter/front-matter file.
- Tables are represented as fenced TSV blocks; this is intended to preserve dense alignment better than prose conversion.
- No page-image or publisher-PDF collation was performed in this pass; therefore visual-only validation of character shapes was not attempted.

## Image-glyph inventory

- `42186inline27_1.png` → `⇍` (inline MathML operator used in place of EPUB image fallback).

## Image inventory

- EPUB image assets copied: 1168.
- XHTML-referenced figure/image placements: 87.
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu2-1.png` from `42186figu2_1.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu3-1.png` from `42186figu3_1.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu3-2.png` from `42186figu3_2.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu3-3.png` from `42186figu3_3.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu3-4.png` from `42186figu3_4.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu3-5.png` from `42186figu3_5.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu3-6.png` from `42186figu3_6.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu3-7.png` from `42186figu3_7.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu3-8.png` from `42186figu3_8.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu3-9.png` from `42186figu3_9.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu3-10.png` from `42186figu3_10.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu3-11.png` from `42186figu3_11.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu5-1.png` from `42186figu5_1.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu5-2.png` from `42186figu5_2.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu6-1.png` from `42186figu6_1.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu6-2.png` from `42186figu6_2.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-1.png` from `42186fig7_1.png`; label: Figure 7.1; page: [not anchored]; caption: Figure 7.1 Tonal contours in Cologne, focus, nonfinal position; stressed accent syllable nonshaded, overall post-tonic contour shaded
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-2.png` from `42186fig7_2.png`; label: Figure 7.2; page: [not anchored]; caption: Figure 7.2 Tonal contours in Cologne (Rule A) and Arzbach (Rule B), focus, nonfinal position; nuclear contour nonshaded, overall post-nuclear contour shaded
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-3.png` from `42186fig7_3.png`; label: Figure 7.3; page: [not anchored]; caption: Figure 7.3 Analysis with lexical tone for Rule A (Gussenhoven and Peters 2004), Cologne dialect; focus, nonfinal position
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-4.png` from `42186fig7_4.png`; label: Figure 7.4; page: [not anchored]; caption: Figure 7.4 Analysis with a foot-based approach (Köhnlein 2016) for Rule A, Cologne dialect; focus, nonfinal position
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-5.png` from `42186fig7_5.png`; label: Figure 7.5; page: [not anchored]; caption: Figure 7.5 Reconstructed accent contours before and after tone accent genesis in West Germanic (before = dashed contour; after = solid contour)
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-6.png` from `42186fig7_6.png`; label: Figure 7.6; page: [not anchored]; caption: Figure 7.6 The development from the predecessor toward Rule A (before = dashed contour; after = solid contour)
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-7.png` from `42186fig7_7.png`; label: Figure 7.7; page: [not anchored]; caption: Figure 7.7 The development from the predecessor toward Rule B (before = dashed contour; after = solid contour)
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-8.png` from `42186fig7_8.png`; label: Figure 7.8; page: [not anchored]; caption: Figure 7.8 Idealized tonal contours in Central Swedish
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-9.png` from `42186fig7_9.png`; label: Figure 7.9; page: [not anchored]; caption: Figure 7.9 Idealized tonal contours in different dialect areas, distinguished by number of peaks in Accent 2 (1 /2) and alignment of the tonal melodies (A = early; B = late)
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-10.png` from `42186fig7_10.png`; label: Figure 7.10; page: [not anchored]; caption: Figure 7.10 Competing analyses with lexical tone for Central Swedish
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-12.png` from `42186fig7_12.png`; label: Figure 7.11; page: [not anchored]; caption: Figure 7.11 Basics of the North Germanic tone accent genesis in the accent-first, peak-delay approach (before = dashed contour; after = solid contour)
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig7-13.png` from `42186fig7_13.png`; label: Figure 7.12; page: [not anchored]; caption: Figure 7.12 Development of two-peaked Accent 2 in the accent-first, peak-delay approach
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig8-1.png` from `42186fig8_1.png`; label: Figure 8.1; page: [not anchored]; caption: Figure 8.1 Pitch track of the German utterance “auf gar keinen Fall” (“by no means”)
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig8-2.png` from `42186fig8_2.png`; label: Figure 8.2; page: [not anchored]; caption: Figure 8.2 Tonal alignment in L1 German
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig8-3.png` from `42186fig8_3.png`; label: Figure 8.3; page: [not anchored]; caption: Figure 8.3 Tonal alignment in L2 English
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu8-1.png` from `42186figu8_1.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig8-4.png` from `42186fig8_4.png`; label: Figure 8.4; page: [not anchored]; caption: Figure 8.4 A stylized Dutch hat pattern (“Peter comes never too late.”) recreated from ’t Hart (1998: 97)
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu8-2.png` from `42186figu8_2.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig8-5.png` from `42186fig8_5.png`; label: Figure 8.5; page: [not anchored]; caption: Figure 8.5 Stylized intonation contour of Danish statements, wh-questions, questions with word order inversion, and declarative questions (recreated from Grønnum 2009: 600)
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig8-6.png` from `42186fig8_6.png`; label: Figure 8.6; page: [not anchored]; caption: Figure 8.6 Contour of a Dutch interrogative “Heeft Peter een nieuwe auto gekocht?“ (“Has Peter bought a new car?”) reproduced from ’t Hart (1998: 103)
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig8-7.png` from `42186fig8_7.png`; label: Figure 8.7; page: [not anchored]; caption: Figure 8.7 Norwegian utterance “Du aner ikke hvor dyr den er, vel?” (“You do not know how expensive it is, right?”) with rising intonation on the tag question
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig8-8.png` from `42186fig8_8.png`; label: Figure 8.8; page: [not anchored]; caption: Figure 8.8 Norwegian utterance “Du aner ikke hvor dyr den er, vel.” (“Well, you do not know how expensive it is.”) with falling intonation on the tag
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu8-3.png` from `42186figu8_3.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu8-4.png` from `42186figu8_4.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu8-5.png` from `42186figu8_5.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu8-6.png` from `42186figu8_6.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu8-7.png` from `42186figu8_7.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig10-1.png` from `42186fig10_1.png`; label: Figure 10.1; page: [not anchored]; caption: Figure 10.1 Complexity of nominal inflection of the GMC languages
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig10-2.png` from `42186fig10_2.png`; label: Figure 10.2; page: [not anchored]; caption: Figure 10.2 Preservation, elimination and functionalization of umlaut in GMC languages
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig10-3.png` from `42186fig10_3.png`; label: Figure 10.3; page: [not anchored]; caption: Figure 10.3 Direction of formal determination and influence between stem and suffix
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig12-1.png` from `42186fig12_1.png`; label: Figure 12.1; page: [not anchored]; caption: Figure 12.1 Pragmatic hierarchy of gender agreement, from Köpcke et al. (2010: 179)
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig12-2.png` from `42186fig12_2.png`; label: Figure 12.2; page: [not anchored]; caption: Figure 12.2 The pronominal gender system of Danish and Swedish, translated and adapted from Braunmüller (2007: 54)
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu12-2.png` from `42186figu12_2.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu16-1.png` from `42186figu16_1.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu16-2.png` from `42186figu16_2.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu16-3.png` from `42186figu16_3.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu16-4.png` from `42186figu16_4.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu16-5.png` from `42186figu16_5.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu16-6.png` from `42186figu16_6.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu21-1.png` from `42186figu21_1.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu22-1.png` from `42186figu22_1.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu23-1.png` from `42186figu23_1.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu23-2.png` from `42186figu23_2.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu23-3.png` from `42186figu23_3.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu23-4.png` from `42186figu23_4.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu25-1.png` from `42186figu25_1.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig25-1.png` from `42186fig25_1.png`; label: Figure 25.1; page: [not anchored]; caption: Figure 25.1 Potential boundaries of an event
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig25-2.png` from `42186fig25_2.png`; label: Figure 25.2; page: [not anchored]; caption: Figure 25.2 Ingressive, dynamic, eventive, inchoative¹¹
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig25-3.png` from `42186fig25_3.png`; label: Figure 25.3; page: [not anchored]; caption: Figure 25.3 Progressive, imperfective, continuative, durative, stative, atelic
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig25-4.png` from `42186fig25_4.png`; label: Figure 25.4; page: [not anchored]; caption: Figure 25.4 Egressive, perfective, telic
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig25-5.png` from `42186fig25_5.png`; label: Figure 25.5; page: [not anchored]; caption: Figure 25.5 Iterative, generic, habitual
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu25-2.png` from `42186figu25_2.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu25-3.png` from `42186figu25_3.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu26-1.png` from `42186figu26_1.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186figu26-2.png` from `42186figu26_2.png`; label: [none]; page: [not anchored]; caption: [none]
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig28-1.png` from `42186fig28_1.png`; label: Figure 28.1; page: [not anchored]; caption: Figure 28.1 Afrikaans sentence with wide focus
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig28-2.png` from `42186fig28_2.png`; label: Figure 28.2; page: [not anchored]; caption: Figure 28.2 Afrikaans sentence with a narrow focus
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig28-3.png` from `42186fig28_3.png`; label: Figure 28.3; page: [not anchored]; caption: Figure 28.3 Afrikaans sentence with a topic
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig31-1.png` from `42186fig31_1.png`; label: [[page 739]] Map 31.1; page: 739; caption: [[page 739]] Map 31.1 Westgermanic Dialect Continuum: Low German varieties 1–11; Low Franconian (Dutch) varieties 12–20; Middle German varieties 21–28; Upper German varieties 29–32; Frisian varieties 33–35. https://commons.wikimedia.org/wiki/File:Deutsch-Niederl%C3%A4ndischer_Sprachraum_(nach_Werner_K%C3%B6nig).png.
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig31-2.png` from `42186fig31_2.png`; label: Map 31.2; page: [not anchored]; caption: Map 31.2 Apocope of final schwa *Atlas zur deutschen Alltagssprache*
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig31-3.png` from `42186fig31_3.png`; label: Map 31.3; page: [not anchored]; caption: Map 31.3 N-AD case systems to the east (Shrier 1965: 434).Solid line, definite article; short dashes, personal pronoun; dotted line, indefinite article; line of diagonals, adjective; long dashes, 1 <span class="sc">sg</span> pronouns
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig31-4.png` from `42186fig31_4.png`; label: Map 31.4; page: [not anchored]; caption: Map 31.4 NA-D case systems to the west (Shrier 1965: 435).Solid line, definite article; short dashes, personal pronoun; dotted line, indefinite article; line of diagonals, adjective
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig31-5.png` from `42186fig31_5.png`; label: Map 31.5; page: [not anchored]; caption: Map 31.5 *Brötchen* ‘bread roll’
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig31-6.png` from `42186fig31_6.png`; label: Map 31.6; page: [not anchored]; caption: Map 31.6 Tag question *gell?*
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig32-1.png` from `42186fig32_1.png`; label: Figure 32.1; page: [not anchored]; caption: Figure 32.1 The Nordic language tree
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig32-2.png` from `42186fig32_2.png`; label: Figure 32.2; page: [not anchored]; caption: Figure 32.2 The model of the modern Nordic languages
- `putnam-ed-2020-cambridge-handbook-germanic-42186map32-1.png` from `42186map32_1.png`; label: Map 32.1; page: [not anchored]; caption: Map 32.1 Characterization of the Nordic dialects
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig32-3.png` from `42186fig32_3.png`; label: Figure 32.3; page: [not anchored]; caption: Figure 32.3 The mean results of the five investigations on mutual intelligibility in Scandinavia in Table 32.1
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig33-1.png` from `42186fig33_1.png`; label: Figure 33.1; page: [not anchored]; caption: Figure 33.1 VOT-times in Wisconsin Kölsch and varieties of English
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig33-2.png` from `42186fig33_2.png`; label: Figure 33.2; page: [not anchored]; caption: Figure 33.2 Differences in Wisconsin heritage German case marking between NPs and pronouns
- `putnam-ed-2020-cambridge-handbook-germanic-42186fig33-3.png` from `42186fig33_3.png`; label: Figure 33.3; page: [not anchored]; caption: Figure 33.3 Frequency of the two word orders in the production of subordinate clauses in MSG according to clause type

## Limits of this pass

The extraction uses the EPUB XHTML text layer as authority. Automated checks cannot detect errors that are already encoded consistently in the EPUB layer, nor can they verify image-internal text in figure graphics without a dedicated visual collation pass.
