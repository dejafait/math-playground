# Quantitative multipair certificate — source assessment

TARGET: Construct an explicit degree bound and certified tail-error tolerance yielding at least m negative directions in L030's form for any specified m distinct nonreal conjugate node pairs under L032's summability hypotheses, retaining multiplicities and without assuming actual Xi signs.
CHECKED: 2026-11-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Hermite signature/Hankel power sums, summable nonreal-node inertia, and moment negative-square theory; inspected Akoglu-Szanto's primary finite weighted Hermite statements and local L024/L030/L032/L034/L042/L057. Targeted notebook searches for simultaneous negative subspaces and quantitative Hermite inertia found no matching certificate; no novelty follows.
SOURCE_EVIDENCE: Ayyildiz Akoglu-Szanto https://arxiv.org/pdf/2110.10313v1 (19 October 2021), Section2 Definitions2.1/2.3, Example2.2, Theorems2.4/2.7, printed pp4-5; Higham https://nhigham.com/2021/03/09/eigenvalue-inequalities-for-hermitian-matrices/ (9 March 2021), Courant-Fischer theorem and perturbation inequalities(1), including the operator-norm eigenvalue bound. Full relevant statements were read; L032's complete interpolation and tail proof supplies the local infinite-node comparison.
COMPARISON: Finite weighted Hermite signatures and symmetric perturbation stability are known. L032 already detects one pair qualitatively. The only unpaid specialization is a simultaneous, explicitly bounded finite-dimensional certificate with the entire summable tail and repeated-node weights retained. No source-to-Xi sign inference or originality claim is proposed.
GAP: Explicit common degree, basis independence, negative margin, complete compressed-tail error and allowed coefficient-error tolerance remain to be supplied. Actual Xi node data and all-degree positivity remain independent open inputs; no finite universal cutoff is justified.
REASON: A stable multi-direction certificate could connect a conditional off-real node census to finitely many logarithmic coefficients with rigorous errors. It replaces the exhausted geometric route by an independently testable algebraic certificate problem, rather than by another contour-existence claim.
SCOPE: Exactly TARGET for finite or countable conjugation-invariant nonzero nodes with sum of absolute values finite; specified distinct pairs, their positive integer multiplicities, and a complete finite head enclosing all selected pairs. One bounded specialization using interpolation and finite real symmetric quadratic forms; no scripts, numerical sweep, new spectral realization, unconditional Xi sign or universal degree bound is preapproved.

## Relevance, comparison and bounded test

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
This intermediate target pays a quantitative detection obligation only.
Its plausible downstream use is to make a future independently obtained
node exclusion or signed coefficient certificate checkable at a stated
finite precision. It cannot supply the missing actual-Xi inequality.
If it merely repeats L032 without a simultaneous strict margin and
explicit degree/error bounds, close the attempt as no advance.

Compare three mechanisms:

1. Potential negative-ray incidence: parked by the supervisor; the
   full actual-density image theorem and Jacobian bridge are unpaid.
2. Primitive-K determinant replacement: the unchanged ansatz is already
   excluded and audited in L876 (step26 and repeated step31). A fresh
   audit or fitted repair would duplicate stopped work.
3. Quantitative Hermite certificates: selected. This asks for finite
   evidence conditioned on specified pairs, not an unsupported sign
   or a replacement density. It uses the original mixed form directly.

This is routine specialization of established algebra and L032, not a
creative central sign mechanism. Preparing a creative attempt remains
desirable, but this review supplies no new theta-specific sign input
that would justify labeling the certificate creative.

## Precisely inspected source scope

Tulay Ayyildiz Akoglu and Agnes Szanto, *Certified Hermite Matrices from
Approximate Roots*, arXiv:2110.10313v1, printed pp4-5 (PDF pp4-5):
Definition2.1 allows finite multisets and gives the weighted Vandermonde
form V-transpose G V. Example2.2 gives the univariate weighted power-sum
entries. Definition2.3 and Theorem2.4 identify this with the finite
quotient-algebra trace form, listing roots with multiplicity.
Theorem2.7 states the classical named weighted Hermite signature
theorem for a zero-dimensional real ideal and a polynomial weight:
signature is the number of distinct real roots with positive weight
minus those with negative weight. This is a signature statement, not a
count of positive eigenvalues or a claim of positivity for nonreal roots.
It is stated by citation there, not proved in that paper; import the
standard named theorem rather than attribute a proof to these authors.

Only these finite algebraic statements are reused. Their rational
reconstruction algorithms require additional rational system/input
hypotheses; none is imported for unknown Xi nodes. Repeated equal nodes
cannot be counted as independent directions. The power shift and
nonzero-node weights in L030 must be reconciled in the later
specialization, not assumed to be the unweighted source matrix.

Higham's author exposition states Courant-Fischer for arbitrary finite
Hermitian matrices and records the eigenvalue error bound in spectral
norm for a Hermitian additive perturbation. Read the quadratic-form
section through inequality(1) and its spectral-norm consequences.
The page explicitly omits proofs; use the standard named min-max
theorem by citation. For this application the matrices must be real
symmetric and the error bound must cover the full compressed tail.
No estimate of that tail or negative margin is imported from Higham.

The local L032 proof was read in full, including its fixed finite head,
real interpolation polynomial, multiplicities and complete geometric
tail bound. L030 supplies absolute convergence of the algebraic square;
L042 supplies an absolutely convergent determinant expansion, but no
sign from it. L034 warns that scalar power signs do not determine mixed
inertia. L057 proves that any fixed finite collection of tests may pass
in a generic nonreal-zero family; a uniform cutoff would contradict
that obstruction's lesson and is outside this target.

Queries included `Hermite theorem signature Hankel matrix power sums
number real complex roots trace form`, `Hankel moment matrix negative
index nonreal nodes infinite summable sequence generalized Nevanlinna`,
`Hermite Hankel summable nonreal nodes negative index`, and
`Certified Hermite Matrices from Approximate Roots arxiv`.
The UCSD Lecture11 PDF returned502 and was not retried or used.
Generalized Nevanlinna search results were leads only; no such class
membership theorem is imported or essential here. Jouve-Rodriguez-Villegas
1004.4208v3 was inspected narrowly as a finite Bezoutian comparison;
its rational finite-dimensional signature discussion supplies no
infinite-tail certificate. An unrelated arXiv2110.05645 result was
discarded and supplies no evidence. No search result snippet is treated
as theorem coverage.

## Exact continuation obligations

Use L030/L032 and, for the actual-Xi interpretation only, L024's
summability and L025's logarithmic power sums. L034/L042/L057 are
comparison safeguards, not assumptions. No cross-notebook input occurs.
The supplied finite head must include every node above a stated radius
smaller than all selected pair moduli; its distinct locations,
multiplicities and a rigorous tail-square-mass bound must be explicit
inputs. Their availability for any actual off-line Xi zero is unresolved.

The later attempt should return a common finite degree, m independent
real coefficient vectors and a strictly negative compressed-form margin,
with a rigorous tail and coefficient-error tolerance, all expressed
from those input data. Certify the whole m-dimensional subspace, not
merely m individually negative vectors. Continue only if this adds the
quantitative stability absent from L032; otherwise record the specific
failure or duplication and stop after the bounded attempt. Do not infer
an actual nonreal node, RH, a fixed all-degree cutoff or a spectral
determinant identity. No formula is derived in this literature turn.

Mathlib coverage for the complete specialization is unchecked; this is
not an absence claim. Known general algebra should be cited, with only
the explicit infinite-tail specialization justified locally. The new
assessment requires separate approval next turn before mathematics.
