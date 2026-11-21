# Lemma 849: the prescribed actual-G exchange data admit an exact positive collar

## Hypotheses

Use the actual entire G, the positive constants R,C, and the full
oriented form of L847 and L848:

\[
 G(z)=\frac18\xi\left(\frac12+\frac{\sqrt z}{2}\right),\qquad
 RG'(R)/G(R)=1,\qquad C=R^2/G(R)^2>0,
\]
\[
 \omega=C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
                       dz_1\wedge dz_2.                    \tag{1}
\]

Evenness defines G as an entire function without a square-root choice.
Prescribe exactly L848's periodic data, with m in R/2pi Z:

\[
 \begin{split}
 d(m)&=\sqrt{600^2-400^2\sin^2m},\quad
 r(m)=-400\cos m+d(m),\quad h(m)=\log(r(m)/R),\\
 z(m)&=r(m)e^{im},\quad f(m)=G(z(m))/z(m),\quad
 \phi(m)=\operatorname{Im}\operatorname{Log} f(m),\\
 b(m)&=\tan\bigl((2\phi(m)-\arctan h'(m))/3\bigr),
 \end{split}                                                \tag{2}
\]

where Log is the principal logarithm. The accepted sector and phase
estimates of L848(5),(12)–(13) give well-defined bounded smooth data,
f avoiding the nonpositive real axis, and the real function

\[
 K_0(m)=4C f(m)^2(1-i h'(m))(1-i b(m))^3
       >4C\,10^{-16}.                                      \tag{3}
\]

The sector input retains L848's inherited analytic and trusted-software
qualifications. This proof uses its exact actual-G conclusion, not a
polynomial substituted for G, a sampled phase or a numerical zero list.
No RH, simplicity, or nonvanishing of G away from the specified curve
is assumed.

## Conclusion

There exist a real C-infinity map u:T^2 -> R^2, periodic in both
angular variables, and one epsilon>0 such that

\[
 \begin{split}
 u_2(t,s)&=u_1(s,t),\\
 u_1(m,m)&=h(m),\qquad
 (\partial_1-\partial_2)u_1(m,m)=b(m).                       \tag{4}
 \end{split}
\]

For the radial graph z_j=R exp(u_j+i theta_j), theta=(t,s), write
Phi_u^*omega=q_u(t,s) dt wedge ds in the original orientation.
Let K_* = min_m K_0(m)>0. Throughout the uniform collar
dist_(R/2pi Z)(t,s)<2 epsilon, represented uniquely by
t=m+delta,s=m-delta with |delta|<epsilon, the full density is
exactly real and satisfies

\[
 q_u(m,m)=0,\qquad
 q_u(m+\delta,m-\delta)\geq\frac{K_*}{2}\delta^2>0
                   \quad(0<|\delta|<\epsilon).             \tag{5}
\]

The local graph is real analytic in (m,delta); its extension to the
torus is smooth. The width is existential, not an effective numerical
bound. L847 makes this an oriented embedded torus homologous to the
radius-R torus. No reality or sign is claimed outside the collar.
The collision zero is retained. All actual-G zeros remain in the full
formula; none is removed by modifying the form.

The separate conceptual audit of 6 November 2026 below accepts this
local construction with its inherited analytic and trusted-software
qualifications. It is not an all-angle contour, a new mixed-minor sign
or an RH candidate. Global sign, extension with global reality, other
orders/shifts and transfer to all-degree mixed positivity remain open.
The original POTENTIALLY_NEW classification records only the limited
construction-stage literature comparison, not certified originality.

## Proof

### Source scope and regularity of the precise data

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-exchange-diagonal-exact-collar.md`.
It covers this exact collar target, including an analytic
desingularization and an implicit normal formulation. The standard
existence input is Marc Chaperon, *On the Cauchy-Kowalevski theorem*,
9 January 2007, Section 1, Corollary 1, p2,
[analytic implicit function theorem](https://webusers.imj-prg.fr/~marc.chaperon/Chaperon_Cauchy_Kowalevski.pdf#page=2):
an analytic equation with an invertible derivative in the unknown
has a unique local analytic solution near its base solution. The
assessment already inspected this corollary. Below the unknown is
one real scalar and the derivative is explicitly strictly negative.
The corollary is imported, not reproved. No Cauchy PDE, Cartan–Kähler
or singular-PDE theorem is used; their extra hypotheses are unnecessary
for this particular gauge and primitive. The reduction and global
compatibility argument are the application that the sources did not
provide.

The functions in (2) are in fact real analytic. The radicand of d is
at least 200000, r>=200 and R>0, so positive square root and logarithm
are analytic at every value used. Composition with entire G preserves
real analyticity. The slit-plane logarithm is holomorphic at every
f(m), by L848's sector exclusion, so its imaginary part is real
analytic in m. Finally the strict bound
|2 phi-arctan h'|<3pi/2 from L848 keeps the tangent in (2) away from
its poles. These functions are 2pi-periodic with no branch jump.
In particular K_0 is continuous and (3), together with compactness,
gives K_*>4C 10^(-16).

### Mean-radius gauge, full primitive and orientation

Work first on the cylinder m mod 2pi, |delta|<epsilon_0, with
epsilon_0<pi/2. Seek a real function V(m,delta) and set

\[
 u_1=h(m)+V(m,\delta),\quad u_2=h(m)-V(m,\delta),\quad
 v=V+i\delta,\quad z_1=z(m)e^v,\quad z_2=z(m)e^{-v}.        \tag{6}
\]

This fixes only the mean logarithmic radius; the required normal
derivative will be supplied by V. Locally write
w=log R+h(m)+im, so exp(w)=z(m), and put alpha(m)=h'(m)+i.
Although w itself changes by 2pi i on a full turn, dw=alpha dm and
every function of exp(w) used below is globally periodic.

Define, for complex v,

\[
 A(m,v)=z(m)^{-2}G(z(m)e^v)G(z(m)e^{-v})\sinh^2 v,\qquad
 J(m,v)=\int_0^v A(m,\zeta)\,d\zeta.                       \tag{7}
\]

For fixed m, A is entire and even in v. The integral is its entire
primitive normalized by J(m,0)=0. Equivalently integrate its entire
Taylor series term by term; convergence is uniform on compact v disks,
also locally uniformly in m. Thus J is odd in v and is jointly real
analytic in m and the real and imaginary parts of v. Its expansion is

\[
 A(m,v)=f(m)^2v^2+O(v^4),\qquad
 J(m,v)=f(m)^2v^3/3+O(v^5).                                 \tag{8}
\]

All statements here concern exact holomorphic functions. The removable
quotient

\[
 H(m,v)=\begin{cases}3J(m,v)/v^3,&v\ne0,\\f(m)^2,&v=0
             \end{cases}                                  \tag{9}
\]

is even and analytic. This divides a primitive's known Taylor factor,
not the original form or its pullback at a deleted point.

For completeness the full form, including its sign, becomes

\[
 dz_1\wedge dz_2=-2z_1z_2\,dw\wedge dv,\qquad
 (z_1-z_2)^2=4z(m)^2\sinh^2v,
\]
\[
 \omega=-8C A(m,v)\,dw\wedge dv.
\]

On (6), dw wedge dv = alpha(V_delta+i) dm wedge ddelta;
the term V_m is killed by the wedge with dm. Also
dt wedge ds=-2 dm wedge ddelta. Consequently the scalar density
in the required original orientation is exactly

\[
 q(m+\delta,m-\delta)
 =4C\alpha(m)A(m,v)(V_\delta+i)
 =4C\alpha(m)\partial_\delta J(m,v).                       \tag{10}
\]

Thus making alpha J real as a function of real delta makes q exactly
real. This is a sufficient condition, without an asserted equivalence
for arbitrary gauges. The equation remains valid at delta=0.

### A nonsingular scalar equation through the cubic zero

Set V=delta beta(m,delta), with beta real. Let

\[
 D(m)=\alpha(m)f(m)^2(b(m)+i)^3=K_0(m)/(4C)>0.              \tag{11}
\]

Indeed h'+i=i(1-i h') and b+i=i(1-i b); the product of the four
factors i is +1. This checks the sign against (3).
For real beta define the real analytic scalar function

\[
 E(m,\delta,\beta)=\operatorname{Im}\left[
 \alpha(m)(\beta+i)^3 H(m,\delta(\beta+i))\right].          \tag{12}
\]

Since H is even, E is even in delta. At the prescribed data,

\[
 E(m,0,b(m))=0,\qquad
 \partial_\beta E(m,0,b(m))
 =3\operatorname{Im}\frac{D(m)}{b(m)+i}
 =-\frac{3D(m)}{1+b(m)^2}<0.                               \tag{13}
\]

No derivative of H contributes at delta=0: its argument derivative
with respect to beta has the factor delta. The diagonal collision
therefore produces no degeneracy in this normalized scalar equation.
In particular this verifies, rather than assumes, the relevant
implicit-function hypothesis.

Here is the uniform compatibility argument. Put x=beta-b(m) and
E_tilde(m,delta,x)=E(m,delta,b(m)+x). Continuity of the derivative
and compactness of the m circle, applied to (13), give c>0, eta>0
and epsilon_1>0 such that

\[
 \partial_x\widetilde E\leq-c
 \quad\text{for every }m,\ |x|\leq\eta,\ |\delta|\leq\epsilon_1.
                                                               \tag{14}
\]

The joint continuity and E_tilde(m,0,0)=0 allow epsilon_1 to be
decreased until |E_tilde(m,delta,0)|<c eta/2 uniformly. The mean
value theorem then gives E_tilde(m,delta,-eta)>0 and
E_tilde(m,delta,eta)<0. The intermediate value theorem supplies a
root with |x|<eta, and (14) makes it unique there. At each such root
the imported analytic implicit function theorem makes the root
analytic in (m,delta) on a neighborhood. Uniqueness on the same
interval |x|<eta identifies these solutions on every overlap.
This constructs a single real analytic beta for all m and sufficiently
small |delta|, with beta(m,0)=b(m). The same uniqueness, together
with the periodicity of the equation and its evenness in delta, gives

\[
 \beta(m+2\pi,\delta)=\beta(m,\delta),\qquad
 \beta(m,-\delta)=\beta(m,\delta).                         \tag{15}
\]

There is no continuation around an unknown monodromy branch: the
unique root always remains in the fixed tube |beta-b(m)|<eta.
This construction proves actual convergence and existence by the
named theorem, rather than merely solving a recurrence of jets.

### Exact reality, uniform positivity and preserved jets

For this beta define

\[
 S(m,\delta)=\alpha(m)(\beta(m,\delta)+i)^3
                 H(m,\delta(\beta(m,\delta)+i)).            \tag{16}
\]

Equation (12) says S is real for every real (m,delta) in the cylinder.
It is analytic, even in delta, and S(m,0)=D(m). Equations (9) and (16)
give the exact identity alpha J(m,v)=delta^3 S(m,delta)/3, including
delta=0. Differentiating at fixed m in (10) yields

\[
 q(m+\delta,m-\delta)
   =4C\delta^2\left(S(m,\delta)
                      +\frac\delta3\partial_\delta S(m,\delta)\right).
                                                               \tag{17}
\]

This is an exact real identity, not a truncated expansion.
The bracket is continuous on the cylinder, with value D(m) at
delta=0. Shrink the width uniformly, by compactness and
min D=K_*/(4C)>0, until that bracket is at least (min D)/2.
Formula (17) proves (5) on the resulting cylinder, with the zero
on the diagonal intact.

The local u in (6) is real analytic and exchange-equivariant since
V=delta beta is odd in delta. Its value at delta=0 is h. In these
coordinates partial_t-partial_s=partial_delta, so
(partial_1-partial_2)u_1(m,m)=V_delta(m,0)=beta(m,0)=b(m).
The tangential derivative also remains exactly h'. No phase branch
or prescribed jet has been changed to obtain solvability.

### The torus collar and a smooth global extension

For any width less than pi/2 the map
(m,delta) -> (m+delta,m-delta) modulo 2pi is a smooth injective
collar chart. To check uniqueness, two representatives give
delta'-delta=pi(n-l) for integers n,l; its absolute value is less
than pi, so n=l, delta'=delta and m'=m modulo 2pi. Conversely, the
unique representative of t-s in (-pi,pi) gives 2delta, then m=s+delta
modulo 2pi. Thus a cylinder of width a<pi/2 is exactly the set
dist_(R/2pi Z)(t,s)<2a. Exchange of t,s sends (m,delta) to (m,-delta).

Choose 0<a<b_0<epsilon_0, where epsilon_0 is a width on which the
local analytic construction and (17) are valid and positive off the
diagonal. A smooth even cutoff chi(delta), equal to 1 for |delta|<=a
and 0 for |delta|>=b_0, can be given explicitly by

\[
 \rho(x)=\begin{cases}e^{-1/x},&x>0,\\0,&x\leq0,\end{cases}
 \qquad
 \chi(\delta)=\frac{\rho(b_0^2-\delta^2)}
 {\rho(b_0^2-\delta^2)+\rho(\delta^2-a^2)}.                 \tag{18}
\]

The denominator is positive everywhere because a<b_0. The flatness
of rho at zero makes chi smooth. On the collar set
u_1=chi(delta)(h(m)+delta beta(m,delta)) and
u_2=chi(delta)(h(m)-delta beta(m,delta)), and set both to zero
outside this chart. They already vanish on an open neighborhood of
the chart boundary, so this defines a smooth map on the whole torus.
Periodicity in the original angles follows because the definition is
on T^2 itself, not on a chosen global midpoint lift. Evenness of chi
and (15) preserve exchange symmetry. On |delta|<a the functions and
all their derivatives equal the local construction. Taking epsilon=a
therefore proves (4)–(5) for the full pullback of this global graph.
The cutoff can change the phase and sign outside that smaller collar;
neither property is asserted there.

The form (1) has not been divided by G, by the Vandermonde factor or
by a complex graph Jacobian. Its only denominators z_1,z_2 are
nonzero on every radial graph. The removable normalization (9) was
used solely to construct a graph; (10) and (17) restore its full
collision factor. L847's graph and homotopy conclusions now apply to
the smooth periodic u just constructed. The global product-graph stop
and L848's negative averaged extension are unchanged.

### Separate conceptual audit, 6 November 2026

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-06-exact-collar-construction-audit.md`.
This audit reproduces and checks the written construction; it does not
claim another theorem, new source coverage, an effective width or a new
numerical enclosure. The precise Chaperon corollary cited above is the
imported analytic existence theorem. Its real scalar hypotheses are
verified below; the corollary itself is not reproved.

**Data and removable normalization.** The exact sector conclusion of
audited L848 excludes the whole principal-logarithm cut and zero, not
just sampled points. Together with the positive radicand, positive r,
and the strict tangent-pole margin, it makes h,b real analytic and
periodic. Compactness supplies uniform margins. This imports L848's
actual-G conclusion with its L778(2)–(5)/step433 analytic and software
qualifications; no fresh evaluator replay or zero census is used.

An independent check of (8)–(9) writes

\[
 B(m,v)=z(m)^{-2}G(z(m)e^v)G(z(m)e^{-v})
                       \left(\frac{\sinh v}{v}\right)^2,
 \qquad H(m,v)=3\int_0^1 t^2B(m,tv)\,dt.
\]

The quotient sinh(v)/v has its entire removable value 1 at zero;
B is even, entire in v and locally jointly analytic after complexifying
a chart of m. Integration on the fixed compact interval preserves that
analyticity: on each smaller complex neighborhood its analytic series
converges uniformly and can be integrated term by term. Substituting
zeta=tv in J gives the displayed formula for H, including v=0, with
H(m,0)=f(m)^2. It checks both the factor 3 and evenness. Only the
primitive has been normalized; the original form's collision factor
has not been cancelled from the claimed density.

**Full orientation cross-check.** Directly in (t,s) coordinates the
graph (6) has tr(Du)=h'+V_delta and det(Du)=h' V_delta;
the V_m terms cancel. Thus L847's full formula gives

\[
 q=-4C A(m,v)(1-i h')(1-iV_\delta)
   =4C\alpha(m)A(m,v)(V_\delta+i).
\]

This independently agrees with (10), including its sign and factor,
without changing the original dt wedge ds orientation or assuming a
nonzero complex Jacobian. Also alpha(b+i)^3=(1-i h')(1-i b)^3,
because the four factors i multiply to +1. Hence D=K_0/(4C), as used
in (11), is positive and has the stated normalization.

**Actual uniform branch.** Let
d_0=min_m 3D(m)/(1+b(m)^2)>0. Joint continuity and compactness give
a tube |x|<=eta, |delta|<=epsilon_1 in which
partial_x E_tilde<=-d_0/2. Taking c=d_0/2 and then shrinking only
epsilon_1 gives |E_tilde(m,delta,0)|<c eta/2 uniformly. The endpoint
signs in (14) follow by integrating this derivative inequality. The
unique root actually satisfies |x|<eta/2, so it stays inside the tube
where the local real analytic implicit function theorem applies.
Its equation is real analytic, its value is zero at that root, and
the unknown derivative is nonzero. Local analytic solutions agree on
overlaps by uniqueness in the same tube. This supplies actual analytic
solutions, not just Taylor jets. Translation by 2pi in m and reflection
of delta preserve the equation, center b and tube, giving exactly (15).
No unproved periodic continuation or monodromy assertion is needed.

**Full-density bound and extension.** With that actual root, S in (16)
is real and even and has S(m,0)=D(m). Differentiating alpha J at fixed
m gives exactly (17), including delta=0. On a closed smaller cylinder,
the bracket in (17) is uniformly continuous and equals D on the central
circle. Its lower bound min D/2 therefore gives precisely K_*/2 in
(5), not a bound merely for Re q or a leading Taylor coefficient.
V=delta beta is odd and has V_delta(m,0)=b(m), so both the prescribed
jet and exchange symmetry hold. The zero on the diagonal is retained.

For a width below pi/2, equality of two collar images forces
delta'-delta=pi(n-l), hence n=l; the coordinate chart is injective.
The representative of t-s in (-pi,pi) supplies its inverse, including
where an individual angle crosses its coordinate seam. Periodicity in
m makes the local functions well-defined there. In (18), a<b_0 makes
the denominator strictly positive; chi is even, smooth, identically
one on the smaller collar and zero on an open neighborhood of the
chart boundary. Extending by zero is therefore smooth and periodic,
and all derivatives on the smaller collar are unchanged. Neither
reality nor nonnegativity is asserted on the cutoff transition.
Angular projection composed with the resulting radial graph is the
identity, giving the embedding; L847's radial homotopy stays in
(C minus zero)^2 and preserves the parameter orientation. No new
homology or sign assumption has entered.

All stated local claims pass. The direct mathematical inputs remain
L847 and L848; the latter carries the qualified analytic/numerical
inputs just noted. No new DAG edge, mathematical script or certificate
is required. The audit is REPRODUCTION of this local application, not
progress beyond the inspected literature or a second collar discovery.
It accepts no conclusion about global phase/sign, quantitative width,
other orders/shifts, positivity transfer or RH.

## Mathlib

Full matching coverage for this prescribed actual-G collar has not
been checked. No Mathlib theorem is claimed as a full match or as
verification of the exact primitive, periodic patching, cutoff or
inherited numerical sector input. The analytic implicit function
theorem is imported by the precise source above. An independent
conceptual audit of this application is recorded above; it is informal
verification and makes no claim of new Mathlib coverage.
