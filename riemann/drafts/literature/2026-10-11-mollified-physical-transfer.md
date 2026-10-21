# Short mollifier: weighted physical replacement and response tails

TARGET: Establish the constant-scale weighted physical replacement and uniform response-tail bound for the length H^(1/100) Mobius mollifier with P(u)=u^2.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-statistic and stronger-moment comparison in 2026-10-11-arithmetic-resonator-discriminant.md; this covered subtarget changes only the application, not the inspected scalar theorem or its hypotheses. No local weighted-transfer duplicate was found in the specific mollifier and fixed-weight records checked.
SOURCE_EVIDENCE: Bui–Hall arXiv:2304.05178v1 mollifier definition, Proposition 1 and Section 3 (6)–(8), pp. 6–8, directly inspected in step 58; L390 complete leading-jet replacement and pointwise full-response tail proof; L394's fixed-weight comparison is retained as stop evidence, not an input to this transfer.
COMPARISON: The source gives sharp normalized mollified critical-jet moments at fixed orders; L390 gives pointwise physical and response-head errors. Their weighted physical specialization is not stated in the source and must be justified, but needs no new moment theorem, growing-twist carrier result or arithmetic coefficient evaluation.
GAP: Verify the actual Hardy identification and ordinary derivative factors through order two, normalize with L=log(2+t), retain envelope curvature and complete response derivative errors, and obtain an N-uniform absolute tail bound before taking limits. No such weighted estimate is proved in this assessment.
REASON: One bounded known-source specialization can remove an essential weighted-transfer obligation of the positive-discriminant-mean proposal while leaving its independently unresolved carrier and total coefficient untouched. Import the primary theorem by citation; do not reprove it.
SCOPE: Fixed actual Delta,d,d_N,U of L390, real H tending to infinity, sharp [H,2H], y=H^(1/100), P_H(t)=sum_(n<=y) mu(n)n^(-1/2-it)(log(y/n)/log y)^2; uniform response-head limits; no RH, simplicity, common-zero assumption, D sign or positive-mean assertion.

## Exact proposed thresholds

Set U=x^2+y_jet^2+z^2 in L390's notation (y_jet=f'/L; the
mollifier length y is a separate symbol), eta_N=sum_(n>N)n^(-5/2).
The sought conclusions, with one constant independent of N and H, are

    (1/H) integral_[H,2H] U |P_H|^2 = O(1),
    (1/H) integral_[H,2H] |Delta-d| |P_H|^2 = O(1/log H),
    limsup_(H->infinity) (1/H) integral_[H,2H]
                    |d-d_N| |P_H|^2 <= C eta_N.

They are targets only. The absolute second and third bounds would permit
signed mean transfer at constant scale, first H->infinity at fixed N,
then N->infinity. They would not evaluate either signed mean.

## Source applicability and proof obligations

Import Bui–Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, Proposition 1, Section 3 (6)–(8)](https://arxiv.org/html/2304.05178v1#S3).
The polynomial u^2 satisfies P(0)=0 and P(1)=1; exponent 1/100
is strictly below 4/7. The moments are already sharp on [H,2H].
Use fixed derivative orders only. Do not differentiate the mollifier:
the relevant derivatives are those of the critical function. The
actual f/Hardy identification and the signs of ordinary derivatives
must be stated explicitly; source (7) includes i^k and source (8)
controls its errors. L=log(2+t) differs from log H pointwise on this
interval; justify every use of that change rather than differentiate
an unspecified asymptotic error.

Reuse L390's pointwise physical comparison, its controlled response
derivatives and its full-tail proof. Its unweighted L2 result alone
does not establish the proposed weighted conclusion. Retain the exact
envelope-curvature term and the derivative-series bounds responsible
for the physical error. Verify constants independent of the response
head N, and do not sum errors whose constants grow with N.

No signed bracketing or new endpoint theorem is required for these
absolute transfer bounds, since the cited scalar input is sharp.
No fixed-head moment coefficient or growing-support carrier estimate
is covered here. These remain independent gaps of the full weighted
mean. The precise global main gap is still actual-theta mixed positivity.

Continue if all three thresholds hold for the complete physical quantity;
otherwise preserve the exact failed obligation and stop this transfer
implementation. A valid transfer is useful without a positive mean:
it would make a later carrier/coefficient test about actual Delta rather
than an uncontrolled approximation. It provides no discriminant sign,
common-zero count, extended positivity range or RH consequence.
Matching Mathlib coverage is not checked. This newly written ready
continuation requires the supervisor's separate next-turn approval.
