---
title: "Chapter 7. Previous Optimality-Theoretic Accounts of Sonorant Syllabicity"
author: "Adam I. Cooper"
date: "2015"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "cooper-2015-reconciling-ie-syllabification.pdf"
chunk: "Chapter 7"
pages: "169-183"
---
# Chapter 7. Previous Optimality-Theoretic Accounts of Sonorant Syllabicity
## 7.0 Introduction
To review, a satisfactory analysis of nucleus selection and sonorant vocalization in Proto-Indo-European must be able to generate the following patterns of segment syllabicity: (1) Generalizations about Syllabicity in Proto-Indo-European a. Obstruents are never syllabic. b. Non-high vowels are never glides, i.e., non-syllabic. c. Sonorants are syllabic when not adjacent to a syllabic segment. d. When a sequence of more than one sonorant is not adjacent to a syllabic segment, it is the right-hand one which is syllabic, regardless of its relative sonority vis-à-vis the preceding one. Before proceeding to develop our own approach to capturing these generalizations—our focus in the next chapter—we first take the opportunity in this chapter to present an assessment of two previous Optimality-Theoretic accounts, highlighting both their respective strengths and issues. In 7.1 we review the approach of Kobayashi (2004),1 while in 7.2 we review that of Keydana (2008 [2010]). In a summary evaluation in 7.3, we will ultimately argue that these analyses suffer from two deficiencies, which significantly affect the comprehensiveness of their scope: their primary, if not exclusive, focus on accounting for generalizations (1c.–d.), leaving those in (1a.–b.) formally unaccounted for; and their reliance on a dispreference for syllable codas, which can make undesirable predictions about certain data. In sum the absence of a comprehensive story will amply demonstrate that there is room, if not need, for a new approach. 1 Maintained in another recent approach to analyzing Proto-Indo-European syllabification in Optimality Theory, that of Byrd (2010).

<!-- pdf-page: 185; source-page: 170 -->
## 7.1 Kobayashi (2004)
As a prelude to his exploration of historical developments in the phonology of
Old Indo-Aryan consonants, Kobayashi (2004: 23–24) sets up an Optimality-Theoretic analysis of nucleus selection in Proto-Indo-European. His account
relies on the constraints in (2); the definitions are Kobayashi’s (with some
minor reformatting).
(2)	 Constraints for an Account of Proto-Indo-European Nucleus Selection
(Kobayashi 2004: 23)
a. Hnuc (Prince and Smolensky 1993 [2004]: 72): When there is more
than one segment which can become the nucleus of a syllable,
the nucleus is assigned to the one with the highest sonority. In the
case of PIE */k̑u̯nbhis/ inst.pl. ‘dog,’ this constraint requires *u̯ to
be the nucleus (> xk̑un-bhis); when, on the other hand, *n becomes
the nucleus (> *k̑u̯n̥-bhis), it is counted as a violation of this constraint.
b. AlignNuc: Align(Nucleus, R, σ, R): Align the right edge of a syllable
nucleus with the right edge of a syllable, i.e. minimize syllable codas.2
c. Onset: A segment to the left of a syllable nucleus is an onset; in
other words, diereses are not allowed. The candidate *k̑u.n̥.bhis (> Ved.
xśuabhis), in which both the adjoining sonorants become the nuclei of
two separate syllables to better satisfy AlignNuc, is ruled out by this
constraint.
The ranking of these constraints is given in (3), and Kobayashi’s sample tableau is reproduced (with some minor reformatting) in (4).
(3)	 Onset » AlignNuc » Hnuc
/k̑u̯n.bhis./
Onset
AlignNuc
Hnuc
a. k̑un.bhis.
*!
F b. k̑u̯n̥.bhis.
*
c. k̑u.n̥.bhis.
*!
(4)
2	 Note that to cooperate with the conception of syllable structure we maintain, ‘nucleus’
should be taken as a descriptive term for the primary, or leftmost, moraic segment in the
syllable. It is also the case that AlignNuc seems equivalent in its influence, if not its explicit
form, to the more commonly deployed NoCoda. Why this constraint is not used is not clear.

<!-- pdf-page: 186; source-page: 171 -->
Before assessing the predictions this analysis makes, both welcome and problematic, we first make a couple of comments. To begin with, we note that syllabification is included already in the input, with no further comment; its presence is unusual, if syllabification is to be conceived as predictable, and hence an outcome of the evaluation process.3 (The distinction between consonantal *u̯ and vocalic *i in the input is also interesting, but may be due simply to the focus of the evaluation on the first syllable over the second one.) That the assignment would not seem to influence the outcome raises additional questions concerning its justification. We note also that, as this tableau demonstrates, the constraint Onset need not technically dominate AlignNuc; in fact we cannot conceive of a scenario in which such a strict ranking must hold, i.e., a case in which a form containing both an onset and a coda will be evaluated more favorably than a candidate lacking an onset but not having a coda, purely on these grounds. Finally, only the first syllable is evaluated in Kobayashi’s original tableau, but one might also consider the permissibility of the second syllable .bhis., which, because of final s, violates AlignNuc. Indeed the issue of obstruent-final syllables in this analysis will be considered in more detail shortly. Kobayashi’s analysis is able to straightforwardly account for at least one of the ostensible exceptions noted by Schindler, the behavior of a word-initial sequence of two sonorants. Both segments in initial *u̯r-, *u̯l-, *u̯i̯-, *mr-, *ml-, *mn- are realized as consonants; it is not the case, as might be expected, that the first sonorant is syllabic. The consonantal outcome is generated by the analysis: /#RRV/ Onset AlignNuc Hnuc F a. .RRV (*) b. R̥.RV. *! (5) The candidate in (5a.) violates only Hnuc, but only if we assume the constraint would be violated by a relatively high sonority segment like *u̯ not being syllabic; meanwhile the candidate in (5b.) violates higher-ranking Onset, and so is less optimal. Of course we should point out that this account predicts that any word-initial sonorant + sonorant sequence should surface without vocalization, not simply those listed above. 3 We will return to the idea of input prosodic structure in Chapter 9, where it will play a role in the morphophonological analysis of Proto-Indo-European sonorant syllabicity we develop there.

<!-- pdf-page: 187; source-page: 172 -->
Without modification, Kobayashi’s account also makes a number of rather problematic predictions, of varying degrees of concern. For instance, while the analysis correctly selects vocalization of *r over *u̯ in a form like *peru̯r̥ (> Gk. πεῖραρ nom. acc. sg. ‘end, boundary’) it does so at the cost of forcing one syllabification in particular: /per-u̯r/ Onset AlignNuc Hnuc a. per.u̯r̥. *! * b. per.ur. *! F c. pe.ru̯r̥. * d. pe.rur. *! e. pe.ru.r̥. *! (6) The winning candidate in (6c.) features a complex onset, as opposed to the arguably next most plausible candidate, that in (6a.), with heterosyllabic coda *r + onset *u̯. As a complex onset would go against our expectations for the preferable syllabification—given all the evidence for heterosyllabification of medial consonants we considered in Chapter 2, and because it is arguably dispreferred by sonority sequencing in containing two sonorants in sequence (the first of which is not a labial)—we ultimately find this to be an undesirable outcome. In our own attempts at analysis, beginning in the following chapter, we will seek to select the output in (6a.) as most optimal. We return to the conflict in positing a drive to minimize codas as a means of generating right-hand vocalization of sonorants, while maintaining a heterosyllabic parse of consonants in the sequence VCCV, at the end of this chapter. In addition, there is also the fact that under this analysis a word-initial sonorant is predicted to be consonantal not only before another sonorant, but before an obstruent as well, to avoid a violation of Onset (note L indicates the desired, though unselected winner): /#ROV/ Onset AlignNuc Hnuc F a. .ROV. (*) L b. R̥.OV. *! (7) The candidate in (7a.) features a tautosyllabic pre-vocalic sonority reversal, and does not match the evidence of forms such as the weak aorist stem *n̥s- (> Gk. part. ἄσμενος) built to the root *nes- ‘get away’ (LIV 454–455; IEW 766–767), in which the sonorant is syllabic. If we wish the analysis to select (7b.) as the optimal output, we need to introduce the constraint Sonority-Sequencing into a dominant position in the ranking; this constraint would militate against

<!-- pdf-page: 188; source-page: 173 -->
the sonority reversal which candidate (7a.) features in the form of a complex onset of falling sonority (sonorant followed by obstruent), so as to incur no violations of Onset. Furthermore, for another of Schindler’s noted exceptions, the behavior of accusative singular marker *-m in acrostatic and proterokinetic *i-, *u-, and *r-stems, the analysis predicts that *m should syllabify over the stem-final sonorant: (8) /-i̯-m/ Onset AlignNuc Hnuc L a. -im. *! F b. -i̯m̥ . * That *m does not vocalize here, but is in fact consonantal, could conceivably be accounted for as (morpho)phonological idiosyncrasy; still, the lack of an explicit statement to such effect leaves the account less comprehensive than it could be.4 The final two predictions of Kobayashi’s analysis we consider here each concern the core notion that segments vocalize to minimize syllable codas. Problematically, there is no formal mechanism in the account which prevents an extension of this behavior to configurations beyond those containing sequences of sonorant consonants, leading the analysis to select some rather unusual output forms in some cases as most optimal. For one example of this effect, consider the tableau in (9), which features a full (non-high) vowel before a sonorant in the input */ph₂ter/, the vocative singular of ‘father’. (9) /ph₂ter/ Onset AlignNuc Hnuc F a. ph₂te̯r̥. * L b. ph₂ter. *! c. ph₂te.r̥. *! Because of the relatively low position of the constraint Hnuc, the analysis predicts that the liquid *r should vocalize, so as to avoid a violation of higher ranked AlignNuc; and because of highest ranked Onset, the mid vowel’s syllabicity is compromised, to avoid an onsetless syllable. We are thus left with the candidate in (9a.), an undesirable result. For another example of the problematic extension of right-hand vocalization, we turn to consideration of the tableau in (10), which features the familiar input */k̑u̯nbhis/; we focus here not 4 For further discussion of the status of *m, see 10.1.2 in Chapter 10.

<!-- pdf-page: 189; source-page: 174 -->
on the first syllable, but on the second, to exemplify the scenario we are concerned with. (10) /k̑u̯n-bhis/ Onset AlignNuc Hnuc F a. k̑u̯n̥.bhi̯s̥. * L b. k̑u̯n̥.bhis. *! c. k̑u̯n̥.bhi.s̥. *! As can be seen, in principle there is nothing formally encoded in the grammar (i.e. the constraint ranking) that can prevent syllabification of obstruents as in (10a.), in the interest of avoiding a coda and satisfying AlignNuc. Again, the constraint Hnuc, which must involve some awareness of the set of potentially syllabic segments in the language, and thus could potentially weigh in on the matter, is rendered inactive in the evaluation process by its low position in the ranking. In sum, while Kobayashi’s formal analysis of nucleus selection in Proto-Indo-European is so far as we have seen able to generate the right results for the vocalization of sonorants occurring in sequence (where the second one is syllabic, regardless of relative sonority)—the complex coda in *pe.ru̯r̥ (6) notwithstanding—because it is not adequately constrained when it comes to treating sequences featuring vowels and obstruents as well, it is in the end too limited in scope to be taken as a comprehensive view of the issue.
## 7.2 Keydana (2008 [2010])
Keydana’s exclusive focus in this paper is the issue of right-hand sonorant vocalization in Proto-Indo-European. He connects this phenomenon in sequences
like CRRC to the place of articulation of the sonorant in question: coronal
sonorants, he surmises, are disfavored in coda position in Proto-Indo-European,
hence CRR̥C over †CR̥RC, even if the first sonorant is greater in sonority. This
restriction is formalized into the constraint *R/C, defined in (11) along with the
other markedness constraints invoked for the Optimality-Theoretic analysis;
the faithfulness constraints are presented in (12). (Definitions are Keydana’s;
translations are our own.)
(11)	 Markedness Constraints for an Account of PIE Right-Hand Sonorant
Syllabicity (Keydana 2008 [2010]: 60)
a.	*R/C: Coronal sonorants are not licensed in the coda.
b. *(a ⊳ t / Mar): At syllable edge a is less preferred than . . . than t.
c. *(t ⊳ a / Peak): In the nucleus t is less preferred than . . . than a.

<!-- pdf-page: 190; source-page: 175 -->
(12)	 Faithfulness Constraints for an Account of PIE Right-Hand Sonorant
Syllabicity (Keydana 2008 [2010]: 61)
a. Parse(μ, Δ): Lexical material μ (features (F) or prosodic specification
of the segment) must be parsed in a slot of a structural domain Δ: No
deletion.
b. Fill(Δ, μ): A slot in a structural domain Δ must be filled with lexical
material μ: No epenthesis.
c. Linearity(μi, δ, ti): Between a segment μi and its trace ti there should
be no other segment δ. [No metathesis.]
Parse and Fill are essentially equivalent to Max-IO and Dep-IO, the basic
faithfulness constraints militating against deletion and insertion of phonological material, respectively. The constraint *(t ⊳ a / Peak) we take to be
equivalent to Kobayashi’s HNuc, that is, it encodes gradient sonority-driven
preferences for what can fill the nucleus position of the syllable, with segments
like t (i.e., obstruents) least preferred, and segments like a (i.e., non-high vowels) most preferred.5 The constraint *(a ⊳ t / Mar) operates in a similar way,
albeit for another domain within the syllable, its margins; the opposite set of
preferences hold for this position, with segments like t most preferred, and segments like a least preferred.6
The first ranking Keydana posits is given in (13); it is intended to generate
the correct result in the CRRC case. His sample tableau is reproduced (with
some reformatting) in (14).
(13)	 Ranking, First Pass
*R/C, Parse, Fill, Linearity » *(t ⊳ a / Peak)
(14)
/k̑unbh-/
*R/C
Parse
Fill
Linearity
*(t ⊳ a / Peak)
F a. k̑u̯n̥.bh*
b. k̑un.bh*!
c. k̑nu.bh*!
d. k̑u<n>.bh*!
e. k̑u.n .bh*!
5	 While t could more specifically refer to voiceless stops, and a could more specifically refer
to low vowels, such a degree of fine-grainedness in nucleus preferences is unwarranted
for Proto-Indo-European (but has been argued to be relevant in languages like Imdlawn
Tashlhiyt Berber; see Dell and Elmedlaoui 1985, 1988, et al., as well as the discussion of this
language in Chapter 10).
6	 In our own analysis of sonorant syllabicity, undertaken in the following chapter, we will see
fit to split these unitary constraints into families of constraints, each member of which targets a particular manner class.

<!-- pdf-page: 191; source-page: 176 -->
In the case of input /k̑unbh-/ (note the input high vowel; we will assume the associated glide *u̯ is underlying), high ranking *R/C disfavors the coronal nasal *n from occupying a coda position in the associated output syllable; hence elimination of the candidate in (14b.). The other three high-ranking constraints each serve to eliminate one additional candidate, for featuring either metathesis (as in (14c.)), segment loss (as in (14d.)), or segment insertion (as in (14e.)). Thus the most optimal syllabification involves vocalization of *n, as in candidate (14a.), despite the violation of *(t ⊳ a / Peak) it incurs due to the more sonorous *u̯ functioning as a consonant. Keydana explicitly seeks to differentiate cases such as this from those in which the coronal sonorant follows a non-high vowel; in this latter environment, the sonorant never vocalizes. The ranking in (15), which includes highlypositioned *(a ⊳ t / Mar), is introduced to account for this distinct outcome; Keydana’s example tableau, for the vocative singular of ‘father’ (cf. (9) above) is reproduced (again, with some minor reformatting) in (16). (15) Ranking, Second Pass

*(a ⊳ t / Mar) » *R/C, Parse, Fill, Linearity » *(t ⊳ a / Peak)
(16)
/ph₂ter/
*(a ⊳ t / Mar) *R/C Parse Fill Linearity *(t ⊳ a / Peak)
a. ph₂te̯r̥.
*!
F b. ph₂ter.
*
For an input such as /ph₂ter/, the preferred candidate in (16b.) satisfies *(a ⊳ t /
Mar), while violating *R/C; its competitor is eliminated due to its mirror-image
violation profile. Indeed Keydana’s approach arguably does one better than
Kobayashi’s in at least attempting to formally encode in the ranking gradient
preference for both syllabic peaks and margins, through the two constraints
*(t ⊳ a / Peak) and *(a ⊳ t / Mar), instead of introducing a single constraint,
Hnuc, to effectively negotiate the distribution of segments in both positions.
With respect to the predictions which Keydana’s analysis as developed
makes about the Proto-Indo-European system, we can identify both positives and negatives. One ostensibly positive result the analysis generates is
that, since rightmost contra-sonority vocalization applies only for coronals,
Schindler’s accusative *-m exceptions are not unusual, but rather find explanation squarely within the phonological domain:
(17)
/-i̯-m/
*R/C
Parse
Fill
Linearity
*(t ⊳ a / Peak)
F a. -im.
b. -i̯m̥ .
*!

<!-- pdf-page: 192; source-page: 177 -->
(Note here and below we will include glides in the input, as per the conception we will maintain in the next chapter, and unlike Keydana’s; this
does not effect the evaluation of his approach.) Because *m is not a coronal
sonorant, if it occupies coda position, it does not incur a violation of *R/C.
Thus the evaluation in (17) comes down to preferences for nuclear status,
and since glide *i̯ is more sonorous than nasal *m, the candidate in (17a.) is
the winner.
In fact, the analysis can account for the syllabification of all non-likemanner RR sequences in which the second sonorant is non-coronal (i.e., a
glide or *m)—evaluation simply comes down to the relatively lower-ranked
*(t ⊳ a / Peak). For glides, this constraint selects the vocalization RG̥, as shown
in (18):
(18)
/CRGC/
*R/C
Parse
Fill
Linearity
*(t ⊳ a / Peak)
F a. CRG̥.Cb. CR̥G.C*
c. CGR.C*!
d. CR<G>.C*!
e. CR.G .C*!
For *m, it selects the vocalization R̥m, as seen above in (17). The analysis also
explicitly accounts for the absence of vocalization in obstruents, again given
the constraint *(t ⊳ a / Peak):
(19)
/CRGC/
*R/C
Parse
Fill
Linearity
*(t ⊳ a / Peak)
F a. CR̥OC
b. CRO̥C
*!
A sonorant will always vocalize in preference to an obstruent, even if it precedes it, as any obstruent would make a worse syllable nucleus.
On the less positive side, the analysis predicts the syllabification *pe.ru̯r̥
(as opposed to *per.u̯r̥), with complex onset, the potential issue with which
we have noted above in our discussion of Kobayashi’s account. We take
high-ranking Onset into consideration here, a constraint which Keydana
acknowledges the influence of in cases like *k̑u.nes gen. sg. ‘dog’, but does
not explicitly include in his ranking for the sake of clarity (2008 [2010]: 61).
Clearly, though, its presence is required for cases like this, as the tableau in (20)
demonstrates:

<!-- pdf-page: 193; source-page: 178 -->
(20)
/per-u̯r/
Onset
*R/C
Parse
Fill
Linearity
*(t ⊳ a / Peak)
a. per.u̯r̥
*!
*
b. per.ur
*!
F c. pe.ru̯r̥
*!
d. pe.rur
*!
e. pe.ru.r̥
*!
High-ranking Onset militates against the syllabification †pe.ru.r̥ in (20e.),
which avoids a coronal sonorant coda at the cost of an onsetless syllable, and
violates no other constraints. Still, because of the constraint *R/C, the correct
selection of the sonorant that is vocalized comes at the cost of positing a syllable structure we hold to be disfavored.
Further, the analysis as developed is unable to make any prediction about
the syllabicity of glides following glides and *m following another nasal, in an
environment in which either of two sonorants can presumably be the nucleus
of a syllable (e.g., between two consonants). By the constraint *(t ⊳ a / Peak),
assuming like-manner consonants are equally sonorous, either of the glides
*i̯ or *u̯ should be equally suitable targets for vocalization in the hypothetical
configuration in (21), as should *m and any preceding nasal *m or *n in (22)
(a second position syllabic *n would be ruled out by *R/C). (We annotate each
of the candidates in these tableaux with the winning F symbol, since under
the given rankings they remain equally viable.)
(21)
/CGGC/
*R/C
Parse
Fill
Linearity
*(t ⊳ a / Peak)
F a. CGG̥C
F b. CG̥GC
(22)
/CNmC/
*R/C
Parse
Fill
Linearity
*(t ⊳ a / Peak)
F a. CNm̥ C
F b. CN̥mC
Indeed it is the case that in these sequences, as in sequences which feature a
coronal sonorant in second position, it is the second sonorant which vocalizes,
not the first (so at least we think with respect to *m; we will have more to say
about this particular sonorant in 10.1.2 in Chapter 10). So Keydana’s analysis
requires some elaboration if it is to capture the system of nucleus selection as
a whole; but in and of itself it misses this noteworthy generalization.
Lastly in this context, the analysis does not weigh in on the case of word-initial sonorants, either before a sonorant (23), in which position they should
be consonantal, or an obstruent (24), in which position they should be vocalic.

<!-- pdf-page: 194; source-page: 179 -->
(23)
/#RRV/
*R/C
Parse
Fill
Linearity
*(t ⊳ a / Peak)
F a. .RRV
F b. R̥.RV.
(24)
/#ROV/
*R/C
Parse
Fill
Linearity
*(t ⊳ a / Peak)
F a. .ROV
F b. R̥.OV.
For the former case we might again reasonably factor into the analysis
Keydana’s use of high-ranking Onset; indeed in previous work (2004: 5) he has
noted the crucial dominance of this constraint over Hnuc, a constraint which,
as indicated above, is effectively identical to the constraint *(t ⊳ a / Peak)
used in the analysis under examination. With Onset thus undominated in the
ranking, the candidate in (25a.) (= (23a.)) emerges as most optimal:
(25)
/#RRV/
Onset
*(t ⊳ a / Peak)
F a. .RRV
b. R̥.RV.
*!
With this adjustment, the analysis would be able to account for a word-initial
consonantal sonorant. But in order to generate an initial vocalic sonorant
before an obstruent, a constraint like Sonority-Sequencing would be
required as well, so as to disfavor a sonority reversal in the onset of the syllable;
this is not a scenario to our knowledge considered by Keydana.
A downright problematic consequence of Keydana’s analysis reveals itself
in consideration of the ranking in (15), used to account for the behavior of
vowel + sonorant sequences. Once we introduce the constraint *(a ⊳ t / Mar)
into the ranking, the correct result is no longer obtained in the main environment Keydana seeks to account for, namely a sonorant + sonorant sequence
not adjacent to a vowel:
(26)
/k̑u̯nbh-/
*(a ⊳ t /
Mar)
*R/C Parse Fill Linearity *(t ⊳ a / Peak)
L a. k̑u̯n̥.bh*!
*
F b. k̑un.bh*
F c. k̑nu.bh*
F d. k̑u<n>.bh*
F e. k̑u.n .bh*

<!-- pdf-page: 195; source-page: 180 -->
Given high-ranking *(a ⊳ t / Mar), the candidate in (26a.), which ought to be most optimal, is ruled out at the outset, because *u̯ makes a poorer syllable margin than lower-sonority *n; all other candidates in (26b.–e.) present equally better alternatives by comparison. This unwelcome development results from the introduction and non-differentiation of the comprehensive constraint *(a ⊳ t / Mar) in particular, which in its unitary form encapsulates the entire gamut of preferences for syllable margins. To resolve this issue we could unpack the constraint into the finer-grained fixed subhierarchy *Margin/ Vowel » *Margin/Glide » *Margin/ Liquid and so forth after Prince and Smolensky (1993 [2004]) (used in the following chapter), and rank only *Margin/Vowel over *R/C; this would have the effect of maintaining a strong dispreference for non-high vowels to be syllable margins, while allowing for high vowels (glides) to occur in such a position, at least under some circumstances. Still, even with this repair strategy, the same concern remains—namely, the fact that the analysis is built around the constraint *R/C, disfavoring coronal sonorants from occupying coda position. This constraint fails to fully formally capture the generalization that it is always the second of two non-vowel adjacent sonorants which vocalizes, regardless of its relative sonority, and even if it is not coronal, as would be the case in e.g. glide + glide sequences and nasal + *m sequences (cf. (21) and (22) above).
## 7.3 Conclusion: Missing Generalizations and the Problem
with Minimizing Codas As we noted at the outset of this chapter, and as we have observed in the previous two subsections, the Optimality-Theoretic analyses of nucleus selection developed by Kobayashi and Keydana focus almost exclusively on accounting for the behavior of sonorants. This is understandable given that only sonorants involve an instance of allophony, meaning a potential for mismatch from input to output (i.e., something to actually analyze). More particularly, with reference to generalization (1d.) above, the phenomenon is one that seemingly bucks our expectations, from a theoretical and perhaps even cross-linguistic perspective. While clearly aware of the first two generalizations in (1)—concerning the non-alternating status of obstruents and non-high vowels—nonetheless Kobayashi and Keydana fashion analyses which, as constructed, fail to formally account for them—in fact, quite the contrary: Kobayashi’s conception of Hnuc, and its ranking below AlignNuc (= NoCoda), would predict sonorants vocalize even when following a non-high vowel (e.g., †CV̯R̥C); one could even claim the ranking would similarly prefer the syllabification of obstruents in the same

<!-- pdf-page: 196; source-page: 181 -->
environment (e.g., †CV̯O̥C). Keydana’s analysis, while formally acknowledging
the first two generalizations in the form of the constraints *(a ⊳ t / Mar) and
*(t ⊳ a / Peak), deploys these constraints in such a way as to void any viability
his novel constraint *R/C has as a means of accounting for the fourth generalization. In other words, the ends of these efforts are analyses which are, again,
unable to generate all the right results.
A more fundamental issue for both Kobayashi’s and Keydana’s accounts is
that they rely on some form of coda minimization to motivate nucleus selection—Kobayashi uses the alignment constraint AlignNuc (= NoCoda), and
Keydana posits a more specified constraint targeting only coronal sonorants,
*R/C. To be sure, for the canonical example of Proto-Indo-European sonorant
vocalization, *k̑u̯n̥.bhis, each approach works—in its own way—as shown in
the following tableaux, repeated from the relevant discussion earlier in this
chapter.7
(27)	 Kobayashi on *k̑u̯n̥bhis (2004: 24)
/k̑u̯n-bhis/
Onset
AlignNuc
Hnuc
 a. k̑un.bhis.
*!
F b. k̑u̯n̥.bhis
*
 c. k̑u.n̥.bhis.
*!
(28)	 Keydana on *k̑u̯n̥bhis (2008 [2010]: 61)8
/k̑u̯nbh-/
*R/C
Parse
Fill
Linearity
*(t ⊳ a / Peak)
F a. k̑u̯n̥.bh*
b. k̑un.bh*!
c. k̑nu.bh*!
d. k̑u<n>.bh*!
e. k̑u.n .bh*!
Crucially ranking the constraint against codas (AlignNuc, *R/C) over the
constraint encoding preferences for syllable nuclear constituency (Hnuc,
*(t ⊳ a / Peak)) results in the desired selection of the most optimal output.
7	 Again, both tableaux have been reformatted from the authors’ own presentations, but not in
any way significantly affecting their claims.
8	 For these purposes we abstract away from the complication in the analysis arising from the
inclusion of high-ranking *(a ⊳ t / Mar), which again would disfavor the desired result, the
candidate in (28a.).

<!-- pdf-page: 197; source-page: 182 -->
Yet maintaining only some version of an anti-coda constraint to compel
right-hand sonorant vocalization ultimately proves inadequate as a means
of accounting for all the Proto-Indo-European data, as the system has been
reconstructed. An analysis of this nature is unable to handle forms in which
the sonorant sequence under examination falls in a non-initial syllable; in such
cases NoCoda (or variations thereof) proves ineffective in distinguishing output candidates. Recall that Kobayashi’s and Keydana’s analyses each make the
same prediction in the case of the form *per-u̯r̥, namely, the syllabification
†pe.ru̯r̥ (see the tableaux in (6) and (20)). While this form matches the prediction of Schindler’s rule that *r vocalizes over *u̯ (supported by Gk. πεῖραρ ‘end,
boundary’ < *peru̯ar),9 nonetheless it does not abide by our expectations for
the syllabification of the medial consonant sequence *-ru̯-, which given our
examination of medial consonant syllabification in the first part of this book,
we expect should be broken up across syllables. Assuming that there is some
constraint appropriately positioned in the ranking so as to militate against a
complex onset *.ru̯- in this form,10 the issue at the heart of Kobayashi’s and
Keydana’s analyses becomes readily apparent when trying to zero in on the
most optimal output:
(29)	 Kobayashi’s Prediction
/per-u̯r/
Onset
AlignNuc
Hnuc
L a. per.u̯r̥
*
*!
F b. pe.rur
*
(30)	 Keydana’s Prediction
/per-u̯r/
*R/C
Parse
Fill
Linearity
*(t ⊳ a / Peak)
L a. per.u̯r̥
*
*!
F b. pe.rur
*
9
As Keydana points out (2008 [2010]: 55–56), this treatment holds at least of a pre-stage
of Greek, if not of Proto-Indo-European itself. See also Schindler (1975), and Hoffmann
(1974) for Ved. párur.
10
In the analysis of the phenomenon we develop in the following chapter, this will be
achieved by a constraint permitting complex onsets only in word-initial position. (Highranking Sonority-Sequencing, which in our analysis of Vedic in Chapter 3 militated
against complex onsets of flat sonority—maintaining a sonority hierarchy R > O—is
arguably relevant for this case as well, though in our account of Proto-Indo-European
nucleus selection we will rely on this constraint mainly as a means of governing word-initial syllabification.)

<!-- pdf-page: 198; source-page: 183 -->
The problem is as follows: once we move beyond consideration of the single syllable in which the candidates for syllabicity find themselves, violations of the coda-targeting constraints equalize—the preferred syllable .u̯r̥ may lack a coda, but its associate per. does not; thus each candidate has one violation of either AlignNuc or *R/C. Consequently, evaluation falls to the lower-ranked nuclear preference constraints, Hnuc or *(t ⊳ a / Peak), and determination of the more optimal output hinges on which sonorant makes the better nucleus: hence the candidate in (29–30b.) wins, since it features a vocalic glide over a vocalic liquid. The issue, then, is how do we arrive at *per.u̯r̥? How can we effectively suppress sonority-based preferences on syllabicity so as to eliminate the alternative form †pe.rur? For that matter, how can we effectively motivate medial consonant heterosyllabicity so as to eliminate the alternative form †pe.ru̯r̥? Arriving at a satisfying answer to these questions will animate our own attempt at developing an account Proto-Indo-European nucleus selection, the exercise to which we now turn.

<!-- pdf-page: 199; source-page: 184 -->
