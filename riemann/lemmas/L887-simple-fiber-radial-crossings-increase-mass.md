# Lemma 887: fixed radial bumps across a simple G-zero fiber increase mass

## Hypotheses

Retain L847's actual entire G, positive R,C and full oriented density:

\[
 z_j(y)=R e^{u_j(y)+iy_j},\qquad
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \quad H=I-iDu,\quad J=\det H,\quad Q=F(z_1,z_2)J,
 \quad \mathcal B(u)=(2\pi)^{-2}\int_{T^2}|Q|\,dy.            \tag{1}
\]

Assume exactly L879's graph hypotheses: u is smooth, real and periodic;
J is nowhere zero; and B is stationary for smooth real radial fields
compactly supported in {Q!=0}. Its audited conclusion supplies
Q=lambda*s, where |lambda|=1 and s is smooth and real. No graph
existence, minimum, positivity or RH assumption is made.

Assume conditionally a point p0=(alpha,y0) where z1=zeta is a **simple**
zero of G, G(z2)!=0 and z1!=z2. L879 then supplies a local contact fiber
z1(alpha,y)=zeta. Choose a sufficiently small lifted angular rectangle

\[
 \Omega=(-\delta,\delta)\times I,\qquad x=y_1-\alpha,\quad
 I=(y_0-\ell,y_0+\ell),                                    \tag{2}
\]

with compact closure in that clean neighborhood. Its properties and
existence are justified below. Take a fixed real
chi in C_c^infinity(Omega) with chi(0,.) not identically zero, extend
v=(chi,0) by zero to T2, and set u_t=u+t*v. The bump is fixed as t
tends to zero. No assertion about parameter-dependent bumps is made.

For a concrete choice take
chi(x,y)=eta(2x/delta)*eta(2(y-y0)/ell), where
eta(r)=exp(-1/(1-r^2)) for |r|<1 and eta(r)=0 otherwise.
This standard smooth bump has compact support inside Omega and
strictly positive trace on an interval of the fiber.

## Conclusion

Write a(y)=partial_1 u1(alpha,y) and
h0(y)=partial_1 s(alpha,y), which is real and nowhere zero on I.
As t tends to zero through either sign,

\[
 \mathcal B(u_t)-\mathcal B(u)
   =c_\chi t^2\log(1/|t|)+O_{u,\Omega,\chi}(t^2),\qquad
 c_\chi=\frac1{(2\pi)^2}\int_I
       \frac{|h_0(y)|\chi(0,y)^2}{(1+a(y)^2)^2}\,dy>0.       \tag{3}
\]

The error means that there are finite K and t0>0, depending on the
fixed data, for which its absolute value is at most K*t^2 whenever
0<|t|<t0. In particular B(u_t)>B(u) when also
log(1/|t|)>K/c_chi. The full Jacobian and nonlinear density, the
cutoff transition and both sides of the contact are included.
J_t remains nowhere zero for sufficiently small |t|; the density
outside the bump support remains unchanged.

With eta_y=z2(alpha,y), the coefficient retains the actual Jacobian:

\[
 |h_0(y)|=
 \frac{C|G'(\zeta)||G(\eta_y)||\zeta-\eta_y|^2}
      {|\zeta||\eta_y|^2}\,|J(\alpha,y)|\sqrt{1+a(y)^2}.     \tag{4}
\]

This stops every **fixed** field of the stated single-coordinate,
nonzero-trace class as an infinitesimal lowering direction at such a
simple contact. It does not prove a local minimum, treat zero-trace
bumps, other multiplicities, intersections, varying bump families or
arbitrary coupled fields, or exclude/construct a stationary graph.
Minima, compactness, L868's sharp bound, higher signs and Xi transfer
remain open. The independent conceptual audit of 7 November 2026
below accepts this scoped expansion. It is a local application of the
known complex-modulus logarithmic mechanism, not a claim of a new
general singular-integral theorem or progress beyond the sources checked.

## Proof

### Assessed scope and sources

The invocation-start EXPLORE assessment is
drafts/literature/2026-11-07-cross-fiber-mass-variation.md, with the
exact crossing-bump target in its COVERED_TARGET. This is that bounded
mathematical application. L847 supplies (1); L879 supplies the phase
line, local fiber assertion and full variation formula used below.
L882's conditional simple-fiber branch is one possible setting, but
neither it nor L886 is an input. The chord and unsigned product-kernel
stops are comparisons.

The known pullback differentiation underlying L879 is Guillemin and
Sternberg, *Semi-classical analysis*, 13 January 2010,
[Sections 13.13–13.14.1, equations (13.7)–(13.9), pp449–455](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
L879 already checked its constrained radial specialization, indices
and orientation. Its isolated-zero input is Lebl, *Guide to Cultivating
Complex Analysis*, v1.10, 5 November 2026,
[Theorem 2.4.7 and finite-order factorization, pp49–50](https://www.jirka.org/ca/ca.pdf#page=49),
applicable because G is entire and G(0)>0. These citations are reused
from the inspected assessments; no new source claim is introduced.

Wachsmuth and Wachsmuth, *Second-order conditions for non-uniformly
convex integrands: quadratic growth in L1*, JNSAO **3** (2022), 8733,
[Section 3.2, Lemma 3.5, pp10–14](https://jnsao.episciences.org/9596/pdf#page=10),
is for a real kink and does not apply to the transverse complex
variation below. The inspected [DLMF 19.12.2–19.12.3](https://dlmf.nist.gov/19.12#E2)
gives a convergent logarithmic elliptic-integral model without this
variable coefficient or nonlinear pullback. Neither theorem is used
as an unproved transfer to (3). The elementary cutoff estimate below
is needed precisely for those application differences; it does not
reprove either cited general result. Taylor's theorem, compact uniform
bounds, dominated convergence and integration by parts are applied
with their hypotheses checked explicitly.

### Clean rectangle and the full first variation

Isolate zeta in an open disc not containing zero or another G zero.
At p0 the second G factor and z1-z2 are nonzero. Continuity gives a
neighborhood where both stay bounded away from zero and z1 stays in
a smaller compact subdisc of the isolating disc. In a short angular
lift, G(z1)=0 there implies x=0. L879's odd-contact assertion (here
the order is one) gives z1(alpha,y)=zeta on a whole smaller interval.
A smaller rectangle with compact closure therefore has exactly that
G-zero fiber, with no second-factor contact or diagonal intersection.

Put eta_y=z2(alpha,y). Since z1 is constant along the fiber,
partial_2 u1(alpha,y)=0. The real a=partial_1 u1 satisfies
partial_1 z1=zeta*(a+i), which is nonzero. Differentiating the full
Q at the fiber gives

\[
 \partial_1 Q(\alpha,y)=
 -C\frac{G'(\zeta)G(\eta_y)(\zeta-\eta_y)^2}{\zeta^2\eta_y^2}
       J(\alpha,y)\zeta(a+i)\ne0.                          \tag{5}
\]

Every other differentiated term contains G(zeta)=0; none is omitted
at a nonzero point. Thus h0=conjugate(lambda)*partial_1 Q is real
and nonzero. Since s(0,y)=0, the exact identity

\[
 s(x,y)=x h(x,y),\qquad
 h(x,y)=\int_0^1\partial_1s(rx,y)\,dr                       \tag{6}
\]

gives smooth real h. Shrink the closed rectangle once more so that
|h|>=m>0 there. Its sign is constant since the rectangle is connected.
Equation (5) also proves (4).

Write a_jk=partial_k u_j on the whole rectangle. Only the first row
of Du changes, so the exact Jacobian and density are

\[
 J_t=J+t\dot J,\qquad
 \dot J=-a_{22}\chi_x+a_{21}\chi_y-i\chi_x,                 \tag{7}
\]
\[
 Q_t=-C\frac{G(z_1e^{t\chi})G(z_2)(z_1e^{t\chi}-z_2)^2}
                   {z_1^2e^{2t\chi}z_2^2}\,(J+t\dot J).   \tag{8}
\]

This retains the full coefficient variation on the cutoff as well
as in its interior. Compactness, smoothness and nonzero z_j give a
uniform second-t-derivative bound in (8). Set
q_t=conjugate(lambda)*Q_t and p=partial_t q_t at t=0. Then

\[
 q_t=s+t p+t^2r_t,\qquad
 \sup_{\overline\Omega,\,|t|<t_0}|r_t|<\infty.              \tag{9}
\]

In particular p is smooth in the spatial variables. Since the torus
has min|J|>0, (7) preserves J_t!=0 for sufficiently small |t|.
The isolating-disc and nonvanishing conditions persist by uniform
continuity. Outside supp(chi), the field and its derivatives vanish,
so Q_t=Q exactly. In the rectangle, a perturbed contact with zeta
must still have x=0. There z1,t=zeta*exp(t*chi(0,y)); for t!=0 it
equals zeta precisely where chi(0,y)=0. The bump displaces the graph
radially off the contact where its trace is nonzero; it does not
translate the zero's argument or discard contacts in the transition.

At x=0, differentiating (8) and comparing with (5) gives

\[
 p(0,y)=\frac{h_0(y)\chi(0,y)}{a(y)+i},\qquad
 \operatorname{Im}p(0,y)
      =-\frac{h_0(y)\chi(0,y)}{1+a(y)^2}.                  \tag{10}
\]

Thus this variation is transverse in the complex plane, not merely
a scalar sign crossing. The dot-J term disappears in (10) solely
because F=0 on the fiber; (7)–(9) retain it everywhere else.

### The integrated linear term vanishes across the fiber

L879's full variation identity, valid also at F=0, gives

\[
 p=-i\operatorname{div}(sH^{-1}v),\qquad
 \operatorname{Re}p=\operatorname{div}(s w),\qquad
 w=\operatorname{Im}(H^{-1}v).                             \tag{11}
\]

The field w is smooth and compactly supported in Omega since H is
smooth and invertible. On either open half-rectangle sign(s) is
constant by (6). Integrate the divergence on each closed half.
The outer flux vanishes by compact support; the common-boundary
flux vanishes because s=0 there and w is bounded. Hence

\[
 \int_\Omega\operatorname{sgn}(s)\operatorname{Re}p\,dx\,dy=0.
                                                               \tag{12}
\]

Assign any value to sign(s) on x=0, a set of two-dimensional measure
zero. This integral is also the first mass derivative: (9) and the
modulus Lipschitz inequality uniformly bound the difference quotients,
whose limit at s!=0 is sign(s)*Re p. Dominated convergence applies on
this finite rectangle; the rest of the torus is unchanged. Thus no
stationarity for a forbidden zero-crossing support was assumed.
Equation (11) and the vanishing boundary flux prove the required
first-derivative statement for the present support.

### Variable-coefficient modulus estimate and integrated remainder

The modulus is 1-Lipschitz, so (9) yields

\[
 \int_\Omega |q_t|=\int_\Omega |s+t p|+O(t^2).              \tag{13}
\]

This controls the complete nonlinear acceleration; it does not drop
an unestimated second-order term. Put
D_t=|s+t*p|-|s|-t*sign(s)*Re p.
Let P=sup|p| on the closed rectangle, and fix
L>=max(1,2P/m). For 0<|t|<delta/L split the rectangle into
|x|<=L|t| and its complement. On the inner strip |D_t|<=2P|t|
by Lipschitz continuity. Its area is 2L|t|*|I|, so its complete
contribution is O(t^2), including where the bump trace vanishes.

On the complement |t*p|<=|s|/2. Taylor's theorem for the Euclidean
norm on the closed balls of radius 1/2 about the two real unit
points has uniformly bounded third derivatives, and gives

\[
 D_t=\frac{t^2(\operatorname{Im}p)^2}{2|s|}+E_t,\qquad
 |E_t|\le C_0\frac{|t|^3P^3}{m^2x^2}.                      \tag{14}
\]

Both balls avoid zero. The integral of x^(-2) over
L|t|<|x|<delta is at most 2/(L|t|), so the integrated error in
(14) is O(t^2).

The function k(x,y)=(Im p(x,y))^2/|h(x,y)| is smooth on the
closed rectangle and has a bounded x derivative. Therefore
|k(x,y)-k(0,y)|<=K1*|x| uniformly. Using |s|=|x|*|h| in
(14), replacement by k(0,y) costs O(t^2). Both sides of the
fiber now give

\[
 \begin{split}
 \int_\Omega D_t
 &=\frac{t^2}{2}\int_I k(0,y)\,dy
       \int_{L|t|<|x|<\delta}\frac{dx}{|x|}+O(t^2)\\
 &=t^2\log(1/|t|)\int_I k(0,y)\,dy+O(t^2).                 \tag{15}
 \end{split}
\]

The finite term log(delta/L) belongs to the O(t^2) remainder.
No t-dependent direction, noncompact support or uncontrolled
singular limiting integral has been used. Equations (10), (12),
(13) and (15), with normalization (2pi)^(-2), prove (3).
Every factor in |h0| is nonzero, and a smooth nonzero trace is
nonzero on an interval, proving c_chi>0. The cutoffs and error
bounds use |t| and work for both signs.

The proof uses no property of chi beyond the stated fixed smooth
compact support and nonzero trace, so it proves the sign throughout
precisely that class. Its constants need not be uniform in chi.
For zero trace c_chi=0; this comparison cannot decide the remaining
O(t^2) sign. No assertion for that case is inferred or attempted.

### Independent conceptual audit, 7 November 2026

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-07-l887-cross-fiber-mass-audit.md`
covers this audit. Equations (3)–(15) are accepted under the unchanged
hypotheses, without a mathematical repair or an additional direction
class. This verifies the submitted conditional obstruction, not a new
theorem, a graph construction or a minimum assertion. L847 and L879
remain the only direct mathematical inputs.

**Geometry and trace.** The isolated-zero disc can be chosen away
from zero because G(0)>0. Shrinking the angular lift to length less
than 2pi ensures that z1=zeta requires exactly x=0. The other G
factor and the diagonal factor have positive modulus minima on a
sufficiently small compact rectangle. L879's audited intrinsic
odd-contact argument applies even at an added arrangement vertex:
it uses these actual nonvanishing factors, not absence of an
irrelevant auxiliary angle. It supplies the entire central fiber.
Thus partial_2 u1=0 there. Simplicity, zeta!=0 and the imaginary
part 1 of a+i make (5) nonzero. No lower bound on G away from all
its ambient zeros is needed. Since s is smooth real, (6) is exact;
continuity then gives one fixed m>0 on the smaller closed rectangle.

The full matrix determinant is
J=1-a11*a22+a12*a21-i(a11+a22). Differentiating its first row gives
exactly (7), including the a21*chi_y term. At the fiber, every
derivative of Q except the one hitting G(z1) contains G(zeta)=0.
The spatial derivative of that factor is G'(zeta)*zeta*(a+i);
its parameter derivative is G'(zeta)*zeta*chi. Their ratio proves
(10). Taking moduli of (5) leaves one power |zeta| in the denominator
and the factor sqrt(1+a^2), as in (4). Squaring the imaginary part
in (10) and dividing by |h0| gives
|h0|*chi(0,y)^2/(1+a^2)^2, with no missing Jacobian or factor of two.
The sign choice of the global phase lambda does not change it.

**Interface and nonlinear path.** L879(7) is a smooth density
identity, obtained before dividing by Q. Multiplication by the
constant conjugate(lambda) therefore proves (11) also where Q=0.
H inverse is smooth and bounded on the torus because J never
vanishes. The field w is compactly supported in the rectangle.
On each closed half-rectangle the divergence theorem applies to
the smooth field s*w; the outer boundary contributes zero by
support and the central edge contributes zero because s=0.
Multiplying each half by its constant sign(s) proves (12), with
neither a hidden interface distribution nor assumed stationarity
of the deformed graph. The fiber has area measure zero. The bound
|(|q_t|-|s|)/t| <= |p|+|t|*sup|r_t| supplies the integrable dominator
for the two-sided first derivative.

Fix a small closed parameter interval [-tau,tau]. The arguments
z1*exp(t*chi) in (8) stay in a compact subset of C*, all other
factors and their required derivatives are bounded, and (8) has no
division by G. Its second t derivative has a finite uniform bound.
Taylor's integral remainder gives one R0 with |r_t|<=R0 for both
signs of t. This estimate holds throughout the cutoff, including
trace-zero points. If j_* is min|J| on the torus, the condition
|t|*sup|dot J|<j_*/2 preserves J_t!=0 (with no restriction needed
from this inequality when dot J is identically zero). The compact
support gives a smooth extension and unchanged exterior density.
Uniform continuity also preserves the isolating disc and the other
nonvanishing factors. None of these checks requires Q_t to be nonzero
everywhere or to retain a common phase.

**Complete integrated error bound.** Let b=|I|, P=sup|p|,
L=max(1,2P/m), and choose 0<|t|<min(tau,delta/L,1).
Let K1 bound |partial_x k| for k=(Im p)^2/|h|. All these constants
are fixed by u, the rectangle and chi. The inner strip contributes
at most 4*L*P*b*t^2 to the integral of |D_t|. On its complement
|t*p/s|<=1/2; the norm's third derivatives are bounded on the two
closed radius-1/2 balls about +1 and -1. Rescaling gives (14),
whose integrated absolute error is at most
2*C0*P^3*b*t^2/(m^2*L). The coefficient-freezing error is at most
K1*delta*b*t^2. These estimates do not divide by p or its trace,
so they remain valid at every cutoff transition and trace zero.

The exact outer integral is
integral_(L|t|<|x|<delta) dx/|x| = 2*log(delta/(L|t|)).
It cancels the 1/2 in (14), giving exactly (15). Its constant
log(delta/L) contributes at most
|log(delta/L)|*integral_I k(0,y)dy*t^2. Finally (13) has absolute
error at most 2*delta*b*R0*t^2. Consequently the sum

\[
 4LPb+\frac{2C_0P^3b}{m^2L}+K_1\delta b
 +|\log(\delta/L)|\int_I k(0,y)\,dy+2\delta bR_0
\]

is a finite unnormalized remainder bound for the asserted expansion.
Multiplication by (2pi)^(-2), followed by (12) and (10), proves the
claimed normalized bound and coefficient. A nonzero smooth trace is
nonzero on an interval; |h0|>0 there, so c_chi>0. For each fixed bump
the logarithm eventually exceeds the finite remainder bound divided
by c_chi, proving strict increase for both signs of sufficiently small
t. There is no uniform onset over bumps, and nothing here signs the
O(t^2) term when the trace vanishes.

The audit accepts the stated stop only. It neither repeats the bump
test as a new mechanism nor strengthens it to arbitrary coupled
fields, finite deformations, other multiplicities or contact
intersections. Graph/minimizer existence and compactness, L868's
sharp bound, higher signs and actual-Xi transfer remain unresolved.
No numerical computation or mathematical script was needed for
these analytic checks. The existing source comparisons remain
comparisons; neither the real-kink theorem nor the DLMF model was
used to certify the variable-coefficient expansion.

## Mathlib

Full matching coverage for (3), and supporting coverage for the
constrained pullback and singular integral estimate, were not checked.
No Mathlib theorem is imported and no absence claim is made. The
independent conceptual audit above is informal verification of the
written argument; it does not change this Mathlib coverage status.

