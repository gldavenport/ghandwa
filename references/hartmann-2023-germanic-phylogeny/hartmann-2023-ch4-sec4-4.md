---
title: "Germanic Phylogeny"
author: "Frederik Hartmann"
date: "2023"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "hartmann-2023.pdf"
chunk: "§4.4"
pages: "87"
---

# 4.4 The setting and purpose of the Germanic diversification model


<!-- source-page: 87; pdf-page: 106 -->
4.4 SETTING AND PURPOSE OF THE GERMANIC DIVERSIFICATION MODEL  87

migration values are compatible with the data, or, in other words, the param-
eter migration is negligible in its impact on the simulation outcome. If, on
the other hand, this parameter showed a very narrow posterior distribution
around the value 0.5, it would indicate that only a small range of values around
0.5 yielded a good fit to the data. Therefore, the flexibility in the parameters is
of crucial importance to the interpretation of the simulation results.


          4.4 The setting and purpose of the Germanic
                      diversification model

As has been touched on in previous sections, the aim of this endeavour is
to devise an agent-based model that simulates the diversification of the Ger-
manic languages by modelling the process of innovation, innovation spread,
and population migration. The result is thus a model that computationally
reconstructs the historical events by drawing mainly on a wave-like horizontal
process.
  The environment to which the model is applied is an approximation of late
Bronze Age and early Iron Age northern central Europe. This approximation
is represented as a grid (i.e. a map) with representations of three terrain types:
inhabitable land, sea, and river. The map is subdivided into smaller pieces of
terrain (henceforth: tiles) which the simulated entities (henceforth: agents)
are positioned. Figure 4.1 shows a zoomed part of the simulation surface to
illustrate the individual terrain types.
  The agents in this model represent individual speech communities and
function as the smallest simulated units. Each agent is positioned on an inhab-
itable tile and can border a river tile, a free (inhabitable) tile, an occupied
(inhabitable) tile, and a non-inhabitable tile.


                      Sea tiles                         Uninhabited tiles


                    Inhabited tiles                           River tiles

Figure4.1 Zoom of the simulation surface showing the three terrain types includ-
ing inhabited tiles that are occupied by agents
