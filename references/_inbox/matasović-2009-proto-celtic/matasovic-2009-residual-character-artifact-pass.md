# Matasović 2009 — Residual Character-Artifact Pass

- Generated: 2026-05-07T02:43:23Z
- Scope: pass 10 post-repair audit for residual OCR/character artifacts.

## Literal artifact searches

| Pattern | Count | Status | First hits |
|---|---:|---|---|
| `[unclear]` | 0 | clean | — |
| `fJ` | 0 | clean | — |
| `[Noun)` | 0 | clean | — |
| `(Noun]` | 0 | clean | — |
| `GOlD` | 0 | clean | — |
| `Olr.` | 0 | clean | — |
| `Peelt` | 0 | clean | — |
| `JEW` | 0 | clean | — |
| `PlE` | 0 | clean | — |
| `LElA` | 0 | clean | — |
| `Falleyev` | 0 | clean | — |
| `De1amarre` | 0 | clean | — |
| `Matasovi6` | 0 | clean | — |
| `StUber` | 0 | clean | — |
| `JordAn` | 0 | clean | — |
| `MLH V.I` | 0 | clean | — |
| `IOf` | 0 | clean | — |
| `l7th` | 0 | clean | — |
| `bOn` | 0 | clean | — |
| `*bODU` | 0 | clean | — |
| `~` | 0 | clean | — |
| `¢` | 0 | clean | — |
| `€` | 0 | clean | — |
| `£` | 0 | clean | — |
| `§` | 0 | clean | — |
| `�` | 0 | clean | — |
| `h\` | 0 | clean | — |
| `h}` | 0 | clean | — |
| `h!` | 1 | review | L8062: `**COGN:** Russ. gljadet' 'watch', Latv. dial. gledni [Ipv.] 'search!', perhaps` |
| `Stempel1999` | 0 | clean | — |
| `Stüber1998` | 0 | clean | — |
| `Matasović2004` | 0 | clean | — |
| `OreI2003` | 0 | clean | — |
| `V.l` | 0 | clean | — |
| `IE W` | 0 | clean | — |
| `DlL` | 0 | clean | — |
| `perfecet` | 0 | clean | — |
| `prerrztsa` | 0 | clean | — |
| `g/jadet` | 0 | clean | — |
| `GPCg` | 0 | clean | — |
| `g>jr` | 0 | clean | — |
| `problel` | 0 | clean | — |
| `buaautton` | 0 | clean | — |
| `buddutton` | 0 | clean | — |
| `pn:` | 0 | clean | — |
| `CEL TIB` | 0 | clean | — |
| `eEL TIB` | 0 | clean | — |
| `Bottorita` | 0 | clean | — |
| `Botorricl` | 0 | clean | — |
| `Pefialba` | 0 | clean | — |
| `UIROS'man'` | 0 | clean | — |
| `UER-AMOM[` | 0 | clean | — |
| `Toponym](A 52)` | 0 | clean | — |

## Regex artifact searches

| Test | Count | Status | First hits |
|---|---:|---|---|
| Starred token with raw hI/hz | 0 | clean | — |
| Raw ASCII labiovelar gW/kW | 0 | clean | — |
| No-space GPC form | 0 | clean | — |
| Broken name+year no-space | 0 | clean | — |
| Broken bracket heading close/open mismatch | 1 | review | L18064: `### *su- 'good' [Adv], [(Prefixed) Adjective]` |

## Section-boundary check

| Section | Hits | First hits |
|---|---:|---|
| `## References` | 2 | L87: `## References`<br>L22324: `## References` |
| `## Indices` | 2 | L88: `## Indices`<br>L23005: `## Indices` |
| `## Appendix` | 1 | L22108: `## Appendix: The Non-Indo-European Elements in the Celtic Lexicon` |

## Assessment

The targeted stress-test artifacts were substantially reduced. Remaining review hits are mostly legitimate source forms or broad-pattern false positives: the single `h!` hit is the ordinary word `search!`, and the remaining bracket-heading warning is the source-style compound heading `*su-`.
