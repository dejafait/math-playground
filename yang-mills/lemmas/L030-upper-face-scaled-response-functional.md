# L030 — A scaled continuum functional for the upper-face response

## Hypotheses

Use exactly L029's upper-face axial one-internal-action-pair class,
three colors, straight lower-rooted forest, and its sign convention
G_top(i,p)=-24 Tr(M W_i), for i=3,6. Keep L008's specified smooth
Psi, displacement, two probes and tau=1/16, and L009's generator.
Use L028's physical Laplacian Delta_a, residual N_a and exterior
mode expansion. Write G_top(i,a) for the sum over all selected
plaquettes, including transverse boundary-adjacent ones. Limits are
through admitted even N, a=8/N, after the fixed-mesh small-coupling
coefficient has been taken.

All continuum operators below use L008's relative sine/cosine basis
f_k on D=(-4,4)^4, physical eigenvalues lambda_k=(pi/8)^2|k|^2,
and its unflowed one-color B_i=Delta^(-1/2) Q_i Delta^(-1/2).
The transverse cube is D_perp=(-4,4)^3. Define

\[
 (Tb)(y)=\int_{-4}^4 b_1(x_1,y)\,dx_1.
 \tag{1}
\]

The differential operator N_2 used in the conclusion is specified
by the finite composition rule (5)–(8) below. It is a compactly
supported coefficient operator, not an assumed continuum counterterm.

## Conclusion

Define real functions

\[
 h_k=T(\lambda_k^{-1/2}f_k),\qquad
 r_\ell=T(\lambda_\ell^{-1/2}\Delta^{-1}N_2 f_\ell),
\]
\[
 w_i(y)=\sum_{k,\ell}e^{-\tau(\lambda_k+\lambda_\ell)}
 (B_i)_{k\ell}h_k(y)r_\ell(y),\qquad
 I_i=\int_{D_\perp}w_i(y)\,dy .                    \tag{2}
\]

The series converges absolutely in C^1 of the closed transverse cube.
In particular I_i is a specified finite signed functional of the
original probe and residual stencil. For both probes,

\[
 \boxed{\lim_{a\downarrow0}a^2G_{\mathrm{top}}(i,a)=-48 I_i.}
 \tag{3}
\]

A remainder statement that does not hide a sign assumption is

\[
 |a^2G_{\mathrm{top}}(i,a)+48 I_i|
 \le C_i\{a+\delta_i(a)+\epsilon+\sqrt{a/\epsilon}\},
 \quad 2a<\epsilon<1,                              \tag{4}
\]

for sufficiently small a. Here delta_i(a) is the maximum over all
selected plaquettes of |a^(-2)(W_i)_HH-w_i(y_p)|, where y_p is the
transverse midpoint; the proof establishes delta_i(a)->0 by full-mode
bounds. Thus (4), for example with epsilon=a^(1/3), is a rigorous
o(1) remainder. It is not a numerical certificate or an asserted
explicit rate for delta_i.

Neither I_3 nor I_6 is evaluated or proved nonzero here. Even I_i=0
would only imply o(a^(-2)), not O(1) or absence of a logarithm. The
other pairing class, other plaquettes and action/measure/residual/flow
jets are outside (3). No cancellation in the complete Ward coefficient,
finite matching, or reflected-error bound <= c_box/2 follows. This is
a local specialization within the saved literature assessment, not a
claim of originality or a Yang–Mills construction.

## Proof

### 1. Specify the leading residual stencil without changing the probes

Let t be a formal scalar, and retain only its coefficients through
degree one in the following compositions. At component cell centers
replace the staggered incidence derivative in direction j by

\[
 D_j(t)=\partial_j+\frac{t}{24}\partial_j^3.
 \tag{5}
\]

Use the usual exterior incidence signs to form d(t). Its formal
adjoint has the reversed incidence signs and D_j(t)^*=-D_j(t).
Define the diagonal plane and link averaging operators

\[
 C_{\mu\nu}(t)=1+\frac t8(\partial_\mu^2+\partial_\nu^2),
 \qquad E_\nu(t)=1+\frac t8\partial_\nu^2.
 \tag{6}
\]

Set

\[
 u^{(2)}_\mu=\frac16\sum_\nu\partial_\nu^3\Psi_{\mu\nu},
 \quad u(t)=u+t u^{(2)},
\]
\[
 w_\mu(t)=w_\mu+t(\partial_\mu u^{(2)}_\mu+
                    \partial_\mu^3u_\mu/6),
\]
\[
 s_{\mu\nu}(t)=s_{\mu\nu}+t(\partial_\mu u^{(2)}_\nu+
 \partial_\nu u^{(2)}_\mu+
 (\partial_\mu^3u_\nu+\partial_\nu^3u_\mu)/6).
 \tag{7}
\]

Let M(t)F have nu component sum_rho u_rho(t) F_(rho nu),
with F extended antisymmetrically. Let S(t) be precisely the symmetric
six-component multiplication matrix whose quadratic form is
sum_(mu<nu) s_(mu nu)(t) sum_alpha F_(mu alpha)F_(nu alpha).
Thus its off-diagonal entries retain the polarization factors in
L008. Let W_3(t) be diagonal multiplication by
C_(mu nu)(t)[w_mu(t)+w_nu(t)] in plane mu nu; the derivatives here
act on the weight, not on the argument of W_3. Put

\[
 K(t)=E(t)M(t)C(t)d(t),\quad L(t)=d(t)^*d(t),
\]
\[
 Q_3(t)=d(t)^*W_3(t)d(t),\quad
 Q_6(t)=d(t)^*C(t)^*S(t)C(t)d(t),
\]
\[
 N_2=[t]\left\{\frac{L(t)K(t)+K(t)^*L(t)}2
                         -Q_3(t)-Q_6(t)\right\}.       \tag{8}
\]

Here [t] denotes the coefficient of t; adjoints reverse the entire
composition, including the multiplication operators. These formulas
are a finite explicit definition of N_2, requiring no limit or
unknown coefficient. Its differential order is at most five. All
its coefficients are smooth and supported in the support of Psi.

To justify (8), the centered staggered difference has expansion
partial_j+a^2 partial_j^3/24+O(a^4), its average has expansion
1+a^2 partial_j^2/8+O(a^4), and the full-step central difference
has expansion partial_j+a^2 partial_j^3/6+O(a^4). Taylor's integral
remainder proves these in every C^r norm with the corresponding
higher derivatives. L028's exact compositions are K_a=E_a M_a C_a d_a,
L_a=d_a^*d_a, Q_3,a=d_a^*W_3,a d_a and
Q_6,a=d_a^*C_a^*S_a C_a d_a. The adjoints on the coefficient support
are the reversed centered maps. In particular W_3,a averages the
weight; it is not a clover-square probe.

Substitution of the expansions, including all coefficient differences
in (7), yields on any smooth one-form f the compact extension estimate

\[
 \|N_a f-a^2N_2 f\|_{C^r}
 \le C_r a^4\|f\|_{C^{r+9}}.                         \tag{9}
\]

The zeroth term vanishes by L009's polarized continuum identity.
For (9), expand each finite composition through degree two in a;
the retained a^2 terms give (8). Each remaining term either contains
a single fourth-order Taylor remainder or two second-order errors.
The original order is at most three, so at most seven derivatives
of f are necessary; r+9 is a harmless upper bound. Product derivatives
of the fixed smooth coefficients enter C_r. Integral difference
formulas bound the unexpanded derivative maps uniformly between the
required C^s spaces. Compact support keeps every coefficient-bearing
composition away from boundary rows for sufficiently small a. This
also justifies the formal adjoints; no boundary term is omitted.

### 2. Convergence with the complete relative inverse and heat sums

For a fixed allowed continuum mode f_ell, let
b_(ell,a)=lambda_(ell,a)^(-1/2) Delta_a^(-1)(a^(-2)N_a f_(ell,a)),
extended by the finite relative sine/cosine series. We claim

\[
 b_{\ell,a}\longrightarrow
 \lambda_\ell^{-1/2}\Delta^{-1}N_2f_\ell
 \quad\hbox{in }C^1(\overline D).                    \tag{10}
\]

Indeed (9) gives convergence of the compactly supported source in
every fixed C^r norm. Each fixed Fourier coefficient of that source
converges by its a^4-weighted staggered Riemann sum, and the fixed
relative eigenvalue converges. There is no zero eigenvalue. L028(6),
divided by a^2, bounds the third Laplacian of the source by
C(1+|ell|)^11. Thus the coefficients of its inverse are bounded by
C(1+|ell|)^11 lambda_(m,a)^(-4). Their C^1 contributions are bounded
by C(1+|ell|)^11(1+|m|)lambda_(m,a)^(-4), summable uniformly over
all four-dimensional relative labels since lambda_(m,a)>=|m|^2/16.
Truncate this summable series, pass to the limit in its finite part,
and then remove the truncation. This proves (10), and the same bound
holds for its continuum limit. This is a full inverse argument, not
an assumption of damping on the internal action loop.

Let v_k,z_ell be the exterior columns of L028(11), resolved into
L029's H,L,d coordinates. The full axial sum of a sampled field is
a midpoint Riemann sum for T; averaging the two transverse endpoints
converges to evaluation at their midpoint. Consequently, uniformly
on all selected transverse plaquettes, including endpoints on faces,

\[
 (v_k)_H\longrightarrow h_k(y_p),\qquad
 a^{-2}(z_\ell)_H\longrightarrow r_\ell(y_p).       \tag{11}
\]

For the second limit apply (10); for the first apply it directly to
the fixed smooth mode lambda_k^(-1/2) f_k. The relative component-1
extension vanishes on the transverse boundary, agreeing with the
pinned endpoints. These limits therefore do not assume an unpinned
upper potential.

L029(13) and L028(8) bound both factors in (11) by fixed polynomials
in their mode labels, uniformly in a. L008 gives uniformly bounded
B_(i,a); its fixed matrix entries converge to B_i by smooth-mode
Riemann sums for the two specified quadratic forms. Heat weights
are bounded by exp(-tau |k|^2/16). L028(14) now implies

\[
 a^{-2}(W_i)_{HH}(p)\longrightarrow w_i(y_p)
 \quad\hbox{uniformly over all }p.                  \tag{12}
\]

In detail truncate both heat indices. Equation (11) proves uniform
convergence of the finite part. The complement is bounded by a
mesh-independent summable polynomial times
exp(-tau(|k|^2+|ell|^2)/16), and its bound tends to zero as the
truncation increases. This proves delta_i(a)->0 as defined in (4).
The same polynomial estimates for the continuum C^1 norms give
absolute C^1 convergence of (2). Only the first factor h_k has the
axial-zero projection: the residual can mix modes before T acts on
its inverse. No commutation of N_2 or B_i with T or heat is used.

### 3. The three-dimensional edge factor and its boundary strip

By L029(11), for a transverse edge p=(v,v+hat(mu)),

\[
 \rho_{N,p}:=l_p/N
  =(\delta_v-\delta_{v+\hat\mu})^T
        G_{3,N}(\delta_v-\delta_{v+\hat\mu}),\quad
 0\le\rho_{N,p}\le1.                              \tag{13}
\]

Boundary deltas mean zero, as in that lemma. We give the needed bulk
limit rather than assume that a local vertex has a local covariance.
On Z^3 use the dimensionless nearest-neighbor Laplacian Delta_Z and
the lazy walk P=I-Delta_Z/12. Its Fourier symbol is
p(theta)=1/2+(cos(theta_2)+cos(theta_3)+cos(theta_4))/6, in [0,1].
Since 1-p(theta)>=c|theta|^2 on [-pi,pi]^3, its Fourier integral gives

\[
 0\le P^n(x,y)\le P^n(0,0)\le C(n+1)^{-3/2}.
 \tag{14}
\]

The first inequality follows from the walk probabilities, the second
from taking the absolute value of the Fourier integrand, and the
last from p^n<=exp(-n(1-p)) and integration. Hence
G_Z=(1/12)sum_(n>=0) P^n is a finite kernel. The killed walk on the
interior cube has P_N=I-Delta_(3,N)/12, so the same convergent series
is G_(3,N), and 0<=P_N^n(x,y)<=P^n(x,y).

If x is at graph distance at least R from the boundary, the two walk
kernels agree for n<R. Therefore each inverse entry difference with
such a starting point is at most C sum_(n>=R)(n+1)^(-3/2)
<=C R^(-1/2). Apply this to the four entries in (13) when both
endpoints have that distance. The infinite-volume edge value is

\[
 \int_{[-\pi,\pi]^3}
 \frac{2-2\cos\theta_\mu}
 {\sum_{j=2}^4(2-2\cos\theta_j)}\,
 \frac{d^3\theta}{(2\pi)^3}=\frac13.                \tag{15}
\]

To see the value, sum the three numerators, cancel the denominator
off its measure-zero zero set, and use coordinate symmetry. The
integrals are finite (the ratios are bounded). It follows that

\[
 |\rho_{N,p}-1/3|\le C\sqrt{a/\epsilon}
 \tag{16}
\]

when the physical distance of both endpoints to the transverse
boundary is at least epsilon>2a. The remaining boundary strip has
at most C(epsilon+a)a^(-3) edges in each direction. Its contribution
to an a^3-weighted bounded sum is O(epsilon+a), by (13). This retains
the corner and boundary-adjacent edges explicitly.

### 4. Assemble the signed limit and remainder

The HH coefficient is exactly N rho_(N,p)(1/4-1/(3N)). Thus (12)
and Na=8 give

\[
 a^2G_{HH}(i,a)
 =(-48+8a)\,a^3\sum_{p}\rho_{N,p}
                   \{w_i(y_p)+e_{i,a,p}\},
 \qquad |e_{i,a,p}|\le\delta_i(a).                 \tag{17}
\]

For each of the three transverse directions, the midpoint sum of
the C^1 function w_i over the selected edges converges to its integral
with O(a) error. Excluding edges contained in other faces changes
such a sum by O(a). Equations (13),(16) and the strip estimate yield

\[
 \left|a^3\sum_{p\parallel\mu}\rho_{N,p}w_i(y_p)
                  -\frac13 I_i\right|
 \le C_i\{a+\epsilon+\sqrt{a/\epsilon}\}.           \tag{18}
\]

The same w_i occurs for every direction: both endpoint averages in
(11) converge to T of the field at the common continuum point.
Summing (18) over mu=2,3,4 gives I_i. The error in (17) is bounded
by C_i delta_i(a), since rho<=1 and there are O(a^(-3)) edges.
Finally L029's five other channels have absolute sums bounded by
O(a^(-1)), O(1), O(1), O(a), O(a^2). Their a^2-scaled total is O(a).
Combining these estimates proves (4) and hence (3), with the -24
three-color contraction already included. No positivity of W_i was
used.

The general flow-renormalization and matching results assessed in
`drafts/literature/2026-09-26-current-target.md` are not reproved or
invoked to infer a value of I_i. The extra argument here is required
for this forest, physical box boundary and actual residual stencil.
The finite-step walk comparison above proves the only Green-kernel
specialization needed for the reduction. It is not an import of an
unread lattice boundary theorem.

## Mathlib

Coverage of this full forest-specific scaled-response limit: not
checked. Coverage of the supporting Fourier, Taylor and dominated
series facts: not checked. No full matching theorem or formal
verification is asserted. All specialized boundary, normalization
and limiting arguments used here are written above.
