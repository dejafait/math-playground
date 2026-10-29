# L156 — One additional row in the original pair's factor coordinates

## Hypotheses

Let E be any field extension of F_97. Retain C155a's original domain

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
    S={1,8,12,18,22,27,33}, J=H minus S.

The 756 labels j=(I_j,K_j) run through binom(S,2) times binom(J,2),
with I outermost and both pairs in increasing lexicographic order.
Fix any original a<b with disjoint four-element supports I_a union K_a
and I_b union K_b, and any original c distinct from a and b. There is
no disjointness, incidence, injectivity or genericity assumption on c.

Put W=E^S in increasing coordinate order. For j=a,b,c set

\[
 z_j=\min(S\setminus I_j),\qquad
 g_j(X)=\prod_{v\in J\setminus K_j}(X-v),\qquad
 (Q_jw)_u=g_j(z_j)w_u-g_j(u)w_{z_j}
 \quad(u\in(S\setminus I_j)\setminus\{z_j\}),                 \tag{1}
\]

with increasing u-order in each target E^4. These are L109's actual
quotients, not quotient maps obtained by transporting another label.
Write A=ker Q_a, B=ker Q_b. Use C155a, including its inherited audited
L155/L153 finite-input qualifications: dim A=dim B=3, A intersect B=0,
and every selected-pair decomposable point has the unique factor form
([x],[y]) in P(A)(E) times P(B)(E), with plane L=span_E(x,y).
Both selected quotient ranks are one. This lemma adds only the row c.

Define restrictions into the **same** actual target E^4 by

\[
 f_A=Q_c|_A,\quad f_B=Q_c|_B,\quad
 K_A=\ker f_A=A\cap\ker Q_c,\quad
 K_B=\ker f_B=B\cap\ker Q_c,
\]
\[
 U=\operatorname{im}f_A,\quad V=\operatorname{im}f_B,\quad
 T=U\cap V,\qquad d_A=\dim_E K_A,\quad d_B=\dim_E K_B.       \tag{2}
\]

All projective spaces below mean E-valued lines; P(0)(E) is empty.
For compact notation write P(D) for P(D)(E) in the formulas.
No coding-pencil or recovery-gate hypothesis is imposed.

## Conclusion

The exact locus R_c where rank(Q_c|_L)=1 is the disjoint union

\[
 R_c=R_{0*}\ \sqcup\ R_{*0}\ \sqcup\ R_{**},               \tag{3}
\]
\[
 R_{0*}=\mathbb P(K_A)\times
                  (\mathbb P(B)\setminus\mathbb P(K_B)),\qquad
 R_{*0}=(\mathbb P(A)\setminus\mathbb P(K_A))
                  \times\mathbb P(K_B),                     \tag{4}
\]
\[
 R_{**}=\coprod_{\ell\in\mathbb P(T)}
       F_A(\ell)\times F_B(\ell),\qquad
 F_A(\ell)=\mathbb P(f_A^{-1}(\ell))\setminus\mathbb P(K_A),
 \quad
 F_B(\ell)=\mathbb P(f_B^{-1}(\ell))\setminus\mathbb P(K_B).
                                                                  \tag{5}
\]

In (5), ell is a one-dimensional vector subspace of the common target;
the union is a disjoint union of sets of factor pairs. Its fiber over
ell is noncanonically an affine space of dimension d_A+d_B over E.
More explicitly, choose any nonzero t in ell and linear right inverses
s_A:U -> A, s_B:V -> B of the restrictions in (2). The complete fiber
is parametrized bijectively by

\[
 K_A\times K_B\longrightarrow F_A(\ell)\times F_B(\ell),\qquad
 (k,h)\longmapsto
       ([s_A(t)+k],[s_B(t)+h]).                              \tag{6}
\]

Each single factor in (5) is an affine space of dimension d_A or d_B:
f_A^{-1}(ell) has dimension d_A+1, and K_A is its codimension-one
subspace; the analogous statement holds for B. Formula (6) does not
assert a canonical or global product trivialization over P(T).

The whole rank-zero locus is exactly P(K_A) times P(K_B) and is
excluded from (3). If T=0 the both-nonzero branch is empty. If f_A=0,
(3) reduces to P(A) times (P(B) minus P(K_B)); if f_B=0 it reduces
to (P(A) minus P(K_A)) times P(B). If both restrictions are zero,
R_c is empty. These conditional statements cover all degeneracies
without asserting that each occurs for an original triple.

In any C155a factor bases a_1,a_2,a_3 of A and b_1,b_2,b_3 of B,
the data in (2) are computed from the two actual four-by-three matrices

\[
 (M_A)_{u,i}=g_c(z_c)(a_i)_u-g_c(u)(a_i)_{z_c},\qquad
 (M_B)_{u,i}=g_c(z_c)(b_i)_u-g_c(u)(b_i)_{z_c}.              \tag{7}
\]

Thus K_A, K_B are their kernels in factor coordinates, U,V their
images in the same c-target, and (4)–(6) give the requested locus in
those coordinates. No numeric pair or third label is singled out.
This is an exhaustive one-row parametrization, not a simultaneous-row
exclusion, a tractability bound, or a claim that coding gates hold.
The first separate critical audit below passes with the inherited
finite-input qualifications.

## Proof

### Imported tools and why specialization is needed

Import A. I. Kostrikin and Yu. I. Manin, *Linear Algebra and Geometry*,
Gordon and Breach paperback, 1997, ISBN 90-5699-049-7, translated from
the second Russian edition by M. E. Alferieff:
[Chapter 1 Theorem 3.12, pp. 20–21; sections 6.2–6.9, pp. 44–46;
Chapter 3 sections 6.2–6.4, pp. 222–226, 6.8–6.10, pp. 227–228,
8.1, p. 233, and 8.10, pp. 239–240](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf).
These arbitrary-field linear/projective tools give rank-nullity,
quotient cosets, coimage/image identification, projectivization away
from a kernel, intersections and projection fibers. In particular a
surjective linear map has a linear section after choosing a complement
to its kernel. A projective hyperplane complement is affine. Zero maps
use the linear formulation and the empty projective domain, rather than
assuming the nonzero summands of the source's projection construction.

The unchanged invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-25-segre-additional-row-rank-one-review.md`.
Its inspected source coverage is reused. The general projection results
are imported, not reproved. Their local use must still specify the
actual common target, prove which pairs occur, separate zero images,
and identify the fibers over E itself. C155a provides the factor
coordinates; L109 provides the actual maps and the distinction between
rank zero and rank one. The argument below is this bounded applicability
check, classified REPRODUCTION, without a novelty claim.

### Reduction to the two actual image vectors

For any factor pair choose nonzero x in A and y in B. C155a gives
x,y independent and L=span_E(x,y), so

\[
 Q_c(L)=\operatorname{span}_E\{f_A(x),f_B(y)\}.             \tag{8}
\]

Multiplying either representative by a nonzero E-scalar does not
change whether its image vanishes, its projective image when nonzero,
or the dimension in (8). By (1), restrictions in any factor bases have
exactly (7). In particular the two images are compared in the same
four-dimensional target; no independent change of target coordinates
is used for either factor.

If f_A(x)=0=f_B(y), (8) has dimension zero, and this happens exactly
on P(K_A) times P(K_B). It must be rejected. If f_A(x)=0 but
f_B(y) is nonzero, (8) has dimension one, giving exactly R_{0*}.
If f_A(x) is nonzero but f_B(y)=0, it has dimension one, giving
exactly R_{*0}. This proves both directions for every one-zero branch.

If both images are nonzero, (8) has dimension one if and only if
their projective lines coincide. That common line must lie in both
U and V, hence is a unique ell in P(T). Conversely, for such ell,
the two fiber conditions in (5) say precisely that both images are
nonzero and lie in ell, giving dimension one in (8). Thus (5) is
exhaustive in both directions. Different ell cannot give the same
factor pair, and zero versus nonzero images make all three branches
disjoint. No dimension-two image pair is inadvertently included.

This alone describes the strata but not yet their fiber parameters;
the next calculation supplies these rather than stopping at dependence
of the two images, equivalently the original exterior minors equation.

### Complete fibers, uniqueness and E-rationality

Fix ell in P(T). It is in U and V, so both f_A:A -> U and
f_B:B -> V have ell in their image. The imported coimage/image
and complement results give E-linear sections s_A and s_B. Fix a
nonzero E-vector t in ell. Since f_A(s_A(t)+k)=t for every k in K_A,
the first coordinate of (6) is nonzero and lies in F_A(ell).
Conversely, for [x] in F_A(ell) there is a unique representative x'
with f_A(x')=t: write f_A(x)=alpha*t with alpha nonzero and take
x'=alpha^{-1}x. Any two normalized representatives of the same
projective point are related by a scalar beta with beta*t=t,
forcing beta=1. Then k=x'-s_A(t) belongs to K_A and is unique.
The identical argument for B proves (6) is a bijection, including
uniqueness of both parameters. It works over E, without passing to an
algebraic closure or choosing a base-field representative of ell.

The quotient of f_A^{-1}(ell) by K_A maps isomorphically to ell,
so the imported rank-nullity and projective hyperplane-complement
description give its stated dimension and affine structure. Formula
(6) realizes the complement explicitly. If K_A=0 this is a single
point, an affine zero-space, rather than a deleted fiber. The same
holds for B. The product therefore has affine dimension d_A+d_B.

Changing the section to s'_A translates the parameter by
s_A(t)-s'_A(t) in K_A. Changing t to rho*t, rho nonzero, replaces
k by rho*k for the same projective point when the same section is
used. These invertible affine changes, and the identical changes on B,
show that the resulting locus and fiber descriptions are independent
of the choices. No choice is claimed to be canonical across ell.

### Empty and zero cases, uniformity and boundary

If T=0 there is no ell, so (5) contributes no points. A zero-dimensional
K_A or K_B has empty projectivization in (4) and in the rejected
rank-zero product. If f_A=0 then K_A=A, U=0, T=0; (5) and R_{*0}
are empty and R_{0*} is exactly the reduction stated. If f_B=0 then
K_B=B, V=0, T=0 and only the stated R_{*0} can remain. If both
are zero their surviving products are empty too, while every pair has
rank zero by (8). These exhaust the possible zero restrictions; no
division by an image has occurred before its nonzero branch is fixed.
For nonempty P(T), each fiber has points by the sections, even over
a finite E; no geometric-point existence is substituted for E-points.

The proof fixed an arbitrary original pair and an arbitrary distinct
third label over an arbitrary E/F_97. C155a's disjoint-kernel statement
is used only for A and B. Intersections of ker Q_c with either factor
are retained as K_A and K_B, and images are intersected in the actual
common target. Thus overlapping third supports and all their possible
kernel intersections are covered without a new position hypothesis.
No enumeration, new rank certificate or triple classification is used.
The direct local inputs are C155a and L109; L155 and its audited L153
input enter through C155a, with their original qualifications.

The result could constrain a later simultaneous-row factor problem,
but no compatibility of different additional rows is proved here.
In a coding application retain q=97^20, k=8, the pinned
1/4<=delta<5/16 cell, coefficient syndromes in U_S, nonzero actual D
and locators, sixteen original finite events, coding t=0, arbitrary
weights and the original chart, and L056/L069/L040 plus L051/L055
qualifications. No nonzero lambda, full recovered weights, original
finite directions, remaining-event balance or challenge identification
follows from the rank-one locus. C152a/L086/L152 and L154 are only
prospective uses, not premises. L104 survivors, L151's label limits
and ATTEMPTS/041–043,/048–049 remain intact. The frozen comparison-model
interval remains 11/q–16/q; no complete challenge candidate is asserted.

### Separate critical audit — step 493, 2026-10-25

This first audit uses the unchanged invocation-start SPECIALIZE scope
`drafts/literature/2026-10-25-l156-critical-audit-review.md`. It reuses
the inspected Kostrikin–Manin passages cited above and step 490's
duplicate/failure comparison. It checks the complete written statement,
not a generic-third or algebraically closed subcase. C155a's audited
conclusion and L109's actual maps and recovery limits were compared
directly; no passed finite certificate was replayed.

**Domain and actual maps.** C155a supplies independent x,y for every
factor pair and all original a<b; hence they are a basis of L, not
merely two possibly dependent generators. Its H,S,J and ordering agree
with (1). L109 permits any z_c in S minus I_c; the chosen minimum is
such a coordinate. Substitution of a_i and b_i into its covector gives
exactly (7), in the identical increasing c-target coordinate order.
Every g_c(z_c) is nonzero: its roots lie in J minus K_c, disjoint
from S. Thus this is the original quotient, not a transported label
or a separately rescaled target for each factor. These observations
hold over E because the label differences are already nonzero in F_97.
Only the independence of A and B is used; no condition on their
intersections with ker Q_c is inferred from support incidence.

**Exhaustion and exclusions.** In the basis x,y, Q_c|_L has columns
f_A(x),f_B(y). The four exhaustive image-vanishing possibilities are
both zero, only the first zero, only the second zero, and neither zero.
The first has rank zero and its factor pairs are exactly
P(K_A) times P(K_B). The middle two have rank exactly one and give
(4) in both directions. In the last case rank one is equivalent to
equal image lines; that unique line is contained in U intersect V.
Membership in each F_A(ell) and F_B(ell) is equivalent to a nonzero
image in this same ell. This proves the converse of (5) as well as
necessity. A pair cannot lie over two different lines. Pairs with
independent nonzero images have rank two and occur in none of (3).
Thus neither rank zero nor rank two is silently admitted.

**Complete fibers over E.** For ell in P(T), fix t in ell minus {0}.
Both maps onto U and V are surjective by their definitions, so the
finite-dimensional complement theorem supplies E-linear sections.
For any [x] in F_A(ell), write f_A(x)=alpha*t with alpha nonzero.
The vector alpha^{-1}x is the unique representative with image t:
rescaling a representative by beta changes its image to beta*t, so
preserving t forces beta=1. Subtracting s_A(t) therefore gives one
and only one k in K_A. Conversely each k gives a nonzero vector
with image t. This checks surjectivity and injectivity without an
algebraic-closure or base-field representative assumption. The B
argument is identical and independent once t is fixed. In particular
there is no additional simultaneous scalar quotient on K_A times K_B:
the two projective representatives are each uniquely normalized.

The preimage of ell surjects onto the one-space ell with kernel K_A,
so its dimension is d_A+1. Removing P(K_A) is precisely the affine
hyperplane complement covered by the cited source, not an arbitrary
bijection being used to assign geometric dimension. The two factors
therefore have affine dimensions d_A,d_B and their fiber product in
(5), over this fixed image line, has dimension d_A+d_B. A zero kernel
gives one point in its fiber, not the empty set P(0).

For a new section s'_A at the same t the parameter changes by
k'=k+s_A(t)-s'_A(t), a translation in K_A. With a fixed section and
t'=rho*t the uniquely normalized vector is rho*(s_A(t)+k), giving
k'=rho*k. Both transitions are invertible affine maps over E;
the B transitions obey the same checks. Thus the affine assertion
is valid with its stated choices and makes no global trivialization
or scheme/descent assertion.

**Degenerate cases and verdict.** If T=0 there are no shared image
lines. If K_A=0 or K_B=0 its projectivization is empty in the zero-image
strata, consistently with the single-point fiber just checked. If
f_A=0 then K_A=A and T=0, leaving only P(A) times
(P(B) minus P(K_B)); the symmetric reduction holds for f_B=0.
If both vanish that remaining complement is empty and every plane
has rank zero. When ell exists, sections give actual E-rational lifts,
also when E is finite. These checks include all conditional degeneracies
without claiming any particular one occurs in the original registry.

Pass for the full stated one-row field-valued locus, original-map
formula and affine fibers over every E/F_97, conditional on C155a's
inherited audited L155/L153 input. No statement repair, new hypothesis,
new theorem or DAG edge is needed. This is REPRODUCTION, an audit of
an existing local result, not progress beyond the checked sources.
L109's rank-one requirement is only one recovery gate: nonzero lambda,
full weights, original finite directions and the remaining sixteen-event
conditions are not supplied here. All coding qualifications in the
proof above remain. In particular this audit supplies no
simultaneous-row compatibility, solving bound or radius improvement.
ATTEMPTS/041–043,/048–049 and the L104/L151 limitations are preserved.

## Mathlib

Full matching original-pair additional-row factor-locus theorem:
**not checked**. Supporting projective linear maps, quotient fibers,
complements, affine hyperplane complements and rank-nullity coverage:
**not checked anew**. The precise standard source above supplies the
imported mathematics. Unknown Mathlib coverage is not evidence of
absence. The separate informal critical audit above is not formal
verification or a challenge resolution.
