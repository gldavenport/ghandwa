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
      ["PIE-reconstruction","subgrouping","phylogeny"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-2.md",
      "§2.2", "8-24",
      "§2.2 PIE phonology",
      ["PIE-phonology","laryngeals","syllabic-resonants","labiovelars","stops","sonorants","accent","ablaut",
       "law-Sievers","law-Lindeman","law-Szemerenyi","law-Stang","law-Bartholomae","law-Pinault",
       "thorn-clusters","Auslautgesetze"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-3-1.md",
      "§2.3.1", "25-28",
      "§2.3.1 PIE inflectional categories",
      ["PIE-inflection","noun-inflection","verb-inflection","aspect"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-3-2.md",
      "§2.3.2", "29",
      "§2.3.2 Formal expression of inflectional categories",
      ["PIE-inflection","paradigms","verb-inflection"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-3-3.md",
      "§2.3.3", "30-48",
      "§2.3.3 PIE verb inflection",
      ["PIE-inflection","verb-inflection","thematic-stems","athematic-stems","perfect","aorist",
       "nasal-infix","personal-endings","mood","aspect","paradigms","law-Stang","law-Szemerenyi"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch2-sec2-3-4.md",
      "§2.3.4", "49-62",
      "§2.3.4 PIE noun inflection",
      ["PIE-inflection","noun-inflection","o-stem","s-stem","root-nouns","athematic-nouns","paradigms",
       "law-Szemerenyi","law-Stang","accent"], Q)

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
      ["PIE-inflection","derivational-morphology","word-formation","compounding","Caland"], Q)

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
      ["Proto-Germanic","sound-changes","historical-linguistics-theory","dialect-geography"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-1.md",
      "§3.2.1", "86-99",
      "§3.2.1 The elimination of laryngeals, and related developments of vowels",
      ["laryngeals","ablaut","sound-changes","Proto-Germanic","sound-change-chronology","law-Cowgill","law-Osthoff"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-2.md",
      "§3.2.2", "100-105",
      "§3.2.2 Changes affecting sonorants",
      ["sonorants","syllabic-resonants","sound-changes","Proto-Germanic","Auslautgesetze"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-3.md",
      "§3.2.3", "106-112",
      "§3.2.3 Changes affecting obstruents",
      ["stops","fricatives","labiovelars","sound-changes","Proto-Germanic"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-4.md",
      "§3.2.4", "113-140",
      "§3.2.4 Grimm's Law and Verner's Law",
      ["law-Grimm","law-Verner","law-Kluge","stops","fricatives","sound-changes","Proto-Germanic","accent"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-5.md",
      "§3.2.5", "141-152",
      "§3.2.5 Sievers' Law and unstressed syllables",
      ["law-Sievers","law-Lindeman","sonorants","sound-changes","Proto-Germanic","accent"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-2-6.md",
      "§3.2.6", "153-169",
      "§3.2.6 Loss of *j, *w, and *ə; *uj > *ij; miscellaneous consonant changes",
      ["sonorants","fricatives","sound-changes","Proto-Germanic","ablaut","Auslautgesetze"], Q)

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
      ["noun-inflection","verb-inflection","Proto-Germanic","sound-changes","paradigms","adjective-inflection","aspect"], Q)

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
      ["Proto-Germanic","verb-inflection","thematic-stems","athematic-stems","perfect","paradigms","nasal-infix","mood"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch3-sec3-4-4.md",
      "§3.4.4", "221-226",
      "§3.4.4 Changes in noun inflection",
      ["Proto-Germanic","noun-inflection","o-stem","paradigms","n-stem"], Q)

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
      ["Proto-Germanic","subgrouping"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-2.md",
      "§4.2", "242-259",
      "§4.2 PGmc phonology",
      ["Proto-Germanic","PIE-phonology","ablaut","labiovelars","stops","sonorants","accent","law-Sievers","fricatives"], Q)

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
       "paradigms","personal-endings","nasal-infix","mood"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-3-4.md",
      "§4.3.4", "299-312",
      "§4.3.4 PGmc noun inflection",
      ["Proto-Germanic","noun-inflection","o-stem","s-stem","root-nouns","paradigms","n-stem"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-3-5.md",
      "§4.3.5", "313-317",
      "§4.3.5 PGmc adjective inflection",
      ["Proto-Germanic","adjective-inflection","paradigms","n-stem"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-3-6.md",
      "§4.3.6", "318-322",
      "§4.3.6 The inflection of other PGmc nominals",
      ["Proto-Germanic","pronouns","numerals","paradigms"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-4.md",
      "§4.4", "323-327",
      "§4.4 PGmc word formation",
      ["Proto-Germanic","derivational-morphology","word-formation","compounding","n-stem"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-5.md",
      "§4.5", "328",
      "§4.5 PGmc syntax",
      ["Proto-Germanic","syntax"], Q)

entry(W,D, "ringe-2017-pie-to-proto-germanic-2nd-ch4-sec4-6.md",
      "§4.6", "328-330",
      "§4.6 The PGmc lexicon",
      ["Proto-Germanic","lexicon","borrowing"], Q)

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
# DEUFFIC 2021 — The relative chronology of sound changes from PIE to Proto-Celtic
# (Leiden University MA thesis)
# ---------------------------------------------------------------------------
W = "Deuf21"
D = "deuffic-2021-relative-chronology-sound-change"
Q = "born-digital"

entry(W,D, "deuffic-2021-relative-chronology-sound-changes.md",
      "full text", "n/a",
      "The relative chronology of sound changes from PIE to Proto-Celtic "
      "(laryngeals; stops incl. *gw>*b, *Dh>D aspirate loss; fricative *s; "
      "resonants incl. *R>aR; vowels; relative-chronology synthesis)",
      ["laryngeals","stops","fricatives","sonorants","syllabic-resonants","ablaut",
       "sound-changes","sound-change-chronology","comparative-reconstruction","Celtic"], Q)


# ---------------------------------------------------------------------------
# FULK 2018 — A Comparative Grammar of the Early Germanic Languages
# (directory/files renamed from uploaded-PDF date "2008" to actual pub date 2018)
# ---------------------------------------------------------------------------
W = "Fulk18"
D = "fulk-2018-comparative-grammar-early-germanic"
Q = "born-digital-glyph-corrupted"

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-front-matter.md",
      "front-matter", "1-17",
      "Front matter",
      ["Germanic","historical-linguistics-theory"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch1-introduction.md",
      "Ch1", "18-49",
      "Chapter 1. Introduction",
      ["Germanic","historical-linguistics-theory"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch2-prosodic-features-syllable.md",
      "Ch2", "52-59",
      "Chapter 2. Prosodic features and the syllable",
      ["Germanic","accent"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch3-vowels-pie-proto-germanic.md",
      "Ch3", "60-71",
      "Chapter 3. Vowels: PIE to Proto-Germanic",
      ["PIE-phonology","ablaut","Proto-Germanic","Germanic"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch4-stressed-vowels-germanic.md",
      "Ch4", "72-95",
      "Chapter 4. Stressed vowels in Germanic",
      ["ablaut","accent","Germanic"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch5-vowels-lesser-stress.md",
      "Ch5", "96-115",
      "Chapter 5. Vowels of lesser stress",
      ["ablaut","law-Sievers","Germanic"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch6-consonants.md",
      "Ch6", "116-157",
      "Chapter 6. Consonants",
      ["stops","fricatives","sonorants","law-Grimm","law-Verner","Germanic"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch7-nouns.md",
      "Ch7", "158-197",
      "Chapter 7. Nouns",
      ["noun-inflection","o-stem","s-stem","root-nouns","paradigms","Germanic"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch8-pronouns.md",
      "Ch8", "198-224",
      "Chapter 8. Pronouns",
      ["pronouns","paradigms","Germanic"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch9-adjectives.md",
      "Ch9", "225-238",
      "Chapter 9. Adjectives",
      ["adjective-inflection","paradigms","Germanic"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch10-numerals.md",
      "Ch10", "239-253",
      "Chapter 10. Numerals",
      ["numerals","Germanic"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch11-adverbs-prepositions-conjunctions.md",
      "Ch11", "254-258",
      "Chapter 11. Adverbs, prepositions, conjunctions",
      ["syntax","Germanic"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-ch12-verbs.md",
      "Ch12", "259-354",
      "Chapter 12. Verbs",
      ["verb-inflection","thematic-stems","athematic-stems","perfect","present-stems",
       "personal-endings","mood","aspect","paradigms","Germanic"], Q)

entry(W,D, "fulk-2018-comparative-grammar-early-germanic-index-verborum.md",
      "index verborum", "393-437",
      "Index verborum",
      ["Germanic","comparative-reconstruction"], Q)


# ---------------------------------------------------------------------------
# KROONEN 2013 — Etymological Dictionary of Proto-Germanic (EDPG)
# ---------------------------------------------------------------------------
W = "Kroon13"
D = "kroonen-2013-proto-germanic"
Q = "mixed-OCR"

entry(W,D, "kroonen-2013-proto-germanic-frontmatter.md",
      "front matter", "PDF 1-11",
      "Front matter: title pages, contents, preface, symbols/abbreviations, entry-structure note",
      ["Proto-Germanic","etymological-dictionary"], Q)

entry(W,D, "kroonen-2013-proto-germanic-introduction.md",
      "introduction", "PDF 12-38",
      "Introduction: phonology and sound changes, incl. relative-chronology flowchart",
      ["Proto-Germanic","sound-changes","sound-change-chronology","PIE-phonology"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-a.md",
      "Letter A", "1-45",
      "Dictionary entries under A",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-b.md",
      "Letter B", "46-85",
      "Dictionary entries under B",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-d.md",
      "Letter D", "86-114",
      "Dictionary entries under D",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-e.md",
      "Letter E", "115-122",
      "Dictionary entries under E",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-f.md",
      "Letter F", "123-163",
      "Dictionary entries under F",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-g.md",
      "Letter G", "164-197",
      "Dictionary entries under G",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-h.md",
      "Letter H", "198-269",
      "Dictionary entries under H",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-i.md",
      "Letter I", "270-272",
      "Dictionary entries under I",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-j.md",
      "Letter J", "273-277",
      "Dictionary entries under J",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-k.md",
      "Letter K", "278-322",
      "Dictionary entries under K",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-l.md",
      "Letter L", "323-347",
      "Dictionary entries under L",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-m.md",
      "Letter M", "348-381",
      "Dictionary entries under M",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-n.md",
      "Letter N", "382-394",
      "Dictionary entries under N",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-o.md",
      "Letter O", "395-396",
      "Dictionary entries under O",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-p.md",
      "Letter P", "397-402",
      "Dictionary entries under P",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-r.md",
      "Letter R", "403-420",
      "Dictionary entries under R",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-s.md",
      "Letter S", "421-505",
      "Dictionary entries under S",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-t.md",
      "Letter T", "506-531",
      "Dictionary entries under T",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-thorn.md",
      "Letter Þ", "532-557",
      "Dictionary entries under Þ",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-u.md",
      "Letter U", "558-564",
      "Dictionary entries under U",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-letter-w.md",
      "Letter W", "565-603",
      "Dictionary entries under W",
      ["Proto-Germanic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "kroonen-2013-proto-germanic-index.md",
      "index", "640-795",
      "Language index",
      ["Proto-Germanic","etymological-dictionary"], Q)


# ---------------------------------------------------------------------------
# MATASOVIĆ 2009 — Etymological Dictionary of Proto-Celtic (EDPC)
# ---------------------------------------------------------------------------
W = "Matas09"
D = "matasovic-2009-proto-celtic"
Q = "mixed-OCR"

entry(W,D, "matasovic-2009-proto-celtic-front-matter.md",
      "front matter", "1-8",
      "Front matter: title, copyright, contents, preface, abbreviations",
      ["Celtic","etymological-dictionary"], Q)

entry(W,D, "matasovic-2009-proto-celtic-introduction.md",
      "introduction", "9-27",
      "Introduction: sound changes, structure of entries",
      ["Celtic","sound-changes","sound-change-chronology","etymological-dictionary"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-a.md",
      "Dictionary A", "28-56",
      "Dictionary entries under A (102 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-b.md",
      "Dictionary B", "57-90",
      "Dictionary entries under B (104 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-d.md",
      "Dictionary D", "91-117",
      "Dictionary entries under D (82 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-i.md",
      "Dictionary I", "176-178",
      "Dictionary entries under I (12 entries); page range corrected from the "
      "source README's internally inconsistent 49-178 (D ends 117, E begins 118) "
      "to 176-178, confirmed via embedded pdf-page anchors in the extraction "
      "(176/177/178/179 sequential, with G ending at 175 and K's frontmatter "
      "independently declaring 179-236).",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-e.md",
      "Dictionary E", "118-125",
      "Dictionary entries under E (27 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-f.md",
      "Dictionary F", "126-149",
      "Dictionary entries under F (87 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-g.md",
      "Dictionary G", "150-175",
      "Dictionary entries under G (78 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-k.md",
      "Dictionary K", "179-236",
      "Dictionary entries under K (196 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-l.md",
      "Dictionary L", "237-256",
      "Dictionary entries under L (68 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-m.md",
      "Dictionary M", "257-286",
      "Dictionary entries under M (105 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-n.md",
      "Dictionary N", "288-298",
      "Dictionary entries under N (29 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-o.md",
      "Dictionary O", "299-308",
      "Dictionary entries under O (29 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-r.md",
      "Dictionary R", "309-320",
      "Dictionary entries under R (40 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-s.md",
      "Dictionary S", "321-368",
      "Dictionary entries under S (161 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-t.md",
      "Dictionary T", "369-398",
      "Dictionary entries under T (101 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-u.md",
      "Dictionary U", "399-403",
      "Dictionary entries under U (23 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-w.md",
      "Dictionary W", "404-435",
      "Dictionary entries under W (92 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-x.md",
      "Dictionary X", "435-435",
      "Dictionary entries under X (1 entry)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-letter-y.md",
      "Dictionary Y", "436-441",
      "Dictionary entries under Y (13 entries)",
      ["Celtic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "matasovic-2009-proto-celtic-appendix-non-indo-european-elements.md",
      "appendix", "443-446",
      "Appendix: non-Indo-European elements in the Celtic lexicon",
      ["Celtic","borrowing","comparative-reconstruction"], Q)


# ---------------------------------------------------------------------------
# STUART-SMITH 2004 — Phonetics and Philology: Sound Change in Italic
# ---------------------------------------------------------------------------
W = "StSm04"
D = "stuart-smith-2004-phonetics-phonology"
Q = "OCR-scanned"

entry(W,D, "stuart-smith-2004-phonetics-phonology-front-matter.md",
      "front matter", "2-25",
      "Front matter",
      ["Italic","historical-linguistics-theory"], Q)

entry(W,D, "stuart-smith-2004-phonetics-phonology-ch1-introduction-phonetics-and-philology.md",
      "Ch1", "26-39",
      "Chapter 1: Introduction: Phonetics and Philology",
      ["historical-linguistics-theory","Italic"], Q)

entry(W,D, "stuart-smith-2004-phonetics-phonology-ch2-italic-sound-change-background.md",
      "Ch2", "40-54",
      "Chapter 2: The Italic Sound Change: Background",
      ["Italic","sound-changes","fricatives"], Q)

entry(W,D, "stuart-smith-2004-phonetics-phonology-ch3-philology-evidence-italic-development.md",
      "Ch3", "55-168",
      "Chapter 3: Philology: The Evidence for the Italic Development",
      ["Italic","sound-changes","fricatives","sound-change-chronology"], Q)

entry(W,D, "stuart-smith-2004-phonetics-phonology-ch4-traditional-arguments-reviewed.md",
      "Ch4", "169-184",
      "Chapter 4: The Traditional Arguments Reviewed",
      ["Italic","sound-changes","fricatives","historical-linguistics-theory"], Q)

entry(W,D, "stuart-smith-2004-phonetics-phonology-ch5-phonetics-predictions-parallels.md",
      "Ch5", "185-219",
      "Chapter 5: Phonetics, Predictions, Parallels",
      ["Italic","fricatives","phonology"], Q)

entry(W,D, "stuart-smith-2004-phonetics-phonology-ch6-phonetic-explanation-italic-development.md",
      "Ch6", "220-249",
      "Chapter 6: A Phonetic Explanation for the Italic Development",
      ["Italic","fricatives","phonology"], Q)

entry(W,D, "stuart-smith-2004-phonetics-phonology-ch7-concluding-remarks.md",
      "Ch7", "250-251",
      "Chapter 7: Concluding Remarks",
      ["Italic","fricatives"], Q)

entry(W,D, "stuart-smith-2004-phonetics-phonology-index-of-words.md",
      "index of words", "276-289",
      "Index of Words",
      ["Italic","comparative-reconstruction"], Q)

entry(W,D, "stuart-smith-2004-phonetics-phonology-general-index.md",
      "general index", "290-295",
      "General Index",
      ["Italic","historical-linguistics-theory"], Q)


# ---------------------------------------------------------------------------
# SWANENVLEUGEL 2021 — Reconstructing Proto-Italo-Celtic
# (Leiden University MA thesis)
# ---------------------------------------------------------------------------
W = "Swan21"
D = "swanenvleugel-2021-reconstructing-proto-italo-celtic"
Q = "born-digital"

entry(W,D, "swanenvleugel-2021-reconstructing-proto-italo-celtic.md",
      "full text", "n/a",
      "Reconstructing Proto-Italo-Celtic: common origins of the phonemic systems "
      "(obstruents incl. mediae aspiratae; vocalic resonants; laryngeals; vowels; "
      "stress) and verbal TAM categories (tense/mood/aspect) of Italic and Celtic",
      ["stops","fricatives","sonorants","syllabic-resonants","laryngeals","ablaut","accent",
       "verb-inflection","aspect","mood","perfect","aorist","comparative-reconstruction",
       "Italic","Celtic"], Q)


# ---------------------------------------------------------------------------
# DE VAAN 2008 — Etymological Dictionary of Latin and the other Italic Languages (EDL)
# ---------------------------------------------------------------------------
W = "Vaan08"
D = "vaan-2008-latin-italic-dialects"
Q = "mixed-OCR"

entry(W,D, "vaan-2008-front-matter.md",
      "front matter", "cover-xiii",
      "Front matter",
      ["Italic","etymological-dictionary"], Q)

entry(W,D, "vaan-2008-introduction.md",
      "introduction", "1-15",
      "Introduction: Italic sound laws and phonology overview",
      ["Italic","sound-changes","sound-change-chronology","etymological-dictionary"], Q)

entry(W,D, "vaan-2008-letter-a.md",
      "Letter A", "PDF 33-81",
      "Dictionary entries under A",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-b.md",
      "Letter B", "PDF 81-91",
      "Dictionary entries under B",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-c.md",
      "Letter C", "PDF 91-174",
      "Dictionary entries under C",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-d.md",
      "Letter D", "PDF 174-198",
      "Dictionary entries under D",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-e.md",
      "Letter E", "PDF 198-211",
      "Dictionary entries under E",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-f.md",
      "Letter F", "PDF 211-268",
      "Dictionary entries under F",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-g.md",
      "Letter G", "PDF 268-291",
      "Dictionary entries under G",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-h.md",
      "Letter H", "PDF 291-306",
      "Dictionary entries under H",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-i.md",
      "Letter I", "PDF 306-333",
      "Dictionary entries under I",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-l.md",
      "Letter L", "PDF 333-370",
      "Dictionary entries under L",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-m.md",
      "Letter M", "PDF 370-413",
      "Dictionary entries under M",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-n.md",
      "Letter N", "PDF 413-435",
      "Dictionary entries under N",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-o.md",
      "Letter O", "PDF 435-453",
      "Dictionary entries under O",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-p.md",
      "Letter P", "PDF 453-517",
      "Dictionary entries under P",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-q.md",
      "Letter Q", "PDF 517-525",
      "Dictionary entries under Q",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-r.md",
      "Letter R", "PDF 525-545",
      "Dictionary entries under R",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-s.md",
      "Letter S", "PDF 545-617",
      "Dictionary entries under S",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-t.md",
      "Letter T", "PDF 617-650",
      "Dictionary entries under T",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-u.md",
      "Letter U", "PDF 650-663",
      "Dictionary entries under U",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-letter-v.md",
      "Letter V", "PDF 663-706",
      "Dictionary entries under V",
      ["Italic","lexicon","etymological-dictionary","comparative-reconstruction"], Q)

entry(W,D, "vaan-2008-index.md",
      "index", "723-833",
      "Indices",
      ["Italic","etymological-dictionary"], Q)


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
        "o-stem", "s-stem", "n-stem", "root-nouns", "athematic-nouns",
        "pronouns", "numerals", "paradigms",
        "derivational-morphology", "word-formation", "compounding", "Caland",
    ]),
    ("Sound Changes & Chronology", [
        "sound-changes", "sound-change-chronology", "Auslautgesetze",
        "law-Grimm", "law-Verner", "law-Sievers", "law-Lindeman", "law-Szemerenyi",
        "law-Stang", "law-Bartholomae", "law-Pinault", "law-Cowgill", "law-Osthoff", "law-Kluge",
    ]),
    ("Languages & Branches", [
        "Proto-Germanic", "Proto-Greek", "Tocharian",
        "Germanic", "Greek", "Italic", "Celtic", "Balto-Slavic",
    ]),
    ("Comparative & Theoretical", [
        "comparative-reconstruction", "etymological-dictionary", "subgrouping", "phylogeny", "cladistics",
        "dialect-geography", "borrowing", "historical-linguistics-theory",
        "syntax", "lexicon",
    ]),
]

lines = [
    "---",
    'title: "Sources — Speed Lookup"',
    'description: "Tag → file index for fast in-session navigation. Grep for a tag heading to get relevant files."',
    'last_updated: "2026-06-27"',
    "---",
    "",
    "# Sources Speed Lookup",
    "",
    "**Usage:** `awk '/^## tag-name$/{p=1} p && /^## / && !/^## tag-name$/{p=0} p' sources-lookup.md`",
    "",
    "**Path prefix:** `sources/{dir}/{file}`",
    "",
    "**Works:** R1996 = Ringe 1996 (Tocharian, OCR); R2013 = Ringe & Eska 2013 (Hist. Ling.); "
    "R2017 = Ringe 2017 (PIE→PGmc, primary); R2024 = Ringe 2024 (Ling. Roots of Greek); "
    "Deuf21 = Deuffic 2021 (PIE→PCelt chronology, MA thesis); "
    "Fulk18 = Fulk 2018 (Comparative Grammar of Early Germanic); "
    "Kroon13 = Kroonen 2013 (EDPG); Matas09 = Matasović 2009 (EDPC); "
    "StSm04 = Stuart-Smith 2004 (Italic sound change); "
    "Swan21 = Swanenvleugel 2021 (Proto-Italo-Celtic, MA thesis); "
    "Vaan08 = de Vaan 2008 (EDL)",
    "",
]

quality_marks = {
    "OCR-scanned": " ⚠OCR",
    "mixed-OCR": " ⚠mixed/OCR",
    "born-digital-glyph-corrupted": " ⚠glyph",
}

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
            q = quality_marks.get(e["quality"], "")
            lines.append(f"- **{e['work']}** {e['section']} pp.{e['pages']}{q} — {e['title']}")
            lines.append(f"  `{e['dir']}/{e['file']}`")
        lines.append("")

leftover = set(tag_map.keys()) - seen_tags
if leftover:
    lines += ["---", "### Other", ""]
    for tag in sorted(leftover):
        lines.append(f"## {tag}")
        for e in tag_map[tag]:
            q = quality_marks.get(e["quality"], "")
            lines.append(f"- **{e['work']}** {e['section']} pp.{e['pages']}{q} — {e['title']}")
            lines.append(f"  `{e['dir']}/{e['file']}`")
        lines.append("")

md_path = os.path.join(out_dir, "sources-lookup.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Written: {tsv_path} ({len(rows)} rows)")
print(f"Written: {md_path}")
print(f"Leftover tags: {sorted(leftover)}")
