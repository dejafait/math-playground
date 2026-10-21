# L066 — Relative Hom and its first-order test do not settle separation

## Hypotheses

Retain the conditional actual bundle F and classifying map f:B -> M of
L063--L064, with all hypotheses of L060 and L062--L064. In particular B and Y
are the specified projective K3 surfaces, F is locally free of rank two,
c_1(F)=0, ch_2(F)=-6e_1-7e_2+tau_D, and F is slope-polystable for the
specified product metric. Every E_x=F|_{x x Y} has c_1=0,c_2=7 and is
stable for L063's common H. No existence of F is established.
L065's normalization conclusion is retained as context; it is not a
mathematical input to the calculations below.

Put T=B x B, let p:T x Y -> T be projection, let F_i be pulled back
using the ith parameter, and put K=Rp_*(F_1^vee tensor F_2). Denote the
family Kodaira--Spencer maps by kappa_x, in L062's convention.

## Conclusion

The perfect complex K has derived fibre RHom_Y(E_x,E_x') at (x,x').
Its Euler characteristic is always -20. Its fibre Ext dimensions in
degrees 0,1,2 are exactly

    (0,20,0) if E_x is not isomorphic to E_x';
    (1,22,1) if E_x is isomorphic to E_x'.

Nevertheless the cohomology sheaf H^0(K) is zero on all T, including
the diagonal. Its ordinary fibres therefore do not detect the Hom jumps.

If phi:E_x -> E_x' is an isomorphism, its obstruction to extension over
the dual-number pair direction (u,v) is the class

    delta_phi(u,v)=kappa_x'(v) phi - phi kappa_x(u)
                  in Ext^1_Y(E_x,E_x').                         (1)

It extends if and only if this class vanishes. After identifying the
two bundles by phi, delta_phi has rank between two and four. On the
diagonal with phi=id its rank is two and its kernel is the diagonal
tangent space. At a hypothetical distinct isomorphic pair, injectivity
and the nonzero family form do not force a nonzero kernel: rank four
is compatible with these constraints. Conversely rank four does not
exclude an isomorphism at the central pair.

The proof gives a local perfect-complex model with precisely these
dimensions, scalar self-Hom, symplectic middle pairing, and rank-four
linear obstruction, while retaining a Hom jump at its central point.
This model is not asserted to arise from F or to have its global K-class.
Thus the Euler, cohomology-sheaf and first-order tests here do not prove
all-pair separation. The actual higher differential and global geometry
remain undetermined. This is a bounded negative test, a REPRODUCTION
of known tools, not a counterexample to separation or to the Hodge
conjecture. Full faithfulness, an embedding and existence of F are not
conclusions.

## Proof

**Imports and actual derived fibres.** Apply Stacks, Lemma 36.30.4(1),
[Tag 0B91](https://stacks.math.columbia.edu/tag/0B91), and Lemma 36.22.5,
[Tag 08IB](https://stacks.math.columbia.edu/tag/08IB). The projection p
is proper, flat and of finite presentation; its coefficient bundle is
locally free and hence perfect. Flatness gives Tor independence for
point base change. Consequently K is perfect and its derived point
pullback is R Gamma(Y,E_x^vee tensor E_x'), namely RHom_Y(E_x,E_x').
No assertion of ordinary cohomology-sheaf base change is used.
Lemma 36.31.1, [Tag 0BDI](https://stacks.math.columbia.edu/tag/0BDI),
supplies upper semicontinuity of these derived-fibre dimensions, not
vanishing at all off-diagonal points.

Import stable Hom detection and simplicity from Huybrechts--Lehn,
*The Geometry of Moduli Spaces of Sheaves*, first edition, 1997,
[Proposition 1.2.7 and Corollary 1.2.8, pp. 11--12](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=23).
L063 checks the same H, same Hilbert polynomial and stability for all
fibres. Thus Hom is zero for nonisomorphic fibres and one-dimensional
for isomorphic ones. Serre duality on the smooth projective K3 Y gives
Ext^2(E_x,E_x')=Hom(E_x',E_x)^*, since K_Y is trivial. Higher Ext groups
vanish because both sheaves are locally free and Y is a surface.

For the numerical specialization of surface Riemann--Roch, equivalently
Huybrechts--Lehn [Definition 6.1.4 and Corollary 6.1.5,
p. 142](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=154), use
ch(E_x)=ch(E_x^vee)=2-7eta and td(Y)=1+2eta. Keeping top degree gives

    ch(E_x^vee) ch(E_x') td(Y)
       =(4-28eta)(1+2eta)=4-20eta.

Hence chi(E_x,E_x')=-20, and the asserted triples follow. In the usual
Mukai convention v=(2,0,-5) has square 20 and chi=-<v,v>, confirming
the sign. No mixed term of F contributes after restricting both
parameters to points. This calculation concerns actual pair fibres,
not the full relative K-class.

**Vanishing of the sheaf does not remove the jumps.** Let
R=B x_M B, a closed subscheme of T since M is separated. Its closed
complex points are exactly pairs of isomorphic stable fibres. It is
properly contained in T: L064 gives df of rank two, so f is not constant.
The complement is a dense open in the integral T. For any nonempty
open U in T, a section of p_*(F_1^vee tensor F_2) on U is a morphism
between the two bundles on U x Y. At every complex parameter outside
R its restriction is zero by stable Hom detection. It therefore
vanishes on the dense open (U minus R) x Y. A section of a vector bundle
on the integral U x Y vanishing on a dense open is zero: locally its
coordinate functions inject into the function field. Thus this
pushforward sheaf is zero. As the input is a sheaf in degree zero,
it equals H^0(K). On every diagonal derived fibre Hom is C, so the
comparison with the zero ordinary fibre cannot be an isomorphism.

This uses neither image normality nor a diagonal-support assertion.
L065's generic-degree-one conclusion is retained but does not eliminate
the possible additional closed points of R.

**The differential on a hypothetical isomorphism.** This is a direct
linearization of the actual Hom differential, needed to test the
approved target beyond its Euler class. It is not a reproof of the
general moduli or base-change theorems. Let A=C[epsilon]/(epsilon^2).
Choose smooth trivializations of the two bundle deformations along
(u,v). Their relative holomorphic structures have the form

    dbar_1+epsilon a,  dbar_2+epsilon b,

where a and b are closed End-valued (0,1)-forms representing
kappa_x(u) and kappa_x'(v). L062's equation (4a) and L064's natural
dual-number comparison identify these with the actual algebraic
deformation classes. A smooth lift of phi is phi+epsilon psi. It is
holomorphic precisely when the coefficient of epsilon in its Hom
differential is zero, namely

    dbar_Hom psi + b phi - phi a = 0.                         (2)

The central coefficient is zero because phi is holomorphic. The class
of the last two terms in H^1(Y,Hom(E_x,E_x')) is (1). Equation (2)
has a global smooth solution exactly when this class is zero, by the
Dolbeault resolution. The resulting morphism is an isomorphism: a
morphism reducing to an isomorphism modulo a square-zero ideal has
an inverse, obtained locally by the finite inverse formula and glued
by uniqueness. Exact GAGA on the projective Y_A identifies these
holomorphic coherent morphisms with algebraic ones, as in L064.
Changing trivializations adds a coboundary, so the criterion is intrinsic.

Use phi to put both Kodaira--Spencer images in
V=Ext^1(E_x,E_x), of dimension 22 by the preceding calculation. Call
these images U_1 and U_2. Both have dimension two by L062. Formula (1)
has image U_1+U_2, so

    rank(delta_phi)=4-dim(U_1 intersect U_2) in {2,3,4}.        (3)

For x=x' and phi=id the maps coincide and their difference has
kernel {(u,u)} and rank two. The trace/Yoneda symplectic form on V
restricts nondegenerately to each U_i by L062. Transport by phi
preserves this form because conjugation preserves trace and Yoneda
composition. Nondegenerate two-planes in a 22-dimensional symplectic
space can have zero intersection. The next explicit calculation checks
compatibility with the required nonzero form, rather than assuming a
genericity property of the actual family.

**A local differential with a surviving isolated jump.** Take a
22-dimensional complex vector space V with basis e_i,f_i, 1<=i<=11,
and symplectic form omega(e_i,f_j)=delta_ij, all other pairings set by
alternation and zero. The embeddings

    k_1(u)=u_1 e_1+u_2 f_1,
    k_2(v)=v_1 e_2+v_2 f_2

have nondegenerate restrictions and independent images. Bases of each
source tangent plane may be chosen so its actual nonzero pulled-back
form has this value; this is only a pointwise linear-algebra comparison,
not an asserted coordinate identification of the actual family. Put
A_0=C[[u_1,u_2,v_1,v_2]] and s=k_2(v)-k_1(u). Consider the finite free
complex in degrees 0,1,2

    A_0 --d0--> V tensor A_0 --d1--> A_0,
    d0(a)=a s,             d1(w)=omega(s,w).                 (4)

Alternation gives d1 d0=0. At the closed origin both differentials
vanish, giving dimensions (1,22,1). At any residue field where s is
nonzero, d0 and d1 each have rank one; their composition is zero, so
the dimensions are (0,20,0). The zero locus of the coefficients of s
is precisely the origin. The Euler rank is 1-22+1=-20. Moreover d0 is
injective as an A_0-module map, since A_0 is a domain and s is nonzero;
thus the degree-zero cohomology sheaf is zero despite its derived-fibre
jump. The middle pairing omega identifies the two differentials as
adjoints up to the alternating sign. Finally the linearization of d0
on the central scalar generator is exactly k_2(v)-k_1(u), of rank four.
All assertions about (4) follow from these displayed matrices; no
numerical sampling or mathematical script is used.

This is a model for the tested local differential constraints only.
It supplies no bundle on B x Y, no global hyperholomorphic connection,
no realization of tau_D, and no global relative Chern class. It cannot
disprove separation under the full hypotheses. It does show why an
injective first-order Hom-lifting obstruction cannot remove a central
isomorphism: it can merely make the jump isolated. A further constraint
on the actual higher differential or a different global mechanism is
needed. The required all-pair degree-zero vanishing remains unproved;
full all-degree off-diagonal orthogonality is in fact incompatible with
the computed Euler value. F existence, reconstruction, transport and
the universal primitive Hodge gap remain unresolved.

## Mathlib

Full coverage of this specialization and the relative-Hom deformation
test is **not checked**. Unknown coverage is not evidence of absence.
The primary base-change, stable-Hom and RR results are cited above;
L062 and L064 supply the actual deformation/form conventions. The
explicit finite free model and rank calculation reproduce elementary
linear and homological algebra. No novelty or verified Hodge resolution
is claimed.
