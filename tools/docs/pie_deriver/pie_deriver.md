# derive.py — PIE Derivation Generator

last_updated: 2026-06-02

## What it does

`derive.py` takes a single PIE verbal root in e-grade and generates the set of
attested derivational patterns that operate directly on the root or one of its
ablaut grades. Output is PIE only — no Ghandwa surface forms. The tool is a
triage and exploration aid: it shows what is *formally derivable*, not what is
*historically attested*. Most outputs for any given root will be unattested or
implausible; that is expected.

Secondary derivations (patterns that operate on the output of primary ones, e.g.
deadjectival abstracts, denominative verbs) are not yet implemented. The output
marks them as deferred.

---

## Invocation

From `tools/`:

```
python3 derive.py ROOT [options]
```

`ROOT` is the e-grade root with a trailing hyphen. ASCII shorthand is accepted
and expanded automatically.

| Option | Description |
|--------|-------------|
| `ROOT` | E-grade root, e.g. `"bʰer-"` or shorthand `"bher-"`, `"g'neh3-"` |
| `--gloss GLOSS` | English gloss for the root, shown in each output row |
| `--zero ZERO` | Override the zero-grade (e.g. for schwebe-ablaut roots) |
| `--lengthened LENG` | Override the lengthened grade |
| `--reduplication BASE` | Override the reduplicated base (present and perfect) |
| `--nasal-infix BASE` | Override the nasal-infix base |
| `--export` | Write a markdown table to `lexicon/derivata/{root}-derivata.md` |

The screen clears on each run.

---

## Reading the output

### Header line

```
ROOT: *bʰer-*  (zero *bʰr̥-*  o-grade *bʰor-*  lengthened *bʰēr-*)   gloss: "carry"
```

Shows the four ablaut grades as computed. If the root has no single `e` token
(ambiguous or zero-only input), grades other than e are unavailable and a warning
is printed. Use `--zero` / `--lengthened` to supply them manually.

### Output rows

Rows are grouped by part of speech under `## Verbs`, `## Adjectives`, `## Nouns`.

```
  bʰéreti     thematic present   "carry"
  bʰr̥tós      verbal adjective: result/passive   "carry"
```

Columns (left to right):

1. **Derived form** — PIE notation, no asterisk. Stems (s-stems, oblique stems in
   secondary notes) carry a trailing hyphen.
2. **Derivation type** — expanded English description of the pattern.
3. **Gloss** — root gloss as supplied with `--gloss`, if any.
4. **Secondary notes** — mobile alternants, oblique stems, grade caveats; appended
   after the gloss.

`variable` patterns (where both root-accent and suffix-accent variants are
historically possible) emit two rows, labelled `(root-accent)` and `(suffix-accent)`.

Rows where a required grade is unavailable show `(skipped: reason)` instead of a form.

---

## The 36 primary derivation patterns

### Verbs

| Label | Description | Input grade | Accent |
|-------|-------------|-------------|--------|
| RootPres | Athematic root present | e-grade (sg); zero (pl) | mobile |
| ThemPres | Thematic present | e-grade | root |
| RedupPres | Reduplicated present (C₁i- prefix) | e-grade | root |
| NasalPres | Nasal-infix present (né inserted before coda) | zero | suffix |
| NasalSuf | Nasal-suffix present (-néw/-nu-) | zero | suffix |
| SkePres | Iterative/inchoative present (-sḱe/o-) | zero | suffix |
| YePres | Present (-ye/o-) | zero | suffix |
| CausIter | Causative/iterative (-éye/o-) | o-grade | suffix |
| Perfect | Perfect/stative (C₁e- reduplication, o-grade root) | o-grade | root |
| RootAor | Root aorist (3sg -t) | e-grade | root |
| SigAor | Sigmatic aorist (3sg -st) | lengthened | root |

### Adjectives

| Label | Description | Input grade | Accent |
|-------|-------------|-------------|--------|
| VerbAdjTo | Verbal adjective: result/passive (-to-) | zero | suffix |
| VerbAdjNo | Verbal adjective: state (-no-) | zero | suffix |
| AdjRo | Adjective: state/result (-ro-) | zero | suffix |
| AdjLo | Adjective (-lo-) | e-grade* | suffix |
| UStemC | Caland-system adjective (-u-) | zero | suffix |

### Nouns

| Label | Description | Input grade | Accent |
|-------|-------------|-------------|--------|
| RootNounAcro | Root noun, acrostatic | e-grade | root |
| RootNounMob | Root noun, mobile (nom. -s / obl. zero) | e-grade / zero | mobile |
| ThemNounR | Thematic noun: o-grade, root-accent (result/action) | o-grade | root |
| ThemNounS | Thematic noun: o-grade, suffix-accent (agent) | o-grade | suffix |
| ThemNounZR | Thematic noun: zero-grade, root-accent | zero | root |
| ThemNounZS | Thematic noun: zero-grade, suffix-accent (object/instrument) | zero | suffix |
| ActNounTi | Action noun / abstract (-ti-) | zero | suffix |
| ActNounTu | Verbal noun (-tu-) | zero | suffix |
| MenNounR | Neuter result/instrument noun (-mn̥, root-accent) | e-grade | root |
| MonNounPrim | Primary deverbal noun/adjective (-món-, suffix-accent) | zero | suffix |
| MenNounAnim | Animate internal derivative (-mōn-, mobile) | e-grade | mobile |
| AgentNounE | Event-agent noun (-tōr, nom.; -tor-, obl.) | e-grade | mobile |
| AgentNounR | Role/status agent noun (-tēr) | zero | suffix |
| SStem | S-stem abstract/result noun (oblique stem) | e-grade | root |
| UStemM | U-stem noun, mobile non-Caland | zero | mobile |
| IStem | I-stem noun/adjective | e-grade* | variable |
| FemEventNoun | Feminine event/result noun (-éh₂) | o-grade | suffix |
| InstrNounTro | Neuter instrument noun (-tro-) | e-grade* | variable |
| InstrNounTlo | Neuter instrument noun (-tlo-) | e-grade* | variable |
| LoNoun | Noun of place/object/result (-lo-) | e-grade* | variable |
| MoNoun | Action/event noun or adjective (-mo-) | e-grade* | variable |
| NoNoun | Noun (-no-) | e-grade* | variable |

\* Grade is root-specific and not derivable from input alone; the tool defaults to
e-grade and notes this on each row.

---

## Zero-grade resolution

The zero grade is computed by deleting the root vowel `e` and resolving the
resulting cluster using right-priority sonority:

1. If the segment **after** the deleted `e` is a glide, vocalize it (w→u, j→i).
   If it is a liquid or nasal, syllabify it (r→r̥, l→l̥, m→m̥, n→n̥).
2. If the segment **before** the deleted `e` is a liquid or nasal (onset-cluster
   case, e.g. *ǵneh₃-), syllabify it.
3. If neither neighbour is a resonant or glide, the result is a bare consonant
   cluster (e.g. *sed- → *sd-). This is valid; it is not flagged.

The `--zero` flag overrides this computation entirely for irregular or
schwabe-ablaut roots.

---

## Reduplication

The reduplicated present uses C₁i- prefixation; the perfect uses C₁e-.
Both are auto-derived when the root onset is a single atomic consonant.
Auto-derivation is skipped (with a note) when the onset is a laryngeal, an
s+C cluster, or a complex cluster. Use `--reduplication` to supply the base
manually in those cases.

---

## Nasal infix

The nasal-infix present inserts *né* before the single final coda consonant of
the zero grade (strong stem). Auto-derivation is skipped when the zero grade
has no coda consonant, or when the coda is a cluster. Use `--nasal-infix` to
supply the base manually.

---

## Markdown export

`--export` writes a table to `lexicon/derivata/{root}-derivata.md` relative to
the current working directory (i.e. run from `tools/`, output lands under
`tools/lexicon/derivata/`). The filename is a sanitized ASCII rendering of the
root's e-grade. The table has the same rows as the screen output but includes
accent type and skipped-pattern reasons as additional columns.

---

## Known limitations

- Grades marked `*` (root-specific) default to e-grade regardless of the actual
  historical pattern for the root.
- `variable` patterns always emit both accent variants; filtering for the
  historically attested one is left to the user.
- Reduplication and nasal-infix predictability checks are conservative: ambiguous
  onsets are skipped rather than guessed.
- Secondary derivations are not yet implemented.
- No batch input; one root per invocation.
- No NocoDB write-back; output is screen/markdown only.
