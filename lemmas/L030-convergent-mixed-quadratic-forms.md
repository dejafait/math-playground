# Lemma 30: convergent mixed quadratic forms

**Hypotheses.** β_j=α_j^{-2} as in Lemma 24 and q(X)=Σ_{m=0}^d c_mX^m has real coefficients. Define Q(q)=Σ_jβ_j²q(β_j)²; the square here is algebraic, not absolute-value squared.

**Conclusion.** Q(q) converges absolutely, is real, and

Q(q)=Σ_{m,n=0}^d c_mc_n S_{m+n+2}.

If RH holds, Q(q)≥0 for every real polynomial q. Thus RH implies positive semidefiniteness of every real Hankel matrix H_d=(S_{m+n+2})_{0≤m,n≤d}.

**Proof.** Lemma 24 gives A=Σ_j|β_j|<∞. Choose B=max(1,A), so |β_j|≤B and Σ_j|β_j|²≤BA. For the fixed polynomial q put C_q=Σ_{m=0}^d |c_m|B^m. Then |q(β_j)|≤C_q and

Σ_j|β_j²q(β_j)²|≤C_q²BA<∞.

This bound also covers an empty node multiset (A=0). Each expanded monomial series converges absolutely, since Σ_j|β_j|^{m+n+2}≤B^{m+n+1}A. Expanding the finite polynomial square and interchanging its finite sum with the absolutely convergent node series therefore gives

Q(q)=Σ_{m,n=0}^d c_mc_n Σ_jβ_j^{m+n+2}=Σ_{m,n=0}^d c_mc_n S_{m+n+2}.

The index shift is two because of the weight β_j². The S_k are real by Lemma 25, so Q(q) is real. Under RH all α_j are real and nonzero, hence β_j>0 and every β_j²q(β_j)² is nonnegative. Absolute convergence then gives Q(q)≥0. The matrix assertion is precisely the definition of positive semidefiniteness, since cᵀH_dc=Q(q). Without RH, replacing q(β_j)² by |q(β_j)|² would change the expression and would not prove the stated sign. ∎

The convergence bound depends on the fixed polynomial and provides no sign, even in one degree. The required downstream statement is Q(q)≥0 for every real polynomial for the actual nodes; the bound above is not an estimate toward that inequality. This review changes neither the statement nor its mathematical inputs.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
