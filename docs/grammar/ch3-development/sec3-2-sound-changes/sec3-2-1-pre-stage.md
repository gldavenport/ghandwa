---
title: "§3.2.1 Pre-Stage: Centum Merger and Labiovelar Normalization"
last_updated: 2026-05-30T00:00-04:00
chapter: ch3-development
section: sec3-2-sound-changes
supersedes: "docs/grammar/ch3-development/phonological-history.md (§3)"
---

# §3.2.1 Pre-Stage: Centum Merger and Labiovelar Normalization

These changes are shared by all centum IE languages and are presupposed by every subsequent rule. They are not Ghandwa innovations but features of the centum node from which Ghandwa descends.

## §3.2.1.1 Centumization

> \*ḱ → k, \*ǵ → g, \*ǵʰ → gʰ

The PIE palatal series merges unconditionally with the plain velars. After this rule, no subsequent rule ever sees a palatovelar.

**Examples:**
- \*ḱr̥h₂nóm 'horn (acc.)' → kr̥h₂nom → … → *karnom*
- \*ḱm̥tóm 'hundred' → km̥tom → … → *kantom*
- \*déḱm̥ 'ten' → dekm̥ → … → *dekam*
- \*h₂ŕ̥tḱos 'bear' → h₂r̥tkos → … → *arktos*

## §3.2.1.2 Labiovelar Absorption

> Kw → Kʷ (velar + w sequences merge with inherited labiovelars)

Any sequence of a plain velar immediately followed by \*w is treated as a single labiovelar segment. This collapses the distinction between inherited labiovelars (\*kʷ, \*gʷ, \*gʷʰ) and surface-identical sequences arising from morpheme boundaries or compounding.

This rule is a standing constraint: it reapplies after every stage. See §4.2 (*sec4-2-phonology/sec4-2-phonology.md*) for the synchronic treatment.

## §3.2.1.3 PIE-Internal Delabialization

> Kʷ → K / {u, ū, w} \_ (preceding rounded segment)
> Kʷ → K / \_ {u, ū, w} (following rounded segment)

A PIE-internal surface constraint: labiovelars delabialized when flanked by a rounded segment (u, ū, or w) on either side. The rule is **bidirectional** — it fires for both the preceding and following environment — and runs **once at the pre-stage** before any Ghandwa-specific changes apply. It does not recur.

**Examples:**
- \*gʷr̥h₂ús 'heavy' → gr̥h₂us (kʷ before u; bidirectional rule fires once)

## §3.2.1.4 Ghandwa Boukólos Rule

> Kʷ → K / \_ {C, w, u, ū} (forward-only; C excludes syllabic resonants)

The primary labiovelar simplification rule of Ghandwa. Labiovelars delabialize before any consonant, or before w/u/ū. The rule is **forward-only** (not triggered by preceding rounded segments) and runs as a **standing rule post-Stage 1 and post-Stage 2** — never at the pre-stage. This restriction means it catches derived environments created by laryngeal loss and syllabic resonant vocalization, which the PIE-internal rule (§3.2.1.3) could not have seen.

Syllabic resonants (r̥, l̥, m̥, n̥) do not trigger the rule. After vocalization (§3.2.3.1) they yield CaRC sequences, and by that point the labiovelar environment has already resolved.

**Examples:**
- \*h₃ékʷs 'horse (acc.)' → ókʷs → oks (kʷ before s, standing rule post-Stage 1)
- \*nókʷts 'night' → nókts (kʷ before t, standing rule post-Stage 1)

**Interaction example:** The o-stem noun \*perkʷus ~ \*perkʷéws 'oak' illustrates the standing rule in action. In the nominative, \*kʷ stands before \*u and delabializes: *perkus*. In the genitive, \*kʷ stands before \*e and is preserved: *perkʷews*. The result is a stem alternation kʷ ~ k conditioned by the following vowel — a deliberate unresolved tension that daughter languages may level in either direction.

**Ordering:** Both delabialization rules must follow labiovelar absorption (§3.2.1.2), since absorption creates new labiovelars that feed both simplification rules. §3.2.1.3 fires once at the pre-stage; §3.2.1.4 fires as a standing rule after every subsequent stage. See §3.2.4 for the complete rule ordering and §4.2 for the synchronic treatment of both standing rules.
