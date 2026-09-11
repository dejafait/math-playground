# Lemma 181: positive quartic stationary product strip

**Hypotheses.** Use the block, profiles, weights and kernels of L180.
Write t−=2T−h, t+=2T, a±=(t±−π/2)/(2π), and
J=[2log a−,2log a+]. For an integer quadruple n in I⁴ put
k=n1*n2*n3*n4 and δ(k)=dist(log k,J). Constants below may depend
on the fixed profiles and on the comparison constants in h≍N^(3/2).
All assertions hold for sufficiently large real N; N need not be integral.

**Conclusion.** The all-positive kernel K_2(log(k/N⁴)) has a stationary
point in the closed block exactly when

                         a−²≤k≤a+².                         (1)

Uniformly in k it is O(N/h). For δ(k)>0 it is also O(1/(hδ(k))).
Partition the quadruples into S satisfying (1), the exterior collar C
with 0<δ(k)≤1/N, and the far exterior E with δ(k)>1/N. Define

A_R=N^(−2) Σ_(n∈R) w(n) K_2(log(k/N⁴)).

Then the following bounds hold even with absolute values inside each sum:

|A_S|=O(N),  |A_C|=O(N²/h),  |A_E|=O((N²/h)log(2N)).             (2)

Thus the exterior is O(N^(1/2)log(2N)); the stationary portion is
only O(N) by this calculation. Its signed cancellation remains unresolved.
The all-positive and all-negative terms together contribute
−Re(A_S+A_C+A_E)/8 to L180's mixed moment.

**Proof.**

For u=log(k/N⁴), let φ(t)=(t−π/2)u−2θ(t). L180 gives

φ'(t)=log(k/a(t)²),    φ''(t)=−2/(t−π/2).

On B, −φ'' lies between positive constant multiples of N^(−2).
The derivative is strictly decreasing, so its zero is exactly at
 t=2π sqrt(k)+π/2. This proves (1), including endpoint zeros.
If there is no zero in B, min_B|φ'|=δ(k).

Here are elementary integral bounds, including the transition region.
On any subinterval where φ' has one sign and |φ'|≥λ,
integration by parts gives

∫ exp(iφ)dt=[exp(iφ)/(iφ')] + ∫ exp(iφ)φ''/(i(φ')²)dt.

The two boundary terms have total modulus at most 2/λ. Monotonicity
of φ' bounds the integral of |φ''|/|φ'|² by 2/λ (in fact 1/λ
suffices when its sign is fixed). This proves an O(1/λ) bound.
For the uniform estimate remove the interval where |φ'|≤1/N.
Its length is O(N), by the lower bound for |φ''|. The complement
has at most two intervals, each with integral O(N) by the preceding
calculation. The removed interval also contributes O(N) by its length.
Division by h proves O(N/h). With λ=δ(k), the same integration by
parts on all of B proves the stated nonstationary bound.

For clarity the arithmetic count uses only the actual integer window.
Fix n1,n2,n3. As the last integer n4 increases in [N,2N], consecutive
values of log k differ by log(1+1/n4)≥c/N. Consequently any interval
of log-products of length L contains at most C(NL+1) choices of n4.
There are O(N³) choices of the first three indices. This also covers
nonintegral N and closed endpoints.

The length of J is 2log(a+/a−)=O(h/N²). Hence

#S≤C(N²h+N³).

The exterior collar is two intervals of length 1/N, giving #C=O(N³).
Since |w| is bounded, multiplication by N^(−2)N/h proves
|A_S|≤C(N+N²/h)=O(N) and |A_C|≤CN²/h.

For the exterior use shells j/N<δ(k)≤(j+1)/N, j≥1, assigning
boundary points to either adjacent shell consistently. Each shell is
the union of two intervals of length 1/N and contains O(N³)
quadruples. All log k and J lie within a bounded distance of 4log N,
so there are O(N) nonempty shells. The kernel bound in shell j is
CN/(hj). Summing their absolute contributions gives

N^(−2) C N³ Σ_(1≤j≤CN) N/(hj)
                 ≤ C(N²/h)log(2N).

This proves (2). Finally the weights are real and the negative-sign
kernel is the conjugate of the positive-sign kernel. Both have s3*s4=1
in L180's expansion, so their combined coefficient is −1/8. ∎

## Scope, verification, and formalization obligations

The stationary product strip has width O(N²h) in product coordinates;
it cannot be replaced by exact equal-product resonances. This lemma
isolates, but does not estimate sharply, its signed contribution.
The O(N) bound does not improve L180's bound for the full mixed moment,
which uses a different argument. No lower bound or impossibility of
cancellation is asserted. First-moment decay and RH remain unproved.

Verification is analytic: phase derivatives, endpoint stationary criterion,
integration-by-parts boundary terms, derivative transition length, integer
spacing, shell endpoints, normalization and conjugate coefficient were
checked explicitly above. Formalization would require finite sums,
compact oscillatory integration, the monotone spacing count and a harmonic
sum bound. No numerical certificate is used.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
