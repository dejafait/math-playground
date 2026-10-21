# Full-response cubic passage — step 117 working record

Approved target: establish the full-response signed cubic asymptotic at
H(log H)^2, taking H to infinity before N. Prior coverage is
`literature/2026-10-14-full-response-cubic-passage.md` (SPECIALIZE).
Main gap: global actual-theta mixed positivity. The intermediate result
would give a complete signed benchmark for a later clipping test, without
supplying clipping, regulator choice, total L367 margin or common-zero control.

The supplied overview/DAG and assessment were used directly. Read L407's
complete reduction and L408's pole/endpoint proof; reused their audits.
Narrow searches of the recent cubic records found no completed passage.
The L394/L399/L400 ATTEMPTS records concern different weights and remain
stopped. Existing notebook edits are preserved.

Work in progress, not yet a theorem: with a=21/20 and r=mn/k, apply the
assessed Milinovich–Ng Lemma 6.1 frequency bound to j/r before summing j.
Separate j comparable to rH from its complement. The endpoint lattice
sum should be bounded by C[H^(-1/2)+r log H], uniformly in the moving
endpoint. Taking d_3(j)<=C j^(1/100) suggests weighted primitive error

    C[H^(11/20) r^(11/20)
      +H^(1/100) r^(-49/100)(1+log_+r)^d
      +H^(51/100)(log H)r^(51/100)(1+log_+r)^d], d<=6.

All three proposed twist powers are summable against (mnk)^(-5/2).
The main arithmetic sum has candidate majorant
C H(log H)^2 sqrt(r)(1+log_+r)^8, also summable. Zero-carrier twists
are integers mnk: isolate j=r, bound nearby denominators using integer
spacing, and check the response-summed resonance is O(H).

Continuation/abandonment test: prove these bounds with both sharp endpoints,
analytic weights and connectors retained, then obtain the signed tail by
dominated response summation. Abandon this certificate if any necessary
twist factor is nonsummable or its H exponent reaches the target scale.
No fixed-head O_N term may be treated as uniform. Essential inputs are
L407/L408, their L391 coefficient/connector bounds and L406 transfer.
The pending tail proof and beta passage remain unresolved at this checkpoint.

## Completed attempt

The preceding text preserves the pre-proof working checkpoint, not the
current result. The complete proof, hypotheses, exact citations and
qualifications now live in
[L409](../lemmas/L409-full-response-positive-signed-cubic-mean.md).
Its uniform kernel estimate, both connectors, zero-carrier resonances
and summable main-term majorant prove the tail and positive coefficient
passage, including physical transfer. No mathematical script was needed.
This is local REPRODUCTION under the prior SPECIALIZE scope, pending
a separately approved critical audit. The proposed continuation is in
`literature/2026-10-14-full-response-cubic-audit.md` (REVIEW_REQUIRED).
Clipping and all independent main-goal gaps remain unresolved.
