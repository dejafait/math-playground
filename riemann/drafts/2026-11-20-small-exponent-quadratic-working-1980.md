# Approved norm attempt1980 — saved reasoning

2026-11-20. Scope is exactly assessment1978's full-line bound for
t_d=f_d/d. This note preserves the attempt before the full proof is
written; it does not assert an audited conclusion.

Candidate argument: write t_d as the equal-weight average of the
single-root logarithms g_alpha(y)=log|y-alpha|-log|y|. The function
Phi(t)=t^2 exp(|t|/4) is convex. Scale a nonzero alpha to unit modulus
and split the real line at |x|=1/2 and |x|=2. The origin and the possible
real root each require an integrable power -1/4 with a logarithm squared;
the exterior needs a uniform O(x^(-2)) bound for Phi(g). The middle
interval can be dominated in terms of |x-Re(alpha/|alpha|)|, so no
lower bound on the imaginary part is needed.

The resulting norm would be at most a universal constant times
d^(-1) sum |alpha_j|. C028b's inversion and C028d's real shift reduce
this to b_1+sum_(U_d(u)=0) 1/|u|. Choose a common small r_0 with
F(r_0)-1<=1/2; C028f's coefficient multipliers give |U_d-1|<=1/2
on that disk for every d. Its closed count at 1 and strict tail at 1
then pay the entire reciprocal sum, with all boundary multiplicities.

Remaining writing checks: explicit uniform middle-interval envelope,
finite constants for all three regions, alpha=0, arbitrary collisions,
and finite-sum integration. No signed-mean estimate follows. Success
is local reproduction of known methods, not a solution of RH.

Completion: the estimates were written out in
[C029i](../lemmas/C029i-actual-quotient-uniform-exponential-quadratic-norm.md).
The canonical proof achieves the approved bound; a separate audit remains
pending. This saved outline is retained as the unfinished-work checkpoint.
