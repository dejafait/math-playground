# L008 — The cubic support lifts only in the Dickson-family tangent directions

## Hypotheses

Let S and C be as in L007. Work at a very general parameter of [the cubic RM family](../foundations/05-cubic-rm-family.md), with a and b_1 nonzero. In particular the finite singular fibres are nodal, the fibres over t = +/-2 sqrt(a) are smooth, and the three-dimensional family has differential of rank three in the marked K3 deformation space. These are generic conditions, not assertions about every specialization.

Let F be the elliptic fibre class, O the zero section, and N = NS(S). Put X = S x S. Let V_N be the tangent space of marked deformations preserving N, let V_RM be its subspace preserving the given cubic real-multiplication action, and let V_D be the image of the tangent space of the Dickson family. Thus V_D is contained in V_RM. A first-order deformation is over A = C[epsilon]/(epsilon^2). Use the ideal-sheaf obstruction ob_C and normal sheaf N_C of L007.

## Conclusion

The support C has exactly three singular points. Each consists of two transverse smooth surface branches, and all three lie over (infinity,infinity) on the two elliptic bases. Its normalization nu:W -> C is smooth. Both projections g_0,g_1:W -> S are finite flat double covers, and j=(g_0,g_1):W -> X has injective differential everywhere. Here “immersion” refers to a holomorphic immersion and allows the three pairs of identified points. With

\[
0\longrightarrow T_W\xrightarrow{(dg_0,dg_1)}
g_0^*T_S\oplus g_1^*T_S\longrightarrow N_j\longrightarrow0,
\]

one has N_C = nu_*N_j. In particular the obstruction of L007 is the image of (g_0^*kappa,g_1^*kappa) in H^1(W,N_j), under the natural identification with H^1(C,N_C).

Its kernel on the NS-fixed tangent space is

\[
\ker(\operatorname{ob}_C|_{V_N})=V_D.
\]

Consequently dim V_D = 3, dim V_RM = 4, and ob_C has rank one on V_RM. Every direction in V_RM outside V_D has a nonzero first-order obstruction to a flat embedded lift of this particular reduced support C.

This does not obstruct a different representative of its cohomology class, a cycle obtained after adding algebraic components, or all algebraic cycles in the transverse direction. It supplies no new surface on which the full 21-dimensional Hodge span is realized and is not a disproof of the Hodge conjecture.

## Proof

**A finite normalization, rather than an arbitrary resolution.** Take the fibre product of the smooth elliptic surface S with the degree-two base map

\[
t=v+a/v.
\]

Call the resulting surface W. The base map branches only over the two stipulated smooth fibres. Thus W is smooth: near those fibres it is the base change of a smooth morphism, and elsewhere the base change is etale. The projection g_0 is finite flat of degree two. Its branch divisor is the sum of two fibres and its trace line bundle is O_S(F). The double-cover canonical formula gives

\[
K_W=g_0^*F=2F_W,
\]

where F_W is the fibre class on the v-line. In particular K_W is nef and W has no exceptional (-1)-curves. The zero section O_W=g_0^{-1}(O) is a copy of P^1 and has self-intersection -4.

The rotation sigma(v)=zeta v, with x,y unchanged on the Laurent chart, extends to W. For example, putting x_v=v^4x, y_v=v^6y gives a minimal Weierstrass equation on the v-chart with coefficients

\[
A_v=b_1(v^{15}+a^7v)+b_0v^8,\qquad
B_v=c_1(v^{19}+a^7v^5)+c_0v^{12}.
\]

Its rotation is (v,x_v,y_v) -> (zeta v,zeta^4x_v,zeta^6y_v). It is regular on both base charts. The only singularities of this Weierstrass total space are the A_1 points at the two type-III fibres; blowing them up is equivariant. This recovers the smooth base change W. Define g_1=g_0 sigma. Its dense formula is the one in L007, and it too is finite flat of degree two. The deck involutions are

\[
\tau_0(v)=a/v,\qquad \tau_1(v)=a\zeta^{-2}/v.
\]

The map j is finite onto its image: its first projection is finite. It is birational onto C by the recovery formula for v in L007. Since W is normal, this identifies W with the normalization of C. The ramification loci of its two projections lie respectively over v^2=a and v^2=zeta^{-2}a, which are disjoint. At every point at least one projection is etale, including over infinity and the singular elliptic fibres. Hence j is an immersion and N_j is a rank-two vector bundle.

**All identifications over infinity.** Away from v=0,infinity, the base pair (t,s) recovers v. The same assertion holds over the zero section and the resolved finite fibres: the first projection identifies the corresponding base-changed fibre with the original fibre. Thus there are no identifications there and j is locally an embedding.

Near infinity choose an analytic coordinate q such that P_a(t)=q^(-7), with q asymptotic to 1/t. This is possible by taking a seventh root of the unit in (1/t)^7 P_a(t). In the minimal coordinates X=q^4x and Y=q^6y the equation is

\[
Y^2=X^3+(b_1q+b_0q^8)X+c_1q^5+c_0q^{12}.
\]

The two branches of C over this neighbourhood are graphs of f and f^(-1), where

\[
f(q,X,Y)=(\zeta^{-1}q,\zeta^3X,\zeta Y).
\]

Here f has exact order seven. This follows either by successive choices of the inverse branches of P_a or directly from the displayed equation. Both inverse branches are those furnished by v=infinity and v=0. Therefore their intersections are precisely the fixed points of f^2, equivalently of f, on the fibre q=0.

The zero-section point is fixed and has tangent weights (6,2), meaning eigenvalues (zeta^6,zeta^2), as also computed in L007. The Weierstrass singularity at (q,X,Y)=0 has nondegenerate quadratic part Y^2-b_1qX, so it is A_1. Its blowup has exceptional conic

\[
Y^2=b_1qX\quad\text{in }\mathbb P^2_{[X:Y:q]}.
\]

The three ambient projective weights 3,1,6 are distinct. Exactly two eigenpoints lie on this conic, namely [1:0:0] and [0:0:1]. In the X-chart, with Y=Xr and q=Xu, the strict-transform equation solves for u; local coordinates (X,r) have weights (3,5). In the q-chart, coordinates (q,Y/q) have weights (6,2). These are the two exceptional fixed points. The strict transform of the cuspidal cubic is P^1; its nonidentity order-seven action has just its zero-section point and its intersection with the exceptional curve fixed. Hence there are exactly three fixed points in the entire resolved fibre.

For each of the weight pairs (6,2), (3,5), (6,2), neither eigenvalue is 1 or -1. Thus df-df^(-1) is invertible. The two graph surfaces meet transversely at each fixed point. This proves that there are exactly three double points and no other singularities of C. The third fixed point and the tangency point of the type-III fibre have not been omitted.

**The global normal sheaf and simultaneous normalization to first order.** At each double point the local ring and its normal module are exactly those computed in L007:

\[
B=\mathbb C[[r_1,r_2,s_1,s_2]]/(r_i s_j),\qquad
\operatorname{Hom}(I/I^2,B)
=\mathbb C[[r_1,r_2]]^2\oplus\mathbb C[[s_1,s_2]]^2.
\]

The two summands are the normals of the two immersed branches. On the smooth part this is the usual immersion normal bundle. These identifications are intrinsic: the identification away from the two origins extends uniquely over each smooth surface branch, and the displayed module says that every extended pair occurs. They therefore glue to N_C=nu_*N_j. Finite pushforward is exact and preserves coherent cohomology, giving the claimed cohomology identification. Applying an ambient derivation to the branch equations shows that L007's map to the normal sheaf becomes the quotient map from g_0^*T_S direct sum g_1^*T_S. This proves the assertion about ob_C.

We also need what this local calculation implies for an actual first-order lift; preservation of a Hodge class would not suffice. Let C_A be a flat embedded lift in S_A x_A S_A. At every double point L007 proves that every local embedded first-order deformation is induced by an ambient derivation. Hence C_A is locally a product deformation of its two-branch singularity. At smooth points it is locally smooth. Splitting the two branches of each product chart gives a smooth first-order deformation W_A and a finite morphism nu_A:W_A -> C_A.

To justify gluing this splitting, in the two-plane ring every derivation preserves both branch ideals. Indeed, differentiating r_i s_j=0 forces the s-branch component of D(r_i), and the r-branch component of D(s_j), to vanish, including their common constant terms. Such a derivation extends uniquely to the two power-series rings of the normalization. Thus a transition map reducing to a fixed central transition has a unique lift to the split charts. On a punctured smooth surface branch the same uniqueness follows from extension of holomorphic functions across an isolated point. The lifted transitions satisfy the cocycle identities, giving the asserted finite simultaneous normalization. One can work analytically here and apply proper GAGA over A to its finite coherent algebra. This argument is specific to these isolated transverse surface crossings; it does not assert that normalization commutes with arbitrary deformations.

Composing nu_A with the two ambient projections gives G_0,G_1:W_A -> S_A. They are proper and their special fibres are finite, so they are finite over the nilpotent base. The local flatness criterion, using A-flatness and the flat special-fibre maps, makes each finite module locally free of rank two. In characteristic zero its trace splits it as O direct sum a line bundle; negation on the trace-zero summand gives the canonical deck involution. Denote these lifted involutions by tau_0,A and tau_1,A.

**The dihedral relations must lift.** First H^0(W,T_W)=0. The canonical map of W is its elliptic fibration followed by the conic embedding of the v-line, since K_W=2F_W and the fibres are connected. An infinitesimal automorphism therefore induces a vector field on P^1 preserving the singular-fibre set. There are at least three distinct singular values (indeed two type-III fibres and the preimages of the finite nodal fibres), so this base vector field is zero. A remaining vertical vector field restricts along O_W to a section of its normal bundle O_P1(-4), hence vanishes there. On a smooth elliptic fibre a regular vector field vanishing at one point is zero. Density of those fibres proves the claim.

For any smooth first-order deformation, an automorphism reducing to the identity has the form 1+epsilon D with D a global vector field of the special fibre. Therefore it is the identity here. On W,

\[
\tau_0\tau_1(v)=\zeta^2v.
\]

The seventh power of tau_0,A tau_1,A reduces to the identity and must consequently equal the identity on W_A. Taking its fourth power gives a lifted rotation sigma_A reducing to sigma. The two involutions and this rotation satisfy the dihedral relations exactly over A. This step rules out an infinitesimal failure of the order-seven relation; it is not an assumption of equivariant deformation.

**Recovering the elliptic base in an NS-fixed lift.** Assume now kappa belongs to V_N. The line bundles O_S(F), O_S(O), and the class of the exceptional component of the type-III fibre extend to S_A. Here we use the usual line-bundle obstruction kappa contracted with c_1, which vanishes precisely in an NS-preserving tangent direction. Their extensions are unique because H^1(S,O_S)=0. Riemann–Roch on the K3 gives h^1(O_S(F))=0 and h^1(O_S(D))=0 for either of the effective (-2)-curves D just specified. Thus the two sections of the fibre pencil and the defining sections of those curves lift. Basepoint freeness is preserved over a nilpotent thickening. This gives an elliptic map S_A -> P^1_A, its zero section, and its exceptional (-2)-curve.

Write the trace splitting of G_0 as O_SA direct sum L_A^(-1). Its reduction has L=O_S(F), so uniqueness of line-bundle lifting gives L_A=O_SA(F_A). A finite flat double cover in characteristic zero is recovered by multiplication on this trace-zero line, namely a section of L_A^2. Every section of O_SA(2F_A) is a quadratic in the lifted pencil sections: this holds on S, and reduction followed by subtraction of a lift, then division by epsilon, proves it over A. Consequently W_A is still obtained from S_A by the double cover of its base branched over two points. That cover is a smooth genus-zero curve over A and is isomorphic to P^1_A.

The double-cover canonical formula now gives K_WA=G_0^*F_A=pi_WA^*O(2). Hence its relative canonical system recovers this elliptic base, without invoking a general deformation theorem for Iitaka fibrations. Every lifted symmetry preserves the base fibration. They preserve its zero section as well: the base-changed zero section exists, every translate reduces to O_W, and two embedded first-order lifts of O_W in a fixed W_A differ by H^0(O_W,N_OW/W)=H^0(O(-4))=0.

For reference, the standard Weierstrass and canonical formulas used here are Schuett–Shioda, [*Elliptic Surfaces*, sections 2.6, 4.10, 5.1–5.2, Theorem 6.8 and Corollary 6.9](https://arxiv.org/pdf/0907.0298). The formulas over A follow from the same relative Weierstrass construction using functions of pole orders two and three along the section. Completing the square and cube is valid since 2 and 3 are invertible. The fundamental line bundle of W_A is O(4), so its short Weierstrass coefficients have degrees at most 16 and 24.

**Counting all equivariant first-order coefficients.** A local rescaling of t and v sets a=1; a square root exists since a is nonzero. This does not lose a moduli direction: P_a(sqrt(a)t)=a^(7/2)P_1(t), and that factor is absorbed in b_1,c_1.

The lifted finite-group action on the base can be conjugated to the constant action v -> zeta v and v -> 1/v. Here is the infinitesimal justification: differences from the constant action form a group 1-cocycle with values in H^0(P^1,T_P1); averaging over the fourteen elements kills its cohomology in characteristic zero. The fundamental line bundle and its action can likewise be identified with the central O(4) and its linearization: H^1(P^1,O)=0 and the same averaging argument remove infinitesimal choices. A character cannot vary infinitesimally because a unit 1+epsilon c of finite order prime to the characteristic has c=0. In short Weierstrass coordinates, an origin-preserving isomorphism has only the scaling x -> u^2x, y -> u^3y; translations would reintroduce the eliminated x^2, xy, or y terms.

Thus the actions on the v-chart may be written

\[
\sigma(v,x_v,y_v)=(\zeta v,\zeta^4x_v,\zeta^6y_v),\quad
\tau_0(v,x_v,y_v)=(v^{-1},v^{-8}x_v,v^{-12}y_v).
\]

Rotation forces the exponents of A_v to be congruent to 1 modulo 7, leaving 1,8,15 within its degree bound. For B_v they are congruent to 5, leaving 5,12,19. Inversion gives A_v(v^(-1))=v^(-16)A_v(v) and B_v(v^(-1))=v^(-24)B_v(v), pairing the two outer coefficients in each. Over A the full coefficient space is therefore

\[
A_v=\alpha(v^{15}+v)+\beta v^8,\qquad
B_v=\gamma(v^{19}+v^5)+\delta v^{12}.
\]

This is four-dimensional before the one-dimensional Weierstrass scaling. The scaling has a nonzero tangent orbit because alpha reduces to a nonzero coefficient. Put x=x_v/v^4 and y=y_v/v^6 on the common Laurent chart. Quotienting by tau_0 fixes x,y and t=v+v^(-1), and gives

\[
y^2=x^3+(\alpha P_1(t)+\beta)x+\gamma P_1(t)+\delta.
\]

It remains essential to pass from this Weierstrass statement to the *smooth* surface deformation, without losing a resolution direction. The finite Weierstrass total space is smooth, and the sole singularity of S's Weierstrass model is the A_1 point at infinity. In the simultaneous-resolution deformation of A_1, the smoothing coordinate is the square of a resolution coordinate lambda. The locus on which the exceptional (-2)-curve lifts is lambda=0, including infinitesimally. This is the A_1 case of Brieskorn's simultaneous-resolution theorem and Wahl's [*Simultaneous resolution of rational singularities*, sections 1.2–1.4, especially the exceptional-curve locus in 1.4](https://www.numdam.org/item/CM_1979__38_1_43_0.pdf#page=5). Those results identify the only local resolution ambiguity; they do not assert that an arbitrary first-order smoothing is detected by its Weierstrass coefficients.

Explicitly the local model xy=z^2-lambda^2 resolves by blowing up (x,z-lambda). Its two charts have transition y=r^2x+2lambda r, r'=1/r. For lambda=epsilon l, a lift of the exceptional P^1 would require regular functions f(r),g(r') with g(1/r)=r^2 f(r)+2lr. The exponent-one Laurent term cannot be removed by the terms of exponents at least two or at most zero, so l=0. In the NS-fixed deformation the exceptional curve already lifts by the preceding cohomology calculation. This excludes precisely the otherwise invisible resolution tangent. The equisingular resolution, or equivalently the blowup of the persistent A_1 section, therefore recovers S_A from the displayed coefficients. The local identifications glue uniquely: an automorphism over the contracted model is the identity on its dense smooth locus, hence everywhere, also to first order. Its class belongs to V_D.

We have proved that every flat embedded lift with kappa in V_N forces kappa in V_D. This is a necessary condition for *every* embedded lift, not just for lifts initially assumed to preserve the cover construction.

**The reverse inclusion and the exact rank.** V_D does supply flat embedded lifts. Vary the Dickson parameters in a small neighbourhood satisfying the generic hypotheses, form the smooth double covers and the two projections, and take their reduced image. Away from the three image double points this is a family of smooth embedded surfaces. At those points the two graph branches and their transverse intersections vary holomorphically; the implicit function theorem and simultaneous local coordinates give the constant two-plane-crossing model relative to the parameter space. Hence the image family is flat, including at infinity. This proves V_D is contained in the obstruction kernel, by L007. The two inclusions give the asserted equality.

The family theorem and the generic-rank hypothesis give dim V_D=3. To check the actual required comparison, rank T(S)=18 and its dimension over the cubic field is six. The marked RM periods lie on the smooth quadric q(omega,omega)=0 in the projectivization of the six-dimensional eigenspace containing H^(2,0). Positivity selects an open set and does not change its dimension, which is 6-2=4. Local Torelli identifies this with V_RM. This is the period calculation in van Geemen–Schuett [section 2.6 and sections 5.3–5.4](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=15), with N fixed. Rank-nullity now gives rank(ob_C|V_RM)=1. No basis or numerical value in H^1(N_C) is required to conclude that its value on each transverse direction is nonzero.

This is a first-order obstruction for the specified support. L007's Hodge-preservation observation still applies in all four RM directions. Thus the failure occurs after that necessary cohomological test. The successful cycle span from L006 remains confined to its already treated family; changing the cycle representative is a separate mathematical question.

The command `python3 scripts/cubic-deformation/check_global_weights.py` checks the three pairs of tangent weights, all rotation/inversion coefficient constraints within the full degree bounds, the Dickson descent identity, and the A_1 resolution chart relation. It is supporting exact algebra, not a computational verification of normalization, deformation equivalence, or the global kernel theorem.

## Mathlib

Coverage of the full statement: **not checked**. No full match, supporting Mathlib theorem name, or absence is claimed. L007 supplies the local normal-module calculation and the exact embedded lifting criterion. The directly linked Schuett–Shioda results support the standard elliptic-surface formulas; Wahl sections 1.2–1.4 support the A_1 simultaneous-resolution and exceptional-curve distinction; van Geemen–Schuett supplies the family and RM dimension input. None of these sources is asserted to state this global obstruction theorem or to be a Mathlib match. The normalization, forced dihedral action, coefficient restriction, and both kernel inclusions are proved above.
