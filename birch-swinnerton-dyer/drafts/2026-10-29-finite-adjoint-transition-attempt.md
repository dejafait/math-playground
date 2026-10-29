# Step 547 — finite adjoint transition working record

Target: the unchanged step-546 SPECIALIZE target, only levels 2 and 1.
Main gap: arbitrary rational rank versus analytic order. Downstream use:
a legitimate finite interface for the held L128 relation comparison;
no arithmetic nonvanishing or control conclusion follows.

Local duplicate/failure check: L128 step-534 audit, L129 and its
step-539 audit, ATTEMPTS/061--063. Reused step-535 and step-545 source
coverage; reopened Fornea v2 Proposition 2.9 including both p-level
cases and Remark 2.12 as calculation inputs, not a new review.

Unfinished checkpoint: direct conjugation gives
w_n^{-1}[[a,b],[c,d]]w_n=[[d,-c/p^n],[-p^n b,a]], so the proposed
w_n normalizes the actual K_n. It inverts diamond labels and exchanges
diag(1,p) with its projective inverse. Transport of the dual of
coefficient pullback appears to be r_1*, since
w_2^{-1}w_1=diag(p^{-1},1) equals diag(1,p) in PGL_2.
The integral evaluation/transfer comparison, projector restriction,
and multiplicities must still be written before claiming a finite pass.

Continue only with the exact integral square and all original labels;
stop on the first discrepancy. Even a finite pass supplies no
surjectivity, all-level control, tame-Hecke relation transfer, scalar,
rational Kummer membership or BSD conclusion. No division by p is
authorized merely by a rational formula.

Completed: the full proof and precise qualifications are canonical in
`lemmas/L131-finite-adjoint-degeneracy-transport.md`. The unfinished
checkpoint above is preserved as working history, not the final claim.
The necessary finite square passes: F_1 beta=r_* F_2 integrally on
the actual ordinary, trivial-finite-diamond summands. The corrected
transition is not asserted to satisfy control. L129's factor p remains
in pi_*=p r_* U_2^{-1}. Separate conceptual review is required before
using this new finite specialization; no all-level extension was tried.
No mathematical script was needed: all checks are exact symbolic
matrix, correspondence and integral-duality arguments written in L131.
