#!/usr/bin/env python3
"""
sources-index.py — Rebuild sources-index.tsv and sources-lookup.md from source definitions.

Run from the sources/ directory:
    python3 sources-index.py

Outputs:
    sources-index.tsv   — canonical record, 8 cols: work|dir|file|section|pages|title|tags|quality
    sources-lookup.md   — speed lookup organized by tag group for in-session grep use

Tags within TSV cells are pipe-separated (|).
To add a new source: add entries via the helper functions at the bottom of this file,
following the existing pattern, then re-run.
"""

import csv
from collections import defaultdict

rows = []

# ---------------------------------------------------------------------------
# Helper — one per work for brevity
# ---------------------------------------------------------------------------

def entry(work, dir_, file_, section, pages, title, tags, quality):
    rows.append([work, dir_, file_, section, pages, title, "|".join(tags), quality])


# ---------------------------------------------------------------------------
# RINGE 1996 — On the Chronology of Sound Changes in Tocharian
# ---------------------------------------------------------------------------
W = "R1996"
D = "ringe-1996-chronology-sound-changes-tocharian"
Q = "OCR-scanned"

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-front-matter.md",
      "front-matter", "i-xxv",
      "Front matter, abbreviations, preface, introduction",
      ["PIE-phonology","Tocharian","sound-change-chronology","PIE-reconstruction"], Q)

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-ch1.md",
      "Ch1", "1-6",
      "Chapter 1. Proto-Indo-European",
      ["PIE-phonology","PIE-reconstruction","PIE-inflection"], Q)

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-ch2.md",
      "Ch2", "7-38",
      "Chapter 2. The development of laryngeals in Tocharian",
      ["laryngeals","Tocharian","sound-changes","sound-change-chronology"], Q)

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-ch3.md",
      "Ch3", "39-50",
      "Chapter 3. Early changes of stops",
      ["stops","Tocharian","sound-changes","sound-change-chronology"], Q)

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-ch4.md",
      "Ch4", "51-66",
      "Chapter 4. PIE *y and *w, and related matters",
      ["sonorants","stops","Tocharian","sound-changes","sound-change-chronology"], Q)

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-ch5.md",
      "Ch5", "67-88",
      "Chapter 5. Syllabic resonants, consonant clusters, and Auslautgesetze",
      ["syllabic-resonants","sonorants","Tocharian","sound-changes","sound-change-chronology"], Q)

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-ch6.md",
      "Ch6", "89-100",
      "Chapter 6. Early shifts of back vowels",
      ["ablaut","Tocharian","sound-changes","sound-change-chronology"], Q)

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-ch7.md",
      "Ch7", "101-118",
      "Chapter 7. Palatalization",
      ["stops","Tocharian","sound-changes","sound-change-chronology"], Q)

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-ch8.md",
      "Ch8", "119-140",
      "Chapter 8. Restructuring of the vowel system",
      ["ablaut","Tocharian","sound-changes","sound-change-chronology"], Q)

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-ch9.md",
      "Ch9", "141-154",
      "Chapter 9. Further restructuring of the consonant system",
      ["stops","sonorants","fricatives","Tocharian","sound-changes","sound-change-chronology"], Q)

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-ch10.md",
      "Ch10", "155-168",
      "Chapter 10. Late sound changes",
      ["Tocharian","sound-changes","sound-change-chronology"], Q)

entry(W,D, "ringe-1996-chronology-sound-changes-tocharian-index.md",
      "index", "181-203",
      "PIE, PT, TA, and TB indexes",
      ["Tocharian","PIE-reconstruction"], Q)


# ---------------------------------------------------------------------------
# RINGE 2013 — Historical Linguistics: Toward a Twenty-First Century Reintegration
# ---------------------------------------------------------------------------
W = "R2013"
D = "ringe-2013-historical-linguistics"
Q = "born-digital"

entry(W,D, "ringe-2013-historical-linguistics-introduction.md",
      "intro", "1-6",
      "Introduction",
      ["historical-linguistics-theory"], Q)

entry(W,D, "ringe-2013-historical-linguistics-ch1.md",
      "Ch1", "7-27",
      "Chapter 1. The nature of human language and language variation",
      ["historical-linguistics-theory"], Q)

entry(W,D, "ringe-2013-historical-linguistics-ch2.md",
      "Ch2", "28-44",
      "Chapter 2. Language replication and language change",
      ["historical-linguistics-theory","sound-changes","borrowing"], Q)

entry(W,D, "ringe-2013-historical-linguistics-ch3.md",
      "Ch3", "45-58",
      "Chapter 3. Language change in the speech community",
      ["historical-linguistics-theory","dialect-geography","borrowing"], Q)

entry(W,D, "ringe-2013-historical-linguistics-ch4.md",
      "Ch4", "59-77",
      "Chapter 4. Language contact as a source of change",
      ["borrowing","dialect-geography","historical-linguistics-theory"], Q)

entry(W,D, "ringe-2013-historical-linguistics-ch5.md",
      "Ch5", "78-104",
      "Chapter 5. Sound change",
      ["sound-changes","PIE-phonology","historical-linguistics-theory"], Q)

entry(W,D, "ringe-2013-historical-linguistics-ch6.md",
      "Ch6", "105-151",
      "Chapter 6. The evolution of phonological rules",
      ["sound-changes","PIE-phonology","historical-linguistics-theory"], Q)

entry(W,D, "ringe-2013-historical-linguistics-ch7.md",
      "Ch7", "152-166",
      "Chapter 7. Morphology",
      ["noun-inflection","verb-inflection","derivational-morphology"], Q)

entry(W,D, "ringe-2013-historical-linguistics-ch8.md",
      "Ch8", "167-211",
      "Chapter 8. Morphological change",
      ["noun-inflection","verb-inflection","derivational-morphology","historical-linguistics-theory"], Q)

entry(W,D, "ringe-2013-historical-linguistics-ch9.md",
      "Ch9", "212-227",
      "Chapter 9. Syntactic change",
      ["syntax","historical-linguistics-theory"], Q)

entry(W,D, "ringe-2013-historical-linguistics-ch10.md",
      "Ch10", "228-255",
      "Chapter 10. Reconstruction",
      ["comparative-reconstruction","PIE-reconstruction","historical-linguistics-theory"], Q)

entry(W,D, "ringe-2013-historical-linguistics-ch11.md",
      "Ch11", "256-280",
      "Chapter 11. Beyond comparative reconstruction: subgrouping and 'long-distance' relationships",
      ["subgrouping","phylogeny","cladistics","comparative-reconstruction","historical-linguistics-theory"], Q)

entry(W,D, "ringe-2013-historical-linguistics-appendix.md",
      "appendix", "281-290",
      "Appendix. Recovering the pronunciation of dead languages: types of evidence",
      ["historical-linguistics-theory","comparative-reconstruction"], Q)


# ---------------------------------------------------------------------------
# RINGE 2017 — From Proto-Indo-European to Proto-Germanic, 2nd ed.
# ---------------------------------------------------------------------------
W = "R2017"
D = "ringe-2017-pie-to-proto-germanic-2nd"
Q = "born-digital"

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch1.md",
      "Ch1", "1-4",
      "Chapter 1. Introduction",
      ["PIE-reconstruction","Proto-Germanic","historical-linguistics-theory"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-1.md",
      "§2.1", "5-7",
      "§2.1 Introduction [PIE survey]",
      ["PIE-reconstruction"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-2.md",
      "§2.2", "8-24",
      "§2.2 PIE phonology",
      ["PIE-phonology","laryngeals","syllabic-resonants","labiovelars","stops","sonorants","accent","ablaut"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-3-1.md",
      "§2.3.1", "25-28",
      "§2.3.1 PIE inflectional categories",
      ["PIE-inflection","noun-inflection","verb-inflection"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-3-2.md",
      "§2.3.2", "29",
      "§2.3.2 Formal expression of inflectional categories",
      ["PIE-inflection","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-3-3.md",
      "§2.3.3", "30-48",
      "§2.3.3 PIE verb inflection",
      ["PIE-inflection","verb-inflection","thematic-stems","athematic-stems","perfect","aorist",
       "nasal-infix","personal-endings","mood","aspect"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-3-4.md",
      "§2.3.4", "49-62",
      "§2.3.4 PIE noun inflection",
      ["PIE-inflection","noun-inflection","o-stem","s-stem","root-nouns","athematic-nouns","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-3-5.md",
      "§2.3.5", "63-64",
      "§2.3.5 PIE adjective inflection",
      ["PIE-inflection","adjective-inflection","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-3-6.md",
      "§2.3.6", "65-71",
      "§2.3.6 The inflection of other PIE nominals",
      ["PIE-inflection","pronouns","numerals","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-4.md",
      "§2.4", "72-76",
      "§2.4 PIE derivational morphology",
      ["PIE-inflection","derivational-morphology","word-formation"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-5.md",
      "§2.5", "77-82",
      "§2.5 PIE syntax",
      ["PIE-syntax","syntax"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-6.md",
      "§2.6", "83",
      "§2.6 The PIE lexicon",
      ["PIE-lexicon","lexicon"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-1.md",
      "§3.1", "84-85",
      "§3.1 Introduction [PIE to PGmc sound changes]",
      ["Proto-Germanic","sound-changes","historical-linguistics-theory"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-1.md",
      "§3.2.1", "86-99",
      "§3.2.1 The elimination of laryngeals, and related developments of vowels",
      ["laryngeals","ablaut","sound-changes","Proto-Germanic","sound-change-chronology"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-2.md",
      "§3.2.2", "100-105",
      "§3.2.2 Changes affecting sonorants",
      ["sonorants","syllabic-resonants","sound-changes","Proto-Germanic"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-3.md",
      "§3.2.3", "106-112",
      "§3.2.3 Changes affecting obstruents",
      ["stops","fricatives","labiovelars","sound-changes","Proto-Germanic"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-4.md",
      "§3.2.4", "113-140",
      "§3.2.4 Grimm's Law and Verner's Law",
      ["Grimm","Verner","stops","fricatives","sound-changes","Proto-Germanic","accent"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-5.md",
      "§3.2.5", "141-152",
      "§3.2.5 Sievers' Law and unstressed syllables",
      ["Sievers","sonorants","sound-changes","Proto-Germanic","accent"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-6.md",
      "§3.2.6", "153-169",
      "§3.2.6 Loss of *j, *w, and *ə; *uj > *ij; miscellaneous consonant changes",
      ["sonorants","fricatives","sound-changes","Proto-Germanic","ablaut"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-7.md",
      "§3.2.7", "170-174",
      "§3.2.7 Other changes of vowels",
      ["ablaut","sound-changes","Proto-Germanic"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-8.md",
      "§3.2.8", "175-176",
      "§3.2.8 Chronological overview [PIE to PGmc]",
      ["sound-change-chronology","sound-changes","Proto-Germanic"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-3.md",
      "§3.3", "177-195",
      "§3.3 Restructurings of the inflectional morphology",
      ["noun-inflection","verb-inflection","Proto-Germanic","sound-changes"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-4-1.md",
      "§3.4.1", "196",
      "§3.4.1 Changes in inflectional categories",
      ["Proto-Germanic","verb-inflection","noun-inflection"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-4-2.md",
      "§3.4.2", "197-198",
      "§3.4.2 Changes in the formal expression of inflectional categories",
      ["Proto-Germanic","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-4-3.md",
      "§3.4.3", "199-220",
      "§3.4.3 Changes in verb inflection",
      ["Proto-Germanic","verb-inflection","thematic-stems","athematic-stems","perfect","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-4-4.md",
      "§3.4.4", "221-226",
      "§3.4.4 Changes in noun inflection",
      ["Proto-Germanic","noun-inflection","o-stem","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-4-5.md",
      "§3.4.5", "227-235",
      "§3.4.5 Changes in the inflection of other nominals",
      ["Proto-Germanic","pronouns","numerals","adjective-inflection","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-5.md",
      "§3.5", "236-239",
      "§3.5 Changes in syntax",
      ["Proto-Germanic","syntax"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-6.md",
      "§3.6", "240",
      "§3.6 Lexical changes",
      ["Proto-Germanic","lexicon"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-1.md",
      "§4.1", "241",
      "§4.1 Introduction [PGmc survey]",
      ["Proto-Germanic"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-2.md",
      "§4.2", "242-259",
      "§4.2 PGmc phonology",
      ["Proto-Germanic","PIE-phonology","ablaut","labiovelars","stops","sonorants","accent"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-3-1.md",
      "§4.3.1", "260",
      "§4.3.1 Inflectional categories of PGmc",
      ["Proto-Germanic","noun-inflection","verb-inflection"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-3-2.md",
      "§4.3.2", "261",
      "§4.3.2 The formal expression of PGmc inflectional categories",
      ["Proto-Germanic","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-3-3.md",
      "§4.3.3", "262-298",
      "§4.3.3 PGmc verb inflection",
      ["Proto-Germanic","verb-inflection","thematic-stems","athematic-stems","perfect",
       "paradigms","personal-endings"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-3-4.md",
      "§4.3.4", "299-312",
      "§4.3.4 PGmc noun inflection",
      ["Proto-Germanic","noun-inflection","o-stem","s-stem","root-nouns","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-3-5.md",
      "§4.3.5", "313-317",
      "§4.3.5 PGmc adjective inflection",
      ["Proto-Germanic","adjective-inflection","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-3-6.md",
      "§4.3.6", "318-322",
      "§4.3.6 The inflection of other PGmc nominals",
      ["Proto-Germanic","pronouns","numerals","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-4.md",
      "§4.4", "323-327",
      "§4.4 PGmc word formation",
      ["Proto-Germanic","derivational-morphology","word-formation","compounding"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-5.md",
      "§4.5", "328",
      "§4.5 PGmc syntax",
      ["Proto-Germanic","syntax"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-6.md",
      "§4.6", "328-330",
      "§4.6 The PGmc lexicon",
      ["Proto-Germanic","lexicon"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-index.md",
      "index", "348-406",
      "Index (PIE forms, PGmc forms, subjects)",
      ["PIE-reconstruction","Proto-Germanic"], Q)


# ---------------------------------------------------------------------------
# RINGE 2024 — The Linguistic Roots of Ancient Greek
# ---------------------------------------------------------------------------
W = "R2024"
D = "ringe-2024-linguistic-roots-ancient-greek"
Q = "born-digital"

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch1.md",
      "Ch1", "1-3",
      "Chapter 1. Introduction",
      ["Proto-Greek","Greek","historical-linguistics-theory"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-1.md",
      "§2.1", "4-6",
      "§2.1 Introduction [PIE survey]",
      ["PIE-reconstruction"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-2.md",
      "§2.2", "7-23",
      "§2.2 PIE phonology",
      ["PIE-phonology","laryngeals","syllabic-resonants","labiovelars","stops","sonorants","accent","ablaut"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-3-intro.md",
      "§2.3", "24",
      "§2.3 PIE inflectional morphology [intro]",
      ["PIE-inflection"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-3-1.md",
      "§2.3.1", "24-27",
      "§2.3.1 PIE inflectional categories",
      ["PIE-inflection","noun-inflection","verb-inflection"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-3-2.md",
      "§2.3.2", "28-29",
      "§2.3.2 Formal expression of inflectional categories",
      ["PIE-inflection","paradigms"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-3-3.md",
      "§2.3.3", "30-50",
      "§2.3.3 PIE verb inflection",
      ["PIE-inflection","verb-inflection","thematic-stems","athematic-stems","perfect","aorist",
       "nasal-infix","personal-endings","mood","aspect"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-3-4.md",
      "§2.3.4", "51-65",
      "§2.3.4 PIE noun inflection",
      ["PIE-inflection","noun-inflection","o-stem","s-stem","root-nouns","athematic-nouns","paradigms"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-3-5.md",
      "§2.3.5", "66-68",
      "§2.3.5 PIE adjective inflection",
      ["PIE-inflection","adjective-inflection","paradigms"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-3-6.md",
      "§2.3.6", "69-75",
      "§2.3.6 The inflection of other PIE nominals",
      ["PIE-inflection","pronouns","numerals","paradigms"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-4.md",
      "§2.4", "76-80",
      "§2.4 PIE derivational morphology",
      ["PIE-inflection","derivational-morphology","word-formation"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-5.md",
      "§2.5", "81-86",
      "§2.5 PIE syntax",
      ["PIE-syntax","syntax"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch2-sec2-6.md",
      "§2.6", "87",
      "§2.6 The PIE lexicon",
      ["PIE-lexicon","lexicon"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch3-sec3-1.md",
      "§3.1", "88",
      "§3.1 Introduction [Greek sound changes]",
      ["Proto-Greek","sound-changes"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch3-sec3-2.md",
      "§3.2", "88-111",
      "§3.2 The elimination of laryngeals",
      ["laryngeals","Proto-Greek","sound-changes","ablaut","sound-change-chronology"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch3-sec3-3.md",
      "§3.3", "112-115",
      "§3.3 Early developments of nasals",
      ["sonorants","syllabic-resonants","Proto-Greek","sound-changes"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch3-sec3-4.md",
      "§3.4", "116-130",
      "§3.4 Early developments of obstruents",
      ["stops","fricatives","labiovelars","Proto-Greek","sound-changes"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch3-sec3-5.md",
      "§3.5", "131-152",
      "§3.5 The origin and development of Proto-Greek *h",
      ["Proto-Greek","sound-changes","fricatives","laryngeals"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch3-sec3-6.md",
      "§3.6", "153-166",
      "§3.6 The development of PIE *y",
      ["sonorants","Proto-Greek","sound-changes"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch3-sec3-7.md",
      "§3.7", "167-168",
      "§3.7 Other clusters of dental stops",
      ["stops","thorn-clusters","Proto-Greek","sound-changes"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch3-sec3-8.md",
      "§3.8", "169",
      "§3.8 Accent in Proto-Greek",
      ["accent","Proto-Greek","sound-changes"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch3-sec3-9.md",
      "§3.9", "170-172",
      "§3.9 Relative chronology of sound changes",
      ["sound-change-chronology","Proto-Greek"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch4-sec4-1.md",
      "§4.1", "173",
      "§4.1 Introduction [Greek inflection]",
      ["Proto-Greek","noun-inflection","verb-inflection"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch4-sec4-2-intro.md",
      "§4.2", "173",
      "§4.2 Changes in verb inflection [intro]",
      ["Proto-Greek","verb-inflection"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch4-sec4-2-1.md",
      "§4.2.1", "174-200",
      "§4.2.1 The development of present stems",
      ["Proto-Greek","verb-inflection","present-stems","thematic-stems","athematic-stems","nasal-infix"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch4-sec4-2-2.md",
      "§4.2.2", "201-215",
      "§4.2.2 The development of aorist stems",
      ["Proto-Greek","verb-inflection","aorist"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch4-sec4-2-3.md",
      "§4.2.3", "216-222",
      "§4.2.3 Perfect stems",
      ["Proto-Greek","verb-inflection","perfect"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch4-sec4-2-4.md",
      "§4.2.4", "223-224",
      "§4.2.4 Future stems",
      ["Proto-Greek","verb-inflection"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch4-sec4-2-5.md",
      "§4.2.5", "225-226",
      "§4.2.5 Mood suffixes and the augment",
      ["Proto-Greek","verb-inflection","mood"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch4-sec4-2-6.md",
      "§4.2.6", "227-231",
      "§4.2.6 Personal endings",
      ["Proto-Greek","verb-inflection","personal-endings"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch4-sec4-2-7.md",
      "§4.2.7", "232",
      "§4.2.7 Participles and infinitives",
      ["Proto-Greek","verb-inflection"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch4-sec4-2-8.md",
      "§4.2.8", "232",
      "§4.2.8 The accent of Greek verb forms",
      ["Proto-Greek","verb-inflection","accent"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch4-sec4-3.md",
      "§4.3", "233-261",
      "§4.3 Changes in nominal inflection",
      ["Proto-Greek","noun-inflection","paradigms","o-stem","s-stem","root-nouns"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch5.md",
      "Ch5", "262-299",
      "Chapter 5. The initial diversification of Greek dialects",
      ["Greek","dialect-geography","subgrouping","sound-changes","phonology"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch6.md",
      "Ch6", "300-311",
      "Chapter 6. The Attic-Ionic dialects",
      ["Greek","dialect-geography","sound-changes"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch7.md",
      "Ch7", "312-327",
      "Chapter 7. Widely shared later innovations",
      ["Greek","sound-changes","dialect-geography"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch8.md",
      "Ch8", "328-335",
      "Chapter 8. Syntax",
      ["Greek","syntax"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-ch9.md",
      "Ch9", "336-342",
      "Chapter 9. Lexicon",
      ["Greek","lexicon","Proto-Greek"], Q)

entry(W,D, "ringe-2024-linguistic-roots-ancient-greek-index.md",
      "index", "361-405",
      "Index (Greek forms, PIE forms, subjects)",
      ["PIE-reconstruction","Proto-Greek","Greek"], Q)


# ---------------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------------

import os
out_dir = os.path.dirname(os.path.abspath(__file__))

# TSV
tsv_path = os.path.join(out_dir, "sources-index.tsv")
header = ["work","dir","file","section","pages","title","tags","quality"]
with open(tsv_path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(header)
    w.writerows(rows)

# Lookup markdown
tag_map = defaultdict(list)
for row in rows:
    r = dict(zip(header, row))
    for tag in r["tags"].split("|"):
        tag_map[tag].append(r)

tag_groups = [
    ("PIE Phonology & Reconstruction", [
        "phonology", "PIE-phonology", "PIE-reconstruction", "laryngeals", "syllabic-resonants",
        "labiovelars", "stops", "sonorants", "fricatives", "accent", "ablaut", "thorn-clusters",
    ]),
    ("PIE Morphology", [
        "PIE-inflection", "PIE-syntax", "PIE-lexicon",
        "noun-inflection", "verb-inflection", "adjective-inflection",
        "thematic-stems", "athematic-stems", "present-stems",
        "perfect", "aorist", "nasal-infix", "mood", "aspect", "personal-endings",
        "o-stem", "s-stem", "root-nouns", "athematic-nouns",
        "pronouns", "numerals", "paradigms",
        "derivational-morphology", "word-formation", "compounding",
    ]),
    ("Sound Changes & Chronology", [
        "sound-changes", "sound-change-chronology", "Grimm", "Verner", "Sievers",
    ]),
    ("Languages & Branches", [
        "Proto-Germanic", "Proto-Greek", "Tocharian",
        "Germanic", "Greek", "Italic", "Celtic", "Balto-Slavic",
    ]),
    ("Comparative & Theoretical", [
        "comparative-reconstruction", "subgrouping", "phylogeny", "cladistics",
        "dialect-geography", "borrowing", "historical-linguistics-theory",
        "syntax", "lexicon",
    ]),
]

lines = [
    "---",
    'title: "Sources — Speed Lookup"',
    'description: "Tag → file index for fast in-session navigation. Grep for a tag heading to get relevant files."',
    'last_updated: "2026-05-31"',
    "---",
    "",
    "# Sources Speed Lookup",
    "",
    "**Usage:** `awk '/^## tag-name$/{p=1} p && /^## / && !/^## tag-name$/{p=0} p' sources-lookup.md`",
    "",
    "**Path prefix:** `sources/{dir}/{file}`",
    "",
    "**Works:** R1996 = Ringe 1996 (Tocharian, OCR); R2013 = Ringe & Eska 2013 (Hist. Ling.); "
    "R2017 = Ringe 2017 (PIE→PGmc, primary); R2024 = Ringe 2024 (Ling. Roots of Greek)",
    "",
]

seen_tags = set()
for group_name, tags in tag_groups:
    lines += ["---", f"### {group_name}", ""]
    for tag in tags:
        seen_tags.add(tag)
        entries = tag_map.get(tag, [])
        if not entries:
            continue
        lines.append(f"## {tag}")
        for e in entries:
            q = " ⚠OCR" if e["quality"] == "OCR-scanned" else ""
            lines.append(f"- **{e['work']}** {e['section']} pp.{e['pages']}{q} — {e['title']}")
            lines.append(f"  `{e['dir']}/{e['file']}`")
        lines.append("")

leftover = set(tag_map.keys()) - seen_tags
if leftover:
    lines += ["---", "### Other", ""]
    for tag in sorted(leftover):
        lines.append(f"## {tag}")
        for e in tag_map[tag]:
            lines.append(f"- **{e['work']}** {e['section']} pp.{e['pages']} — {e['title']}")
            lines.append(f"  `{e['dir']}/{e['file']}`")
        lines.append("")

md_path = os.path.join(out_dir, "sources-lookup.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Written: {tsv_path} ({len(rows)} rows)")
print(f"Written: {md_path}")
print(f"Leftover tags: {sorted(leftover)}")
