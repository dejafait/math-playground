# L042 — Cancellation of the companion's apparent a^-4 coefficient

## Hypotheses

Keep L040–L041's exact hypotheses, ordinary dimensionless matrices,
straight forest, both original probes, all three colors and every upper
(1,mu) plaquette, including transverse boundary strips. Write T_(i,a)
for L041(4), a=8/N and tau=1/16. Constants below may depend on these
fixed smooth data but not on sufficiently fine admitted meshes.

Transverse indices j,k,mu range over {2,3,4}. Write G=Delta_3^(-1),
R=G bar A G and P_i=G h_3 bar Q_i h_3 G as in L040. A boundary
vertex evaluation means zero. Let bar u be the smooth continuum limit
of L040(12), and put w_j(x)=partial_j bar u_j(x). Thus
sum_j w_j=0. These w_j are continuum compressed coefficients, not
an assumption that each finite-difference extension has zero continuous
divergence. No heat factor is introduced into R.

## Conclusion

For every compact K contained in (-4,4)^3, uniformly over transverse
edges v to v+e_mu with x_v in K,

\[
 \frac{v_l(v,\mu)}N
 = (\delta_v-\delta_{v+e_\mu})^T R
       (\delta_v-\delta_{v+e_\mu})
 = c_* w_\mu(x_v)+o_K(1).                              \tag{1}
\]

Here, with normalized integration dtheta/(2 pi)^3 over [-pi,pi]^3,

\[
 \lambda_j=2-2\cos\theta_j,\quad \lambda=\sum_j\lambda_j,
 \qquad
 c_* =\frac18\int
  \frac{\lambda_4(\lambda_2-\lambda_3)^2}{\lambda^2}
  \frac{d\theta}{(2\pi)^3}>0.                           \tag{2}
\]

The value at theta=0 is immaterial. The direction sum in (1) vanishes
to leading order, although its individual directions need not vanish.
For the actual signed companion,

\[
 \sum_p u_l v_h=O(a^{-2}),\qquad
 \sum_p u_b v_b=O(a^{-2}),\qquad
 a^4 T_{i,a}\longrightarrow0,\quad i=3,6.               \tag{3}
\]

Together with L041 this also gives a^4 sum_p G^(0)_(i,p) -> 0.
The last conclusion is **o(a^-4)**, not O(a^-2). No quantitative
remainder in (1), existence of an a^2-scaled limit, cancellation of
L039's negative a^-2 coefficient, or logarithmic coefficient is proved.
In particular a^-3 growth and other rates between a^-4 and a^-2
remain possible. This is local progress by standard methods, not
progress beyond the inspected literature on the full Yang–Mills target.

## Proof

### 1. The frozen affine residual is a nonzero scalar stencil

Extend the compact coefficient functions by zero and use the infinite
unit transverse lattice for this local computation. Write S_j for the
shift phi(n) -> phi(n+e_j), T_j=(S_j-S_j^(-1))/2,
C_j=(S_j+S_j^(-1))/2 and Delta_j=2-S_j-S_j^(-1).
Thus Delta=sum_j Delta_j. The C_j here average two full-step vertex
neighbors; they are not L040's edge-to-vertex averages.

Freeze bar u at a physical point x to the affine function
u_k(n)=u_k(x)+a sum_j M_jk n_j, where M_jk=partial_j bar u_k(x),
w_j=M_jj. For K=a^(-1) sum_k M_(u_k) T_k, direct shift commutators give

\[
 [\Delta,M_{u_k}]=-2a\sum_j M_{jk}T_j,\qquad
 [T_k,M_{u_k}]=a w_k C_k.
\]

Consequently the symmetric transport part is exactly

\[
 \frac{\Delta K+K^T\Delta}{2}
 =-\sum_{j,k}M_{jk}T_jT_k-\frac12\sum_k w_k C_k\Delta.
                                                               \tag{4}
\]

For these affine coefficients L040's triplet is sum_j w_j Delta_j,
and its shear is -sum_(j<k)(M_jk+M_kj)T_jT_k. Thus every off-diagonal
entry of M cancels between transport and shear. On the Fourier torus
the residual symbol, before imposing zero trace, is

\[
 \sigma_M=\sum_j w_j
   \left(\sin^2\theta_j-\lambda_j
                      -\frac\lambda2\cos\theta_j\right).
                                                               \tag{5}
\]

Using sin²(theta_j)=lambda_j-lambda_j²/4 and
cos(theta_j)=1-lambda_j/2 yields

\[
 \sigma_M=-\frac\lambda2\sum_jw_j
       +\frac14\sum_jw_j\lambda_j(\lambda-\lambda_j).
\]

For trace-free M only the second term remains. This is the affine
constant-coefficient residual A_M used below. Its symbol is real and
|sigma_M|<=C|M|lambda, so its form is bounded by the lattice energy.
The constant part u(x), including its apparent factor a^-1, cancels
exactly in (4); no large constant transport term is neglected.

The actual smooth coefficient extensions in L040(12) converge in every
fixed C^r norm to bar u. To see this directly, their central differences
converge in C^r to the corresponding derivatives of x rho(x), and
c_N=N^(-1) sum rho(-4+aj) converges to (1/8) integral rho. Their
derivatives are uniformly bounded and their supports stay compactly
inside the transverse box. Since bar u_2 is a transverse derivative
of the averaged Psi_24 and bar u_4 its negative other derivative,
partial_2 bar u_2+partial_4 bar u_4=0 and bar u_3=0.

For any fixed finite set of lattice offsets n around v, Taylor's
formula now shows that the coefficients of the actual translated
bar A tend uniformly, for x_v in a compact interior K, to those of
A_(M(x_v)). Indeed subtract the local constant and affine terms of
bar u_a. The remainder on those offsets is O_K(a²); the transport
stencil divides it only by a. The constant term cancels as above,
the affine derivative tends uniformly to M(x_v), and the central
strain and edge-average coefficients converge to their affine values.
This is convergence of each coefficient of a fixed finite stencil,
not application of smooth-input consistency to a singular Green column.

### 2. Justify the dipole limit by finite-domain energy approximation

Here is the required discrete argument, including control of distant
coefficient rows. Put eta_mu=delta_0-delta_(e_mu) on Z^3 and let
g_mu have Fourier transform hat eta_mu/lambda. It belongs to l2:
near theta=0, |hat eta_mu|²/lambda² <=C|theta|^-2, which is integrable
in dimension three, and away from zero the denominator is bounded
below. Fourier inversion gives Delta g_mu=eta_mu. With
||f||_E²=sum_j ||(S_j-I)f||_2², its energy is

\[
 \|g_\mu\|_E^2=\int\frac{\lambda_\mu}{\lambda}
                         \frac{d\theta}{(2\pi)^3}<\infty.
                                                               \tag{6}
\]

These facts use the elementary unitary Fourier transform on l2(Z^3).
No continuum Green asymptotic is imported. In particular, truncations
h supported on increasingly large finite sets approximate g_mu in l2
and hence in energy, because Delta is a bounded l2 operator.

Translate the finite pinned cube so that v is at 0, and extend its
Dirichlet Green dipole g_(a,v)=G eta_(v,mu) by zero outside that cube.
For every field f supported on its interior,

\[
 \langle g_{a,v},f\rangle_E=\langle\eta_\mu,f\rangle
                           =\langle g_\mu,f\rangle_E.
\]

The energy includes the edges to the pinned boundary, so this identity
has exactly the Dirichlet Laplacian used in L040. It implies the
orthogonality of g_mu-g_(a,v) to the finite supported space and therefore

\[
 \|g_{a,v}-g_\mu\|_E
 \le \inf_{h\text{ supported in the translated cube}}
                  \|h-g_\mu\|_E.                     \tag{7}
\]

For x_v in any fixed compact interior K the distance to every pinned
face, measured in lattice steps, tends uniformly to infinity. Each
fixed compact approximation h is thus admissible eventually, uniformly
in v, so (7) tends uniformly to zero. This also bounds ||g_(a,v)||_E
by ||g_mu||_E. No convergence rate in physical a is asserted.

Extend the actual bar A to Z^3 by its zero-extended compact coefficient
stencils. Its forms on pinned fields are unchanged: every nonzero
coefficient stencil stays a positive physical distance from the faces.
The proof of L041(13), with the same bounded coefficient derivatives,
applies on this whole lattice and gives uniformly

\[
 |\langle f,\bar A f\rangle|\le C\|f\|_E^2,
 \quad
 |\langle f,\bar A h\rangle|\le C\|f\|_E\|h\|_E.    \tag{8}
\]

The bilinear estimate follows by polarization and optimizing the relative
scale of f,h. It extends from finite supports to their energy limits.
The affine operator A_M has the same bound for bounded M by (5).

Fix epsilon>0 and a finite h with ||h-g_mu||_E<epsilon. Equation (7)
gives ||g_(a,v)-h||_E<=2 epsilon eventually. Equation (8) bounds the
difference of their bar A quadratic forms by C epsilon, uniformly in
v and a. For this fixed h, the finite-stencil convergence proved in
section 1 gives

\[
 \langle h,\bar A h\rangle
   -\langle h,A_{M(x_v)}h\rangle\longrightarrow0
\]

uniformly on K. Replacing h by g_mu in the second form again costs
at most C epsilon, uniformly since M is bounded. Letting epsilon tend
to zero proves the full untruncated local limit

\[
 \eta_{v,\mu}^T G\bar A G\eta_{v,\mu}
   =\int\frac{\lambda_\mu\sigma_{M(x_v)}}{\lambda^2}
                        \frac{d\theta}{(2\pi)^3}+o_K(1).        \tag{9}
\]

Thus distant rows and all unflowed frequencies have been controlled by
energy approximation; freezing the symbol alone would not prove (9).

### 3. Compute the direction sum without discarding the anisotropy

Let kappa_mu(w) denote the integral in (9) for trace-free w. It is
linear in w. Permuting coordinate labels in the torus integral shows
that its coefficient of w_mu is a common value alpha and the other
two coefficients have a common value beta. Hence
kappa_mu=(alpha-beta)w_mu on the trace-free plane. To determine this
difference, take w_2=1,w_3=-1,w_4=0. Equation (5) gives
sigma=lambda_4(lambda_2-lambda_3)/4. Interchanging theta_2 and theta_3
in the integral for kappa_2 and averaging gives precisely (2). Thus
kappa_mu=c_* w_mu for every mu, and sum_mu kappa_mu=0.

The integrand in (2) is nonnegative, bounded by a constant times
lambda, and strictly positive on an open set where lambda_4>0 and
lambda_2 differs from lambda_3. Therefore it is integrable and its
integral is strictly positive. This also rules out individual-direction
annihilation as an explanation for the cancellation. Equations (9)
and L040(5) prove (1).

### 4. Retain the full signed sum and the transverse end edges

Define the actual flowed diagonal and the unflowed diagonal by

\[
 F_i(v)=N(P_i)_{vv},\qquad Z(v)=N R_{vv},
\]

both zero on the transverse boundary. Symmetry gives on each edge
v to v'

\[
 u_h=F_i(v)-u_b-u_l/4,
 \quad u_b=\tfrac12(F_i(v)-F_i(v')),
 \quad v_b=\tfrac12(Z(v)-Z(v')).                       \tag{10}
\]

L040(13) shows |F_i|<=C_i, u_h=F_i(v)+O(a), and |u_l|<=C_i a².
L041 gives |v_h|+|v_l|+|v_b|+|Z|<=C/a uniformly, including end edges.
It follows immediately that sum_p |u_l v_h|=O(a^-2).

For the mixed product use one extra smoothness fact from the flowed
mode expansion: F_i has a smooth extension to the closed transverse
cube with uniformly bounded C² norm. Explicitly its one-color expansion
pairs two complete axial-sum columns a sum_(r=0)^(N-1) b_(k,1)(r,v)
against the bounded relative probe matrix and the two heat factors,
as in L040(13) and L041's proof of (16). Each column and every fixed
transverse derivative is bounded by a polynomial of the mode label:
there are N summands and aN=8. Each entry of the bounded relative
probe matrix is bounded by its norm. The double sum of these polynomial
bounds times exp(-tau(lambda_k+lambda_l)) is finite uniformly, by
the relative spectral bound used in L008. Differentiating twice is
therefore justified by an absolutely summable majorant. The axial
component modes vanish at transverse faces, so this smooth extension
has the stated zero boundary values. This argument requires no spatial
regularity of the unflowed diagonal Z.

Thus |Delta_3 F_i(v)|<=C_i a² at every interior vertex, also adjacent
to a face. The exact Dirichlet summation identity with all end edges is

\[
 \sum_p u_bv_b
 =\frac14\sum_{\text{all transverse edges }(v,v')}
             (F_i(v)-F_i(v'))(Z(v)-Z(v'))
 =\frac14\sum_{v\text{ interior}}(\Delta_3 F_i)(v)Z(v).
                                                               \tag{11}
\]

Its right side is O(a² a^-1 a^-3)=O(a^-2). Edges contained in another
transverse face have identically zero rows; including them changes
nothing. This proves the first two estimates of (3) without dropping
any boundary strip.

It remains to sum u_h v_l. Set r_mu(v)=v_l(v,mu)/N. Uniformly,
|r_mu(v)|<=C. Replacing u_h by F_i(v) costs O(a) per edge before the
factor N. There are O(a^-3) edges, so its error after multiplication
by a^4 is O(a). For delta>0, take vertices at physical distance at
least delta from every transverse face. At all these vertices each
of the three positive-direction edges exists for small a; (1) gives

\[
 \sum_\mu r_\mu(v)
 =c_*\sum_\mu w_\mu(x_v)+o_\delta(1)=o_\delta(1)
\]

uniformly. Their contribution after multiplying by a^4 N=8a³ tends
to zero, since |F_i| is bounded and the number of vertices is O(a^-3).
The remaining collar and end edges number at most
C(delta a^-3+a^-2). Their same scaled contribution is bounded by
C_i(delta+a), using the uniform bounds, rather than deleting them.
Take a to zero first and then delta to zero. This proves
a^4 sum_p u_hv_l ->0. Combining with (11), the u_l v_h estimate,
and L041(4) proves (3), with its existing color factor -3.
L041's O(a^-1) estimate for the other two lines proves the assertion
for the complete selected companion.

### 5. Scope, checks and the remaining threshold

The proof uses exactly the compressed operators already justified in
L040 and the energy bound in L041. It does not replace the first
probe by a different observable, discard Psi_13 from d-containing
entries, or apply a heat bound to the residual. The vanishing occurs
after summing three transverse directions with their common leading
flowed diagonal. It is compatible with c_*>0 and nonzero local loops.

The exact affine-stencil check is reproduced by
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_companion_affine_symbol.py`.
Its certificate is
`scripts/combined-ward-response/companion-affine-symbol-certificate.json`.
It compares the full transport, triplet and shear stencils with (5)
for all nine first-derivative matrix basis elements, and all three
constant transports, by exact Laurent coefficients. It also checks
the trace-free symbol reduction and the permutation-averaging numerator
in (2). These are finite algebra checks, not verification of a cutoff
rate; sections 2 and 4 supply the analytic limiting argument.

Reuse `drafts/literature/2026-09-26-current-target.md`, SPECIALIZE.
Luescher–Weisz, *Perturbative analysis of the gradient flow in
non-abelian gauge theories*, [arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2),
sections 7.1–7.4, (7.1)–(7.8), and section 8.2, remains the inspected
general bulk flow-finiteness input. It does not supply (1) for this
unflowed fixed-box kernel and is not reproved here. The present work
specializes finite difference algebra, Fourier inversion and elementary
energy projection to the exact residual, under the unchanged scope.
It is classified REPRODUCTION, with no claim of original mathematics
beyond the sources checked.

The next unresolved estimate is a quantitative remainder strong enough
to control all powers above a^-2, followed by the a²-scaled trace.
The energy approximation above is qualitative and supplies neither.
Even that scaled trace would leave slower powers and the full logarithm,
other plaquettes and action/measure/flow jets, L019 compensation, finite
matching and the interacting reflected-error threshold c_box/2 open.
Continuum fields, full reflection positivity, infrared control and
finite positive mass remain independent gaps.

## Mathlib

Coverage of the full fixed-box limit (1) or (3): **not checked**.
Coverage of supporting lattice Fourier transforms, energy projections,
finite matrix identities and pinned summation by parts: **not checked**.
No matching Mathlib theorem is asserted; unknown coverage is not absence.
