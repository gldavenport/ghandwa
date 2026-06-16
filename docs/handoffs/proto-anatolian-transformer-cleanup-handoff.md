# Proto-Anatolian Transformer Cleanup Handoff

Scope: `proto_anatolian.py` currently mixes (1) PIE → Proto-Anatolian sound changes, (2) post-Proto-Anatolian daughter/profile rules, and (3) phonological interpretations of the Proto-Anatolian stage.

This handoff lists only:

1. Rules missing from the base Proto-Anatolian transformer.
2. Rules currently in the base transformer that should come out of the mandatory base stage.
3. Rules that are phonological interpretation layered on top of Proto-Anatolian, not base sound changes.

---

## 1. Rules to add for a fuller PIE → Proto-Anatolian base

These are missing or underrepresented in the current base transformer.

### 1.1 Dorsal-series treatment

Current issue: `ḱ` appears only in the optional prosodic voicing target list. There is no general treatment of PIE palatovelars/plain velars/labiovelars.

Add an explicit Proto-Anatolian dorsal layer:

```text
ḱ  → k   or retained as Ḱ in abstract mode until source decision
ǵ  → g   or retained as Ǵ in abstract mode until source decision
ǵʰ → g   after Dʰ → D merger
kʷ, gʷ → explicitly preserved or resolved according to the chosen Proto-Anatolian analysis
```

Needed because the current code does not define what happens to PIE palatovelars or labiovelars except for `kʷR̥ → kuR`.

---

### 1.2 General labiovelar handling

Current issue: only `kʷR̥ → kuR` is implemented.

Add a general rule or explicit preservation layer for:

```text
kʷ
gʷ
gʷʰ → gʷ after deaspiration
```

The base transformer needs to decide whether these are preserved as labiovelars at the Proto-Anatolian stage or converted to daughter/profile outputs later.

---

### 1.3 Diphthong outcomes

Current issue: no systematic handling of PIE diphthongs.

Add a checked Proto-Anatolian/daughter-stratified layer for:

```text
ey / ei
oy / oi
ow / ou
ew / eu
ay / ai
aw / au
```

The likely missing candidates include Anatolian-style monophthongizations such as:

```text
*ey / *ei → ē-type outcome
*ew / *eu → ū-type outcome
```

but the exact layer must be separated into Proto-Anatolian base vs daughter/profile outcome.

---

### 1.4 PIE *o and *a treatment

Current issue: the code handles `h₃` coloring to `o`, but does not define the general Proto-Anatolian treatment of PIE `*o` and `*a`.

Add explicit handling for:

```text
*o
*a
*h₃-colored *o
*h₂-colored *a
```

The transformer needs a base-stage decision about whether `*o` is preserved distinctly, merges with `a`, or remains abstract until daughter/profile resolution.

---

### 1.5 Full syllabic-resonant layer

Current issue: the code mostly preserves syllabic resonants but applies two specific repairs:

```text
wR̥ → uR
kʷR̥ → kuR
```

Add a complete layer for:

```text
r̥
l̥
m̥
n̥
```

The base transformer should either:

```text
preserve R̥ in abstract/research mode
```

or provide a source-backed Proto-Anatolian vocalization layer.

Do not leave only the partial `wR̥` and `kʷR̥` repairs as the only syllabic-resonant treatment.

---

### 1.6 Final-position behavior

Current issue: no systematic treatment of final vowels, final stops, final resonants, or final laryngeals beyond `h₁` loss.

Add checked rules for:

```text
word-final vowels
word-final stops
word-final resonants
word-final laryngeals
word-final *-m, *-n, *-r, *-s
```

These may be Proto-Anatolian or daughter-specific depending on source; the current base transformer does not classify them.

---

### 1.7 Initial *y / *w behavior

Current issue: no general treatment of initial glides.

Add checked handling for:

```text
#y-
#w-
y before front vowels
w before rounded/back vowels
```

This may belong to daughter/profile modules if not Proto-Anatolian.

---

### 1.8 Long-vowel normalization

Current issue: the code creates `ǣ` from `eh₁`, and uses `lengthen()` for other `Vh₁`, but there is no complete Proto-Anatolian long-vowel layer.

Add explicit treatment for:

```text
ē
ā
ō
ī
ū
ǣ
```

including whether `ǣ` is a research notation, a Proto-Anatolian phoneme, or a daughter-profile input symbol.

---

### 1.9 General laryngeal-loss/residue layer beyond h₁

Current issue: `h₂` and `h₃` are converted to `χ` and `χʷ` and then kept. `h₁` is deleted. There is no abstract base option.

Add an abstract base laryngeal layer:

```text
h₂ → H₂
h₃ → H₃
h₁ → H₁ / ∅ depending on stage
```

Then let profiles decide:

```text
H₂ → χ / x / ḫ / h / ∅
H₃ → χʷ / xʷ / ḫw / hʷ / H / ∅
```

---

## 2. Rules that should come out of the mandatory Proto-Anatolian base

These rules may still be useful, but they should not be mandatory PIE → Proto-Anatolian base rules.

### 2.1 Fixed `h₂ → χ`, `h₃ → χʷ` as surface output

Current rule:

```text
h₂ → χ
h₃ → χʷ
```

Classification:

```text
phonological interpretation / conlang profile
```

Base should allow abstract:

```text
h₂ → H₂
h₃ → H₃
```

The `χ/χʷ` realization belongs to an interpreted Proto-Anatolian, Hittite-like, or adstrate profile.

---

### 2.2 Initial `h₁ → ʔ`

Current rule/toggle:

```text
h₁ → ʔ / #_V
```

Classification:

```text
phonological interpretation / Kloekhorst-like profile / adstrate profile
```

Remove from mandatory base default.

---

### 2.3 h₁ cluster assimilation

Current toggle:

```text
VRh₁V → VRRV
sh₁ → ss
Th₁ → TT
```

Classification:

```text
interpretive/profile-specific unless independently source-backed
```

Remove from mandatory base.

---

### 2.4 Broad `Tχ/Tχʷ → TT`

Current rule:

```text
Tχ, Tχʷ → TT
```

Classification:

```text
post-base / daughter-profile / Anatolianizing profile
```

The broad version should come out of mandatory base.

A narrower source-backed cluster rule may be added separately if supported.

---

### 2.5 e-lowering

Current rule:

```text
e → a / _Rχ, _Rχʷ, _{r,n}{T,#}
```

Classification:

```text
daughter/profile-specific or Anatolianizing interpretation
```

Remove from mandatory base unless exact environments are source-backed as Common Proto-Anatolian.

---

### 2.6 Partial syllabic-resonant repairs as universal base

Current rule:

```text
wR̥ → uR
kʷR̥ → kuR
other R̥ retained
```

Classification:

```text
mixed intermediate/profile behavior
```

Remove as a universal base rule. Replace with either abstract preservation of all `R̥` or a complete source-backed syllabic-resonant layer.

---

### 2.7 Prosodic stop voicing

Current optional rule:

```text
T → D / prosodically weak position
```

Classification:

```text
phonological interpretation / Common Anatolian phonetic profile / daughter-sensitive rule
```

Keep out of mandatory base. It may be available in interpreted or daughter/profile modes.

---

### 2.8 Surface claim: `χ/χʷ survive into Proto-Anatolian`

Current note:

```text
χ/χʷ survive into Proto-Anatolian; only h₁ is deleted.
```

Classification:

```text
phonological interpretation, not neutral research base
```

Remove as a mandatory base assumption. Replace with abstract `H₂/H₃` in research mode.

---

## 3. Current rules that are phonological interpretation rather than base sound change

These are not necessarily wrong, but they are not plain PIE → Proto-Anatolian sound changes.

### 3.1 `H₂ = χ`

Current realization:

```text
h₂ → χ
```

Interpretation:

```text
Proto-Anatolian H₂ was a uvular/velar fricative-like segment.
```

Layer:

```text
phonological interpretation
```

---

### 3.2 `H₃ = χʷ`

Current realization:

```text
h₃ → χʷ
```

Interpretation:

```text
Proto-Anatolian H₃ remained distinct from H₂ and was labialized.
```

Layer:

```text
phonological interpretation
```

---

### 3.3 `h₁ = ʔ` initially

Current realization:

```text
h₁ → ʔ / #_V
```

Interpretation:

```text
Initial h₁ had a glottal-stop-like surface reflex.
```

Layer:

```text
phonological interpretation
```

---

### 3.4 Prosodic voicing as surface phonetics

Current optional rule:

```text
T → D / prosodically weak position
```

Interpretation:

```text
Common Anatolian voiceless stops had strong/weak allophones or underwent prosodically conditioned lenition/voicing.
```

Layer:

```text
phonological interpretation or daughter-sensitive phonology
```

---

### 3.5 Voiced-stop allophony after Dʰ merger

Not currently implemented as such, but relevant to later profiles:

```text
Dʰ → D  = base sound change
D → [D] in strong positions, [Ð] in weak positions = phonological interpretation
```

Layer:

```text
phonological interpretation / donor profile
```

---

### 3.6 Syllabic-resonant pronunciation

Current mixed treatment:

```text
R̥ retained
wR̥ → uR
kʷR̥ → kuR
```

Interpretive options:

```text
R̥ pronounced as syllabic resonant
R̥ → aR
R̥ → ar/al/am/an by resonant
R̥ → daughter-specific mixed outcomes
```

Layer:

```text
phonological interpretation / daughter resolution
```

---

### 3.7 `ts` realization

Current base output:

```text
ty → ts
```

Interpretive/profile outputs may include:

```text
ts
z
s
t+s
```

Layer:

```text
base affrication plus later phonological interpretation/daughter resolution
```

---

### 3.8 `ǣ` as a distinct output

Current rule:

```text
eh₁ → ǣ
```

Interpretation:

```text
The result of eh₁ is represented as a distinct PA vowel-quality symbol rather than simply ē/ā.
```

Layer:

```text
base sound change plus phonological/notation interpretation
```

---

## 4. Minimal corrected classification of the existing rules

### Keep as base Proto-Anatolian

```text
Dʰ → D
ty → ts
laryngeal coloring, but with abstract H₂/H₃ option
VRHV → VRRV, if source-backed
sH → ss, if source-backed
h₁ loss and compensatory lengthening, with notation separated from surface phonetics
accent preserved as metadata
```

### Add to base or stage explicitly

```text
dorsal-series treatment
labiovelar treatment
diphthong outcomes
*o/*a treatment
full syllabic-resonant layer
final-position behavior
initial glide behavior
long-vowel normalization
general abstract H₂/H₃ handling
```

### Remove from mandatory base

```text
fixed h₂ → χ, h₃ → χʷ as surface output
initial h₁ → ʔ
h₁ cluster assimilation
broad Tχ/Tχʷ → TT
e-lowering rule
partial wR̥/kʷR̥ repairs as universal
prosodic stop voicing
mandatory claim that χ/χʷ survive as surface Proto-Anatolian
```

### Treat as phonological interpretation

```text
H₂ = χ
H₃ = χʷ
h₁ = ʔ initially
D has strong [D] and weak [Ð] allophones
T voices/lenites in prosodically weak position
R̥ pronunciation/resolution
surface realization of ts
surface value of ǣ
```
