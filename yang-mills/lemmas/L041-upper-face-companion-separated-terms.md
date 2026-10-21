# L041 — The d-containing companion lines vanish at the a² scale

## Hypotheses

Keep precisely L040's hypotheses, matrices, local coordinates, three-color
contraction and both original probes. In particular a=8/N, tau=1/16,
the forest is lower-rooted in direction 1, and every upper (1,mu)
plaquette is retained, including transverse boundary strips. Constants
may depend on the fixed smooth displacement, box and tau, but not on
sufficiently fine admitted meshes or the selected plaquette. Take the
fixed-mesh small-coupling coefficient first.

All matrices in this proof use ordinary dimensionless coordinates.
Write r_H,r_L,r_d for the transposes of the three local lifted rows, and
x_s=Sigma r_s. Thus v_rs=x_r^T A_0 x_s, in L040's notation. The letter
d in these subscripts denotes the local circulation, not a physical
incidence operator. Use L040(1) for u_h,...,u_f and v_h,...,v_f.

## Conclusion

Let D_(i,a) be the sum of the last two lines of L040(3):

\[
D_{i,a}=\sum_p\{u_lv_e+u_ev_l-2u_fv_f
             +4(u_hv_f+u_fv_h-u_bv_c-u_cv_b)\}.       \tag{1}
\]

For i=3,6,

\[
 |D_{i,a}|\le C_i a^{-1},\qquad |a^2D_{i,a}|\le C_i a\longrightarrow0.
                                                               \tag{2}
\]

The estimates used are uniform, with all transverse boundary strips:

\[
 |v_e|+|v_c|+|v_f|\le Ca^4,\qquad
 |v_h|+|v_l|+|v_b|\le Ca^{-1}.                         \tag{3}
\]

The borderline sum of u_c v_b is controlled by exact summation by
parts, not by its absolute termwise bound. Consequently, if

\[
 T_{i,a}=-3\sum_p(u_hv_l+u_lv_h-2u_bv_b),              \tag{4}
\]

then a²(sum_p G^(0)_(i,p)-T_(i,a)) tends to zero. By L040, T depends
only on Psi_24. No existence or value of lim a² T is asserted. In
particular no cancellation against L039, full power or logarithmic
coefficient, finite matching, or interacting reflected bound follows.
The bound O(a^-1) in (2) does not exclude a logarithm in these lines.

## Proof

### 1. A separated circulation Green column is smooth and small

L029(10) gives the exact row, before forest retraction,

\[
 r_d^T z=z_1(N-1,v)-z_1(N-1,v')-z_\mu(N-1,v),\quad v'=v+\hat\mu.
                                                               \tag{5}
\]

Fixed links and boundary vertex evaluations are zero. In particular this
is the row of the relative plaquette incidence D_1, including when an
endpoint meets a transverse face. We prove that x_d=Sigma r_d has a
smooth extension on a fixed neighborhood of the coefficient support
with, for every fixed m,

\[
 \|x_d\|_{C^m}\le C_m a^3.                            \tag{6}
\]

This is a local extension of its sampled entries, not a bound near its
source or a global continuum interpolation claim.

Use L003's relative tensor spectrum, separating the three transverse
coordinates and leaving the axial resolvent explicit. In component 1,
all transverse coordinates are Dirichlet vertices. For transverse
indices k let sigma_k=4 sum sin²(k_j pi/(2N)) and eta_k>0 satisfy
2 cosh eta_k=2+sigma_k. The remaining axial operator is the
N-edge Neumann difference Laplacian plus sigma_k. Its last-column
inverse, at r=0,...,N-1, is

\[
 R^N_k(r,N-1)=
 \frac{\cosh((r+1/2)\eta_k)}
 {2\sinh(\eta_k/2)\sinh(N\eta_k)}.                   \tag{7}
\]

In component mu the transverse mu coordinate is an edge cosine
coordinate (including k_mu=0); the other two transverse coordinates
are Dirichlet vertices. The axial coordinate is an interior vertex,
and the corresponding last-column inverse is

\[
 R^D_k(j,N-1)=\frac{\sinh(j\eta_k)}{\sinh(N\eta_k)},
 \qquad j=1,...,N-1.                                 \tag{8}
\]

These are finite inverse-matrix entries, with no measure factor.
For (8), the homogeneous recurrence and zero endpoint conditions give
the usual Dirichlet inverse; the source at N-1 cancels its sinh eta
factor. For (7), the left endpoint equation is satisfied by
cosh((r+1/2)eta). At the right endpoint its numerator obeys
(1+sigma)cosh((N-1/2)eta)-cosh((N-3/2)eta)
=2 sinh(N eta)sinh(eta/2), giving unit source. The interior
recurrence is the same. Positivity gives uniqueness. Thus (7)–(8)
verify the required mixed boundary cases directly.

Here |k| is bounded below by a positive constant: component 1 has
three positive indices and component mu has two. The elementary sine
bounds and eta=2 asinh(sqrt(sigma)/2) give
c a|k| <= eta <= C a|k|, uniformly over all allowed indices.
Also N eta is bounded below away from zero. On any fixed compact axial
interval at distance delta>0 from the top face, (7) is bounded by
C(a|k|)^(-1) exp(-c delta |k|) and (8) by
C exp(-c delta |k|). Their smooth hyperbolic extensions have m-th
physical derivatives bounded by these same estimates times
C_m |k|^m. This follows by differentiating the numerators, using
physical axial coordinate a(r+1/2) or aj and bounding the denominator
by its exponential form. Shrinking delta by a fixed factor covers
every stencil neighbor as well.

Each normalized transverse product mode has magnitude <=C N^(-3/2)
and m-th physical derivatives <=C_m N^(-3/2)(1+|k|)^m.
In component 1 the source coefficient is its value at v minus its
value at v', hence has magnitude <=C a|k|N^(-3/2).
This bound remains true at pinned endpoints because the same sine
extension is zero there. In component mu the single source coefficient
has magnitude <=C N^(-3/2), or is zero when the link is fixed.
Multiplying the observation mode, source coefficient and (7) or (8)
gives, in either case, at most
C_m a^3(1+|k|)^(m+1) exp(-c delta |k|) for each differentiated term.
The sum of this majorant over all transverse indices is uniformly
finite. These are finite mode expansions, and their positive
majorants extend to the full integer orthant, so the derivative bounds
are uniform without dropping high modes. This proves (6), including
all transverse source positions. Only components 1 and mu occur.

### 2. Apply the compact residual to that column

The physical residual N_a of L028 and the dimensionless residual here
satisfy A_0=a² N_a. L028's proof of its equation (5) establishes, more
generally for smooth inputs on the coefficient neighborhood,

\[
 \|N_a f\|_\infty\le Ca^2\|f\|_{C^5}.               \tag{9}
\]

It telescopes the centered incidence, endpoint, clover and coefficient
stencils, including their adjoints, against L009's polarized continuum
identity. Thus it applies to the mesh-dependent smooth extension in
(6), not only to a fixed relative mode. All nonzero rows and their
input neighbors stay in a fixed compact subset of the box. Multiply
that extension by a fixed smooth cutoff equal to one on a slightly
larger neighborhood of these stencils. The global C^5 norm remains
O(a³), and all samples relevant to A_0 are unchanged. Therefore

\[
 \|A_0 x_d\|_\infty\le Ca^7,\qquad
 \|A_0 x_d\|_{\ell^2}\le Ca^5.                       \tag{10}
\]

The second estimate counts O(a^-4) link entries. No pointwise
consistency assertion is applied to a singular source neighborhood.

For s=H,L, L040 gives x_s=sqrt(N) E_0 G_3 eta_s. Its transverse
spectrum yields

\[
 (G_3^2)(v,v)\le C N^{-3}N^4
       \sum_{k_2,k_3,k_4\ge1}|k|^{-4}\le CN.          \tag{11}
\]

The sum is finite by three-dimensional shell counting. The two-entry
vectors eta_H and eta_L therefore give ||x_H||+||x_L||<=CN<=C/a.
For d, D_1 Sigma D_1^T is an orthogonal projection, by L003's finite
Hodge decomposition; thus r_d^T Sigma r_d<=1. The gap gives
||Sigma||<=Ca^-2, so ||x_d||²=r_d^T Sigma²r_d<=Ca^-2.
Cauchy–Schwarz with (10) proves the first three bounds in (3).
The norm argument includes pinned and degenerate plaquette rows.

### 3. A relative form bound for the compressed scalar residual

Use the exact compressed stencils bar K, bar Q_i, bar A of
L040(9)–(11). Their coefficient functions have compact transverse
support and uniformly bounded first physical derivatives. Extend a
pinned transverse vertex field phi by zero outside the cube. All
coefficient stencils are interior for sufficiently fine meshes, so
these extensions compute the compressed forms exactly.

On the infinite grid write S_j for the unit shift, D_j=S_j-I and
T_j=(S_j-S_j^(-1))/2. The T_j are skew-adjoint, commute with D_l,
and satisfy ||T_j phi||<=||D_j phi||. The product rule is

\[
 D_j\bar K\phi=K^{(j)}D_j\phi+
       \sum_k M_{D_j\bar u_k/a}T_k\phi,\qquad
 K^{(j)}=a^{-1}\sum_k M_{S_j\bar u_k}T_k.             \tag{12}
\]

The symmetric part of K^(j) is a sum of
[M_(S_j bar u_k),T_k]/(2a). Each commutator is a sum of two shifts
with coefficients bounded by C a before division by a, since adjacent
coefficient values differ by O(a). Consequently its operator norm
is bounded uniformly. Also ||D_j bar u_k/a||_infinity<=C.
Pairing (12) with D_j phi and summing j shows

\[
 |\langle\phi,\Delta_3\bar K\phi\rangle|
 \le C\sum_j\|D_j\phi\|^2.
\]

The exact bar Q_3 edge weights and bar Q_6 central-difference weights
in L040(10) are bounded. Their forms satisfy the same right-side
bound. Since bar A is symmetric, this proves the two-sided form
inequality

\[
 -C\Delta_3\le\bar A\le C\Delta_3.                  \tag{13}
\]

This calculation estimates the particular finite scalar transport
stencil; no unproved general boundary regularity theorem is used.
By (13), |eta^T G_3 bar A G_3 zeta| is at most
C sqrt(eta^T G_3 eta) sqrt(zeta^T G_3 zeta).
L029's bounds G_3(v,v)<=6, eta_L^T G_3 eta_L<=1 and
eta_H^T G_3 eta_H<=6 then give the remaining bounds in (3).
The zero-extended calculation retains all pinned transverse faces.

### 4. Sum the borderline cross term by parts

Define the real diagonal field on transverse vertices

\[
 Z(v)=N\delta_v^T G_3\bar A G_3\delta_v,
 \quad Z(v)=0\text{ on the transverse boundary}.      \tag{14}
\]

It obeys |Z(v)|<=C/a by (13) and L029's diagonal bound. Symmetry
of G_3 bar A G_3 gives the exact identity on every mu-edge,

\[
 v_b(v,\mu)=\tfrac12\{Z(v)-Z(v+\hat\mu)\}.          \tag{15}
\]

We need a smoothness bound only for the flowed entry u_c. At fixed mu,
let c_(i,mu)(v)=u_c(v,mu) on that edge. The full heat expansion behind
L040(13) gives

\[
 |c_{i,\mu}(v)|\le C_i a^2,\qquad
 |c_{i,\mu}(v)-c_{i,\mu}(v-\hat\mu)|\le C_i a^3.     \tag{16}
\]

Here is the extra derivative justification, including edges meeting a
face. In L028's physical modes the stored covariance-square-root
column is a R_F b_k, with b_k=lambda_k^(-1/2) f_k. Its smooth sine/cosine
extension has every fixed C^m norm bounded by a polynomial in k,
uniformly in a. As a function of the transverse edge position y, its
H row is a/2 times the sum of b_(k,1) over all N axial edges at y and
y+a e_mu. Thus its C^1 norm is polynomially bounded, since Na=8.
Its d row is a times the expression in (5), with the transverse
component sampled at its edge midpoint. The first two terms differ
by O(a) in C^1. The transverse component at axial vertex 4-a is
O(a) in C^1, because its sine extension is identically zero at the
top face x_1=4. Hence this d row is O(a²) in C^1 with a polynomial
mode bound. These formulas remain the exact rows at pinned transverse
endpoints because the corresponding mode components vanish there.

The U expansion pairs these H and d columns against
exp(-tau lambda_k) (B_(i,a))_(kl) exp(-tau lambda_l), where the
relative probe matrix B_(i,a) of L008 has uniformly bounded norm.
(The B_(i,a) in this sentence is L008's relative form, not L040's
heat-sandwiched dimensionless matrix.) Each entry is consequently
bounded by the same constant. L003's lambda_k>=c|k|² makes the
product of any two polynomial mode bounds and these two heat factors
summable uniformly over all modes. Thus the transverse smooth
extension of c_(i,mu) has C^1 norm <=C_i a². The mean-value theorem
over distance a proves (16). There is no differentiation of an
uncontrolled mesh error.

Fix mu and the other two transverse coordinates. Sum over the full
mu-edge interval j=0,...,N-1. With Z_0=Z_N=0, exact finite summation
by parts gives

\[
 \sum_{j=0}^{N-1}c_jv_{b,j}
  =\tfrac12\sum_{j=1}^{N-1}(c_j-c_{j-1})Z_j.          \tag{17}
\]

The end edges are included in this identity, not discarded. Positions
on either of the other transverse faces have only fixed rows and
contribute zero; the remaining coordinates range over every interior
vertex. There are O(a^-3) terms after summing those coordinates and
mu=2,3,4. Equations (14), (16), (17) imply

\[
 \left|\sum_p u_cv_b\right|\le C_i a^{-1},\qquad
 a^2\left|\sum_p u_cv_b\right|\le C_i a.             \tag{18}
\]

No pointwise improved bound for v_b, sign, or cancellation between
different potential sectors is presumed.

### 5. Assemble the scaled bound and delimit its scope

Combine (3) with L040(13). The absolute per-plaquette bounds for
u_l v_e, u_e v_l, u_f v_f, u_h v_f, u_f v_h, u_b v_c are,
respectively, O(a^6), O(a^3), O(a^7), O(a^4), O(a²), O(a^5).
There are at most 3N(N-1)²=O(a^-3) nonfixed selected plaquettes.
After summation and multiplication by a² these bounds are,
respectively, O(a^5), O(a²), O(a^6), O(a³), O(a), O(a^4).
Equation (18) controls the one remaining summand. The fixed factors
and all three colors are already in L040(3), so (1)–(2) follow with
no extra color multiplier. This proves the claimed reduction to (4).

Reuse the ready SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. The general bulk flow
renormalizability input remains Luescher–Weisz,
[arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2), sections 7.1–7.4,
equations (7.1)–(7.8), and section 8.2, in its stated perturbative scope.
It is not used to bound the unflowed physical-boundary column here.
The finite recurrence verification, local centered-stencil estimate
and summation by parts specialize standard methods to the exact
fixed-box rows; they do not reprove that general theorem. This is
local REPRODUCTION progress, with no originality claim. No additional
source hypothesis or different mathematical target is introduced.

The exact finite checks are reproducible with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_companion_separated_identities.py`.
The certificate is
`scripts/combined-ward-response/companion-separated-identities-certificate.json`.
All 24 endpoint-inverse checks at N=2,3,8,24 and three positive rational
exponentials pass with exactly zero residual. All 616 bilinear basis
pairs of (17) at those sizes also pass. These check endpoint factors
and the complete pinned summation identities at the listed sizes;
the uniform estimates and every-mesh conclusion are the analytic
proof above, not numerical extrapolations.

The remaining trace (4), its unflowed diagonal asymptotics and possible
cancellation against L039 are unresolved. Even that cancellation would
leave slower powers and logarithms, other plaquettes and nonlinear
jets, L019 compensation, finite matching, the reflected-error threshold
c_box/2, full continuum axioms and infrared finite positive mass open.

## Mathlib

Coverage of the full fixed-box estimate (2): **not checked**. Coverage
of its supporting finite matrix, trigonometric spectrum, recurrence,
Taylor and summation-by-parts identities: **not checked**. No matching
Mathlib theorem is asserted, and unknown coverage is not absence.
