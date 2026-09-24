# Lemma 148: correction mass and leading-sum threshold

**Hypotheses.** Use S, S_1, F, H and q_1 from L147 and N=sqrt(t/(2π)), c₀=exp(π²/16) from L139, with real t>0. Set a=π/4 and

Q(y)=5(−a+iy)−i((−a+iy)²+1/2),
C₁=c₀∫_R exp(−y²−y)|Q(y)|dy,
V=c₀∫_R exp(−y²−2y)|Q'(y)−(2y+2)Q(y)|dy,
B=sqrt(2π)C₁.

**Conclusion.** Both constants are finite and C₁>0. The absolute term mass M₁(t) of S_1 satisfies

|M₁(t)−C₁/N|≤V/N².                                      (1)

In particular, |S_1(t)|≤M₁(t)=O(t^(−1/2)). There is a constant K≥0 such that, for all sufficiently large t,

|F(−1,t+3i/2)/H(t)−S(t)|≤B t^(−3/2)+K t^(−2).            (2)

Consequently a hypothetical uniform lower bound |S(t)|≥d t^(−δ), d>0, suffices to give q_1(t+3i/2)≥c t^(−δ) if δ<3/2. L139 excludes δ<1/2, so the nonexcluded power range for this sufficient condition is 1/2≤δ<3/2. At δ=3/2, d>B also suffices. No such lower bound is proved.

More generally, if a positive lower-bound function L(t) satisfies

liminf_(t→∞) L(t)/(B t^(−3/2)+K t^(−2))>1,

then |S(t)|≥L(t) implies q_1(t+3i/2)≥c L(t) eventually. At the power endpoint d≤B, or for δ>3/2, a bound d t^(−δ) alone does not dominate the error envelope (2). This is a limitation of these absolute estimates, not a necessary threshold for the actual oscillatory correction.

**Proof.**

L139's modulus calculation, with the multiplier in L147, gives

M₁(t)=c₀ Σ_(n≥1) n^(−2)exp(−(log(n/N))²)|Q(log(n/N))|.

Consider the complex profile

h_N(x)=c₀ x^(−2)exp(−(log(x/N))²)Q(log(x/N)), x>0.

Extend it by zero at x=0. A Gaussian times any fixed polynomial decays faster than every exponential at either end in y=log(x/N); thus this extension is continuously differentiable and the following integrals converge. Substitution x=N exp(y) gives

∫₀^∞ |h_N(x)|dx=C₁/N,
∫₀^∞ |h_N'(x)|dx=V/N².

For the second equality differentiate h_N(x)=c₀N^(−2)exp(−y²−2y)Q(y) and use dy=dx/x. Finiteness follows because Q and Q' are polynomials. Since Q(0)=−5a−i(a²+1/2) is nonzero, continuity proves C₁>0.

On each interval [n−1,n], the fundamental theorem of calculus and the modulus inequality give

||h_N(n)|−∫_(n−1)^n |h_N(x)|dx|
 ≤∫_(n−1)^n |h_N(n)−h_N(x)|dx
 ≤∫_(n−1)^n |h_N'(u)|du.

Summing finitely and then passing to infinity proves both absolute convergence and (1). This is the quadrature argument of L139, applied to a complex profile so no differentiability of its modulus at a zero is needed.

Since 1/N=sqrt(2π)t^(−1/2), (1) gives

M₁(t)/t≤B t^(−3/2)+2πV t^(−2).

L147 provides F/H=S+S_1/t+E₂ with |E₂|≤K₂t^(−2), eventually. The triangle inequality proves (2) with K=2πV+K₂.

Also, as recorded in L147, D(t)=A_1(t+3i/2)/|H(t)| is bounded above by a fixed positive constant C_D, and q_1=|F/H|/D. Hence

q_1(t+3i/2)≥[|S(t)|−B t^(−3/2)−K t^(−2)]/C_D.

For δ<3/2 the error divided by d t^(−δ) tends to zero, giving the claimed lower bound with c=d/(2C_D) eventually. If δ=3/2 and d>B, use K t^(−1/2)≤(d−B)/2 to obtain c=(d−B)/(2C_D). The general liminf condition gives a fixed positive relative margin in exactly the same inequality.

Finally, the error envelope divided by d t^(−δ) tends to B/d at δ=3/2 and to infinity at δ>3/2. Therefore the stated smaller endpoint constants or larger exponents provide no positive relative margin by this estimate alone. No assertion is made that S_1 attains its absolute mass or cancels S. ∎

## Scope and verification

The correction mass is on the same scale as L139's leading absolute mass; division by t supplies the extra power. Its finite positive integral constant was not numerically approximated. Analytic verification consists of the exact modulus identity, differentiated complex profile, integrable Gaussian majorants, quadrature error, conversion between N and t, and reverse triangle inequality. The center lower bound, common heat-interval strip, and RH remain unresolved.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
