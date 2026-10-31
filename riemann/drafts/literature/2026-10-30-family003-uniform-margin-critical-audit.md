# Family 003 conditional uniform-margin audit

TARGET: Audit the real-loss and late-height choices in OpenAI family 003 prop:parameter-order at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a for a common positive m and sigma=m/2, conditional on the explicitly stated arithmetic and uniformity contracts.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed uniform-margin-audit-scope source review and existing family003 overlap/analytic assessments; no new discovery claim. The exact parameter-selection result is already in the pinned source and is excluded from L531's completed audit.
SOURCE_EVIDENCE: Complete primary prop:parameter-order proof and final application, bootstrap, all final endpoint/range cases, plain and detector-counts hypotheses, principal contract and late-height-closure proof were retrieved in the companion assessment; stable labels, rendered line ranges and exact primary URL are there. No additional essential source is needed for this conditional audit.
COMPARISON: A successful audit reproduces the manuscript's conditional loss allocation and height closure, not its arithmetic estimates, Theorem 1.1 or a stronger zero-free region. Reproof is justified only as independent verification of the remaining uniformity step after L531.
GAP: Check finite loss budgets, all bin/frequency endpoints, mesh-before-slot order, common positive exponent selection and target-dependent late height/order choices. Preserve the 11/12 bootstrap, arithmetic estimates, uniformity and N-independent retained degrees as explicit assumptions.
REASON: The changed continuation is covered by accessible primary proof cases; separate next-turn approval must precede execution. This is a conditional REPRODUCTION target with an order-of-choices test.
SCOPE: Real-parameter/slot selection and late-height assembly under source contracts, including algebraic replay of the displayed endpoint certificate if needed. No new arithmetic estimate, internal fourth-moment proof, H construction, full manuscript/formal audit, transfer or new half-plane conclusion.

The [completed source assessment](2026-10-30-family003-uniform-margin-audit-scope.md)
records the full margin inventory, case boundaries, exact inspected passages
and remaining premises. Primary source:
[OpenAI September 30 TeX, pinned commit](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`prop:parameter-order` (rendered lines 15331–15576) and
`lem:late-height-closure` (6129–6187). Full matching Mathlib coverage is
unchecked; L531's inversion theorem is supporting analytic context only.

State beta_*=7/8+Delta with 0<Delta<=1/24, kappa=2 beta_*-1, the primitive
Hecke family and pole convention of L531, and h=13/16, ell=1/6,
l_x=17/48, l_y=23/48. The earlier 11/12 theorem is an unaudited premise.
Assume the source's normalized low, principal, moderate-bin, row-count and
outer-row contracts, with the qualifications in the companion review.
In particular assume arbitrarily small losses with coefficients independent
of eta, mesh independent of slot count, finite internal orders uniform over
moving labels, and tail scale degrees independent of external N. Deep proofs
of these assertions remain outside the result being audited.

The source's desired margin is

    m=(1/4)min{min((51/64)Delta,63/800),23/960,13/9600,7/(96K)}.

This is a source claim awaiting audit, not a result of the present review.
Test that losses, even K and disjoint windows, e, zeta and the large-row
line can be fixed before eta without assuming the final 7/8 conclusion or
uniform constants/thresholds over eta. Then test the detector ceiling,
late tau_eta and N_eta choices, and common omega=Delta/2, sigma=m/2
needed by L531. At delta=5/6 use the separate no-slot contract. Do not
treat pointwise row pieces as holomorphic sums.

Pass only if each inequality and choice follows from explicit contracts and
leaves m>0 independent of eta. If a coefficient depends on a later choice in
a way not covered by the contracts, record the precise missing uniformity;
do not silently assume another theorem. Preserve partial reasoning on failure.

L531 supplies the downstream analytic reduction, not the missing arithmetic
premises. L452/L461 are context only. Actual-Xi all-degree positivity, initial
signs, effective overlap, arithmetic realization and RH remain open. No
cross-notebook input is proposed. This newly ready assessment requires
separate approval next turn and authorizes no mathematics in this literature
step. Route as proof_audit/conceptual_audit; no justified new arithmetic
mechanism is prepared for a creative attempt.
