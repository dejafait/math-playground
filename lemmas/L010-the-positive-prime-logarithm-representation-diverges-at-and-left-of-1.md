# Lemma 10: the positive prime-logarithm representation diverges at and left of 1

**Hypotheses.** 0<σ≤1 is real.

**Conclusion.** Σ_p1/p=∞, and Σ_pΣ_{k≥1}p^{-kσ}/k=∞. For complex s with 0<Re(s)≤1, the corresponding double series is not absolutely convergent.

**Proof.** Suppose Σ_p1/p were finite. For each prime p,

Σ_{k≥1}p^{-k}/k ≤ 1/(p-1) ≤ 2/p.

Hence the finite products Π_{p≤X}(1-1/p)^{-1} would be bounded independently of X by exp(2Σ_p1/p). Expanding each finite product as convergent geometric series shows it is at least Σ_{1≤n≤X}1/n: every such integer has all its prime factors ≤X. The harmonic sums are unbounded (by integral comparison), a contradiction. For 0<σ≤1 the k=1 terms satisfy p^{-σ}≥1/p, proving divergence of the nonnegative double sum. Absolute values of p^{-ks}/k equal p^{-k Re(s)}/k, proving the complex assertion. This makes no claim about conditional convergence at individual nonreal points. ∎
