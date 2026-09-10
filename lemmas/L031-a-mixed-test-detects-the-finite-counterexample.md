# Lemma 31: a mixed test detects the finite counterexample

**Hypotheses.** b=1/25, c=(10+i/4)^{-2}, and T_k=b^k+c^k+conj(c)^k, as in Lemma 29.

**Conclusion.** There is a real polynomial q of degree at most two such that

b²q(b)²+c²q(c)²+conj(c)²q(conj(c))²=-2.

Thus the 3-by-3 Hankel matrix (T_{m+n+2})_{0≤m,n≤2} is not positive semidefinite, although all T_k>0.

**Proof.** The three nodes b,c,conj(c) are distinct because b is real and c is nonreal. Define

L_c(X)=(X-b)(X-conj(c))/[(c-b)(c-conj(c))],

L_conj(c)(X)=(X-b)(X-c)/[(conj(c)-b)(conj(c)-c)],

q(X)=(i/c)L_c(X)-(i/conj(c))L_conj(c)(X).

The two Lagrange basis polynomials have conjugate coefficients, and the two scalar coefficients are conjugates, so q has real coefficients. Its values are q(b)=0, q(c)=i/c, and q(conj(c))=-i/conj(c). Substitution makes the three terms 0,-1,-1. The Hankel identity is the finite version of Lemma 30, proving the matrix claim. ∎
