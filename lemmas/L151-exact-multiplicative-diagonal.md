# Lemma 151: exact multiplicative diagonal has one logarithm

**Hypotheses.** Use the weights of L149,

b_n(t)=c₀ n^(−2)exp(−log(n/N_t)²), c₀=exp(π²/16), N_t=sqrt(t/(2π)),

and put a_k(t)=Σ_{mn=k}b_m(t)b_n(t).

**Conclusion.** There are absolute constants c,C>0 such that, for all sufficiently large T,

c T^(−2)log T ≤ ∫_T^(2T)Σ_k a_k(t)²dt ≤ C T^(−2)log T.

Thus the exact multiplicative diagonal already has a logarithmic excess over T^(−2). This is not a lower bound for the full fourth moment: the integrated off-diagonal terms need not be nonnegative.

**Proof.**

Fix N≥1 and write b_n=c₀n^(−2)exp(−log(n/N)²) and D(N)=Σ_k(Σ_{mn=k}b_m b_n)². All terms are nonnegative, and their total is bounded by (Σ_n b_n)^4<∞. Tonelli therefore permits every regrouping below.

Every solution mn=pq has a unique parametrization

m=gr, p=gs, n=hs, q=hr, with gcd(r,s)=1.

Indeed take g=gcd(m,p); the equality rn=sq and coprimality give n=hs and q=hr. Consequently

D(N)=Σ_{gcd(r,s)=1}(Σ_{g≥1}b_{gr}b_{gs})²
 =c₀⁴Σ_{gcd(r,s)=1}(rs)^(−4)exp(−log(r/s)²)H(N/sqrt(rs))²,       (1)

where H(X)=Σ_{g≥1}g^(−4)exp(−2log(g/X)²). The identity in the exponent follows by expanding two squares about their midpoint.

### One-dimensional weight bounds

For X≥1, integration and total variation of h_X(x)=x^(−4)exp(−2log(x/X)²), extended by zero at x=0, give

∫₀^∞h_X(x)dx=C₁X^(−3),  ∫₀^∞|h_X'(x)|dx=C₂X^(−4).

Both constants are finite by substituting x=X exp(y); the resulting integrands are a Gaussian times an exponential and, for the derivative, an absolute linear factor. Comparing h_X(g) to its integral on [g−1,g] proves H(X)≤C X^(−3). For 0<X<1 use exp(−2(log z)²)≤C z^(−2), z>0 (complete the square in log z). This gives H(X)≤C X²Σ_g g^(−6)≤C X^(−1). Together,

H(X)≤C X^(−3) min(1,X²),   X>0.                         (2)

For X≥2 there are at least X/2 integers in [X,2X]. Each contributes at least (2X)^(−4)exp(−2(log 2)²), so

H(X)≥c X^(−3),   X≥2.                                  (3)

### Upper bound, including the tails

By (1) and (2), dropping coprimality only increases the bound:

D(N)≤C N^(−6)Σ_{r,s≥1}(rs)^(−1)exp(−log(r/s)²)
                         ·min(1,N⁴/(rs)²).             (4)

Partition r and s into [2^j,2^(j+1)) and [2^k,2^(k+1)), j,k≥0. The sum of 1/r over each such block is at most 1. On a block,

exp(−log(r/s)²)≤C exp(−c(j−k)²),
min(1,N⁴/(rs)²)≤min(1,N⁴2^(−2(j+k))).

Here |log(r/s)|≥max(0,|j−k|−1)log 2, which proves the first estimate with some fixed positive c. Set d=|j−k| and v=min(j,k); there are at most two blocks for each pair (d,v). For fixed d the sum over v is bounded above by

Σ_{v≥0}min(1,N⁴2^(−4v))=O(1+log N):

the terms up to floor(log₂ N) are at most one and the remaining geometric tail is bounded. Summing exp(−cd²) over d proves

D(N)≤C N^(−6)(1+log N).                                 (5)

### Lower bound from coprime squares

For integer R≥2, the square R≤r,s<2R contains R² ordered pairs. If a pair is not coprime, some integer 2≤d≤2R divides both coordinates. The number of multiples of d in the interval is at most R/d+1. The union bound gives at most

Σ_{d=2}^{2R}(R/d+1)²
 ≤(3/4)R²+2R(1+log(2R))+2R

noncoprime pairs. We used Σ_{d=2}^∞d^(−2)≤1/4+∫₂^∞x^(−2)dx=3/4 and the elementary harmonic bound. Hence for every sufficiently large R the square contains at least R²/8 coprime pairs.

Restrict (1) to such pairs with R≤N/4. Then N/sqrt(rs)≥2, |log(r/s)|≤log 2 and rs≤4R². Equation (3) makes each term in (1) at least cN^(−6)/(rs)≥c' N^(−6)/R². Each square thus contributes at least c''N^(−6). The squares with R=2^j, R above a fixed threshold and R≤N/4, are disjoint and number at least c'''log N for sufficiently large N. Therefore

D(N)≥c N^(−6)log N.                                    (6)

Finally, uniformly on t∈[T,2T], N_t^(−6) is comparable to T^(−3) and log N_t to log T. Integrating (5) and (6) over this interval proves the conclusion. ∎

## Scope, verification, and formalization obligations

The bound sharpens only the exact diagonal in the fourth-moment expansion. It neither determines the full fourth moment nor rules out a positive-proportion large-value set. No pointwise lower bound or RH conclusion follows.

Verification is analytic: unique coprime parametrization, the Gaussian midpoint identity, sum/integral variation, the small-X power bound, convergent dyadic tails, the elementary common-divisor union bound, and uniform conversion from N_t to T. No numerical certificate is needed. Formalization would require these statements and nonnegative-series regrouping. L149 supplies the weights; no fourth-moment estimate or unproved cancellation claim is used.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
