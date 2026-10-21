# L051 — Factor polystability excludes the boundary topological survivor

## Hypotheses

Retain L044's final common hyperkahler metric on the very general
cubic RM K3 surface S. Write h=omega_c for its real Kahler class,
q for cup product, and sigma for a nonzero holomorphic two-form.
On X=S x S take the product metric and
Omega=p_1^*h+p_2^*h. Retain L048's full integral mixed class tau_D,
with self-adjoint operator D given by

\[
D|_{NS(S)_{\mathbb Q}}=2A_c+4\pi_K,\qquad D|_{T(S)}=2U.
\]

L044 gives D=2lambda on the metric's positive real three-plane
spanned by h, Re(sigma), Im(sigma), and D preserves its orthogonal
complement. Here lambda>1. With eta the integral point class of S,
integral_S eta=1, set e_1=eta tensor 1 and e_2=1 tensor eta.
Fix only the L050 survivor a=-7,b=-6, so p=-3,t=-2. A prospective
F is a holomorphic locally free bundle of rank two, slope-polystable
at Omega, with

\[
c_1(F)=0,\qquad \operatorname{ch}_2(F)=-3e_1-2e_2+\tau_D.
\tag{1}
\]

First Chern class zero is a cohomological assertion. No presentation,
prescribed splitting, Gieseker stability or transverse deformation
is assumed. L050's topological realization is retained, without
being promoted to a holomorphic structure.

## Conclusion

No such slope-polystable locally free F exists. Thus the fixed
boundary survivor has topological SU(2) realizations but none with
all the holomorphic and polystability hypotheses (1) at this metric.

This is an informative NEGATIVE, classified as REPRODUCTION of the
assessed hyperholomorphic and K3 cohomological tools. It closes this
one input before transverse transport. It neither excludes other
correction pairs nor proves nonexistence of all holomorphic bundles
with (1), and supplies no Hodge counterexample. The known algebraic
span remains 21 and the attained RM directions three against four
required; the universal Hodge gap remains open.

## Proof

**Import the inspected inputs.** Use Verbitsky, *Hyperholomorphic
connections on coherent sheaves and stability*,
[arXiv:math/0107182v10, Theorem 3.9, pp. 13--14](https://arxiv.org/pdf/math/0107182v10#page=13):
a stable bundle with rotation-invariant c_1,c_2 has a
hyperholomorphic Hermitian Yang--Mills connection. Its curvature is
invariant under the quaternionic SU(2) action on forms. Use
[Proposition 3.7 and Lemma 3.8, pp. 12--13](https://arxiv.org/pdf/math/0107182v10#page=12)
for zero Kahler contraction of invariant two-forms. These results
apply to the product hyperkahler manifold in the assessed scope.
Only the stable formulation is needed; total invariant classes
will not be assigned to stable summands of a polystable bundle.

Use Huybrechts, *Lectures on K3 Surfaces*, author-hosted prepublication
draft, [Chapter 9, Section 3.1, pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175)
for slope stability with a real Kahler class and dual stability,
and [Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182)
for the Hermite--Einstein/polystability correspondence. Surface and
line Riemann--Roch and Serre duality are in
[Chapter 1, equations (2.5)--(2.6) and Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11).
In particular, on S, chi(E)=2 rank(E)+c_1(E)^2/2-c_2(E)
and chi(L)=2+c_1(L)^2/2. The general theorems are imported;
the fixed-data case analysis below is their specialization. It is
needed because these statements alone do not test (1), and ordinary
restriction of a stable product bundle need not be stable.

**Exclude the split product branch without assuming summand
invariance.** A rank-two polystable bundle is either stable or a
direct sum of two stable rank-one bundles of the same slope.
Any direct summand of a locally free sheaf is locally free, so
these rank-one bundles are line bundles L,M. By c_1(F)=0,
c_1(M)=-c_1(L), hence ch_2(F)=c_1(L)^2.

Kunneth and H^1(S,Q)=0 write c_1(L)=x tensor 1+1 tensor y,
with x,y divisor classes on S: they are the first Chern classes
of restrictions of L. Thus its mixed second character is
2x tensor y, whose correspondence operator sends z to 2q(z,x)y.
For z=sigma this is zero, because divisors have type (1,1).
But the mixed class in (1) sends sigma to 2lambda sigma, which
is nonzero by L044. This contradiction excludes the entire split
product branch, including non-product presentations of L. No
invariance of c_1(L) or c_1(M) was assumed.

**Verify full-class rotation invariance in the stable branch.**
For this K3 metric, H^2(S,R) is the direct sum of the positive
three-plane and its q-orthogonal complement. The quaternionic
rotation action is the ordinary rotation representation on the
three-plane and trivial on its complement. L044's scalar and
self-adjoint properties imply that D commutes with this action.
Under the q-identification of mixed tensors with endomorphisms,
the simultaneous action on both tensor factors becomes conjugation
of D. Thus the full tau_D, not just its transcendental projection,
is invariant. Each eta is a top-degree class and is invariant too.
Consequently ch_2(F) in (1) is invariant. Since c_1=0 and
c_2=-ch_2, both classes required by the stable criterion are
invariant. That criterion now supplies a hyperholomorphic connection
nabla on F. The topological SU(2) structure group alone was not
used to obtain this connection.

**Restrict curvature before invoking surface polystability.**
For any y and x in S consider j_y(z)=(z,y) and k_x(z)=(x,z).
The differential of each embedding commutes with I,J,K: on tangent
spaces it is respectively v mapped to (v,0) and v mapped to (0,v).
Curvature of the pulled-back unitary connection is j_y^*R_nabla
or k_x^*R_nabla, by naturality of connection curvature. Quaternionic
invariance of R_nabla therefore implies invariance of each of these
endomorphism-valued two-forms on S, component by component in its
endomorphism coefficients.

The imported invariant-form contraction statement on the K3
metric gives Lambda_h(j_y^*R_nabla)=0 and the same for k_x.
The restricted connections are compatible with the restricted
holomorphic structures and have curvature of type (1,1).
They are therefore Hermite--Einstein with constant zero.
Kobayashi--Hitchin gives slope-polystability at the actual real
class h for each restricted bundle. This proves the restriction
passage; ambient Lambda_Omega R=0 by itself would not prove it.

Pullback of a mixed H^2 tensor H^2 class to either factor is zero.
From c_2(F)=3e_1+2e_2-tau_D we consequently obtain locally free
rank-two polystable bundles E_1=j_y^*F and E_2=k_x^*F with

\[
c_1(E_i)=0,\qquad \int_Sc_2(E_1)=3,\quad
\int_Sc_2(E_2)=2.\tag{2}
\]

**Treat stable surface restrictions.** If a rank-two E with
c_1(E)=0 is slope-stable at h, it has no nonzero section.
Indeed, a section injects O_S into E. Its saturated rank-one
subsheaf has determinant O_S(D) for an effective divisor D
(possibly zero), and so has degree q(D,h)>=0, contradicting
strict stability at slope zero. The dual E^* is stable of slope
zero by the imported dual-stability statement, so H^0(S,E^*)=0
as well. Since K_S is trivial, Serre duality gives H^2(S,E)=0.
Thus chi(S,E)=-h^1(S,E)<=0. But Riemann--Roch gives
chi(S,E)=4-integral_S c_2(E), which is 1 or 2 for (2).
Neither restriction can be stable.

**Treat split surface restrictions.** A remaining polystable E
in (2) must be L_1 direct sum L_2 with line classes l,-l and
both slopes zero. Whitney gives c_2(E)=-l^2. The square of an
integral line class is even, also following from the imported
line Riemann--Roch formula. This excludes second Chern number 3.
For second Chern number 2 it forces l^2=-2 and chi(L_1)=1.
Serre duality then gives

\[
h^0(L_1)+h^0(L_1^{-1})=1+h^1(L_1)\geq1.
\]

Thus L_1 or its inverse has a section. Its zero divisor is
nonzero because l^2=-2 rules out a trivial line bundle. An
effective nonzero divisor has strictly positive degree against
the Kahler class h. This contradicts q(l,h)=0 in either sign.
So neither surface restriction can be split polystable either.

All product and surface alternatives have been retained and
excluded. This proves nonexistence of F. Local freeness is essential:
rank-one torsion-free summands could carry zero-dimensional defects,
and a stable torsion-free moduli point is not a replacement for E_i.
No rational approximation of h, preservation of restriction stability,
or existence theorem for low-Chern surface bundles was invoked.
L050's topological existence is untouched. Other correction pairs
and transverse transport are outside this proof's scope.

## Mathlib

Coverage of the full fixed-survivor exclusion: **not checked**.
No matching declaration or absence from checked Mathlib sources is
asserted. The directly linked Verbitsky criterion and invariant-form
lemma, Huybrechts Theorem 4.9, surface Riemann--Roch, dual stability
and Serre duality are supporting inputs, not matches for the full
product statement. Kunneth, Whitney and curvature pullback are
standard supporting tools. This is REPRODUCTION under the saved
SPECIALIZE assessment, with no originality or Hodge resolution claim.
