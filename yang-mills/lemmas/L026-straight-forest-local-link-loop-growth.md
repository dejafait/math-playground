# L026 — The straight-forest local link loop has linear path growth

## Hypotheses

Keep L025's fixed-mesh SU(2) Gaussian and its dimensionless exponential
coordinates x=theta/g=a A. The box is [-4,4]^4, a=8/N, and N is an
admitted even mesh. Choose specifically L003's direction-1 straight
forest F: at every interior transverse vertex triple, retain axial
edges with tails at levels 0,...,N-2, rooted at the lower face.
The axial edge at level N-1 is omitted from F. Links lying in the
physical boundary are fixed, and all boundary vertices are pinned.

Use ordinary stored-coordinate transposes and Euclidean norms. As in
L018, let D0,D1 be the unscaled relative incidence matrices and put

\[
\Delta=D_1^T D_1+D_0D_0^T,\qquad \Sigma=\Delta^{-1}.
\tag{1}
\]

For one color let z have the Hodge Gaussian covariance Sigma. L017's
path retraction, in these dimensionless coordinates, is

\[
R_Fz=z-D_0\phi_z,\qquad
\phi_z(j,v_2,v_3,v_4)=\sum_{\ell=0}^{j-1}
 z_1(\ell,v_2,v_3,v_4),\quad 1\le j\le N-1,
\tag{2}
\]

with phi_z zero at every boundary vertex. L018 identifies R_Fz with
the forest Gaussian inserted into full links, including its zero
forest entries. Its three color copies are independent.

Select a positive transverse edge e=(mu,v), mu in {2,3,4}, whose two
endpoints are interior, and write j=v1. For a plaquette p whose four
vertices are interior, let j denote its lower axial vertex level.
Let C_p be L025's twelve-dimensional signed-edge covariance; use its
ordinary operator norm. No action/probe tensor contraction is assumed
positive, and no nonlinear polynomial is transferred to the Hodge law.

## Conclusion

For each color and each selected transverse edge,

\[
\boxed{\frac j8\le \operatorname{Var}_F(x_e)\le j+8.}
\tag{3}
\]

More precisely its variance is the sum of a direct Hodge-link variance
bounded by 8 and a path-difference variance lying between j/8 and j.
For every selected plaquette,

\[
\boxed{\frac j8\le\|C_p\|_{\rm op}\le 4(j+9).}
\tag{4}
\]

Fix 0<delta<1/2 and restrict to plaquettes in a fixed compact interior
region whose axial coordinates lie between -4+8delta and 4-8delta.
For all sufficiently fine meshes their vertices are interior and
j>=delta N. Uniformly over these plaquettes,

\[
\delta/a\le\|C_p\|_{\rm op}\le32/a+32.
\tag{5}
\]

Thus the raw unflowed local loop in this particular forest is
Theta(a^(-1)), and a mesh-uniform O(1) matrix bound is false. This
does not establish growth or nonvanishing of K:C_p, of either pairing
class in L025, or of the complete response. Its tensor directions,
the external probe/residual contractions, and L019's cancellations
must still be considered. No cutoff-log coefficient, interacting
reflected-error bound <= c_box/2, continuum construction or mass gap
is established.

## Proof

### 1. Spectrum and the exact linear lift

L003's relative tensor-product decomposition gives a componentwise
Hodge Laplacian. A link component uses an edge coordinate in its own
direction and interior vertex coordinates in the other three. In
ordinary Euclidean normalization its one-dimensional modes are

\[
e_0(\ell)=N^{-1/2},\quad
e_k(\ell)=\sqrt{2/N}\cos(k\pi(\ell+1/2)/N),\quad
v_k(r)=\sqrt{2/N}\sin(k\pi r/N),
\tag{6}
\]

where edge indices k range from 0 to N-1 and vertex indices from
1 to N-1. The component eigenvalues are

\[
\lambda_k=4\sum_{r=1}^4\sin^2(k_r\pi/(2N)).
\tag{7}
\]

These are the dimensionless eigenvalues: (1) contains no 1/a^2.
L018's scaling of the a^4 cochain weight and x=a A makes Sigma,
rather than a rescaled inverse, the covariance. There are at least
three positive vertex indices, so Delta is positive definite.
Each component eigenvalue is at most 16. Consequently

\[
\Sigma\succeq \tfrac1{16}I.
\tag{8}
\]

There are no mixed component covariances because Delta is block
diagonal in the link directions. Gaussian independence follows.

The path sum (2) is the prescribed lower-root sum on interior
vertices, with the separately pinned upper face. Its differences
equal z1 on every forest edge of levels 0,...,N-2. Thus these axial
entries of R_Fz vanish. L018's exact covariance identification is

\[
R_F\Sigma R_F^T=I_F\Sigma_F I_F^T,
\qquad \Sigma_F=((D_1I_F)^T D_1I_F)^{-1}.
\tag{9}
\]

Only this linear Gaussian identity is used. The calculation makes
no replacement of L025's quartic vertex by an unmodified Hodge
polynomial.

### 2. A uniform bound on a direct Hodge-link variance

Every squared tensor-product wave in (6) is at most 16/N^4.
The elementary sine inequality sin(u)>=2u/pi on [0,pi/2] gives
lambda_k>=4|k|^2/N^2. For any stored link in any direction,

\[
\Sigma_{ee}\le\frac4{N^2}
 \sum_{\substack{0\le k_\mu\le N-1\\
                  1\le k_r\le N-1\ (r\ne\mu)}}\frac1{|k|^2}.
\tag{10}
\]

Count the indices with max_r k_r=m. There are exactly
(m+1)m^3-m(m-1)^3=4m^3-3m^2+m, at most 4m^3, for
1<=m<=N-1. Every such index has |k|^2>=m^2. Therefore

\[
\Sigma_{ee}\le\frac{16}{N^2}\sum_{m=1}^{N-1}m
=8(1-1/N)\le8.
\tag{11}
\]

This bound includes the constant edge mode. No infinite-volume
replacement or asymptotic sum is used.

### 3. Two-sided bound on the path-difference variance

For a selected transverse edge, both path endpoints are interior,
so (2) gives the exact identity

\[
(R_Fz)_\mu(v)=z_\mu(v)-
 \sum_{\ell=0}^{j-1}
 \big[z_1(\ell,v_\perp+\widehat\mu)
      -z_1(\ell,v_\perp)\big].
\tag{12}
\]

Let w be the coefficient vector of the sum on the component-1 link coordinates.
Its 2j entries have magnitude one and are all distinct, hence
||w||^2=2j. Equation (8) gives

\[
w^T\Sigma_1w\ge(2j)/16=j/8.
\tag{13}
\]

Here Sigma1 is the component-1 block of Sigma. For the upper bound,
let T be the transverse unscaled differential in direction mu on
component-1 links, mapping to the relative (1,mu) plaquette space;
choose its sign so that it is the difference in (12). The tensor
decomposition yields

\[
T^T T\preceq\Delta_1.
\tag{14}
\]

Let b have value one on the j (1,mu) plaquettes with axial edges
at levels 0,...,j-1 and the fixed transverse edge location, and zero
elsewhere. These are valid relative plaquettes even at level zero;
no component-1 link on a transverse face is included. Then
w=T^T b and ||b||^2=j. Multiplying (14) on both sides by
Sigma1^(1/2) shows that T Sigma1 T^T has operator norm at most one:
the squared norm of T Sigma1^(1/2) is at most one, and its product
with its transpose has the same norm. Therefore

\[
w^T\Sigma_1w=b^TT\Sigma_1T^Tb\le\|b\|^2=j.
\tag{15}
\]

The component z_mu(v) and the entire component-1 path sum are
independent. Their covariance is zero exactly, rather than bounded
by an inequality. Add their variances in (12), use (11), (13) and
(15), and transfer the linear covariance by (9). This proves (3).

### 4. The actual local loop matrix

For one color let C_p^(1) be the four-by-four covariance of L025's
signed traversal entries. Traversal signs leave the diagonal entries
unchanged. Every interior plaquette has a transverse edge at level
j or j+1. Thus (3) and positivity give
||C_p^(1)||>=max_e (C_p^(1))_(ee)>=j/8.

If the plane contains direction 1, its two axial edges are forest
edges: their levels are j<=N-2 since all four vertices are interior.
Their variances are zero. The remaining transverse edges occur at
levels j and j+1. If the plane is purely transverse, all four edges
are transverse at level j. In either case each nonzero diagonal
is at most j+9, and

\[
\|C_p^{(1)}\|_{\rm op}\le\operatorname{Tr}C_p^{(1)}
\le4(j+9).
\tag{16}
\]

After permutation of coordinates, C_p is the direct sum of three
identical C_p^(1), because the colors are independent with the same
covariance. Its operator norm equals that of a single block, giving
(4). Interior levels satisfy j<=N-1; the compact-support condition
gives j>=delta N. Substituting N=8/a into (4) proves (5).

### 5. Verification and the remaining contraction question

Run
`OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_straight_forest_loop.py`.
The script builds independent relative vertex, link and plaquette
incidence matrices, inverts both the Hodge and forest Hessians, and
checks (9). At N=4 it checks all 162 interior transverse edges and
216 interior plaquettes against (3) and (4), as well as (12)'s
variance decomposition and the path row norm. The N=2 test has no
such interior edges/plaquettes and checks only the lift and spectrum;
it is not counted as an edge or plaquette verification. These small
meshes test the geometry and do not assert admission of the supported
Ward-generator stencil.

Independent tensor-mode evaluations at N=4,8,16,32 sample a
direction-2 edge with tail (N/2,N/2,N/2,N/2). Its variances are
approximately 0.74894, 1.43339, 2.76923 and 5.43645, inside the
respective required intervals [0.25,10], [0.5,12], [1,16], [2,24].
The N=4 dense/spectral difference is about 1.1e-15. The full
certificate is `scripts/combined-ward-response/straight-forest-loop-certificate.json`;
the complete checks field was inspected, with seven passed checks
and no failures. The finite samples are normalization checks;
the analytic proof, not their trend, establishes (3)–(5).

The bounded attempt rules out an O(1) bound on raw C_p in this forest.
It does not rule out a bound after applying K, summing plaquettes,
or combining L011's other terms. In particular the matrix lower
bound cannot be inserted into L025's signed tensor contraction as
a lower bound for either probe response. L019 still requires the
nonlinear observable/residual jets in cancellations. Investigating
the growing path directions inside the normal-ordered quadratic
coefficient 6 K_(alpha beta gamma delta) (C_p)_(gamma delta), together
with the other pairing class, remains a quantitative contraction
question within the unchanged approved full-response target.

## Mathlib

Coverage of the full specialized forest-loop growth statement:
**not checked**. Coverage of the supporting finite Gaussian
covariance, incidence, spectral order and norm inequalities:
**not checked**. No matching Mathlib theorem is asserted.

This is local REPRODUCTION of the established linear Gaussian and
relative-spectrum machinery in the actual forest convention, not
a novelty claim. The tree-map precedent is Freidel–Livine,
[hep-th/0205268v2](https://arxiv.org/pdf/hep-th/0205268v2), section 2.1,
(2.1)–(2.8), as specialized in L017. No ultraviolet estimate is
imported from that source. The precise primary citations and their
renormalization qualifications remain in
`drafts/literature/2026-09-26-current-target.md`; none assigns a value
to this partial action contribution or the complete logarithm.
The explicit bound is needed because the radial curvature projection
estimate does not control L025's unflowed forest-link loop.
