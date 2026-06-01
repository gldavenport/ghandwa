---
title: "§3.1 Introduction"
last_updated: 2026-05-31T00:00-04:00
chapter: ch3-development
supersedes: "docs/grammar/ch3-development/phonological-history.md (§§0, 2)"
---

# §3.1 Introduction

PIE phonology is substantially reconstructable, and Ghandwa preserves much of it. Nevertheless, the development from PIE to Ghandwa is not a short one. More than twenty regular sound changes can be reconstructed, and their relative chronology is largely recoverable. The most distinctive changes are phonological: Ghandwa is separated from its sister branches above all by the voiced fricatives it develops from the PIE aspirated stops, and by the *a*-colored epenthesis that resolves the syllabic resonants.

The changes are not evenly distributed. Sound changes are the most extensive, comprising a pre-stage of shared centum and labiovelar developments, a first stage of laryngeal elimination and related vowel changes, and a second stage of Ghandwa-specific innovations. Morphological development, while real, is more conservative than in Germanic or Celtic; nominal and verbal paradigms retain PIE structures with relatively modest restructuring. Syntactic changes are not yet fully studied and are deferred.

This chapter documents the phonological development in detail. For the synchronic grammar of Ghandwa — the surface phonological inventory, standing alternations, and morphology — see Chapter 4. For notation and transliteration conventions, see §1.2 (*ch1-introduction/notation.md*).

The primary structural model throughout is Ringe 2017 (*From Proto-Indo-European to Proto-Germanic*, 2nd ed.), supplemented by Ringe 2024 for thorn clusters. The rule inventory is also implemented computationally in the transformer tool at *tools/pie_transformer/*, which serves as a verification device for the derivations given in individual dictionary entries and in the worked examples of §3.2.5.

## §3.1.1 Ghandwa's Comparative Position

Ghandwa is a centum language of the western Indo-European group. Its primary comparanda are Proto-Germanic (PGmc), Proto-Italic (PIt), and Proto-Celtic (PC) — together "Western Indo-European" (WIE). Where all three share an inherited form, that is the Ghandwa form. Where they diverge through independent innovation, Ghandwa generally preserves the PIE-inherited state rather than following any single branch. Proto-Balto-Slavic (PBS) is consulted as a fourth witness but held at arm's length due to satemization and structural divergences in nominal morphology.

Two developments define Ghandwa relative to PIE and distinguish it from its closest neighbors:

**Voiced fricatives from aspirates.** The PIE breathy-voiced stops \*bʰ, \*dʰ, \*gʰ, \*gʷʰ surface as voiced fricatives β, ð, ɣ, ɣʷ — not as voiceless fricatives (as in Germanic via Grimm's Law) and not as plain voiced stops (as in Italic and Celtic). The initial step of Grimm's Law — aspirates becoming voiced fricatives — is thus shared with Germanic, but Ghandwa does not continue into the full chain shift.

**CaRC syllabic resonant vocalism.** The PIE syllabic resonants \*r̥, \*l̥, \*m̥, \*n̥ vocalize with an *a*-colored epenthetic vowel preceding the resonant: \*r̥ → *ar*, \*l̥ → *al*, \*m̥ → *am*, \*n̥ → *an*. This aligns with Celtic in vowel quality (*a*, not Germanic *u*) and with Germanic in linear order (*aR*, not Italic *Ra*).

Several major innovations attested in sister branches are explicitly absent from Ghandwa. The full Grimm's Law chain shift (voiceless stops to voiceless fricatives, voiced stops to voiceless stops) is Germanic-specific; Ghandwa applies only the aspirate step. Verner's Law (accent-conditioned voicing of fricatives) is replaced in Ghandwa by a simpler phonotactic rule. The o/a merger is Germanic-specific; Ghandwa preserves the PIE *o/a* distinction. The shift \*gʷ → *b* and the loss of \*p are Celtic-specific; Ghandwa preserves both. The Ghandwa *s*-voicing rule (§3.2.3.4) is conditioned by the voicing of adjacent segments, not by accent position — the crucial formal difference from Verner's Law that determines its classification as an independent development.

The comparative framework also bears on the interpretation of Pre-Ghandwa. The parent stage is best understood as a dialect continuum rather than a uniform protolanguage; variant formations from the same root can coexist in the lexicon as regional or register doublets.
