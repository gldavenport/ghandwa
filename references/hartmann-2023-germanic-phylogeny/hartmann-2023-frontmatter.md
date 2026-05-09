---
title: "Germanic Phylogeny"
author: "Frederik Hartmann"
date: "2023"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "hartmann-2023.pdf"
chunk: "Front matter"
pages: "i-xvii"
---

# Front matter


<!-- pdf-page: 1 -->


<!-- pdf-page: 2 -->
Germanic Phylogeny

<!-- pdf-page: 3 -->
OXFORD STUDIES IN DIACHRONIC
      AND HISTORIC AL LINGUISTICS
                              General editors
         Adam Ledgeway and Ian Roberts, University of Cambridge

                                Advisory editors
    Cynthia L. Allen, Australian National University; Ricardo Bermúdez-Otero,
       University of Manchester; Theresa Biberauer, University of Cambridge;
Charlotte Galves, University of Campinas; Geoff Horrocks, University of Cambridge;
    Paul Kiparsky, Stanford University; David Lightfoot, Georgetown University;
 Giuseppe Longobardi, University of York; George Walkden, University of Konstanz;
                     David Willis, University of Oxford

                 RECENTLY PUBLISHED IN THE SERIES
                                  44
                      Romance Object Clitics
                    Microvariation and Linguistic Change
                             Diego Pescarini
                                  45
         The Diachrony of Differential Object Marking in Romanian
                        Virginia Hill and Alexandru Mardale
                                  46
     Noun-Based Constructions in the History of Portuguese and Spanish
                       Patrícia Amaral and Manuel Delicado Cantero
                                  47
                           Syntactic Change in French
                          Sam Wolfe
                                  48
                     Periphrasis and Inflexion in Diachrony
                    A View from Romance
         Edited by Adam Ledgeway, John Charles Smith, and Nigel Vincent
                                  49
                        Functional Heads Across Time
                         Syntactic Reanalysis and Change
                  Edited by Barbara Egedi and Veronika Hegedűs
                                  50
        Alignment and Alignment Change in the Indo-European Family
                             Edited by Eystein Dahl
                                  51
                         Germanic Phylogeny
                               Frederik Hartmann
For a complete list of titles published and in preparation for the series, see pp. 276–80

<!-- pdf-page: 4 -->
Germanic Phylogeny

        FREDERIK HARTMANN

<!-- pdf-page: 5 -->
Great Clarendon Street, Oxford, OX2 6DP,
                            United Kingdom
     Oxford University Press is a department of the University of Oxford.
    It furthers the University’s objective of excellence in research, scholarship,
  and education by publishing worldwide. Oxford is a registered trade mark of
      Oxford University Press in the UK and in certain other countries
              © Frederik Hartmann 2023
            The moral rights of the author have been asserted
  All rights reserved. No part of this publication may be reproduced, stored in
  a retrieval system, or transmitted, in any form or by any means, without the
prior permission in writing of Oxford University Press, or as expressly permitted
  by law, by licence or under terms agreed with the appropriate reprographics
rights organization. Enquiries concerning reproduction outside the scope of the
 above should be sent to the Rights Department, Oxford University Press, at the
                               address above
            You must not circulate this work in any other form
         and you must impose this same condition on any acquirer
     Published in the United States of America by Oxford University Press
     198 Madison Avenue, New York, NY 10016, United States of America
                 British Library Cataloguing in Publication Data
                            Data available
              Library of Congress Control Number: 2023930750
                    ISBN 978–0–19–887273–3
             DOI: 10.1093/oso/9780198872733.001.0001
                           Printed and bound by
              CPI Group (UK) Ltd, Croydon, CR0 4YY
    Links to third party websites are provided by Oxford in good faith and
   for information only. Oxford disclaims any responsibility for the materials
         contained in any third party website referenced in this work.

<!-- pdf-page: 6 -->
Contents


Series preface                                                                            viii
Acknowledgements                                                              ix
Preface                                                                           xi
List of figures                                                                          xii
List of tables                                                               xvi

 1. Introduction                                              1
    1.1 A note on the definition of the term cladistics                      3
    1.2 Summary of cladistical theories concerning Germanic subgroupings   4
         1.2.1 North Germanic, West Germanic, East Germanic                 4
         1.2.2 Gotho-Nordic                                              4
         1.2.3 Northwest Germanic                                        5
         1.2.4 Ingvaeonic and Anglo-Frisian                                 5
    1.3 Computational modelling of the Germanic languages               5
    1.4 Wave model, tree model, and Germanic phylogeny                 7
 2. Data                                                    10
 3. Tree-based phylogenetics                                   15
    3.1 Phylogenetic algorithms                                      15
         3.1.1 Distance-based methods                                    17
         3.1.2 Bayesian phylogenetic models                                25
         3.1.3 Core concepts                                             28
    3.2 The Germanic diversification model                            40
         3.2.1 Model specifications                                        40
         3.2.2 Model differences                                          47
         3.2.3 Results                                                   55
         3.2.4 Model comparison                                         67
         3.2.5 Discussion of findings                                      73
    3.3 Beyond phylogenetic tree inference                             76
 4. A wave model implementation                               79
    4.1 On agent-based models                                       80
    4.2 Agent-based models to model language differentiation              81
         4.2.1 ABMs as process simulations                                 83
    4.3 Agent-based models with Bayesian assumptions                   85
    4.4 The setting and purpose of the Germanic diversification model      87
    4.5 Parameters of the model                                      88
         4.5.1 Migration and birth                                        89

<!-- pdf-page: 7 -->
4.5.2  Innovation spreading and aligning                          91
          4.5.3  Geospatial parameters                                    95
          4.5.4  The innovation mechanism                                97
          4.5.5  Hierarchical modelling                                   99
     4.6 The evaluation of the model                                 103
          4.6.1  The concept of Approximate Bayesian computation           104
          4.6.2  The spatial component                                   109
          4.6.3  The temporal component                                112
          4.6.4  Optimization of runs                                    114
          4.6.5  The evaluation process                                   116
     4.7 The modules of the ABM                                    119
          4.7.1  The updating module                                    121
          4.7.2  The innovation module                                  123
          4.7.3   Initialization and region-specific updating
               parameters                                            124
     4.8 Putting the model approach to the test                         125
          4.8.1  The results of the example simulation test                   128
     4.9 Model summary                                           137
    4.10 Prior summary                                            139
    4.11 ABM model results                                        139
          4.11.1 The global parameters                                   140
          4.11.2 The consensus runs                                     150
 5. Genealogical implications and Germanic phylogeny            172
     5.1 Prelude: society and identity in pre-Roman and
        migration-age central Europe                                172
     5.2 Origin and disintegration of Proto-Germanic                   173
          5.2.1   Brief remarks on the stages of Proto-Germanic               173
          5.2.2  The origins of the Germanic clade                         174
          5.2.3  Proto-Germanic—a dialect continuum?                     176
          5.2.4  Time estimations of Germanic diversification                177
     5.3 The Eastern Rim languages                                  178
          5.3.1  The provenance of Gothic—a linguistic perspective           178
          5.3.2  Widening the view: Vandalic and Burgundian                183
          5.3.3  A dialect continuum on the Eastern Rim                    186
          5.3.4  The development of the Eastern Rim                       189
     5.4 Core-Germanic                                           192
          5.4.1  The beginning: Core-Germanic vs. Northwest
             Germanic                                             192
          5.4.2  The decline of Core-Germanic                            194
          5.4.3  Linguistic and social orders in transition                    197
     5.5 West Germanic and its daughters                             199
          5.5.1  West Germanic origins                                   199
          5.5.2  West Germanic disintegration                             200
     5.6 The development of the Germanic family—final considerations    206

<!-- pdf-page: 8 -->
5.6.1  The central aspects of Germanic phylogeny                  206
          5.6.2  Attempt to construct a stemma                            208
 6. Computational tree and wave models—final remarks           212
     6.1 Rethinking wave models under a computational paradigm?       213
     6.2 Of hammers and nails                                      217

Appendix                                                     221
References                                                    263
Index                                                        273
Index of subjects                                               274

<!-- pdf-page: 9 -->
Series preface


Modern diachronic linguistics has important contacts with other subdisci-
plines, notably first-language acquisition, learnability theory, computational
linguistics, sociolinguistics, and the traditional philological study of texts. It
is now recognized in the wider field that diachronic linguistics can make a
novel contribution to linguistic theory, to historical linguistics, and arguably
to cognitive science more widely.
  This series provides a forum for work in both diachronic and historical lin-
guistics, including work on change in grammar, sound, and meaning within
and across languages; synchronic studies of languages in the past; and descrip-
tive histories of one or more languages. It is intended to reflect and encourage
the links between these subjects and fields such as those mentioned above.
  The goal of the series is to publish high-quality monographs and collections
of papers in diachronic linguistics generally, i.e. studies focussing on change
in linguistic structure, and/or change in grammars, which are also intended to
make a contribution to linguistic theory, by developing and adopting a cur-
rent theoretical model, by raising wider questions concerning the nature of
language change or by developing theoretical connections with other areas
of linguistics and cognitive science as listed above. There is no bias towards
a particular language or language family, or towards a particular theoretical
framework; workin all theoreticalframeworks, andworkbased onthe descrip-
tive tradition of language typology, as well as quantitatively based work using
theoretical ideas, also feature in the series.
                             Adam Ledgeway and Ian Roberts
                                                    University of Cambridge

<!-- pdf-page: 10 -->
Acknowledgements


A myriad of people have contributed in one way or another to this book
through advice and support such that I cannot possibly acknowledge every
single contribution in the way it deserves. I thus want to, at least in a few sen-
tences, mention all of you, who helped in making this book happen. To those
who I may have inadvertently forgotten in this list, I sincerely apologize.
  As this book grew out of my PhD work, it was supported financially by the
Studienstiftung des Deutschen Volkes and Deutsche Forschungsgemeinschaft
(grant no. 429663384, ‘Germanic dispersion beyond trees and waves’) who
funded me during this period.
   I am greatly indebted to my supervisor George Walkden whose support
throughout and beyond my PhD cannot be overstated. This book has benefited
greatly from his advice and his input, but he has been even more influential
on my work in general by fostering my academic personality and by helping
me pursue my linguistic enthusiasm in productive ways. I am so grateful that
he has been my mentor ever since the first time I walked into his office in June
2018.
  Likewise, I want to thank my second PhD supervisor Gerhard Jäger who
encouraged and supported my academic endeavours since I was a master’s
student in Tübingen at the Department of Linguistics. In matters of compu-
tational linguistics, it was often ultimately him who pointed me in the right
direction whether or not he realized it at the time. He incited me to pursue
Bayesian modelling and agent-based models which today make up a large
proportion of my methodological toolbox.
  Many thanks are due to Karsten Donnay who helped me grasp the topic
of simulation models during multiple long discussions early on. He was a
strong influence on my views on agent-based models and my first approaches
to implement these models in a linguistic setting.
   I wouldlike to thank all of those whose expertise helped me with thisproject.
Specifically, I want to thank Patrick Stiles and Johanna Nichols for giving me
feedback on individual aspects of Germanic phylogeny. Further, Andy Wedel,

<!-- pdf-page: 11 -->
Henri Kauhanen, and Katerina Kalouli have given me helpful advice espe-
cially at the early stages of the project which has enabled me to navigate the
difficulties of starting a big computational project.
  In particular I want to thank Hans-Jörg Karlsen who helped me put my
findings in the archaeological context. Without him, the sections on histori-
cal influences on the linguistic diversifications in Germanic would not be in
this book.
  The project benefited from many discussions with colleagues about the ins-
and-outs of Germanic cladistics and modelling complex systems, most notably
Richard Blythe, Jiaming Luo, Rolf Bremmer, and Nelson Goering. In particu-
lar, I want to thank Anne Popkema and Johanneke Sytsema who were mainly
responsible for organizing the Old Frisian Summer School in Oxford and
Groningen which I had the great fortune of attending in 2019 and to be invited
to as a speaker in 2021. In both years, we had great discussions about earlier
Germanic languages in general and the role of Old Frisian in the diversifica-
tion of West Germanic. In this vein, I want to thank the other speakers and also
the attendees who truly made the summer school a hotspot for lively debate
and a place-to-be for early Germanic linguistics during those weeks.
   I am grateful to Miriam Butt and her group at the University of Konstanz
who took me in as a fellow computational linguist, enabled me to go to con-
ferences with them, and gave me access to computing power of which I was in
dire need.
  Special thanks are due to my student assistant Chiara Riegger for her help
with checking, organizing, and formatting the data and bibliography. More-
over, this book greatly benefited from our joint work on Burgundian which
helped in fleshing out the Burgundian data.
   I want to thank my father Jörg Hartmann whose graphic design skills helped
me with the implementation of the wave model graphs.
   Lastly, I want to thank all the unsung heroes who have supported (and con-
tinue to support) me on my academic way, namely my family and my friends
who, in more ways than they might realize, made it possible for me to write this
book. Most of all, I am incredibly grateful to my lovely wife Sigrid for always
believing in me and for giving me strength, support, and distraction when I
most needed it.

<!-- pdf-page: 12 -->
Preface


The general field of Indo-European cladistics is one of the most well researched
fields in the study of genealogical relationships between languages. We have
relatively precise information on how individual Indo-European subclades
split up from their most recent common ancestor. However, for some Indo-
European subfamilies, such as Germanic, we still have open questions as to
the nature and the detailed structure of the diversification of this family.
  The aim of this book is twofold: firstly, it aims to examine the Germanic
language family with computational methods while building on the rich pool
of previous research. The goal is, ideally, to be able to tell the most accu-
rate story of the linguistic diversification of Germanic from the break-up of
Proto-Germanic to the individual daughter languages. Secondly, this book
introduces a novel method for a computational implementation of the wave
model that can be used to investigate similar problems concerning wave-like
diversification processes in language families.
  The reader might find that this book involves a high level of intricate cladis-
tical aspects of Germanic. I attempt to convey the computational aspects in
a way that is accessible to all readers, computational and non-computational
alike. Although parts of this book can be used as an introduction to phylo-
genetic algorithms and simulation-based models of language, it is, at its core,
a study on Germanic, phylogenetics, and computational wave-model imple-
mentations. The structure of this book is such that the first chapters focus
on introducing, justifying, and applying the models whereas the chapter on
Germanic phylogeny then pools the insights gained from the computational
analyses together with previous research to describe the process of Germanic
diversification. That is, this chapter seeks to unify all computational and non-
computational studies on Germanic phylogeny to paint the most complete
picture of this genealogy to date.
  This book is the outcome of my PhD work at the University of Konstanz,
the topic of which came to me during my work on Vandalic during my grad-
uate studies in Tübingen. Thus, my 2020 book on the Vandalic language is in
some ways the spiritual prequel to this book at hand. After I had worked on
the Vandalic relationships with other Germanic languages, I felt the need to
re-examine the Germanic family more in detail and with methods that have
not yet been applied to Germanic.

<!-- pdf-page: 13 -->
List of figures


 3.1. Neighbour joining network                                        18
 3.2. Neighbour joining phylogram                                      19
 3.3. UPGMA phylogram                                              20
 3.4. UPGMA phylogram, only innovations                               21
 3.5. UPGMA phylogram, incorrect topology                              22
 3.6. NeighborNet clustering                                            23
 3.7. NeighborNet clustering, only innovations                             25
 3.8. A potential tree topology                                           30
 3.9. A potential tree topology                                           30
3.10. Gamma density function                                          35
3.11. Node age prior density                                            44
3.12. Topology with unequal branch rates                                 46
3.13. Incorrect inference of an underlying topology with unequal branch rates   46
3.14. Gothic tip date prior                                              49
3.15. Graphical representation of the Germanic diversification model          52
3.16. Consensus tree of model Hardbounded-JC                            57
3.17. Consensus tree of model Hardbounded-InnovOnly                     58
3.18. Consensus tree of model Hardbounded-VarRates                       58
3.19. Consensus tree of model Inferredbounds-JC                           59
3.20. Consensus tree of model Inferredbounds-InnovOnly                    59
3.21. Consensus tree of model Inferredbounds-VarRates                      60
3.22. Visualization of episodic speciation and extinction rates over inferred time  72
3.23. Consensus tree of the preferred model Hardbound-VarRates              73
3.24. Maximum clade credibility tree of the preferred model
     Hardbound-VarRates                                              74
 4.1. Zoom of the simulation surface showing the three terrain types
      including inhabited tiles that are occupied by agents                    87
 4.2. Example ABM migration: snapshots at ticks 0, 20, 40, 60, 80, 100          89
 4.3. Example ABM migration with multiple agents: snapshots at ticks 0,
      20, 40, 60, 80, 100                                                90

<!-- pdf-page: 14 -->
4.4. Example ABM migration with multiple agents and migration
      restrictions: snapshots at ticks 0, 20, 40, 60, 80, 100                     90
 4.5. Example ABM migration and birth with multiple agents and migration
      restrictions: snapshots at ticks 0, 20, 40, 60, 80, 100                     91
 4.6. Example ABM innovation with one starting agent: snapshots at ticks
       0, 20, 40, 60, 80, 100                                              92
 4.7. Example ABM innovation with two starting agents and two possible
      innovations: snapshots at ticks 0, 20, 40, 60, 80, 100                     92
 4.8. Example ABM innovation with two starting agents and two possible
      innovations including alignment: snapshots at ticks 0, 20, 40, 60, 80, 100   93
 4.9. Example ABM innovation with two starting agents and two possible
      innovations including strong alignment after 60 ticks: snapshots at
      ticks 0, 20, 40, 60, 80, 100                                          93
4.10. Example ABM innovation with two starting agents and two possible
      innovations: snapshots at ticks 0, 20, 40, 60, 80, 100                     94
4.11. Example ABM migration with multiple starting agents and a partial
      barrier: snapshots at ticks 0, 20, 40, 60, 80, 100                         95
4.12. Example ABM innovation with two starting agents and two possible
      innovations: snapshots at ticks 0, 20, 40, 60, 80, 100                     96
4.13. Example ABM innovation mechanism with two possible innovations
     and random innovation occurrence: snapshots at ticks 0, 20, 40, 60,
      80, 100                                                         97
4.14. Example ABM innovation mechanism with two unique possible
      innovations: snapshots at ticks 0, 20, 40, 60, 80, 100                     98
4.15. Fixed-value update of α and β by 1 per time step                      100
4.16. Change of mean under a random normal-valued update process         101
4.17. Trace plot of mean development for twenty agents under a random
     normal-valued update process                                     102
4.18. Change of mean under a random normal-valued update process with
      values < 0.2 at tick 250                                           102
4.19. Change of mean under a random normal-valued update process with
     update ~ Normal(0.001, 0.1)                                       103
4.20. Posterior distribution of p(innovation)                              106
4.21. Posterior distribution of p(innovation), adjusted x-axis                 107
4.22. Posterior distribution of p(innovation) of the ABC with error included    108
4.23. Posterior distribution of p(innovation) of the ABC with error included,
      adjusted x-axis                                                  108
4.24. Simulation surface map of northern Europe                          109
4.25. Evaluation space of Old English                                    110
4.26. Evaluation space of Old Saxon                                     110

<!-- pdf-page: 15 -->
4.27. Evaluation space of Old High German                              110
 4.28. Evaluation space of Gothic, Burgundian, and Vandalic                 110
 4.29. Evaluation space of Old Frisian                                    111
 4.30. Evaluation space of Old Norse                                     111
 4.31. Logarithmic loss function                                         119
 4.32. Model graph of the Bayesian ABM only including model-internal nodes   120
 4.33. Graphical representation of the updating module                     123
 4.34. Graphical representation of the innovation module                    124
 4.35. Example ABM run with two possible innovations: snapshots at ticks 0,
       20, 40, 60, 80, 100                                               126
 4.36. Posterior distribution plot of Spreading                              129
 4.37. Posterior distribution plot of Innovation                             130
 4.38. Posterior distribution plot of Obstacle spreading                       130
 4.39. Posterior distribution plot of Innov. 1                               131
 4.40. Posterior distribution plot of Innov. 2                               132
 4.41. Results from run analysis using maximum support heat maps           135
 4.42. Results from run analysis using maximum support heat maps           136
 4.43. Results from run analysis using maximum support heat maps           137
 4.44. Full model graph of the Bayesian agent-based model                   138
 4.45. Posterior values of age parameters                                  141
 4.46. Correlation plot of posterior ages                                   142
 4.47. Homoplasy parameter on the scale of raw rate and homoplastic events
      per century (p/c)                                                143
 4.48. Environmental independence of agents from 0 (entirely dependent
     on the neighbouring agents) to 1 (completely independent from
      neighbouring agents)                                            144
 4.49. Development of the linguistic fit metric MCC (std.) as a function of
      age (in 1,000 years before present)                                  151
 4.50. Distance from Gothic fit as a function of age                         152
 4.51. Distance from Vandalic fit as a function of age                        153
 4.52. Distance from Burgundian fit as a function of age                     154
 4.53. Distance from Old Norse fit as a function of age                       155
 4.54. Distance from Old Saxon fit as a function of age                      155
 4.55. Distance from Old High German fit as a function of age                156
 4.56. Distance from Old English fit as a function of age                     157
 4.57. Distance from Old Frisian fit as a function of age                      157
 4.58. Development of the innovation parameter in each region over time       158

<!-- pdf-page: 16 -->
4.59. Development of the align parameter in each region over time            159
4.60. Development of the spread parameter in each region over time          160
4.61. Development of the spread vulnerability parameter in each region over
     time                                                          160
4.62. Development of the spread sea parameter in each region over time       161
4.63. Development of the river spread parameter in each region over time      161
4.64. Development of the migration parameter in each region over time        162
4.65. Development of the river crossing parameter in each region over time     163
4.66. Development of the birth parameter in each region over time           163
4.67. PCA plot of linguistic distance at age 2.4 (400 BC)                     165
4.68. PCA plot of linguistic distance at age 2.2 (200 BC)                     166
4.69. PCA plot of linguistic distance at age 2 (at the beginning of the
    Common Era)                                                  167
4.70. PCA plot of linguistic distance at age 1.8 (200 AD)                     167
4.71. PCA plot of linguistic distance at age 1.6 (400 AD)                     168
4.72. PCA plot of linguistic distance at age 1.4 (600 AD)                     168
4.73. PCA plot of linguistic distance at age 1.2 (800 AD)                     169
4.74. Contour plots of the spread sea parameter at different ages              170
4.75. Contour plots of the spread parameter at different ages                 171
 5.1. Germanic unity until ~ 500 BC (± 100 years)                         209
 5.2. The fragmentation of the eastern part of the area and the formation of
     a geographically defined contact zone Eastern Rim                    209
 5.3. The diversification of Core-Germanic                               210
 5.4. The rise of the West Germanic continuum                           210

<!-- pdf-page: 17 -->
List of tables


 2.1. Sample innovations from the dataset                                11
 2.2. Sample innovations from the dataset                                12
 3.1. Distance matrix of the hypothetical languages A, B, and C               22
 3.2. Estimates of the existence time of Proto-Germanic                     43
 3.3. Summary of priors                                               53
 3.4. Attestation time estimates of the Germanic languages                   54
 3.5. Hard-bounded tip date priors                                      55
 3.6. Inferred-tip model tip date priors                                   55
 3.7. Posterior estimates of model parameters                              61
 3.8. Posterior estimates of tip ages                                      63
 3.9. Support and posterior estimates of age of specific clades across
      different models                                                 65
3.10. Support and posterior estimates of branch lengths of specific clades
      across different models                                            68
3.11. Marginal log-likelihoods of the phylogenetic models under the
      stepping-stone sampling (SS) and path sampling (PS) algorithms
     along with their differences to the model Hardbounded-JC               71
 4.1. Agent action overview chart                                       88
 4.2. Origin and tip date priors                                        113
 4.3. Posterior estimates of simulation parameters                         130
 4.4. Summary of posterior coefficients                                  133
 4.5. Summary table of model priors                                    140
 4.6. Posterior values of age parameters                                  141
 4.7. Posterior estimates of μ-hyperparameters                            146
 4.8. Posterior estimates of σ-hyperparameters                            148
 A.1. Innovation dataset                                              221
 A.2. Innovation dataset (cont.)                                        222
 A.3. Innovation dataset (cont.)                                        223
 A.4. Innovation dataset (cont.)                                        224
 A.5. Innovation dataset (cont.)                                        225
 A.6. Innovation dataset (cont.)                                        226

<!-- pdf-page: 18 -->
A.7. Innovation dataset (cont.)                                        227
 A.8. Innovation dataset (cont.)                                        228
 A.9. Innovation dataset (cont.)                                        229
A.10. Innovation dataset (cont.)                                        230
A.11. Innovation dataset (cont.)                                        231
A.12. Innovation dataset (cont.)                                        232
A.13. Innovation dataset (cont.)                                        233
A.14. Innovation dataset (cont.)                                        234
A.15. Innovation dataset (cont.)                                        235
A.16. Innovation dataset (cont.)                                        236
A.17. Innovation dataset (cont.)                                        237
A.18. Innovation dataset (cont.)                                        238
A.19. Innovation dataset (cont.)                                        239
A.20. Innovation dataset (cont.)                                        240
A.21. Innovation dataset (cont.)                                        241
A.22. Posterior estimates of feature occurrence times                       242
A.23. Posterior estimates of feature occurrence times (cont.)                 243
A.24. Posterior estimates of feature occurrence times (cont.)                 244
A.25. Posterior estimates of feature occurrence times (cont.)                 245
A.26. Posterior estimates of feature occurrence times (cont.)                 246
A.27. Posterior estimates of feature occurrence times (cont.)                 247
A.28. Posterior estimates of feature occurrence times (cont.)                 248
A.29. Posterior estimates of feature occurrence times (cont.)                 249
A.30. Posterior estimates of feature occurrence times (cont.)                 250
A.31. Posterior estimates of feature occurrence times (cont.)                 251
A.32. Posterior estimates of feature occurrence times (cont.)                 252
A.33. Posterior estimates of feature occurrence times (cont.)                 253
A.34. Posterior estimates of feature occurrence times (cont.)                 254
A.35. Posterior estimates of feature occurrence times (cont.)                 255
A.36. Posterior estimates of feature occurrence times (cont.)                 256
A.37. Posterior estimates of feature occurrence times (cont.)                 257
A.38. Posterior estimates of feature occurrence times (cont.)                 258
A.39. Posterior estimates of feature occurrence times (cont.)                 259
A.40. Posterior estimates of feature occurrence times (cont.)                 260
A.41. Posterior estimates of feature occurrence times (cont.)                 261
A.42. Posterior estimates of feature occurrence times (cont.)                 262

<!-- pdf-page: 19 -->

