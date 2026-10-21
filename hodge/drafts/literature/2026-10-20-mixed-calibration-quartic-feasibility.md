# Equality kernel — one mixed-calibration quartic feasibility test

TARGET: Test whether the exact-rank pointwise bound Q(K)>=gamma L(K)^2 holds for some gamma above the L071/L131 characteristic threshold, or give an exact curvature triple ruling out every such gamma.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed exact-rank curvature-cone assessment records exact and stronger searches, duplicate/failure comparisons and no inspected theorem supplying this universal lower bound; reuse that comparison without claiming novelty.
SOURCE_EVIDENCE: Fowdar CMP 405 (2024), 183, Section 2 (2.1)–(2.14), https://link.springer.com/article/10.1007/s00220-024-05060-0 gives the exact tangent module; Dai, Lectures on Dirac Operators and Index Theory (7 January 2015), Theorem 3.2.3 and (2.11), https://web.math.ucsb.edu/~dai/book.pdf#page=43 gives Chern–Weil descent; standard integral Cauchy–Schwarz gives the required integration tool; L071/L131 supply the conditional SU(2) category and fixed pairings.
COMPARISON: This asks for a lower bound on the characteristic-square density itself, rather than an upper bound by an unknown fourth-power curvature norm, ordinary positive-form input, or a repeat of the quadratic energy test.
GAP: The universal quartic inequality, its optimal or sufficient constant, the exact threshold evaluation and a discriminating witness are unproved; no new mathematical calculation has been made in preparing this assessment.
REASON: Representation and cohomological coverage are adequate for one bounded algebraic test, with an explicit threshold and a negative witness criterion; separate source review on 2026-10-20 confirms this scope with direct primary URLs; the mathematical test remains unperformed.
SCOPE: Only the specified real thirty-variable triple and fixed mixed four-form below, under L071's equality hypotheses. No search over other functionals, changed metrics, extra positivity, actual-curvature realization or broader classification is approved.

## Essential inputs and precise proposed question

Essential local inputs are L071 and L131; their full tensor and identical
metric are retained. L071 prescribes c_2=14e_1+21e_2+tau_D. L131 supplies
the determinant-trivial SU(2) connection and the pairing with the closed
parallel form Psi=omega_{I,1} wedge omega_{I,2}. F existence is hypothetical.
The universal primitive Hodge gap, reconstruction and transverse transport
are independent unresolved assumptions. No actual connection is built
from a passing pointwise algebraic value.

Work at one standard oriented Euclidean quaternionic product
V=H direct sum H with the same ordered structures as the factors.
Let W be the real invariant two-form space in Fowdar (2.6), of dimension
ten. Choose a basis T_1,T_2,T_3 of skew-Hermitian trace-free two-by-two
matrices orthonormal for -tr(AB), and let
K=sum_{j=1}^3 T_j alpha_j, with arbitrary alpha_j in W.
This is the full exact-rank coefficient model, with thirty real variables;
commuting or one-coefficient examples are allowed witnesses, not a
restriction on a prospective positive proof.

Define C(K) to be the degree-four component of

    det(1 + i K/(2 pi)),

using wedge multiplication in the even form entries, and define

    Q(K) = *(C(K) wedge C(K)),
    L(K) = *(C(K) wedge Psi).

Psi here is the product of the two unit-metric I-Kähler forms on the
quaternionic summands; the Hodge star uses the product complex orientation.
Do not confuse this fixed parallel test form with a claimed Spin(7)
calibration. Do not assume C(K) is weakly positive or Hodge self-dual.
The first task of the mathematical attempt is to check these normalizations
against the full Chern–Weil determinant and L131's conventions.

## Comparison threshold and legitimate downstream use

Name the fixed quantities, without evaluating them in this source turn:

    J = <c_2(F)^2,[X]>, as supplied by L071's full-square formula;
    M = <c_2(F) [Psi],[X]> = 2 lambda s, from L131;
    V_X = Vol(X) = s^2/4, from L131;
    gamma_req = J V_X / M^2.

The requested future calculation must retain the full tau_D contribution
in J and verify its value and the positive-threshold comparison exactly.
The source-covered proposed mechanism is a *universal* inequality
Q>=gamma L^2 with gamma>0. Chern–Weil identifies the two relevant
integrals with J and M. Integral Cauchy–Schwarz on the compact finite-volume
product is the tool for comparing the integral of L^2 with M^2/V_X.
Thus the criterion to be checked in the mathematical attempt is whether
a universal gamma can be strictly greater than gamma_req. No inequality
or numerical threshold is asserted established by this assessment.
In particular an unknown integral of a density product cannot be
replaced by a product of fixed factor charges.

A rigorous positive outcome needs a uniform exact quartic certificate
and the strict characteristic comparison; samples or a numerical minimum
are not proof. An exact triple with L nonzero and Q/L^2<=gamma_req rules
out every strictly stronger gamma of this form. A triple with L=0,Q<0
also refutes the entire proposed family. Either is an informative stop
for this functional, even though it need not occur as curvature of a
global F. If a weaker bound alone survives, compare it with the required
threshold and park this test without asserting existence or an exclusion.
Do not enlarge the functional family during the same bounded attempt.

## Literature use, limits and review boundary

The source and hypothesis comparison is canonical in
[the completed cone review](2026-10-20-rank-two-curvature-square-cone.md).
Its cited primary ranges were inspected before this registration.
No theorem covers the proposed bound in those sources: EXPLORE means a
bounded search did not establish coverage, not certified originality.
A subsequent attempt is POTENTIALLY_NEW, or REPRODUCTION if an adequate
matching result is then identified; it cannot be called KNOWN_IMPORTED.
No reproof of Chern–Weil or ordinary Cauchy–Schwarz is needed. The only
proposed mathematical work is the stated exact-rank specialization and
quartic feasibility question. Mathlib coverage is not checked.

This continuation received its separate source review on 2026-10-20 (step 447).
It was not invoked or derived during either literature-only step. Existing
energy, topology, positivity and calibration stops are preserved, and no
lemma, mathematical script or main argument changed.

## Separate source review — 2026-10-20, step 447

The recovery issue was missing direct URLs in this ready assessment, not
missing theorem-level coverage. Reused the completed cone review and its
duplicate/failure comparison, including ATTEMPTS/081; no new search scope
or mathematical target was introduced. The DOI redirect failed in the
browser, but the direct publisher article above was accessible. Verified
Fowdar's Section 2, especially (2.5)–(2.10): the invariant module is the
adjoint ten-dimensional real two-form representation for an Sp(2)-structure.
This is tangent-space coverage, not a nonabelian curvature-square sign theorem.
The product specialization and the distinction from the independent su(2)
coefficient space remain as justified in the reused cone review.

Verified Dai's Theorem 3.2.3, its Bianchi/transgression proof, and the total
Chern determinant in (2.11), printed pp. 43–44 (PDF pages 43–44). These are
the imported statements. Qualification for the calculation: the displayed
expanded c_2 expression on printed p. 45 uses an i!=j sum and lacks the
usual factor 1/2 in its trace expression; do not import that expansion.
Use (2.11)'s determinant and its homogeneous-degree definition, exactly as
the proposed question already specifies. This source caution changes no
functional or normalization in the saved target. No quartic inequality,
threshold evaluation or witness has been derived. Mathlib remains unchecked.

DECISION remains EXPLORE for precisely the existing TARGET and SCOPE.
This is a process repair with source verification, not a mathematical
advance or a renewed exploration budget. The next turn defaults to the
saved bounded mathematical attempt; no further literature is essential.
