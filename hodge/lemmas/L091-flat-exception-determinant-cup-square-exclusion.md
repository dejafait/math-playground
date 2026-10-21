# L091 — Determinant cup-square excludes the changed-sign flat exception

## Hypotheses

Use precisely L071's marked projective complex K3 surface S, real
Kähler class h, identical hyperkähler metrics on X=S_1 x S_2 and
Omega=p_1^*h+p_2^*h. Let eta be the integral point class of integral
one, e_1=eta tensor 1 and e_2=1 tensor eta. Retain its full integral
mixed tensor tau_D, including its divisor component, and the unchanged
self-adjoint operator D and metric. Suppose F is holomorphic locally
free of rank two, Omega-slope-polystable, with integral classes

\[
c_1(F)=0,\qquad \operatorname{ch}_2(F)=-6e_1-13e_2-\tau_D.
\]

This is the correction pair (a,b)=(-10,-17). Initial higher characters
and the initial K-class are unrestricted subject to actual rank two.
Neither image, an image identification, an inverse transform, a lifted
projector nor transport is assumed. All use of F is hypothetical.

## Conclusion

No F satisfies these hypotheses. Both actual degree-one images have
two-dimensional global-section spaces with perfect symmetric forms.
Their actual restriction/trace comparisons force a determinant self-cup
with two simultaneously nonzero scalar Künneth components, contradicting
the rank-two square-zero identity.

This is a NEGATIVE / REPRODUCTION specialization of the assessed known
transform, coefficient-cohomology and duality machinery, preserved by
the separate critical audit below. It retires only this exact common-kernel recipe.
It neither excludes other Chern data nor proves Hodge nonalgebraicity,
and supplies no algebraic cycle or transverse transport. The universal
primitive rational Hodge-class gap remains open.

## Proof

**The forward image and the changed opposite fibres.** The pair satisfies
L071's necessary domain: -6(-13)=78 is 6 modulo 12 and both corrections
are at most -9. L073 and L074 therefore apply to these exact negative
mixed data. They give the actual holomorphic bundle

\[
G=R^1p_{2*}F=\mathcal O_{S_2}^{\oplus2},\qquad
Rp_{2*}F=G[-1],
\tag{1}
\]

with ordinary and derived base change. Here the equality G=O^2 is
L074's forced split conclusion at b=-17, not a reconstruction hypothesis.
Its audited preservation input supplies the compatible quaternionic
connection and slope-zero polystability at h.

Independently, L071 supplies a unitary hyperholomorphic connection on
the actual stable product F, and polystability at h on every opposite
fibre E_w=F|_{\{w\}x S_2}. Each E_w has rank two, integral c_1=0
and charge c_2=13. The split alternative at this exact h has charge
14r^2 for r in Z. Since 13 is not such a value, every E_w is stable.
Slope-zero stability gives Hom(O,E_w)=0; dual stability and K3 Serre
duality give H^2(E_w)=0. K3 Riemann--Roch then gives

\[
(h^0(E_w),h^1(E_w),h^2(E_w))=(0,9,0)
\quad\text{for every closed }w.
\tag{2}
\]

The cited surface inputs are Huybrechts, *Lectures on K3 Surfaces*,
author-hosted prepublication draft, Chapter 1 (2.5)--(2.6) and
Proposition 2.4, [pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11),
and Chapter 9 Section 3.1(ii)--(iv),
[pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175).
The all-fibre polystability and exact split lattice are L071's inputs;
ordinary restriction stability has not been assumed.

**The actual opposite image and its preservation.** GAGA algebraizes F
on projective X. For p_1, smooth projectivity gives properness, flatness
and finite presentation; F[0] is bounded coherent and base-flat with
proper support, and O_X is perfect. Import
[Stacks 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H), assigning
perfect object O_X and base-flat complex F[0]. Thus Rp_{1*}F is perfect
and compatible with derived base change. Equation (2) identifies all
its closed derived fibres as rank-nine vector spaces in degree one.
[Stacks 36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK)
gives an open rank-nine degree-one bundle locus. It contains every
closed point; its closed complement is empty because a nonempty closed
subset of a finite-type complex variety has a closed point. Hence

\[
H=R^1p_{1*}F\text{ is locally free of rank nine},\qquad
Rp_{1*}F=H[-1].
\tag{3}
\]

All other higher images vanish. Smoothness and local freeness identify
derived pullbacks of F and H with ordinary pullbacks, giving ordinary
base change as well. Proper GAGA comparison identifies H with the
actual holomorphic higher image, not just an index class.

Import Bartocci--Bruzzo--Hernandez Ruiperez, *A hyperkahler Fourier
transform*, Differential Geometry and its Applications **8** (1998),
239--249, Sections 3.1--3.3, Definition 2 and Lemmas 1--2,
pp. 243--245, and [Theorem 3, p. 246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=8).
Use source S_2 and target S_1 with their identical compatible spheres,
the flat source O_{S_2} and L071's actual hermitian quaternionic-instanton
kernel F. The source is compact, and (2) verifies odd IT at every
parameter. The theorem identifies the higher-image holomorphic bundle
with a compatible quaternionic instanton; by (3) this bundle is H.
There is no image-rank, mixed-sign positivity or equivalence hypothesis.
The alternating K-class is -[H]; it does not negate the positive bundle
or its connection. Import Verbitsky, *Hyperholomorphic connections on
coherent sheaves and stability*, math/0107182v10, Proposition 3.7 and
Lemma 3.8, [pp. 12--13](https://arxiv.org/pdf/math/0107182v10#page=12):
its invariant surface curvature has zero h-contraction coefficientwise.
The compatible unitary connection on H is consequently Hermite--Einstein
with constant zero. The real-Kähler Kobayashi--Hitchin correspondence,
Huybrechts Chapter 9, [Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182),
makes H slope-zero polystable at the same h, allowing reducibility.
These are cited general theorems with their changed-direction hypotheses
checked; no preservation theorem is reproved.

**One determinant and the actual relative forms.** Integral c_1(F)=0
and H^1(X,O_X)=0 make det(F)=O_X by the exponential-sequence injection
Pic(X)->H^2(X,Z). Fix one holomorphic trivialization, giving the perfect
alternating wedge A:F tensor F->O_X. Fix nowhere-zero two-forms sigma_i
on S_i. For either p:X->B, E=R^1p_*F is the actual G or H above.
Define Q_E by the derived cup, this same A, multiplication by the
relative sigma_i and relative trace:

\[
Rp_*F\otimes^{\mathbf L}Rp_*F\longrightarrow Rp_*O_X
\longrightarrow Rp_*\omega_p\longrightarrow O_B[-2].
\tag{4}
\]

Taking its degree-two part with Rp_*F=E[-1] gives E tensor E->O_B.
Import smooth proper coherent duality, relative dimension two,
[Stacks 48.19(2),(9), 0AU3](https://stacks.math.columbia.edu/tag/0AU3),
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT), and
the cup/trace pairing [48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q),
in the bounded coherent/perfect setting. The base coefficient is O_B;
F is locally free and p is smooth proper over a Noetherian base.
Here p^!O_B=omega_p[2]. Fibrewise, (4) is the perfect Serre pairing
on H^1(F|_{X_z}), using A and sigma_i to identify its dual coefficient.
Actual base change makes Q_E perfect on every fibre, hence as a bundle
map. The cohomological interchange of two degree-one inputs contributes
-1 and A contributes -1, so Q_E is symmetric. No phase or positivity
of this symmetric form is asserted.

**Its restriction to global sections is perfect in both directions.**
Derived composition or the single-row Leray spectral sequence,
[Stacks 20.13.1/4, 01EZ/01F2](https://stacks.math.columbia.edu/tag/01F2),
gives actual isomorphisms on the same space V:

\[
V=H^1(X,F)\xrightarrow{\ell_G}H^0(S_2,G),\qquad
V\xrightarrow{\ell_H}H^0(S_1,H),\qquad \dim V=2.
\tag{5}
\]

For G=O^2, its perfect form has a constant matrix, so it is perfect
on global sections. For H use its slope-zero stable decomposition.
Any nontrivial stable summand M has H^0(M)=H^0(M^vee)=0:
a nonzero map O->M of equal slope is an isomorphism by the stable-Hom
criterion, unless M is trivial, and the same holds for its stable dual.
This criterion is Huybrechts Chapter 9 Section 3.1(ii)--(iv), cited
above. Thus (5) makes the full trivial isotypic part of H exactly
T=O^2. Write H=T direct sum W. The cross blocks of Q_H vanish,
since Hom(T,W^vee)=Hom(W,T^vee)=0 by those section vanishings.
Perfection of Q_H therefore makes its T block perfect. Its entries
are constant on connected projective S_1; evaluation identifies H^0(H)
with T_z. Consequently both forms pull back through (5) to nondegenerate
symmetric forms on V. Perfection on all of H alone would not suffice;
the trivial-part argument is essential. No residual index or L079
branch enumeration has been used.

**Both comparisons on the same global class.** Reuse L090's audited
coefficient-cup and actual-map calculation after verifying its geometric
requirements above. Its rank-two identity and these comparisons do not
use L079's Chern pair or image ranks. Choose nonzero
theta_i in H^2(S_i,O), put x=p_1^*theta_1 and y=p_2^*theta_2, and define

\[
B(u,v)=A_*(u\smile v),\qquad B(u,u)=a(u)x+b(u)y.
\tag{6}
\]

Scalar Künneth, [Stacks 36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN),
applies over C to projective quasi-compact quasi-separated factors.
K3 H^1(O)=0 gives H^2(O_X)=Cx direct sum Cy and
H^4(O_X)=C(x cup y), with x^2=y^2=0 and x cup y nonzero.

For either projection p and closed fibre square (i,j), the section
s=ell_E(u) corresponds by derived composition to O_B->Rp_*F[1].
The morphism representing u is its pullback followed by the counit
Lp^*Rp_*F->F. The coefficient base-change map is adjoint to the
pulled-back counit, [Stacks 20.28.3, 08HY](https://stacks.math.columbia.edu/tag/08HY).
Thus evaluation s(z), followed by our actual fibre base-change
isomorphism, is precisely i^*u. No coefficient Tor term appears since
F,E are locally free and p is flat. Cup and the same A commute with
this base change, [Stacks 20.31.7/8, 0FP6/0H99](https://stacks.math.columbia.edu/tag/0H99);
retain that the general cup/base-change proof is omitted in this source.
The coefficient Dolbeault realization gives the same restriction
comparison, as explained in L090.

The fibre square is Tor independent because p is flat; j need not
be flat. All its schemes are Noetherian, quasi-compact and
quasi-separated, and p is proper flat of finite presentation.
[Stacks 48.12.4, 0AAB](https://stacks.math.columbia.edu/tag/0AAB)
identifies dualizing base change, and
[48.7.1, 0B6J](https://stacks.math.columbia.edu/tag/0B6J)
identifies the pulled-back relative trace with the fibre trace.
Applied to (4), these yield the actual equalities

\[
Q_G(\ell_Gu,\ell_Gu)=c_1a(u),\qquad
Q_H(\ell_Hu,\ell_Hu)=c_2b(u),\qquad
c_i=\operatorname{Tr}_{S_i}(\sigma_i\theta_i)\ne0.
\tag{7}
\]

Indeed p_2-fibre restriction sends x to theta_1 and y to zero;
p_1-fibre restriction does the reverse. Multiplication by sigma_i
identifies O with omega, and Serre trace on H^2(omega) is an
isomorphism to C, proving c_i nonzero. The left sides are constant
functions on their projective bases, so fibre evaluation proves (7).
Both comparisons use the very same u, A and actual edge maps;
independently selected image identifications never enter.

**The contradiction.** L090's audited coefficient identity applies
to any determinant-trivial holomorphic rank-two F on this product.
In its Dolbeault resolution a closed representative of u is locally
alpha=f_1 a+f_2 b in a determinant-one holomorphic frame. Then
A(alpha wedge alpha)=2a wedge b and its scalar square is zero.
It follows that B(u,u)^2=0 for every u. The imported coefficient
resolution/product theorem is Demailly, *L2 vanishing theorems for
positive line bundles and adjunction theory*, alg-geom/9410022v3,
28 February 1995, Section 1.A (1.1)--(1.3),
[pp. 4--5](https://arxiv.org/pdf/alg-geom/9410022v3);
its coefficient Serre pairing is Section 4.A (4.3)--(4.4'), pp. 27--28.
No multiplication of harmonic representatives is assumed.

The two nondegenerate symmetric forms on V from (5) have nonzero
quadratic polynomials q_G,q_H. The same-vector argument in L090
applies in dim V=2: take v with q_G(v) nonzero and w with q_H(w)
nonzero. Neither q_G(v+s w) nor q_H(v+s w) is the zero polynomial
(the former has nonzero constant term and the latter nonzero quadratic
coefficient). Choose s in C outside their finite sets of roots.
For u=v+s w both quadratic values are nonzero, allowing isotropic
vectors for either individual form. Equation (7) then gives a(u)b(u)
nonzero. But scalar Künneth and even-degree commutativity give

\[
B(u,u)^2=2a(u)b(u)\,x\smile y\ne0,
\]

contrary to the rank-two identity. This proves the scoped exclusion.
All bridges required by the approved stopping test succeed. The older
positive-sign numerical and orthogonal-index stops are comparisons,
not premises; the changed pair is excluded by this different global
coefficient mechanism. No other pair is asserted excluded here.

**Separate critical audit, 2026-10-11 (step 226).** The exact exclusion
survives without substantive correction. This is an EXPLORATION /
REPRODUCTION audit of the approved specialization, not a new exclusion
or a construction. The following checks concern the actual conditional
F throughout.

The numerical input is precisely p=-6, t=-13 in L071, with pt=78
congruent to 6 modulo 12. Thus audited L073/L074 apply and give the
actual G=O^2, not only its character. L071 first rules out product
line splitting using the nonzero action on the holomorphic two-form,
then supplies the compatible connection on stable F. Its restriction
to every opposite fibre is quaternionic-invariant at the unchanged
metric. Such a fibre is polystable of charge thirteen. A nonstable
rank-two polystable fibre would split into two inverse zero-slope
lines, with charge 14r^2; this cannot be thirteen. Stability and dual
stability therefore remove H^0 and H^2 on every fibre, and RR gives
h^1=13-4=9. This checks concentration rather than just constancy of
the Euler characteristic.

For the opposite projection, the perfect/base-change theorem has
perfect object O_X and base-flat bounded coefficient F[0], with
proper support. All closed derived fibres are concentrated in degree
one with dimension nine. The open bundle locus of 0BDK therefore
contains every closed point, and its closed complement in S_1 is
empty. The resulting H and both base-change maps are actual; the
negative alternating class is not substituted for a positive bundle.
BBHR's cited Definition 2, Lemmas 1--2 and Theorem 3 have compact
source S_2, flat source line, compatible spheres, the same hermitian
kernel and every-parameter odd IT. Their scope is arbitrary image
rank and permits reducibility. Surface invariant curvature has zero
h-contraction, so the preserved holomorphic H is polystable of slope
zero at exactly h. No opposite GRR, character classification or
positive-sign result is required.

Integral determinant triviality follows before any coefficient cup
is formed, since H^1(O_X)=0 makes Pic(X)->H^2(X,Z) injective. Fixing
one wedge A is therefore legitimate. In relative dimension two the
dualizing complex is omega_p[2]; both concentrated images E[-1]
meet the bounded coherent/perfect duality hypotheses. The cup, wedge,
relative two-form and trace in (4) specialize to the Serre pairing
on every H^1 fibre. The perfect alternating coefficient form and
the cohomological degree-one sign together make this pairing
symmetric and nondegenerate. Thus Q_E is an actual perfect bundle
form for each E=G,H.

The single-row Leray identifications give dim H^0(H)=dim H^0(G)=2.
In H's slope-zero stable decomposition, a nontrivial stable summand
and its stable dual have no sections by the equal-slope stable-Hom
criterion. Its full trivial part is consequently T=O^2. Writing
H=T direct sum W gives both H^0(W)=0 and H^0(W^vee)=0, killing
both off-diagonal blocks of Q_H:T plus W -> T^vee plus W^vee.
Since the whole map is invertible, its T block is invertible. Its
entries are constant because S_1 is connected and projective. This
proves perfection on global sections; perfection on H alone would
not prove it. Neither parallelness of Q_H nor determinant triviality
of H is needed. For G the same conclusion follows directly from O^2.

For the actual comparison, write P=Rp_*F=E[-1]. Under derived
composition a class u is the morphism s:O_B->P[1]=E. Its counterpart
on X is O_X->Lp^*P[1]->F[1], with second arrow the counit. For the
closed fibre square (i,j), base change is adjoint to the pulled-back
counit, as in 08HY. Hence the base-change image of s(z) is exactly
i^*u. This holds separately for p_2 and p_1 with the same u.
There is no coefficient Tor correction, since E and F are locally
free and p is flat. Restriction commutes with their holomorphic wedge
A and cup; equivalently it pulls back the same closed coefficient
Dolbeault representative and its scalar wedge product.

The trace comparison also concerns the actual morphism (4). Each
closed-fibre square is Tor independent by flatness of p, although
the closed-point map itself is not flat. Proper flat finite
presentation and the Noetherian hypotheses allow 0AAB and 0B6J to
identify the pulled-back dualizing object and trace with the fibre
ones. Consequently its value on s(z) is precisely
Tr_(S_i)(sigma_i A_*((i^*u) cup (i^*u))). On the p_2 fibre the
scalar restrictions of (x,y) are (theta_1,0), and on the p_1 fibre
they are (0,theta_2). Multiplication by sigma_i is an isomorphism
O->omega, and trace on H^2(omega) is dual to H^0(O)=C. Both constants
c_i in (7) are therefore nonzero. No equal phase, equal normalization
or positivity of these constants is needed.

Finally L090's rank-two coefficient identity applies without its
L079 numerical assumptions: in a determinant-one local frame the
scalar representative is 2a wedge b, whose exterior square vanishes
before passing to cohomology. Closedness and compatibility with the
coherent cup follow from the holomorphic wedge and coefficient
resolution. This requires no multiplicative harmonic projection.
Each pulled-back symmetric form on V is nondegenerate, so its
quadratic polynomial is nonzero by polarization over C. Along the
line v+s w used above one has a nonzero constant coefficient for
q_G and a nonzero quadratic coefficient for q_H. Avoiding finitely
many roots gives one u with both values nonzero, even when either
form has isotropic vectors. The two actual comparisons then give
a(u)b(u) nonzero. Scalar Kunneth supplies x cup y nonzero and even
degrees supply the factor 2, contradicting square-zero. This verifies
the stopping threshold for exactly the stated pair. Other correction
data, common-kernel construction and transverse transport remain open.

## Mathlib

Full matching coverage of this changed-pair exclusion, preservation,
coefficient Dolbeault comparison and both actual trace comparisons:
**not checked**. No absence claim is made. The precise general inputs
above are imported; L071, L073 and L074 supply the unchanged metric,
connection/factor hypotheses and forward image, and L090 supplies the
audited rank-two identity and actual-map method. Their exact numerical
exclusions are not generalized without the new applicability proof.
