# L006 — Dihedral descent realizes the cubic real-multiplication field

## Hypotheses

Let S be a very general smooth projective member of [the cubic RM family](../foundations/05-cubic-rm-family.md). Thus, with a nonzero,

\[
P_a(t)=t^7-7at^5+14a^2t^3-7a^3t,
\qquad
y^2=x^3+(b_1P_a(t)+b_0)x+(c_1P_a(t)+c_0).
\]

Write zeta = exp(2 pi i/7), theta = zeta+zeta^(-1), X = S x S, V = H^2(S,Q), N = NS(S)_Q, T = N perpendicular to the cup-product pairing q, and E = End_Hdg(T). The family input gives rho = dim N = 4 and the **full** field E isomorphic to Q(theta). Choose an ample divisor h on S and put H = pi_1^*h+pi_2^*h. Let D^2(X) be the rational span of products of divisor classes.

For a codimension-two cycle Z on X, use the convention

\[
T_{[Z]}(w)=(\pi_2)_*(\pi_1^*w\smile[Z]).
\]

The brackets denote its cohomology class. In the construction below, all proper pushforwards of cycles retain their generic multiplicities.

## Conclusion

There is an algebraic cycle Z in CH^2(X)_Q whose action U on T satisfies

\[
U\omega=\theta\omega,\qquad
U^3+U^2-2U-\operatorname{id}_T=0,\qquad
E=\mathbb Q\operatorname{id}_T\oplus\mathbb Q U\oplus\mathbb Q U^2,
\]

where omega = dx wedge dt/y spans H^(2,0)(S). The displayed cubic is U's minimal polynomial. In particular U is neither a rational scalar nor a q-isometry.

Define the **composition** cycle

\[
Z^{\circ2}=(p_{13})_*\bigl(p_{12}^*Z\cdot p_{23}^*Z\bigr)
\quad\hbox{in }\mathrm{CH}^2(S\times S)_{\mathbb Q},
\]

using the projections from S x S x S and its Chow intersection product. Then

\[
\operatorname{Hdg}^2(X)
=D^2(X)+\mathbb Q[\Delta_S]+\mathbb Q[Z]+\mathbb Q[Z^{\circ2}].
\]

Every class on the right is algebraic. The attained dimension is rho^2+2+3 = 21, exactly the required dimension, whereas divisor products and the diagonal give only rho^2+3 = 19. The unique representatives modulo D^2(X) in T tensor T are algebraic and H-primitive.

This establishes the codimension-two rational Hodge conjecture for these very general self-products. It does not cover all specializations, the larger deformation space of K3 surfaces with this RM field, arbitrary K3 self-products, or arbitrary fourfolds. It makes no novelty claim: the dihedral construction is published in van Geemen–Schütt section 4.8.

## Proof

**The residual criterion for this K3 model.** The cohomological calculation in L003 applies after checking its geometric inputs beyond quartics. A projective K3 has H^1(S,Q) = H^3(S,Q) = 0, H^4(S,Q) = Qe for a point class of integral one, and one-dimensional H^(2,0). For the chosen ample h, h^2 = m e with m > 0, so e is still a rational divisor-product class; the quartic value m = 4 was not otherwise used in that calculation. Hodge index gives the rational orthogonal Hodge decomposition V = N direct sum T. By Lefschetz (1,1), T has no nonzero rational (1,1)-vector.

Consequently the Kunneth calculation and tensor/endomorphism identification proved in L003 give

\[
D^2(X)=\mathbb Q(e\otimes1)\oplus(N\otimes N)\oplus\mathbb Q(1\otimes e),
\qquad
\operatorname{Hdg}^2(X)=D^2(X)\oplus K,
\]

where K is the rational (2,2)-part of T tensor T. The mixed rational Hodge tensors vanish: expanding in a rational basis of N would require rational (1,1)-vectors in T. Nondegeneracy of q identifies K with E by a tensor r tensor s acting as w -> q(w,r)s. In particular every rational Hodge correspondence preserves T, and

\[
0\longrightarrow D^2(X)\longrightarrow\operatorname{Hdg}^2(X)
\xrightarrow{\Phi}E\longrightarrow0,
\qquad
\Phi([\Delta_S])=\operatorname{id}_T.
\]

Here Phi is restriction of the displayed correspondence action. The dimension of D^2(X) is rho^2+2. Also H cup K = 0 since h is orthogonal to T. These conclusions use L003's proof with checked K3 hypotheses, not its quartic statement outside its scope.

**A resolved algebraic correspondence.** Make the degree-two change of base t = v+a/v. The exact identity

\[
P_a(v+a/v)=v^7+a^7v^{-7}
\]

puts the cover on the affine chart

\[
y^2=x^3+\bigl(b_1(v^7+a^7v^{-7})+b_0\bigr)x
             +c_1(v^7+a^7v^{-7})+c_0.
\]

For j = 0, 1, -1 put

\[
t_j=\zeta^jv+\zeta^{-j}a/v.
\]

Each P_a(t_j) is the same Laurent polynomial v^7+a^7v^(-7), so the maps (x,y,v) -> (x,y,t_j) all have target S. Each has generic degree two: C(v)/C(t_j) is the degree-two function-field extension of the indicated map of projective lines, and the smooth elliptic generic fiber of S is geometrically integral, so this base change remains integral of degree two. Equivalently, C(t_j) is algebraically closed in the generic elliptic function field, so the quadratic extension does not split there.

Take a smooth projective model of the cover and resolve the three rational maps simultaneously. Resolution of projective surfaces and elimination of indeterminacy give a smooth projective W with morphisms

\[
g_j:W\longrightarrow S\quad(j=0,1,-1)
\]

having these formulas on the common dense open set. No assumption that the cover is itself K3 is required. Set

\[
C_j=(g_0,g_j)_*[W]\quad(j=1,-1),
\qquad Z=\tfrac12(C_1+C_{-1}).
\]

These are codimension-two algebraic cycles; W maps to a surface in X since its first projection is dominant. Choosing a further resolution does not change the pushforward cycle. On the cover's function field, the maps sigma(v) = zeta v and tau(v) = a/v preserve x,y and the equation. Thus C_1 and C_(-1) are precisely the resolved pushforwards of the rotation graphs in the source's section 4.8. The formulas above specify the descent even if a quotient map is only rational on a chosen minimal model.

The projection formula identifies the action of [C_j] on H^2(S,Q) as (g_j)_*g_0^*. Its restriction to T belongs to E by the residual calculation. The graph convention is thereby fixed without assuming that a graph acts by its usual pullback.

**Trace and the factor of two.** Compute on holomorphic two-forms on the common dense open set. Put

\[
\alpha=g_0^*\omega=(1-a/v^2)\frac{dx\wedge dv}{y},
\qquad
\beta_j=g_j^*\omega=(\zeta^j-\zeta^{-j}a/v^2)\frac{dx\wedge dv}{y}.
\]

The nonidentity deck transformation for g_j at the level of function fields is

\[
\kappa_j(v)=a\zeta^{-2j}/v,
\qquad \kappa_j(x)=x,\quad\kappa_j(y)=y.
\]

It fixes t_j and interchanges the two generic sheets. Including the differential of kappa_j gives

\[
\kappa_j^*\alpha
=(\zeta^{2j}-a\zeta^{-2j}/v^2)\frac{dx\wedge dv}{y},
\qquad
\alpha+\kappa_j^*\alpha=(\zeta^j+\zeta^{-j})\beta_j
=\theta\beta_j.
\]

For a generically finite morphism of smooth projective surfaces, the Gysin map on H^(2,0) is the trace on holomorphic top forms. On its finite etale locus this is the sum over inverse branches, as follows either from integration along the fibers or the adjoint definition of Gysin. Pulling that trace back to a degree-two cover gives the sum of the form and its deck transform. The Gysin map preserves Hodge type, so the equality on this dense open set determines the global holomorphic form on S. It follows that

\[
g_j^*((g_j)_*\alpha)=\alpha+\kappa_j^*\alpha
=\theta g_j^*\omega,
\qquad
(g_j)_*g_0^*\omega=\theta\omega.
\]

Pullback on forms is injective because g_j is dominant and generically etale. It is unnecessary for kappa_j to extend regularly on the chosen resolution: only the equality on the two-sheeted open cover was used. Nor has an uncorrected identity on all of H^2 of a rational quotient been asserted.

Thus each pushed graph acts by theta on H^(2,0). Their sum acts by 2 theta, and the factor 1/2 in Z gives U omega = theta omega. This is the normalization left implicit in the source's statement that the graph sum induces a cycle downstairs, not a claim of a contradiction in that source. The coefficient 1/2 is allowed by the rational target. Although coordinates use zeta, these algebraic cycles over C have rational cycle coefficients and rational cohomology classes.

**From the holomorphic line to the whole field.** Every element of E acts on the one-dimensional holomorphic line. Its eigenvalue defines a unital Q-algebra homomorphism epsilon: E -> C. Since E is a field, epsilon is injective. With epsilon(U) = theta and zeta^7 = 1, zeta not equal to 1, one has

\[
\theta^3+\theta^2-2\theta-1
=\zeta^3+\zeta^2+\zeta+1+\zeta^{-1}+\zeta^{-2}+\zeta^{-3}=0.
\]

The last sum is zeta^(-3) times the sum of the seven powers of zeta. The cubic f(z) = z^3+z^2-2z-1 has no rational root: a rational root of this monic integral polynomial could only be 1 or -1, and f(1) = -1, f(-1) = 1. Therefore f is irreducible. Injectivity gives f(U) = 0 on all of T, and the same irreducibility shows that id, U, U^2 are rationally independent. The full-field hypothesis gives dim_Q E = 3, so they span E. A mere inclusion of Q(theta) in a larger endomorphism field would not justify that last step.

Also theta is real and theta^2 is not 1. Since q(omega, conjugate(omega)) is nonzero, rationality of U gives

\[
q(U\omega,U\bar\omega)=\theta^2q(\omega,\bar\omega)
\ne q(\omega,\bar\omega).
\]

Thus U is not a q-isometry. The construction can therefore supply directions missed by an isometry-only span.

**Composition and the exact cycle span.** On the smooth product S x S x S, Chow pullback, intersection, and proper pushforward define Z^(circ 2) as above even when cycle representatives do not meet properly. Their compatibility with cycle classes and the projection formula show that this cycle acts as T_[Z] composed with itself on cohomology, hence as U^2 on T. It is not the cup square of [Z] in H^8(S x S). The polynomial relation has been proved for the action on T only; no relation in the Chow ring is asserted.

If c is any rational (2,2)-class on X, write Phi(c) = r id+s U+t U^2 with r,s,t rational. Then

\[
c-r[\Delta_S]-s[Z]-t[Z^{\circ2}]\in D^2(X).
\]

Every subtracted class and every class in D^2(X) is algebraic. Hence c is algebraic. The three additional classes are independent modulo D^2(X), so the achieved dimension is 4^2+2+3 = 21. This attains the full required dimension for this family; diagonal and divisor products alone give 19, and adding Z alone gives 20. Finally, subtracting the D^2-component from any algebraic Hodge class yields its algebraic primitive representative in K.

The exact identities used for the base change, both traces, the cubic, and the dimensions are checked by `python3 scripts/rm-cubic/check_correspondence.py`. That calculation is supporting arithmetic, not a substitute for the resolution, trace, Hodge-theoretic, or cycle-composition arguments above. The full-field equality remains restricted to the very general parameters supplied by the named theorem.

## Mathlib

Coverage of the full statement: **not checked**. No full or supporting Mathlib match, or absence, is claimed. Van Geemen–Schütt [Theorem 1.2(7) and sections 5.3–5.4](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=15) match the family and very-general full-field input; [section 4.8](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=13) supplies the known geometric construction. Neither is presented as a Mathlib theorem. L003 supplies the residual argument after the K3 hypotheses are checked here. Resolution of surfaces and indeterminacy, trace on top forms, the projection formula, Chow correspondence composition, and the standard Hodge inputs are supporting named results. The explicit normalized action and 21-dimensional spanning calculation are proved here.
