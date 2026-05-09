---
title: "Germanic Phylogeny"
author: "Frederik Hartmann"
date: "2023"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "hartmann-2023.pdf"
chunk: "Chapter 1"
pages: "1-9"
---

# 1 Introduction


<!-- source-page: 1; pdf-page: 20 -->
1
              Introduction


The linguistic history of the Germanic languages is among the best understood
areas in the field of historical linguistics. Since the early days of linguis-
tic investigations, generations of researchers have provided the foundation
of what we know today. We have reconstructed the Germanic protolan-
guage Proto-Germanic (PGmc) to a degree where gaps in our knowledge are
only found on minor or peripheral issues, at least as regards the phonology,
morphology, and lexicon of the language.
  But despite this detailed coverage, Germanic phylogeny (i.e. the linguistic
relatedness within the family) is comparably unclear. The reasons for this is
that early Germanic linguistics faces what can be described as a black-box
problem. We can reconstruct Proto-Germanic in detail but the earliest exten-
sive textual evidence, except minor text fragments in runic inscriptions, is
not attested for at least 800 years (even more than 1,000 for some languages)
after the demise of Germanic linguistic unity. This leaves a gap of many hun-
dred years in the records which can only be filled by investigating the later
attested languages and reconstructing their possible diversification from a
somewhat coherent unity into the individual daughters.
  Germanic linguistic research has also yielded insights into the further sub-
grouping of the family. We have a fairly good understanding that there are
North and West Germanic subgroups that are themselves descended from
a Northwest Germanic clade (cf. Grønvik 1998: 134–135; Seebold 2013).
Unfortunately, this grouping is rather coarse given that the language family
comprises at least six well-attested and diverse daughters from which the mod-
ern Germanic languages descend. Not only is this subgrouping in itself coarse,
but solely assigning languages to these subfamilies does not yield insights
into how these subfamilies evolved out of the common ancestor of Proto-
Germanic. Those endeavours that aim at shedding light on the questions in
detail are often very much debated. Some of the current issues can be listed in
the following comprehensive overview.
  The earliest definable—now commonly accepted—subgroup  is that of
Northwest Germanic, yet the language that  is excluded from Northwest
Germanic, Gothic, is often assigned to a coarsely defined ‘East Germanic’.

<!-- source-page: 2; pdf-page: 21 -->
However, the notion of East Germanic as a Germanic subgroup next to North-
west Germanic has been called into question (e.g. Hartmann 2020; Hartmann
and Riegger 2022). Moreover, what was the situation that yielded the split
between these groups? Some have argued that the split was brought forth by
Northwest Germanic undergoing certain subgroup-defining changes that left
behind a conservative East Germanic (e.g. Grønvik 1998: 148). Yet it is still
unclear whether the data warrant such conclusions as such a notion requires
finding clear innovations indicative of a common development among the East
Germanic languages which is not the case (see e.g. Hartmann 2020: 115–124).
Furthermore, various smaller Germanic languages such as Burgundian and
Vandalic have rarely been scrutinized regarding their position in the family
and are often assumed to be ‘East Germanic’ without a clear definition of what
this subgroup constitutes.
  Having established that Northwest Germanic is its own subgroup, the ques-
tion arises of why we find so few Northwest Germanic innovations and what
this implies about the earliest diversification of Germanic.
  Even within Northwest Germanic, especially as pertaining to West Ger-
manic, we find a long-standing debate about whether or not West Germanic
constitutes a protolanguage which would in turn suggest the West Germanic
languages to either descend from a fairly homogeneous subgroup or from a
loosely connected dialect continuum. This issue is connected to two somewhat
linked debates about the validity of further subgroups such as Anglo-Frisian or
Ingvaeonic (for a comprehensive overview see Stiles 1995). It becomes increas-
ingly clear that we have to see Germanic, and especially West Germanic, as a
highly connected area where contact and horizontal transmission of changes
frequently occurs and for which it is difficult, if not impossible, to draw clear
family trees.
  Given these problems, I consider research into the Germanic languages to
be in need of a thorough investigation using methods that go beyond, but com-
plement, the traditional methods. Computational research has received much
attention in historical linguistics in recent decades as the field of linguistics
in its entirety moves towards increased use of quantitative and computational
models. The advancement of widely available computational resources and
methods calls for a detailed examination of early Germanic linguistics.
  The study at hand attempts to be such an investigation. The goal, as will be
more precisely defined in later sections, is to apply both computational tree-
based phylogenetic and wave-model oriented approaches to the Germanic
family to gain novel insights in long-standing debates. In this, I will apply
both previously used Bayesian phylogenetic models to the problem and create

<!-- source-page: 3; pdf-page: 22 -->
1.1 A NOTE ON THE DEFINITION OF THE TERM CLADISTICS  3

a novel algorithm which represents a computational implementation of the
wave model by means of agent-based simulations modelling linguistic spread,
geographical factors, and diachrony. In some sense, the study itself therefore
pursues two aims: modelling Germanic linguistic diversification up to the ear-
liest attested languages and presenting and evaluating a novel approach that
can be used as a method to model linguistic diversification based on wave-like
transmission.
  The investigation is therefore chiefly computational, drawing heavily on
previous research in historical Germanic linguistics. Without the thorough
work of generations of researchers, it would not be possible for the models
to build on this knowledge. This, however, entails that the study predomi-
nantly discusses linguistic issues and issues pertaining to Germanic phylogeny
on a meta-level. In other words, examining the intricate details of certain lin-
guistic changes as arguments for a specific subgrouping is beyond the scope
of this endeavour. This is not to say that detailed analysis is irrelevant, but
rather that the methods and the viewpoint of the present investigation build
on these previous studies rather than re-examining the evidence in detail. The
conclusions about Germanic phylogeny therefore stem from a confluence of
previous research and novel methods building on this research to obtain a
clearer picture of certain issues.
   It needs to be stressed that this work seeks not to replace previous research
by computational models but attempts to thoroughly investigate the problem
at hand using quantitative and computational methods based on traditional
research to enrich the picture with powerful tools in order to improve our
understanding of these processes.

        1.1 A note on the definition of the term cladistics

The term ‘cladistics’ does not, as of yet, have a fixed definition in diachronic
linguistics and is sometimes used interchangeably with ‘phylogenetics’. For
this reason, I henceforth adopt the following definitions: ‘Linguistic cladistics’
as used in this book describes the linguistic inquiry into language relation-
ships based on the (commonly accepted) assumption that languages descend
from one another and linguistic families diversify from a common ances-
tor.¹ ‘Linguistic phylogenetics’ is a way of studying cladistical relationships

    ¹ Note that in this definition, the process of the descent is unspecified, meaning that not just tree-like
diversification models can be used in cladistical investigations. Hence, cladistics contains investigations
of genetic relationships between languages without assumptions about the shape of the descent process.

<!-- source-page: 4; pdf-page: 23 -->
by employing methods that model linguistic traits across time to analyse
phylogenies, chiefly in the form of evolutionary tree models.

   1.2 Summary of cladistical theories concerning Germanic
                      subgroupings

Over the decades, there have been a number of theories regarding poten-
tial subgroupings of the Germanic languages. The most prominent of the
discussed theories are summarized here to outline the basic proposals and
their research history. Note that these proposals are reviewed in detail in
sections 5.1 to 5.6.

      1.2.1 North Germanic, West Germanic, East Germanic

The first and earliest grouping of the Germanic languages was a tripartite split
of the Germanic languages in North, West, and East Germanic languages.
This notion can be found in the earliest linguistic research, for example in
Krahe (1948); Prokosch (1939); Schleicher (1860); Wrede (1886). This idea
was based both on linguistic considerations but also on Roman and Greek
historiographic work where, for example, we find the proposal of a common
origin of the ‘Gothic peoples’, among which the East Germanic languages
were counted (cf. Braune and Heidermanns 2004: 4). Very early, the tripartite
division of Germanic was challenged from multiple angles with researchers
proposing two potential further subgroupings of the three languages: Gotho-
Nordic and Northwest Germanic.² To this day, the tripartite division is still
found as the basic assumption of Germanic subgrouping in many books and
studies, including introductory works.

                         1.2.2 Gotho-Nordic

A close relationship between Gothic (or East Germanic in general) and North
Germanic first was appealing to many early researchers who based their
investigations partly on historiographic work (cf. Grønvik 1998: 70). In his
Getica, Jordanes uses the foundational myth of Gothic origins in Scandinavia
(cf. Miller 2019: 1–2) which, were this to be believed, would warrant closer

   ² There is also the notion that East and West Germanic were more closely related (see e.g. Kortlandt
2001), yet since this theory has never in the past had a strong following, I omitted the proposal at this
point. I do not consider it further here.

<!-- source-page: 5; pdf-page: 24 -->
1.3 COMPUTATIONAL MODELLING OF THE GERMANIC LANGUAGES  5

inspection of Northeast Germanic relations. Further, some supposed linguistic
changes common to Gothic and Old Norse brought the Gotho-Nordic hypoth-
esis some adherents (e.g. Schwarz 1951; Krahe and Meid 1969: 37–38), yet it
was ultimately abandoned in the common consensus in favour of Northwest
Germanic.

                      1.2.3 Northwest Germanic

Northwest Germanic is the commonly accepted second-order subgrouping of
Germanic at least starting with Kuhn (1955), which proposes a closer relation-
ship of the North and West Germanic languages to the exclusion of Gothic.
Examples for such changes are, for instance, lowering of earlier *ē to *ā or
the loss of several inflectional categories (see Ringe and Taylor 2014: 10–24).
Although this theory is accepted in most contemporary research, criticisms
of the concept are found in earlier research (chiefly pre-1980) suggesting
alternative groupings such as Gotho-Nordic.

                 1.2.4 Ingvaeonic and Anglo-Frisian

Further subgroupings have been proposed predominantly in the context of
West Germanic with Ingvaeonic being a subgroup consisting of Old Saxon,
Old English, and Old Frisian (e.g. Schwarz 1951), and Anglo-Frisian which
is proposed by some as a linguistic ancestor to Old English and Old Frisian
(for an extensive survey see Nielsen 1981). However, the research history into
these subgroupings is intricate as Old Saxon is suggested to be a hybrid lan-
guage which does not fit perfectly into an Ingvaeonic subgroup (e.g. Nielsen
1989: 79). Moreover, some have cast doubt on whether or not the languages
can in fact be regarded as related via their own linguistic ancestors or whether
their similarities are due to geographical proximity and membership of a larger
dialect continuum (e.g. Stiles 1995, 2013).

    1.3 Computational modelling of the Germanic languages

There have been computational studies in the past investigating Germanic
phylogeny at least as a by-product of their analyses.
  Among the  first quantitative attempts to model early Indo-European
language relatedness was Ringe, Warnow, and Taylor (2002) who base their

<!-- source-page: 6; pdf-page: 25 -->
investigation on a lexical dataset. The results of their findings do not contain
Germanic interrelationships but cast light on some of the difficulties of placing
Germanic in a larger Indo-European family tree.
  In the early 2000s, Gray and Atkinson (2003) published a Bayesian phylo-
genetic study that received much attention in the following years with many
researchers heavily criticizing the approach for a variety of reasons (e.g. Chang
et al. 2015; Pereltsvaig and Lewis 2015). In this study, they attempt to date
the break-up of the Indo-European languages in order to investigate the ques-
tion of the most likely Indo-European homeland. They eventually estimate
an early date for the Indo-European disintegration, 8,700 years before present
(Gray and Atkinson 2003: 437), thus concluding the Anatolian homeland the-
ory to be correct. Their analysis also includes the Germanic languages, albeit
only in the form of modern variants, inferring a split between North and West
Germanic languages 1,750 years before present.
  As a Bayesian phylogenetic reevaluation of the Gray–Atkinson model,
Chang et al. (2015) presented a study which provided evidence against their
claim using a model incorporating fixed ancestral states. In particular, the
authors constrained certain extinct languages in their dataset to be treated
as ancestor nodes of extant languages (e.g. Latin as an ancestor node of the
Romance languages). In the Germanic branch of their model results, they
arrive at the traditionally assumed Gothic–Northwest Germanic split with a
further division of Northwest Germanic into a branch containing English,
Dutch, and German and a lineage comprised of, among others, Norwegian
and Swedish.
  More recent studies, such as Verkerk (2019), aim at a compromise between
strictly tree-like structures common in Bayesian phylogenetics and notions of
other forms of diversification, namely horizontal contact and linguistic spread.
The ideas to display a language family—in this case Germanic—as a horizontal
diversification process (‘wave-like’) is not unique to computational modelling.
Traditional linguistics has debated the wave theory since it was proposed by
scholars such as Schmidt (1872) and applied to Germanic language relatedness
(e.g. Kufner 1972). Today, the notion is that Germanic can be understood as a
chain of dialects occupying a defined geographical area (Roberge 2020). This
assumption of Germanic as a dialect continuum raises the question whether or
not it would be beneficial to further the understanding of this language family
by computationally modelling the development of the Germanic languages
as a gradual diversification process, starting from a geographically influenced
dialect continuum.

<!-- source-page: 7; pdf-page: 26 -->
1.4 WAVE MODEL, TREE MODEL, AND GERMANIC PHYLOGENY  7

     1.4 Wave model, tree model, and Germanic phylogeny

The process of linguistic development from a common ancestor language has
often been framed as running along two different models of linguistic descent:
the tree and wave models.
  The origins of the viewpoints of tree and wave models can be traced back
to research into Indo-European linguistic relationships in the mid-nineteenth
century. One of the researchers, to whom an early version of the tree model
idea is attributed, is August Schleicher who was among the first to describe
Indo-European cladistics using a family tree (Schleicher 1860). A short time
later, Schmidt (1872) put forth the theory of a wave-like diversification of the
Indo-European languages, suggesting that languages emerge through over-
laying isoglosses rather than through splitting from an earlier ancestor. The
diagram below shows the most widely accepted family tree of Germanic with
the second-order grouping Northwest Germanic.

                      PGmc


               EGmc       NWGmc


                      WGmc  NGmc

                            Traditional family tree

  The wave model itself has never received a commonly accepted definition
as the tree model had but most current research encompassing aspects of
wave-like relationships define the wave model as a model which uses inter-
secting isoglosses to define linguistic subgroups. These concepts are closely
related to the notions behind dialect geography which investigates the geo-
graphical distribution of languages, variants, and linguistic features in a given
area or for a given linguistic family. For Germanic, Nielsen (1989: 116–133)
summarizes the earlier research into dialect-geographical aspects of early
Germanic.
  The wave theory describes a diversification process in which innovations
occur in a linguistic community and spread through the area either encom-
passing all members (or sub-units) of the speech community or stopping
earlier, thus only affecting a subset of members. When repeated multiple times

<!-- source-page: 8; pdf-page: 27 -->
with multiple innovations, this process yields a linguistic area that is char-
acterized by overlaying innovations. As a result, areas will arise that tend to
share more innovations with their nearest neighbours than with communities
farther away by virtue of more intensive contact and exchange.
  While in earlier research, both models were seen as mutually exclusive, more
recent overviews point out that both capture different aspects of linguistic
diversification (e.g. Hock 1991: 454).
  The emergence of linguistic subgroups through innovation spreading has
strong ties to the geographical space they occur in, as shown in recent Labo-
vian sociolinguistic studies (summarized in Labov 2001: 35–73). Although lin-
guistic spread is not (always) congruent with geographical distance, the spread
of an innovation permeating through a speech community which eventually
dies out is less likely to affect communities at the other end of the dialectal
region. Knowledge of the geographical position therefore complements and
aids the modelling of the diversification process in question.
  Some approaches forego the geographical component and rely solely on lin-
guistic data, such as historical glottometry (as presented in François 2015) (see
section 6.2).
  While the wave models come closer to how certain languages diversify
into subgroups, especially in high-contact and close proximity situations, they
are considered to be less easily visualized and harder to summarize with a
small number of parameters. Tree models, on the other hand, can be regarded
as easier to interpret. This is especially true for the dimensionality of the
display. Whereas trees are by definition two dimensional, exhibiting unidirec-
tional branches which can have a certain length and a determinable split time
and ordering. Wave-like diversification processes, at least in the most simple
definition, operate in three dimensions: two dimensions for the geographical
spread of the waves with one temporal dimension for the development of the
spread of innovations over time, whereas by definition, wave model diagrams
are necessarily two-dimensional (see for discussion Anttila 1989: 300–310).
This makes them inherently more complex and less well interpretable. More-
over, from a modelling perspective, a linguistic stemma is more clear and
less complicated to devise for a given family, as they mostly only require
approximate estimates of similarity and linguistic history of each branch to
be collected. Wave-model displays rely on either certain distance measures or
measures of group coherence, or they require the researcher to plot a large
number of isoglosses on a geographical map. A study that previously used geo-
graphical information incorporated in a phylogenetic model is Bouckaert et al.
(2012).

<!-- source-page: 9; pdf-page: 28 -->
1.4 WAVE MODEL, TREE MODEL, AND GERMANIC PHYLOGENY  9

  With the advent of computational methods in linguistics and large compu-
tational resources being readily available, more complex problems that could
not be analysed with earlier methods are now in reach.
  Germanic is, in some ways, a model case for this issue as the diversifica-
tion of certain Germanic subgroups is increasingly seen as a diversification
of dialect continua in more recent literature (e.g. Seebold 2013; Stiles 2013).
Moreover, the family is reasonably well-understood and recent such that we
have large datasets and a rich research history which makes it ideally suited
to being analysed quantitatively. The present study therefore aims to present
a computational wave-model approach that has previously not been applied
in cladistics. It is a computational agent-based implementation of the wave
theory taking into account temporal and diachronic aspects. In this, it is dis-
tinct from previous implementations such as historical glottometry insofar as
it operates on computational simulations, statistical principles, and specifi-
cally aims at modelling the diversification process rather than displaying single
numerical relationships between languages in the form of subgroups.
  In short, the approach rests on multiple individual simulations of the Ger-
manic diversification process under the assumption of wave-like innovation
spreading. Those simulations that show an isogloss pattern that comes close
to the observed linguistic data can then be further analysed to see if there
are common patterns of diversification under these best-fit simulations. These
simulations take in the factors of time, geography, and linguistic features
to approximate the spreading process in order to reconstruct the possible
pathways of how the disintegration unfolded.
