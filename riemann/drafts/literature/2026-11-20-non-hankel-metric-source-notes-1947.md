# Non-Hankel metric discovery1947

Literature-only review, 20 November 2026. No new commutator estimate,
coefficient asymptotic, lemma or mathematical program is established.
The actual gap is C028b's H_d=o(d), alongside L030-L032/C032a's
all-degree actual-Xi positivity. This review compares two constructions;
the finite-horizon construction survives only as an untested proposal.

## Primary sources actually inspected

**Finite-horizon energy metric.** Tony Stillfjord and Filip Tronarp,
*Computing the matrix exponential and the Cholesky factor of a related
finite horizon Gramian*, arXiv:2310.13462v2, 30 April 2024 (PDF title
date 1 May 2024), [primary PDF](https://arxiv.org/pdf/2310.13462v2),
Section1, (1b)-(2), p1; Section1.2, (5), p4. Read these definitions,
hypotheses and the differentiation justification. For arbitrary real
finite matrices N,B, the integral W=integral_0^1 exp(tN)BB^T exp(tN^T)dt
is positive semidefinite, and positive definite for a controllable pair.
The source's endpoint identity is

    N W+W N^T=-BB^T+exp(N)BB^T exp(N^T).

No stability or invertibility of the Lyapunov operator is needed for
this identity. For a proposed real generator M and horizon T>0, use
N=T M^T and B=sqrt(T)I. This gives the observability energy integral
over [0,T]; the identity input makes the pair controllable. Principal
blocks inherit positive definiteness. Thus this construction supplies
a positive metric without assuming real roots. It supplies no small
defect, conditioning bound, uniform-in-degree estimate or certified
numerical inverse. None of the paper's floating-point error guarantees
is imported for a new implementation.

The HTML endpoint displayed a different manuscript date; the versioned
PDF above fixes the source used here. The numerical-algorithm proof is
not needed for this exact integral construction and was not audited.

**An essential qualification on equation solving.** Martin Redmann and
Patrick Kürschner, *An H2-Type Error Bound for Time-Limited Balanced
Truncation*, author manuscript dated 2 July 2018,
[primary repository PDF](https://pure.mpg.de/rest/items/item_2491617_13/component/file_2630664/content),
Lemma2.1 and complete proof/remark, pp5-6 (PDF indices4-5), inspected.
Its Sylvester formulation assumes Lambda(A1) intersect -Lambda(A2)
is empty. The proof inverts the Kronecker-sum operator; the following
product-rule remark establishes the endpoint equality directly.
Finite-time integrals exist for unstable systems too. We use the
integral definition, not an asserted unique algebraic solve. In the
proposed oscillatory realification, spectral pairs make uniqueness
particularly unsafe. No spectral-disjointness premise is imported.

**Bézout/Nuij quasi-symmetrizers.** Tatsuo Nishitani, *Notes on
symmetrization by Bézoutiant*, arXiv:2004.03825v2, 12 June 2020,
[primary PDF](https://arxiv.org/pdf/2004.03825v2), Proposition2.1,
Corollary2.1, pp4-7, and Proposition3.1 with full proof, pp7-8,
inspected. Proposition2.1 assumes a monic hyperbolic p and a separating
q. Corollary2.1 takes q=p'. Section3 starts with hyperbolic p and
strictly hyperbolic approximants p_epsilon. Its (3.1)-(3.2) control
p_epsilon' and (p-p_epsilon) at the approximating roots; (3.3) is an
energy-relative commutator estimate. The proof uses the real-root
Vandermonde/Gram representation and the residual factorization
Q_epsilon=S_epsilon G_epsilon. These are not coefficient-only
positivity statements for arbitrary nonhyperbolic polynomials, and the
constants are not established uniformly in degree. The source uses
the transposed companion convention. Transposing coordinates cannot
remove its hyperbolicity premise. This construction is not selected:
positivity for the actual family would require the unknown root reality.
No assertion is made that all conceivable Bézout modifications fail.

## Reuse and comparison with existing results

Reuse Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica16(2002),203-217,
[Lemma1, pp211-212](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
as already inspected in source-notes1931/1943 and canonical C028h:
total absolute imaginary eigenvalue parts are bounded above by the
Schatten trace norm of the Hermitian imaginary part, with algebraic
multiplicities. Reuse Watrous, *The Theory of Quantum Information*,
2018 author version, [Section1.1, (1.165)-(1.181), pp32-34](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf),
under ready assessment1523, for the ideal/compression inequality.
No repeat search or reproof of these matrix inputs is necessary.

Read C028b's actual family/criterion, C028h/i's hypotheses and proofs,
C028o/p's exact measure/metric and norm formulas, the four stops1525,
1588,1695,1713, and C029a's audited branch hypotheses/conclusion.
C028h excludes every positive diagonal similarity; C028i also excludes
one specified terminal shear. C028o/p exclude the prescribed full-theta
moment metrics at fixed/arbitrary positive dilations. C029a excludes
its specified two-site Schmeisser branch. None asserts a lower height
bound or excludes a general positive metric. The proposed dynamical
Gramian mixes all companion coordinates and is not restricted by
construction to any of those moment-matrix or shear families. No claim
that its defect is smaller, or that it is non-Hankel in every degree,
has been established. It must not simply reuse the old block formula.

## Bounded search evidence and exclusions

Queries included `time limited observability Gramian Lyapunov equation
finite time positive definite matrix exponential paper`, `companion
matrix symmetrizer Bezoutian positive definite real roots theorem`,
`approximate symmetrization matrix time average real spectrum finite
time Gramian`, `Jensen polynomial Gramian symmetrizer`,
`"Jensen" "finite-horizon Gramian"`, and `"companion" "Gramian"
"commutator" symmetrizer`. No exact actual-Jensen/d^2-horizon/terminal
three estimate was located. This does not establish novelty.

Notebook-scoped searches in companion/Jensen assessments and attempts,
then exact finite-horizon/observability/Nuij terms in drafts/literature
and ATTEMPTS, found no recorded dynamical-Gramian companion test.
Nuij references found there concern other hyperbolic-root perturbation
questions; finite-horizon hits concern unrelated detector continuations.
No sibling notebook was read or used. The supplied PROOF/DAG preceded
these targeted local reads. Existing unfinished changes are preserved.

Kürschner's *Balanced truncation model order reduction in limited time
intervals for large systems*, repository item2473547, was a relevant
search lead but its PDF returned403. It is not a theorem input; the
accessible versioned Stillfjord-Tronarp PDF and Redmann-Kürschner proof
resolve the needed finite-horizon scope. Generalized Riccati Gramians,
root-fitted spectral metrics and search-result RH constructions were
not inspected or imported. This is not a persistent essential source
blocker. Full matching Mathlib coverage is unchecked, not absent.

## Selected bounded test and remaining gaps

The exact proposal is saved in assessment1947. It fixes a normalized
actual companion, the real oscillatory generator, horizon T_d=d^2,
and a G-orthonormal terminal-three commutator. The increasing horizon
allows full-coordinate propagation instead of a single shear; no
source proves this horizon is sufficient. The discriminating question
is whether its normalized compression tends to zero or has a positive
liminf. The former would only remove this one obstruction; the latter
would stop this prescribed metric schedule. Both require new analysis.
The complete trace-norm defect, actual coefficient uniformity,
conditioning and any numerical evaluator/backend contracts remain
unresolved. A small terminal compression alone cannot pay H_d=o(d).

This completes the discovery target as EXPLORATION, without a
mathematical estimate. The newly prepared test assessment needs separate
approval next turn before research. No PROOF/DAG update is warranted.
