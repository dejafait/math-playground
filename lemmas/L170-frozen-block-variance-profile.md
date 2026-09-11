# Lemma 170: frozen block variance profile

**Hypotheses.** Use the frozen sums S_j⁰, squares Q_j⁰, equal blocks
B_j, midpoints c_j, and normalized block averages E_j of L169.
Thus N=sqrt(T/(2π)), I consists of the integers in [N,2N],
J=ceil(T/H), h=T/J, and 1≤H≤T. Put u_j=c_j/T and
c₀=exp(π²/16). Define, for 1≤u≤2,

V(u)=c₀²(2π)^(3/2) ∫_1^2 x^(−4)
                  exp(−2(log x−(log u)/2)²) dx.

**Conclusion.** Uniformly over all blocks,

E_j Q_j⁰ = V(u_j) + O(T^(−1/2)+sqrt(T)log T/h).           (1)

In particular at H=T^(3/4) the error is O(T^(−1/4)log T).
The function V is positive, continuously differentiable, and nonconstant;
indeed V'(1)>0. There is a constant δ>0 such that, for all sufficiently
large T at this scale and every real m_T,

max_j |E_j Q_j⁰−m_T| ≥ δ.                               (2)

Consequently the laws of Q_j⁰ under uniform block sampling cannot all
approach a common law in a manner preserving their first moments
uniformly in j. This conclusion does not rule out common weak limits
without uniform integrability, or common values of a particular bounded
cutoff expectation.

**Proof.**

The exact amplitudes in L156 (specializing its window to [1,2]) are

A_n(c_j)=c₀ T^(3/4)n^(−2)
         exp(−(log(n/N)−(log u_j)/2)²).

Expanding the finite square, the diagonal is D_j=Σ A_n(c_j)².
For m≠n, direct integration gives

|E_j exp(i(t−π/2)log(m/n))| ≤ 2/(h|log(m/n)|).

The amplitude bound A_n(c_j)≤CT^(−1/4) and the ordered
frequency sum in L156 therefore bound the total off diagonal by

C T^(−1/2) N²log(2N)/h ≤ C sqrt(T)log T/h.               (3)

The estimate includes both endpoints and is independent of c_j;
no distributional equidistribution assertion is involved.

Set g_u(x)=x^(−4)exp(−2(log x−(log u)/2)²) on [1,2].
Both g_u and its x derivative are bounded uniformly on the compact
rectangle [1,2]². Comparison on mesh cells of width 1/N yields

Σ_(N≤n≤2N) g_u(n/N)=N ∫_1^2 g_u(x)dx+O(1),             (4)

uniformly in u. For clarity, on each complete cell the difference
between its integral and its sampled value times 1/N is at most
sup|∂_x g_u|/N². There are O(N) cells, and the two incomplete
boundary cells and any endpoint sample contribute O(1/N) to the
normalized sum. Multiplication by N proves (4), regardless of
whether N or 2N is an integer.

Now

D_j=c₀² T^(3/2)N^(−4) Σ_(N≤n≤2N) g_(u_j)(n/N)
   =V(u_j)+O(T^(−1/2)),

since T^(3/2)N^(−3)=(2π)^(3/2) and
T^(3/2)N^(−4)=O(T^(−1/2)). Combining this with (3) proves (1).
At the stated scale H/2≤h≤H, giving its claimed specialization.

Positivity follows from the positive integrand. Differentiation under
the integral is justified by continuity of the integrand and its
u derivative on a compact rectangle, and gives

V'(u)=(2c₀²(2π)^(3/2)/u) ∫_1^2
                  (log x−(log u)/2)g_u(x)dx.

At u=1 the integrand is positive for every x>1, so V'(1)>0.
Continuity of V' supplies two fixed interior points 1<u_a<u_b<2
with d=V(u_b)−V(u_a)>0. The midpoint grid has mesh 1/J→0.
Choose blocks with midpoints divided by T tending to u_a and u_b.
Uniformity in (1) and continuity of V show that their mean difference
tends to d. It is at least d/2 eventually. For any m_T, the triangle
inequality forces one of its distances to these two means to be at
least d/4. Taking δ=d/4 proves (2).

More explicitly, let μ_(T,j) be the probability law of Q_j⁰ obtained
by normalized Lebesgue measure on B_j. There cannot be probability
laws ν_T on [0,∞) with finite first moments such that

sup_j |∫q dμ_(T,j)(q)−∫q dν_T(q)| → 0,

by (2). This includes uniform approximation in the distance defined
as the infimum of E|X−Y| over couplings of the two laws: every coupling
bounds the difference of the means by E|X−Y|.

There is also no single common weak limit for the two selected block
sequences if their first moments are uniformly integrable. Indeed,
for R>0 the bounded continuous function min(q,R) passes to the weak
limit. Uniform integrability bounds the omitted first moment by
∫_(q>R)q dμ, uniformly along each sequence, tending to zero as
R→∞. Monotone convergence for the limit law then shows that both
mean limits must equal its first moment, contradicting their distinct
values V(u_a) and V(u_b). Uniform integrability is not established
by the present mean-square calculation. ∎

## Scope, verification, and formalization obligations

This is the second moment of the complex frozen sum, equivalently the
first moment of its nonnegative square. The fixed window [N,2N] is
essential to the displayed profile; the whole Gaussian series has a
different integral range. Nonconstant variance invalidates a common law
with uniformly accurate first moments. It does not evaluate
E_j χ''(Q_j⁰/M), prove nonzero cutoff covariance, or exclude weak-limit
agreement through escaping first-moment mass. The signed correlation,
the tail target, and RH remain unproved.

Verification is analytic: finite square expansion, both endpoint terms,
ordered frequency sum, compact mesh error including integer endpoints,
the power of 2π, differentiation sign, and the two selected midpoint
limits. No numerical certificate is needed. Formalization would require
these uniform estimates, the derivative formula, and the elementary
truncation argument for weak convergence with uniform integrability.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
