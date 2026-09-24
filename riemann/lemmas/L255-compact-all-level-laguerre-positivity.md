# Lemma 255: compact all-level generalized Laguerre positivity

**Hypotheses.** Let Ξ have the unconditional paired product of L024 and the zero localization of L026. For real x define D_n(Ξ;x) to be the coefficient of y^(2n) in Ξ(x+iy)Ξ(x−iy). Equivalently,

D_n(Ξ;x)=Σ_{k=0}^{2n} (−1)^(n+k) Ξ^(k)(x)Ξ^(2n−k)(x)/(k!(2n−k)!).

**Conclusion.** For every integer n≥1 and every real |x|≤7/2, D_n(Ξ;x)>0. In particular the second expression Ξ″²/4−Ξ′Ξ‴/3+ΞΞ⁗/12 is strictly positive on that interval. More generally the proof applies at any real nonzero point of Ξ where every nonreal zero a+ib obeys |x−a|>|b|. This condition is sufficient, not necessary.

**Proof.** Fix such an x. Exhaust the paired product of L024 by finite sets closed under conjugation, retaining multiplicities. This is permitted by its absolutely convergent logarithmic tails. Write the resulting real even polynomials as P_N; they converge locally uniformly to Ξ. There are no zeros at x for the interval in the conclusion by L026. In the general assertion this is assumed. Thus

P_N(x+iy)P_N(x−iy)/P_N(x)² → Ξ(x+iy)Ξ(x−iy)/Ξ(x)²

locally uniformly for complex y. Denominators are nonzero, and converge to Ξ(x)²>0. Coefficients consequently converge by the Cauchy integral formula. The use of complex y here is an analytic product, not complex conjugation; for real y it equals the normalized squared modulus.

Factor each finite real polynomial into real linear factors and conjugate quadratic factors. A real zero r contributes to its normalized product the factor

1+y²/(x−r)².

A conjugate pair a±ib, b≠0, contributes, with u=x−a,

[((u+iy)²+b²)((u−iy)²+b²)]/(u²+b²)²
 =1+[2(u²−b²)/(u²+b²)²]y²+y⁴/(u²+b²)².

The constant multipliers in the polynomial cancel in its normalized product. Every displayed factor has constant coefficient 1 and nonnegative coefficients in y²; its linear coefficient in y² is strictly positive under |u|>|b|. Repeated zeros merely repeat factors. On |x|≤7/2, L026 gives

|x−a|≥|a|−|x|>4−7/2=1/2>|b|,

so the condition holds for every nonreal zero, with strict inequalities even at the endpoints.

By L027 there are infinitely many zeros counted with multiplicity, hence infinitely many such real or conjugate blocks. For fixed n take a finite initial product containing at least n blocks. The coefficient of y^(2n) is strictly positive: the product of the positive y² coefficients of any n distinct blocks is one of its summands. Every later block has constant coefficient 1 and nonnegative other coefficients, so the coefficient cannot decrease as the exhaustion grows. Its convergent limit is therefore strictly positive. Multiplication by Ξ(x)² proves the result. The Taylor coefficient formula follows directly by multiplying the two entire Taylor series; the factors i^k(−i)^(2n−k) equal (−1)^(n+k). ∎

The achieved bound covers every level but only a fixed real interval. The required associated-kernel criterion concerns every level at every real argument; the main reciprocal-node mixed positivity is also unproved. The condition can fail near the real center of a hypothetical nonreal zero. Increasing n on this compact interval does not remove that spatial gap. No positive Fourier spectrum on the whole line, positive Stieltjes representation, or RH conclusion is asserted. This is distinct from L246's scalar signs on the squared imaginary axis and from the finite Hankel certificates.

**Mathlib.** Not checked: coverage of the full statement and supporting local-uniform coefficient convergence and polynomial-factor identities was not looked up. No matching theorem is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
