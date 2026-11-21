# Nomination664: independently testable diagonal setup

TARGET: Assess a Bernoulli-corrected digamma rule for C998a's fixed frequencies n=0,...,255 with analytic error at most 2^-45, elementary/rounding error at most 2^-47 and total diagonal setup cost at most 10000000 scalar operations.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Comparison665 searched complex digamma/Bernoulli remainder terminology and Johansson's rigorous gamma algorithms; checked scoped12November duplicates/failures and reused655/656/658 elementary inclusion. Exact queries, inspected passages and failed URL leads are in source-notes665. No novelty inference.
SOURCE_EVIDENCE: DLMF1.2.8(15September2026),5.11.2/5.11(ii),5.5.2,24.2.1; Johansson arXiv:2109.08392v1(17September2021),Sections3.1-3.2 printed pp13-14,(25)-(32),Theorems3.1-3.2 and full3.2 proof, Algorithm4 pp11-12 and Section3.3 pp15-16. Full hypotheses and exact remainder are recorded in source-notes665.
COMPARISON: Known recurrence and finite Bernoulli remainder cover the entire fixed complex set, including the real zero mode. They supply a higher-order alternative to664's stopped first-order prescription; neither their asymptotic work discussion nor661's positive-real bridge establishes this finite setup's error/cost target.
GAP: Select a finite shift/order/precision prescription and certify complete constants, coefficient, rounding,256-value and assembly costs within10000000. Source scope is ready; no local tolerance, parameter feasibility or cost bound has been proved665.
REASON: Primary derivative remainder and its proof discharge the changed source hypothesis. A separate bounded REPRODUCTION calculation may specialize them after next-turn approval of the newly written continuation665; no further general browsing is needed under unchanged assumptions.
LITERATURE_REASON: Bernoulli corrections and their higher-order complex-sector remainder replace the stopped first-order C999(19) prescription, outside the exact numerical rule assessed655/656; a positive-real gamma bridge does not discharge these hypotheses.
SCOPE: Same exact ell=log(3)/2,k_n=n*pi/ell,n=0,...,255; no reference, trial, witness, threshold or forcing change. Total full-Gram ceiling remains100000000; diagonal setup gets at most10000000. Source review only; no new formula implementation or lemma this review turn.

## Completion665

The source review is complete. Full citations, theorem hypotheses,
the inspected proof case, applicability and remaining numerical gap are in
[source-notes665](2026-11-12-higher-order-diagonal-source-notes-665.md).
This is known-method coverage, not a feasible diagonal certificate or
progress beyond the sources checked. No new mathematics was derived.
The separately nominated continuation is
[test665](2026-11-12-higher-order-diagonal-test-review-665.md).
Its fresh ready coverage needs separate approval next turn.

## Original nomination664 (pending-review statements superseded above)

Main gap remains L030-L032/C032a actual-Xi positivity, including signed
S3 remote-plus-induced coupling. A certified affordable diagonal setup
would remove one concrete prerequisite for the complete residual-Gram
calculation. It would supply neither a sign nor an efficient quadrature
and would leave all higher/mixed endpoint, H2 and global gaps unresolved.

Preserve the cost result in C998e and its full certificate664. Its product
identity and conditional budget are unaudited; the next SOURCE REVIEW
does not depend on accepting that identity. The diagonal target is defined
independently by C998a's finite q and C999(19)'s diagonal. Any later use
of C998e's full representation still needs critical review. Reuse ready
coverage of elementary inclusion arithmetic and exact Z; do not repeat
Si/Ci browsing or point-oracle threshold searches.

Inspect primary DLMF5.11.2 and5.11(ii), with5.5.2 for the recurrence, or
a primary equivalent with a complete usable remainder. Record exactly
which sector, shift, order and error convention the theorem permits.
Neither an asymptotic symbol nor an unqualified special-function call
pays absolute error. No chosen Bernoulli order or shifted-sector estimate
is asserted in this nomination. Retrieve statements and essential proof
cases before a larger extract. The changed precision mechanism needs a
separate approval; do not derive and approve it together.

Continue only if inspected sources cover the entire finite complex set
and allow an explicit setup error/work test with these unchanged tolerances.
If they do not, record the specific mismatch and nominate a materially
different independent target; do not repeat the stopped first-order rule.
The intended subsequent calculation would count constants, coefficients,
all256 shared diagonal values, precision and assembly within10000000
scalar operations. This is a future discriminator, not achieved work.

Essential inputs: C998a/audit655 with complete654/655 data; C999/audit650
Section4(19); C999q's exact Z and C999y/audit642's exact X; C744v/w/z,
C999k and C999z/audit646 for retained interpretation contracts. Pinned652
archive SHA2562b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6
is unchanged. C998e664 is local unaudited evidence, not a verified signed
input. C998b657/C998c660/C998d662 remain unaudited. Full scalar/complex
quadrature, exact interface, projection, residual-size and signed-pairing
obligations remain open. No cross-notebook input. Mathlib full matching
coverage is unchecked; no absence claim.

No justified creative central sign mechanism is ready: removing this
setup bottleneck supplies no signed S3 control, and full residual/inverse
debt is still unknown. The source task is ordinary theorem comparison,
standard/high, rather than a creative proof attempt.
