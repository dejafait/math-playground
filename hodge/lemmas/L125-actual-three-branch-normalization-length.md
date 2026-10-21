# L125 — Actual span-two triple collision has normalization length four

## Hypotheses

Retain the full conditional setting of L118, L120 and L121. Thus
X=B x Y=S_1 x S_2 is the product of the identical marked projective
complex K3 surfaces, with common hyperkähler metric g, ordered structures
I,J,K, real ample class h and Omega=p_1^*h+p_2^*h. Normalize the point
class by integral_S eta=1 and put e_1=eta tensor 1, e_2=1 tensor eta.
The full integral mixed tensor tau_D has self-adjoint cup operator D,
with D[sigma]=2lambda[sigma], sigma=omega_J+i omega_K and
1<lambda<5/4. Suppose F is holomorphic locally free of rank two,
Omega-slope-polystable, with integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Use the actual opposite stable classifying morphism
f:B -> M=M_H^s(2,0,-19) of L118, with its actual compatible connection
and natural holomorphic differential. Its metric pullback is 2lambda g.
L120 identifies B with the finite normalization nu:B -> Z of the
integral reduced scheme-theoretic image Z in M. L121 supplies distinct,
pairwise disjoint quaternionic tangent lines at distinct preimages.

Fix a closed point z of Z with exactly three distinct preimages
b_1,b_2,b_3 in B. Assume that their quaternionic tangent lines in the
common smooth ambient tangent space T_zM span quaternionic dimension
two. The ambient quaternionic dimension is 39 (complex dimension 78).
All nonlinear normal jets of the three branch maps are allowed.
No simultaneous linearization or image normality is assumed.

## Conclusion

For the actual algebraic normalization quotient

\[
 Q_z=(\nu_*\mathcal O_B)_z/\mathcal O_{Z,z}
\]

one has

\[
 \operatorname{length}_{\mathcal O_{Z,z}}Q_z=4.
                                                               \tag{1}
\]

More precisely, if m_A is the maximal ideal of A=O_{Z,z}, then
m_A^2 Q_z=0, dim_C(Q_z/m_A Q_z)=2 and dim_C(m_A Q_z)=2.
This is conditional on the stated actual collision and on F; it proves
neither that such a point occurs nor that F exists. It supplies a local
gluing input, not a global obstruction, algebraic Hodge realization or
transport. The result is a REPRODUCTION/specialization of assessed tools;
the separate step-375 critical audit below preserves it.

## Proof

**Coverage and precise imported tools.** The pre-invocation SPECIALIZE
assessment is
`drafts/literature/2026-10-18-actual-three-branch-normalization-length.md`.
It covers this exact nonlinear restriction attempt, including its
complete tail and algebraic descent. Local duplicates and failures were
checked there and in ATTEMPTS/070--072. L122 supplies all-degree
interpolation for the tangent arrangement, not the actual image ring.
The new application is justified below; no general completion or
filtered lifting theorem is reproved.

Import Wen-Wei Li, *Yanqi Lake Lectures on Algebra, Part 3*, version
2026-07-05, Lemma 5.2.3, printed p. 53,
[author-hosted PDF, p. 58](https://www.wwli.asia/downloads/YAlg3.pdf#page=58):
a filtration-preserving map with complete source, Hausdorff exhaustive
target and surjective associated graded map is surjective. Import also
[Stacks Lemma 10.97.1, 00MA](https://stacks.math.columbia.edu/tag/00MA)
(exact completion for finite modules over a Noetherian ring),
[Lemma 10.97.8, 07N9](https://stacks.math.columbia.edu/tag/07N9)
(completion of a finite algebra is the product of its local completions
above the prime),
[Lemma 10.97.3, 00MC](https://stacks.math.columbia.edu/tag/00MC)
(faithful flatness of Noetherian local completion), and
[Lemma 10.160.10(2), 0C0S](https://stacks.math.columbia.edu/tag/0C0S)
(formal coordinates for a complete regular local ring with coefficient
field equal to its residue field). The source review inspected their
statements and relevant proofs. Here the residue and coefficient field
is C throughout.

**Identify the actual completed restriction map.** Write
R=O_{M,z} and T=(nu_*O_B)_z. These are Noetherian local R and a finite
A-algebra T, respectively; A=R/I for the scheme-theoretic image ideal.
The actual map A -> T is injective by that definition. The modules
A,T,Q_z are finite over A and also over R. Completion of
0 -> A -> T -> Q_z -> 0 is therefore exact by 00MA. Completion over
R or A agrees here, since m_R maps onto m_A.

There are exactly three maximal ideals of T over m_A: their residue
points are precisely the three assumed preimages. By 07N9,

\[
 \widehat T=\prod_{i=1}^3\widehat{\mathcal O}_{B,b_i}.
                                                               \tag{2}
\]

This uses the given finite normalization, not a general assertion that
normalization commutes with completion. L118 gives a smooth algebraic
ambient germ of dimension 78 at z and B is smooth of dimension two at
each b_i. Consequently 0C0S gives

\[
 \widehat R=\mathbf C[[x_1,x_2,y_1,y_2,w_1,\ldots,w_{74}]],
 \qquad
 T_i:=\widehat{\mathcal O}_{B,b_i}=\mathbf C[[u_{i1},u_{i2}]].
                                                               \tag{3}
\]

Put n_i=(u_{i1},u_{i2}) and m=m_{\widehat R}. The completed ambient
restriction map rho:widehat R -> product_i T_i has image widehat A:
the completed surjection widehat R -> widehat A followed by the
completed injection widehat A -> widehat T is the given map. This
follows from exact completion of the original quotient and injection,
not from an assumed description of a tangent-cone ideal. Thus

\[
 \widehat Q_z=\operatorname{coker}(\rho).
                                                               \tag{4}
\]

**Normalize only tangent coordinates.** Fix I. The first two distinct
quaternionic lines give a direct sum V_1+V_2 of quaternionic dimension
two. By the span assumption V_3 is contained in that sum. Each of its
projections to V_1,V_2 is injective, since its intersection with the
other line is zero, and hence is an isomorphism. Choose complex linear
coordinates on these planes using the two projection isomorphisms.
In these coordinates the three tangent inclusions are

\[
 u\longmapsto(u,0,0),\quad
 u\longmapsto(0,u,0),\quad
 u\longmapsto(u,u,0).                                  \tag{5}
\]

Extend to linear coordinates on T_zM and choose formal parameters in
(3) inducing these cotangent bases; choose each branch's parameters
with the corresponding derivative basis. A linear change of a regular
system of parameters is still a regular system, so (3) permits these
choices. These changes need not preserve the metric. They are used
only for the local ring calculation.

Formula (5) describes the linear terms of rho. In full, its first
branch is (x,y,w)=(u_1,0,0)+O(n_1^2), its second is
(0,u_2,0)+O(n_2^2), and its third is
(u_3,u_3,0)+O(n_3^2), with independent arbitrary higher series.
In particular no nonlinear coefficient has been set to zero.

**Lift the entire order-two tail.** Let J=product_i n_i^2 inside
widehat T, and restrict rho to the filtered map

\[
 \rho_2:m^2\longrightarrow J.
\]

Use decreasing filtrations F^k(m^2)=m^{k+2} and
F^kJ=product_i n_i^{k+2}, for k>=0; for k<=0 take the full modules.
The source is complete as the closed ideal m^2 of widehat R, and J
is complete and Hausdorff in its branchwise filtration. Both are
exhaustively filtered. They are widehat R-modules via rho, and the
map preserves the filtrations because rho(m) is contained in each
branch maximal ideal. These are the filtrations used for lifting;
no intrinsic maximal-ideal filtration of the singular image is
substituted for the branchwise filtration.

For every d=k+2>=2 the corresponding associated graded map is

\[
 \operatorname{Sym}^d(T_z^*M)\longrightarrow
       \bigoplus_{i=1}^3\operatorname{Sym}^d(T_{b_i}^*B),
 \quad P\longmapsto(P(u,0,0),P(0,u,0),P(u,u,0)).          \tag{6}
\]

Indeed substitution of (5) plus terms of order at least two into a
degree-d monomial changes it only in order at least d+1; the same
holds for the degree-d leading part of any series in m^d. Thus (6)
is the actual graded map, independent of all nonlinear normal jets.
It is surjective for every d>=2 by L122's homogeneous interpolation:
the polynomial subspace using x,y alone already maps onto all three
degree-d branch spaces. The extra 74 coordinates are harmless.

Li's Lemma 5.2.3 now applies with precisely these complete filtrations
and proves

\[
                       \rho(m^2)=J.                    \tag{7}
\]

This is a complete formal lifting argument, with all graded degrees
checked by L122. It is neither finite-jet extrapolation nor a claim
of convergence for formal interpolating series. In particular an
ambient function whose linear term vanishes on the tangent span may
have nonzero quadratic restrictions; (7) has already absorbed these
and all higher restrictions into the full tail J.

**Compute exactly the remaining quotient.** By (7), J is contained
in rho(widehat R). Modulo J the target widehat T has dimension nine:
three constants and three two-dimensional linear spaces. The image
modulo J is precisely the five-dimensional space

\[
 (d+\ell_1(u_1),\ d+\ell_2(u_2),\
                 d+\ell_1(u_3)+\ell_2(u_3)),
 \quad d\in\mathbf C,\quad \ell_1,\ell_2\in(\mathbf C^2)^*.
                                                               \tag{8}
\]

Necessity follows from (5), since terms of ambient order two have no
constant or linear restriction. Sufficiency modulo J follows by the
ambient affine linear polynomial d+ell_1(x)+ell_2(y).
Together with (7), this also proves that a full formal branch tuple
is in the image exactly when its constants agree and its first
differentials satisfy dc=da+db in the coordinates (5). In particular

\[
                \dim_{\mathbf C}\widehat Q_z=9-5=4.      \tag{9}
\]

For completeness keep the module action, not just the vector-space
colength. A product of two elements of m_{widehat A}, multiplied by
any branch tuple, lies in J, so m_{widehat A}^2 widehat Q_z=0.
Multiplication by m_{widehat A} gives zero constant coordinates, so
its image is contained in the two-dimensional linear-discrepancy
subspace of (9). Both dimensions occur: the ambient coordinate x_j
times the class of (0,0,1) has branch entries
(0,0,u_{3j}+O(n_3^2)), j=1,2. These two independent classes span
that subspace. Hence the two module layers have dimensions two each.

**Descend to the original algebraic quotient.** By 00MA,
widehat Q_z=Q_z tensor_A widehat A. Its square-maximal-ideal
annihilation and faithful flatness (00MC) give m_A^2 Q_z=0:
the finite module m_A^2 Q_z has zero base change, hence is zero.
Thus Q_z has finite length. Its two layers base-change to the layers
just calculated (flatness preserves the image of multiplication and
the quotient), and the residue field stays C. Each layer therefore
has dimension two over C. This proves (1) and the asserted filtration
over A itself. In particular length is not assigned merely from a
formal preview or from the number of preimages.

**Scope and traps.** The special hypothesis of quaternionic span two
is essential to the tangent interpolation used here. This proof says
nothing about a different number of branches or a different tangent
span. It determines the quotient of the actual finite normalization
through the completed image map, while retaining every nonlinear jet.
Pairwise reduced intersections alone are not substituted for
simultaneous gluing; the length remains four rather than r-1=2.
Neither strictness of the restriction map nor simultaneous ambient
linearization was assumed. No analytic convergence is needed because
exact Noetherian completion and faithful flatness descend the finite
module calculation. The K3 and global F hypotheses are retained to
identify the actual branches, but this length calculation needs no
additional curvature assertion. It does not reopen the curvature
exclusion mechanisms in ATTEMPTS/071--072 or assert any global
cohomological consequence. F existence, actual collisions, transport
and universal primitive Hodge realization remain unresolved.

**Separate critical audit, 2026-10-18 (step 375).** The pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-18-actual-three-branch-length-critical-audit.md`
covers this exact audit. Reuse its primary statements and proof readings;
no general filtered lifting or completion theorem is reproved. The
verdict is that the conditional conclusion and both module layers survive.
There is no substantive mathematical correction or stronger conclusion.

First check the rings and maps before computing a cokernel. The finite
normalization in L120 makes T finite over A; A is a quotient of the
Noetherian local ring R, so all modules in the two sequences
0 -> I -> R -> A -> 0 and 0 -> A -> T -> Q_z -> 0 are finite over R.
The maximal-ideal filtrations from R and A agree on A-modules. Exact
completion (00MA) therefore gives both the surjection onto widehat A
and its injection into widehat T, with their composite the actual
completed pullback. The finite algebra T is semilocal, and its maximal
ideals over m_A are exactly the three specified source points; localizing
T there gives O_{B,b_i}. Thus 07N9 gives precisely (2), not an abstract
normalization of a possibly different completed image. L118's stable
germ is smooth of complex dimension 78 and the source rings are regular
of dimension two, all with their given C coefficient field. These check
every use of 0C0S in (3).

The tangent choices do not impose constraints on higher jets. In the
direct sum V_1+V_2, each projection of V_3 has zero kernel because the
three lines intersect pairwise only at zero, by L121. Each projection is
a complex-linear isomorphism of two-dimensional spaces. Transporting a
basis from V_3 to the other two lines gives (5); extend the resulting
basis to the whole ambient tangent space. Lifting these cotangent bases
to regular parameters is allowed independently in all four smooth local
rings. No orthogonality or preservation of the metric is required.

For the shifted filtrations of rho_2, the negative graded components
are zero and the kth nonzero component has degree d=k+2. A product of d
ambient parameters has leading restriction equal to the product of their
linear restrictions; any nonlinear substitution contributes order at
least d+1. This includes every monomial involving an exterior normal
parameter, whose linear restriction vanishes on every branch. For each
d>=2, L122's formula (4), with homogeneous q_i of degree d-1, gives an
ambient homogeneous polynomial in x,y attaining any prescribed triple
of degree-d polynomials. Thus all the graded maps, not just finitely
many tested ones, are surjective. The closed ideal m^2 in the complete
power-series ring is complete for m^{k+2}, and the finite product J is
Hausdorff and exhaustive for its displayed branch filtrations. The map
is a filtration-preserving widehat R-module map through rho. These are
exactly Li Lemma 5.2.3's hypotheses. Its conclusion is (7), including
arbitrary nonlinear normal corrections. This does not require strictness
of the original map or equality of an intrinsic image tangent cone.

Modulo that whole tail, the map is exactly (8). Its constant image has
dimension one and its linear image has dimension four, as the first two
branch entries independently determine ell_1 and ell_2. Hence (9) follows.
To check the module action explicitly, take an element of m_{widehat A}
whose first jets are (ell_1,ell_2,ell_1+ell_2). If a representative tuple
has constants (alpha,beta,gamma), its product has zero constants and
linear discrepancy

\[
       (\gamma-\alpha)\ell_1+(\gamma-\beta)\ell_2.
\]

Terms of order two are already in the image, so this is the entire
product class. It shows both that the image is contained in the
linear-discrepancy space and that multiplying (0,0,1) supplies every
linear discrepancy. Multiplying once more gives zero. Consequently
m_{widehat A} widehat Q_z has dimension two and its quotient has
dimension two. The wording about constant discrepancies in the proof
has been clarified: multiplication erases the constant coordinates,
not necessarily a class represented by constant tuples. This is an
expository clarification, not a change in the argument or result.

Finally 00MA identifies this computed module with Q_z tensor_A widehat A,
and 00MC makes the local completion faithfully flat. Images of
multiplication and their quotients commute with this flat base change,
so the stated annihilator and layer calculation descend exactly as above.
As a direct additional check, import
[Stacks Lemma 10.52.13 (02M1)](https://stacks.math.columbia.edu/tag/02M1),
whose statement and both proof cases were read in the audit assessment:
for a flat local map A -> C, module length after tensoring is the original
length times length_C(C/m_A C), with equivalent finiteness when the latter
length is finite. Apply this to A -> widehat A: its closed fibre is the complex residue
field of length one, and the computed tensor module has length four.
It follows directly that length_A Q_z=4. This uses the actual finite
module Q_z and introduces no analytic convergence or support assumption.

The direct local inputs remain L118, L120, L121 and L122; the DAG is
unchanged. This bounded audit is RESEARCH / REPRODUCTION / EXPLORATION,
not an advance by confirmation. It does not re-audit all upstream K3
constructions or assert anything beyond their retained hypotheses.
ATTEMPTS/070--072 remain valid within their scopes. F existence, occurrence
of the collision, other branch configurations, global sheaf consequences
and transport remain unresolved; no Hodge-class algebraicity follows.

## Mathlib

Full matching coverage for this nonlinear three-branch normalization
length specialization is **not checked**. Unknown coverage is not
evidence of absence. The complete-filtered lifting and Noetherian
completion inputs are cited precisely above; the specialization and
all nonlinear applicability checks are the informal argument here.
No Lean verification or numerical certificate is claimed.
