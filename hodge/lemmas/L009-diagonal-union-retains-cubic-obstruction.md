# L009 — Adding the diagonal retains the cubic support's transverse obstruction

## Hypotheses

Let S, C, X=S x S, V_N, V_RM, and V_D satisfy L008. Write pi:S -> P^1 for the elliptic fibration, F for its fibre class, zeta=exp(2 pi i/7), and

\[
Y=C\cup\Delta_S
\]

for the reduced scheme-theoretic union. Work over A=C[epsilon]/(epsilon^2), with the **same** first-order deformation S_A in both factors of X_A=S_A x_A S_A.

Retain the very-general hypotheses, and explicitly require that the degree-21 polynomial

\[
4(b_1P_a(t)+b_0)^3+27(c_1P_a(t)+c_0)^2
\]

has distinct finite roots and does not vanish at the two numbers t_+,t_- defined below. Thus there are 21 distinct finite nodal fibres and the two specified fibres are smooth. These are open conditions satisfied at very general parameters: the cubic in P_a has three distinct roots avoiding the two critical values of P_a. In particular at least five nodal values are available. Singular specializations are excluded.

Let N_Y=Hom(I_Y/I_Y^2,O_Y). Use the ideal-sheaf obstruction

\[
\operatorname{ob}_Y(\kappa)=H^1(\delta_Y)(\kappa_X|_Y),
\qquad \delta_Y(D)(h)=D(h)\bmod I_Y.
\]

The general ideal-gluing argument in L007 applies to this ideal too: its vanishing is equivalent to a flat embedded first-order lift of Y in X_A. No lci hypothesis on the entire Y is imposed.

## Conclusion

Every flat embedded first-order lift Y_A contains the relative diagonal Delta_{S_A}. It also yields a flat embedded first-order lift of C, including at the three points over infinity. Consequently

\[
\ker(\operatorname{ob}_Y|_{V_N})=V_D,
\qquad
\dim\ker(\operatorname{ob}_Y|_{V_{\rm RM}})=3,
\qquad
\operatorname{rank}(\operatorname{ob}_Y|_{V_{\rm RM}})=1.
\]

In particular adding the diagonal does not remove the obstruction in the fourth RM tangent direction. The action of [Y] on T(S) is U+id, by L006 and L007; subtracting the always-algebraic diagonal would recover U if this union extended. The obstruction concerns this reduced representative, not every cycle with that action. The required 21-dimensional Hodge span is still attained only on the already treated family, and the universal rational Hodge conjecture remains unresolved.

## Proof

**The intersection contains two curves.** On the finite chart of L007 put

\[
t=v+a/v,\qquad s=\zeta v+\zeta^{-1}a/v.
\]

The equations of the two elliptic points use the same x,y. Thus the intersection with the diagonal occurs when t=s, namely

\[
v^2=a/\zeta.
\]

Choose its two roots v_+,v_- and set t_\pm=(1+\zeta)v_\pm. These are two distinct finite numbers. Write F_\pm=pi^{-1}(t_\pm). The finite intersection is the diagonal copy of each smooth elliptic curve F_\pm, with no other finite points. This includes their zero-section points: the maps identify the entire smooth fibres, not merely the affine Weierstrass charts.

At either root,

\[
\frac{dt}{dv}=1-\zeta\ne0,\qquad
\frac{ds}{dv}=\zeta-1,\qquad \frac{ds}{dt}=-1.
\]

Both projections of the relevant branch of C are locally isomorphisms. To see its local involution explicitly, eliminate v to obtain the symmetric conic relation

\[
t^2+s^2-(\zeta+\zeta^{-1})ts
=a\bigl(4-(\zeta+\zeta^{-1})^2\bigr).
\]

Its s-derivative at (t_\pm,t_\pm) is nonzero. The implicit function s=f_base(t) near this point is therefore an involution, by symmetry and uniqueness, with derivative -1. The corresponding local isomorphism f on S fixes x,y and the entire fibre. A base coordinate u=(t-f_base(t))/2 satisfies f^*u=-u. Averaging a local fibre coordinate with its pullback by f gives a coordinate w with f^*w=w; its derivative along the fixed fibre remains nonzero. Hence f(u,w)=(-u,w).

In product coordinates put

\[
r=u_2-u_1,\quad s_0=u_2+u_1,\quad z=w_2-w_1.
\]

With w=w_1, the union has local ideal

\[
I_Y=(z,rs_0),\quad I_\Delta=(z,r),\quad I_C=(z,s_0).
\tag{1}
\]

It is a curve times a node, and is lci along these two curves. In particular it has a local smoothing parameter: one can replace rs_0=0 by rs_0=epsilon. This is why the locally trivial normalization argument for C alone cannot simply be repeated for Y.

At infinity, L008 identifies the two branches of C as graphs of f and f^(-1), where f has order seven. Intersecting either graph with the diagonal gives exactly the same three fixed points as in L008. Denote these points on S by q_1,q_2,q_3 and put p_i=(q_i,q_i). The tangent weights (6,2), (3,5), (6,2) show that id, f, and f^(-1) have pairwise transverse graph tangent planes there. The intersection scheme at these isolated points need not be reduced; no reduced-point or flatness assumption about that intersection will be used.

**A lifted diagonal branch defines a meromorphic vector field.** Suppose Y_A is a flat embedded lift. Set

\[
S^\circ=S\setminus(F_+\cup F_-\cup\{q_1,q_2,q_3\}).
\]

Over this open set the central diagonal is disjoint from C. The first projection of Y_A is finite: it is proper, and its special fibre is finite, so it is quasi-finite and hence finite over the nilpotent base. Its algebra over S_A^circ has a unique lifted idempotent selecting the central diagonal summand. That summand is A-flat and reduces to O_{S^circ}; the local flatness criterion and Nakayama's lemma identify its unit map with O_{S_A^circ}. Equivalently, the lifted diagonal branch maps isomorphically to S_A^circ under the first projection.

Its second projection reduces to the identity, so it differs from the identity by epsilon times a derivation. This gives

\[
v\in H^0(S^\circ,T_S).
\]

This step uses that both ambient factors are the same S_A. There is no difference of two Kodaira–Spencer classes to absorb into v.

Use the same local coordinates on both factors of S_A near F_\pm, so that the actual relative diagonal is still (z,r)=0. The ideal-parametrization from L007 and (1) give local equations

\[
z=\epsilon\alpha,\qquad rs_0=\epsilon\beta,
\]

where alpha and beta are regular functions modulo (z,rs_0). Restricting their central classes to the diagonal, where s_0=2u, yields on u nonzero

\[
v=\frac{\beta_\Delta}{2u}\frac{\partial}{\partial u}
  +\alpha_\Delta\frac{\partial}{\partial w}.
\tag{2}
\]

Thus v has at worst a simple pole along each of F_+,F_-, and its possible polar part is in the base direction. The formula covers the whole smooth elliptic fibre using the invariant local coordinates just constructed. At the three omitted isolated points, sections of a vector bundle on the smooth surface extend across a puncture by Hartogs. Consequently

\[
v\in H^0\bigl(S,T_S(F_++F_-)\bigr).
\tag{3}
\]

Here and below the algebraic Hartogs fact follows from a locally free module being reflexive over a normal local domain: it is the intersection of its height-one localizations. See the supporting [Stacks Project, Lemma 15.24.18, tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB). Analytically it is the usual extension theorem applied to the coefficients in a local trivialization.

**The singular fibres prohibit those polar parts.** Apply dpi to (3). Since pi has connected fibres, pi_*O_S=O_{P^1}; also O_S(F_++F_-)=pi^*O_{P^1}(t_++t_-). The projection formula identifies dpi(v) with a section

\[
\xi\in H^0\bigl(P^1,T_{P^1}(t_++t_-)\bigr)
      =H^0(P^1,O(4)).
\]

At the node of every finite singular fibre, pi has a critical point: in smooth surface coordinates its local map is t-t_0=xy up to analytic coordinates. The vector field v is regular there, since these fibres are disjoint from F_+,F_- and the omitted points at infinity. Evaluating dpi(v) at this critical point gives zero. Therefore xi vanishes at each of the 21 distinct finite nodal values. A nonzero section of O(4) has at most four zeros counted with multiplicity, so xi=0.

In (2) this forces beta_Delta=0, and the remaining component is regular across u=0. Thus v extends to a global holomorphic vector field on S. A K3 has none: contraction with its nowhere-vanishing holomorphic two-form identifies T_S with Omega_S^1, and H^0(S,Omega_S^1)=0. Hence v=0.

It follows that the lifted branch equals the actual diagonal on S_A^circ. The restriction of I_{Y_A} to O_{Delta_{S_A}} is zero everywhere: each local restricted function has zero reduction, is therefore epsilon times a regular function on S, and vanishes on the dense open S^circ; that regular function is zero. We have proved

\[
\Delta_{S_A}\subset Y_A
\tag{4}
\]

scheme-theoretically, including at infinity. In particular a local node-smoothing parameter cannot be used by a global lift to evade (4).

**Extracting C away from the three isolated points.** Locally at a finite double curve, (4) forces alpha and beta in the preceding equations to vanish on the diagonal. Modulo (z,rs_0), both are thus multiples of r. Absorbing multiples of z by elementary changes of generators puts the ideal in the form

\[
J_A=(z-\epsilon r a_0,\ r(s_0-\epsilon b_0)).
\]

Its colon by I_{Delta_A}=(z,r) is

\[
J_A:(z,r)=(z-\epsilon r a_0,\ s_0-\epsilon b_0).
\tag{5}
\]

For completeness, after quotienting by z-epsilon r a_0, the ring is A[[r,s_0,w]], the diagonal ideal is (r), and J_A is (r(s_0-epsilon b_0)). Multiplication by r is injective, so the colon is (s_0-epsilon b_0), proving (5). The two residual equations have independent central differentials dz,ds_0, so their quotient is A-flat and is a deformation of the smooth C branch.

Away from the diagonal the residual is simply Y_A; away from C it is empty. These local residual ideals therefore define a flat embedded C_A^circ on X_A minus {p_1,p_2,p_3}, with special fibre C minus those points. This does not yet assume anything about colon flatness at a three-branch point.

**Hartogs fills the isolated gaps in the residual lift.** L008 gives

\[
N_C=\nu_*N_j,
\]

where nu:W -> C is finite, W is smooth, and N_j is a vector bundle. Removing any p_i removes only two points from W. Hartogs for this vector bundle therefore gives, on a sufficiently small neighbourhood U of p_i,

\[
H^0(U,N_C)\xrightarrow{\ \sim\ }H^0(U\setminus\{p_i\},N_C).
\tag{6}
\]

Trivialize the smooth ambient first-order deformation on U. By the ideal-parametrization in L007, the already constructed residual lift on its puncture is a section of N_C there. Extend it uniquely using (6). The extended section defines an A-flat ideal lifting I_C on all of U, again by the same ideal-parametrization. Uniqueness ensures agreement with C_A^circ on overlaps. These ideals glue to a flat embedded C_A in X_A.

This argument neither asserts that Y_A has a simultaneous normalization nor applies a lci theorem at its three-branch points. Nor does it assume that a colon ideal is automatically flat at an isolated intersection. The specific Hartogs property of the already computed N_C is the reason those points cannot rescue a transverse lift.

**Both kernel inclusions.** We have shown that a lift of Y yields a lift of C. For kappa in V_N, L008 then gives kappa in V_D. This proves the kernel containment in V_D.

Conversely, vary the Dickson parameters in a small neighbourhood satisfying the hypotheses and form the relative reduced union with the diagonal. Away from its intersection loci it is a family of smooth embedded surfaces. Along each of the two moving smooth fibres, the involution coordinates used in (1) give a relative model (z,rs_0), so it is flat there.

At infinity the local order-seven action f from L008 varies with the parameters. Each fixed point extends as a section, since df-id is invertible. Its two eigenvalues are fixed seventh roots of unity, and its tangent eigenspaces can be trivialized over a small parameter neighbourhood. In any local coordinates with derivative id, the averaging formula

\[
h=\frac1{7}\sum_{k=0}^6 M^{-k}\,h_0\circ f^k,
\qquad M=df,
\]

has derivative id and satisfies h composed with f = M h. It is therefore an invertible relative coordinate change, by the inverse function theorem. Use this same coordinate change in both factors. The three graphs become the fixed linear graphs of id, M, M^(-1). Their reduced union is a constant three-plane arrangement times the parameter space, hence flat. This also checks the isolated points omitted in the residual extraction.

Thus the Dickson family supplies flat lifts of Y in every direction of V_D. Proper GAGA over the dual numbers identifies the analytic embedded ideals used in these local arguments with algebraic ones. The two inclusions prove the claimed kernel equality. The dimensions dim V_D=3 and dim V_RM=4 from L008 then give rank one on V_RM.

The local smoothing calculation was necessary but not sufficient: it exhibited parameters that the global vector-field calculation forces to vanish. The achieved kernel is three-dimensional; removing the transverse obstruction would require four. This is a negative result for adding this diagonal, not an obstruction to a different added component or to every algebraic representative of the Hodge class.

`python3 scripts/cubic-deformation/check_diagonal_union.py` checks the finite intersection equation, slope -1, critical-fibre identity, conic relation, and distinct graph tangent eigenvalues with exact cyclotomic arithmetic. It does not verify the global vector-field, Hartogs, or flat-family arguments, which are given above.

## Mathlib

Coverage of the full statement: **not checked**. No matching or supporting Mathlib theorem, or absence from Mathlib, is claimed. L006 and L007 supply the cycle action and ideal-deformation parametrization; L008 supplies the three isolated points, the normal-sheaf Hartogs input, and the kernel for C. The directly linked [Stacks Project tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB) supports extension of sections of a vector bundle across codimension two; it is neither a Mathlib match nor a citation for this union's obstruction theorem. Idempotent lifting over nilpotent ideals, the local flatness criterion, the projection formula, and proper GAGA are supporting named standard results. The finite-curve analysis, forced diagonal, residual extraction, and both kernel inclusions are proved here.
