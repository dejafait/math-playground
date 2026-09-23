# Lemma 154: moment information and a truncated-tail criterion

**Hypotheses.** Let S be the series of L149. On [T,2T] use probability
measure dt/T, write E_T and P_T for expectation and probability, and set

X_T(t)=T^(3/2)|S(t)|²,  L=log(2T).

Let K>0 be L149's second-moment constant. All statements below concern
sufficiently large T. Auxiliary random variables used as countermodels need
not have the series representation of S.

**Conclusion.** The following assertions hold.

1. E_T X_T=K+O(T^(−1/2)log T) and E_T X_T²=O(L).
   For any q>1 with finite q-th moment and any 0<θ<E_T X_T,

   P_T(X_T>θ) ≥ ((E_T X_T−θ)^q / E_T X_T^q)^(1/(q−1)).       (1)

   Interpolating only the established first and second moments gives
   E_T X_T^q=O_q(L^(q−1)) for 1<q≤2, hence the same order 1/L
   in (1). For q>2, an additional bound O_q(L^(q−1)) would still
   give that order through (1).

2. The abstract information E X=K and E X^q≤K^q L^(q−1) for
   every real q>1, simultaneously, permits P(X>θ)=1/L for each
   fixed θ>0 once L is sufficiently large. Thus even this entire
   collection of higher-moment upper bounds cannot, by itself, imply
   a measure lower bound whose ratio to T/L tends to infinity.

3. A sufficient additional estimate for a positive proportion for the actual
   S is: there exists a fixed M≥K/4 such that

   E_T[X_T 1_{X_T>M}] ≤ K/4                                (2)

   for all sufficiently large T. Under this explicitly unproved condition,

   meas{t∈[T,2T]: |S(t)|>sqrt(K/4) T^(−3/4)} ≥ K T/(4M).    (3)

   More generally a uniform bound E_T X_T^q≤C for any fixed q>1
   implies (2) for a sufficiently large fixed M. Neither this bound nor
   (2) is established here for S.

**Proof.**

Normalization gives E_T X_T=T^(1/2)∫_T^(2T)|S(t)|²dt and
E_T X_T²=T²∫_T^(2T)|S(t)|⁴dt. L149 and L153 prove assertion 1's
first two estimates. The series converges uniformly on each such compact
interval by L149, so X_T is bounded there and every fixed moment is finite;
this does not give a bound uniform in T.

Let A={X_T>θ}. Nonnegativity and Hölder's inequality give

E_T X_T ≤ θ + E_T[X_T 1_A]
        ≤ θ + (E_T X_T^q)^(1/q) P_T(A)^((q−1)/q).

Rearrangement proves (1). For 1<q<2, another application of Hölder,
with exponents 1/(2−q) and 1/(q−1), yields

E_T X_T^q = E_T[X_T^(2−q)(X_T²)^(q−1)]
          ≤ (E_T X_T)^(2−q)(E_T X_T²)^(q−1).

The asserted interpolation bound follows, and q=2 is already known.
For a fixed threshold θ<K, the numerator in (1) is bounded below by a
positive constant for large T. Substituting an upper bound C_q L^(q−1)
therefore yields c_q/L. This computes the guarantee from this bound;
it does not assert that the actual probability is of that size.

For assertion 2 take [0,1] with Lebesgue probability measure, L≥1, and set
Y_L=KL on [0,1/L], and Y_L=0 elsewhere. Direct integration gives

E Y_L=K,   E Y_L^q=K^q L^(q−1)  (q>1).

For every fixed θ>0 and L>θ/K, the set {Y_L>θ} has probability exactly
1/L. To express this in dyadic length units, the measurable function
T^(−3/4)sqrt(Y_L((t−T)/T)) on [T,2T] has squared normalized
amplitude Y_L. This is only an auxiliary family of functions, not an
identity or model theorem about S. It proves the stated failure of inference
from moment data alone. Bounds with larger logarithmic exponents also admit
this countermodel, provided their constants accommodate these values.

For assertion 3, L149 ensures E_T X_T≥3K/4 for sufficiently large T.
Set θ=K/4 and split into the three disjoint ranges X_T≤θ,
θ<X_T≤M, and X_T>M. Condition (2) gives

3K/4 ≤ E_T X_T ≤ K/4 + M P_T(X_T>θ) + K/4.

Thus P_T(X_T>θ)≥K/(4M), which is (3) after multiplying by T
and taking square roots in the event. If E_T X_T^q≤C uniformly,
then X_T 1_{X_T>M}≤M^(1−q)X_T^q. Choosing M≥K/4 so that
CM^(1−q)≤K/4 proves (2).

In contrast, L153 alone gives only

E_T[X_T 1_{X_T>M}] ≤ E_T X_T²/M ≤ C L/M.

This bound can ensure (2) by taking M proportional to L, which returns
only the already available order T/L in the same splitting argument.
It does not prove or disprove (2) for a fixed M. ∎

## Scope and verification

This resolves the information-theoretic part of the higher-moment question.
It does not rule out stronger fractional moments, additional arithmetic
structure, or direct distributional estimates for S. In particular it does
not identify the auxiliary spikes with S, infer any full-moment lower bound
from a multiplicative diagonal, or assert failure of positive proportion.
The fixed-tail estimate (2) is a sufficient target, not a necessary condition
for positive proportion. No pointwise nonvanishing or RH conclusion follows.

Verification is analytic: the two normalization powers, Hölder exponents,
exact spike integrals, the three-range split including threshold endpoints,
and the tail power inequality. No numerical certificate is required.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
