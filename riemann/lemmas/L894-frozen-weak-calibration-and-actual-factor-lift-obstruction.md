# Lemma 894: a frozen weak calibration and failure of its actual-factor lift

## Hypotheses

Use logarithmic coordinates w_j=x_j+i y_j and the forms

\[
\eta=dw_1\wedge dw_2,\qquad \beta=dy_1\wedge dy_2.
\]

For the **frozen diagnostic only**, let kappa>0 and F_0=kappa*w_1
on C^2, with omega_0=-F_0 eta. The model graph is x_1=x_2=0,
oriented by dy_1 wedge dy_2. This is not L847's actual density,
an asserted tangent of the nominated graph, or a realized stationary
actual-G graph. In particular no change of coordinates making a
general Du vanish is assumed to preserve the allowed graph planes.

For the separate actual-factor test, retain L847's entire G, G(0)>0,
positive R,C and full density

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2}.
 \tag{1}
\]

Fix a point (zeta,eta_0) with zeta a simple G zero and with
G(eta_0)!=0, zeta!=eta_0, zeta*eta_0!=0. On a sufficiently small
connected bidisc use z_1=zeta*exp(w_1), z_2=eta_0*exp(w_2).
These are translations of L893's logarithmic coordinates, so the
coframe and weak closure equations are unchanged. A real candidate
form has the necessary L893 representation

\[
 a=\operatorname{Re}(g\eta)-h\beta,\qquad
 g=q-ir,\quad h\geq0,\quad |g|\leq|F|,
 \tag{2}
\]

with locally Lipschitz real q,r,h. Distributional closure requires

\[
 r_{x_j}=q_{y_j},\qquad (q+h)_{x_j}=-r_{y_j}
 \quad(j=1,2).
 \tag{3}
\]

## Conclusion

The frozen diagnostic admits the following explicit locally Lipschitz
closed form of type (2), with F replaced by F_0. Write x=x_1,y=y_1:

\[
\begin{split}
 q_0&=-\kappa\max(|x|,|y|),\\
 r_0&=-\kappa\operatorname{sgn}(xy)\min(|x|,|y|),\\
 h_0&=2\kappa(|x|-|y|)_+,
 \qquad g_0=q_0-ir_0.
\end{split}\tag{4}
\]

Take sgn(0)=0. It satisfies |g_0|=|F_0| everywhere, the two closure
directions (3), domination on every ordered graph plane including
J=0 and F_0=0, and saturation of the entire flat model graph. Thus
the forced corner and the frozen equations with h>=0 are compatible
in this explicitly restricted model.

For the actual density, F=w_1 H on the bidisc, where H is holomorphic
and nonzero after shrinking. Take the unit version kappa=1 of (4).
For **every constant real theta**, the proposed lift

\[
                 g=e^{i\theta}H g_0                       \tag{5}
\]

has the exact modulus |g|=|F| and is locally Lipschitz. Nevertheless,
no locally Lipschitz h, of either sign, makes its form weakly closed
on any neighborhood of the contact point. The first equation of (3)
already fails. Graph saturation is not asserted for this lift, and
is not needed to exclude it.

These are a feasible diagnostic and an obstruction to the specific
multiplication construction (5). They provide neither an actual-G
calibration nor a nonexistence theorem for the full nominated class.
No conclusion about finite descent, the paired strip, graph existence,
mixed positivity or RH follows. This result has not had an independent
audit.

## Proof

### Scope and reused results

The invocation-start EXPLORE coverage is
`drafts/literature/2026-11-07-weak-local-paired-strip-calibration.md`.
This is its one-fiber compatibility and nonsmooth-extension test on
the unchanged target. L893 supplies the necessary local weak system;
its pointwise algebra is also verified directly below for the model.
No weak Stokes theorem or new mass comparison is needed here. The
ready assessment's Kangasniemi–Prywes comparison is not an existence
theorem and is not used as one.

The finite piecewise-affine calculation and the actual holomorphic
factor check are the parts not supplied by a general calibration
comparison. The standard named identity theorem for holomorphic
functions is used below with its connected-domain hypothesis explicit.
No general theorem is being reproved. The prior search did not identify
this exact construction/obstruction; it does not certify originality.
The L887 fixed-bump, L892 thin-bridge and attempt65/69 stops are
contrasts, not premises. No new stop on those broader routes is inferred.

### All regions, interfaces and weak derivatives of the frozen form

On the four open cones the coefficients in (4) are

\[
\begin{array}{c|ccc}
\text{region}&q_0&r_0&h_0\\ \hline
y>|x|&-\kappa y&-\kappa x&0\\
y<-|x|&\kappa y&\kappa x&0\\
x>|y|&-\kappa x&-\kappa y&2\kappa(x-|y|)\\
x<-|y|&\kappa x&\kappa y&2\kappa(-x-|y|)
\end{array}                                                    \tag{6}
\]

In the last two cones split once more at y=0 for h_0. At x=y and
x=-y the adjacent q_0,r_0 values agree and h_0=0 on both sides.
Across y=0 in the right/left cones q_0,r_0 are unchanged affine
functions and h_0 is continuous. All coefficients vanish at the
origin. They are continuous on this finite conical subdivision and
affine with bounded gradients on each piece. Restricting to any
line segment, summing the finitely many piecewise gradient bounds
(or taking a limit for a segment on an interface) proves a global
Lipschitz bound. Thus their distributional first derivatives are the
piecewise classical derivatives, with no interface jump measures.

In the upper cone,
r_0,x=-kappa=q_0,y and (q_0+h_0),x=0=-r_0,y.
In the lower cone these are kappa=kappa and 0=0.
In the right cone r_0,x=q_0,y=0 and
(q_0+h_0),x=kappa=-r_0,y.
In the left cone r_0,x=q_0,y=0 and
(q_0+h_0),x=-kappa=-r_0,y.
The remaining interfaces have ambient measure zero. These identities
prove (3) for j=1 as distributions. Every coefficient is independent
of x_2,y_2, so both j=2 equations hold as well. In particular this
does not check only one of the two required closure directions.

In each cone q_0^2+r_0^2=kappa^2(x^2+y^2); continuity gives the
same identity on every interface. Also h_0>=0. For an arbitrary
real matrix A, write U=det A-1, V=tr A, so that
eta(E_1,E_2)=U+iV and |J|=sqrt(U^2+V^2) in the logarithmic frame.
The evaluation of the form is

\[
 q_0 U+r_0 V-h_0
 \leq\sqrt{q_0^2+r_0^2}\sqrt{U^2+V^2}
 =|F_0||J|=|\omega_0(E_1,E_2)|.                         \tag{7}
\]

This uses Cauchy–Schwarz without dividing by either factor. If J=0
the left side is -h_0<=0. If F_0=0 then x=y=0 and all coefficients
are zero. Thus the degeneracies are included.

On x_1=x_2=0, q_0=-kappa*|y_1|, r_0=h_0=0 and J=1. Hence the
pullback coefficient is -q_0=kappa*|y_1|=|F_0 J|. This proves
whole-graph saturation for the model. It proves no assertion about
the actual graph's slopes or density. In particular no unproved
blow-up compactness or averaging argument is used to transfer it.

### The actual factor and the unavoidable failure of the lift

Simple vanishing of G at zeta gives the holomorphic factorization
F=w_1 H, with

\[
 H(0,w_2)=-C\frac{G'(\zeta)G(z_2)(\zeta-z_2)^2}
                        {\zeta z_2^2}.
 \tag{8}
\]

The right side is nonzero at w_2=0. Thus H is nonzero on a smaller
bidisc. It is nonconstant as a function of w_2 already on w_1=0:
if G(z)(zeta-z)^2/z^2 were constant K on a nonempty open disc of
nonzero z, then the entire function

\[
                    G(z)(\zeta-z)^2-Kz^2
\]

would vanish on that disc. The identity theorem on the connected
plane would make it identically zero. At z=0 its value is
G(0)*zeta^2!=0, a contradiction.

Equations (3) imply, with partial_bar_j=(partial_xj+i partial_yj)/2,

\[
 \partial_{\bar w_j}g
 =\tfrac12(q_{x_j}+r_{y_j})
   +\tfrac i2(q_{y_j}-r_{x_j})
 =-\tfrac12 h_{x_j}.                                    \tag{9}
\]

In particular this derivative must be real as a distribution. On
the open right cone x_1>|y_1| the unit model has
g_0=-x_1+i y_1=-overline(w_1). The lift (5) is smooth there, so
holomorphy of H gives

\[
             \partial_{\bar w_1}g=-e^{i\theta}H.
 \tag{10}
\]

Any neighborhood of the origin contains a nonempty open part of
this cone times a w_2 disc. If (9) held weakly, its imaginary part
and smoothness of H would force Im(e^{i theta}H)=0 everywhere on
that open set. A holomorphic real-valued function is locally
constant by the Cauchy–Riemann equations in both variables.
Choose a product of discs inside this open set; H is a constant
there. For each w_2 in its second disc, the one-variable identity
theorem in w_1 extends that constant to the full first disc of
the centered bidisc, in particular to w_1=0. Applying the same
identity theorem in w_2 would make H(0,w_2) constant. This
contradicts (8) and the preceding paragraph.

The contradiction is to r_x1=q_y1 alone. Altering h cannot repair
it, even without nonnegativity. Formula (5) does attain the full
actual modulus because |g_0|=|w_1|, but the modulus condition is
only one requirement. More general g, dependence on both coordinate
directions, a change to the cone structure, or a correction that
also changes g are not excluded. Nor does failure of this ansatz
prove a mass-lowering competitor or failure of dual attainment.

## Mathlib

Coverage of the full piecewise weak-calibration construction and its
actual-factor obstruction was not checked. No matching theorem or
absence claim is asserted. Lipschitz piecewise-affine functions,
Cauchy–Schwarz, distributional exterior differentiation and the
holomorphic identity theorem are supporting ingredients, not a
claim that this result or its actual-G specialization is formalized.
