# L073 — Sign-reversed six-charge direct-image polystability

## Hypotheses

Retain L071's marked smooth projective complex K3 surface S, its real
Kähler class h=omega_c and the identical hyperkähler metric on both
factors of X=S x S. Put Omega=p_1^*h+p_2^*h. Write eta for the
integral point class, integral_S eta=1, e_1=eta tensor 1 and
e_2=1 tensor eta. Retain L071's full integral mixed class tau_D,
with q-self-adjoint operator D, scalar 2lambda on the metric's
positive three-plane and preserving its orthogonal complement.
Here lambda is the positive root of z^3+z^2-2z-1. These are the
full marked metric and tensor, including the divisor and
transcendental parts, rather than a transcendental projection alone.

Let b be any integer admitted by L071 at a=-10, that is,

\[
b\leq-9,\qquad -6(b+4)\equiv6\pmod{12}.                 \tag{1}
\]

Suppose F is a locally free rank-two holomorphic bundle on X,
slope-polystable at Omega, with cohomological Chern data

\[
c_1(F)=0,\qquad
\operatorname{ch}_2(F)=-6e_1+(b+4)e_2-\tau_D.            \tag{2}
\]

Initial higher characters and the initial K-class are unrestricted.
No existence, presentation, gluing or transverse transport of F is
assumed. In particular, a topological SU(2) realization is not an
assumption of a compatible connection or a holomorphic bundle.

## Conclusion

For pi=p_2 the actual holomorphic direct image

\[
G=R^1\pi_*F
\]

is locally free of rank two, commutes with base change, and is
slope-polystable of slope zero at the identical real class h.
It carries a unitary quaternionic-instanton connection compatible
with this holomorphic structure. Moreover,

\[
R^i\pi_*F=0\quad(i\ne1),\qquad
R\pi_*F\simeq G[-1],\qquad \pi_![F]=-[G].               \tag{3}
\]

Base change here includes arbitrary algebraic base change for the
GAGA algebraization, and the usual holomorphic fibre identification.
G may be reducible; stability, a transform equivalence and stability
of the opposite-factor restrictions are not conclusions or inputs.
No transformed character is evaluated in this result.

This is a conditional REPRODUCTION/specialization of the assessed
preservation and base-change theorems to the changed sign. L056's
positive-sign assertion is a comparison, not an application to (2).
The result could support a later necessary surface-character test,
but constructs neither F nor a cycle and resolves no transport or
universal primitive-Hodge algebraicity gap. The separate critical audit
of 2026-10-08 below preserves this conditional specialization.

## Proof

**Use the changed-sign connection input.** Conditions (1)--(2) are
precisely the a=-10 slice of L071's conditional holomorphic input.
Its proof establishes stability of the product F before applying
the connection criterion: a nonstable polystable rank-two F would
split into two lines with opposite first Chern classes. Their mixed
second character lies in divisor tensor divisor and acts trivially
on the holomorphic two-form sigma, whereas (2) has mixed action
-2lambda sigma, which is nonzero. This excludes that alternative.

L071 checks invariance of the full c_1 and c_2 under the simultaneous
quaternionic rotations at this product metric. In particular -D
commutes with those rotations just as D does; a negative scalar on
the positive three-plane does not spoil invariance. The pure point
classes are invariant for every b. L071 then imports Verbitsky,
*Hyperholomorphic connections on coherent sheaves and stability*,
[arXiv:math/0107182v10, Theorem 3.9, pp. 13--14](https://arxiv.org/pdf/math/0107182v10#page=13).
The resulting unitary hyperholomorphic connection on the actual
stable F induces its given holomorphic structure and has curvature
of type (1,1) for every induced product complex structure. Thus it
is the hermitian quaternionic-instanton kernel required below.
No topological-existence conclusion is used in this passage.

**Verify odd IT at every fibre.** For every closed y in S set
E_y=F|_(S x {y}). L071's actual curvature-restriction argument gives
slope-polystability at h on every such fibre: the factor embedding
is quaternionic-equivariant, so restricted curvature is invariant
as an endomorphism-valued surface two-form and has zero contraction.
This is not an appeal to ordinary stability under restriction.
The restrictions are locally free of rank two with c_1(E_y)=0 and
c_2(E_y)=6; both e_2 and the mixed class pull back to zero.

At the identical h, L071's split alternative has charge 14r^2 for
an integer r. Since 6 is not such a value, every E_y is stable.
Use its surface-cohomology argument, based on slope stability and
dual stability (Huybrechts, *Lectures on K3 Surfaces*, author-hosted
draft, [Chapter 9, Section 3.1, pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175))
and K3 Riemann--Roch and Serre duality ([Chapter 1, (2.5)--(2.6)
and Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11)).
A nonzero section would give a rank-one subsheaf O_S of slope zero
in E_y, contradicting strict slope stability. Hence H^0(E_y)=0.
The dual is also stable of slope zero, so H^0(E_y^*)=0; K_S=O_S
and Serre duality give H^2(E_y)=0. Surface Riemann--Roch gives

\[
\chi(S,E_y)=2\operatorname{rk}(E_y)
               +\tfrac12c_1(E_y)^2-c_2(E_y)=4-6=-2.
\]

Consequently at every closed y,

\[
H^0(S,E_y)=H^2(S,E_y)=0,\qquad h^1(S,E_y)=2.            \tag{4}
\]

All cohomology above degree two vanishes on a surface. This proves
odd IT on every complex fibre, for every b in (1), without any
assumption of stability on the opposite fibres.

**Obtain the actual rank-two locally free sheaf and base change.**
By Serre's GAGA theorem, F algebraizes on the projective X, with
the same analytic fibre cohomology. The algebraic projection pi
is smooth projective of finite presentation and is flat. The
complex F[0] is bounded with finitely presented coherent terms, flat
over S, with support proper over S; O_X is a perfect complex. Apply
[Stacks Lemma 36.30.1, Tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
with perfect object O_X and base-flat complex F[0]: K=Rpi_*F is
perfect and compatible with arbitrary derived
base change. Its derived fibre at each closed y is R Gamma(S,E_y).
Equation (4) makes this a two-dimensional vector space in degree
one and zero in every other degree.

Apply [Stacks Lemma 36.31.3, Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH)
with degree i=1 and rank r=2. The open locus where K is a locally
free sheaf of rank two placed in degree one contains every closed
point. Its complement is closed and must be empty: every nonempty
closed subset of a finite-type complex variety contains a closed
point. Therefore G=H^1(K)=R^1pi_*F is locally free of rank two and
K is canonically isomorphic to G[-1]. All other cohomology sheaves
vanish. This proves the direct-image and concentration assertions
in (3), including the negative alternating K-class.

For any algebraic base change f:T->S, with pulled-back projection
pi_T and pulled-back bundle F_T, smoothness of pi and local freeness
of F identify the derived pullback on X with F_T. The derived
base-change isomorphism gives

\[
R(\pi_T)_*F_T\simeq Lf^*K
                   \simeq f^*G[-1],                   \tag{5}
\]

where the last equality uses local freeness of G. Taking degree-one
cohomology proves ordinary base change for G, not only a virtual
index formula. Proper direct-image comparison in GAGA identifies
the analytification of G with the actual holomorphic R^1pi_*F.
In particular its holomorphic fibre is H^1(S,E_y).

**Import the compatible transform for this actual kernel.** Use
Bartocci--Bruzzo--Hernandez Ruiperez, *A hyperkahler Fourier
transform*, Differential Geometry and its Applications **8** (1998),
239--249, [Definition 2, p. 244, and Theorem 3, p. 246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6).
For a hermitian quaternionic-instanton kernel P on X_source x Y
and a quaternionic instanton E on compact hyperkähler X_source
satisfying IT relative to P, the theorem identifies the sum of
the higher holomorphic direct images of p_X^*E tensor P with the
holomorphic sheaf of a quaternionic instanton on Y. Definition 2's
odd IT is vanishing of every even cohomology group on every fibre.
Sections 3.1--3.3 and Lemmas 1--2, pp. 243--246, establish the
connection's compatibility with the actual holomorphic restrictions
and higher direct images. Import this theorem and its identification;
no twistor reproof or new preservation theorem is needed.

Set X_source=Y=S with the fixed identical metric and its compatible
sphere of complex structures. Use P=F with the unitary connection
from L071, and E=O_S with its flat hermitian connection. The source
S is compact. The flat source line is a quaternionic instanton and
its product with P has restriction E_y. The connection on P is
quaternionic for the simultaneous rotations on this very product.
Equation (4) verifies the required odd IT. By (3), the sum of
higher direct images in the theorem is precisely the positive
holomorphic bundle G, with no other summands. The theorem therefore
supplies a unitary quaternionic-instanton connection inducing this
G's actual holomorphic structure.

No positivity condition on the mixed Chern operator occurs in this
theorem; its connection hypotheses have been verified for -tau_D
through L071. The alternating class -[G] is separate from the
holomorphic bundle G and does not negate its connection or metric.
No moduli kernel, transform equivalence or irreducibility is required.
Bartocci--Jardim, *Hyperkahler Nahm transforms*,
[arXiv:math/0312045v1, Theorem 2 and Theorem-Definition 3 with its
following remark, pp. 4--5](https://arxiv.org/pdf/math/0312045v1#page=4),
corroborates compatible hermitian preservation and permits reducible
transforms. The published theorem is the input, so the latter
preprint's printed target typo is not used.

**Conclude slope-zero polystability at the unchanged h.** The
connection just obtained has quaternionic-invariant curvature on
the target K3. Verbitsky, the same cited work,
[Proposition 3.7 and Lemma 3.8, pp. 12--13](https://arxiv.org/pdf/math/0107182v10#page=12),
give zero Kähler contraction of invariant surface two-forms.
Apply this coefficientwise to its endomorphism-valued curvature:

\[
i\Lambda_h R_{\nabla_G}=0.                             \tag{6}
\]

Thus the unitary connection compatible with G is Hermite--Einstein
with constant zero. Tracing (6), Chern--Weil and the surface identity
alpha wedge h=(Lambda_h alpha)h^2/2 give degree_h(G)=0. The
Hermite--Einstein/polystability correspondence at this real Kähler
class (Huybrechts, [Chapter 9, Section 3.1 and Theorem 4.9,
pp. 175--176 and 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182))
makes G slope-polystable of slope zero at the identical h, allowing
a reducible connection. No rational approximation of h is made.

All required applicability tests succeed: every-fibre concentration,
actual base change and local freeness, compatible holomorphic
preservation, and zero contraction at the same metric. This is the
known theorem's specialization only. F existence, global gluing,
transverse transport, other representatives and universal primitive
rational Hodge-class algebraicity remain unresolved.

**Separate critical audit, 2026-10-08.** No substantive error or stronger
conclusion was found. The audit is REPRODUCTION of the approved inputs,
with an EXPLORATION outcome rather than a new mathematical advance.

The full negative mixed class first excludes product line splitting:
its action on sigma is nonzero, whereas any two-line product splitting
has divisor-only mixed action. Thus the stable hypothesis of the
imported connection criterion is established. The audited L071 passage
uses the actual compatible connection, not a connection on a different
bundle with the same character. Its pullback to every first-factor
fibre is quaternionic-invariant. The identical metric is essential:
L071's inherited zero-slope line lattice has split charges 14r^2,
which cannot equal six. Local freeness persists under pullback. Hence
all fibres, not merely generic fibres, are stable with c_1=0, c_2=6.
A nonzero section is an injection O_S into the locally free stable
bundle on integral S and violates strict slope stability; dual stability
removes H^2. RR therefore gives exactly (h^0,h^1,h^2)=(0,2,0).
There is no hidden dependence on b or an opposite-fibre assumption.

For 0A1H the assignments are f=pi, perfect object O_X and bounded
base-flat complex F[0], supported properly over S. Smoothness makes
pi flat, so the resulting base-change square is Tor independent;
local freeness of F and G identifies derived pullbacks with ordinary
pullbacks in (5). The rank-two degree-one locus of 0BDH contains
all closed complex points. Its closed complement in finite-type S
would contain a closed point if nonempty, so it is empty. The
canonical truncation is G[-1], and its K-class is negative. These
checks independently establish the actual bundle before preservation
is invoked; no higher-dimensional parity-only rank assertion is used.

The published theorem's precise setup in Sections 3.1--3.3 was checked:
the source is compact, the two spheres of complex structures are
identified, the kernel is a hermitian quaternionic instanton and the
source flat line satisfies odd IT. Definition 2 fixes one induced
complex structure and requires vanishing for every parameter y.
Thus (4) verifies exactly its condition. Section 3.3 imports rotation
independence of this IT condition; Lemmas 1--2 identify the resulting
higher images with their actual holomorphic restrictions. Those are
parts of the cited theorem, not extra generic-fibre or moduli-kernel
hypotheses. Its hermitian connection construction and Theorem 3
identify the positive bundle G. The index sign does not reverse a
metric or replace G by a virtual negative bundle. No positivity of
the mixed operator, equivalence, or irreducibility of G is required.

Finally, on the target surface each curvature coefficient is an
invariant two-form, so its contraction with h vanishes. This gives
zero Einstein constant and degree zero at the original real class.
The compatible unitary connection therefore proves polystability,
including reducible G. The audit supplies neither a new construction
of F nor a stronger filter, inverse, gluing or transport assertion.

## Mathlib

The full preservation theorem and this complete changed-sign
specialization: **not checked**. No matching Mathlib declaration or
absence is asserted. The precise published preservation theorem,
Stacks perfect-base-change and concentration lemmas, GAGA, and the
real-metric Hermite--Einstein inputs above are imported. L071
supplies the changed-sign connection and exact-metric factor test.
This is local progress by REPRODUCTION under the prior SPECIALIZE
assessment, without an originality or complete-solution claim.
