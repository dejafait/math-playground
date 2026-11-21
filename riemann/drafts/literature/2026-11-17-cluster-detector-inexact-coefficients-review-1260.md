# Enclosure detector with certified coefficient errors — review1260

TARGET: Review sufficient certified error tolerances for C032b's enclosure-only detector when both its degree-M polynomial coefficients and the logarithmic moments ell_k=-S_k/k (2<=k<=2M+2) are approximated, retaining a rigorous full Q<0 conclusion under the unchanged support and mass hypotheses.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the 7November multipair assessment and review1256; read L895's complete finite-error argument, L030, and C032b's hypotheses, bounds and full-Q proof. Targeted local searches for inexact basis/polynomial, simultaneous moment/coefficient errors and quadratic-form perturbation found no matching cluster certificate. External queries and inspected sources are recorded below; no novelty inference.
SOURCE_EVIDENCE: N.J.Higham, What Is a Matrix Norm?, 12October2021, Mixed Subordinate Matrix Norms, Theorems1 and3, including the duality and row/column proof cases; N.J.Higham, Eigenvalue Inequalities for Hermitian Matrices, 9March2021, Quadratic Form, Courant-Fischer and inequality(1)/spectral-norm consequence. Precise URLs and hypotheses below. The second source reuses existing coverage; the first covers the changed bilinear-error tool.
COMPARISON: Standard mixed-norm bounds cover finite bilinear terms with arbitrary real coefficient vectors and matrices, without positivity or distinct-node assumptions. L895 covers moment errors with an exact vector only. Neither source states the requested joint cluster-specific tolerance; specialize the standard tools to C032b's supplied M,C,A,B and strict margin, rather than reprove a general perturbation theorem.
GAP: Explicit jointly sufficient polynomial-coefficient and logarithmic-moment tolerances, their full error accounting and a rigorous negative certificate remain to be derived. Certified approximations are inputs, not an implemented output. Actual-Xi support, a nonreal cluster, mass/coefficient data and all-degree signs remain independent gaps.
REASON: Missing source coverage for the changed inexact polynomial is now supplied by finite bilinear norm bounds. This approves one subsequent specialization, not a tolerance theorem or an implementation. Preserve the original target and all geometric hypotheses.
SCOPE: Exactly C032b's conjugation-invariant nonzero multiset, multiplicities, full closed support and mass assumptions. A supplied real polynomial of degree at most M has a certified coefficient-l1 distance from the exact constructed q; supplied real ell_hat_k have certified uniform errors for every 2<=k<=2M+2. Only one scalar negative direction, finite tolerances and full Q control are covered; no node separation, root reconstruction, new Runge construction or actual-Xi inference.
COVERED_TARGET: Derive explicit jointly sufficient coefficient-l1 and logarithmic-moment error tolerances for C032b's degree-M detector using its M,C,A,B bounds and Q(q)<=-3/2 margin, proving strict negativity for both the rounded polynomial's exact Q and its finite approximate-moment evaluation under the unchanged support and mass hypotheses.
LITERATURE_REASON: The saved nomination1259 was REVIEW_REQUIRED because L895 assumes an exact basis; simultaneous polynomial and moment errors change that hypothesis. Reused ready Runge and moment coverage and inspected only the missing finite bilinear tool.

## Relevance and retained problem

The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
The intermediate target is stability of a conditional negative detector
under two certified finite-data errors. Its downstream use is a finite
logarithmic-coefficient certificate robust to polynomial rounding and
cluster collisions. This supplies neither actual Xi data nor positivity.

Retain nomination1259's target without substituting a root-recovery
problem. C032b supplies a finite M, a coefficient-l1 upper bound C and
the complete bound Q(q)<=-3/2. Its nodes lie in |z|<=B and have total
absolute mass at most A, including multiplicities and the infinite
near-zero part. Its exact construction was independently audited1259;
there is no reason to repeat the pole-chain proof here.

For the later specialization, pad both real coefficient vectors through
degree M. Use the same finite monomial Hankel expression as L030, with
the generic summability justification in L895. All logarithmic moments
through 2M+2 must be supplied, including both endpoints. Distinguish
the exact Q of the rounded polynomial from its evaluation using rounded
moments. A certificate must pay both errors and any separately incurred
evaluation rounding; exact rational evaluation is an allowable choice.
This review derives no new error bound or tolerance formula.

## Precisely inspected tools

N.J.Higham, [What Is a Matrix Norm?](https://nhigham.com/2021/10/12/what-is-a-matrix-norm/),
12October2021, section Mixed Subordinate Matrix Norms, Theorems1 and3.
Theorem1 applies to any finite complex rectangular matrix and vector
norms, characterizing the mixed subordinate norm by a bilinear expression
with the dual norm on the left vector. Read its complete duality proof.
Theorem3 gives column and row characterizations when an input norm is
1 or an output norm is infinity. Read the column expansion and the
row Hölder proof, including their equality cases. These are sufficient
finite bilinear tools; positivity is not a hypothesis of these cases.
Use the real restriction here, with nonzero vectors in norm quotients
and zero-vector cases handled directly. The later real symmetric
Hankel matrix may be indefinite. No positive-measure assumption is
introduced. Do not use the separate positive-semidefinite special case
at the end of Theorem3, which is unnecessary for this target.

N.J.Higham, [Eigenvalue Inequalities for Hermitian Matrices](https://nhigham.com/2021/03/09/eigenvalue-inequalities-for-hermitian-matrices/),
9March2021, Quadratic Form and Courant-Fischer sections, inequality(1)
and its spectral-norm consequence. Reused the inspected 7November
assessment and checked the displayed primary statement. Finite Hermitian
matrices, including real symmetric matrices, are required. This is
additive matrix stability; it does not itself control a moving test
vector. A scalar certificate needs no eigenvalue computation. Do not
misuse a negative eigenvalue as a guarantee about a prescribed vector.

These author expositions supply precise standard statements. The
mixed-norm proof cases were read; the eigenvalue exposition does not
provide a complete proof of Courant-Fischer, which remains a named
standard input. No source is asserted to contain the final joint
tolerance for C032b. The explicit specialization is needed to track
the particular mass/support bounds, polynomial norm, power shift and
logarithmic normalization. General continuity alone gives no specified
precision and does not meet the continuation target.

## Comparisons, searches and limitations

L895's finite-precision proof bounds moment perturbation at a fixed
coefficient vector and explicitly excludes uncontrolled basis errors.
It may be reused for that part after bounding the rounded vector's
norm; its exact-node interpolation constants are not imported for
enclosures. C032b and L030 supply the relevant normalization and finite
form identity. No renewed external Hermite-signature review is needed:
the existing 7November assessment already records its finite-system
scope, and no rational reconstruction or root input is proposed here.

Queries used: `quadratic form perturbation vector matrix error bound
certified polynomial moments Hankel`; `site.nhigham.com matrix norms
subordinate norm bilinear form`. The first returned structured-Hankel,
matrix-pencil and random quadratic-form leads but no inspected matching
joint certificate. These leads are unread and unused, not evidence
of absence. The second led to the inspected author's matrix-norm
exposition. Only the primary statements above are used as coverage.

Local searches covered the cluster/multipair assessments and failure
records, then exact inexact-basis, simultaneous-error and bilinear terms
in active-notebook assessments and ATTEMPTS. No matching completed
cluster tolerance was found. Preserve the direct-constants stop1256:
this target does not reopen Schönlein's unchecked quadrature/pole-shift
constants. Grunsky and spin stops remain as recorded in review1256;
no mathematical input is taken from those routes. Full Mathlib coverage
is unchecked, not claimed absent. No cross-notebook theorem is used.

## Continuation and abandonment test

Approve only the COVERED_TARGET above for a later mathematical attempt.
Seek explicit positive sufficient tolerances in the supplied parameters,
retaining a strict negative margin after both errors. Check B below,
equal to and above 1, degree-zero padding where applicable, zero errors,
all cross terms and the complete moment range. An exact Q<0 statement
alone does not certify an inaccurately evaluated scalar; conversely a
negative approximate scalar needs a rigorous error allowance.

Continue only with certified coefficient distance and moment errors
as explicit inputs and complete finite bounds. If the argument needs
unprovided root positions, internal separation or unexplained accuracy,
record that limitation rather than claiming an implementable certificate.
No practical precision or complexity threshold is required or promised.
Actual-Xi realization and signs remain unresolved even if this succeeds.

This is routine specialization of known finite-form tools, not a new
central signing mechanism. A justified creative target remains blocked
by the absence of a concrete theta-specific signed input. Do not invent
one to satisfy scheduling. The newly covered continuation receives its
separate approval next turn; no lemmas, mathematical scripts, PROOF or
DAG were modified in this literature-only step.
