# Coupled third-contour phase jet — nomination945

TARGET: Assess the local cubic-phase cancellation test for a coupled permutation-equivariant three-variable Bromwich deformation at x=B'(1), retaining the full algebraic Vandermonde and all Jacobians.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review946 searched equivariant holomorphic volume normal forms, singular-volume/hyperplane-arrangement equivalence, isochore Morse lemmas, and perfect contours; inspected the primary passages below. Reused review925's integration/deformation coverage and compared C466a/k/l/p and stop941. No exact theorem with the full prescribed jet and equivariance was located; no novelty inference.
SOURCE_EVIDENCE: Domitrz–Rieger, author preprint v2.pdf https://www2.mathematik.uni-halle.de/rieger/v2.pdf Section2 definitions, Theorem2.6/proof pp6-7 and Proposition2.14/proof p10; Lebl, Tasty Bits v4.4 (31May2026), https://www.jirka.org/scv/scv.pdf Theorem1.3.8 p32 and Theorem1.2.1 pp20-21; Cardona–Miranda arXiv:1812.03800v3 https://arxiv.org/html/1812.03800 Definitions2.1-2.2, Section3 Theorem4 and its transversality case. Reuse review925 for Andreief and closed-form deformation; precise comparisons below.
COMPARISON: The inspected tools permit a local normalization applicability audit, not an import of this contour. Nonvanishing-volume results do not apply directly to the entire Vandermonde-weighted form; transverse-zero results do not cover intersecting squared collisions. Existing finite signs already settle D3 under C466p's external qualifications. A genericity negative control must precede actual-weight coefficient fitting.
GAP: Whether center-coordinate normalization meets all collision, equivariance, prescribed-derivative and cubic pullback conditions remains unproved. Generic feasibility would disqualify this local jet as a sign discriminator. Global admissible deformation, convergence, orientation outside the germ, unbounded order and Xi transfer remain independent gaps.
REASON: Adequate local analytic tools are now inspected for one bounded specialization audit. Import those tools and check their applicability; do not reprove normal-form theory, assume its symmetry hypotheses, or claim a globally perfect contour. This literature turn performs no normalization, coefficient calculation or new mathematical derivation.
LITERATURE_REASON: Changed coupled-contour hypothesis in nomination945 required essential normal-form coverage absent from the earlier product-contour and signed-inversion assessments. This review supplies that local coverage; further literature before the bounded audit needs a new essential reason.
SCOPE: Nomination945's exact local three-variable test, including a generic symmetric nonvanishing holomorphic-weight negative control with positive value at the origin. Check one center-coordinate normalization with differences held fixed, then its degree-four truncation only if justified. No global contour construction, all-order claim, actual determinant-sign computation or independent certificate replay is covered. New ready scope receives separate supervisor approval next turn.

## Review946 — source statements and limits (14 November 2026)

This is one literature comparison, not a proof of generic feasibility
or an obstruction. The original finite test below is preserved.

The relevant local records were read narrowly: C466a's hypotheses and
normalization; C466k's hypotheses, signed inversion and scope; C466l's
three-variable inversion through its full real-coordinate Jacobian;
C466p in full; and stop941. Review925's assessed deformation input is
reused. C466k demands separately positive scalar/pair factors on a common
curve, unlike this test. Stop941 concerns the original marginal, not
all coupled cycles. C466p prevents presenting a third-sign calculation
as discovery. No sibling notebook or broader historical census was used.

The external queries included `equivariant holomorphic volume forms
Moser normal form singular volume form Coxeter discriminant`, `isochore
Morse lemma Vey 1977 holomorphic volume form theorem`, `singular volume
forms quasihomogeneous relative Darboux theorem Domitrz Rieger`,
`holomorphic volume form hyperplane arrangement local equivalence Moser
theorem`, `holomorphic rectification theorem vector field parameters`,
and `Lawrence Yamauchi perfect contour local existence holomorphic
volume form Jacobian`. Searches located tools and limitations, not an
exact equivariant collision-preserving theorem. Uninspected Vey and
equivariant Darboux leads are not theorem inputs.

**Subgroup normal forms.** Domitrz–Rieger's author-hosted preprint
[Section 2, printed pp6-10](https://www2.mathematik.uni-halle.de/rieger/v2.pdf)
uses origin-fixing local diffeomorphisms H and a function-module M
inside LH. Theorem 2.6 requires nonvanishing forms and
Omega0-Omega1=d(i_X Omega), X in M; real orientations must agree.
Its complete proof divides by an interpolated density and integrates
the resulting field. Proposition 2.14 requires X(0) nonzero and the
entire maximal-ideal module mX inside LH, then gives H-isotopy of
volume germs. Its complete proof uses a one-coordinate primitive.
Module membership and the prescribed derivative/equivariance remain
to check; this is no direct singular-form import. Lemma 4.10 was read
as a nonessential lead. Publication:
*Mathematische Annalen* 345 (2009), 783-817,
[doi:10.1007/s00208-009-0375-z](https://doi.org/10.1007/s00208-009-0375-z);
the locators above refer to the inspected preprint, not journal pagination.

**Elementary analytic tool.** Lebl's author-hosted
[*Tasty Bits of Several Complex Variables*, v4.4](https://www.jirka.org/scv/scv.pdf),
Theorem 1.3.8, printed p32, concerns holomorphic f(z,w) on an open
subset of C^n x C^m. At a zero with invertible w-derivative it supplies
a unique local holomorphic solution w=g(z). The preceding explanation
reduces holomorphicity to the real implicit theorem and chain rule;
the detailed proof is an exercise. Theorem 1.2.1, pp20-21, supplies
locally uniformly absolutely convergent power series, via the iterated
Cauchy formula. These are imported standard tools. A parameter-dependent
primitive and its derivative, symmetry and finite truncation still
require an applicability argument. They are not supplied here.

**Singular-form comparison.** Cardona–Miranda,
[*On the volume elements of a manifold with transverse zeroes*,
arXiv:1812.03800v3](https://arxiv.org/html/1812.03800), Definitions
2.1-2.2 and Section 3, Theorem 4, treat smooth folded forms: the
coefficient vanishes transversally along a hypersurface. The equivalence
theorem assumes matching ordinary and relative cohomology classes;
its proof uses a primitive vanishing quadratically in a defining
function. The squared collision factors in nomination945 are not
transverse, and their intersections introduce another mismatch. Thus
this theorem cannot approve the nominated germ or its continuation.

**Contour interpretation.** Reuse review925's inspected
Lawrence–Yamauchi,
[*Convex optimization of contour deformations*, PRD110 (2024) 014508](https://doi.org/10.1103/PhysRevD.110.014508),
equations (4)-(8), p3. Section II.B's equations (11)-(16), also read
in the primary publisher text during review946, distinguish constant
effective phase (including the Jacobian) from the phase of the weight
alone. Local minimizers can still have global phase differences
separated by zeros. This comparison does not assert existence of a
minimizer for the present integral.

## Bounded audit reserved for a later research turn

First test whether a center-coordinate change holding both difference
coordinates fixed can normalize a generic symmetric nonvanishing
holomorphic coefficient with positive constant term. Use the inspected
parameter-dependent implicit theorem; verify rather than assume every
nonzero derivative, uniqueness-based symmetry, collision extension and
the full determinant of the coordinate change. Equivariance alone
does not license invoking a theorem whose Lie algebra must contain a
whole module. Keep the original real parameterization, signed
Vandermonde, factors of i and orientation.

If the generic normalization exists with the required first derivative,
check whether its degree-four truncation really pays all imaginary
terms through degree three after division by the squared Vandermonde.
Do not assume truncation preserves a divided identity. Only then compare
with the actual A_x; no actual-density Taylor fitting is needed if
genericity settles the discriminator. This is an ordinary specialization
audit, not a creative claim about a new route to RH.

The decisive result sought is a precise genericity verdict or a
specified collision/symmetry/orientation obstruction. If genericity is
established, park the cubic local test and require a materially global,
independently testable target before reopening coupled contours. If an
actual obstruction is established, abandon that ansatz with its exact
scope. Failure of one construction is neither an obstruction theorem
nor evidence of nongeneric feasibility; save that unresolved condition
without spending another turn merely increasing the jet order.

Essential local inputs are C466a/k/l, with C466p only for the already
known sign and its stronger external trust base. Generic local
analytic hypotheses must be distinguished from those density inputs.
Global integrability, deformation homology, zeros encountered by a
continuation, end connectors, all orders and L030-L032/C032a transfer
are not approved by this assessment. Full matching Mathlib coverage is
unchecked. No lemma or mathematical script was written in review946.

## Original nomination (prospective test preserved)

## Exact prospective test, for assessment rather than execution

Use C466a/k/l's actual h, p and x=B'(1), and put
A_x(z)=exp(xz)/h(z). The evaluation point is the same, but the
proposed object is a local cycle, not a new computation of its known
determinant sign. Retain C466p's stronger external qualifications
only when invoking its sign; the local analytic formulation itself
must say precisely which density and analytic inputs it needs.

The prospective unknown is a coupled map z(u), u in R^3 near zero,
with z(0)=(1,1,1), Dz(0)=iI and permutation equivariance. For a bounded
test restrict its correction to homogeneous polynomial terms of
degrees two through four. It must retain each collision plane:
u_i=u_j implies z_i(u)=z_j(u). Analyze the full pullback of

    -Delta(z)^2 product_j A_x(z_j) product_j(dz_j/i),

where Delta is the algebraic Vandermonde, without conjugation or
separate scalar/pair positivity. The proposed success condition is
that division by the real squared Vandermonde leaves an analytic
coefficient with positive constant term and no imaginary Taylor
terms of total degree at most three. Analytic extension across
collisions is part of the target, not a fact established here.
No coefficients, cancellation identities or feasibility verdict
have been computed. The degree-four ansatz is a proposed finite
scope whose adequacy also requires review.

## Relevance and continuation test

The main gap remains L030-L032/C032a all-degree actual-Xi positivity.
A genuinely coupled phase construction could supply a starting
mechanism for signed integration after the failure of pointwise
marginal positivity; it would still require a global contour and an
order-uniform argument before informing that gap. A local positive
jet alone proves no integral sign and cannot be promoted to a proof.

First compare precise primary results and recorded local failures,
including whether the same finite jet exists for arbitrary analytic
weights and therefore fails to discriminate actual-Xi positivity.
If a generic coordinate-straightening theorem makes it automatic
without a useful global extension, park the test as uninformative;
do not create a lemma solely to record that local feasibility.
If an exact collision/orientation obstruction rules it out, retain
that obstruction and abandon this ansatz. Only adequate source
coverage plus a concrete mathematical discriminator permits a later
attempt. Neither adding more Taylor coefficients nor citing the
already-positive third determinant resolves a failed compatibility
test. No historical product-contour stop is treated as a ban on
all coupled cycles.

This new continuation receives a separate literature turn. Its
assessment should search exact local normal-form/holomorphic volume
and steepest-descent statements, inspect primary hypotheses and
essential cases, and import any matching result rather than reprove
it. Full Mathlib coverage is unchecked. No creative proof attempt
is approved until the review identifies a relevant, nonautomatic
test; source coverage is the current routing blocker.
