---
title: "Handoff — Transformer Pipeline Spec Gaps"
last_updated: 2026-06-06T00:00-04:00
status: open
---

# Transformer Pipeline Spec Gaps

Pipeline spec docs live in `tools/docs/pie_transformer/`. The following pipelines have implementations in `tools/pie_transformer/pipelines/` but no corresponding spec doc.

## Pipelines without spec docs

| Pipeline file | Notes |
|---|---|
| `ghandwa.py` | Main Ghandwa pipeline; the core of the transformer. No standalone spec. Rule set is partially reconstructable from `tools/docs/pie_transformer/ARCHITECTURE.md` and `docs/grammar/ch3-development/sec3-2-sound-changes/` but no single authoritative doc. |
| `late_common_ghandwa.py` | Shared Stage 1 rules applied before daughter divergence. No standalone spec. |
| `daughter_a.py` | Daughter A (Western). Stage 2A rules documented in `docs/grammar/ch5-daughters/ch5-03-comparative-phonology.md` §2A but no dedicated pipeline spec doc. |
| `proto_anatolian.py` | Proto-Anatolian pipeline. No spec doc at all; status and rule coverage unknown. |

## Pipelines with partial or external specs

| Pipeline file | Spec location | Gap |
|---|---|---|
| `daughter_b.py` | `docs/grammar/ch5-daughters/ch5-03-comparative-phonology.md` §2B | No standalone `tools/docs/pie_transformer/` spec; ch5 doc is authoritative but not transformer-focused |
| `daughter_c.py` | `docs/grammar/ch5-daughters/ch5-03-comparative-phonology.md` §2C, 3C | Same as above |
| `wekwos_old.py` + `wekwos_neo.py` | `tools/docs/pie_transformer/crotonian-rules.md` | Doc predates pipeline split into Old/Neo; two rules in wekwos_neo.py (final nasal drop, final lateral rhotacism) not yet documented |

## Recommended next steps

1. Write a standalone spec for `ghandwa.py` — highest priority, as it is the root pipeline.
2. Write a standalone spec for `late_common_ghandwa.py`.
3. Assess `proto_anatolian.py` — read the implementation and determine scope and status.
4. Write a standalone spec for `daughter_a.py` (can largely reference ch5-03).
5. Update `crotonian-rules.md` to document the two undocumented wekwos_neo.py rules: final nasal drop (VN# → Ṽ#) and final lateral rhotacism (l → r / _#).
