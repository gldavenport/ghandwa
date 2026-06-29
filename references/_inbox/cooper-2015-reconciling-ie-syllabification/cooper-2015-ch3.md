---
title: "Chapter 3. Formal Analysis of Vedic Medial Syllabification"
author: "Adam I. Cooper"
date: "2015"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "cooper-2015-reconciling-ie-syllabification.pdf"
chunk: "Chapter 3"
pages: "75-106"
---
# Chapter 3. Formal Analysis of Vedic Medial Syllabification
## 3.0 Introduction1
An analysis of medial syllabification in Vedic, in order to achieve explanatory adequacy, must account for the following generalizations established to hold for the language’s word-internal syllable structure: (1) Generalizations about Vedic Medial Syllabification a. V.CV: Single intervocalic consonants are onsets. b. VC.CV: A sequence of two intervocalic consonants is treated heterosyllabically, i.e. as a sequence of coda + onset. c. VRO.RV, VRO.OV, VO.ORV: A sequence of three or more intervocalic consonants is treated first in accordance with generalization (1b.); the syllabic allegiance of the remaining intermediate consonant(s) is determined by the sonority sequencing principle and influenced by a dispreference for complex onsets which is stronger than that for superheavy syllables (or complex codas). d. Superheavy syllables are disfavored, but are actively and consistently prevented from surfacing only in the perfect conjugation. e. Segments are generally neither inserted nor deleted to improve syllabification. With respect to the final generalization, we recognize one exception we must also account for. It is a case of epenthesis: the appearance of i peculiar to the perfect paradigm (referred to in (1d.)), which breaks up potential superheavy syllables and complex onsets, and allows for the syllabification of what would otherwise be unsyllabifiable sequences of consonants.2 1 A condensed version of the analysis developed here can be found in Cooper 2013a, and elaborated discussion on several theoretical points can be found in Cooper 2013c. 2 In the analysis developed here we abstract away from two other exceptions: the loss of s when between consonants (see 2.2.3 in the previous chapter), and svarabhakti, which can also be motivated by preferences of syllable structure (see the discussion in Kobayashi 2004: 35ff.).

<!-- pdf-page: 91; source-page: 76 -->
In this chapter we develop an account of Vedic medial syllabification in the constraint-based framework of Optimality Theory (Prince and Smolensky 1993 [2004]). We will proceed as follows: in 3.1 we build an analysis of the general syllabification system in Vedic, as captured in the generalizations above, particularly (1a.–c.). We turn to syllabification in the perfect conjugation in 3.2, and address the question of how to incorporate the exceptional patterns observed in this domain within the overall system. We summarize the contours of our final analysis in 3.3. Before moving on to 3.1, we first briefly introduce the constraints that will play a role in the general analysis. We begin with the set of relevant markedness constraints, presented in (2) according to their order of appearance in the discussion (with the exception of (2h.–i.), which are addressed below); all pertain to syllable well-formedness. (2) Vedic Medial Syllable Structure Markedness Constraints a. Onset Syllables have onsets. b. NoCoda Syllables may not have a coda. c. *ComplexOnset Syllables may not have more than one onset segment. d. Syllable-Contact A syllable contact A.B is the more preferred, the higher the sonority of the offset A and the lower the sonority of the onset B. e. *3μ

No trimoraic (superheavy) syllables.
f. 	 *ComplexCoda
Syllables may not have more than one coda segment.
g. Sonority-Sequencing
Complex onsets rise in sonority, and complex codas fall in sonority.3
h.	*Appendix

No appendix (i.e. non-moraic coda) segments. i. *μ/Consonant Consonants must not be moraic. These constraints are all well established in the literature; we will comment briefly on a few of them. First, we differentiate between two versions of the *Complex constraint schema, *ComplexOnset (2c.) and *ComplexCoda 3 For a more technical definition, see n. 11 in Chapter 1.

<!-- pdf-page: 92; source-page: 77 -->
(2f.), so as to formally encode the greater dispreference for complex onsets than for complex codas, an aspect of Vedic syllabification which in an Optimality-Theoretic account must be due to the influence of multiple distinctly-ranked constraints. Also, with respect to (2d.), we assume a general conception of Syllable-Contact, defining it so as to simply prefer a fall in sonority from coda to following onset, such as one would have in the case of VR.OV, but not VO.RV;4 as we will see, however, such a preference is consistently unsatisfied in the syllabification of Vedic. As for the constraint Sonority-Sequencing in (2g.), it is defined here in accordance with our proposal in the previous chapter that Vedic maintains a strong version of the sonority sequencing principle word-medially, allowing only for complex onsets of rising sonority and complex codas of falling sonority, and no sonority plateaus (sequences of segments of like sonority) in either position. Further, we assume for Vedic an associated sonority hierarchy that at a minimum makes a distinction between obstruents (O) and sonorants (R), with the latter of course being greater in sonority than the former. Finally, we can note the importance of the constraints *Appendix and *μ/Consonant in (2h.–i.), the interaction of which, after Sherer (1994), governs the status of coda consonants vis-à-vis syllable weight.5 Even though these constraints will not feature explicitly in the following analysis, their activity in the overall Vedic constraint ranking is clear, given that syllables which end in -VC. are counted as heavy by Vedic meter. As such, we assume the relevant ranking of these constraints to be *Appendix » *μ/Consonant, by which coda consonants are preferably moraic, as opposed to being an appendix, that is, attached directly to the syllable node.6 In addition to these markedness constraints, the usual faithfulness constraints Dep-IO and Max-IO (McCarthy and Prince 1995), defined in (3), are relevant in the analysis of Vedic medial syllabification as well. (3) Vedic Medial Syllable Structure Faithfulness Constraints a. Dep-IO An output segment has a correspondent in the input. (‘No epenthesis.’) b. Max-IO An input segment has a correspondent in the output. (‘No deletion.’) 4 But see Gouskova 2004 for a more fine-grained approach to the issue of syllable contact, in which the phenomenon emerges out of the influence of a hierarchy of relational constraints. 5 Alternatively, one could also invoke high-ranking Weight-By-Position (‘Coda consonants are moraic’), after Hayes (1989). 6 These constraints will be explicitly introduced into the ranking in the morphophonological analysis of Proto-Indo-European nucleus selection we develop in Chapter 9.

<!-- pdf-page: 93; source-page: 78 -->
Generally, neither epenthesis nor deletion is resorted to as a means of improving syllable structure, suggesting that these two constraints hold a rather high position in the constraint ranking. They feature in the tableaux to follow only when their influence is a focus of discussion (for example, in the insertion of the perfect union vowel). Additional constraints that will prove relevant in various subcomponents of the analysis, such as the interaction of syllabification and reduplicated stem formation (3.1.2.1) and, more importantly, perfect union vowel epenthesis (3.2), will be introduced as required; again, the preceding constraint overview is meant to apply to the general process of syllabification in Vedic.
## 3.1 Vedic Medial Syllabification: The General System
In this section we begin our formal analysis of medial syllabification in Vedic by accounting for the syllabification patterns observed in general in the language. In 3.1.1 we focus on generalization (1a.) and provide an analysis of VCV sequences; in 3.1.2 we account for (1b.), looking at VCCV sequences with both short and long initial vowels; and in 3.1.3 we account for generalization (1c.), looking at VCCCV sequences. Sequences of more than three consonants are examined in 3.1.4, and in 3.1.5 we summarize the ranking of constraints relevant for Vedic in general.
### 3.1.1 Syllabification of VCV Sequences
A single intervocalic consonant is always treated as the onset of the syllable
headed by the following vowel, not as the coda of the syllable headed by the
preceding one, as in (4): the syllabification é.mi is most optimal because it violates neither Onset (2a.) nor NoCoda (2b.), which are not crucially ranked
with respect to one another.7
(4)	 VCV: é.mi  1 sg. pres. act. ind ‘go’8
/e-mi/
Onset
NoCoda
F a. e.mi
b. em.i
*!
*
7	 Though because of subsequent constraint rankings requiring the demotion of NoCoda,
these two constraints will come to occupy different tiers in the ranking.
8	 Accent is indicated where applicable, but will not play a role in the formal analysis.

<!-- pdf-page: 94; source-page: 79 -->
This syllabification holds regardless of where a morpheme boundary may lie: thus the form ās-a 1 sg. perf. act. ind ‘be’ is syllabified ā.sa, not †ās.a.
### 3.1.2 Syllabification of VCCV Sequences
Medial biconsonantal sequences preceded by a short vowel are treated in 3.1.2.1, while those preceded by a long vowel are treated in 3.1.2.2.
#### 3.1.2.1 Syllabification of V̄CCV Sequences
Intervocalic sequences of two consonants are treated heterosyllabically, as has been shown by, among other things, consideration of Vedic metrical practice. Such treatment holds for both sequences preceded by a short vowel, and those preceded by a long vowel (as addressed in the next subsection). Even if the consonants rise in sonority, thus forming a theoretically viable onset (as per the sonority sequencing principle), they are still syllabified as coda + onset. This outcome is instantiated by introducing the markedness constraints *ComplexOnset (2c.) and Syllable-Contact (2d.) and the faithfulness constraints Dep-IO (3a.) and Max-IO (3b.) into the system, in the crucial ranking in (5): (5) Dep-IO, Max-IO, *ComplexOnset » NoCoda, Syllable-Contact Due to the prevailing dispreference for complex onsets over coda consonants in Vedic, the constraint *ComplexOnset must dominate NoCoda, and as such this constraint can no longer occupy the top tier of the ranking. Likewise, since so far we have seen neither epenthesis nor deletion figure as a strategy aiding syllabification, the constraints Dep-IO and Max-IO are at this point undominated in the ranking. The tableau in (6), for the form pavítrais inst. pl. neut. ‘filter’, demonstrates the effect of this ranking: the obstruent-sonorant sequence -tr- can constitute a perfectly good onset, but because of the dispreference for complex onsets, it does not syllabify as such. (6) V̆ORV: pa.vít.rais inst. pl. neut. ‘filter’ /pavitrais/ Dep-IO Max-IO *CompOns NoCoda Syll-Cont F a. pa.vit.rais ** * b. pa.vi.trais *! * c. pa.vi.tV.rais *! d. pa.vi.rais *!

<!-- pdf-page: 95; source-page: 80 -->
We also see in this tableau the prevailing influence of the faithfulness constraints Max-IO and Dep-IO: neither insertion (as in (6c.)) nor deletion (as
in (6d.)) is tolerated to avoid the disfavored complex onset structure. Lastly,
the tableau also shows the lack of influence of the Syllable Contact Law
(Vennemann 1988); the optimal syllabification satisfies *ComplexOnset at
the cost of violating Syllable-Contact, by positioning less sonorous t in a
coda preceding more sonorous r in a following onset.
Given the ranking in (5), the heterosyllabic treatment of the three other
types of medial biconsonantal sequences (if differentiating between obstruents and sonorants)—i.e., VOOV, VROV, and VRRV—is easily accounted for as
well. We can see as much in the tableaux in (7)–(9); in view of the sonority
profiles involved, heterosyllabicity is to be expected. (Note we omit from these
tableaux disfavored candidates showing epenthesis or deletion, in the interests
of space.)
(7)	 V̆OOV: a.pap.tan 3 pl. aor. act. ind. ‘fall’
/a-pa-pt-an/
*ComplexOnset
NoCoda
F a. a.pap.tan
**
b. a.pa.ptan
*!
*
(8)	 V̆ROV: sár.pa.ti  3 sg. pres. act. ind. ‘creep’
/sarpa-ti/
*ComplexOnset
NoCoda
F a. sar.pa.ti
*
b. sa.rpa.ti
*!
(9)	 V̆RRV: kár.ma  nom. acc. sg. neut. ‘act’
/karma/
*ComplexOnset
NoCoda
F a. kar.ma
*
b. ka.rma
*!
Given high-ranking *ComplexOnset, complex onsets are consistently
avoided, regardless of the sonority profile of the consonants in question. As
an alternative take on the evaluation process, we might reason that the complex onsets resulting from a tautosyllabic treatment of these consonantal
sequences (†.pta-, †.rpa-, †.rma-) would be disfavored from the start, as they
violate the relevant conception of the sonority sequencing principle. While

<!-- pdf-page: 96; source-page: 81 -->
this intuitively makes sense, nonetheless the forms examined in (7)–(9) would not crucially justify inclusion of the constraint Sonority-Sequencing (2g.) in the ranking, as the desired optimal output in each of these cases is still attained, despite its absence, with the constraints and ranking established thus far. Rather, the inclusion of this constraint will be justified in view of another case, examined below in 3.1.3. Note also that in the case of sárpati in (8), the structure we might want to avoid more reasonably than the candidate †sa.rpa.ti would be, given sonority sequencing, †sarp.a.ti, with complex coda of falling sonority; but such a candidate, in featuring both an onsetless syllable -.a.- as well as a syllable with two coda consonants (sarp.-), would be ruled out by both Onset and NoCoda, respectively. In the context of V̆CCV syllabification, it is also important to note the formation of certain aorist and intensive stems, requiring reduplicated prefixes of minimally bimoraic size. As we saw in the previous chapter, the heterosyllabic treatment of medial consonants establishes a syllabification that can play a role in the satisfaction of these templatic size requirements. Typically, in the case of roots beginning with a single consonant, the final vowel of the reduplicated prefix must be lengthened to meet this requirement, an outcome shown in the stem forms ájījana- aor. ‘beget’ and ganīgam- intens. ‘go’. To obtain this result, we propose the ranking in (10): (10) [Ci]2μAor, [CV[Ci]2μ]Intens » Dep-μ-IO The constraints [Ci]2μAor (‘The aorist reduplicated prefix Ci- should be a heavy syllable’) and [CV[Ci]2μ]Intens (‘The intensive reduplicated prefix CVCi- should terminate in a heavy syllable’) are used here as a shorthand to represent the associated bimoraic size requirement for the syllable headed by prefix-final i. Since it is preferable to lengthen i than to fail to satisfy bimoraicity, these constraints must crucially outrank the constraint Dep-μ-IO, a variant of the basic anti-insertion constraint in (3a.) relativized to the mora and militating against processes such as vowel lengthening. The effect of this ranking, in the evaluation of the stem forms noted above, can be seen in the following tableaux; note that, as the nature of the reduplication process involved in the formation of these stems is beyond the scope of the current discussion, we simply include in the inputs the template for the reduplicated prefix—[Ci] for the aorist, [CVCi] for the intensive—and its filled-in realization in the various output candidates (-ji- and gani-, respectively).

<!-- pdf-page: 97; source-page: 82 -->
(11)	 Ci-CV: á.jī.ja.na- aor. ‘beget’
/a-[Ci]-jan-a-/
[Ci]2μAor
Onset
Dep-μ-IO
a. a.ji.ja.na*!
*
b. a.jij.a.na*!
*
F c. a.jī.ja.na*
(12)	 CVCi-CV: ga.nī.gam-  intens. ‘go’
/[CVCi]-gam-/
[CV[Ci]2μ]Intens
Onset
Dep-μ-IO
a. ga.ni.gam*!
b. ga.nig.am*!
*
F c. ga.nī.gam*
The general principles of Vedic syllabification yield the candidates in (11a.)
and (12a.), in which the root-initial consonant functions as an onset; yet the
templatic size requirement is unmet, meaning the forms incur a fatal violation
of highly-ranked [Ci]2μAor and [CV[Ci]2μ]Intens and are thus eliminated from
consideration. Two alternatives are syllabifying the root-initial consonant as a
coda (the candidates in (11b.) and (12b.)), or lengthening the prefix-final i (the
candidates in (11c.) and (12c.)). Each of these strategies incurs a violation of
Dep-μ-IO, as an additional mora comes into play, associated either to a coda
consonant9 or the lengthened vowel. But, given the high position of Onset in
the ranking, the latter option is the more preferred.
For roots which begin with a sequence of two consonants, though, the heterosyllabic treatment of intervocalic CC sequences means that these two consonants will be split up, such that the first C will constitute the coda of the
reduplicated prefix syllable. In this way, the bimoraic size requirement is satisfied; the tableaux in (13) and (14) demonstrate as much.
(13)	 Ci-CCV: cik.ṣi.pa- aor. ‘throw’
/[Ci]-kṣipa-/
[Ci]2μAor
*CompOns
NoCoda
Dep-μ-IO
F a. cik.ṣi.pa*
*
b. ci.kṣi.pa*!
*
c. cī.kṣi.pa*!
*
9	 Again, coda moraicity is assumed to follow from the ranking *Appendix (2h.) » *μ/
Consonant (2i.). Note that in the tableaux for the intensive stems in (12) and (14) we
abstract away from the moraicity of any codas that may occur in the final syllable associated
with the root; e.g. no violation of Dep-μ-IO is shown for the segment m in ganigam-.

<!-- pdf-page: 98; source-page: 83 -->
(14)	 CVCi-CCV: ka.nik.rand- intens. ‘cry out’
/[CVCi]-krand-/
[CV[Ci]2μ]Intens
*CompOns
NoCoda
Dep-μ-IO
F a. ka.nik.rand*
*
b. ka.ni.krand*!
*
c. ka.nī.krand*!
*
That the prefix-final syllable is heavy here is a natural outcome of the general
principles of Vedic syllabification. Thus the lengthening process in these cases
is unnecessary: the quantity of prefix-final i is not altered in either of the winning candidates in (13a.) or (14a.), because the syllable the vowel heads has
already been made heavy by virtue of medial consonant heterosyllabicity. Note
that since Dep-μ-IO is violated by any form that features a coda consonant in
Vedic, it must be crucially ranked below *ComplexOnset, since otherwise we
might expect the candidates in (13b.) and (14b.) to (undesirably) be selected
as most optimal. Lastly, we also see here that, again, morpheme boundaries
which may intervene in internal consonantal sequences do not necessarily
have an effect on their syllabification.
#### 3.1.2.2 Syllabification of V̅CCV Sequences
Given the relevance of superheavy syllables in Vedic (see the discussion in the
previous chapter) we have no reason to believe that the syllabification of forms
such as śāsmahe 1 pl. pres. mid. ind. ‘order’, which feature a long vowel, should
not follow the general heterosyllabic treatment of intervocalic biconsonantal
sequences. So, based on the established constraint rankings, we see that the
most optimal candidates in the tableaux in (15) and (16) break up the intervocalic consonant cluster across two syllables, the first of which is consequently
superheavy. This fact suggests the ranking in (15):
(15)	 *ComplexOnset » *3μ
*ComplexOnset (2c.) must outrank *3μ (2e.): it is worse to feature a complex
onset than a superheavy syllable. The tableaux in (16)–(17) demonstrate the
importance of this relationship.
(16)	 V̅ORV: śās.ma.he 1 pl. pres. mid. ind. ‘order’
/śās-mahe/
*ComplexOnset
*3µ
NoCoda
F a. śās.ma.he
*
*
b. śā.sma.he
*!

<!-- pdf-page: 99; source-page: 84 -->
(17)	 V̅ROV: ār.ta 3 sg. aor. mid. ind. ‘move, rise’
/ār-ta/
*ComplexOnset
*3µ
NoCoda
F a. ār.ta
*
*
b. ā.rta
*!
We also see, once again, that the type of juncture preferred by the Syllable-Contact constraint continues to be unrealized, as the winning candidate in
(16a.) features an obstruent coda followed by a sonorant onset. In addition,
recall that the general syllabification of sequences involving long vowels is one
of the outcomes explicitly avoided in the perfect by the insertion of i (see 3.2
below).10
### 3.1.3 Syllabification of VCCCV Sequences
The syllabification of sequences of three consonants between vowels is
understandably more complex than the cases reviewed above. Here sonority
sequencing comes into play as an influential force weeding out non-optimal
candidates: while the first and last consonants are treated heterosyllabically,
the association of the intervening consonant depends on whether it can
better comprise the final consonant of a complex coda or the initial consonant of a complex onset. If either position is theoretically possible, then the
stronger restriction on complex onsets means that the consonant will be part
of the coda.
Before moving on to individual cases, it is important to note that, as already
observed in the previous chapter, of all possible combinations of consonants
in a string VCCCV, only a subset are actually attested in Vedic. Operating with
a sonority hierarchy making a distinction between only sonorants and obstruents, we earlier posited the following eight logically possible shapes:
(18)	 Logically Possible VCCCV Sequences
a. VOORV
VRORV
VROOV
b. VOOOV
c. VOROV
VORRV
VRRRV
d. VRROV
10
One might question the inclusion of the constraint *3μ in these tableaux, since the
correct result can be achieved without it, given the effects of NoCoda. While this may be
the case here, the importance of *3μ will prove crucially distinct from that of NoCoda in
the discussion of the perfect union vowel.

<!-- pdf-page: 100; source-page: 85 -->
These eight shapes have been classified as follows. Starting with the three in (18a.), these actually appear in general in Vedic, with varying frequency, and will be treated below. The shape in (18b.) appears in non-perfect forms only underlyingly, specifically when s occurs between consonants (see n. 2). In addition, the same shapes in (18a.) and (18b.), together with those in (18c.), are also found in the underlying structure of forms of the perfect, but fail to surface as a contiguous sequence because of the insertion of i; these cases will be addressed in 3.2. Left remaining is the final potential sequence -VRROV- in (18d.), which, following Gotō’s (2005: 205–206) survey of internal triconsonantal groups in Indo-Iranian, does not occur at all in Vedic, lexically or by virtue of morpheme concatenation. As such it will not feature in the analysis developed here. Again, we find it significant that the three sequences which do surface generally in Vedic given in (18a.) are the only ones which can straightforwardly be syllabified in accordance with the sonority sequencing principle calling for complex codas to fall in sonority and complex onsets to rise in sonority. The remaining five in (18b.–d.) cannot be so treated, as is, although it is interesting that a majority of them can be found in the perfect, where i-epenthesis significantly improves their ability to be syllabified.11 With respect to unattested VRROV, while we would predict it not to surface as such, it is not unreasonable to think it possible in the underlying form of a perfect. In fact a potential candidate presents itself in the perfect stem dadhanv- ‘run’; while its only attested indicative form is third plural middle dadhanviré, if inflected in either the second person singular active (-tha) or middle (-sé), or the second person plural middle (-dhvé), we would have an instance of the environment VRROV. As such we would sooner characterize the absence of this shape as more accidental than anything else, a consequence of the limits of our sources. Returning to the generally attested sequences, let us begin with VROOV. Given a strong version of the sonority sequencing principle, sequences of this shape are syllabified with a complex coda, that is, as VRO.OV. The constraint rankings established thus far are enough to guarantee this outcome, as the tableau in (19) shows; we also include here the constraint *ComplexCoda (2f.), which clearly must rank below *ComplexOnset.12 11 A question worth considering is whether the insertion of i in these particular cases should be analyzed as a perfect-internal phenomenon, as epentheses to resolve superheavy syllables and complex onsets are, or as a more general process, given the all-around poor sonority profiles the sequences feature. We take up this issue at the end of 3.2. 12 The need to invoke *ComplexCoda in addition to *3μ is worth considering further. Under the assumption that each coda consonant bears weight, every violation of *ComplexCoda

<!-- pdf-page: 101; source-page: 86 -->
(19)	 VROOV: chant.si 2 sg. pres. act. ind. ‘seem’
/chant-si/
Dep-IO Max-IO *CompOnset
*3µ
*CompCoda NoCoda
F a. chant.si
*
*
**
b. chan.tsi
*!
*
c. chan.tV.si
*!
*
d. chan.si
*!
*
Given high-ranking Max-IO and Dep-IO, a superheavy syllable / complex
coda is better than resorting to deletion or epenthesis. Further, because of the
position of *ComplexOnset over both *3μ and *ComplexCoda, this option
is also preferable over realizing a complex onset. Thus the winning candidate
is chant.si in (19a.).
Moving on to VRORV, there are two possible syllabifications for forms containing this sequence, given strong sonority sequencing. Depending on the
treatment of the intervening obstruent, we could have a complex onset (VR.
ORV) or a complex coda (VRO.RV). Evaluated under the constraint ranking
developed thus far, however, it is the latter option which is selected as most
optimal, just as it was in (19); the tableau in (20) demonstrates as much:
(20)	 VRORV: várt.ma nom. acc. sg. neut. ‘track’
/vartma/
Dep-IO Max-IO
*CompOnset
*3µ
*CompCoda NoCoda
F a. vart.ma
*
*
**
b. var.tma
*!
*
c. var.tV.ma
*!
*
d. var.ma
*!
*
Again, given the general dispreference for segment insertion or deletion, as
well as for complex onsets, the winning candidate must be várt.ma in (20a.).13
necessarily means a violation of *3μ (assuming the latter militates against superheavy
syllables of three moras or more). The reverse does not hold, however—consider long
vowels in closed syllables—suggesting that while there is indeed some overlap between
the two constraint’s domains of influence, a distinction between superheavy syllables and
complex codas is worth maintaining. See also the discussion in n. 13.
13
On the other hand, incorporating the findings presented in the following chapter, in
which we identify evidence for the syllabification VR.ORV based on palatalization in the
development of Greek, we note that one could force selection of the candidate in (20b.)
rather straightforwardly with a ranking of Sonority-Sequencng over *ComplexCoda
over *ComplexOnset; this would be a situation in which the second constraint and

<!-- pdf-page: 102; source-page: 87 -->
Finally, with respect to the sequence VOORV, it is this case which provides crucial evidence of the importance of the sonority sequencing principle in the formal analysis. The constraint Sonority-Sequencing (2g.) has not played a role in the discussion thus far, as the constraint rankings which have been introduced have proven sufficient to account for the cases we have examined. Yet to maintain these rankings unchanged in the case of VOORV would result in the selection of an incorrect output, indicated by the pointing finger (the sad face marking the desired, but unselected, output): (21) VOORV: yók.tram nom. acc. sg. neut. ‘rope’14 /yoktram/ Dep-IO Max-IO *CompOnset *3µ *CompCoda NoCoda F a. yokt.ram * * ** L b. yok.tram *! * c. yok.tV.ram *! * d. yok.ram *! * Failure to incorporate Sonority-Sequencing into the constraint hierarchy results in the selection of the candidate in (21a.) as most optimal, given the established stronger dispreference for complex onsets than for complex codas or superheavy syllables. As such, we are compelled to introduce this constraint into the hierarchy, positioning it as in (22): (22) Sonority-Sequencing, Dep-IO, Max-IO » *ComplexOnset The three constraints Sonority-Sequencing, Dep-IO, and Max-IO must each outrank *ComplexOnset, so that complex onsets can be tolerated in the specific situation in which the alternative syllabifications would involve either a complex coda of flat sonority (a sonority plateau), or insertion or deletion of a segment. This is shown by the selection of the correct output in the revised tableau in (23) (low ranking constraints are omitted in the interests of space). *3µ would have to be differentiated, since a sequence such as V̄CCV would still need to be syllabified V̄C.CV (i.e. *3µ cannot outrank *ComplexOnset). We have chosen not to pursue this approach here, however, as we aim to develop as elegant an analysis as possible for the Vedic system in view of Vedic data. 14 Note that as suggested by this form we assume the proposed VCCCV syllabification patterns hold regardless of the length of the initial vowel.

<!-- pdf-page: 103; source-page: 88 -->
(23)	 VOORV: yók.tram nom. acc. sg. neut. ‘rope’
/yoktram/
Son-Seq
Dep-IO
Max-IO
*CompOnset
a. yokt.ram
*!
F b. yok.tram
 *
c. yok.tV.ram
*!
d. yok.ram
*!
The prioritization of strong sonority sequencing now makes candidate (23a.)
untenable, even though in general complex codas are better than complex
onsets: in other words, it is worse to violate this principle, than to surface with
a complex onset. The departure of candidate (23a.) from consideration allows
for the desired outcome, the selection of yók.tram in (23b.) as the winning
candidate.
### 3.1.4 VCCCCV Sequences
Intervocalic sequences of more than three consonants are relatively infrequent, due to the possible shapes of Vedic morphemes and the greater chance
of sonority sequencing violations. Still, the analysis as developed thus far is
predicted to yield appropriate syllabifications for any such sequences which do
occur. Abiding by sonority sequencing remains a priority, but there is greater
leeway for the surfacing of both complex onsets and complex codas, as the
example in (24) shows.
(24)	 VROORV: yung.dhvam 2 pl. mid. aor. ‘join’
/yung-dhvam/
Son-Seq Dep-IO Max-IO *CompOns
*3μ
*CompCoda
a. yungdh.vam
*!
*
*
F b. yung.dhvam
*
*
*
c. yung.dhV.vam
*!
d. yung.vam
*!
The optimal syllabification of the form yungdhvam features both a complex
onset and a complex coda, in the interest of satisfying undominated Sonority-Sequencing. And again, since the segments concerned are amenable to syllabification via strong sonority sequencing without any adjustment, neither
epenthesis nor deletion occurs, satisfying Dep-IO and Max-IO as well.

<!-- pdf-page: 104; source-page: 89 -->
### 3.1.5 Summary: General Vedic Constraint Ranking
Accounting for the general system of medial syllabification in Vedic has
required us to propose the overall constraint ranking in (25), with the crucial
subrankings listed in (25a.–o.); for each crucial ranking, we note the relevant
data that justifies it.
(25)	 Interim Constraint Ranking for Vedic Medial Syllabification
Sonority-Sequencing, Dep-IO, Max-IO, Onset »
*Complexonset »
*3μ, *ComplexCoda, NoCoda, Syllable-Contact
a. 	Sonority-Sequencing »
(yok.tram not †yokt.ram; cf. (23))

*Complexonset
b. Dep-IO » *Complexonset
(yok.tram not †yok.tV.ram; cf. (23))
c.	 Dep-IO » *3μ
(śās.ma.he not †śā.sV.ma.he; cf. (16))
d.	Dep-IO » *ComplexCoda
(chant.si not †chan.tV.si; cf. (19))
e.	 Dep-IO » NoCoda
(pa.vit.rais not †pa.vi.tV.rais; cf. (6))
f.	 Dep-IO » Syllable-Contact	 (pa.vit.rais not †pa.vi.tV.rais; cf. (6))
g. 	Max-IO » *Complexonset
(yok.tram not †yok.ram; cf. (23))
h.	Max-IO » *3μ
(śās.ma.he not †śā.ma.he; cf. (16))
i.	 Max-IO » *ComplexCoda
(chant.si not †chan.si; cf. (19))
j.	 Max-IO » NoCoda
(pa.vit.rais not †pa.vi.rais; cf. (6))
k.	 Max-IO » Syllable-Contact
(pa.vit.rais not †pa.vi.rais; cf. (6))
l.	 *Complexonset » *3μ
(śās.ma.he not †śā.sma.he; cf. (16))
m.	*Complexonset » *ComplexCoda	 (várt.ma not †vár.tma; cf. (20))
n.	*Complexonset » NoCoda
(pa.vit.rais not †pa.vi.trais; cf. (6))
o.	 *Complexonset »
(pa.vit.rais not †pa.vi.trais; cf. (6))

Syllable-Contact Generally speaking, it is worse in Vedic to have a complex onset, as opposed to a superheavy syllable, coda consonant, or syllable contact violation; but it is still worse to feature a sonority sequencing violation or epenthesis or deletion of a segment. We have also seen that the different strategies observed in the satisfaction of the bimoraic size requirement holding for certain aorist and intensive stems follow directly from the general syllabification patterns captured by the ranking in (25). When incorporated into this ranking, the subranking in (26), repeated from (10) above, prioritizes heterosyllabification of medial consonants over vowel lengthening as a way to achieve a bimoraic syllable, when either option is possible given the input.

<!-- pdf-page: 105; source-page: 90 -->
(26) [Ci]2μAor, [CV[Ci]2μ]Intens » Dep-μ-IO When the verb root begins with only a single consonant, however, lengthening of i is tolerated. To summarize our findings up until this point, though complex onsets and superheavy syllables are marked structures in Vedic, in general they can and do still surface, given the appropriate conditions. In the next section we examine—and seek to account for—how these structures fare in the morphological subdomain of the perfect conjugation.
## 3.2 Syllabification in the Vedic Perfect
So far we have developed an account of the general process of medial syllabification in Vedic. This process may disfavor complex onsets and superheavy syllables, but when no reasonable syllabification exists by which they could be avoided (neither epenthesis nor deletion being an option), they do surface. Yet as we have seen, such tolerance, however limited, does not hold for forms of the perfect. In the perfect epenthesis of i occurs either to resolve a superheavy syllable, or to break up a complex onset, or simply to render syllabifiable an otherwise unsyllabifiable sequence of segments. Given this starkly different treatment, where a phonological process is conditioned by the morphological identity of the form it occurs in, we must now equip our analysis with the means of accounting for the exceptional behavior of perfect union vowel epenthesis. In this section we seek to integrate the idiosyncratic syllabification patterns of the perfect conjugation within the larger account of Vedic medial syllabification we have constructed. We begin in 4.1 by first clarifying the limits of the analysis as it stands for treating the perfect data, while in 4.2 we use the approach of constraint indexation (Pater 2006, 2009) to incorporate the perfect system within the general analysis.
### 3.2.1 The Limitations of the General Analysis
The analysis of Vedic medial syllabification in its current form is largely incompatible with the perfect data, as we will see below, given the much stronger dispreference shown in the perfect domain for superheavy syllables and complex onsets. Accounting for this dispreference, and the associated appearance of the perfect union vowel i, will require a means of instantiating morphological conditioning within the constraint ranking; we will employ constraint indexation to serve this function.

<!-- pdf-page: 106; source-page: 91 -->
To be sure, though, there are a number of perfect forms for which the established analysis, as captured by the ranking in (25), already makes the correct
predictions—specifically, those forms in which perfect union vowel epenthesis does not occur. The tableaux in (27)–(28), which make use of the established ranking as is, demonstrate as much. Each treats a slightly different case;
note that only a selection of relevant constraints from the hierarchy is included
in each one.
(27)	 V̄CV: ā.sa 1 sg. perf. act. ind. ‘be’
/ās-a/15
Dep-IO
Max-IO
*3µ
NoCoda
a.
ās.a
*!
*
F b. ā.sa
c.
ā.sV.a
*!
d.
ā.a
*!
(28)	 VC.CV: yu.yuj.ma 1 pl. perf. act. ind. ‘yoke’
/yu-yuj-ma/
Dep-IO
Max-IO
*CompOns
NoCoda
F a.
yu.yuj.ma

*
b.
yu.yu.jma

*!
c.
yu.yu.ji.ma
*!

d.
yu.yu.ma
*!
(29)	 VC.CVC: pap.túr 3 pl. perf. act. ind. ‘fall’
/pa-pt-ur/
Son-Seq
Dep-IO
Max-IO
*CompOns
NoCoda
F a.
pap.tur

*
b.
pa.ptur
*!
*
c.
pa.pi.tur
*!

d.
pa.tur
*!
In the tableau in (27), the winning candidate in (27b.) violates none of the constraints; as is the general case in Vedic, a single intervocalic consonant is best
treated as the onset of the syllable headed by a following vowel. The inputs in
both (28) and (29) feature an intervocalic sequence of two consonants (stem-final + ending-initial in (28), both stem-final in (29)); this sequence, again as
15
Given the scope of this study, we abstract away from the evaluation and selection of optimal perfect stem forms, and assume their presence already in the input.

<!-- pdf-page: 107; source-page: 92 -->
per general Vedic, is heterosyllabified in the optimal outputs in a., rather than
treated as a complex onset (as in the candidates in b.), broken up by epenthesis (as in the candidates in c.), or simplified by deletion (as in the candidates
in d.). The distinction between these two cases lies in the role of Sonority-Sequencing in their evaluation; in (28) this constraint plays no role, as all
candidates abide by it, while in (29) it serves to eliminate the complex onset
candidate, as the sonority plateau exhibited by the sequence .pt- is disfavored.
On the other hand, the analysis as it has been developed thus far is unable
to account for any situation in which the perfect union vowel i actually does
occur. Recall that we analyzed the insertion of this vowel as a means of avoiding superheavy syllables and complex onsets, but also of allowing for otherwise
unsyllabifiable sequences of consonants to be assigned licit syllable structure.
Concerning the latter function, permitting the syllabification of forms containing one of the consonant sequences given in (18b.–c.) above, VOOOV, VOROV,
VORRV, or VRRRV, in this case the ranking in its current form is unable to converge on a single most optimal output. We see as much in the tableaux for the
perfect forms in (30)–(33):
(30)	 VOOOV: va.vák.ṣi.tha 2 sg. perf. act. ind. ‘increase’
/va-vakṣ-tha/
Son-Seq
Dep-IO
Max-IO
*CompOns
*3µ
NoCoda
a. vavakṣ.tha
*
*!
**
b. vavak.ṣtha
*
*!
*
F c. vavak.ṣi.tha
*
*
F d. vavak.tha
*
*
(31)	 VOROV: jaj.ñi.ṣé
2 sg. perf. mid. ind. ‘beget’
/ja-jñ-ṣe/
Son-Seq
Dep-IO Max-IO *CompOns
*3µ
NoCoda
a. jajñ.ṣe
*
*!
**
b. jaj.ñṣe
*
*!
*
F c. jaj.ñi.ṣe
*
*
F d. jaj.ṣe
*
*
(32)	 VORRV: jag.mi.ré
3 pl. perf. mid. ind. ‘go’
/ja-gm-re/
Son-Seq Dep-IO Max-IO *CompOns *3µ NoCoda
a. jagm.re
*
*!
**
b. jag.mre
*
*!
*
F c. jag.mi.re
*
*
F d. jag.re
*
*

<!-- pdf-page: 108; source-page: 93 -->
(33)	 VRRRV: da.dhan.vi.ré 3 pl. perf. mid. ind. ‘run’
/da-dhanv-re/
Son-Seq Dep-IO Max-IO *CompOns *3µ NoCoda
a. da.dhanv.re
*
*!
**
b. da.dhan.vre
*
*!
*
F c. da.dhan.vi.re
*
*
F d. da.dhan.re
*
*
In these tableaux, since the faithfulness constraints Dep-IO and Max-IO have
not been shown to require crucial ranking with respect to each other, deletion and epenthesis are equally favored as a repair mechanism for sequences
with poor sonority profiles; thus the candidates in c.–d. fare best in the evaluation, the alternatives containing either a complex onset (b. candidates)
or superheavy syllable (a. candidates), which happen to violate Sonority-Sequencing. However, in the perfect domain epenthesis of i is preferred over
deletion in this role.16
In fact the desired results can be obtained with a simple adjustment to the
constraint ranking, as in (34):
(34)	 Max-IO » Dep-IO
With this ranking in place, deletion will be more strongly disfavored than
epenthesis as a means of creating syllabifiable sequences. We show how this
ranking works with a revised version of the tableau in (30):
(35)	 VOOOV: va.vák.ṣi.tha 2 sg. perf. act. ind. ‘increase’
/va-vakṣ-tha/
Son-Seq Max-IO Dep-IO *CompOns *3µ NoCoda
a. vavakṣ.tha
*!
*
**
b. vavak.ṣtha
*!
*!
*
F c. vavak.ṣi.tha
*
*
d. vavak.tha
*!
*
16
As noted in the previous chapter (n. 63), it is apparently also favored over vocalization,
at least of ñ (†jajaṣe (← jajñ̥ṣe)) and u (†dadhanure); but cf. cakṛma 1 pl. act. ind. ‘make’
(†cakrima).

<!-- pdf-page: 109; source-page: 94 -->
With Dep-IO demoted in the hierarchy, the epenthesis candidate in (35c.)
fares best among the four options, as it contains no violations of undominated
Sonority-Sequencing or Max-IO.17
As for the other function of the perfect union vowel i, the avoidance of superheavy syllables and complex onsets, this role is also not readily accounted for
given the general system, nor can it be made such with a simple reranking of
constraints. Indeed superheavy syllables and complex onsets are predicted to
be perfectly acceptable, as demonstrated by the following pairs of tableaux,
each of which features a perfect form compared against a non-perfect form
of similar shape (again, the sad face is used to indicate the desired winner,
unselected given the ranking). In each case we limit the focus to the crucial
ranking of Max-IO over Dep-IO (as in (34)), over the most relevant markedness constraint(s); furthermore, output candidates that would violate undominated Sonority-Sequencing (which militates against flat sonority profiles
in complex syllable margins) are not included for consideration.
(36)	 V̄C. Superheavy Syllables
a. Non-perfect: śās.ma.he 1 pl. pres. mid. ind. ‘order’
/śās-mahe/
Max-IO
Dep-IO
*ComplexOnset
*3µ
F i. śās.ma.he
*
ii. śā.sma.he
*!
iii. śā.sV.ma.he
*!
iv. śā.ma.he
*!
b. Perfect: da.dā.śi.ma 1 pl. perf. act. ind. ‘wait on’
/da-dāś-ma/
Max-IO
Dep-IO
*ComplexOnset
*3µ
F
i. da.dāś.ma
*
ii. da.dā.śma
*!
L iii. da.dā.śi.ma
*!
iv. da.dā.ma
*!
17
Note this ranking could potentially pose a problem for interconsonantal s deletion
(see 2.2.3 in the previous chapter), in which deletion is clearly favored over epenthesis
as means of syllabifying triconsonantal sequences; this issue requires some additional
consideration, but may rest on singling out s as idiosyncratic.

<!-- pdf-page: 110; source-page: 95 -->
(37)	 VCC. Superheavy Syllables
a. Non-perfect VROOV: chant.si 2 sg. pres. act. ind. ‘seem’
/chant-si/
Max-IO
Dep-IO
*3µ
*ComplexCoda
F
i. chant.si
*
*
ii. chan.tV.si
*!
iii. chan.si
*!
b. Perfect VROOV: ta.tar.di.tha 2 sg. perf. act. ind. ‘split’
/ta-tard-tha/
Max-IO
Dep-IO
*3µ
*ComplexCoda
F
i. ta.tard.tha
*
*
L ii. ta.tar.di.tha
*!
iii. ta.tar.tha
*!
c. Non-perfect VRORV: várt.ma nom. acc. sg. ‘track’
/vartma/
Max-IO
Dep-IO *CompOnset
*3µ
*CompCoda
F
i. vart.ma
*
*
ii. var.tma
*!
iii. var.tV.ma
*!
iv. var.ma
*!
d. Perfect VRORV: va.van.di.ma 1 pl. perf. act. ind. ‘praise’
/va-vand-ma/
Max-IO Dep-IO *CompOnset *3µ *CompCoda
F
i. va.vand.ma
*
*
ii. va.van.dma
*!
L iii. va.van.di.ma
*!
iv. va.van.ma
*!
(38)	 .CCV Complex Onsets
a. Non-perfect: yók.tram nom. acc. sg. neut. ‘rope’
/yoktram/
Max-IO
Dep-IO
*Complexonset
F
i. yok.tram
*
ii. yok.tV.ram
*!
iii. yok.ram
*!

<!-- pdf-page: 111; source-page: 96 -->
b. Perfect: pap.ti.ma 1 pl. perf. act. ind. ‘fall’
/pa-pt-ma/
Max-IO
Dep-IO
*Complexonset
F
i. pap.tma
*
L ii. pap.ti.ma
*!
iii. pap.ma
*!
Operating with the constraint ranking in its current form (as in (25), with the
adjustment in (34)), we observe superheavy syllables surfacing in the undesired
optimal outputs †da.dāś.ma, †ta.tard.tha, and †va.vand.ma in (36b.) and (37b.,
d.), and a complex onset surfacing in the undesired optimal output †pap.tma in
(38b.); in every case epenthesis or deletion would be worse options.
In view of these unsatisfying results, we find that we are faced with a ranking paradox: one set of forms in the system suggest one constraint ranking,
while another set of forms suggests the very opposite ranking. In (36)–(38),
non-perfect forms argue for the dominance of Dep-IO over constraints militating against superheavy syllables and complex onsets, while perfect forms
argue for the opposite relationship. As we will show in the next subsection, a
paradox like this can be overcome by appeal to frameworks concerned with
morphologically-conditioned phonology; the one we will make use of is constraint indexation.
### 3.2.2 Constraint Indexation and the Exceptionality of the Perfect
#### 3.2.2.1 Overview of the Framework
Constraint indexation, as developed by Pater (2006, 2009), is a formal approach to morphology-sensitive phonology in Optimality Theory. It involves the introduction of lexically-specified markedness and faithfulness constraints, the satisfaction of which yields the results of morphologically-conditioned phonological processes. Our discussion here is concerned with the application of constraint indexation to the Vedic data; a more elaborated discussion, focusing on the implications the Vedic data hold for this framework, can be found in Cooper 2012, Cooper 2013a, and in particular Cooper 2013c.18 We begin by introducing the general schema of an indexed markedness constraint, which according to Pater (2009: 133) is as follows: 18 In addition, evaluation of two other approaches to exceptionality, cophonologies (Anttila 2002, 2009, Inkelas and Zoll 2007) and allomorphy subcategorization (Paster 2005, 2006), both of which prove problematic for the Vedic data, can be found in Cooper 2012. Assessment of a fourth approach, involving Harmonic Serialism (McCarthy 2008, Wolf 2008), is a goal of future work on this issue.

<!-- pdf-page: 112; source-page: 97 -->
(39)	 *XL
Assign a violation mark to any instance of X that contains a phonological
exponent of a morpheme specified as L.
Pater furthermore states: “This formulation serves as a locality convention for
indexed constraints: they apply if and only if the locus of violation contains
some portion of the indexed morpheme” (133).
As an example of a phenomenon involving lexically-conditioned markedness, consider the allomorphy involved in the sequence /a+i/ in Finnish:
sequences of [ai] arising through the addition of the past tense marker /-i-/L to
a-final stems are disfavored by the associated indexed constraint *[ai]L, while
morpheme-internal sequences of [ai] are disfavored by a more general constraint *[ai]. The resolution of these sequences is shown in (40) (adapted from
Pater 2009: 134; note that the constraint labeled ‘Ident’ militates against any
alteration of segments from their associated input form).
(40)
/taitta-iL/ ‘break (past)’
*[ai]L
Max-IO
Ident
*[ai]
a.
taittai
*!
**
F b.
taitti
*
*
F c.
taittoi
*
*
d.
titti
**!
e.
toitti
**!
As can be seen, high-ranking *[ai]L forces /a+i/ sequences to be resolved
through either vowel deletion, as in (40b.), or mutation, as in (40c.).
Crucially, however, morpheme-internal [ai] is unaffected, as in (40d.–e.),
since the general constraint against this sequence is the lowest-ranked in
the hierarchy.
#### 3.2.2.2 Developing and Deploying the Analysis
Turning to the situation in the Vedic perfect, we see that there are a number of issues we need to focus on in applying the constraint indexation framework: first, which morphological unit, perfect stem or ending, requires indexation; second, the identity of the indexed constraints to be proposed; and lastly, the position in the constraint ranking the indexed constraints should occupy. Once we have dealt with these, we can proceed to show how the analysis accounts for the perfect data. With respect to which morpheme, stem or ending, ought to be co-indexed with the variant constraints, the issue is perhaps obscured by the fact that epenthetic i occurs at the morpheme juncture: as we have analyzed it

<!-- pdf-page: 113; source-page: 98 -->
synchronically, a non-original segment is inserted, and not within the bounds of any morpheme, but rather at the juncture between stem and ending: [dadāś]iperf[ma] versus [dadāś]i[ma]perf. As such, we note that we are dealing with a case to be distinguished from any considered by Pater, where segments undergoing change are already present in underlying structure. Yet, it must be the perfect endings that are indexed. As already discussed in the previous chapter (2.1.1.2., 2.3.1), the perfect stem is a derived structure created by prefixed reduplication of the verbal root, and is as such unamenable to lexical indexation. Even if we were to posit a perfect stem template, capable of indexation, a bigger concern remains: namely, that indexing the stem would incorrectly predict i-epenthesis throughout the perfect, when it does not occur in perfect forms such as the following: (41) a. /mu-mok-tu/ → mu.mok.tu 3 sg. perf. act. impv. ‘release’ (†mu.mo.ki.tu) b. /cā-skambh-a/ → cās.kám.bha 3 sg. perf. act. ind. ‘prop’ (†cā.si.kám.bha) Epenthesis occurs only at the morpheme juncture, as suggested by (41b.), and only with certain endings, as suggested by (41a.), in which the ending is the generally-distributed imperative -tu. Thus it appears simplest to co-index the perfect endings with the indexed constraints we will introduce. As for the identity of these indexed constraint(s), following Pater’s schema in (39) for an indexed markedness constraint, we introduce three variants on the already established constraints *3μ, *ComplexOnset, and *ComplexCoda, linked exclusively to the perfect paradigm, and defined in (42): (42) Indexed Markedness Constraints for Vedic Perfect Syllable Structure a. *ComplexOnset-L Assign a violation mark to any instance of a complex onset that contains a phonological exponent of a morpheme specified as L. b. *3μL Assign a violation mark to any instance of a trimoraic (superheavy) syllable that contains a phonological exponent of a morpheme specified as L. c. *ComplexCoda-L Assign a violation mark to any instance of a complex coda that contains a phonological exponent of a morpheme specified as L.

<!-- pdf-page: 114; source-page: 99 -->
These constraints have been defined in accordance with (39), but we note that this creates a problem given Pater’s stated conception of locality. For all three of the indexed constraints we have proposed, we can replace “a morpheme specified as L” with “an ending of the perfect tense,” as it is only this set of morphemes which we have identified for indexation for the reasons given above (as opposed to the perfect stem). While the condition that the structure penalized by the constraint of shape *XL must contain a phonological exponent of the perfect ending is satisfied in the case of *ComplexOnset-L, since the second member of a disfavored complex onset will be the initial consonant of the ending (cf. pap.ti.ma over †pap.tma in (38b.)), this condition is not met in cases involving *3μL (cf. da.dā.śi.ma over †da.dāś.ma in (36b.)) and/or *ComplexCoda-L (cf. va.van.di.ma over †va.vand.ma in (37d.)). In the relevant forms the perfect union vowel resolves superheavy syllables and/or complex codas, but while the C-initial ending crucially creates the context for the disfavored (input) structure, it is itself not part of, but rather adjacent to, it: (43) da dāś-maPerf → dadāśima

3μ Indeed, based on the evidence, the perfect ending can never itself, or any part of it, be included in a structure that violates the constraints *3μ and *ComplexCoda (indexed variants or otherwise) by virtue of its shape and position in the word. Thus the Vedic data, in which indexed C-initial perfect endings create the environment for, but are not actually part of, disfavored superheavy syllables, suggest the need to distinguish between two different factors in morphologically-conditioned phonological processes: phonological environment and phonological exponence. Within a constraint indexation framework, we must determine the status of the two morphemes involved—one indexed, one adjacent—with respect to each criterion: (44) Two Factors in Morphologically-Conditioned Phonology a. Phonological Exponence: Is there some portion of the (indexed, adjacent) morpheme contained within the disfavored structure? b. Phonological Environment: Does the shape of the (indexed, adjacent) morpheme create an environment in which the disfavored structure can surface? Phonological exponence entails phonological environment—if a morpheme contributes phonological material to a disfavored structure, it is by definition

<!-- pdf-page: 115; source-page: 100 -->
providing context for that structure to surface—though the converse does not hold. We propose to replace the requirement of phonological exponence with one of phonological environment; as such we redefine Pater’s indexed markedness constraint schema as follows: (45) *XL Assign a violation mark to any instance of X for which a morpheme specified as L provides phonological context. Specifically for Vedic, the indexed markedness constraints are redefined as in (46): (46) Indexed Markedness Constraints for Vedic Perfect Syllable Structure (Revised) a. *3μL Assign a violation mark to any instance of a trimoraic (superheavy) syllable for which a morpheme specified as L (i.e. a perfect ending) provides phonological context. b. *ComplexOnset-L Assign a violation mark to any instance of a complex onset for which a morpheme specified as L (i.e. a perfect ending) provides phonological context. c. *ComplexCoda-L Assign a violation mark to any instance of a complex coda for which a morpheme specified as L (i.e. a perfect ending) provides phonological context. In order to satisfy the locality condition, the indexed morpheme must minimally contribute to the environment conditioning the surfacing of the disfavored structure. This may involve providing actual phonological material for that structure (as in the case of complex onsets), but not necessarily so (as in the case of superheavy syllables and/or complex codas). While the adjustment we have made here in consideration of the Vedic data remains to be more fully evaluated from a cross-linguistic perspective, nevertheless we maintain that it is the least problematic means of accounting for our conception of perfect union vowel epenthesis using constraint indexation.19 19 In Cooper 2012 we show how the locality issue cannot be resolved by using indexed faithfulness constraints (Fukazawa 1999, Itô and Mester 1999, 2001), Alignment constraints

<!-- pdf-page: 116; source-page: 101 -->
Operating with the constraints in (46), we propose the following revision to the ranking in (25) (with the adjustment given in (34)), which covers both general medial syllabification in Vedic, as well as the idiosyncratic patterns observed in the perfect: (47) Sonority-Sequencing, *ComplexOnset-L, *3μL, *ComplexCoda-L, Max-IO, Onset » Dep-IO » *Complexonset » *3μ, *ComplexCoda, NoCoda, Syllable-Contact The indexed markedness constraints *ComplexOnset-L, *3μL, and *ComplexCoda-L must outrank Dep-IO, which in turn must continue to outrank their associated general versions, as established for general Vedic syllabification. Given these relationships, epenthesis is now privileged in the perfect but continues to be disfavored elsewhere word-medially.20 The tableaux in (48)–(50) illustrate the crucial ranking in (47). For the sake of comparison, evaluation of both perfect and similarly shaped non-perfect forms is again considered (cf. the tableaux in (36)–(38) above); as above, (McCarthy and Prince 1993a), or anti-Alignment constraints (Buckley 1998, Downing 1998); similarly, we also claim that broadening the local domain to operate over both the indexed morpheme itself, as well as any segment(s) that may be immediately adjacent to it (an approach implicit in Padgett’s [2009] tentative analysis of depalatalization in Russian), would have potentially unwelcome typological implications. More recently, in Cooper 2013b we also evaluate (negatively) approaches using local constraint conjunction (Łubowicz 2002) or assuming the perfect union vowel to be latent (after Zoll 1996; see n. 66 in the previous chapter). Further, as already indicated in n. 18, other approaches to morphologically-conditioned phonology have issues of their own when it comes to analyzing the Vedic data. 20 We also understand the constraint Contiguity (McCarthy and Prince 1995), which militates against disruption of morpheme-internal structure (‘No intrusion’), to have a role in the analysis of the Vedic perfect, to capture the fact that it is the morpheme juncture that serves as insertion point for i (e.g. jag.mi.re over †ja.gim.re); we set aside for now its explicit integration into the constraint ranking. Recall that this aspect of perfect union vowel epenthesis is comparable to epenthesis in Chukchi CCC sequences (Kenstowicz 1979, 1994), examined in 2.3.5 in the previous chapter. We note further that, as Contiguity is interested strictly in the linear order of a string of segments, and not any overarching prosodic structure, this may raise the question again of whether the distribution of the perfect union vowel can appropriately be captured wholly in these terms. As we argued in the previous chapter (2.3.3), given the relevance of weight, as demonstrated by the inclusion of sequences V̅CCV in the phenomenon, such an analysis would arguably be less elegant by comparison.

<!-- pdf-page: 117; source-page: 102 -->
output candidates that would violate Sonority-Sequencing are not
included and only a relevant selection of constraints is explicitly employed
(but due to space constraints, indexed and general *ComplexCoda are
excluded from the tableaux in (49c.–d.)).
(48)	 V̄C. Superheavy Syllables Revisited
a. Non-perfect: śās.ma.he 1 pl. pres. mid. ind. ‘order’
/śās-mahe/
*Compons-l *3µL Max Dep
*Compons
*3µ
F
i. śās.ma.he
*
ii. śā.sma.he
*!
ii. śā.sV.ma.he
*!
iii. śā.ma.he
*!
b. Perfect: da.da.śi.ma 1 pl. perf. act. ind. ‘wait on’
/da-dāś-mal/
*Compons-l *3µL Max Dep
*Compons *3µ
i. da.dāś.ma
*!
*
ii. da.dā.śma
*!
*
F ii. da.dāśi.ma
*
iii. da.dā.ma
*!
(49)	 VCC. Superheavy Syllables Revisited
a. Non-perfect VROOV: chant.si 2 sg. pres. act. ind. ‘seem’
/chant-si/
*3µL *CompCoda-l Max Dep
*3µ
*CompCoda
F
i. chant.si
*
*
ii. chan.tV.si
*!
iii. chan.si
*!
b.	 Perfect VROOV: ta.tar.di.tha 2 sg. perf. act. ind. ‘split’
/ta-tard-thal/
*3µL *CompCoda-l Max Dep *3µ *CompCoda
i. ta.tard.tha
*!
*
*
*
F ii. ta.tar.di.tha
*
iii. ta.tar.tha
*!

<!-- pdf-page: 118; source-page: 103 -->
c. Non-perfect VRORV: várt.ma nom. acc. sg. ‘track’
/vartma/
*Compons-L
*3µL
Max
Dep
*Compons
*3µ
F
i. vart.ma
*
ii. var.tma
*!
iii. var.tV.ma
*!
iv. var.ma
*!
d. Perfect VRORV: va.van.di.ma 1 pl. perf. act. ind. ‘praise’
/va-vand-mal/
*Compons-L *3µL Max Dep *Compons *3µ
i. va.vand.ma
*!
*
ii. va.van.dma
 *!
*
F iii. va.van.di.ma
 *
iv. va.van.ma
*!
(50)	 .CCV Complex Onsets Revisited
a. Non-perfect: yók.tram nom. acc. sg. neut. ‘rope’
/yoktram/
*Compons-L
Max-IO
Dep-IO
*Compons
F
i. yok.tram
*
ii. yok.tV.ram
*!
iii. yok.ram
*!
b. Perfect: pa.pti.ma 1 pl. perf. act. ind. ‘fall’
/pa-pt-maL/
*Compons-L
Max-IO
Dep-IO
*Compons
i. pap.tma
*!
*
F ii. pap.ti.ma
*
iii. pap.ma
*!
In each of the perfect conjugation tableaux, we observe that neither complex
onsets nor superheavy syllables and complex codas are licit syllable structures;
the candidates which feature them are eliminated from consideration due to
the relevant high-ranking indexed markedness constraints. We also can confirm in view of these evaluations that while general *Complexonset must
outank general *3µ, the indexed versions of these constraints need not exist in
a crucial ranking relationship.

<!-- pdf-page: 119; source-page: 104 -->
In addition to accounting for epenthesis of the perfect union vowel, we can
also see how the analysis handles forms in which epenthesis does not occur. The
first case of non-epenthesis concerns forms featuring a medial sequence only
one or two consonants long, because the stem ends in a single consonant and/
or the perfect ending is vowel-initial. For a sample form such as yuyujma,
we saw above in (28) that the general analysis could account for this form;
now we see in the tableau in (51) that the updated ranking is no different in
this regard.
(51)	 VC.CV: yu.yuj.ma 1 pl. perf. act. ind. ‘yoke’
/yu-yuj-mal/
*Compons-l
Max
Dep
*CompOns
NoCoda
F a. yu.yuj.ma
*
b. yu.yu.jma
*!
*
c. yu.yu.ji.ma
*!
d. yu.yu.ma
*!
With the indexed constraints, the only difference in the way the evaluation works is that the candidate in (51b.) violates not only lower-ranked
*ComplexOnset, but higher-ranked *Complexonset-l as well; this has no
effect on the selection of the desired winner, however.
Likewise, perfect forms which feature otherwise unsyllabifiable sequences
of consonants also find successful analysis with the proposed ranking. Consider
the tableau in (52), for the form vavákṣitha (and cf. the one for the same form
in (35) above):
(52)	 VOOOV: va.vák.ṣi.tha 2 sg. perf. act. ind. ‘increase’
/va-vakṣ-thal/
Son-Seq
*Compons-l
*3µL
Max-IO
Dep-IO
a. vavakṣ.tha
*!
*
b. vavak.ṣtha
*!
*
F c. vavak.ṣi.tha
*
d. vavak.tha
*!
As can be seen, epenthesis continues to be the most optimal means of rendering the sequences in question syllabifiable; and even without the violations of high-ranking Sonority-Sequencing incurred by the candidates in

<!-- pdf-page: 120; source-page: 105 -->
(52a.–b.), this pair would be disfavored due to their violation of one of the two indexed markedness constraints.21 Given the position of Sonority-Sequencing in the ranking, it is worth noting that for the cases like va.vák.ṣi.tha—forms containing VOOOV, VORRV, VOROV, or VRRRV—we might be tempted to consider i-epenthesis an aspect of general Vedic syllabification, rather than a part of the idiosyncratic perfect phenomenon. Such forms differ from dadāśima, paptima, or vavandima, where inserted i breaks up a superheavy syllable or complex onset, in that they lack analogous forms outside of the perfect, in which epenthesis does not occur (cf. śāsmahe, yóktram, and vártma, respectively). We have no indication, then, that the sequences VOOOV, VORRV, VOROV, or VRRRV are tolerated in Vedic (as already noted above in 3.1.3), and this is a point arguably in favor of classifying the insertion of i in such cases as a more general phenomenon: under this view, epenthesis would be predicted to occur in any and all cases where syllabification of the input sequence would violate sonority sequencing. But in fact, we see that such a position is difficult to maintain, since, as we saw in the previous chapter (2.2.3), when the intermediate obstruent in a sequence VOOOV is s, it is actually avoided by the deletion of this consonant (as in ábhakta ← /á-bhak-s-ta/ 3 sg. aor. mid. ‘share’; cf. ábhutsmahi 1 pl. aor. mid. ‘wake’). So while we can certainly maintain that, regardless of the domain (perfect or non-perfect), triconsonantal sequences of this type are disfavored, such sequences could not be claimed to be universally subject to a uniform phenomenon of epenthesis. Indeed it remains a topic of future work in this area to expand the analysis to integrate the facts of s loss, and consider its relationship to perfect i insertion.
## 3.3 Conclusion
In this chapter we have developed an Optimality-Theoretic analysis of word-internal syllabification in Vedic, which accounts for both the general state-ofaffairs as well as the idiosyncratic behavior of the perfect. Vedic in general is characterized by across-the-board heterosyllabification of word-medial biconsonantal sequences. Simplex onsets are preferred, and complex onsets surface 21 Again, the high-ranking (if not undominated) position of Sonority-Sequencing is justified in view of general Vedic yóktram, which we have argued is syllabified yók.tram over †yókt.ram (cf. the tableau in (23)).

<!-- pdf-page: 121; source-page: 106 -->
only when a complex coda is untenable due to strict sonority sequencing. In the perfect, though, dispreference for superheavy syllables (and complex onsets) is resolved through epenthesis of i. The final constraint hierarchy we propose here is presented in (53), accompanied by justifications for the crucial rankings beyond those given in (25) above, which were revealed as we extended the analysis to account for the perfect union vowel. (53) Final Constraint Ranking for Vedic Medial Syllabification Sonority-Sequencing, *ComplexOnset-L, *3μL, *ComplexCoda-L, Max-IO, Onset » Dep-IO » *Complexonset » *3μ, *ComplexCoda, NoCoda, Syllable-Contact a. *3μL » Dep-IO (da.dā.śi.ma not †da.dāś.ma; cf. (48b.)) b. *ComplexCoda-L » Dep-IO (ta.tar.di.tha not †ta.tard.tha; cf. (49b.)) c. *ComplexOnset-L » Dep-IO (pap.ti.ma not †pap.tma; cf. (50b.)) We resolved the mismatch between the general system and the perfect domain using constraint indexation: markedness constraints targeting complex onsets and superheavy syllables, specially indexed to the perfect endings, outrank the very faithfulness constraints whose otherwise undominated position permits such structures to occur outside of the perfect. Using constraint indexation to deal with the mismatch between Vedic perfect and non-perfect environments raises significant questions about the theory’s conception of locality. The nature of the data suggests the need to loosen the conception of the local domain such that the indexed morpheme is minimally required to contribute to phonological environment, rather than full exponence.

<!-- pdf-page: 122; source-page: 107 -->
