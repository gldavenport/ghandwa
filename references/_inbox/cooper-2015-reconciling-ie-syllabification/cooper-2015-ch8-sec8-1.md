---
title: "Chapter 8, §8.1. Restricting Sonorant Syllabicity"
author: "Adam I. Cooper"
date: "2015"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "cooper-2015-reconciling-ie-syllabification.pdf"
chunk: "Chapter 8 §8.1"
pages: "186-190"
---
## 8.1 Restricting Sonorant Syllabicity
Our first goal in establishing an updated account of sonorant syllabicity is to adequately constrain this property to the relevant class of segments. In other words, our formal analysis should explicitly not allow for obstruents to ever be preferred as syllabic peaks, nor for non-high vowels to ever be preferred as syllable margins. We will achieve this aim by building the Optimality-Theoretic constraint ranking around the well-established Peak and Margin families of

<!-- pdf-page: 202; source-page: 187 -->
constraints (Prince and Smolensky 1993 [2004]).3 The basic Peak constraint schema is given in (4), while the basic Margin constraint schema is given in (5) (repeated from (1a.–b.) above). (4) *Peak/X No syllable peaks of category X. (5) *Margin/X No syllable margins of category X. The specific members of these two constraint families are generated in connection with the sonority hierarchy, the arrangement of manner classes we have already shown to be relevant in the composition of complex onsets and codas in Vedic (see Chapters 2 and 3). While for Vedic complex syllable margins we saw fit to operate with a hierarchy differentiating only sonorants from obstruents (a system that will be extended to Proto-Indo-European later in this chapter),4 for the purposes of nucleus selection, following Prince and Smolensky we operate with the conception of the sonority hierarchy given in (6); segment classes decrease in sonority moving from left to right. (6) Vowels > Glides > Liquids > Nasals > Obstruents A couple of notes about this hierarchy as it relates to Proto-Indo-European are in order. First, we consider the category of ‘glides’ to subsume both high vowels *i and *u and their corresponding semivowels *i̯ and *u̯, under the assumption that in Proto-Indo-European high vowels were underlyingly non-syllabic.5 Further, we choose not to differentiate within the class identified as ‘vowels’ mid- vs. low-vowels (classifying high vowels elsewhere), nor within the class 3 For alternative analyses using a stringency approach to constraint formulation (after de Lacy 2004), and arguments in favor of the one developed here, the reader is referred to Cooper 2012. 4 Indeed, the suppression of distinctions within the members of these two classes is a simplification in the hierarchy that could be in principle be captured by constraint ranking (as we will do in the case of nucleus selection). How exactly this should be achieved is a matter we leave for future investigation. 5 See e.g. Weiss 2011. This is a characterization which, incidentally, Pawley (1966) has proposed for the Trans-New Guinea language Kalam (see also Foley 1986).

<!-- pdf-page: 203; source-page: 188 -->
identified as ‘liquids’ rhotics vs. laterals, because so far as we can determine,
such distinctions are irrelevant for the matter at hand.6
The sonority hierarchy allows us to flesh out the Peak and Margin constraint systems along two dimensions. First, the variable X in the constraint
schemata given above is replaced with the various manner classes arrayed in
the sonority hierarchy; for each manner class, a separate Peak and Margin
constraint is generated. Further, in accordance with their arrangement along
the hierarchy, the specific constraints targeting the various manner classes
exist in fixed subhierarchies. These specific constraints and their fixed ranking
are given in (7) and (8).
(7)	 *Pk/Obstruent » *Pk/Nasal » *Pk/Liquid » *Pk/Glide »
*Pk/Vowel
(8)	 *Mar/Vowel » *Mar/Glide » *Mar/Liquid » *Mar/Nasal »
*Mar/Obstruent
The fixed ranking in (7) encodes the increasing dispreference for segments to
be syllable peaks as one moves rightward along the sonority hierarchy: obstruents make worse syllable nuclei than nasals do, nasals make worse syllable
nuclei than liquids do, and so forth.7 On the other hand, the fixed ranking in
(8) encodes the increasing dispreference for segments to be syllable margins
as one moves leftward along the sonority hierarchy: (non-high) vowels make
worse syllable margins than glides do, glides make worse syllable margins than
liquids do, and so forth.
Having established these fleshed out constraint subhierarchies, we begin to
sketch the analysis of sonorant syllabicity first by showing how high-ranking
*Pk/Obstruent prevents obstruents from ever being vocalic. Consider the
following tableau:
(9)
/CROC/
*Pk/Obs
*Pk/Nas
*Pk/Liq
*Pk/Gli
a. CRO̥C
*!
F b. CR̥OC
(*)
(*)
(*)
6	 Although we do note that these subgroups can be distinguished from each other in certain
ways—the near, if not complete, absence of *a in the language as compared to *e and *o, and
the rarity of *r in initial position as compared to *l, come to mind in this context.
7	 Though in recent work (Cooper 2013b), we have shown how sonority-driven syllabicity,
which does hold to some extent for Proto-Indo-European, is not necessarily the rule for all
languages with syllabic consonants.

<!-- pdf-page: 204; source-page: 189 -->
The interconsonantal environment of the schematic sequence RO (where R =
any sonorant consonant) in theory provides an opportunity for the obstruent
to become syllabic, but it does not—it is the sonorant which preferentially
vocalizes, whether it be a nasal, liquid, or glide (or even non-high vowel, given
that *Pk/Vowel is lower-ranked as well).
A problematic consequence of this approach should already be apparent:
with the fixed ranking of Peak constraints, with no intervention the more
sonorous segment will always be preferably vocalized over the less sonorous
one.
(10)
/CGNC/
*Pk/Obs
*Pk/Nas
*Pk/Liq
*Pk/Gli
L a. CGN̥C
*!
F b. CG̥NC
*
Here, for a sequence of glide + nasal, the candidate containing a vocalic glide
(i.e. a high vowel) is selected as more optimal than one featuring a vocalic
nasal, counter to our expectations for Proto-Indo-European.
The appropriate means of avoiding this outcome is to posit some additional
constraint. For the time being we identify this constraint simply as C, but will
take up the question of its identity in the next section. As shown by the tableau
in (11), C should intervene in the hierarchy, precisely at a point where it can
have the effect of conflating the treatment of nasals, liquids, and glides, but
crucially not obstruents, in the process of nucleus selection.
(11)
/CGNC/
*Pk/Obs
C
*Pk/Nas
*Pk/Liq
*Pk/Gli
F a. CGN̥C
*
b. CG̥NC
*!
*
C must be violated by the otherwise favored candidate, here CG̥NC, such that
it is consistently the second sonorant, regardless of relative sonority, which
preferably vocalizes. Ideally C will also negotiate between candidates featuring sonorants of like-sonority (e.g. CNN̥C over CN̥NC); but an additional constraint could also be involved in this particular case.
The introduction of C into the ranking may affect the viability of the analysis
as concerns nucleus selection in other sequences. If C is at all concerned with
the linear order of segments, at a strictly segmental level or otherwise—e.g., if
C is to be identified with NoCoda (an obvious possibility), a constraint which
would penalize right-hand segments over left-hand ones—then its influence
may have to be appropriately constrained in the case of CVRC sequences.
Otherwise it would predict the outcome †CV̯R̥C, analogous to CRR̥C (although

<!-- pdf-page: 205; source-page: 190 -->
in the case of CVOC, high-ranking *Pk/Obstruent would militate against a
syllabic obstruent).
(12)
/CVNC/
*Pk/Obs
C
*Pk/Nas
*Pk/Liq
*Pk/Gli
*Pk/V
F a. CV̯N̥C
*
L b. CVNC
*!
*
In this example the nasal on the right is preferably syllabic over the non-high
vowel to its left, so as to satisfy C.
As we would like to penalize instances in which non-high vowels are not
actually syllabic, we see in this case justification for including in the ranking
the constraint *Mar/Vowel ‘No (non-high) vowels as syllable margins’, which
was introduced in (8) as the highest-ranked member of the Margin family of
constraints. This constraint should be inserted high enough into the ranking to
force the syllabicity of non-high vowels, regardless of any violations of C which
may be consequently incurred:
(13)
/CVNC/
*Pk/Obs
*Mar/V
C
*Pk/N
*Pk/L
*Pk/G
*Pk/V
 a. CV̯N̥C
*!
*
F b. CVNC
*
*
*Mar/Vowel can be non-crucially ranked with respect to *Pk/Obstruent,
but must outrank constraint C.8
Finally, to ensure that epenthesis is not permitted as a means of repairing illicit sequences featuring sonorants, but rather that vocalization is the
preferred strategy, we must also include the constraint Dep-IO in (2), which
militates against insertion of segments; its influence can be observed in the
tableau in (14).
(14)
/CRRC/
*Pk/Obs *Mar/V Dep-IO C *Pk/N *Pk/L *Pk/G *Pk/V
F a. CVRR̥C
*!
(*)
(*)
(*)
(*)
b. CRVRC
*!
*
The positioning of Dep-IO allows for epenthesis only when the alternative
would be a vocalic obstruent; otherwise insertion of a vowel is less preferred
8	 Though we will not explicitly include them in the ranking, we assume that the remaining
members of the Margin constraint family are dominated by the constraint C, so as to generate the desired outcomes.

<!-- pdf-page: 206; source-page: 191 -->
than vocalizing a sonorant consonant.9 As for the ranking of this constraint with respect to *Mar/Vowel, we note that epenthesis would be doubly disfavored if associated with the marginalization of a non-high vowel (e.g. †CV̯VC). We also expect that a violation of Dep-IO coincides here with a violation of C, since C disfavors the maintaining of right-hand consonants. At this point it appears that no crucial relationship is discernible between these two constraints, although as we have shown in (13) *Mar/Vowel must outrank C.10 This is the final step in the initial development of an analysis building on the fixed Peak subhierarchy of constraints, with the goal of restricting syllabicity to sonorants (including vowels). To summarize, we see fit to propose the following constraint ranking: (15) *Pk/Obstruent, *Mar/Vowel » Dep-IO, C » *Pk/Nasal » *Pk/Liquid » *Pk/Glide » *Pk/Vowel While we have included here all of the members of the Peak subhierarchy, it is only the constraints enclosed in the box which are actually active in the analysis. The constraint C serves, as desired, to conflate the segments targeted by the constraints it outranks.11 How exactly it generates the right-hand vocalization of sonorants in Proto-Indo-European—that is, how this constraint is to actually be defined—is the next matter we take up.
