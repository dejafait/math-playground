# Full-theta Stein specialization — saved reasoning

Approved target: the exact reciprocal-hazard specialization in
`drafts/literature/2026-10-31-actual-theta-stein-specialization.md`.
Main gap: actual-Xi all-degree signs at unbounded heights. This step can
establish only the actual-density monotonicity premise, leaving sign transfer.

L019 and Csordas v2 (4.2) match as k(u)=4 Phi(u/2) on the full line,
using the imported even extension. Put q(s)=Phi(sqrt(s)), J=integral q,
f=q/J, S(s)=integral_s^infinity f, r=f/S. For u>=0 the substitution
v=2 sqrt(s) gives v dv=2 ds, so integral_u^infinity v k(v) dv
=8 integral_(u^2/4)^infinity q(s) ds. Thus tau(u)=2/r(u^2/4).
Check finite J using J=2 integral_0^infinity t Phi(t) dt; finite positive
full-line normalization uses L019. Theorems 4.1 and 4.2(b) give even
smoothness/decay and log-concavity of q; Bagnoli--Bergstrom Corollary 2
then gives nondecreasing r. Retain nonstrict monotonicity only.

At zero, q(0)=Phi(0)>0 and its tail tends to J, so tau(0)=2J/Phi(0).
The centered full-line numerator is even and smooth with derivative
-u k(u), hence the quotient is even smooth and tau'(0)=0.
Do not infer a Fourier sign or sign L604's integrated remainder.

Primary theorem statements and the complete hazard concave proof case
were retrieved. Its printed last line has the already-recorded sign/reference
typo; the preceding inequality and Remark 4 agree with Theorem 3/Corollary 2.
Import those named results without reproving them. Original 1988 theta
proof remains unaudited. No scripts or numerical certificates are needed.

Completed: L605 contains the full specialization and qualifications.
The factor 2, normalization cancellation and zero endpoint all pass;
the remaining downstream gap is the Fourier-sign transfer. A separate
later audit is proposed, not performed or approved within this attempt.
