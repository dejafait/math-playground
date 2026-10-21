# L061 — Rank-three image is orthogonal and necessarily nonspin

## Hypotheses

Retain L044's fixed smooth projective complex K3 S, real Kahler
class h and mixed tensor tau_D, and the hypothetical rank-two
locally free slope-polystable F of L060 on X=S x S:

\[
c_1(F)=0,\qquad ch_2(F)=-6e_1-7e_2+\tau_D.
\]

Here e_1=eta tensor 1, e_2=1 tensor eta and integral_S eta=1.
Use L052's compatible connections and L060's actual opposite image
H=R^1p_1*F, with Rp_1*F=H[-1], stable at h,
c_1(H)=0, c_2(H)=8eta and cohomology dimensions (0,2,0).
No F, lift or image existence is assumed. L059 supplies a duality
and real-reduction framework, not a pairing already proved for H.

## Conclusion

H has a perfect parallel symmetric O_S-valued form and a compatible
oriented real rank-three reduction R, with p_1(R)=-8eta. Its oriented
orthogonal torsor is a holomorphic PGL_2 torsor. Write w for its
SL_2 lifting obstruction in H^2(S,mu_2)=H^2(S,Z/2), and alpha
for the image of w in the holomorphic Brauer group. Then

\[
w=w_2(R)\ne0,\qquad \mathcal P(w)=0\ \text{in }H^4(S,Z/4).
\tag{1}
\]

In particular, its degree-two Clifford Azumaya algebra is
A=O_S direct sum H as a vector bundle, with c_2(A)=8eta and
cohomology dimensions (1,2,1). The following alternatives remain:

- alpha=0: any ordinary rank-two lift E is h-slope-stable, with
  arbitrary determinant l=c_1(E) in NS(S), satisfying
  l mod 2=w, l^2 divisible by four, and
  4c_2(E)-l^2=8. Its Mukai vector is (2,l,l^2/4), of square zero.
  Its determinant has nonzero h-degree.
- alpha!=0: the local rank-two lifts define a Brauer-twisted locally
  free E. Its descending End bundle is A; E is simple, its twisted
  Mukai square is zero, and its self-Ext dimensions are (1,2,1).

The spin alternative w=0 is impossible. Nonspin ordinary and
Brauer-twisted alternatives are not excluded by these tests. The
ordinary determinant l=f_ell, l^2=0, passes the stated characteristic
and index constraints formally; this is not existence of that lift.
No actual w or alpha of H is determined. Stop this bounded lifting
and index mechanism. This is a NEGATIVE / REPRODUCTION specialization
of the reviewed tools, with no originality or Hodge-solution claim.

## Proof

**Reapply duality to the actual image.** Torsion-free integral K3
cohomology and Kunneth make rational vanishing of c_1(F) integral
vanishing. Coherent Kunneth gives H^1(X,O_X)=0. The exponential
sequence therefore makes the Picard Chern map injective, and
det(F)=O_X. Choose its trivialization and a nonzero holomorphic
two-form on the second K3. They give a perfect alternating wedge
form b on F and a trivialization of the relative canonical bundle.

Import [Stacks 48.19, (2),(9), 0AU3](https://stacks.math.columbia.edu/tag/0AU3),
[48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q) and
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT), as checked
in the saved assessment and applied in L059. The projection is
proper smooth of relative dimension two, the base is Noetherian,
and F is locally free. Coefficient duality gives

\[
Rp_{1*}(F^\vee)[2]=R\mathcal Hom(Rp_{1*}F,O_S).
\]

L060 verifies concentration and base change on every fibre, so the
cup/wedge/trace morphism

\[
q:H\otimes H\longrightarrow R^2p_{1*}O_X\longrightarrow O_S
\tag{2}
\]

is a perfect pairing of actual bundles. Its fibre maps are the
perfect Serre pairings. The relative canonical choice identifies
R^2p_1*O_X with O_S. Swapping degree-one cohomology classes gives
a minus sign; swapping the alternating coefficients gives another.
Thus (2) is symmetric. This is the sign convention of
[Stacks 15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN);
on Dolbeault representatives the integrand is b(a,c)u wedge v,
and both factors change sign under interchange. No flat residual
or trivial summand from L059 is used here.

L060 gives the actual zero-Einstein Chern connection at h. Import
Perego, *Kobayashi--Hitchin corrispondence for twisted vector bundles*,
Complex Manifolds **8** (2021), 1--95,
[Propositions 3.9--3.12 and 3.15, pp. 36--38](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36).
The untwisted dual connection also has Einstein function zero;
the holomorphic map q:H -> H^vee is parallel by Proposition 3.15.
This verifies connection compatibility rather than assuming it
from fibrewise Serre duality.

**Real reduction and projective description.** Reapply the
dimension-independent normalization proved in L059 directly to H.
For the parallel positive Hermitian metric g, linear in its first
argument, write q(u,v)=g(u,Jv). In a unitary basis its symmetric
matrix B gives Jv=bar(B)bar(v) and J^2=B^*B>0. The parallel map
j=J(J^2)^(-1/2) is an isometric antilinear involution: unitary Takagi
diagonalization makes J=diag(s_i) times conjugation, s_i>0, and
makes j conjugation. Its fixed spaces form a parallel real
rank-three R with H=R tensor_R C. Since H^1(S,Z/2)=0, this real
bundle is oriented. Its orientation trivializes the determinant of
the complex orthogonal frames holomorphically, giving an SO_3(C)
torsor. By the defining complexification convention,
p_1(R)=-c_2(H)=-8eta. The underlying real rank-six H is different.

Import the everywhere regular complex specialization of Venkata
Balaji, *A Limiting Version of a Theorem in Cohomology*,
[math/0407079v1, Theorems 1.1 and 1.5(b), pp. 1--4;
proof p. 12](https://arxiv.org/pdf/math/0407079v1).
The base is integral, characteristic zero, and (2) is everywhere
nondegenerate. Its even Clifford algebra is degree-two Azumaya;
the oriented group identifies with its automorphisms. Locally the
split algebra is M_2 and its automorphisms are PGL_2. The ternary
representation is the traceless adjoint representation, so the
associated algebra bundle is A=O_S direct sum H, with scalar
inclusion and reduced trace projection. An overall scale of q
does not change the adjoint torsor. This imports general Clifford
lifting without assuming the algebra globally split.

The central cover SL_2 -> SO_3(C) restricts on compact groups to
SU_2=Spin(3) -> SO(3); its transition-function sign cocycle is
therefore exactly w_2(R). Use Yoshioka, *Moduli spaces of twisted
sheaves on a projective variety*,
[math/0411538v2, Section 1.1 and Lemmas 1.2--1.4, PDF p. 2](https://arxiv.org/pdf/math/0411538v2#page=2),
for the distinct SL_2 and GL_2 boundaries: alpha is the image of
w; alpha=0 gives an ordinary lift; such a lift has w=l mod 2.
Equivalently, alpha=0 iff w is in the reduction of NS(S).
Base spin and c_1(H)=0 imply none of these obstruction vanishings.

**Every ordinary lift is stable, with unrestricted determinant.**
Suppose E is an ordinary holomorphic locally free rank-two lift,
so End_0(E)=H. If E were not h-slope-stable, take a saturated
rank-one subsheaf of degree at least mu_h(E). Its double dual is
a line L; on the complement of finitely many points it is a
subbundle, and the quotient there is det(E) tensor L^(-1).
Composition quotient -> L -> E gives a generically injective map

\[
L^2\otimes\det(E)^{-1}\longrightarrow\operatorname{End}_0(E).
\tag{3}
\]

These endomorphisms have square zero and hence trace zero. Hartogs
extension for the locally free Hom bundle extends (3) over the
finite omitted set. The global map is injective since its source
is a line on an integral surface and it is generically nonzero.
Its source has degree 2deg_h(L)-deg_h(det(E))>=0. Saturating its
image cannot decrease this degree. This contradicts h-stability
of H at slope zero. Thus E is stable. This argument justifies the
changed applicability; it does not assume lift stability or put
the arbitrary determinant in L052's zero-slope lattice.

For Chern roots x,y, End_0(E) has roots 0,x-y,y-x. Consequently

\[
8=c_2(H)=4c_2(E)-l^2,\qquad l=c_1(E).
\tag{4}
\]

In particular l^2 is divisible by four. Surface RR gives
chi(E)=2+l^2/4. The ordinary Mukai vector
v(E)=ch(E)sqrt(td_S) is (2,l,l^2/4), whose square is zero.
This computation uses an actual ordinary lift only.

**Exclude the spin case.** If w=0, the holomorphic boundary
criterion supplies an SL_2 lift E with determinant O_S. By (3)
it is stable at h; (4) forces c_2(E)=2. L052's stable factor
test applies: a section would give a nonnegative-slope line,
and dual stability with K3 Serre duality similarly kills H^2.
Thus chi(E)=-h^1(E)<=0. But surface RR gives chi(E)=4-2=2,
a contradiction. These inputs are Huybrechts, *Lectures on K3
Surfaces*, author-hosted draft,
[Chapter 1, (2.5)--(2.6), Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11)
and [Chapter 9, Section 3.1, pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175).
The actual real h is retained. Hence w!=0; in particular an
ordinary lift cannot have an even determinant class.

Nor can an ordinary determinant have h-degree zero. L052 would
then give l=rk, k^2=-14. Equation (4) requires 4 to divide 14r^2,
forcing r even, so l is even and w=0, already excluded. This
deduction uses the zero-slope lattice only after testing its slope;
it does not constrain arbitrary determinants to that lattice.

**Retain the nonsplit case and evaluate its descending index.**
For any projective torsor choose local rank-two lifts of its
transitions. Scalar triple-overlap failures define an alpha-twisted
locally free E, with descending End(E)=A. No ordinary Chern
class is assigned to E when alpha!=0. L060 and K3 cohomology give

\[
(h^0,h^1,h^2)(A)=(1,2,1),\qquad \chi(A)=0.
\tag{5}
\]

In particular the global twisted endomorphisms are only scalars:
E is simple, as required for the simple-sheaf index test. Its
self-Ext groups are H^i(S,A), since E is locally free on the
gerbe and the descending Hom sheaf computes them (equivalently,
use Yoshioka's locally trivial Y-sheaf formulation).

Import [Yoshioka v2, Lemma 3.1, PDF p. 6](https://arxiv.org/pdf/math/0411538v2#page=6)
for the descending discriminant congruence. At rank two it is
8=c_2(A) congruent to -xi^2 modulo four, for any integral lift
xi of w. Such lifts exist since H^3(S,Z)=0. Therefore xi^2=0
modulo four. This is exactly P(w)=0. Independence of the lift
also follows from (xi+2z)^2-xi^2=4(xi.z+z^2).
This obtains (1) without presuming a vanished w_4 or a spin lift.

In the conventions of [Yoshioka v2, Definition 3.1 and (3.3),
PDF p. 7; Proposition 3.6, p. 8](https://arxiv.org/pdf/math/0411538v2#page=7),
the twisted Mukai square is -chi(E,E)=-chi(A)=0, above the
necessary lower bound -2. The self-Ext middle dimension is two,
and its symplectic parity also passes. Proposition 3.6 applies
to a simple sheaf and does not require replacing h by a general
ample polarization. Its smooth dimension-two deformation conclusion,
conditional on E, constructs no sheaf or family here. For an
ordinary lift (5) gives the same compatible simple index.

**What the surviving tests do and do not imply.** The integral
primitive fibre class f_ell is in L052's divisor basis and has
square zero. It is not even. Thus the formal ordinary choice
l=f_ell has nonzero w, alpha=0, c_2(E)=2 and primitive isotropic
vector (2,f_ell,0), satisfying (4)--(5). Its h-slope is positive,
so L052's slope-zero section vanishing cannot be applied to it.
This is a witness to compatibility of these necessary equations,
not construction of a stable E or identification with H. Arbitrary
determinants cannot be half-normalized by an imaginary line bundle.

For alpha!=0, (1) and (5) leave nonzero obstruction classes and
a compatible simple index; the calculation neither selects the
actual class nor proves all such classes realizable at charge eight.
The inspected degree-two Azumaya examples of Ingalls--Khalid,
*An explicit derived equivalence of Azumaya algebras on K3 surfaces
via Koszul duality*,
[1104.4333v3, Theorems 4.3 and 4.7, pp. 10,15](https://arxiv.org/pdf/1104.4333v3),
already have the same adjoint character/cohomology on their specified
double-plane K3 surfaces. As recorded in the prior assessment,
their hypotheses do not identify L044's S,h or supply F. No
general charge-only exclusion is inferred. Exact-h twisted existence,
kernel reconstruction and transport are outside this bounded test.
The main primitive Hodge gap is unchanged.

## Mathlib

Full coverage of this holomorphic lifting and exact-metric
specialization: **not checked**. No matching declaration or absence
claim is made. The cited primary duality, connection, Clifford,
lifting and index results are imported; their applicability, pairing
sign, stable-lift test, spin contradiction and characteristic values
are the necessary local REPRODUCTION. No new algebraic cycle,
transverse surface or complete Hodge candidate is supplied.
