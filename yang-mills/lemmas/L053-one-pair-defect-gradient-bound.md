# L053 — The one-internal-pair boundary defect is subleading

## Hypotheses

Keep L051–L052's actual three-color SU(2) forest law, both original
probes i=3,6, fixed tau=1/16, a=8/N, all upper transverse edges and
the small-coupling coefficient taken at fixed mesh first. Use their
one-color vertex matrices C=NG3, U,V,W and functional Phi_D. Boundary
vertex values are zero. The edge set includes all transverse end
edges. Let T be L050's incidence, (T h)_e=h(v)-h(v'), and let
P=T G3 T^T. In particular P is an orthogonal projection and

\[
D=P/N+b_N(\Delta_T)(I-P),\qquad 0\le b_N(\Delta_T)\le I.
\tag{1}
\]

Constants below may depend on the fixed displacement, box and flow
time, but not on sufficiently fine admitted meshes.

## Conclusion

For each original probe,

\[
 |\Phi_D(C,W+W^T)|\le C_i a^{-1},\qquad
 a^2\Phi_D(C,W+W^T)\longrightarrow0.               \tag{2}
\]

Consequently L052's complete selected upper nonradial quartic plus
top/top cubic-pair group satisfies

\[
 G_i=-6\Phi_D(U,V)+E_B+E_A+E_\times+O_i(a^{-1}).    \tag{3}
\]

The four displayed sums in (3) still have no joint scaled limit or
cancellation established here. The estimate (2) does not exclude a
subleading power or logarithm in its term. Other cubic pairs, all
remaining action/measure/insertion/flow jets, the complete logarithm,
finite matching and the interacting reflected error <=c_box/2 remain
open, as do continuum fields, full reflection positivity and finite
positive mass. No full compensation of L047 is claimed.

## Proof

### 1. Write the rank-two contraction as a positive-kernel pairing

For a real deterministic pinned vertex field h and a real random
pinned vertex field xi with mean zero and covariance C, define

\[
 (B_h\xi)_e=h(v)\xi(v')-h(v')\xi(v),\qquad
 (M\xi)_e=(\xi(v)+\xi(v'))/2.                      \tag{4}
\]

Only the covariance of xi will be used; it may be taken Gaussian.
For real pinned h,k, expand the four terms in
E[(B_h xi)_e(B_k xi)_f]. If e=(v,v') and f=(w,w'), they are

\[
 h(v)k(w)C_{v'w'}-h(v)k(w')C_{v'w}
 -h(v')k(w)C_{vw'}+h(v')k(w')C_{vw}.               \tag{5}
\]

Sum (5) against the symmetric matrix D. Interchanging the ordered
edge indices shows that the result is symmetric in h,k. Comparing
with all four terms of L051(2) therefore gives exactly

\[
 \Phi_D(C,hk^T+kh^T)
 =E\langle B_h\xi,D B_k\xi\rangle.                \tag{6}
\]

There is no extra color factor in (6): Phi_D is the one-color
functional; the factor 6 in L051 and (3) already accounts for color.
Since D is positive semidefinite, Cauchy–Schwarz gives

\[
 |\Phi_D(C,hk^T+kh^T)|
 \le \mathcal Q(h)^{1/2}\mathcal Q(k)^{1/2},\quad
 \mathcal Q(h)=E\|D^{1/2}B_h\xi\|^2.              \tag{7}
\]

These identities include coincident edges and pinned endpoints.
In particular an end edge has B_h xi=0 when one endpoint is pinned;
it is nevertheless retained in T, P and every matrix sum.

### 2. Use the gradient split without assuming a small rough defect

The exact product identities on each edge are

\[
 B_h\xi=(T h)M\xi-(M h)T\xi
        =-T(h\xi)+2(T h)M\xi.                    \tag{8}
\]

Multiplication of edge vectors in (8) is pointwise. The product
h xi is a pinned vertex field, so (I-P)T(h xi)=0. Since P commutes
with b_N(Delta_T), (1) and its bound b_N<=1 imply

\[
 \mathcal Q(h)\le\frac1N E\|B_h\xi\|^2
                  +E\|(I-P)B_h\xi\|^2.          \tag{9}
\]

Put m_0=||h||_infinity and m_1=||T h||_infinity. The first and
second versions of (8), respectively, give

\[
 \mathcal Q(h)\le
 \frac{2m_0^2}{N}E\|T\xi\|^2
 +(2/N+4)m_1^2 E\|M\xi\|^2.                     \tag{10}
\]

Here ||M h||_infinity<=m_0 and ||I-P||<=1. This is an operator
argument on the complete edge space; it does not replace D by its
low-frequency limit. Its useful small factor m_1 is a difference
of the deterministic external field, not of the rough xi.

There are m=(N-1)^3 interior vertices. From C=NG3 and T^T T=G3^(-1),

\[
 E\|T\xi\|^2=N\operatorname{Tr}P=Nm\le N^4.      \tag{11}
\]

Each vertex belongs to at most six edges, and
|(x+y)/2|^2<=(x^2+y^2)/2. Thus ||M xi||^2<=3||xi||^2,
also at the pinned endpoints. L029(12)'s full-spectrum diagonal
bound G3(v,v)<=6 gives

\[
 E\|M\xi\|^2\le3\operatorname{Tr}C\le18N^4.      \tag{12}
\]

Equations (10)–(12) prove the explicit bound

\[
 \mathcal Q(h)\le
 2N^3m_0^2+(36N^3+72N^4)m_1^2.                   \tag{13}
\]

In particular, if ||h||_infinity<=H and ||T h||_infinity<=aH,
then Q(h)<=C N^3 H^2, since a=8/N and N>=2. Both (11) and (12)
retain the entire covariance spectrum. No operator-norm o(1) bound
on D, and no uniform smallness on quadratic products of rough
potentials, is used. Thus ATTEMPTS/017's obstruction is respected.

### 3. Apply the estimate to the actual heat-expanded exterior

Restrict L028(11)–(14)'s ordinary and residual exterior columns to
the upper potential vertices; denote them by h_k and j_l. L029's
upper-face proof of (13) yields, with a fixed polynomial p,

\[
\begin{split}
 ||h_k||_\infty&\le p(k),& ||T h_k||_\infty&\le a p(k),\\
 ||j_l||_\infty&\le a^2p(l),& ||T j_l||_\infty&\le a^3p(l).
\end{split}                                                       \tag{14}
\]

For the vertex bounds, the local H and L rows give each endpoint as
H+L/2 or H-L/2. The difference bounds are precisely its L rows.
The proof there uses the relative sine extension and includes end
edges. All columns vanish at transverse boundary vertices. Its
estimates are uniform for every allowed mode, with polynomial growth;
no finite-mode truncation has been made.

The exact nonsymmetric exterior product is

\[
 W=\sum_{k,l}e^{-\tau(\lambda_k+\lambda_l)}
       (B_{i,a})_{kl}\,h_k j_l^T.                 \tag{15}
\]

Here B_(i,a) is the bounded relative probe form of L028, not the
forest matrix in L051. The restriction of the full forest exterior
to upper potentials is exactly L051's W=JSBSASJ^T. The residual is
in j_l, with the order of all operators as in L028; it has not been
commuted past a heat factor.

By (13)–(14),

\[
 \mathcal Q(h_k)\le C N^3p(k)^2,\qquad
 \mathcal Q(j_l)\le C a^4 N^3p(l)^2.
\tag{16}
\]

Apply (7) term by term to W+W^T in (15). The relative gap
lambda_k>=c|k|^2 and uniform bound on ||B_(i,a)|| from L028 show
that the complete double sum of the heat weights times p(k)p(l)
is bounded independently of the mesh. Hence

\[
 |\Phi_D(C,W+W^T)|
 \le C_i a^2 N^3 =512 C_i a^{-1}.                 \tag{17}
\]

This proves (2). Substitution into L052(5) proves (3); its O(a^-1)
already retains the contributions from R and E_BA at this scale.
Every dependency in this deduction concerns actual lattice rows,
finite Gaussian contraction, or all-mode estimates. No asymptotic
exchange involving an unbounded internal mode sum has been used.

### 4. Scope and the remaining obstruction

This is a local reproduction of the Gaussian contraction already
proved in L051, the exact spectral split proved in L050, and the
existing smooth exterior estimates. The unchanged SPECIALIZE
assessment `drafts/literature/2026-09-26-current-target.md` covers
the same response, representatives and boundary hypotheses. General
flow renormalization and stress matching are reused within their
recorded scope, not reproved or assigned this boundary estimate.
The four-term expansion (5), the product identities (8), the exact
trace (11), and the endpoint counting in (12) provide analytic checks;
no new numerical certificate or asymptotic diagnostic is needed.

This does not promote (17) to the complete Z cumulant. In
Phi_D(U,V), the residual block V is not a heat-expanded small
external column j_l. Substituting an estimate on smooth modes for
that whole block would repeat the rough-mode error. Nor does (17)
bound E_B, E_A or E_cross. Their joint signed comparison in (3) is
the remaining discriminating a^2-scale test against L047. For any
logarithmic calculation the O(a^-1) terms must be restored.

## Mathlib

Coverage of the full specialized boundary contraction and bound:
**not checked**. Supporting positive-semidefinite Cauchy–Schwarz,
finite Gaussian second moments and finite spectral calculus:
**not checked**. No full matching Mathlib theorem or library
verification is asserted. The precise local results used are
L028–L029, L050–L052; no additional external theorem is imported.
