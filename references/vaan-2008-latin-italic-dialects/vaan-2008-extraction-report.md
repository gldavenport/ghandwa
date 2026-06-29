---
title: "Etymological Dictionary of Latin and the other Italic Languages — extraction report"
author: "Michiel de Vaan"
date: "2008"
source_type: mixed
extraction_date: 2026-05-07
source_file: "vaan-2008-latin-italic-dialects.pdf"
chunk: "extraction-report"
---

# Extraction report

## Source classification

The PDF contains full-page scanned raster images plus a machine-readable text layer. I treated it as a mixed scanned/OCR PDF rather than a clean born-digital PDF. The extraction therefore uses the embedded text layer as the base input and records that character-level verification remains incomplete. No new OCR pass was run over all pages.

## Corrections applied

- Used PyMuPDF block extraction to preserve the dictionary block structure and avoid collapsing the whole work into a single text stream.
- Chunked the work by the source PDF outline: front matter, introduction, one file per dictionary letter section, bibliography, and index.
- Removed running page headers from dictionary, bibliography, and index pages where they were exposed as separate top-margin text blocks.
- Inserted page anchors as Markdown comments using PDF page number and an estimated printed page number.
- Normalized visible ASCII laryngeal digits `h1`, `h2`, `h3` to `h₁`, `h₂`, `h₃`; also normalized a limited set of OCR variants for `h₁` when they appeared as `h]`, `h!`, or `h,` before root material.
- Applied conservative recurring OCR/text-layer repairs: `1EW`→`IEW`, `L1V`→`LIV`, common `BibL` variants→`Bibl.`, `P1.`/`Ρ1.`→`Pl.`, `Ο.`→`O.`, and several arrow variants→`→`.
- Preserved the index in line-oriented form instead of collapsing entries into prose, because dense index entries are high-risk for dropped diacritics and page references.

## Unresolved issues list

- The text layer contains many OCR-like errors in Greek, diacritics, superscripts, page headers, bibliography strings, and dense index columns. This extraction should be treated as a first-pass corpus extraction, not a character-authoritative edition.
- Superscript aspiration and labiovelar notation were not globally normalized, because automatic conversion of `h`/`w` in this source would create false positives in ordinary text and bibliography entries.
- The scanned-page visual layer was not exhaustively compared against the text layer. Any character not already represented in the embedded text layer may remain wrong or missing.
- No inline `[?]` markers were inserted, because I did not manually infer individual characters from page images at scale.
- The last index page and some dense index columns show severe text-layer disorder and should be visually checked before relying on exact forms.

### Automated issue samples

- `visible_ocr_digit_for_l_or_o_in_common_contexts`: …x 7\), acupenser (Lucil.+) / acipenser (Hor.+) 'a fish, probably the sturgeon* (P1-+); acinus [mVn.] 'grape or other berry; also the seeds of grapes' (Cato+). Pit…
- `visible_ocr_digit_for_l_or_o_in_common_contexts`: …rate, aedile* (Elog.Scip. aidilis\ aedilicius 'of or connected with an aedile' (P1-+), aedilitas 'the office of an aedile' (Pl.+); aedificare "to build' (PL+), ae…
- `visible_ocr_digit_for_l_or_o_in_common_contexts`: …-estimate: 29 -->  aevus / aevum 'period of time; past; future' [m. (PL, Lucr., C1L); n. (mostly) o] (Pl.+) Derivatives: aetas, -atis 'age' (Pl.+) < aevitas (Lex X…
- `visible_ocr_digit_for_l_or_o_in_common_contexts`: …mate: 31 -->  peragere 'to perform, finish' (Enn.+); (4) iurigare 'to quarrel' (P1-+); lltigare 'to litigate' (PL+); navigare 'to go by ship' (Pl.+); purigare 'to…
- `visible_ocr_digit_for_l_or_o_in_common_contexts`: …alk' (Ten), inambulare 'to pace up and down' (PL+), obambulare 'to walk up to' (P1-+), perambulare 'to roam about' (PI.), redambulare 'to walk back' (PL)- Pit. *a…
- `visible_ocr_digit_for_l_or_o_in_common_contexts`: …119, Schrijver 1991: 113.  antae 'square pilasters' [f. (mostly pi.) a] (Vitr., C1L) Pit *an(a)ta- 'post, pillar'. PIE *h₂enHt-h₂- 'door-post'. IE cognates: Skt. a…
- `visible_ocr_digit_for_l_or_o_in_common_contexts`: …991: 69. → arduus  area 'chest' [ft a] (PL+) Derivatives: arcula 'small chest' (P1-+), arcanus 'secret' (Hor+), arcera 'kind of  <!-- pdf-page: 65; printed-page-e…
- `visible_ocr_digit_for_l_or_o_in_common_contexts`: …eapons' [n.pl. ο] (Ρ1Λ; gen.pl. armum Pac,, Ace.) Derivatives: armatus 'armed' (P1-+); armentum 'herd of cattle' (Van, Lucr.+), armenta 'id.' (Enn., Pac); armiger…
- `isolated_unclear_or_inferred_markers`: … [2 or 3s.fut.pf], benust [3s.fiit.pf.], benurent, benurent [3p.fut.pf], benuso [?], O. kumbened [kom- + 3s.pfJ, O. cebnust [ke- + 3s,fut.pf] 'to come' < *ben- < *…
- `isolated_unclear_or_inferred_markers`: …r', visti, 3s. vysta 'to multiply, breed', vaisius 'fruit'; OIc. visir 'sprout' [?]; OE wise 'sprout, stem' [f.]; OHG wlsa 'meadow' [£].  Uncertain etymology. None…

## Confusion-pair report

- `h₁ h₂ h₃`: ASCII `h1/h2/h3` was normalized where detected. Remaining misrecognized laryngeals may exist where the OCR produced other shapes such as punctuation, brackets, or plain `H`.
- Macron vowels: preserved where present in the text layer; not visually audited across all body text, bibliography, and index sections.
- Superscript `ʰ` and `ʷ`: not globally restored from plain `h`/`w`; unverified.
- `ə`: preserved where present; unverified against page images.
- Underdot letters and acute consonants: preserved where present; not exhaustively audited.
- Asterisk `*`: preserved where present; some OCR misreads may remain.
- Dagger `†`: preserved where present; not exhaustively audited.
- Greek letters: preserved from the text layer where present, but Greek is a high-risk area in this extraction.

## Codepoint inventory

- note: All counts are approximate and for cross-pass comparison only.
- laryngeals: {'h1': 354, 'h2': 1855, 'h3': 462}
- macron_a: 0
- macron_e: 0
- macron_i: 0
- macron_o: 0
- macron_u: 0
- schwa: 0
- greek_chars: 23545
- combining_diacritics: 0
- dagger: 0

## Structural integrity check

- Headings and chunks follow the source outline.
- Dictionary letter sections are separated into individual files. Several letter headings in the text layer were Greek-lookalike or OCR-corrupted and were normalized in filenames and top headings.
- Bibliography and index are separate files.
- Footnote-like and bibliography references remain inline as in the source text layer; the book does not expose a normal note apparatus in the extracted layer.
- Tables and dense abbreviation lists were not converted to semantic Markdown tables except where line-oriented extraction was safer.
- No discrete figures, maps, diagrams, or plates were identified for extraction beyond the scanned page images themselves.

## Image inventory

No extracted figure/table/map/plate images are included. The PDF consists of scanned page images, but no discrete source figures requiring separate `images/` collation were identified.
