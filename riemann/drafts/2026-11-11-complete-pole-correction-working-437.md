# Complete correction specialization: working record, step437

Gate: supplied review436, SPECIALIZE, exact complete-Q formula only.
Main gap: actual-Xi positivity; signed event residual and curvature remain open.
Inputs: C999h definition(1), C999g modular normalization, and the
Lagarias–Rains Theorem5.1/proof Mellin transform (review421/435).
No cross-notebook input. Existing unrelated edits are preserved.

Candidate matching to check: write s=w/2+i*t and substitute r=exp(x)
in the imported Mellin integral. Splitting its negative half-line and
using B(-x)=x+B(x) suggests that its polynomial half-line contribution
matches the entire rational pole correction. Check every factor and
absolute/local-uniform convergence before recording an identity.

Continuation test: exact equality with C999h(1) and no uncanceled term;
otherwise record the domain or normalization obstruction. This attempt
does not sign Q, a jump residual, curvature, or an event product.

Completed: C999i gives I(s)=2*xi_Q(0,s)/s^2 and Q=2 Re I(s).
Its half-line split retains integral_0^infinity u*exp(-s*u)du=1/s^2,
which supplies exactly the rational correction. Explicit common
majorants justify the split and local uniformity. The source product
factor is -1/2 after substitution. No mathematical script was needed.
Full proof and qualifications are canonical in C999i; no sign is paid.
