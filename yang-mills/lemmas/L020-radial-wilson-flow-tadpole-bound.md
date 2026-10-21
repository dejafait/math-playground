# L020 — An internal radial Wilson-flow tadpole vanishes in both responses

## Hypotheses

Keep exactly L010's SU(2) box, relative boundary links, displacement,
two probes, and tau = 1/16. Use L011's full exponential coordinates,
forest Gaussian, and flow jets z_1,z_2,z_3. All statements about
perturbative coefficients take g to zero at fixed a first.

Let d be the relative edge-to-plaquette differential, D = a d its
unscaled incidence, Delta the relative one-form Hodge Laplacian, and
L = d* d. Inner products have weight a^4. Let E_t = exp(-t Delta).
On transverse one-forms E_t equals exp(-t L). Let Q_i be the symmetric
operator of the one-color form q_(i,a) in L008, and put

\[
B_i=\Delta^{-1/2}Q_i\Delta^{-1/2},\qquad i=3,6.
\]

The local plaquette logarithm w_p(theta) has linear term (D theta)_p.
Select from the full fourth-order Wilson numerator the particular term

\[
S_{4,\mathrm{rad}}(\theta)=-\frac1{96}\sum_p|(D\theta)_p|^4.
\tag{1}
\]

Select its Euclidean-gradient contribution to the cubic coordinate-flow
field, then in that cubic vertex select only Wick pairings of two of its
three input fields **with each other**. Call this its internal tadpole.
Do not include contractions of a vertex input with the outer quadratic
probe leg in this definition. This selection is a specified summand of
L011's coefficient, not a gauge-invariant grouping of the full interacting
expansion and not the entire radial-vertex contribution.

## Conclusion

For each color let

\[
v_{p,a}(s)=\mathbb E_F[(D z_1(s))_p^c{}^2],\qquad
V_s=\operatorname{diag}(v_{p,a}(s)).
\tag{2}
\]

These variances do not depend on the color or forest. Uniformly over all
plaquettes, including those adjacent to physical faces, for 0 < s <= tau,

\[
0\le v_{p,a}(s)\le \min\{1,Ca^4s^{-2}\},\qquad
\int_0^\tau\|V_s\|\,ds\le C'a^2.
\tag{3}
\]

In physical connection coordinates the selected internal pairing in z_3
is the linear map

\[
T_a A=\frac5{24}\int_0^\tau
 E_{\tau-s}d^*V_s d E_s A\,ds.
\tag{4}
\]

Gradients on the input are killed, so (4) also specifies its value on
the forest representative. With three independent Hodge Gaussians A^c,
the selected term in f_(i,2) is

\[
p_{i,a}^{\mathrm{tad}}=
2\sum_{c=1}^3\langle E_\tau A^c,Q_iT_a A^c\rangle_a.
\tag{5}
\]

Let r_0 be L011's full leading residual, equivalently L009's quadratic
residual up to its irrelevant additive constant. The selected contribution
to Gamma_(i,a) is

\[
G_{i,a}^{\mathrm{tad}}
=\operatorname{Cov}_0(p_{i,a}^{\mathrm{tad}},r_0),\qquad
|G_{i,a}^{\mathrm{tad}}|\le C_i a\quad(i=3,6).
\tag{6}
\]

Thus this particular internal contraction has no unsuppressed
log(sqrt(tau)/a) term. No bound is asserted for the other pairings of the
same vertex, for the other flow vertices, or for the complete Gamma.
The constants can depend on this box, displacement, and fixed tau.
There is no bound on the interacting reflected error required to be
at most c_box/2.

## Proof

### 1. Locate the term in the actual coordinate flow

For SU(2), in the convention of L010,

\[
4P_p=4(1-\cos(|w_p|/2))
=\tfrac12|w_p|^2-\tfrac1{96}|w_p|^4+O(|w_p|^6).
\]

Substitute w_p = D theta + w_(p,2) + w_(p,3) + ... . The fourth-order
terms are one half |w_(p,2)|^2, the product (D theta)_p dot w_(p,3),
and (1). In full product exponential coordinates the metric equals the
Euclidean metric at zero and has no linear term. One can see the latter
directly from the differential of exp: its linear correction is one half
ad(theta), skew-adjoint for the invariant inner product, and hence cancels
in its metric Gram matrix. The quadratic inverse-metric correction times
the quadratic action contributes a different cubic vector field. It does
not alter the summand -a^-2 grad S_(4,rad), which is exactly

\[
Q_{3,\mathrm{rad}}(\theta)
=\frac1{24a^2}D^*(|D\theta|^2D\theta).
\tag{7}
\]

This identifies a summand of L011's genuine coordinate Q_3; it does not
replace coordinate derivatives by left-frame derivatives. The BCH terms,
the inverse-metric correction, and DQ_2 z_2 remain outside the selection.

At each plaquette, Y = D z_1(s) has three independent Gaussian color
components of common variance v. The exact Wick decomposition is

\[
|Y|^2Y^c=\sum_{b=1}^3:Y^bY^bY^c:+5vY^c.
\tag{8}
\]

There are three contractions pairing the repeated b components and two
additional contractions when b = c. This proves the factor 5 without
assuming different plaquettes are independent. Insert the linear part
of (8) into (7) and L011's variation-of-constants formula for z_3.
Since D = a d and z_1(s) = a exp(-s L) A in connection coordinates,
division by a gives the factor 5/24 in (4). Both d*'s range and the
curvature of the input are transverse, where exp(-t L) may be replaced
by E_t. Polarizing j_(i,2) gives (5).

The polynomials now used in (2), (4), (5), and r_0 are invariant under
the linear gauge shifts A -> A + d_0 phi. L003's Gaussian quotient
therefore transfers their joint law from the forest to the Hodge law.
This transfer is justified for this selection only; it transfers no
general nonlinear vertex or forest-coordinate density.

### 2. The internal loop has an integrable cutoff-scale bound

Let Delta_2 denote the relative two-form Hodge Laplacian and P_ex the
orthogonal projection onto exact two-cochains. The finite cochain
identities give d Delta = Delta_2 d and
d Delta^-1 d* = P_ex. The latter follows either by decomposing into
exact/coexact modes, or by observing that d Delta^-1 d* acts as identity
on im d and as zero on its orthogonal complement. There are no relevant
zero modes in this relative box. These operators commute with their
respective heat operators.

In stored point coordinates, a Hodge Gaussian has covariance
a^-4 Delta^-1. The plaquette circulation is a^2 d A, so its covariance
at time s is, with these factors canceled,

\[
C_Y(s)=d\Delta^{-1}E_{2s}d^*
=P_{\rm ex}\exp(-2s\Delta_2).
\tag{9}
\]

Consequently v_p(s) is a diagonal entry of this matrix. The operator in
(9) lies between zero and both identity and exp(-2s Delta_2), proving
v_p <= 1 and bounding it by the two-form heat diagonal.

For completeness the latter diagonal estimate holds up to the faces.
For a component dx_mu wedge dx_nu the relative product modes have edge
cosines in directions mu,nu and vertex sines in the other two directions.
The allowed indices are 0,...,N-1 in a cosine direction and 1,...,N-1
in a sine direction. They are obtained from the same one-dimensional
relative incidence pairs as L003's one-form modes. Each factor, normalized
in the unweighted stored-coordinate Euclidean norm, has squared value
at most 2/N. Every four-dimensional product hence has squared value at
most 16/N^4 = a^4/256. Its eigenvalue is the sum of the four frequencies
4a^-2 sin^2(pi k/(2N)), bounded below by |k|^2/16. Thus uniformly in p,

\[
(e^{-2s\Delta_2})_{pp}
\le C a^4\sum_{k\in\mathbb N_0^4}e^{-s|k|^2/8}
\le C_\tau a^4s^{-2},\qquad 0<s\le\tau.
\tag{10}
\]

The last estimate follows by multiplying the four one-dimensional bounds
sum_(k>=0) exp(-s k^2/8) <= 1 + integral_0^infinity exp(-s x^2/8) dx.
Allowing all nonnegative indices only enlarges the sum. No translation
invariance, infinite-volume approximation, or omission of boundary modes
was used. Splitting the integral at s = a^2, for sufficiently small a,

\[
\int_0^\tau\|V_s\|ds
\le a^2+C a^4\int_{a^2}^\tau s^{-2}ds
\le (1+C)a^2,
\]

which proves (3). Also sup_(s>=tau/2) ||V_s|| <= C_tau a^4.

### 3. Contract with the actual two probes and the unsmoothed residual

Whiten a one-color Gaussian as A = Delta^-1/2 xi in an orthonormal
cochain basis, so xi has identity covariance. L008 gives ||B_i|| <= M_i
and the uniformly finite trace ||E_tau||_1. Write the symmetric whitened
matrix of r_0 as R_a, summed over colors. From L009's concrete generator,
||K_a A|| <= C_u ||d A||. Also ||d|| <= 4/a, since the Hodge spectrum
is bounded above by 16/a^2. Therefore

\[
|\langle d\Delta^{-1/2}\xi,
 dK_a\Delta^{-1/2}\xi\rangle_a|
\le (4C_u/a)\|\xi\|^2.
\]

Subtracting the two bounded B_i gives

\[
\|R_a\|\le 4C_u/a+M_3+M_6\le C/a.
\tag{11}
\]

This deliberately crude bound makes no assumption that the unflowed
residual is small in operator norm.

Put M_(i,a) = Delta^-1/2 E_tau Q_i T_a Delta^-1/2. Using (4),

\[
M_{i,a}=\frac5{24}\int_0^\tau
 E_\tau B_i
 [\Delta^{1/2}E_{\tau-s}d^*]\,V_s\,
 [d E_s\Delta^{-1/2}]\,ds.
\tag{12}
\]

The right bracket has norm at most one. To bound the left bracket,
write d* = Delta^1/2 (d Delta^-1/2)* and use
||d Delta^-1/2|| <= 1. Hence its norm is at most
||Delta E_(tau-s)||. For s <= tau/2 this is bounded by
sup_(lambda>=0) lambda exp(-tau lambda/2) <= 2/(e tau);
for s >= tau/2 use the cutoff bound 16/a^2. Applying the trace-ideal
inequality to (12) gives

\[
\begin{split}
\|M_{i,a}\|_1
&\le C_i\left[
\int_0^{\tau/2}\|V_s\|ds
+a^{-2}\int_{\tau/2}^\tau\|V_s\|ds\right]\\
&\le C'_i(a^2+a^{-2}a^4)\le C''_i a^2.
\end{split}\tag{13}
\]

Only the uniform trace of E_tau, the bound for B_i, and the two estimates
in step 2 are needed. In particular V_s need not commute with the heat
operator or have controlled spatial derivatives.

Equation (5) is 2 sum_c (xi^c)^T M_(i,a) xi^c. Gaussian covariance of
quadratic forms is 2 Tr(sym M R); the extra factor 2 in (5) and the three
colors give

\[
G_{i,a}^{\mathrm{tad}}
=12\operatorname{Tr}(\operatorname{sym}M_{i,a}\,R_a).
\]

Use ||sym M||_1 <= ||M||_1, (11), and (13) to prove (6).

### 4. Scope and literature comparison

The screened target is the complete coefficient in L011. The proof
controls one internally contracted summand in its first term,
kappa_0(f_(i,2),r_0), using the actual radial Wilson vertex and both
actual quadratic probes. The Wick-ordered cubic part in (8) still has
nonzero possible pairings with the outer probe leg and r_0. Neither its
contribution nor any other term in L011 is bounded by (6).

This is a specialization/reproduction of finite Gaussian and relative
heat estimates, not an asserted result beyond the checked literature.
The [saved assessment](../drafts/literature/2026-09-26-current-target.md)
identifies Luescher–Weisz, [arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2),
sections 7 and 8.2, as supporting bulk flow-renormalization context, not a
theorem evaluating this boundary-box summand or the whole covariance.
No reproof of that general renormalization theorem is attempted here.
The remaining full logarithm, finite matching, reflected-error estimate,
continuum construction and mass gap are unresolved.

## Mathlib

Coverage of the full selected-contraction statement: **not checked**.
Coverage of supporting Wick decompositions, finite Hilbert complexes,
relative trigonometric heat kernels, and trace-ideal estimates: **not
checked**. No Mathlib theorem is asserted to match this statement; the
named source above is supporting literature rather than a full match.
