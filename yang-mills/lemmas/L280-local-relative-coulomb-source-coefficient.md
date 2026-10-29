# L280 — Local relative-Coulomb density and the exact source coefficient

## Hypotheses

Use exactly the fixed-mesh SU(2) model and real probes of L003 and
L279: positive even N, a=8/N, the cube [-4,4]^4, all boundary-contained
links pinned to identity, every other link variable, and gauge
transformations identity at every boundary vertex. The coupling tends
to zero with this mesh fixed. Write E for the positively oriented
variable links and I for the interior vertices. Normal links touching
the boundary are in E, including those used by L003's forest.

Use L279's generators t^c=i sigma^c/2 and Euclidean color components.
Let V=(su(2))^I and X=(su(2))^E, with the component Euclidean inner
products. Extend u in V by zero at boundary vertices. For an edge e
with tail e_- and head e_+, define

\[
(Bu)_e=u_{e_-}-u_{e_+},\qquad
(Mu)_e=u_{e_-}+u_{e_+},\qquad
\Delta=B^*B,\qquad \mathcal H=\ker B^* .                 \tag{1}
\]

B is minus the unscaled zero-cochain incidence. Consequently
mathcal H is exactly L003's ker d*: the factors a and the common
factor a^4 in the cochain inner products do not change this kernel.
All matrices below include all three colors. The group
G=SU(2)^I acts by (h.U)_e=h_{e_-}U_e h_{e_+}^{-1}, with h=1 on
boundary vertices, and has normalized product Haar measure dh.

Keep L279's exact functions mathcal S, H_{h_-}, H_{h_+}. Set
F=||f_*||_infinity and fix any 0<eta<1. Sources are real and satisfy
(|s|+|t|)F<eta. Define the unnormalized source partition function using
normalized Haar measure on every variable link:

\[
Z(g;s,t)=\int \exp\{-\Phi_{s,t}(U)/g^2\}\prod_{e\in E}dU_e,
\qquad \Phi_{s,t}=\mathcal S-sH_{h_-}-tH_{h_+}.             \tag{2}
\]

The source-covered standard inputs are the finite-dimensional analytic
inverse-function and change-of-variables theorems and the Laplace
theorem cited precisely in the proof. This is a specialization of local
quotient integration, not a global gauge-fixing assertion.

## Conclusion

There is a ball O about zero in mathcal H such that

\[
\Psi:O\times G\longrightarrow SU(2)^E,\qquad
\Psi(v,h)=h.\exp(v)                                      \tag{3}
\]

is an analytic diffeomorphism onto an invariant open neighborhood of
the flat orbit. Each orbit in this neighborhood has exactly one
representative exp(v), v in O. This is uniqueness within the small
slice; no assertion concerns intersections with a larger slice.

Here is its complete density through degree two. Let
mathcal A(v) be the block diagonal operator with edge blocks ad(v_e),
and let mathcal D(v):V->X be the derivative, in u at zero, of
log(exp(u).exp(v)). The logarithm is componentwise near exp(v).
Put

\[
\begin{split}
D_1(v)&=-\tfrac12\mathcal A(v)M,\qquad
D_2(v)=\tfrac1{12}\mathcal A(v)^2B,\\
A_1(v)&=\Delta^{-1}B^*D_1(v),\qquad
A_2(v)=\Delta^{-1}B^*D_2(v),\\
\ell_2(v)&=-\tfrac1{12}\sum_{e\in E}|v_e|^2
             +\operatorname{Tr}_V A_2(v)
             -\tfrac12\operatorname{Tr}_V(A_1(v)^2).
\end{split}                                               \tag{4}
\]

With Euclidean volume dv on mathcal H and normalized dh,
Psi^*(product dU_e)=rho(v)dv dh, where, on a sufficiently small O,

\[
\begin{split}
\rho(v)&=\rho_0\prod_{e\in E}
 \left(\frac{\sin(|v_e|/2)}{|v_e|/2}\right)^2
 \det_V\bigl(\Delta^{-1}B^*\mathcal D(v)\bigr),\\
\rho_0&=c_0^{|E|-|I|}\sqrt{\det_V\Delta},
\qquad c_0=(16\pi^2)^{-1},\\
\log(\rho(v)/\rho_0)&=\ell_2(v)+O_a(|v|^3).
\end{split}                                               \tag{5}
\]

The determinant in (5) is positive on O. There is no degree-one
density term. Formula (4) retains both the all-link Haar term and
the gauge-coordinate determinant terms; it is not the forest M_2.

Define S_m^H and b_{+/- ,k}^H by taking the jets of the exact functions
mathcal S and H_{h_+/-} on exp(x), x in mathcal H, with L279's jet
convention (4). Their explicit formula is L279(8)–(9), with
X_{p,j}=epsilon_{p,j}x_{e_{p,j}}^c t^c on EVERY variable link, and
zero only on pinned links. Forest links are not set to zero here.
Let E^H_{s,t} be normalized Gaussian expectation on mathcal H with
quadratic action S_2^H-s b_{-,0}^H-t b_{+,0}^H. Set

\[
V_H=S_3^H-sb_{-,1}^H-tb_{+,1}^H,\qquad
W_H=S_4^H-sb_{-,2}^H-tb_{+,2}^H .                          \tag{6}
\]

Then on the stated open source domain the exact identity is

\[
\boxed{\quad R(s,t)=\tfrac12 E^H_{s,t}[V_H^2]
                 -E^H_{s,t}[W_H]+E^H_{s,t}[\ell_2]\quad}  \tag{7}
\]

for precisely L279(22)'s forest expression R, without an additional
source-independent additive constant. In particular kappa_a is the
mixed source derivative at zero of the right side of (7). Both source
insertions, moving means, action jets and complete density correction
are retained.

This is a finite-mesh representation of an already identified
coefficient. It proves no sign or growth estimate, uniform remainder,
physical trajectory, composite renormalization, continuum theory,
reflection-positive interacting sector, or finite positive mass.
The separate critical audit in section 6 accepts this specialization
under exactly these fixed-mesh hypotheses.

## Proof

### 1. Relative domains, freeness, and the local product chart

A boundary-contained link has both endpoints on the boundary, so the
action in (3) preserves its prescribed identity value. All normal links
stay in X; no gauge parameter is imposed at their interior endpoints.
If Bu=0, following L003's rooted forest from an interior vertex to its
boundary root gives u=0 at that vertex. Thus B is injective and Delta
is positive definite. Orthogonal decomposition gives
X=mathcal H direct-sum im B.

The action of G on the entire configuration space is free. Indeed,
h.U=U implies h_{e_+}=U_e^{-1}h_{e_-}U_e along each edge. Starting
with h=1 at the boundary roots and following the forest forces h=1
at every interior vertex, for every U. At (0,1) the derivative of
Psi is (w,u) maps to w+Bu, hence is an isomorphism. The analytic
inverse-function theorem supplies injectivity and an analytic inverse
on a product neighborhood of (0,1). By shrinking its v-neighborhood,
the derivative at (v,1) remains invertible.

One must also exclude identifications by a distant h. If arbitrarily
small slice points exp(v_n), exp(w_n) were related by h_n outside a
fixed identity neighborhood in G, compactness would give a convergent
subsequence h_n->h_*. Taking v_n,w_n->0 gives h_*.1=1. Freeness at
the identity implies h_*=1, a contradiction. Choose that identity
neighborhood within the inverse-function neighborhood. Shrink O so
that any h relating two points of exp(O) belongs to it. Local
injectivity now implies v=w and h=1 whenever h.exp(v)=exp(w).
If Psi(v,h)=Psi(w,k), apply k^{-1}: the same assertion proves v=w
and h=k. Thus Psi is injective on O times all of G.

For general h, the identity Psi(v,kh)=k.Psi(v,h) transports the
derivative from h=1 by diffeomorphisms. It is therefore invertible
at every point of O times G. An injective local diffeomorphism has
open image and an analytic inverse patched from its local inverses.
The image is invariant and contains the full flat orbit. L003's
plaquette/path argument says this is the only orbit of minima of
mathcal S. We have proved the needed local section without a global
section or a global Gribov-copy assertion.

### 2. Exact density, orientation, and all boundary rows

Write theta_e=log U_e in color coordinates. Normalized SU(2) Haar
measure is c_0 j(theta_e)dtheta_e, with j as in (5), by L279(11).
For normalization, exp(theta^ct^c) covers SU(2) once for |theta|<2pi
up to its antipodal endpoint of measure zero. The radial integral is
4pi integral_0^{2pi} 4 sin^2(r/2) dr=16pi^2, giving the displayed
c_0. Gauge Haar has density c_0^{|I|} at u=0 in h=exp u.

At (v,1), the derivative of theta=log Psi is the block map
[Q,mathcal D(v)], where Q is an orthonormal inclusion of mathcal H.
Let P=B Delta^{-1/2}; its columns are an orthonormal basis of im B.
In the orthonormal output basis [Q,P] the derivative matrix is
block upper triangular, with diagonal blocks 1 and
Delta^{-1/2} B^* mathcal D(v). Hence its absolute determinant is

\[
\sqrt{\det\Delta}\,
\left|\det(\Delta^{-1}B^*\mathcal D(v))\right|.            \tag{8}
\]

At v=0, mathcal D(0)=B and the last determinant is 1. On a small
connected O it remains positive, so the absolute value can be removed.
Multiplying (8) by the link Haar density and dividing by the gauge
coordinate density at u=0 proves (5) at h=1. The action preserves
product link Haar. The identity Psi(v,kh)=k.Psi(v,h), together with
left invariance of dh, makes the density relative to dv dh independent
of h. This proves the full pullback formula. In particular the gauge
volume integrates to exactly one, and rho_0 contains every remaining
constant factor.

Here is the derivative used in (8), including the nonlinear terms.
For a Lie algebra variation z at v, the right-trivialized derivative
(delta exp(v))exp(-v) is E(ad v)z, where
E(A)=integral_0^1 exp(rA)dr=(exp A-1)/A, with its analytic value at
A=0. This follows by differentiating the matrix exponential under
the integral. Along the gauge orbit the same right-trivialized
variation is u_{e_-}-exp(ad v_e)u_{e_+}. Consequently

\[
(\mathcal D(v)u)_e
 =E(\operatorname{ad}v_e)^{-1}
   \bigl(u_{e_-}-e^{\operatorname{ad}v_e}u_{e_+}\bigr).
                                                               \tag{9}
\]

The inverse exists near zero. Expanding
E(A)^{-1}=1-A/2+A^2/12+O(A^3) and
E(A)^{-1}exp A=1+A/2+A^2/12+O(A^3) gives

\[
\mathcal D(v)=B-\tfrac12\mathcal A(v)M
                    +\tfrac1{12}\mathcal A(v)^2B+O_a(|v|^3).
                                                               \tag{10}
\]

For a normal edge with boundary tail this row is explicitly
-u_{e_+}-(ad v_e)u_{e_+}/2-(ad v_e)^2u_{e_+}/12+O(|v_e|^3|u|).
With boundary head it is
u_{e_-}-(ad v_e)u_{e_-}/2+(ad v_e)^2u_{e_-}/12+O(|v_e|^3|u|).
Both rows participate in Delta and (8)–(10). They are neither
deleted nor replaced by tangential boundary rows.

Now Delta, B and M act on vertices/edges with identity on color.
Every color block of A_1 is a scalar linear combination of ad(v_e),
which has trace zero. Thus Tr_V A_1=0 identically, even before
restricting v to mathcal H. The convergent local log-determinant
expansion gives

\[
\log\det(1+A_1+A_2+O(|v|^3))
 =\operatorname{Tr}A_2-\tfrac12\operatorname{Tr}(A_1^2)
   +O_a(|v|^3).
                                                               \tag{11}
\]

Together with log j(v_e)=-|v_e|^2/12+O(|v_e|^4), this proves (4)–(5).
In particular rho(gx)/rho_0=1+g^2 ell_2(x)+O_a(g^3|x|^3) on
bounded rescaled sets. The lack of a linear term means that there
is no omitted product of a linear density jet with a cubic phase jet.

A finite consistency check of both the sign and the normalization is
the path of two oriented links from a boundary vertex through one
interior vertex to another boundary vertex. It is not an input about
the box. Here B=(-1,1), Delta=2 times the color identity, and the
slice has v_1=v_2=v. Then A_1=0, A_2=(ad v)^2/12 and
Tr(ad v)^2=-2|v|^2. Formula (4) gives ell_2=-|v|^2/3, agreeing with
log j(2v) through degree two for the quotient holonomy exp(2v).
Euclidean slice coordinate y=sqrt(2)v gives holonomy exp(sqrt(2)y),
whose density at zero is c_0 2^{3/2}, also exactly rho_0 in (5).

### 3. Source localization and the quadratic law on this slice

Extend h_{+/- ,p} by zero to plaquettes not parallel to 12. Then

\[
\Phi_{s,t}=4\sum_p w_p(s,t)P_p,\qquad
w_p=1-s h_{-,p}-t h_{+,p}\ge 1-\eta>0.                 \tag{12}
\]

Since SU(2) plaquettes have P_p>=0, the zero set is precisely the
flat orbit, for every allowed source, and Phi_{s,t}>=(1-eta)mathcal S.
Choose a smooth cutoff in O, supported compactly in O and equal to
one near zero; use (3) to extend it invariantly, then by zero outside
the image. The support of one minus this extended cutoff is compact and
disjoint from the flat orbit. L003's minimum argument gives a
strictly positive lower bound for mathcal S on that support. The discarded
part of (2) is therefore O_a(exp(-c_a/g^2)), with c_a>0 for the
chosen eta and cutoff. This statement also holds for each fixed
finite insertion amplitude. There is no unaccounted orbit-volume
factor because dh integrates to one.

Let C be the unscaled oriented edge-to-plaquette incidence on all
relative edges, acting independently on colors. Directly from
L279(10), now allowing every variable edge, the quadratic part is

\[
S_2^H-sb_{-,0}^H-tb_{+,0}^H
 =\tfrac12\sum_p w_p |(Cx)_p|^2,\qquad x\in\mathcal H.
                                                               \tag{13}
\]

If Cx=0, L003's closed-cochain argument gives x in im B. Its
intersection with ker B^* is zero. Thus (13) is positive definite
and defines E^H_{s,t}. This uses only the linear relative decomposition
for the quadratic form. All higher jets in (6) are evaluated directly
on the nonlinear section exp(x); none is transferred from forest
coordinates by that decomposition. In particular the covariance is
on mathcal H, not an instruction to add longitudinal Gaussian fields
to nonlinear observables.

### 4. Comparing the entire source integral, not separate summands

Use William D. Kirwin, *Higher Asymptotics of Laplace's Approximation*,
Asymptotic Analysis 70 (2010), 231–248,
[arXiv:0810.1700v2](https://arxiv.org/pdf/0810.1700v2), Theorem 2.1,
with its smooth nondegenerate specialization in section 3.2 and the
signed-amplitude argument in Lemma 2.3, as already applied in L279.
Here the local phase Phi_{s,t}(exp v) and density rho(v) are analytic,
the minimum is internal with positive Hessian (13), and the cutoff is
smooth and compactly supported. These verify the same finite-order
Laplace hypotheses at each fixed source. The complement estimate just
proved makes all omitted terms exponentially negligible. No remainder
uniform in mesh or differentiable in sources is required below.

Let q=3(|E|-|I|)=dim mathcal H and let
I_H(s,t)=integral_H exp(-S_2^H+s b_{-,0}^H+t b_{+,0}^H)dx.
Under v=gx the local phase divided by g^2 is the quadratic form
(13), plus g V_H+g^2 W_H at the orders needed. Formula (5) gives the
density factor 1+g^2 ell_2 at these orders. The order-g integrand is
-V_H, odd under x maps to -x, so its Gaussian integral is zero.
The order-g^2 integrand is exactly V_H^2/2-W_H+ell_2. The cited
Laplace theorem justifies this integrated expansion and its remainder:

\[
Z(g;s,t)=\rho_0 g^q I_H(s,t)
 \{1+g^2 R_H(s,t)+o_a(g^2)\},\qquad
R_H=E^H_{s,t}[V_H^2/2-W_H+\ell_2].                     \tag{14}
\]

The little-o here is for each fixed s,t. All omitted higher jets
enter at higher powers of g after scaling; one is not claiming a
pointwise expansion on the whole rescaled integration domain.

L003's exact forest quotient applies to the same gauge-invariant
integral (2). Its remaining link count is |E|-|I| and its normalized
Haar coordinate constant is c_0^{|E|-|I|}. By (12) its reduced phase
has the same unique minimum and positive Hessian as in L279, with
the source weights inserted. Applying the same Laplace theorem there
gives, with I_F(s,t) its unnormalized quadratic Gaussian integral,

\[
Z(g;s,t)=c_0^{|E|-|I|} g^q I_F(s,t)
 \{1+g^2 R(s,t)+o_a(g^2)\}.                            \tag{15}
\]

Indeed the order-two forest density is -M_2, and the phase jets are
exactly V(s,t), W(s,t) of L279(21), so the correction in (15) is
exactly its (22), not a different coefficient. This also supplies
an ordinary fixed-source interpretation of that finite formal formula.

Both (14) and (15) expand the identical unnormalized positive integral.
Their leading coefficients therefore agree:
I_F(s,t)=sqrt(det Delta) I_H(s,t). After division by this common
positive leading factor, subtraction, division by g^2, and g->0,
their next coefficients agree, R_H(s,t)=R(s,t). All constants were
fixed before this comparison, and none depends on g or the sources;
hence no hidden source-independent order-g^2 constant remains.
This proves (7).

The expressions on both sides of (7) are analytic on the open real
source domain: their quadratic precision matrices are positive
definite and depend affinely on s,t, and their finite polynomial
Gaussian moments are polynomials in the inverse precision entries
with polynomial source coefficients. Differentiate this equality of
explicit coefficient functions, not the asymptotic remainders.
L279(22) now identifies the mixed derivative with kappa_a. Source
derivatives of the Gaussian insert the centered quadratic observables;
derivatives of V_H and W_H supply both higher insertion jets. Thus
the equality retains both moving means and the entire connected
coefficient. A comparison of just action or just Haar contributions
would not have proved this statement.

### 5. Source attribution and qualifications

The general section/orbit change-of-variables prescription is known:
M. Polyak, *Feynman diagrams for pedestrians and mathematicians*,
[math/0406251v1](https://arxiv.org/pdf/math/0406251v1), section 3.1,
printed pp. 11–12, Remarks 3.1–3.2; and N. Reshetikhin, *Lectures on
quantization of gauge systems*,
[1008.1411v1](https://arxiv.org/pdf/1008.1411v1), Theorem 3 and its
proof, printed pp. 29–30, with local qualifications pp. 31–32.
Their uniqueness and nonsingular orbit-derivative conditions cannot
be assumed for a global lattice slice. We verified them locally for
this boundary-fixed box, and computed the actual positive pullback
Haar density rather than importing a signed determinant. The
specialization is needed to retain the normal-link domain and the
full degree-two density absent from the inspected general formulas.
No oscillatory-asymptotic remainder, unread lattice theorem, or
global compact BRST normalization is an input.

Equation (7) opens a way to examine this same coefficient with the
relative transverse covariance. It does not bound that covariance's
internal contractions in the complete expression, nor prove their
cancellations. The stopped integration-by-parts route in L279(31)–(34)
remains stopped; its nonzero pointwise test is not contradicted by
changing coordinates and comparing integrated coefficients. Uniform
higher-order errors and all continuum/infrared gaps remain separate.


### 6. Separate critical audit (2026-10-25)

**Verdict:** (3)–(7) pass this fixed-mesh audit. This accepts a local
specialization of known quotient integration and Laplace methods, not
an estimate on kappa_a or a new general gauge-fixing theorem. Wording
clarifications identify the **support of one minus the cutoff** as the
compact set in section 3, and call (delta exp(v))exp(-v) right-trivialized
in section 2. No mathematical input or formula changes. The five audit obligations were covered in the prior
SPECIALIZE assessment; no unread source or new theorem is used.

**Domains and full-group uniqueness.** All normal links belong to E.
There is one forest edge per interior vertex, with a boundary root in
every component. Thus Bu=0 forces every u to vanish. For the group
stabilizer of any U, propagate
h_head=U_e^{-1}h_tail U_e from the boundary along this same forest;
every h is identity. In particular there is no residual center.
Choose product neighborhoods O_0 times U_0 where the inverse-function
theorem makes Psi injective. If no smaller slice ball excluded an h
outside U_0 relating two slice points, there would be v_n,w_n tending
to zero and h_n in the closed compact complement of U_0 with
h_n.exp(v_n)=exp(w_n). A subsequential limit would stabilize the
identity, hence equal 1, contradicting h_* outside U_0. After shrinking
the ball, any relation is therefore inside the injectivity neighborhood
and forces v=w, h=1. For two arbitrary group coordinates apply this
to k^{-1}h. Invertibility of the derivative at (v,1) persists on a
small ball and transports by the action to (v,h). Thus the claimed
analytic product chart is justified over the full compact G, not just
near its identity. No statement about a larger slice is needed.

**Positive density and normalization.** At h=1, theta(v,1)=v,
so the slice derivative is exactly the orthonormal inclusion Q; it
has no additional exponential-coordinate Jacobian. Complete Q by
P=B Delta^{-1/2}. Then the lower-right block of [Q,D(v)] is
Delta^{-1/2}B*D(v), while the lower-left block is zero. Its absolute
determinant is (8), with all three colors in Delta. Dividing the
link-coordinate factor c_0^{|E|} product j(v_e) by the gauge-coordinate
factor c_0^{|I|} gives exactly (5). Here

\[
4\pi\int_0^{2\pi}r^2j(r)\,dr=16\pi^2,
\]

so c_0=(16 pi^2)^{-1} normalizes the full SU(2) group. The normalized determinant factor
in (8) equals one at zero and stays positive on a connected smaller
ball. Gauge invariance and normalized left Haar make the density
independent of h and its total orbit factor one. This rules out both
a sign ambiguity and an omitted group-volume constant.

The right-trivialized exponential differential is
E(A)=(exp A-1)/A. The orbit variation is u_tail-exp(A)u_head.
Thus (9) has the correct order and sign, and its expansion gives
D_1=-A M/2 and D_2=A^2 B/12. At a boundary tail these are respectively
-A u_head/2 and -A^2 u_head/12; at a boundary head they are
-A u_tail/2 and +A^2 u_tail/12. Both cases are included in B, M
and Delta. Because the graph matrices are color-scalar, every diagonal
color block contributing to Tr A_1 is a linear combination of ad(v_e),
whose trace is zero. Consequently the determinant contributes
Tr A_2-Tr(A_1^2)/2 at degree two and nothing at degree one. Combined
with log j=-|v|^2/12+O(|v|^4), this is precisely ell_2. The square term
cannot be dropped even though Tr A_1=0. There is no linear-density
term to multiply the cubic phase. The two-edge example in section 2
checks the conventions but is not used to establish these identities.

**Source localization and Laplace order.** For each real allowed
(s,t), every plaquette weight in (12) is at least 1-eta, including
plaquettes with zero source. Thus the exact phase is nonnegative,
has the same flat zero orbit, and bounds (1-eta)mathcal S below.
The invariant cutoff has compact support inside the product-chart
image. Its extension by zero is smooth. The support of 1-chi is
compact and avoids the flat orbit, so the discarded integral is
exponentially small. This support formulation also works when the
cutoff is not a characteristic function. The forest argument in L003
shows ker C=im B on relative edges. Hence the weighted quadratic
form (13) is strictly positive on ker B*. Boundary pins do not put
zero on the boundary of the slice-coordinate ball.

For clarity, in Kirwin v2 Theorem 2.1 take large parameter k=g^{-2},
leading radial phase order nu=2, radial amplitude exponent lambda=q,
and expansion index 2. The positive quadratic form gives a strictly
positive leading radial coefficient on the unit sphere. Phase jets
through degree four and density jets through degree two exist; the
cutoff gives weighted integrability and separation from the minimum.
The theorem then gives g^q times coefficients through g^2 with
little-o(g^2) remainder. The possible relative order-g coefficient
integrates to zero because V_H is cubic and the Gaussian is even.
The only relative degree-two integrand is V_H^2/2-W_H+ell_2.
These are precisely the hypotheses and orders of (14). The same
argument on the compact forest quotient gives (15), with density
jet -M_2. This uses the previously inspected nondegenerate Laplace
case, not an oscillatory stationary-phase remainder. Everything is
at fixed mesh and fixed sources.

**Equality and connected terms.** Both expansions concern Z itself,
with no division by Z(g;0,0). Their common power is
q=3(|E|-|I|). Their leading constants must therefore satisfy
c_0^{|E|-|I|} I_F=rho_0 I_H. Subtracting after this leading equality
and dividing by g^{q+2} gives R=R_H. In particular an additive
source-independent constant in R would also be detected and cannot
be suppressed. The ratio I_F/I_H=sqrt(det Delta) is independent of
sources because both quadratic forms arise from the same relative
curvature map, consistently with this comparison.

Only now differentiate the explicit coefficient functions, which are
analytic since their precision matrices are positive definite and
their polynomial Gaussian moments are finite sums of inverse-precision
entries. To display every connected term, suppress the superscript H
in this paragraph and let cum denote cumulants for E^H_{0,0}. The
mixed derivative of the right side of (7) is

\[
\begin{aligned}
&\operatorname{cum}(b_{-,2},b_{+,0})
 +\operatorname{cum}(b_{-,1},b_{+,1})
 +\operatorname{cum}(b_{-,0},b_{+,2})\\
&\quad-\operatorname{cum}(b_{-,1},b_{+,0},S_3)
 -\operatorname{cum}(b_{-,0},b_{+,1},S_3)\\
&\quad-\operatorname{cum}(b_{-,0},b_{+,0},S_4-\ell_2)
 +\tfrac12\operatorname{cum}(b_{-,0},b_{+,0},S_3,S_3).
\end{aligned}
\]

Indeed differentiating a Gaussian expectation inserts its centered
quadratic source observable; differentiating V_H and W_H supplies
both cubic and quartic insertion jets. Odd V_H has zero expectation
for every source, so its two-copy moment has exactly the connected
subtractions displayed. Equivalently these are the seven finite
cumulant terms of L279(7), with this slice's own jets and with
-M_2 replaced by ell_2. Identity (7), rather than a termwise transport
of higher jets, identifies their complete sum with kappa_a. No source
derivative of either asymptotic remainder has been taken.

The audit adds no new direct mathematical input to the existing
L003/L279 dependency rows. It establishes no internal-contraction
bound, cutoff cancellation or uniform higher error. ATTEMPTS/047's
stopped forest rearrangement and all interacting, continuum and
infrared gaps remain unaffected. Mathlib coverage remains as below.


### 7. Complete transverse contraction test (2026-10-25)

This bounded attempt uses the hypotheses above and the previously
approved full-coefficient growth assessment. It does **not** establish
or refute the logarithmic bound. The calculation below specializes the
finite Gaussian pairing method of L279 section 6 to the actual slice;
its additional content is the full density matrix and relative spectral
estimates. No nonlinear jet is transported from the forest slice.

First suppress color in B,M,Delta and put

\[
 P=B\Delta^{-1}B^*,\qquad J=M\Delta^{-1}B^*,\qquad
 D_{ef}=-\left(\frac1{12}+\frac{P_{ee}}6\right)\delta_{ef}
                 +\frac14J_{ef}J_{fe}.                         \tag{16}
\]

Then the **entire** density jet, including both determinant terms, is

\[
 \ell_2(x)=\sum_{e,f}D_{ef}\,x_e\mathbin{\cdot}x_f.             \tag{17}
\]

Indeed Tr(ad u ad v)=-2 u dot v with the generators in the
hypotheses. Cycling the trace of A_2 gives
sum_e P_ee Tr(ad x_e)^2/12=-sum_e P_ee |x_e|^2/6.
Cycling the trace of A_1 squared gives
(1/4) sum_(e,f) J_ef J_fe Tr(ad x_e ad x_f).
Multiplication by -1/2 yields the last term of (16).
The remaining term is the all-link Haar contribution -|x_e|^2/12.
These computations are on the full edge set E. For a boundary tail
B has row -u_head and M has row u_head; for a boundary head they
are u_tail and u_tail. Thus (16) retains both endpoint signs and
normal links; no boundary value of x is deleted. D is symmetric.
Write D also for D tensor the three-color identity below.

Let Q be an orthonormal inclusion of H, and define the extended
transverse covariance and its source derivatives by

\[
 G(s,t)=Q[Q^* C^*\operatorname{diag}(1-sh_--th_+)CQ]^{-1}Q^*,
 \quad K_\pm=C^*\operatorname{diag}(h_\pm)C,
\]
\[
 G_\pm=G K_\pm G,\qquad
 G_{-+}=G K_-G K_+G+G K_+G K_-G,\qquad G=G(0,0).              \tag{18}
\]

The matrices act on all edges/colors; G vanishes on im B. Inverses
and inverse square roots involving G always mean restriction to H.
C here is the incidence of (13), not a covariance. Every tensor in
what follows is computed from the all-variable-link jets (6): write
V_H=T(s,t)_(ijk) x_i x_j x_k/6 and
W_H=U(s,t)_(ijkl) x_i x_j x_k x_l/24, where
T(s,t)=T-sT_--tT_+, U(s,t)=U-sU_--tU_+.
The sums are over edge/color positions, including the actual finite
plaquette domains in those jets.

Use the contractions mathcal B and mathcal U defined in L279(24),
now with these tensors and G. The color covariance is a scalar edge
matrix times delta_cd. Hence every cubic internal contraction is
zero by the alternating color trace, exactly as in L279(23).
All quartic pairings and the six fully crossing cubic pairings give

\[
 R_H(s,t)=\frac1{12}\mathcal B(T(s,t),T(s,t);G(s,t),G(s,t),G(s,t))
 -\frac18\mathcal U(U(s,t);G(s,t),G(s,t))
 +\operatorname{Tr}(D G(s,t)).                               \tag{19}
\]

Pairing remains valid for the extended, singular covariance because
it is the covariance of a nondegenerate Gaussian on H. No integral
over longitudinal variables has been added. Differentiating (19)
therefore organizes the complete signed sum as

\[
\begin{aligned}
\mathcal K_3^H=\tfrac1{12}\big[&
 2\mathcal B(T_-,T_+;G,G,G)
 -6\mathcal B(T_-,T;G_+,G,G)
 -6\mathcal B(T_+,T;G_-,G,G)\\
 &+3\mathcal B(T,T;G_{-+},G,G)
 +6\mathcal B(T,T;G_-,G_+,G)\big],\\
\mathcal K_4^H=-\tfrac18\big[&
 -2\mathcal U(U_-;G_+,G)-2\mathcal U(U_+;G_-,G)\\
 &+2\mathcal U(U;G_{-+},G)+2\mathcal U(U;G_-,G_+)\big],\\
\kappa_a={}&\mathcal K_3^H+\mathcal K_4^H+
                      \operatorname{Tr}(D G_{-+}).             \tag{20}
\end{aligned}
\]

The factorials and derivative multiplicities are those proved in
L279(25)–(27), applied to this slice's jets. Equation (19), not a
termwise gauge-independence assertion, justifies their use. Thus (20)
retains both cubic and quartic insertion corrections, moving means,
two action vertices, and both determinant jets. It is not by itself
new cancellation evidence.

Here is the discriminating finite-domain estimate for the absolute
norm approach. Work first with one color and unscaled incidence, and
set L=C*C+BB*. L003's relative tensor-product modes, rescaled to
Euclidean counting measure, give for component mu the indices
0<=k_mu<=N-1 and 1<=k_nu<=N-1 for nu different from mu, with

\[
 \lambda_k=4\sum_{\nu=1}^4\sin^2(\pi k_\nu/(2N)),\qquad
 \lambda_k\ge 4|k|^2/N^2.                                   \tag{21}
\]

The eigenvector squared at any edge is at most 16/N^4. There are at
most 15 m^3 allowed indices with max k=m, for m>=1: even the larger
set of all nonnegative four-tuples has
(m+1)^4-m^4<=15m^3. Consequently

\[
 (L^{-1})_{ee}\le\frac{16}{N^4}\frac{N^2}{4}
             \sum_{m=1}^{N-1}15m\le30.                       \tag{22}
\]

The same bound holds for (Delta^{-1})_vv using four positive vertex
indices. These estimates apply to normal end links too, whose own
coordinate uses midpoint cosine modes, including k_mu=0.
The relative Hodge decomposition gives

\[
 L^{-1}=G+B\Delta^{-2}B^*,\qquad 0\le G\le L^{-1}.             \tag{23}
\]

To check (23), L B=B Delta, C B=0, and on H the operator L is C*C;
the two orthogonal summands are invariant and positive. The inverse
on im B is B Delta^{-2} B*. Thus (22) is also a uniform bound on
all diagonal transverse covariances. This is a quadratic-law use
of the relative decomposition only.

Both determinant terms can now be estimated without dropping them.
Since P is an orthogonal projection, 0<=P_ee<=1. Furthermore

\[
 JJ^*=M\Delta^{-1}M^*,\qquad
 J^*J\le16 B\Delta^{-2}B^*\le16L^{-1}.                        \tag{24}
\]

For the inequality, each row of M has at most two unit entries and
each interior vertex has degree eight, so
||Mu||^2<=16||u||^2. By positivity and (22), every entry of
Delta^{-1} has absolute value at most 30. Each diagonal of JJ*
is therefore at most 120, while each diagonal of J*J is at most
480. Rowwise Cauchy–Schwarz yields

\[
 \sum_f|J_{ef}J_{fe}|\le\sqrt{120\,480}=240,\qquad
 \|D\|_{\mathrm{op}}\le\frac14+60=\frac{241}{4}.              \tag{25}
\]

Symmetry of D bounds its operator norm by its largest absolute row
sum; restriction to H cannot increase it. These are deliberately
coarse constants, independent of N and valid also for boundary rows.

A bounded diagonal does not imply a small Hilbert–Schmidt norm.
For each all-positive index k the edge-mode block has dimension four;
B spans one longitudinal direction, leaving three transverse
polarizations of eigenvalue lambda_k. If precisely one index is zero,
there is one allowed edge component, already transverse. Thus, for
one color,

\[
 \operatorname{Tr}G^2=
 3\sum_{k\in\{1,\ldots,N-1\}^4}\lambda_k^{-2}
 +\sum_{\mu=1}^4\ \sum_{\substack{k_\mu=0\\1\le k_\nu<N\ (\nu\ne\mu)}}
                  \lambda_k^{-2}.                           \tag{26}
\]

This expression includes all boundary mode sectors. For an explicit
upper estimate use G<=L^{-1} on their common invariant decomposition,
(21), and at most 15m^3 indices per component. For a lower estimate
retain the all-positive indices of maximum m. There are
m^4-(m-1)^4>=m^3 such indices, and
lambda_k<=pi^2 |k|^2/N^2<=4pi^2 m^2/N^2. With
H_(N-1)=sum_(m=1)^(N-1) 1/m, the bounds are

\[
 \frac{3N^4}{16\pi^4}H_{N-1}
 \le\operatorname{Tr}G^2
 \le\frac{15N^4}{4}H_{N-1}.                                 \tag{27}
\]

All three colors multiply these bounds by three. Since N>=2,
H_(N-1) is comparable to log(eN), giving
||G||_HS of order N^2 sqrt(log(eN)), with constants independent of N.
This is an exact spectral scale estimate, not evidence for that
scale in kappa_a.

Finally let P_\pm=G^(1/2)K_\pm G^(1/2) on H. The same finite
quadratic response argument as L279(28)–(29) applies because the
curvature law is L003's law:
0<=P_\pm<=F and Tr(P_-P_+)=2q_a. It gives
||P_-P_++P_+P_-||_HS<=2F sqrt(2q_a). Therefore the **full density**
contribution obeys the insufficient bound

\[
 |\operatorname{Tr}(D G_{-+})|
 \le 2F\sqrt{2q_a}\,
       \|G^{1/2}D G^{1/2}\|_{\mathrm{HS}}
 \le\frac{241}{2}F\sqrt{2q_a}\,\|G\|_{\mathrm{HS}}
 =O(N^2\sqrt{\log(eN)}).                                    \tag{28}
\]

For the second inequality, diagonalize G with nonnegative eigenvalues
r_i. Then sum_(i,j) r_i r_j |D_ij|^2 is at most
sum_i r_i^2 sum_j |D_ij|^2, using
2r_i r_j<=r_i^2+r_j^2 and symmetry, and this is at most
||D||_op^2 sum_i r_i^2. Boundedness of q_a is supplied by L003.
No sign or lower bound for Tr(D G_-+) follows from (28).

The required estimate remains
|mathcal K_3^H+mathcal K_4^H+Tr(D G_-+)|<=C log(eN), with all
terms in (20) summed with their signs. Equation (28) falls short;
it cannot be used as an estimate of the other terms or of their sum.
In particular the distinct-line G_-,G_+ contractions and the source
jets cannot be bounded just by Tr(P_-P_+). This calculation rules out
claiming the desired bound from bounded covariance diagonals and the
available Hilbert–Schmidt response estimate alone. It does not rule
out stronger separated-kernel estimates or signed cancellation.

**Decision:** park this absolute-norm approach. One mathematical
EXPLORATION turn has been used on the transverse mechanism. A second
attempt on the same covered target must test an actual finite-domain
cancellation across the complete (20), including the insertion jets;
repeating (19), (25) or (28) is not a continuation. No uniform higher
remainder, interacting lower bound, or continuum result is obtained.

### 8. Direct gauge-identity cancellation test (2026-10-25)

This is the second bounded transverse test under the same approved
full-coefficient assessment. Its conclusion is a limitation of using
gauge-variation identities alone, **not** a failure of the Wilson
logarithmic bound. The comparison below is a finite Gaussian diagnostic;
it does not change the hypotheses or action in (2).

First keep the jets on the full edge space X, before restricting them
to H. Write phi_m=(mathcal S-sH_{h_-}-tH_{h_+})_[m]. For every
u in V the exact infinitesimal gauge identity is

\[
 d_x[\Phi_{s,t}(\exp x)][\mathcal D(x)u]=0.                 \tag{29}
\]

Here the differential means that of the function x maps to
Phi_{s,t}(exp x). Expand D(x) by (10), and use that the constant
and linear phase jets vanish. Its homogeneous degrees one, two and
three give, on all of X,

\[
\begin{aligned}
 d\phi_2(x)[Bu]&=0,\\
 d\phi_3(x)[Bu]+d\phi_2(x)[D_1(x)u]&=0,\\
 d\phi_4(x)[Bu]+d\phi_3(x)[D_1(x)u]
                         +d\phi_2(x)[D_2(x)u]&=0.
\end{aligned}                                                \tag{30}
\]

No boundary term was dropped: u is zero at every boundary vertex,
while D_1,D_2 contain both normal-endpoint rows displayed after (10).
The identities hold for every allowed source, so differentiating
them retains both insertion jets. They determine orbit-direction
derivatives; they do not assert that the restrictions of phi_3,phi_4
to H vanish. Nor may one replace D(x) by its orthogonal projection
to H and declare a measure-preserving vector field there. The true
quotient coordinate v of (3) is unchanged by a gauge transformation,
including the nonlinear return to the slice.

The measure identities do not supply an extra transverse equation.
Product Haar invariance says exactly
div_X(j_X(x) D(x)u)=0, where j_X=product_e j(x_e).
For example, div_X(D_1(x)u)=0 by the zero trace of ad, and

\[
 \operatorname{div}_X(D_2(x)u)=\tfrac16\sum_e x_e\cdot(Bu)_e,
 \qquad
 d(\log j_X)_{[2]}(x)[Bu]=-	frac16\sum_e x_e\cdot(Bu)_e.
                                                               \tag{31}
\]

To check the first equality edgewise, ad(x)^2 z=x(x dot z)-|x|^2 z
and its three-dimensional divergence is 2 x dot z; multiply by 1/12.
This includes edges with either boundary endpoint. The second is
the all-link Haar jet. On the quotient, both gauge-coordinate
determinant terms remain in ell_2 by (4); (31) is not permission to
remove them. Integrating out the normalized orbit in (3) leaves
rho(v)dv and an arbitrary invariant phase on that quotient.

A diagnostic quantifies the unconstrained transverse freedom and
tests it **after** both source derivatives, keeping the entire signed
formula (7). Fix a mesh-independent lambda>0 and consider, solely
for comparison, the gauge-invariant phase

\[
 \widehat\Phi_{s,t}(U)=\Phi_{s,t}(U)+\lambda\mathcal S(U)^2.
                                                               \tag{32}
\]

It has the same source insertions and the same quadratic and cubic
phase jets. Its quartic jet is phi_4+lambda S_2^2. Both exact phases
satisfy (29), with the same D(x), and hence every identity (30).
In particular d(S_2^2)[Bu]=2S_2 dS_2[Bu]=0. The measure, slice,
Haar jet and both density determinants are identical. Positivity
and the flat zero orbit are preserved since
widehat Phi >= (1-eta)mathcal S. The added term is nonlocal: it
couples different plaquettes through the square of their total action.
Consequently it tests gauge identities without Wilson locality, and
is not a counterexample within the target's specified action class.

Let widehat R_H denote the finite expression on the right of (7)
with W_H replaced by W_H+lambda(S_2^H)^2. Without estimating any
individual diagram, the exact difference of the **complete** sums is

\[
 \widehat R_H(s,t)-R_H(s,t)
                  =-\lambda E^H_{s,t}[(S_2^H)^2].             \tag{33}
\]

All cubic, insertion and full-density terms cancel between these two
expressions because they are unchanged, rather than being set to zero.
Source differentiation in (33) includes the changing Gaussian means.
No asymptotic remainder is differentiated or claimed uniform.

Here is the full mixed derivative of (33). Put d_H=dim H and work
intrinsically on H. Let K=C*C|_H>0, G=K^{-1}, and use the P_-,P_+
of section 7. The variable z=K^{1/2}x has source covariance
A(s,t)=(1-sP_--tP_+)^{-1} and S_2^H=|z|^2/2. Finite Gaussian
pairing, as used in (19), gives

\[
 E^H_{s,t}[(S_2^H)^2]
       =\tfrac14\{(\operatorname{Tr} A)^2+2\operatorname{Tr}(A^2)\}.
                                                               \tag{34}
\]

At zero, A=1, A_s=P_-, A_t=P_+, and
A_st=P_-P_++P_+P_-. Thus

\[
\begin{aligned}
 \mathcal A_N
 &:=\left.\partial_s\partial_t E^H_{s,t}[(S_2^H)^2]\right|_0\\
 &=\tfrac12\operatorname{Tr}P_-\operatorname{Tr}P_+
              +(d_H+3)\operatorname{Tr}(P_-P_+),\\
 \widehat\kappa_a-\kappa_a&=-\lambda\mathcal A_N.
\end{aligned}                                                 \tag{35}
\]

For clarity, the mixed derivative of (Tr A)^2 is
2 Tr P_- Tr P_+ +4 d_H Tr(P_-P_+); that of 2 Tr(A^2) is
12 Tr(P_-P_+). These give every factor in (35).
The symbols widehat kappa and kappa here mean mixed derivatives of
the displayed finite coefficient expressions; no new interacting
comparison or limiting theory is inferred.

Since f_*>=0, P_-,P_+ are positive semidefinite. Their traces are
nonnegative and Tr(P_-P_+)=2q_a by the same quadratic curvature law
used in section 7. There are 4N(N-1)^3 relative edges and (N-1)^4
interior vertices; injectivity of B therefore gives

\[
 d_H=3(N-1)^3(3N+1),\qquad
 \mathcal A_N\ge 2(d_H+3)q_a
                \ge 2(d_H+3)c_{\rm box}                      \tag{36}
\]

on L003's sufficiently fine even-mesh range. In particular d_H is
of order N^4, and the last bound grows at least as N^4. The two
mixed coefficients cannot both satisfy an O(log(eN)) bound: their
difference (35) already exceeds that scale. This is a lower bound
on their difference, not on the actual Wilson kappa_a. There is
no claimed sign or divergence for that kappa_a or any of its summands.

**Test result and decision.** The exact finite-domain orbit identities
and complete measure identities admit transverse changes with a
power-growing mixed coefficient. They alone cannot force the target
bound; one must additionally use specific Wilson locality and signed
kernel estimates. This test retains every source jet and both density
determinants and supplies no such estimate for the fixed Wilson sum
(20). Stop this direct gauge-identity cancellation mechanism after its
second transverse attempt, preserving ATTEMPTS/047–048. This is a
limitation of the tested inference, not a ban on future Wilson-specific
cancellation with a new discriminating input. No uniform higher error,
continuum construction or mass-gap conclusion follows.

## Mathlib

Coverage of the full local relative-Coulomb chart, density jet,
two-source identity and section 8's diagnostic is **not checked**.
Coverage of supporting analytic
inverse-function/change-of-variables theorems, SU(2) exponential Haar
volume, and finite-dimensional Laplace expansions is **not checked**
in Mathlib. No exact library theorem name or link is asserted. The
primary mathematical citations and the box-specific applicability
proof above are the evidence for this informal specialization.

For section 7, Mathlib coverage of the complete signed coefficient,
density matrix and finite-domain estimates is **not checked**. The
finite Gaussian pairing and relative mode inputs are the explicitly
proved specializations in L279 and L003, respectively; no new external
renormalization or boundary theorem is invoked.
