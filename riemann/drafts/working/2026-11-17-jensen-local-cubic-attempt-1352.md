# Exact local cubic replacement1352 — working checkpoint

Approved target: the exact TARGET of assessment1350, whose SPECIALIZE
coverage was supplied at invocation. No source refresh or new target is
being undertaken. C019c/C019d and their critical replays have been read;
automatic-Airy stop1345 is retained. Existing unfinished work is preserved.

Main gap: L030–L032/C032a actual-Xi all-degree positivity. The intermediate
test is a uniform additive o(M_d) replacement on
epsilon=(log d)d^(-1/3), keeping every finite Taylor coefficient,
P_d and both counterclockwise arcs. Success could enable a later signed
reference comparison; it cannot provide signs or exceptional-root control.
Continue only if both errors have a complete uniform vanishing certificate.

Candidate calculation (not yet recorded as a result): write
Psi=-A exp(i theta)+(E+i C theta)exp(i theta/2)-2 log r-i theta,
where A=q r^2, C=2 kappa r/Lambda and E=2 kappa r+2 C log r.
The exact saddle equation gives E=2(A+1)cos(alpha)-2C.
After the common C019d onset, 1<=A<=3, 0<C<=1 and |E|<=10.
Direct differentiation suggests
Psi''''=-A exp(i theta)+(E/16+C/2+i C theta/16)exp(i theta/2),
so |Psi''''|<=5 on |theta|<=theta_0<=1/10.
Taylor remainder then gives |Psi-T3|<=5|theta|^4/24.
Use Re(Psi)<=H_q and the exact exponential-difference integral to
bound interpolation by exp(d H_q+5 d epsilon^4/24); this does not
assume that the cubic inherits Re(T3)<=H_q.

Remaining verification: common branch/amplitude across zero, both
orientations, exact integration of the B1|theta| amplitude error and
the B0*(5d/24)|theta|^4 phase error, and division only by positive M_d.
No mathematical script or numerical evidence is needed.

Completed: the full specialization is recorded in
[C019e](../../lemmas/C019e-actual-jensen-finite-cubic-replacement.md).
The fourth-derivative certificate is at most 661/160<5. Both error
terms integrate to a uniform O(d^(-1/3)(log d)^5) bound on the
unchanged M_d scale. No failed inequality remains in this attempt;
independent critical replay is pending. The next turn can reuse the
unchanged assessment1350 for this same mathematical target. A signed
reference and global exceptional-root control are still separate gaps.
