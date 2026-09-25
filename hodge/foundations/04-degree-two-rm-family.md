# The elliptic K3 family with quadratic real multiplication

Source checked on 2026-09-25. All surfaces and algebraic cycles are over C; cohomology coefficients are Q.

## Hypotheses

Take very general polynomials alpha(s), beta(s) with deg(alpha) <= 1 and deg(beta) <= 3 in the family below. Let S be its smooth minimal projective model, and put

\[
a(t)=t\alpha(t^2),\qquad b(t)=\tfrac12a(t)^2+t\beta(t^2),\qquad
S:\ y^2=x(x^2+2a(t)x+b(t)).
\]

## Conclusion

S is a projective K3 surface, rho(S) = 10, and its full transcendental endomorphism field is End_Hdg(T(S)) = Q(sqrt(2)). The family has dimension four in moduli. On the displayed chart, dx wedge dt/y represents a generator of H^(2,0)(S).

## Proof

Use Bert van Geemen and Matthias Schütt, *On families of K3 surfaces with real multiplication*, Forum of Mathematics, Sigma 13 (2025), e2, [Proposition 6.2, second case, and section 6.4, pp. 18–19](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=18), also Theorem 1.3(2). The introduction's family convention means equality with the full field for a very general member. Degenerate parameters and every-specialization claims are excluded.

This citation supplies the family and field, not the cycle-span conclusion of L005. The coordinate normalization in section 6.4 is checked and corrected for its stated direction in L005.

## Mathlib

Coverage: **not checked**. No full or supporting Mathlib match, or absence, is asserted.
