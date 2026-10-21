# L021 — All pairings of the selected radial cubic flow vertex vanish

## Hypotheses

Keep L020's conventions, including the SU(2) box with relative boundary
conditions, tau = 1/16, L010's two actual probes, and the fixed-mesh
small-coupling coefficient of L011. Select the same summand of the cubic
coordinate-flow field as in L020:

\[
Q_{3,\mathrm{rad}}(\theta)
 =\frac1{24a^2}D^*(|D\theta|^2D\theta),\qquad D=ad.
\tag{1}
\]

Include this summand in z_3 and hence in D j_(i,2)(z_1) z_3, the first
term of f_(i,2) in L011. Call the resulting entire quartic polynomial
p_(i,a)^rad. This definition includes **all** its Wick pairings with the
quadratic residual r_0. It does not include the radial action insertion
elsewhere in L011's expansion, other cubic flow summands, two quadratic
flow vertices, or higher jets of the observable itself.

Write E_t = exp(-t Delta) for the relative one-form Hodge heat operator,
Q_i for the one-color quadratic probe operator, and
B_i = Delta^(-1/2) Q_i Delta^(-1/2). In orthonormal cochain coordinates,
let A^c = Delta^(-1/2) xi^c with three independent standard Gaussian
vectors xi^c. Write the leading residual as

\[
r_0=\sum_{c=1}^3(\xi^c)^T R_a\xi^c+\text{constant},
\]

with symmetric R_a. L020 establishes ||R_a|| <= C/a, uniform boundedness
of B_i and Tr(E_tau), and the integrated heat-diagonal estimates used
below. Matrix adjoints below are Euclidean transposes in these
orthonormal bases.

## Conclusion

The complete selected radial flow contribution to each response obeys

\[
G_{i,a}^{\mathrm{rad}}
=\operatorname{Cov}_0(p_{i,a}^{\mathrm{rad}},r_0)=O(a),
\qquad i=3,6.
\tag{2}
\]

More explicitly, set, for 0 <= s <= tau,

\[
H_s=d E_s\Delta^{-1/2},\qquad
Z_{i,s}=d E_{\tau-s}Q_i E_\tau\Delta^{-1/2},
\]
\[
v_p=(H_sH_s^*)_{pp},\quad
\alpha_p=(Z_{i,s}H_s^*)_{pp},\quad
\beta_p=(H_sR_aH_s^*)_{pp},\quad
\delta_p=(Z_{i,s}R_aH_s^*)_{pp}.
\]

Then the exact finite-mesh formula is

\[
G_{i,a}^{\mathrm{rad}}
 =\frac52\int_0^\tau\sum_p
       (v_p\delta_p+\alpha_p\beta_p)\,ds.
\tag{3}
\]

The first term is L020's internal tadpole. The second contains every
remaining connected pairing, and separately is O(a). Thus this entire
selected summand has no unsuppressed log(sqrt(tau)/a) contribution.
This statement assigns no logarithmic coefficient or cutoff bound to
the complete Gamma_(i,a), and gives no interacting reflected-error bound
against c_box/2.

## Proof

### 1. Normalize the actual flow summand

All cochain inner products have weight a^4. A stored coordinate vector
therefore becomes an orthonormal coordinate vector by multiplication
by a^2. The numerical matrices of d and its adjoint are unchanged by
this simultaneous scaling of the one-form and two-form spaces.

In stored coordinates z_1(s) = a exp(-s d*d) A. Its circulation is
Y = D z_1(s) = a^2 d E_s A, since curvature kills the longitudinal
part. Consequently, in the whitened coordinates used here, the stored
circulation is precisely

\[
Y_p^c=(H_s\xi^c)_p.
\tag{4}
\]

By variation of constants in L011, the radial contribution to the
physical connection jet z_3/a, in stored coordinates, is

\[
\frac1{24a^2}\int_0^\tau
 E_{\tau-s}d^*(|Y|^2Y)\,ds.
\]

The use of E is legitimate because d* has transverse range. Multiplying
by a^2 to obtain its orthonormal coordinates removes the displayed
power of a. Polarizing the actual quadratic probe and moving its
operators onto the outer leg gives the exact polynomial

\[
p_{i,a}^{\mathrm{rad}}
 =\frac1{12}\int_0^\tau\sum_{p,c,b}
       (Z_{i,s}\xi^c)_p
       (H_s\xi^b)_p(H_s\xi^b)_p(H_s\xi^c)_p\,ds.
\tag{5}
\]

Here 1/12 is the factor 2 from polarization times the 1/24 in (1).
This also checks the bare probe normalization: j_(i,2)(z) is
q_(i,a)(z/a), as in L020.

The selected polynomial (5) depends only on the linear curvature of
its input: the source of the radial correction uses d E_s A, and the
outer probe operator kills gradients. The leading r_0 also depends
only on the linear curvature. Thus the same finite Gaussian quotient
argument used in L020 transfers their joint law from the forest to
the Hodge Gaussian. This reasoning does not transfer a general
nonlinear forest vertex or its Haar density.

### 2. Exhaust the connected Wick pairings

Fix p,s and suppress those indices. Let h,z be the corresponding rows
of H_s,Z_(i,s); then Y^c = h xi^c and X^c = z xi^c. There are n = 3
independent colors, with common v = h h*, alpha = z h*.

The exact cubic Wick decomposition is

\[
\sum_b Y^bY^bY^c
 =\sum_b:Y^bY^bY^c:+(n+2)vY^c.
\tag{6}
\]

The second term yields the internal contribution

\[
(n+2)v\operatorname{Cov}\left(\sum_c X^cY^c,r_0\right)
 =2n(n+2)v\,zR_a h^*.
\tag{7}
\]

To treat the first term, multiplication by X^c can contract X with
one of its three Wick-ordered inputs, or leave a fourth-order
Wick polynomial. The latter has zero covariance with the quadratic
r_0: in a six-field pairing two residual legs cannot pair all four
Wick-ordered legs. A contraction with Y^c gives
alpha sum_b :Y^bY^b:, while the other two contractions give
2 alpha :Y^cY^c:. Summing over c leaves

\[
(n+2)\alpha\sum_b:Y^bY^b:.
\]

Its covariance with r_0 is

\[
2n(n+2)\alpha\,hR_a h^*.
\tag{8}
\]

Equations (7)–(8) exhaust the covariance: pairing the two residual legs
with each other is exactly the disconnected subtraction, while every
remaining pairing either contracts two cubic inputs internally or
contracts X with one cubic input. No independence of different
plaquettes is assumed. Multiplication by 1/12 in (5) gives
2n(n+2)/12 = 5/2 and proves (3).

The script
`python3 scripts/combined-ward-response/check_radial_remaining_pairings.py`
independently enumerates the connected six-field pairings for 24 exact
rational cases, using one through four colors and symmetric residual
matrices including an indefinite one. It checks (7) and (8) separately.
The argument above, rather than the finite tests, proves the identity
for every mesh and the actual probes.

### 3. Bound every remaining pairing uniformly

For the second term of (3), positivity of h h* gives

\[
|\beta_p|\le\|R_a\|v_p.
\tag{9}
\]

For any finite real square matrix T,
sum_p |T_pp| <= ||T||_1. Indeed choose a diagonal matrix of signs S
so that Tr(ST) = sum_p |T_pp| and use ||S|| <= 1 and trace-norm
operator-norm duality. It follows that

\[
\sum_p|\alpha_p\beta_p|
 \le\|R_a\|\|V_s\|\|Z_{i,s}H_s^*\|_1,
\qquad V_s=\operatorname{diag}(v_p).
\tag{10}
\]

The matrix in this bound factors as

\[
Z_{i,s}H_s^*
 =[dE_{\tau-s}\Delta^{1/2}]B_i E_\tau H_s^*.
\tag{11}
\]

The norm of H_s is at most one. The first factor in (11) is
(d Delta^(-1/2)) Delta E_(tau-s), so its norm is at most
||Delta E_(tau-s)||. The uniform bounds for B_i and Tr(E_tau)
therefore give

\[
\|Z_{i,s}H_s^*\|_1
 \le C_i\|\Delta E_{\tau-s}\|
 \le\begin{cases}
 C_i'&0\le s\le\tau/2,\\
 C_i''a^{-2}&\tau/2\le s\le\tau.
 \end{cases}
\tag{12}
\]

The first case uses sup_(lambda>=0) lambda exp(-tau lambda/2)
<= 2/(e tau), and the second uses the lattice spectral bound
||Delta|| <= 16/a^2. No commutation of B_i or V_s with heat is used.

L020 proves, uniformly up to the physical faces,

\[
\int_0^\tau\|V_s\|ds\le Ca^2,\qquad
\sup_{\tau/2\le s\le\tau}\|V_s\|\le C_\tau a^4.
\tag{13}
\]

Combining (10)–(13) and ||R_a|| <= C/a gives

\[
\left|\frac52\int_0^\tau\sum_p\alpha_p\beta_p\,ds\right|
 \le\frac{C_i}{a}\left(a^2+a^{-2}a^4\right)
 \le C_i'a.
\tag{14}
\]

The first term of (3) is exactly L020's contribution and is O(a)
there. This proves (2). The proof uses the finite-box relative kernels
and includes s approaching zero; it discards neither boundary modes
nor the cutoff-scale part of the time integral.

### 4. Scope and relation to the checked literature

This completes the pairings of one actual flow summand in
kappa_0(f_(i,2),r_0). The radial quartic action can still occur in other
terms of L011; those terms are not bounded by (2). BCH and coordinate
metric contributions to Q_3, the DQ_2 z_2 contribution, and action,
measure and insertion corrections remain unevaluated. Neither a zero
full logarithm nor absence of faster terms in the full sum follows.
The required interacting bound <= c_box/2 is unchanged, as are the
continuum, reflection positivity, infrared and mass-gap gaps.

This is a local specialization/reproduction of Wick and heat/trace
estimates, not an asserted discovery beyond the checked literature.
The [saved SPECIALIZE assessment](../drafts/literature/2026-09-26-current-target.md)
records Luescher–Weisz,
[arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2), sections 7 and 8.2,
as supporting bulk flow-renormalization context. That theorem does not
evaluate this specified bare-normalized finite-box summand. The present
calculation extends L020 only by its previously excluded pairings; it
does not reprove general flow renormalizability.

## Mathlib

Coverage of the full selected-vertex bound: **not checked**. Coverage
of supporting Wick products, Gaussian polynomial orthogonality,
trace-norm duality and relative heat estimates: **not checked**.
No Mathlib theorem is asserted to match the full statement. The named
primary source above is supporting context, not a full match.
