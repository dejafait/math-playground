# Lemma 335: endpoint Liouville-phase negativity

**Hypotheses.** Let r tend to infinity through real values. Use the
endpoint weights and finite sums of L303:

W_r(j,k)=(jk)^(−1/2)(1−log(jk)/(2r))_+^r,
J_r={j≥1: j<exp(3r/4)},
S_r(a)=Σ_(j,k≥1) W_r(j,k)exp(ia log(k/j)),
T_r(a)=Σ_(j,k∈J_r) W_r(j,k)exp(ia log(k/j)).

For a completely multiplicative function ω with |ω(m)|=1 define

S_r[ω]=Σ_(j,k≥1) W_r(j,k)ω(j)conjugate(ω(k)),
T_r[ω]=Σ_(j,k∈J_r) W_r(j,k)ω(j)conjugate(ω(k)).

Both are finite and real. Write λ(m)=(−1)^Ω(m), where Ω counts
prime factors with multiplicity, and put A=ζ(2)²>0.

**Conclusion.** The Liouville assignment satisfies

S_r[λ]=−A/(4r)+O(r^(−2)),
T_r[λ]=−A/(4r)+O(r^(−2)).                              (1)

In particular both are at most −A/(8r) for all sufficiently large r.
For each fixed such r there are arbitrarily large positive a for which

S_r(a)<−A/(16r),  T_r(a)<−A/(16r).                     (2)

Thus every approximation to either sum by a function nonnegative at
every real height has uniform error at least A/(16r). Positivity
uniform over completely multiplicative unit phases is false, even
with a negative error allowance O(E_r), where
E_r=(1+r)²exp(−r/256)=o(1/r).

There is no bound here on the first height in (2), nor any claim that
one equals a_n=sqrt(4π²exp(4r)−25) when r=2n. These negative arithmetic
values are not negative Laguerre coefficients, off-line zeros, or a
counterexample to RH. The endpoint margin at those coupled pairs and
the lower-index signs remain unresolved.

**Proof.** We first obtain the exact twisted Mellin identity in its
absolutely convergent domain. For Re s>1 set

F(s)=Σ_(m≥1)λ(m)m^(−s).

If m=∏p^e, then
Σ_(d|m)λ(d)=∏_(p^e||m)Σ_(j=0)^e(−1)^j equals one when m is a
square and zero otherwise. Absolute convergence therefore gives
ζ(s)F(s)=ζ(2s). L001 supplies nonvanishing of ζ(s) in this half-plane,
so

F(s)=ζ(2s)/ζ(s),  |F(σ+iv)|≤ζ(σ) for σ>1.             (3)

Also λ(j)λ(k)=λ(jk), and the finite product grouping gives

S_r[λ]=Σ_(m<exp(2r))λ(m)τ(m)m^(−1/2)
                         ·(1−log m/(2r))^r.            (4)

No estimate of a conditionally convergent Liouville sum is being used.

Let c=1/2+1/r, σ=1+1/r, and introduce L304's normalized kernel

K_r(v)=Γ(r+1)(2r)^(−r)exp(2r(c+iv))
                         ·(c+iv)^(−r−1)/(2π).

Apply L298's scalar inversion formula to each weight before summing.
The sum of the absolute integrands is at most a constant depending
on r times
ζ(σ)²(c²+v²)^(−(r+1)/2), which is integrable. Fubini and (3) yield

S_r[λ]=∫_ℝ K_r(v)F(σ+iv)²dv.                          (5)

The square here is an analytic square, not a modulus square. Both
Dirichlet factors have the same Liouville coefficients and the same
argument. This is the only modification of L303's inversion argument.

We next check the expansion where the kernel concentrates. The standard
meromorphic continuation gives a simple pole of ζ at 1. Its residue
is one: for real x>0 the integral comparison

1/x≤ζ(1+x)≤1+1/x

implies xζ(1+x)→1. Thus H(w)=wζ(1+w) extends holomorphically across
zero with H(0)=1 and is nonzero in a fixed neighborhood of zero.
Equation (3) consequently continues near s=1 as

F(1+w)=wζ(2+2w)/H(w).

The numerator is analytic there by absolute Dirichlet convergence near
2. There exist fixed δ∈(0,1/4), B∈ℝ and C<∞ such that

F(1+w)²=A w²+B w³+R(w),
|R(w)|≤C|w|⁴ for |w|≤2δ.                              (6)

This follows from its convergent Taylor series on a larger disk; B is
real because the function is real on the real axis. No zero-free region
at a growing height or continuation of the series in (3) is assumed.

Here are the error bounds needed to use (6) on the full contour.
L304's kernel estimate is

|K_r(v)|=P_r(1+(v/c)²)^(−(r+1)/2),  P_r=O(sqrt(r)).

For r≥2, c≤1. On |v|≤c it gives

|K_r(v)|≤C sqrt(r)exp(−r v²/4).                        (7)

For |v|>c and r≥16, splitting the exponent gives the stronger
integrable bound

|K_r(v)|≤C sqrt(r)2^(−r/4)(1+(v/c)²)^(−4).             (8)

Indeed split off (1+(v/c)²)^(−r/4)≤2^(−r/4); the remaining
exponent is −r/4−1/2≤−4. These estimates imply, for some fixed κ>0,

∫_(|v|>δ)|K_r(v)|(1+|1/r+iv|³)dv
                                      =O(sqrt(r)exp(−κr)). (9)

For δ<|v|≤c, split the Gaussian in (7) into two equal factors to
extract exp(−rδ²/8); the other factor has integral O(r^(−1/2)).
For |v|>c use (8), whose product with 1+|v|³ is integrable uniformly
in c∈[1/2,1]. This proves (9). By (3) and ζ(σ)≤r+1, the part of (5)
with |v|>δ is O((r+1)²sqrt(r)exp(−κr)).

On |v|≤δ and for r large enough, w=1/r+iv satisfies |w|≤2δ.
Equations (6) and (7) show that its integrated Taylor remainder is

∫_(|v|≤δ)|K_r(v)R(1/r+iv)|dv
 ≤C sqrt(r)∫_ℝ exp(−r v²/4)(r^(−4)+v⁴)dv
 =O(r^(−2)).                                          (10)

The constant here is independent of r. The exponentially small tails
in (9) allow the quadratic and cubic polynomial integrals to be
extended to the whole line. Thus every discarded part of (5) is
O(r^(−2)); no growing finite-head expansion has been substituted.

The remaining signed moments are exact. Put z=c+iv and let
r^(underline k)=r(r−1)…(r−k+1), with the empty product one.
For each integer 0≤k≤3 and r>k, scalar inversion from L298, now
with exponent r−k at t=2r, gives

∫_ℝ K_r(v)z^k dv
 =Γ(r+1)/[(2r)^k Γ(r−k+1)]
 =r^(underline k)/(2r)^k.                              (11)

These integrals are absolutely convergent, since r>k. Expanding
w=z−1/2 and using (11) yields

∫ K_r w²=−1/(4r),  ∫ K_r w³=1/(4r²).                  (12)

Substitution of (6), (9), (10) and (12) into (5) proves
S_r[λ]=−A/(4r)+B/(4r²)+O(r^(−2)), hence the first assertion of (1).
The negative sign comes from the exact centered quadratic moment of
the complex kernel, despite its total signed mass being one.

L303 proves the coefficient absolute-tail estimate

Σ_((j,k)∉J_r²) W_r(j,k)=O(r exp(−9r/128)).              (13)

Its proof uses only nonnegative weights. Therefore it applies to any
unit phase assignment, giving
|T_r[λ]−S_r[λ]|=O(r exp(−9r/128))=o(r^(−2)). This proves the second
assertion of (1) and the negative bounds for sufficiently large r.

We now prove (2), including the phase approximation needed to connect
the test assignment with the actual finite functions of a. Fix such
an r. Let p_1,…,p_d be all primes below exp(2r). For
θ=(θ_1,…,θ_d) on the d-dimensional torus assign ω_θ(p_j)=exp(iθ_j)
and extend multiplicatively to all integers occurring in the sums.
Both S_r[ω_θ] and T_r[ω_θ] are continuous real trigonometric
polynomials. At θ_*=(π,…,π) they satisfy the negative bounds just
proved. Hence a box U about θ_* exists on which both are less than
−A/(16r).

For completeness, an elementary finite Fourier argument shows that
the orbit θ_j(a)=−a log p_j visits U at arbitrarily large positive a.
Shrink U if needed to the box of circular distances |θ_j−π|<ε,
with 0<ε<π, and put q=cos²(ε/2)<1. For an integer M≥1 define

g_M(θ)=∏_(j=1)^d [(1−cos θ_j)/2]^M.

This is a finite nonnegative trigonometric polynomial, bounded by one;
outside U at least one factor bounds it by q^M. Its constant Fourier
coefficient is

b_M=[binom(2M,M)/4^M]^d≥(2M+1)^(−d).                  (14)

The formula follows by expanding each factor, and the inequality
follows since the central binomial coefficient is the largest of the
2M+1 coefficients whose sum is 4^M. Choose M so large that b_M>q^M;
d is finite and fixed in this choice.

For any nonzero integer vector k, unique prime factorization gives
Σ_j k_j log p_j≠0. Thus each nonconstant Fourier term of
g_M(θ(a)) has average zero over [A_0,A_0+T] as T→∞, for every fixed
A_0. Direct integration of that exponential proves this assertion;
only finitely many terms are involved. Its constant term remains
b_M. If the orbit never visited U after A_0, the same averages would
be at most q^M, contradicting b_M>q^M. Since A_0 is arbitrary, the
visits occur at arbitrarily large positive heights.

On this orbit ω_θ(m)=m^(−ia), so its two polynomial values are exactly
S_r(a) and T_r(a). The bounds on U prove (2), with no approximation
or omission of multiplicative relations or equal-ratio collisions.
At any height in (2), approximation by a nonnegative real value has
absolute error at least A/(16r), proving the uniform-error assertion.

Finally rE_r=r(1+r)²exp(−r/256)→0. Thus the negative margin in (1)
and (2) is larger in magnitude than the assembled endpoint error
scale. This rules out a uniform sign mechanism, not its restriction
to the coupled heights in L303: the phase-approximation argument fixes
r before letting a grow and gives no height estimate on the scale
exp(2r). The main endpoint and low-index gaps are unchanged. ∎

**Mathlib.** Full statement: not checked. Coverage of the Liouville
identity, twisted asymptotic, centered kernel moments and finite
prime-phase approximation is not checked; these are proved above.
The supporting nonvanishing theorem is recorded as present in L001:
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
L001 also records the supporting reciprocal identity and convergence:
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius)
and
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff).
Those sources were not rechecked. They support division by ζ on
Re s>1, not the full result here. Scalar inversion and Stirling-based
kernel bounds are supplied by L298 and L304, whose library coverage
is not checked. No full match or absence from checked sources is claimed.
