# L070 — Rational dyadic Kummer image has index two in the norm-square unit space

## Hypotheses

Let E0/Q2 be L033's elliptic curve

    y²+y=x³−x²−10x−20,

with its specified origin O. Use L069's origin-preserving change
X=4x, Y=8y+4 to write E0 as Y²=g(X), where

    g(X)=X³−4X²−160X−1264.

Let A=Q2[X]/(g) be the ENTIRE cubic étale algebra, and let O_A be
the product of the maximal integer rings of all its field factors.
Put

    M=ker(N:O_A*/O_A*² -> Z2*/Z2*²),
    H=δ2(E0(Q2)/2E0(Q2)) ⊂ A*/A*²,

where δ2 is the full cubic two-descent Kummer map in these coordinates.
Identify M with its image in A*/A*². This is two-descent, not L033's
five-isogeny map. No global class, rank or primitive solution assumption
is imposed. The rational place exists in the whole local field algebra
of L046; the comparison itself is solely over Q2.

## Conclusion

    H ⊂ M,     [M:H]=2,     M ∩ H=H ⊊ M.

Thus the rational two-adic Kummer condition imposes one nonzero F2-linear
condition on this local norm-square unit space. This is a specialization
of a known local theorem, not a new local-image theorem. It does not
identify an excluded representative or assert that any of L069's global
norm-square unit classes is removed. Their localization could lie
entirely in H. Global coverage, the other places, rank below twelve,
subgroup indices, rational point coverage and integer lifting remain
unresolved. In particular no Beal branch is excluded.

## Proof

Import Daniel Barrera Salazar, Ariel Pacetti and Gonzalo Tornaría,
*On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020, Definition 1.6(iv), Theorem 1.8 and the FIRST
assertion of Theorem 1.11, printed pp.5–7. Published in
Math. Res. Lett. **28** (2021), 1633–1659,
[DOI](https://doi.org/10.4310/MRL.2021.v28.n6.a1).
The citation and numbering refer specifically to the inspected arXiv
version. Its local theorem says that, for a finite extension F/Q2
satisfying Definition 1.6, the full cubic Kummer image lies in the
norm-square maximal-unit subgroup with index 2^[F:Q2]. Clause (iv)
applies when F/Q2 is unramified and the elliptic curve has good
reduction. Theorem 1.8 supplies inclusion; the first-claim proof of
Theorem 1.11 supplies the index using Lemmas 1.3 and 1.5. We do not
import its separate U4 assertion or global Hypotheses 2.1.

Here F=Q2 is an unramified extension of itself, of degree one.
L069 verifies that g is monic and integral and has nonzero discriminant
−256·11^5; thus A is indeed an entire cubic étale algebra. The change
X=4x, Y=8y+4 is invertible over Q2 and carries O to the point at
infinity, so it identifies elliptic groups and their quotients by two.
L033's original integral generalized Weierstrass model has discriminant
−11^5. This is a two-adic unit, certifying good reduction of E0/Q2,
as also used in L046. The changed cubic model itself need not have
unit discriminant: clause (iv) concerns good reduction of the elliptic
curve, not smoothness of that particular integral cubic model.
No maximality of Z2[X]/(g) is required under this clause.

The definitions match the source's cubic Kummer group (Section 1,
pp.3–4): it uses the norm-square subgroup of A*/A*² with no quotient
by scalar square classes. Its integer ring is the product of maximal
rings, as in Remark 1.4. Unit square classes inject into field square
classes factor by factor: if a unit equals b² in a field, every finite
valuation of b is zero, so b is a unit. Likewise a unit of Q2 that is
a field square is a unit square. Consequently the displayed M is
exactly the image of maximal-unit classes whose norm is a square in
Q2, matching the target's convention. No polynomial-order unit group
is substituted for it. δ2 denotes the abstract map at every group
point; the theorem includes O and rational two-torsion points, without
requiring evaluation of X−θ at a zero or pole.

All hypotheses of Definition 1.6(iv) therefore hold. The cited
Theorem 1.11 gives H ⊂ M and [M:H]=2^1=2. Since these are square-class
groups, they are F2-vector spaces; a subgroup of index two is the
kernel of one nonzero linear functional. Inclusion yields M ∩ H=H,
and the index makes the containment proper. The achieved threshold
for this local comparison is strictness, with exact index two;
no global dimension decrease has been certified. Local factorization,
a torsion enumeration and an explicit class list are unnecessary
for this theorem application, and none is claimed.

### Independent critical application audit (2026-10-14)

The audit accepts the stated inclusion and index without a correction.
The computations below are exact substitutions and integer arithmetic,
not a new local-image algorithm or a reproof of the imported theorem.

Write the original homogeneous equation as

    F(x,y,z)=y²z+yz²−x³+x²z+10xz²+20z³=0.

The projective linear change

    [x:y:z] -> [4x:8y+4z:z]

has determinant 32, nonzero over Q2, and sends [0:1:0] to itself.
If G(X,Y,Z)=Y²Z−X³+4X²Z+160XZ²+1264Z³, direct expansion gives
G(4x,8y+4z,z)=64F(x,y,z). This verifies an isomorphism of the
whole projective curves preserving the origin, not merely their affine
point sets. Its affine inverse is x=X/4, y=(Y−4)/8. It transports
the group law, multiplication by two and the abstract Kummer map.
It is not claimed to be an integral change at two.

For the original coefficients
(a1,a2,a3,a4,a6)=(0,−1,1,−10,−20), the usual Weierstrass invariants are

    b2=−4, b4=−20, b6=−79, b8=−21,
    Δ=−b2²b8−8b4³−27b6²+9b2b4b6
     =336+64000−168507−56880=−161051=−11^5.

The integral model therefore has unit discriminant at two. Directly,
its affine reduction has partial derivative 2y+1=1 in F2, and its
unique point at infinity [0:1:0] has F_z=1; this also checks smooth
reduction on every chart, over the algebraic closure of F2. Thus the
elliptic curve has good reduction independently of the changed model.
For g=X³+bX²+cX+d with (b,c,d)=(−4,−160,−1264), the cubic formula gives

    disc(g)=b²c²−4c³−4b³d−27d²+18bcd
           =409600+16384000−323584−43137792−14561280
           =−41229056=−256·11^5.

Hence g is monic, integral and square-free over Q2; its reduction
need not be square-free. These are exactly the distinct hypotheses
needed for the cubic algebra and for the curve's good reduction.

L046's rational place is also explicit: its defining polynomial m
satisfies m(2u)/4 ≡ 1+u modulo two, with unit derivative. Its simple
root gives an embedding K -> Q2. The audited complete decomposition
there is Q2 times a ramified degree-eleven field. Only the rational
factor is used here; the latter field is not an unramified base for
Definition 1.6(iv). The symbols E0 here and E0(K) in the source's
different clause (iii) have different meanings; that clause is unused.

For every field factor F_i of A, if u_i is a maximal-ring unit and
u_i=b_i² in F_i, then 2v_i(b_i)=v_i(u_i)=0, so b_i is a unit.
Thus the product unit-square quotient injects into A*/A*². Norms of
units and their inverses are integral, so N(u) belongs to Z2*. If
N(u)=c² in Q2 then v2(c)=0, proving that the field-square and
unit-square norm conditions coincide. Scalar units are retained:
N(a)=a³ has square class [a], which verifies the norm convention,
not a quotient by those classes. These checks identify precisely M
with the source's norm-square subgroup in maximal rings, for any
factorization of g. They assume no maximality of the polynomial order.

Reinspection of the cited arXiv version confirms Section 1's full
cubic Kummer target and Remark 1.4's ring convention. Definition
1.6(iv) requires unramified dyadic base and good reduction of the
curve; both now hold over Q2. The good-reduction proof case of
Theorem 1.8, printed p.6, covers ordinary and supersingular reduction
separately, so no reduction-type assumption is missing. This supplies
H ⊂ M before any size comparison. In Lemmas 1.3 and 1.5, put
t=|E0(Q2)[2]|: their sizes specialize to |H|=2t and |M|=4t.
Their ratio is two, as in Theorem 1.11's first assertion and proof,
printed p.7. The same t occurs in both formulas; no assumption that
the local two-torsion is trivial, and no enumeration of it, is needed.
The abstract map includes O and every two-torsion point; an undefined
evaluation of X−theta is never used. The general source theorems,
including the cited Brumer–Kramer inputs, remain imports rather than
independently reverified proofs.

The strict local threshold is met: [M:H]=2, compared with index one
for no cut. This accepts only the necessary rational-place condition.
It supplies no nonzero value of the induced condition on L069's
global unit kernel, whose localization could be contained in H.
The existing DAG inputs remain sufficient and unchanged. The bare-unit
stop and the unresolved global rank and integer-lifting gaps remain.

## Mathlib

Full matching local dyadic image/index theorem and supporting coverage:
not checked. The mathematical input is the precise primary theorem
above; unknown Mathlib availability is not evidence of absence.
