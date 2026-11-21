# Fixed actual-theta Gram test1695 — working checkpoint

Approved target: assessment1694's fixed full-theta measure, scaling d,
upper Cholesky similarity and quadratic residual only. Main gap:
C028b's H_d=o(d), hence actual-Xi all-degree positivity, remains unpaid.

Partial reasoning, not yet an audited result: let p_n be the monic
orthogonal polynomials for the normalized even theta measure and put
beta_n=h_n/h_(n-1), T_n=sum_(k=1)^n beta_k. The scaled monic basis is
p_j^(d)(x)=d^j p_j(x/d). Its coefficient of x^(d-2) in p_d^(d) is
-d^2*T_(d-1). Thus the expansion of Q_d has proposed quadratic residual
alpha_(d-2)=d^2*T_(d-1)-binom(d,2)*S_2, with norm-ratio contribution
|alpha_(d-2)|/(d*sqrt(beta_(d-1))). The Cholesky coordinate map is
z=S_d*c, since the monomial coefficient norm is c^T*G_d*c.

Remaining checks: identify the whole quotient-multiplication matrix,
not just its characteristic polynomial; check full-cost equality;
prove T_n->infinity using only finite moments and unbounded support.
A bounded-recurrence contradiction via ||x*f||<=2*sqrt(M)||f|| on
polynomials appears to avoid any density/uniqueness assumption. Then
beta_n<=T_n would force the retained contribution divided by d to
diverge. No individual beta_n asymptotic or numerical evidence is used.

Continue/stop test: a rigorous uniform positive linear floor stops this
metric only; an unverified map or small retained term is inconclusive.
Essential inputs: L019, C028h; C028b supplies downstream interpretation.
Known comrade/recurrence sources are reused from source-notes1694.
No new source search, parameter variation, cross-notebook input or
mathematical script is part of this step.

Completed: the full proof is canonical in
`lemmas/C028o-actual-theta-gram-companion-cost-floor.md`. It verifies
the map and exact full cost, proves the support implication by finite
polynomial norm estimates, and obtains K_d^theta/d->infinity. The
earlier partial reasoning above is preserved as an unfinished-work
checkpoint, not a separate proof. Independent audit remains pending.
