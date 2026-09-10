# Lemma 43: ordinary moment matrices are strictly positive definite

**Hypotheses.** d≥0 is an integer and G_d=(M_{2m+2n})_{0≤m,n≤d}, with the theta moments of Lemma 21.

**Conclusion.** G_d is positive definite for every d. This is not the same matrix as H_d=(S_{m+n+2}).

**Proof.** For a real vector (c_0,…,c_d), let q(X)=Σ_{m=0}^d c_mX^m. Finite expansion under the moment integral gives

Σ_{m,n=0}^d c_mc_nM_{2m+2n}=∫_0^∞K(u)q(u²)²du.

It converges by the fixed moment bounds and is nonnegative. If the vector is nonzero, q is a nonzero polynomial and has only finitely many real roots. Thus q(u²)² is strictly positive on some open interval in (0,∞), where K is strictly positive, and the integral is strictly positive. This is a genuine modulus-free square of a real-valued function; unlike the reciprocal-node expressions, its arguments are real. ∎
