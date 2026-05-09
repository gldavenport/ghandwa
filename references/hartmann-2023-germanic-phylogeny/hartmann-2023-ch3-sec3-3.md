---
title: "Germanic Phylogeny"
author: "Frederik Hartmann"
date: "2023"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "hartmann-2023.pdf"
chunk: "§3.3"
pages: "76-78"
---

# 3.3 Beyond phylogenetic tree inference


<!-- source-page: 76; pdf-page: 95 -->
detectable via an episodic rate change model. A global speciation setting is suf-
ficient to account for the data. This does not mean that, in reality, there were
no changes in the rate of speciation and extinction. On the contrary, one might
hypothesize that during late antiquity, where population movements occurred
that might or might not have been unusually large, we might see an increase
in speciation (i.e. more languages breaking away from larger linguistic units)
at least regarding those languages that were spoken in migrating communi-
ties such as Gothic, Vandalic, and Burgundian. In this analysis, however, these
potential changes in speciation rates are not detectable because they are likely
too minor to be visible in a dataset of this size and scope.
  The coherence of the dataset with regard to the individual substitution rates
across different sites is rather homogeneous with a mean α value of 30. As a
result, we can assume that the rate difference per site is not flat but rather has
most of the probability mass at around 1. It is, however, not strong either as
would be the case for values of α > 100. We can therefore conclude that the
substitution rates differ across sites but not by large values which means in
effect that the underlying changes occur at similar rates.
   Lastly, the inferred dates for the root age and the sufficiently supported splits
indicate an early date of the entire tree. Whereas the root age interval is sam-
pled to be between 2.15 and 2.7 (between 700 and 150 BC), the mean and
median ages at approximately 2.45 (450 BC) are on the early end of most pre-
vious estimations pointing to a date later than 500 BC for the break-up of
Proto-Germanic. Similarly, the splitting of the West Germanic languages is
estimated by the model to have occurred between 170 BC and 370 AD, which
is early compared with most previous estimates.


            3.3 Beyond phylogenetic tree inference

The insights gained from the phylogenetic models have shown a rather incon-
clusive picture regarding subgrouping in the Germanic language family. This
is not unprecedented as previous phylogenetic inference studies have also
encountered similar problems. It becomes clear that the possible subgroups in
Germanic do not exhibit sufficient differentiation with regard to the under-
lying data. This issue therefore needs to be taken as the basis of further
investigation as we have seen that phylogenetic analysis alone does not yield
reliable results for Germanic. The current phylogenetic models may therefore
be complemented by focusing on certain aspects where alternative models can
yield further insights.

<!-- source-page: 77; pdf-page: 96 -->
3.3 BEYOND PHYLOGENETIC TREE INFERENCE  77

  A spatial component, although newer approaches incorporate geospatial
elements in their models (see Ree et al. 2005; Landis et al. 2013), would
improve the subgrouping insofar as geographic distance and subgrouping is
likely to be correlated to some degree.²⁴ That is, distant speech communities
are less likely to undergo common changes and some type of changes such
as areal spreading affects far-apart communities less by definition.²⁵ However,
accounting for this distance was not incorporated in the Bayesian phylogenetic
model at hand which is agnostic of geographic distribution. It is worth noting
that this aspect is not a criticism of the model per se, as in some cases it might
be advantageous to leave out the geographic component to investigate the rela-
tionship estimates that were inferred independently of geographic proximity.
It is advisable to consider comparing a geospatially agnostic model with spa-
tial models in any analyses to investigate the effect of geographic parameters
themselves.
  Nevertheless, geographical distance further is a factor in the emergence
of new subgroups beyond the pure processes of innovation spreading but
isolation of linguistic communities—whether due to migration, geographic
barriers, or even social processes—likewise contributes to this issue.
  Furthermore, Bayesian phylogenetics assumes ‘hard’ splits in every individ-
ual tree as do all tree-based models, the practice of which has been criticized
in light of the debate around the adequacy of the tree model (see section 1.4).
The split time intervals can be interpreted as a ‘softer’ diversification process,
yet the underlying mechanic assumes trees that assume clear, sudden splits
for the clades. Assuming a hard-splitting tree model as a necessary abstrac-
tion from the real-world process is legitimate, however, yet certain conditions
have to apply in this case. Specifically, if languages diversify in such a way that
the diversification process is short enough that, out of this gradual diversifica-
tion, no significant innovations arise that obscure the genetic relationships in
a tree-based inference model, then a hard split is a good model for this process.
  Adjacent to this issue is the assumption of bifurcating splits in these models.
Rapid consecutive splits may be interpreted as a simultaneous diversification
process but again, the models themselves only assume bifurcation.²⁶


   ²⁴ Bouckaert et al. (2012) use phylogenetic models with a geographic component directly to
quantitatively investigate current theories concerning the Indo-European homeland.
   ²⁵ This is not to say that geographically close languages are necessarily linguistically close but that
under certain circumstances (e.g. in a dialect continuum) the spread of linguistic change is dependent
on geographical variables of which distance is one. Thus, in studies such as François (2015: 179) it is
the case that geographically close members of a language family tend to show lower linguistic distance.
   ²⁶ That the consensus trees as the outputs of such models are not necessarily binary-branching is
not a violation of this assumption as each individual tree sampled by the model is binary branching.

<!-- source-page: 78; pdf-page: 97 -->
Resulting from these assumptions at the basis of phylogenetic models is
the conceptual difficulty in capturing linguistic processes that violate these
assumptions. Phenomena such as dialect continua are real entities but in the
results of phylogenetic models they appear mostly as the absence of phyloge-
netic support. In other words, when a certain subclade shows daughter taxa
and clades with low support, one possible interpretation is a dialect contin-
uum. This is the case for Germanic where West Germanic itself is inferred as
a clearly distinct clade but Old English and Old Frisian show low grouping
support, which suggests that these languages exhibit too few clearly distinct
innovations that warrant further subgrouping. This particular property of
Germanic is not surprising, as it has surfaced before in phylogenetic studies
on this family (see e.g. Verkerk 2019). The alternative of subgrouping might
therefore be the assumption of a dialect continuum that has brought forth
these languages. In this interpretation, the degree of horizontal transmission,
areal changes, and linguistic contact have yielded a diversification process for
these languages that is incompatible with rigid tree-like structures, or at least
not captured by them.²⁷
   It would therefore be a further complement of the existing methods to apply
a model to the Germanic dataset which specifically models geospatial relation-
ships and dialect continua. The building of such a model and the requirements
for implementing an algorithm will be addressed in the following chapter.


Only when clade support is low, consensus trees display these clades as multifurcating. Thus, this is a
way to depict strong uncertainty in bifurcating sub-branches.
   ²⁷ For an extensive discussion of the interplay between language contact, language change, and
language relatedness see Aikhenvald (2007); Hickey (2020); Heine, and Kuteva (2020); Grant (2020).
