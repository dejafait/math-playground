# Lemma 194: positive Fresnel coefficient in the interval mass

**Hypotheses.** Use L193's Z_G, ell and exact signed weights, including
its coprimality restriction. Use L185's G_m and L182's coordinates,
with a±=s±/(2π), a+−a−=h/(2π), h≍N^(3/2), and m≍N².
Let M_in=M∩[a−,a+]. All profiles are the original bounded real profiles.

**Conclusion.** There are constants c,C>0, independent of sufficiently
large N, such that

c ≤ alpha_m=(sqrt(2πm)/N)G_m ≤ C  for every m∈M_in.       (1)

Define the finite signed sum

Y_N=Σ_(u,v,m∈M_in: gcd(m,u)=1)
       P(u)Q(v) phi(u)/u² alpha_m ell.

Then, for every epsilon>0,

Z_G=Y_N+O_epsilon(N^(3/2+epsilon)).                         (2)

Consequently Z_G=o(Nh) if and only if Y_N=o(Nh). This decay
remains **unproved**. In the special case P(u)Q(v)≥0 on every
summand, define

D_N=Σ_(u,v,m∈M_in: gcd(m,u)=1) P(u)Q(v) phi(u)/u² ell.

Then c D_N≤Y_N≤C D_N, so decay is equivalent to D_N=o(Nh).
No sign hypothesis is imposed on the actual profiles in (1)–(2).

**Proof.**

First let S(x)=∫_0^x sin(z²) dz for x≥0. Substitution t=z² gives
S(x)=(1/2)∫_0^(x²) sin(t)/sqrt(t) dt. Define positive half-period
masses

A_j=(1/2)∫_(jπ)^((j+1)π) |sin(t)|/sqrt(t) dt, j≥0.

The integrable singularity at zero causes no difficulty. Translation by
π and strict decrease of t^(−1/2) give A_j>A_(j+1)>0.
At the end of every negative half-period the cumulative integral is
(A_0−A_1)+...+(A_(2k)−A_(2k+1))≥A_0−A_1>0.
Within a positive half-period it increases, and within a negative one
it decreases to its right-endpoint value. Thus S(x)>0 for x>0.
More precisely, for x≥1,

S(x)≥c0=min(S(1),A_0−A_1)>0:                              (3)

on 1≤x²≤π use monotonicity, on π≤x²≤2π use the terminal
value A_0−A_1, and thereafter use the half-period argument.
This is a finite-interval proof and uses no infinite Fresnel evaluation.
The uniform upper bound |S(x)|≤C0 follows by integration by parts
on [1,x] using sin(z²)=−(2z)^(−1)(cos(z²))', with the remaining
integral bounded by (1/2)∫_1^∞ z^(−2) dz.

For m∈M_in the exact coordinates satisfy Z−(m)≤0≤Z+(m).
Evenness of sin(z²) therefore gives

G_m=S(|Z−(m)|)+S(Z+(m)).                                  (4)

L182's smooth coordinate formula v(x)=x sqrt(2f(x)/x²),
f(x)=(1+x)log(1+x)−x, implies uniformly in this block

|Z±(m)|≍|s±−2πm|/N,

with zero on both sides when the difference is zero. Indeed the smooth
positive quotient tends to 1 and m≍N². At least one of the two
endpoint distances |s±−2πm| is ≥h/2, so its coordinate tends
to infinity uniformly, since h/N≍N^(1/2). For large N it is ≥1.
Equations (3)–(4), positivity of the other term, and the upper bound
for S prove c0≤G_m≤2C0. Multiplying by sqrt(2πm)/N≍1
proves (1), including m exactly at a stationary endpoint.

The complement M\M_in contains O(1) integers, because M extends
the real interval by only rho=N^(−1/2) at each end. L185 bounds
|alpha_m| uniformly there too. For each such m, L192's two-cell
argument, ell≤2R, phi(u)/u≤1, u≥N², and the pair-weight
bounds used in L193 give

Σ_(u,v: gcd(m,u)=1) |P(u)Q(v)| phi(u)/u² |alpha_m| ell
 ≤ C_epsilon R N^(−2+epsilon) Σ_u |P(u)|
 = O_epsilon(R N^epsilon).

This is a nonnegative majorant only; the exact sum retains coprimality
and all signs. Since R=O(N^(3/2)), it proves (2). Divide by
Nh≍N^(5/2) and choose epsilon<1 for the equivalence. Under
the additional nonnegative-product hypothesis every remaining factor
in D_N is nonnegative, so termwise use of (1) proves the comparison.
For signed profiles this comparison is not asserted. ∎

## Qualifications, verification

The coefficient G supplies no sign oscillation on the interior m interval.
For signed profiles cancellation may still come from P,Q and their
arithmetic selection. For nonnegative products the required estimate is
a positive mass bound; neither a lower bound contradicting decay nor an
upper bound proving decay has been established here. Nonzero additive
frequencies, other gcd sectors and RH remain unresolved.

Verification is analytic: decreasing half-period masses, integration by
parts, smooth coordinate comparability, endpoint separation, and the
finite absolute exterior bound. No numerical Fresnel sign test is used
as evidence.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
