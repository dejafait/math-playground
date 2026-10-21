# L024 — The radial action local loop is uniformly bounded

## Hypotheses

Use exactly L023's SU(2) relative-cochain box, meshes a = 8/N, compact
displacement, fixed tau = 1/16, and two L010 probes. The small-coupling
coefficient is taken at each fixed mesh first. Keep all relative modes.
Write H, T_i, R_a, alpha_(i,p), beta_p and G^act_(i,a) as in L023,
with i = 3,6. Inner-product orthonormal coordinates are used throughout;
the common a^4 weight makes incidence matrices identical to their
stored-coordinate matrices. Constants below are independent of a and p,
but can depend on the fixed box, displacement and flow time.

The selected term is only
-kappa_0(f_(i,0),r_0,S_(4,rad)), not the BCH remainder of S4 or any
nonlinear residual/flow jet. Let C_(u,a) be the curvature-to-link
averaging map in L009, so K_a = C_(u,a) d. Put
M_a = M_(3,a)+M_(6,a), using L008's actual curvature forms, including
the average of squares in the triplet and the clover products in the
shear. Thus Q_3+Q_6 = d* M_a d and sup_a ||M_a|| is finite.

## Conclusion

For all sufficiently fine admitted meshes,

\[
\sup_p|\beta_p|\le C,\qquad
\left|W_{i,a}\right|
:=\left|\sum_p\alpha_{i,p}\beta_p\right|\le C_i,
\qquad |G^{\rm act}_{i,a}|\le C'_i\quad(i=3,6).
\tag{1}
\]

In particular G^act_(i,a)/log(sqrt(tau)/a) tends to zero. This excludes
an unsuppressed logarithm and faster divergence in this selected action
summand. No convergence or finite value of that summand is asserted.
The full Gamma, its logarithmic asymptotic, finite matching and the
interacting reflected-error bound <= c_box/2 remain unproved.

## Proof

### 1. Reduce the diagonal to a local row of the curvature projection

Let Delta_1 and Delta_2 be the relative Hodge Laplacians and
P = d Delta_1^(-1) d*. L003's tensor complex and L020 identify P as
the orthogonal projection onto exact two-cochains; P commutes with
Delta_2. Set L = d* d and
N = (L K_a+K_a* L)/2 - d* M_a d. By L023,
R_a = Delta_1^(-1/2) N Delta_1^(-1/2).

For a coordinate unit plaquette e_p set A_p = Delta_1^(-1) d* e_p.
The cochain identities give d* A_p = 0, L A_p = d* e_p, and
d A_p = P e_p. For example d* A_p = Delta_0^(-1) d* d* e_p = 0;
Delta_0 is invertible on relative vertices. Consequently the symmetric
generator terms have the same real diagonal and

\[
\begin{split}
\beta_p
&= A_p^* N A_p\\
&= (d C_{u,a} P)_{pp} - (P M_a P)_{pp}.
\end{split}\tag{2}
\]

The second term has absolute value <= ||M_a||. The first uses only
the finitely many entries in the p-th row of d C_(u,a). It is zero
outside a fixed enlargement of the coefficient support. Every nonzero
row, and every plaquette in that row, stays a fixed distance delta > 0
from the physical faces for sufficiently small a. This follows from
the support [-3,3]^4 in L008 and the fixed stencil radius; for example
delta = 1/2 works after refining sufficiently. The projection itself
is still the full relative-box projection.

### 2. A quantitative interior comparison of projection entries

On the infinite cubical lattice of spacing a let P_infty be the
orthogonal exact-two-form projection and Delta_(j,infty) the Hodge
Laplacians. Fourier transformation gives P_infty = d Delta_(1,infty)^(-1)
d* as a bounded multiplier: away from zero frequency its symbol is the
orthogonal projection onto the image of the incidence symbol. Its
value at the single zero frequency is immaterial in l^2. The following
identities are finite spectral identities for the box and bounded
Fourier-multiplier identities for the infinite lattice:

\[
P = d\int_0^t e^{-s\Delta_1}\,ds\,d^*
       + P e^{-t\Delta_2},\qquad
P_\infty = d\int_0^t e^{-s\Delta_{1,\infty}}\,ds\,d^*
       + P_\infty e^{-t\Delta_{2,\infty}}.
\tag{3}
\]

For the finitely many q in a nonzero p-th stencil row, we prove

\[
|P_{qp}-(P_\infty)_{qp}|\le C a^2.
\tag{4}
\]

Here p and q are identified with their infinite-lattice cells, including
their component and staggered center. Take t = delta a/128; for small
a, t <= tau. First control the two tails in (3). The relative two-form
heat diagonal has L020's bound C a^4 t^(-2), proved there from its full
edge-cosine/vertex-sine spectrum. Since 0 <= P e^(-t Delta_2) <=
e^(-t Delta_2), positivity and Cauchy–Schwarz bound every tail entry
by C a^4 t^(-2).

The infinite diagonal has the same bound. Its component Fourier
formula is

\[
(e^{-t\Delta_{2,\infty}})_{pp}
=\left[\frac1{2\pi}\int_{-\pi}^{\pi}
 e^{-4t a^{-2}\sin^2(\theta/2)}\,d\theta\right]^4
\le C a^4t^{-2}.
\tag{5}
\]

Indeed sin(|theta|/2) >= |theta|/pi on this interval, and extending
the resulting Gaussian integral to the real line bounds each factor
by C a/sqrt(t). The same projection-order/Cauchy–Schwarz argument
applies to P_infty. At the chosen t both tails are O(a^2).

For the short integrals use the explicit component one-form
Laplacians of L003. Each has nearest-neighbor off-diagonal entries
-a^(-2), nonnegative diagonal <= 8a^(-2), and nonnegative row sums.
The edge coordinate has the one-dimensional Neumann endpoint diagonal
a^(-2); the vertex coordinates have Dirichlet diagonal 2a^(-2).
Thus U = I - a^2 Delta_1/8 has nonnegative entries and row sums <= 1.
The infinite U_infty is stochastic, and both agree in the interior.
The exact exponential series is

\[
e^{-s\Delta_1}
=e^{-\mu_s}\sum_{m\ge0}\frac{\mu_s^m}{m!}U^m,
\qquad \mu_s=8s/a^2,
\tag{6}
\]

with the same formula for U_infty. A power represents m steps, each
moving at most a (or staying). All edges in d* e_p and d* e_q are
within a of these fixed interior plaquettes. Choose
M = floor(delta/(4a)). For sufficiently small a their paths of fewer
than M steps cannot reach a boundary row, so the corresponding matrix
entries of U^m and U_infty^m agree. Each entry is at most one.
Uniformly for 0 <= s <= t, mu_s <= delta/(16a) <= M/2, after
refining so M >= delta/(8a). Exponential Markov inequality at parameter
log 2 gives

\[
\Pr\{\operatorname{Pois}(\mu_s)\ge M\}
\le e^{-M\log2+\mu_s}
\le e^{-(\log2-1/2)M}\le e^{-c\delta/a}.
\tag{7}
\]

Each entry difference in (6) is therefore at most 2e^(-c delta/a).
There are four incidence entries in each plaquette boundary, of
absolute size 1/a. The short-integral entry difference in (3) is at
most 32 t a^(-2) e^(-c delta/a) = O(a^(-1)e^(-c delta/a)), which is
O(a^2). Combining with the tails proves (4). No limit exchange or
replacement of relative boundary conditions was made.

### 3. Freeze the coefficient and use exact stencil parity

Extend u_a to all real x by the same central-difference formula on
the fixed smooth Psi. This extension and its first derivatives are
uniformly bounded. At the plaquette center z_p put c = u_a(z_p).
For an interior row, replace every endpoint displacement in C_(u,a)
by this constant c, obtaining C_c. The curl contributes a factor 1/a,
while every displacement sample in its fixed stencil differs from c
by at most C a. Thus the row error E_p obeys

\[
(d C_{u,a})_{p,\cdot}=(d C_c)_{p,\cdot}+E_p,
\qquad \sum_q|(E_p)_q|\le C,
\qquad \sum_q|(d C_c)_{pq}|\le C|c|/a.
\tag{8}
\]

The frozen row is exactly odd under spatial inversion about z_p.
To verify this without a continuum approximation, on staggered grids
write A_r = (S_(+a e_r/2)+S_(-a e_r/2))/2 for a centered average.
The clover at a vertex is A_rho A_nu F_(rho nu), and averaging the
two link endpoints gives
(C_c F)_nu = sum_rho c_rho A_rho A_nu^2 F_(rho nu).
These centered averages are even. The curl at z_p is the centered
incidence difference D_mu of this link component minus D_nu of the
other component, with D_r = (S_(+a e_r/2)-S_(-a e_r/2))/a.
Each difference is odd, so the full row is odd, for every input plane.
Inversion preserves all the relevant staggered component grids.

Conversely P_infty e_p is even about z_p. The geometric pullback of
this inversion acts with sign +1 on two-cochains and fixes e_p;
the infinite exact-form space and its orthogonal projection are
invariant under that pullback. Equivalently, its Fourier projection
kernel has this inversion symmetry. Pairing the finite odd row with
the even column therefore gives exactly

\[
(d C_c P_\infty)_{pp}=0.
\tag{9}
\]

The independent exact-rational check
`python3 scripts/combined-ward-response/check_radial_action_local_stencil.py`
builds the clover/endpoint/curl row in units a/2 for every output plane
and each of four displacement components. All 24 inversion checks
have zero defect. The full certificate is
`scripts/combined-ward-response/radial-action-local-stencil-certificate.json`.
This checks parity only; (3)–(7) provide the boundary estimate.

Now |P_qp| <= 1 because P is an orthogonal projection. Equations
(4), (8), and (9) imply

\[
|(d C_{u,a}P)_{pp}|
\le |E_p P e_p|+|(d C_c)(P-P_\infty)e_p|
\le C+(C|c|/a)Ca^2\le C'.
\tag{10}
\]

For a zero stencil row the first term in (2) is zero, including at
the physical boundary. Together with the bounded M_a term, (2) and
(10) prove the uniform beta bound for every plaquette, not just those
in the displacement support.

### 4. Sum against both actual flowed probes

L023 proves
sum_p |alpha_(i,p)| <= ||T_i||_1 <= M_i Tr(E_tau), uniformly in a.
The beta bound therefore proves |W_(i,a)| <= C_i for both i.
L023's other pairing class is o(1), and its exact contraction is
G^act_(i,a) = (5/4)W_(i,a)+(5/2)sum_p v_p chi_(i,p).
This proves (1) and the ratio-to-log conclusion. A bounded sequence
need not converge, so no finite matching constant is inferred.

### 5. Scope and literature qualification

This specializes elementary projection, heat-kernel and stencil
identities to the actual relative boundary and endpoint-averaged
generator. It improves L023's O(a^(-1)) estimate for the selected
radial action occurrence; L021 treats a different flow occurrence.
It transfers no higher nonlinear polynomial through the linear gauge
quotient and does not evade L022's obstruction.

Reuse the SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. Luescher–Weisz,
[*Perturbative analysis of the gradient flow in non-abelian gauge
theories*, arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2),
sections 7.1–7.4, equations (7.1)–(7.8), and section 8.2, establish
perturbative positive-flow-time finiteness after ordinary bulk
renormalization on R^4. That input is supporting context only: its
flow-direction boundary does not control the physical box faces or
this unflowed residual diagonal. The explicit proof above supplies
that specialization; it does not reprove general flow renormalizability.
Classify the local progress as REPRODUCTION, without a novelty claim.
Remaining action, measure, residual and observable jets can still have
divergent contributions and cancellations. No full logarithmic
coefficient, prescribed interacting trajectory, reflected-error bound,
reflection-positive continuum theory or physical mass is obtained.

## Mathlib

Full coverage of the selected radial-action bound and the interior
relative/infinite projection estimate: **not checked**. Supporting
projection order, spectral heat identities, Poisson-tail inequalities,
Fourier multipliers and trace ideals: **not checked**. No matching
Mathlib theorem is asserted. The primary flow theorem cited above
does not match the full hypotheses or conclusion here.
