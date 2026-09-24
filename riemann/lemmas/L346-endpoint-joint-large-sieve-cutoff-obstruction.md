# Lemma 346: a cutoff obstruction for the unweighted joint endpoint large sieve

**Hypotheses.** Use L332's absolutely convergent grouped expansion

R_r(a)=S_r(a)/|ζ(1+1/r+ia)|²−1
      =Σ_((p,q)=1)b_r(p,q)exp(ia log(q/p)),
c_r(m,n)=(mn)^(−1−1/r)H_r(m,n),
b_r(p,q)=Σ_(d≥1)c_r(dp,dq),
|H_r(m,n)|≤(e+1)τ(m)τ(n).

Here r≥2, τ is the divisor function, and S_r is the endpoint sum
in L332. For integer N≥1 put

a_n=sqrt(4π²exp(8n)−25),
D_N=(1/N)Σ_(n=N)^(2N−1)|R_(2n)(a_n)|².

For an integer cutoff Q≥2, retain m,n≤Q before grouping:

F_Q={(p,q): 1≤p,q≤Q, gcd(p,q)=1, p≠q},
ω_(p,q)=log(q/p),
b_(r,Q)(p,q)=Σ_(1≤d≤Q/max(p,q))c_r(dp,dq),
v_(r,Q)=(b_(r,Q)(p,q))_((p,q)∈F_Q).

Thus the constant frequency is excluded from v and may be handled
exactly. The specified absolute tail budget is

E_(r,Q)=(e+1)Σ_(max(m,n)>Q,m≠n)
             τ(m)τ(n)/(mn)^(1+1/r).                    (1)

For a nonempty consecutive sample interval I⊆{N,…,2N−1}, let
L(I,Q) be the optimal unweighted squared sampling norm:

L(I,Q)=sup_(z≠0)
 [Σ_(n∈I)|Σ_(ν∈F_Q)z_ν exp(ia_nω_ν)|²]/Σ_(ν∈F_Q)|z_ν|².

The certificate tested here uses this coefficient-independent
operator on the full F_Q, exact vector Abel summation for moving
v_(2n,Q), and absolute triangle bounds for the tail and for joining
the Abel terms. A partition into consecutive intervals is allowed,
with a separate Q on each interval. It does not use an adapted
frequency weight, a smaller support chosen from the actual
coefficients, or cancellations between the resulting norm bounds.
Using the optimal L makes the test stronger than substituting any
particular large-sieve upper estimate.

**Conclusion.** Uniformly for 2N≤r<4N and Q≥2,

(e+1)r(Q+1)^(−1/r)≤E_(r,Q)
 ≤K N^4 Q^(−1/(8N)).                                   (2)

In particular Q=(N+1)^(64N) gives E_(r,Q)=O(N^(−4)).
Nevertheless, for every I and Q≥exp(16N), eventually,

L(I,Q)≥c |I| Q exp(−8N),
||v_(r,Q)||_2≥c/N,                                     (3)

with positive absolute constants. At the displayed sufficient
cutoff the coefficient norm is also O(1/N), so (3) is not a claim
that the actual coefficient vector has large unweighted energy.

The fully specified certificate (9) below for D_N tends to infinity
uniformly over all cutoffs and all such partitions. It therefore
cannot reach D_N=o(1), or the fixed sufficient threshold 1/4.
The obstruction persists with the constant frequency removed and
with the actual exponentially increasing sample gaps retained.

This is a lower bound on this upper-bound certificate, not on D_N,
on its off-diagonal sum, or on a sample value of R. No endpoint
margin, Laguerre sign, or zero-exclusion range is extended.

**Proof.** The finite rectangular truncation and then the unique
reduced-ratio grouping retain all equal frequencies in that
rectangle. Absolute convergence of L332's full expansion gives

R_r(a)=b_r(1,1)+Σ_(ν∈F_Q)b_(r,Q)(ν)exp(iaω_ν)+ε_(r,Q)(a),
|ε_(r,Q)(a)|≤E_(r,Q),                                  (4)

uniformly in real a. Here the diagonal is retained in full, and
the error consists only of pairs m≠n outside the rectangle. Thus
no diagonal cancellation is required of the tested operator.

For the lower bound in (2), retain m>Q,n=1 in the positive
majorant (1), use τ(m)≥1, and integrate the decreasing function
x^(−1−1/r) on [Q+1,∞). For the upper bound, overcount the
two possible escaping indices. With σ=1+1/r,

Σ_(m>Q)τ(m)m^(−σ)
 ≤Q^(−1/(2r))Σ_(m≥1)τ(m)m^(−1−1/(2r))
 =Q^(−1/(2r))ζ(1+1/(2r))².

Ordered-divisor counting gives the identity; its sums are
nonnegative. The decreasing integral estimate ζ(1+u)≤1+1/u
then bounds E_(r,Q) by

2(e+1)(r+1)²(2r+1)² Q^(−1/(2r)).

This proves (2) and the sufficient-cutoff assertion. The lower
bound in (2) is a bound on the chosen positive majorant, not on
the actual truncation error in (4).

We next use the actual sample locations in a joint operator test.
Rationalizing the square root, or its convergent expansion, gives

a_n=2πexp(4n)+O(exp(−4n)),
a_(n+1)−a_n=2π(exp(4)−1)exp(4n)+O(exp(−4n)).           (5)

Thus their smallest gap is comparable to exp(4N), while all
heights and their total span are bounded above by
T_N=2πexp(8N). We will not replace these samples by an arithmetic
progression or infer equidistribution from their large gaps.

Let j_0=ceil(Q/2), M=floor(Q/(16T_N)), and take the M+1 ratios
(j_0+j)/Q, 0≤j≤M. For the large cutoffs in (3) they are all
strictly between zero and one. Reducing each fraction leaves
distinct members of F_Q; coprimality of its unreduced numerator
and Q is unnecessary. Their frequencies ω_j satisfy

0≤ω_j−ω_0=log((j_0+j)/j_0)≤2M/Q≤1/(8T_N).

They cluster near −log 2, not near zero. For I=[u,v], choose
z_ν=exp(−ia_uω_ν)/sqrt(M+1) on this cluster and zero elsewhere.
Its norm is one. At every n∈I, remove the common phase at ω_0;
each remaining angle lies in [0,1/8], by the actual span bound.
The real part is therefore at least sqrt(M+1)cos(1/8). Since
cos²(1/8)>1/2 and M+1≥Q/(16T_N),

L(I,Q)≥|I|(M+1)/2≥|I|Q/(32T_N).                       (6)

This proves the first assertion in (3). The test vector need
not equal the actual reciprocal coefficient vector: that is
precisely why it constrains a coefficient-independent operator
norm, and does not give a lower bound on the actual sampled sum.

For the second assertion in (3) it is useful to check a nonzero
frequency, so that separating the constant term cannot avoid the
comparison. L332 proves, for every fixed reduced pair,

b_r(p,q)=β(p,q)/r+O_(p,q)(r^(−2)).

Its finite-divisor formula, with δ_m=1 for m=1 and zero otherwise,
Λ the prime-power logarithm and A(m)=Σ_(j|m)μ(m/j)(log j)², is

U(m,n)=Λ(m)δ_n+δ_mΛ(n)
       −[A(m)δ_n+δ_mA(n)+2Λ(m)Λ(n)]/8,
β(p,q)=(1/(pq))Σ_(d≥1)U(dp,dq)/d².

For (p,q)=(2,1), the d=1 term is log 2−(log 2)²/8.
For d>1 both deltas vanish. The product Λ(2d)Λ(d) is nonzero
exactly when d is a positive power of two, and then equals
(log 2)². Summing Σ_(k≥1)2^(−2k)=1/3 yields

β(2,1)=(log 2)/2−5(log 2)²/48>0.                       (7)

Positivity follows already from 0<log 2<1. This uses the full
ratio grouping, not only the d=1 coefficient.

The elementary bound τ(d)≤C d^(1/8), proved in L332, and
τ(2d)≤2τ(d) bound the missing part of this grouped coefficient by

|b_r(2,1)−b_(r,Q)(2,1)|
 ≤K Σ_(d>Q/2)τ(d)²/d²≤K Q^(−3/4),                     (8)

uniformly in r≥2. For Q≥exp(16N), (7), (8) and 2N≤r<4N
give |b_(r,Q)(2,1)|≥β(2,1)/(2r)≥β(2,1)/(8N), eventually.
This proves the norm lower bound. At Q=(N+1)^(64N), (2)
also bounds the ℓ² norm of the difference between the truncated
and full nonconstant grouped vectors by O(N^(−4)). L332's
identity Σ|b_r|²=C/r²+O(r^(−3)) therefore proves the asserted
O(1/N) upper bound there.

We now specify and check the complete moving-weight certificate.
For I=[u,v] and its chosen cutoff Q write v_n=v_(2n,Q),
d_n=b_(2n)(1,1), and

B_I=√L(I,Q)||v_v||_2
    +Σ_(t=u)^(v−1)√L([u,t],Q)||v_t−v_(t+1)||_2,
U_N=(1/N)Σ_(I in the partition)
       ( ||(d_n)_(n∈I)||_2+B_I+||(E_(2n,Q))_(n∈I)||_2 )².    (9)

Then D_N≤U_N. Indeed v_n=v_v+Σ_(t=n)^(v−1)(v_t−v_(t+1)).
Evaluate each vector at its sample height. The first term uses
the operator on I, while the t term is supported on [u,t].
The triangle inequality in the finite sample ℓ² space gives
B_I exactly. Apply (4) and its tail budget to obtain (9),
then sum the squared bounds over the disjoint intervals.
This is finite vector Abel summation; no freezing, differentiation
in r, or limiting exchange has occurred. Any larger valid
large-sieve constants only increase this budget.

There are now two cases on every nonempty I, uniformly over the
partition. If Q<exp(16N), then log(Q+1)/r≤9 for 2N≤r<4N and
large N. The lower bound in (2) gives E_(r,Q)≥cN, so that
I's contribution to U_N is at least c|I|N.

If Q≥exp(16N), retain only the first nonnegative term of B_I.
Equations (3) and (9) give a contribution at least

(1/N)L(I,Q)||v_v||_2²
 ≥c (|I|/N) Q exp(−8N)/N²
 ≥c (|I|/N) exp(8N)/N².

Since Σ_I|I|=N, both cases together prove the uniform bound

U_N≥c min(N², exp(8N)/N²) → ∞.                         (10)

This includes singleton intervals and independent cutoffs on
different intervals. Optimizing the implicit constants, the
cutoff, the partition, or the exact joint sampling norm cannot
turn this specified certificate into o(1).

The obstruction uses densely clustered frequencies that have very
small individual arithmetic coefficients. A weighted sampling
norm or a coefficient-sensitive decomposition could suppress
their effect; (6) does not apply unchanged to such a norm. Nor
does (10) rule out a smaller signed tail error than (1). It stops
only the full-support unweighted operator plus the stated
absolute-tail and vector-Abel certificate. No negative sample,
failure of D_N=o(1), or RH candidate has been obtained. ∎

**Mathlib.** Full statement: not checked. Coverage of the finite
sampling-operator lower bound, exact grouped coefficient (7),
tail tradeoff and moving-vector certificate is not checked;
all needed arguments are proved above. L332 retains the supporting
results recorded as present through L001:
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
and [`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
Those links were not rechecked. They support the reciprocal
expansion and denominator; none matches the present conclusion.
No external large-sieve theorem is needed: the optimal finite
operator constant is defined here and tested directly. No full
library match or absence from checked sources is asserted.
