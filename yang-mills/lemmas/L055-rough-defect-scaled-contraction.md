# L055 — A scaled limit for the rough full-curvature defect contraction

## Hypotheses

Keep L054's actual SU(2) straight-forest Gaussian, both original
probes i=3,6, tau=1/16, a=8/N through admitted even meshes and every
upper transverse edge, including pinned end edges. Take the
small-coupling coefficient at each fixed mesh before a tends to zero.
Use its one-color vertex matrices

\[
 U=JSBSJ^T,\qquad V=JSASJ^T=N R_a,\qquad
 R_a=G\bar A G,\quad G=(T^T T)^{-1},
 \qquad D_0=b_N(\Delta_T)(I-P),\quad P=TGT^T.
\]

Vertex rows at pinned endpoints are zero. Orient an edge of direction
mu from v to v+e_mu, with (T h)_e=h(v)-h(v+e_mu), and put
(M h)_e=(h(v)+h(v+e_mu))/2. Use Phi from L051(2) with D_0
in place of D. Let K_i be precisely L045(1)'s smooth one-color
continuum kernel, and set

\[
 E_{i,\mu\nu}(x)=
   \left.\partial_{x_\mu}\partial_{y_\nu}K_i(x,y)\right|_{y=x}.
\]

Thus E_(i,mu,mu)=E_(i,mu) in L045. Let bar u and
w_mu=partial_mu bar u_mu be L042/L045's continuum compressed
displacement and diagonal strain on D_perp=(-4,4)^3. In particular
sum_mu w_mu=0. All transverse labels are mu=2,3,4.

## Conclusion

Use normalized torus measure dtheta/(2 pi)^3 on [-pi,pi]^3 and define

\[
 \lambda_\mu=2-2\cos\theta_\mu,\quad
 \lambda=\lambda_2+\lambda_3+\lambda_4,\qquad
 b_\infty(\lambda)=\frac{\sqrt{\lambda(\lambda+4)}-\lambda}{2},
\]
\[
 d_*:=\frac1{32}\int
 b_\infty(\lambda)
 \frac{\lambda_4(4+\lambda_4)(\lambda_2-\lambda_3)^2}{\lambda^3}
 \frac{d\theta}{(2\pi)^3}>0.                         \tag{1}
\]

The value at the single point theta=0 is immaterial. Then

\[
 \boxed{\lim_{a\downarrow0} a^2\Phi_{D_0}(U,V)
   =-16d_*\int_{D_\perp}\sum_{\mu=2}^4
                       E_{i,\mu\mu}(x)w_\mu(x)\,dx.}   \tag{2}
\]

Consequently the contribution -6 Phi_D0(U,V) in L054(8)
has scaled limit +96 d_* times the displayed physical integral.
Neither that integral's sign nor the complete group limit is evaluated
here. L054's three K sums and the remaining mixed Omega term are
still present. This does not establish compensation of L047,
subleading powers or logarithms, the full response, finite matching,
the interacting reflected error <=c_box/2, continuum fields, full
reflection positivity or a finite positive physical mass.

## Proof

### 1. An exact gradient-annihilating contraction identity

For a symmetric edge matrix D with DT=0 and symmetric vertex matrices
U,V, one has at every finite mesh

\[
 \Phi_D(U,V)=2\sum_{e,h} D_{eh}(TUT^T)_{eh}(MVM^T)_{eh}. \tag{3}
\]

To verify the normalization, first set U=hh^T and take a formal
mean-zero vertex field xi with covariance V. If V is positive
semidefinite it can be an actual Gaussian. L053(5)–(6), or direct
expansion of its four terms, gives

\[
 \Phi_D(hh^T,V)=\tfrac12 E\langle B_h\xi,D B_h\xi\rangle,
 \qquad (B_h\xi)_e=h(v)\xi(v')-h(v')\xi(v).
\]

The exact identity B_h xi=-T(h xi)+2(Th)M xi and DT=0 reduce this
to the right side of (3). Every real symmetric U is a signed sum
of hh^T by its spectral decomposition. Every symmetric V is a
difference of positive semidefinite matrices. Bilinearity therefore
proves (3) for the actual, possibly indefinite U,V. This also proves
(3) at pinned endpoints; no boundary row is removed. It applies both
to D_0 and to the approximants used below.

### 2. Uniform finite-range approximation of the full defect

L050(2) gives, with gamma=2 arsinh(sqrt(lambda)/2),

\[
 b_N(\lambda)-b_\infty(\lambda)
   =\frac{2\sinh\gamma}{e^{2N\gamma}-1},\qquad
 0\le b_N(\lambda)-b_\infty(\lambda)\le\frac1N.       \tag{4}
\]

For the inequality use
e^(2N gamma)-1=2e^(N gamma)sinh(N gamma) and
sinh(N gamma)>=N sinh(gamma) for integer N>=1. The latter follows
inductively from the addition formula and cosh(gamma)>=1.
At lambda=0 the continuous extension of the difference is 1/N.
All transverse Laplacian eigenvalues lie in [0,12].

The continuous function b_infinity on [0,12] vanishes at zero.
The standard Weierstrass approximation theorem supplies, for every
epsilon>0, a real polynomial q with q(0)=0 and
sup_[0,12]|q-b_infinity|<=epsilon: approximate to epsilon/2 and
subtract the approximating polynomial's value at zero. Define

\[
 D_q=q(\Delta_T)(I-P)
     =q(\Delta_T)-p(\Delta_T)TT^T,\qquad p(z)=q(z)/z. \tag{5}
\]

Here p is a polynomial because q(0)=0. For the equality in (5),
use Delta_T T=T(T^T T) and Delta_T^(-1)TT^T=P, proved in L050.
Thus D_q is symmetric, annihilates T and has a fixed finite range
in lattice steps. This is valid on the actual relative edge space,
not merely on the infinite lattice. Spectral calculus and (4) give

\[
 \|D_0-D_q\|\le\epsilon+1/N.                       \tag{6}
\]

The error estimate needed for the scaled contraction is uniform:

\[
 a^2|\Phi_{D_0-D_q}(U,V)|\le C_i(\epsilon+1/N).     \tag{7}
\]

Here is its full-spectrum justification. L054(10) proves
-cC<=V<=cC with C=NG, so V=C^(1/2)R_V C^(1/2), ||R_V||<=c.
Expand U in L054(13)'s absolutely heat-weighted deterministic
exterior columns h_k h_l^T. Their sup norms and first edge
differences are bounded by p(k) and a p(k). For a rank-two term,
(3), symmetry and Hilbert–Schmidt Cauchy–Schwarz bound its pairing
with an arbitrary symmetric gradient-annihilating edge matrix E by a constant times

\[
 \|E\|\|\operatorname{diag}(Th_k)MC^{1/2}\|_{HS}
          \|\operatorname{diag}(Th_l)MC^{1/2}\|_{HS}.
\]

Each squared norm is at most a² p(k)² Tr(MCM^T).
L053(12) proves Tr(MCM^T)<=18N^4, including end edges.
Summing the complete heat weights gives C_i ||E|| a²N^4.
Multiply by a² and use aN=8 to get (7). This argument uses the
whole rough covariance and no cutoff on its internal modes.

### 3. Fixed-offset limits of the rough residual kernel

For every fixed pair of lattice offsets s,t and every compact
physical interior K, uniformly for x_v in K,

\[
 (R_a)_{v+s,v+t}\longrightarrow
 r_{M(x_v)}(t-s):=
 \int e^{i\theta\cdot(t-s)}
        \frac{\sigma_{M(x_v)}(\theta)}{\lambda(\theta)^2}
                           \frac{d\theta}{(2\pi)^3},           \tag{8}
\]
\[
 \sigma_M(\theta)=\frac14\sum_j w_j
                       \lambda_j(\lambda-\lambda_j).          \tag{9}
\]

Equation (9) is exactly L042(5)'s frozen trace-free residual,
with M_jk=partial_j bar u_k and w_j=M_jj. No off-diagonal strain
has been dropped; L042's stencil calculation cancels it.

To justify (8), use the monopole g_s with Fourier transform
exp(-i theta.s)/lambda in the discrete energy completion.
L045's proof, section 1, establishes its finite energy and identifies
the translated pinned Green column G delta_(v+s) as its orthogonal
energy projection onto the translated finite interior. For fixed
s,t these columns converge in energy uniformly on K: each fixed
finite-support approximation fits inside every such translated cube
for sufficiently small a. L041/L042's uniform bilinear form bound
|<f,bar A h>|<=C||f||_E||h||_E controls replacement of each column
by a finite-support approximation. For those two fixed finite
supports, L042's Taylor argument makes the actual residual stencil
converge uniformly to A_(M(x_v)). Its form has the same energy
bound. Replace the approximations back by g_s,g_t and let their
energy errors tend to zero. This proves (8), with no l² monopole
assumption and no interchange of an uncontrolled rough-mode sum.
Fourier transformation gives its displayed integral; it is absolutely
integrable since |sigma_M|<=C lambda and 1/lambda is integrable
in dimension three. In fact the trace-free formula is O(lambda²).

The same energy bound and the global Green diagonal bound give
|(R_a)_vw|<=C on the whole finite cube, including zero pinned rows.
This will control the physical boundary collars.

### 4. Pass to the scaled limit for each finite-range approximant

The full vertex block U is precisely the sampled kernel K_(i,a)
of L045(9). Indeed every upper vertex covariance column in Hodge
coordinates is sqrt(N)E_0G delta_v. Compressing the two probe
legs, including their heat factors, gives
U=N G h_3 bar Q_i h_3 G, by the calculation in L040(5) for
arbitrary vertex evaluation rows. Thus L045's C^r convergence
K_(i,a)->K_i applies to the entire block, not just its diagonal.
In particular, for fixed offsets and directions mu,nu,

\[
 a^{-2}(TUT^T)_{(v,\mu),(v+z,\nu)}
       \longrightarrow E_{i,\mu\nu}(x_v)              \tag{10}
\]

uniformly on compact interiors. Apply the fundamental theorem of
calculus in each kernel argument to obtain (10); both incidence
signs are negative, so their product has positive sign. The same
formula gives |TUT^T|<=C_i a² globally, including end edges.

Fix q. Its operator (5) agrees with the infinite-lattice finite
stencil on every row farther than its fixed range from the pinned
faces. By (3), V=N R_a and aN=8,

\[
 a^2\Phi_{D_q}(U,V)
 =16a^3\sum_{e,h}(D_q)_{eh}
                  \frac{(TUT^T)_{eh}}{a^2}(MR_aM^T)_{eh}. \tag{11}
\]

Only a fixed finite set of offsets h-e contributes. On a fixed
physical delta-interior, (8) and (10) are uniform. Therefore their
a³ Riemann sum tends to

\[
 16\int_{D_\perp}\sum_{\mu,\nu}
                   E_{i,\mu\nu}(x)\mathcal L^q_{\mu\nu}(x)\,dx,
                                                                  \tag{12}
\]

where L^q is the finite stencil contraction with the endpoint-
averaged frozen kernel r_M. For completeness, the omitted collar
and end-edge rows number at most C_q(delta a^-3+a^-2). Their
summands in (11), apart from the factor a³, are bounded by C_(i,q)
using the global R bound, the global bound in (10), bounded stencil
entries and a fixed number of neighbors per row. The collar
contribution is at most C_(i,q)(delta+a). First let a tend to zero
and then delta tend to zero. This proves (12) with all retained
boundary rows; it assumes no translation invariance at the faces.

To evaluate L^q, use edge-midpoint Fourier coordinates. The
incidence multiplier is -2i sin(theta_mu/2), and the endpoint
average multiplier is cos(theta_mu/2). The midpoint symbol of
P has entries 4 sin(theta_mu/2)sin(theta_nu/2)/lambda.
Consequently Parseval for the finite stencil yields

\[
 \mathcal L^q_{\mu\nu}(x)=\int q(\lambda)
 \left(\delta_{\mu\nu}
       -\frac{4\sin(\theta_\mu/2)\sin(\theta_\nu/2)}\lambda\right)
 \cos(\theta_\mu/2)\cos(\theta_\nu/2)
 \frac{\sigma_{M(x)}(\theta)}{\lambda^2}
                              \frac{d\theta}{(2\pi)^3}.        \tag{13}
\]

One may equivalently anchor all components at vertices: the matching
edge phases in D_q and MR_aM^T cancel in their entrywise contraction.
Thus (13) does not impose an extra half-grid assumption. The frozen
kernel is real symmetric; the Parseval product is the symbol of D_q
times the conjugate kernel symbol, which is real in midpoint
coordinates.

### 5. Remove the approximation and evaluate the tensor

Choose q with epsilon tending to zero. The matrix in parentheses
in (13) is an orthogonal projection and the cosines have modulus
at most one. Since sigma_M/lambda² is absolutely integrable
uniformly for bounded M, replacing q by b_infinity changes each
integral by at most C epsilon. Equation (7) then proves that (12)
holds for the actual D_0 with L^infinity in place of L^q. More
explicitly, for each epsilon the limsup scaled difference from
(12) is at most C_i epsilon; the limiting integrals converge as
epsilon tends to zero. This establishes a limit of the full
untruncated nonlocal contraction without assuming summable
pointwise defect kernels.

For mu!=nu, (13) with b_infinity is odd separately in theta_mu
and theta_nu, while (9) and the other weights are even. Hence its
integral is zero. For the diagonal mu=2 it is

\[
 \mathcal L^\infty_{22}(x)=\frac14\int
 b_\infty(\lambda) f_\lambda(\lambda_2)
 \frac{\sum_jw_j(x)\lambda_j(\lambda-\lambda_j)}{\lambda^2}
                 \frac{d\theta}{(2\pi)^3},
 \quad f_\lambda(z)=(1-z/\lambda)(1-z/4).            \tag{14}
\]

The coefficients of w_3,w_4 agree by their coordinate swap. Since
sum_j w_j=0, (14) equals chi w_2, with

\[
 \chi=\frac14\int b_\infty(\lambda)f_\lambda(\lambda_2)
             \frac{(\lambda_2-\lambda_3)\lambda_4}{\lambda^2}
                        \frac{d\theta}{(2\pi)^3}.
\]

Swap coordinates 2 and 3 and average the two expressions. Using

\[
 f_\lambda(x)-f_\lambda(y)
       =-\frac{(x-y)(4+\lambda_4)}{4\lambda}
       \quad\text{when }x=\lambda_2,\ y=\lambda_3
\]

gives chi=-d_* with exactly (1)'s factor 1/32. Permuting the
directions proves L^infinity_(mu,mu)=-d_* w_mu for all three mu.
Near zero the nonnegative integrand in (1) is O(|theta|), because
b_infinity=O(sqrt(lambda)), lambda_4<=lambda and
|lambda_2-lambda_3|<=lambda. Away from zero it is bounded. It is
strictly positive on an open set with lambda_4>0 and
lambda_2!=lambda_3. Thus 0<d_*<infinity. Substituting the diagonal
tensor into (12) proves (2), including its sign and factor 16.

### 6. Verification, applicability and remaining terms

The finite identities (3), (5) and the exact scaling (11) hold for
arbitrary admitted meshes. The uniform error (7), the bilinear
energy argument (8), and the collar estimate justify all limits.
The Fourier parity and coordinate-swap calculations evaluate the
whole frozen tensor, including every direction and frequency.
No numerical evidence or new mathematical script is needed.

This is local standard-method reproduction under the unchanged
SPECIALIZE assessment `drafts/literature/2026-09-26-current-target.md`.
The standard named Weierstrass approximation theorem is imported;
its application is to the continuous scalar symbol on the compact
interval [0,12]. Gaussian contraction, spectral calculus and energy
projection are reused in the exact local forms cited above.
General flow renormalization and stress matching are not reproved
or extended to physical boundaries. The finite-range approximation
is necessary because L050's low-mode estimate does not cover the
rough block V and L045 alone treats only finitely separated entries.

In L054(8), Phi_D0(C,W_+) is O(1). Its K_BA^d term and four
Omega types are o(a^-2) by the displayed bounds there. The remaining
K_B^d delta(C,V), K_A^d delta(C,U) and
Omega(H_B^d,H_0;V) terms still have only O(a^-2) bounds. Equation
(2) evaluates none of them. They may compensate or reinforce it.
The O(a^-1) remainder in L054(9) also remains relevant to the
logarithm. No sign is assigned to the physical integral in (2),
and no complete group or Ward-response coefficient is inferred.

## Mathlib

Coverage of the complete specialized scaled-limit result: **not checked**.
Coverage of supporting Weierstrass approximation, real symmetric
spectral calculus, finite Gaussian contraction, energy completion,
Fourier transformation and Riemann sums: **not checked**. No matching
Mathlib theorem or machine verification is asserted. The precise
local inputs used are L040–L042, L045, L050–L051 and L053–L054. Unknown coverage
is not evidence of absence.
