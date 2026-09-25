# The Dickson-cover K3 family with cubic real multiplication

Source checked on 2026-09-25. Surfaces and cycles are over C; cohomology coefficients are Q.

## Hypotheses

Let a, b_0, b_1, c_0, c_1 be very general complex parameters with a nonzero. Put

\[
P_a(t)=t^7-7at^5+14a^2t^3-7a^3t,
\qquad
S:\ y^2=x^3+(b_1P_a(t)+b_0)x+(c_1P_a(t)+c_0),
\]

and take the smooth minimal projective model. Write zeta = exp(2 pi i/7).

## Conclusion

S is an elliptic K3 surface with rho(S) = 4 and full transcendental endomorphism field

\[
\operatorname{End}_{\rm Hdg}(T(S))\simeq
\mathbb Q(\zeta+\zeta^{-1}).
\]

The family has dimension three in moduli. The form dx wedge dt/y spans H^(2,0)(S).

## Proof

The family, Picard rank, and full field are [van Geemen–Schütt, *On families of K3 surfaces with real multiplication*, Forum of Mathematics, Sigma 13 (2025), e2, Theorem 1.2(7), sections 5.3–5.4, especially equation (5.2) and its Dickson deformation](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=15). The introduction defines a family's RM field by equality for its very general member; Proposition 4.6 alone states only a field inclusion. Section 4.2 defines the Dickson polynomial, and section 4.5 identifies the holomorphic form. Singular parameters and assertions about every specialization are excluded.

The paper's [section 4.8](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=13) provides the known geometric correspondence. L006 checks its normalization and the resulting cycle span.

## Mathlib

Coverage: **not checked**. No full or supporting Mathlib match, or absence, is asserted.
