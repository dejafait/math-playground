# Penultimate Jacobi reference: retained-cost stop1504

One research attempt under the pre-existing EXPLORE assessment1503.
Canonical result and complete qualifications:
[C028c](../lemmas/C028c-penultimate-jacobi-reference-retained-cost-obstruction.md).
Its finite certificate is `scripts/jacobi-reference/penultimate-cost-1504.json`.
Positive matching is feasible in every degree d>=5. The failure is the
retained cost, not a failure to find admissible parameters.

**WHY IT FAILS.** Positivity bounds the shifted mean and variance even
when the original recurrence parameters vary or approach their boundary.
Three cancellations force the cubic residual to tend uniformly to zero.
The actual first five coefficients, using L778's audited evaluator and
complete error under its existing contracts, exclude a simultaneous zero
of the cubic, fourth and fifth residual polynomials. The canonical
compactness argument therefore gives B_d>=c*d^4 uniformly over all
feasible choices eventually; the required necessary budget was o(d^2).
No omitted squared term can repair this obstruction. Actual root heights,
other positive references and RH remain undecided.

Stop this specified family and preserve the prior C028a/L763/L764 and
L827 scope stops. A separate audit of C028c is nominated, not another
parameter search or an extension of the failed full-sum calculation.
After audit, reopening would require a materially different recurrence
mechanism or a demonstrated error, not changed parameter scalings already
covered by C028c. The new finite arithmetic is not formally verified.
