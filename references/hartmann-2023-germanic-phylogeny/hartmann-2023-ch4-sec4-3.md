---
title: "Germanic Phylogeny"
author: "Frederik Hartmann"
date: "2023"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "hartmann-2023.pdf"
chunk: "§4.3"
pages: "85-86"
---

# 4.3 Agent-based models with Bayesian assumptions


<!-- source-page: 85; pdf-page: 104 -->
4.3 AGENT-BASED MODELS WITH BAYESIAN ASSUMPTIONS  85

together. The decision to migrate, however, can be set as an individual deci-
sion of an agent itself. Thus, large migration movements would emerge when
an areal group of agents exhibits similarly high migration probabilities.

      4.3 Agent-based models with Bayesian assumptions

Bayesian probability is, in the broadest sense, a probability concept which
represents a specific interpretation of probability.² Whereas the frequentist
interpretation of probability assumes probability to be equal to the relative
frequency of occurrence of an event after many trials, inherent to Bayesian
probability is the notion that probability can best be approximated by a prob-
ability distribution while at the same time this distribution contains the key
concept of uncertainty: the probability of an event is not a fixed value but dis-
tributed around a mean value with a certain standard deviation. This concept
is best exemplified using the example of a fair coin toss. We assume, a fair coin
exhibits, theoretically, the probability of 1 for the event ‘heads’ when tossed.                                                 2
However, as soon as the coin is tossed ten times, the relative frequency of
‘heads’ might not be exactly 12. If this experiment is repeated twenty times, we
can observe twenty different proportions of the event ‘heads’ after ten tosses.
The density of these twenty observations might peak at 2,1 but adjacent values
will also be likely to have given rise to the data. In the Bayesian sense, we want
to infer the probability of ‘heads’ from the available data, that is, to estimate
the (posterior) probability of certain probabilities for ‘heads’ given the data.
  The most important notion at this point is that events, even with theoretical
fixed probabilities, can, when tested, exhibit some degree of uncertainty. This
uncertainty is assumed to be inherent to our knowledge of the events, which
is a crucial assumption as it describes quantifiable events as at least partially
influenced by other factors and chance. The Bayesian approach, which is rel-
evant for the type of ABM described in the following sections, will also draw
on this principle of uncertainty, prior, and posterior distributions. The central
point of a Bayesian approach is the question of which events (and with which
probability) have most likely given rise to the data we observe.
   I will briefly illustrate this notion using the example of a hypothetical ‘inno-
vation’ parameter which determines the occurrence of a linguistic innovation
in the (non-deterministic) ABM simulation. In a fixed-value approach, the
parameter could be set to a specific value, for example 0.3, which would result

   ² In recent years Bayesian statistics was popularized again by influential works such as McElreath
(2020); Gelman et al. (2013).

<!-- source-page: 86; pdf-page: 105 -->
in a probability of 30 per cent for the occurrence of a linguistic innovation at
each time step. This would inevitably result in the assumption that this proba-
bility is always and exactly 0.3. However, if the simulation were re-run with the
same value, it might produce a slightly different outcome since this time, other
agents interact and other conditions and situations arise. This means that dif-
ferent final states of the simulations are compatible with the same parameter
value. Or, vice versa, a specific situation in the real-world could be compat-
ible with different parameter values in the simulation. As a result, we have
to simulate a large range of parameter values to gauge the different possible
outcomes.
  A way in which this can be done is that for every run of the simulation,
a new value is drawn from a prior distribution, resulting in different values
each time with every parameter value having its own prior probability. This
means that if a rather flat distribution is assumed, the range of possible val-
ues increases, virtually representing a situation in which this parameter varies
much from time step to time step. On the other hand, an underlying prob-
ability distribution with a small standard deviation will yield values that are
similar to one another. This approximates a situation in which a particular
area in the parameter space is designated for this parameter. After the simu-
lation has been run multiple times, we can filter out those results that do not
approximate the observed data well and we obtain a posterior distribution.³
  This has implications for the interpretation of a simulation result: both the
flat and a narrow posterior probability distribution for an individual param-
eter need to be interpreted differently. If the posterior parameter probability
distribution is flat (i.e. approximates a uniform distribution), we can interpret
this as this parameter setting being not very influential for the simulation out-
come. If there were simulation-internal drivers demanding a certain parameter
setting space from this parameter, the parameter would adjust accordingly and
hence develop a more narrow probability distribution.
  To summarize, the Bayesian approach enables exactly these insights into the
mechanics of the ABM simulation: (1) it assumes a prior probability distribu-
tion for the inferred parameters, and (2) it can, in the posterior, show both flat
distributions, and a very narrow distribution approximating a fixed value. The
latter benefit of obtaining a posterior distribution for parameters is that the
shape of the posterior can indicate whether a parameter has an impact on the
outcome. If, for example, the migration parameter approximated a uniform
distribution in the posterior runs, this would indicate that a large variety of


   ³ For more detail see section 4.6.1.
