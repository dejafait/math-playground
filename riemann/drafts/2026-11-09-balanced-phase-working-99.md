# Finite balanced-phase attempt — step99

Completed later in this step: the candidate 1/512 constant and closed
simplex transfer are proved in
[L951](../lemmas/L951-finite-balanced-phase-quadratic-localization.md).
Both exact Taylor checks passed. The earlier partial reasoning below
is preserved as working history, not an outstanding obligation or a
substitute for the canonical proof. Independent audit is still pending.

Approved scope: the unchanged EXPLORE target in
`literature/2026-11-09-balanced-phase-finite-localization-97.md`, including
only its finite-sum transfer. Main gap: L030–L032/C032a actual-Xi
all-degree mixed positivity. A scalar constant could supply one later
signed-localization input; no signed mass payment is attempted.

Inputs read: L939(10)–(14), L938's exact signed density and simplex;
the L940 amplitude obstruction and L950 fixed-row stop are contrasts.
The supplied assessment and its source approval are reused unchanged.
No new literature search, cross-notebook input or numerical kernel
contract is needed for this analytic attempt.

Partial reasoning saved before the constant check:
put tau=sqrt(1+s/r)-1, a=2r. Then

    s=r tau(tau+2), h_r(s)=exp(a tau)-1-a tau-r tau^2.

For -1<=tau<=0, DLMF1.4.37's exponential integral remainder gives

    h_r(s)>=(r-1+exp(-2r)) tau^2.

For tau>=0 it gives h_r(s)>=r(2r-1)tau^2. No square-root
derivative is taken at s=-r; tau=0 is an exact equality case.
Candidate constant: 1/512. For r<=1, it suffices to prove
exp(-13/8)>25/128, since r>=sqrt(2/3)>13/16 and
r-1+exp(-2r) is increasing there. For 1<=r<=2 it suffices to
prove exp(-2)>1/8. The seventh-degree Taylor polynomial with
positive eighth-order remainder should certify both inequalities.
These rational checks and the complete domain transfer are still to
be written out. No completed proof or mass estimate is claimed here.

Continue only if both uniform scalar cases and all simplex endpoints
close; otherwise preserve the unpaid obligation or rigorous obstruction.
Independent remaining gaps: signed-amplitude errors, local-ball fit,
full-theta/boundary mass, effective infinite join, head/global variation,
other signs/degrees, contacts, initialization and realization.
