# Lemma 892: a connected bridge of sufficiently small transverse width increases full mass

## Hypotheses

Retain L847's actual entire function and positive constants,

\[
G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2}),\qquad
R>0,\quad RG'(R)/G(R)=1,\quad C_G=R^2/G(R)^2,
\]
\[
F(z_1,z_2)=-C_G\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2}.
                                                               \tag{1}
\]
Evenness defines G without a square-root branch. Assume L879's
smooth real periodic graph u:T^2 -> R^2, with J=det(I-iDu) nowhere
zero and stationarity for radial variations supported away from
its density zeros. Put

\[
z_j(x,y)=R e^{u_j(x,y)+i\theta_j},\quad (\theta_1,\theta_2)=(x,y),
\quad Q(x,y)=F(z_1,z_2)J(x,y),\quad
\mathcal B(u)=(2\pi)^{-2}\int_{T^2}|Q|.
                                                               \tag{2}
\]

Condition on the approved clean strip S=(l,r)x(c,d), with compact
closure in one lifted angular chart and l<alpha<beta<r. Its only
density zeros are the two complete simple G(z1)-zero fibers at
x=alpha,beta; G(z2), z1-z2 and J are nonzero on the closure. Thus
z1(gamma,y)=zeta_gamma is constant on each fiber and u1,y=0 there.
No actual stationary graph or such configuration is asserted to exist.

Fix y0 in (c,d) and one smooth real cutoff rho with compact support
in (l,r), values in [0,1], and rho=1 on a neighborhood of
[alpha,beta]. Fix the entire profile, including its collars:

\[
\eta(Y)=\begin{cases}e^{-Y^2/(1-Y^2)},&|Y|<1,\\0,&|Y|\ge1,
\end{cases}\qquad \phi(Y)=\eta(Y)+Y\eta'(Y),
\quad \bar h=\tfrac14\min\{y_0-c,d-y_0,1\}>0.
                                                               \tag{3}
\]

For definiteness rho may be fixed as follows. Let
a0=l+(alpha-l)/4, a1=alpha-(alpha-l)/4,
b1=beta+(r-beta)/4, b0=r-(r-beta)/4. Define
e(t)=exp(-1/t) for t>0, zero otherwise, and
T(t)=e(t)/(e(t)+e(1-t)). Then take
rho(x)=T((x-a0)/(a1-a0))*T((b0-x)/(b0-b1)).
This is positive on (a0,b0) and one on [a1,b1], so its support
connects the two fibers through the whole middle cell.

For 0<h<=bar h, define the single bridge shape

\[
v_h(x,y)=\bigl(h\rho(x)\eta(Y),\,-hY\rho(x)\eta(Y)\bigr),
\qquad Y=(y-y_0)/h,\qquad u_h=u+v_h.                       \tag{4}
\]

Extend it by zero to the torus. The nominated finite endpoint is
h=bar h. Smaller h in (4) are members of the same shape family;
a conclusion about them does not certify that nominated endpoint.
No nonvanishing of J_h is assumed for the mass calculation below.
Admissibility for the replacement problem still requires it.

## Conclusion

The constants m>0 and K>=0 defined in (8) and (13) below are finite
and depend only on the conditional actual data and fixed cutoff.
For every 0<h<=bar h, the full, finite mass difference satisfies

\[
\left|(2\pi)^2[\mathcal B(u_h)-\mathcal B(u)]-hm\right|
 \le 2(r-l)K h^2.                                         \tag{5}
\]

In particular, for the explicit positive threshold

\[
h_* =\min\left\{\bar h,\frac{m}{4(r-l)(1+K)}\right\},
\qquad 0<h\le h_*\quad\Longrightarrow\quad
\mathcal B(u_h)-\mathcal B(u)
 \ge\frac{hm}{2(2\pi)^2}>0.                              \tag{6}
\]

The whole middle cell, both x collars, both y collars, all numerator
zeros, and the full determinant are included. No contact-slope
restriction is imposed. If a bridge in this range is admissible,
it cannot lower mass; if its endpoint J vanishes, it already fails
the separate admissibility requirement. Formula (17) below gives
a sufficient endpoint check, not an automatic nonvanishing claim.

For the nominated h=bar h, (5) gives a strict obstruction if
2(r-l)K*bar h<m. Neither this numerical inequality nor nonvanishing
of that endpoint is asserted for arbitrary conditional data. When
the inequality is unverified or fails, the nominated full-mass sign
is unresolved. A failed sufficient bound is not evidence of descent.

The independent conceptual audit of 7 November 2026 below accepts
this conditional specialization of the full pullback and triangle
inequality, classified REPRODUCTION. It is
not a general obstruction to finite connected replacements, a
realized actual-G example, a paired-configuration exclusion, a
new general contour theorem or certified novelty. Minimizer
existence/compactness, other contacts, L868's sharp bound, higher
mixed signs and Xi transfer remain open.

## Proof

### Assessed scope, source reuse and nonduplication

Use the invocation-start EXPLORE assessment
`drafts/literature/2026-11-07-paired-fiber-finite-replacement-test.md`
and its inspected parent comparison. They permit this finite
coupled strip construction and an explicitly scoped actual-form
obstruction. L887's fixed one-component infinitesimal calculation,
L888's pinned traces, L889's small trace box, L890's disjoint fixed
shears and L891's two shrinking squares do not evaluate (4). In
particular no slope subclass or conclusion of L891 is an input.
Attempt65/69's unsigned-kernel/unpaid-chord stops are unchanged.
The targeted local comparison found no matching connected-strip
calculation; this is not a novelty claim.

The exact radial pullback is imported from L847:
Phi_u^*omega=F(Phi_u)det(I-iDu) dx wedge dy, including zeros.
Its underlying smooth pullback calculus is the already inspected
Guillemin and Sternberg, *Semi-classical analysis*, 13 January 2010,
[Sections 13.13–13.14.1, (13.7)–(13.9), pp449–455](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
We use its full finite formula, not an off-zero variation or
existence theorem. For comparison, Lawrence–Yamauchi,
*Convex optimization and contour deformations*, arXiv:2311.13002v2,
14 August 2024,
[Section III, (18)–(19), p5](https://arxiv.org/pdf/2311.13002v2#page=5),
requires a closed dominated form for a boundary certificate. No
global calibration, dual attainment or graph realization is imported.
The elementary integral triangle inequality and fundamental theorem
of calculus below suffice. The application difference requiring
calculation is the full determinant for this bridge and its uniform
finite actual-G error; no general optimization theorem is reproved.

### Exact rescaling over the whole support

Let P=[l,r]x[-1,1]. For t in [0,bar h] and (x,Y) in P, put

\[
a(x,Y)=\binom{\rho\eta}{-\rho Y\eta},\quad
D_0(x,Y)=\begin{pmatrix}0&\rho\eta'\\0&-\rho\phi\end{pmatrix},
\quad
D_1(x,Y)=\begin{pmatrix}\rho'\eta&0\\-\rho'Y\eta&0\end{pmatrix},
\]
\[
A_t=Du(x,y_0+tY),\qquad
Z_{t,j}=R\exp\{u_j(x,y_0+tY)+t a_j(x,Y)
                         +i\theta_{t,j}\},
\quad (\theta_{t,1},\theta_{t,2})=(x,y_0+tY),
\]
\[
j_t=\det[I-i(A_t+D_0+tD_1)],\qquad
q_t=F(Z_{t,1},Z_{t,2})j_t,\qquad
r_t=Q(x,y_0+tY).                                         \tag{7}
\]

These are smooth functions on the compact set [0,bar h]xP,
including t=0 and Y=+-1. The bump and all derivatives vanish at
Y=+-1; its standard smoothness follows by writing it as
e*exp(-1/(1-Y^2)) inside and extending by zero. The fixed cutoff
has the same smooth flat-endpoint property. The Z_t lie in compact
annuli of (C*)^2, since the real exponents are bounded. G is entire,
so numerator zeros are not singularities in (7).

For h>0, direct differentiation of (4) gives
Dv_h(x,y0+hY)=D0+hD1, with row j, column k equal to partial_k v_j.
Consequently q_h is exactly the endpoint full density in the
rescaled support and r_h exactly the original density there.
Outside [l,r]x[y0-h,y0+h] the graph and its derivatives are
unchanged. Since dy=h dY,

\[
(2\pi)^2[\mathcal B(u_h)-\mathcal B(u)]
 =h\int_P(|q_h|-|r_h|)\,dx\,dY,\qquad
m=\int_P(|q_0|-|Q(x,y_0)|)\,dx\,dY.                      \tag{8}
\]

The t=0 quantities in (7) are auxiliary smooth rescaled functions,
not the derivative of an h=0 graph variation. Indeed Dv_h need
not tend to zero. Equation (8) is exact for every positive h.

### The full leading coefficient is strictly positive

Write H(x)=I-iDu(x,y0), Q0(x)=Q(x,y0), and
b(x,Y)=(rho*eta',-rho*phi)^T, so D0=b e2^T.
Invertibility of the original H gives the elementary rank-one
determinant identity

\[
q_0(x,Y)=Q_0(x)\left[1-i e_2^T H(x)^{-1}b(x,Y)\right].   \tag{9}
\]

For completeness this particular identity follows by factoring H
and using det(I+c e2^T)=1+c2 for a two-by-two matrix; no determinant
factor has been dropped. Both components of b have zero Y integral:
integral eta'=eta(1)-eta(-1)=0 and
integral phi=[Y eta(Y)]_{-1}^1=0. Thus, for every x,

\[
\int_{-1}^1q_0(x,Y)\,dY=2Q_0(x),\qquad
\int_{-1}^1|q_0(x,Y)|\,dY\ge2|Q_0(x)|.                 \tag{10}
\]

This includes original contacts: if Q0=0, original J!=0 implies
F(z(x,y0))=0, hence q0=0 for every Y. No division by Q0 at those
x is made. Integrating (10) gives m>=0 and prevents negative
contributions from any of the x collars from cancelling the
strict contribution found next.

At (alpha,y0), the complete fiber gives u1,y=0. Write its real
matrix as A=[[p,0],[n,k]]. Direct triangular inversion gives

\[
\operatorname{Re}(H(\alpha)^{-1})_{22}
 =\operatorname{Re}\frac1{1-ik}=\frac1{1+k^2}>0.           \tag{11}
\]

By continuity choose x0 strictly between alpha and beta,
sufficiently close to alpha that rho(x0)=1 and
Re(H(x0)^(-1))22>0. Cleanliness gives Q0(x0)!=0. At Y=0,
eta=phi=1 and eta'=0, so (9) gives
q0(x0,0)/Q0(x0)=1+i(H(x0)^(-1))22. Its imaginary part is
strictly positive. Thus q0(x0,0) does not lie on the nonnegative
ray through Q0(x0).

Here is an explicit positive-measure justification, rather than
using a single point to claim strict integral inequality. Put
theta(x)=Q0(x)/|Q0(x)| wherever Q0(x)!=0; it is continuous on
the middle cell. The continuous quantity
Im(conjugate(theta(x))*q0(x,Y)) is positive at (x0,0).
Choose a closed interval I0 contained in (alpha,beta) of positive
length, 0<delta<1 and kappa>0 so it is >=kappa on
K0=I0x[-delta,delta]. Set M0=max_K0 |q0|, which is finite and
at least kappa. Then on K0,

\[
|q_0|-\operatorname{Re}(\overline\theta q_0)
 =\frac{[\operatorname{Im}(\overline\theta q_0)]^2}
 {|q_0|+\operatorname{Re}(\overline\theta q_0)}
 \ge\frac{\kappa^2}{2M_0}>0.                              \tag{12}
\]

The denominator is positive there because the imaginary part is
nonzero. At every other noncontact x the same difference is
nonnegative, and its Y integral equals the excess in (10).
The contact x have zero excess. Therefore
m>=delta*|I0|*kappa^2/M0>0. This establishes strict positivity with
the actual density at nonzero middle-cell points; it is neither
a replacement G model nor an assertion about hypothetical slopes.
The phase theta is used only on noncontact x. No differentiation
of it and no global phase-sign assumption enter (10)–(12).

### A finite, uniform error bound

Define the actual-data constant

\[
K=\max_{[0,\bar h]\times P}
       (|\partial_t q_t|+|\partial_t r_t|)<\infty.        \tag{13}
\]

All hypotheses for this maximum and for the fundamental theorem
of calculus hold by the smoothness and compact-annulus checks
following (7). In particular derivatives of complex densities,
not derivatives of their possibly nonsmooth moduli, are bounded.
For every (x,Y) and h in [0,bar h], the elementary Lipschitz
inequality for the complex modulus gives

\[
\big|(|q_h|-|r_h|)-(|q_0|-|r_0|)\big|
 \le|q_h-q_0|+|r_h-r_0|\le Kh.                           \tag{14}
\]

The area of P is 2(r-l). Integrating (14) and using (8) proves
(5). If h<=h*, then 2(r-l)Kh<=m*K/[2(1+K)]<=m/2,
which proves (6). No limit, zero exclusion or contour interchange
is used to infer a finite sign. K is a specified compact supremum,
not an evaluated constant for a supplied graph. This distinction
is why the untested nominal width remains unresolved.

### Endpoint determinant and precise scope of the stop

The field (4) is smooth, real and periodic after extension and
agrees with u near every component of the strip boundary. For
any fixed h its exact endpoint determinant is j_h on P and
the original J outside the support. A sufficient optional check is

\[
\mu=\min_P|j_0|>0,\qquad
K_J=\max_{[0,\bar h]\times P}|\partial_t j_t|<\infty.     \tag{15}
\]

The positive inequality in (15) is an additional condition;
original J!=0 does not establish it. Indeed at t=0, writing
A=[[p,tau],[n,k]], direct expansion gives

\[
j_0=1-pk+\tau n+\rho(p\phi+n\eta')
                         -i(p+k-\rho\phi).              \tag{16}
\]

For example the two real equations j0=0 amount to
p+k=rho*phi and 1+p^2+n(tau+rho*eta')=0. This is a diagnostic
identity, not a claim of a realized singular stationary graph.
It shows why this proof cannot infer a determinant bound merely
from a bound for the unperturbed determinant. If (15) is verified,
the fundamental theorem of calculus yields

\[
0<h\le\min\left\{\bar h,\frac{\mu}{2(1+K_J)}\right\}
\quad\Longrightarrow\quad |j_h|\ge\mu/2>0.              \tag{17}
\]

Together with original J!=0 off the support, this makes that
endpoint admissible. If mu=0, (17) is inconclusive; j_h itself
could still be nonzero. No homotopy through nonzero Jacobians
is required or asserted. The mass lower bound (6) holds regardless
of these endpoint tests and so applies in particular to every
admissible member in its stated width range.

The decisive new scoped information is a strictly positive
order-h middle-cell cost with a rigorous finite O(h^2) error,
without L891's special slopes or disjoint supports. It stops
shrinking this connected bridge as a way to obtain descent.
It does not decide finite widths outside the certified range,
other bridge profiles or arbitrary replacements. There is no
numerical certificate, realized conditional graph or RH conclusion.

### Independent conceptual audit, 7 November 2026

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-07-paired-fiber-finite-replacement-test.md`
already covers checking an applicable full-mass obstruction with
the full endpoint determinant. This audit accepts (5)–(6) and the
conditional endpoint test (17) without changing the hypotheses,
construction or constants. It verifies a submitted conditional input;
it does not claim a new theorem beyond the inspected sources.

**Support, orientation and scaling.** The x cutoff is identically one
near both fibers and the middle cell and vanishes near l,r. Its two
transition denominators are respectively (alpha-l)/2 and (r-beta)/2,
both positive. The flat extension of eta is smooth at both endpoints.
Since h<=bar h is less than each vertical boundary distance, the
extended field is smooth and vanishes near the whole strip boundary.
Direct differentiation at y=y0+hY gives

\[
Dv_h=\begin{pmatrix}
h\rho'\eta&\rho\eta'\\
-h\rho'Y\eta&-\rho(\eta+Y\eta')
\end{pmatrix}=hD_1+D_0.
\]

L847's wedge convention therefore gives exactly q_h, with no
transposition or sign change. The positive substitution dy=h dY
gives the normalized identity (8). Every region where the graph
or its derivative changes lies in this rectangle. Integrating over
the whole P includes the x transitions and the entire Y profile;
no collar or middle-cell contribution is replaced by a boundary flux.

**Average and strictness.** At t=0, Z_t equals the original graph
point, although its derivative factor is H-i b e2^T. Original J!=0
permits factoring H and gives (9). The two exact identities
integral eta'=0 and integral (Y eta)'=0 imply (10), including x
where F=0. Thus the Y-integrated excess is nonnegative for each x,
including either x collar. Constancy of z1 on the complete contact fiber gives
u1,y=0 and the triangular inverse (11), independently of n and p.
Continuity then gives a noncontact middle-cell x0 with
Re(H^(-1))22>0. At Y=0 the imaginary part of q0/Q0 is this positive
number. Hence Im(conjugate(theta)q0)=|Q0| Re(H^(-1))22>0
at this point, with factor |Q0|>0.

The rectangle K0 in the proof is therefore available with positive
area 2 delta |I0|, a strictly positive uniform kappa and finite
M0>=kappa. On it the denominator in (12) is strictly positive and
at most 2M0. Off it, |q0|-Re(conjugate(theta)q0)>=0 wherever theta
is defined. Its Y integral is exactly the excess in (10), since the
integral of q0 is 2Q0. At the two contact x, both original and
auxiliary densities vanish. This proves the stated full lower bound
m>=delta |I0| kappa^2/M0>0. A single point of phase mismatch alone
would not suffice; the proof correctly pays for a positive-area set.
No stationarity conclusion or general common-phase premise is
needed for this averaging check. The submitted stationarity and
simple-fiber hypotheses are retained, not broadened by this audit.

**Finite bound through all zeros.** The family Z_t stays in compact
annuli with strictly positive inner radii. For an explicit check of
regularity, set B_t=A_t+D0+tD1 and H_t=I-iB_t. Differentiation of
the displayed smooth auxiliary functions gives

\[
\dot Z_{t,j}=Z_{t,j}\bigl(Yu_{j,y}(x,y_0+tY)+a_j+iY\delta_{j2}\bigr),
\qquad \dot B_t=Y\partial_yDu(x,y_0+tY)+D_1,
\]
\[
\dot j_t=-i\operatorname{tr}(\operatorname{adj}(H_t)\dot B_t),
\qquad
\dot q_t=\sum_j F_{z_j}(Z_t)\dot Z_{t,j}j_t+F(Z_t)\dot j_t,
\qquad \dot r_t=Y\partial_yQ(x,y_0+tY).
\]

The adjugate identity is polynomial and remains valid when j_t=0.
F and its first derivatives are smooth on those annuli, including
all numerator zeros. These expressions are consequently bounded
on the full compact parameter set, verifying (13) without dividing
by F, q_t or j_t. The modulus Lipschitz inequality, rather than
differentiation of |q_t|, yields (14). Multiplication by the area
2(r-l) and by h gives the precise error in (5). The proposed h_*
indeed satisfies 2(r-l)K h_*<=m K/[2(1+K)]<=m/2, even when K=0.
This establishes a finite sign, not merely a limiting asymptotic.

**Admissibility and accepted scope.** Expansion of
det(I-i[[p,tau+rho eta'],[n,k-rho phi]]) gives (16). Setting its
imaginary part to zero reduces its real part to
1+p^2+n(tau+rho eta'), as stated. Original invertibility alone
does not bound this new determinant away from zero: Dv_h has an
order-one second column as h tends to zero. If the additional
condition mu>0 is verified, the same compact derivative estimate
gives |j_h|>=mu-K_J h>=mu/2 under (17). Original J handles the
complement of the support. If mu=0, this sufficient test says
nothing about a particular positive-width endpoint.

The audit accepts increased mass for every 0<h<=h_*, whether or
not that endpoint is admissible, and hence for every admissible
member in that range. It leaves bar h undecided unless the strict
inequality 2(r-l)K bar h<m is verified. No actual conditional graph,
evaluated K or m, graph-independent width, general finite-bridge
obstruction, minimizer, sign criterion or RH conclusion follows.
The direct inputs remain L847 and L879; L887–L891 are comparisons,
not mathematical premises. No repair, numerical replay, new source
import or change to the main argument was needed.

## Mathlib

Full matching coverage for this actual-G connected-bridge result,
and supporting formal coverage for its determinant and compact
derivative estimates, have not been checked. No Mathlib theorem
is imported and no absence is asserted. The independent conceptual
audit above is informal verification of the stated conditional bounds,
not a formal verification.
