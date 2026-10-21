# L045 — The selected companion has a finite a²-scaled functional

## Hypotheses

Keep L040–L044's exact SU(2), fixed all-face box, lower-rooted straight
forest, two original probes i=3,6 and tau=1/16. Take the small-coupling
coefficient at fixed mesh first, then a=8/N tends to zero through the
admitted meshes. Retain every selected upper (1,mu) plaquette, all three
colors and all transverse pinned end edges. All matrices below are
ordinary dimensionless matrices on transverse interior vertices.

Write Delta=Delta_3, G=Delta^(-1), A=bar A,
P_i=G h_3 bar Q_i h_3 G and R=G A G. Use L043's fields
F_(i,a)(v)=N(P_i)_vv and Z_a(v)=N R_vv, zero at pinned vertices.
Let bar u be L042's smooth continuum compressed displacement on
D_perp=(-4,4)^3, and w_mu=partial_mu bar u_mu, so sum_mu w_mu=0.
The mesh-dependent bar w_(mu,a) are L040(9)'s exact central strains,
not these continuum derivatives. They converge in each fixed C^r
norm to w_mu by L042's coefficient argument. Let c_*>0 be exactly
L042(2)'s torus integral.

For transverse labels k=(k_2,k_3,k_4) with each k_mu>=1, put
psi_k(x)=product_(mu=2)^4 [(1/2)sin(pi k_mu(x_mu+4)/8)],
lambda_k=(pi/8)^2|k|² and b_k=psi_k/sqrt(lambda_k).
Let beta_(i;k,l) be the matrix element of L008's one-color continuum
relative form B_i between the component-1 modes with axial index zero
and transverse indices k,l. These modes are 8^(-1/2)psi_k in component
1. Define the symmetric real kernel

\[
 K_i(x,y)=8\sum_{k,l}e^{-\tau(\lambda_k+\lambda_l)}
                \beta_{i;k,l}b_k(x)b_l(y),\quad
 F_i(x)=K_i(x,x),\quad
 E_{i,\mu}(x)=\left.\partial_{x_\mu}\partial_{y_\mu}
                        K_i(x,y)\right|_{y=x}.             \tag{1}
\]

All labels in (1) are retained. Both arguments have zero Dirichlet
values on every transverse face. The proof below establishes smooth
convergence of this series; it is not an assumed continuum kernel.
Transverse direction sums range over {2,3,4}; integrals over D_perp
use ordinary Lebesgue measure dx.

## Conclusion

Uniformly on each fixed compact transverse interior K,

\[
 R_{vv}\longrightarrow0,\qquad
 R_{v,v+e_\mu}\longrightarrow-\tfrac12c_*w_\mu(x_v).
                                                               \tag{2}
\]

L043(4)'s two remaining signed products have the complete limits

\[
 a^2\sum_v(\Delta F_{i,a})(v)Z_a(v)\longrightarrow0,
 \qquad
 a^2\sum_e u_l(v_h-v_l/4)
       \longrightarrow-4c_*\int_{D_\perp}
                            \sum_\mu E_{i,\mu}w_\mu.       \tag{3}
\]

Consequently the complete selected no-internal-action-pair class has

\[
 \boxed{\lim_{a\downarrow0}a^2\sum_p G^{(0)}_{i,p}
   =J_i:=2\int_{D_\perp} F_i\sum_\mu\partial_\mu^2w_\mu
             +12c_*\int_{D_\perp}\sum_\mu E_{i,\mu}w_\mu.} \tag{4}
\]

This also is lim a² T_(i,a). No value or sign for J_i, equality
J_i=48 I_i, cancellation against L030/L039, rate of convergence,
subleading powers or logarithms, or full Ward coefficient is asserted.
Other plaquettes and jets, L019's compensation, finite matching,
interacting reflected error <=c_box/2, continuum field axioms and
finite positive physical mass remain unresolved.

## Proof

### 1. Project the infinite monopole in the energy completion

Use L043's normalized torus measure, symbol lambda(theta) and Green
kernel g. On finitely supported sequences put
||f||_E²=integral lambda |hat f|². L044's resolvent-then-truncation
construction proves that hat g=1/lambda is in the completion of
these sequences for this norm, with ||g||_E²=b0=integral 1/lambda.
This does not claim g is in l². For finite f, Fourier inversion gives
<g,f>_E=f(0). In particular point evaluation is continuous for the
energy norm, since |f(0)|<=sqrt(b0)||f||_E. Translates have the same
properties.

Let g_(a,v)=G delta_v, extended by zero outside the finite interior,
and translate its source to the infinite-lattice origin. For every
finite field f supported in that translated interior,

\[
 \langle g_{a,v},f\rangle_E=f(0)=\langle g,f\rangle_E.
                                                               \tag{5}
\]

Its infinite energy is exactly the pinned finite energy, including
edges to zero boundary vertices. Thus g_(a,v) is the orthogonal
projection of g onto this finite-dimensional supported space, and

\[
 \|g_{a,v}-g\|_E\le
       \inf_{h\text{ supported in the translated interior}}
                      \|h-g\|_E,\qquad
 \|g_{a,v}\|_E\le\sqrt{b0}.                            \tag{6}
\]

Given epsilon>0, fix L044's finitely supported real h with
||h-g||_E<epsilon. For x_v in a fixed compact K, its translated
support fits inside the pinned cube uniformly for all sufficiently
small a. Equation (6) then implies uniform energy convergence on K.
There is no rate and no l² assumption on the monopole.

### 2. Freeze the residual form and use permutation symmetry

Extend A's compact stencils by zero to Z³, translating v to zero.
L041's relative form estimate, in its infinite-grid proof, gives
|<f,A h>|<=C||f||_E||h||_E uniformly in a and source location.
It extends continuously to the energy completion. L042's affine
stencil A_(M(x_v)), where M_jk=partial_j bar u_k, has the same
bound. For any fixed finite h, its finite-stencil convergence gives
<h,A h>-<h,A_(M(x_v))h> ->0 uniformly on K. Indeed all entries
needed for this quadratic form involve a fixed finite set of offsets,
and L042's Taylor argument applies uniformly there.

Choose the h of section 1. The uniform energy bounds and the bilinear
estimate bound replacement of g_(a,v) by h in the first form by
C epsilon, and replacement of h by g in the affine form by
C epsilon. The finite h comparison then tends to zero. Letting
epsilon decrease to zero proves

\[
 R_{vv}=\langle g_{a,v},A g_{a,v}\rangle
   =\int\frac{\sigma_{M(x_v)}(\theta)}{\lambda(\theta)^2}
                  \frac{d\theta}{(2\pi)^3}+o_K(1).        \tag{7}
\]

The integral follows by Fourier transformation of the energy-continuous
affine form. It is absolutely integrable since |sigma_M|<=C lambda
and 1/lambda is integrable. L042(5), with trace-free M, is
sigma_M=(1/4)sum_j w_j lambda_j(lambda-lambda_j).
Every coefficient integral
(1/4)integral lambda_j(lambda-lambda_j)/lambda² has the same value
by permutation invariance of the torus measure and lambda. Their
linear combination is therefore zero because sum_j w_j=0. This
proves the diagonal assertion in (2). It is a symmetry of the frozen
form, not annihilation of the actual variable-coefficient operator.

For neighboring compact-interior vertices, symmetry gives exactly

\[
 2R_{v,v+e_\mu}=R_{vv}+R_{v+e_\mu,v+e_\mu}
     -(\delta_v-\delta_{v+e_\mu})^T R
                            (\delta_v-\delta_{v+e_\mu}). \tag{8}
\]

L042's dipole limit and (7) prove the other assertion of (2), uniformly
after enlarging K slightly to include its neighbor vertices. Globally,
including pinned endpoint evaluations, the relative form estimate
and G_vv<=b0 give |R_vw|<=C b0. This bound will control collars.

### 3. Obtain the actual flowed kernel with its derivatives

Let lambda_(k,a)=a^(-2)sum_mu 4 sin²(pi k_mu/(2N)) and
b_(k,a)(x)=psi_k(x)/sqrt(lambda_(k,a)) for 1<=k_mu<N.
The ordinary normalized vertex eigenvector is exactly
phi_(k,a)(v)=a^(3/2)psi_k(x_v): sqrt(2/N)=sqrt(a)/2 in
each coordinate. Define
beta_(i,a;k,l) as the matrix element of
Delta^(-1/2)bar Q_i Delta^(-1/2) in these ordinary eigenvectors.
L040's isometry E0 and its intertwining with Delta show this is
exactly the axial-zero component-1 submatrix of L008's relative
B_(i,a). In particular its norm is uniformly bounded and, for fixed
k,l, beta_(i,a;k,l)->beta_(i;k,l) by L008(16).

Spectrally expanding both inverse factors in P_i now gives the exact
smooth interpolation of its sampled kernel:

\[
 K_{i,a}(x,y):=8\sum_{k,l<N}
 e^{-\tau(\lambda_{k,a}+\lambda_{l,a})}
      \beta_{i,a;k,l}b_{k,a}(x)b_{l,a}(y),\qquad
 K_{i,a}(x_v,x_w)=N(P_i)_{vw}.                         \tag{9}
\]

The factor is 8: each inverse-square-root eigenvector is
a^(1/2)b_(k,a), and Na=8. No color factor belongs in (9), which
uses the one-color block. This agrees with the full axial-column
normalization T(lambda_k^(-1/2)f_k)=sqrt(8)b_k in L030.

L008's eigenvalue bound lambda_(k,a)>=|k|²/16 and the uniform beta
bound imply that every fixed derivative in x,y of a summand of (9)
is bounded by a mesh-independent polynomial in k,l times
exp[-tau(|k|²+|l|²)/16]. This is summable on the full double
positive orthant. Truncate both indices; the fixed finite portion
and each derivative converge uniformly by beta convergence and
lambda_(k,a)->lambda_k. The omitted derivative tails tend to zero
uniformly in a by this majorant. Hence K_(i,a)->K_i in every fixed
C^r norm on the closed product cube, proving (1)'s smoothness and
F_(i,a)->F_i with uniformly bounded derivatives.

For any edge (v,v'), including an end edge, its exact u_l is
K_(i,a)(x_v,x_v)+K_(i,a)(x_v',x_v')-2K_(i,a)(x_v,x_v').
Symmetry and the fundamental theorem of calculus express this as

\[
 u_l=\int_0^a\int_0^a
  \partial_{x_\mu}\partial_{y_\mu}K_{i,a}
        (x_v+s e_\mu,x_v+t e_\mu)\,ds\,dt.            \tag{10}
\]

The formula remains exact at a pinned endpoint because each kernel
argument vanishes on that face. The C² convergence and uniform
continuity of the limiting derivatives give, uniformly over all edges,
u_l/a²=E_(i,mu)(x_v)+o(1). In particular |u_l|<=C_i a².
Similarly |Delta F_(i,a)|<=C_i a² on every interior row including
ones adjacent to pinned faces, by its uniformly bounded C² extension.

### 4. Sum both products while retaining the collars

Fix delta>0 and first restrict to vertices and edges at physical
distance at least delta from all transverse faces. By (2), R_vv=o(1)
uniformly there. Since Z_a=N R_vv, the absolute scaled second
product is bounded by
C_i a² a² N a^(-3) sup|R_vv|=O(1)sup|R_vv| ->0.
The remaining collar vertices number at most
C(delta a^(-3)+a^(-2)). Their global |R_vv|<=C bound gives a
scaled bound C_i(delta+a). Take a to zero and then delta to zero.
This proves the first assertion in (3), including its sign in L043(4).

On every edge the exact identity v_h-v_l/4=N R_vv' holds, even
when an endpoint is pinned. Therefore the third product is

\[
 a^2\sum_e u_l(v_h-v_l/4)
       =8a^3\sum_{\mu,e\parallel\mu}(u_l/a^2)R_{vv'}.  \tag{11}
\]

On the fixed delta-interior, (2) and (10) give uniform convergence
of the summand to -c_* E_(i,mu)w_mu/2. Its a³ Riemann sum
converges to that integral over the interior region. All omitted
collar and end edges have a uniform bound on (u_l/a²)R_vv', so
their contribution to (11) is at most C_i(delta+a). The limiting
smooth integrand also has a collar integral O(delta). Taking the
limits in this order proves the second assertion in (3).
Edges contained in another pinned face have zero rows and contribute
zero exactly. No physical face or signed weight has been deleted.

### 5. Assemble the selected functional and delimit its meaning

For L043(4)'s first term use L044(3). All nonzero strain stencils
are supported in a fixed compact interior. C² convergence of their
smooth extensions and the central difference formula give
a^(-2)Delta_mu bar w_(mu,a)->-partial_mu² w_mu uniformly.
The smooth kernel convergence in section 3 and the compact Riemann
sum consequently yield

\[
 a^2N\operatorname{Tr}(M_{F_{i,a}}A G)
    \longrightarrow-\frac23\int_{D_\perp}
                                  F_i\sum_\mu\partial_\mu^2w_\mu.
                                                               \tag{12}
\]

The constant is (a²N/12)a²a^(-3)=2/3. L044 supplies the discarded
scaled o(1) covariance correction; it is not assumed bounded merely
from a diagonal approximation. Combining (3) and (12) in L043's
exact full-edge identity gives the limit of S_(i,a). L041 has
T_(i,a)=-3 S_(i,a) and an O(a^(-1)) remainder for all d-containing
lines, whose a² multiple tends to zero. These facts give precisely
(4), with the color and cumulant signs already included.

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. The supporting bulk
source remains Lüscher–Weisz, *Perturbative analysis of the gradient
flow in non-abelian gauge theories*,
[arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2), sections
7.1–7.4, equations (7.1)–(7.8), and section 8.2. Its ordinary
renormalization and R⁴ hypotheses do not supply this fixed-box
unflowed-kernel limit; its general theorem is not reproved. The
necessary applicability difference here is resolved by elementary
Fourier energy projection, L042's exact affine residual, and the
existing relative-mode heat bounds. This is REPRODUCTION of standard
methods in the specified setting, with no originality claim beyond
the inspected sources. No numerical extrapolation or script is needed
to prove the qualitative limits.

The two selected upper-face classes now have combined a²-scaled
functional J_i-48 I_i. This expression is not evaluated or assumed
zero here. Comparison for both probes is necessary before drawing a
route conclusion about compensation. Even equality to zero would
leave slower powers and the logarithm, other plaquette classes and
action/measure/flow corrections, and the nonperturbative reflected
bound unproved. The construction and mass-gap target remains open.

## Mathlib

Coverage of the full fixed-box companion scaled functional: **not
checked**. Coverage of supporting homogeneous-energy Fourier
completion, orthogonal projections, discrete relative kernels,
heat-mode convergence and Riemann sums: **not checked**. No matching
Mathlib theorem is asserted; unknown availability is not absence.
