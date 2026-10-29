# Near-complete common-star rigidity — completed source assessment

TARGET: Assess whether two ambient common stars in L126's polynomial model sharing at least 18633 actual supports must be equal, with left distinguished column 16 and arbitrary ambient bijections.
CHECKED: 2026-10-25
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched quadratic-star/RS partial isomorphisms, orthogonal-array intersection spectra and defining sets, linear-array trades, approximate homomorphisms and near-automorphisms; read the primary statements and proof passages below. Scoped local comparison inspected L030, L125's star proof, L126, ATTEMPTS/105 and history/491; no matching near-complete result was established.
SOURCE_EVIDENCE: Ben-Or–Coppersmith–Luby–Rubinfeld, https://people.csail.mit.edu/ronitt/papers/convd.pdf, Theorem 1 p. 3 and proof pp. 3–6; Cavenagh–Donovan–Demirkale, https://researchcommons.waikato.ac.nz/bitstreams/b5546026-8db3-4698-914b-a7ee1a224d52/download, definitions pp. 2–3, Theorems 10–11 and proof pp. 4–5, Theorems 16–17 p. 7; Camps-Moreno–Lau–López–Santos, https://arxiv.org/html/2601.00122v1, Theorem IV.6 and Remark IV.10; Demirkale–Donovan–Küçükçifçi–Yazıcı, author manuscript https://www.researchgate.net/publication/283275620_Orthogonal_Trades_and_the_Intersection_Problem_for_Orthogonal_Arrays, definitions pp. 2–4 and Corollary 2.2 with proof p. 5, Lemma 2.6 pp. 7–8.
COMPARISON: Exact automorphism results do not cover partial overlap or arbitrary ambient labels; finite-group stability supplies a possible conditional tool only after a justified reduction to one-map homomorphism testing. General and linear Latin-trade results do not settle this six-column, isomorphic-polynomial-star question. No inspected theorem proves or refutes the 18633 threshold.
GAP: Prove intrinsic column recovery from the common subfamily and exact completion of its partial affine-evaluation correspondence, or produce a counterexample under the exact arbitrary-label hypotheses. Both are unproved; the complete-star 840-map test applies only after full equality or an exact full-star isomorphism is justified.
REASON: Essential source comparison is now completed for one bounded attempt at the unchanged target. No direct import suffices, and no novelty claim follows from the search; exact-star rigidity may not be assumed stable.
SCOPE: Exactly TARGET with L030/L125/L126's q=137, seven-point T, two 61-cores sharing 60 points, left column 16 and unrestricted ambient bijections; one symbolic proof/counterexample attempt through common-incidence recovery and a partial affine functional equation. No change to overlap, laws, labels or packing assumptions is approved.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED assessment identified missing robustness and partial-isomorphism coverage after the accepted full-star repair was exhausted; this separate review addresses that changed hypothesis.

## Exact scope and relevance

Use H,K,a,b,C,C',Omega,T and the arbitrary bijections of L126. The
ambient stars are all left supports containing b and all right supports
containing a. Compare actual 68-subsets, removing K,a,b only when passing
to the residual six-subsets. The left preimage of b is (16,y_0); the
right distinguished column is unspecified. Each nonempty ambient star
has 18769 members by the existing local proofs. The proposed hypothesis
is at least 18633 common members, equivalently at most 136 missing on
each side. This threshold is a proposed test, not an established bound.
No packing condition on the full ambient union, independence, uniform
law or column-preserving map is assumed.

The main unresolved claim remains arbitrary-center 67/68 agreement
safety, with bracket 955–957. This intermediate rigidity test could
support a later incomplete-star retention obstruction. Such a retention
bound, lower-overlap cases, other laws, global extension and RS
realization remain independent gaps. Even a successful rigidity proof
would not settle the main claim.

## Local reuse, duplicates and failures

L030 supplies the actual quadratic families. L125's audited proof
recovers columns from complete cooccurrence, normalizes to its affine
six-column family A(S), and uses equation (4) for every pair of field
values. Its prime-field argument and complete 840-map check are ready
inputs for their stated exact hypotheses. L126 and ATTEMPTS/105 close
the full-star-preserving thinning repair only. History/491 explicitly
leaves the present changed-overlap question unapproved. Targeted reads
found no robust counterpart in these materials; no sibling notebook
was searched or used. Existing work and its stop evidence are preserved.

## Primary theorem comparison

**Finite-group stability.** Michael Ben-Or, Don Coppersmith, Mike Luby
and Ronitt Rubinfeld, *Non-Abelian Homomorphism Testing, and Distributions
Close to their Self-Convolutions*, Random Structures & Algorithms 32(1)
(2008), 49–70, DOI [10.1002/rsa.20182](https://doi.org/10.1002/rsa.20182).
The inspected version is the undated 18-page
[author preprint](https://people.csail.mit.edu/ronitt/papers/convd.pdf),
Theorem 1, p. 3: for finite groups G,H and any f:G→H, put
δ=Pr[f(x)f(y)≠f(xy)] for independent uniform x,y. If δ<2/9, some
homomorphism differs from f on at most τ|G| arguments, where
τ=(3−sqrt(9−24δ))/12. Read the majority-map construction, Lemmas 1–6,
including identity, inverse and product cases and the three disjoint
error events (pp. 3–6). Import this result if applicable; do not reprove it.
Applicability is conditional: L125 (4) concerns three symbol permutations
on a partial domain, before column recovery. The single-map reduction,
its precise error count and any upgrade from closeness to exact equality
remain to be proved. An overlap fraction is not automatically δ.

**Trades inside the prime-field construction.** Nicholas J. Cavenagh,
Diane M. Donovan and Fatih Demirkale, *Orthogonal trades in complete sets
of MOLS*, Electronic Journal of Combinatorics 24(3) (2017), P3.15,
[institutional published author PDF](https://researchcommons.waikato.ac.nz/bitstreams/b5546026-8db3-4698-914b-a7ee1a224d52/download).
Read definitions and normalization on pp. 2–3: B_p(k)(i,j)=ki+j,
p an odd prime; an index-(1,k) trade changes B_p(1) while retaining
orthogonality to B_p(k), k≠1. Theorems 10–11, p. 5, give per-symbol
and total-volume logarithmic lower bounds using K=min{k,k^{-1}},
with inverse represented by its least nonnegative residue. Read the
trade-matrix argument and both irreducible/reducible cases, pp. 4–5.
Theorems 16–17, p. 7, also give small Latin trades and trades permuting
O(log p) entire rows. These do not assert a 137-block minimum for our
six-column stars. The altered square need not be isomorphic to the
original, and preserving one orthogonal mate does not verify all our
coordinates. These theorems supply comparisons, not a counterexample
or a completion theorem for TARGET.

**Exact coordinate automorphisms.** Eduardo Camps-Moreno, Jun Bo Lau,
Hiram H. López and Welington Santos, *The permutation group of
Reed-Solomon codes over arbitrary points*,
[arXiv:2601.00122v1](https://arxiv.org/html/2601.00122v1), submitted
31 December 2025. Read §II's permutation-group definition, Theorem IV.6
with proof and Remark IV.10. For distinct evaluation points A and
1<k<n−1, coordinate permutations preserving the entire RS(A,k) are
exactly those induced by degree-one polynomials permuting A. The
normalized six-point dimension-two code has the numerical n,k range,
but the target has neither a given coordinate permutation nor full
code equality. Arbitrary individual symbol permutations, maps between
different puncturings and arbitrary ground-set bijections are additional
issues. The theorem therefore cannot replace either robust recovery
or exact completion, or L125's projective/symbol argument.

**General orthogonal-array intersection caution.** Fatih Demirkale,
Diane M. Donovan, Selda Küçükçifçi and Emine Şule Yazıcı, *Orthogonal
Trades and the Intersection Problem for Orthogonal Arrays*, Graphs and
Combinatorics 32 (2016), 903–912, DOI 10.1007/s00373-015-1638-y.
Inspected the [author-uploaded manuscript](https://www.researchgate.net/publication/283275620_Orthogonal_Trades_and_the_Intersection_Problem_for_Orthogonal_Arrays),
dated 17 July 2015, not just its abstract. Definitions pp. 2–4 fix
strength two, index one and matching pair projections for a bi-trade.
Corollary 2.2 with proof p. 5 excludes volumes 1,2,3,4,5,7 for four
columns; Lemma 2.6 pp. 7–8 constructs all other positive volumes using
patching. Those existence results range over arrays and foundations;
they do not give trades in this fixed six-column linear array, much
less trades whose completion is an isomorphic ambient star. They
exclude treating strength-two incidence alone as a universal rigidity
theorem. Theorem 4.5 was not used: its extracted exclusions appear
inconsistent with Corollary 2.2, so no intersection-spectrum conclusion
is imported.

## Search record and unread leads

Queries on 25 October 2026 included `orthogonal arrays intersection
common rows trade minimum volume strength two index one`, `Reed Solomon
codes large intersection isometry partial isomorphism dimension two
arbitrary symbol permutations`, `orthogonal array defining set n q squared
q-1 trade`, `linear orthogonal arrays trades`, `approximate homomorphisms
7/9 finite groups theorem`, and `near automorphisms orthogonal arrays`.
Exact-title and author follow-ups located the primary texts above.
Final terminology checks used `Pexider finite groups stability almost`,
`Pexider most pairs finite` and `partial isomorphism Reed-Solomon`;
they supplied no additional inspected theorem. The three-function
equation's reduction to the single-map theorem remains a proof obligation.
These bounded searches establish no assertion of originality or exhaustive
coverage of all design theory.

Cavenagh–Stones, *Near-automorphisms of Latin squares*, J. Combin.
Designs 19(5) (2011), 365–377, DOI 10.1002/jcd.20282, is an unread
full-theorem lead. The institutional/publisher abstracts were accessible;
the publisher full-PDF endpoint failed. No theorem or fixed-model
counterexample from it is used. Dür's broader exact code-automorphism
work remains a bibliographic lead, not an import. These are optional,
not essential source blockers: the current attempt assumes no general
classification or stability theorem beyond the explicitly conditional
finite-group input. Institutional screenshot requests timed out; the
relevant MOLS theorem/proof text was accessible and inspected. Mathlib
coverage for the full target and these stability results is not checked.

## One bounded mathematical continuation

Retain exactly TARGET for the next action, using this EXPLORE assessment.
The following are proposed proof obligations, not deductions made here.
Try to recover the used labels and six column classes intrinsically from
the large common subfamily. Any correspondence must be induced by the
actual ambient bijections; a chosen coordinate correspondence cannot be
substituted. Account for unused points and the unspecified right column.

If recovery succeeds, use L125's normalization to formulate the partial
three-function affine equation. Seek exact completion through finite
incidence or a justified reduction to the finite-group theorem above.
Track exceptional ordered pairs, translations and constants explicitly;
setting an input to zero is unjustified unless that instance is known
to survive. Near-affinity alone does not establish the target. Use the
existing 840-map certificate only after its exact input hypotheses hold.
No new factorial enumeration or mathematical script is part of this
proposed symbolic attempt, and no general classification theorem is
needed as an unstated premise.

Continue on a rigorous proof of the target, a counterexample satisfying
all its hypotheses, or an independently useful recovery statement with
an explicit residual completion test. A counterexample must retain the
actual q,T and overlap threshold; arbitrary Latin-square trades do not
qualify. If the attempt requires full-star equality, imposed column
preservation, a stronger overlap hypothesis or unbounded enumeration,
record that failure and park this mechanism or choose a materially
different test. Do not silently strengthen hypotheses. A complete-looking
proof must receive a later separate critical audit.

## Disposition

The source-only outcome is EXPLORATION: the exact implication remains
unanswered, but inspected primary results and comparisons justify the
specified bounded residual test. No new lemma, target specialization,
mathematical calculation, counterexample or script was produced, and no
new mathematics is approved as established. No mathematical exploration
turn is spent by this review. PROOF.md and DAG.md remain unchanged because
the mathematical argument and its inputs have not changed. This completed
review supersedes the provisional source-review checkpoint saved in this
file during the turn. Any separate supervisor approval of this updated
ready continuation remains separate from the completed review.
