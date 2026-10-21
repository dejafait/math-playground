# L056 — Six-charge direct-image polystability at the fixed metric

## Hypotheses

Retain L044's smooth projective complex K3 surface S, its common
hyperkahler metric with real Kahler class h=omega_c, and the product
metric with Kahler class Omega=p_1^*h+p_2^*h on S x S. Write
eta for the integral point class with integral_S eta=1,
e_1=eta tensor 1 and e_2=1 tensor eta. Retain the full integral
mixed tensor tau_D of L052: D is 2A_c+4pi_K on divisors and 2U
on T(S), is self-adjoint, and is scalar 2lambda on the metric's
positive three-plane. This is the simultaneous rotation-invariant
mixed class, including its divisor and transcendental parts.

Let b be any integer for which (a,b)=(-10,b) is an L052 survivor:

\[
b\leq-9,\qquad (-6)(b+4)\equiv6\pmod{12}.
\tag{1}
\]

Suppose F is a rank-two locally free holomorphic bundle on S x S,
slope-polystable at Omega, with cohomological Chern data

\[
c_1(F)=0,\qquad
\operatorname{ch}_2(F)=-6e_1+(b+4)e_2+\tau_D.
\tag{2}
\]

Its initial higher characters and K-class are unrestricted. No
existence of F, stability of its other-factor restrictions,
moduli interpretation, transform equivalence, or transport is assumed.

## Conclusion

For pi=p_2 the actual holomorphic sheaf

\[
G=R^1\pi_*F
\]

is locally free of rank two, commutes with base change, and is
slope-polystable of slope zero at the same real Kahler class h.
It is the holomorphic bundle of a compatible unitary quaternionic-
instanton connection at that metric. In addition,

\[
R^i\pi_*F=0\quad(i\ne1),\qquad
R\pi_*F\simeq G[-1],\qquad \pi_![F]=-[G].
\tag{3}
\]

The transform may be reducible; stability is not asserted. This is
a conditional preservation result for a hypothetical F, not existence
or an exclusion of the coefficient slice. It is a REPRODUCTION and
specialization of the assessed preservation and base-change theorems.
It supplies an input for a later surface test without enlarging the
algebraic cycle span or resolving transverse transport or the Hodge
conjecture.

## Proof

**Obtain the actual hermitian kernel from the approved local input.**
The pair in (1) satisfies L052's hypotheses: its sum is at most -19,
and its topological congruence is exactly the one in that lemma.
L052's coefficient-independent connection argument therefore applies.
In particular, the nonzero action of the mixed tensor on the
holomorphic two-form excludes line splitting of the product F.
Thus F is stable. The full first two Chern classes are rotation-
invariant, including the pure point coefficients for every b.
L052 applies Verbitsky's hyperholomorphic connection criterion,
*Hyperholomorphic connections on coherent sheaves and stability*,
[arXiv:math/0107182v10, Theorem 3.9, pp. 13--14](https://arxiv.org/pdf/math/0107182v10#page=13).
It supplies a unitary connection on the actual F, compatible with its
given holomorphic structure, whose curvature is of type (1,1) for
every induced complex structure. This is the hermitian quaternionic-
instanton kernel required below. It is not inferred merely from the
existence of a topological SU(2) bundle.

**Verify odd IT on every fibre, not just a generic fibre.**
For every closed y in S, L052's curvature-restriction argument gives
a locally free rank-two slope-polystable bundle E_y=F|_(S x {y})
at h with c_1(E_y)=0 and c_2(E_y)=6. Its zero-slope line lattice
makes a split polystable rank-two factor have second Chern number
14r^2 for an integer r. Six is not such a number, so every E_y
is stable. L052's stable surface calculation, equation (4), gives

\[
H^0(S,E_y)=H^2(S,E_y)=0,\qquad
\chi(S,E_y)=4-6=-2,\qquad h^1(S,E_y)=2.
\tag{4}
\]

There is no cohomology above degree two on this surface. The
vanishings use strict slope stability, dual stability and Serre
duality as justified in L052. The argument neither restricts b
further nor assumes stability on the other-factor fibres.

**Identify an actual locally free direct image.**
Serre's GAGA theorem makes F an algebraic vector bundle with the
same analytic fibre cohomology on the projective S x S. The
projection pi is smooth projective of finite presentation. F[0]
is a bounded coherent complex, flat over S with proper support;
O_(S x S) is perfect. Apply
[Stacks Lemma 36.30.1, Tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H):
K=Rpi_*F is perfect and commutes with arbitrary derived base change.
Its derived fibre is R Gamma(S,E_y). By (4) this is a two-dimensional
vector space in degree one at every closed point. By
[Stacks Lemma 36.31.3, Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH),
the open locus on which K is locally free of rank two in degree one
contains every closed point. Its complement is empty, since every
nonempty closed subset of this finite-type complex S has a closed
point. Thus K=G[-1] for a rank-two locally free G, and (3) holds.
Derived base change yields the ordinary base-change statement for
G as well. Analytification identifies this G with the actual
holomorphic R^1 pi_*F. The positive rank and holomorphic bundle are
obtained from fibre concentration, not from a virtual index alone.

**Import quaternionic-instanton preservation with these exact inputs.**
Use Bartocci, Bruzzo and Hernandez Ruiperez, *A hyperkahler Fourier
transform*, Differential Geometry and its Applications **8** (1998),
239--249, [Definition 2, p. 244, and Theorem 3, p. 246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6).
For a hermitian quaternionic-instanton kernel P on X x Y and a
quaternionic instanton E on compact hyperkahler X satisfying IT,
the theorem identifies the sum of the higher holomorphic direct
images of E tensor P with the holomorphic sheaf of a quaternionic
instanton on Y. Odd IT means that every even fibre cohomology
group vanishes. The proof in Sections 3.1--3.3, Lemmas 1--2,
pp. 243--246 establishes compatibility with the actual holomorphic
direct images, not merely a smooth bundle of the same K-class.
Import that theorem without reproving its twistor construction.

Set X=Y=S with the fixed metric, P=F with the connection obtained
above, and E=O_S with its flat hermitian connection. The trivial
line is a quaternionic instanton and E tensor P_y=E_y. The source
is compact; the kernel is the actual hermitian bundle on the
simultaneous product metric. Equation (4) verifies odd IT at every
y. By (3) the theorem's sum of higher direct images is precisely G.
It therefore supplies G with a unitary quaternionic-instanton
connection inducing its actual holomorphic structure. The negative
alternating class -[G] in (3) does not replace this positive
holomorphic sheaf by a negative-rank object. The theorem requires
no equivalence, moduli interpretation, or irreducibility of the
transform. Bartocci--Jardim, *Hyperkahler Nahm transforms*,
[arXiv:math/0312045v1, Theorem-Definition 3 and following remark,
pp. 4--5](https://arxiv.org/pdf/math/0312045v1#page=4), also explicitly
retains possibly reducible transforms; the published theorem is
the preservation input used here.

**Deduce polystability at h from this connection.**
On the target K3, quaternionic-instanton curvature is invariant
under the rotation action. Such two-forms have zero Kahler
contraction; apply Verbitsky, the same cited work,
[Proposition 3.7 and Lemma 3.8, pp. 12--13](https://arxiv.org/pdf/math/0107182v10#page=12).
This holds componentwise for the endomorphism-valued curvature of
G. Hence i Lambda_h R_(nabla_G)=0, the Hermite--Einstein equation
with constant zero. Its trace also gives degree_h(G)=0.
The Hermite--Einstein/polystability correspondence at a real
Kahler class, Huybrechts, *Lectures on K3 Surfaces*, author-hosted
draft, [Chapter 9, Section 3.1 and Theorem 4.9, pp. 175--176
and 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182),
therefore makes G slope-polystable at the same h. A reducible
connection is fully allowed by this conclusion. No rational
approximation of h or assumption that G is stable is used.

All three applicability tests succeed: all-fibre odd IT, local
freeness, and the compatible holomorphic identification. No
six-charge character or discriminant is evaluated in this proof.
Compatible global existence of F and its transverse transport,
other representatives, and universal primitive-Hodge algebraicity
remain unresolved.

## Mathlib

Coverage of this complete specialization and of the full hyperkahler
Fourier-transform preservation theorem: **not checked**. No matching
declaration or absence from checked Mathlib sources is asserted.
The linked primary preservation theorem, Stacks base-change results,
and real-metric Hermite--Einstein inputs are imported. L044 and L052
fix the tensor/metric and supply the connection and all-fibre
restriction test. This is local progress by REPRODUCTION under the
prior SPECIALIZE assessment, without a claim of originality or a
complete Hodge-conjecture candidate.
