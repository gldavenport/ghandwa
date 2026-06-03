---
title: "Proto-Seldanic Sound-Change Rule Set"
type: "constructed Western Indo-European daughter-language rule set"
status: "provisional working draft"
created: "2026-05-17"
updated: "2026-05-17"
notes: "Constructive historical-phonology design, not a claim about a real unattested branch."
---

# Proto-Seldanic Sound-Change Rule Set

Proto-Seldanic is a constructed Western Indo-European daughter defined by a hard centum profile, devoiced but still aspirated reflexes of PIE voiced aspirates, uniform *a*-repair of interconsonantal laryngeals, and a simplified syllabic-resonant rule with a narrow labiovelar exception.

## Branch profile

```text
centum
western-adjacent
non-Anatolian
non-satem
non-Grimm
non-Celtic-p-loss
non-Greek three-way interconsonantal laryngeal reflex
not Ghandwa
```

Core identity:

```text
ḱ, ǵ, ǵʰ > k, g, gʰ

Dʰ > Tʰ
that is:
bʰ, dʰ, gʰ, gʷʰ > pʰ, tʰ, kʰ, kʷʰ

CHC > CaC

R̥ > aR generally
KʷR̥ > KʷuR > KuR
```

## Notation

```text
H  = h₁, h₂, h₃
R  = r, l, m, n
P  = labial: p, b, pʰ, bʰ, m, w
K  = velar: k, g, kʰ, gʰ
Kʷ = labiovelar: kʷ, gʷ, kʷʰ, gʷʰ (covers all labiovelars regardless of aspiration)
Dʰ = voiced aspirate
Tʰ = voiceless aspirate
T  = dental: t, d, tʰ, dʰ
```

## Ordered sound changes

### 1. Adjacent laryngeal coloring

```text
h₁e, eh₁ > e, ē
h₂e, eh₂ > a, ā
h₃e, eh₃ > o, ō
```

Examples:

```text
*h₂éǵros > *agros
*steh₂-  > *stā-
*deh₃-   > *dō-
```

### 2. Postvocalic laryngeal lengthening

```text
VH > V̄
```

Examples:

```text
*méh₂tēr > *mātēr
*steh₂-  > *stā-
```

### 3. Dental clusters

Ordered before CHC repair so that cluster simplification sees the pre-vocalization consonantal environment.

```text
TT > ss
ssC > sC
```

Examples:

```text
*tt > *ss
*dt > *tt > *ss
*ssC > *sC
```

### 4. Interconsonantal laryngeals

Laryngeals in *CHC* position vocalize to *a* uniformly. Placed before centum merger and aspirate devoicing; operates on the post-cluster environment from §3.

```text
CHC > CaC
```

Consequence for *KʷHC* sequences: the labiovelar precedes a vowel after this rule applies (*KʷaC*) and is not caught by the delabialization rule (§8), which operates only before consonants and near *u/w/ū*. *KʷaC* survives intact.

Examples:

```text
*ph₂tḗr  > *patēr
*sth₂tó- > *statό-
*dʰh₁tó- > *dʰató-   (aspirate still present; rule §6 applies later)
```

### 5. Centum merger

Centum merger precedes voiced-aspirate devoicing so that *ǵʰ* first merges with *gʰ*, then both undergo devoicing.

```text
ḱ, ǵ, ǵʰ > k, g, gʰ
```

### 6. Voiced aspirates devoice, retaining aspiration

```text
bʰ  > pʰ
dʰ  > tʰ
gʰ  > kʰ
gʷʰ > kʷʰ
```

Because this rule follows centum merger:

```text
ǵʰ > gʰ > kʰ
```

The reordered dorsal system:

```text
PIE *ḱ, *k       > k
PIE *ǵ, *g       > g
PIE *ǵʰ, *gʰ     > kʰ
PIE *gʷʰ         > kʷʰ
```

Examples:

```text
*bʰréh₂tēr > *pʰrātēr
*medʰyos   > *metʰyos
*dʰató-    > *tʰató-   (CHC repair from §4 already applied)
```

### 7. Syllabic resonants

The labiovelar exception runs first; its output feeds rule §8. *Kʷ* as a class label covers all labiovelars regardless of aspiration, so *kʷʰ* (< *gʷʰ* via §5–6) participates in *KʷR̥ > KʷuR*.

```text
KʷR̥ > KʷuR    (runs first)
R̥   > aR      (remaining syllabic resonants)
```

Examples:

```text
*kʷr̥mi-  > *kʷurmi-
*gʷr̥-    > *gʷur-
*deḱm̥   > *dekam
*ḱm̥tóm  > *kamtóm
*septḿ̥  > *septam
```

### 8. Labiovelars

Labiovelars delabialize before consonants and near *u/w/ū*. The *KʷuR* sequences created by §7 are caught by the *_{u}* environment. Applies to all labiovelars (*kʷ*, *gʷ*, *kʷʰ*).

```text
Kʷ > K / _C
Kʷ > K / _{u, ū, w}
Kʷ > K / {u, ū, w}_
```

Examples:

```text
*kʷékʷlos  > *kʷeklos    (second Kʷ before C)
*kʷurmi-   > *kurmi-     (Kʷ before u, from §7)
*gʷur-     > *gur-
*penkʷe    > *penkʷe     (Kʷ before e: no change)
*kʷod      > *kʷod       (Kʷ before o: no change)
```

## Structural notes (not transformations)

```text
Plain voiceless stops remain voiceless stops. No Grimm's Law.
Plain voiced stops remain voiced stops.
No Celtic-style *p-loss.
No general s > z rule.
No final-syllable erosion.
Final *-m, *-s, and *-t retained.
```

## Diagnostic sample forms

| PIE | Proto-Seldanic | Notes |
|---|---:|---|
| *ph₂tḗr* | *patēr* | uniform *CHC > CaC* |
| *méh₂tēr* | *mātēr* | postvocalic *h₂* lengthening |
| *bʰréh₂tēr* | *pʰrātēr* | *bʰ > pʰ*, *eh₂ > ā* |
| *dʰh₁tó-* | *tʰató-* | *CHC > CaC* (§4), then *dʰ > tʰ* (§6) |
| *sth₂tó-* | *statό-* | uniform *CHC > CaC* |
| *h₂éǵros* | *agros* | centum *ǵ > g* |
| *kʷékʷlos* | *kʷeklos* | second *kʷ* before C |
| *penkʷe* | *penkʷe* | *kʷ* retained before *e* |
| *kʷod* | *kʷod* | *kʷ* retained before *o* |
| *septḿ̥* | *septam* | general *R̥ > aR* |
| *deḱm̥* | *dekam* | centum plus general *R̥ > aR* |
| *ḱm̥tóm* | *kamtóm* | centum plus general *R̥ > aR* |
| *kʷr̥mi-* | *kurmi-* | *KʷR̥ > KʷuR* (§7), then *Kʷ > K* before *u* (§8) |
| *medʰyos* | *metʰyos* | *dʰ > tʰ* |

## Open questions

```text
1. Whether CHC repair should interact with any cluster simplifications beyond TT > ss.
   Current stance: no additional cluster rules specified; revisit if needed.
```

## Resolved

```text
1. CHC > CaC uniformly (no high-vowel conditioning). Old CuC/CiC rule removed.
2. KʷR̥ > KʷuR applies to kʷʰ (< gʷʰ) as well as inherited kʷ. Kʷ class covers
   all labiovelars regardless of aspiration.
3. kʷʰ delabializes near u/w/ū exactly like plain kʷ (same class, same rule).
4. CHC placed at rule 4, after dental cluster simplification (§3), so clusters
   are resolved before CHC vocalization. Same ordering as Ghandwa.
5. KʷaC sequences survive delabialization (Kʷ precedes vowel after CHC repair;
   rule §8 only fires before C and near u/w/ū).
```

## Relationship to Ghandwa

| Feature | Ghandwa | Proto-Seldanic |
|---|---|---|
| Overall profile | shallow WIE-like intermediate | distinct western daughter |
| Voiced aspirates | voiced fricatives broadly | voiceless aspirates: *Dʰ > Tʰ* |
| Interconsonantal laryngeals | western-like *a*-repair | same: uniform *CaC* |
| Dental clusters | *TT > ss* | same: *TT > ss*, *ssC > sC* |
| Syllabic resonants | generally *R̥ > aR* | same generally; *KʷR̥ > KuR* exception |
| Labiovelars | preserved with filters | preserved; *KʷR̥* creates diagnostic *KuR* |
| Plain stops | mostly retained | retained |

## Changelog

- 2026-05-17 | 8 rules | Added TT > ss / ssC > sC (§3), ordered before CHC repair per Ghandwa pattern. Resolves CHC/cluster interaction open question. All prior open questions now resolved. One residual open question retained (further cluster rules TBD).
- 2026-05-17 | 7 rules | Resolved: kʷʰ delabializes near u/w/ū same as kʷ; Kʷ class covers all labiovelars. Resolved: KʷR̥ > KʷuR applies to kʷʰ. Open questions reduced to 2.
- 2026-05-17 | 7 rules | Initial file. CHC > CaC (uniform). KʷR̥ > KʷuR feeds delabialization. CHC at rule 3 (laryngeal-era). Removed non-transformation "Kʷ > Kʷ elsewhere." KʷaC survives delabialization. Old CHC > CuC/CiC removed.
