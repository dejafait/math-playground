# L040 — Exact color contraction and axial-zero compression of the companion

## Hypotheses

Use L025's exact forest Gaussian, three SU(2) colors, bare coupling
convention and no-internal-action-pair term. Keep L008–L009's specified
displacement, central differences, endpoint/clover maps and both original
probes at tau=1/16. Use L029's straight lower-rooted forest and all its
upper-face (1,mu) plaquettes, mu=2,3,4, including transverse boundary
strips. The fixed-mesh small-coupling coefficient is taken first.

In L029's local coordinates H=(A+B)/2, L=A-B, d=A-B-T, write U and V
for the **one-color** blocks of L025's matrices U_(i,p), V_p. Denote their
six entries by

\[
(u_h,u_l,u_e,u_b,u_c,u_f)
=(U_{HH},U_{LL},U_{dd},U_{HL},U_{Hd},U_{Ld}),
\]
\[
(v_h,v_l,v_e,v_b,v_c,v_f)
=(V_{HH},V_{LL},V_{dd},V_{HL},V_{Hd},V_{Ld}).             \tag{1}
\]

These matrices are symmetric but need not be positive. Colors give three
identical blocks with no cross-color entries. The letters in (1) are not
L029's entries of the internal covariance C.

For the compression use **dimensionless** ordinary-coordinate matrices
from L018: Delta=D_1^T D_1+D_0D_0^T, Sigma=Delta^(-1),
L_0=D_1^T D_1, H_tau=exp(-tau Delta/a^2),

\[
B_i=H_\tau Q_i H_\tau,\qquad
A_0=(L_0K_a+K_a^T L_0)/2-Q_3-Q_6.                       \tag{2}
\]

The subscript on A_0 distinguishes this residual matrix from the local
upper axial coordinate A. In particular Delta is a^2 times L028's
physical Laplacian; no further a factors are implicit in (2).

## Conclusion

The full no-internal-pair contribution per selected plaquette, with all
three colors and L025's negative cumulant sign, is exactly

\[
\begin{split}
G^{(0)}_{i,p}={}&-3(u_hv_l+u_lv_h-2u_bv_b)\\
 &+(u_lv_e+u_ev_l-2u_fv_f)\\
 &+4(u_hv_f+u_fv_h-u_bv_c-u_cv_b).                       \tag{3}
\end{split}
\]

The sum of (3) over all selected plaquettes is the companion to L029's
one-internal-pair sum. No heat factor is supplied to V.

There is an exact three-dimensional formula for the H,L blocks of both
U and V. Let Delta_3 be the dimensionless Dirichlet vertex Laplacian on
the transverse cube, G_3=Delta_3^(-1), and h_3=exp(-tau Delta_3/a^2).
For an edge with endpoints v,v', set
eta_H=(delta_v+delta_v')/2 and eta_L=delta_v-delta_v', with a boundary
delta interpreted as zero. Define E_0 from transverse vertex functions
to full one-cochains by

\[
(E_0\phi)_1(r,v)=\phi(v)/\sqrt N\quad(0\le r<N),\qquad
(E_0\phi)_\mu=0\quad(\mu\ne1).                         \tag{4}
\]

Put bar Q_i=E_0^T Q_i E_0 and bar A=E_0^T A_0 E_0. For r,s in {H,L},

\[
 U_{rs}=N\eta_r^T G_3h_3\bar Q_i h_3G_3\eta_s,\qquad
 V_{rs}=N\eta_r^T G_3\bar A G_3\eta_s.                  \tag{5}
\]

All three compressed operators bar Q_3, bar Q_6, bar A depend **only on
Psi_24**. Their Psi_13 parts vanish exactly at every admitted mesh.
Consequently the first line of (3), considered as a sum or pointwise on
a plaquette, depends only quadratically on Psi_24; it has neither a
pure Psi_13 contribution nor a mixed-potential contribution. This does
not remove the remaining two lines involving d.

Explicit finite stencils for the compressed operators are (9)–(11)
below. Thus (5) is an evaluable reduction with no unproved continuum
kernel assumption. This step does **not** establish existence or value
of lim a^2 sum_p G^(0)_(i,p). In particular it proves no cancellation
of L039's selected coefficient, no full power/logarithmic coefficient,
and no improvement of the reflected-error threshold c_box/2.

## Proof

### 1. Contract the complete local polynomial

Use L029's exact polynomial

\[
q=|[H,L]|^2/8-|[L,d]|^2/24
       -\langle[H,d],[H,L]\rangle/6.                    \tag{6}
\]

For an auxiliary centered three-color Gaussian with one-color covariance
C=(h,l,e,b,c,f) in the order (1), the standard Isserlis formula gives

\[
\begin{split}
E|[H,L]|^2&=6(hl-b^2),\\
E|[L,d]|^2&=6(le-f^2),\\
E\langle[H,d],[H,L]\rangle&=6(hf-bc).
\end{split}                                            \tag{7}
\]

For example the last identity follows from
|H|^2(d dot L)-(H dot L)(H dot d): the first expectation is
9hf+6bc, the second is 3hf+12bc. The bracket sign in SU(2) cancels
between its two occurrences. Thus E q=3(hl-b^2)/4-(le-f^2)/4-hf+bc.

If K is the symmetric quartic tensor of q, then E q=3 K:C C.
This identity first holds for positive definite C and hence, by polynomial
identity, for every symmetric C. Polarizing the quadratic polynomial
K:C C gives

\[
\begin{split}
K:UV={}&(u_hv_l+u_lv_h-2u_bv_b)/8\\
 &-(u_lv_e+u_ev_l-2u_fv_f)/24\\
 &-(u_hv_f+u_fv_h-u_bv_c-u_cv_b)/6.
\end{split}                                            \tag{8}
\]

Here U,V on the left mean the full three-color block matrices. Inserting
-24 K:UV from L025 gives (3). The color sum has already been performed
in (7); there is no additional factor of three. Degenerate local boundary
coordinates satisfy the same polynomial identity by restriction.

### 2. Exact scalar stencils after the axial projection

On the transverse vertex grid let D_mu be the dimensionless pinned
incidence from vertices to mu-edges, C_mu the centered average from
mu-edges to vertices, and T_mu=C_mu D_mu, for mu=2,3,4. Their transposes
use the ordinary sum inner products. Thus T_mu is the dimensionless
full-step central difference and Delta_3=sum_mu D_mu^T D_mu. Boundary
vertices are zero. Define, for each transverse interior vertex,

\[
\bar u_\mu(v)=\frac1N\sum_{j=1}^{N-1}u_{a,\mu}(j,v),\quad
\bar w_\mu=T_\mu\bar u_\mu/a,\quad
\bar s_{\mu\nu}=(T_\mu\bar u_\nu+T_\nu\bar u_\mu)/a.
                                                               \tag{9}
\]

Only transverse mu,nu occur on the right. If M_f means multiplication
by the indicated vertex or edge coefficient, the compressed stencils are

\[
\begin{split}
\bar K&=a^{-1}\sum_{\mu=2}^4 M_{\bar u_\mu}T_\mu,\\
\bar Q_3&=\sum_{\mu=2}^4D_\mu^T M_{C_\mu^T\bar w_\mu}D_\mu,\\
\bar Q_6&=\frac12\sum_{2\le\mu<\nu\le4}
 (T_\mu^T M_{\bar s_{\mu\nu}}T_\nu
  +T_\nu^T M_{\bar s_{\mu\nu}}T_\mu),
\end{split}                                                   \tag{10}
\]
\[
\bar A=(\Delta_3\bar K+\bar K^T\Delta_3)/2-\bar Q_3-\bar Q_6.
                                                               \tag{11}
\]

Here C_mu^T bar w_mu is an **edge weight**; replacing it by a clover
square would give a different triplet.

To verify these equations, E_0 is an isometry since there are N equal
axial entries. Its fields are co-closed: D_0^T E_0=0, because the
axial divergence is the difference of consecutive equal entries. The
relative tensor spectrum therefore gives
Delta E_0=L_0 E_0=E_0 Delta_3. For x=E_0 phi its only nonzero curls
are (D_1 x)_(mu,1)=D_mu phi/sqrt N. They are constant in the axial edge
coordinate. The axial clover average maps this constant to the same
constant on the N-1 vertices. The transverse clover average then gives
T_mu phi/sqrt N. The component-1 endpoint map is the transpose axial
average. Summing its output over all N edges returns exactly the sum
of its input over the N-1 vertices: each vertex occurs twice with weight
1/2. Compressing K_a consequently gives bar K in (10), including 1/a.
The other output components of K_a need not vanish, but L_0 E_0 has
only component 1, so they do not enter E_0^T L_0K_a E_0.

For the triplet, only planes (1,mu) survive. Its weight is the
two-coordinate average of w_1+w_mu. The same axial sum rule leaves
C_mu^T applied to the axial average of that coefficient. The average
of w_1 is zero: the central axial difference telescopes, and u_1 is
zero on the first and last interior axial vertex layers, as well as on
the boundary, by the admitted compact support. The axial average of
w_mu, for transverse mu, is bar w_mu because transverse differences
commute with that finite sum. This proves bar Q_3 without exchanging
an average of squares for a square of an average.

For the shear form only transverse pairs mu,nu with alpha=1 survive:
F_(mu,1) F_(nu,1) has positive product sign. The clover values are
T_mu phi/sqrt N and T_nu phi/sqrt N. All pairs with an index 1 vanish
because their second curvature factor is a transverse-plane curvature
or F_11. Averaging s_mu nu along the axial vertices gives bar s_mu nu;
polarizing the resulting quadratic form yields bar Q_6, including the
1/2. Finally L_0 E_0=E_0 Delta_3 and its transpose prove (11).

The support condition just used also applies to all reversed stencils.
No boundary term is removed from a nonzero coefficient row; near a
transverse boundary the formulas are the ordinary pinned incidences and
their transposes.

### 3. The Psi_13 cancellation and the actual forest rows

For the Psi_13 displacement the only transverse component is
u_3=-nabla^c_1 Psi_13. Its axial sum is exactly zero by the same central
telescoping identity: for a sequence z with zero boundary and first/last
interior values,
sum_(j=1)^(N-1)(z_(j+1)-z_(j-1))=0. The transverse u_2,u_4 are zero.
Thus every bar u_mu in (9) is zero for this potential. Equations
(10)–(11) show bar Q_3=bar Q_6=bar A=0 for that part individually.
The possible nonzero axial component u_1 has already disappeared in
the explicit compression calculation; it has not been discarded by a
gauge choice.

For comparison, put c_N=N^(-1) sum_(j=1)^(N-1) rho(-4+aj), and write
x_mu for a transverse coordinate. The remaining coefficients are

\[
\bar u_2=c_N x_2\rho(x_2)\rho(x_3)
                   \nabla^c_4[x_4\rho(x_4)],\qquad
\bar u_4=-c_N\nabla^c_2[x_2\rho(x_2)]\rho(x_3)x_4\rho(x_4),
\quad\bar u_3=0.                                      \tag{12}
\]

This is an exact finite sum specialization of L008, not its continuum
integral limit.

L018's free-gauge-invariant quadratic insertions give the exact lifted
matrices R_F Sigma B_i Sigma R_F^T and R_F Sigma A_0 Sigma R_F^T.
This follows either from that lemma's quotient law or by using
R_F^T B_i R_F=B_i and R_F^T A_0 R_F=A_0 in the forest covariance
product. It transfers only the quadratic contractions and retains the
forest rows of the quartic.

By L029's exact path formula the upper omitted link at v is the sum
of all N axial Hodge links at v. Hence its H,L rows, after retraction,
are sqrt N eta_H^T E_0^T and sqrt N eta_L^T E_0^T. Since
Sigma E_0=E_0 G_3 and H_tau E_0=E_0 h_3, multiplying those rows into
the two lifted matrices gives precisely (5). These identities hold
also when an endpoint is a pinned transverse vertex. Thus all boundary
strips are retained. Each H,L block in (5) is linear in Psi_24 and has
zero Psi_13 part, proving the assertion about the first line of (3).
The d row is a top-layer circulation, not an axial-zero projection,
so this proof does not apply to entries containing d.

### 4. What the reduction does and does not estimate

L029's smooth-column estimate and L008's bounded heat-weighted probe
matrix imply the uniform bounds

\[
(|u_h|,|u_l|,|u_e|,|u_b|,|u_c|,|u_f|)
\le C_i(1,a^2,a^4,a,a^2,a^3).                           \tag{13}
\]

Indeed the local lifted columns have sizes (1,a,a^2) times a fixed
polynomial of their mode labels in (H,L,d). In the expansion of U,
both columns have exp(-tau lambda) factors, so their product sums are
uniformly bounded by the corresponding powers in (13). All relative
modes are included, as in L028–L029. Equation (13) does not supply
analogous bounds on V: its formula (5) has G_3 bar A G_3 without heat.
Nor does L028's O(a^2) consistency on fixed smooth modes bound the
diagonal of this untruncated three-dimensional kernel. The d-containing
terms in (3), the transverse boundary strips in any asymptotic estimate,
and the weighted diagonal sum in (5) remain unresolved.

Cancellation of L039's one-pair limit would require the **complete**
companion sum to have limit +48 I_i after multiplication by a^2.
Neither (12) nor (13) establishes that. Even such cancellation would
leave other classes and L019's compensation, slower powers and the
full logarithm, finite matching and the interacting comparison open.

### 5. Checks and source scope

Reproduce the bounded checks with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_upper_face_companion.py`.
The full certificate is
`scripts/combined-ward-response/upper-face-companion-certificate.json`.
The polynomial check forms (6) in nine scalar variables and computes
minus its two covariance-Laplacian derivatives. This is -24 K:UV.
All 36 ordered pairs of the six symmetric one-color matrix basis
elements agree exactly with (3), using rational arithmetic. This is
complete coefficient verification of the bilinear color identity,
independent of a probe sample or positivity assumption.

At the admitted N=24 mesh, the script compares direct four-dimensional
compression with (10)–(11), separately for the residual and each
unflowed probe, for the full displacement and its two potential parts.
It uses one smooth scalar mode product and one fixed-seed input with
all frequencies. The 24 floating diagnostics, including the six
Psi_13 annihilation checks, pass with maximum defect below 6.04e-14;
each required tolerance is recorded in the certificate. These two-input
checks are not a proof of operator equality or an interval enclosure.
The proof of equality on every input is the finite stencil calculation
above. No numerical asymptotic extrapolation was performed.

Reuse `drafts/literature/2026-09-26-current-target.md`, DECISION SPECIALIZE.
The supporting Luescher–Weisz result, *Perturbative analysis of the
gradient flow in non-abelian gauge theories*,
[arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2), sections 7.1–7.4,
equations (7.1)–(7.8), and section 8.2, concerns perturbative bulk flow
finiteness after ordinary renormalization. It is not an estimate of the
unflowed fixed-box kernel in (5). That theorem is not reproved here.
The local color polarization and pinned-stencil specialization are
REPRODUCTION of standard finite Gaussian/operator methods, with no
originality claim beyond the sources checked. No new assessment was
needed or written; the actual probes, generator, boundary conditions
and combined-response target are unchanged.

## Mathlib

Full coverage of (3), (5) and this particular stencil compression:
**not checked**. Supporting Gaussian moments, matrix polarization,
finite sums and tensor-product Laplacians: **not checked**. No matching
Mathlib theorem is asserted; unknown coverage is not claimed absence.
