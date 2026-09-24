# Lemma 258: a Cauchy bound for the first negative Laguerre witness

**Hypotheses.** Let F be a nonzero entire function real on the real axis. Suppose F(a+ib)=0 for real a,b with b≠0. Write

H(y)=F(a+iy)F(a−iy)=Σ_(n≥0) D_n(F;a)y^(2n).

Choose R>|b| and a finite M with |H(y)|≤M on the complex circle |y|=R. Let m be the order of vanishing of F at a, including m=0 when F(a)≠0. Put

c=(F^(m)(a)/m!)²>0, q=b²/R²∈(0,1), B=M/R^(2m),
N=ceil(log(B/[c(1−q)])/log(1/q)).

**Conclusion.** The integer N is at least 1. There is an integer j with 1≤j≤N for which

D_(m+j)(F;a)b^(2j)≤−c(1−q)/N<0.

In particular, if F(a)≠0, a negative Laguerre coefficient occurs at an index 1≤n≤N with c=F(a)² and B=M. This is a conditional quantitative witness from a specified nonreal zero, not an assertion that such a zero exists for Ξ.

**Proof.** The function H is entire and even. Conjugation symmetry of F gives real Taylor coefficients for H. If F(a+z)=u z^m+O(z^(m+1)), with real nonzero u=F^(m)(a)/m!, then

H(y)=u²y^(2m)+O(y^(2m+2)),

since i^m(−i)^m=1 and H is even. Consequently Q(y)=H(y)/y^(2m), with its removable value Q(0)=c, is even entire and has expansion

Q(y)=Σ_(j≥0) d_j y^(2j), d_j=D_(m+j)(F;a), d_0=c.

On |y|=R its modulus is at most B. The Cauchy coefficient estimate gives |d_j|≤B/R^(2j). In particular B≥c, so B/[c(1−q)]>1 and N≥1. At the real nonzero point y=b, the assumed zero gives Q(b)=0. Absolute convergence and the coefficient estimate yield

|Σ_(j>N) d_j b^(2j)|≤B q^(N+1)/(1−q).

By the definition of N and log(1/q)>0,

q^N≤c(1−q)/B,

so the last tail is at most cq<c. Therefore

Σ_(j=1)^N d_j b^(2j)=−c−Σ_(j>N)d_j b^(2j)≤−c(1−q).

At least one of the N real summands is at most their average bound −c(1−q)/N. This proves both the sign and its quantitative margin. All evaluations use absolutely convergent entire Taylor series inside the chosen circle; no positivity or zero-location theorem is assumed. ∎

The multiplicity clause is essential for comparison with L257: a real zero at the same center makes F(a)² vanish and invalidates an argument that divides by it. Deflation repairs the estimate, but the witness bound then begins after m. There is no contradiction with arbitrarily many masked initial levels. Even for m=0 the bound depends on the ratio M/F(a)² and on |b|/R; no uniform finite index follows without further estimates.

The exact threshold furnished here is positivity through m+N at the real center of each putative nonreal zero. If those signs were established, the displayed strict negative witness would exclude that zero. For actual theta, signs are known at every level only on the compact interval in L255, whereas possible nonreal centers lie outside it. Neither positivity through the location-dependent index outside that interval nor a uniform bound on the normalized growth ratio has been established. The main mixed-positivity gap remains open.

**Mathlib.** Not checked for the full result or the supporting Cauchy coefficient estimate, removable division by a zero, and geometric-series bound. No matching or supporting theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
