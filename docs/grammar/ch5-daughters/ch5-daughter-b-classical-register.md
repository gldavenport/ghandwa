# Daughter B: Classical Register

---
last_updated: 2026-06-15
status: working notes
related: ch5-01-overview.md, ch5-02-late-common-ghandwa.md, docs/world/ghandwa-historical-sociolinguistic-model.md
---

## Overview

Daughter B (Xandwā) has two strata: a living spoken register and a classical
literary register. The classical register is not a direct continuation of
Common Ghandwa but an artificially codified prestige variety, created at a
specific historical moment by scribal and priestly networks as an instrument
of administrative and religious power. It is nobody's native language.

Historical parallel: Katharevousa Greek. Secondary parallels: Carolingian
Latin reform, post-Pāṇinian Sanskrit.

---

## Sociolinguistic Context

The classical register emerges in the Iron Age transition, when the old
trifunctional Dumézilian order (sovereign/priestly, warrior, producer)
is disrupted by the rise of a mercantile class with no place in the
sacred tripartite scheme. This fourth type — whose power derives from
circulation and information asymmetry rather than production or force —
co-opts or creates the classical register as a centering tool.

The difficulty of the classical register is functional, not incidental.
Legal documents, contracts, property records, and religious texts in
classical Xandwā require specialist training to read and write correctly.
This gates access to administrative, legal, and religious authority within
the networks that control the standard. The scribal class operates as a
junior partner: literate enough to administer, not powerful enough to
challenge.

The syntax of classical B texts becomes progressively rigid and formulaic
as the morphological distinctions the register has collapsed require
syntactic disambiguation instead. Over time syntactic rigidity itself
becomes a prestige marker; loose syntax signals low register or uneducated
composition.

---

## Transformer Architecture

The classical register is implemented as a fork from the Daughter B pipeline
at a specified point, followed by a prestige correction ruleset rather than
continued regular development.

```
ghandwa.py → late_common_ghandwa.py → daughter_b.py         [spoken]
                                     ↘ daughter_b_classical.py  [literary]
```

**Fork point:** After regular Daughter B sound changes are complete, before
any spoken B innovations. The classical register is essentially Stage 2B
output dressed with artificial etymological spelling conventions and
morphological hypercorrections.

**Prestige correction ruleset** (`daughter_b_classical.py`) applies:
- Pseudo-etymological restorations (undoing some regular B changes,
  inconsistently)
- Hypercorrections (restored forms applied in environments where they
  historically did not occur)
- Morphological regularization toward a prestigious norm
- Possible lexical borrowing back from Common Ghandwa forms

The corrections are rule-governed but with documented exceptions, producing
a system that feels like a living tradition rather than mechanical restoration.

---

## i-stem and u-stem Hypercorrection

The most systematic classical B intervention is in the i- and u-stem
declensions. Scribes identify stems in *-i-* and *-u-* and preserve the
glide at all costs, jamming it against every ending mechanically regardless
of the original phonological behavior.

**Spoken B outcomes** (regular development):

| Form | i-stem | u-stem |
|---|---|---|
| gen sg | *-eis* | *-ews* |
| nom pl | *-eies* | *-ewes* |

The *e*-vowel in the ending caused the glide to interact differently across
cells, producing distinct surface forms that the scribes failed to recognize
as the same paradigm.

**Classical B correction:**

| Form | i-stem | u-stem |
|---|---|---|
| gen sg | *-ies* | *-wes* |
| nom pl | *-ies* | *-wes* |

The same fix applies to all oblique cases (dat sg, acc sg, etc.).

**Consequence:** The correction eliminates a morphological distinction that
the regular sound changes had actually preserved, just in a form the scribes
did not recognize. Gen sg and nom pl are now homophonous in both declension
classes. Spoken B retains the distinction; classical B loses it.

This creates a **covert case system** in the classical register: distinctions
are still present semantically but have been pushed from morphology into
syntax and context. Educated readers learn to resolve gen/nom pl ambiguity
from word order and clause structure. The resulting syntactic rigidity
compounds over time.

The irony is precise: the "restoration" destroys something the spoken
language still had.

---

## Spoken B / Classical B Split

| | Spoken B | Classical B |
|---|---|---|
| i/u-stem paradigm | Distinct gen sg / nom pl | Collapsed under *-ies* / *-wes* |
| Ambiguity resolution | Morphology | Syntax + context |
| Syntactic rigidity | Flexible | Fossilized formulaic order |
| Access | Native acquisition | Years of specialist training |
| Orthography | Reflects current phonology | Fossilized at fork point |

---

## 🔲 Pending

- Fork point: specify exactly which stage in daughter_b.py the classical
  register branches from
- Full prestige correction ruleset beyond i/u-stem fix
- Identify which other morphological classes receive "fixup"
- Document hypercorrection-in-reverse: ordinary speakers imitating the
  classical register imperfectly (source of further morphological erosion
  in late spoken B)
- Social worldbuilding: is the classical register primarily religious,
  administrative, commercial, or all three?
- Transformer implementation: `daughter_b_classical.py` stub
