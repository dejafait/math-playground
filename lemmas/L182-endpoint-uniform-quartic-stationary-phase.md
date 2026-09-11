# Lemma 182: endpoint-uniform quartic stationary phase

**Hypotheses.** Use L181's block, stationary set S, real weights w,
normalization A_S and integer product k. In particular h≍N^(3/2).
Use the exact phase of L179,
θ(t)=s log(s/(2πN²))−s−π/4, where s=t−π/2.
Write s±=t±−π/2. For each stationary product k put

s0=2π sqrt(k),
z±=sign(s±−s0) sqrt(2[s± log(s±/s0)−s±+s0]),
F(x,y)=∫_x^y exp(−iz²) dz.

The continuous value at s±=s0 is zero. All estimates below are uniform
for s0∈[s−,s+], including equality at either endpoint.

**Conclusion.** The stationary kernel has the expression

K_2(log(k/N⁴))
 = exp(i(4π sqrt(k)+π/2)) sqrt(2π sqrt(k))/h * F(z−,z+)
   + O(1/h).                                                     (1)

Define the finite signed product weight

W(k)=Σ_(n∈I⁴: n1*n2*n3*n4=k) w(n).

Then

A_S = (N²h)^(−1) Σ_(integer k∈[a−²,a+²])
 W(k) sqrt(2π sqrt(k)) exp(i(4π sqrt(k)+π/2)) F(z−,z+)
 + O(1).                                                        (2)

The remainder estimate in (2) holds after taking absolute values of the
individual weighted errors. Formula (2) retains the endpoint transition;
no cancellation estimate for its displayed product sum is asserted.

**Proof.**

With u=log(k/N⁴), the kernel phase is

φ(s)=su−2[s log(s/(2πN²))−s−π/4].

Its derivative vanishes at s0, and substitution gives
φ(s0)=2s0+π/2. Direct subtraction yields the exact identity

φ(s)−φ(s0)=−2[s log(s/s0)−s+s0].                                 (3)

Here s,s0≍N² and |s−s0|≤h throughout the stationary block.
We justify a smooth quadratic coordinate, including at the saddle.
Put x=(s−s0)/s0 and

f(x)=(1+x)log(1+x)−x,
v=sign(x)sqrt(2f(x)).

Since f(0)=f'(0)=0 and f''(x)=1/(1+x), the function
2f(x)/x² extends smoothly and positively near zero with value 1.
Thus v=x sqrt(2f(x)/x²) is smooth with derivative 1 at zero.
It has a smooth inverse x=H(v) on a fixed neighborhood of zero,
with H(0)=0 and H'(0)=1. All derivatives needed here are bounded
on a smaller fixed closed neighborhood. This applies uniformly on
our blocks since |x|≤h/s0=O(N^(−1/2)).

Set z=sqrt(s0)v, which is exactly the coordinate in the statement.
Then (3) becomes φ(s)=φ(s0)−z² and

ds/dz=sqrt(s0)H'(z/sqrt(s0))
      =sqrt(s0)+z g(z/sqrt(s0)),                                 (4)

where g(v)=(H'(v)−1)/v extends smoothly at zero. In particular
|g|+|g'|≤C on the relevant fixed neighborhood. The transformation is
increasing, so the integral runs from z− to z+. Moreover
|z±|≤C h/sqrt(s0) and z−≤0≤z+.

The error in replacing (4) by sqrt(s0) in the unnormalized kernel is,
apart from a unit factor,

R=∫_(z−)^(z+) z g(z/sqrt(s0)) exp(−iz²) dz.

Use d exp(−iz²)=−2iz exp(−iz²) dz. Integration by parts gives

R=−[g(z/sqrt(s0)) exp(−iz²)]_(z−)^(z+)/(2i)
  +(2i sqrt(s0))^(−1)∫_(z−)^(z+) g'(z/sqrt(s0)) exp(−iz²) dz.

Consequently |R|≤C+C(z+−z−)/sqrt(s0)≤C(1+h/s0)=O(1).
There is no singular boundary term at z=0. Division by h proves (1).
In particular no full-line Fresnel integral has been substituted for the
finite one: the estimate remains valid when a saddle meets an endpoint.
For example s0=s− gives z−=0 exactly; that transition is not an error
term being silently discarded. The finite Fresnel integral is uniformly
bounded: bound its part in [−1,1] by length, and integrate by parts using
−2iz on each exterior part to bound those tails. Thus its scale is also
consistent with L181's uniform kernel bound.

All sums are finite. Grouping equal products in (1) gives the displayed
main term in (2). Boundedness of w and L181's count
#S≤C(N²h+N³) bound the accumulated error by

C #S/(N²h) ≤ C(1+N/h)=O(1).

This proves (2) with absolute error control, without any assumption on
the signs or cancellation of W(k). ∎

## Scope, verification, and formalization obligations

The saddle phase contains the exact additive π/2. The square-root phase
and finite endpoint factors must both remain when estimating the signed
integer product sum. Formula (2) does not itself improve the O(N)
absolute stationary bound, nor give a lower bound. The combined
all-positive/all-negative stationary term in the mixed moment is still
−Re(A_S)/8 as in L181. First-moment decay, uniform integrability,
cutoff covariance and RH remain unproved; the overall argument is unchanged.

Verification is analytic: exact phase subtraction, the smooth inverse
at zero, the Jacobian, both integration-by-parts endpoint terms, and the
absolute accumulated error are proved above. No numerical assertion is
needed. Formalization would require the local smooth inverse theorem,
compact substitution and integration by parts, and finite grouping by
integer products with L181's counting bound.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
