# Low-order radial associated-theta model stop — 2026-10-31

The gate-approved test was whether delta*A(i(pi/4-delta))->+infinity
for the exact first associated theta kernel, retaining all modes.
The full proof and constants are in [L596](../lemmas/L596-associated-theta-radial-boundary-growth.md),
which is written but not independently audited. It gives the stronger
lower bound A(i(pi/4-delta))>=C delta^(-9/2), C>0. The previous
bounded-strip and proportional-degree saddle work is retained.

WHY IT FAILS: An ansatz requiring A(i(pi/4-delta))=O(delta^(-1))
at this point contradicts that lower bound, provided L596 passes audit.
In particular the tested low-order radial behavior cannot be supplied
by assuming bounded or simple-pole radial size for this exact A.
This stops that ansatz only. It does not exclude arbitrary integrable
horizontal traces, stronger singularities, subtraction or regularization,
nor establish any Tuck positivity hypotheses or Xi signs. Reopening a
boundary route requires materially different, independently assessed
hypotheses compatible with this growth. Next: independent L596 audit.

Audit update — 31 October 2026: the complete independent replay in
canonical L596 passes without a change to its estimate. The provisional
condition on this radial-model rejection is discharged. Stronger-growth,
subtracted or regularized contour methods remain unassessed; the stop
does not extend to them or to horizontal traces.
