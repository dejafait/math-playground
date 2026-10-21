# L114 — The moved trace's finite-projection boundary error is subcubic

## Hypotheses

Use exactly L113(8), both actual L010 probes i=3,6, SU(2), the straight
lower-rooted direction-1 forest, all-face relative fixed-link box
(-4,4)^4, sufficiently fine admitted even N, a=8/N and tau=1/16.
Take the bare small-coupling coefficient at fixed mesh before refinement.
All coordinates and norms are ordinary stored ones. Retain every axial
level, transverse end row, both generator orientations, both exterior
coefficient levels and every exterior heat mode. Import L111's exact
infinite stencils, compact displacement coefficients and energy E_j,
and L113's S_alpha and clamped scalar coefficients phi_(k,alpha,t).

Let J_0 and J_1 extend the finite transverse interior vertex and
relative edge spaces by zero into their respective arrays on Z^3.
Write J_2=J for L111's plaquette extension. Let T_inf be the
dimensionless full-grid gradient with the sign convention of L085,
Delta_inf=T_inf^* T_inf, and define the bounded orthogonal projection

    P_inf(theta)=t(theta)t(theta)^*/lambda(theta),
    t_nu=exp(i theta_nu)-1, lambda=sum_(nu=2)^4 |t_nu|^2.   (1)

Its value at theta=0 is immaterial. The overall gradient sign cancels
in (1). Set P_bulk=J_1^* P_inf J_1 on the finite relative edge space.
This is a compression, not generally an orthogonal projection there.

## Conclusion

For any collection Omega_N of at most C_0 N^3 finite edge rows whose
endpoints have distance at least delta N from all transverse faces,
with fixed delta>0,

    ||R_Omega (P-P_bulk)||_HS <= C_delta (log N)^(3/4).     (2)

Here R_Omega is the diagonal edge-space selector onto Omega_N.
Constants may depend on delta, C_0 and the fixed data, but not on N
or the heat labels.
Only output rows are restricted; every finite boundary input edge
remains. No small operator norm is asserted.

In L113(5) replace only P by P_bulk, defining

    Z^sc,bulk_(kl;st)=a^2 sum_(alpha,beta) S_alpha^T P_bulk
          M^1_(phi_(l,alpha,s) phi_(k,beta,t)) S_beta.

Use this replacement in L113(8) to define R_bulk,sc,Pbulk, with its
unchanged X_(t,t-s), outside a^-1 and weights. Then

    |R_bulk,sc-R_bulk,sc,Pbulk|
                      <= C_i N^(5/2) (log N)^(3/4)=o(N^3),
    a^3 (R_bulk,sc-R_bulk,sc,Pbulk) -> 0, i=3,6.           (3)

The displacement localizes the columns of X S_alpha^T, not the
output of X. No boundary input is discarded or exterior coefficient
frozen. This controls one remaining boundary comparison; it supplies
no cubic bound for the surviving trace, finite transverse H limit,
coefficient value or complete-group compensation. L110/L111/L113's
O(N^3) errors remain and may contribute at cubic scale. The other
unevaluated functionals, response jets, finer powers/logarithm,
matching, interacting error <=c_box/2, continuum axioms, reflection
positivity, infrared control and finite positive mass remain open.

## Proof

### 1. Identify the projection difference with its exact relative domains

The finite vertices are {1,...,N-1}^3, with zero boundary values.
Every edge with an interior endpoint is a retained relative edge,
including normal end edges. An omitted tangential boundary edge has
two zero endpoint values. Consequently, on every full-grid edge,

    T_inf J_0=J_1 T,
    Delta_0=T^T T=J_0^* Delta_inf J_0.                    (4)

The second identity is the scalar Dirichlet Laplacian, including its
endpoint diagonal 2 in each coordinate. Equation (4) does not impose
Dirichlet conditions on edge components. Transposing its first identity
and using P=T Delta_0^-1 T^T gives

    P=J_1^* T_inf J_0 Delta_0^-1 J_0^* T_inf^* J_1.

The finite spectral theorem and Fourier Plancherel give the projection
difference as the strong heat integral

    P-P_bulk=integral_0^infinity I_v dv,
    I_v=J_1^* T_inf [J_0 exp(-v Delta_0)J_0^*
                         -exp(-v Delta_inf)] T_inf^* J_1.       (5)

For the infinite term, integration to V has multiplier
(tt^*/lambda)(1-exp(-V lambda)), which converges strongly to (1)
by bounded dominated convergence. An unbounded infinite inverse is
never applied as an l2 operator. The estimates below prove absolute
Hilbert--Schmidt integrability after the output restriction in (2),
and therefore justify that restriction of (5) in the stronger norm.

### 2. Compare the scalar heat walks on interior output vertices

The matrix exp(-v Delta_0) is the nearest-neighbor continuous-time
walk with rate one in each signed coordinate, killed on reaching a
boundary vertex. Its zero extension and exp(-v Delta_inf) have
nonnegative entries and row and column sums at most one. Couple their
proposals from an interior vertex until the first boundary visit.
The l1 distance of their terminal rows, over every full-grid input
vertex, is at most twice the probability of that visit by time v.

Use L112's proof of the diffusive maximal-displacement bound: the
one-coordinate martingale exp(eta X(w)-2w(cosh eta-1)), Doob's
maximal inequality and eta=min(1,R/(4v)) give
Pr{sup_(w<=v)|X(w)|>=R}<=2 exp[-c min(R,R^2/v)].
The same clocks apply here, with three coordinates and no reflected
coordinate. Union over the three coordinates and put R=c_delta N.
Thus for output vertices a fixed physical distance inside the box,
the row l1 difference is bounded by

    C exp[-c_delta min(N,N^2/v)].                         (6)

The column l1 difference is at most 2 without any input restriction.
The Schur test yields the corresponding localized operator bound
C exp[-c'_delta min(N,N^2/v)]. The endpoints of Omega_N lie in
such an interior vertex set. T_inf samples just those endpoints and
has bounded dimensionless norm; T_inf^* J_1 has bounded norm too.
The rank of R_Omega I_v is at most C_0 N^3, even though the scalar
comparison included infinite input vertices. Therefore

    ||R_Omega I_v||_HS
          <= C N^(3/2) exp[-c'_delta min(N,N^2/v)].        (7)

This bound keeps all input edges after the final J_1 restriction.

### 3. Retain both gradients in the full-spectrum long-time tail

The finite gradient heat sandwich has squared Hilbert--Schmidt norm
exactly

    ||T exp(-v Delta_0) T^T||_HS^2
                              =Tr(Delta_0^2 exp(-2v Delta_0)).    (8)

This follows either by cyclicity or from the isometry
T Delta_0^-1/2. Its full spectrum, imported from L085/L113, is
lambda_m=4 sum_(nu=2)^4 sin^2(pi m_nu/(2N)), 1<=m_nu<N.
On a shell r=max m_nu, 4r^2/N^2<=lambda_m<=3 pi^2 r^2/N^2,
and there are at most 3r^2 labels. For v>=1,

    Tr(Delta_0^2 exp(-2v Delta_0))
       <= C N^-4 sum_(r>=1) r^6 exp(-c v r^2/N^2)
       <= C N^3 v^(-7/2).                               (9)

For completeness, sum r^6 exp(-c x r^2)<=C x^(-7/2) for all x>0:
when x<=1 put L=ceil(x^-1/2) and group r in intervals
[kL,(k+1)L). Each interval contributes at most
L^7 (k+1)^6 exp(-c k^2), since x L^2>=1. Their sum is at most
C L^7<=C' x^(-7/2). When x>=1,
extract exp(-cx/2), dominate the remaining sum by its value at x=1,
and use exp(-cx/2)<=C x^(-7/2). This includes times beyond N^2
and every low physical mode, rather than truncating the spectrum.

For a component row of the infinite sandwich, Fourier Plancherel
and ||tt^*||_F^2=lambda^2 give

    row_l2_norm_squared <= C integral_([-pi,pi]^3)
                                lambda^2 exp(-2v lambda) dtheta
                         <= C v^(-7/2), v>=1.           (10)

Indeed c|theta|^2<=lambda<=|theta|^2, and the radial majorant is
C integral_0^infinity r^6 exp(-cv r^2)dr. Summing (10) over the
O(N^3) output rows and retaining the finite input restriction gives
the same square-root bound as (9). By the triangle inequality,

    ||R_Omega I_v||_HS<=C N^(3/2) v^(-7/4), v>=1.         (11)

Keeping both gradients is essential for the integrable exponent.

### 4. Integrate and obtain the localized projection estimate

Fix A large enough that c'_delta A>=6, and let
V=N^2/(A log N). For sufficiently large N, V>=1 and
min(N,N^2/v)>=A log N throughout 0<v<=V. Equation (7) gives

    integral_0^V ||R_Omega I_v||_HS dv
                       <= C N^(3/2) V N^-6 <= C.

Equation (11) gives

    integral_V^infinity ||R_Omega I_v||_HS dv
                 <= C N^(3/2) V^(-3/4)
                  = C A^(3/4) (log N)^(3/4).

Minkowski's integral inequality proves (2) and the promised absolute
convergence of the localized integral (5). The cutoff is an explicit
bound on this heat integral, not a substitution into a fixed-mass
limit theorem. No projection operator-norm approximation is used.

### 5. Place the estimate on the actual compact columns in L113's trace

Write psi_(kl;alpha,beta;st)=phi_(l,alpha,s) phi_(k,beta,t).
Its supremum is at most C p(k)p(l) by L113(3). Each summand of
X_(t,j) S_alpha^T ends with

    M_(b_(r,t)) J_2 S_alpha^T.

The multiplication is on plaquette indices. By L111's compact smooth
displacement support and S_alpha's fixed range, a nonzero column of
this product has edge index within a fixed stencil range of that
support. Choose one Omega_N containing those columns for all r,t,alpha.
For sufficiently fine meshes its endpoints are at distance delta N
from all transverse faces and its size is O(N^3). Consequently,
exactly

    X_(t,j) S_alpha^T=X_(t,j) S_alpha^T R_Omega.           (12)

Here R_Omega is understood as the edge-space diagonal selector when
composed on that same finite space. Equation (12) transfers compact
input support to the projection's output rows; it says nothing about
support of X's output. No exterior scalar or filter has crossed a
projection in this identity.

L111(8) gives W_j<=C(1+|j|)^(-5/2) with sum_j W_j<infinity.
L113(18), obtained by counting all finite output rows, gives

    ||X_(t,j) S_alpha^T||_HS<=C N^(3/2) W_j.              (13)

Its proof retains every input row before restriction; the bounded
norm of S_alpha only changes C. Cyclic rectangular trace identities,
(12), trace Cauchy--Schwarz, (2) and bounded ||S_beta|| yield

    |Tr[X_(t,j) S_alpha^T (P-P_bulk) M^1_psi S_beta]|
       <= C p(k)p(l) N^(3/2) W_j (log N)^(3/4).          (14)

Both levels in psi remain distinct. Summing the fixed path labels,
the a^2 in Z, the outside a^-1, and the exact axial weights uses

    sum_(s,t=1)^(N-1) min(s,t) W_(t-s)
                                      <= N^2 sum_(j in Z) W_j.

Finally sum every exterior heat label with
sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i from L111. The full error is

    C_i a N^(7/2) (log N)^(3/4)
       =8 C_i N^(5/2) (log N)^(3/4).

This proves (3), including its zero a^3 limit. Both generator
orientations are already retained in the imported trace; the complete
other/other outside factor 3 is not introduced again. A fixed factor
would preserve the zero scaled error.

### 6. Scope of the advance

L112 compares the four-dimensional circulation energy covariance.
The present comparison concerns the separate three-dimensional middle
gradient projection, in its actual moved-trace placement. Its heat
exponent and compact-column identity required the specialization above.
The established result is local standard-method progress, classified
REPRODUCTION under the unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`;
it is not a novelty claim beyond the checked sources. No general
Ward/flow finiteness theorem is applied to this isolated bare group.

The surviving trace still contains finite compressions, the full path
filters, both scalar coefficient levels and their placement relative
to E_j. Those require controlled comparisons before using any joint
frozen cancellation. In particular (3) does not discard the earlier
cubic errors, prove a finite H limit, evaluate the other functionals
or compare the complete contribution with -12 gamma D_i. Any later
numerical comparison retains L084/L082's IEEE qualifications.

## Mathlib

Full matching projection-boundary trace theorem: **not checked**.
Supporting spectral heat identities, Fourier Plancherel, Doob maximal
inequality, Schur test, Minkowski integral inequality and finite
Hilbert--Schmidt trace estimates: **not checked**. Unknown availability
is not absence. The standard named results are used in the explicit
forms above; L112 supplies the already proved walk estimate.
