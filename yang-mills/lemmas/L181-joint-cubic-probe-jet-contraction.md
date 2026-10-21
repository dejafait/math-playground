# L181 — Joint cubic probe-jet contraction with the full flow integral

## Hypotheses

Use L011's fixed-mesh bare expansion for SU(2) in the relative box
(-4,4)^4, a=8/N through admitted even meshes, L008's complete compact
displacement, and both actual L010 probes at tau=1/16. Use the straight
direction-1 lower-rooted forest, including its upper pinned condition.
Small coupling is expanded at each fixed mesh before taking a limit.
All coordinates below are dimensionless x=theta/g, with ordinary
Euclidean adjoints and three independent colors.

Write I=I_F, Sigma=Sigma_F and A=A_F from L018(3). In this lemma Sigma
is the positive forest covariance, not L018's full Hodge inverse. Thus
r_0=sum_c (x^c)^T A x^c. Let n be the number of forest coordinates
and m the number of full variable links. The full matrices retain
forest links; fixed boundary links are omitted, with their group values
held at identity. Write

\[
 L=D_1^T D_1,\quad E_t=e^{-tL/a^2},\quad R_t=E_t I,\quad
 j_{i,2}(z)=\sum_c(z^c)^T Q_i z^c.                         \tag{1}
\]

Here Q_i is the full-coordinate symmetric matrix of the actual
quadratic numerator, as in L018(2); it is neither the flowed matrix
B_i nor a restricted forest Hessian. E_t retains its gradient kernel.
Use the full action Taylor polynomial s_3 and numerator j_(i,3) of
L011, and put S_3=s_3 composed with I. Use its complete r_1, including
both insertion subtractions, as specified in L155(2).

For an alternating real tensor h on link indices, define

\[
 P_h(x)=\sum_{r<s<t}h_{rst}\,x_r\cdot(x_s\times x_t)
       =\frac16\sum_{rst,cde}h_{rst}\epsilon_{cde}
                          x_r^c x_s^d x_t^e.                \tag{2}
\]

Define the full-space tensors c and d_i and the forest tensors b,h_i
by s_3=P_c, j_(i,3)=P_(d_i), r_1=P_b and f_(i,1)=P_(h_i).
These definitions are justified below, and specify the tensors without
any truncation: for increasing r,s,t extract the coefficient of
x_r^1 x_s^2 x_t^3 from the indicated polynomial, and extend alternatingly.
Let c_F be the analogous tensor of S_3. In particular, the full c
includes every action plaquette, including physical faces.

## Conclusion

The selected response

\[
 G_{i,a}=\kappa_0(f_{i,1},r_1)
                  -\kappa_0(f_{i,1},r_0,S_3),\qquad i=3,6,
\]

has the following exact fixed-mesh reduction. Set

\[
 T=2\Sigma A,\qquad
 \rho=r_1-D S_3(x)[Tx]=P_k(x),                              \tag{3}
\]
\[
 k_{rst}=b_{rst}-\sum_u\left(
 T_{ur}(c_F)_{ust}+T_{us}(c_F)_{rut}+T_{ut}(c_F)_{rsu}
 \right).                                                  \tag{4}
\]

Then

\[
 \boxed{G_{i,a}=\mathbb E_0[f_{i,1}\rho]
   =\sum_{rst,uvw}(h_i)_{rst}k_{uvw}
                  \Sigma_{ru}\Sigma_{sv}\Sigma_{tw}.}       \tag{5}
\]

All six index sums in (5) are unrestricted forest sums. There is no
additional factor 3 or 1/2 in this convention. Both cubics are pure
third Gaussian chaos: every internal pair vanishes, including those
that could arise after the quadratic tilt used to form the cumulant.
The effective residual rho is generally nonlocal because T contains
Sigma. Formula (3) does not claim a gauge-invariant or forest-invariant
separate insertion.

Here is an explicit full-flow version of (5). For full tensors u and
forest tensors v, define the finite sum

\[
 \mathcal T(u,v;X,Y,Z)
 =\sum_{\alpha\beta\gamma,rst}u_{\alpha\beta\gamma}v_{rst}
                  X_{\alpha r}Y_{\beta s}Z_{\gamma t}.
\]

Set Z_t=R_t Sigma and
Y_(i,s)=E_(tau-s) Q_i R_tau Sigma. The complete joint group is

\[
 \boxed{G_{i,a}
 =\mathcal T(d_i,k;Z_\tau,Z_\tau,Z_\tau)
 -\frac6{a^2}\int_0^\tau
       \mathcal T(c,k;Y_{i,s},Z_s,Z_s)\,ds.}                  \tag{6}
\]

The first term is the actual cubic observable jet. The integral is the
entire quadratic coordinate-flow contribution, including s=0. Both
probe sectors, all coefficient transitions, full link modes, physical
faces and the constant axial mode remain. The formula requires only
the existing local Taylor words, finite matrices and a finite-time
integral; no new matching or boundary prescription is introduced.

This is a finite signed reduction, not a proof of O(a^-3), a finite
a^3-scaled limit, or vanishing. Neither actual-probe coefficient is
evaluated. The remaining f_(i,2),r_0 term, finer powers/logarithm,
full compensation, finite matching, reflected error <=c_box/2 and
continuum/infrared construction remain unresolved. This specializes
standard Gaussian pairing and flow differentiation; it makes no claim
of progress beyond the sources checked in the approved assessment.

## Proof

### 1. The actual cubic probe and its color structure

Simultaneous conjugation by a fixed SU(2) element preserves the
identity boundary links, each action word and each probe trace/clover
product. The full Wilson-flow vector field is equivariant for this
conjugation. Exponential coordinates respect it, as does forest
restriction. Thus all four scalar cubics in the hypotheses are
invariant under a simultaneous SO(3) rotation of every color vector.
This argument does not require global conjugation to be one of the
boundary-rooted gauge transformations used to fix the forest.

For completeness, apply L155's invariant-cubic tensor argument to
these polynomials. A degree-three symmetric tensor on combined
link/color indices is invariant under the rotations by pi about the
color axes only if each color occurs once. Rotations by pi/2 then
make it alternating in colors. It is consequently a multiple of
epsilon_cde for every three link indices. Symmetry in combined slots
makes its link tensor alternating too. Its Taylor normalization is
precisely h_rst epsilon_cde/6 as in (2). This proves the asserted
representations, including the full f_(i,1), without assuming it is
a polynomial in linear curvature.

For any color-diagonal covariance C tensor identity_3, contracting two
slots in (2) sets two colors equal and gives zero. This holds for any
link covariance C, not merely Sigma. Each such cubic therefore equals
its Wick-ordered cubic, has mean zero, and has no first-chaos component.
The same statements hold for D S_3[Tx], since T acts only on link
indices. Neither gauge-gradient directions nor growing covariance
directions have been discarded.

### 2. Absorb the complete quadratic insertion

For sufficiently small real t the normalized quadratic tilt by
exp(t r_0) is a centered Gaussian with one-color covariance

\[
 \Sigma(t)=(\Sigma^{-1}-2tA)^{-1},\qquad
 \Sigma'(0)=2\Sigma A\Sigma.                                 \tag{7}
\]

Positivity holds on a neighborhood of zero at each fixed mesh by
positive definiteness of Sigma and continuity in t. Polynomial
moments may be differentiated there. No exponential moment of a
cubic is required. The finite cumulant definition in L011 gives

\[
 \kappa_0(f_{i,1},r_0,S_3)
   =\left.\frac d{dt}\mathbb E_t[f_{i,1}S_3]\right|_{t=0},    \tag{8}
\]

because each cubic mean vanishes throughout the tilt. Explicitly the
right side is E[f_(i,1)r_0 S_3]-E[r_0]E[f_(i,1)S_3]; the other
third-cumulant subtractions vanish by odd degree.

Use the named Isserlis Gaussian pairing theorem. By section 1, the
only nonzero pairings of two cubics are the six cross matchings. The
combined tensors are symmetric, so all six give the same summed
contraction. The color sum is sum epsilon_cde^2=6; the two tensor
normalizations are 1/6 each. Hence their product is 6*6/36=1, giving

\[
 \mathbb E_t[P_h P_v]
    =\sum h_{rst}v_{uvw}
                \Sigma(t)_{ru}\Sigma(t)_{sv}\Sigma(t)_{tw}.  \tag{9}
\]

Differentiating (9) inserts 2 Sigma A Sigma on each of the three
cross lines, once. The expectation E[P_h D P_v[Tx]] gives exactly
these three terms: the line incident on a transformed right slot is
Sigma T^T=2 Sigma A Sigma. This also fixes the order T=2 Sigma A;
replacing it by 2 A Sigma is not justified. Combining (8) and (9)
proves (3) and (5). Expanding the directional derivative in the three
slots of (2) gives (4). This proves the complete connected subtraction
and the single-action minus sign in the selected group.

### 3. Retain the full coordinate flow before contraction

L022's coordinate-flow identity is Q_2(z)=-a^-2 grad s_3(z), on the
full link coordinates. Its applicability here can also be checked
directly: if J(theta) is the differential of exp in the left frame,
then J(theta)=1+ad_theta/2+O(theta^2). The adjoint action is skew for
-2 Tr, so J^T J=1+O(theta^2). The coordinate gradient-flow metric has
no linear term. Since the action has no linear coefficient, its
quadratic vector-field coefficient is -a^-2 grad s_3. Thus no left-frame
quadratic coefficient has been substituted for the coordinate one.

L011(11)–(12) now give, with all gradients and pairings in full
link/color coordinates,

\[
 \begin{split}
 f_{i,1}(x)
 &=j_{i,3}(R_\tau x)
 -\frac2{a^2}\int_0^\tau
    \left\langle Q_i R_\tau x,
       E_{\tau-s}\nabla s_3(R_s x)\right\rangle\,ds\\
 &=j_{i,3}(R_\tau x)
 -\frac2{a^2}\int_0^\tau
    D s_3(R_s x)[H_{i,s}x],ds,\quad
 H_{i,s}=E_{\tau-s}Q_i R_\tau .                              \tag{10}
 \end{split}
\]

The factor 2 is from D j_(i,2), and self-adjointness of E_(tau-s)
justifies its displayed placement. Q_i is not commuted through any
semigroup or covariance. Formula (10) uses precisely the plaquette
triplet and clover-product shear of L010; their different j_(i,3)
remain in the first term.

Pair (10) with P_k in the forest Gaussian. For the first term (9)
gives T(d_i,k;Z_tau,Z_tau,Z_tau). The derivative of P_c has three
slot placements H_(i,s),R_s,R_s. Each gives the same scalar T after
pairing: exchange the corresponding two full indices and the two
forest indices together; the alternating tensors supply two minus
signs. Consequently their sum is 3 T(c,k;H_(i,s)Sigma,Z_s,Z_s).
This proves the -6/a^2 coefficient in (6).

At fixed mesh all spaces are finite dimensional, E_t is continuous
on [0,tau], and every integrand is a polynomial of degree six in a
fixed Gaussian. A finite coefficient bound on that compact interval
gives integrability and justifies interchanging this single time
integral and expectation. The bound may depend on a. Nothing here
permits interchanging this integral with mesh refinement.

### 4. Verification and the missing estimate

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_joint_cubic_probe.py`.
The complete certificate is
`scripts/combined-ward-response/joint-cubic-probe-certificate.json`.
Its 19 exact rational checks pass, with maximum discrepancy zero
against required discrepancy zero. An independent polynomial Gaussian
moment recursion checks (5) and (3) for two positive covariances,
two symmetric quadratic matrices (one indefinite and not commuting
with the second covariance), and two different cubic tensors. Two
rectangular full-space/forest tests check the factor -6 and all three
directional-derivative placements in (10). Those tests use rational
integrand maps and weights, not a quadrature of the actual flow.
A sign control with a determinant cubic, r_1=S_3 equal to that cubic,
identity covariance and r_0 the sum of all squares gives G=-30.
All of these are synthetic algebra checks, not either actual probe's
value or a proof of a cutoff bound.

The remaining estimate is specific. Z_0=I Sigma has no flow damping,
and E_s preserves its gradient kernel for every s. Moreover k contains
the nonlocal operator 2 Sigma A. L026's raw covariance growth and
L022's failed curvature-only transfer therefore cannot be bypassed by
assigning positive final flow time to all three lines in (6). No bound
on the full signed sum in a near-zero interval, nor a uniform remainder
for removing such an interval, has been proved here. The exact joint
subtraction is available for estimating it; it has not been replaced
by absolute estimates of separate cumulants. L019's nonlinear forest
compensation remains necessary for any claim about the full response.

## Mathlib

Full matching theorem and supporting Gaussian chaos, matrix tilt,
invariant tensors and flow differentiation: **not checked**. Unknown
coverage is not evidence of absence. The named standard input is
Isserlis' Gaussian pairing theorem; its connected and color-specific
specializations are proved above. The reused
[assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
records precise primary flow/Ward sources and why their full renormalized
statements do not settle this selected bare group. No general flow
renormalization theorem is reproved or used as a cutoff estimate.
