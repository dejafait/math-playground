# L062 — Conditional charge-seven family form and injective differential

## Hypotheses

Use precisely L060's conditional locally free holomorphic rank-two F
on X=B x Y, where B and Y are the same marked projective K3 surface
S of L044. Retain the exact real Kahler class h, product metric,
c_1(F)=0 and ch_2(F)=-6e_1-7e_2+tau_D. The mixed correspondence
operator D is q-self-adjoint, is 2U on T(S), and satisfies
D(sigma)=2lambda sigma, where sigma is a nonzero holomorphic
two-form under the factor marking and 1<lambda<3/2. L052 supplies
the compatible connection; L060 supplies stability of every
E_x=F|({x} x Y), with c_1(E_x)=0 and c_2(E_x)=7.

All assertions are conditional on F. Neither its existence nor a
global separated or projective moduli space at h is assumed. Write
q(alpha,beta)=integral_S alpha cup beta and identify differential-form
and Betti classes by the ordinary de Rham comparison.

## Conclusion

The raw cohomological family form is

\[
 C_F(\sigma):=p_{B*}\bigl(ch_2(F)p_Y^*\sigma\bigr)
       =2\lambda\sigma\in H^{2,0}(B).                         \tag{1}
\]

For an explicit ordered Yoneda normalization, let kappa_x be the
family Kodaira--Spencer map into Ext^1_Y(E_x,E_x), represented in
the Dolbeault complex, and set

\[
 \beta_F(v,w)=\frac{1}{(2\pi i)^2}
       \int_Y \sigma\wedge
       \operatorname{tr}\bigl(\kappa_x(v)\wedge\kappa_x(w)\bigr).
                                                                  \tag{2}
\]

Composition in (2) means the displayed order of multiplication of
End(E_x)-valued Dolbeault representatives. With this convention,

\[
                  \beta_F=-2\lambda\sigma.                       \tag{3}
\]

The pairing without the displayed prefactor is therefore
-2(2pi i)^2 lambda sigma. Reversing the Yoneda order changes its
sign. These choices do not affect nondegeneracy.

Every kappa_x is injective, of complex rank two. Thus any local
simple-bundle classifying germ for F has injective differential.
This is a conditional local constraint, not global injectivity,
an embedding, metric equality, reconstruction, existence of F,
or transverse transport. It is an ADVANCE in the notebook and a
REPRODUCTION of assessed family-form tools, with no originality
claim or additional algebraic Hodge class.

## Proof

**Imported family construction and its scope.** Use
[Kuznetsov--Markushevich, *Symplectic structures on moduli spaces
of sheaves via the Atiyah class*, arXiv:math/0703264v2,
Section 2, Theorem 2.2 and equations (12)--(14), pp. 8--10](https://arxiv.org/pdf/math/0703264v2#page=9).
Its surface specialization is the trace of the Yoneda product
paired with the surface holomorphic two-form, and its family
differential is the Kodaira--Spencer map. Section 2 permits simple
sheaves and analytic local charts. Use also
[Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*,
1997 text, Sections 10.1.6--10.1.8, Definition 10.3.1,
Lemma 10.3.3 and Proposition 10.4.1, printed pp. 219--225,
227--228](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=231).
These give the Newton/Atiyah normalization, relative trace,
family pairing and Serre-duality nondegeneracy criterion.
Their general proofs are imported. The local exterior calculation
below is necessary to translate their conventions to the ordinary
Betti ch_2 already fixed in this notebook and to (2); it is not
a reproof of their general closedness or moduli theorems.

F is flat over B since it is locally free on B x Y. Each E_x is
stable at exactly h by L060 and hence simple. For completeness,
the relevant local unobstructedness hypothesis follows from K3
Serre duality: Ext^2(E_x,E_x) is dual to Hom(E_x,E_x)=C.
The dual of its trace map is the nonzero scalar inclusion
H^0(O_Y) -> Hom(E_x,E_x). Hence the trace map is an isomorphism
and Ext^2(E_x,E_x)_0=0. This meets the smooth-locus criterion
used in Huybrechts--Lehn Section 10.2 (Theorem 4.5.4 as invoked
there). Alternatively (2) can be constructed directly from F
without any global moduli target. No change of polarization is
involved in either description.

**Evaluate the full mixed class.** Write tau_D=sum_i a_i tensor b_i
in H^2(B,C) tensor H^2(Y,C). Its conventional action from B to Y
is z -> sum_i q(z,a_i)b_i. The contraction in (1) instead gives
sum_i q(b_i,sigma)a_i, namely the q-adjoint action on sigma.
L044's self-adjointness identifies it with D(sigma)=2lambda sigma.
In particular the transpose direction has been checked, not assumed.

The two pure terms make zero contribution: e_1 p_Y^*sigma has
target degree two rather than four, and e_2 p_Y^*sigma has target
degree six, exceeding Y's top degree. Mixed divisor tensors also
contract to zero because q(NS(Y),sigma)=0. The transcendental
(2,0) tensor (0,2) component survives; it has not been discarded
by replacing the mixed tensor with its divisor part. This proves
(1) in Hodge cohomology. On a projective K3, holomorphic two-forms
inject into H^2(B,C), so this also determines their actual forms.

**Factorial, exterior sign and Yoneda convention.** We give a
Dolbeault representative computation so that no hidden convention
for the value of a Newton two-form enters (3). Choose a smooth
Hermitian metric on F and its Chern connection, with curvature R.
Import the ordinary Chern--Weil convention from
[Jean-Michel Bismut, *Index Theorem and the Heat Equation*,
Proceedings of the ICM, Berkeley 1986 (1987), p. 492, equation
(0.2)](https://www.imo.universite-paris-saclay.fr/~jean-michel.bismut/Bismut/1987c.pdf#page=2):
ch(F)=tr exp(-R/(2pi i)). Its degree-four component is

\[
                   \frac{1}{2(2\pi i)^2}\operatorname{tr}(R\wedge R).
                                                                  \tag{4}
\]

The sign choice for representing c_1 by curvature is immaterial
in this square. On a holomorphic coordinate open of B, write the
part of R with one parameter holomorphic leg and one target
antiholomorphic leg as

\[
                         \sum_j dz_j\wedge a_j.
\]

Here a_j is an End(F)-valued target (0,1)-form depending smoothly
on the parameter. To check its normalization, choose a differentiable
identification of the bundles over a small parameter open with one
fixed smooth bundle on Y. In local frames on that fixed bundle write
its relative Dolbeault operator as dbar_Y+A(z), and the horizontal
(1,0) covariant derivative as partial_j+H_j. Then

\[
 a_j=\partial_j A-\bar\partial_{\operatorname{End}(E_x)}H_j.
 \tag{4a}
\]

Indeed the commutator of these two operators is multiplication by
partial_j A-dbar_Y H_j+[H_j,A], the mixed curvature R_{j,bar Y}.
Differentiating (dbar_Y+A)^2=0 shows that partial_j A is closed
for the induced Dolbeault operator. Differentiating the holomorphic
structure of the family identifies its class with kappa_x(partial_j);
(4a) has the same class. In particular this representative involves
no 2pi i factor. The convention taking the opposite derivative changes
all these classes by the same sign, which cancels in (2).

Changing differentiable identifications changes partial_j A by a
Dolbeault coboundary. This assertion and (4a) are invariant under
the fixed bundle's frame changes, so they describe global classes
on Y. Representative independence of the ordered trace can also be
checked directly: for closed degree-one representatives a,b and
degree-zero u,v, the change under a -> a+dbar u, b -> b+dbar v is

\[
 \bar\partial\operatorname{tr}
       (u b-a v+u\bar\partial v).
\]

Here dbar is the induced operator and trace commutes with it.
Wedging with the holomorphic sigma and integrating on compact Y
kills this exact term by Stokes. This also proves directly that
(2) depends on Ext classes and is alternating by graded trace
cyclicity, rather than only on the chosen connection.

Only two such mixed terms can supply the parameter-(2,0),
target-(0,2) part of (4), since R has total type (1,1).
For j<k, their contribution to tr(R wedge R) is

\[
 dz_j\wedge dz_k\wedge
       \bigl[-\operatorname{tr}(a_j\wedge a_k)
              +\operatorname{tr}(a_k\wedge a_j)\bigr]
   =-2dz_j\wedge dz_k\wedge\operatorname{tr}(a_j\wedge a_k).
                                                                  \tag{5}
\]

The minus sign in the first term moves a target one-form past a
parameter one-form. Graded cyclicity of trace gives
tr(a_k wedge a_j)=-tr(a_j wedge a_k), including noncommuting
matrix coefficients. Consequently the 2 in (5) cancels the 2!
in (4); evaluating the resulting exterior two-form on the ordered
coordinate vectors introduces no further factorial. For fibre integration use the complex orientation and the order
parameter forms followed by target forms. Moving the target two-form
sigma past the target degree-two product has sign +1; both factors
have real dimension four, so this agrees with the Kunneth pushforward
in (1). Multiplication by sigma and fibre integration yield exactly

\[
                          C_F(\sigma)=-\beta_F.
                                                                  \tag{6}
\]

At the level of the traced curvature square, the factorial comparison
with the Atiyah/Newton description is as follows: before division
by 2!, its relevant traced square is twice the second-character
component. Its exterior evaluation contains the two ordered
products in (5). Thus neither a traced Newton square nor the raw
Betti contraction may be identified directly with the ordered
Yoneda pairing in (2). The factor (2pi i)^2 records the curvature
to integral-character conversion, and the sign in (6) records the
de Rham exterior reordering. No Mukai dual convention has been
inserted: (1) uses ch_2(F), not -ch_2(F), ch(F)^vee, or a
quasi-universal-family similitude. A differently normalized source Serre trace would give a scalar
multiple of (2); no exact scalar conversion to the printed abstract
Serre pairing is asserted here. Equations (2),(4),(5) fix the explicit
integral normalization independently of that notation.

To justify the passage from cohomology to pointwise forms without
assuming it, denote the actual curvature integral by

\[
 \gamma_R=p_{B*}\left(
   \frac{\operatorname{tr}(R\wedge R)}{2(2\pi i)^2}
      \wedge p_Y^*\sigma\right).
 \tag{7}
\]

The Chern curvature has total type (1,1); the integrand has type
(4,2), and integration along the complex surface Y gives a smooth
form of pure type (2,0) on B. The Bianchi identity makes tr(R wedge R)
closed, sigma is closed, and fibre integration on the compact
boundaryless Y commutes with d (its real dimension is even).
Thus d gamma_R=0, in particular dbar gamma_R=0, so gamma_R is
holomorphic. Its de Rham class is precisely (1). On the compact
Kahler surface B the Hodge decomposition injects holomorphic two-forms
into de Rham cohomology. Consequently gamma_R=2lambda sigma as
actual forms, with no undetermined exact term. The representative
calculation (5) gives gamma_R=-beta_F pointwise, proving (3) and
holomorphicity of beta_F. This also agrees with the imported
relative trace/Yoneda construction. No harmonicity of a chosen
mixed-curvature representative, or equality of the product metric
with a moduli metric, is used.

**Pointwise differential consequence and its limits.** A nonzero
holomorphic two-form on a K3 is nowhere vanishing. Since lambda
is nonzero, (3) is nondegenerate on each two-dimensional T_xB.
If kappa_x(v)=0, formula (2) gives beta_F(v,w)=0 for every w,
and nondegeneracy forces v=0. This proves injectivity at every
point, rather than only at a generic point or in cohomology.
The imported local moduli differential identification then gives
the stated classifying-germ interpretation.

This meets the continuation test by imposing a genuine local
constraint. It supplies no contradiction: injectivity into a
simple-sheaf tangent space is compatible with a family of stable
charge-seven bundles. Global exact-h moduli placement, existence
of F and transverse transport remain unresolved. The stopped
index/lifting mechanisms in ATTEMPTS/044--045 are not reopened.
The independent critical audit of 2026-10-06 confirms (1)--(6),
including the coefficient -2lambda in the explicit convention (2).
It supplies the explicit mixed-curvature check (4a), representative
independence and the closed pure-type argument (7) needed to audit
the pointwise inference. No coefficient correction or stronger
geometric conclusion results. No mathematical script or numerical
sampling is needed for these exact identities.

## Mathlib

Coverage of this full family-form specialization, simple-sheaf
charts and exact-h statement: **not checked**. No matching theorem
or absence is asserted. The primary sources above provide the
general family and Serre-duality inputs; L044, L052 and L060
provide the precise conditional data. This is local progress by
known-tool specialization, not a claim beyond the checked literature
or a Hodge-conjecture candidate.
