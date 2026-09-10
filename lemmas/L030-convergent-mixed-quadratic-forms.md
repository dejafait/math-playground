# Lemma 30: convergent mixed quadratic forms

**Hypotheses.** β_j=α_j^{-2} as in Lemma 24 and q(X)=Σ_{m=0}^d c_mX^m has real coefficients. Define Q(q)=Σ_jβ_j²q(β_j)²; the square here is algebraic, not absolute-value squared.

**Conclusion.** Q(q) converges absolutely, is real, and

Q(q)=Σ_{m,n=0}^d c_mc_n S_{m+n+2}.

If RH holds, Q(q)≥0 for every real polynomial q. Thus RH implies positive semidefiniteness of every real Hankel matrix H_d=(S_{m+n+2})_{0≤m,n≤d}.

**Proof.** Lemma 24 gives Σ_j|β_j|<∞, hence the β_j are bounded and Σ_j|β_j|²<∞. Any fixed polynomial is bounded on a closed disk containing them, so Σ_j|β_j²q(β_j)²|<∞. Expand the finite polynomial square and interchange only a finite sum with this absolutely convergent series to obtain the identity. The S_k are real by Lemma 25, so Q(q) is real. Under RH all α_j are real and nonzero, hence β_j>0 and every β_j²q(β_j)² is nonnegative. The matrix assertion is precisely the definition of positive semidefiniteness, since cᵀH_dc=Q(q). Without RH, replacing q(β_j)² by |q(β_j)|² would change the expression and would not prove the stated sign. ∎
