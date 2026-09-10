# Lemma 1: an absolutely convergent reciprocal

**Hypotheses.** Re(s)=σ>1. Define μ(1)=1, μ(n)=0 if a prime square divides n, and μ(n)=(-1)^k if n is a product of k distinct primes.

**Conclusion.** M(s)=Σ_{n≥1} μ(n)n^{-s} converges absolutely and ζ(s)M(s)=1. In particular ζ(s)≠0.

**Proof.** Since |μ(n)|≤1, both series are dominated by Σ n^{-σ}<∞, whose convergence follows from the integral test. The double series for their product has sum of absolute values at most (Σ n^{-σ})². It can therefore be grouped by the product of the indices, giving

ζ(s)M(s)=Σ_{k≥1} k^{-s} Σ_{d|k} μ(d).

For k>1 with r distinct prime factors, the inner sum is Σ_{j=0}^r binom(r,j)(-1)^j=(1-1)^r=0. For k=1 it is 1. This proves the claim. No continuation of this reciprocal series to σ≤1 is asserted. ∎
