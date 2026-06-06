# PIE Derivational Generator — Technical Spec v0.1

last_updated: 2026-06-01

---

## 1. Purpose

CLI tool. Takes a PIE verbal root as input. Generates:
- **Tier 1** — derivations operating directly on the root or an ablaut grade of it
- **Tier 2** — derivations operating on Tier 1 outputs

Output is displayed on screen. Optional markdown export. PIE forms only in v1; Ghandwa surface forms deferred.

**Build order:** Tier 1 is implemented first (well-grounded, matches the original ask). Tier 2 implementation is **deferred** pending attested input-restriction data from the reference corpus — the current Tier 2 table is provisional, and its "any nominal Tier 1" input columns are known to overgenerate and will be re-tiered before implementation. See §5.

---

## 2. CLI Interface

```
python3 tools/derive.py ROOT [--zero ZERO_GRADE] [--lengthened LENG_GRADE] [--gloss GLOSS] [--reduplication BASE] [--nasal-infix BASE] [--export]
```

| Argument | Required | Description |
|---|---|---|
| `ROOT` | yes | e-grade root with trailing hyphen, e.g. `bʰer-` |
| `--zero` | no | zero-grade form; derived algorithmically if omitted |
| `--lengthened` | no | lengthened grade, e.g. `bʰēr-`; omitted if not supplied |
| `--gloss` | no | root gloss in English, e.g. `"carry"`; enables semantic output column |
| `--reduplication` | no | reduplicated base, supplied when auto-derivation is not possible |
| `--nasal-infix` | no | nasal-infix base, supplied when auto-derivation is not possible |
| `--export` | no | write markdown to `lexicon/derivata/{egrade}-derivata.md` |

---

## 3. Root Parsing and Ablaut Algorithm

### 3.1 Input Handling

The root is processed through the shared `pie_core` primitives (§3.5), not a hand-rolled parser:

1. `normalize(root)` — NFC-normalizes, strips leading `*`, extracts any input accent, and expands ASCII shorthand (`bh`→`bʰ`, `gwh`→`gʷʰ`, `H2`→`h₂`, `r_`→`r̥`, `g'`→`ǵ`, etc.). The derivator ignores any input accent and assigns its own per pattern (§3.7). This means the user may type `bher-`, `g'neh3-`, or the canonical `bʰer-` interchangeably.
2. `tokenize(clean)` — returns a token list (longest-match), e.g. `bʰer-` → `['bʰ', 'e', 'r', '-']`. Multichar segments (`bʰ`, `gʷʰ`, `kʷ`, `h₂`, `r̥`) are already atomic, so locating and manipulating the `e` token is safe.

All ablaut operations (§3.2) work on the token list, not the raw string. The trailing morpheme-boundary token `-` is retained internally and stripped for display.

**Degenerate input:** if the tokenized root contains zero `e` tokens (root supplied in o- or zero-grade) or more than one, flag `[ambiguous root vowel — supply e-grade]` and proceed only with grades that can be formed unambiguously.

### 3.2 Ablaut Grades

**Accent and ablaut grade are independent dimensions.** Neither predicts the other. *wĺ̥kʷos* is zero-grade root-accented; *bʰorós* is o-grade suffix-accented. The spec tracks them in separate columns.

**`variable` accent_type** means the pattern generates both accent variants as distinct output rows. Gary selects.

Operations are on the token list. Let `e` be the root-vowel token.

| Grade | Algorithm | `bʰer-` | `ǵneh₃-` | `yewg-` | `sed-` |
|---|---|---|---|---|---|
| e-grade | as supplied | `bʰer-` | `ǵneh₃-` | `yewg-` | `sed-` |
| o-grade | `e` token → `o` | `bʰor-` | `ǵnoh₃-` | `yowg-` | `sod-` |
| zero-grade | delete `e` token, then resolve deletion site (below) | `bʰr̥-` | `ǵn̥h₃-` | `yug-` | `sd-` |
| lengthened | `e` token → `ē` | `bʰēr-` | `ǵnēh₃-` | `yēwg-` | `sēd-` |

**Zero-grade resolution (sonority-based, operates on the post-deletion token sequence):** after removing the `e` token, inspect the segments now adjacent to the deletion site.

1. If a **liquid or nasal** (`r l m n`) is now interconsonantal (or consonant-flanked at a word edge) on either side of the site — whether it came from the onset cluster or the coda — syllabify it: `r→r̥`, `l→l̥`, `m→m̥`, `n→n̥`. This catches both *bʰer-* → *bʰr̥-* (coda) and *ǵneh₃-* → *ǵn̥h₃-* (onset cluster).
2. If a **glide** (`w`, `y`/`j`) is in that position, it **vocalizes** rather than syllabifying: `w→u`, `y`/`j→i`. So *yewg-* → *yug-*, *leykʷ-* → *likʷ-*, *bʰewdʰ-* → *bʰudʰ-*.
3. If **no resonant or glide** is adjacent (e.g. *sed-* → *sd-*, *deh₃-* → *dh₃-*), the bare consonant cluster **is** the zero grade. This is valid (cf. *ni-sd-os* "nest"); do not flag.
4. **Flag for `--zero`** only on genuine ambiguity: two candidate nuclei flanking the site (both sides resonant/glide), or a known Narten/*schwebe* irregularity the algorithm cannot resolve. Print `[zero-grade ambiguous — supply --zero]` and skip zero-grade-dependent patterns.

`--zero`, when supplied, overrides the algorithm entirely.

### 3.3 Reduplication

Reduplication vowel differs by formation:
- **Reduplicated present** (`RedupPres`): **i-reduplication**, `C₁i-`. *dʰi-dʰeh₁-ti*, *si-sd-eti*, *gʷi-gʷeh₃-*.
- **Perfect** (`Perfect`): **e-reduplication**, `C₁e-`. *we-woid-e*, *bʰe-bʰór-e*.

`C₁` = the first atomic consonant token of the onset.

**Predictable:** onset is a single atomic consonant. Auto-derive.
Example: `bʰer-` → present *bʰi-bʰer-* / perfect *bʰe-bʰór-*.

**Not predictable — prompt user:** onset begins with s+C cluster (reduplication may copy either segment, with s-mobile complications), laryngeal (colors the reduplication vowel), or ambiguous cluster. Tool skips the affected pattern and prints:
```
[RedupPres skipped — complex onset. Supply --reduplication BASE to generate.]
```

### 3.4 Nasal Infix Insertion

**Predictable:** coda-final segment is a single atomic consonant. Insert `né` before it in strong grade, `n` in weak grade.
Example: `yewg-` → coda `wg` → coda-final = `g` → `yu-né-g-ti` / `yu-n-g-énti`.

**Not predictable — prompt user:** coda-final segment is a cluster or otherwise ambiguous. Tool skips `NasalPres` and prints:
```
[NasalPres skipped — complex coda. Supply --nasal-infix BASE to generate.]
```

### 3.5 Shared Primitives (`pie_core`)

The tokenizer, token inventory, and normalizer are **PIE-general primitives shared by both the transformer and the derivator**, extracted into `tools/pie_core/`:

```
tools/pie_core/
  tokens.py       # inventory (PHONEME_PATTERNS) + category sets + predicates
  tokenize.py     # tokenize(), tokens_to_string(), accent mapping
  normalize.py    # normalize(): NFC, star-strip, accent extraction, shorthand expansion
```

The derivator imports:

```python
from pie_core.normalize import normalize
from pie_core.tokenize import tokenize, tokens_to_string
from pie_core.tokens import LIQUIDS, NASALS, GLIDES, SYL_RES, is_consonant, is_vowel
```

`pie_core/tokens.py` retains the full union inventory (including daughter-output tokens β/ð/ɣ and the uvulars); the derivator simply uses the PIE subset. The transformer is refactored to import from `pie_core` in the same operation (see §11). One canonical inventory, no duplication, neither end-tool depends on the other.

**Zero-grade segment classes:** liquids/nasals (`LIQUIDS | NASALS` = `r l m n`) syllabify to `SYL_RES`; glides (`GLIDES` = `w y j`) vocalize to `u`/`i` — they do **not** syllabify to `w̥`/`y̥`. See §3.2 step 2.

### 3.6 Stem vs. Citation Form

Every pattern emits two values:
- a **citation form** (with inflectional ending) for display, e.g. `ThemNounR` → *bʰóros*;
- a **derivational stem** (no ending) for Tier 2 chaining, e.g. *bʰóro-*.

**Morpheme-boundary rule (the only one needed):** when a suffix is **vowel-initial** and the base stem ends in the **thematic vowel** (`-o-`/`-e-`), the thematic vowel is **deleted** before the suffix. Otherwise the suffix appends to the stem.

- `FemEh2 ← ThemNounR`: stem *bʰóro-* + vowel-initial *-eh₂* → delete thematic vowel → *bʰór-eh₂* → cite *bʰórā*. ✓ (not \**bʰoroeh₂*)
- `Possessive ← SStem`: stem *bʰéres-* + consonant-initial *-went-* → append → *bʰéreswent-*. ✓

This rule is mechanical and bites only where naive concatenation would otherwise produce hiatus.

### 3.7 Accent Placement

`accent_type` is a label; the tool places the acute (combining/precomposed, on the vowel or syllabic resonant, matching `pie_core.normalize`'s convention so forms round-trip to the transformer later):

- `root` — acute on the nucleus of the root syllable.
- `suffix` — acute on the suffix nucleus.
- `mobile` — cite the strong-stem cell with its accent; note the weak stem alongside where the construction column gives one (e.g. `AgentNounE` nom. *déh₃-tōr* / obl. *deh₃-tór-*).
- `inherit` — copy the accented position of the input stem (Tier 2).

A single form carries exactly one acute.

---

## 4. Tier 1 Patterns

Each row = one generation function. Output label used in screen display and as key in Tier 2 lookups.

| Label | Pattern name | Input grade | PIE construction | accent_type | Output category |
|---|---|---|---|---|---|
| `RootPres` | Root present | e/zero alternation | `onset-é-coda-ti` (sg.) / `onset-∅-coda-énti` (pl.) | mobile | verbal present stem |
| `ThemPres` | Thematic present | e-grade | `onset-é-coda-e-ti` | root | verbal present stem |
| `RedupPres` | Reduplicated present | C₁i- + e/zero | `C₁i-onset-é-coda-ti` | root | verbal present stem |
| `NasalPres` | Nasal-infix present | zero-grade + infix | `onset-∅coda₁-né-coda_final-ti` | suffix | verbal present stem |
| `NasalSuf` | Nasal-suffix present | variable | `grade-néw-ti` / `grade-nu-énti` | suffix | verbal present stem |
| `SkePres` | *-sḱe/o-* present | zero-grade | `zero-sḱé-ti` | suffix | iterative/inchoative present |
| `YePres` | *-ye/o-* present | zero-grade | `zero-yé-ti` | suffix | present stem |
| `CausIter` | Causative/iterative | o-grade | `o-grade-éye-ti` | suffix | causative/iterative verbal stem |
| `Perfect` | Perfect | C₁e- + o-grade | `C₁e-ó-grade-e` (3sg.) | root | perfect/stative stem |
| `RootAor` | Root aorist | e/zero | `onset-é-coda-t` (3sg.) | root | aorist stem |
| `SigAor` | Sigmatic aorist | lengthened (active sg.) | `lengthened-s-t` | root | aorist stem (*dēyḱ-s-t*) |
| `RootNounAcro` | Root noun, acrostatic | root-fixed, paradigm-dependent | grade-specific bare stem, root-accent throughout paradigm | root | noun, acrostatic paradigm (*dóm-* "house") |
| `RootNounMob` | Root noun, mobile | root/ending alternating | grade-specific bare stem, mobile accent | mobile | noun, mobile paradigm (*pṓd-s ~ ped-és* "foot") |
| `ThemNounR` | Thematic noun, o-grade root-accent | o-grade | `ó-grade-o-s` | root | action/result noun (*bʰóros* "burden, thing carried") |
| `ThemNounS` | Thematic noun, o-grade suffix-accent | o-grade | `o-grade-ó-s` | suffix | agent/active noun (*bʰorós* "bearer, carrier") |
| `ThemNounZR` | Thematic noun, zero-grade root-accent | zero-grade | `∅-grade-o-s` (root-accent) | root | lexicalized animate/common noun (*wĺ̥kʷos* "wolf") |
| `ThemNounZS` | Thematic noun, zero-grade suffix-accent | zero-grade | `∅-grade-ó-s` | suffix | object/result/instrument noun (*yugóm* "yoke") |
| `VerbAdjTo` | Verbal adjective *-tó-* | zero-grade | `zero-tó-s` | suffix | result/passive adjective |
| `VerbAdjNo` | Verbal adjective *-nó-* | zero-grade | `zero-nó-s` | suffix | state adjective |
| `AdjRo` | Adjective *-ró-* | zero-grade | `zero-ró-s` | suffix | state/result adjective |
| `AdjLo` | Adjective *-ló-* | root-specific; e-grade or zero-grade | `grade-ló-s` | suffix | adjective |
| `ActNounTi` | Action noun *-tí-* | zero-grade | `zero-tí-s` | suffix | action noun / abstract |
| `ActNounTu` | Action noun *-tú-* | zero-grade | `zero-tú-s` | suffix | verbal noun |
| `MenNounR` | Neuter *-mn̥* noun | e-grade (root full grade) | `é-grade-mn̥` (nom./acc. sg.) / `é-grade-mōn` (pl.) | root | neuter result/action/instrument noun (*dʰéh₁-mn̥*, *spér-mn̥*); Yates: paradigmatic root full grade, fixed root stress |
| `MonNounPrim` | Primary deverbal *-món-* noun | zero-grade | `∅-grade-món-` | suffix | primary deverbal noun/adjective (*wid-món-* "knowing", *pl̥th₂-món-* "breadth"); Yates: independent resegmented suffix, zero-grade root, stem-final stress |
| `AgentNounE` | Agent noun, event-agent | e-grade | `é-grade-tōr` (nom.) / `e-grade-tór-` (obl.) | root | event-agent noun (*déh₃-tōr* "giver") |
| `AgentNounR` | Agent noun, role-agent | zero-grade | `∅-grade-tḗr` | suffix | role/status agent noun (*dh₃-tḗr* type) |
| `SStem` | s-stem neuter | e-grade | `é-grade-es-` (stem) | root | abstract/result noun |
| `UStemC` | u-stem, Caland type | zero-grade | `zero-ú-s` | suffix | Caland-system adjective (*gʷr̥h₂-ú-s* "heavy") |
| `UStemM` | u-stem, mobile non-Caland | zero-grade | `zero-u-s` | mobile | noun (*méd-hu* "mead" type) |
| `IStem` | i-stem | e-grade or o-grade, root-specific | `grade-i-s` | variable | noun/adjective; both accent variants generated |
| `FemEventNoun` | Primary feminine event/result noun *-éh₂* | o-grade | `o-grade-éh₂` | suffix | feminine event/result noun (*tomh₁-éh₂* "cutting") |
| `InstrNounTro` | Instrument noun *-tro-* | root-specific; zero-grade or e-grade | `grade-tro-m` | variable | neuter instrument noun (*h₂érh₃-tro-m* "plow"); both accent variants generated |
| `InstrNounTlo` | Instrument noun *-tlo-* | root-specific; zero-grade or e-grade | `grade-tlo-m` | variable | neuter instrument noun (*sneh₁-tló-m* "needle"); both accent variants generated |
| `LoNoun` | Noun *-lo-* | root-specific; e-grade possible | `grade-lo-` | variable | noun of place/object/result (*sed-lo-* "seat"); both accent variants generated |
| `MoNoun` | Noun/adjective *-mo-* | root-specific; e-grade or o-grade | `grade-mo-` | variable | action/event noun; adjective (*gʷher-mo-* "heat, warm"); both accent variants generated |
| `NoNoun` | Noun *-no-* | root-specific; e/o/zero variation | `grade-no-` | variable | noun of various sorts (*deh₃-no-* "gift"); both accent variants generated |
| `MenNounAnim` | Animate (ID) *-mōn-* noun | e-grade (root full grade) | `é-grade-mṓn` (nom. sg.) / `é-grade-mn-´` (weak, stressed ending) | mobile | animate/common internal derivative from a neuter *-men-* base (*dʰarmā́ṇam* "supporter" ← *dʰárma*); Yates: root full grade, stem-final stress strong |

---

## 5. Tier 2 Patterns

> **PROVISIONAL — IMPLEMENTATION DEFERRED.** Input restrictions below are now sourced from the reference corpus (ChatGPT pass against Fortson, Neri & Schuhmann, Keydana/Hock/Widmer, NIL, LIV²) and the `input from` columns have been re-tiered to attested bases. The split is largely **adjective-input vs. nominal-input**: comparative/superlative/factitive/abstract-from-adjective take adjective stems; collective/relational/possessive/feminine take nominal stems. Tier 1 still ships first; this table is implemented in the second phase.

**Two patterns dropped from the deverbal generator:** `ComparativeTero` (*-tero-*) and `SuperlativeMm̥o` (*-m̥mo-*) take pronominal/deictic/spatial/local bases, which a verbal root does not produce. They are retained in the catalog note below for reference but are **not generated**.

When implemented, output volume uses a **high-yield default** (each pattern fires from its most representative base) with `--all` for the full cross-product over all eligible bases.

Each row takes one or more Tier 1 labels as input. `input from` lists the Tier 1 labels that feed this pattern.

| Label | Pattern name | Input from | PIE construction | accent_type | Output category |
|---|---|---|---|---|---|
| `PresActPtcp` | Present active participle (thematic) | `ThemPres`, `SkePres`, `YePres`, `CausIter` | pres.stem + `-nt-s` | inherit | active participle |
| `PresActPtcpAthem` | Present active participle (athematic) | `RootPres`, `NasalPres`, `NasalSuf`, `RedupPres` | pres.stem + `-ent-s` (strong) / `-nt-` (weak) | inherit | athematic active participle |
| `MidPtcp` | Middle participle | `ThemPres`, `SkePres`, `YePres` | pres.stem + `-mh₁no-s` | inherit | middle participle |
| `PerfPtcp` | Perfect active participle | `Perfect` | perf.stem + `-wós-` (strong) / `-us-` (weak) | suffix | perfect participle |
| `AorActPtcp` | Aorist active participle | `RootAor`, `SigAor` | aor.stem + `-nt-s` | suffix | aorist active participle |
| `FemEh2` | Feminine *-eh₂* | thematic adj/noun: `ThemNounR`, `ThemNounS`, `ThemNounZR`, `ThemNounZS`, `VerbAdjTo`, `AdjRo` | stem + `-eh₂` | inherit | feminine of thematic stems (consonant-stem/agent feminines prefer `-ih₂`) |
| `FemIh2` | Feminine *-ih₂* | animate/agent: `AgentNounE`, `AgentNounR`, animate nouns, derived consonant stems | stem + `-ih₂` | inherit | feminine of animate/agent nouns |
| `Collective` | Collective *-eh₂* | neuter/count nominal stems: `ThemNounZS`, `SStem`, `InstrNounTro`, `InstrNounTlo`, `MenNounR` | stem + `-eh₂` | suffix | collective / neuter plural of count nouns |
| `AbstractAdj` | Abstract from adjective | adjective stems: `AdjRo`, `VerbAdjTo`, `UStemC` (Caland/property) | stem + `-eh₂` or `-ih₂` | inherit | abstract noun |
| `Comparative` | Comparative *-yos-* | property adjectives: `AdjRo`, `VerbAdjTo`, `UStemC` | stem + `-yos-` (strong) / `-is-` (weak) | mobile | comparative adjective (amphikinetic) |
| `Superlative` | Superlative *-isto-* | property adjectives: `AdjRo`, `VerbAdjTo`, `UStemC` | stem + `-isto-s` | suffix | superlative adjective |
| `Possessive` | Possessive *-went-* | nominal stems (concrete + abstract/result): `SStem`, `MenNounR`, `MenNounAnim`, `ThemNounR`, `ThemNounS` | stem + `-went-s` | suffix | possessive adjective |
| `Relational` | Relational *-iyo-* | nominal stems (thematic + consonant-stem nouns) | stem + `-iyo-s` | suffix | relational adjective |
| `SecThematic` | Secondary thematicization | `SStem` | oblique-stem + `-o-s` | inherit | thematic noun/adjective |
| `DenomVerb` | Denominal *-ye/o-* verb | nominal **and** adjectival stems | stem + `-yé-ti` | suffix | denominal "be/become/do X" verb |
| `Factitive` | Factitive *-éye/o-* | adjective stems (property): `AdjRo`, `VerbAdjTo`, `UStemC` | stem + `-éye-ti` | suffix | factitive "make X" verb |
| `AgentFem` | Feminine from agent noun | `AgentNounE`, `AgentNounR` | agent-obl-stem + `-ih₂` | inherit | feminine agent noun |
| `AbstractActNoun` | Abstract from action noun | `ActNounTi`, `MenNounR`, `MenNounAnim`, `MonNounPrim` | stem + `-eh₂` | suffix | abstract/collective noun |
| `SubstTo` | Substantivized *-to-* adjective | `VerbAdjTo` | accent retraction to root syllable | root | result/exemplar noun (*ǵénh₁-to-m* "thing born") |
| `CausalFromNoun` | Caland network derivative | `AdjRo`, `UStemC` | Caland-network alternation | variable | adjective/abstract network; both accent variants generated |

**Catalog-only (not generated — base type not produced from a verbal root):**

| Label | Pattern name | Attested base | Note |
|---|---|---|---|
| `ComparativeTero` | Contrastive *-tero-* | pronominal/deictic/adverbial/spatial/contrastive | *deḱs-tero-* "right-hand"; ordinary qualitative comparison is *-yos-*. No deverbal base. |
| `SuperlativeMm̥o` | Superlative *-m̥mo-* | local/adverbial/spatial/scalar | "extreme position" type; general adjective superlative is *-isto-*. No deverbal base. |

---

## 6. Output Format

### 6.1 Screen

Forms display in PIE notation. With `--gloss`, a semantic **function chain** is appended (§7) — the tool does not synthesize a finished English gloss; it shows the base meaning plus each suffix's general function, and Gary supplies the real lexical gloss on selection.

```
ROOT: *bʰer-  (zero *bʰr̥-  o-grade *bʰor-  lengthened *bʰēr-)   gloss: "carry"

TIER 1 — ROOT DERIVATIONS
  ThemPres     *bʰéreti        "carry" → [thematic present]
  ThemNounR    *bʰóros         "carry" → [o-grade root-accent: result/action noun]
  ThemNounS    *bʰorós         "carry" → [o-grade suffix-accent: agent noun]
  VerbAdjTo    *bʰr̥tós         "carry" → [verbal adj: result/passive]
  ActNounTi    *bʰr̥tís         "carry" → [action noun]
  MenNounR     *bʰérmn̥          "carry" → [neuter result noun]
  AgentNounE   *bʰértōr         "carry" → [event-agent noun]
  SStem        *bʰéres-         "carry" → [s-stem abstract/result]
  ...

TIER 2 — SECONDARY DERIVATIONS   (deferred; see §5)
```

Without `--gloss`, the function-chain tail still prints (e.g. `[event-agent noun]`), just without the leading root meaning.

### 6.2 Markdown Export

Mirrors screen structure. Filename: `{sanitized-egrade}-derivata.md` under `lexicon/derivata/`. Sanitization: replace `ʰ` → `h`, `ʷ` → `w`, `̥` → `0`, other non-ASCII → closest ASCII equivalent. Directory created if absent.

Header includes: root, date, grades used.

---

## 7. Semantics — Function Chain

The tool does **not** synthesize finished English glosses (templating "female {burden}" is both fragile and false-precise at derivational distance). Instead each pattern carries a single **function label**, and output shows the derivational path. Gary reads the chain and supplies the real lexical gloss when selecting a form.

### 7.1 Function Store

File: `tools/pie_core/derivation-functions.tsv` (shared location; derivator-only consumer for now). Columns:

```
label	function
```

One function label per pattern, e.g.:

```
ThemNounR	o-grade root-accent: result/action noun
ThemNounS	o-grade suffix-accent: agent noun
ActNounTi	action noun / abstract
AgentNounE	event-agent noun
VerbAdjTo	verbal adjective: result/passive
```

### 7.2 Output

- **Tier 1, with `--gloss "carry"`:** `"carry" → [function]`
- **Tier 1, no `--gloss`:** `[function]`
- **Tier 2 (when implemented):** the chain extends — `"carry" → [base function] → [suffix function]` — making the derivational distance visible rather than papering over it with a fabricated gloss.

No slot-filling, no `{GLOSS}` substitution. The store is a flat label lookup.

---

## 8. File Locations

```
tools/pie_core/                     # shared primitives (extracted; see §11)
  tokens.py  tokenize.py  normalize.py
  derivation-functions.tsv          # §7 function store
tools/derive.py                     # the derivator
```

`unicodedata.normalize('NFC', ...)` is applied via `pie_core.normalize` to all input; lemma comparisons NFC-normalize.

---

## 9. Out of Scope for v1

- **Tier 2 implementation** — deferred pending attested input-restriction data (§5)
- Ghandwa surface forms / transformer integration — deferred
- `auto_generate` / `productivity_status` / `confidence` metadata — deferred
- Desiderative and Intensive patterns — excluded; require root-specific information not inferable from input
- Batch input (multiple roots in one run)
- NocoDB write-back

---

## 10. Resolved Data

- **Tier 2 input restrictions** — received (Fortson, Neri & Schuhmann, Keydana/Hock/Widmer, NIL, LIV²). §5 re-tiered: adjective-input vs. nominal-input split; `ComparativeTero` and `SuperlativeMm̥o` dropped from the generated set (no deverbal base).
- **m-stem accent classes (Yates)** — received. §4 restructured: `MenNounR` corrected to root full grade; `MenNounS` dropped (no productive suffix-accented deverbal neuter); `MonNounPrim` added (primary deverbal *-món-*, zero-grade, suffix-accent); `MenNounAnim` confirmed as ID *-mōn-*.

No open questions.

---

## 11. Architecture & Extraction Plan

`pie_core` is extracted from `pie_transformer` as a prerequisite to building the derivator. This is one atomic refactor (a half-done extraction leaves the transformer with dangling imports):

1. Grep every import of `.tokens` / `.tokenize` / `.normalize` across `pie_transformer/` (includes `tsv_io.py`, which uses `strip_crlf` from `normalize.py`).
2. Create `tools/pie_core/` with the three modules moved verbatim; add `__init__.py`.
3. Redirect all transformer import sites to `pie_core`.
4. Run the transformer's existing test suite → confirm green.
5. Build `tools/derive.py` (Tier 1) against `pie_core`.

Testing runs in a container clone; only verified files are written back to the working copy. Before writing back, re-pull local state and diff, to preserve any uncommitted transformer changes. Gary commits — Claude cannot push.
