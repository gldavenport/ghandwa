---
title: "Germanic Phylogeny"
author: "Frederik Hartmann"
date: "2023"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "hartmann-2023.pdf"
chunk: "§4.2"
pages: "81-84"
---

# 4.2 Agent-based models to model language differentiation


<!-- source-page: 81; pdf-page: 100 -->
4.2 AGENT-BASED MODELS TO MODEL LANGUAGE DIFFERENTIATION  81

by the global (applying to all agents equally) property of wanting to escape the
simulated room through the nearest exit.
  Global parameters are different from the individual properties of agents
in an ABM. For this reason, one has to distinguish between the two: global
parameters are sets of parameters which define the basic structure of the
actions of, and interactions between, individual agents. Global parameters can
be, for example, birth/death probabilities of agents, speed of movement or fre-
quency of interaction. Of course, these parameters can also be properties of the
agents; the decision about what parameters to include as global parameters or
properties of individual agents depends on the task at hand. To illustrate the
usual procedure of conducting an agent-based simulation, I will briefly outline
the steps in the process: first, one has to decide on the design of the study. How
meaningful the results of a simulation are depends heavily on what the aim of
the study is. The parameters are subsequently chosen and it is decided which
parameters are to be set as global parameters. Thereafter, the simulation is run:
a simulation is commonly divided into runs and ticks. A run refers to one sim-
ulation pass with a given set of parameters and consists of a certain number
of ticks. A tick is one iteration loop of the simulation in which all or a subset
of agents are updated. Usually, a run, while representing an entire simulation
from beginning to end, is not exhaustive. The global parameters are fixed for
each run which requires simulating multiple runs to be able to compare the
results with the parameters of each run. This procedure is also called a param-
eter sweep in which many different permutations of parameter combinations
are tested to evaluate the effects of the different parameters on the simulation
outcomes.


   4.2 Agent-based models to model language differentiation

Both in the field of language change research as well as in studies on language
differentiation, agent-based models have been used on multiple occasions.
  Sóskuthy (2015) who models sound change emergence though agent-based
models where the agents are subject to different phonological pressures can
be taken as an example for such studies. Other studies such as Winter and
Wedel (2016) use agent-based approaches to study agent interactions and the
effect on sound change and changes in the sound inventory. These repre-
sent a plethora of research into intra-population changes and the emergence
of different varieties. They are not necessarily directly comparable to the
more geospatial models of language evolution. Geospatial models include

<!-- source-page: 82; pdf-page: 101 -->
simulations of agents that are not rooted in abstract agent communities but
attempt to account for geographical distributions of agents in inter-agent inter-
actions. Such applications are used in sociology (e.g. Weidmann and Salehyan
2013; Bhavnani et al. 2014) or cultural evolution (e.g. Turchin et al. 2013). As
agent-based approaches are suited for simulating speech communities, they
are used as methods for the development of languages. Among the first, Steels
(2011) investigates language evolution by tying it to models of cultural evo-
lution. Furthermore, Gong, Minett, and Wang (2006) show the emergence of
a common language through communication. Several studies investigate lan-
guage emergence from a single starting language into multiple languages over
time reviewed in Wichmann (2008: 451). In such studies, emphasis is placed
on understanding the main driving factors of differentiation. Schulze, Stauffer,
and Wichmann (2007) review the effects of geographical distance and natural
barriers on language development and differentiation.
  Probably the most important difference between ABMs and other meth-
ods in computational cladistics is that ABMs are simulation-based, contrary
to descriptive or analytical approaches such as phylogenetic modelling or
statisticalanalyses. That is, they aim at approximating a real-worldprocess gen-
eratively through simulations rather than analytically describing or analysing
observed data.
  This property of ABMs comes with certain benefits concerning modelling of
the differentiation of languages. The approach is inherently bottom-up (Lek-
vam, Gambäck, and Bungum 2014: 50). The entire notion rests on the attempt
to recreate the processes in the real world in a simulated rule-governed space.
Complex simulations can still encompass randomness, but in essence, they are
strictly rule driven. These rules in the form of interactions and parametrized
events taking place in the simulated space can be altered, removed, and added
while monitoring their effect on the outcomes. In comparison with more infer-
ential methods, this approach yields the advantage of not needing to infer
processes based on data but to observe the fundamental and complex link-
ages between factors, parameters, and events. In other words, the researcher
can observe the behaviour of a system under varying conditions rather than
deducing the process from observed data only.
   It has to be noted that one of the additional differences between ABM
approaches and inferential methods is that the different outcomes and the
interactions between parameters are observed in a wide possibility space. With
external factors involved such as geographical data (in geospatial models),
we can observe high-dimensional interactions between the parameters them-
selves and external settings of the simulation. In this case, high-dimensional
interactions are parameter interactions that contain a high number of

<!-- source-page: 83; pdf-page: 102 -->
4.2 AGENT-BASED MODELS TO MODEL LANGUAGE DIFFERENTIATION  83

variables. In low-dimensional interactions, two or three variables interact (i.e.
exhibit inter-dependencies with regard to some outcome variable), whereas
high-dimensional interactions can have interactions between more than three
variables. In inferential methods, we are used to thinking in a data-driven way,
that is, we observe data directly and infer the immediate processes that might
have given rise to these data. In Germanic cladistics it is particularly salient
that purely analytical tools are limited since we do not have much diachronic
coverage of the processes. Between the proposed protolanguage and the attes-
tations of the individual languages, we have no records of the developments
that took place in between these two points in time. Therefore, as already dis-
cussed in previous chapters, we are faced with a centuries-spanning black box
where we can only infer the processes that have taken place. An agent-based
model of this problem can help by recreating the most important processes
that were present in the beginning of the development to investigate which
factors have contributed to yielding which outcome. However, it is not given
that all ABMs can be employed to model these processes we observe in Ger-
manic cladistics. An ABM that provides a good fit has to be individually crafted
to suit the requirements that this specific problem entails. ABMs which are pri-
marily used for simple problems are not ideal for this task since they do not
provide sufficient flexibility to approximate the real-world processes. That is,
simple ABMs that model diversification using only a low number of parame-
ters might not capture crucial patterns in the real-world process. With an ABM
specifically fit to the problem of Germanic linguistics, we can, however, recre-
ate the processes at hand in this very instance to observe the effects and to
understand which trajectories of movement and interactions might approxi-
mate the data best. The specific model type that was used here shall be further
described in section 4.3.


                 4.2.1 ABMs as process simulations

As already mentioned, ABMs are simulations and not statistical or compu-
tational inference models. Therefore, they are best suited to investigating
dynamic processes which are sparsely documented. The basic notions behind
the simulation of individual aspects are outlined in the following sections.

Generaldynamics
ABMs exhibit great flexibility and fluidity in all facets of the architecture.
Having this built-in dynamic structure means that processes are neither
discrete nor fully hard-coded but repeatable and gradient. It is generally

<!-- source-page: 84; pdf-page: 103 -->
advantageous to not need to assume fixed terms for processes such as migra-
tion speed since such a factor is not just decided once but can change in
frequency of occurrence and impact strength over the course of a simulation.
The ability of the simulated system to change on its own on the basis of inher-
ent factors and interactions makes it more flexible in terms of capability to
approximate real-world processes. This flexibility and ability to self-develop
is then found in all sub-processes in the model. This is not to say that more
flexible parameters are always better in any case. In certain cases, they merely
increase random noise or the likelihood of overfitting. For this reason, to make
use of the flexibility of agent-based models to the full extent, one must also add
sensible model parameter spaces and fit diagnostics.

Innovationdynamics
The dynamics of innovation in language can be modelled as conditional prob-
abilistic processes that occur as events of varying and individual frequency.
This means that innovations in language do not need to be predefined or
deterministic but can be modelled as fluctuating events. In particular, the inno-
vation of a certain linguistic feature can be modelled as an event that occurs
with a certain (globally or agent-specific) probability. This probability can be
globally fixed or change based on certain conditions during the course of a
simulation.

Contactdynamics
Language contact effects can also be dynamically modelled in an ABM simula-
tion. These contact effects are mainly modelled as interactions between agents
where one agent transfers certain features of its language to another. It is also
important to note that this is not done at predetermined points in time, but
rather governed by simulation-internal factors. Thus, we can generate spread-
ing of language properties that comes close to how innovations spread in a
wave-model. Innovations can spread and be overlaid with other innovations
during the simulation. Thus, contact can be modelled more fluidly and with
smooth transitions between the speech communities.

Migrationdynamics
Migration dynamics as such are mainly based on how frequently a commu-
nity changes its position in the simulation space. Migrations in an ABM can
be modelled as a confluence of many individual actions of the agents. It is pos-
sible to approximate a ‘relaxed’ migration model insofar as individual agents
can migrate to a neighbouring location or larger groups of agents can migrate
