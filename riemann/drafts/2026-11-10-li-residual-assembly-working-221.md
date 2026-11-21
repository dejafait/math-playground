# Weak-cutoff residual assembly — step221 working record

Approved target: review219's corrected actual-zeta residual, n>=2.
Inputs read: L013, L018, L977, L978, L979; normalization context
L964/L968; source comparison review218 and integration review216.
No independent finite-head sign mechanism is asserted.

Planned assembly: write H_n=lambda_n(sqrt(n)), R_n for the actual
conjugate-paired tail, V_n for the arctangent-model tail, and
B_n=integral_0^infinity K_n(t) log(t/(2*pi))/(2*pi) dt.
L978 pays R_n-V_n; L979 pays V_n-(B_n-lower interval).
Arias's inspected J1 formula gives B_n=n*J1(n), matching Lagarias's
archimedean trend. Need to write absolute paired radial/height
agreement, both smooth endpoints, the lower interval bound, and
the exact identity lambda_n=H_n+R_n before claiming the result.
Delta=1 must remain in the arithmetic identity. All cutoff atoms
belong to H_n. No Section6 contour estimate will be used.

This is a saved proof plan, not evidence of the estimate. The final
proof, if completed, will be canonical in L980; this record is retained.

Completed later in this step: the full argument is now in
`lemmas/L980-corrected-weak-cutoff-li-residual.md`. All listed
obligations were written, including the retained delta=1. This
working plan remains historical; it is not a second proof or status
record. Independent critical review of L980 is still required.
