# Lemma 42: absolutely convergent Vandermonde expansion

**Hypotheses.** β_j=α_j^{-2} for Ξ as above, with indices counting multiplicity. Let d≥0 be fixed and H_d=(S_{m+n+2})_{0≤m,n≤d}.

**Conclusion.**

det H_d=Σ_{j_0<⋯<j_d}(Π_{r=0}^dβ_{j_r}²)Π_{0≤r<s≤d}(β_{j_s}-β_{j_r})²,

and the sum converges absolutely. These are algebraic squares, not modulus squares. Under RH every det H_d is strictly positive, but that unconditional sign has not been proved.

**Proof.** First keep only indices j≤N and define the (d+1)-by-N matrix V by V_{m,j}=β_j^{m+1}. The truncated Hankel matrix is VVᵀ, with transpose rather than conjugate transpose. The standard named Cauchy–Binet formula expresses det(VVᵀ) as the sum of squared determinants of its (d+1)-column submatrices. Factoring one β from each column leaves the standard Vandermonde determinant, giving exactly the finite version of the displayed formula.

Let R be a positive upper bound for all |β_j|, which exists by Σ|β_j|<∞. The absolute value of a summand is at most (2R)^{d(d+1)}Π_r|β_{j_r}|². The sum over increasing (d+1)-tuples of the latter products is at most (Σ_j|β_j|²)^{d+1}/(d+1)!, finite. Thus the infinite determinant expansion is absolutely convergent. Each entry of the truncated matrix converges absolutely to the corresponding S_{m+n+2}, and the determinant is a polynomial in finitely many entries, hence continuous. Passing N to infinity proves the identity. Repeated equal nodes contribute zero when both are selected, exactly as the Vandermonde factor prescribes; their other multiplicity contributions are counted by the indices.

Under RH all β_j are positive real. Lemma 27 gives infinitely many zeros, each of finite multiplicity, hence infinitely many distinct nodes. Every summand is nonnegative and at least one tuple of d+1 distinct nodes has strictly positive contribution. This proves strict positivity conditionally. For nonreal nodes, even one conjugate pair can make a square negative, as Lemma 34 demonstrates. ∎
