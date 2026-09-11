# Lemma 63: uniform growth and paired products for heat slices

**Hypotheses.** Let F(λ,z)=∫₀^∞e^{λu²}K(u)cos(zu)du be the theta deformation of Lemma 58. Fix L≥0 and R≥1, and let C be the explicit positive kernel-bound constant in that lemma.

**Conclusion.** Uniformly for real |λ|≤L and complex |z|≤R,

|F(λ,z)|≤(C/2)exp(2L²/π) exp((R/2+4)log(R/2+4)).                 (1)

The same bound holds for complex |λ|≤L. In particular each real-parameter slice has entire order at most one. For each fixed real λ, choose one representative α_j(λ) of each pair of zeros {α,-α}, with multiplicity. Then none is zero,

Σ_j |α_j(λ)|^{-2}<∞,

F(λ,z)=F(λ,0) Π_j(1-z²/α_j(λ)²),                              (2)

with locally uniform convergence in z and arbitrary ordering of the pairs. No assertion of reality, simplicity, or parameter-continuous indexing of the zeros is made.

## Proof

Lemma 58 gives joint entirety, evenness, and F(λ,0)>0 for real λ, as well as

K(u)≤C exp(9u/2-πe^{2u})  (u≥0).

The exponential series implies u²≤2e^u for u≥0. Completing a square gives, with t=e^u,

Lu²-(π/2)e^{2u}≤2Lt-(π/2)t²
=2L²/π-(π/2)(t-2L/π)²≤2L²/π.

Since |cos(zu)|≤e^{Ru}, the absolute value of the integral is therefore at most

C exp(2L²/π) ∫₀^∞ exp((R+9/2)u-(π/2)e^{2u})du
=(C/2)exp(2L²/π) ∫₁^∞ x^{a-1}e^{-(π/2)x}dx,

where a=(R+9/2)/2. Put m=ceil(a). Because π/2>1, and x≥1, this last integral is bounded by

∫₀^∞ x^m e^{-x}dx=m!≤m^m.

Here m≤R/2+13/4<R/2+4, and y log y is increasing for y≥1, proving (1). The bound is O_L(R log R) after taking a logarithm. Thus, for B_λ(R)=max_{|z|≤R}|F(λ,z)|,

limsup_{R→∞} log log(max(e,B_λ(R)))/log R≤1.

For clarity, apply the standard named Hadamard factorization theorem in the same order-at-most-one form used in Lemma 24: an entire f of order at most one with f(0)≠0 has square-summable reciprocal zeros ρ and representation

f(z)=f(0)e^{bz} Π_ρ E₁(z/ρ),  E₁(w)=(1-w)e^w,

where b=f'(0)/f(0). This includes the possibility of finitely many zeros. For our fixed real λ, positivity at zero verifies the nonvanishing hypothesis, and evenness gives b=0 and opposite zeros with equal multiplicities. Pairing is justified by the logarithmic estimate used in Lemma 24: for |w|≤1/2,

|log E₁(w)|=|−Σ_{k≥2}w^k/k|≤2|w|².

On any fixed compact z-disc only finitely many zeros fall outside this tail estimate, and reciprocal-square summability makes the remaining logarithms absolutely uniformly summable. Hence reordering and pairing are legitimate, and E₁(z/α)E₁(−z/α)=1-z²/α² proves (2). The sum for pair representatives is half the sum over all zeros. ∎

## Qualifications and verification

The uniform estimate concerns function growth; the product assertion is for each fixed real λ. It supplies neither a parameter-uniform zero enumeration nor the boundary lower bounds in the conditional continuation criterion. It does not prove initial global reality or reality at λ=0. The original main RH gap is unchanged.

The proof requires no numerical certificate. Direct checks are the completed-square inequality, the substitution x=e^{2u}, the factorial majorant, and the vanishing linear exponential factor. Formalization would require those inequalities uniformly in L,R, the order bound, the stated Hadamard theorem, multiplicity pairing by evenness, and absolute locally uniform logarithmic-tail convergence.
