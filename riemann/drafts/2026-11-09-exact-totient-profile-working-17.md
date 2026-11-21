# Exact totient profile — working checkpoint, step17

Approved target: the unchanged exact normalized cross pairing in the
step16 EXPLORE assessment. Main gap: L030–L032/C032a. No new source,
length, vector family, or signed transfer premise is being introduced.

Partial reasoning, not yet a verified result: set r=log N and
v_d=phi(d)^(-1/2). L737's column identity gives
v^T K v=sum_(n<=N) log(n)/phi(n). For the right action,
(Kv)_d/v_d=sum_(p^a<=N/d) log(p)*phi(d)/phi(dp^a).
Each summand differs from log(p)/p^a by zero if p divides d and
by log(p)/(p^a(p-1)) otherwise. The latter corrections have one
absolutely convergent bound. The previously inspected first-Mertens
theorem thus suggests ||(A-rI)v||<=C||v||, uniformly in N.
L930's finite exponential bound should propagate this to
M(2i/L)v=exp(-2ir/L)v+O(||v||/L).

The general-totient Lemma2 is applicable with beta=-1, sigma=1/2,
kappa=0, theta_p=1/(p-1), since its prime hypothesis is bounded by
the convergent sum over integers 1/(sqrt(n)(n-1)). It supplies
S(x)=sum_(d<=x)1/phi(d)=C_phi log x+O(1), with
C_phi=product_p(1+1/(p(p-1))). Moving complex exponents still
require explicit partial summation; no uniform complex theorem is
being assumed. The mean kappa correction can be bounded using
phi(pm)>=phi(p)phi(m) and sum_p log(p)/(p-1)^2<infinity.

Tentative endpoint computation: with alpha=r/L, W_- has scalar
pairing C_phi L exp(-i alpha)sin(alpha)+O(1), and W_+ has
C_phi L exp(-3i alpha)sin(alpha)+O(1). Combining their poles
before taking modulus predicts numerator
C_phi L^2 exp(-2i alpha)sin(alpha)sin(1-alpha)+O(L).
Each full energy should be C_phi L^2 alpha(1-alpha)+O(L).
This predicts rho -> sinc(1/5)sinc(4/5)<1, uniformly in X.

Remaining checks in this attempt: all finite exponential-error signs,
transpose rather than adjoint, weighted Jordan correction, lower
endpoint in partial summation, full-metric denominator error, exact
weight/phase and regular-zeta charges. If they pass, park this profile
as a saturation witness only; no operator upper bound follows. The
canonical proof will record precise source citations and qualifications.

Completion: the proof is now recorded in
../lemmas/L931-exact-totient-profile-cross-pairing.md. The listed
propagation, transpose, partial-summation, metric and endpoint errors
were supplied, yielding the proposed uniform limit with O(1/log T)
error and an eventual bound rho<=9/10. This working checkpoint is
preserved as partial reasoning, not a substitute for the canonical
proof; separate conceptual review remains pending.
