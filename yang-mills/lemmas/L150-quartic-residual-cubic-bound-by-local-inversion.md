# L150 — Local inversion bounds the complete quartic residual at cubic scale

## Hypotheses

Keep exactly L149's hypotheses, local quartic construction and connected
contraction, including all three colors, both actual L010 probes at
tau=1/16, both insertion subtractions and the straight lower-rooted
direction-1 forest. Thus a=8/N tends to zero through sufficiently fine
admitted even meshes, and the bare coefficient is taken at fixed mesh
before refinement. The displacement and insertion coefficients are the
smooth compact interior coefficients of L008 as used in L028. Every
link in a supported local stencil is then interior; its axial coordinate
is a forest coordinate and is zero. Covariances still come from the
full pinned forest law, including its upper-face condition.

Use L149's ordinary-coordinate tensors K_lambda, U_(i,lambda), C_lambda
and its normalized signed sum Z_(i,a). Use L085's transverse relative
gradient projection P and transverse Hodge Laplacian Delta_T. P_inf is
the infinite-grid transverse gradient projection of L114(1), with unit
edge orientations. No higher Taylor polynomial is replaced by its
unmodified Hodge counterpart.

## Conclusion

For both actual probes i=3,6 there is a mesh-independent constant C_i
such that

\[
 |\kappa_0(f_{i,0},r_2)|\le C_i a^{-3},\qquad
 |Z_{i,a}|\le C_i a.                                      \tag{1}
\]

This improves L149's direct absolute O(a^-4) bound by a signed local
inversion cancellation. It excludes stronger powers in this one
complete insertion response. It proves neither convergence nor a zero
cubic coefficient: the target requires Z_(i,a)=o(a), whereas (1) gives
only O(a). Both insertion subtractions and all first-order force/vector
remainders may contribute at cubic scale. No compensation with L147,
finer power/logarithm estimate, interacting error bound, continuum
construction or mass gap follows.

## Proof

### 1. A bounded remainder after the growing local gradient covariance

Fix a supported edge stencil and let j_* be its central edge midpoint's
axial coordinate in lattice units (a half-integer is allowed). Every
nonzero selected link is transverse and has axial level s with
|s-j_*|<=R, where R is a fixed stencil radius. By the exact finite
identity L085(2), its one-color covariance is

\[
 C((s,e),(t,f))=\min(s,t)P(e,f)
       +\{R_{st}(\Delta_T)(I-P)\}_{e,f}.                   \tag{2}
\]

Here e,f are transverse positive-edge indices, and R_st is the full
Dirichlet axial resolvent. Define the local comparison covariance by

\[
 C^0((s,e),(t,f))=j_*P_{\inf}(e,f),                         \tag{3}
\]

with zero rows for axial links and independent identical color copies.
It is independent of s,t. We prove, entrywise on every such stencil,

\[
 |C-C^0|\le C,\qquad |C|+|C^0|\le C N.                    \tag{4}
\]

First the co-closed term in (2) is locally bounded. Its full two-level
array is a positive covariance. Its diagonal level block is bounded
above by Delta_T^-1, since
R_ss(lambda)<=1/lambda and P commutes with Delta_T. In each component
of Delta_T the tensor modes have one cosine edge index (possibly zero)
and two positive sine vertex indices. Their squared entries are at
most 8/N^3, their eigenvalues are at least 4r^2/N^2 for
r=max(k_2,k_3,k_4), and there are at most C(r+1)^2 labels on a shell.
Consequently every diagonal entry of Delta_T^-1 is at most

\[
 {C\over N}\sum_{r=1}^{N-1}{(r+1)^2\over r^2}\le C.
\]

Covariance Cauchy--Schwarz bounds every cross-level entry of the
co-closed array by C too. This keeps the complete axial and transverse
spectra; it does not localize the raw forest covariance.

We also need a local projection comparison. For any finite transverse
edge e whose endpoints are at distance at least delta N from the
faces, we claim

\[
 \|\operatorname{row}_e(P-P_{\rm bulk})\|_2
       \le C_\delta N^{-3/2}(\log N)^{3/4},\qquad
 P_{\rm bulk}=J_1^*P_{\inf}J_1.                            \tag{5}
\]

This is a single-row specialization of L114's heat argument, with the
row estimate supplied here rather than inferred from its all-row
Hilbert--Schmidt bound. Use its exact heat representation L114(5)
and the killed/free scalar walk comparison L114(6). Both endpoints
of e are interior. Taking their signed difference, then applying the
bounded right gradient, bounds the l2 norm of that row of the heat
integrand I_v by

\[
 C\exp[-c_\delta\min(N,N^2/v)].                            \tag{6}
\]

Indeed the scalar row difference is bounded in l1 by the coupled
walk's boundary-visit probability; l2 is no larger than l1. All finite
input edges remain, including end edges.

For the long-time bound let phi_m be an ordinary-coordinate normalized
three-dimensional Dirichlet vertex mode, with eigenvalue lambda_m.
Its gradient at any edge obeys

\[
 |(T\phi_m)_e|^2\le C N^{-3}\lambda_m.
\]

This follows directly by subtracting the two sine samples: in the
edge direction their difference is
2 sqrt(2/N) sin(pi m_mu/(2N)) cos(pi m_mu(r+1/2)/N),
and the two other factors are bounded by sqrt(2/N). This formula
also includes normal end edges with a zero boundary vertex. The
vectors T phi_m/sqrt(lambda_m) are orthonormal. Thus the finite
gradient heat sandwich has the row bound

\[
 \|\operatorname{row}_e(T e^{-v\Delta_0}T^T)\|_2^2
  =\sum_m\lambda_m e^{-2v\lambda_m}|(T\phi_m)_e|^2
  \le C N^{-3}\sum_m\lambda_m^2 e^{-2v\lambda_m}
  \le C v^{-7/2},\quad v\ge1.                             \tag{7}
\]

The final inequality is the full shell sum in L114(9), whose proof
holds for all v>=1, including v>N^2. Fourier Plancherel gives the
same single-row bound for the infinite gradient heat sandwich:
its squared norm is at most C integral lambda(theta)^2
exp(-2v lambda(theta)) dtheta <= C v^-7/2, since
lambda(theta) is comparable to |theta|^2 on [-pi,pi]^3.
Restricting its input to finite edges cannot increase that norm.
Hence row_e(I_v) has l2 norm at most C v^-7/4.

Choose A so that c_delta A>=6 and split the exact heat integral at
V=N^2/(A log N). For sufficiently large N, V>=1. The integral of
(6) on (0,V) is at most C V N^-6. The integral of the long-time
bound on (V,infinity) is C V^-3/4. Minkowski's inequality proves
(5), as well as absolute convergence of this row integral. No
infinite inverse is asserted to be a bounded l2 operator.

All local rows are a fixed physical distance from the transverse
faces, so (5) is uniform on the supported stencils. In (2) subtract
(3), keeping the exact finite covariance:

\[
 C-C^0=(\min(s,t)-j_*)P
       +j_*(P-P_{\rm bulk})+R_{st}(\Delta_T)(I-P).
\]

The first term is bounded by C because |min(s,t)-j_*|<=R and
P is an orthogonal projection. The second is bounded by
C N^-1/2(log N)^3/4 and hence by a constant; the last was bounded
above. This proves (4), also using ||P_inf||<=1 and j_*<=N.
The comparison is made only on these local entries; it does not
delete the upper pin or claim a global covariance-norm approximation.

### 2. Freeze the smooth exterior matrix with a controlled neighbor error

For a supported stencil centered at the physical edge midpoint c,
there is a component/color matrix U_i^0(c), constant across its
spatial placements and zero on axial components, such that

\[
 |U_i^0|+|U_i|\le C_i a^2,
 \qquad |U_i-U_i^0|\le C_i a^3.                            \tag{8}
\]

Here constant means that an entry depends only on the two link
components and colors, not on which occurrence of a link is selected.
This is an exterior comparison, not a replacement of the insertion.
To justify the additional neighbor estimate, use L149(9)'s exact
heat-mode expression for U_i and L028's smooth interior forest lift.
In ordinary orthonormal coordinates a relative mode e_k has entries
a^2 f_k, where f_k is a sampled normalized sine/cosine product.
The lifted column T_a e_k=a^-1 R_F Delta^-1/2 e_k therefore has
a smooth interior extension with C^1 norm bounded by
C a p(k), for a fixed polynomial p.

For completeness, in transverse component mu the lift before the
inverse eigenvalue factor is

\[
 a^2\left[f_{k,\mu}(x)
  -a\sum_{\ell=0}^{j-1}
       \delta_{\mu,a} f_{k,1}(-4+(\ell+1/2)a,x_\perp)\right].
\]

The finite axial cosine sum has its exact sine-primitive extension;
for axial index zero it is j times the constant mode. For nonzero
index its denominator is 2 sin(pi k_1/(2N));
(k_1/N)/sin(pi k_1/(2N)) is uniformly bounded for 1<=k_1<N.
Differentiating once and bounding the transverse finite difference
by its integral formula gives a polynomial bound in the full mode
label. This works on every interior stencil, keeps the constant axial
mode and uses no smooth extension across the pinned upper jump.
Axial forest columns vanish identically there.

The physical eigenvalues satisfy lambda_k>=c|k|^2. The coefficient
matrix mathcal B_i in L149(9) is uniformly bounded by L028, so each
of its mode entries is bounded. Consequently the full double series
with factors exp[-tau(lambda_k+lambda_l)] p(k)p(l) is uniformly
summable. Freezing both lifted column values at c in that exact
series defines U_i^0; moving either column by a bounded number of
mesh steps costs O(a^2) in that column and hence O(a^3) in their
product. This proves (8), without truncating any exterior heat mode.
Color covariance and the probe are diagonal with identical copies,
so this comparison includes all three colors.

### 3. The complete frozen force/vector quartic is odd under inversion

For a positive edge e=(z,nu), let Q_e(U;u)=<G_e(U),X_e(U;u)>, with
the exact action force and endpoint-transported generator of L149
(5)–(6). Its degree-four coefficient is precisely the three
force/vector terms in L149(7), before restricting axial coordinates.
Freeze u at its value at the midpoint c of e and denote this local
quartic and its symmetric tensor by q_e^0 and K_e^0.

Invert the entire local lattice stencil about c. Write iota for this
vertex map. A positive link l=(x,mu) is mapped to the reversed
positive link l^iota=(iota(x+a e_mu),mu); reflected configurations
are U'_l=U_(l^iota)^-1 and transformed displacements are
u'(x)=-u(iota x). Inverting all coordinate axes preserves the
ordered two-plane orientation. The four based clover loops are
permuted, so C'(x)=C(iota x) for each ordered plane.

The central edge is mapped to itself with its orientation reversed.
Writing U=U_e, direct substitution in the two endpoint terms gives

\[
 X_e(U';u')=-U^{-1}X_e(U;u)U.
\]

Both endpoint transports are necessary for this equality. The sum of
Wilson plaquette actions incident to this interior edge is invariant
under the local stencil inversion: it permutes the incident squares
and preserves their traces. No inversion of the finite box is needed.
Differentiating
U'_e=U_e^-1 sends a left-frame variation Z on U'_e to the
left-frame variation -U_e Z U_e^-1 on U_e. Therefore its force is

\[
 G_e(U')=-U^{-1}G_e(U)U.
\]

The trace inner product is invariant under this conjugation. Thus
Q_e(U';u')=Q_e(U;u). With u frozen constant, u'=-u, and Q_e is
linear in u. In exact exponential coordinates the reflection is
Theta'_l=-Theta_(l^iota). Taking homogeneous degree four proves

\[
 q_e^0(-\Theta\circ\iota)=-q_e^0(\Theta).                  \tag{9}
\]

This is an identity of the complete force/vector quartic, including
the three degree splittings and all coordinate-conversion terms
already justified in L149. It is not a separate-monomial parity
claim. The interior axial-zero slice is preserved by this reflection.
The union of its incident-force and two endpoint-clover edge stencils
is invariant as a set; one may enlarge any selector to this union by
zero coefficients. Repeated occurrences remain the same variable.

The frozen exterior matrix U_i^0 has no spatial dependence, and its
two link signs under reflection multiply to +1. The internal matrix
C^0 is invariant too: the infinite transverse gradient projection
is the covariance of a stationary scalar-gradient field and is
equivariant under the reflected edge orientations. Equivalently its
Fourier multiplier tt*/lambda is obtained from the even scalar
Green kernel by one edge difference at each endpoint. The common
factor j_* and its axial-level independence do not change that
identity. Inversion about c is a valid grid inversion even when c
has a half-integer coordinate. Both matrices have zero axial rows
and independent identical color copies.

Apply this signed permutation to all four indices in the finite
tensor contraction. Covariance invariance and (9) give exactly

\[
 K_e^0:U_i^0:C^0=-K_e^0:U_i^0:C^0=0.                      \tag{10}
\]

Positivity of U_i^0 is unnecessary; the identity is bilinear in
the two invariant matrices. It keeps every connected pairing in
L149, rather than deleting the internal gradient pair.

### 4. Bound the actual complete response after that cancellation

All local index sets have a fixed size. L149 gives |K_e^0|<=C/a.
The smooth extension of u_a in L028 has uniformly bounded first
derivatives; its two endpoint values differ from u_a(c) by O(a).
The force/vector coefficients have one outside factor a^-1 and are
linear in those values. Thus |K_e-K_e^0|<=C. By (4),(8),(10),

\[
 \begin{split}
 |K_e:U_i:C|
 &\le |(K_e-K_e^0):U_i:C|
    +|K_e^0:(U_i-U_i^0):C|
    +|K_e^0:U_i^0:(C-C^0)|\\
 &\le C_i\bigl(a^2 a^{-1}
             +a^{-1}a^3 a^{-1}+a^{-1}a^2\bigr)
 \le C_i a.                                              \tag{11}
 \end{split}
\]

For either insertion subtraction in L149(7) the tensor entries
are bounded by C, without an outside a^-1. Its unchanged direct
bound is C_i a^2 a^-1=C_i a per local placement. There are
O(a^-4) supported edge, plaquette and vertex placements. Summing
(11) and these two signed insertion terms, and multiplying by
L149's exact connected factor twelve, proves (1).

In particular the cancellation removes only the fully frozen
force/vector contraction. Each of the three retained differences
in (11), and both insertion subtractions, is still cubic-bounded
after summation. No estimate here is little-o at that scale, and
no cancellation between these five sources is claimed. L149's
identity a^3 kappa=12 Z/a converts the bound to Z=O(a), not o(a).

The exact word-geometry check is reproducible with
`python3 scripts/combined-ward-response/check_quartic_residual_inversion.py`.
Its full certificate is
`scripts/combined-ward-response/quartic-residual-inversion-certificate.json`.
All 104 based-clover, incident-action and complete-stencil mappings
pass, with zero failures (required: zero), in all four central-edge
directions. This confirms the finite permutation geometry used in
(9); the analytic proof above supplies the covariance, smooth-column
and asymptotic bounds. The script is not a numerical preview of the
actual response or an independent verification of those estimates.

## Mathlib

Full matching coverage: **not checked**. Supporting finite Gaussian
pairing and lattice heat-kernel/projection coverage: **not checked**;
unknown coverage is not absence. The connected contraction is reused
from L149, the exact forest covariance from L085, and the heat-integral
argument from L114 with the necessary single-row bound proved above.
The new local specialization is justified rather than importing a
full-response finiteness claim from the inspected flow literature.
The saved source assessment
[quartic residual cubic scale](../drafts/literature/2026-10-12-quartic-residual-insertion-cubic-scale.md)
found no matching theorem for this isolated response. This local
improvement is not a certified originality claim or a solution.
