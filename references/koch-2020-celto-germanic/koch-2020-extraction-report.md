# koch-2020 extraction report

## Source type

Born-digital PDF with a machine-readable text layer. The raw extracted text layer was used as the primary input. Rendered page images were used for the extracted figure image files and as a fallback basis for figure handling.

## Corrections applied

- Ligature repairs: approximately 0.
- Non-semantic PDF/control artifacts removed where detected: BOM/noncharacter/control-form artifacts.
- Superscript/labialized glide repair from PDF span geometry: approximately 428 small `w` spans converted to `ʷ`.
- Aspirated/superscript h repair from PDF span geometry: approximately 4 small `h` spans converted to `ʰ`.
- Laryngeal-like lowered digits after H/h converted to subscript digits: approximately 286.
- Superscript note markers converted to Markdown-style note markers: approximately 164.
- Running footers removed: approximately 174; bracketed page-number ornaments removed: approximately 10.
- Unicode normalization: output Markdown was normalized to NFC after character-level repairs.
- Figure images were extracted as page-level PNG renders rather than precise cropped figure-only images because the PDF mixes raster images, vector charts, and composite figure layouts.

## Unresolved-issues list

- No `[unclear]` markers were inserted in this pass. This does not certify that all characters are correct.
- Figure 36 caption included a PDF text-layer artifact reading `Figure 36. Figure 29.`; this was repaired to `Figure 36.` in the Markdown. Verify against the page image if the caption is used critically.
- The extraction preserves most source lineation inside dense lexical lists, bibliography entries, and the index to avoid dropping diacritics or technical notation. A later prose-reflow pass could make running prose smoother but may increase risk to forms.
- The index and bibliography should be considered first-pass character-faithful extractions, not manually proofread editions.

## Confusion-pair report

- `h₁ h₂ h₃` / `H₁ H₂ H₃` vs ASCII digits: lowered laryngeal-like digits after H/h were converted where PDF span geometry exposed them. Remaining ASCII `H1/H2/H3` or `h1/h2/h3`, if any, are listed in the unresolved pattern checks above.
- Macron vowels: output Markdown was normalized to NFC, so ordinary macron vowels are precomposed where Unicode supports composition. Remaining combining marks are mainly non-precomposable scholarly notation or stacked diacritics.
- `ʰ` and `ʷ`: small superscript/glide spans were converted where identifiable from PDF geometry. Some authorial plain `w` in forms such as `kw`/`gw` may remain if the PDF text layer did not expose them as separate raised spans.
- `ə`: counted only where present in the text layer; absence in a passage was not visually verified globally.
- Underdot characters (`ṛ ḷ ṃ ṇ`) and acute consonants (`ǵ ḱ`): retained where present; not every dense form was visually checked.
- Asterisks before reconstructed forms were preserved from the text layer; no global visual proofing was performed.
- Daggers were counted where present; no global visual proofing was performed.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 52,
    "h2": 75,
    "h3": 16
  },
  "macron_a": 741,
  "macron_e": 365,
  "macron_i": 394,
  "macron_o": 383,
  "macron_u": 193,
  "schwa": 15,
  "greek_chars": 1129,
  "combining_diacritics": 339,
  "dagger": 3,
  "modifier_superscript_w": 222,
  "modifier_superscript_h": 2
}
```

## Structural integrity check

- Chunking follows the source section labels: front matter; §§1–26; grouped §§27–34; §§35–51; bibliography; index.
- Page anchors are included as HTML comments at page transitions.
- Bibliography and index are separated from the main text.
- Footnote text remains in page order and is not fully normalized into endnote syntax. Superscript markers in running text were converted to Markdown-style note markers where identifiable.
- Tables, charts, and figure-heavy pages are represented by page-level figure PNGs plus the text-layer captions.
- No claim is made that page-boundary continuation text is fully reflowed or that all paragraph breaks are normalized.

## Image inventory

Extracted images are page-level PNG renders unless otherwise noted.

| File | Source label | Page | Caption |
|---|---:|---:|---|
| `images/koch-2020-cover.png` | Cover image | 1 | Cover image |
| `images/koch-2020-fig1.png` | Figure 1 | 11 | Figure 1. Bronze Herzsprung type shield from Fröslunda, Sweden, made with copper traced to to Ossa Morena region of South-west Spain (source SHFA). |
| `images/koch-2020-fig2.png` | Figure 2 | 16 | Figure 2. Proto-Indo-European lexemes attested in each branch (after Mallory 2019). |
| `images/koch-2020-fig3.png` | Figure 3 | 19 | Figure 3. Celtic and Germanic linguistic territories and contact zone in the Iron Age ~500 BC–1 BC/AD according to Schumacher 2007. |
| `images/koch-2020-fig4.png` | Figure 4 | 24 | Figure 4. First-order subgroups of Indo-European: simplified adaptation of the Indo-European family tree of Ringe, Warnow, and Taylor (2002), indicating the close association of Italic and Celtic and the anomalous position of Germanic. |
| `images/koch-2020-fig5.png` | Figure 5 | 29 | Figure 5. Anatolian, Post-Anatolian Indo-European, and some cultures and migrations up to ~2500 BC. |
| `images/koch-2020-fig6.png` | Figure 6 | 31 | Figure 6. The Indo-European family tree published by August Schleicher in 1861 anticipated groupings universally accepted (Balto-Slavic and Indo-Iranian) or widely accepted (Italo-Celtic) today. At the time, Anatolian and Tocharian were not yet discovered. |
| `images/koch-2020-fig7.png` | Figure 7 | 32 | Figure 7. Bad trees? If we recognize no common ancestral languages between Proto-Indo-European and the 10 primary branches, that implies either the impossible situation of the proto-language undergoing a ten-way split or a series in which each branch split off as a unique new language from a resi... |
| `images/koch-2020-fig8.png` | Figure 8 | 50 | Figure 8. Table summarizing approximate date ranges for reconstructed Indo-European languages in Western Europe: Pre- Germanic and Proto-Germanic, Pre- and Proto-Italo-Celtic, Pre- and Proto-Celtic, Pre- and Proto-Italic. |
| `images/koch-2020-fig9.png` | Figure 9 | 51 | Figure 9. Migrations, cultures, and proto-languages after ~2500 BC. |
| `images/koch-2020-fig10.png` | Figure 10 | 54 | Figure 10. First-order subgroupings of Indo-European (Figure 4), showing the overlying positions of the Post-Proto-Indo-European commonalities: North-west Indo-European (NW), Italo-Celtic/Germanic (ICG), and Celto-Germanic (CG). |
| `images/koch-2020-fig11.png` | Figure 11 | 65 | Figure 11. Totals of a. CG, b. ICG, c. CGBS, d. ANW, and e. CG+ words in the Corpus. |
| `images/koch-2020-fig12-13.png` | Figures 12–13 | 71 | Figures 12–13. Comparison of total numbers of vocabulary, words with meanings relatable to Bronze Age rock art iconography, and those relatable to further aspects of to Bronze Age life amongst a. Celto-Germanic items in the Corpus, b. Italo-Celtic/Germanic, c. Italo-Celtic/Balto- Slavic, d. items... |
| `images/koch-2020-fig14.png` | Figure 14 | 75 | Figure 14. Comparison of numbers of CG words occurring in fully attested pre-modern Germanic and Celtic languages. |
| `images/koch-2020-fig15.png` | Figure 15 | 78 | Figure 15. Post-Tocharian Indo-European in the North and West: dialect chains and separating languages. |
| `images/koch-2020-fig16.png` | Figure 16 | 81 | Figure 16. Summary: Prehistoric cultural complexes as probable vectors for the steppe genetic component and, by implication, early Indo European languages. Because human remains associated with the Pitted Ware Culture lack the steppe component (Malmström et al. 2009), PWC was potentially signific... |
| `images/koch-2020-fig18.png` | Figure 18 | 83 | Figure 18. CG *pluk- ‘BOATLOAD’, *rō- ‘TO ROW OR PADDLE’: rubbing of rock art image of a sea-going vessel and crew with paddles, Tanum, Bohuslän, Sweden (source: SHFA). |
| `images/koch-2020-fig17.png` | Figure 17 | 83 | Figure 17. CG *pluk- ‘BOATLOAD’, *rō- ‘TO ROW’, *bheyatli- ‘AXE’: Rock art panel from Skee parish, Bohuslän, Sweden: iconography includes sea-going vessel and crew with paddles and an upper scene confronting warriors with raised axes. (discovered in 1992 by Sven-Gunnar Broström and Kenneth Ihres... |
| `images/koch-2020-fig20.png` | Figure 20 | 86 | Figure 20. (above) ICG *mazdlo- ‘MAST’, CG *pluk- ‘BOATLOAD’, CG *sighlo- ‘SAIL’: Bronze Age rock carving depicting a sea-going vessel with a mast, rigging, and crew: Järrested, Skåne, Sweden. |
| `images/koch-2020-fig19.png` | Figure 19 | 86 | Figure 19. (left) ICG *mazdlo- ‘MAST’, CG *pluk- ‘BOATLOAD’, CG *sighlo- ‘SAIL’: Bronze Age rock carving depicting a sea-going vessel with a mast, rigging, and crew: Auga dos Cebros, Galicia, Spain (photo: Xabier Garrido). |
| `images/koch-2020-fig21.png` | Figure 21 | 87 | Figure 21. ICG *peisk-, *pisko- ‘FISH’. Rock carving probably representing a large fish: lower left-hand side of the chariot panel, massive Bronze Age tomb at Kivik, Skåne, Sweden ~1400 BC (photo: Jane Aaron). |
| `images/koch-2020-fig22-23.png` | Figures 22–23 | 89 | Figures 22–23. CG *bhodwo- ‘BATTLE, FIGHTING, VIOLENCE’, *katu- ‘BATTLE, FIGHTING, VIOLENCE’, *weik- ‘BATTLE, FIGHTING, VIOLENCE’,*nīt- ‘BATTLE, FIGHTING, VIOLENCE’,*nant- ‘BATTLE, FIGHTING, VIOLENCE’, *bhēgh-, *bhōgh- ‘BATTLE, FIGHTING, VIOLENCE’, *bhrest- ‘BATTLE, FIGHTING, VIOLENCE’: Late B... |
| `images/koch-2020-fig24.png` | Figure 24 | 89 | Figure 24. (bottom) CG *bhei(a)tlo- ~ *bhei(a)l- ‘AXE’, *treg- ‘STRENGTH’, *bhodwo- ‘BATTLE, FIGHTING, VIOLENCE’, *katu- ‘BATTLE, FIGHTING, VIOLENCE’, *weik- ‘BATTLE, FIGHTING, VIOLENCE’,*nīt- ‘BATTLE, FIGHTING, VIOLENCE’,*nant- ‘BATTLE, FIGHTING, VIOLENCE’, *bhēgh-, *bhōgh- ‘BATTLE, FIGHTING,... |
| `images/koch-2020-fig25.png` | Figure 25 | 90 | Figure 25. CG *bhei(a)tlo- ~ *bhei(a)l- ‘AXE’, √treg- ‘STRENGTH’, *bhodwo- ‘BATTLE, FIGHTING, VIOLENCE’, *katu- ‘BATTLE, FIGHTING, VIOLENCE’, *weik- ‘BATTLE, FIGHTING, VIOLENCE’,*nīt- ‘BATTLE, FIGHTING, VIOLENCE’,*nant- ‘BATTLE, FIGHTING, VIOLENCE’, *bhēgh-, *bhōgh- ‘BATTLE, FIGHTING, VIOLENCE... |
| `images/koch-2020-fig26.png` | Figure 26 | 92 | Figure 26. CG *ghaiso- ‘SPEAR’, *lust- ‘SPEAR’, *dhelgo-, *dholgo- ‘DRESS PIN, BROOCH’, *gʷistis ‘DIGIT, FINGER’, ICG *arkʷo- ‘BOW AND ARROW’, NW *skeltu- ~ *skeito- ~ *skoito- ‘SHIELD’. Late Bronze Age stela from La Pimienta, Badajoz, Spain, showing two warriors with swords, a bow and arrow, a l... |
| `images/koch-2020-fig27.png` | Figure 27 | 93 | Figure 27. CG *ghaiso- ‘SPEAR’, *lust- ‘SPEAR’, possibly *dhelgo-, *dholgo- ‘DRESS PIN, BROOCH’, *aksilā ‘AXLE’, *marko- ‘HORSE’, *kankistos, *kanksikā ‘HORSE’, *weghnos ‘WHEELED VEHICLE’, NW *skeltu- ~ *skeito- ~ *skoito- ‘SHIELD’: Late Bronze Age stela showing warrior with lyre, mirror, v-not... |
| `images/koch-2020-fig28-29.png` | Figures 28 & 29 | 100 | Figures 28 & 29. ICG *arkʷo- ‘BOW AND ARROW’. Late Bronze Age rock art depicting bows and arrows: left – Fossum, Bohuslän, Sweden (source: SHFA); right – Montemolín, Sevilla, Spain (after Harrison 2004, C79). |
| `images/koch-2020-fig30.png` | Figure 30 | 100 | Figure 30. ICG *arkʷo- ‘BOW AND ARROW’. The bow-shaped hill viewed from the ruined Roman town of Arcobriga (Monreal de Ariza, Zaragoza, Spain; source: http://aeternitas- numismatics.blogspot.co.uk/2012/03/la-ciudad-celtibera-de-arcobriga.html) with the bow and arrow of the Montemolín stela (Figur... |
| `images/koch-2020-fig31.png` | Figure 31 | 100 | Figure 31. All bows and arrows as represented on Iberian Late Bronze Age ‘warrior stelae’ (after Harrison 2004, Figure 7.15). |
| `images/koch-2020-fig32.png` | Figure 32 | 102 | Figure 32. Drawing of Late Bronze Age stela from Santa Ane de Trujillo, Cáceres, Spain, showing a crested bronze helmet, spear, v-notched herzprung shield viewed from the back showing the hand grip, leaf-shaped sword, and brooch or mirror (after Harrison 2004, no. C17) . |
| `images/koch-2020-fig33.png` | Figure 33 | 104 | Figure 33. Proto-Celtic *skeito-, Proto- Italic *skoito-, Pre-Germanic *skeltu- ‘SHIELD’: Detail of Late Bronze Age rock art panel from Hede, Kville parish, Bohuslän, Sweden, showing a warrior holding at his left a round shield with a pattern of concentric circles (one of seven such shields survi... |
| `images/koch-2020-fig34.png` | Figure 34 | 104 | Figure 34. Scan of Late Bronze Age stela from Brozas, Cáceres, Spain, with large cetral carved image of v-notched Herzsprung shield, viewed from the back showing the hand grip, spear, sword, mirror, comb, and brooch (image: B. Schulz Paulsson) |
| `images/koch-2020-fig35.png` | Figure 35 | 105 | Figure 35. CG *aksilā ‘AXLE’, *markos ‘HORSE’, *kankistos, *kanksikā ‘HORSE’, *weghnos ‘WHEELED VEHICLE’, *ghaiso- ‘SPEAR’, *lust- ‘SPEAR’, *dhelgo-, *dholgo- ‘DRESS PIN, BROOCH’, ICG *arkʷo- ‘BOW AND ARROW’, NW *skeltu-, *skeito-, *skoito- ‘SHIELD’, ICG *rotos, *rotā ‘WHEEL’: Late Bronze Age ... |
| `images/koch-2020-fig37.png` | Figure 37 | 106 | Figure 37. CG *aksilā ‘AXLE’, *marko- ‘HORSE’, *kankistos ~ *kanksikā ‘HORSE’, *weghnos ‘WHEELED VEHICLE’, NW *rotos ~ *rotā ‘WHEEL’: rubbing of rock art image of a chariot and two-horse team from Frännarp, Skåne, Sweden, showing recurrent conventional representation of the horse, chariot fram... |
| `images/koch-2020-fig36.png` | Figure 36 | 106 | Figure 36. Figure 29. *aksilā ‘AXLE’, CG *marko- ‘HORSE’, *kankistos ~ *kanksikā ‘HORSE’, *weghnos ‘WHEELED VEHICLE’, NW *rotos ~ *rotā ‘WHEEL’. Fragmentary Late Bronze Age stela depicting chariot with two- horse team, from El Tejadillo, Capilla, Badajoz, Spain; Museo Arqueológico Provincial d... |
| `images/koch-2020-fig38.png` | Figure 38 | 106 | Figure 38. CG *marko- ‘HORSE’, *kankistos, *kanksikā ‘HORSE’, *weghnos ‘WHEELED VEHICLE’, ICG *rotos, *rotā ‘WHEEL’. Chariot panel, massive Bronze Age tomb at Kivik, Skåne, Sweden, ~1400 BC (photo: Jane Aaron). |
| `images/koch-2020-fig39.png` | Figure 39 | 107 | Figure 39. CG *aksilā ‘AXLE’, *marko- ‘HORSE’, *kankistos ~ *kanksikā ‘HORSE’, *weghnos ‘WHEELED VEHICLE’, ICG *rotos ~ *rotā ‘WHEEL’: Late Bronze Age stela from Majada Honda, Badajoz, Spain, showing warriors, one with a horned helmet, chariot with two-horse team, warrior, and a subsequently a... |
| `images/koch-2020-fig40.png` | Figure 40 | 110 | Figure 40. The Isle of Thanet, Richbough, and Cliffs End Farm. |
| `images/koch-2020-fig41.png` | Figure 41 | 115 | Figure 41. The Hispano-Celtic personal names Ambatus and Ambata. |
| `images/koch-2020-fig42.png` | Figure 42 | 121 | Figure 42. The Palaeohispanic personal names in Tonc- and Tong-. |
| `images/koch-2020-fig43.png` | Figure 43 | 128 | Figure 43. The zones of Palaeohispanic place-names with Celtic -briga and non-Indo-European il(t)i and groups called ‘Celts’. |
| `images/koch-2020-fig44.png` | Figure 44 | 143 | Figure 44. CG *weghnos ‘WHEELED VEHICLE’, *ton(a)ros ~ *tn̥ros ‘THUNDER, THUNDER GOD’ 1. This rock carving, in which a large bihorned figure standing on a chariot pulled by a small horned quadruped to the apparent wonder of man standing aboard a vessel below (from the famous Vitlycke panel, Tanum... |
| `images/koch-2020-fig46.png` | Figure 46 | 146 | Figure 46. CG *gʷistis ‘DIGIT, FINGER’, ICG *arkʷo- ‘BOW AND ARROW’. Late Bronze Age stela from Las Yuntas, Capilla, Badajoz, Spain, showing a warrior with a bow and arrow, and clear representation of 10 splayed fingers (photo: J. Koch). |
| `images/koch-2020-fig45.png` | Figure 45 | 146 | Figure 45. CG *gʷistis ‘DIGIT, FINGER’. Bronze Age rock art on a panel from Backa- Brastad, Bohuslän, Sweden, showing a warrior figure with raised arms and 10 splayed fingers (photo: J. Koch). |
| `images/koch-2020-fig47.png` | Figure 47 | 150 | Figure 47. ICG *natr- ~ *nētr- ‘ADDER, SNAKE, VIPER’, CGBS *slenk- ‘MOVE LIKE A SNAKE, SLINK’: Bronze Age rock carving depicting an adder slinking: Järrested, Skåne, Sweden. (photo: J. Aaron). |
