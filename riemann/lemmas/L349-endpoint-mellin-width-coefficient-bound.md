# Lemma 349: Mellin-width normalization bounds the endpoint coefficient mass

**Hypotheses.** For real r≥2 put δ=r^(-1/2), σ=1+δ and
c=1/2+δ. Retain the full endpoint sum of L303,

S_r(a)=Σ_(j,k≥1)(jk)^(-1/2)(1−log(jk)/(2r))_+^r
                                      ·exp(ia log(k/j)),

with the cutoff weight zero at equality. For real a define

R_r^w(a)=S_r(a)/|ζ(σ+ia)|²−1.

Here the superscript w distinguishes this normalization from
L332's normalization at σ=1+1/r. Let μ, τ and Λ be the Möbius,
divisor-counting and von Mangoldt functions, with Λ(1)=0. Set

f_r(t)=exp((1/2+δ)t)(1−t/(2r))_+^r,  t≥0,
H_r^w(m,n)=Σ_(j|m,k|n)μ(m/j)μ(n/k)[f_r(log(jk))−1],
b_r^w(p,q)=Σ_(d≥1)(d²pq)^(-σ)H_r^w(dp,dq),  gcd(p,q)=1.

All logarithms of integers are real. The constant frequency is
the single reduced pair (p,q)=(1,1). A Liouville evaluation of a
grouped series means replacing exp(ia log(q/p)) by λ(p)λ(q),
where λ(m)=(−1)^Ω(m); it does not specify a sampled height.

**Conclusion.** The denominator is nonzero, the grouped expansion

R_r^w(a)=Σ_((p,q)=1)b_r^w(p,q)exp(ia log(q/p))             (1)

is absolutely convergent, and there is an absolute constant C with

Σ_((p,q)=1)|b_r^w(p,q)|≤C  for every r≥2.                (2)

Thus widening the pole distance to the Mellin width removes the
diverging coefficient-mass obstruction of L347–L348. The mass
does not tend to zero: with
A_r^w=Σ_((p,q)=1,p≠q)|b_r^w(p,q)|, one has

b_r^w(1,1)=O(1/r),
R_r^w(0)→3,  R_r^w[λ]→−5/4,
liminf_(r→∞) A_r^w≥3.                                 (3)

There is also the precise long-height mean-square asymptotic

lim_(H→∞)(1/(2H))∫_(−H)^H |R_r^w(a)|²da
 =Σ_((p,q)=1)|b_r^w(p,q)|²
 =C_w/r+O(r^(-3/2)),
C_w=2Σ_(m≥2)Λ(m)²/m²,  0<C_w<∞.                      (4)

This is larger than L332's order-r^(-2) mean square at the narrower
normalization. Neither (2) nor (4) controls the prescribed heights
a_n=sqrt(4π²exp(8n)−25), r=2n. The needed condition there remains
a positive S_r(a_n) margin dominating (1+r)²exp(−r/256).
No Laguerre sign, zero-exclusion range or RH candidate follows.

**Proof.** L001 supplies nonvanishing and the absolutely convergent
reciprocal series throughout Re s>1. For 0≤t<2r,

log f_r(t)≤δt−t²/(8r)≤2,

using log(1−u)≤−u−u²/2 and completing the square. Beyond the
cutoff f_r=0, so 0≤f_r≤exp(2) everywhere. Expanding the two
reciprocals in R_r^w and writing m=ju, n=kv therefore gives

R_r^w(a)=Σ_(m,n≥1)(mn)^(-σ)H_r^w(m,n)exp(ia log(n/m)).   (5)

Indeed (jk)^(-σ)f_r(log(jk)) is the original weight. The divisor
sum of the subtracted constant is δ_(m,1)δ_(n,1). At each fixed
r the absolute majorant is

(exp(2)+1)Σ_(m,n≥1)τ(m)τ(n)/(mn)^σ
 =(exp(2)+1)ζ(σ)^4<∞.

The identity for the divisor sum follows by counting factorizations.
Unique reduction m=dp,n=dq proves (1), and shows that every
equal-ratio collision has been retained. This initial majorant
does not give (2), since it grows with r.

For the uniform bound, use L303's exact Mellin integral on the
line c=1/2+δ. Write

K_r(v)=Γ(r+1)(2r)^(-r)exp(2r(c+iv))
                                      ·(c+iv)^(-r−1)/(2π),
A_(σ,v)(a)=ζ(σ+i(a+v))/ζ(σ+ia).

Then

1+R_r^w(a)=∫_ℝ K_r(v)A_(σ,v)(a)A_(σ,v)(−a)dv.          (6)

This product has the same v in both factors; it is not a modulus
square. We estimate its coefficient norm, without replacing the
complex kernel by a positive averaging measure.

For a prime ℓ let q_ℓ=ℓ^(-σ), z=exp(−ia log ℓ) and
u_ℓ=exp(−iv log ℓ). The exact local ratio is

(1−q_ℓ z)/(1−q_ℓ u_ℓ z)
 =1+Σ_(k≥1)q_ℓ^k(u_ℓ−1)u_ℓ^(k−1)z^k.                 (7)

Its sum of coefficient absolute values is
1+|u_ℓ−1|/(ℓ^σ−1). Unique prime factorization and absolute
Euler products, as in L005, consequently give an absolutely
summable Dirichlet expansion for A_(σ,v), of norm

E_σ(v)=Π_ℓ[1+|exp(−iv log ℓ)−1|/(ℓ^σ−1)].              (8)

For completeness, each finite product has exactly this coefficient
norm, and the product of these nonnegative local norms converges
since Σ_ℓ 2/(ℓ^σ−1)<∞. Its tails tend to one. Expanding over all
integers therefore converges in the coefficient ℓ¹ norm and agrees
with the ratio of the two absolutely convergent Euler products.
No limiting series at Re s=1 is used.

Two complementary estimates for (8) are

E_σ(v)≤exp(|v| B(σ)),
B(σ)=Σ_ℓ log ℓ/(ℓ^σ−1)=−ζ′(σ)/ζ(σ),
E_σ(v)≤Π_ℓ(1+ℓ^(-σ))/(1−ℓ^(-σ))
       =ζ(σ)²/ζ(2σ).                                  (9)

The first uses |exp(−ix)−1|≤|x| and log(1+x)≤x; the
second uses the bound 2. Termwise differentiation of L005 is
legitimate on each compact sub-half-plane Re s>1: its derivative
series is dominated by a constant times Σ_(m≥2)(log m)m^(-σ₀)
for some fixed σ₀>1. This proves the derivative identity in (9).
L335 proves that H(w)=wζ(1+w) is analytic and nonzero near zero,
with H(0)=1. Thus

B(1+δ)=1/δ−H′(δ)/H(δ)=1/δ+O(1),

and B(σ)≤C₀ sqrt(r) for all sufficiently large r. Also
ζ(σ)≤1+sqrt(r), by the decreasing integral comparison.

L338's moving-line kernel estimates at α=1 give, for large r,

|K_r(v)|≤C₁ sqrt(r)exp(−rv²/4),  |v|≤c,
|K_r(v)|≤C₁ sqrt(r)2^(-r/4)(1+(v/c)²)^(-2),  |v|>c.    (10)

Their prefactor is O(sqrt(r)) because Stirling's formula gives
the exponential exp(2sqrt(r)−r log(1+2/sqrt(r))), whose exponent
tends to 2. Here 1/2<c≤1 for r≥4. In particular all constants
in (10) are independent of r and a. Combining the first bounds
in (9) and (10), and putting t=sqrt(r)v, gives

∫_(|v|≤c)|K_r(v)|E_σ(v)²dv
 ≤C₁∫_ℝ exp(−t²/4+2C₀|t|)dt<∞,                       (11)

uniformly in r. On the rest of the contour use the second bound
in (9), not its linearly growing exponential bound. Since
ζ(2σ)≥1 and c≤1,

∫_(|v|>c)|K_r(v)|E_σ(v)²dv
 ≤C₂ r^(5/2)2^(-r/4)=o(1).                            (12)

The same integrals are uniformly bounded on any remaining compact
r-interval in [2,∞): σ stays a positive distance above one, the
kernel prefactor stays bounded, and its tail has a uniform
integrable majorant C(1+v²)^(-3/2). Thus

∫_ℝ |K_r(v)|E_σ(v)²dv≤C₃  for every r≥2.              (13)

To check that this bounds the actual coefficients in (1), expand
both factors A in (6). Before grouping their two-index coefficient
norm is E_σ(v)². Tonelli applied to its product with |K_r(v)| is
justified by (13); coefficient integration and every subsequent
ratio grouping are therefore valid in ℓ¹. For a fixed pair m,n,
the expansion of the ratio factors gives the coefficient

(mn)^(-σ)Σ_(j|m,k|n)μ(m/j)μ(n/k)(jk)^(-iv).

L303's scalar inversion gives
∫K_r(v)exp(−iv t)dv=f_r(t). Integrating the displayed coefficient
therefore gives precisely (5) before subtracting its constant.
Grouping can only decrease the coefficient ℓ¹ norm. Subtracting
one changes that norm by at most one, so (13) proves (2).

We next control the constant coefficient and square norm; these
also distinguish bounded mass from a small uniform error. The
following estimate holds uniformly for r≥2 and t≥0:

|f_r(t)−1−δt|≤C₄t²/r.                                 (14)

For 0≤t≤sqrt(r), put u=t/(2r)≤1/(2sqrt(2)). The power series
for log(1−u) shows
log f_r(t)=δt−D, with 0≤D≤C t²/r. Since δt≤1,
|f_r(t)−exp(δt)|≤eD, and
|exp(δt)−1−δt|≤e(δt)²/2. This proves (14) on that interval.
For t≥sqrt(r), the bound f_r≤exp(2) and δt≥1 give
|f_r−1−δt|≤exp(2)+1+δt≤C(δt)², proving the rest,
including the cutoff and its tail.

The finite convolution identity μ*log=Λ, proved in L332, gives

Σ_(j|m,k|n)μ(m/j)μ(n/k)log(jk)
 =Λ(m)δ_(n,1)+δ_(m,1)Λ(n).                             (15)

When m=dp,n=dq with p,q coprime, a nonzero term in (15) requires
d=1 and one of p,q to be 1. Define γ(p,q) on the reduced pairs by

γ(1,q)=Λ(q)/q  for q>1,
γ(p,1)=Λ(p)/p  for p>1,
γ(p,q)=0  otherwise.

Summing (14) over the finite divisors and then over d gives

|b_r^w(p,q)−δγ_σ(p,q)|≤(C₅/r)D_2(p,q),
D_2(p,q)=τ(p)τ(q)(1+log(pq))²/(pq),                    (16)

where γ_σ has the same axial support as γ and values Λ(m)/m^σ.
Indeed τ(dp)≤τ(d)τ(p), σ≥1, and
1+log(d²pq)≤(1+2log d)(1+log(pq)); the remaining d-sum is
bounded by Σ_d τ(d)²(1+2log d)²/d²<∞. L332 proves this
convergence and square summability of D_2 by elementary divisor
bounds. Also

||γ_σ−γ||_2²
 ≤2δ²Σ_(m≥2)Λ(m)²(log m)²/m²=O(δ²),

using |exp(−δ log m)−1|≤δ log m and Λ(m)≤log m.
Consequently (16) implies

||b_r^w−δγ||_2=O(1/r),
||b_r^w||_2²=δ²||γ||_2²+O(r^(-3/2)).                  (17)

The constant coefficient in (16) is O(1/r) because γ_σ(1,1)=0.
Moreover ||γ||_2²=C_w; finiteness follows from the integral test,
and its m=2 term proves strict positivity. For each fixed r,
absolute convergence in (1) dominates the squared Fourier series
by (Σ|b_r^w|)². Averaging each exponential over [−H,H] and taking
H→∞ retains exactly equal reduced ratios. This proves (4) from
(17), without interchanging the r and H limits.

Finally L297's full-mass calculation gives S_r(0)=4r+o(r).
The pole expansion gives ζ(1+δ)²=δ^(-2)(1+O(δ))
=r(1+O(r^(-1/2))), so R_r^w(0)→3. For the other character,
L335 gives

F_λ(s)=Σ_m λ(m)m^(-s)=ζ(2s)/ζ(s),  Re s>1,
F_λ(1+δ)=ζ(2)δ+O(δ²),
S_r[λ]=−ζ(2)²/(4r)+O(r^(-2)).                          (18)

Twisting the absolutely convergent reciprocal series by λ gives
1/F_λ, by the same finite Möbius inversion. In each grouped
coefficient λ(dp)λ(dq)=λ(p)λ(q). Thus the exact evaluation is

R_r^w[λ]=S_r[λ]/F_λ(σ)²−1→−1/4−1=−5/4.               (19)

All products here are in Re s>1. Removing the constant frequency
from the trivial evaluation yields
A_r^w≥|R_r^w(0)−b_r^w(1,1)|→3 in the lower-limit sense.
This proves (3); neither character locates an exception at a_n.

The obtained O(1) mass meets the proposed boundedness threshold,
but its lower bound precludes a uniform error norm below one.
For fixed 0<η<1, (4) only gives upper exceptional density
O_η(1/r), with the height limit first. If one could instead prove
|R_(2n)^w(a_n)|≤η, then L001 and ζ(σ)≤1+sqrt(r) would give

S_r(a_n)≥(1−η)/(1+sqrt(r))²,

which dominates L303's assembled error (1+r)²exp(−r/256).
No such sampled bound is established. The previously divergent
absolute-mass obstruction is removed; a bound for the moving
coefficient vectors, their actual sampling norm, and ultimately
every required endpoint and lower-index sign remain separate
unproved steps. ∎

**Mathlib.** Full statement: not checked. Coverage of the normalized
Euler-factor coefficient norm, its uniform Mellin integral, the
grouped ℓ¹ bound and the changed mean-square asymptotic is not
checked; the proofs are above. L001 and L005 record as present
the supporting results
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re),
and [`riemannZeta_eulerProduct_exp_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
These inherited links were not rechecked. They support the
reciprocal and Euler products in their actual half-plane, not the
full statement here. No full library match or absence from checked
sources is asserted.
