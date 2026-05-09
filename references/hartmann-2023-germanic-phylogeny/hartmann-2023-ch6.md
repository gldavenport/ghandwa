---
title: "Germanic Phylogeny"
author: "Frederik Hartmann"
date: "2023"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "hartmann-2023.pdf"
chunk: "Chapter 6"
pages: "212-220"
---

# 6 Computational tree and wave models—final remarks


<!-- source-page: 212; pdf-page: 231 -->
6
Computational tree and wave models—final
               remarks


This study has shown that a computational wave-theory approach using ABM
simulations can yield valuable insights for real-world applications. Applied to
the Germanic diversification case, it was shown how tree-based phylogenetics
and wave-based simulations detect different parts of a diversification process,
each model with its own advantages and disadvantages.
  For the languages Gothic, Burgundian, and Vandalic, for example, the
phylogenetic model did not yield reliable results. Further, the specific inter-
relations between the West Germanic languages remain uncertain under this
model. The wave-model ABM could step in where the phylogenetic model
yielded inconclusive results, showing that East Germanic was a gradual diver-
sification process with strong cross-linguistic contact on the eastern rim of
the Germania region rather than a true subclade of Germanic with its own
protolanguage. Equally, it showed subclades below West Germanic cannot be
established as the diversification process in this region likely did not run along
the lines of tree-like splits. It, too, was a dialect continuum influenced by con-
tact lines between languages and geographical proximity. ABM wave models
are, however, computationally more resource-intensive and custom-built for
the specific task at hand.
  This chapter will be a retrospective, a reassessment of computational
wave-based and tree-based models for genealogical diversification which out-
lines their strengths and weaknesses. This meta-level perspective is intended
to map out a path forward to refining and improving the computational
methods in the future. The discussion about advantages and disadvantages
of wave-like ABM implementations over Bayesian phylogenetic models in
section 6.1 will be purely from a computational standpoint. The following
section 6.2 discusses tree and wave implementations from a theoretical and
interpretive perspective.

<!-- source-page: 213; pdf-page: 232 -->
6.1 RETHINKING WAVE MODELS UNDER A COMPUTATIONAL PARADIGM?  213

      6.1 Rethinking wave models under a computational
                       paradigm?

Firstly, the advantages of tree-based phylogenetics and the wave-based ABM
presented in this study, as is the case with most quantitative and computa-
tional approaches, is that they follow a stringent and repeatable process in
which every decision can be criticized and improved. In this respect, they com-
plement more traditional methods in historical linguistics by making certain
aspects of linguistic problems quantifiable and more transparent. While it is
not possible in a Bayesian ABM framework to replicate a study exactly because
of the inherent randomness in the task, nevertheless the individual parts of the
models can be replicated, changed, and extended according to the researcher’s
modelling preferences.
  The main advantage of an ABM approach is that, beside modelling linguis-
tic diversification as a gradual process, it takes extralinguistic parameters into
account. Especially factors that contribute to the geographical position of a
speech community with regard to its neighbours, and the adjacent landscape
can be fed into the analysis. Introducing this geographical variable comple-
ments the purely linguistic analysis by making it sensitive to the factors at play
in a geography-dependent diversification process such as the emergence or
breakup of a dialect continuum. Agent-based models can also model a vari-
ety of different pathways of linguistic spread which can be adjusted based on
the current linguistic theory. Issues such as founder effects due to population
growth and migration can also be taken into account.
  Due to this parametric versatility and the gradual nature of the underlying
process, it can show diversification nonlinearly. In other words, convergences
and divergences between languages or speech communities that are confined
to certain periods of a diversification process can be detected. This makes it
easier to model temporally limited contact and horizontal convergence events
between speech communities.
  The disadvantages of the agent-based models are mainly related to their
complexity. For Bayesian phylogenetic inference, there are currently many
different off-the-shelf methods that follow a building blocks system where a
researcher can choose each model part based on the theoretical underpin-
nings of the problem at hand. Agent-based models are, mainly by virtue of
their flexible nature, inherently more complex to set up as the basic model
architecture needs to be implemented from the bottom up. Moreover, because

<!-- source-page: 214; pdf-page: 233 -->
of this complexity, the interpretation of the results is more intricate and needs
a variety of different complementary methods such as clustering algorithms
or regression models to extract valuable insights.
  Further, they are very much resource intensive. Even extensively using par-
allel computation on large-scale computing clusters it can take fifteen to twenty
days for 200,000 simulations to finish. In comparison, Bayesian phylogenetic
algorithms take from minutes to a few hours to finish their calculations. Run-
ning multiple agent-based models or repeatedly improving certain model
aspects proves difficult when the time delay between model programming and
model results is a matter of weeks. Of course, there are ways to improve the effi-
ciency and smaller models can run faster in less time, but, for the time being,
simulating several thousand agents in one simulation over the course of more
than 1,000 simulated years is resource intensive nevertheless.
   It is clear that the agent-based model proposed in this study is only one of
the possible set-ups of a computational wave-theory implementation. That is,
there are numerous possibilities to set up such a model. What this study has
demonstrated, however, is that the results obtained from ABM implementa-
tions can complement tree-based methods such as Bayesian phylogenetics.
  As described above, the main advantage of ABMs is simultaneously their
biggest weakness: whereas Bayesian phylogenetics is based on more or less
straightforward algorithms that make use of the dimensions of a tree (branch
lengths and rates, tip dates, branching order, and branching times), agent-
based models are much more flexible in how they can be implemented. The
upside of this feature is that the researcher can incorporate many problem-
specific factors into the model. The downside is that, due to this property,
each model is unique to a problem and knowledge cannot be effectively
shared between a specific ABM implementation for one language family and
an implementation for another. The main lines of discussion will pertain to
the model parameters that are similar between both models. Unlike ABMs,
Bayesian phylogenetic model architectures can more easily be applied to other
problems by switching out the data and the priors.
   It is also clear that the model in this study is merely the beginning of
hopefully subsequent research into the best modelling techniques, limits, and
benefits of Agent based models used for wave-like language diversification.
Many of the aspects of the model presented here need to be refined in the
future—Germanic thus served as a test case for an early computational wave
model.

<!-- source-page: 215; pdf-page: 234 -->
6.1 RETHINKING WAVE MODELS UNDER A COMPUTATIONAL PARADIGM?  215

  Some of the aspects in particular that  will need to be investigated
further are:
Data types: Can ABM wave models model the innovation and spread of fea-
tures other than raw innovations? Research is needed into how a model needs
to be designed to simulate the spread of competing variants (e.g. lexical).
Weighting of innovations: Is there a benefit of using only a specific subset
of innovations to be modelled (only phonological innovations or only regu-
lar sound changes)? Do the different types of change need to be differently
weighted?
Missing data estimation: Does an ABM implementation benefit from approx-
imating missing data? When datapoints are missing, is there an alternative
to leaving them out of the evaluation? Techniques exist in other fields of
quantitative research that compensate for missing data. For example, multiple
imputation is widely used to recover approximate values of a missing variable
based on the other variables in the dataset. It is to be investigated whether
missing datapoints can effectively be modelled themselves in the simulation
to reduce their impact.
Improvement of optimization: The optimization process used in this study
is very resource-intensive and inefficient. How can the posterior estimation of
the ABM be improved to save time and computational resources?
Model comparison and model choice: In this study, I only presented one
model as an early example of an implementation using ABMs. Yet unlike with
Bayesian phylogenetic models which have a variety of goodness-of-fit estima-
tions for model comparison, there is no consensus in how the fit of agent-based
models can be compared. Although there are possible starting points such as
the sum of the posterior model fit, measures for model comparison need to
be found to make it possible to generate multiple competing models for one
problem particularly for the linguistic datasets.
Partitioning of the model: As it stands, the ABM proposed here contains a
large number of variables and factors that each contribute to the result in some
form. Yet it is to be investigated whether certain modules of the model can
function on their own or if a smaller model will yield more precise answers
to more narrow-scope questions. For example, it might be possible to devise a
small model just to investigate the relative chronology of a few innovations.
The geographical spread of innovations and the resulting isoglosses could
potentially be modelled very precisely in a limited geographical area.
   Finally, it is important to compare the results obtained in this study with the
findings in Agee (2018) since this allows comparisons to be drawn between

<!-- source-page: 216; pdf-page: 235 -->
three methods in quantitative cladistics: Bayesian phylogenetics, agent-based
models, and historical glottometry.¹
  The results of the study show five subgroupings with high subgroupiness val-
ues, namely West Germanic, Ingvaeonic, Northwest Germanic, Teuto-Saxon,
and Anglo-Frisian in descending order of subgroupiness (Agee 2018: 49).
These findings are partially supported by the investigation at hand where West
Germanic and Northwest Germanic were meaningful subgroups identified
by the agent-based and phylogenetic models. However, in the phylogenetic
approach, Northwest Germanic was found to be only weakly supported as a
subgroup (see e.g. section 3.2.5) which was taken as a sign that it was rela-
tively short-lived (see section 5.4). Yet in the study by Agee (2018), we see that
Northwest Germanic is calculated to be the third-best supported subgroup.
This difference might be due to the fact that exclusively shared innovations
are very important in historical glottometry (Agee 2018: 12–13) which can
enhance subgroups that share few but mostly exclusive innovations.
  Further, the subgroups Anglo-Frisian and Ingvaeonic found by Agee (2018)
are not supported by the findings in this study. The reason for this might be
that, as mentioned above, historical glottometry weights exclusively shared
innovations more strongly. On the other hand, ABM and Bayesian phylo-
genetic approaches account for randomness and parallel innovations which
results in less weight being put on individual innovations.
   It is worth noting that, interestingly, the Teuto-Saxon subgroup that Agee
finds is reflected as a meaningful subgroup in the phylogenetic model (section
3.2.3). This indicates a parallel in results between the tree-based phyloge-
netic algorithm and the glottometric wave-model implementation while the
ABM approach finds Old High German and Old Saxon to be not more closely
aligned (see Figures 4.54 and 4.55). One interpretation of this is that both the
phylogenetic and glottometric approaches weight aspects of the data higher,
which the agent-based approach does not. Since the ABM takes temporal and
geographical factors into account, this could mean that the closeness between
the languages in the data becomes insignificant when adding a geographical
variable and an innovation spreading mechanism. It cannot be decided at this
point which interpretation comes closer to the actual diversification process,
yet this observation itself is an important starting point for future investiga-
tions. More research is needed to examine in which situations this discrepancy
between ABM approaches and phylogenetics/glottometry arises and what the
underlying causes are.


    ¹ For a comparison between the modelling strategies themselves see section 6.2.

<!-- source-page: 217; pdf-page: 236 -->
6.2 OF HAMMERS AND NAILS  217

                   6.2 Of hammers and nails

The prize of solving these issues in the future is the promise of computa-
tional wave models that can investigate linguistic families with a wide range of
geographical and horizontal factors underlying their diversification by using
a complementary method to Bayesian phylogenetics, which can yield novel
insights into the processes of change. Concretely, aspects of the history of, for
instance, the Romance family could be better understood. This links back to
the discussion of the usefulness of tree and wave model in linguistic research,
as with a reliable and empirical wave model method that captures temporal
and spatial diversification, wave-like spreads might gain explanatory power
which they did not have before.
  The question is therefore not whether tree models can and should be used
in computational cladistics but rather in which cases. In the present study, the
tree model, despite yielding valuable insights into the support of certain rela-
tionships, does not fully capture the geospatial and dialectal disintegration
processes in Germania. The wave model implementation was more useful in
outlining the general trajectories of Germanic diversification. Yet this does not
devalue the tree model per se but the agent-based approach presents a novel
method to complement the robust tree models.
  There is, however, an epistemological issue raised in the applications of
either method. A famous quote by the twentieth-century psychologist Abra-
ham Maslow states, paraphrased, that if the only tool available is a hammer,
every problem will be treated like a nail. This hammer and nail problem is
a widely referenced metaphor for scientific bias towards known methods. In
its most simple interpretation, the questions we have about real-world issues
might be answered using the tools we have available—from the perspective
of the tools themselves. In the worst case, our methods to approach a topic
shape our understanding of the process not by leading us to new insights but
by suggesting that the obtained results are the real process.
  This viewpoint is intended as a caveat for any discussions regarding com-
putational tree or wave models. Although we can analyze the linguistic data
both with tree-based and wave-based methods, we have to be aware that the
results of each method will mostly fit within the framework of the method
itself. It is therefore crucial to be aware of the limits of every method. Not in
the sense of where the model is inaccurately making assumptions about model-
internal issues but where the model entirely fails to capture a vital aspect of the
real-world process. In other words, we must be aware that both wave and tree
models in computational contexts are blind to certain aspects regarding which

<!-- source-page: 218; pdf-page: 237 -->
they are not merely inaccurate but which they a priori disregard as an artefact
of the method itself. It is the researcher who is responsible for contextualizing
the results of each method to gain a more complete understanding of certain
aspects of the real-world process.
  This discussion above and of what follows, therefore, is a call to assume a
meta-level viewpoint in which the issue of tree and wave models is not a ques-
tion of either/or but what each method, in its limited scope, can contribute to
a broader understanding of the subject matter.
   It is therefore clear that the tree model as a tool for genealogical analysis
cannot—and should not—be abolished. If anything, the analysis has shown
that only a confluence of both methods can yield results that take a broad
scope of linguistic diversification into account. This means that we cannot
discard one or the other method when computationally analysing linguistic
relatedness.
  In general, we have to distinguish between modelling language diversifica-
tion and how we assume the actual diversification process of a particular lan-
guage has developed. As pointed out numerous times (Drinka 2013; François
2015), the pure tree model has numerous issues when assumed to be the only
form of linguistic diversification. However, as a modelling technique, com-
putational tree model implementations capture certain scenarios better than
wave implementations. For example, tree and subgroup dating in computa-
tional Bayesian phylogenetics runs along a rigorous site-dependent tree that
approximates intermediate stages and can take into account and even reflect
uncertainty in the diversification process. Moreover, linguistic diversification
resulting from migration processes (such as, perhaps, early Indo-European) is
best captured in a tree model. In many cases, a highly horizontally influenced
diversification process may even result in poor subgrouping results with regard
to clade support, making the model indicate that the process is more intricate
than can possibly be captured in a tree. In non-computational contexts, the
advantages of a tree are even more pronounced as the standard comparative
method operates in a way where it assumes relatively homogeneous protolan-
guages (Fox 1995: 128–133). At the end of a comparative reconstruction stands
a tree-like confluence of linguistic features into a single protolanguage.
  There is no doubt that a computational wave-theory implementation can
yield more insights than a Bayesian phylogenetics could on its own but it is
exactly this: a complement. In the Germanic case, the tree model as a phy-
logenetic analysis tool is of vital importance and by no means subordinate to
the agent-based wave model implementation. However, the results have shown
that Germanic in particular is less well captured in a pure tree-like display

<!-- source-page: 219; pdf-page: 238 -->
6.2 OF HAMMERS AND NAILS  219

which would entail more abrupt splits between groups with a following rela-
tive isolation. Rather, Germanic is a highly connected web of mutual influence
and the diversification processes take place in gradually disintegrating com-
munities in a dialect continuum. Whereas for Germanic, this question can
be answered quite clearly in favour of a wave-like diversification process, this
does not translate to other language families. The finding that for Germanic a
gradual process is preferred neither invalidates the tree model being applied to
other language families nor does it show that tree-model-based analysis prac-
tices are to be abolished. In a sense, we need both approaches to be applied
to a problem in order to arrive at the conclusion that one might be preferred
over the other. Whether or not a tree-like scenario can be subsumed under
the wave-theory as François (2015: 171–172) attempts, would be a different
question not related to the issue of modelling.
  As the ABM approach is a computational implementation of the wave the-
ory, it is important to examine its relationship to historical glottometry, the
most prominent quantitative wave-model implementation to date as outlined
in François (2015), tested and fleshed out in Daniels, D. Barth, and W. Barth
(2019) and applied to the Germanic family in Agee (2018).
  The most salient difference between the agent-based approach proposed
in this study and historical glottometry is that, while the former is a com-
putational simulation model, the latter is a calculation method based on a
series of equations operating on the number of shared or cross-cutting innova-
tions in various possible subgroups. In other words, while the ABM simulates
pathways of diversification across time, historical glottometry calculates the
credibility (‘subgroupiness’) of a certain subgroup within an innovation-based
dataset as a numerical value (François 2015: 181–184). Therefore, both meth-
ods are, despite being quantitative in nature, substantially different in their
complexity and assumptions. Historical glottometry outputs a single value
based on weightings of shared innovations governed by a predetermined set
of equations whereas the ABM approach seeks to give the model freedom to
infer parameter values from the data during the process, outputting a variety
of different parameters, linguistic distances, and geographical properties.
  Due to this difference, both methods are differently complex in their output
interpretation. Yet the simulation-based, and therefore more complex, agent-
based model has advantages concerning the ability to directly account for
fluctuations and uncertainty in the data as well as to report the uncertainty
regarding specific parameters and model results. Historical glottometry has,
in its current form, no metric which can report the ‘significance level’ of sub-
groupings to be accepted as valid. Some studies consider subgroups to be valid

<!-- source-page: 220; pdf-page: 239 -->
above a certain number of exclusively shared innovations, yet depending on
different cutoff points, the accepted subgroups may include false positive due
to many parallel innovations (cf. Daniels, D. Barth, and W. Barth 2019: 106).
This is moreover the case when the subgroupiness values of two groupings are
very close to one another as small errors or uncertainties regarding individual
innovations can distort the values.
  Further, this can lead to shared innovations being weighted higher than in
other methods. The results in the study by Agee (2018), for example, show
both Ingvaeonic and Anglo-Frisian as valid subgroups (Agee 2018: 49). How-
ever, the agent-based approach and the phylogenetic algorithm found these
two subgroups to be spurious and likely to be an artefact of the linguistic
discretization of languages in a diversifying dialect continuum.
   Lastly, the factors considered for the computation of the results are, cru-
cially, different since historical glottometry is a purely linguistic computa-
tion method that attempts to determine subgroups based on the association
strengths between individual languages as part of subgroups with shared and
cross-cutting innovations. On the other hand, the agent-based approach mod-
els the diachronic development of a linguistic family by taking into account
geographical and linguistic factors.
  As a complementary method for modelling linguistic diversification, the
agent-based approach has therefore proven effective in modelling aspects of
linguistic history that trees are not able to fully capture. Moreover, the model
is the first computational and non-descriptive wave-theory implementation
that takes diachrony and temporal progression into account, which previous
methods such as historical glottometry do not. It is therefore an improvement
on previous methods which have frequently been criticized for not modelling
the temporal aspect of wave-like diversification processes (e.g. Jacques and List
2019).
