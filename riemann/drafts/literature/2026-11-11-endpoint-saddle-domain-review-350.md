# Fixed endpoint saddle — missing domain comparison

TARGET: Assess whether Vanlessen's exact bulk Laguerre formulas supply uniform analytic amplitudes on a contour through the theta=1 endpoint saddle for the complete compensated packet response.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step351 reused reviews291/325/344/345 and searched Vanlessen Laguerre bulk lens 3.45; no matching fixed-contour theorem was identified. Read the primary lens construction and exact bulk proof; unrelated search hits remain unread leads.
SOURCE_EVIDENCE: Read https://arxiv.org/pdf/math/0504604v2 (29 August 2005), Theorem2.4(b)/Remark2.5 pp5-7, Section3.4/(3.39)-(3.52) pp18-20, Section3.8 construction pp31-32, Proposition3.31/Theorem3.32/(3.100)-(3.110) pp32-34 and Proposition5.1/(5.5)-(5.6) p39; reused C997e's audited normalization.
COMPARISON: Exact analytic matrix control and two-branch reconstruction are covered conditional on an admissible bulk lens. The existential strip and endpoint-disk constants do not certify the prescribed contour. C997m's movable large-theta saddle does not close this difference; C997n supplies no data lower bound.
GAP: A quantitative Q=x lens/sign and containment specialization remains necessary before the theta=1 saddle-rate calculation; neither success nor failure of that specialization is established.
REASON: Source access is resolved but automatic fixed-contour import is unavailable. Park the rate calculation; nominate an independently testable phase-sign/lens construction for separate approval, without deriving a contour theorem here.
LITERATURE_REASON: Essential unread source scope: quantitative placement or permissible choice of the bulk lens and reduced contour around the fixed theta=1 saddle, outside the containment guaranteed by C997m's large-theta argument.
SCOPE: Same review345 family, theta=1,lambda=A/128,fixed A>=A_0 before n; only the exact analytic-amplitude domain and its source hypotheses. No new saddle estimate, changed packet, varying parameters or actual-Xi transfer in the review.

The following nomination was saved after step350 and reviewed in the
separate literature-only step351 below; it does not approve new mathematics.
Reuse the existing inspected theorem
and proof ranges wherever they already answer the question; retrieve
the primary domain/lens hypotheses and relevant proof cases before
larger source passages. No broad repeat search is requested.

For clarity the proposed stationary point is specified algebraically:
delta=1/8, beta=1/8+i, and

    s=delta^2*beta/(1+sqrt(1+delta^2*beta^2)),

with the positive-real-part square root. A contour at Im(c)=Im(s)
between the two slope endpoints is one proposal, not a certified
deformation. Assess whether the exact R_N representation is uniformly
controlled on a neighborhood of that contour and its vertical sides,
for c*(n+u)/(4*(n+1)), all real u in [0,2] and all sufficiently large n.
Do not silently extend a real-axis O(1/n) estimate. If another contour
is supplied by the inspected theorem, record its exact hypotheses;
do not derive a new contour theorem during the source review.

Continue to a separately approved mathematical test only if this domain
coverage is adequate. Otherwise record the precise source limitation
and park this dependent saddle calculation; do not repeat access or
domain audits without a new independently testable input.

Essential local inputs for later mathematics are C997n(2)-(3), C997m(2),
C997e(4),(15)-(16) and C997c(1),(5), with L997 through those contracts.
C997n is unaudited and must be checked before being used as a decisive
error bound. The proposed rate threshold is strictly greater than13/64
for the pure endpoint comparison at2; achieving it would rule out this
subfamily, whereas failure to prove it is inconclusive. The source
review alone cannot establish leading nonvanishing, endpoint charges,
other-branch dominance or any complete data rate.

Main gap remains L030-L032/C032a actual-Xi positivity, L966/L968 signed
forcing and L984(H). Point bridge, selected/both-sign transfer, C997a(8),
assay/reconstruction, recovery/complements/regulators and L993 remain
unpaid. Matching Mathlib coverage is unknown. No cross-notebook input.

## Separate source comparison — step351

M. Vanlessen, *Strong asymptotics of Laguerre-type orthogonal polynomials
and applications in random matrix theory*,
[arXiv:math/0504604v2](https://arxiv.org/pdf/math/0504604v2),
29 August 2005, is the primary source. Printed pages are one greater
than PDF page indices. No other version was inspected.

The source hypotheses specialize to alpha=2>-1, Q=x, degree N=n+1
and beta_N=4N. Its construction chooses
0<delta_src<min(delta_1,delta_2,delta_3), 2pi/3<nu<5pi/6.
Equation(3.45) supplies an existential positive-phase strip; Section3.4
places the lips there. Section3.8 matches the end pieces to local
Airy/Bessel inverse images; the reduced outer arcs are independent
of N. Proposition3.31 removes the real bulk jump, Theorem3.32
controls R_N off the reduced contour, and Proposition5.1 gives exact
reconstruction inside the bulk lens. Equation(5.6) retains both branches.

Thus no continued real-axis O symbol is needed. Conversely, R_N's
analyticity does not place a point inside the lens, where reconstruction
changes. The inspected statements and proof cases give no quantitative
height enclosing this prescribed contour. Figure5 is schematic. The
explicit phase(3.39),(3.41),(3.47) and monomial Remarks2.3/3.15
supply a testable specialization, not its conclusion.

This is a source-scope negative: automatic import does not discharge the
fixed-contour hypothesis. It is neither a counterexample nor an access
failure or packet-family stop. No phase-sign calculation, new contour
theorem, lemma or script was made. The response-rate test stays parked.
The next phase-sign/lens construction is nominated in
[review351](2026-11-11-classical-laguerre-fixed-lens-test-review-351.md)
for separate approval. It does not use C997n's unaudited error estimate.
