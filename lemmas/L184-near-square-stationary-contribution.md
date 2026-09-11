# Lemma 184: near-square stationary contribution

**Hypotheses.** Use L182's block, bounded real weights w, integer product
weights W(k), kernel K_2 and exact coordinates z±(k). Thus h≍N^(3/2),
a±≍N², and a+−a−=h/(2π). Let 0<rho≤N^(−1/2), for sufficiently
large real N, and define

Q_rho={k integer: a−²≤k≤a+², 0<|sqrt(k)−m|≤rho
                         for some integer m}.

There is a unique such m=m(k), since rho<1/2. Put d_k=sqrt(k)−m(k),
and retain the original endpoints in

C_k=∫_(z−(k))^(z+(k)) cos(z²) dz,
G_k=∫_(z−(k))^(z+(k)) sin(z²) dz.

Define A_rho=N^(−2) Σ_(n∈I⁴: product(n)∈Q_rho)
w(n)K_2(log(product(n)/N⁴)). Constants may depend on the fixed
profiles, comparison constants and epsilon, but not on rho or N.

**Conclusion.** For every epsilon>0, the absolute contribution satisfies

N^(−2) Σ_(n∈I⁴: product(n)∈Q_rho)
 |w(n)K_2(log(product(n)/N⁴))|
 ≤ C_epsilon N^(−1+epsilon)(1+N²rho).                         (1)

Its exact real projection, up to the kernel approximation error, is

Re A_rho=(N²h)^(−1) Σ_(k∈Q_rho) W(k)sqrt(2π sqrt(k))
 [cos(4πd_k)G_k−sin(4πd_k)C_k]
 + O_epsilon(N^(−2+epsilon)(1+N²rho)).                        (2)

In particular for rho=N^(−1/2),

Re A_rho=(N²h)^(−1) Σ_(k∈Q_rho) W(k)sqrt(2π sqrt(k))
                         [G_k−4πd_k C_k]
             + O_epsilon(N^(−1/2+epsilon)).                  (3)

The error in (3) is o(1) by choosing epsilon<1/2. Bound (1) is only
O_epsilon(N^(1/2+epsilon)) at this width and does not establish decay.
For every fixed kappa>0 the narrower nonsquare window
rho=N^(−1−kappa) does satisfy A_rho=o(1) by (1).

**Proof.**

The possible m lie in [a−−rho,a++rho], even when m itself is outside
the stationary root interval. There are O(h+1)=O(h) such integers,
uniformly in rho. They are positive and O(N²). For each m the possible
integer products lie in [(m−rho)²,(m+rho)²], an interval of length
4m rho=O(N²rho). A closed interval of length L contains at most L+1
integers. Intersecting with the stationary interval and removing m²
cannot increase the count. Hence

#Q_rho≤C h(1+N²rho).                                         (4)

L183's prime-factorization argument proves d_4(k)≤C_eta k^eta
for every positive integer k, not only for squares. Here k≤C N⁴,
so eta=epsilon/4 bounds the number of ordered factorizations of each
k by C_epsilon N^epsilon. Restricting factors to I reduces the count.
Consequently both the number of relevant quadruples and their total
absolute weight are at most

C_epsilon h(1+N²rho)N^epsilon.                               (5)

L182's finite Fresnel integral is uniformly bounded, including at either
stationary endpoint, and sqrt(2π sqrt(k))≍N. Its formula therefore
gives |K_2|≤CN/h. Multiplying this by (5) and N^(−2) proves (1).
The accumulated O(1/h) kernel errors are bounded by

C_epsilon N^(−2+epsilon)(1+N²rho).                           (6)

Since m(k) is integral, the saddle factor is exactly

exp(i(4π sqrt(k)+π/2))=i exp(i4πd_k).

Also F(z−,z+)=C_k−iG_k. Thus

Re(i exp(i4πd_k)(C_k−iG_k))
                  =cos(4πd_k)G_k−sin(4πd_k)C_k.

The weights are real, so grouping the finite sums and using (6) proves
(2). Neither sign of W(k) has been changed, and neither endpoint has
been frozen or replaced by infinity.

The same finite Fresnel bound gives |C_k|+|G_k|≤C. Elementary Taylor
bounds for sine and cosine, uniformly for |d|≤rho≤1, give

|cos(4πd)G−sin(4πd)C−(G−4πd C)|≤C rho²

when |C|+|G|≤C. Combining (5) with sqrt(2π sqrt(k))≤CN
bounds the normalized sum of these Taylor errors by

C_epsilon N^(−1+epsilon)(1+N²rho)rho².                       (7)

For rho=N^(−1/2), (6) is O_epsilon(N^(−1/2+epsilon)) and
(7) has that same bound. This proves (3). At this width the separate
absolute estimates on the G term and the linear d_k C term are only
O_epsilon(N^(1/2+epsilon)) and O_epsilon(N^epsilon), respectively;
in particular the linear term cannot be absorbed into the proved o(1)
remainder by these estimates.

Finally, setting rho=N^(−1−kappa) in (1) gives
O_epsilon(N^(−1+epsilon)+N^(−kappa+epsilon)). Taking
0<epsilon<min(1,kappa) proves the narrow-window assertion. ∎

## Scope, verification, and formalization obligations

This resolves a narrower portion of the requested window and reduces
the full near-square real contribution to the signed sum in (3) with
a vanishing error. It does not bound that signed sum by o(1). In fact
Re A_rho=o(1) is equivalent to decay of that displayed normalized sum,
by (3); neither decay nor nondecay is established here. The combined
all-positive/all-negative contribution is −Re A_rho/8 as in L182.
No conclusion about the other stationary products, the full mixed moment,
first-moment decay, uniform integrability, cutoff covariance or RH follows.

Verification is analytic: the enlarged root interval prevents endpoint
omissions; the product interval has exact length 4m rho; the divisor
bound applies to nonsquares; the phase multiplication fixes the minus
sign on C_k; and (6) and (7) check both independent error scales.
No numerical or external input is required. Formalization would require
integer interval counting, the divisor estimate proved in L183, finite
sum grouping, elementary Taylor inequalities and L182's uniform kernel
and finite Fresnel estimates.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
