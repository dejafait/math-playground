# Lemma 56: every finite comparison-base Hankel matrix is positive definite

**Hypotheses.** G(z)=∫_R exp(-cosh(2u))e^{izu}du. Select its positive zeros α_j with multiplicity, and define β_j=α_j^{-2}, T_k=Σ_jβ_j^k, and H_d(G)=(T_{m+n+2})_{0≤m,n≤d}.

**Conclusion.** G has infinitely many distinct real zeros, Σ_jβ_j<∞, and H_d(G) is positive definite for every fixed d≥0.

**Proof.** Lemma 51 gives order at most 1; G(0)>0 and G is even. Lemma 54 proves all zeros real and nonzero. The named Hadamard theorem and exactly the pairing argument of Lemma 24 give G(z)=G(0)Π_j(1-z²/α_j²), with Σ_j|α_j|^{-2}<∞. The positive density g has finite and strictly positive moments of every even order, so its cosine Taylor series has every even coefficient nonzero and G is not a polynomial. A finite zero set would make the paired product a polynomial; thus G has infinitely many zeros, and hence infinitely many distinct zeros since every zero of a nonzero entire function has finite multiplicity.

All β_j are now strictly positive. For any nonzero real polynomial q, the convergent sum Σ_jβ_j²q(β_j)² is strictly positive: every term is nonnegative and q can vanish at only finitely many distinct nodes. Its convergence follows from Σβ_j<∞ and boundedness of q on the node set, as in Lemma 30. This sum is the quadratic form of H_d(G) when deg q≤d, proving positive definiteness for every fixed d. ∎
