---
title: "Chapter 8, §8.2.2. Directionality in Syllabification"
author: "Adam I. Cooper"
date: "2015"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "cooper-2015-reconciling-ie-syllabification.pdf"
chunk: "Chapter 8 §8.2.2"
pages: "197-226"
---
### 8.2.2 Directionality in Syllabification
As neither invoking a constraint against codas, nor a preference for minimized moraicity of consonants, offers us a satisfactory means of translating Schindler’s insight that the rule of sonorant vocalization in Proto-Indo-European operates iteratively from right to left, we are compelled to examine more closely the issue of directionality itself in phonology, and consider other ways in which its effects have been encoded in Optimality Theory. In the following subsections we undertake this exercise. We begin in 8.2.2.1 by reviewing two relevant pre-Optimality Theory works on directionality as a parameter of syllable structure assignment, that of Kaye and Lowenstamm (1981) and Itô (1989), before moving on to consider how directionality has been formalized in a constraint-based framework by Mester and Padgett (1994) in 8.2.2.2.15 We then move on in 8.2.2.3 to consider how such approaches may be adapted to treat directionality in consonant syllabicity, specifically in Proto-Indo-European, and propose an analysis for this language.
#### 8.2.2.1 Directionality in Derivational Accounts
An early reference to directionality in theoretical literature on syllable structure assignment can be found in Kaye and Lowenstamm 1981. As part of their discussion of markedness in syllable structure, the two authors identify two directional syllable-structural parsing strategies that are capable of accounting for ostensibly language-specific syllabifications of similar phonological strings. They call these strategies the Rightward Strategy and the Leftward Strategy; both are defined in (22): (22) Directional Syllabification Strategies (Kaye and Lowenstamm 1981) a. The Rightward Strategy (their (33)) Scanning a word from left to right, make the first syllable as unmarked as possible. If the resulting syllable on the right conforms to the formal and substantive syllable constraints of the language, then there is a syllable boundary at that point. If the resulting right syllable violates a constraint, move the syllable boundary over one segment to the right and try again. Repeat until the resulting right syllable is licit. After the first syllable boundary has been found, repeat the process for successive syllables until the end of the string is reached (307). 15 We do not claim to strive for exhaustivity in the following review; see the discussion in Cooper 2012 for more on this topic.

<!-- pdf-page: 213; source-page: 198 -->
b. The Leftward Strategy (their (36)) Scanning a word from right to left, make the last syllable as unmarked as possible. If the resulting syllable on the left conforms to the formal and substantive syllable constraints of the language, then there is a syllable boundary at that point. If the resulting left syllable violates a constraint, move the syllable boundary over one segment to the left and try again. Repeat until the resulting left syllable is licit. After the first syllable boundary has been found, repeat the process for successive syllables until the beginning of the string is reached (308–309). To exemplify these strategies, Kaye and Lowenstamm introduce data from English, which they analyze as a language with left-to-right syllabification (e.g. a.stute over †as.tute, supported by the lack of aspiration associated with the first dental stop), and Polish, which they identify as a language with right-toleft syllabification (e.g. wys.pa over †wy.spa ‘island’, based on native speaker judgment).16 But perhaps the most well-known discussion of directional syllabification effects can be found in the work of Itô (1986, 1989). Itô introduces directionality in syllable structure assignment to account for different epenthesis sites in two dialects of Arabic, Cairene and Iraqi, as well as for initial and medial epenthesis in the Austroasiatic language Temiar. We review her analysis of the former here.17 16 As Kaye and Lowenstamm acknowledge (1981: 308), ideally phonological processes such as aspiration will point to syllable breaks, but in the absence of such evidence, native judgments, problematic and inconsistent as they may be, are a potential source of insight. 17 Our purpose here is to review Itô’s general framework, not to dwell on how well it fits the Arabic data, the basis of much discussion in the literature over the past two decades. Indeed a few issues which have been raised with Itô’s account of the Arabic dialects involve the behavior of consonants at word-edge, the behavior of syncope, and the interaction of epenthesis and stress placement, specifically in Iraqi. To elaborate just on this last point, syllables headed by epenthetic vowels resolving a single unsyllabifiable consonant (i.e. in words with triconsonantal sequences) are apparently invisible to the rules of stress placement in Iraqi, a result which Itô’s account would not predict. Piggott (1995) offers a revised analysis which maintains Itô’s directional syllable structure, while Broselow (1992) argues against it, promoting instead an analysis invoking onset/rime syllable constituency. More recently, Kiparsky (2003) has formalized an Optimality Theoretic approach to these data involving semisyllables, unsyllabified moras dominating a single consonant.

<!-- pdf-page: 214; source-page: 199 -->
In neither Cairene nor Iraqi Arabic are triconsonantal sequences permitted in medial position, so epenthesis serves to render such sequences syllabifiable, when they occur via morphological concatenation. While for a medial
sequence -CCC-, there are two potential sites for a vowel to be inserted into—
between the first and second consonant, i.e. CVCC, or between the second and
third, i.e. CCVC—Cairene and Iraqi differ in that the former consistently epenthesizes CCVC (23), while the latter consistently epenthesizes CVCC (24).
(23)	 CCC Epenthesis in Cairene Arabic (from Itô’s (41))
a. /ʔul-t-l-u/
→
ʔultilu
‘I said to him’
b. /katab-t-l-u/
→
katabtilu
‘I wrote to him’
c. /katab-t dars/
→
katabtidars
‘you wrote a lesson’
(24)	 CCC Epenthesis in Iraqi Arabic (from Itô’s (42))
a. /gil-t-l-a/
→
gilitla
‘I said to him’
b. /triid ktaab/
→
triidiktaab
‘you want a book’
c. /katab-t ma-ktuub/
→
katabitmaktuub 	 ‘I wrote a letter’
To generate these distinct results, Itô posits that while Cairene Arabic and Iraqi
Arabic share the same possible moraic and syllable structures, given in (24)
and (25), crucially these languages differ with respect to how syllable structure
is assigned: Cairene syllabifies from left to right, while Iraqi syllabifies from
right to left.
(25)	 Permitted Moraic Structures in Cairene and Iraqi Arabic (Itô’s (46))
(c) v
   μ
μ
μ
μ →
 c
c v
v
c18
(26)	 Permitted Syllabic Structures in Cairene and Iraqi Arabic (Itô’s (47))
σ → μ (μ)
σ
σ
σ
μ μ
μ μ
μ
(c)  v c
(c)  v v
(c)  v
18
Itô uses lowercase letters to indicate melodic rather than skeletal elements.

<!-- pdf-page: 215; source-page: 200 -->
In Cairene Arabic, moraic structure is first assigned according to the allowable
moraic sequences of the language, which as shown in (25) include cv, v, c. At this
point it is important to note that, in terms of moraic structure, Itô’s theoretical
perspective is more in line with that of Hyman (1985), for whom all segments
are dominated by a mora, including onsets; in particular, in this view onsets
and nuclei come to be dominated by the same mora.19 On the other hand, in
our discussion of consonant moraicity in the previous subsection, we saw that
the presence or absence of an onset had no effect on moraic structure; rather,
vowels projected their own moras, and coda consonants were moraic given
the greater dispreference for appended segments (see the syllable structures
and tableau in (17)–(19)), a view more in line with the alternative approach
of McCarthy and Prince (1986 [1996]), Hayes (1989), et al. While we choose to
maintain Itô conception of moraic structure for the purposes of the present
discussion—and later, in our examination of the Proto-Indo-European from
the same perspective—note this does not amount to its endorsement; as we
will see, the Optimality-Theoretic translation of Itô’s approach is in fact compatible with what is arguably the more typical view of moraicity assumed in
the literature, as invoked in the previous subsection.
Once moraic structure has been assigned, syllabification proceeds from
the beginning of the word to create a CVC syllable out of the initial bimoraic
sequence ʔul-. As the remaining material cannot constitute a licit syllable in
this language, the interconsonantal -t- is incorporated into a syllable of its own,
as an onset, leaving the remaining two segments, -lu, to be incorporated in a
syllable of shape CV. Itô schematizes this process as follows (her (50)):
(27)	 Left-to-Right Syllabification in Cairene Arbaic
a.
σ
b.
σ
σ
μ    μ μ  μ
μ  μ  μ  μ
ʔ  u   l  t   l u
ʔ u l  t ___ l u
↑
c.
σ   σ
i
μ  μ  μ  μ

ʔ    u l t i l u
19
For Itô, via the general prosodic principle of Maximality, for Hyman, via application of the
universal Onset Creation Rule. This conception of moraic structure is more generally in
line with the Strict Layer Hypothesis (Selkirk 1984, Nespor and Vogel 1986).

<!-- pdf-page: 216; source-page: 201 -->
Note that, although the language allows for syllables of shape VC, t is prevented from becoming the coda of the syllable headed by the epenthetic vowel (i.e. ʔul.it.lu) because of the nature of the epenthesis process, and the nature of moraic structure: only a vowel is inserted into the string, unaccompanied by a superordinate mora. Thus the only moraic structure permitted given the already moraified [t]μ is [tV]μ; the syllable Vt would have the bimoraic structure [V]μ[t]μ.20 In Iraqi Arabic, on the other hand, once moraification has taken place, syllabification proceeds starting from the end of the word as follows. The largest possible licit syllable at word-edge is -la, of shape CV; anything larger is blocked by the presence of the preceding t. This segment, together with the preceding l, are both moraic, but cannot themselves constitute a licit syllable. Epenthesis thus occurs, creating a syllable of shape CVC; again, given that only a vowel is inserted, not a mora, this is the only possible repair, operating in this direction. Finally, remaining is the initial sequence gi-, which is incorporated into a second CV syllable. This process is schematized by Itô as in (28) (her (51)). (28) Right-to-Left Syllabification in Iraqi Arabic a. σ b. σ σ

μ  μ  μ  μ
μ  μ μ μ
g i   l   t  l a
   g  i l  ___  t l a
↑
i
c.
σ     σ   σ
μ  μ   μ  μ

g i l i t l a Itô’s analysis has the additional empirical advantage of straightforwardly accounting for the location of epenthesis in quadriconsonantal sequences in these languages: in both Cairene and Iraqi a vowel inserted as follows: /VCCCCV/ → VCCVCCV. This is exactly as expected given the procedures she 20 This means of forcing t into a syllable onset position is of course then contingent on a syllable onset sharing a mora with a syllable nucleus (Hyman 1985), rather than being adjoined directly under the syllable node (McCarthy and Prince 1986 [1996], Hayes 1989). Under this latter view of moraic structure, epenthesis after t could be compelled by a preference for onsetful syllables.

<!-- pdf-page: 217; source-page: 202 -->
defines for rightward and leftward syllabification (operating in languages
which disallow onset and coda clusters). Relevant data are given in (29)–(30),
and sample syllabifications in (31)–(32).
(29)	 CCCC Epenthesis in Cairene Arabic (from Itô’s (41))
a. /ʔul-t-l-ha/
→
ʔultilha
‘I said to her’
b. /katab-t-l-ha/
→
katabtilha
‘I wrote to her’
c. /katab-t-l-gawaab/
→
katabtilgawaab
‘I wrote the letter’
(30)	 CCCC Epenthesis in Iraqi Arabic (from Itô’s (42))
a. /gil-t-l-ha/
→
giltilha
‘I said to her’
b. /triid-l-ktaab/
→
triidliktaab
‘you want the book’
c. /kitab-t-l-maktuub/
→
kitabtilmaktuub
‘I wrote the letter’
(31)	 Left-to-Right Syllabification in Cairene Arabic
a.
σ
b.
σ
σ
μ  μ μ   μ   μ
μ μ μ     μ  μ
ʔ u l  t l h a
ʔ u l  t   ___   l h a
↑
i
c.
σ
σ
σ

μ μ μ μ  μ

ʔ  u  l t I l  h a
(32)	 Right-to-Left Syllabification in Iraqi Arabic
a.
σ
b.
σ
σ

μ μ μ μ  μ
μ μ μ μ  μ
g i  l  t  l  h a
g i  l  t  ___  l h a
↑
i
c.
σ
σ
σ

μ μ μ μ   μ

g i l t i  l h a

<!-- pdf-page: 218; source-page: 203 -->
In intervocalic sequences of four consonants, it is the intermediate two which are unsyllabifiable: in (31)–(32), the first consonant is assigned to the coda of the syllable headed by the preceding vowel (Cairene [ʔul]σ, Iraqi [gil]σ,), while the final consonant is assigned to the onset of the syllable headed by the following vowel (Cairene, Iraqi [ha]σ). Left with a sequence CC, the most economical way of rendering it syllabifiable (through epenthesis) is to insert a single intervening vowel: the second consonant thus serves as onset, and the third consonant as coda, to the syllable headed by this epenthetic vowel (Cairene, Iraqi [til]σ).
#### 8.2.2.2 Directionality in a Constraint-Based Account
The directional syllabification effects as analyzed by Itô (1986, 1989) and others are not straightforwardly accounted for in the traditional conception of Optimality Theory. Such effects have been conceived as resulting from a stepwise accretion of syllable structure, but the constraint-based framework is at its core anti-derivation. Instead, as per the basic tenets of Optimality Theory, the approach we review here, that of Mester and Padgett (1994), focuses on the agreeability of fully-specified output candidates with syllable-structural preferences captured in the form of constraints.21 Following up on the work of McCarthy and Prince (1993a), who develop the notion of Alignment constraints as a means of capturing directional foot parsing effects, Mester and Padgett (1994) extend the approach into the subordinate realm of syllable structure. They construct an Optimality-Theoretic translation of Itô’s analysis of directional effects in Cairene Arabic- and Iraqi Arabic-type languages, the core of which is an alignment constraint which they schematize as follows (their (1); the definition is ours): (33) Syll-Align (Syll,Edge,PrWd,Edge) Align every syllable with an edge (specified left, right) of the prosodic word. In view of current conventions in constraint representation, we will henceforth depict this constraint as Align-X(σ, PrWd), where X represents the specified margin, either left or right. Mester and Padgett first account for languages patterning with Iraqi Arabic, which has been described as featuring right-to-left syllabification, as determined by the position of the epenthetic vowel breaking up a triconsonantal sequence (/gil-t-l-a/ → gilt[la]σ → gi[lit]σ[la]σ → [gi]σ[lit]σ[la]σ ‘I said to him’). 21 See Cooper 2012 for consideration and comparison of an alternative Alignment-based approach based on consonants (after Rose 2000).

<!-- pdf-page: 219; source-page: 204 -->
They introduce the left-edge oriented variant of the alignment constraint,
Align-L(σ, PrWd), ranking it as follows (their (4)):
(34)	 Onset, Parse,22 *Complex23 » Align-L(σ, PrWd), Fill24 » NoCoda
The following tableaux illustrate how this ranking operates; the first is their
(5) (with some formatting adjustments), the second is our application of the
ranking to the actual Iraqi form:
(35)	 Right-to-Left Syllabification
a.
/CVCCCV/
Fill
Align-L(σ, PrWd)
NoCoda
σ1
σ2
σ3
σ4
F i. CV.CVC.CV
*
μ
μμμ
*
ii. CVC.CV.CV
*
μμ
μμμ!
*
iii. CV.CV.CV.CV
**(!)
μ
μμ
μμ(!)μ
b.
/gil-t-l-a/
Fill
Align-L(σ, PrWd)
NoCoda
σ1
σ2
σ3
σ4
F i. gi.lit.la
*
*
***
*
ii. gil.ti.la
*
**
***!
*
iii. gi.li.ti.la
**(!)
*
**
**(!)*
Mester and Padgett assume, after McCarthy, that violation of the syllable-sensitive alignment constraint is measured in moras, the unit immediately
below the syllable on the prosodic hierarchy.25 Though they are not explicit in
the version of moraic theory they adhere to (see the discussion in 8.2.2.1), note
that regardless of how one treats onsets in this regard, the number of moras
to be evaluated remains unchanged: assuming coda consonants to be moraic,
under either Ito’s (1989) approach (and Hyman’s [1985]) or that of McCarthy
22
= Max-IO, i.e., a constraint militating against deletion.
23
This constraint militates against complex syllable margins of any sort, whether onset
(.CCV) or coda (VCC.).
24
= Dep-IO (2), i.e., a constraint militating against epenthesis. Recall that both Parse and
Fill were used by Keydana (2008 [2010]) in his analysis of right-hand vocalization, examined in the previous chapter.
25
As they note, counting violations according to syllables will not yield the correct result;
though they do not exclude the possibility of counting in segments, an approach argued
for by Rose (2000).

<!-- pdf-page: 220; source-page: 205 -->
and Prince (1986 [1996]), Hayes (1989), et al., there are only as many moras in
a syllable as there are vowels and codas (in this case the upper limit is two).
So under either conception of moraic structure, the same result is obtained,
that is, the candidate in (35a.i.) is selected as most optimal because it minimizes violations of Align-L(σ, PrWd) across all three syllables. The initial syllable, being immediately adjacent to the left edge, incurs no violations. As this
syllable is open, the second syllable, which follows it, is only one mora away
from the left edge (CVμ.). And as this syllable is closed, the third syllable is
three moras away from the left edge (CVμ.CVμCμ.). Thus (35a.i.) incurs in total
four violations of Align-L(σ, PrWd), compared to (35a.ii.), which incurs five
due to the initial syllable being heavy, and (35a.iii.), which incurs six, due to the
creation of an additional syllable.
The account of Cairene Arabic-type languages proceeds along similar lines.
On the basis of the epenthesis site in triconsonantal sequences, this language has been characterized as assigning syllable structure from left to right
(/ʔul-t-l-u/ → [ʔul]σtlu → [ʔul]σ[ti]σlu → [ʔul]σ[ti]σ[lu]σ ‘I said to him’). For the
Optimality-Theoretic analysis, Mester and Padgett introduce the left-edge variant of the alignment constraint, Align-L(σ, PrWd), and rank it as they did
Align-R(σ, PrWd) above, i.e. (their (8)):
(36)	 Onset, Parse, *Complex » Align-R(σ, PrWd), Fill » NoCoda
The tableaux in (37) demonstrate how the ranking works; again, (37a.) corresponds to Mester and Padgett’s (9) (with formatting adjustments), and (37b.)
includes the actual Cairene form.
(37)	 Left-to-Right Syllabification
a.
/CVCCCV/
Fill
Align-R(σ, PrWd)
NoCoda
σ1
σ2
σ3
σ4
i. CV.CVC.CV
*
μμμ
μ!
*
F ii. CVC.CV.CV
*
μμ
μ
*
iii. CV.CV.CV.CV
**(!)
μμμ
μ(!)μ
μ
b.
/CVCCCV/
Fill
Align-R(σ, PrWd)
NoCoda
σ1
σ2
σ3
σ4
i. ʔu.lit.lu
*
***
*!
*
F ii. ʔul.ti.lu
*
**
*
*
iii. ʔu.li.ti.lu
**(!)
***
*(!)*
*

<!-- pdf-page: 221; source-page: 206 -->
Instead of evaluation according to distance from the left edge of the prosodic
word, it is distance from the right edge which is now the decisive factor. The
candidate in (37a.ii.) wins due to its minimal violation of Align-R(σ, PrWd),
spread out across its three syllables. In short, relegating the lone heavy syllable
to the left edge of the prosodic word allows for both it and the following syllables to be that much closer to the right edge of the prosodic word.
With respect to intervocalic sequences of four consonants, as Itô’s analysis
was capable of doing, so too can Mester and Padgett’s account generate the
same result for both the Cairene and Iraqi Arabic treatment of such sequences,
again, VCCVCCV. We see as much in the following two tableaux.
(38)	 CCCC: Left-to-Right Syllabification
/CVCCCCV/
Fill
Align-R(σ, PrWd)
NoCoda
σ1
σ2
σ3
σ4
F a. CVC.CVC.CV
*
μμμ
μ
**
b. CVC.CV.CV.CV
**(!)
μμμ
μμ(!)
μ
*
c. CV.CV.CVC.CV
**(!)
μμμμ
μ(!)μμ
μ
*
(39)	 CCCC: Right-to-Left Syllabification
/CVCCCCV/
Fill
Align-R(σ, PrWd)
NoCoda
σ1
σ2
σ3
σ4
F a. CVC.CVC.CV
*
μμ
μμμμ
**
 b. CVC.CV.CV.CV
**(!)
μμ
μμμ
μμ(!)μμ
*
c. CV.CV.CVC.CV
**(!)
μ
μμ
μμμμ(!)
*
Mester and Padgett do not claim to provide the best Optimality-Theoretic analysis of the directional syllabification effects, but merely intend to demonstrate
how such an analysis could work. Indeed they acknowledge a few issues with
their approach, as it has been developed,26 and in general leave the question
26
See the discussion in Cooper 2012. One concern for them is the fact that the same result
can also be obtained with a variety of other techniques: using opposite-edge alignment
constraints, for example, i.e. Align(σ, R, PrWd, L) (‘Align the right edge of a syllable with
the left edge of the prosodic word’) for languages described with right-to-left syllabification, and Align(σ, L, PrWd, R) (‘Align the left edge of a syllable with the right edge of the
prosodic word’) for languages described with left-to-right syllabification.
Mester and Padgett also leave open the possibility, as suggested in Broselow (1992),
that directionality is not actually a factor in the Arabic dialects considered at all, and

<!-- pdf-page: 222; source-page: 207 -->
open, as to how this strategy functions as a linguistically-significant contribution to the theory. As we will now show, we can make use of their basic insight as a way of resolving the issue of the identity of the constraint C, and thereby propose a fuller account of sonorant syllabicity in Proto-Indo-European.
#### 8.2.2.3 Directionality in Consonant Syllabicity: Analyzing
Proto-Indo-European Having reviewed derivational and constraint-based approaches to formally capturing directionality in assignment of syllable structure, we return to the Proto-Indo-European system and resume the development of our analysis. Interestingly, because it employs consonant vocalization as a means of repairing unsyllabifiable sequences of segments, as opposed to the epenthesis we saw operative in Arabic, the Proto-Indo-European system is a departure from those of languages considered in previous studies in this area. As such we have a valuable opportunity not only to better understand how the relevant phenomena operate within this language, but also to make a contribution to our understanding of the theory as well. Although we will ultimately develop an analysis couched in Optimality Theory, nonetheless we will begin this exercise in 8.2.2.3.1 first by conceptualizing the Proto-Indo-European phenomenon within the framework of Itô (1989), so as to provide a basis of comparison analogous to that holding for the Arabic data introduced in 8.2.2.1, which have been analyzed both from a derivational perspective and later from a constraint-based one. We will then move on to capture the system in a constraint-based framework in 8.2.2.3.2, following the approach of Mester and Padgett (1994).
#### 8.2.2.3.1 Proto-Indo-European after Itô (1989)
From the perspective of Itô’s (1989) framework, crucial for the Proto-Indo-European data is directionality in the process of moraification, not syllabification. Simply plugging the Proto-Indo-European data into Itô’s prosodic analysis of epenthesis will not work. To demonstrate as much, we assume for the moment that Proto-Indo-European shares its set of moraic and syllable structures with Cairene and Iraqi Arabic. As already noted, this is arguably a departure from the usual assumptions about moraic structure one finds in the literature, which tend to adhere more closely to the view of McCarthy acknowledge issues with generating word-initial syllabification patterns. As Rose (2000) points out, an additional concern is that not all coda consonants are necessarily moraic, even in the same language; in the Arabic languages under consideration, for instance, moraicity does not hold of final consonants.

<!-- pdf-page: 223; source-page: 208 -->
and Prince (1996 [1986]), Hayes (1989), et al., under which onsets are not moraic, only vowels and codas are.27 As we will see when we transition into the Optimality-Theoretic analysis (and as was noted in the overview of Mester and Padgett 1994 presented above), the specific version of moraic theory one adheres to will not matter, and indeed one can maintain the more familiar, non-moraic onset view without complication. In any case, proceeding for now as we have suggested, we end up with the following structures assigned to the string /per-u̯r/: the moraic structure as in (40), and the syllable structures in (41) and (42), with syllabification proceeding from left to right and right to left, respectively. (40) μ μ μ μ

p e r u̯ r
(41)	 Left-to-Right Syllabification
а.
σ
b.
σ
σ
μ μ  μ μ
μ μ  μ μ

p e r  u̯ r
p   e r  u̯  _  r
(42)	 Right-to-Left Syllabification
а.
σ
b.
σ
σ
μ μ  μ μ
μ μ  μ μ

p e r u̯ _ r p e r u̯ _ r Again, in moraification as maintained by Itô (and contrary to what one might expect), a mora is assigned to the initial CV sequence *pe-, and to each of the three sonorants remaining in the string; this is the only possible outcome, given the limits on moraic structure (only units with melodies (c)v, c). We see that under an approach in which epenthesis is the repair mechanism, there is a single possible site for the epenthetic vowel, regardless of the 27 The latter on a language-specific basis, which again we assume applies in the case of Proto-Indo-European, given the facts of e.g. Vedic; recall the array of weight-based phenomena surveyed in Chapter 2.

<!-- pdf-page: 224; source-page: 209 -->
direction in which syllable structure is assigned: between the second and third
sonorant. If we assume that sonorant vocalization involves insertion not of a
full vowel, but rather of a vocalic element which coalesces with an adjacent
sonorant, we immediately face a problem: the only permissible way in which
such a unit can be incorporated into moraic structure, given the permitted
shapes of moras, is if it assimilates to the preceding sonorant *u̯, yielding a
mora of shape cv, as in (43a.); a mora of shape vc, which would be the result of
assimilation to the following *r, would be illicit, as in (43b.).28
(43)	 a.
σ
σ
b.
σ
σ

μ μ μ μ μ μ μ μ ü p e r u̯ u r û p e r u̯ r̥ r The result in both of these cases would be something like †peru̯ur. In fact this result is akin to the treatment of intervocalic sequences of four consonants shared by both Cairene and Iraqi Arabic and reviewed above, that is, /VCCCCV/ → VCCVCCV. Once we factor out the final C, which is analyzed as an onset to the syllable headed by the following vowel, and the initial C, which is analyzed as a coda to the syllable headed by the preceding vowel, what we have left are two consonants, each assigned a mora, that cannot be syllabified as is. The most economical solution, given epenthesis as a repair mechanism, is insertion of a single vowel intervening between these two consonants: recall Cairene Arabic /ʔul-t-l-ha/ → ʔultilha ‘I said to her’ as compared to Iraqi Arabic /gil-t-l-ha/ → giltilha ‘I said to her’, in both of which the epenthetic vowel intervenes between the second and third consonants, t and l. From this perspective it is not surprising that the syllabifications in (41)–(42) share an identical outcome, even if an undesired one. If, for the present purposes, we want to tackle the Proto-Indo-European data while maintaining the underpinnings of Itô’s approach (i.e. her general theoretical assumptions concerning moraic and syllable structure), then we must 28 Cf. Steriade’s (1988) comments regarding a translation of her account of Sanskrit sonorant vocalization into moraic theory (and see also the discussion in Chapter 9): if there is no recourse to the structural positions of onset versus rime, and if moras dominate onsets, then there is no way to differentiate the sonorant which does vocalize from the one which does not, since both are ‘moraic’. Of couse, if one assumes that onsets are not moraic—a position that, again, is wholly compatible with the Optimality-Theoretic analysis we will eventually develop—then this issue is moot.

<!-- pdf-page: 225; source-page: 210 -->
recognize for this language a different set of licit moraic structures. Proposing
anything different at the level of the syllable will not work; as consideration of
the structures in (43) show, the end result is a form consisting of four moras,
when the desired outcome, *peru̯r̥, is one containing three. So moraic structure is crucially what must be differentiated for Proto-Indo-European, in order
for an analysis after Itô’s (1989) to be possible.
We propose that, as Proto-Indo-European allows syllabic sonorants, under
Itô’s approach moras should be composed of the melodies cv, v, c, and, additionally, cr and r, as in (44).29
(44)	 μ → {(c)v, (c)r, c}
μ
μ
μ
μ
μ
c v
v
c
c r
r
The process of moraification would apply to a string directionally, assigning at
any given iteration the largest possible mora, given the set in (44).
For the current purposes we assume that syllables can be of shape V, CV,
CVC, R, CR, CRC, with moraic structure as in (45). As with the building of
moraic structure, syllable structure is assigned directionally, with the largest
possible syllable constructed at any given point in the process, according to the
principle of Maximality.
(45)	 a.	 σ
b.
σ
c.
σ
d.	 σ
e.
σ
f.
σ
μ
μ

μ  μ
μ
μ
μ
μ
v
c v
c v	 c
r
c r
c r	 c
As Itô does, we note that the syllable peak must be associated with the initial
mora. But as we are dealing with the potential for syllabic sonorants, we must
also stipulate that the leftmost component of this mora constitutes the syllable
peak, as otherwise there would be no way of identifying it in a syllable of shape
[[cr]μ([c]μ)]σ, where the initial c is also a sonorant.30
29
We abstract away, for the purposes of this exercise, from the treatment of initial consonants in complex onsets, such as the palatovelar in *k̑u̯n̥bhis.
30
We might try to rely on the Onset principle to generate this result, but note *k̑u̯n̥bhis,
in which this principle is satisfied regardless, by the initial palatovelar. Alternatively,
we could rely on weak vs. strong labeling, or head designation (Selkirk 1995, Zec 2003).

<!-- pdf-page: 226; source-page: 211 -->
Once we apply this revised Proto-Indo-European-specific analysis to the
string /per-u̯r/, we find that, as was not the case with Cairene and Iraqi Arabic,
different results are obtained depending on the direction in which the process of moraification applies. Moraification operating from left to right yields
the moraic structure [pe]μ[ru̯]μ[r]μ in (46), while the structure [pe]μ[r]μ[u̯r]μ is
obtained if the process operates from right to left, as in (47).
(46)	 Left-to-Right Moraification
a.
μ
b.
μ
μ
c.
μ
μ
μ

p e r u̯ r
p e r u̯ r
p e r u̯ r
(47)	 Right-to-Left Moraification
a.
μ
b.
μ
μ
c.
μ
μ
μ

p e r u̯ r
p e r u̯ r
p e r u̯ r
In turn these distinct moraifications are syllabified in distinct ways, shown
in (48)–(49). Interestingly, however, in both cases the same syllabification is
obtained, regardless of the direction in which syllable structure is assigned.
(48)	 Left-to-Right Moraification
a. Left-to-Right Syllabification
i.
σ
ii.
σ
σ
iii.
σ
σ
μ
μ
μ
μ
μ
μ
μ
μ
μ

p e r u̯ r
p e r u̯ r
p e r u r
b. Right-to-Left Syllabification
i.
σ
ii.
σ
σ
iii.
σ
σ
μ
μ
μ
μ
μ
μ
μ
μ
μ

p e r u̯ r
p e r u̯ r
p e r u r
Otherwise it would seem necessary for identification of the peak to be stipulated. Note
that this would not be an issue if the initial sonorant in the sequence were not also
moraic, as per Itô’s version of moraic theory; again, if one maintains the alternative, non-moraic onset view, this issue no longer remains.

<!-- pdf-page: 227; source-page: 212 -->
(49)	 Right-to-Left Moraification
a. Left-to-Right Syllabification
i.
σ
ii.
σ
σ
iii.
σ
σ
μ
μ
μ
μ
μ
μ
μ
μ
μ

p e r u̯ r
p e r u̯ r
p e r u̯ r̥
b. Right-to-Left Syllabification
i.
σ
ii.
σ
σ
iii.
σ
σ
μ
μ
μ
μ
μ
μ
μ
μ
μ

p e r u̯ r p e r u̯ r p e r u̯ r̥ When moraic structure is assigned from the beginning of the word, the end result is a syllabified form †pe.rur, no matter the direction in which syllabification occurs. On the other hand, when moraification proceeds from the end of the word, the end result is the desired syllabified form *per.u̯r̥, regardless of the directionality of the syllabification process. It is clear now that an analysis of Proto-Indo-European sonorant vocalization adapted from Itô’s approach to epenthesis in Cairene and Iraqi Arabic crucially hinges, not on the directionality in which syllable structure is assigned, but rather on the directionality in which moraic structure is assigned. While we ultimately prefer to maintain a different view of moraic structure than that of Itô—one in which onsets are not assigned to a mora—nevertheless we can exploit this insight, if only descriptively, as we begin to consider the Proto-Indo-European system from the constraint-based perspective.
#### 8.2.2.3.2 Proto-Indo-European after Mester and Padgett (1994)
Our efforts in the previous section provide a good starting point for adapting Mester and Padgett’s approach to directionality effects to the Proto-Indo-European data. As we saw, conceived in Itô’s framework directionality was crucial not for the process of syllabification, but rather for the process of moraification: specifically, only with moraic structure assigned from right-toleft could the desired result, the syllabified form *per.u̯r̥, be obtained. In their paper, Mester and Padgett sought to translate into Optimality Theory the directional syllabification phenomena proposed by Itô for Cairene and Iraqi Arabic. They did so in the form of the Alignment constraint schema in (50), repeated from (33) above.

<!-- pdf-page: 228; source-page: 213 -->
(50) Syll-Align (Syll,Edge,PrWd,Edge) Align every syllable with an edge (specified left, right) of the prosodic word. Specific variants of this constraint were keyed to the right edge of the syllable and prosodic word (to account for left-to-right syllabification in Cairene Arabic) or the left edge of the syllable and prosodic word (to account for right-to-left syllabification Iraqi Arabic). In essence, these constraints serve to successfully replicate the directionality effects because they (indirectly) prefer the end results generated by directional syllabification: a heavy CVC syllable in relatively closer proximity to one edge of the prosodic word or another. The end result of left-to-right syllabification has the CVC syllable closer to the left edge of the prosodic word (ʔul.ti.lu), which in turn minimizes the distance of each syllable from the right edge (hence Syll-Align-R), while the outcome of right-to-left syllabification has the CVC syllable closer to the right edge of the prosodic word (gi.lit.la), which in turn minimizes the distance of each syllable from the left edge (hence Syll-Align-L). In principle, if moraification, not syllabification, is key in Proto-Indo-European nucleus selection, then the Alignment constraint to be introduced should be concerned with the proximity of moras, not syllables, to prosodic word edge. We thus propose the following constraint schema: (51) Mora-Align (Mora,Edge,PrWd,Edge) Align every mora with an edge (specified left, right) of the prosodic word.31 We assess violations of this constraint in terms of segments, a method which, as Mester and Padgett point out, is not ruled out under their approach, and indeed would follow from their assumption that violations of Alignment constraints be reckoned in terms of those units one level down from the unit referred to in the first part of the constraint (1994: 81). The violation count for any given mora, then, is determined by counting the number of segments intervening between the segment which it dominates and the relevant edge of the prosodic word. We note that this metric is arguably more in line with the view of moraic theory proposed by McCarthy and Prince (1986 [1996]), Hayes (1989), et al., in which onset segments are adjoined directly to the syllable node, as opposed to being subsumed under the nuclear mora, as held to 31 This constraint is not to be confused with ‘mora alignment’ as proposed by Crowhurst (2004), in which the mora is argued to be a unit of alignment evaluation, akin to the approach taken by Mester and Padgett in their original analysis.

<!-- pdf-page: 229; source-page: 214 -->
be the case by Hyman (1985) and, as we have seen, Itô (1989); under the latter approach, it would not be immediately clear whether an onset consonant
should actually be counted in assessing violations, since it would be subsumed
within a mora being evaluated.32
As the desired result could only be obtained when moraification proceeded
in a leftward direction, we expect the actual constraint operative for Proto-Indo-European to be Mora-Align-L. This expectation is borne out in consideration of the comparative tableaux for *per-u̯r̥ in (52)–(53); the constraints *Pk/
Obstruent and *Pk/Nasal are omitted for clarity of presentation, as they
play no role in the evaluation of the candidates under consideration.
(52)
/peμr-u̯r/
*Mar/V
Dep-IO
Align-R(μ, PrWd)
*Pk/
Liq
*Pk/
Gli
μ1
μ2
μ3
μ4
L a. peμrμ.u̯r̥μ
***
**!
*
F b. peμ.ruμrμ
***
*
*
c. peμ.ruμ.r̥μ
***
*
*!
*
d. peμrμ.u̯Vμrμ
*!
****
***
*
e. pe̯r̥μ.u̯r̥μ
*!
**
**
(53)
/peμr-u̯r/
*Mar/V Dep-IO
Align-L(μ, PrWd)
*Pk/
Liq
*Pk/
Gli
μ1
μ2
μ3
μ4
F a. peμrμ.u̯r̥μ
*
**
****
*
b. peμ.ruμrμ
*
***
****!
*
c. peμ.ruμ.r̥μ
*
***
****!
*
*
d. peμrμ.u̯Vμrμ
*!
*
**
****
*****
e. pe̯r̥μ.u̯r̥μ
*!
**
****
**
Note that here and throughout the rest of this subsection we do not include
in the evaluation the candidate †pe.ru̯r̥, which shows the desired vocalization but an undesirable syllabification; the successful elimination of this
form will be taken up in 8.3. Further, we assume that the input /per-u̯r/ cannot
be faithfully realized as such—i.e., as a monosyllable †peru̯r—due to Proto-Indo-European preferences for syllable structure, the enforcement of which
will fall within the purview of Sonority-Sequencing (1f.). Finally, with
respect to syllable weight, as per moraic theory, we assume full vowels are by
their very nature moraic, hence the mora associated with *e already in the
input. On a related note, though not explicitly included here, we assume that
32
In point of fact, if such segments were ignored, the same results would be obtained,
though treating them in this way would still have to be stipulated.

<!-- pdf-page: 230; source-page: 215 -->
coda moraicity follows from ranking of the constraint *Appendix over *μ/ Consonant (cf. (17)–(19) above);33 in other words, we can easily maintain the arguably more familiar conception of moraic theory which excludes onsets from moraic structure. We have five output candidates to evaluate in these tableaux, each of which departs from the input in some way: two in which a single sonorant is vocalized, *r̥ in (52–53a.) and *u in (52–53b.); one in which both sonorants are vocalized, (52–53c.); one in which epenthesis occurs instead of vocalization, (52–53d.); and one in which both vocalization and marginalization of a non-high vowel occur, (52–53e.). As we are contemplating candidates for the posited constraint C, we have located the Alignment constraint in each tableau in the position identified for it: namely, ranked crucially over the sonoranttargeting Peak constraints, but below *Mar/Vowel (and below *Pk/ Obstruent, not included here). Furthermore, we see the importance of assessing violations of the Mora-Align constraints on the basis of segmental distance intervening between mora and prosodic word edge; moraic-based assessment of the Mora-Align constraints would result in a lack of distinction between the candidates in (52–53a.–c.), each of which would incur three violations of either Align-R(μ, PrWd) or Align-L(μ, PrWd). In the tableau in (52), Align-R(μ, PrWd) is included in the ranking, and in part due to its influence the wrong candidate is selected as most optimal, that in (52b.). The desired winner, the candidate in (52a.), loses because of one too many violations of this constraint, as its second mora is associated with the first *r and thus that much further from the relevant edge of the prosodic word. Evaluation eventually comes down to the low-ranked Peak constraints, which as we have already discussed should be inactive. On the other hand, the presence of Align-L(μ, PrWd) in the tableau in (53) does contribute to the selection of the desired winner as most optimal. By virtue of the same moraicity of the first *r, the candidate in (53a.) incurs one fewer violation of this constraint as compared to its serious competitors in (53b.–c.). If we extend our consideration to the relatively less problematic form *k̑u̯n̥bhis, which again in and of itself has found adequate analysis in Optimality-Theoretic terms by appeal to NoCoda-type constraints, we find that introduction of the constraint Align-L(μ, PrWd) into the ranking generates the desired syllabification in (54), just as NoCoda can in (55) (though we only include the latter tableau as a hypothetical comparison; as we have amply 33 Given the ranking in (52) and (53), there is no reason not to assume that *Appendix, as the higher-ranked member of this subhierarchy, occupies a position on par with highranking *Mar/Vowel.

<!-- pdf-page: 231; source-page: 216 -->
demonstrated, it is problematic to assume that NoCoda occupies such a position in the ranking, at least unaccompanied by some higher-ranked constraint
consistently forcing right-hand vocalization).34
(54)
/k̑u̯n-bhi̯s/
Dep-IO
Align-L(μ, PrWd)
*Pk/
Nas
*Pk/
Gli
μ1
μ2
μ3
μ4
F a. k̑u̯n̥μ.bhiμsμ
**
****
*****
*
b. k̑uμnμ.bhiμsμ
*
**
****
*****!
*
c. k̑uμ.n̥μ.bhiμsμ
*
**
****
*****!
*
*
d. k̑u̯Vμnμ.bhiμsμ
*!
**
***
*****
******
(55)
/k̑u̯n-bhi̯s/
Dep-IO
NoCoda
*Pk/Nas
*Pk/Gli
F a. k̑u̯n̥μ.bhiμsμ
*
*
b. k̑uμnμ.bhiμsμ
**
*
c. k̑uμ.n̥μ.bhiμsμ
*
*
*
d. k̑u̯Vμnμ.bhiμsμ
*!
**
Unlike the case of *peru̯r̥, the primary contenders for most optimal output of
the input /k̑u̯n-bhi̯s/ differ in the number of moras they contain: the candidates
in (54b.–c.) each have four moras (in two bimoraic syllables), while the candidate in (54a.) has only three (in one monomoraic and one bimoraic syllable).
As we have already discussed above, the more units there are in a given output
candidate to be assessed by these Alignment constraints, the more violations
that candidate will incur. Thus, the candidate in (54a.) wins because it has the
fewest moras, three, which means then fewer violations of Align-L(μ, PrWd).
Interestingly, because this winning candidate features fewer moras than any
of its competition, in fact it is compatible with either Mora-Align constraint:
the tableau in (56) includes Align-R(μ, PrWd) instead.
(56)
/k̑u̯n-bhi̯s/
Dep-IO
Align-R(μ, PrWd)
*Pk/
Nas
*Pk/
Gli
μ1
μ2
μ3
μ4
F a. k̑u̯n̥μ.bhiμsμ
***
*
*
b. k̑uμnμ.bhiμsμ
****
*!**
*
*
c. k̑uμ.n̥μ.bhiμsμ
****
*!**
*
*
*
d. k̑u̯Vμnμ.bhiμsμ
*!
****
***
*
34
For this very approach, see the discussion of the tableau in (60) below.

<!-- pdf-page: 232; source-page: 217 -->
In view of this finding, we note that although the form *k̑u̯n̥bhis has enjoyed
special status as the Paradebeispiel of Proto-Indo-European nucleus selection
and sonorant vocalization, in an Optimality-Theoretic approach, in which,
after Mester and Padgett, sonorants are vocalized according to how best the
result will line up with the prosodic word edge, the importance of this form
is diminished: it alone is incapable of revealing which edge is critical. More
crucial in this regard is the form *peru̯r̥, the successful analysis of which can
only be achieved with left-oriented Align-L(μ, PrWd), and not with Align-R(μ, PrWd).
At this point we should note that an important consequence of working
in an Optimality-Theoretic framework, in which output candidates are evaluated fully formed, is that application of processes of moraification and syllabification, or lack thereof, cannot effectively be relied on to differentiate
viable candidates. In other words, it is also possible to analyze the Proto-Indo-European data using Mester and Padgett’s own Syllable-Alignment constraint
schema. All the candidates we have considered in the tableaux above indeed
have syllable structure, and as such are liable to evaluation by a syllable-based
Alignment constraint.
While in Itô’s framework the direction of syllabification proved to be irrelevant once the appropriate direction of moraification was identified, we will
show that, in an Optimality-Theoretic analysis, only one variant of Mester and
Padgett’s Syllable-Alignment schema is crucially required, namely, Align-R(σ, PrWd). This constraint has been associated with languages like Cairene
Arabic, characterized as having left-to-right syllabification, or, put another way,
a preference for heavy CVC syllables to occur closer to the left edge of the prosodic word.
We begin with the form *peru̯r̥, which, as it was in the mora-based Alignment
approach, is crucial in this determination. Consider first the tableau in (57), in
which Align-L(σ, PrWd) is introduced into the constraint ranking, and the
wrong result is obtained.
(57)
/peμr-u̯r/
*Mar/V
Dep-IO
Align-L(σ, PrWd)
*Pk/
Liq
*Pk/
Gli
σ1
σ2
σ3
L a. peμrμ.u̯r̥μ
**!
*
F b. peμ.ruμrμ
*
*
c. peμ.ruμ.r̥μ
*
**!
*
*
d. peμrμ.u̯Vμrμ
*!
**
e. pe̯r̥μ.u̯r̥μ
*!
*
**

<!-- pdf-page: 233; source-page: 218 -->
Align-L(σ, PrWd) eliminates the desired winner (57a.) due to the two violations incurred by its second syllable: locating the syllable boundary after
the first *r creates a closed syllable, meaning two moras separate the second
syllable from the left edge of the prosodic word (the same result holds for
the already-eliminated epenthesis candidate (57d.) as well). On the other
hand the winner, (57b.), has an initial open syllable, meaning its second syllable incurs only one violation of Align-L(σ, PrWd). As for the candidate in
(57e.), in which the full vowel in the first syllable is marginal, and the following *r is syllabic, if not for high-ranking *Mar/Vowel, this candidate could
be favored to win. Indeed there is no way to rerank the constraints to favor
the desired winner, demonstrating that the constraint Align-L(σ, PrWd) cannot be active. If instead we introduce the alternative Alignment constraint,
Align-R(σ, PrWd), into the ranking, the desired candidate is selected as most
optimal:
(58)
/peμr-u̯r/
*Mar/V
Dep-IO
Align-R(σ, PrWd)
*Pk/
Liq
*Pk/
Gli
σ1
σ2
σ3
F a. peμrμ.u̯r̥μ
*
*
 b. peμ.ruμrμ
**!
*
c. peμ.ruμ.r̥μ
**!
*
*
*
d. peμrμ.u̯Vμrμ
*!
**
e. pe̯r̥μ.u̯r̥μ
*!
*
**
The winning candidate in (58a.) is favored, as it avoids a marginal vowel or
epenthetic segment, and, by closing its first syllable instead of its second
(unlike (58b.)), and avoiding introduction of an additional syllable by way of
vocalizing both sonorants (unlike (58c.)), it is able to achieve closer distance of
each of its syllables to the right edge of the prosodic word.
Having identified the appropriate version of the constraint, a syllable-based
Alignment analysis of *peru̯r̥ appears to be as straightforward as a mora-based
approach: no additional constraints are needed. Once we add *k̑u̯n̥.bhis into
the mix, however, we face a problem, as the tableau in (59) shows.
(59)
/k̑u̯n-bhi̯s/
Dep-IO
Align-R(σ, PrWd)
*Pk/
Nas
*Pk/
Gli
σ1
σ2
σ3
L a. k̑u̯n̥μ.bhiμsμ
**
*!
F b. k̑uμnμ.bhiμsμ
**
*
c. k̑uμ.n̥μ.bhiμsμ
***!
**
*
*
d. k̑u̯Vμnμ.bhiμsμ
*!
**

<!-- pdf-page: 234; source-page: 219 -->
Because of the nature of the input here, regardless of which sonorant is vocalized, the syllable boundary in the two most viable candidates in (59a.–b.) is
unaffected ([k̑u̯n̥]σ[bhis]σ versus [k̑un]σ[bhis]σ). This means that evaluation
falls to the lower-ranked Peak constraints, which as we have already shown
should be inert in this language; as a syllabic nasal is worse than a syllabic
glide, hence the winner is (59b.).
In order to generate the correct result, we must force the inertness of the
Peak constraints by introducing an additional constraint into the ranking,
crucially above *Pk/Nasal. As the candidates in (59a.–b.) are distinguished
not only by the sonorant which is vocalized, but also by the number of codas
contained—in favor of (59a.), which has only one—we propose to introduce
the constraint NoCoda. We thus revise the tableau in (59) accordingly, as
in (60).
(60)
/k̑u̯n-bhi̯s/
Dep-IO Align-R(σ, PrWd) NoCoda
*Pk/
Nas
*Pk/
Gli
σ1
σ2
σ3
F a. k̑u̯n̥μ.bhiμsμ
**
*
*
 b. k̑uμnμ.bhiμsμ
**
**!
*
c. k̑uμ.n̥μ.bhiμsμ
***!
**
*
*
*
d. k̑u̯Vμnμ.bhiμsμ
*!
**
**
The analysis now works. Again, active evaluation of the most viable candidates
(60a.–b.) does not end with Align-R(σ, PrWd), as both are tied in violations
of this constraint due to their initial syllable being a consistent two moras
away from the end of the word. Rather, the evaluation persists to lower-ranked
NoCoda, which eliminates (60b.) with its two codas, leaving (60a.) to emerge
as most optimal, as it minimizes both distance violations and codas (note the
ranking of NoCoda is contingent on the evaluation of *per.u̯r̥ above; in view of
*k̑u̯n̥.bhis alone, no crucial ranking with the higher constraints suggests itself).
We also note that, as an alternative to NoCoda, we could just as easily introduce the left-aligned variant of the Syllable-Alignment constraint, Align-L(σ,
PrWd), and achieve the same result:
(61)
/k̑u̯n-bhi̯s/
Dep-IO
Align-R(σ, PrWd) Align-L(σ, PrWd) *Pk/
Nas
*Pk/
Gli
σ1
σ2
σ3
σ1
σ2
σ3
F a. k̑u̯n̥μ.bhiμsμ
**
*
*
 b. k̑uμnμ.bhiμsμ
**
**!
*
c. k̑uμ.n̥μ.bhiμsμ
***!
**
*
**
*
*
d. k̑u̯Vμnμ.bhiμsμ
*!
**
**

<!-- pdf-page: 235; source-page: 220 -->
That the analysis would work even in the absence of Align-R(σ, PrWd) again
shows how crucial a form like *per.u̯r̥ is in developing an Optimality-Theoretic
account: with *k̑u̯n̥.bhis alone Align-L(σ, PrWd) (or NoCoda) would appear
to be the only necessary constraint.
Since only the Align-R(σ,PrWd)-based approach works for both *peru̯r̥
and *k̑u̯n̥.bhis, arguably any syllable-based Alignment analysis must include
it. But as we just saw, we could also make use of Align-L(σ, PrWd) in conjunction with it. The tableau in (62) demonstrates how such an account would
work for *peru̯r̥ (for *k̑u̯n̥.bhis compare (61)).
(62)
/peμr-u̯r/
*Mar/
V
Dep Align-R(σ, PrWd) Align-L(σ, PrWd) *Pk/
Liq
*Pk/
Gli
σ1
σ2
σ3
σ1
σ2
σ3
F a. peμrμ.u̯r̥μ
*
**
*
 b. peμ.ruμrμ
**!
*
*
c. peμ.ruμ.r̥μ
**!
*
*
*
*
*
d. peμrμ.u̯Vμrμ
*!
**
**
e. pe̯r̥μ.u̯r̥μ
*!
*
*
**
The constraint ranking must maintain the dominance of Align-R(σ, PrWd)
over Align-L(σ, PrWd), since otherwise the wrong result would be predicted for *peru̯r̥, namely, †pe.rur.35 This approach suggests the superfluity of
NoCoda (not included here), since it would lack an active role in the evaluation of either set of output candidates. On the other hand, as we have seen,
NoCoda could just as easily play a crucial role in selecting *k̑u̯n̥.bhis, if we
omit Align-L(σ, PrWd) from the ranking; so one could equally well consider
Align-L(σ, PrWd) to be unneeded. Which constraint might we eliminate,
then? We propose that the account of Proto-Indo-European following Mester
and Padgett’s syllable-based approach should maintain NoCoda as opposed
to Align-L(σ, PrWd). Considering the fact that Align-R(σ, PrWd) is apparently essential regardless, it would arguably be more intuitive to bundle it
35
We can compare the situation in Cairene Arabic, as analyzed by Zawaydeh (1997: 203–
206): this language requires Align-R(σ, PrWd) to account for epenthesis patterns, but
Align-L(σ, PrWd) to account for syncope patterns; in each case the alternative constraint will not work. This presents a paradox in ranking, as high-ranking Align-R(σ,
PrWd) would select the wrong result for syncope, while high-ranking Align-L(σ, PrWd)
would select the wrong result for epenthesis. As we can see, this is not the case in Proto-Indo-European, in which Align-R(σ, PrWd) can safely outrank Align-L(σ, PrWd) with
no ill effect.

<!-- pdf-page: 236; source-page: 221 -->
with another constraint making reference to a right edge, namely, NoCoda (as we saw from Kobayashi’s work, this constraint can be schematized as Align-R(Nuc, σ), ‘Align the nucleus with the right edge of the syllable’),36 instead of a constraint oriented to an opposite edge.37 It is also of course the case that NoCoda is a constraint whose cross-linguistic credentials have been well-established in the literature; this too may be viewed as a point in favor of its inclusion over Align-L(σ, PrWd). In any case, the more important finding to take away from this discussion is the fact that syllable-based Alignment requires an additional constraint to capture the data, whereas mora-based Alignment does not: so far as we have seen, Align-L(μ, PrWd) alone can generate the correct results. Incidentally, we have seen here that indeed both *k̑u̯n̥bhis and *peru̯r̥ feature right-hand sonorant vocalization, but only the former works with Mester and Padgett’s original, unadjusted analysis of right-to-left syllabification. Why should this be so? A key feature distinguishing *k̑u̯n̥bhis from *peru̯r̥ is the fact that regardless of which sonorant is vocalized in the former (assuming only one is), the syllable boundary is unaffected ([k̑u̯n̥]σ[bhis]σ versus [k̑un]σ[bhis]σ). For *peru̯r̥, however, which sonorant vocalizes directly affects the syllable structure ([per]σ[u̯r̥]σ versus [pe]σ[rur]σ). Once the initial syllable of this form is made heavy as a result of right-hand sonorant vocalization, the desired syllabification is disfavored by Align-L(σ, PrWd).
#### 8.2.2.2.3 Further Thoughts on Mora- versus Syllable-Based Alignment
Applying Ito’s framework to Proto-Indo-European in 8.2.2.2.1, we saw the importance of differentiating directionality in sonorant vocalization (nucleus selection) from directionality in syllable structure assignment, even if the two phenomena appear to be intimately related.38 Yet, given the nature of Optimality Theory, in which fully-structured candidates are evaluated—that is, the processes of moraification and syllabification cannot effectively be distinguished—we have also found it possible to subject the same output candidates to analysis using Mester and Padgett’s syllable-based Alignment constraint schema and our proposed mora-based Alignment constraint schema, 36 Although whether this formulation requires the positing of an explicit nucleus constituent is an issue requiring further consideration. 37 Again, cf. Zawaydeh’s (1997: 203–206) claim that alignment to both edges is a priority for Cairene Arabic, albeit for two different phenomena. 38 Cf. Itô (1989: n. 30), who notes cases of parallelism in directionality effects, such as between metrical structure building and syllabification in Cairene and Iraqi Arabic (both proceed left to right for Cairene and right to left for Arabic), and between syllabification and nonconcatenative morphology in Temiar, which both operate right to left.

<!-- pdf-page: 237; source-page: 222 -->
and achieve the same results. That such alternatives are possible compels us
to consider in the immediate context which Alignment approach provides the
best fit for Proto-Indo-European.
Perhaps the most obvious criterion to consider in assessing the elegance of
the competing analyses of Proto-Indo-European is the number of constraints
required to generate all the desired results. To better appreciate the difference
in the two accounts, in the following table we summarize, given the Alignment
constraint in the leftmost column as a starting point, the additional constraints
required for a successful analysis of the two forms which have figured prominently in our discussion, *peru̯r̥ and *k̑u̯n̥bhis.
(63)	 Required Constraints in Syllable- vs. Moraic-Alignment Systems
*per.u̯r̥
*k̑u̯n̥.bhis
Align-R(σ, PrWd)
—
NoCoda / Align-L(σ, PrWd)
Align-L(μ, PrWd)
—
—
Using only Align-R(σ, PrWd) after Mester and Padgett, *per.u̯r̥ can be
accounted for, but we are compelled to include in addition either the constraint NoCoda or the constraint Align-L(σ, PrWd), so as to account for
*k̑u̯n̥.bhis. On the other hand, no additional constraints are needed using the
proposed mora-based Align-L(μ, PrWd).
We can supplement these considerations with some additional data. We
begin with the genitive singular form of ‘dog’, *k̑u.nos (> Gk. κυνός). This form
shows that right-hand sonorant vocalization is blocked when the following
segment is a vowel, suggesting a dispreference in the language for hiatus and
onsetless syllables. The tableaux in (64)–(65) illustrate how the syllable-based
and mora-based Alignment approaches, respectively, handle *k̑u.nos.
(64)
/k̑u̯n-oμs/
Dep-IO
Align-R(σ, PrWd)
NoCoda
*Pk/
Nas
*Pk/
Gli
σ1
σ2
σ3
a. k̑u̯n̥μ.oμsμ
**
*
*!
F b. k̑uμ.noμsμ
**
*
*
c. k̑uμ.n̥μ.oμsμ
***!
**
*
*
*
d. k̑u̯Vμ.noμsμ
*!
**
**

<!-- pdf-page: 238; source-page: 223 -->
(65)
/k̑u̯n-oμs/
Dep-IO
Align-L(μ, PrWd)
*Pk/
Nas
*Pk/
Gli
μ1
μ2
μ3
μ4
a. k̑u̯n̥μ.oμsμ
**
***
****!
*
F b. k̑uμ.noμsμ
*
***
****
*
c. k̑uμ.n̥μ.oμsμ
*
**
***
***!*
*
*
d. k̑u̯Vμ.noμsμ
*!
**
****
*****
As can be seen, while the syllable-based account does actually select the correct output in (64), it does so only by resorting to the constraints whose influence we have sought to neutralize: the low-ranked sonorant-targeting Peak
constraints. If the position of the glide and nasal were reversed, we would
still expect the left-hand sonorant in this case to vocalize, suggesting that the
analysis cannot stand as is. Rather, here we are motivated to introduce the constraint Onset (1g.), ranked at least above *Pk/Nasal:
(66)
/k̑u̯n-oμs/
Dep-IO Align-R(σ, PrWd) Onset NoCoda *Pk/
Nas
*Pk/
Gli
σ1
σ2
σ3
a. k̑u̯n̥μ.oμsμ
**
*!
*
*
F b. k̑uμ.noμsμ
**
*
*
c. k̑uμ.n̥μ.oμsμ
***!
**
**
*
*
*
d. k̑u̯Vμ.noμsμ
*!
**
**
Note that, once we have introduced Onset into the ranking, we have a
means of ruling out an additional candidate not included here, namely
†k̑un.os, which, differing from the optimal output only in the syllabic affiliation of the nasal, would, absent this constraint, fare just as well in the
evaluation.
As for the mora-based Alignment approach depicted in (65), it also generates the correct result, but does so without appeal to the low-ranking Peak
constraints. Because fewer moraic segments mean fewer violations overall, the
candidate in (65b.) wins the evaluation, since the nasal is not vocalic (as in
(65d.)), and hence not moraic. Note that if the nasal were a coda consonant—
as in †k̑un.os—it would also be moraic, meaning that the constraint Align-L(μ, PrWd) could successfully eliminate this form from the competition as
well. In view of these findings, we revise the table presented in (63) above as
follows.

<!-- pdf-page: 239; source-page: 224 -->
(67)	 Required Constraints in Syllable- vs. Moraic-Alignment Systems (Updated)
*per.u̯r̥
*k̑u̯n̥.bhis
*k̑u.nos
Align-R(σ, PrWd)
—
NoCoda (/ Align-L(σ, PrWd))
Onset
Align-L(μ, PrWd)
—
—
—
While at this stage the moraic-based Alignment approach continues to
be most attractive in view of its requiring the fewest number of additional
constraints—none—to accommodate the forms considered thus far, this distinction breaks down in view of the environment we turn to now. Because
we have assessed violations of Align-L(μ, PrWd) in terms of segments, and
because this constraint is left-edge-oriented, the segment at this edge of the
prosodic word can be moraic essentially for free—such a mora will incur no
violations, as there are no segments intervening between the word edge and
the segment it dominates. The constraint therefore cannot distinguish between
the candidates as in (68), differing only in the moraicity of the initial segment:39
(68)
/RRCV/
Align-L(μ, PrWd)
μ1
μ2
F a.	 RμRμCV
*
F b.	 RRμCV
*
While the violation profiles of the two candidates may differ at the level of
the mora, more relevant for the purposes of the evaluation is the fact that,
overall, each incurs one violation apiece of the constraint Align-L(μ, PrWd).
Practically speaking, this means that, although we want the candidate type
in (68b.) to emerge as most optimal, the mora-based Alignment approach as
developed thus far has no means of ruling out the vocalization of an initial
sonorant in situations in which we expect that a following sonorant should
vocalize instead.
39
We omit from consideration a logically possible third candidate, RμRCV, in which only the
initial sonorant is moraic, as we believe it would be disfavored by higher-level preferences
involving sonority sequencing and/or the moraicity of (sonorant) codas.

<!-- pdf-page: 240; source-page: 225 -->
For a concrete example of this issue, consider the tableau in (69), for the
present stem *mn̥-i̯é- (Ved. mányate) built to the root 1.*men- ‘think’ (LIV 435–
436; IEW 726–728).40
(69)
/mn-i̯eμ-/
Dep-IO
Align-L(μ, PrWd)
*Pk/Nas
*Pk/Gli
μ1
μ2
μ3
μ4
a. mniμ.eμ**
***!
*
F b. mn̥μ.i̯eμ*
***
*
F c. m̥ μnμ.i̯eμ*
***
*
d. mn̥μ.iμ.eμ*
**
**!*
*
*
e. m̥ μ.niμ.eμ**
***!
*
*
f. m̥ μ.n̥μ.i̯eμ*
***
**!
g. m̥ μ.n̥μ.iμ.eμ*
**
**!*
**
*
h. mVμnμ.i̯eμ*!
*
**
****
As we can see, the schematic string RμRμC in (68a.) is ambiguous, in that it
can actually correspond to at least two possible syllabifications, assuming the
moraicity of coda consonants—either the syllabification R̥μRμ.CV, in which
the initial sonorant is syllabic and the second sonorant is a coda (exemplified by the candidate in (69c.)), or the syllabification R̥μ.R̥μ.CV, in which both
sonorants are syllabic and wholly constitute their own syllables (exemplified
by the candidate in (69f.)). As we expect, the constraint Align-L(μ, PrWd)
assesses both of these candidates equally—each incurs four violations arrayed
across the same moraic structure (but not the same syllable structure)—and
between them and the candidate in (69b.), which exemplifies the schematic
string RRμC in (68b.) and also incurs four violations, is incapable of selecting
a single most optimal output. Although ultimately the evaluation presented
here comes down to the two candidates in (69b.–c.), once the lower-ranked
Peak constraints come into play—the two syllabic nasals of the candidate in
(69f.) serve to eliminate it from competition—resorting in such a way to these
constraints is an undesirable outcome, as it suggests that if the initial sonorant
were instead a sonorant of higher sonority, the candidate in which it vocalizes
40
Note in all candidates featuring a single medial consonant—*n in (69e.), *i̯ in (69f.)—
this consonant is grouped with the syllable headed by the following vowel. Such practice, as we have seen in the case of *k̑unos, conforms with the preferences of Align-L(μ,
PrWd), as fewer moraic segments mean fewer violations. On the other hand, ostensibly in
spite of this constraint, in all candidates featuring a medial consonant sequence—*-ni̯in (69c., h.)—this sequence is split up across syllables, as we have argued to hold also in
the case of *per.u̯r̥ (†pe.ru̯r̥). For more on heterosyllabification, see the discussion in 8.3.

<!-- pdf-page: 241; source-page: 226 -->
would be favored, when ideally it should be the second sonorant, again regardless of relative sonority.
To resolve this issue, we need a constraint like Onset. Its effect can be seen
in the tableau in (70).
(70)
/mn-i̯eμ-/
Dep-IO
Align-L(μ, PrWd)
Onset
*Pk/Nas *Pk/Gli
μ1
μ2
μ3
μ4
a. mniμ.eμ**
***!
*
*
F b. mn̥μ.i̯eμ*
***
*
 c. m̥ μnμ.i̯eμ*
***
*!
*
d. mn̥μ.iμ.eμ*
**
**!*
**
*
*
e. m̥ μ.niμ.eμ**
***!
**
*
*
f. m̥ μ.n̥μ.i̯eμ*
***
*!*
**
g. m̥ μ.n̥μ.iμ.eμ*
**
**!*
****
**
*
h. mVμnμ.i̯eμ*!
*
**
****
We can also update the summary table introduced in (63) and revised in (67)
as follows:
(71)	 Required Constraints in Syllable- vs. Moraic-Alignment Systems (Updated
Further)
*per.u̯r̥
*k̑u̯n̥.bhis
*k̑u.nos
*mn̥.i̯e-Align-R(σ, PrWd)
—
NoCoda (/ Align-L(σ, PrWd))
Onset
Onset
Align-L(μ, PrWd)
—
—
—
Onset
Onset is common now to both approaches. Importantly, once this constraint
is introduced into the ranking, it becomes more difficult to differentiate an
account built on Mester and Padgett’s syllable-based Align-L(σ, PrWd) from
one built on our proposed Align-L(μ, PrWd). The fact that, given the set of
data we have considered so far here, more forms require the inclusion of this
constraint under the former approach compared to the latter one is inconsequential; regardless of how little or how much work it does, once Onset is part
of the analysis, it is part of the analysis.

<!-- pdf-page: 242; source-page: 227 -->
At this point, then, we find that the syllable-based Alignment approach requires one more constraint than the mora-based Alignment approach does to account for the same breadth of data. Barring any as yet unseen advantages the former approach may boast over the latter one, we therefore choose to maintain, moving forward, the mora-based approach, because of the fact that it does require fewer constraints to be introduced, subsuming the role played by NoCoda (and/or Align-L(σ, PrWd)). Another potential asset of the morabased approach we have developed here, as opposed to Mester and Padgett’s syllable-based approach, is the prominence it assigns to the left edge of the prosodic word. Indeed, initial position in Proto-Indo-European is privileged in a number of phenomena, such as the νεογνός rule (Weiss 2009b: 113), and, as we will claim in the next subsection, in the distribution of complex onsets, so its privileged status in the phenomenon of sonorant vocalization would not be in isolation.
