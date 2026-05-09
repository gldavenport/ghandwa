---
title: "Laryngeal Realism and the Prehistory of Celtic"
author: "Joseph F. Eska"
date: "2018"
source_type: "born-digital"
extraction_date: "2026-05-08"
source_file: "eska-2018-laryngeal-realism.pdf"
chunk: "extraction-report"
---

# Extraction Report: Eska 2018, “Laryngeal Realism and the Prehistory of Celtic”

## Source type

Born-digital PDF with a machine-readable text layer. The PDF text layer was used as the primary input. Visual/rendered inference was used only in a limited way where the text layer exposed obvious encoding damage in linguistic symbols, accents, and diacritics.

## Deliverables

- `eska-2018-laryngeal-realism.md` — main article text, excluding bibliography.
- `eska-2018-laryngeal-realism-bibliography.md` — references section.
- `eska-2018-laryngeal-realism-extraction-report.md` — this QC report.
- `manifest.json` — machine-readable extraction metrics.

No index is present in the source. No figures, maps, plates, or image-rendered tables were detected; the small phonological/VOT/system tables were reconstructed as Markdown tables or fenced text blocks.

## Corrections applied

- Removed running heads, page numbers, Wiley download footer lines, copyright/publisher footers, and page-boundary artifacts.
- Rejoined paragraphs broken by PDF lineation and page boundaries.
- Converted article footnotes into Markdown footnotes while retaining note text.
- Split bibliography into a separate Markdown file.
- Reconstructed the VOT tables as Markdown tables.
- Reconstructed plosive-system displays as fenced text blocks to preserve spacing and symbolic contrast.
- Repaired common PDF ligature artifacts: `ﬁ` → `fi`, `ﬀ` → `ff`, `ﬂ` → `fl`, `ﬃ` → `ffi`, `ﬄ` → `ffl`.
- Repaired obvious broken accent encodings in names and quoted forms, including but not limited to: `Ó Siadhail`, `Ní Chasaide`, `Beguš`, `Gašper`, `Jordán Colera`, `Cécile`, `Solé`, `Ségéral`, `Kümmel`, `réalisation`, `nécessairement`, `être`, `réalisées`, `règle`, and `L’année épigraphique`.
- Normalized aspiration and labialization in technical forms where the PDF text layer flattened superscripts: e.g. `/ph th kh/` → `/pʰ tʰ kʰ/`, `kw` → `kʷ` where the article’s phonological context required labial-velar notation, and `ɡw` → `ɡʷ` in corresponding reconstructed forms.
- Preserved the author’s use of `ɦ` in voiced aspirated plosives rather than silently converting it to `ʱ`.
- Repaired the damaged name `St’át’imcets` from a corrupted control-character extraction.
- Repaired the Celtiberian form `śDAḿ` and corresponding bibliographic title form where the text layer exposed damaged accent encoding.
- Used `hₓ` for the unspecified laryngeal in `*hₓupm̩mo-` and `*(s)pelhₓ-`; this is a source-critical normalization from damaged or flattened PDF extraction, and should be verified visually in a subsequent character pass.

## Unresolved issues list

1. The source PDF has custom embedded fonts, and several italic/accented spans lack clean Unicode mappings. Repairs were made where the intended form was strongly recoverable, but the extraction should not be treated as final character-authoritative without a visual glyph pass.
2. The exact diacritic in the Celtiberian form printed as damaged `sDAm´` in raw extraction was normalized to `śDAḿ`. This should be visually checked against the PDF glyphs and against Eska’s cited Celtiberian convention.
3. The unspecified-laryngeal forms `*hₓupm̩mo-` and `*(s)pelhₓ-` are normalized from flattened `hx` in the text layer; verify that the source uses subscript `ₓ` rather than plain `x` or another convention.
4. The murmured-plosive bracket `[b̤ d̤ ɡ̈]` is reconstructed from a damaged diacritic display in the text layer. The first two symbols appear to use subscript diaeresis/breathy-voice-style notation in the visual source; the third extracted as `ɡ̈`. Verify visually.
5. Bibliography entries with heavy diacritics were corrected using obvious bibliographic forms, but not all proper-name accents can be certified from the PDF text layer alone.
6. No `[unclear]` markers were inserted in the clean text, because no passage was unreadable enough to require them. The items above remain verification targets.

## Confusion-pair report

- `h₁ h₂ h₃`: no instances in the source/output. The source uses `hₓ`-type unspecified laryngeal notation instead; those forms require visual verification.
- Macron vowels `ā ē ī ō ū`: no macron-vowel instances detected in the output. This is plausible for this article but not independently certified.
- Superscript aspiration `ʰ`: normalized throughout slash-forms and plosive-system displays where the flattened text layer read `ph th kh`.
- Superscript labialization `ʷ`: normalized in reconstructed labial-velar forms where the flattened text layer read `kw`, `gw`, `qw`, etc.
- Schwa `ə`: no source/output instances detected except none in final text. Not independently certified.
- Indic underdot forms `ṛ ḷ ṃ ṇ`: no instances detected. Syllabic marker `m̩` occurs and was preserved in `*hₓupm̩mo-`.
- Acute consonants `ǵ ḱ`: no instances detected.
- Asterisk `*`: preserved before reconstructed and cited forms where present.
- Dagger `†`: no instances detected.
- Source-specific: `ɡ` vs. `g` was preserved in phonetic/phonological symbols; ordinary orthographic `g` was left unchanged.
- Source-specific: `ɸ` and Greek `φ` were kept distinct.
- Source-specific: angle brackets `〈...〉` were preserved for orthographic signs.

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
  "macron_a": 0,
  "macron_e": 0,
  "macron_i": 0,
  "macron_o": 0,
  "macron_u": 0,
  "schwa": 1,
  "greek_chars": 7,
  "combining_diacritics": 12,
  "dagger": 0,
  "superscript_h": 48,
  "superscript_w": 34,
  "script_g": 29,
  "phi_latin": 20,
  "turned_epsilon": 1,
  "angle_brackets": 20
}
```

## Structural integrity check

- Headings are consistent and mirror the article’s sections.
- The abstract, numbered sections, coda, abbreviations, and correspondence block are preserved.
- Footnotes 1–22 are attached as Markdown footnotes.
- The bibliography is separated into its own file.
- Tables/displays are reconstructed in structurally readable Markdown.
- No continuation text appears knowingly lost at page boundaries.
- Running heads, page numbers, and Wiley access footers were removed.

## Image inventory

No image files extracted. No `[image-only ...]` placeholders used.
