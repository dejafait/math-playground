# Conditional common-signal audit — working checkpoint

The approved target is the Section 2 proposition `lem:continuation-criterion`
at OpenAI commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a. Its complete
statement and proof and the pinned Mathlib inversion statements have been
read. The existing source assessment is reused; this is a REPRODUCTION audit.

Main gap: actual-Xi all-degree positivity. This step checks only an analytic
reduction behind the qualified external input, with no arithmetic contracts
proved and no new zero-free region claimed.

Intermediate target: verify holomorphic continuation to Re(s)>alpha, where
epsilon=min(beta_*-sigma_0-omega,sigma)>0 and alpha=beta_*-epsilon>sigma_0.
The same epsilon must work for every primitive target, although constants and
large-Z thresholds may depend on it. Continue only if both endpoints,
inversion, poles and the unattained-supremum case all check out.

Partial reasoning (not yet a final verdict): the deleted reciprocal Euler
product is bounded by product_p(1+Np^(-2)) on Re(s)>=2. Rectangle shifts to
any fixed B>2 give |f(Z)|<=C_B Z^(B+c) for 0<Z<=1. The two assumed large-Z
bounds give |f(Z)|<=C Z^(alpha+c). For compact real-part range [m,M] in the
new half-plane, endpoint majorants are Z^(B-M-1) near zero with B>M, and
Z^(alpha-m-1) near infinity. Logarithmic derivatives are integrable too.

For the exact Fourier convention put a(t)=A(2+it), b(x)=a(2*pi*x), and
g(u)=exp(-(2+c)*u)f(exp(u)). Then g=inverseFourier(b), while directly from
the absolutely convergent defining kernels Fourier(b)(u)=g(-u). Thus the
actual forward-transform L1 hypothesis follows from the endpoint estimates;
the corrected source hypothesis is not an obstruction. Inversion at every
point follows from continuity of b, giving F(2+it)=a(t).

Remaining checks before finalization: identity theorem without assuming
nonvanishing left of 1; principal pole versus a hypothetical nonprincipal
zero at 1; the exact supremum quantifiers. No mathematical script is needed.
No prior work was discarded and no cross-notebook input is used.

Completed: the bounded conditional audit passes. Full hypotheses, proof,
pole cases, unattained-supremum argument and exact Fourier specialization
are canonical in [L531](../../lemmas/L531-conditional-common-signal-continuation-audit.md).
The partial reasoning above is retained as the interruption checkpoint.
