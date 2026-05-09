---
title: "Germanic Phylogeny"
author: "Frederik Hartmann"
date: "2023"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "hartmann-2023.pdf"
chunk: "§4.1"
pages: "79-80"
---

# 4.1 On agent-based models


<!-- source-page: 79; pdf-page: 98 -->
4
     A wave model implementation


A wave model can be computationally implemented in multiple ways; the
modelling method I chose in this approach is to simulate the areal spreads
and horizontal transmission of changes in a geographical setting as part of
an agent-based model (ABM). Agent-based models are a type of model that
simulates virtual entities, ‘agents’, which interact with one another along the
parameters and rules of the simulation. Their interactions and the simula-
tion outcomes can give insights into the trajectories of patterns and behaviour
of the modelled entities. The following sections explain the concept of ABM
simulations further.
  The simulation of a wave model would thus entail simulating speech com-
munities acquiring and transmitting innovations that can overlap and create
new speech communities as a result. This model therefore could account for
phenomena such as vertical transmission, simultaneous linguistic dissimila-
tion of groups of speakers, and a more gradual development of languages from
a common protolanguage.
  Thus, the aim of this model is to simulate waves of innovations in a confined
geographical space where each innovation spreads through a part of a commu-
nity. There, spatial factors such as geographical barriers as well as linguistic
factors can be simulated in the same model.
  After the simulation of a variety of innovation scenarios, the models which
approximate the innovations best are chosen to be analysed further. In addi-
tion to the gradual change processes which are captured by this ABM, it yields
the advantage of granularity: it can build on the notion that parameters such
as site rate, speciation, and change rates are branch-dependent or episodic in
phylogenetic models and assume parameters to be flexible on an even more
fine-grained level. In turn, the parameters do not necessarily need to be set
globally or language-dependent in ABMs, but individual for every simulated
agent. In the subsequent analysis, linguistic areas can be probed for what
range of parameter values is present in the agents that make up the simulated
community and whether spatial patterns can be found.
  In short, the ABM used in this study is an approximation of the real-
world diversification processes in the Germanic languages by simulating the

<!-- source-page: 80; pdf-page: 99 -->
diversification process with virtual agents under different parameter settings.
The simulation can afterwards be analysed to determine which parameter val-
ues and diversification pathways approximate the data best in order to draw
conclusions about the actual process.
  This chapter is structured as follows: first, it gives a general overview of
agent-based models in section 4.1 before the core assumptions are outlined
that are required to model language differentiation in an ABM simulation. The
core mechanisms of the ABM used in this study are presented in sections 4.4
to 4.5, before section 4.7 goe into detail about how the individual mecha-
nisms presented before are computationally implemented in the model. To
show the general workings of the ABM, a test model is run on a toy dataset in
section 4.8. Sections 4.9 and 4.10 summarize the model and its priors before,
finally, section 4.11 examines the results of the main ABM simulation.


                  4.1 On agent-based models

Agent-based models were first used in physics, biology, and social sciences as
a means to simulate processes that involve a heterogeneous mass of simulated
entities. The method came into being at the time standard quantitative models
were assumed to be inadequate for some problems in especially computational
social science and biology.¹ Agent-based models are often used to simulate
complex dynamics in populations, processes, and systems comprised of indi-
vidual sub-units. They can thus be used to model and analyse a wide variety
of problems from population dynamics, molecular evolution, epidemiology,
and social interactions.
  Agent-based models are therefore best described by outlining the differ-
ences from other quantitative models: the heart of agent-based models is
simulating a number of entities (so-called agents) in a defined space according
to defined parameters. The agents in this simulated space usually have a clearly
defined spatial location and can possess different features that govern their
properties, interactions, and behaviour. Since agent-based models are usually
very task-specific, whether or not the individual agents possess features that
are distinct from one another is mostly defined by the type of task itself. For
example, behavioural simulations of emergency evacuations of buildings can
be conducted without agent-specific properties (see e.g. Ren, C. Yang, and Jin
2009). In this case, the agents are all equal and their actions are only governed


    ¹ For a general introduction see Railsback and Grimm (2019).
