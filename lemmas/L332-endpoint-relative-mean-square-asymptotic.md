# Lemma 332: endpoint relative mean-square asymptotic

**Hypotheses.** Let r≥2 be real, c=1/2+1/r and σ=1+1/r. Use the full
endpoint sum from L303, with the cutoff interpreted as zero at equality:

S_r(a)=Z_r(a;c)=Σ_(j,k≥1) W_r(j,k) exp(ia log(k/j)),
W_r(j,k)=(jk)^(−1/2)(1−log(jk)/(2r))_+^r.

For real a put

B_r(a)=|ζ(σ+ia)|²,  R_r(a)=S_r(a)/B_r(a)−1,
𝓜_r=lim_(A→∞) (1/(2A))∫_(−A)^A |R_r(a)|² da.

The sum defining S_r is finite. The denominator is nonzero by L001.
Let μ be the Möbius function, τ(m) the number of positive divisors of m,
δ_m=1 for m=1 and zero otherwise, and Λ(m)=log p if m=p^k with p prime
and k≥1, zero otherwise. In particular Λ(1)=0. All logarithms are real
logarithms of positive numbers.

**Conclusion.** The mean exists for every r≥2, and

𝓜_r=C/r²+O(r^(−3)),  0<C<∞.                              (1)

Here is an exact convergent expression for C. Set

P(t)=t−t²/8,
U(m,n)=Σ_(j|m,k|n) μ(m/j)μ(n/k)P(log(jk)),
β(p,q)=(1/(pq))Σ_(d≥1) U(dp,dq)/d²  for gcd(p,q)=1.

Then

C=Σ_((p,q)=1) β(p,q)²,
β(1,1)=−(1/4)Σ_(d≥2) Λ(d)²/d²<0.                         (2)

All series in (2) converge in the senses explicitly proved below, and
C≥(log 2)^4/144. The long-height mean of the relative error itself is

lim_(A→∞) (1/(2A))∫_(−A)^A R_r(a)da
 =−(1/(4r))Σ_(d≥2) Λ(d)²/d²+O(r^(−2)).                  (3)

For every fixed 0<η<1, the exceptional-height set has upper density

limsup_(A→∞) meas{a∈[−A,A]: |R_r(a)|≥η}/(2A)
 ≤𝓜_r/η²=O_η(r^(−2)).                                  (4)

Outside this set S_r(a)≥(1−η)B_r(a)≥(1−η)/(r+1)².
This polynomial margin dominates E_r=(1+r)²exp(−r/256) as r→∞.
However, A→∞ is taken first with r fixed. No rate in A uniform in r,
no information at the prescribed a_n=sqrt(4π²exp(4r)−25), r=2n, and
no additional Laguerre sign or zero-exclusion range are asserted.

**Proof.** We first establish a uniform scalar estimate that will
control the divisor sums, including their moving cutoff. For t≥0 let

f_r(t)=exp(t/2+t/r)(1−t/(2r))_+^r.

For 0≤t<2r, the power series for log(1−u) gives

log f_r(t)≤(t−t²/8)/r≤2/r.

Thus 0≤f_r(t)≤e for all t≥0 and r≥2, also beyond the cutoff. If
0≤t≤r, the same series gives

log f_r(t)=P(t)/r−D_r(t),  0≤D_r(t)≤C₀t³/r².             (5)

Indeed the terms starting with u³ are bounded by u³/[3(1−u)] for
u=t/(2r)≤1/2. For real x,
|exp(x)−1−x|≤x² exp(max(x,0))/2, by the integral Taylor remainder.
Also |exp(x−D)−exp(x)|≤exp(x)D for D≥0. Apply these with x=P(t)/r,
whose positive part is at most 1. This proves, on 0≤t≤r,

|f_r(t)−1−P(t)/r|≤C₁(1+t)^4/r².                         (6)

For t≥r, the bound f_r≤e and the quadratic size of P prove (6)
directly: each of 1, t/r and t²/r is at most a constant times
(1+t)^4/r² there. Consequently (6) holds for every t≥0 with one
constant independent of r. This is not a fixed-head expansion.

By L001 the two reciprocal Dirichlet series converge absolutely at σ.
Expanding S_r/B_r, and setting m=ju and n=kv for reciprocal indices
u,v, yields

R_r(a)=Σ_(m,n≥1) (mn)^(−σ) H_r(m,n) exp(ia log(n/m)),
H_r(m,n)=Σ_(j|m,k|n) μ(m/j)μ(n/k)[f_r(log(jk))−1].        (7)

To check the subtraction, the same divisor sum with the constant 1
equals δ_mδ_n by the elementary identity Σ_(j|m)μ(m/j)=δ_m.
Moreover W_r(j,k)=(jk)^(−σ)f_r(log(jk)), proving the coefficient
identity including its cutoff. All series in (7) are absolutely
convergent for each fixed r: |f_r−1|≤e+1 and

Σ_(m,n) (mn)^(−σ)τ(m)τ(n)=ζ(σ)^4<∞.

The identity Σ τ(m)m^(−σ)=ζ(σ)² follows by counting m=uv; no
reciprocal series is used on or to the left of Re s=1.

Every positive rational n/m has a unique reduced form q/p. Grouping
all m=dp, n=dq in (7) gives the absolutely summable expansion

R_r(a)=Σ_((p,q)=1) b_r(p,q) exp(ia log(q/p)),
b_r(p,q)=Σ_(d≥1) (d²pq)^(−σ) H_r(dp,dq).                 (8)

Its coefficients are real and symmetric in p,q. For distinct reduced
pairs the frequencies log(q/p) are distinct. The mean of a single
exponential over [−A,A] tends to zero unless its frequency is zero,
when it is one. Absolute summability justifies applying this limit
to the double expansion of |R_r|²: the summable dominating series
is (Σ |b_r|)². Therefore

𝓜_r=Σ_((p,q)=1) |b_r(p,q)|²,                            (9)

and the mean of R_r is b_r(1,1). This proves existence and groups
every equal-ratio collision before taking the mean.

We now obtain domination uniform as σ decreases to 1. From (6), for
L=log(mn),

|H_r(m,n)−U(m,n)/r|
 ≤C₁τ(m)τ(n)(1+L)^4/r²,
|U(m,n)|≤C₂τ(m)τ(n)(1+L)².                              (10)

Since |(mn)^(−σ)−(mn)^(−1)|≤(mn)^(−1)L/r, (10) implies

|r(mn)^(−σ)H_r(m,n)−(mn)^(−1)U(m,n)|
 ≤(C₃/r) τ(m)τ(n)(1+log(mn))^4/(mn).                    (11)

For clarity, the elementary divisor estimates needed to sum (11) are
proved here. The prime-exponent formula gives τ(dm)≤τ(d)τ(m).
For any ε>0, τ(m)≤C_ε m^ε: for primes p≥2^(1/ε), k+1≤2^k≤p^(εk);
for each of the finitely many smaller primes the supremum of
(k+1)/p^(εk) is finite. Multiplying those finitely many constants
proves the assertion. Taking, for example, ε=1/8 shows that

Σ_(d≥1) τ(d)²(1+2log d)^j/d²<∞                         (12)

for every fixed nonnegative integer j, by the integral test.
Also 1+log(d²pq)≤(1+2log d)(1+log(pq)). Thus summing (11) over d
is justified absolutely and proves

|r b_r(p,q)−β(p,q)|≤(C₄/r)D_4(p,q),
|β(p,q)|≤C₅D_2(p,q),
D_j(p,q)=τ(p)τ(q)(1+log(pq))^j/(pq).                    (13)

For j=2,4 the squares of D_j are summable over all p,q, hence over
the reduced pairs: bound 1+log(pq) by (1+log p)(1+log q), separate
the sums, and use (12). This proves absolute convergence of each
series defining β, square summability of β, and the quantitative
norm estimate

||r b_r−β||_(ℓ²)=O(1/r).                                (14)

In particular ||r b_r||_(ℓ²) is bounded. The inequality
| ||x||²−||y||² |≤||x−y||(||x||+||y||), applied to (14) and (9),
gives r²𝓜_r=Σ β²+O(1/r). This proves (1) except for strict
positivity. It also makes the order of limiting operations explicit:
the first limit (9) is at fixed r, and the second argument is a
uniform bound on its coefficient norm, not an exchange of r and A.

We compute the diagonal coefficient without any estimate on primes.
Finite divisor sums satisfy

Σ_(j|m) μ(m/j)log j=Λ(m).                               (15)

One elementary proof is that log m=Σ_(d|m)Λ(d), by prime factorization;
convolving this finite identity with μ and using μ*1=δ proves (15).
Define A(m)=Σ_(j|m)μ(m/j)(log j)². Expanding P(log j+log k) in
the finite definition of U gives exactly

U(m,n)=Λ(m)δ_n+δ_mΛ(n)
       −[A(m)δ_n+δ_mA(n)+2Λ(m)Λ(n)]/8.                  (16)

For m=n=d>1 this is −Λ(d)²/4, and U(1,1)=0. Hence (2) follows.
The sum is finite because Λ(d)≤log d; it is strictly positive
before multiplication by −1/4 because d=2 contributes. More
explicitly, its powers-of-two contribution is

Σ_(k≥1) Λ(2^k)²/(2^k)²=(log 2)²/3.

Thus C≥β(1,1)²≥(log 2)^4/144>0. Formula (13) at (1,1), followed
by the mean identity after (9), proves (3). In particular the mean
square is of exact order r^(−2), not merely bounded by that order.

Finally Chebyshev's inequality on each interval [−A,A], followed by
(9), gives (4). Since R_r and S_r are real, |R_r|<η implies
S_r>(1−η)B_r. L001 and the decreasing integral comparison give

|1/ζ(σ+ia)|≤ζ(σ)≤1+1/(σ−1)=r+1,

so B_r≥(r+1)^(−2). The ratio of the asserted positive lower bound
to E_r is (1−η)exp(r/256)/(r+1)^4, which tends to infinity.
This is a margin for the arithmetic sum at heights outside the
exceptional set. L303's endpoint assembly applies at its prescribed
paired parameters; nothing above places those parameters outside
that set. A set of small, or even zero, density can contain every
point of a prescribed sequence. No interchange of limits supplies
a finite-height conclusion either. This proves all claims and
their stated qualifications. ∎

This supplies arithmetic cancellation in a relative average that the
uniform absolute error estimate does not detect. It leaves both a
quantitative finite-height estimate at a comparable to exp(2r) and
control of exceptional prescribed heights unproved. It does not
change the existing all-level interval, the excluded nonreal-center
range, or the global low-index gap; no RH candidate follows.

**Mathlib.** Full statement: not checked. The supporting reciprocal
identity is recorded as present in L001:
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
with absolute convergence supported by
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff)
and nonvanishing by
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
These previously recorded references were not looked up again and
are supporting results, not matches for (1)–(4). Coverage for the
reduced-ratio mean identity, uniform divisor estimates and limiting
coefficient norm is not checked; all needed arguments are proved
above. No absence or full library match is asserted.
