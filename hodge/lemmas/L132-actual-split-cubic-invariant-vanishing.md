# L132 — No invariant of source order three at an actual split fibre

## Hypotheses

Retain L071's identical marked projective K3 factors, ordered
hyperkähler structures I,J,K and metric g. Suppose the locally free
Omega-polystable rank-two bundle F exists with integral c_1(F)=0 and
ch_2(F)=-14e_1-21e_2-tau_D. Use its actual compatible determinant-one
unitary connection. Select a split parameter 0 in B=S_2, if one exists,
with fibre E=L direct sum L^{-1}, c_1(L)=k, k^2=-14 and k.h=0.
The restricted connection is the split HE connection A of L094.

Put d=bar-partial_A and H=H^1(S_1,End_0 E), represented by the fixed
central harmonic forms. Thus H=H_+ direct sum H_-, with no weight-zero
sector, and the full effective automorphism action is
z(p,q)=(zp,z^{-1}q). Let alpha:(B,0) -> (H,0) be a holomorphic
base change of the actual marked family into the fixed harmonic slice
a(alpha)=alpha+d^*beta(alpha), with beta=O(alpha^2). Retain the actual
family isomorphism, not just equality of pointwise coarse classes.
Allow all smooth determinant-one comparison gauges, including a
constant parallel complex central marking. Let m be the maximal ideal
of the smooth complex surface germ (B,0).

## Conclusion

For every full-stabilizer invariant polynomial f on H with f(0)=0,

\[
                 f\circ\alpha\in\mathfrak m^3
          \quad\Longrightarrow\quad
                 f\circ\alpha\in\mathfrak m^4.                 \tag{1}
\]

In particular no such polynomial pulls back with zero terms through
degree two and a nonzero cubic term. This holds for the actual first
plane, without identifying it with L094's example or prescribing any
second jet. The source Christoffel terms and marked-gauge terms are
retained explicitly below.

This conditional ADVANCE / REPRODUCTION specializes the assessed
curvature and slice tools; it is not a certified original result.
The separate critical audit below preserves the conclusion. It eliminates only this cubic
mechanism. It proves no all-orders parity, parameter involution, local
degree two, actual coarse-image identification or nonempty split locus.
F existence, separation, reconstruction, transport and universal
primitive rational Hodge realization remain unresolved.

## Proof

**Imported slice and actual comparison.** Reuse Buchdahl–Schumacher,
*Polystable bundles and representations of their automorphisms*,
Complex Manifolds 9 (2022), 78–113, DOI 10.1515/coma-2021-0131,
[Theorem 1 and introduction, pp. 78–79; Lemma 2.5, p. 83;
Proposition 2.6 and Remarks 1–3, p. 84](https://d-nb.info/1262812674/34).
These are the semiversal base-change and fixed harmonic slice inputs
inspected in the prior SPECIALIZE assessment
`drafts/literature/2026-10-19-equality-split-actual-local-degree.md`.
S_1 is compact Kähler and E is polystable for its actual real metric;
take Sobolev exponent p>4. The gauge inverse is on the complement of
ker d; reducibility is allowed. The trace-free restriction is valid
because d, d*, the harmonic projections and Green operators preserve
the scalar/trace-free splitting, and the trace of the square of an
endomorphism-valued one-form is zero. Uniqueness of the implicit
coexact correction retains this restriction and beta=O(alpha^2).

The actual holomorphic bundle on S_1 times a sufficiently small base
germ is a deformation of E. Semiversality supplies a holomorphic base
change together with an isomorphism of families. With the smooth
unitary trivialization furnished by the product connection, that
isomorphism is a smooth complex gauge over the entire germ, including
zero. Its determinant can be normalized to one locally: the determinant
ratio is a nowhere-zero base function (holomorphic functions on compact
S_1 are constant), and a local square root removes it. No lift through
a coarse quotient or smoothly varying HE metric is being asserted.
The conclusion applies to every such marked base change.

Reuse the curvature framework of Yang Li, *Mukai duality on K3 surfaces
from the differential geometric perspective*,
[1908.05017v1, Section 3.2, Lemmas 3.5–3.6 and following qualifications,
pp. 12–13](https://arxiv.org/pdf/1908.05017v1#page=12), through L094/L095's
audited coefficient identities. No irreducible universal connection
is used. L106's audited proof through (11) uses this framework, but
its stated hypotheses prescribe a particular plane. We therefore
justify below precisely the part whose scope changes. We do not import
its prescribed-jet contradiction as an arbitrary-plane theorem.

**The arbitrary-plane harmonic Hessian.** Work first with central
marking equal to the identity. In real source coordinates x^i, write
A_y for the vertical connection, H_i for its horizontal coefficients,
r_i=R(partial_i,-), and F_B for its pure horizontal curvature. Then

\[
 r_i=\partial_i A_y-d_{A_y}H_i,\qquad
 D_Xr(Y)-D_Yr(X)-r([X,Y])=-d_{A_y}F_B(X,Y).          \tag{2}
\]

L095 gives actual harmonicity of r(Y) and quaternionic type
r(QY)=Q_c r(Y), where Q_c a=-a composed with Q. At zero let P be
projection onto V=ker d_A^* intersect ker d_A^+. L094 gives invariance
of V under the orthogonal I_c,J_c,K_c, so P commutes with them on
all real coefficient one-forms. It kills every d_A u. Define

\[
 T(X,Y)=P\{D_Xr(Y)-r(\nabla^B_XY)\}\big|_0.        \tag{3}
\]

Torsion-freeness and (2) make T symmetric: the entire antisymmetric
term is -P d_A F_B(X,Y)=0. Parallelness of both triples gives
T(X,QY)=Q_c T(X,Y). Symmetry gives the same property in the first
slot. Evaluating T(IX,JY) in the two orders gives K_c T(X,Y) and
-K_c T(X,Y). Hence T=0. This uses the fixed projection only after
differentiation, and uses no chosen tangent vectors or moment normal
form. In particular the actual arbitrary first plane is permitted.

Choose a smooth unitary gauge equal to one centrally with H_i(0)=0;
its prescribed first derivatives accomplish this without restricting
F_B(0). Differentiating (2) and applying T=0 gives

\[
 P\partial_i\partial_j A_y|_0=\Gamma_{ij}^k r_k(0).
                                                               \tag{4}
\]

Indeed partial_i r_j=partial_i partial_j A_y-d_A(partial_i H_j)
at zero, and P kills the last term. The Gamma are the actual source
Christoffel symbols; the source metric is not assumed flat.
Let b=(A_y-A)^{0,1}, and Pi be the central Dolbeault harmonic
projection. The map B(a)=a^{0,1} is a real scaled isometry onto all
complex (0,1)-forms, with inverse b mapped to b-b^*. Since B(V)=H,
it intertwines P and Pi on arbitrary forms, including second
coefficients. Thus b_i is harmonic and

\[
                         \Pi b_{ij}=\Gamma_{ij}^k b_k.          \tag{5}
\]

**All marked-gauge terms.** Write the actual comparison gauge as
g=exp(phi), with phi=x^i phi_i+(1/2)x^i x^j phi_ij+O(|x|^3),
and let a'=a(alpha). Its first variation is a'_i=b_i-d phi_i.
Both a'_i and b_i are harmonic, because the slice correction has no
linear term. Therefore b_i=a'_i=:ell_i and d phi_i=0. L094's
H^0(L^{+/-2})=0 makes each trace-free phi_i a parallel scalar multiple
of Delta=diag(1,-1). The actual smooth gauge expansion gives

\[
 a'_{ij}=b_{ij}+[\phi_i,b_j]+[\phi_j,b_i]-d\phi_{ij}.
\]

The possible terms involving [phi_i,d phi_j] vanish because d phi_j=0.
Projecting and using Pi a'=alpha and (5) yields

\[
 \alpha_{ij}(0)=\Gamma_{ij}^k\ell_k
                     +[\phi_i,\ell_j]+[\phi_j,\ell_i].         \tag{6}
\]

These are derivatives in all four real directions; antiholomorphic
dependence of the comparison gauge is allowed. If its central value
is g_0 rather than one, g_0 is a parallel diagonal complex automorphism
by L094. Factor g=h g_0 and apply Ad(g_0) to (5). Its constant block
scalars commute with d and Pi, so (5) and then (6) hold with the
transformed ell_i as well. The unitary curvature calculation precedes
this transport of Dolbeault identities; no nonunitary conjugation of
real curvature is used.

Set ell(x)=sum x^i ell_i, C(x,x)^k=Gamma_ij^k x^i x^j, and
phi(x)=sum x^i phi_i. Equation (6) says that the homogeneous real
quadratic Taylor term alpha_2 is exactly

\[
          \alpha_2(x)=\tfrac12\ell(C(x,x))
                                  +[\phi(x),\ell(x)].          \tag{7}
\]

The ell in this formula is the actual derivative. L095 identifies it
with the injective quaternionic derivative before a constant marking;
no normalization of that plane is needed for (7) or what follows.

**Complete invariant cubic test.** L103's full-invariant generation
applies to the representation alone, independently of its chosen
family or degree calculation: invariant monomials have equal positive
and negative weights and are products p_i q_j. Thus every invariant
polynomial with zero constant term has the form f=Q+f_{>=4}, where
Q is an invariant homogeneous quadratic and f_{>=4} has ambient degree
at least four. There is no linear or cubic ambient term. Since
alpha(0)=0, f_{>=4}(alpha) belongs to m^4. The quadratic and cubic
source terms of f(alpha) are respectively

\[
                    Q(\ell(x)),\qquad
                    dQ_{\ell(x)}(\alpha_2(x)).                 \tag{8}
\]

Assume f(alpha) belongs to m^3. Then Q(ell(x))=0 identically.
Differentiating this identity in any real direction v gives
dQ_{ell(x)}(ell(v))=0 for every x,v. For each fixed x, take
v=C(x,x); the first term of (7) contributes zero. Infinitesimal
invariance of Q gives dQ_w([z Delta,w])=0 for every w in H and
every complex scalar z. Take w=ell(x) and z Delta=phi(x); the second
term of (7) also contributes zero. Consequently the entire cubic in
(8) is zero, for every quadratic invariant Q simultaneously.

This real Taylor calculation determines the holomorphic cubic as
well: a holomorphic polynomial in two complex coordinates vanishing
for all four real coordinates is the zero polynomial. Thus the
holomorphic germ f(alpha) has order at least four, proving (1).
Neither the rank of either weight projection nor a basis change to
L094's special example was required. We used the exact gauge action,
not just L106's weaker containment in four weight modes.

Only the second jet entered (8). Higher odd source terms are not
controlled; a generic degree-one map is not excluded. L099's global
normalization and L104's conditional degree-two description therefore
yield no contradiction from this finite-order result alone.

**Independent critical audit, 2026-10-19 (step 406).** The unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-19-actual-split-cubic-critical-audit.md`
covers this audit. The precise Buchdahl–Schumacher and Li inputs cited
above are reused within their inspected scope. Their slice and curvature
theorems do not themselves assert (1); the following verifies the actual
comparison and its specialized cancellation. No substantive error or
stronger conclusion was found. This audit is EXPLORATION / REPRODUCTION,
not a new mathematical advance or a claim of originality.

First, determinant normalization can be performed on the total family,
before any Taylor expansion. L095's determinant argument uses integral
c_1(F)=0 and Pic^0(S_1 times S_2)=0 to obtain a global holomorphic
determinant frame. Its HE norm is constant on the compact product, so
the frame is parallel. Choose the smooth identification of the family
with the central smooth bundle to preserve this frame. The trace-free
slice has the fixed determinant frame as well. Indeed its operators
preserve the trace splitting, H^1(O_{S_1})=0, and the trace of the
quadratic one-form term is zero; the unique small coexact correction
therefore has zero scalar component. Thus the full semiversal slice
restricts to these determinant-trivial deformations, without requiring
a separate universal fixed-determinant moduli space.

Semiversality here is a base-change assertion about deformations of E,
with an isomorphism of bundles over the whole small parameter germ.
It is not uniqueness of the base change. Smoothness of that isomorphism
in smooth bundle frames gives the smooth comparison used in (6).
The slice construction has smooth fibre coefficients by elliptic
regularity; the Sobolev condition p>4 is met. In the two holomorphic
determinant frames, the isomorphism's determinant is an invertible
holomorphic function on S_1 times the base. Compact connected S_1
makes it a base function. Shrinking the base permits a holomorphic
square root; multiplying the isomorphism by its inverse normalizes
the determinant. In the smooth unitary frames this still gives a
smooth determinant-one gauge. Its central value is a holomorphic
automorphism of E, hence parallel diagonal by H^0(L^{+/-2})=0.
No smoothly varying HE metric or lift of coarse points is needed.

Second, the tensor computation is independent of the chosen first
plane. In a gauge H_i(0)=0, direct differentiation gives
partial_i r_j=partial_i partial_j A-d_A(partial_i H_j) at zero;
the omitted commutator is [partial_i A,H_j]=0 there. The antisymmetric
part is exactly -d_A F_{ij}. Integration by parts gives P d_A u=0,
including u=F_{ij}; the horizontal block has not been assumed zero.
Subtracting r(nabla_X Y) makes (3) tensorial and symmetric. Since
Q_c preserves V and its orthogonal complement, P commutes with Q_c
on all one-forms. Differentiating the mixed-type identity and using
nabla Q=0 gives T(X,QY)=Q_c T(X,Y). Symmetry supplies the other slot;
the opposite compositions I_c J_c and J_c I_c force T=0. No varying
projection, flat source or specified tangent basis enters this argument.

For arbitrary real skew-adjoint forms a,c, the full type decomposition
gives (a,c)_R=2 Re <a^{0,1},c^{0,1}>. L094's coefficient Kähler
identities identify V with H. Orthogonality to both h and ih makes
real orthogonal projection to H equal to its Hermitian projection.
Consequently B P=Pi B holds even for second coefficients not solving
the linearized ASD equations. This verifies (5), including its source
Christoffel term; it is not merely a first-order tangent identification.

Third, directly expanding the smooth gauge in all four real directions
gives a'=b-d phi+[phi,b]-[phi,d phi]/2+O(|x|^3).
Both first derivatives are harmonic, so their difference -d phi_i
vanishes as a form, not just as a cohomology class. Thus phi_i is a
parallel multiple of Delta. The quadratic [phi,d phi] term vanishes,
and the unrestricted phi_ij contributes only the exact term killed
by Pi. This proves the precise formula (6), rather than containment
in a span. For g=h g_0, Ad(g_0) is a constant scalar on each parallel
coefficient block and commutes with d,d* and Pi. Applying it after
the unitary calculation preserves (5) and the same expansion for h.
This treats nonunitary central markings without projecting nonunitary
real curvature, and allows antiholomorphic gauge dependence throughout.

Finally, the determinant-one diagonal subgroup still surjects onto
the effective ratio C*: its character is z mapped to z^2. Hence no
additional invariants appear after fixing determinant. Equal positive
and negative monomial degrees give exactly the quadratic products and
their products, with no odd ambient homogeneous degree. Only Q can
contribute through cubic source degree. The identity Q(ell(x))=0
implies dQ_{ell(x)} ell(v)=0 for every real x,v. Substituting the
real vector v=C(x,x) is legitimate pointwise. Invariance separately
gives dQ_{ell(x)}[phi(x),ell(x)]=0 for every complex value of the
diagonal coefficient. Thus both terms of (7) vanish in (8), uniformly
for every such Q and actual first plane. All four real coordinates
range over the underlying complex surface germ, so this vanishing
is precisely vanishing of its holomorphic cubic Taylor polynomial.

The DAG is unchanged. L103 is used only for its representation,
not for its special family's first plane or degree. ATTEMPTS/061–063
remain intact. The audit controls no higher odd jet, coarse-image
comparison, split-locus nonemptiness or existence of F. The universal
primitive Hodge gap is unchanged.

## Mathlib

Full matching coverage is not checked. The application uses analytic
bundle slices, coefficient harmonic theory and finite Taylor identities;
no formalization is supplied. Unknown coverage is not evidence of absence.
