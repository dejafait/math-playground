# Single real-zero factor — working checkpoint2227

Approved target: assessment2225, separately approved2226. This is one
REPRODUCTION application, not a new general-method or RH claim.

For an arbitrary actual root 14<x<29/2, try
G_x(u)=x integral_u^infinity K(t) sin(x(t-u)) dt, u>=0.
Differentiation gives G_x'=-x^2 integral_u^infinity K(t)cos(x(t-u))dt
and G_x''+x^2 G_x=x^2 K. Hence G_x'(0)=-x^2 Xi(x)=0.
The imported even smooth theta kernel and the ODE should give all odd
origin derivatives zero. Both G_x and G_x' are bounded by constants
times the complete tail integral of K; derivatives then follow by
the ODE. The imported strictly decreasing-amplitude sine theorem
applies to K(u+v) and should give G_x(u)>0 at every u>=0.

Remaining checks before canonicalization: full weighted-tail bounds,
dominated differentiation, smooth even extension, absence of a decaying
homogeneous ambiguity, the two transform endpoint terms, entire
extension and values at removable poles including multiple roots.
No numerical script is needed. C919f is used only for existence under
its retained backend contracts; L024 is background for the factor
interpretation and may be unnecessary as a direct proof input.

Repeated-removal monotonicity and the all-degree bridge remain open.
Do not infer either from the positive residual. Exact source and failure
coverage is reused from notes2225; no source discovery is being repeated.

Completion2227: all listed checks are now written in canonical C919m.
This checkpoint is preserved as unfinished reasoning history, not a
second proof or current continuation. The result is REPRODUCTION and
pending separate critical audit; PROGRESS.md records the next action.
