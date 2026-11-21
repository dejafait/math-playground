# Continuation665: bounded Bernoulli diagonal test

TARGET: Test whether a finite Bernoulli-corrected digamma prescription for C998a's fixed frequencies n=0,...,255 certifies analytic error at most 2^-45, elementary/rounding error at most 2^-47 and total diagonal setup cost at most 10000000 scalar operations.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed review664/comparison665 and source-notes665's exact complex-diagonal terminology search, primary theorem comparison and local duplicate/failure check; the frozen inputs and tolerances are unchanged. No novelty inference.
SOURCE_EVIDENCE: Primary direct URLs verified666: https://dlmf.nist.gov/5.11#ii (5.11.2 and complex remainder); https://dlmf.nist.gov/5.5#E2 (recurrence); https://dlmf.nist.gov/24.2#E1 (Bernoulli convention); https://arxiv.org/pdf/2109.08392v1 (Johansson Sections3.1-3.2, printed pp12-14,(25)-(32),Theorems3.1-3.2 and full3.2 proof). Reuse655/656/658 only for elementary inclusion; source-notes665 retains full scope and algorithm cautions.
COMPARISON: Known recurrence plus a finite higher-order complex remainder covers the method for all256 arguments. C999(19) supplies effective first-order computability;664 stops that prescription's cost. Neither imports a complete higher-order numerical ledger, and661's positive-real gamma bridge is not that ledger.
GAP: Choose finite parameters, pay constants and exact Bernoulli coefficients, prove analytic and arithmetic errors separately for every output, and bound the entire shared diagonal setup. No parameter/error/cost calculation was performed665.
REASON: Essential source scope is ready for one bounded REPRODUCTION calculation after separate next-turn approval; citation alone cannot establish these finite tolerance/work requirements.
SCOPE: Same C998a frozen652 archive, exact frequencies and operator, all256 modes including0, original scalar work convention664, no quadrature batch or signed-pairing claim. No trial, witness, reference, threshold or forcing change.

The main gap remains L030-L032/C032a actual-Xi positivity, including signed
S3 remote-plus-induced coupling. An affordable certified diagonal would
remove one prerequisite for a complete residual-Gram computation and
C999 inverse comparison. Full Gram, inverse debt and the subsequent sign
remain independent obligations. This is numerical specialization, not a
creative mechanism at the central sign gap.

Use the cited higher-order digamma formula and recurrence, not a new
special-function identity. For this single bounded test consider shifts
K in {16,32,64}, first-omitted Bernoulli indices N in {4,8,16}, and
fractional precisions in {128,256,512} bits. These are proposed exploration
limits, not certified feasible parameters. A single uniform prescription
may suffice; mode-dependent choices require a finite certified table and
paid branch decisions. Do not use unbounded order/precision doubling.
Do not import log-gamma relative-error examples as digamma absolute errors.

Keep the analytic remainder at most2^-45 for EACH returned h(k_n).
All other errors together, including ell, pi, k_n, log(pi), elementary
series truncation, coefficient enclosures, reciprocal/log evaluation,
summation and rounding, must be at most2^-47 per value. The source bound
is evaluated at the exact mathematical argument; interval uncertainty in
that argument must be paid, not silently substituted into the theorem.
Separate analytic remainder from numerical enclosure width and retain
the n=0 case. The complex-sector theorem supplies magnitude, not sign.

Use664's work unit: one real addition, subtraction, multiplication,
division, comparison or assignment at the chosen finite precision.
Expand complex and elementary calls into charged operations. Explicitly
count coefficient generation, constant construction/range reduction,
all256 shared values, table/branch setup, cache writes and the scalar
assembly needed for the three frozen finite Dq columns. Charge precision
management; disclose operand/register bounds, with a16384-bit cap as an
additional finite-design limit. Do not treat one special-function call,
one Bernoulli term or a benchmark time as one scalar operation. A claim
of radius/precision from a library needs actual inclusion evidence.

Continuation test: a full analytic/arithmetic certificate meeting BOTH
per-value tolerances and a rigorous complete setup upper bound<=10000000
permits continuation toward the residual ledger. No actual Gram or sign
is authorized by that success alone. A proved mandatory cost>10000000
stops the tested prescription. A loose upper bound exceeding the ceiling
only leaves feasibility unresolved. If no allowed prescription is
certified, save all partial/error/cost evidence and choose a materially
different mechanism or independently testable target, preserving664's
first-order stop; do not start another parameter-retuning loop.

Essential inputs: C998a/audit655, complete654/655 data; C999/audit650
Section4(19) and floor; C999q exact Z; C999y/audit642 exact X;
C744v/w/z,C999k,C999z/audit646 for retained interpretation contracts.
Pinned652 SHA2562b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6
is unchanged. C998e's full Gram/error result requires its separate audit;
the scalar theorem comparison and this test do not assume it. C998b/c/d/e
remain unaudited. Scalar/quadrature/interface/projection/residual-size,
signed S3,higher/mixed endpoints,C744q/H2, non-neutral and global/source
obligations remain open. No cross-notebook input. Mathlib full matching
coverage is unchecked. Save unfinished reasoning before lengthy work;
any later mathematical script saves complete evidence under
scripts/separation-seven/ and prints bounds, failures and artifact paths.

This continuation was written665; separate literature approval666 verified
the direct primary URLs and retained SPECIALIZE with the target unchanged.
The derivative formulas (25)-(29) are on printed p12, not p13; the
remainder definition and Theorem3.1 are on p13 and Theorem3.2 with its
complete proof is on p14. The source-notes665 page shorthand is corrected
accordingly. No theorem scope, finite parameter choice or work bound is
added by this repair. No lemma or mathematical script was modified.
