# L124 — Full real first-curvature-derivative range on three lines

## Hypotheses

Let (V,g,I,J,K) be a positive quaternionic Hermitian vector space of
quaternionic dimension n>=2. Let P_1,P_2,P_3 be distinct quaternionic
lines spanning a quaternionic two-plane W. An admissible algebraic
first curvature derivative means a real element of
V* tensor R(sp(n)) satisfying differential Bianchi, where R(sp(n))
is the space of hyperkähler algebraic curvature tensors. On each P_i
prescribe an arbitrary such source derivative for its induced metric.
Only derivative directions tangent to that branch are prescribed.
Require the differentiated full vector Gauss identity for a totally
geodesic branch, including its normal component. No normal-connection
curvature or transverse derivative is prescribed.

For application retain L118's conditional locally free rank-two
Omega-polystable F with integral c_1=0 and
ch_2=-14e_1-21e_2-tau_D on the identical marked K3 factors. Its actual
opposite map has parallel quaternionic differential and metric pullback
c g_B, c=2lambda, 1<lambda<5/4. Retain L121's distinct tangent lines
at three distinct coincident preimages (and its L120 normalization
input). Suppose their span has quaternionic dimension two in the
ambient quaternionic dimension 39. The actual source derivatives and
angles are unknown. Order-zero compatibility is separately L123's
condition; no conclusion here removes that condition.

## Conclusion

For every positive metric and every such triple of lines, the real
first-derivative restriction range is the entire 36-dimensional space
of admissible prescribed source triples: twelve real components on
each quaternionic line. All differentiated normal equations can be
satisfied simultaneously. On W the space satisfying these homogeneous
normal equations has real dimension 52; the extensions of any prescribed
triple form a real affine space of dimension 16. Orthogonal compression
and extension prove the same restriction range on V. There are no angle
exceptions, including L123's two exceptional cases.

If a_i=a,b,t are L123's squared coordinate-frame scales, the coordinate
source five-tensors are a_i^(5/2) k_i/c^(3/2), where k_i are the original
K3 derivatives in matched unit quaternionic frames. These are prescribed
unknowns, not values assigned to the actual K3.

This is a NEGATIVE / REPRODUCTION specialization of the assessed
framework: it parks the finite order-one restriction mechanism because
it supplies no additional restriction on admissible source derivatives,
even when the order-zero values are fixed and compatible. It is not
metric-jet realization, branch integration, collision existence, F
existence, an algebraic cycle or Hodge realization. The separate critical
audit below preserves this conclusion; no originality is claimed.

## Proof

**Coverage and imported identities.** Reuse the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-18-three-line-curvature-first-derivative.md`
and its exact covered calculation target. Import Rozansky--Witten,
*Hyper-Kähler Geometry and Invariants of Three-Manifolds*,
[hep-th/9612216v1, Section 2.1, equation (2.4), and Section 2.2,
equation (2.5), PDF pp. 9–11](https://arxiv.org/pdf/hep-th/9612216v1#page=11).
Their equation D_AI Omega_JKLM=D_AJ Omega_IKLM, together with the
four-slot symmetry of Omega, gives symmetry in all five E indices.
This is a local identity and includes quaternionic dimension one.
The real kernel being specialized is precisely R^nabla(h) in Galaev,
*Covariant derivative of the curvature tensor of pseudo-Kählerian
manifolds*, Ann. Global Anal. Geom. 51 (2017), 245–265,
[1010.0861v2, Sections 2–3, PDF pp. 4–6](https://arxiv.org/pdf/1010.0861v2#page=5).
Its definition applies to h=sp(n) without requiring full actual holonomy.
No highest-weight dimension formula or omitted classification proof is used.

Retain the positive quaternionic reality and curvature formula imported
in L123 from Semmelmann--Weingart, *Vanishing Theorems for Quaternionic
Kaehler Manifolds*, [math/0001061v1, Section 2, Lemma 2.3,
equations (13)–(15)](https://arxiv.org/pdf/math/0001061v1#page=5).
For V_C=H tensor E, write a derivative coefficient as

    T in H* tensor Sym^5 E*.

The lowered five-tensor on decomposable arguments, with the derivative
slot written first, is, in the common curvature convention,

    K(h0 e0; h1 e1,h2 e2,h3 e3,h4 e4)
      =epsilon(h1,h2) epsilon(h3,h4) T(h0;e0,e1,e2,e3,e4).    (1)

Tensor signs/scalars from the chosen curvature convention are identical
on ambient and source. The imported identity proves necessity of the
fivefold E symmetry. To check sufficiency for the actual real kernel,
the curvature symmetries hold for each fixed derivative argument by
the imported quartic formula. The cyclic differential Bianchi sum in
slots 0,1,2 vanishes by

    epsilon(h1,h2) ell(h0)+epsilon(h2,h0) ell(h1)
       +epsilon(h0,h1) ell(h2)=0

for every ell in H*, since dim_C H=2; the E coefficients are symmetric.
Thus (1) identifies exactly the complexified kernel, not a larger space
of independent quartic derivatives. It is injective by choosing nonzero
epsilon pairings. The induced antilinear operation applies quaternionic
conjugation to the one H slot and all five E slots. Its square is
(-1)^6=1. Its fixed tensors are exactly the real five-tensors in (1).
On a single line the complex dimension is 2 dim Sym^5(C^2)*=12,
so the fixed real dimension is twelve. An individual odd quintic has
quaternionic square minus one and is not by itself a real source tensor.

**Differentiate the full identity.** Import the named Gauss and Weingarten
formulas and combined Gauss-Codazzi identity in Chen, *Riemannian
Submanifolds*, [Section 3.1, equations (3.1)–(3.7), PDF
pp. 14–15](https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Chen_Riemann_Submanifolds.pdf#page=14).
For each actual branch L118 gives second fundamental form identically
zero and parallel df. Along the branch, the ambient connection preserves
both tangent and normal bundles and induces the source connection.
Differentiate R^M(df X,df Y)df Z=df(R^B(X,Y)Z) in a tangent direction
df v, subtracting all argument-connection terms on both sides. Parallel
df cancels those terms, and there is no derivative of a nonzero second
fundamental form. The resulting vector identity is

    (nabla^M_(df v) R^M)(df X,df Y)df Z
       =df((nabla^B_v R^B)(X,Y)Z).                        (2)

Here B carries c g_B. Lowering the output gives intrinsic matching and
zero whenever the final argument is normal. A normal field remains
normal under tangent differentiation, so this step retains its connection
term as well. Curvature skew-adjointness also gives preservation of the
normal space; there is no extra prescribed action on that space.

Let L_i subset E correspond to P_i. By (1), the full zero-normal part
of (2) is exactly

    T(H;L_i,L_i,L_i,L_i,L_i-perp)=0.                      (3)

The four tangent E arguments can be polarized from their diagonal
values; the H arguments are independent and both epsilon factors can
be nonzero. Thus neither differential Bianchi nor any normal component
is lost by the polynomial formulation below. No equation for a derivative
direction transverse to P_i is obtained by differentiating along P_i.

**Ambient reduction.** Orthogonally split E=E_W direct-sum E_U. Restrict
all five E arguments to E_W, leaving H unchanged. Symmetry, reality and
the Bianchi identity above survive, and (3) implies all normals inside
W. Conversely extend a solution on E_W by orthogonal projection in each
E argument. This projection commutes with the quaternionic structures.
The extension has zero value if any argument is in E_U, hence satisfies
every exterior normal equation as well as (3) inside W. Its restrictions
are unchanged. This proves equality of the full ambient and W ranges,
without assuming actual curvature or its derivative preserves W.

**Uniform quintic interpolation.** Use exactly L123's graph coordinates
P_1=(x,0), P_2=(0,x), P_3=(x,x), retaining the positive metric
[[a,Q],[Q*,b]], a,b>0, ab>|Q|^2. Set

    t=a+b+2 Re(Q), C=Q/a, D=Q*/b,
    H_0=(a Id+Q*)/t.

The three normal spaces are parametrized by (-Cv,v), (u,-Du), and
((Id-H_0)u,-H_0 u). All these are quaternionic maps; the positive metric
ensures t>0. The symbol H_0 here is a projection coefficient, distinct
from the two-dimensional tensor factor H.

Fix one component of H* temporarily and write its symmetric coefficient
as a degree-five polynomial F(x,y), with x,y in C^2. Prescribe its
three restrictions as binary quintics A,B,T_3. The first two full
normal equations fix exactly the (4,1) and (1,4) terms, so every solution
on those axes is uniquely

    F=A(x)+dA_x[Cy]+K_32(x,y)+K_23(x,y)+dB_y[Dx]+B(y),     (4)

where the subscripts are the two degrees. Their combined coefficient
space has dimension 12+12=24. Put K=K_32+K_23 and

    T_0=T_3-A-B-dA_x[Cx]-dB_x[Dx],
    U(x;u)=dT_3,x[H_0 u]-dA_x[u]
             -d^2 A_x[u,Cx]-dB_x[Du].                    (5)

The diagonal restriction and complete normal equation are equivalent to

    K(x,x)=T_0(x),   d_1 K_(x,x)[u]=U(x;u).               (6)

Indeed, full derivative matching is
dF_(x,x)[u,v]=dT_3,x[H_0 u+(Id-H_0)v]. Once the first-variable
equation and the diagonal value hold, differentiating that value recovers
the second-variable equation. In differentiating dA_x[Cy] with respect
to x, y is still independent; this gives the Hessian term in (5) and
no extra dA_x[Cu].

We prove that (6) is solvable for every binary quintic T_0 and every
quartic-in-x, linear-in-u expression U. Write U_rad(x)=U(x;x) and set

    P=U_rad-2T_0,   Q_0=3T_0-U_rad.

Choose K_32 and K_23 with diagonal values P and Q_0. Each diagonal
evaluation is onto the binary quintics: every degree-five monomial
splits into a degree-three and a degree-two monomial (or the reverse).
Then K(x,x)=T_0 and Euler homogeneity gives

    d_1 K_(x,x)[x]=3P+2Q_0=U_rad.

The residual R(x;u)=U(x;u)-d_1K_(x,x)[u] has zero radial contraction.
Writing R=u0 r0(x)+u1 r1(x), this says x0 r0+x1 r1=0. Since x0,x1
are coprime in C[x0,x1], there is a binary cubic g with
r0=x1 g and r1=-x0 g. Therefore

    R(x;u)=(u0 x1-u1 x0)g(x).

Let Delta=x0 y1-x1 y0. Choose a polynomial L_21 of bidegree (2,1)
with L_21(x,x)=g(x); this evaluation is onto the binary cubics by the
same monomial splitting argument. Adding Delta L_21 to K_32 changes
neither diagonal value and changes d_1 K by exactly R, since
d_1 Delta_(x,x)[u]=u0 x1-u1 x0. It preserves both axis conditions
because its bidegree is (3,2). This solves all of (6).

Thus the map K -> (K(x,x),d_1K_(x,x)) is onto a space of dimension
6+10=16 and has kernel dimension eight. The proof is independent of
C,D,H_0; in particular it covers all positive metrics, not just generic
ones. In contrast to degree four, the distinct Euler weights 3 and 2
permit independent prescribed radial derivative and value.

**Real range and dimensions.** Apply the construction to both complex
H components. The normal and restriction maps commute with the full
antilinear involution: the graph embeddings and orthogonal projections
are quaternionic and the metric is real. For real prescribed data,
average any complex solution with its full involution. The average
satisfies the same equations and is a real solution. This is averaging
on H* tensor Sym^5, not an invalid reality condition on a lone quintic.

For one H component there are 56 quintic coefficients. The combined
axis data (values and normal derivatives) use 2(6+10)=32 independent
coordinates, leaving the 24 middle coefficients. The diagonal value
and normal derivative use sixteen more independent coordinates by (6).
Hence the combined three-line first-jet map has rank 48 and kernel
eight, for all metrics. In particular the thirty normal conditions
are independent, leaving dimension 26; the intrinsic restriction range
has dimension eighteen. Tensoring with the two-dimensional H* gives
complex dimensions 52,36,16 for the normal solution space, restriction
range and restriction kernel, respectively. These are also their fixed
real dimensions. The normal solution space and every real restriction
fibre are invariant under the real structure, so the stated real affine
fibre dimension follows. Orthogonal extension already proved ambient
surjectivity; no dimension for the unused ambient kernel is required.

**Source scaling and limits.** Let k_i encode (nabla R) of the original
K3 metric in unit quaternionic frames matched to phi_i/sqrt(a_i) by
the actual isometry df_i/sqrt(c), where a_i=a,b,t. Constant metric
rescaling leaves the connection unchanged and multiplies both the
covariant curvature and its covariant derivative by c. Also
df_i(e)=sqrt(c/a_i) phi_i(e) in these matched frames. Applying (2)
in all five slots gives

    (c/a_i)^(5/2) K|_(phi_i)=c k_i,
    K|_(phi_i)=a_i^(5/2) k_i/c^(3/2).                     (7)

Equivalently the scaled metric's unit-frame derivative is k_i/c^(3/2).
The fifth slot includes the derivative direction; copying L123's
four-tensor factor would be incorrect. All scale factors are nonzero,
so this rescaling preserves the full-range conclusion.

At this algebraic order the curvature value and its first derivative
have separate linear identities: the differentiated zero-second-
fundamental-form condition is (2), with no remaining curvature-value
term. Thus any fixed compatible order-zero data may be retained when
performing this first-derivative extension. This is not a claim that an
arbitrary such pair integrates to a metric, much less to three actual
branches or the global F. Higher derivatives, actual K3 values and
angles, original-image gluing, reconstruction, transport and the
universal primitive Hodge gap remain unresolved. No local symmetry,
vanishing source derivative or nonvanishing source derivative was assumed.

**Checks.** The standard-library exact rational script
`scripts/opposite-curvature/check_three_line_first_derivative.py`
builds the complete 30-by-56 normal and 18-by-56 restriction matrices
for one complex H component at four positive metrics: orthogonal equal,
generic nonorthogonal, and both of L123's exceptional types. Each has
normal rank 30, combined rank 48 and restriction range 18. The complete
mixed interpolation matrix has rank 16 and kernel eight; the zero-value
corrections have derivative rank four and zero radial contraction.
The odd-quintic quaternionic operation squares to minus one as required.
All checks pass with no failures. The full matrices and results are in
`scripts/opposite-curvature/three_line_first_derivative_certificate.json`.
Reproduce with `python3 scripts/opposite-curvature/check_three_line_first_derivative.py`.
These samples support the uniform proof above; they do not certify
arbitrary angles, reality, geometric realization or actual source jets
by themselves. The imported framework is not reproved; the interpolation,
full-kernel bridge and scaling are the necessary specialization.

**Separate critical audit, 2026-10-18 (step 371).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-18-three-line-first-derivative-critical-audit.md`.
This is EXPLORATION / RESEARCH / REPRODUCTION, task proof_audit. The
audit finds no substantive error or stronger conclusion, and does not
claim a second advance for the previously established full range. It
retains L118, L121 (including L120 through it), and L123 as conditional
inputs rather than re-auditing their upstream proofs. The imported
primary statements and their assessed scope are unchanged.

For the real-kernel bridge, before imposing Bianchi a coefficient has
one derivative E index and four symmetric curvature E indices. In the
cyclic identity take h_0=h_1=h and choose h_2 with epsilon(h,h_2)
nonzero; choose the last two H arguments with nonzero pairing. The
first two cyclic terms then have opposite nonzero coefficients and
the third vanishes. This equates the coefficients obtained by exchanging
the derivative E argument and the first curvature E argument, for
every h. Together with the four curvature symmetries this is precisely
fivefold E symmetry. Conversely the two-dimensional alternating-form
identity in the proof kills the cyclic sum for every H argument. Thus
there is neither a missing Bianchi equation nor a larger independent-
quartic-derivative space hidden in (1). This checks the specialized
bridge to the imported kernel, without using an omitted representation
classification or an n>=2 restriction on the source.

The antilinear operation is on the whole coefficient: quaternionic
operations on H* and each of the five E* arguments have six minus signs
on squaring. Compatibility of epsilon_H with quaternionic conjugation
identifies its fixed tensors with real covariant five-tensors. A line,
its metric orthogonal complement and its orthogonal projection are
quaternionic. Restriction and normal evaluation therefore intertwine
this operation, including the H index. Averaging a solution for fixed
real data preserves those data and every homogeneous normal equation.
The real dimension is the complex dimension of this full real form;
it is not twice that dimension, and an odd quintic alone is not real.

For (2), use the tensor-product connection on the Hom bundle of three
tangent inputs and one ambient output. Its derivative subtracts the
connection term of each of X,Y,Z and adds the ambient output derivative.
Parallel df cancels every comparison term, and the derivative direction
is df(v). After lowering, metric parallelness supplies exactly the
fifth covariant slot. Testing a normal fourth curvature argument adds
no unaccounted second fundamental term: its tangent derivative is
still normal because the branch is totally geodesic. Polarizing the
four tangent E arguments (the derivative and three curvature inputs)
then gives exactly (3). Skew-adjointness supplies the corresponding
normal-space preservation, not prescribed normal curvature. No
transverse derivative equation is being suppressed. At this first
order there is no curvature-commutator term; such terms belong to a
further covariant differentiation, outside this audit.

For the coordinate interpolation, direct pairing with the diagonal
gives H_0=(a Id+Q*)/t and its complementary coefficient Id-H_0.
The first two normals fix only bidegrees (4,1) and (1,4). At the
diagonal the first derivative of dA_x[Cy] is its Hessian in the
independent x variable; it has no extra derivative of Cy. This confirms
both signs and every fixed term in (5). The diagonal value and first
partial derivative determine the second partial derivative by the chain
rule, so (6) retains the complete normal equation.

Independently checking the uniform construction, diagonal values P,Q_0
have sum T_0 and weighted sum 3P+2Q_0=U_rad. The remaining derivative
has radial contraction zero. The polynomial relation
x_0 r_0+x_1 r_1=0 gives r_0=x_1 g and r_1=-x_0 g by coprimality,
with g of degree three. The derivative of Delta in the first variable
has exactly the sign u_0 x_1-u_1 x_0. Multiplication by any (2,1)
lift of g therefore corrects precisely this residual and preserves both
axis jets and the diagonal value. All the monomial splitting maps used
here are onto. No assumption about C,D,H_0 is needed in this argument,
so all positive metrics, including both order-zero rank drops, remain
covered. The middle map consequently has rank 16 and kernel eight.
The two axis jets have 32 independent coordinates and leave exactly
these 24 middle coefficients; adjoining the diagonal jet adds 16 to
the rank. Projection of this surjective combined jet map onto its
30 normal coordinates is also onto. Hence its zero-normal subspace
has dimension 26 and restriction range 18 per H component. The whole
real-module dimensions are indeed 52,36,16.

Orthogonal compression preserves symmetry and the real Bianchi bridge.
Conversely extending by the orthogonal projection in all five E slots
annihilates every exterior normal, even when the derivative slot is
tangent to a branch. This proves range equality and does not assume
that the actual curvature derivative preserves W. Source rescaling
also survives an independent count: lowering multiplies the original
covariant derivative by c, while df on each of the five matched source
unit arguments contributes sqrt(c/a_i). Thus (7), rather than a
four-slot scale, is required. The common ordered quaternionic triple
is retained; the actual positive scale is L118's c=2lambda.

The construction script was rerun, then
`scripts/opposite-curvature/audit_three_line_first_derivative.py`
independently reconstructed all saved normal and restriction entries
by the monomial product rule, and all interpolation/correction entries
by their two-monomial determinant formulas. A separate sparse rational
row reduction checks the complete matrices, rather than their preview
or recorded ranks. All 11,196 required entries match. Each sample has
normal rank 30/30, combined rank 48/48 and range 18/18; interpolation
rank is 16/16 and correction rank 4/4, with zero diagonal values and
zero radial corrections. There are no failures. The full audit evidence
is in `scripts/opposite-curvature/three_line_first_derivative_audit_certificate.json`.
Reproduce with `python3 scripts/opposite-curvature/audit_three_line_first_derivative.py`.
These are finite supporting checks; the uniform and real conclusions
rest on the audited proof above, not on sampling.

ATTEMPTS/072 remains the bounded order-one stop. The independent L123
order-zero conditions remain necessary, with actual source curvature
values and angles still unknown. Neither the real extension nor this
audit realizes a metric germ, an actual collision, F, a cycle or
transport; the universal primitive Hodge gap remains unresolved.

## Mathlib

Full matching coverage of this real hyperkähler derivative module and
the simultaneous restriction calculation has not been checked. No
absence claim is made. Primary inputs are precisely cited above;
their specializations and the complete interpolation proof are recorded
here. No metric-realization theorem is used or asserted.
