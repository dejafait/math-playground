# Ihat accumulation rounding: source-scope nomination1809

TARGET: Develop a costed rational-comparison rounding contract for C033z's Ihat(1) accumulation, propagating its error to all eight scalars while preserving both2^-10 allowances and the10^6 full-evaluator cap; stop if no such contract is certified.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Parent rounded-execution review1808 completed by source comparison1809; exact rational/rounding/operation-count searches and scoped direct-positive-real duplication/failure check are recorded in drafts/literature/2026-11-19-direct-positive-real-rounded-source-notes-1809.md. This narrower finite-sum target has no matching cost theorem among the inspected sources; no novelty inferred.
SOURCE_EVIDENCE: Johansson1611.02831v1 Sections3.1.1-3.2/4/5-5.1, https://arxiv.org/pdf/1611.02831v1; Arb2.23.0 enclosure/quotient contracts, https://arblib.org/arb.html and exact-input/conversion contracts, https://arblib.org/arf.html; MPFR4.2.2 Sections4.4/4.6/5.2, https://www.mpfr.org/mpfr-4.2.2/mpfr.html . Inspected cases and reused analytic sources are specified in source-notes1809; no black-box cost import.
COMPARISON: Known enclosure principles cover accumulation-error propagation; C033z(19)-(23),(28),(31)-(32) supplies the unchanged finite expression and downstream map. A rational-comparison implementation and its cap-specific error/count remain the identified difference. No source establishes a successful schedule or precision.
GAP: Specify and cost selected accumulation-rounding checkpoints with exact samples; bound new error and all downstream effects without spending either allowance or exceeding the full10^6 ledger. Denominator growth/runtime elsewhere and scalar execution remain unresolved even after a successful Ihat contract.
REASON: General arithmetic coverage is ready for a bounded local specialization, with no new analytic or source hypothesis. This newly written ready nomination requires separate next-turn approval; it approves no derived result, implementation or scalar execution in1809.
SCOPE: Only Ihat(1) accumulation rounding; exact samples and other C033z constructors retained. All rounding, comparisons and runtime error-bound work must be expressed and charged in the original rational +,-,*,/,comparison model. No free floor, quotient/remainder, mantissa access, approximate library call or fused operation. No interpolation, TV or actual-Xi conclusion.

Import the known enclosure principles; prove only the finite application's
new cost and propagated error. Use C033z's current989767 ledger/10233
slack as an inherited upper budget, not a verified completed-run count.
No precision, spacing or rounding implementation is predetermined here.
A failed sufficient schedule is not a lower bound for all schedules.
Save partial reasoning and the first failing budget if the test fails.
No lengthy scalar execution belongs to this preflight target.

Essential inputs are C033y/z/u/w, C032s/q/w, C032j and1808 exact
execution/replay artifacts. Retain all divisor, conjugation/multiplicity,
ordinate0 exclusion, strict strip/gamma>14, counting, through100/one-real-
zero-in(14,15), reciprocal-square tail, heat positivity/separate fixed-j,
fixed-v1, zero drift/killing and Gaussian half-variance qualifications.
Source-wide/zero-data validity and matching Mathlib coverage are unverified.
Preserve C033x/1781/1782 and unfinished C033v/audit1791. Downstream use is
finite interpolation data; conditioning, exact weights, TV, observation
interval, signed height, cancellation, realization and actual-Xi positivity
remain open. This is ordinary cost/error calculation, not a creative route.
