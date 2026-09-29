# L014 — Two rotation supports retain the transverse cubic obstruction

## Hypotheses

Retain S, the smooth finite cover W, X=S x S, zeta, C, and the marked tangent spaces V_N, V_RM and V_D of L008. In particular S is a very general member of the cubic Dickson family, a and b_1 are nonzero, and both ambient factors have the same deformation S_A over A=C[epsilon]/(epsilon^2). Put

\[
\theta_j=\zeta^j+\zeta^{-j},\qquad
C^{(j)}=\operatorname{im}(g_0,g_0\sigma^j)_{\mathrm{red}}
\quad(j=1,2,3),\qquad C^{(1)}=C,
\qquad Y=C^{(1)}\cup C^{(2)}
\]

with the reduced scheme-theoretic union structure. Throughout, the ambient deformation direction kappa belongs to V_N, so the marked Neron--Severi lattice stays fixed. The third image is only a test locus; it is not a component of Y. None of these image supports is defined to be a composition cycle.

Choose c with c^2=a. Let

\[
R(z)=1728\,\frac{4(b_1z+b_0)^3}
 {4(b_1z+b_0)^3+27(c_1z+c_0)^2},\qquad
J_0(t)=R(P_a(t)).
\]

Require the elliptic fibres over the two values z=2c^7 and z=-2c^7 in this expression to be smooth, and R'(2c^7), R'(-2c^7) to be nonzero. These are nonempty open conditions, hence hold at very general parameters. For the extra conditions one may take a=1, b_1=b_0=c_1=1, c_0=3: at z=+/-2 the denominator and the derivative numerator are nonzero. The other generic conditions remain those of L008; the intersection of these nonempty opens in the irreducible parameter space is nonempty.

Use N_Y=Hom(I_Y/I_Y^2,O_Y) and the first-order ideal-gluing obstruction ob_Y from L007, applied to I_Y. That criterion applies to arbitrary ideals in a smooth ambient first-order deformation; it does not require Y to be lci everywhere.

## Conclusion

There are exactly four finite intersection curves between the two components. They are complete smooth elliptic curves over the ordered base pairs

\[
(p_{e,2},p_{e,3}),\quad(p_{e,3},p_{e,2}),
\qquad p_{e,k}=ec\theta_k,\quad e\in\{1,-1\}.
\]

Along each curve Y has a local model (z,rs), and its intrinsic double-crossing smoothing line is trivial. Thus these four curves alone supply four scalar candidate smoothing parameters. At infinity the two components intersect at the same three points as in L008. At each there are four pairwise transverse surface branches, whose full local ideals are specified below; no normal-crossing hypothesis is imposed there.

For any flat embedded lift of Y, all four finite smoothing residues vanish. The lift therefore yields a flat embedded lift of C, including at infinity, and

\[
\ker(\operatorname{ob}_Y|_{V_N})=V_D,\qquad
\dim\ker(\operatorname{ob}_Y|_{V_{\rm RM}})=3,\qquad
\operatorname{rank}(\operatorname{ob}_Y|_{V_{\rm RM}})=1.
\]

The global compatibility calculation giving the vanishing is explicit. Write J_A=J_0+epsilon dJ for the j-map of the NS-fixed elliptic deformation, and a_{e,k}=dJ(p_{e,k}). Set

\[
h_e=R'(2ec^7)(p_{e,2}-p_{e,3})
       Q_3(p_{e,2},p_{e,3})\ne0,\qquad
Q_j(t,s)=t^2+s^2-\theta_jts-a(4-\theta_j^2).
\]

With the smoothing coordinate defined using r=Q_1 and s_0=Q_2, the two residues for sign e are both

\[
b_e=\frac{a_{e,3}-a_{e,2}}{h_e}.
\tag{1}
\]

Smooth points on Y over the other critical pairs force

\[
E_e(a_e):=(a_{e,1}-a_{e,2},\,a_{e,1}-a_{e,3})=(0,0).
\tag{2}
\]

The numerator in (1) is the first coordinate of E_e minus its second. Therefore the residue map is zero on the globally compatible data. This computes the double-curve channel relevant to the proposed cancellation; it is not a presentation of every cotangent-cohomology group at the isolated points.

The cycle [Y] acts on T(S) as U^2+U-2 id, a non-scalar cubic RM endomorphism. Nevertheless this reduced representative supplies only the three existing lifting directions, against four required. The calculation stops this first-order test. It neither obstructs all representatives of that class nor addresses possible ramified higher-order families, and it is not a disproof of the rational Hodge conjecture.

## Proof

**Finite incidence and multiplicities.** For every j=1,2,3 the parametrization is

\[
t=v+a/v,\qquad s=\zeta^jv+\zeta^{-j}a/v.
\]

It recovers v by

\[
v=\frac{s-\zeta^{-j}t}{\zeta^j-\zeta^{-j}}.
\]

Thus the proper image has generic multiplicity one. The construction of W and the rotation in L008 gives both projections as finite flat double covers. Their ramification loci are disjoint, so each image is smooth and embedded away from its identified points at infinity, by this recovery formula and the injectivity of the differential. This applies over the zero section as well as on the affine Weierstrass chart.

Elimination gives Q_j(t,s)=0. The exact Dickson identity gives the factorization

\[
P_a(t)-P_a(s)=(t-s)Q_1(t,s)Q_2(t,s)Q_3(t,s).
\tag{3}
\]

For example, with generic s=v+a/v the seven roots in t are s and the six values associated to zeta^j v, j=+/-1,+/-2,+/-3. Both sides of (3) are monic of degree seven in t. This proves the polynomial identity, including exceptional base values.

The six numbers p_{e,k} are the distinct simple critical points of P_a, with

\[
P_a(p_{e,k})=2ec^7,\qquad P_a'(p_{e,k})=0.
\]

Indeed take v=ec zeta^k. The derivative of v^7+a^7v^{-7} has a simple zero there, whereas dt/dv is nonzero since k=1,2,3. Distinctness also follows from the three distinct roots theta_k of the irreducible cubic in L006. No two of these roots are negatives: otherwise their third root would be -1, which is not a root of that cubic.

For each sign e the unordered critical pairs have the following incidence:

| Pair of critical-point indices | Conics through either ordered pair |
| --- | --- |
| 1, 2 | Q_1 and Q_3 |
| 1, 3 | Q_2 and Q_3 |
| 2, 3 | Q_1 and Q_2 |

The two points of the v-line above p_{e,k} are ec zeta^k and ec zeta^(-k); their j-th images have base values ec theta_{j+k} and ec theta_{j-k}, with theta_{-m}=theta_m and indices modulo seven. This proves the table. There are no additional finite intersections of any conic pair: subtracting Q_i=Q_j=0 yields

\[
ts=a(\theta_i+\theta_j),\qquad
t^2+s^2=a(4+\theta_i\theta_j),
\]

which has at most four solutions. The table supplies four distinct ones for each pair, including both signs and both orders. At each the determinant of the two conic gradients is

\[
2(\theta_i-\theta_j)(t^2-s^2)\ne0.
\tag{4}
\]

There is no finite triple intersection, since the equation for ts for two different pairs would equate distinct theta_j. Both projections of each conic branch at these pairs are unramified: in the parametrization neither its source nor its target is an endpoint with theta_0=2, including after taking the sign e.

Above an intersection pair the surfaces identify the same whole elliptic curve by their common x,y coordinates. The fibres are smooth by hypothesis. More intrinsically, near the common value 2ec^7 the original surface is a base change of the smooth elliptic family with coefficients b_1z+b_0, c_1z+c_0. Choose a local fibre coordinate on that family and pull it to both factors. Its difference z, together with r=Q_1, s_0=Q_2 and a coordinate along the fibre, forms local coordinates by (4). The two ideals are (z,r) and (z,s_0), so

\[
I_Y=(z,rs_0).
\tag{5}
\]

This description also holds near the zero-section point of the fibre. The scheme-theoretic intersection there is (z,r,s_0), a reduced smooth elliptic curve.

On the normalization of either component each such curve is an entire smooth fibre over the v-line. Its normal line is trivial. The ordinary-double-crossing formula identifies the intrinsic smoothing line with the tensor product of those two normal lines, hence O_D. This is the supporting case of [Tziolas, arXiv:1007.3038v1, Theorem 3.5, p. 7](https://arxiv.org/pdf/1007.3038v1#page=7); the branches are labeled here, so no sheet-exchange descent remains. Directly, (5) gives the smoothing coordinate beta in rs_0=epsilon beta, restricted to D. The base equations Q_1,Q_2 trivialize this line along the whole D, and H^0(D,O_D)=C. The four curves are disjoint, giving four candidate scalars. This computation is only on the double-crossing locus.

**The complete locus at infinity.** Use the order-seven local automorphism f of the resolved fibre in L008. The j-th image has graph branches of f^j and f^(-j). Two of the four graph branches in Y can coincide at a point of S only when it is fixed by f^m for a nonzero m modulo seven, hence by f. L008 computes exactly three such points q_i, with tangent-weight pairs (6,2), (3,5), (6,2). Thus the only remaining intersections are p_i=(q_i,q_i).

Linearize f by averaging its coordinate map over its finite group, and use the same coordinates in both factors. At a point with weights (d_1,d_2), put

\[
R_\infty=\mathbb C[[u_1,u_2,w_1,w_2]],\qquad
J_k=(w_1-\zeta^{kd_1}u_1,\ w_2-\zeta^{kd_2}u_2).
\]

The completed ideals are exactly

\[
I_C=J_1\cap J_{-1},\qquad
I_{C^{(2)}}=J_2\cap J_{-2},\qquad
I_Y=\bigcap_{k\in\{1,-1,2,-2\}}J_k.
\tag{6}
\]

The scheme-theoretic intersection of the two components has ideal
(J_1 intersect J_{-1})+(J_2 intersect J_{-2}), rather than an assumed reduced point. Each difference of distinct graph matrices is invertible: both d_i and the difference of the exponents k are nonzero modulo seven. This proves pairwise transversality and finite support of the intersection. Formula (6) retains its possibly nonreduced scheme structure. Below we use puncture extension, not a normal-crossing formula or an assumed flat residual at these four-branch points.

**Every embedded lift preserves the j-map relation.** Let kappa belong to V_N and suppose Y_A is a flat embedded lift in X_A. The NS-fixed argument in L008 lifts the elliptic pencil and zero section on S independently of a support lift: the fibre line bundle lifts, its H^1 vanishes, and its generating sections lift. Identify the base with P^1_A, which is possible because P^1 is rigid. This gives pi_A:S_A -> P^1_A and its rational j-map

\[
J_A(t)=J_0(t)+\epsilon\,dJ(t).
\tag{7}
\]

The function dJ is regular at every p_{e,k}. A first-order base-coordinate change alters dJ by a multiple of J_0', so the values a_{e,k} at these critical points are independent of that change.

We claim

\[
J_A(t)=J_A(s)\quad\hbox{on }Y_A
\tag{8}
\]

where both functions are defined. This must follow from an arbitrary embedded lift, rather than from an assumption that the cover construction persists.

The first projection Y_A -> S_A is finite: it is proper and its special fibre is finite, so it is quasi-finite over the nilpotent thickening. Choose a small disk B in a dense open of the first base, avoiding branch values, singular fibres, intersection values and infinity. The central inverse image over S_B is a disjoint union of four graphs. Each first projection is an isomorphism, and each second projection is an isomorphism onto a neighbourhood of a smooth fibre. These statements follow by taking the four distinct unramified branches of the parametrizations.

The four idempotents of the finite central algebra lift uniquely over the nilpotent ideal. Each summand is A-flat and reduces to O_{S_B}. The local flatness criterion makes it a rank-one locally free module over O_{S_{A,B}}; its unit map reduces to an isomorphism and hence is an isomorphism. Each lifted summand is therefore the graph of a morphism from S_{A,B} to the other S_A.

The second base coordinate of this morphism is a function on the whole S_{A,B}, and comes from B_A. Indeed, its reduction comes from B since connected proper elliptic fibres give pi_*O_S=O_B. Subtract a lift of that base function. The remainder is epsilon times another central function, which again comes from B. Thus the graph map sends each complete smooth elliptic fibre to a fibre. Its fibre map reduces to an isomorphism and is itself an isomorphism over the dual numbers: a morphism between proper smooth curves with isomorphic special fibre is finite, and the rank-one algebra argument again identifies its structure sheaf with the target's.

Such an isomorphism preserves j. The supporting formula and theorem are [Schuett--Shioda, Elliptic Surfaces, section 2.6 and Theorem 2.4, p. 5](https://arxiv.org/pdf/0907.0298#page=5). The required direction also holds over A: after translating the image of the origin to the origin, an isomorphism of short Weierstrass equations changes x,y by u^2,u^3 for a unit u; numerator and denominator of j have the same weight. We use no converse from equal j-invariants to an isomorphism and make no assumption about twists. This proves (8) on the dense open just described.

It proves (8) everywhere that the two functions are regular. Its central reduction vanishes on Y by (3). Flatness identifies epsilon O_{Y_A} with O_Y, so the difference is epsilon times a central regular function. That function vanishes on a dense open of each component. Since Y is reduced, it is zero. This retains nilpotents in Y_A; the lifted union has not been assumed reduced.

**The global double-curve compatibility map.** Fix a sign e. At the ordered pair (p_{e,1},p_{e,2}), Y contains only its C branch; the other conic through that pair is Q_3. At (p_{e,1},p_{e,3}), it contains only its C^(2) branch. Both are smooth points of Y along whole smooth elliptic fibres. A flat lift of a smooth point is smooth over A and admits a section lifting that point. On such a section the two base coordinates can change by arbitrary epsilon multiples. Their contributions to J_0 vanish to first order because J_0' vanishes at both central coordinates. Evaluating (8) gives exactly (2). The transposed ordered pairs impose the same equalities.

At D over (p_{e,2},p_{e,3}), (3) and the nonzero derivative of R give

\[
J_0(t)-J_0(s)=h(t,s)Q_1(t,s)Q_2(t,s),\qquad
h(p_{e,2},p_{e,3})=h_e\ne0.
\tag{9}
\]

The divided difference of R is regular at the common value 2ec^7, with value R'(2ec^7). Also t-s and Q_3 are nonzero at this pair by the incidence calculation. Hence h is a unit near the entire double curve.

Choose local coordinates in X_A using the lifted base coordinates t,s. The ideal parametrization of L007 and (5) writes any flat lift locally as

\[
I_{Y_A}=(z-\epsilon\alpha,\ rs_0-\epsilon\beta),
\qquad r=Q_1(t,s),\quad s_0=Q_2(t,s).
\tag{10}
\]

The residues beta|D glue because r,s_0 are fixed functions of the two base coordinates; fibre-coordinate changes do not alter their product. Substituting (10) in (8), then restricting its epsilon coefficient to D, gives

\[
h_e\,\beta|_D+a_{e,2}-a_{e,3}=0.
\tag{11}
\]

This proves (1). Under interchange of t,s both h and the numerator change sign, so the residue on the reversed pair is the same b_e. It is a scalar on the complete elliptic curve, as required by the computed smoothing line.

Equations (2) now force b_e=0 for each sign. In linear terms, the coordinates of E_e are constraints at the smooth part of Y, and the double-curve numerator is their difference. Thus the local smoothing candidates cannot be chosen independently of the global embedding. This is the required compatibility calculation; it does not replace embedded deformations by abstract smoothings or infer vanishing from Hodge persistence. It also shows that every global embedded first-order deformation in a fixed X has zero double-curve residue.

**Recovering the first component.** Away from the three p_i, the two components are smooth and meet only along the four curves. Since beta|D=0, its central class in O_Y belongs to (r,s_0). Write beta=r b+s_0 a_0. In (10) choose lifts of these functions and absorb terms in the central ideal into the generators. The ideal becomes

\[
(z-\epsilon\alpha,\ (r-\epsilon a_0)(s_0-\epsilon b)).
\tag{12}
\]

Taking either last factor together with z-epsilon alpha gives an A-flat smooth component lift. This follows from the independent central differentials, or from the infinitesimal coordinate change sending z,r,s_0 to these lifted functions. Their intersection is (12).

The component lifts are unique with their assigned central component and their restriction off D. Two embedded first-order lifts of a smooth branch differ locally by a section of its normal bundle, by L007. If they agree on the dense complement of D, that regular section is zero. Consequently these local lifts glue with the isolated component of Y_A away from the other branch. We obtain a flat embedded lift of C on X minus {p_1,p_2,p_3}.

We need no flatness claim for a colon ideal at a point of (6). L008 gives N_C=nu_*N_j with W smooth and N_j locally free. Removing p_i removes only two points on W. Sections of N_j extend uniquely across these punctures by Hartogs, hence so do sections of N_C. On a small neighbourhood of p_i trivialize the smooth ambient deformation. By L007 the punctured lift of C is a section of N_C; extend that section and use the same ideal parametrization to obtain an A-flat lift on the entire neighbourhood. Uniqueness makes the ideals glue. Proper GAGA over A turns the resulting coherent analytic ideal into an algebraic one when these local arguments are made analytically.

Thus every Y_A with kappa in V_N yields a flat C_A in X_A. L008 then gives kappa in V_D. This proves the kernel containment even if Y has additional local deformation parameters at infinity.

**The reverse inclusion.** Vary the Dickson parameters near the very general point and take the two reduced images and their reduced union. Off the intersections these are families of smooth embedded surfaces. The four finite intersections move as distinct smooth elliptic curves. The transverse base equations and common fibre coordinate give the constant local model (5) relative to the parameters, proving flatness there.

At infinity the order-seven automorphism f varies with the parameters, and its fixed points persist as sections since df-id is invertible. Its eigenvalues remain the specified seventh roots of unity. Trivialize the two eigenlines over a small parameter neighbourhood. If M is the resulting constant derivative matrix and h_0 is a coordinate map with derivative id, then

\[
h=\frac17\sum_{k=0}^6 M^{-k}h_0\circ f^k
\]

has derivative id and satisfies h composed with f = M h. The relative inverse function theorem makes h a relative coordinate system. Use it in both factors. All four branches become the fixed linear graphs of (6), so their reduced union is a constant plane arrangement times the parameter space. This proves flatness at the isolated points. Pullback to a first-order Dickson-family direction gives a lift of Y, proving the reverse kernel inclusion.

The two inclusions give equality. The dimensions three and four from L008 give rank one on V_RM. This is a necessary and sufficient first-order statement for this support, with no conclusion about arbitrary cycle representatives.

**The cycle action and its scope.** The multiplicity calculation above and L006's trace computation with j=2 give eigenvalue theta_2 on the holomorphic line for [C^(2)]. Explicitly the deck involution of g_0 sigma^j is v -> a zeta^(-2j)/v; the sum of the two pullbacks of g_0^*omega is theta_j (g_0 sigma^j)^*omega. The injective action of the full RM field on that line therefore identifies [C^(2)] with U^2-2 id on T, since theta_2=theta_1^2-2. The components are distinct and reduced, so [Y]=[C]+[C^(2)] acts as U^2+U-2 id. It is non-scalar by the irreducible cubic for U. Its holomorphic eigenvalue is also -1-theta_3.

This is an action identity on T, not an identification of a support with a composition cycle or a claimed Chow relation. The tested representative fails the fourth-direction threshold. The known 21-dimensional cycle span is not extended to a new surface. Higher-order lifting, algebraization, arbitrary K3 surfaces and the universal Hodge target remain unresolved.

The supporting command

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/cubic-deformation/check_two_rotation_union.py

checks (3), every ordered finite incidence, simple critical points, the nonzero transverse determinants and smoothing units, the linear compatibility identity, nonemptiness of the extra j-map conditions, the action identity and the distinct infinity weights by exact cyclotomic arithmetic. It does not verify the dense-open argument for an arbitrary lift, component recovery, Hartogs extension or the global kernel inclusions; those proofs are given above.

## Mathlib

Coverage of the full statement: **not checked**. No matching or supporting Mathlib theorem, or absence from checked Mathlib sources, is asserted. The prior [two-rotation assessment](../drafts/literature/2026-09-26-current-target.md) supplies the scope comparison: general singular embedded deformation theory and the conditional double-crossing formula do not state this union's compatibility map. The supporting named statements are [Buchweitz--Flenner, Lemma 7.6, published p. 190](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=56), the linked Tziolas theorem, and the linked Schuett--Shioda formula and j-invariance theorem. L007 supplies the first-order ideal criterion, L008 the normalization, infinity geometry and obstruction of C, and L006 the correspondence action and full-field input. These are supporting inputs, not a literature match for the full result.

The general tools and family construction are imported; only the two-rotation incidence, j-map compatibility and resulting kernel test are specialized here. Their full coverage was not established in the saved bounded source review. The classification is POTENTIALLY_NEW in that limited sense, without a claim of certified originality.
