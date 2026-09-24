# Lemma 333: endpoint finite-height relative mean square

**Hypotheses.** Let r≥2, σ=1+1/r, and use the real functions from L332:

S_r(a)=Σ_(j,k≥1) (jk)^(−1/2)(1−log(jk)/(2r))_+^r exp(ia log(k/j)),
B_r(a)=|ζ(σ+ia)|²,  R_r(a)=S_r(a)/B_r(a)−1.

Let 𝓜_r denote L332's long-height mean square, and C>0 its limiting
constant, so 𝓜_r=C/r²+O(r^(−3)). For A real and T>0 put

M_r(A,T)=(1/T)∫_A^(A+T)|R_r(a)|²da.

**Conclusion.** There is an absolute K such that, uniformly in r≥2,
A∈ℝ and T>0,

|M_r(A,T)−𝓜_r|≤K(r+1)^17/T.                            (1)

In particular, as r→∞,

M_r(A,T)=C/r²+O(r^(−3))                                (2)

uniformly in A and T≥r^20. The exponent twenty is a sufficient length,
not an optimal threshold. On the prescribed sequence

r=2n,  a_n=sqrt(4π²exp(4r)−25),

(1/a_n)∫_(a_n)^(2a_n)|R_r(a)|²da=C/r²+O(r^(−3)).        (3)

For every fixed 0<η<1, the subset of either the interval in (3) or
any interval in (2) on which |R_r(a)|≥η has relative measure
O_η(r^(−2)). At every point of its complement,

S_r(a)>(1−η)B_r(a)≥(1−η)/(r+1)².                       (4)

This margin dominates E_r=(r+1)²exp(−r/256). Equations (1)–(3)
remove the iterated-height-limit restriction for these averages.
They do not put any particular a_n outside the exceptional set and
do not establish an endpoint Laguerre sign or a new zero-exclusion
range.

**Proof.** L332 supplies the absolutely convergent expansion

R_r(a)=Σ_(m,n≥1)c_r(m,n)exp(ia log(n/m)),
c_r(m,n)=(mn)^(−σ)H_r(m,n),
|H_r(m,n)|≤(e+1)τ(m)τ(n),                               (5)

where τ is the positive-divisor function. The last bound follows
there from 0≤f_r≤e and the finite Möbius divisor sums. In particular
Σ|c_r(m,n)|≤(e+1)ζ(σ)^4<∞. The coefficients are real. Every
product and grouping in the following expansion is therefore
absolutely convergent, uniformly in the real height at each fixed r.

In the product of (5) with its conjugate, write k=nu and l=mv,
where (u,v) index the conjugate factor. Define the finite divisor sum

g_r(k,l)=Σ_(n|k,m|l)c_r(m,n)c_r(k/n,l/m).

Then

|R_r(a)|²=Σ_(k,l≥1)g_r(k,l)exp(ia log(k/l)).             (6)

Let d_j(k) count ordered factorizations of k into j positive
integers. Thus τ=d_2 and τ*τ=d_4, by grouping four factors into
two pairs. The product mnuv=kl in (5) gives

|g_r(k,l)|≤(e+1)² d_4(k)d_4(l)/(kl)^σ.                  (7)

In particular Σ|g_r(k,l)|<∞. The constant-frequency contribution
in (6) is exactly Σ_k g_r(k,k)=𝓜_r: average (6) over [−H,H]
and let H→∞, using this absolute majorant and L332's definition
of 𝓜_r. This retains every equal-ratio collision. The individual
g_r(k,k) need not be nonnegative, and we do not replace their sum
by its absolute majorant.

For k≠l, direct integration gives

|(1/T)∫_A^(A+T)exp(ia log(k/l))da|
 ≤2/(T|log(k/l)|).                                     (8)

We now prove that the sum of (7) times this bound is finite with
the required uniform control. Put x_k=d_4(k)k^(−σ). The needed sum,
apart from the absolute constant and 1/T, is

Q_σ=Σ_(k≠l)x_k x_l/|log(k/l)|.                          (9)

For l≥2k or k≥2l the denominator is at least log 2. These pairs
contribute at most (log 2)^(−1)(Σ_k x_k)², which equals
(log 2)^(−1)ζ(σ)^8.

For k<l<2k,

log(l/k)≥(l−k)/(2k),  2x_kx_l≤x_k²+x_l².

Consequently their contribution is at most

Σ_(k<l<2k) k(x_k²+x_l²)/(l−k)
 ≤K₀ Σ_k k x_k² log(2k).                               (10)

For the x_k² part, fix k and sum 1/(l−k) up to k−1. For the
x_l² part, fix l, use k≤l, and sum 1/(l−k) up to l−1. Each
harmonic sum is at most 1+log of its upper index. This proves
(10) first for finite nonnegative sums and then by monotone
convergence. The reversed ordered pairs satisfy the same bound.

We need an elementary divisor estimate that is uniform as σ↓1:

d_4(k)²≤d_16(k).                                       (11)

At a prime power p^v the left side counts pairs of nonnegative
four-component integer vectors, both summing to v. Every such pair
is the row-sum and column-sum pair of a nonnegative integer 4×4
matrix: successively place the minimum of the remaining row and
column totals in their intersection, exhausting a row or column
at each step. Equal total sums ensure that the construction ends
with all totals exhausted. The map from these matrices onto vector
pairs is therefore surjective. The matrices have sixteen entries
summing to v, so their number is d_16(p^v). This proves (11) at
prime powers; multiplicativity proves it for every k, including 1.

Set u=2/r and s=2σ−1=1+u. Ordered-factor counting and nonnegative
summation give

Σ_k d_16(k)k^(−s)=ζ(s)^16,
Σ_k d_16(k)log k·k^(−s)=16ζ(s)^15 L(s),
L(s)=Σ_(k≥1)log k·k^(−s).                              (12)

The second identity follows by writing log(k_1⋯k_16) as the sum
of sixteen logarithms in the product series. No differentiation
on the boundary of convergence is used. For u>0 the decreasing
integral comparison yields ζ(1+u)≤1+1/u. Also

L(1+u)≤∫_1^∞log(2x)x^(−1−u)dx
       =1/u²+(log 2)/u.                                (13)

Indeed, on [k−1,k] for k≥2, one has k≤2x and k^(−1−u)≤x^(−1−u),
so its integral majorizes the kth summand. Equations (11)–(13)
prove the finite bound

Σ_k k x_k² log(2k)
 ≤(log 2)ζ(1+u)^16+16ζ(1+u)^15L(1+u)
 =O((r+1)^17).                                         (14)

The far-pair bound is O((r+1)^8), since σ−1=1/r. Combining it
with (10) and (14) proves Q_σ=O((r+1)^17), with an absolute
constant for r≥2. In particular all nonzero-frequency integrals
in (8) may be summed absolutely. Subtract the exact diagonal
𝓜_r from the integral of (6), and apply (7)–(9); this proves (1),
independently of A. No minimum gap for an infinite set of reduced
rational frequencies has been assumed.

Combining (1) with L332 gives

M_r(A,T)=C/r²+O(r^(−3))+O((r+1)^17/T).                  (15)

If T≥r^20, the final error is O(r^(−3)), proving (2). On the
prescribed sequence a_n=2πexp(2r)(1+O(exp(−4r))), so its final
error is O(r^17exp(−2r))=o(r^(−3)), proving (3). In particular
the coupled mean square has the same positive leading constant
as the iterated mean, and tends to zero.

Chebyshev's inequality on each finite interval proves the
exceptional-measure claims from (2) and (3). By L332, R_r is real
and B_r≥(r+1)^(−2). Thus |R_r|<η proves (4). Its lower bound
divided by E_r equals (1−η)exp(r/256)/(r+1)^4, tending to infinity.
This is a sufficient arithmetic margin wherever the relative error
is small. A finite exceptional-measure estimate does not exclude
an isolated prescribed height: even a continuous function can have
a narrow excursion at that height. The endpoint assembly is needed
at the paired point a_n itself, not merely almost everywhere on
its surrounding interval. The stated pointwise qualifications
therefore remain essential. ∎

The analytic verification consists of the four-index grouping, the
exact zero-frequency identification, both harmonic sums, the
prime-power counting inequality, and the convergent logarithmic
Dirichlet sums. The powers in (15) are deliberately unoptimized;
their exponential-scale comparison already meets the proposed
finite-average target. The proof does not assert a pointwise
bound, an extension of Laguerre positivity, or an RH candidate.

**Mathlib.** Full statement: not checked. Coverage of the finite
interval estimate, ordered-divisor counting inequality and its
uniform limiting regime is not checked; these arguments are proved
above. L332 retains the supporting reciprocal-series identity,
absolute convergence and nonvanishing references, recorded as
present in L001:
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
and [`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
Those sources were not rechecked here. They support L332's expansion
and denominator, and are not matches for (1)–(4). No full library
match or absence from checked sources is asserted.
