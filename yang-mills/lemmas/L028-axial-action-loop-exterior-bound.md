# L028 — A uniform bound for the interior axial action-loop response

## Hypotheses

Use precisely L008's smooth displacement, central-difference strains and
two quadratic forms, L009's endpoint-averaged generator, L010's probes at
tau=1/16, and L026's lower-rooted direction-1 straight forest. Take the
small-coupling coefficient at each fixed mesh a=8/N first. Select only
L027's one-internal-action-pair contribution on (1,mu) plaquettes whose
four vertices are interior, mu=2,3,4. Denote this set by P_ax. In
particular its lower axial levels are 1,...,N-2; the upper-face omitted
forest links are not included.

All constants below may depend on the fixed box, displacement and tau,
but not on sufficiently fine admitted meshes or the chosen plaquette.
Delta below is the physical relative one-form Hodge Laplacian, with
the factors 1/a^2 included. Matrices use inner-product orthonormal
coordinates unless explicitly called stored coordinates.

## Conclusion

Decompose the signed sum of L027(7) into the path, mixed and curvature
pieces of L027(16), denoted G_path, G_mix and G_curv. For both i=3,6,

\[
 |G_{i,\mathrm{path}}|\le C_i,\qquad
 |G_{i,\mathrm{mix}}|\le C_i a^{1/2},\qquad
 |G_{i,\mathrm{curv}}|\le C_i a.
 \tag{1}
\]

Consequently the selected sum is O(1), and its ratio to
log(sqrt(tau)/a) tends to zero. No sign, limiting finite value, or
bound with a useful numerical constant is asserted. This does not
contradict L027's growing coefficient matrix or its finite-mesh samples.

The no-internal-pair class, transverse and excluded boundary plaquettes,
other action/measure/residual/flow jets and L019's cancellations are not
evaluated. Neither the complete logarithm nor the interacting reflected
error <= c_box/2 follows. No continuum construction or mass gap follows.

## Proof

### 1. Quantitative consistency of the actual residual

Use L023's notation

\[
 N_a=\tfrac12(L_a K_a+K_a^*L_a)-Q_{3,a}-Q_{6,a},\quad
 L_a=d_a^*d_a,\quad R_a=\Delta^{-1/2}N_a\Delta^{-1/2},
 \quad B_{i,a}=\Delta^{-1/2}Q_{i,a}\Delta^{-1/2}.
 \tag{2}
\]

L008 gives sup_a ||B_(i,a)||<infinity. We need a rate stronger than
L023's strong-mode convergence. Here it follows from the particular
centered stencils; it is not inferred from that convergence.

Regard each component as sampled at its cell center. Between staggered
grids the incidence derivative and averaging map are, in the affected
coordinate,

\[
 \delta_{j,a}f(z)=\frac{f(z+a e_j/2)-f(z-a e_j/2)}a,
 \qquad c_{j,a}f(z)=\frac{f(z+a e_j/2)+f(z-a e_j/2)}2.
 \tag{3}
\]

Their formal interior adjoints are respectively -delta and c, acting
between the reverse grids. Taylor's integral remainder gives, for
each nonnegative integer r,

\[
 \|\delta_{j,a}f-\partial_j f\|_{C^r}
 \le C a^2\|f\|_{C^{r+3}},\qquad
 \|c_{j,a}f-f\|_{C^r}\le C a^2\|f\|_{C^{r+2}}.
 \tag{4}
\]

The same estimates hold for the full-step central derivative used in
u_a,w_a,s_a. Interpret those coefficients as smooth functions on all
real points by L008's same formulas on the fixed smooth Psi. They
converge to u,w,s with O(a^2) error in every fixed C^r norm and are
uniformly bounded in those norms. Their supports lie in one compact
interior set for small a.

For completeness, the relevant operator compositions are as follows.
The clover map from plane mu nu to vertices is c_mu c_nu. The endpoint
map from vertices to nu-links is c_nu. Thus K_a first applies d_a,
then the clover map, multiplies by the appropriate u_(a,rho), sums
rho and applies the endpoint map. Its adjoint reverses precisely
these maps, including differentiation of the coefficient through d_a*.
The triplet is d_a* W_3 d_a, where W_3 on a mu nu plaquette is the
four-vertex average c_mu c_nu(w_(a,mu)+w_(a,nu)). This is the weight
of the average of squares, not the square of an averaged curvature.
The shear is d_a* C* S_a C d_a, where C is the ordered clover map
and S_a is the symmetric vertex matrix of L008's stated shear
quadratic form. These identities follow by polarizing those forms;
the symmetric cross-entry factors are retained in S_a.

Here is an explicit check of the adjoint composition. Use six
independent plane components, extend them antisymmetrically when
contracting indices, and write E_a for the diagonal endpoint map
whose nu component is c_nu. Define
(M_a F)_nu=sum_rho u_(a,rho) F_(rho nu) on vertices. Then

\[
 K_a=E_a M_a C_a d_a,\qquad
 K_a^*=d_a^* C_a^* M_a^* E_a^*,\qquad
 (M_a^*b)_{\rho\nu}=u_{a,\rho}b_\nu-u_{a,\nu}b_\rho
 \quad(\rho<\nu).
\]

All these spaces have the same a^4 weight, so no dimension or
cell-volume factor enters these adjoints. On the coefficient
support, C_a^* and E_a^* are the same centered averages on the
reverse grids. The incidence adjoint uses -delta with the exterior
signs. In particular d_a* differentiates the products containing
u_a; no derivative of u_a is suppressed. Outside a fixed compact
enlargement of that support the complete adjoint term is zero.

Every map just listed is centered between its input and output grids.
Replacing it by its continuum limit using (4), with the product rule
for smooth coefficients, therefore yields an O(a^2) C^r error for
N_a applied to a smooth one-form, bounded by C_r a^2 times its
C^(r+5) norm. Indeed the longest compositions L_a K_a and K_a* L_a
have three derivatives; replacing any one derivative by its error
adds at most two derivatives. Averages add at most two when replaced
by their error, and all other factors have bounded coefficients.
The continuum limiting operator is
(d*d K+K* d*d)/2-Q_3-Q_6=0 by L009's polarized compact-displacement
identity. This identity holds for arbitrary smooth inputs, since all
coefficients vanish near the physical boundary. It applies also to
the smooth extensions of the relative modes.

To make the error comparison precise, telescope each finite operator
composition by replacing one factor at a time by its continuum
factor. A centered derivative is uniformly bounded from C^(s+1)
to C^s by its integral difference formula, and an average is bounded
from C^s to C^s. Multiplication by each coefficient is bounded in
every fixed C^s norm. Replacing a derivative costs two extra
derivatives in addition to its original one, by (4); replacing an
average costs two, and replacing a coefficient costs O(a^2) in
the same C^s norm. The total original differential order is at most
three. Thus every telescoping term is bounded by
C_r a^2 ||f||_(C^(r+5)), including the reversed adjoint compositions.
This comparison uses the smooth coefficient extensions, which differ
from u,w,s by O(a^2); it does not assume div u_a=0 as a continuum
identity. The exact continuum identity uses div u=0.

Let f_(k,a) be an L2_a-normalized relative product mode, with the
component included in k. Its stored entries are exact samples of a
sine/cosine product f_k with C^r norm <= C_r(1+|k|)^r. The normalizing
constants are independent of N, including the zero own-direction
cosine mode. Thus N_a f_(k,a) has a smooth compactly supported
extension g_(k,a) with

\[
 \|g_{k,a}\|_{C^r}\le C_r a^2(1+|k|)^{r+5}.
 \tag{5}
\]

This estimate holds for all allowed k, not only fixed modes: (4)
has no restriction on a|k|. High frequencies merely enlarge its
polynomial right side. Boundary adjoints cause no additional term:
on the enlarged coefficient support they are the interior centered
maps, and elsewhere their outputs vanish.

Applying Delta three times to g uses six centered differences on
this compact support. Repeated integral difference formulas bound
each by the corresponding sixth derivative, without inverse powers
of a. The fixed support stays away from boundary rows, also after
these finitely many shifts. Bounded box volume then gives

\[
 \|\Delta^3 N_a f_{k,a}\|_a
 \le C a^2(1+|k|)^{11}.
 \tag{6}
\]

### 2. Retain the relative inverse and bound its smooth lift

The relative modes and physical eigenvalues obey L009's bounds
|k|^2/16 <= lambda_(k,a) <= pi^2 |k|^2/64, with a uniform positive
gap. Expand g=N_a f_(k,a) in all allowed relative modes. By (6)
and self-adjointness,

\[
 |\langle f_{\ell,a},g\rangle_a|
 \le C a^2(1+|k|)^{11}\lambda_{\ell,a}^{-3}.
 \tag{7}
\]

Extend Delta^(-1)g off-grid by its finite sine/cosine series using
the same coefficients divided by lambda_(ell,a). Equation (7)
bounds the C^1 norm of this extension by

\[
 C a^2(1+|k|)^{11}
 \sum_{\ell\ \mathrm{allowed}}(1+|\ell|)\lambda_{\ell,a}^{-4}
 \le C' a^2(1+|k|)^{11}.
 \tag{8}
\]

The last sum is bounded independently of the mesh: at large |ell|
its summand is O(|ell|^(-7)), summable over four-dimensional labels
and four components. The gap treats the remaining labels. This
retains the full inverse and physical boundary conditions. In
particular neither an infinite-lattice replacement nor a pointwise
inverse estimate is assumed.

For any smooth one-form b, consider its sampled straight-forest
retraction on an interior transverse edge. L026's exact formula is

\[
 (R_F b)_\mu(j,v)=b_\mu(j,v)
 -\sum_{\ell=0}^{j-1}
       [b_1(\ell,v+\widehat\mu)-b_1(\ell,v)].
 \tag{9}
\]

Each bracket is bounded by a||b||_(C^1), and j a<=8, so its value
is bounded by 9||b||_(C^1). The difference at levels j+1 and j is
exactly

\[
 b_\mu(j+1,v)-b_\mu(j,v)
 -b_1(j,v+\widehat\mu)+b_1(j,v),
 \tag{10}
\]

bounded by 2a||b||_(C^1). The transverse endpoints in (9) are
interior; hence both path sums start on the lower face and use the
same lengths. The upper pinned potential is never used in (10)
for P_ax. This is the reason for the selected plaquette restriction.

Let e_(k,a) be the ordinary-coordinate normalized mode vector: its
entries are a^2 f_(k,a). Define

\[
 U_a=a^{-1}R_F\Delta^{-1/2},\quad
 v_k=U_a e_{k,a},\quad z_k=U_a R_a e_{k,a}.
 \tag{11}
\]

The factor a^(-1) converts an orthonormal physical connection to
the stored dimensionless link x=a A_stored. Thus v_k is a times
the retraction of lambda_k^(-1/2) f_(k,a), and z_k is a times
the retraction of lambda_k^(-1/2) Delta^(-1)N_a f_(k,a).
Apply (8)–(10) and the gap. On a selected plaquette write m for
the average of its two positive transverse-edge entries and d for
their upper-minus-lower difference, exactly L027's signed (m,d).
There is a fixed polynomial P(k)=C(1+|k|)^11 such that

\[
 |(v_k)_m|\le aP(k),\quad |(v_k)_d|\le a^2P(k),\qquad
 |(z_k)_m|\le a^3P(k),\quad |(z_k)_d|\le a^4P(k).
 \tag{12}
\]

These bounds hold uniformly on all P_ax, including plaquettes near
faces whose vertices remain interior. They need only C^1 extensions
of the two fields before retraction, not global smoothness of R_F b
across its upper-face jump.

### 3. Sum the actual exterior contraction

L018's linear lift, as used in L027(14), gives for the one-color
full-link exterior matrix precisely

\[
 W_i=U_a E_\tau B_{i,a}E_\tau R_a U_a^T.
 \tag{13}
\]

For example the dimensionless covariance is a^(-2)Delta^(-1),
the dimensionless residual matrix is a^2 N_a, and the dimensionless
flowed probe matrix is a^2 E_tau Q_(i,a) E_tau. Multiplying these
three covariances and two insertions yields (13). This checks every
mesh factor and the order of the nonsymmetric product. The quartic
vertex itself remains in the exact forest law.

Explicitly, the stored physical connection has covariance
a^(-4)Delta^(-1), since its inner product has Gram matrix a^4 I.
Passing to x=a A gives the covariance just used, while a physical
quadratic form <A,Q A>_a becomes x^T(a^2 Q)x. Consequently the
stored lifted product is exactly

\[
 a^{-2} R_F\Delta^{-1}E_\tau Q_{i,a}E_\tau
       \Delta^{-1}N_a\Delta^{-1}R_F^T
 =U_a E_\tau B_{i,a}E_\tau R_a U_a^T.
\]

The identity uses commutation of E_tau with Delta, not commutation
of Q_i or N_a with either operator. Also R_a is symmetric, so the
row e_l^T R_a U_a^T in this product is exactly z_l^T. This verifies
the placement of the residual in (14), without supplying it with
a second unproved heat factor.

Expand (13) in the two heat indices:

\[
 W_i=\sum_{k,\ell}e^{-\tau(\lambda_k+\lambda_\ell)}
 (B_{i,a})_{k\ell}\,v_k z_\ell^T.
 \tag{14}
\]

Since |(B_i)_(k ell)|<=||B_i|| uniformly, (12), the spectral
lower bound, and summability of a polynomial times a Gaussian give
the uniform local entry estimates in (m,d) coordinates

\[
 |(W_i)_{mm}|\le C_i a^4,\quad
 |(W_i)_{md}|+|(W_i)_{dm}|\le C_i a^5,\quad
 |(W_i)_{dd}|\le C_i a^6.
 \tag{15}
\]

All allowed modes are included in the absolutely bounded double
sum. No damping was assigned to the internal action loop.

By L027, 0<=e<=1, |beta-alpha|<=sqrt(4j+34)<=C a^(-1/2), and
0<=h<=4j+34<=C a^(-1). The exact three-color response per plaquette
is

\[
 2e(W_i)_{mm}
 +(\beta-\alpha)((W_i)_{md}+(W_i)_{dm})
 +\tfrac h2(W_i)_{dd}.
 \tag{16}
\]

There are at most 3N^4=3(8/a)^4 plaquettes in P_ax. Equations
(15)–(16) bound the sums of the absolute values of their respective
pieces by C_i, C_i a^(1/2), and C_i a. These stronger absolute-sum
bounds prove (1), with no sign assumption or cancellation between
different plaquettes. The factor in (16) already counts three colors.

The argument specializes the recorded finite Gaussian and centered
stencil formulas. It does not reprove the general flow-renormalization
or lattice stress-matching theorems in the saved literature assessment.
Those theorems do not themselves supply this forest-specific bound.
No originality beyond the inspected-source comparison is asserted.

## Mathlib

Coverage of this specialized relative-box, forest and signed-response
bound: not checked. No full matching Mathlib theorem is claimed.
Taylor's integral remainder, finite spectral expansion and absolute
Gaussian-series summability are used explicitly in the proof; no
formalization or library verification is asserted.
