# Extraction Report: Fortson 2010, *Indo-European Language and Culture*

## Source identification

- Source file: `fortson-2010-ie-language-culture.epub.zip`
- Source type used for this pass: EPUB; born-digital XHTML text layer with discrete image files.
- The EPUB does not encode print page ranges in a page-list; chunk `pages` fields therefore say `not encoded in EPUB`.
- Extraction date: 2026-05-07

## Corrections applied

- HTML/XHTML entity decoding performed through BeautifulSoup.
- XHTML subscript tags were rendered as Unicode subscript digits/letters where safe, including laryngeal indices h₁, h₂, h₃. This applies inside inline markup spans processed by the renderer, including italic and bold contexts.
- Superscript w and h were rendered as ʷ and ʰ where safe; more complex superscripts were preserved as HTML `<sup>…</sup>` rather than silently normalized.
- `<em>`, `<b>`, `<small>`, and underline spans were preserved with Markdown/HTML equivalents where feasible.
- Source artifact `>;` was repaired to `>`.
- Narrow source-layer glyph artifacts identified in earlier stress searches were repaired, including `cambi1re` → `cambiāre`, `n1-re` → `nāre`, `b2ta` → `bēta`, `st1n` → `stān`, Pashto `Pa#t*4*`/`Pa#t4` → `Paṣtō`, and related one-off vowel-length artifacts.
- Non-breaking spaces and common HTML spacing artifacts were regularized to ordinary spaces.
- Actual XHTML tables were converted to Markdown tables.
- Discrete EPUB images were copied directly into `images/` without re-encoding or recompression and referenced with standard Markdown image links.
- Inline image glyph handling was enabled for this pass. No inline glyph `<img>` tags were encountered in the XHTML text stream; therefore no Unicode substitutions or `[image-glyph: …]` annotations were inserted.
- Bibliography and indexes were extracted into separate files. Subject Index and Word Index are combined in one `{source}-index.md` file as required by the new instructions.

## Unresolved-issues list

1. Image-internal text remains image-internal. The new pass copies and links images rather than OCRing them. Image-only tables, maps, equations, and review/list blocks are therefore visible in the package but not searchable as text unless a later image OCR/collation pass is run.
2. Print page ranges are not encoded in the EPUB. Chunk page metadata and README page ranges are marked `not encoded in EPUB` pending collation against a paginated PDF or print copy.
3. Superscript determinatives and complex superscript strings, especially in Anatolian/Hittite contexts, were preserved as HTML `<sup>…</sup>` rather than normalized to Unicode, because not all had safe one-character equivalents.
4. The EPUB may contain consistent source-layer errors that this pass cannot detect without collation against the printed book or a publisher PDF.
5. Some image labels such as table numbers are inferred from EPUB filenames (`c12t005` → Table 12.5) where no caption text is encoded near the image. These are file-structure inferences, not print-verified captions.
6. The EPUB manifest includes 404 glyph-like image assets by filename. None are referenced by XHTML `img` tags in the spine; they were not copied as figures and were not inserted as text glyphs.

## Confusion-pair report

Mechanically detectable checks only; this does not certify correctness.

- `h₁ h₂ h₃` vs. `h1 h2 h3`: output counts h₁=423, h₂=668, h₃=206; isolated ASCII h1=0, h2=0, h3=0. Not fully visually verified.
- Macron vowels: ā=1929, ē=991, ī=636, ō=938, ū=425. Combining macron U+0304 count=57; combining marks may be source-authentic in some contexts and are not automatically errors.
- Macron consistency across body/index/reference sections: not fully verified. Index sections were preserved one entry per line, but image-internal table text remains non-searchable image content.
- `ʰ ʷ` vs ASCII `h w`: ʰ=13, ʷ=546. ASCII h/w inside linguistic strings cannot be exhaustively distinguished mechanically in this pass.
- `ə` vs `e`/`9`: ə=237; isolated nonnumeric `9` contexts=225; not fully verified.
- Underdotted/syllabic signs: combining-diacritic count=3171; `r̥`=267; `l̥`=49. Not fully verified.
- Marked palatals vs apostrophe substitutions: `g'`/`g´` contexts=0; `k'`/`k´` contexts=0. Fortson’s EPUB often uses combining-mark forms such as `g̑` and `k̑`; counts: g̑=393, k̑=362.
- Asterisk `*` before reconstructed forms: wrong-star-symbol scan (`✱` plus `×`)=1. Note that `×` can occur source-authentically in non-asterisk contexts, so this mechanical count is not proof of error.
- Dagger `†`: count=0; not fully verified.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 423,
    "h2": 668,
    "h3": 206
  },
  "macron_a": 1929,
  "macron_e": 991,
  "macron_i": 636,
  "macron_o": 938,
  "macron_u": 425,
  "schwa": 237,
  "greek_chars": 328,
  "combining_diacritics": 3171,
  "dagger": 0,
  "modifier_w": 546,
  "modifier_h": 13,
  "g_with_combining_mark": 393,
  "k_with_combining_mark": 362,
  "syllabic_r": 267,
  "syllabic_l": 49,
  "markdown_image_links": 130,
  "unique_images_copied": 130,
  "image_placements": 130,
  "xhtml_files_processed": 36,
  "xhtml_tables": 48
}
```

## Structural integrity check

- Markdown content files produced before report/manifest: 25.
- Heading counts: {'#': 45, '##': 229, '###': 294, '####': 181}.
- Actual XHTML tables converted to Markdown tables: 48.
- Chapter-level chunking follows the EPUB/source chapter structure: front matter, chapters 1–20, glossary, bibliography, and combined index.
- Bibliography is separate from chapter files.
- Subject Index and Word Index are preserved in the combined index file with one entry per Markdown line/list item.
- Images are present as files in `images/` and linked at their source locations in the Markdown.
- No print/PDF collation was performed; no claim is made that source-layer errors absent from the XHTML were caught.

## Image-glyph inventory

- Glyph-like image assets in OPF manifest: 404.
- Glyph-like image assets referenced by XHTML `img` tags: 0.
- Unicode substitutions inserted: 0.
- Unresolved `[image-glyph: …]` annotations inserted: 0.

### Unicode substitutions

- None encountered in XHTML `img` tags in this pass.

### Unresolved image glyphs

- None encountered in XHTML `img` tags in this pass.

### Unreferenced glyph-like image assets

The following OPF image assets look like inline glyph files by filename but were not referenced by XHTML `img` tags in the spine. They are reported for auditability, not treated as missing text:

- `acedil.jpg`
- `acedil1.jpg`
- `acedil1b.jpg`
- `acedil2.jpg`
- `acediltilde.jpg`
- `acediltilde2.jpg`
- `aeligmacr.jpg`
- `aeligmacr1.jpg`
- `aeligmacr1b.jpg`
- `aeligmacr2.jpg`
- `alphacedil.jpg`
- `alphacedilacute.jpg`
- `amacr.jpg`
- `amacr1.jpg`
- `amacr1b.jpg`
- `amacr2.jpg`
- `amacr3.jpg`
- `amacracute.jpg`
- `amacracute1.jpg`
- `amacracute1b.jpg`
- `amacracute2.jpg`
- `amacracuteb.jpg`
- `amacragrave.jpg`
- `amacragrave1.jpg`
- `amacragrave1b.jpg`
- `amacrb.jpg`
- `amacrcurve.jpg`
- `amacrring.jpg`
- `amacrring1.jpg`
- `amacrring1b.jpg`
- `amacrtilde.jpg`
- `amacrtildeb.jpg`
- `amacrtring.jpg`
- `amacrtring2.jpg`
- `btline.jpg`
- `btline1.jpg`
- `cacute.jpg`
- `cacute1.jpg`
- `cacuteb.jpg`
- `capamacr.jpg`
- `capamacr1.jpg`
- `capccaron.jpg`
- `capccaron1.jpg`
- `capccaron1b.jpg`
- `capccaron3.jpg`
- `capccedil1.jpg`
- `capemacr.jpg`
- `capemacr2.jpg`
- `caphcurve.jpg`
- `caphcurve1.jpg`
- `caphucurve.jpg`
- `caphucurve1.jpg`
- `caphuring.jpg`
- `capimacr.jpg`
- `capimacracute.jpg`
- `caplslash1.jpg`
- `caprdown.jpg`
- `caprdring.jpg`
- `capruring1.jpg`
- `capsacute.jpg`
- `capsacute1.jpg`
- `capumacr.jpg`
- `capvmacr.jpg`
- `capzcaron.jpg`
- `ccaron.jpg`
- `ccaron1.jpg`
- `ccaron1b.jpg`
- `ccaron2.jpg`
- `ccaronb.jpg`
- `ccaronsupc.jpg`
- `ccaronsupc1.jpg`
- `ccaronsupc1b.jpg`
- `ccaronsupc2.jpg`
- `csupc.jpg`
- `csupc1.jpg`
- `csupc1b.jpg`
- `curve.jpg`
- `downc.jpg`
- `downe.jpg`
- `downomega.jpg`
- `dtline.jpg`
- `dudot.jpg`
- `dudot1.jpg`
- `dudot2.jpg`
- `dudotb.jpg`
- `ecaron.jpg`
- `ecaron1.jpg`
- `ecaron1b.jpg`
- `ecaron2.jpg`
- `ecaronb.jpg`
- `ecedil.jpg`
- `ecedil1.jpg`
- `ecedil1b.jpg`
- `ecedil2.jpg`
- `ecedilb.jpg`
- `edown.jpg`
- `edown1.jpg`
- `edown1b.jpg`
- `edown2.jpg`
- `edownb.jpg`
- `edownmacr.jpg`
- `edownmacr1.jpg`
- `edownmacrb.jpg`
- `emacr.jpg`
- `emacr1.jpg`
- `emacr1b.jpg`
- `emacr2.jpg`
- `emacr3.jpg`
- `emacr3b.jpg`
- `emacracute.jpg`
- `emacracute1.jpg`
- `emacracute1b.jpg`
- `emacracute2.jpg`
- `emacracuteb.jpg`
- `emacragrave.jpg`
- `emacrb.jpg`
- `emacrtilde.jpg`
- `emacrtilde1.jpg`
- `emacrtilde1b.jpg`
- `etdgrave.jpg`
- `etdgrave1.jpg`
- `etdot.jpg`
- `etdot1.jpg`
- `etdot1b.jpg`
- `etdot2.jpg`
- `etdotacute.jpg`
- `etdotacute2.jpg`
- `etdotacuteb.jpg`
- `etdottilde.jpg`
- `etdottilde1.jpg`
- `etdottilde1b.jpg`
- `etdottilde2.jpg`
- `etilde.jpg`
- `etilde1.jpg`
- `etilde1b.jpg`
- `etilde2.jpg`
- `fr-cacute.jpg`
- `ftdot.jpg`
- `ftdot1b.jpg`
- `ftdot2.jpg`
- `galsuphucurve.jpg`
- `gdot.jpg`
- `grave.jpg`
- `gt1curve.jpg`
- `gtcurve.jpg`
- `gtcurve1.jpg`
- `gtcurve2.jpg`
- `gtcurve3.jpg`
- `gtcurveb.jpg`
- `guline.jpg`
- `guucurve.jpg`
- `h-amacr.jpg`
- `h-amacracute.jpg`
- `h-imacracute1.jpg`
- `h-nudot.jpg`
- `h-ruring1.jpg`
- `h-sacute.jpg`
- `h-sacute1.jpg`
- `htline1.jpg`
- `hucurve.jpg`
- `hucurve1.jpg`
- `hucurve1b.jpg`
- `hucurve2.jpg`
- `hucurveb.jpg`
- `hudot.jpg`
- `hudot1.jpg`
- `hudot1b.jpg`
- `hudot2.jpg`
- `hudotb.jpg`
- `huring.jpg`
- `icaron.jpg`
- `icedil.jpg`
- `icedil2.jpg`
- `icediltilde.jpg`
- `imacr.jpg`
- `imacr1.jpg`
- `imacr1b.jpg`
- `imacr2.jpg`
- `imacr3.jpg`
- `imacracute.jpg`
- `imacracuteb.jpg`
- `imacrb.jpg`
- `imacrtilde.jpg`
- `istrike.jpg`
- `itcurve.jpg`
- `itcurve1.jpg`
- `itcurve1b.jpg`
- `itcurve2.jpg`
- `itcurveb.jpg`
- `itilde.jpg`
- `itilde1.jpg`
- `itilde1b.jpg`
- `itilde2.jpg`
- `itildeb.jpg`
- `iucurve.jpg`
- `iucurve2.jpg`
- `iucurveb.jpg`
- `jacute.jpg`
- `jcaron.jpg`
- `jcaron1.jpg`
- `jcaronb.jpg`
- `ksupc.jpg`
- `ksupc1.jpg`
- `ksupc2.jpg`
- `ksupcb.jpg`
- `ktcurve.jpg`
- `ktcurve1.jpg`
- `ktcurve2.jpg`
- `ktcurve2b.jpg`
- `ktcurveb.jpg`
- `kuucurve.jpg`
- `lacuteuring.jpg`
- `lacuteuringb.jpg`
- `lambdacedil.jpg`
- `lcedil.jpg`
- `lmacruring.jpg`
- `lslash.jpg`
- `lslash1.jpg`
- `lslash1b.jpg`
- `lslash2.jpg`
- `lslash3.jpg`
- `lstrike.jpg`
- `ltildeb.jpg`
- `lttilde.jpg`
- `lucedil.jpg`
- `lucedil1.jpg`
- `ludot.jpg`
- `luring.jpg`
- `luring2.jpg`
- `luringb.jpg`
- `macuteuring.jpg`
- `mmacruring.jpg`
- `mtcurvedot.jpg`
- `mtcurvedotb.jpg`
- `mtdot.jpg`
- `mtdot1b.jpg`
- `mtdot2.jpg`
- `mtdotb.jpg`
- `mtilde.jpg`
- `mtilde1.jpg`
- `mtilde1b.jpg`
- `mtilde2.jpg`
- `mtildeb.jpg`
- `mudot.jpg`
- `mudot1.jpg`
- `mudot1b.jpg`
- `mudot2.jpg`
- `mudotb.jpg`
- `muring.jpg`
- `muring2.jpg`
- `muringacute.jpg`
- `muringacuteb.jpg`
- `muringb.jpg`
- `nacute1.jpg`
- `ncedil.jpg`
- `nddot1b.jpg`
- `ndring.jpg`
- `ndringb.jpg`
- `nmacruring.jpg`
- `ntdot.jpg`
- `ntdot1.jpg`
- `ntdot1b.jpg`
- `ntdot2.jpg`
- `ntilde.jpg`
- `nudot.jpg`
- `nudot1.jpg`
- `nudot1b.jpg`
- `nudot2.jpg`
- `nudotb.jpg`
- `nuring.jpg`
- `nuring2.jpg`
- `nuringacute.jpg`
- `nuringacuteb.jpg`
- `nuringb.jpg`
- `ocedil.jpg`
- `ocedil1.jpg`
- `ocedil1b.jpg`
- `ocedil2.jpg`
- `ocedilacute.jpg`
- `ocedilb.jpg`
- `omacr.jpg`
- `omacr1.jpg`
- `omacr1b.jpg`
- `omacr2.jpg`
- `omacr3.jpg`
- `omacr3b.jpg`
- `omacracute.jpg`
- `omacracute1.jpg`
- `omacracute1b.jpg`
- `omacracute2.jpg`
- `omacragrave1.jpg`
- `omacragrave1b.jpg`
- `omacrb.jpg`
- `omacrcurve.jpg`
- `omacrtilde.jpg`
- `omacrtilde1.jpg`
- `omacrtilde1b.jpg`
- `omacrtilde2.jpg`
- `omacrtildeb.jpg`
- `omegacedil.jpg`
- `psupc.jpg`
- `psupc1-1.jpg`
- `psupc1.jpg`
- `psupc1b.jpg`
- `racuteuring.jpg`
- `racuteuring1.jpg`
- `racuteuring2.jpg`
- `racuteuringb.jpg`
- `rcaron.jpg`
- `rcaron1.jpg`
- `rcaron1b.jpg`
- `rcaron3.jpg`
- `rcaronbold.jpg`
- `rmacracuteuring.jpg`
- `rmacruring.jpg`
- `rtdot.jpg`
- `rtdot1.jpg`
- `rtilde.jpg`
- `rtilde1.jpg`
- `ruring.jpg`
- `ruring1.jpg`
- `ruring1b.jpg`
- `ruring2.jpg`
- `ruring2b.jpg`
- `ruringb.jpg`
- `sacute.jpg`
- `sacute1.jpg`
- `sacute1b.jpg`
- `sacute2.jpg`
- `sacute2b.jpg`
- `sacuteb.jpg`
- `scaronacute.jpg`
- `scaronudot.jpg`
- `scedil.jpg`
- `scedil1.jpg`
- `stdot.jpg`
- `stdot2.jpg`
- `subedownt.jpg`
- `sudot.jpg`
- `sudot1.jpg`
- `sudot1b.jpg`
- `sudot2.jpg`
- `sudotb.jpg`
- `tdot.jpg`
- `tsupc.jpg`
- `tsupc1.jpg`
- `tsupcb.jpg`
- `tudot.jpg`
- `tudot1.jpg`
- `tudot2.jpg`
- `tudot2b.jpg`
- `tudot3.jpg`
- `tudotb.jpg`
- `tutilde.jpg`
- `tutilde1.jpg`
- `tutilde1b.jpg`
- `tutilde2.jpg`
- `umacr.jpg`
- `umacr1.jpg`
- `umacr1b.jpg`
- `umacr2.jpg`
- `umacr3.jpg`
- `umacr3b.jpg`
- `umacracute.jpg`
- `umacracute1.jpg`
- `umacracute1b.jpg`
- `umacracute2.jpg`
- `umacracuteb.jpg`
- `umacrb.jpg`
- `umacrtilde.jpg`
- `umacrtilde2.jpg`
- `umacrtildeb.jpg`
- `upsilonmacr.jpg`
- `utcurve.jpg`
- `utcurve1.jpg`
- `utcurve1b.jpg`
- `utcurve2.jpg`
- `utcurveb.jpg`
- `utdgrave.jpg`
- `utilde.jpg`
- `utilde1.jpg`
- `utilde2.jpg`
- `utildeb.jpg`
- `utildecedil.jpg`
- `utildecedil1.jpg`
- `utildecedil1b.jpg`
- `uttcurve.jpg`
- `uttcurve2.jpg`
- `uucedil.jpg`
- `uucedil1.jpg`
- `uucurve.jpg`
- `uucurve1.jpg`
- `uucurve2.jpg`
- `uucurveb.jpg`
- `v3dot.jpg`
- `xacute.jpg`
- `ymacr.jpg`
- `zacute.jpg`
- `zcaron.jpg`
- `zcaron1.jpg`
- `zcaron1b.jpg`
- `zcaron2.jpg`
- `zcaronb.jpg`
- `ztdot.jpg`

## Image inventory

Image references by type: {'cover': 1, 'title': 1, 'table': 69, 'figure': 20, 'map': 14, 'review-image': 22, 'equation': 2, 'text-sample': 1}

- 1. `fortson-2010-indo-european-language-and-culture-cover.jpg` ← `9781405188968.jpg` — Cover; type=cover; chunk=frontmatter; source-xhtml=`9781405188968_Cover.xhtml`; caption: [none encoded near image]
- 2. `fortson-2010-indo-european-language-and-culture-title.jpg` ← `title.jpg` — Title image; type=title; chunk=frontmatter; source-xhtml=`9781405188968_Title.xhtml`; caption: [none encoded near image]
- 3. `fortson-2010-indo-european-language-and-culture-table1-1.jpg` ← `c01t001.jpg` — Table 1.1; type=table; chunk=Chapter 1; source-xhtml=`9781405188968_001.xhtml`; caption: [none encoded near image]
- 4. `fortson-2010-indo-european-language-and-culture-table1-2.jpg` ← `c01t002.jpg` — Table 1.2; type=table; chunk=Chapter 1; source-xhtml=`9781405188968_001.xhtml`; caption: [none encoded near image]
- 5. `fortson-2010-indo-european-language-and-culture-fig1-1.jpg` ← `c01f001.jpg` — Figure 1.1; type=figure; chunk=Chapter 1; source-xhtml=`9781405188968_001.xhtml`; caption: *Figure 1.1* The Indo-European family tree, showing the approximate geographical distribution of the branches and the principal ancient, medieval, and modern languages of each. The names of branches and subbranches are in boldface. Not all languages or language stages are represented.
- 6. `fortson-2010-indo-european-language-and-culture-map1-1.jpg` ← `c01m001.jpg` — Map 1.1; type=map; chunk=Chapter 1; source-xhtml=`9781405188968_001.xhtml`; caption: *Map 1.1* Geographical distribution of the major Indo-European peoples around 500 <small>BC</small>
- 7. `fortson-2010-indo-european-language-and-culture-p16-fig1.jpg` ← `16.jpg` — Page 16 image; type=review-image; chunk=Chapter 1; source-xhtml=`9781405188968_001.xhtml`; caption: [none encoded near image]
- 8. `fortson-2010-indo-european-language-and-culture-table1-3.jpg` ← `c01t003.jpg` — Table 1.3; type=table; chunk=Chapter 1; source-xhtml=`9781405188968_001.xhtml`; caption: [none encoded near image]
- 9. `fortson-2010-indo-european-language-and-culture-equation2-1.jpg` ← `c02e001.jpg` — Equation 2.1; type=equation; chunk=Chapter 2; source-xhtml=`9781405188968_002.xhtml`; caption: (1.32.1)
- 10. `fortson-2010-indo-european-language-and-culture-equation2-2.jpg` ← `c02e002.jpg` — Equation 2.2; type=equation; chunk=Chapter 2; source-xhtml=`9781405188968_002.xhtml`; caption: (7.89.1)
- 11. `fortson-2010-indo-european-language-and-culture-map2-1.jpg` ← `c02m001.jpg` — Map 2.1; type=map; chunk=Chapter 2; source-xhtml=`9781405188968_002.xhtml`; caption: *Map 2.1* Selected Late Neolithic and Chalcolithic (Bronze Age) cultures north of the Black and Caspian Seas
- 12. `fortson-2010-indo-european-language-and-culture-p50-fig1.jpg` ← `50.jpg` — Page 50 image; type=review-image; chunk=Chapter 2; source-xhtml=`9781405188968_002.xhtml`; caption: [none encoded near image]
- 13. `fortson-2010-indo-european-language-and-culture-table3-1.jpg` ← `c03t001.jpg` — Table 3.1; type=table; chunk=Chapter 3; source-xhtml=`9781405188968_003.xhtml`; caption: [none encoded near image]
- 14. `fortson-2010-indo-european-language-and-culture-table3-2.jpg` ← `c03t002.jpg` — Table 3.2; type=table; chunk=Chapter 3; source-xhtml=`9781405188968_003.xhtml`; caption: [none encoded near image]
- 15. `fortson-2010-indo-european-language-and-culture-table3-3.jpg` ← `c03t003.jpg` — Table 3.3; type=table; chunk=Chapter 3; source-xhtml=`9781405188968_003.xhtml`; caption: [none encoded near image]
- 16. `fortson-2010-indo-european-language-and-culture-p56-fig1.jpg` ← `56.jpg` — Page 56 image; type=review-image; chunk=Chapter 3; source-xhtml=`9781405188968_003.xhtml`; caption: [none encoded near image]
- 17. `fortson-2010-indo-european-language-and-culture-p57-fig1.jpg` ← `57.jpg` — Page 57 image; type=review-image; chunk=Chapter 3; source-xhtml=`9781405188968_003.xhtml`; caption: [none encoded near image]
- 18. `fortson-2010-indo-european-language-and-culture-table3-4.jpg` ← `c03t004.jpg` — Table 3.4; type=table; chunk=Chapter 3; source-xhtml=`9781405188968_003.xhtml`; caption: [none encoded near image]
- 19. `fortson-2010-indo-european-language-and-culture-table3-5.jpg` ← `c03t005.jpg` — Table 3.5; type=table; chunk=Chapter 3; source-xhtml=`9781405188968_003.xhtml`; caption: [none encoded near image]
- 20. `fortson-2010-indo-european-language-and-culture-p73-fig1.jpg` ← `73.jpg` — Page 73 image; type=review-image; chunk=Chapter 3; source-xhtml=`9781405188968_003.xhtml`; caption: [none encoded near image]
- 21. `fortson-2010-indo-european-language-and-culture-p85-fig1.jpg` ← `85.jpg` — Page 85 image; type=review-image; chunk=Chapter 4; source-xhtml=`9781405188968_004.xhtml`; caption: [none encoded near image]
- 22. `fortson-2010-indo-european-language-and-culture-table5-1.jpg` ← `c05t001.jpg` — Table 5.1; type=table; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 23. `fortson-2010-indo-european-language-and-culture-table5-2.jpg` ← `c05t002.jpg` — Table 5.2; type=table; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 24. `fortson-2010-indo-european-language-and-culture-table5-3.jpg` ← `c05t003.jpg` — Table 5.3; type=table; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 25. `fortson-2010-indo-european-language-and-culture-table5-4.jpg` ← `c05t004.jpg` — Table 5.4; type=table; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 26. `fortson-2010-indo-european-language-and-culture-table5-5.jpg` ← `c05t005.jpg` — Table 5.5; type=table; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 27. `fortson-2010-indo-european-language-and-culture-table5-6.jpg` ← `c05t006.jpg` — Table 5.6; type=table; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 28. `fortson-2010-indo-european-language-and-culture-p103-fig1.jpg` ← `103.jpg` — Page 103 image; type=review-image; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 29. `fortson-2010-indo-european-language-and-culture-table5-7.jpg` ← `c05t007.jpg` — Table 5.7; type=table; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 30. `fortson-2010-indo-european-language-and-culture-p104-fig1.jpg` ← `104.jpg` — Page 104 image; type=review-image; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 31. `fortson-2010-indo-european-language-and-culture-p106-fig1.jpg` ← `106.jpg` — Page 106 image; type=review-image; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 32. `fortson-2010-indo-european-language-and-culture-table5-8.jpg` ← `c05t008.jpg` — Table 5.8; type=table; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 33. `fortson-2010-indo-european-language-and-culture-p110-fig1.jpg` ← `110.jpg` — Page 110 image; type=review-image; chunk=Chapter 5; source-xhtml=`9781405188968_005.xhtml`; caption: [none encoded near image]
- 34. `fortson-2010-indo-european-language-and-culture-fig6-1.jpg` ← `c06f001.jpg` — Figure 6.1; type=figure; chunk=Chapter 6; source-xhtml=`9781405188968_006.xhtml`; caption: [none encoded near image]
- 35. `fortson-2010-indo-european-language-and-culture-table6-1.jpg` ← `c06t001.jpg` — Table 6.1; type=table; chunk=Chapter 6; source-xhtml=`9781405188968_006.xhtml`; caption: [none encoded near image]
- 36. `fortson-2010-indo-european-language-and-culture-table6-2.jpg` ← `c06t002.jpg` — Table 6.2; type=table; chunk=Chapter 6; source-xhtml=`9781405188968_006.xhtml`; caption: [none encoded near image]
- 37. `fortson-2010-indo-european-language-and-culture-fig6-2.jpg` ← `c06f002.jpg` — Figure 6.2; type=figure; chunk=Chapter 6; source-xhtml=`9781405188968_006.xhtml`; caption: [none encoded near image]
- 38. `fortson-2010-indo-european-language-and-culture-table6-3.jpg` ← `c06t003.jpg` — Table 6.3; type=table; chunk=Chapter 6; source-xhtml=`9781405188968_006.xhtml`; caption: [none encoded near image]
- 39. `fortson-2010-indo-european-language-and-culture-table6-4.jpg` ← `c06t004.jpg` — Table 6.4; type=table; chunk=Chapter 6; source-xhtml=`9781405188968_006.xhtml`; caption: [none encoded near image]
- 40. `fortson-2010-indo-european-language-and-culture-table6-5.jpg` ← `c06t005.jpg` — Table 6.5; type=table; chunk=Chapter 6; source-xhtml=`9781405188968_006.xhtml`; caption: [none encoded near image]
- 41. `fortson-2010-indo-european-language-and-culture-table6-6.jpg` ← `c06t006.jpg` — Table 6.6; type=table; chunk=Chapter 6; source-xhtml=`9781405188968_006.xhtml`; caption: [none encoded near image]
- 42. `fortson-2010-indo-european-language-and-culture-table6-6a.jpg` ← `c06t006a.jpg` — Table 6.6a; type=table; chunk=Chapter 6; source-xhtml=`9781405188968_006.xhtml`; caption: [none encoded near image]
- 43. `fortson-2010-indo-european-language-and-culture-p138-fig1.jpg` ← `138.jpg` — Page 138 image; type=review-image; chunk=Chapter 6; source-xhtml=`9781405188968_006.xhtml`; caption: [none encoded near image]
- 44. `fortson-2010-indo-european-language-and-culture-table7-1.jpg` ← `c07t001.jpg` — Table 7.1; type=table; chunk=Chapter 7; source-xhtml=`9781405188968_007.xhtml`; caption: [none encoded near image]
- 45. `fortson-2010-indo-european-language-and-culture-table7-2.jpg` ← `c07t002.jpg` — Table 7.2; type=table; chunk=Chapter 7; source-xhtml=`9781405188968_007.xhtml`; caption: [none encoded near image]
- 46. `fortson-2010-indo-european-language-and-culture-table7-3.jpg` ← `c07t003.jpg` — Table 7.3; type=table; chunk=Chapter 7; source-xhtml=`9781405188968_007.xhtml`; caption: [none encoded near image]
- 47. `fortson-2010-indo-european-language-and-culture-table7-4.jpg` ← `c07t004.jpg` — Table 7.4; type=table; chunk=Chapter 7; source-xhtml=`9781405188968_007.xhtml`; caption: [none encoded near image]
- 48. `fortson-2010-indo-european-language-and-culture-table7-4a.jpg` ← `c07t004a.jpg` — Table 7.4a; type=table; chunk=Chapter 7; source-xhtml=`9781405188968_007.xhtml`; caption: [none encoded near image]
- 49. `fortson-2010-indo-european-language-and-culture-p168-fig1.jpg` ← `168.jpg` — Page 168 image; type=review-image; chunk=Chapter 8; source-xhtml=`9781405188968_008.xhtml`; caption: [none encoded near image]
- 50. `fortson-2010-indo-european-language-and-culture-map9-1.jpg` ← `c09m001.jpg` — Map 9.1; type=map; chunk=Chapter 9; source-xhtml=`9781405188968_009.xhtml`; caption: *Map 9.1* Anatolia: combined view of the major principalities and historical regions of both the Bronze Age and the Hellenistic period
- 51. `fortson-2010-indo-european-language-and-culture-table9-1.jpg` ← `c09t001.jpg` — Table 9.1; type=table; chunk=Chapter 9; source-xhtml=`9781405188968_009.xhtml`; caption: [none encoded near image]
- 52. `fortson-2010-indo-european-language-and-culture-table9-2.jpg` ← `c09t002.jpg` — Table 9.2; type=table; chunk=Chapter 9; source-xhtml=`9781405188968_009.xhtml`; caption: [none encoded near image]
- 53. `fortson-2010-indo-european-language-and-culture-fig9-1.jpg` ← `c09f001.jpg` — Figure 9.1; type=figure; chunk=Chapter 9; source-xhtml=`9781405188968_009.xhtml`; caption: *Figure 9.1* One of the fragments composing KBo 17.1. The top line begins in the middle of line 1: the broken sign is UTU, followed closely by *uš* and then a short word-break. Underneath UTU is the right part of LUGAL in line 2 followed again by *uš*. Note the “right justification” of several of the lines, where the last sign or signs of a line were delayed until near the edge of the tablet. Drawing from Heinrich Otten, *Keilschrifttexte aus Boghazköi*, vol. 17 (Berlin: Mann, 1969), p. 3. Reproduced by permission.
- 54. `fortson-2010-indo-european-language-and-culture-fig9-2.jpg` ← `c09f002.jpg` — Figure 9.2; type=figure; chunk=Chapter 9; source-xhtml=`9781405188968_009.xhtml`; caption: *Figure 9.2* The Hieroglyphic Luvian inscription HAMA 2. Each line of text is divided into vertical groupings that are read top to bottom, and successively from right to left in the first line. The direction is reversed in each successive line; faces always point away from the direction of writing (facing the approaching eyes of the reader, as it were). The first group of signs is in the upper right with the figure pointing at himself (EGO) followed by the rectangular signs below that (*mi*). Drawing by David Hawkins from Hawkins 2000 (vol. 1, part 3, plate 222). Reproduced by permission of the publisher.
- 55. `fortson-2010-indo-european-language-and-culture-fig9-3.jpg` ← `c09f003.jpg` — Figure 9.3; type=figure; chunk=Chapter 9; source-xhtml=`9781405188968_009.xhtml`; caption: *Figure 9.3* The Lydian bilingual. The Lydian text is the upper part, beginning in the upper right and reading from right to left (the first easily visible letters are the A and Λ of *oraλ*). Photograph from W. H. Buckler, *Sardis*, Vol. VI: *Lydian Inscriptions*, Part II (Leiden: Brill, 1924).
- 56. `fortson-2010-indo-european-language-and-culture-p199-fig1.jpg` ← `199.jpg` — Page 199 image; type=review-image; chunk=Chapter 9; source-xhtml=`9781405188968_009.xhtml`; caption: [none encoded near image]
- 57. `fortson-2010-indo-european-language-and-culture-p210-fig1.jpg` ← `210.jpg` — Page 210 image; type=review-image; chunk=Chapter 10; source-xhtml=`9781405188968_010.xhtml`; caption: [none encoded near image]
- 58. `fortson-2010-indo-european-language-and-culture-table10-1.jpg` ← `c10t001.jpg` — Table 10.1; type=table; chunk=Chapter 10; source-xhtml=`9781405188968_010.xhtml`; caption: [none encoded near image]
- 59. `fortson-2010-indo-european-language-and-culture-table10-2.jpg` ← `c10t002.jpg` — Table 10.2; type=table; chunk=Chapter 10; source-xhtml=`9781405188968_010.xhtml`; caption: [none encoded near image]
- 60. `fortson-2010-indo-european-language-and-culture-table10-2a.jpg` ← `c10t002a.jpg` — Table 10.2a; type=table; chunk=Chapter 10; source-xhtml=`9781405188968_010.xhtml`; caption: [none encoded near image]
- 61. `fortson-2010-indo-european-language-and-culture-table10-3.jpg` ← `c10t003.jpg` — Table 10.3; type=table; chunk=Chapter 10; source-xhtml=`9781405188968_010.xhtml`; caption: [none encoded near image]
- 62. `fortson-2010-indo-european-language-and-culture-table10-3a.jpg` ← `c10t003a.jpg` — Table 10.3a; type=table; chunk=Chapter 10; source-xhtml=`9781405188968_010.xhtml`; caption: [none encoded near image]
- 63. `fortson-2010-indo-european-language-and-culture-map10-1.jpg` ← `c10m001.jpg` — Map 10.1; type=map; chunk=Chapter 10; source-xhtml=`9781405188968_010.xhtml`; caption: *Map 10.1* Modern Indo-Aryan languages
- 64. `fortson-2010-indo-european-language-and-culture-p224-fig1.jpg` ← `224.jpg` — Page 224 image; type=review-image; chunk=Chapter 10; source-xhtml=`9781405188968_010.xhtml`; caption: [none encoded near image]
- 65. `fortson-2010-indo-european-language-and-culture-fig11-1.jpg` ← `c11f001.jpg` — Figure 11.1; type=figure; chunk=Chapter 11; source-xhtml=`9781405188968_011.xhtml`; caption: *Figure 11.1* Yasna 44.4 in Avestan script, read from right to left. Reproduced with slight alterations from Geldner 1886–96, vol. 1, p. 148.
- 66. `fortson-2010-indo-european-language-and-culture-map11-1.jpg` ← `c11m001.jpg` — Map 11.1; type=map; chunk=Chapter 11; source-xhtml=`9781405188968_011.xhtml`; caption: *Map 11.1* The Persian Empire under Darius I
- 67. `fortson-2010-indo-european-language-and-culture-fig11-2.jpg` ← `c11f002.jpg` — Figure 11.2; type=figure; chunk=Chapter 11; source-xhtml=`9781405188968_011.xhtml`; caption: *Map 11.2* Selected Modern Iranian languages.
- 68. `fortson-2010-indo-european-language-and-culture-map12-1.jpg` ← `c12m001.jpg` — Map 12.1; type=map; chunk=Chapter 12; source-xhtml=`9781405188968_012.xhtml`; caption: *Map 12.1* Greek dialects
- 69. `fortson-2010-indo-european-language-and-culture-table12-1.jpg` ← `c12t001.jpg` — Table 12.1; type=table; chunk=Chapter 12; source-xhtml=`9781405188968_012.xhtml`; caption: [none encoded near image]
- 70. `fortson-2010-indo-european-language-and-culture-table12-2.jpg` ← `c12t002.jpg` — Table 12.2; type=table; chunk=Chapter 12; source-xhtml=`9781405188968_012.xhtml`; caption: [none encoded near image]
- 71. `fortson-2010-indo-european-language-and-culture-table12-3.jpg` ← `c12t003.jpg` — Table 12.3; type=table; chunk=Chapter 12; source-xhtml=`9781405188968_012.xhtml`; caption: [none encoded near image]
- 72. `fortson-2010-indo-european-language-and-culture-table12-4.jpg` ← `c12t004.jpg` — Table 12.4; type=table; chunk=Chapter 12; source-xhtml=`9781405188968_012.xhtml`; caption: [none encoded near image]
- 73. `fortson-2010-indo-european-language-and-culture-table12-5.jpg` ← `c12t005.jpg` — Table 12.5; type=table; chunk=Chapter 12; source-xhtml=`9781405188968_012.xhtml`; caption: [none encoded near image]
- 74. `fortson-2010-indo-european-language-and-culture-p1.jpg` ← `p1.jpg` — Text sample p1; type=text-sample; chunk=Chapter 12; source-xhtml=`9781405188968_012.xhtml`; caption: [none encoded near image]
- 75. `fortson-2010-indo-european-language-and-culture-fig12-1.jpg` ← `c12f001.jpg` — Figure 12.1; type=figure; chunk=Chapter 12; source-xhtml=`9781405188968_012.xhtml`; caption: *Figure 12.1* The Pylos tablet Ta 722. The “footstool” pictogram is the second-rightmost sign on each line. Drawing from Emmett L. Bennett, Jr., *The Pylos Tablets: Texts of the Inscriptions Found 1939–1954* (Princeton: Princeton University Press, 1954), p. 87. Reproduced by permission of the publisher.
- 76. `fortson-2010-indo-european-language-and-culture-fig12-2.jpg` ← `c12f002.jpg` — Figure 12.2; type=figure; chunk=Chapter 12; source-xhtml=`9781405188968_012.xhtml`; caption: *Figure 12.2* Column V of the Gortynian law-code. Line 28 is the second full line of text after the second horizontal seam between two blocks of stone; our excerpt begins after a small space two-thirds through the line. It reads at first left-to-right and then switches direction every line (boustrophedon). The alphabet is among the most archaic of the Greek alphabets, having several letters close in shape to their Phoenician sources. Iota looks like an S, pi like a C, sigma like an M, and theta like a circle enclosing a cross; E and O are used for both short and long *e* and *o*. Drawing reproduced from Margarita Guarducci, *Inscriptiones Creticae opera et consilio Friderici Halbherr collectae*, IV: *Tituli Gortynii* (Rome: Libreria dello Stato, 1950), pp. 142–3 (foldout).
- 77. `fortson-2010-indo-european-language-and-culture-map13-1.jpg` ← `c13m001.jpg` — Map 13.1; type=map; chunk=Chapter 13; source-xhtml=`9781405188968_013.xhtml`; caption: *Map 13.1* Languages of ancient Italy before Roman expansion
- 78. `fortson-2010-indo-european-language-and-culture-p278-fig1.jpg` ← `278.jpg` — Page 278 image; type=review-image; chunk=Chapter 13; source-xhtml=`9781405188968_013.xhtml`; caption: [none encoded near image]
- 79. `fortson-2010-indo-european-language-and-culture-table13-1.jpg` ← `c13t001.jpg` — Table 13.1; type=table; chunk=Chapter 13; source-xhtml=`9781405188968_013.xhtml`; caption: [none encoded near image]
- 80. `fortson-2010-indo-european-language-and-culture-table13-2.jpg` ← `c13t002.jpg` — Table 13.2; type=table; chunk=Chapter 13; source-xhtml=`9781405188968_013.xhtml`; caption: [none encoded near image]
- 81. `fortson-2010-indo-european-language-and-culture-fig13-1.jpg` ← `c13f001.jpg` — Figure 13.1; type=figure; chunk=Chapter 13; source-xhtml=`9781405188968_013.xhtml`; caption: *Figure 13.1* The Duenos inscription. The text starts at the top and goes around counterclockwise from there. The three larger circles represent the three connected pots around which the inscription is written. Drawing from Atilius Degrassi, *Inscriptiones latinae liberae rei publicae: Imagines* (Berlin: de Gruyter, 1965), p. 261. Reproduced by permission of the publisher.
- 82. `fortson-2010-indo-european-language-and-culture-fig13-2.jpg` ← `c13f002.jpg` — Figure 13.2; type=figure; chunk=Chapter 13; source-xhtml=`9781405188968_013.xhtml`; caption: *Figure 13.2* The Ceres inscription. The text begins right below the center and curves counterclockwise around the bottom of the bowl. Drawing reproduced from O. A. Danielsson and G. Herbig, *Corpus Inscriptionum Etruscarum*, vol. 2, part 2, fascicle 1 (Leipzig: Barth, 1912), no. 8079 (p. 23).
- 83. `fortson-2010-indo-european-language-and-culture-fig13-3.jpg` ← `c13f003.jpg` — Figure 13.3; type=figure; chunk=Chapter 13; source-xhtml=`9781405188968_013.xhtml`; caption: *Figure 13.3* The South Picene inscription Sp TE 2. The inscription begins near the bottom of the inner of the two vertical lines of text on the left (right above the vertically stacked triple dots) and proceeds upwards and then clockwise around. Drawing reproduced from Marinetti 1985, p. 204. Reproduced by permission of the publisher.
- 84. `fortson-2010-indo-european-language-and-culture-fig13-4.jpg` ← `c13f004.jpg` — Figure 13.4; type=figure; chunk=Chapter 13; source-xhtml=`9781405188968_013.xhtml`; caption: *Figure 13.4* The Oscan inscription Po 3. The lines read from right to left. Note that what looks like an R in this alphabet is actually a D, and vice versa. The dot above a V and the very short horizontal stroke extending rightward from the stem of an I are the signs conventionally transliterated by an acute accent. Drawing from Iohannes Zvetaieff, *Sylloge Inscriptionum Oscarum ad Archetyporum et Librorum Fidem* (St. Petersburg: Brockhaus, 1878), plate XI.
- 85. `fortson-2010-indo-european-language-and-culture-p304-fig1.jpg` ← `304.jpg` — Page 304 image; type=review-image; chunk=Chapter 13; source-xhtml=`9781405188968_013.xhtml`; caption: [none encoded near image]
- 86. `fortson-2010-indo-european-language-and-culture-map14-1.jpg` ← `c14m001.jpg` — Map 14.1; type=map; chunk=Chapter 14; source-xhtml=`9781405188968_014.xhtml`; caption: *Map 14.1* The Celts
- 87. `fortson-2010-indo-european-language-and-culture-fig14-1.jpg` ← `c14f001.jpg` — Figure 14.1; type=figure; chunk=Chapter 14; source-xhtml=`9781405188968_014.xhtml`; caption: *Figure 14.1* The Chamalières inscription, written in an ancient cursive form of the Latin alphabet that has no relationship to our modern cursive script. The excerpt begins at the end of the sixth line from the bottom (the smudge comes between the *n* and *c* of *toncnaman*). An I twice the height of a normal I is rendered as *í* in the transliteration. Drawing by R. Marichal, from Pierre-Yves Lambert, *Recueil des inscriptions gauloises,* vol. II, fasc. 2: *Textes gallo-latins sur* instrumentum (Paris: CNRS, 2002), p. 271. Reproduced by permission of the publisher.
- 88. `fortson-2010-indo-european-language-and-culture-fig14-2.jpg` ← `c14f002.jpg` — Figure 14.2; type=figure; chunk=Chapter 14; source-xhtml=`9781405188968_014.xhtml`; caption: *Figure 14.2* The front side of the first Botorrita inscription. The inscription reads from left to right; most word-divisions are indicated by double dots (though these are missing after the first word). Drawing from Untermann 1997, vol. 4, p. 567. Copyright Dr. Ludwig Reichert Verlag Wiesbaden. Reproduced by permission of the publisher.
- 89. `fortson-2010-indo-european-language-and-culture-table14-1.jpg` ← `c14t001.jpg` — Table 14.1; type=table; chunk=Chapter 14; source-xhtml=`9781405188968_014.xhtml`; caption: [none encoded near image]
- 90. `fortson-2010-indo-european-language-and-culture-table14-2.jpg` ← `c14t002.jpg` — Table 14.2; type=table; chunk=Chapter 14; source-xhtml=`9781405188968_014.xhtml`; caption: [none encoded near image]
- 91. `fortson-2010-indo-european-language-and-culture-table14-3.jpg` ← `c14t003.jpg` — Table 14.3; type=table; chunk=Chapter 14; source-xhtml=`9781405188968_014.xhtml`; caption: [none encoded near image]
- 92. `fortson-2010-indo-european-language-and-culture-table14-4.jpg` ← `c14t004.jpg` — Table 14.4; type=table; chunk=Chapter 14; source-xhtml=`9781405188968_014.xhtml`; caption: [none encoded near image]
- 93. `fortson-2010-indo-european-language-and-culture-p335-fig1.jpg` ← `335.jpg` — Page 335 image; type=review-image; chunk=Chapter 14; source-xhtml=`9781405188968_014.xhtml`; caption: [none encoded near image]
- 94. `fortson-2010-indo-european-language-and-culture-table15-1.jpg` ← `c15t001.jpg` — Table 15.1; type=table; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 95. `fortson-2010-indo-european-language-and-culture-table15-2.jpg` ← `c15t002.jpg` — Table 15.2; type=table; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 96. `fortson-2010-indo-european-language-and-culture-table15-3.jpg` ← `c15t003.jpg` — Table 15.3; type=table; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 97. `fortson-2010-indo-european-language-and-culture-table15-4.jpg` ← `c15t004.jpg` — Table 15.4; type=table; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 98. `fortson-2010-indo-european-language-and-culture-table15-5.jpg` ← `c15t005.jpg` — Table 15.5; type=table; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 99. `fortson-2010-indo-european-language-and-culture-table15-6.jpg` ← `c15t006.jpg` — Table 15.6; type=table; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 100. `fortson-2010-indo-european-language-and-culture-table15-7.jpg` ← `c15t007.jpg` — Table 15.7; type=table; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 101. `fortson-2010-indo-european-language-and-culture-fig15-1.jpg` ← `c15f001.jpg` — Figure 15.1; type=figure; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: *Figure 15.1* Reproduction of an eighteenth-century engraving of the Gallehus horn containing the inscription in 15.39. The engraving shows the entire decorated surface of the horn, with the rear surface peeled back. The runes encircle the top of the horn and are read rightwards, beginning with what looks like a boldfaced M (= *e*) following the non-boldfaced word in the middle (*tawido*). Most words are separated from one another by a vertical stack of four or five curved marks. From R. I. Page, *Runes* (London: British Museum Publications, 1987), p. 28. Reproduced by permission of the British Museum.
- 102. `fortson-2010-indo-european-language-and-culture-map15-1.jpg` ← `c15m001.jpg` — Map 15.1; type=map; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: *Map 15.1* The Germanic peoples around <small>AD</small> 500
- 103. `fortson-2010-indo-european-language-and-culture-fig15-2.jpg` ← `c15f002.jpg` — Figure 15.2; type=figure; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: *Figure 15.2* Leaf (50 v.) from the sixth-century Codex Argenteus, the only surviving manuscript containing the Gothic Bible. Mark 8:14 begins at the top and our selection runs through the first three letters of the fifth line from the bottom. Reproduced from the facsimile edition *Codex Argenteus Upsaliensis Jussu Senatus Universitatis Phototypice Editus* (Uppsala: Almqvist & Wiksell, 1927), p. 322.
- 104. `fortson-2010-indo-european-language-and-culture-table15-8.jpg` ← `c15t008.jpg` — Table 15.8; type=table; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 105. `fortson-2010-indo-european-language-and-culture-table15-9.jpg` ← `c15t009.jpg` — Table 15.9; type=table; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 106. `fortson-2010-indo-european-language-and-culture-table15-10.jpg` ← `c15t010.jpg` — Table 15.10; type=table; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 107. `fortson-2010-indo-european-language-and-culture-p366-fig1.jpg` ← `366.jpg` — Page 366 image; type=review-image; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 108. `fortson-2010-indo-european-language-and-culture-p379-fig1.jpg` ← `379.jpg` — Page 379 image; type=review-image; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 109. `fortson-2010-indo-european-language-and-culture-fig15-3.jpg` ← `c15f003.jpg` — Figure 15.3; type=figure; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 110. `fortson-2010-indo-european-language-and-culture-fig15-4.jpg` ← `c15f004.jpg` — Figure 15.4; type=figure; chunk=Chapter 15; source-xhtml=`9781405188968_015.xhtml`; caption: [none encoded near image]
- 111. `fortson-2010-indo-european-language-and-culture-map16-1.jpg` ← `c16m001.jpg` — Map 16.1; type=map; chunk=Chapter 16; source-xhtml=`9781405188968_016.xhtml`; caption: *Map 16.1* Greater Armenia during the early Christian era
- 112. `fortson-2010-indo-european-language-and-culture-table16-1.jpg` ← `c16t001.jpg` — Table 16.1; type=table; chunk=Chapter 16; source-xhtml=`9781405188968_016.xhtml`; caption: [none encoded near image]
- 113. `fortson-2010-indo-european-language-and-culture-table16-2.jpg` ← `c16t002.jpg` — Table 16.2; type=table; chunk=Chapter 16; source-xhtml=`9781405188968_016.xhtml`; caption: [none encoded near image]
- 114. `fortson-2010-indo-european-language-and-culture-table16-3.jpg` ← `c16t003.jpg` — Table 16.3; type=table; chunk=Chapter 16; source-xhtml=`9781405188968_016.xhtml`; caption: [none encoded near image]
- 115. `fortson-2010-indo-european-language-and-culture-map17-1.jpg` ← `c17m001.jpg` — Map 17.1; type=map; chunk=Chapter 17; source-xhtml=`9781405188968_017.xhtml`; caption: *Map 17.1* The Tarim Basin
- 116. `fortson-2010-indo-european-language-and-culture-table17-1.jpg` ← `c17t001.jpg` — Table 17.1; type=table; chunk=Chapter 17; source-xhtml=`9781405188968_017.xhtml`; caption: [none encoded near image]
- 117. `fortson-2010-indo-european-language-and-culture-table17-2.jpg` ← `c17t002.jpg` — Table 17.2; type=table; chunk=Chapter 17; source-xhtml=`9781405188968_017.xhtml`; caption: [none encoded near image]
- 118. `fortson-2010-indo-european-language-and-culture-table18-1.jpg` ← `c18t001.jpg` — Table 18.1; type=table; chunk=Chapter 18; source-xhtml=`9781405188968_018.xhtml`; caption: [none encoded near image]
- 119. `fortson-2010-indo-european-language-and-culture-map18-1.jpg` ← `c18m001.jpg` — Map 18.1; type=map; chunk=Chapter 18; source-xhtml=`9781405188968_018.xhtml`; caption: *Map 18.1* The Slavs and Balts around <small>AD</small> 1000
- 120. `fortson-2010-indo-european-language-and-culture-table18-2.jpg` ← `c18t002.jpg` — Table 18.2; type=table; chunk=Chapter 18; source-xhtml=`9781405188968_018.xhtml`; caption: [none encoded near image]
- 121. `fortson-2010-indo-european-language-and-culture-table18-3.jpg` ← `c18t003.jpg` — Table 18.3; type=table; chunk=Chapter 18; source-xhtml=`9781405188968_018.xhtml`; caption: [none encoded near image]
- 122. `fortson-2010-indo-european-language-and-culture-p443-fig1.jpg` ← `443.jpg` — Page 443 image; type=review-image; chunk=Chapter 18; source-xhtml=`9781405188968_018.xhtml`; caption: [none encoded near image]
- 123. `fortson-2010-indo-european-language-and-culture-table18-4.jpg` ← `c18t004.jpg` — Table 18.4; type=table; chunk=Chapter 18; source-xhtml=`9781405188968_018.xhtml`; caption: [none encoded near image]
- 124. `fortson-2010-indo-european-language-and-culture-table18-5.jpg` ← `c18t005.jpg` — Table 18.5; type=table; chunk=Chapter 18; source-xhtml=`9781405188968_018.xhtml`; caption: [none encoded near image]
- 125. `fortson-2010-indo-european-language-and-culture-map19-1.jpg` ← `c19m001.jpg` — Map 19.1; type=map; chunk=Chapter 19; source-xhtml=`9781405188968_019.xhtml`; caption: *Map 19.1* Geographical distribution of Geg and Tosk
- 126. `fortson-2010-indo-european-language-and-culture-p453-fig1.jpg` ← `453.jpg` — Page 453 image; type=review-image; chunk=Chapter 19; source-xhtml=`9781405188968_019.xhtml`; caption: [none encoded near image]
- 127. `fortson-2010-indo-european-language-and-culture-table19-1.jpg` ← `c19t001.jpg` — Table 19.1; type=table; chunk=Chapter 19; source-xhtml=`9781405188968_019.xhtml`; caption: [none encoded near image]
- 128. `fortson-2010-indo-european-language-and-culture-table19-2.jpg` ← `c19t002.jpg` — Table 19.2; type=table; chunk=Chapter 19; source-xhtml=`9781405188968_019.xhtml`; caption: [none encoded near image]
- 129. `fortson-2010-indo-european-language-and-culture-table19-3.jpg` ← `c19t003.jpg` — Table 19.3; type=table; chunk=Chapter 19; source-xhtml=`9781405188968_019.xhtml`; caption: [none encoded near image]
- 130. `fortson-2010-indo-european-language-and-culture-map20-1.jpg` ← `c20m001.jpg` — Map 20.1; type=map; chunk=Chapter 20; source-xhtml=`9781405188968_020.xhtml`; caption: *Map 20.1* The ancient Mediterranean, showing regions and languages in this chapter
