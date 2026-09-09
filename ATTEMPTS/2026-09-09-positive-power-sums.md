# Attempt: all scalar reciprocal-power sums force real zeros

Date: 2026-09-09

Outcome: failed sufficient-condition guess; Lemmas 23–29 in PROOF.md retain the valid actual-Ξ identities and finite sign results.

For the actual Ξ, the theta bound proves a zero-free rectangle and then S_k>0 for k=1,…,6. The attempted stronger goal was to prove all S_k>0 and conclude RH solely from those signs.

Set a=10+i/4 and P(z)=(1-z²/25)(1-z²/a²)(1-z²/conj(a)²). With b=1/25 and c=a^{-2}, |c|<b/4, so the paired reciprocal sum T_k=b^k+2Re(c^k)>b^k(1-2·4^{-k})>0 for every k≥1. Yet P has nonreal zeros ±a and ±conj(a). Multiplying by cos(z/100) supplies infinitely many real zeros and order at most 1, while preserving the positive sums, alternating nonzero even Taylor coefficients, imaginary-axis positivity, and confinement of every zero to |Re z|>4 and |Im z|<1/2.

**WHY IT FAILS.** Positive scalar power sums can hide complex contributions behind a closer positive real node: the contribution b^k dominates the conjugate pair at every exponent. Even all scalar signs therefore do not characterize real zeros, including under the additional verified growth, symmetry, strip, and coefficient conditions listed here. The example is not asserted to have a positive theta kernel or zeta's arithmetic coefficients. A stronger test must combine different powers with coefficients of both signs, rather than merely checking each S_k separately.

Next lemma: derive the mixed quadratic-form tests Q(q)=Σ_jα_j^{-4}q(α_j^{-2})² and use polynomial interpolation to see whether they detect the hidden complex pair.
