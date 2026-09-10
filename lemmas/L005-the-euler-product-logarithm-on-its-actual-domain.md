# Lemma 5: the Euler-product logarithm on its actual domain

**Hypotheses.** Re(s)>1. The index p runs over primes and k over positive integers.

**Conclusion.** L(s)=Σ_p Σ_{k≥1} p^{-ks}/k converges absolutely, locally uniformly on Re(s)>1, and exp(L(s))=ζ(s). Consequently Re L(s)=log|ζ(s)|. For real σ>1, L(σ)=log ζ(σ).

**Proof.** On Re(s)≥1+δ, δ>0, the absolute sum is at most

Σ_p p^{-(1+δ)}/(1-p^{-(1+δ)}) ≤ (1-2^{-(1+δ)})^{-1} Σ_{n≥2} n^{-(1+δ)} < ∞.

This is a uniform majorant. For a finite set of primes p≤X, the power-series identity exp(Σ_{k≥1} z^k/k)=(1-z)^{-1}, |z|<1, gives exp(L_X(s))=Π_{p≤X}(1-p^{-s})^{-1}. Expanding the finitely many absolutely convergent geometric series and applying unique factorization identifies this product with the sum of n^{-s} over integers all of whose prime factors are ≤X. The difference from ζ(s) has absolute value at most Σ_{n>X} n^{-Re(s)}, since any omitted integer has a prime factor >X and hence is >X. This tends to zero, uniformly on Re(s)≥1+δ. Taking the limit proves exp L=ζ. Taking absolute values gives exp(Re L)=|ζ| and thus the real-logarithm identity, with no choice of a complex logarithm required. For real σ the positive Dirichlet series makes the final identity immediate. ∎
