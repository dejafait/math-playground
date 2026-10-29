# First excluded retained-overlap boundary — completed source comparison

TARGET: Test whether L128's bound |A_L|+|A_R|<=2552584+2s still holds at s=18632 under its other unchanged hypotheses, without assuming equality of the ambient stars.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused primary-source comparisons in 2026-10-25-near-complete-common-star-rigidity.md, 2026-10-25-two-core-full-star-thinning.md and 2026-10-25-near-complete-star-retention.md; searched isomorphic orthogonal-array intersections, linear-array minimum trades and Latin-square near-automorphisms; narrowly compared L030, L126, L127, L128, ATTEMPTS/105 and relevant working/audit records. No inspected theorem covers the changed boundary.
SOURCE_EVIDENCE: Rechecked Ben-Or–Coppersmith–Luby–Rubinfeld, author preprint https://people.csail.mit.edu/ronitt/papers/convd.pdf, Theorem 1, PDF p. 3, including independent-uniform convention; reused inspected trade, exact-automorphism and matching statements at the precise locations below. New Tonchev and near-automorphism leads supply no inspected boundary theorem.
COMPARISON: L127 requires ambient overlap >=18633 and uses strictly fewer than q missing rows for label/column recovery and complete base lines; L128 transfers retained overlap to that hypothesis, while L126's nonstar correspondence requires ambient equality. The proposed retained threshold is outside this chain. Known stability, trade and matching results supply tools or mismatched conclusions, not this size bound or its negation.
GAP: Justify sufficient boundary recovery/completion or a replacement conflict correspondence under the unchanged arbitrary-label and retained-indicator hypotheses; alternatively exhibit compatible retained families violating the actual size sum. Failure of ambient equality alone does not decide TARGET.
REASON: Changed essential overlap hypotheses have received a bounded source comparison. No direct import or known specialization resolves them; one symbolic proof/obstruction attempt is justified without claiming novelty, equality, a matching or the bound as established.
SCOPE: Exactly TARGET with q=137, unchanged T, H,K,a,b and arbitrary ambient bijections of L128, left distinguished column 16, equal retained common-support indicators and distinct-support intersection <=63; one bounded symbolic attempt through recovery/completion or a direct conflict correspondence. No imposed ambient equality, lower overlap, different left column, unequal indicators, arbitrary laws, global extension or RS realization.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changes an essential overlap threshold beyond the saved ready assessments; this separate comparison reuses their adequate primary-source coverage.

## Exact scope and local comparison

Use L128's H of size 1024, K of size 60, distinct a,b outside K,
cores C=K union {a}, C'=K union {b}, q=137 and
T={16,64,70,102,112,118,121}. The ambient families are L030's
quadratic polynomial families, including zero, under arbitrary
bijections from (T times F_q) disjoint union four dummy labels onto
the respective core complements. The left preimage of b is (16,y_0).
The right distinguished column remains unspecified initially.
Retained families satisfy W={S in A_L:b in S}={S in A_R:a in S},
now with s=18632. Distinct retained supports in their union intersect
in at most 63 points; equal supports are identified and permitted.
No ambient equality is added. The bound in TARGET is the test, rather
than ambient equality or success of any particular matching.

The main gap remains arbitrary-center 67/68 safety and bracket 955–957.
This intermediate bound could extend a restricted two-core obstruction
for later compatibility work. Other overlaps, unequal indicators,
arbitrary laws, global extension and RS realization remain independent.

L030 supplies actual local families, not an RS list. L126's structural
paragraphs and equations (1)–(3) use ambient equality before the nonstar
matching. L127 proof sections 1 and 3 use m<q for recovery of used
points, untouched-point column recovery, and complete base lines. Its
statement claims no optimal threshold. L128's first proof step invokes
exactly L127's ambient-overlap hypothesis; the subsequent count uses
retained stars. Its separate audit is accepted. These proof comparisons
do not establish failure or success of recovery at the new boundary.
Ambient overlap is not assumed equal to retained overlap.

ATTEMPTS/105 remains the full-star-preserving thinning stop, not a ban
on altered overlap. The preserved near-complete-star notes concern the
previous threshold only. History/499 and the L128 audit assessment do
not settle this boundary. Targeted local reads found no duplicate
boundary result. No cross-notebook input is used.

## Primary theorem comparison

Michael Ben-Or, Don Coppersmith, Mike Luby and Ronitt Rubinfeld,
*Non-Abelian Homomorphism Testing, and Distributions Close to their
Self-Convolutions*, Random Structures & Algorithms 32(1) (2008),
49–70, DOI [10.1002/rsa.20182](https://doi.org/10.1002/rsa.20182),
Theorem 1, p. 3 of the [18-page author preprint](https://people.csail.mit.edu/ronitt/papers/convd.pdf).
For finite groups and a map f, failure probability delta<2/9 on
independent uniform ordered pairs gives distance at most
(3-sqrt(9-24 delta))/12 from a homomorphism. The statement and
uniform convention were rechecked this turn; the majority-map proof
and essential cases, pp. 3–6, were already inspected in the saved
rigidity assessment. Import this theorem if applicable; do not reprove
it. It assumes one map on a full group, not three symbol permutations
on a partial incidence relation. Recovery and the reduction/error count
at the boundary remain obligations. Retain L127's direct qualification
of the zero-error endpoint.

The following are reused primary inspections from the
[rigidity assessment](2026-10-25-near-complete-common-star-rigidity.md),
not newly read full proofs:

- Cavenagh–Donovan–Demirkale, *Orthogonal trades in complete sets of
  MOLS*, EJC 24(3) (2017), P3.15, [author PDF](https://researchcommons.waikato.ac.nz/bitstreams/b5546026-8db3-4698-914b-a7ee1a224d52/download),
  definitions pp. 2–3, Theorems 10–11 and proof pp. 4–5,
  Theorems 16–17 p. 7. Their trade bounds and constructions preserve
  a specified orthogonal mate, not every coordinate of this fixed
  six-column star under arbitrary labels.
- Demirkale–Donovan–Küçükçifçi–Yazıcı, *Orthogonal Trades and the
  Intersection Problem for Orthogonal Arrays*, Graphs Combin. 32
  (2016), 903–912, DOI 10.1007/s00373-015-1638-y,
  [author manuscript, 17 July 2015](https://www.researchgate.net/publication/283275620_Orthogonal_Trades_and_the_Intersection_Problem_for_Orthogonal_Arrays),
  definitions pp. 2–4, Corollary 2.2 with proof p. 5, Lemma 2.6
  pp. 7–8. Four-column trades with varying foundations do not supply
  a fixed six-column polynomial-star counterexample or ambient
  isomorphism. Retain the prior exclusion of Theorem 4.5 from use
  because of the recorded apparent inconsistency in extracted exclusions.
- Camps-Moreno–Lau–López–Santos, *The permutation group of Reed-Solomon
  codes over arbitrary points*, [arXiv:2601.00122v1](https://arxiv.org/html/2601.00122v1),
  Theorem IV.6 with proof and Remark IV.10. Full-code coordinate
  permutations do not recover columns or arbitrary symbol maps from
  partial common supports.

The [full-star assessment](2026-10-25-two-core-full-star-thinning.md)
already inspected König, *Graphs and matrices*, authorized translation
of *Graphok és matrixok* (1931), [arXiv:2009.03780v1](https://arxiv.org/pdf/2009.03780v1),
unnumbered main theorem p. 3 and graph proof pp. 1–2. Finite bipartite
matching/cover equality requires no symmetry, but constructs no
forbidden pairs here; explicit disjoint-edge counting needs no reproof
of it. Wang–Zhang, [arXiv:1101.2257v1](https://arxiv.org/pdf/1101.2257v1),
Theorem 1.1 p. 5, requires part-transitivity and primitive fragments,
unverified for arbitrary labels. Borg–Feghali,
[arXiv:2012.15356v2](https://arxiv.org/pdf/2012.15356v2), Theorem 1
p. 3, assumes lower cross-intersection, unlike the present upper
restriction. None supplies a boundary matching or the numerical bound.

## Bounded search and unused leads

New queries on 26 October 2026 included orthogonal-array isomorphic
intersections, linear-array defining sets, minimum trades over prime
fields, and exact-title searches for Near-automorphisms of Latin
squares. Exact queries included `"orthogonal arrays" "intersection"
"isomorphic" trades`, `"orthogonal array" "defining sets" "linear"
trades prime`, `linear orthogonal array minimum trade volume prime
affine plane defining sets`, and `"orthogonal array" "trade" "prime"
"minimum"`. Results largely repeated saved trade references. This
bounded search proves neither novelty nor comprehensive coverage.

Cavenagh–Stones, *Near-automorphisms of Latin squares*, J. Combin.
Designs 19(5) (2011), 365–377, DOI 10.1002/jcd.20282, remains an
optional unread full-theorem lead. The [institutional record](https://researchcommons.waikato.ac.nz/items/848c5c4b-6cab-463a-b467-fea9f8ce8f0f)
was retrieved; its abstract supplies no theorem import.
Tonchev, *Affine designs and linear orthogonal arrays*, Discrete Math.
294 (2005), 219–222, DOI 10.1016/j.disc.2004.04.048, surfaced a cached
publisher passage containing Theorem 1. Direct publisher retrieval
returned 403 and DOI retrieval failed. No proof was inspected or
result imported. Neither lead is essential to the bounded test below;
these access limits do not make the target SOURCE_BLOCKED. No further
retries of these endpoints are proposed.

## One bounded continuation and stopping test

Keep exactly TARGET. Test symbolic recovery from the common residual
six-subset family at the boundary: account for possible disappearing
labels, absence of untouched points and absence of complete base lines.
These are proof obligations, not newly asserted obstructions or a
classification. Do not impose column correspondence or equality of
full used sets. If recovery succeeds, seek completion of the partial
affine equations, with a justified single-map reduction and its
independent-uniform error count before invoking the stability theorem.
Use L125 rigidity through L126 only after supplying exact hypotheses.

Alternatively, a direct conflict correspondence must work for every
allowed ambient labeling and yield the exact size sum with both
retained-star contributions. Failure of equality or of a proposed
matching is only a route limitation. Refuting TARGET requires actual
retained families, equal indicators, every distinct-support intersection
check and a sum exceeding the target. A general trade or relaxation
is insufficient, and no such counterexample would by itself be an RS list.

Continue on a rigorous bound, an exact counterexample, or useful recovery
with an explicit remaining test. If this single attempt requires stronger
overlap, imposed labels or unbounded enumeration, save the precise
failure and reassess rather than silently changing TARGET. An incomplete
attempt need not settle the inequality. Subtargets outside this scope
need review; complete-looking results need later independent audit.

Outcome: EXPLORATION, an actionable bounded source comparison, not a
mathematical advance beyond the inspected literature. No boundary lemma,
calculation, proof, counterexample or mathematical script was produced.
Mathlib coverage for full and supporting results is not checked.
PROOF.md and DAG.md are unchanged because the argument did not change.
This newly ready continuation receives separate supervisor approval;
no boundary mathematics was performed in this source-only turn.
