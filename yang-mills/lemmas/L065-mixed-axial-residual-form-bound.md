# L065 — Axial-zero to all-axial component-1 residual bound

## Hypotheses

Use L018's ordinary dimensionless full-link coordinates and actual
residual

    A_0=(L_0 K_a+K_a^T L_0)/2-Q_3-Q_6,  L_0=D_1^T D_1.

Keep L009's endpoint-averaged clover generator, L028's centered
coefficient/adjoint stencils, L008's actual triplet and shear forms,
the compact displacement, and sufficiently fine admitted even meshes
a=8/N in the fixed box. Coefficients and their first physical finite
differences are uniformly bounded and supported away from every face,
including the neighboring stencils. No replacement of the triplet
average of squares by a clover square is made.

Let I_1 insert all component-1 links, with N axial edge positions and
three pinned transverse vertex coordinates. Put

    A_11=I_1^T A_0 I_1,   Sigma_1=I_1^T Sigma I_1,
    H_T=I_N tensor Delta_3,   G=Delta_3^(-1),

where Delta_3 is the pinned transverse vertex Laplacian. Let e_0
insert the normalized constant axial edge mode, so E_0=I_1 e_0 is
exactly L040's embedding. Sigma is the full Hodge covariance, not
the forest covariance applied to unmodified higher vertices.

## Conclusion

The retained mixed operator from the prior continuation satisfies

    R_01=G^(1/2) E_0^T A_0 I_1 Sigma_1^(1/2),
    ||R_01|| <= C,

with C independent of N. All axial frequencies on its right remain.
In particular this extends the relevant residual estimate beyond
L041's double axial-zero compression; no mixed full-vector residual
bound is asserted. In the proof, the scalar diagonal form obeys

    |f^T A_11 f| <= C f^T H_T f.                         (1)

The bound removes the generic O(N) whitened-residual loss for the
pure component-1 input block. It does not estimate the direct
transverse input, finish any complete signed term of L064, supply a
mixed a²-scaled limit, or compute a logarithm. The first pair, other
response terms, forest compensation and the reflected-error bound
<=c_box/2 remain open, as do the continuum and mass requirements.
This is local specialization/reproduction of finite stencil energy
and commutator methods, with no claim of originality beyond the
sources checked in the saved response assessment.

## Proof

### 1. Keep the exact scalar generator outputs

Write f for an arbitrary real component-1 field, including all N
axial edge coordinates. In each transverse direction mu=2,3,4 let
D_mu be the pinned vertex-to-edge difference, C_mu the edge-to-vertex
average, and T_mu=C_mu D_mu. In the axial direction C_1 maps the N
edge entries to their averages at the N-1 interior vertices; D_v
maps pinned axial vertices to edges. These maps are dimensionless.
All C maps have operator norm at most one. Set h=C_1 f.

For x=I_1 f only the (mu,1) curls are nonzero, equal to D_mu f.
L009's exact linear generator and L028's adjoint conventions give

    (K_a x)_1=C_1^T k h,
    k h=a^(-1) sum_mu M_(u_mu) T_mu h,
    (K_a x)_mu=-a^(-1) C_mu^T M_(u_1) T_mu h.             (2)

The coefficients u here are the actual u_a on four-dimensional
vertices. They are not averaged over the axial direction. The first
identity retains both axial endpoint averages: h on the input and
C_1^T on the output. Other outputs in (2) cannot be omitted just
because the input has only component 1.

Since only (mu,1) curls of x contribute to its pairing, (2) yields
the exact identity

    <D_1 x,D_1 K_a x>
      =sum_mu <D_mu h,D_mu k h>
       +a^(-1) sum_mu <y_mu,D_v M_(u_1) C_1 y_mu>,
    y_mu=C_mu D_mu f.                                    (3)

Indeed the (mu,1) curl of K_a x is D_mu(K_a x)_1 minus
D_v(K_a x)_mu. Move C_1^T or C_mu^T onto D_mu f, respectively;
maps in different coordinates commute. The minus in (2) gives the
plus in the second line of (3). Thus no cross-component generator
output or derivative of a coefficient has been lost.

### 2. Transverse transport with variable axial coefficients

Let L be a uniform bound on |u_r(z+a e_j)-u_r(z)|/a for every
coefficient and coordinate needed below, including the zero exterior
extension. Such a bound exists by compact support and L028's uniform
smooth coefficient extensions. Fix one axial vertex layer. Extend
its pinned transverse fields by zero to the infinite grid. Every
coefficient term in (3) has an interior stencil, so this computes
the finite-grid pairing exactly, with no physical-boundary term.

Use D_j=S_j-I and T_j=(S_j-S_j^(-1))/2 on this extension. The exact
product rule is

    D_j k h=k^(j) D_j h
               +sum_mu M_(D_j u_mu/a) T_mu h,
    k^(j)=a^(-1) sum_mu M_(S_j u_mu) T_mu.                 (4)

Because T_mu is skew-adjoint, the symmetric part of each transport
summand in k^(j) is [M_(S_j u_mu),T_mu]/(2a). Expanding this
commutator gives two shifts with coefficients equal to adjacent
differences of S_j u_mu, with magnitude at most a L/2 before the
additional division by 2a. Its norm is therefore at most L/2.
The three summands give

    |<D_j h,k^(j)D_j h>| <= (3L/2)||D_j h||².

For the remaining products in (4), ||T_mu h||<=||D_mu h||;
this follows directly from T_mu=C_mu D_mu and ||C_mu||<=1.
The coefficient multipliers D_j u_mu/a have norm at most L.
If E_j=||D_j h||, summing these terms gives at most
L(sum_j E_j)^2<=3L sum_j E_j². Consequently, on this layer,

    |sum_j <D_j h,D_j k h>|
                      <= (9L/2) sum_j ||D_j h||².         (5)

Sum (5) over every axial vertex layer. No axial localization or
regularity of f was used. Axial averaging is a contraction and
commutes with D_mu, so the right side is at most
(9L/2) sum_mu ||D_mu f||².

### 3. Exact axial derivative/average cancellation

Fix a transverse vertex and one y_mu column. Write its axial edge
entries as y_0,...,y_(N-1), and write u_j for the actual u_1 at
axial vertex j, with u_0=u_N=0. For the pinned incidence convention
(D_v z)_r=z_(r+1)-z_r, direct summation gives

    <y,D_v M_u C_1 y>
      =sum_(j=1)^(N-1) (u_j/2)(y_(j-1)²-y_j²)
      =(1/2) sum_(r=0)^(N-1) (u_(r+1)-u_r)y_r².           (6)

To see the first equality, vertex j contributes
u_j(y_(j-1)-y_j)(y_(j-1)+y_j)/2. Cross products cancel
exactly. The second equality includes both end edges and uses only
the stated pinned coefficient values. Thus the constant-coefficient
derivative/average part cancels in the quadratic form; no estimate
of an axial derivative of the rough field is necessary.

Using |u_(r+1)-u_r|<=a L and ||C_mu||<=1, the second term in (3)
has magnitude at most

    (L/2) sum_mu ||C_mu D_mu f||²
                    <= (L/2) sum_mu ||D_mu f||².          (7)

Together (5) and (7) bound the complete generator form by
5L sum_mu ||D_mu f||². All pinned axial end edges were retained.

### 4. Subtract the actual two curvature forms

For this pure component input, Q_3 has just the three (1,mu)
curvature squares with their actual four-vertex averaged weights.
Let W uniformly bound these edge/plaquette weights in magnitude.
Then |x^T Q_3 x|<=W sum_mu ||D_mu f||². This step uses the
weights of the average of squares, as in L040, not clover squares.

For Q_6 only transverse pairs mu<nu with common index 1 survive.
Its quadratic form is

    sum_(2<=mu<nu<=4) <T_mu h,M_(s_mu nu) T_nu h>.

This is L028's exact clover composition before axial averaging;
polarization has the same symmetric cross-entry factor 1/2 as
L040. If S bounds |s_mu nu|, its magnitude is at most
S sum_(mu<nu) ||D_mu h||||D_nu h|| <= S sum_mu ||D_mu f||².
All pairs involving index 1 have a zero transverse-plane curvature
factor on this input. They vanish by the input restriction, not by
a claim about the full residual.

The quadratic form of (L_0 K_a+K_a^T L_0)/2 is precisely (3).
Subtracting Q_3,Q_6 proves (1), for example with C=5L+W+S,
uniformly over sufficiently fine admitted meshes. A finite number
of other admitted meshes may be included by increasing C.

### 5. Polarize before applying the mixed covariances

H_T is positive definite because its three transverse directions
have pinned vertex conditions. Since A_11 is symmetric, (1) implies

    F=H_T^(-1/2) A_11 H_T^(-1/2),  ||F||<=C.              (8)

This follows from the finite-dimensional spectral theorem applied
to its quadratic form, and supplies the corresponding bilinear
bound. It does not assume that A_11 or the residual is positive.

L026's full relative tensor spectrum gives

    Sigma_1=(Delta_edge tensor I + H_T)^(-1),

where Delta_edge is the axial Neumann edge Laplacian and has zero
mode N^(-1/2). It commutes with H_T. Hence
||H_T^(1/2) Sigma_1^(1/2)||<=1. The exact normalized zero-mode
embedding also satisfies

    G^(1/2) e_0^T H_T^(1/2)=e_0^T,  ||e_0^T||=1.

Insert (8) into the actual proposed operator:

    R_01=G^(1/2) e_0^T A_11 Sigma_1^(1/2)
         =e_0^T F H_T^(1/2) Sigma_1^(1/2).

Taking norms proves ||R_01||<=C with no discarded axial modes,
no smooth-input assumption and no generic O(N) residual bound.
Only the scalar component block has been bounded.

### 6. Verification and scope

Run from the notebook:

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/combined-ward-response/check_mixed_axial_residual.py

The full certificate is
`scripts/combined-ward-response/mixed-axial-residual-certificate.json`.
All 349 rational quadratic-basis checks of (6) pass for N=2,4,8,24.
Three binary64 N=24 actual-generator diagnostics, including varying
axial fields, check (3)+(6) with defects 7.96e-13, 6.73e-11 and
8.30e-12, below their stated 6.82e-9, 9.37e-8 and 1.15e-8
tolerances. These finite diagnostics detect stencil/sign errors;
they do not prove a uniform norm or asymptotic limit. Sections 1–5
give the analytic bound with all frequencies and endpoints retained.

This estimate neither replaces the forest cubic vertices by Hodge
ones nor claims that L064's actual trace is O(N²). In particular the
direct transverse component of the right forest lift remains outside
(8), and the left multipliers, right path maps and heat coefficients
must still be composed in their actual order. Other/other cubic pairs,
measure, insertion/flow jets, nonlinear forest compensation and all
nine placements for subleading powers and logarithms remain needed.

## Mathlib

Coverage of the full mixed residual operator statement: **not checked**.
Supporting finite spectral calculus, symmetric quadratic-form bounds,
polarization, contraction norms, discrete product rules and exact
pinned summation identities: **not checked**. No matching theorem or
absence claim is made. This proof specializes the actual local
stencils; the general perturbative flow and stress-renormalization
inputs are reused from the saved primary-source assessment, not reproved.
