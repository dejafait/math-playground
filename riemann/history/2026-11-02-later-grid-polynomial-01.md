# 2 November 2026 — angular evaluation of the later grid coefficients

STEP_ID: 2026-11-02-later-grid-polynomial-01.
One RESEARCH proof_attempt/development under the unchanged ready angular
EXPLORE assessment. Outcome ADVANCE, classification REPRODUCTION: the
advance is an explicit local quantitative reduction, not the target
lower bound or progress beyond the checked standard evaluation machinery.

[C645z](../lemmas/C645z-angular-point-evaluation-and-later-grid-mean.md)
proves maximum angular amplitude <=2n times its root mean square for
the full largest Hankel norm, constant-input response and C645y's later
grid energy. The proof counts both angular pole classes, retains the
polynomial part at infinity, and evaluates their finite Hardy-kernel
cost. It fixes the Hardy input before passing to the operator supremum.
All constants are exact; no mathematical script or quadrature was needed.
The new result remains separately unaudited.

The common degree-M polynomial has not yet supplied a lower bound on
the later coefficients. The reduction removes an exponential angular-
width loss from any future large-angle test. The refined sufficient
threshold is c*n*exp(-n/32) at one rotation per family, or a strict
exponential margin with polynomial factors. This is the sole retained
continuation in [the working note](../drafts/2026-11-02-later-grid-polynomial-working.md).
The original prefix/dual stops are preserved; no operator countersequence
or actual-Xi conclusion follows. No new assessment was written.

PROOF's existing C645 paragraph was shortened to record this input.
Its displaced wording said C645r/v/w had audited subfamily bounds,
C645s/t were stops, C645x was the audited fractional-dual stop, and
C645t stopped initial prefixes through ceil(n/2), including M. Those
qualifications remain canonical in the existing proofs and histories.
The only new DAG row lists C645g and C645y as direct mathematical inputs.
No shared infrastructure, scheduler state or prior unfinished work was
changed.

Validation: the required notebook-scoped documentation checker passed
(711 nodes, 1745 edges), and scoped whitespace checks passed. Direct
mathematical inspection checked the pole multiplicities, reflected
radii, n-j-1 polynomial part, the fixed-input operator argument, and
D_n<4n^2. The final 2n inequalities are non-strict, so they require no
extra assumption that a selected tail is nonzero. This is an author
check, not a separate conceptual audit of C645y or C645z.
