# L005 — A degree-two graph realizes the quadratic real-multiplication field

## Hypotheses

Let S be a very general smooth projective K3 member of the real-multiplication family in [the family input](../foundations/04-degree-two-rm-family.md). Thus, on a Weierstrass chart,

\[
a(t)=t\alpha(t^2),\quad b(t)=\tfrac12a(t)^2+t\beta(t^2),\quad
y^2=x(x^2+2a(t)x+b(t)),
\]

with deg(alpha) <= 1, deg(beta) <= 3, and the **full** field E = End_Hdg(T(S)) equal to Q(sqrt(2)). Write V = H^2(S,Q), N = NS(S)_Q, T = N perpendicular to the cup-product form q, rho = dim_Q N = 10, and X = S x S. Let D^2(X) be the span of products of rational divisor classes. Fix an ample divisor class h on S and H = pi_1^*h + pi_2^*h on X.

Choose the positive real square root sqrt(2). Define on a dense open chart

\[
u=x+2a(t)+\frac{b(t)}x,\qquad
v=y\left(1-\frac{b(t)}{x^2}\right),\qquad
f(x,y,t)=\left(\frac u2,\frac{v}{2\sqrt2},-t\right).
\]

Let Gamma_f be the closure of {(s,f(s))} in S x S and Gamma_f^t its transpose. For a codimension-two class z use T_z(w) = (pi_2)_*(pi_1^*w cup z), as in L003. No quartic embedding is assumed.

## Conclusion

The map f is a dominant rational self-map of degree two. On T, both [Gamma_f^t] and [Gamma_f] induce the same Hodge endomorphism U, with

\[
U\omega=-\sqrt2\,\omega,\qquad U^2=2\operatorname{id}_T,
\qquad q(Ur,Us)=2q(r,s),\qquad
E=\mathbb Q\operatorname{id}_T\oplus\mathbb Q U.
\]

Here omega is a nonzero holomorphic two-form, and r,s belong to T. In particular U is not a rational scalar and is not a q-isometry.

All the classes in the following equality are algebraic:

\[
\operatorname{Hdg}^2(X)
=D^2(X)+\mathbb Q[\Delta_S]+\mathbb Q[\Gamma_f^t]
=D^2(X)+\mathbb Q[\Delta_S]+\mathbb Q[\Gamma_f].
\]

The achieved dimension is rho^2 + 4 = 104, equal to the required dimension; divisor products and the diagonal alone give rho^2 + 3 = 103. The unique T tensor T representatives modulo D^2(X) are H-primitive and algebraic. This proves the codimension-two rational Hodge conjecture for these very general self-products. It asserts neither that every specialization has the same full field nor that arbitrary K3 self-products or fourfolds are covered.

## Proof

**The residual calculation applies to this K3 model.** The only quartic-specific cohomological facts used in L003 were H^1 = H^3 = 0, H^4 = Qe for a point class e with integral one, h^2 = 4e, and dim H^(2,0) = 1. For a projective K3, H^1(O_S) = 0 and K_S is trivial; Hodge decomposition and Poincare duality give the same odd-cohomology vanishing and one-dimensional holomorphic two-form space. An arbitrary ample h instead satisfies h^2 = m e for a positive integer m. Thus e is still a rational divisor-product class, which is the only role of the number 4 in that proof.

Hodge index gives V = N direct sum T, and Lefschetz (1,1) gives T intersect H^(1,1)(S) intersect V = 0. As in L003, Kunneth and the rational Hodge splitting therefore give

\[
D^2(X)=\mathbb Q(e\otimes1)\oplus(N\otimes N)\oplus\mathbb Q(1\otimes e),
\qquad
\operatorname{Hdg}^2(X)=D^2(X)\oplus K,
\]

where K is the rational (2,2)-part of T tensor T. Indeed, expanding a mixed N tensor T Hodge class in a rational basis of N forces rational (1,1)-coefficients in T, hence zero; likewise for T tensor N. The nondegenerate pairing identifies K with E by a tensor b acting as w -> q(w,a)b: complementary Hodge types pair perfectly, so exactly the tensors of type (2,2) give type-preserving endomorphisms. The correspondence map consequently has the same exact sequence as in L003,

\[
0\longrightarrow D^2(X)\longrightarrow\operatorname{Hdg}^2(X)
\xrightarrow{\Phi}E\longrightarrow0,
\qquad \Phi([\Delta_S])=\operatorname{id}_T.
\]

This justifies the extension beyond quartics, rather than applying L003 outside its hypotheses. Cup product with H kills T tensor T because q(h,T) = 0. Divisor products have dimension rho^2 + 2 and are algebraic.

**The map and the source normalization.** The identities a(-t) = -a(t) and b(-t) = a(t)^2-b(t) follow directly from the definitions. Write P = x^2+2ax+b, treating a and b as functions of t. Substitution of y^2 = xP gives

\[
v^2=\frac{P(x^2-b)^2}{x^3},\qquad
u(u^2-4au+4(a^2-b))
=\frac{P\bigl(P^2-4aPx+4(a^2-b)x^2\bigr)}{x^3}.
\]

The numerators agree since the bracket equals (P-2ax)^2-4bx^2 = (x^2-b)^2. Thus (u,v,t) lies on the isogenous surface S' with equation

\[
v^2=u(u^2-4au+4(a^2-b)).
\]

Putting x_new = u/2 and y_new = v/(2sqrt(2)) gives

\[
y_{\rm new}^2
=x_{\rm new}\bigl(x_{\rm new}^2-2a(t)x_{\rm new}+a(t)^2-b(t)\bigr),
\]

exactly S's equation at t_new = -t. This scaling is an isomorphism of the generic models S' -> S, hence yields the asserted rational self-map of the smooth projective model.

For precision, van Geemen–Schütt, [section 6.4, p. 19](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=19), displays (2u,2sqrt(2)v,-t) for this direction. With the equations in their section 6.1, that scaling instead gives the nonzero residual

\[
y_{\rm new}^2-x_{\rm new}
\bigl(x_{\rm new}^2-2ax_{\rm new}+a^2-b\bigr)
=-24au^2+30(a^2-b)u.
\]

The displayed scaling works in the reverse direction S -> S'; its inverse is the scaling used here. This is a coordinate-direction correction, not a rejection of the family statement. The exact rational coefficient check is reproducible with `python3 scripts/rm-degree-two/check_normalization.py`.

The map to S' has generic degree two: x satisfies x^2+(2a-u)x+b = 0, and y is then recovered from v = y(1-b/x^2), so the degree is at most two. The nonidentity involution

\[
(x,y)\longmapsto\left(\frac bx,-\frac{by}{x^2}\right)
\]

preserves S's equation and both u and v, so the degree is at least two. Here b(a^2-b) is not the zero rational function, as the generic elliptic fiber is smooth. The subsequent scaling and t -> -t are invertible, so f also has degree two. No assertion that f is everywhere a morphism is needed.

**Action of the graph and the exceptional classes.** Resolve the rational map by a sequence of point blowups p: Y -> S so that g: Y -> S is a morphism of degree two with g = f p on their common domain. Resolution of indeterminacy for smooth surfaces and the cohomological blowup formula give

\[
H^2(Y,\mathbb Q)=p^*H^2(S,\mathbb Q)\ \mathbin{\perp}\ W,
\]

where W is the nondegenerate span of the exceptional divisor classes. These are named standard surface results; iterating the point-blowup formula gives the stated orthogonal decomposition. The pushforward of Y under (p,g) is [Gamma_f], and under (g,p) it is [Gamma_f^t]. The projection formula gives their actions g_*p^* and p_*g^*, respectively.

If r belongs to T and e is an exceptional divisor class, then

\[
\int_Y g^*r\smile e=\int_S r\smile g_*e=0,
\]

because g_*e is a divisor class or zero. Likewise, for n in N,

\[
\int_Y g^*r\smile p^*n=\int_S r\smile g_*p^*n=0.
\]

Here g_*p^*n is again algebraic. Orthogonality first to W and then to p^*N shows that g^*r lies in p^*T. Hence, setting U = p_*g^* restricted to T, we have g^*r = p^*Ur. The maps preserve Hodge types, so U belongs to E; it is induced by the algebraic transposed graph with rational cycle coefficient one.

Since p has degree one and g has degree two, the projection formula now gives

\[
q(Ur,Us)=\int_Y p^*Ur\smile p^*Us
=\int_Y g^*r\smile g^*s=2q(r,s).
\]

The restriction to T is essential to the first equality with g-pullbacks. No such degree-scaling formula for the naive rational pullback on all of H^2(S) has been assumed.

**The faithful holomorphic-line action determines U.** On the chart, omega = dx wedge dt/y generates H^(2,0)(S), as in the family input. Terms proportional to dt vanish when wedged with dt, so

\[
\frac{du\wedge dt}{v}=\frac{dx\wedge dt}{y},\qquad
f^*\omega
=\frac{d(u/2)\wedge d(-t)}{v/(2\sqrt2)}
=-\sqrt2\,\omega.
\]

This equality on a dense open set is the equality of pulled-back global two-forms on Y. Consequently U acts by -sqrt(2) on the holomorphic line. The sign corresponds to the chosen square root and displayed f; changing the sign of its y-coordinate changes U's sign and not its span.

Every element of E acts on the one-dimensional H^(2,0)(S), giving a unital Q-algebra homomorphism sigma: E -> C. As E is a field, sigma is injective. Therefore sigma(U)^2 = 2 implies U^2 = 2 id_T. The polynomial z^2-2 is irreducible over Q; hence id_T and U are independent and span E, whose full degree is two by hypothesis. Merely containing Q(sqrt(2)) would not justify the spanning conclusion.

The ordinary graph also preserves T: pair g_*p^*r with any n in N and use algebraicity of p_*g^*n. Write its restriction as B. Since g^*r = p^*Ur,

\[
BUr=g_*p^*Ur=g_*g^*r=2r.
\]

As U^2 = 2 id_T, U is invertible and B = 2U^(-1) = U. Thus graph and transpose have the same action on T; equality of their Chow classes is not claimed.

**Spanning algebraic classes and the exact threshold.** Let z be any rational (2,2)-class on X. There are rational c,d with Phi(z) = c id_T+d U. Then z-c[Delta_S]-d[Gamma_f^t] belongs to D^2(X) by the exact kernel proved above. Every term is algebraic, so z is algebraic. The same argument uses Gamma_f because its action is also U. Modulo D^2(X), the two additional generators are independent. Thus the span and the full Hodge space both have dimension rho^2+2+2 = 104, whereas adjoining only the diagonal gives 103. Subtracting the algebraic D^2-component gives the primitive representative in K, also algebraic.

The construction deliberately supplies a similitude of factor two, which escapes the scalar-isometry restriction. It supplies the whole field only under the very-general full-field hypothesis; larger special endomorphism fields can have unaddressed directions. This is a proved restricted case from named inputs and an explicit correspondence, not a complete candidate for the universal target and not a novelty claim.

## Mathlib

Coverage of the full statement: **not checked**. No full or supporting Mathlib theorem match, and no library absence, is asserted. Van Geemen–Schütt Proposition 6.2 is a precise match for the family and very-general full field; its sections 6.1 and 6.4 support the isogeny construction, with the direction correction proved above. L003 supplies the residual tensor/endomorphism argument after its K3 hypotheses have been checked. Resolution of indeterminacy for surfaces, the point-blowup cohomology formula, Kunneth, Poincare duality, Hodge index, Lefschetz (1,1), and the projection formula are supporting named results, not matches for this entire cycle-span statement.
