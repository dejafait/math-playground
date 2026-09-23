# Lemma 25: moment coefficients and reciprocal-zero power sums

**Hypotheses.** α_j are the representatives in Lemma 24, and M_{2n} are as in Lemma 21. Define S_k=Σ_jα_j^{-2k} for integers k≥1.

**Conclusion.** All S_k converge absolutely and are real. In particular

S_1=M_2/(2M_0),

S_2=(3M_2²-M_0M_4)/(12M_0²).

If RH holds, then S_k≥0 for every k≥1, so M_0M_4≤3M_2² is a necessary consequence of RH. No sufficiency is claimed.

**Proof.** Because Ξ(0)=M_0>0 and Ξ is continuous, choose δ>0 so that Ξ has no zero in |z|<δ. Thus |α_j|≥δ. Put A=Σ_j|α_j|⁻²<∞, supplied by Lemma 24. For every k≥1,

Σ_j|α_j|⁻²ᵏ≤δ⁻²⁽ᵏ⁻¹⁾A<∞.

Fix 0<r<δ and put θ=r²/δ²<1. On |z|≤r the double logarithm series satisfies

Σ_j Σ_{k≥1} |z/α_j|²ᵏ/k ≤ r²A/(1-θ).

Indeed |z/α_j|²≤θ and Σ_{k≥1}t^k/k≤t/(1-θ) for 0≤t≤θ. This bound gives absolute uniform convergence on each such closed disk. Define the holomorphic function

L(z)=-Σ_j Σ_{k≥1} z²ᵏ/(kα_j²ᵏ)=-Σ_{k≥1} S_k z²ᵏ/k.

For each finite head of the j sum, exponentiating gives the corresponding paired product, since each factor logarithm is normalized to vanish at 0. Passing to the locally uniform limit and using Lemma 24 gives exp L(z)=Ξ(z)/M_0. Also L(0)=0, so L is precisely the unique analytic logarithm with that normalization on |z|<δ. This uses no global logarithm or real-zero assumption. Lemma 21 gives Ξ(conjugate z)=conjugate Ξ(z). Consequently conjugate L(conjugate z) is another normalized logarithm of the same function and equals L; its Taylor coefficients, and hence all S_k, are real. This does not require the selected α representatives themselves to be closed under conjugation.

The moment expansion from Lemma 21 gives Ξ(z)/M_0=1-a z²+b z⁴+O(z⁶), where a=M_2/(2M_0) and b=M_4/(24M_0). Its logarithm is -a z²+(b-a²/2)z⁴+O(z⁶). The z² and z⁴ coefficients above are -S_1 and -S_2/2, respectively, so S_1=a and S_2=a²-2b. Substitution proves the displayed formulas. Under RH every α_j is real and nonzero by Lemma 18, so every term of each S_k is positive. The asserted nonnegative sign and the necessary moment inequality follow conditionally.

The unconditional Cauchy–Schwarz inequality in Lemma 21 gives M_2²≤M_0M_4, which is a lower bound and does not give the needed upper bound M_0M_4≤3M_2². ∎

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
