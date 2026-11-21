# Lemma 888: finite pinned-fiber replacements cannot lower mass; free traces retain an interface cost

## Hypotheses

Use exactly the actual entire function and positive constants of L847,

\[
G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2}),\qquad
R>0,\quad RG'(R)/G(R)=1,\quad C=R^2/G(R)^2,
\]
\[
F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
\qquad
\omega=C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
                  dz_1\wedge dz_2.                       \tag{1}
\]

Assume the L879 hypotheses: u:T^2 -> R^2 is smooth, real and
periodic, J=det(I-iDu) is nowhere zero, and the full mass is stationary
under smooth real radial variations supported away from its density
zeros. Write

\[
z_j=R e^{u_j+iy_j},\quad H=I-iDu,\quad Q=F(z_1,z_2)J,
\quad \mathcal B(u)=(2\pi)^{-2}\int_{T^2}|Q|.
\]

L879 supplies Q=lambda*s with |lambda|=1 and smooth real s. Assume
conditionally the exact clean strip in the approved target:

\[
S=(l,r)\times(c,d),\quad l=\alpha-\epsilon,
\quad r=\beta+\epsilon,\quad \alpha<\beta,\quad\epsilon>0,
                                                               \tag{2}
\]

whose closure lies in a lifted angular chart. On its closure the only
density zeros are the two complete simple G(z1)-zero fibers at
y1=alpha,beta. The factors G(z2), z1-z2 and J are nonzero there.
On each fiber z1 is consequently one fixed simple zero zeta_gamma
of G, gamma in {alpha,beta}. This follows from continuity into the
discrete zero set, or from the complete-fiber statement in L879.
In particular partial_2 u1(gamma,y2)=0. No existence of such an
actual graph or pair of labels is asserted.

Let v be any smooth real vector field compactly supported in S,
extended by zero to the torus, and put u_tilde=u+v. For admissible
replacements require J_tilde=det(I-iD u_tilde)!=0 everywhere.
The comparison below does not require J to stay nonzero on the
linear homotopy from u to u_tilde. It retains all new density zeros.

Define the three closed rectangles, each with orientation dy1 wedge dy2,

\[
D_0=[l,\alpha]\times[c,d],\qquad
D_1=[\alpha,\beta]\times[c,d],\qquad
D_2=[\beta,r]\times[c,d].                                  \tag{3}
\]

Their overlapping edges have area zero. The signs of s on their
interiors are sigma_0=sigma_2=sigma and sigma_1=-sigma for one
sigma in {1,-1}. Simplicity justifies these sign changes below.

## Conclusion

First, for **every finite replacement satisfying these hypotheses and**

\[
v_1(\alpha,y_2)=v_1(\beta,y_2)=0
                   \quad(c\le y_2\le d),                  \tag{4}
\]

one has the full, normalized mass inequality

\[
                         \mathcal B(u+v)\ge\mathcal B(u).  \tag{5}
\]

There is no amplitude or derivative bound in (5), apart from smoothness
and the stated endpoint admissibility. Both components may change,
v2 may change on both fibers, and arbitrary coupling inside the strip
is allowed. The proof includes an explicit nonzero coupled finite
replacement with endpoint J!=0 to which (5) applies. Thus (5) stops
that contact-preserving construction at the required threshold:
the achieved bound is mass difference >=0, whereas descent requires <0.

For general v without (4), retain the following exact unpaid term.
Let

\[
\Psi(t,y)_j=R e^{u_j(y)+t v_j(y)+iy_j},\qquad 0\le t\le1,
\]
\[
T_\gamma=\int_0^1\int_c^d
 \omega_{\Psi(t,\gamma,y_2)}
       (\partial_t\Psi,\partial_{y_2}\Psi)\,dy_2\,dt,
\qquad \gamma\in\{\alpha,\beta\}.                         \tag{6}
\]

For Q_tilde=F(Phi_(u+v))*J_tilde set

\[
E(v)=\sum_{k=0}^2\int_{D_k}
 \bigl(|Q_{\rm tilde}|-\sigma_k
          \operatorname{Re}(\overline\lambda Q_{\rm tilde})\bigr)
 \ge0.                                                     \tag{7}
\]

Then

\[
(2\pi)^2[\mathcal B(u+v)-\mathcal B(u)]
   = E(v)+2\sigma\operatorname{Re}
               \{\overline\lambda(T_\alpha-T_\beta)\}.     \tag{8}
\]

Consequently a finite depinning construction must prove

\[
2\sigma\operatorname{Re}
       \{\overline\lambda(T_\alpha-T_\beta)\}<-E(v).        \tag{9}
\]

No sign of the left side or bound paying E(v) is asserted for free
traces. In particular (5) is not a no-descent theorem for the entire
approved competitor class, a local-minimum theorem, or an exclusion
of the conditional stationary configuration. It does not prove graph
or minimizer existence/compactness, the sharp L868 bound, higher
mixed signs or RH. This is a reproduction/specialization of the
known boundary-calibration method, with a finite conditional application;
it is not a claim of a new general theorem or certified originality.
The result has not received an independent audit.

## Proof

### Reused coverage, boundary method and scope

The invocation-start assessment is
`drafts/literature/2026-11-07-paired-fiber-finite-replacement-test.md`,
DECISION EXPLORE. Its unchanged scope permits one finite coupled test
or an applicable actual-form boundary obstruction. This attempt tests
the explicitly restricted construction (4), and keeps (9) for the
unrestricted case rather than silently imposing (4) on all competitors.

The known method is Scott Lawrence and Yukari Yamauchi,
*Convex optimization and contour deformations*, arXiv:2311.13002v2,
14 August 2024, [Section III, equations (18)-(19), p5](https://arxiv.org/pdf/2311.13002v2#page=5):
a closed dominated form gives a boundary/homology mass bound.
Here the forms used on the separate pieces are
sigma_k*Re(conjugate(lambda)*omega). Domination is the elementary
inequality |Re(z)|<=|z| on every real tangent two-plane, including
degenerate planes and zeros. The application difference is that these
three forms have different signs. They are NOT asserted to make one
globally closed ambient certificate. Their internal boundary fluxes
are retained in (6)-(9); they vanish under (4).

For smooth pullback differentiation reuse Guillemin and Sternberg,
*Semi-classical analysis*, 13 January 2010,
[Sections 13.13-13.14.1, equations (13.7)-(13.9), pp449-455](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
For its integrated boundary interpretation reuse Lebl, *Tasty Bits
of Several Complex Variables*, v4.4, 31 May 2026,
[Appendix C, Theorem C.6 and regularity remark, p224](https://www.jirka.org/scv/scv.pdf#page=224).
These are the already inspected inputs in the approved assessment.
We use L879's explicit adjugate specialization and integrate its
divergence over rectangles; this also makes all signs and corners
explicit without assuming an invertible homotopy.

L847 supplies the actual form and full pullback. L879 supplies its
phase-line conclusion and variation identity. L883's boundary-fiber
comparison is relevant overlap, not an additional mathematical premise:
no four global fibers, label primitive or conjugate branch is used here.
The L867 global all-plane certificate stop does not rule out this
separate-piece comparison. L887's fixed nonzero-trace expansion and
the attempt65/69 signed-kernel/primitive stops are comparisons only.
None is rederived or strengthened to an unrestricted finite stop.

### Sign and saturation on the three original pieces

The actual Q is nonzero on each connected open rectangle in (3),
so s has one sign there. At a fiber y1=gamma put
zeta=zeta_gamma, eta=z2(gamma,y2) and a=partial_1 u1(gamma,y2).
Differentiating the G(z1) factor, with all other differentiated terms
containing G(zeta)=0, gives

\[
\partial_1 Q(\gamma,y_2)=
-C\frac{G'(\zeta)G(\eta)(\zeta-\eta)^2}{\zeta^2\eta^2}
       J(\gamma,y_2)\zeta(a+i)\ne0.                        \tag{10}
\]

Every nonzero factor is covered by the hypotheses; a is real, so
a+i!=0. Since Q=lambda*s, (10) proves a simple real sign crossing
at each fiber. Hence the pattern is sigma,-sigma,sigma. Up to the
zero-measure edges, each piece saturates its own dominated form:

\[
\int_{D_k}|Q|=
\sigma_k\operatorname{Re}\left(\overline\lambda
                                      \int_{D_k}Q\right). \tag{11}
\]

This is the extra information that an unchanged total period alone
does not supply.

### Full finite boundary identity, with singular intermediate J allowed

The compact homotopy image stays in a product of compact annuli in
(C*)^2: u and v are bounded and t belongs to [0,1]. Thus omega,
all map derivatives and all integrands below are smooth and bounded
on their compact parameter domains. Numerator zeros are not poles.
Differentiation under the finite integrals and Fubini are therefore
justified by uniform bounds. No limit of contours is taken.

Put W_t=y-i(u+t v), H_t=D W_t and
f(W)=F(R exp(iW_1),R exp(iW_2)). L879's variation formula, in its
division-free form, is

\[
Q_t=f(W_t)\det H_t,\qquad
\partial_t Q_t=\operatorname{div}_y B_t,\qquad
B_t=-i f(W_t)\operatorname{adj}(H_t)v.                     \tag{12}
\]

The adjugate derivation applies even when det H_t=0. Indeed each
column of adj(D W_t) has zero divergence by equality of mixed
derivatives, and H_t*adj(H_t)=(det H_t)I. Expanding the right side
of (12) gives
-i(det H_t)*sum_j f_(W_j)*v_j - i*f*tr(adj(H_t)*Dv), exactly
the derivative of f(W_t)*det H_t. This is the same polynomial
specialization as L879, not an extension based on division by J_t.

For any fixed x in [l,r], direct evaluation of (1) gives

\[
(B_t)_1(t,x,y_2)=
\omega_{\Psi(t,x,y_2)}(\partial_t\Psi,\partial_{y_2}\Psi).
                                                               \tag{13}
\]

For example, with A_t=D(u+t v), the first adjugate row in (12)
is (1-i(A_t)22, i(A_t)12), so this coefficient is
-F(Psi)*[v1*((A_t)22+i)-v2*(A_t)12]. In (1) the wedge evaluation
is z1*z2 times that bracket and the positive C coefficient equals
-F/(z1*z2), confirming the sign and all mixed derivative terms.

Integrate (12) over a cell and use the one-variable fundamental
theorem of calculus in both coordinates, then integrate in t. The
upper y1 boundary contributes +(B_t)1 and the lower contributes
-(B_t)1. All exterior boundaries contribute zero because v=0 in
a neighborhood of the whole strip boundary, so B_t=0 there.
Writing P_k=integral_(D_k) Q and P_tilde,k similarly, this yields

\[
P_{{\rm tilde},0}-P_0=T_\alpha,\qquad
P_{{\rm tilde},1}-P_1=T_\beta-T_\alpha,\qquad
P_{{\rm tilde},2}-P_2=-T_\beta.                            \tag{14}
\]

All four boundaries of each rectangle are included, and no extra
corner term occurs in these iterated integrals of a smooth divergence.
The unchanged total-period sum is only the sum of (14); the individual
fluxes need not be zero.

Combining (11), (14), and the definition (7), the difference of the
three absolute integrals is exactly E plus
sigma*Re(conjugate(lambda)*(T_alpha-(T_beta-T_alpha)-T_beta)).
Outside S the density is unchanged, including its derivatives.
This proves (8) with the stated torus normalization. Pointwise
|z|-sigma_k*Re(conjugate(lambda)*z)>=0 proves E>=0 on the entire
cells, including all transition collars and new numerator zeros.
Equation (9) is therefore precisely equivalent to strict descent
for any proposed finite endpoint; it is not asserted to be satisfied.

### Actual trace flux and the pinned obstruction

Formula (6) can be evaluated without solving for the interior graph.
For each gamma put, on [c,d],

\[
a_\gamma=v_1(\gamma,\cdot),\quad
b_\gamma=v_2(\gamma,\cdot),\quad
\eta_\gamma=z_2(\gamma,\cdot),\quad
k_\gamma=\partial_2u_2(\gamma,\cdot),
\]
\[
w_1=\zeta_\gamma e^{t a_\gamma},\qquad
w_2=\eta_\gamma e^{t b_\gamma}.
\]

Primes below denote y2 derivatives. Since the original z1 is constant
on the fiber, differentiation of these explicit traces gives exactly

\[
T_\gamma=C\int_0^1\int_c^d
\frac{G(w_1)G(w_2)(w_1-w_2)^2}{w_1^2w_2^2}
\left[a_\gamma(k_\gamma+i+t b_\gamma')
                         -t b_\gamma a_\gamma'\right]dy_2dt.
                                                               \tag{15}
\]

In particular the mixed trace term -t*b_gamma*a_gamma' is retained.
All integration ranges are compact, w1,w2 are nonzero, and no G
factor is divided out. Thus (15) also includes any new numerator zeros.
It makes no sign assertion when a_gamma is nonzero.

Under (4), a_gamma and its derivative vanish, w1=zeta_gamma for
the whole trace homotopy, and T_gamma=0. This can also be seen
directly because the ambient form (1) vanishes on that homotopy.
Equations (7)-(8) now prove (5) for the full finite class (4).
Equality holds precisely when Q_tilde belongs to the ray
lambda*sigma_k*[0,infinity) on each open D_k: a continuous
nonnegative integrand in (7) has zero integral exactly when it is
identically zero. Zeros themselves satisfy this condition. No
stationarity or phase hypothesis on the replacement was assumed.

### One concrete finite coupled construction, with its endpoint checked

Let eta(t)=exp(-1/(1-t^2)) for |t|<1 and eta(t)=0 otherwise. Put

\[
m=(\alpha+\beta)/2,\quad h=(\beta-\alpha)/2+\epsilon/2,
\quad n=(c+d)/2,\quad k=(d-c)/4,
\]
\[
\chi(y)=\eta((y_1-m)/h)\eta((y_2-n)/k),\qquad
V(y)=\big((y_1-\alpha)(y_1-\beta)\chi(y),\ \chi(y)\big).
                                                               \tag{16}
\]

This is smooth with compact support in S, positive chi on interior
segments of both fibers, and V1=0 on those fibers. Both components
are nonzero functions; both fields depend on both variables.
Extend V by zero to the torus. Smooth extension and periodicity follow
from compact support strictly inside the lifted chart. Every cutoff
transition is part of the same field and of E in (7).

Since H is invertible everywhere on a compact torus, the operator-norm
bound K=sup_(T2)||H^(-1)DV|| is finite. Choose the specific positive
finite parameter tau=1/[2(1+K)] and set v=tau*V. Then

\[
I-iD(u+\tau V)=H(I-i\tau H^{-1}DV),\qquad \tau K<1/2.
                                                               \tag{17}
\]

The second factor has no nonzero null vector: such a vector w would
satisfy ||w||<=tau*K*||w||<||w||. Hence the endpoint Jacobian is
nowhere zero. The exterior and its entire collar are unchanged.
This gives an admissible nonzero finite coupled endpoint for every
conditional datum in the hypotheses, without asserting that any
such datum exists. By (4)-(5), this endpoint has mass >= the original
mass. More generally no admissible amplitude in this pinned class
can give strict decrease. The proof is finite, not an asymptotic
expansion in tau.

The obstruction stops precisely the fiber-preserving mechanism.
A replacement that lowers mass must change the first radial component
on at least one of the two fibers and must meet (9), including E and
endpoint nondegeneracy. The sign of (15), an interior extension paying
(9), and configuration/minimizer existence remain unresolved. An
unchanged omega period or a proposed negative interface term alone
does not pay the missing full mass cost.

## Mathlib

Full matching coverage for this finite strip comparison, and supporting
coverage for the constrained pullback/boundary integration, were not
checked. No Mathlib theorem is imported and no absence claim is made.
The endpoint norm argument and the complete analytic inequalities
above are informal checks, not Lean verification or an independent
audit. No numerical evidence or mathematical script is used.
