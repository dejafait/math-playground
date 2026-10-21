# L046 — Exact companion trace comparison and an unverified separation test

## Hypotheses

Keep L008's exact two probes, tau=1/16, SU(2), fixed all-face box,
L030's selected upper-face one-internal-action-pair class, and
L040–L045's selected companion in the lower-rooted straight forest.
Take the small-coupling coefficient at fixed mesh before a=8/N tends
to zero through the admitted meshes. All operators in this lemma
are one-color continuum operators; L030 and L045 already include
their contraction and color factors.

On D_perp=(-4,4)^3 use L045's normalized Dirichlet modes psi_k,
lambda_k=(pi/8)^2|k|^2, k_j>=1 for j=2,3,4. Put
L=-sum_j partial_j^2, H=exp(-tau L), and let J be L031's isometry
J phi=8^(-1/2)e_1 phi, constant in x_1. Let Q_i^0 be the quadratic
form compression J*Q_i J of L008's actual one-color Q_i.

Write kappa=(1/8) integral rho(x_1) dx_1 and
Phi(y)=y_2 rho(y_2) rho(y_3) y_4 rho(y_4). Then L040's continuum
compressed displacement is
bar u_2=kappa partial_4 Phi, bar u_4=-kappa partial_2 Phi,
bar u_3=0. Put w_j=partial_j bar u_j and S=sum_j partial_j^2 w_j.
M_S denotes multiplication by S. Let c_* be exactly L042(2),
and J_i and I_i exactly L045 and L030 respectively.

## Conclusion

Define the absolutely convergent real mode sums

\[
 A_i=\sum_{k,l}\frac{e^{-\tau(\lambda_k+\lambda_l)}}{\lambda_k\lambda_l}
            (Q_i^0)_{kl}(M_S)_{lk},\qquad
 B_i=\sum_{k,l}\frac{e^{-\tau(\lambda_k+\lambda_l)}}{\lambda_k\lambda_l}
            (Q_i^0)_{kl}(Q_3^0)_{lk}.                       \tag{1}
\]

The exact companion comparison is

\[
 J_i=16 A_i+96 c_* B_i,\qquad 0<c_*\le\tfrac14,
 \qquad B_3>0.                                             \tag{2}
\]

Thus, for each i, J_i lies between the two exact endpoints
16 A_i and 16 A_i+24 B_i. This is a conditional interval in
unevaluated A_i,B_i, not a numerical enclosure. Equivalently,
A_i=Tr(H L^-1 Q_i^0 L^-1 H M_S) and
B_i=Tr(H L^-1 Q_i^0 L^-1 H Q_3^0), with the latter trace interpreted
by (1), or as the heat-sandwiched bounded-form trace below.

Only axial-zero transverse modes occur in (1). L031's I_i instead
retains its unrestricted second mode index, including other one-form
components and positive axial frequencies. Its projection is not
changed here. The combined selected power coefficient remains
J_i-48 I_i. The diagnostic below suggests that it is nonzero for
both probes, but does not prove that claim. No value or sign for
A_i, B_6, J_i or the combined coefficient, subleading power or
logarithm, full response, finite matching, interacting reflected error
<=c_box/2, continuum field content or finite physical mass is proved.

## Proof

### 1. Retain the actual compressed forms and all transitions

L040's axial compression removes Psi_13 from these blocks exactly.
Taking its continuum forms, or directly inserting J phi into L008(1),
gives

\[
 q_3^0(\phi)=\int\sum_j w_j(\partial_j\phi)^2,\qquad
 q_6^0(\phi)=\int\sum_{j<m}s^0_{jm}
                               \partial_j\phi\partial_m\phi,
 \quad s^0_{jm}=\partial_j\bar u_m+\partial_m\bar u_j.     \tag{3}
\]

The factors 8^-1/2 in the two fields supply 1/8, exactly the axial
average in bar u. For the triplet, the axial average of w_1 is zero
by compact support; only the transverse w_j remain. For the shear,
only transverse pairs with common curvature index alpha=1 remain;
their product has positive sign. Polarization of the shear has its
factor 1/2, consistent with L008 and L040. There is no extra color
factor in (3).

For explicit coefficient evaluation these formulas say

\[
\begin{split}
 w_2&=\kappa\partial_2\partial_4\Phi,\quad
 w_4=-w_2,\quad w_3=0,\\
 S&=\kappa(\partial_2^3\partial_4-
                         \partial_2\partial_4^3)\Phi,\\
 s^0_{23}&=\kappa\partial_3\partial_4\Phi,\quad
 s^0_{24}=\kappa(\partial_4^2-\partial_2^2)\Phi,\quad
 s^0_{34}=-\kappa\partial_2\partial_3\Phi.
\end{split}                                                \tag{4}
\]

These identities include the transition support of every rho.
None uses the affine-core formula as a global replacement.

### 2. Express L045's full functional as traces

By compression, beta_(i;k,l)=(Q_i^0)_(kl)/sqrt(lambda_k lambda_l).
L045(1) therefore gives the exact kernel

\[
 K_i(x,y)=8\sum_{k,l}
 \frac{e^{-\tau(\lambda_k+\lambda_l)}(Q_i^0)_{kl}}
      {\lambda_k\lambda_l}\psi_k(x)\psi_l(y).             \tag{5}
\]

All smooth coefficients in (3)–(4) are bounded. The relative form
bound gives |(Q_i^0)_(kl)|<=C_i sqrt(lambda_k lambda_l),
and |(M_S)_(kl)|<=||S||_infinity. The positive gap is
lambda_min=3(pi/8)^2. Consequently both sums in (1) are absolutely
convergent, using the full double heat sum. The same argument with
additional polynomial powers of the indices justifies differentiating
(5) and integrating it against the compact smooth coefficients.
This also follows from L045's already proved smooth convergence.

Integrating K_i(x,x) against S gives 8 A_i. Integrating
sum_j w_j partial_(x_j)partial_(y_j)K_i(x,y)|_(y=x)
gives 8 B_i by the bilinear triplet form in (3).
L045(4)'s factors 2 and 12 c_* thus give (2)'s identity.
This calculation does not introduce a second projection into I_i.

For an operator interpretation let beta_i=L^-1/2 Q_i^0 L^-1/2,
a bounded self-adjoint operator. Then
B_i=Tr(H beta_i H beta_3), as seen term by term in the eigenbasis.
Equivalently this is the Hilbert–Schmidt inner product of
H^(1/2) beta_i H^(1/2) and H^(1/2) beta_3 H^(1/2).
These operators are Hilbert–Schmidt because the heat trace is finite.
In particular B_3 is their squared norm. It is strictly positive:
L031(2) shows Q_3^0=-kappa(partial_2^2-partial_4^2) on compact core
tests and hence Q_3^0 is nonzero. For example phi=y_2^2 eta with eta
supported in the core and equal to one near zero has Q_3^0 phi
nonzero near zero. Thus beta_3 is nonzero. The heat half-operator
has dense range since every heat eigenvalue is positive; a zero
heat-sandwiched operator would imply beta_3=0 by continuity, a
contradiction. No sign for the mixed B_6 follows from this argument.

### 3. Bound the universal torus constant

In L042's normalized torus measure, each lambda_j=2-2 cos theta_j
is nonnegative and lambda=sum_j lambda_j. Thus
|lambda_2-lambda_3|<=lambda_2+lambda_3<=lambda.
Except at the irrelevant zero of lambda, L042's integrand is at
most lambda_4. Its integral is 2. Multiplying by 1/8 proves
c_*<=1/4, while L042's positivity proves c_*>0. Since (2) is
affine in c_*, the exact endpoint interval follows, regardless of
the sign of B_i. No numerical evaluation of c_* is needed for it.

### 4. Diagnostic evidence, with the missing verification retained

The reproduction command is
`OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_companion_functional.py`.
Full evidence is saved at
`scripts/combined-ward-response/companion-functional-certificate.json`.
Despite the filename, this artifact is explicitly a diagnostic,
not an enclosure certificate.

The script implements (1) through the existing weak coefficient
integrals: integration by parts moves every coefficient derivative
in (4) onto the trigonometric mode products. The axial constant
integrals supply kappa for each factor. Pairwise separability of
Phi reduces the double transverse sums to products of complete
one-dimensional tables. Each inverse factor is represented by
lambda^-1 exp(-tau lambda)=integral_tau^infinity exp(-s lambda) ds.
It uses both linear time weights; the auxiliary squared-inverse
diagnostic is checked with its corresponding (s-tau) weight.

Runs use cutoffs 4,24,40,56, coefficient-rule degrees 64,96,128,160,
and progressively refined log-time rules. At cutoff 4 a direct
dense mode contraction with exact-form inverse factors differs from
the separated time contraction by at most 8.89e-16, below the
diagnostic tolerance 1e-7. This checks two contraction implementations;
they share the weak coefficient assembly and do not independently
certify its algebra or arithmetic. The last two runs differ in their
A,B entries by at most 2.874e-5, below the declared refinement
tolerance 1e-4. The inverse-weight diagnostics pass their 1e-11
tolerance. These tolerances are checks, not error bounds.

The last diagnostic gives

\[
 (A_3,A_6)\approx(148.83170727,-147.77979268),\qquad
 (B_3,B_6)\approx(111.03741670,-32.21996993).
\]

Substitution into the exact endpoint formula suggests companion
ranges [2381.3073,5046.2054] and [-3137.7560,-2364.4766].
They are deliberately **not** asserted as enclosures. In contrast,
L039 rigorously retains, under its stated IEEE model,
48 I_3 in (21734.4,21760.8) and
48 I_6 in (160876.8,160972.32).
Those source intervals are unchanged. The diagnostic separation is
a reason to seek a coarse rigorous bound for J_i; it is not a
proof that the two selected classes fail to cancel. Complete relevant
verification still needs omitted-mode, coefficient/time quadrature,
and rounding bounds for this new companion calculation.

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`.
The primary general flow input remains Luescher–Weisz,
*Perturbative analysis of the gradient flow in non-abelian gauge
theories*, [arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2),
sections 7.1–7.4, (7.1)–(7.8), and section 8.2, with its ordinary
renormalization and R^4 hypotheses. It is not a theorem computing
these fixed-box compressed traces and is not reproved here. The
specialization uses the actual representatives and their normalization;
it reproduces standard spectral trace and quadrature methods. No
novelty claim, complete logarithm or nonperturbative bound follows.

## Mathlib

Coverage of the full selected companion comparison: **not checked**.
Coverage of supporting spectral traces, Hilbert–Schmidt products,
Dirichlet heat kernels and Fourier/quadrature enclosures: **not checked**.
No full matching theorem is asserted; unknown coverage is not absence.
