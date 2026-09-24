# Lemma 334: endpoint derivative moment and Sobolev obstruction

**Hypotheses.** Let r≥2, σ=1+1/r, and use the real functions of L332:

S_r(a)=Σ_(j,k≥1)(jk)^(−1/2)(1−log(jk)/(2r))_+^r exp(ia log(k/j)),
B_r(a)=|ζ(σ+ia)|²,  R_r(a)=S_r(a)/B_r(a)−1.

Write b_r(p,q) and β(p,q) for its reduced-ratio coefficients and
their first variations, with gcd(p,q)=1. In particular L332 proves

R_r(a)=Σ_((p,q)=1)b_r(p,q)exp(ia log(q/p)),
|r b_r(p,q)−β(p,q)|≤K D_4(p,q)/r,
|β(p,q)|≤K D_2(p,q),
D_j(p,q)=τ(p)τ(q)(1+log(pq))^j/(pq).

Let 𝓜_r be its long-height mean square, C>0 the constant in
𝓜_r=C/r²+O(r^(−3)), and define

𝓝_r=lim_(H→∞)(1/(2H))∫_(−H)^H |R_r′(a)|²da.

Primes on R_r denote differentiation in the real height a, with r fixed.

**Conclusion.** The derivative and its mean exist, and

𝓝_r=Σ_((p,q)=1)log(q/p)² b_r(p,q)²
    =C_1/r²+O(r^(−3)),
C_1=Σ_((p,q)=1)log(q/p)² β(p,q)²∈(0,∞).                (1)

Uniformly in A∈ℝ, T>0 and r≥2,

|(1/T)∫_A^(A+T)|R_r′(a)|²da−𝓝_r|
 ≤K(r+1)^19/T.                                         (2)

Thus the derivative mean is C_1/r²+O(r^(−3)) on every translated
interval of length T≥r^22, including [a_n,2a_n] when
r=2n and a_n=sqrt(4π²exp(4r)−25).

Nevertheless, inserting (2) and L333 into the elementary
one-dimensional Sobolev estimate does not reach |R_r(a_n)|≤1/2.
More precisely, choose fixed positive constants A_0,A_1,K_0,K_1
so that on any interval I of length T,

E_0:=∫_I |R_r|²≤A_0T/r²+K_0(r+1)^17,
E_1:=∫_I |R_r′|²≤A_1T/r²+K_1(r+1)^19.

For x∈I the resulting explicit upper bound for |R_r(x)|² is

U_r(T)=A_0/r²+K_0(r+1)^17/T
 +2 sqrt((A_0T/r²+K_0(r+1)^17)(A_1T/r²+K_1(r+1)^19)).    (3)

Its optimized size is

inf_(T>0) U_r(T)
 =2 sqrt(K_0K_1)(r+1)^18+O(r^8).                        (4)

This is a statement about the computed certificate, not a lower
bound for the actual value of |R_r|². Its order r^18 exceeds the
required constant 1/4.

There is also an obstruction in the actual arithmetic function to
any height-uniform relative-closeness conclusion at fixed r:

−1<R_r(0)≤−1+[1+2 sqrt(2πr)+4r]/r²=−1+O(1/r).          (5)

For every fixed r≥16 there are arbitrarily large positive heights a
with R_r(a)<−1/2. No assertion places them at a_n or even in
[a_n,2a_n]. These relative-closeness failures do not establish
S_r(a)≤0: the sufficient condition |R_r|≤1/2 is stronger than
the one-sided arithmetic margin actually needed. No endpoint
Laguerre sign, zero-exclusion range or RH candidate follows.

**Proof.** We first justify differentiation, including the infinite
reciprocal tail. L332 gives the absolutely convergent expansion

R_r(a)=Σ_(m,n≥1)c_r(m,n)exp(ia log(n/m)),
|c_r(m,n)|≤(e+1)τ(m)τ(n)/(mn)^σ.                        (6)

Since |log(n/m)|≤log(mn), the series obtained by differentiating
(6) is absolutely and uniformly convergent in real a at fixed r.
Indeed Σ τ(m)(log m)^j m^(−σ)<∞ for j=0,1, by the ordered
two-factor series and the convergent logarithmic Dirichlet sums.
Uniform convergence of both the original series and its derivative
allows integration of the derivative series on any compact
interval, proving termwise differentiation by the fundamental
theorem of calculus. Grouping equal ratios then gives

R_r′(a)=Σ_((p,q)=1)i log(q/p)b_r(p,q)exp(ia log(q/p)).    (7)

The series of coefficient absolute values is finite. Its squared
expansion is therefore absolutely summable, so averaging first at
fixed r retains exactly equal frequencies and gives the first
identity in (1), as in L332.

The extra logarithm does not destroy the uniform limiting norm:
|log(q/p)|≤log(pq), and L332's divisor bounds imply that
Σ D_j(p,q)²<∞ for every fixed j. Explicitly, use
τ(m)≤C_ε m^ε with ε=1/8 and the integral test after separating
1+log(pq)≤(1+log p)(1+log q). Thus

||log(q/p)[r b_r(p,q)−β(p,q)]||_(ℓ²)=O(1/r),
||log(q/p)β(p,q)||_(ℓ²)<∞.

The norm-square identity used in L332 now proves (1) and finiteness
of C_1. To verify strict positivity, put ℓ=log 2. L332's exact
divisor formula for U(m,n) gives

U(2,1)=ℓ−ℓ²/8,
U(2d,d)=−ℓ²/4 if d=2^k, k≥1,
U(2d,d)=0 for all other d>1.

For the last two statements both nonconstant factors must be
prime powers; d and 2d can then only be powers of 2. Consequently

β(2,1)=(1/2)[ℓ−ℓ²/8−(ℓ²/4)Σ_(k≥1)4^(−k)]
      =ℓ/2−5ℓ²/48>0,                                  (8)

since 0<ℓ<1. Symmetry gives the same value at (1,2), and therefore
C_1≥2ℓ²(ℓ/2−5ℓ²/48)²>0. This also proves that the derivative
mean has exact order r^(−2), rather than just an upper bound.

For (2), apply the four-index grouping of L333 to the derivative
series. In its product with its conjugate put k=nu and l=mv.
The grouped coefficient is

h_r(k,l)=Σ_(n|k,m|l)c_r(m,n)c_r(k/n,l/m)
                  ·log(n/m)log((l/m)/(k/n)).

There is no sign assumption on these coefficients. Since
mnuv=kl and all indices are at least one,

|log(n/m)log(v/u)|≤log(mn)log(uv)≤log(kl)².

The convolution τ*τ=d_4 therefore gives

|h_r(k,l)|≤(e+1)² d_4(k)d_4(l)log(kl)²/(kl)^σ.          (9)

All these sums are absolutely convergent for fixed σ>1, including
the logarithmic factors. Averaging the squared series over an
interval tending to the whole line identifies its exact diagonal
Σ_k h_r(k,k)=𝓝_r. No absolute bound replaces this signed diagonal.
For k≠l its average over [A,A+T] has modulus at most
2/(T|log(k/l)|), independently of A. It remains to bound

Σ_(k≠l)x_k x_l log(kl)²/|log(k/l)|,
x_k=d_4(k)k^(−σ).                                      (10)

When k≥2l or l≥2k, the denominator is at least log 2.
The ordered four-factor expansion shows, for j=0,1,2,

Σ_k x_k(log k)^j=O((r+1)^(4+j)).

Expand log(kl)²=(log k+log l)² and separate the two sums.
The far pairs in (10) are O((r+1)^10).

For k<l<2k use log(l/k)≥(l−k)/(2k),
log(kl)≤2log(2k), and 2x_kx_l≤x_k²+x_l². Fixing k in
the first square term and l in the second gives harmonic sums,
exactly as in L333, and bounds the near pairs by

K Σ_k k x_k² log(2k)^3.

For example, the x_l² term uses k≤l and log(2k)≤log(2l),
then Σ_(k<l)1/(l−k)≤1+log l. Reversing the ordered pairs
gives the same estimate. L333 proves the pointwise inequality
d_4(k)²≤d_16(k) by a surjective matrix-counting map. With u=2/r,
the last sum is consequently at most

K Σ_k d_16(k)k^(−1−u)log(2k)^3=O((r+1)^19).             (11)

Here are explicit convergence and exponent checks for both uses
of logarithmic Dirichlet sums. For 0<u≤1 and integer j≥1,

Σ_(k≥1)(log k)^j k^(−1−u)
 ≤∫_1^∞log(2x)^j x^(−1−u)dx
 =Σ_(h=0)^j binom(j,h)(log 2)^(j−h)h!/u^(h+1).

The inequality holds termwise on [k−1,k] for k≥2. For j=0
use Σ k^(−1−u)≤1+1/u. Expand the jth power of the sum of
the logarithms in an ordered d-factor product. Each resulting
product has d factors whose logarithmic degrees total j, so its
bound is O(u^(−d−j)). This proves the four-factor estimates
above with u=1/r and (11) with d=16, j≤3 and u=2/r.
No boundary differentiation or limiting interchange is hidden in
these nonnegative summations.

Equations (9)–(11) make the sum of all nonzero-frequency integral
bounds finite, with size O((r+1)^19/T). Subtracting the exact
diagonal proves (2). Combining with (1) proves the stated finite
means: at T≥r^22 the error is O(r^(−3)), and at T=a_n it is
O(r^19 exp(−2r))=o(r^(−3)). These conclusions hold at fixed r
before taking the coupled limit.

For the pointwise comparison, let f be continuously differentiable
on an interval I of length T. There is a y∈I with
|f(y)|²≤T^(−1)∫_I|f|². For every x∈I, the fundamental theorem
of calculus and Cauchy–Schwarz give

|f(x)|²≤(1/T)∫_I|f|²+2∫_I|f f′|
       ≤E_0/T+2 sqrt(E_0 E_1).                          (12)

For f=R_r, (1), (2), L332 and L333 permit fixed positive
A_0,A_1,K_0,K_1 as in the conclusion, for all r≥2. On the
bounded initial range of r the same bounds follow directly from
the coefficient majorants above. Substitution proves (3).
Every term in (3) is nonnegative, and its square root is at least
sqrt(K_0K_1)(r+1)^18. Conversely, choose T=(r+1)^9.
The two relative corrections inside that square root have orders
r^(−10) and r^(−12), and the separate K_0 term has order r^8.
Thus

2 sqrt(K_0K_1)(r+1)^18
 ≤inf_(T>0)U_r(T)
 ≤2 sqrt(K_0K_1)(r+1)^18+O(r^8),

which proves (4). The sufficient target was a squared bound 1/4;
even the optimized certificate grows. In fact the direct absolute
coefficient bound in (6) already gives |R_r|=O(r^4), better than
the O(r^9) from (3), but still gives no constant-threshold control.
None of these growing majorants is an assertion that R_r grows.

Finally we prove the actual-function obstruction (5). Extend the
summand at a=0 to real x,y≥1 by

W_r(x,y)=(xy)^(−1/2)(1−log(xy)/(2r))_+^r.

It is nonnegative and decreasing in each variable. Applying
Σ_(j≥1)f(j)≤f(1)+∫_1^∞f(x)dx in both variables gives

S_r(0)≤1+2∫_1^∞W_r(x,1)dx
            +∫_1^∞∫_1^∞W_r(x,y)dxdy.

For 0≤L<2r, log(1−L/(2r))≤−L/(2r)−L²/(8r²), so

exp(L/2)(1−L/(2r))_+^r≤exp(−L²/(8r))

also holds past the cutoff. Substituting x=exp(u), y=exp(v)
bounds the two displayed integrals by

∫_0^∞exp(−u²/(8r))du=sqrt(2πr),
∫_0^∞L exp(−L²/(8r))dL=4r,

respectively. All integrands are nonnegative, so these changes
of order need no conditional-convergence argument. Also
ζ(1+1/r)≥∫_1^∞x^(−1−1/r)dx=r. Since S_r(0)≥1, these
estimates prove (5). For r≥16, π<4 and sqrt(8r)≤r yield

S_r(0)/B_r(0)≤(1+6r)/r²≤97/256<1/2.

We give an elementary recurrence argument to avoid any unproved
equidistribution statement. At fixed r the absolutely convergent
series (6) has finite exponential-sum approximations P with
||R_r−P||_∞ arbitrarily small. For any finite list of frequencies
λ_1,…,λ_J and any integer Q≥2, divide the unit J-cube into
Q^J equal boxes. Two of the Q^J+1 vectors of fractional parts
of k(λ_1/(2π),…,λ_J/(2π)), 0≤k≤Q^J, lie in the same box.
Their difference yields an integer 1≤q_Q≤Q^J for which
|exp(iq_Q λ_j)−1|≤2π/Q for every j.

As Q→∞, either an unbounded subsequence of these integers gives
returns approaching one in every phase, or a bounded subsequence
contains a repeated q_* with exp(iq_*λ_j)=1 for all j. In the
second case all positive multiples of q_* are exact returns.
Thus, for any prescribed accuracy, there are arbitrarily large
positive a with P(a) arbitrarily close to P(0). Approximating R_r
first and then using such a return gives arbitrarily large a with
|R_r(a)−R_r(0)| arbitrarily small. The strict margin just proved
therefore gives R_r(a)<−1/2 at arbitrarily large a for fixed r≥16.

This proof offers no return-time bound uniform in r and no relation
to a_n. At zero itself S_r(0)>0 despite the large relative error;
at the recurrent heights no negative S_r value has been proved.
Consequently neither the recurrence nor the failed Sobolev
certificate decides the endpoint arithmetic sign. They stop the
stated height-uniform conversion of these moments to relative
closeness, not a bound exploiting the specific height-cutoff
relation or a one-sided arithmetic sign mechanism. ∎

**Mathlib.** Full statement: not checked. Coverage of the derivative
mean, finite-window bound, optimized Sobolev certificate and
recurrence obstruction is not checked; all are proved above.
Supporting reciprocal-series, convergence and nonvanishing results
are retained from L332–L333, where they are recorded as present
through L001:
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
and [`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
Those sources were not rechecked. They support the original
expansion and denominator, not the full statement here. No full
match or absence from checked sources is asserted.
