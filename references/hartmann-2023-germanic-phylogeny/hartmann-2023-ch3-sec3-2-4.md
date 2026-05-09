---
title: "Germanic Phylogeny"
author: "Frederik Hartmann"
date: "2023"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "hartmann-2023.pdf"
chunk: "§3.2.4"
pages: "67-72"
---

# 3.2.4 Model comparison


<!-- source-page: 67; pdf-page: 86 -->
3.2 THE GERMANIC DIVERSIFICATION MODEL  67

  Other subgroups that were proposed in the past such as East Germanic,
Gotho-Nordic, and Anglo-Frisian were inferred with less support. However,
of those three clades mentioned, Anglo-Frisian was inferred with much higher
support than East Germanic or Gotho-Nordic.
  Further, it is necessary to examine the posterior branch lengths across the
different models (see Table 3.10). Branch lengths are defined as the distance
between two consecutive splits in a tree; in an absolute time-calibrated model
they represent the time between a clade being created by a splitting event
and the break-up of the clade in subclades or taxa. Investigating the inferred
branch lengths for clades yields linguistic insights into the time during which
a clade was extant. In other words, the inferred branch lengths give the time
duration a clade such as West Germanic existed before it split into multiple
daughter clades or taxa.
   It is salient that the branch lengths are positively correlated with the tree sup-
port (correlation coefficient: 0.70) as most proposed clades with low support
values likewise exhibit very small lower credible interval values. The reason
for this is that both low support and short branch lengths are the result of
an unclear topology in a tree. If the distinguishing innovations are few and
uncertainty is high, two clades will often switch positions in the ordering of the
clades having only small branch lengths. Thus short branch length estimates
are the result of low phylogenetic credibility in a tree and therefore need to be
analysed with caution.
  The posterior estimates for the clade with the highest support, West Ger-
manic, show a relatively long branch length on the absolute scale around 0.4
(i.e. 400 years), with the exception of the innovation-only model. Most other
proposed clades have significantly shorter branch lengths, partially due to
their low support as outlined above. For example, the mean branch length
for Northwest Germanic is approximately 0.13 (i.e. 130 years) which is at least
half the time that can be inferred for West Germanic.

                       3.2.4 Model comparison

Up to this point, the different models were treated as equal and their out-
puts compared. However, certain models—especially the innovation-only
models—yielded results that are notably different from the other models. In
order to determine which model yields the best fit to the data, we need to
employ quantitative tests to gauge each model’s relative fit in comparison with
the other models.
  Two of the recommended methods that are already implemented in
RevBayes are the stepping-stone sampling algorithm and the path sampling

<!-- source-page: 68; pdf-page: 87 -->
0.350.230.360.390.260.38   0.360.330.340.360.290.31   0.540.540.540.560.520.55   0.350.360.400.430.440.33                   upper.89CI
          Brlen
models        lower.89CI   0.000.000.000.000.000.00   0.000.000.000.000.000.00   0.010.000.000.000.000.00   0.000.000.000.000.000.00
different    Brlen
across     median              0.110.070.110.120.080.11   0.120.090.100.110.080.09   0.250.220.240.230.210.22   0.090.070.120.150.110.09
clades    Brlen
specific   mean              0.150.100.160.170.110.16   0.160.140.150.150.120.14   0.280.270.270.270.260.26   0.140.140.170.190.150.14
of    Brlen
lengths
              0.710.700.750.700.690.73   0.230.300.210.210.290.20   0.470.470.530.490.490.53   0.040.010.030.040.020.04             Supportbranch
of
estimates
posterior             Support         Hardbounded-JCHardbounded-InnovOnlyHardbounded-VarRatesInferred-JCInferred-InnovOnlyInferred-VarRates         Hardbounded-JCHardbounded-InnovOnlyHardbounded-VarRatesInferred-JCInferred-InnovOnlyInferred-VarRates         Hardbounded-JCHardbounded-InnovOnlyHardbounded-VarRatesInferred-JCInferred-InnovOnlyInferred-VarRates         Hardbounded-JCHardbounded-InnovOnlyHardbounded-VarRatesInferred-JCInferred-InnovOnlyInferred-VarRatesand
Support
3.10                                                                                              GermanicTable    Clade                                     Anglo-Frisian                    East                                                                                 Gotho-Burgundian                                                            Gotho-Nordic

<!-- source-page: 69; pdf-page: 88 -->
– –– –                  0.48       0.48      0.320.290.290.330.280.29   0.240.220.220.220.190.21   0.760.530.700.770.500.69                   upper.89CI
          Brlen
models


    – –– –                   lower.89CI      0.06       0.07      0.000.000.000.000.000.00   0.000.000.000.000.000.00   0.190.090.170.200.080.16different
          Brlenacross
clades     median – –– –                  0.26       0.25      0.120.110.110.120.110.11   0.080.060.070.080.050.07   0.480.300.440.460.280.43
specific    Brlen
of
        mean
    – –– –                  0.28       0.28      0.160.140.140.160.140.14   0.110.090.100.110.080.09   0.490.320.450.480.300.45lengths          Brlen
branch
of          0.001.000.000.001.000.00   0.340.710.370.340.700.37   0.260.190.280.270.210.28   1.001.001.001.001.001.00             Support
estimates
posterior
and             Support         Hardbounded-JCHardbounded-InnovOnlyHardbounded-VarRatesInferred-JCInferred-InnovOnlyInferred-VarRates         Hardbounded-JCHardbounded-InnovOnlyHardbounded-VarRatesInferred-JCInferred-InnovOnlyInferred-VarRates         Hardbounded-JCHardbounded-InnovOnlyHardbounded-VarRatesInferred-JCInferred-InnovOnlyInferred-VarRates         Hardbounded-JCHardbounded-InnovOnlyHardbounded-VarRatesInferred-JCInferred-InnovOnlyInferred-VarRatesSupport
(cont.)                                                                                     Germanic
3.10                                                                                                                                                                                               GermanicTable    Clade                            Ingvaeonic                                             Northwest                                                                       NWGmc–Vandalic                    West

<!-- source-page: 70; pdf-page: 89 -->
algorithm (Xie et al. 2011). Both are used to approximate the marginal like-
lihood of the models which can then be compared with one another. The
marginal likelihood is defined as the probability of the data given a cer-
tain model averaged over all parameters this model contains. As a result, the
marginal likelihood estimate disadvantages models with many parameters,
each of which does not contribute much to the fit, as well as models that are
severely underspecified and therefore yield a subpar fit. In other words, the
marginal likelihood estimation aims for a balance between model complex-
ity and model specificity.²⁰ Stepping-stone sampling and path sampling are
algorithms to estimate the marginal likelihood in phylogenetic models that
run several iterations of the model, each time raising the likelihood by a dis-
crete value. The result of both algorithms is the logarithm of the respective
model’s marginal likelihood estimate that can then be compared to the other
models. In Table 3.11, we see the marginal likelihoods of each model once
for the stepping-stone sampling (SS) and the path sampling (PS) algorithms.
Afterwards, a base (or null) model (M0) is selected, Hardbounded-JC in this
case,²¹ from which value all other model’s likelihood values are subtracted. As
a result, the difference between each individual non-null model and the null
model Δ(M0, Mi) can be further interpreted.
  There are no fixed thresholds or cutoff points at which the models are
deemed significantly different; however, a recommended non-significance
interval is between -1 and 1. If the likelihood differences fall in this range, the
models are not notably different. If values are < -1, the alternative model is pre-
ferred whereas for values > 1, the null model is preferred (cf. Höhna, Landis,
et al. 2017).
  The likelihood comparison summary in Table 3.11 shows that the best
model is model Hardbounded-VarRates (hard-bounded tip dates with an
inferred site change rate) with the second-best model being Hardbounded-
InnovOnly (hard-bounded tip dates with a fixed site rate that only allows for
innovations) However, the difference between all models is strong, therefore
Hardbounded-VarRates is preferred.
  Further, in Table 3.11, all inferred-bound models perform worse than their
hard-bounded counterparts. This indicates that the flexibility given to the tip
dates does not benefit the inference. This does not mean, however, that hard-
coded constraints are better in all cases. It is an observation that arises when
comparing relaxed tip date priors and more constrained priors, namely that

   ²⁰ For a concise overview along with example references see Höhna, Landis, et al. (2017: 86–89).
   ²¹ The choice of the M0 model is arbitrary, I selected this model at this point since it is the model
with the fewest parameters and the strongest assumptions.

<!-- source-page: 71; pdf-page: 90 -->
3.2 THE GERMANIC DIVERSIFICATION MODEL  71

Table 3.11 Marginal log-likelihoods of the phylogenetic models under the
stepping-stone sampling (SS) and path sampling (PS) algorithms along with
their differences to the model Hardbounded-JC

Model                   SS           ΔSS(M0, Mi)   PS          ΔPS(M0, Mi)

Hardbounded-JC           −1527.182      0           −1526.877      0
Inferred-JC                −1539.954     12.772        −1539.004     12.127
Hardbounded-VarRates      −1517.159    −10.023        −1516.922     −9.955
Inferred-VarRates           −1527.377       0.195        −1527.083       0.206
Hardbounded-InnovOnly    −1525.075     −2.107        −1525.095     −1.782
Inferred-InnovOnly         −1538.119     10.937        −1538.258     11.381


added flexibility does not improve inference in this particular case. Thus, the
hard-coded constraints are set well enough to provide a better fit to the data.

Episodicmodel
As discussed in section 3.1.3, some phylogenetic models allow for the tempo-
ral flexibility of speciation and extinction rates by means of using an episodic
rate change model. I decided to test this approach on the best model among
those previously run. If the speciation rates change considerably over time,
the models above would need to be re-evaluated under the episodic paradigm.
The episodic speciation and extinction model, however, was found to be inap-
propriate for this task. To test the influence of episodic changes on the model
parameters, I set up a model with the same architecture as the Hardbounded-
VarRates model under an episodic extinction and speciation rate.²² The rates
themselves received the same priors as before, the episodic model was given
ten rate change events uniformly distributed over the entire age of the tree.
In other words, instead of drawing one global extinction and speciation rate,
the model draws ten different rates for ten equally long time periods from the
sampled root to the sampled tips. As the rates are recorded, they can later be
analysed as to their impact on the inference. If in most posterior samples, the
rates at the root of the tree are considerably lower than at the tips, this means
that there is a significant rate increase over the course of the time the tree
covers. Figure 3.22 shows the output of this analysis.²³


   ²² As the fossil-only tip dating priors and the episodic speciation/extinction model were incompat-
ible in the inference framework RevBayes, I set the youngest taxon (Old Frisian) as extant and its tip
nodes at 0.8 which means that in Figure 3.22, the time axis needs to be interpreted as ‘thousand years
before 1200 AD’.
   ²³ The plot was created using the R package RevGadgets (Höhna and Freyman 2016).

<!-- source-page: 72; pdf-page: 91 -->
speciation rate                             extinction rate


    1.0                                                            1.0
rate                                                                               rate


    0.0                                                            0.0

         1.5        1          0.5        0              1.5        1          0.5        0
          Thousand years before 1200 AD                Thousand years before 1200 AD

             net-diversification rate                      relative-extinction rate
                                                                  0.6

    1.0
rate                                                                               rate 0.3


    0.0                                                            0.0

         1.5        1          0.5        0              1.5        1          0.5        0
          Thousand years before 1200 AD                Thousand years before 1200 AD
Figure3.22 Visualization of episodic speciation and extinction rates over inferred
time


  As we can observe, the credible interval for speciation rate is large and the
mean speciation rate almost constant over time. Equally, the extinction rate is
estimated as being constant. The narrowing of the credible intervals of the spe-
ciation rate is not indicative of a rate change but represents the slim reduction
in uncertainty regarding this parameter. In other words, the credible intervals
are compatible with either a strong increase or decrease in speciation rate but
that, in general, there is little evidence for either in the data. As a result, we
have to conclude that for this dataset and problem, allowing speciation and
extinction rates to vary does not help the model to explain the data better.

Informativeratemodel
The rate matrix estimates presented in section 3.2.3, specifically the high rate
of 1 →0, might be due to the weakly informative prior on the rate matrix.
To investigate this issue and to ascertain what effect a stronger prior on the
rate matrix has, the Hardbounded-VarRates model was re-run with a prior of
Dirichlet(5, 1) which disproportionally favours changes from 0 to 1. This prior
has a median of 0.13 for the rate 1 →0 and a mean of 0.17, meaning half of the
samples drawn from the prior will have a value lower than 0.13. However, the
results show that the chains converge at the interval [0.23, 0.35] with a mean
