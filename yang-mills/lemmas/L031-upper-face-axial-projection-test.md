# L031 — Axial projection does not annihilate the leading residual

## Hypotheses

Keep L030's functional I_i, leading residual N_2, original two probes
i=3,6, relative box spectrum and tau=1/16. In particular the displacement
is precisely L008's sum of the 13 and 24 antisymmetric potentials;
neither the cutoff nor the probe weights are changed. All operators
below are one-color continuum operators. This is a test of the selected
upper-face action class, not of the complete Ward coefficient.

Let J:L^2(D_perp)->L^2(D;R^4) be the isometry
J phi=8^(-1/2) e_1 phi(x_2,x_3,x_4), and let P=JJ*. Its range is the
component-1, zero-axial-frequency subspace in L008's basis. Let Z be
the corresponding set of basis labels, and H=exp(-tau Delta).
The Q_i are L008's unflowed differential quadratic-form operators,
so B_i=Delta^(-1/2)Q_i Delta^(-1/2).

## Conclusion

There is the absolutely convergent signed formula

\[
 I_i=8\sum_{k\in Z}\sum_\ell
 \frac{e^{-\tau(\lambda_k+\lambda_\ell)}}{\lambda_k^2\lambda_\ell}
 (Q_i)_{k\ell}(N_2)_{\ell k}
 =8\sum_{k\in Z}\frac{e^{-\tau\lambda_k}}{\lambda_k^2}
 \langle Q_i f_k,H\Delta^{-1}N_2 f_k\rangle .       \tag{1}
\]

The second index in the double sum is unrestricted. In particular
the axial compression J*N_2 J alone does not determine I_i.

Define kappa=(1/8) integral_(-4)^4 rho(x_1) dx_1>0, using L008's
exact rho, and D_24=partial_2^2-partial_4^2. On every
phi in C_c^infinity((-5/2,5/2)^3), as identities of transverse functions,

\[
 J^*Q_3J\phi=-\kappa D_{24}\phi,\qquad
 J^*Q_6J\phi=0,\qquad
 J^*N_2J\phi=\frac{\kappa}{4}\partial_3^2D_{24}\phi. \tag{2}
\]

Consequently P N_2 P is not zero. More specifically,

\[
 \langle J^*Q_3J\phi,J^*N_2J\phi\rangle
 =\frac{\kappa^2}{4}\|\partial_3D_{24}\phi\|_2^2,   \tag{3}
\]

which is strictly positive for some such phi. This rules out an
identity annihilating the residual merely by the axial-zero projection.
It does **not** prove that I_3 or I_6 is nonzero or has any sign.
Equation (3) is an unweighted compressed pairing on compact tests;
equation (1) retains heat and inverse-Laplacian weights, every relative
mode, and transitions of the original displacement. No full logarithm,
compensating-jet identity, interacting bound or mass gap follows.

## Proof

### 1. Retain the unprojected second index

The adjoint of J is J*b=8^(-1/2) integral b_1 dx_1. Thus L030's
T=sqrt(8)J*, and T*T=8P. If k is in Z, write f_k=J psi_k for the
normalized three-dimensional Dirichlet mode psi_k. Then
T f_k=sqrt(8)psi_k; for other labels T f_k=0. Expansion of L030's
r_ell in these transverse modes gives

\[
 \langle T(\lambda_k^{-1/2}f_k),
 T(\lambda_\ell^{-1/2}\Delta^{-1}N_2f_\ell)\rangle
 =\frac{8(N_2)_{k\ell}}{
                  \lambda_k^{3/2}\lambda_\ell^{1/2}}
 \quad(k\in Z).
\]

Multiply by (B_i)_(k ell)=(Q_i)_(k ell)/sqrt(lambda_k lambda_ell).
The defining compositions of N_2 are formally self-adjoint with
compactly supported coefficients. Integration by parts on the smooth
relative modes therefore gives (N_2)_(k ell)=(N_2)_(ell k), without
physical-boundary terms. This proves the double-sum expression in (1).

These manipulations are absolutely convergent: L008 bounds
|(Q_i)_(k ell)| by C sqrt(lambda_k lambda_ell), and L030's differential
operator of order at most five gives
|(N_2)_(k ell)|<=C(1+|ell|)^5 by Cauchy–Schwarz and the explicit
normalized modes. There is a positive spectral gap, and both mode
indices have Gaussian heat weights. A polynomial times those weights
is summable over the four-dimensional mode labels. Symmetry provides
the corresponding bound with k and ell reversed when needed. Summing
over ell by the spectral action of H Delta^(-1) proves the second
formula in (1). No commutation of N_2 or Q_i with P or H was used.

### 2. Compress the exact formal stencil before extracting its coefficient

Use L030's formal parameter t, with equalities in this paragraph
understood modulo t^2. Write j,m for the transverse indices 2,3,4,
D_j(t)=partial_j+t partial_j^3/24 and
C_j(t)=1+t partial_j^2/8. Put

\[
 \bar u_j(t)=\frac18\int_{-4}^4 u_j(t)\,dx_1,
 \mathcal L(t)=-\sum_{j=2}^4D_j(t)^2,
 \mathcal K(t)=\sum_{j=2}^4\bar u_j(t)
                    (\partial_j+t\partial_j^3/6).
                                                        \tag{4}
\]

The identity L(t)J=J mathcal L(t) follows directly from d(t)J phi:
its only nonzero plane components are (1,j), equal to
-8^(-1/2)D_j(t)phi. Hence the compressed symmetric action variation is
(mathcal L mathcal K+mathcal K* mathcal L)/2. To check mathcal K,
K(t)'s component 1 uses only u_j(t)F_(j1); its endpoint average in
direction 1 disappears under the axial integral. The axial part of
the clover acts trivially on J phi. The remaining C_j(t)D_j(t) is
partial_j+t partial_j^3/6. All differentiated axial coefficients
integrate to zero by compact support. These facts prove (4), including
the factor 1/8; they do not discard any other component of K before
the compression with L.

For clarity, the compressed triplet quadratic form is
sum_j integral bar W_j(t)(D_j(t)phi)^2, where

\[
 \bar W_j(t)=C_j(t)\left\{
       \partial_j\bar u_j(t)+\frac t6\partial_j^3\bar u_j(0)
                         \right\}.                    \tag{5}
\]

Indeed the axial integral of w_1(t) is zero, and averaging the
remaining weight in the axial direction changes no integral. The
compressed shear form is

\[
 \sum_{j<m}\int \bar s_{jm}(t)
  (C_j(t)D_j(t)\phi)(C_m(t)D_m(t)\phi),             \tag{6}
\]

with bar s the axial average of L030's s(t). The pairs involving
index 1 contribute zero to (6), since for a component-1 input the
only common nonzero curvature component in a transverse pair is
alpha=1. Formula (6) retains the normalization of L008's shear.
Polarization of (5)–(6) gives the compressed Q_i(t).

The 13 potential contributes nothing to any of these compressed
operators: its only transverse velocity is u_3(t), an axial total
derivative, and its axial integral is zero. The same applies to its
order-t correction, involving partial_1^3 Psi_31. This statement is
about J*Q_i(t)J and J*N(t)J; it is not an assertion that this potential
can be removed from the unrestricted-index sum (1).

### 3. Compute on compact tests in the affine transverse core

In a neighborhood of the support of phi, rho(x_j)=1 for j=2,3,4.
The 24 potential in (4) therefore gives
bar u_2(t)=kappa x_2, bar u_4(t)=-kappa x_4, bar u_3(t)=0, with
zero order-t correction. Every transverse third derivative entering
that correction vanishes there. Thus (5) has constant weights
(kappa,0,-kappa), and (6) vanishes through order t. The derivatives
of phi remain supported in this core, so these local formulas give
global identities for the resulting compactly supported functions.

Write S=partial_2^2+partial_3^2+partial_4^2 and
A_4=partial_2^4-partial_4^4. The coefficients of (4) on this support are

\[
 \mathcal L_0=-S,\quad
 \mathcal L_2=-\tfrac1{12}\sum_{j=2}^4\partial_j^4,
 \quad \mathcal K_0=\kappa(x_2\partial_2-x_4\partial_4),
 \quad \mathcal K_2=\tfrac\kappa6
                 (x_2\partial_2^3-x_4\partial_4^3).
\]

Here subscripts 2 denote the coefficient of t=a^2. Compact-test
integration by parts gives mathcal K_0*=-mathcal K_0 and
mathcal K_2*=-mathcal K_2-(kappa/2)D_24. Using
[partial_j^r,x_j partial_j^s]=r partial_j^(r+s-1), the coefficient
of t in the symmetric action variation is

\[
 \frac{[\mathcal L_0,\mathcal K_2]
          +[\mathcal L_2,\mathcal K_0]}2
                  -\frac\kappa4D_{24}\mathcal L_0
       =-\frac\kappa3 A_4+\frac\kappa4D_{24}S.      \tag{7}
\]

The triplet coefficient from (5) is -kappa A_4/12, and the shear
coefficient is zero. Subtract them as in L030(8). Since
D_24 S-A_4=partial_3^2 D_24, this yields (2). All adjoints here
differentiate the affine multipliers; omitting their derivatives
would change (7).

Finally integration by parts in x_3 proves (3). For an explicit
nonzero test choose phi=x_2^2 x_3^2 eta(y), where eta is smooth,
supported in the transverse core and equal to one near the origin.
Then partial_3^2 D_24 phi=4 near the origin, so the last operator in
(2) is nonzero. Also partial_3 D_24 phi=4x_3 in that neighborhood,
making (3) strictly positive. These are legitimate compact tests
in the range of J, not a replacement for the two specified probes.

The general flow and matching literature in the saved SPECIALIZE
assessment is reused as context, not as a theorem assigning a value
to (1). The calculation above is needed for the actual residual
stencil and forest projection and does not reprove flow finiteness.

## Mathlib

Coverage of the full projected residual and signed functional:
not checked. Coverage of the supporting spectral, differential and
integration-by-parts identities: not checked. No matching formal
theorem or certified sign of I_i is asserted.
