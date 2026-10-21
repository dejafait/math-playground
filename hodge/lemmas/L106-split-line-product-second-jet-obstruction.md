# L106 — Product curvature excludes the prescribed split-line second jet

## Hypotheses

Retain L094/L101/L105's marked projective K3 surface S, hyperkähler
metric g with ordered parallel triple I,J,K, real Kähler class h,
line bundle L, and E=L direct sum L^{-1}. Its fixed determinant-one
unitary connection A is the direct-sum Hermite–Einstein connection;
c_1(L)=k, k^2=-14 and k.h=0. Write d=bar-partial_A, and identify
H=H^1(S,End_0 E) with the fixed Dolbeault-harmonic forms. As in L094,
H=H_+ direct sum H_-, with H_+=H^1(L^2), H_-=H^1(L^{-2}),
and H^1(O_S)=0. Use the actual first jet

\[
 \ell(s,t)=s(a_1+c_2)+t(-a_2+c_1),
 \qquad a_i=B(e_i),\quad c_i=B(Je_i),\quad B(w)=w^{0,1}.
 \tag{1}
\]

Each pair a_1,a_2 and c_1,c_2 is complex-linearly independent, in H_+
and H_- respectively. The ordered real tangent identification is the
one in L101, including its normalization. Choose any of L105's allowed
u: u belongs to H_+, [u,c_1]=[u,c_2]=0, and
u is not in span_C(a_1,a_2).

The proposed realization is a smooth determinant-one unitary connection
on the pullback smooth bundle E over S times a hyperkähler surface germ
(B,0). Its restriction at zero is A. The triples on S and B are ordered
and identified at the tangent level as in (1). The entire curvature R
is required to satisfy R(QX,QY)=R(X,Y) for Q=I,J,K, acting simultaneously
on both factors. The source metric can be any such hyperkähler germ;
it is not required to be flat. In I-holomorphic source coordinates s,t,
the induced family is to have fixed-central complex harmonic slice jet

\[
 \alpha(s,t)=\ell(s,t)+s^2u+O((s,t)^3).             \tag{2}
\]

Here the slice is L101's actual slice of integrable fibre Dolbeault
operators, a(alpha)=alpha+d^*beta(alpha), with harmonic projection
alpha. Smooth determinant-one complex gauges and horizontal connection
coefficients are allowed. The identification is one of actual smooth
families with the central marking, not merely pointwise equality of
coarse classes. We also allow a constant central parallel determinant-one
automorphism in that marking. No smooth HE gauge for L105's family is
assumed in advance: the hypothetical product connection supplies its
own smooth unitary representatives.

## Conclusion

No such product connection realizes (2), for any allowed u or choice
of higher coefficients, horizontal terms, source metric or permitted
smooth marked gauges. The necessary second harmonic derivative has
zero image in

\[
 H/N,\qquad N=\operatorname{span}_{\mathbb C}(a_1,a_2,c_1,c_2),
 \tag{3}
\]

whereas (2) has second derivative 2u with nonzero image there.

This is a NEGATIVE / REPRODUCTION specialization of the assessed
curvature and slice tools. The separate critical audit below preserves
its scoped exclusion. It stops
this prescribed second-jet recipe only. L094's compatible first tangent
and L105's actual degree-one complex family remain valid. It neither
excludes other second jets nor constructs a product germ, global kernel,
prescribed mixed action, cycle or transport. Universal primitive rational
Hodge realization remains unresolved; no originality claim is made.

## Proof

**Imported inputs and scope.** Reuse Yang Li, *Mukai duality on K3
surfaces from the differential geometric perspective*,
[1908.05017v1](https://arxiv.org/pdf/1908.05017v1), Sections 2.2–2.3,
Proposition 2.13 and Section 3.2, Lemmas 3.5–3.6, PDF pp. 5–8,11–13,
for the product-curvature and quaternionic harmonic-variation framework.
Reuse Buchdahl–Schumacher, *Polystable bundles and representations of
their automorphisms*, Complex Manifolds 9 (2022), 78–113,
[Lemma 2.5 and Proposition 2.6, pp. 83–84](https://d-nb.info/1262812674/34),
for the actual fixed-central complex slice, with its gauge variable in
the complement of ker d. The compact Kähler surface and central split
HE connection satisfy its hypotheses; take Sobolev exponent p>4.
The implicit-function gauge depends smoothly on smooth inputs even
when ker d is nonzero. The determinant restriction and harmonic slice
formula are those checked in L101.

These inputs are reused under the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-split-line-second-jet-hyperholomorphic-compatibility.md`.
No irreducible universal-connection construction, smooth coarse moduli
space, exact quaternionic normal form, formality comparison or geodesy
theorem is imported. L095's local coefficient argument applies, but
its global Chern-class/norm formula does not. The calculation below is
needed because those sources do not decide this marked second jet.

**The complete curvature system and the local harmonic input.** In a
smooth unitary product trivialization write the vertical connection A_y,
horizontal coefficients H_i, mixed forms r_i=R(partial_i,-), and pure
horizontal curvature F_ij. For real source coordinates x^i,

\[
 r_i=\partial_i A_y-d_{A_y}H_i,\qquad
 F_{ij}=\partial_iH_j-\partial_jH_i+[H_i,H_j].       \tag{4}
\]

The simultaneous type equations say: the pure vertical curvature F_S
is ASD on S; the pure horizontal curvature F_B is ASD on B (pointwise
on S); and r(QY)=Q_c r(Y), where Q_c a=-a composed with Q on fibre
one-forms. The Bianchi blocks are the vertical identity d_A F_S=0,
the identity D_X F_S=d_A r(X), the two-base/one-fibre identity

\[
 D_Xr(Y)-D_Yr(X)-r([X,Y])=-d_A F_B(X,Y),            \tag{5}
\]

and the cyclic purely horizontal identity for D F_B. Here D includes
the horizontal coefficient connection; tensor derivatives below also
include the source Levi-Civita connection. These formulas retain both
pure blocks and every horizontal coefficient.

At each y, differentiating F_S^+=0 and using its Bianchi block gives
d_{A_y}^+r(Y)=0. The commutator with H_X changes only coefficients, so
it also preserves ASD. To obtain d_{A_y}^*r(Y)=0 without inverting a
reducible Laplacian, use L095's local coefficient identity. In a normal
orthonormal fibre frame put C_0(a)=sum_f(nabla_f a)(f) and
C_I(a)=sum_f(nabla_f a)(If). Then
d_A^*a=-C_0(a), the omega_I contraction of d_A a is C_I(a), and
C_I(I_c a)=C_0(a). Apply the ASD equation to r(IY)=I_c r(Y).
It gives C_0(r(Y))=0. Thus r(Y) is real ASD-harmonic at every y,
including zero. This uses only the smooth hypothetical germ, vertical
ASD and mixed quaternionic type, not a global metric-scale identity.

Let V=ker d_A^* intersect ker d_A^+ at the central connection, and
let P be its real L2 orthogonal projection. L094's coefficient Kähler
comparison identifies V with H by B. It also shows that V is invariant
under each orthogonal Q_c, hence P commutes with Q_c. Projection P
kills every d_A f, by integration by parts on compact S.

**A vanishing covariant harmonic Hessian.** At zero define the real
bilinear tensor with values in V

\[
 T(X,Y)=P\{D_X(r(Y))-r(\nabla^B_XY)\}.             \tag{6}
\]

It is tensorial in both arguments. The source triple is parallel and
the fixed fibre triple commutes with coefficient covariant differentiation.
Differentiating r(QY)=Q_c r(Y) therefore yields

\[
 T(X,QY)=Q_cT(X,Y).                                \tag{7}
\]

No derivative of a varying harmonic projection is used: P is applied
at the fixed central point after differentiating. By torsion-freeness
and (5), the antisymmetric part is -P d_A F_B(X,Y)=0. Thus T is
symmetric. Symmetry and (7) also give T(QX,Y)=Q_cT(X,Y). Now evaluate
T(IX,JY) in the two orders:

\[
 T(IX,JY)=I_cJ_cT(X,Y)=K_cT(X,Y),\qquad
 T(IX,JY)=J_cI_cT(X,Y)=-K_cT(X,Y).
\]

Over the real numbers K_c is invertible, so T=0. This argument takes
place in the actual affine coefficient spaces at A, before quotienting
by its stabilizer. It remains valid at the reducible central connection.

**Keep the horizontal terms and source connection in the jet.** Choose
a smooth determinant-one unitary gauge equal to the identity over
S times {0} with H_i(0)=0 for all i. Prescribing its first derivatives
to be H_i(0) in the convention g nabla g^{-1} does this; for example
the exponential of sum_i x^i H_i(0) has exactly that jet. No condition
on F_ij(0) or on higher H coefficients is imposed. Then (4) gives
partial_i A_y|_0=r_i(0), which is harmonic. In these arbitrary real
coordinates the equation T=0 becomes

\[
 P\partial_i r_j=\Gamma_{ij}^{k}r_k,
 \qquad
 P\partial_i\partial_j A_y|_0=\Gamma_{ij}^{k}r_k.    \tag{8}
\]

For the second equality differentiate (4). At zero its discarded term
is exactly d_A(partial_i H_j); the term [partial_i A_y,H_j] vanishes
because H_j(0)=0. Projection kills the exact term. The Christoffel
symbols in (8) are those of the arbitrary source metric in the chosen
coordinates. They have not been set to zero. Thus source changes
contribute only the central tangent image r(T_0 B). Source curvature
cannot change (8), which uses only this first covariant derivative and
the parallelness of the triple.

Write b(x)=(A_y-A)^{0,1}. For all real skew-adjoint one-forms the map
B to (0,1)-forms is a real linear isomorphism and multiplies the real
L2 inner product by a constant factor: the two conjugate form types
have equal norm and are orthogonal. Since B(V)=H, it intertwines P
with the Dolbeault harmonic projection Pi, viewed as a real projection.
Consequently b_i is harmonic and

\[
 \Pi b_{ij}=\Gamma_{ij}^{k}b_k.                    \tag{9}
\]

This establishes the needed projection statement for arbitrary second
vertical coefficients, not only for linearized ASD solutions.

**Actual marked complex gauges cannot remove the normal coefficient.**
First take the central marking to be the identity. Let a'(x) be the
actual complex slice coefficient and let a smooth determinant-one
complex gauge g(x), g(0)=1, identify d+b(x) with d+a'(x). Such gauges
are precisely the allowed family comparisons; the fixed-central slice
theorem supplies smooth slice fixing for an induced smooth family.
It is not enough to know only equality of individual coarse classes.
Use a local logarithm

\[
 \phi(x)=\log g(x)=x^i\phi_i+\tfrac12x^ix^j\phi_{ij}+O(|x|^3).
\]

All coefficients are trace-free. The gauge convention gives

\[
 a'_i=b_i-d\phi_i.
\]

The slice correction d^*beta has no linear term, so a'_i=ell_i is
harmonic. Projection gives b_i=ell_i, since b_i is harmonic and Pi
kills d phi_i. Hence d phi_i=0. The actual central holomorphic
trace-free endomorphisms are precisely the parallel constant diagonal
ones, phi_i=z_i D with D=diag(1,-1). This follows from the vanishing
of H^0(L^{+/-2}) and H^0(O_S)=C, already checked in L094.

Expanding g(d+b)g^{-1} through degree two now gives

\[
 a'_{ij}=b_{ij}+[\phi_i,b_j]+[\phi_j,b_i]-d\phi_{ij}. \tag{10}
\]

Indeed the other possible second-order terms are
-([phi_i,d phi_j]+[phi_j,d phi_i])/2, and both vanish. This expansion
keeps arbitrary smooth, including antiholomorphic, parameter dependence
of g. Harmonic projection and (9) therefore give

\[
 \partial_i\partial_j\alpha(0)
 =\Gamma_{ij}^{k}\ell_k+[\phi_i,\ell_j]+[\phi_j,\ell_i]. \tag{11}
\]

Here Pi a'=alpha exactly; coexact slice corrections have not been
identified with zero as forms. Parallel diagonal commutators preserve
harmonic representatives and multiply the two sectors by +2 and -2.
The complex span of ell's real first derivatives is
span_C(a_1+c_2,-a_2+c_1). Its span together with its D-commutators
is exactly N in (3). Every right side of (11) therefore lies in N.

Allowing a nonidentity central parallel complex gauge does not change
this conclusion. Factor it as the constant g_0 followed by a gauge
equal to one at zero. On the Dolbeault coefficient blocks Ad(g_0)
is constant scalar multiplication, so it commutes with d and Pi.
Apply Ad(g_0) to b only after deriving (9) from the unitary product
connection. The transformed first coefficients are again harmonic and
must equal ell_i; (9) still holds. The identical expansion (10)–(11)
applies. This does not conjugate the full unitary curvature by a
nonunitary gauge or assume that such a conjugation preserves its type
equations. Unitary residual marking changes are included as well.

Finally take i=j to be the real coordinate Re s in the prescribed
I-holomorphic chart. Equation (2) implies partial_i^2 alpha(0)=2u.
Since u is in H_+ and outside span_C(a_1,a_2), whereas
N intersect H_+=span_C(a_1,a_2), its image in H/N is nonzero. This
contradicts (11). The argument works for every allowed u; the extra
annihilator conditions ensure L105's complex realization but are not
needed for this obstruction.

All equations used are necessary consequences of the full product
system. The unused pure-horizontal ASD and horizontal Bianchi equations
cannot repair the contradiction: (5) retained their entire curvature
F_B and killed its contribution by an exact projection identity, not
by setting that curvature to zero. No second-order solution or
integration theorem is inferred. Other jets and every global obligation
remain outside this test.

**Independent critical audit, 2026-10-15 (step 290).** The prior
SPECIALIZE assessment
`drafts/literature/2026-10-15-split-line-second-jet-obstruction-critical-audit.md`
covers this audit. Its primary-source comparison is reused, including
the nonzero central kernel in Buchdahl–Schumacher's Lemma 2.5 and
Proposition 2.6. This audit checks the specialized calculation, rather
than importing its conclusion from those sources. No substantive error,
stronger exclusion or existence conclusion was found.

First, the signs and projections can be checked without discarding
either pure curvature block. In the gauge H_i(0)=0, direct
differentiation of (4) gives

\[
 (\partial_i r_j)_0=(\partial_i\partial_j A_y)_0
                     -d_A(\partial_i H_j)_0.
\]

Antisymmetrizing gives -d_A F_ij at zero. With H nonzero, expanding
D_i=partial_i+[H_i,-] restores exactly the covariant identity (5).
The source torsion term is r([X,Y]); subtracting its Levi–Civita
derivative makes (6) bilinear over functions in both X and Y.
Integration by parts gives P d_A f=0 for every smooth skew-adjoint
trace-free f, including the actual F_B(X,Y). Thus symmetry uses the
whole horizontal curvature, not its vanishing or a choice of flat
horizontal connection. The local harmonicity proof uses only ASD and
the coefficient contractions displayed above; L095's global norm
formula is unnecessary.

Each Q_c is orthogonal and preserves V by L094's four contraction
identities. It therefore preserves V's orthogonal complement, proving
P Q_c=Q_c P on *all* real coefficient one-forms. Also
D_X(Q_c r)=Q_c D_X r because the fibre triple is fixed and parallel;
the source identity nabla Q=0 handles the source slot. These statements
justify (7) before symmetry is used. In particular, the two evaluations
of T(IX,JY) use opposite orders of I_c and J_c. Their anticommutation
forces T=0. No differentiation of a family of kernels or projections,
irreducible inverse, or smooth quotient is involved.

Second, the real/Dolbeault projection bridge holds on arbitrary second
coefficients. For arbitrary real skew-adjoint a,b, with B(a)=a^{0,1},
the type decomposition and adjoint reality give

\[
 (a,b)_{\mathbb R}=2\operatorname{Re}
          \langle B(a),B(b)\rangle_{L^2}.
\]

The same identity holds on the Sobolev completions. B is an onto
real-linear scaled isometry with inverse b mapped to b-b^*, and
B(V)=H by L094's coefficient Kähler identities. The real orthogonal
projection onto the complex subspace H equals its complex Hermitian
projection: orthogonality to h and ih gives both real and imaginary
parts. Consequently B P=Pi B on the entire space, including coefficients
not satisfying any linearized ASD equation. This proves the use of
(9) at second order. Differentiating (4) leaves the exact term written
above; [partial_i A_y,H_j] vanishes only at the centre, as required.
The remaining Christoffel term is r(nabla_i partial_j), so an arbitrary
source metric or nonlinear source chart contributes only the first
tangent image, without any flat-source assumption.

Third, for an arbitrary smooth family comparison, differentiate in all
four *real* source directions. Since the slice correction has zero
linear term, both a'_i and b_i are harmonic. The first gauge identity
therefore implies d phi_i=0, not merely Pi d phi_i=0. L094's
H^0(L^{+/-2})=0 identifies phi_i=z_i D with a parallel diagonal
endomorphism. Expanding the gauge action directly gives

\[
 a'=b-d\phi+[\phi,b]-\tfrac12[\phi,d\phi]+O(|x|^3).
\]

Here the last displayed commutator has zero quadratic coefficient
because d phi_i=0. Differentiating twice leaves exactly (10). The
unrestricted second coefficient phi_ij contributes only -d phi_ij,
which Pi kills. This real Taylor expansion includes antiholomorphic
source dependence; holomorphic gauge dependence was never imposed.
Parallel diagonal commutators act by the two weights and preserve
harmonic representatives.

For completeness, if g(0)=g_0 is nonunitary, write g=h g_0 with h(0)=1
and put tilde b=Ad(g_0)b. The central g_0 is a constant diagonal
parallel determinant-one automorphism by the same H^0 calculation.
Its adjoint action is scalar on each of the three parallel coefficient
blocks, so it commutes with d,d* and Pi even though it need not be an
isometry. Apply it to (9) only after that equation has been proved for
the unitary connection. Then tilde b_i is harmonic and the same first
gauge identity forces tilde b_i=ell_i. The expansion for h consequently
gives (11) unchanged. This argument transports Dolbeault identities;
it makes no claim about nonunitary conjugation of real curvature.

Finally the real first derivatives of ell are b_1,ib_1,b_2,ib_2,
where b_1=a_1+c_2 and b_2=-a_2+c_1. Combining b_1 with [D,b_1]
recovers a_1,c_2, and combining b_2 with [D,b_2] recovers a_2,c_1.
Thus their complex span together with all permitted first-gauge
commutators is exactly N. Every source and gauge term in (11) lies
there. Along the real Re s axis, the specified jet has derivative 2u;
all terms of order at least three have zero second derivative. The
direct weight decomposition gives N intersect H_+=span(a_1,a_2), so
every allowed u has nonzero quotient class. This independently verifies
the contradiction for the entire stated range of u and higher terms.
The annihilator conditions on u are inputs for complex realization,
not additional unproved assumptions needed in the obstruction.

The audit outcome is EXPLORATION / REPRODUCTION: it confirms the existing
scoped negative result without a new mathematical advance. Compatible
first tangents, other second jets, arbitrary source germs without this
jet, and all global kernel and Hodge-realization gaps remain open.

## Mathlib

Full matching coverage for this product-connection second-jet obstruction,
the reducible harmonic/gauge comparison and the cited analytic slice:
**not checked**. Unknown availability is not absence. The proof is an
exact tensor and gauge computation using the cited analytic inputs;
no numerical certificate or Lean verification is claimed.
