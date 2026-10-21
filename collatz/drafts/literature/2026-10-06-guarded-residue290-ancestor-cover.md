# Guarded residue-290 ancestor cover — completed source comparison

TARGET: Assess whether every positive n congruent to 290 modulo 729 with actual W(2,3)=(OOEO)^2 O^3 E^2 and an odd endpoint has a positive ancestor p congruent to 20 modulo 27 with p<n and T^t(p)=n for some integer 1<=t<=12.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six exact-statement, word-guard and finite-ancestor queries found no inspected matching cover or refutation; three follow-up queries sought the primary text of one sieve lead. Reused the saved ancestor/coding assessments and checked the primary hypotheses and cases listed below.
SOURCE_EVIDENCE: Sodelin Bounded_Ancestor_Depth_Obstruction.md, exact statement/proof and anchor-20/periodic cases; Complementary_Ancestor_Cylinders.md, both fixed certificates and variable-coordinate theorem; Residue20_Refined_Ancestor.md, sections 1–5; L4_General_Inverse_Word_Coalescence.md, sections 1–5; Rozier–Terracol arXiv:2502.00948v2 equation (2), parity paragraph before Theorem 2.2 and Lemma 2.3 proof. Detailed provenance and reuse below.
COMPARISON: Known affine inverse-word semantics and finite parity coding cover the proposed exact test. The inspected obstruction and guarded ancestor certificates do not state the requested conjunction; no inspected theorem proves its coverage or its failure. This is a scope comparison, not a novelty claim.
GAP: Determine the exact depth-12 ancestor coverage after intersecting the ternary cylinder with the complete actual forward word and odd endpoint, retaining positivity, all inverse guards, residue 20 and p<n; no nonempty uncovered class or least-root admissibility is assumed.
REASON: Approve a bounded specialization of inspected finite arithmetic for a changed cylinder; reuse general coding by citation and preserve all exhausted mechanisms. No new mathematics or mathematical program was performed in this literature turn.
SCOPE: Exactly the TARGET, with shortcut T, all positive roots and no least-root assumption. A later RESEARCH turn may specialize known coding/inverse formulas, prove an exact finite cylinder partition with size thresholds, or give a fully certified uncovered root. It may not enlarge the horizon or infer an all-root claim from sampling.

## Relevance and decision test

The main gap is universal eventual descent. This intermediate target
asks for a smaller positive residue-20 ancestor within twelve actual
shortcut steps on the displayed guarded cylinder. If proved, L014's
least-root argument could exclude this subclass; L014–L018 supply the
existing least-root context, and L020 supplies the local coding
conventions. Universal entry, other cylinders, the residual height
question and later compensation remain independent gaps.

The arithmetic target deliberately has no least-bad-root hypothesis.
An uncovered root would refute this cover even if that root converges
or fails some additional least-root restriction. A successful cover
must cover every positive guarded root, including any finite small
exceptions. A certified uncovered root or subfamily stops this exact
cover; do not increase the horizon to avoid its failure. If coverage
holds, record only the conditional least-root exclusion and remaining
gaps. If the exact partition remains incomplete, retain it unfinished
rather than claim either outcome.

## Inspected ancestor inputs

[Sodelin, *An unbounded-depth obstruction for residue-20 ancestor covers*](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/Bounded_Ancestor_Depth_Obstruction.md),
node `B-S20-ANCESTOR-DEPTH-OBSTRUCTION-001`, exact statement and proof,
web lines 8–41, gives no smaller positive residue-20 ancestor within L
steps at roots 47+3^(L+3)t. The proof transfers every legal inverse
prefix to 47 and retains endpoint order. Lines 75–114 include the
anchor-20 version and simultaneous binary/ternary guards on its named
q5 cylinder. Lines 115–135 give a positive certificate from a negative
periodic rational shadow, including a specific eleven-step family.
These additional cases were checked, rather than assuming the initial
47 family was the only obstruction. None states the present target.
Its supplied 290-modulo-729 restriction differs from the two displayed
anchor neighborhoods at horizon twelve. This difference does not prove
coverage or remove other possible obstructing anchors.

[Sodelin, *Complementary ancestor cylinders and a second ternary-depth coordinate*](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/Complementary_Ancestor_Cylinders.md),
node `B-SECOND-TERNARY-ANCESTOR-001`, web lines 9–63, gives the fixed
nine- and eleven-step cylinders used by L018 and a variable-depth
certificate guarded by v_3(128r-157)>=17. Its formulas, guard propagation,
negative intercept and selector boundary were inspected. These are
partial certificates, not exhaustive coverage of the new cylinder.

[Sodelin, *Refined tail certificates lower the uniform ancestor cutoff to valuation 13*](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/Residue20_Refined_Ancestor.md),
node `B-RESIDUE20-VALUATION13-ANCESTOR-2026-09-05`, sections 1–5,
gives the uniform v_3(4r+1)>=13 theorem and individually guarded lower
rows. The common prefix, retained table, five refined cases, strict
slope bounds and selected-table failures were checked. Their variable
time and lower-row guards cannot be replaced by the requested uniform
twelve-step conclusion. The source now describes the uniform theorem
as Lean kernel-checked in section 6; that description is not a local
Lean audit or Mathlib coverage, and does not include all sharper rows.
Reuse the previously inspected retained-prefix proof from
[the residual-selector assessment](2026-10-03-residue20-residual-ancestor-selector.md)
and [the complementary assessment](2026-10-04-complementary-valuation-three-ancestors.md).

## Imported machinery and necessary specialization

[Sodelin, *L4 — General inverse-word coalescence semantics*](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/L4_General_Inverse_Word_Coalescence.md),
dated 2026-08-23, sections 1–5, uses the local shortcut map. Its positive
inverses are E(y)=2y and O(y)=(2y-1)/3, the latter allowed only at
integer y=2 modulo 3. Equations (2)–(5) give the exact offset recurrence,
prefix and endpoint formula and reversed forward equality. Section 4
explicitly requires cylinder refinement when the odd-inverse count
exhausts the initial ternary precision. Section 5 retains the intercept
in the strict starting-root comparison, including equal slopes.

Import these statements; no general inverse-word reproof is needed.
The later test must apply them to every word of lengths one through
twelve, refine all unfrozen guards, and retain the endpoint's residue
and exact root-relative inequality. Whole-cylinder admissibility cannot
be asserted beyond section 4's precision condition. Positivity follows
only along legal positive integer inverses; rational endpoint
integrality by itself is insufficient.

[Rozier–Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948v2, 13 February 2025](https://arxiv.org/html/2502.00948v2),
equation (2), the paragraph before Theorem 2.2 and the proof of Lemma 2.3,
record the same shortcut map, affine positive remainder and bijection
between length-j parity vectors and classes modulo 2^j. Lemma 2.3 is
an average-remainder theorem; its proof's coding statement is the
supporting input, not an ancestor-cover theorem. Those passages and
proof were read. Reuse the complete finite coding/CRT construction in
[the two-postspell assessment](2026-10-04-two-postspell-compensation.md)
and L020. The odd endpoint must be imposed as the next input parity,
beyond the parities of W itself.

The new work is the intersection and exact finite coverage test on this
particular cylinder, with each strict affine size threshold handled.
This is reproduction of known machinery; the bounded source search
establishes neither originality nor the result. A computational screen
may propose words or a witness, but a positive result needs an exhaustive
partition and mathematical justification; a negative result needs a
complete inverse-tree certificate at the guarded witness and actual
forward replay. No such computation or specialization ran here.

## Search, duplicates, access and provenance

Queries executed:

- Collatz "290" "729" ancestor
- site:github.com/Sodelin/Collatz-Conjecture-Work "290"
- Collatz bounded smaller ancestor residue 20 parity vector cover
- "Collatz" "290" "729" "ancestor"
- "Collatz" "OOEO" "ancestor"
- Collatz inverse parity words smaller ancestor covering theorem finite depth

No inspected exact-target result emerged. General claimed resolutions,
density results and tree descriptions are not imported. Reuse the Monks
et al. section-6/Theorem-6.4 comparison in
[the first-return assessment](2026-10-03-residue20-first-return-descent.md):
forward sufficiency does not supply a bounded smaller ancestor.

One new search lead was [Jim Woods, *Coverage Bounds for a Contracting Inverse-Word Sieve in Z_3*](https://www.jimwoods.com/news/coverage-bounds-for-a-contracting-inverse-word-sieve-in-z).
Only the author's announcement was accessible. Its linked DOI
10.5281/zenodo.22625412, direct record and API record returned browser
errors. Follow-up queries used the exact title plus pdf, the record
number plus pdf, and Jim Woods inverse sieve. The exact sieve guards,
primary theorem and proof remain unread: no bound or cylinder conclusion
from this lead is used. Its unverified aggregate coverage claim does not
supply the exact target or a necessary arithmetic input to the approved
self-contained finite test. This is a parked optional lead, not a claim
of absence or a blocker of the imported inverse semantics.

Read only this notebook's relevant assessments, L020's coding ranges,
L018's citation ranges, Attempts 011/014 and step 052 for duplicates and
stops. No prior exact test on this guarded cylinder was found there.
Attempt 014/L025's coalescence obstruction is a comparison, not a cover
input. The failed carry mechanism in Attempt 017 remains stopped;
this target tests a different ternary cylinder and finite ancestor
relation. No sibling notebook was read.

Primary repository notes were read from live main on 2026-10-06; their
node IDs and sections specify the inspected statements. No immutable
revision or independent source-program run was obtained. The source
bodies and essential proofs are available. General coding coverage is
reused under unchanged map assumptions. The [MathPrize target](https://mathprize.net/posts/collatz-conjecture/),
page dated 2021-07-07, was rechecked: every positive integer must reach
1 under the ordinary map. Prize conditions do not enter this argument.

This LITERATURE / EXPLORATION step provides new target-specific source
scope and a ready test, not a mathematical result or reset of prior
exploration counts. PROOF.md, DAG.md, lemmas/ and scripts/ are unchanged.

## Mathlib

Exact guarded cover/refutation and supporting inverse-word, parity,
congruence and iteration coverage: **not checked**. No matching theorem
or library absence is asserted. External Lean claims are distinct from
Mathlib coverage and from verification of this new finite target.
