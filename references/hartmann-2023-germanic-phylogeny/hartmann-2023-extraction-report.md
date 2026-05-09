---
title: "Germanic Phylogeny"
author: "Frederik Hartmann"
date: "2023"
source_type: "born-digital"
extraction_date: "2026-05-07"
source_file: "hartmann-2023.pdf"
chunk: "extraction-report"
---

# Hartmann 2023 extraction report

## Source type

Born-digital PDF with machine-readable text layer. The raw extracted text layer was used as the primary source. Visual rendering was used only for a spot-check of high-risk character rendering and for cropped figure images.

## Corrections applied

- Converted text-layer `∗` (U+2217 ASTERISK OPERATOR) to `*` (U+002A ASTERISK) throughout, because the visual source uses ordinary linguistic asterisk notation before reconstructed forms and the extraction instructions identify U+002A as the target character.
- Repaired spacing acute and diaeresis extraction artifacts where they followed vowels, e.g. `ra´ð` → `ráð`, `Ja¨ger` → `Jäger`, `Tübingen`, `Höhna`, and similar cases; NFC normalization was then applied.
- Removed repeated running headers, page numbers, chapter-opener DOI/copyright footer lines, and Ghostscript/text-layer control artifacts.
- Repaired source-specific extracted sequence `ˉo¸` to `ǭ` in the appendix form `*þrijǭ` (2 instances), consistent with the rendered combined macron-ogonek vowel.
- Added source-page / PDF-page anchors as HTML comments for later citation and checking.
- Extracted figure images as page-region PNG crops named in kebab-case under `images/`.

## Unresolved issues list

- The extraction is based on the machine-readable text layer; it was not manually proofread character-by-character against every rendered page. Consistent text-layer errors could therefore remain.
- Tables, especially Appendix Tables A.1-A.42, were preserved from the text layer but not fully hand-rebuilt as Markdown tables; some row/column relationships may need a targeted table pass.
- Some figure captions in the text layer wrap across lines. The image link is inserted after the first caption line; continuation text remains in place when present.
- Figure images are cropped from page regions rather than vector-extracted figure-only objects; some crops may contain nearby whitespace or surrounding text.
- Formula/table cases where a standalone numeral follows a form, such as feature rows in Appendix posterior-estimate tables, may represent superscripts or wrapped text and should be checked in a later source-critical pass.

## Confusion-pair report

- `h₁ h₂ h₃`: approximate output counts are low/zero; no comprehensive visual audit was performed.
- Macron vowels: precomposed macron vowels were preserved where present; combining macron remains where the source text layer used it, especially in forms such as `V̄`.
- Superscript modifier letters `ʰ ʷ`, schwa `ə`, underdot letters, acute consonants, and dagger: no full visual audit was performed; counts should be used only for regression comparison.
- Asterisks: U+2217 was normalized to U+002A; remaining `∗` count should be zero in the Markdown output.
- Dense index and appendix sections were not manually checked line-by-line for dropped macrons or special characters.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 0,
    "h2": 0,
    "h3": 0
  },
  "macron_a": 51,
  "macron_e": 100,
  "macron_i": 66,
  "macron_o": 96,
  "macron_u": 31,
  "schwa": 0,
  "greek_chars": 228,
  "combining_diacritics": 25,
  "dagger": 0
}
```

## Structural integrity check

- Chunking follows the source hierarchy and splits long chapters at source section/subsection boundaries.
- Bibliography, index, and backmatter series list are separate Markdown files.
- Main text files contain corpus text only; QC notes are confined to this report.
- Footnotes remain inline in page-order text rather than being converted to Markdown footnote syntax.
- Tables are preserved as text-layer line sequences, not fully normalized Markdown tables.

## Image inventory

- Figure 3.1 (source page 18): `images/hartmann-2023-fig3-1.png` — Neighbour joining network
- Figure 3.2 (source page 19): `images/hartmann-2023-fig3-2.png` — Neighbour joining phylogram
- Figure 3.3 (source page 20): `images/hartmann-2023-fig3-3.png` — UPGMA phylogram
- Figure 3.4 (source page 21): `images/hartmann-2023-fig3-4.png` — UPGMA phylogram, only innovations
- Figure 3.5 (source page 22): `images/hartmann-2023-fig3-5.png` — UPGMA phylogram, incorrect topology
- Figure 3.6 (source page 23): `images/hartmann-2023-fig3-6.png` — NeighborNet clustering
- Figure 3.7 (source page 25): `images/hartmann-2023-fig3-7.png` — NeighborNet clustering, only innovations
- Figure 3.8 (source page 30): `images/hartmann-2023-fig3-8.png` — A potential tree topology
- Figure 3.9 (source page 30): `images/hartmann-2023-fig3-9.png` — A potential tree topology
- Figure 3.10 (source page 35): `images/hartmann-2023-fig3-10.png` — Gamma density function
- Figure 3.11 (source page 44): `images/hartmann-2023-fig3-11.png` — Node age prior density
- Figure 3.12 (source page 46): `images/hartmann-2023-fig3-12.png` — Topology with unequal branch rates
- Figure 3.13 (source page 46): `images/hartmann-2023-fig3-13.png` — Incorrect inference of an underlying topology with unequal branch rates
- Figure 3.14 (source page 49): `images/hartmann-2023-fig3-14.png` — Gothic tip date prior
- Figure 3.15 (source page 52): `images/hartmann-2023-fig3-15.png` — Graphical representation of the Germanic diversification model
- Figure 3.16 (source page 57): `images/hartmann-2023-fig3-16.png` — Consensus tree of model Hardbounded-JC
- Figure 3.17 (source page 58): `images/hartmann-2023-fig3-17.png` — Consensus tree of model Hardbounded-InnovOnly
- Figure 3.18 (source page 58): `images/hartmann-2023-fig3-18.png` — Consensus tree of model Hardbounded-VarRates
- Figure 3.19 (source page 59): `images/hartmann-2023-fig3-19.png` — Consensus tree of model Inferredbounds-JC
- Figure 3.20 (source page 59): `images/hartmann-2023-fig3-20.png` — Consensus tree of model Inferredbounds-InnovOnly
- Figure 3.21 (source page 60): `images/hartmann-2023-fig3-21.png` — Consensus tree of model Inferredbounds-VarRates
- Figure 3.22 (source page 72): `images/hartmann-2023-fig3-22.png` — Visualization of episodic speciation and extinction rates over inferred time
- Figure 3.23 (source page 73): `images/hartmann-2023-fig3-23.png` — Consensus tree of the preferred model Hardbound-VarRates
- Figure 3.24 (source page 74): `images/hartmann-2023-fig3-24.png` — Maximum clade credibility tree of the preferred model Hardbound-VarRates
- Figure 4.1 (source page 87): `images/hartmann-2023-fig4-1.png` — Zoom of the simulation surface showing the three terrain types including inhabited tiles that are occupied by agents
- Figure 4.2 (source page 89): `images/hartmann-2023-fig4-2.png` — Example ABM migration: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.3 (source page 90): `images/hartmann-2023-fig4-3.png` — Example ABM migration with multiple agents: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.4 (source page 90): `images/hartmann-2023-fig4-4.png` — Example ABM migration with multiple agents and migration restrictions: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.5 (source page 91): `images/hartmann-2023-fig4-5.png` — Example ABM migration and birth with multiple agents and migration restrictions: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.6 (source page 92): `images/hartmann-2023-fig4-6.png` — Example ABM innovation with one starting agent: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.7 (source page 92): `images/hartmann-2023-fig4-7.png` — Example ABM innovation with two starting agents and two possible innovations: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.8 (source page 93): `images/hartmann-2023-fig4-8.png` — Example ABM innovation with two starting agents and two possible innovations including alignment: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.9 (source page 93): `images/hartmann-2023-fig4-9.png` — Example ABM innovation with two starting agents and two possible innovations including strong alignment after 60 ticks: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.10 (source page 94): `images/hartmann-2023-fig4-10.png` — Example ABM innovation with two starting agents and two possible innovations: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.11 (source page 95): `images/hartmann-2023-fig4-11.png` — Example ABM migration with multiple starting agents and a partial barrier: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.12 (source page 96): `images/hartmann-2023-fig4-12.png` — Example ABM innovation with two starting agents and two possible innovations: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.13 (source page 97): `images/hartmann-2023-fig4-13.png` — Example ABM innovation mechanism with two possible innovations and random innovation occurrence: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.14 (source page 98): `images/hartmann-2023-fig4-14.png` — Example ABM innovation mechanism with two unique possible innovations: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.15 (source page 100): `images/hartmann-2023-fig4-15.png` — Fixed-value update of α and β by 1 per time step
- Figure 4.16 (source page 101): `images/hartmann-2023-fig4-16.png` — Change of mean under a random normal-valued update process
- Figure 4.17 (source page 102): `images/hartmann-2023-fig4-17.png` — Trace plot of mean development for twenty agents under a random normal-valued update process
- Figure 4.18 (source page 102): `images/hartmann-2023-fig4-18.png` — Change of mean under a random normal-valued update process with values < 0.2 at tick 250
- Figure 4.19 (source page 103): `images/hartmann-2023-fig4-19.png` — Change of mean under a random normal-valued update process with update ~ Normal(0.001, 0.1)
- Figure 4.20 (source page 106): `images/hartmann-2023-fig4-20.png` — Posterior distribution of p(innovation)
- Figure 4.21 (source page 107): `images/hartmann-2023-fig4-21.png` — Posterior distribution of p(innovation), adjusted x-axis
- Figure 4.22 (source page 108): `images/hartmann-2023-fig4-22.png` — Posterior distribution of p(innovation) of the ABC with error included
- Figure 4.23 (source page 108): `images/hartmann-2023-fig4-23.png` — Posterior distribution of p(innovation) of the ABC with error included, adjusted x-axis
- Figure 4.24 (source page 109): `images/hartmann-2023-fig4-24.png` — Simulation surface map of northern Europe
- Figure 4.25 (source page 110): `images/hartmann-2023-fig4-25.png` — Evaluation space of Old English
- Figure 4.26 (source page 110): `images/hartmann-2023-fig4-26.png` — Evaluation space of Old Saxon
- Figure 4.27 (source page 110): `images/hartmann-2023-fig4-27.png` — Evaluation space of Old High German
- Figure 4.28 (source page 110): `images/hartmann-2023-fig4-28.png` — Evaluation space of Gothic, Burgundian, and Vandalic
- Figure 4.29 (source page 111): `images/hartmann-2023-fig4-29.png` — Evaluation space of Old Frisian
- Figure 4.30 (source page 111): `images/hartmann-2023-fig4-30.png` — Evaluation space of Old Norse
- Figure 4.31 (source page 119): `images/hartmann-2023-fig4-31.png` — Logarithmic loss function
- Figure 4.32 (source page 120): `images/hartmann-2023-fig4-32.png` — Model graph of the Bayesian ABM only including model-internal nodes
- Figure 4.33 (source page 123): `images/hartmann-2023-fig4-33.png` — Graphical representation of the updating module
- Figure 4.34 (source page 124): `images/hartmann-2023-fig4-34.png` — Graphical representation of the innovation module
- Figure 4.35 (source page 126): `images/hartmann-2023-fig4-35.png` — Example ABM run with two possible innovations: snapshots at ticks 0, 20, 40, 60, 80, 100
- Figure 4.36 (source page 129): `images/hartmann-2023-fig4-36.png` — Posterior distribution plot of Spreading
- Figure 4.37 (source page 130): `images/hartmann-2023-fig4-37.png` — Posterior distribution plot of Innovation
- Figure 4.38 (source page 130): `images/hartmann-2023-fig4-38.png` — Posterior distribution plot of Obstacle spreading
- Figure 4.39 (source page 131): `images/hartmann-2023-fig4-39.png` — Posterior distribution plot of Innov. 1
- Figure 4.40 (source page 132): `images/hartmann-2023-fig4-40.png` — Posterior distribution plot of Innov. 2
- Figure 4.41 (source page 135): `images/hartmann-2023-fig4-41.png` — Results from run analysis using maximum support heat maps
- Figure 4.42 (source page 136): `images/hartmann-2023-fig4-42.png` — Results from run analysis using maximum support heat maps
- Figure 4.43 (source page 137): `images/hartmann-2023-fig4-43.png` — Results from run analysis using maximum support heat maps
- Figure 4.44 (source page 138): `images/hartmann-2023-fig4-44.png` — Full model graph of the Bayesian agent-based model
- Figure 4.45 (source page 141): `images/hartmann-2023-fig4-45.png` — Posterior values of age parameters
- Figure 4.46 (source page 142): `images/hartmann-2023-fig4-46.png` — Correlation plot of posterior ages
- Figure 4.47 (source page 143): `images/hartmann-2023-fig4-47.png` — Homoplasy parameter on the scale of raw rate and homoplastic events per century (p/c)
- Figure 4.48 (source page 144): `images/hartmann-2023-fig4-48.png` — Environmental independence of agents from 0 (entirely dependent on the neighbouring agents) to 1 (completely independent from neighbouring agents)
- Figure 4.49 (source page 151): `images/hartmann-2023-fig4-49.png` — Development of the linguistic fit metric MCC (std.) as a function of age (in 1,000 years before present)
- Figure 4.50 (source page 152): `images/hartmann-2023-fig4-50.png` — Distance from Gothic fit as a function of age
- Figure 4.51 (source page 153): `images/hartmann-2023-fig4-51.png` — Distance from Vandalic fit as a function of age
- Figure 4.52 (source page 154): `images/hartmann-2023-fig4-52.png` — Distance from Burgundian fit as a function of age
- Figure 4.53 (source page 155): `images/hartmann-2023-fig4-53.png` — Distance from Old Norse fit as a function of age
- Figure 4.54 (source page 155): `images/hartmann-2023-fig4-54.png` — Distance from Old Saxon fit as a function of age
- Figure 4.55 (source page 156): `images/hartmann-2023-fig4-55.png` — Distance from Old High German fit as a function of age
- Figure 4.56 (source page 157): `images/hartmann-2023-fig4-56.png` — Distance from Old English fit as a function of age
- Figure 4.57 (source page 157): `images/hartmann-2023-fig4-57.png` — Distance from Old Frisian fit as a function of age
- Figure 4.58 (source page 158): `images/hartmann-2023-fig4-58.png` — Development of the innovation parameter in each region over time
- Figure 4.59 (source page 159): `images/hartmann-2023-fig4-59.png` — Development of the align parameter in each region over time
- Figure 4.60 (source page 160): `images/hartmann-2023-fig4-60.png` — Development of the spread parameter in each region over time
- Figure 4.61 (source page 160): `images/hartmann-2023-fig4-61.png` — Development of the spread vulnerability parameter in each region over time
- Figure 4.62 (source page 161): `images/hartmann-2023-fig4-62.png` — Development of the spread sea parameter in each region over time
- Figure 4.63 (source page 161): `images/hartmann-2023-fig4-63.png` — Development of the river spread parameter in each region over time
- Figure 4.64 (source page 162): `images/hartmann-2023-fig4-64.png` — Development of the migration parameter in each region over time
- Figure 4.65 (source page 163): `images/hartmann-2023-fig4-65.png` — Development of the river crossing parameter in each region over time
- Figure 4.66 (source page 163): `images/hartmann-2023-fig4-66.png` — Development of the birth parameter in each region over time
- Figure 4.67 (source page 165): `images/hartmann-2023-fig4-67.png` — PCA plot of linguistic distance at age 2.4 (400 BC)
- Figure 4.68 (source page 166): `images/hartmann-2023-fig4-68.png` — PCA plot of linguistic distance at age 2.2 (200 BC)
- Figure 4.69 (source page 167): `images/hartmann-2023-fig4-69.png` — PCA plot of linguistic distance at age 2 (at the beginning of the Common Era)
- Figure 4.70 (source page 167): `images/hartmann-2023-fig4-70.png` — PCA plot of linguistic distance at age 1.8 (200 AD)
- Figure 4.71 (source page 168): `images/hartmann-2023-fig4-71.png` — PCA plot of linguistic distance at age 1.6 (400 AD)
- Figure 4.72 (source page 168): `images/hartmann-2023-fig4-72.png` — PCA plot of linguistic distance at age 1.4 (600 AD)
- Figure 4.73 (source page 169): `images/hartmann-2023-fig4-73.png` — PCA plot of linguistic distance at age 1.2 (800 AD)
- Figure 4.74 (source page 170): `images/hartmann-2023-fig4-74.png` — Contour plots of the spread sea parameter at different ages
- Figure 4.75 (source page 171): `images/hartmann-2023-fig4-75.png` — Contour plots of the spread parameter at different ages
- Figure 5.1 (source page 209): `images/hartmann-2023-fig5-1.png` — Germanic unity until ~ 500 BC (± 100 years)
- Figure 5.2 (source page 209): `images/hartmann-2023-fig5-2.png` — The fragmentation of the eastern part of the area and the formation of a geographically defined contact zone Eastern Rim
- Figure 5.3 (source page 210): `images/hartmann-2023-fig5-3.png` — The diversification of Core-Germanic
- Figure 5.4 (source page 210): `images/hartmann-2023-fig5-4.png` — The rise of the West Germanic continuum
