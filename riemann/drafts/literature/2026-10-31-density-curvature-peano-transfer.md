# Finite-interval density/curvature transfer: known-input specialization

TARGET: Establish the exact finite-interval Peano transfer between the microscopic second difference of |A_M|^2 and L481's ratio component, retaining the fixed cutoff and explicit boundary weights.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed 2026-10-31-microscopic-density-second-difference.md source comparison and its scoped duplicate/failure searches; the finite-interval transfer was not located in the specified existing results. No claim of originality is made.
SOURCE_EVIDENCE: Carl de Boor, Divided Differences, Surveys in Approximation Theory 1 (2005), 46--69, Section 9 (46)--(48), p. 62, primary journal PDF https://surveys-in-approximation-theory.com/papers/2/2.pdf (manuscript dated 21 December 2004); directly reopened 2026-10-31 and read the hypotheses and complete Peano argument. Local definitions: L477 hypotheses/conclusion and L481 hypotheses, with L572's stop retained only as a contrast.
COMPARISON: The general representation is standard and should be cited, not reproved. Only its equally spaced normalization, the finite-polynomial curvature identification, and the integrated finite-interval weights require specialization. This covers an interface, not the unknown absolute density-difference bound.
GAP: Verify every factor and sign and the full boundary weight before claiming a conditional lower-bound transfer; the unconditional c T log T density bound, actual full-residual comparison, defect thresholds and Xi signs remain independent gaps.
REASON: This is a concrete independently testable part of the previous target with adequate known inputs; it needs no joint shifted-density theorem, Haar replacement, new zeta estimate or repetition of the exhausted rank certificate. No specialization is proved in the literature-only nomination.
SCOPE: Fixed real T sufficiently large, M=floor(sqrt(T/(2 pi))), A_M(t)=sum_(n<=M)n^(-1/2-it), F_M=|A_M|^2, h=1/log T, J=[T+h,2T-h], and the complete ratio component U_T of L481; all ordered pairs, equality terms and endpoints retained. No moving cutoff, phase independence, zero assumption, RH, or conclusion for the chirped component is covered.

## Exact proposed calculation and its downstream use

Use the cited Peano representation at the three sites t-h,t,t+h.
First check the finite derivative identity against U_T's actual
coefficient definition, including its sign and the zero diagonal.
Then integrate the absolute-value inequality over J and retain the
explicit weight on the full derivative interval [T,2T]. The requested
comparison is a finite-interval result, not a periodic norm theorem.
All boundary pieces of that weight must be displayed, including what
happens at T, T+2h, 2T-2h and 2T for sufficiently large T.

The discriminating test is whether the integrated kernel is everywhere
bounded by h^2 and has the asserted nonnegative support. Only after
that check should the calculation state the precise conditional
implication of a c T log T lower bound for the microscopic difference
integral, with fixed c>0, for the ratio L1 norm at the T(log T)^3
scale. If the normalization, sign or interval fails, correct or reject
that proposed transfer; do not silently extend the interval or discard
an endpoint. No density lower bound is assumed as an established input.

This interface is useful because the previous continuation expressly
left it unproved. It cannot by itself decide the density lower bound,
compare U_T with L477's full R_T, or settle either defect threshold.
Do not manufacture a new analytic theorem or a stand-alone lemma count
target from this known calculus specialization. A canonical proof may
record the exact interface once checked, with the conditional premise
prominently distinguished from the established conclusion.

## Applicability and source reuse

The cited primary proof was read in the completed comparison. Our
finite polynomial is smooth on the whole real axis, and h>0 gives
three distinct real knots; therefore no extension beyond the source's
smooth-function hypotheses is needed. The general theorem is imported
by citation. The only local work is finite differentiation, ordinary
integration and checking the cutoff and endpoint conventions.
Use no full-zeta shifted-moment theorem in this calculation.

L477 and L481 supply definitions; no saddle, moment asymptotic or
unreviewed external zero-free input is needed. L572's certificate is
not an input to this transfer and remains stopped. No cross-notebook
input is proposed. Full matching and supporting Mathlib coverage have
not been checked; unknown availability is not an absence claim.

## Separate source approval and URL recovery, 31 October 2026

[Direct primary journal PDF, p. 62](https://surveys-in-approximation-theory.com/papers/2/2.pdf#page=17).
Section 9 assumes real knots in [a,b], k derivatives, and
tau_0<tau_k. Equations (46)--(48) give

    DD_tau f = (1/k!) integral_a^b M(y|tau) f^(k)(y) dy,
    M(y|tau) = k DD_tau ((.-y)_+^(k-1)),

with unit kernel integral. The proof uses Taylor's integral remainder,
polynomial annihilation and the finite derivative-evaluation functional.
For this application require C^2 on the closed interval, stronger than
needed in the source's wording, so Taylor's integral formula is valid.
The finite polynomial is smooth and the three knots are distinct.

This separate literature turn approves SPECIALIZE for the unchanged
TARGET. It repairs the missing direct URL and checks the source scope;
it establishes no specialized identity or bound. The equally spaced
kernel, curvature sign, finite-interval weights and conditional scale
transfer remain the research task. Reuse the preceding comparison's
duplicate searches and failure records; no broader search is needed
for this unchanged interface. Mathlib remains unchecked.

This is a process repair, not a mathematical advance or a new source
discovery. No lemma, DAG or mathematical script is changed. The
proposed calculation is ordinary known-input specialization; the
broader density-norm mechanism still lacks essential coverage and
does not yet justify a creative proof-attempt nomination.
