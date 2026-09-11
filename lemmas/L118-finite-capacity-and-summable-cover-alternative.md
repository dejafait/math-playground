# Lemma 118: finite capacity and summable cover alternative

**Hypotheses and definitions.** Let m_l be positive integers, l≥1,
with W=Σ_l m_l/l²<∞. For 1≤k≤n define

A_kn=Σ_(l>n) m_l/(l−k)²,

and put A_kn=0 for k>n. For N≥1 let

C_N=max{Σ_(n=1)^N d_n : d_n≥0,
                         Σ_(n=k)^N A_kn d_n≤1 for 1≤k≤N}.

These programs include the entire destination tail l>n, even when l>N.
A summable cover means a sequence y_k≥0 with Σ_k y_k<∞ and

Σ_(k=1)^n y_k A_kn≥1 for every n≥1.

**Conclusion.** Exactly one of the following alternatives holds:

- C_N tends to infinity, and there exists d_n≥0 with Σ_n d_n=∞
  and sup_k Σ_(l>k) m_l(Σ_(n=k)^(l−1) d_n)/(l−k)²≤1.
- The C_N are bounded, and a summable cover exists. Every nonnegative
  increment sequence with generator at most one then has total mass
  at most Σ_k y_k for any such cover.

In the second alternative the minimum cover mass equals lim_N C_N.
The first alternative is equivalent to existence of a positive strictly
increasing unbounded payoff F with Σ_l m_l F(l)/l²<∞ and bounded
Q_m F(k)=Σ_(l>k) m_l(F(l)−F(k))/(l−k)².
This is an alternative for each fixed sequence, not a determination of
which alternative holds for all sequences satisfying the hypotheses.

## Proof

For fixed k, the finitely many terms with k<l<2k are finite and the
remaining terms are bounded by 4m_l/l². Thus every A_kn is finite.
Also A_nn≥m_(n+1)≥1. Each feasible d_n lies in [0,1/A_nn], so
the finite feasible set is nonempty and compact and its maximum exists.
Extending a feasible vector by zero proves C_(N+1)≥C_N: the new row
has value zero and all previous coefficients are unchanged.

Tonelli's theorem for nonnegative series gives the exact identity

Σ_(l>k) m_l(Σ_(n=k)^(l−1) d_n)/(l−k)²
 =Σ_(n≥k) A_kn d_n.                                      (1)

This identity is valid also when either side is infinite. In particular,
a finite feasible vector extended by zero is feasible for all rows.
If an infinite feasible vector has infinite total mass, its truncations
show C_N≥Σ_(n≤N)d_n→∞.

Conversely suppose the capacities are unbounded. For each j≥1 choose
a finite feasible vector v^(j), extended by zero, with total mass at
least 2^j. Put d_n=Σ_(j≥1)2^(−j)v_n^(j). Coordinate finiteness follows
from v_n^(j)≤1/A_nn. Nonnegative interchange shows that every row
of d is at most Σ_j 2^(−j)=1. Another nonnegative interchange gives
Σ_n d_n≥Σ_j 1=∞. Thus mixing finite solutions produces the required
infinite solution without relying on preservation of mass in a limit.

For the second alternative use the standard finite-dimensional linear
programming strong duality theorem: the dual of the displayed maximization
program is

min{Σ_(k=1)^N y_k : y_k≥0,
                     Σ_(k=1)^n y_k A_kn≥1 for 1≤n≤N}.    (2)

The primal is feasible with finite optimum; the dual is also feasible,
for example y_k=1 for 1≤k≤N, using A_nn≥1. Strong duality therefore
applies and both optima are attained with common value C_N.

If C=lim_N C_N<∞, choose optimal vectors y^(N) in (2), extended
by zero. Each coordinate lies in [0,C]. Successive subsequence extraction
and the diagonal procedure give a subsequence with N tending to infinity
that converges at every fixed coordinate to y_k≥0. For every J,
Σ_(k≤J)y_k≤C, so Σ_k y_k≤C. For a fixed column n, its inequality
contains only k≤n, with finite coefficients. Taking the limit therefore
gives Σ_(k≤n)y_k A_kn≥1. This proves existence of a summable cover.

Conversely, for any cover y and any infinite feasible d, Tonelli gives

Σ_n d_n ≤Σ_n d_n Σ_(k≤n)y_k A_kn
        =Σ_k y_k Σ_(n≥k)A_kn d_n ≤Σ_k y_k.                (3)

The same applies to each finite feasible vector, so C_N≤Σ_k y_k.
The constructed cover consequently has mass exactly C and is optimal.
Equation (3) also makes the alternatives mutually exclusive.

Finally, given the infinite solution d from the first alternative, set
F_0(k)=1+Σ_(n<k)d_n. It is finite, positive, nondecreasing and unbounded.
By (1), Q_m F_0≤1. The first row already provides integrability:

Σ_l m_l F_0(l)/l²
 ≤W+Σ_(l≥2) m_l(F_0(l)−1)/(l−1)²≤W+1.

For strict increase add B(k)=1−1/(k+1). The bounded-correction estimate
proved in Lemma 117 gives Q_m B≤W and Σ_l m_l B(l)/l²≤W.
Thus F=F_0+B meets all payoff requirements. Conversely any such F has
increments d_n=F(n+1)−F(n)>0 of infinite total mass. Its generator bound
K is positive (the k=1,l=2 term is positive); division by K yields a
feasible infinite increment sequence with infinite mass. This proves the
last equivalence. ∎

## Qualifications and verification

This proof does not show that the capacities diverge under weighted
summability. It replaces that unresolved assertion by exclusion of all
summable covers. It proves neither unrestricted nonexplosion nor RH.
The coefficients are exact infinite series; finite numerical tail
truncation alone cannot certify their upper bounds or primal feasibility.
No numerical certificate is needed for this analytic alternative.

The audit checks full-tail finiteness, the last diagonal coefficient
A_NN (which would be lost by destination truncation), zero extension,
coordinate bounds for the mixture, finite-column passage to the limit,
Tonelli in both directions, and the first-row integrability estimate.
Formalization would require nonnegative series interchange, compact finite
optimization, finite linear-programming strong duality, diagonal subsequence
extraction, and the correction estimate. The finite duality theorem is a
standard named input; no infinite-dimensional duality is assumed.
