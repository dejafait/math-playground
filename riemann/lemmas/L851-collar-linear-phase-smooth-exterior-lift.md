# Lemma 851: a smooth exterior phase lift leaves only transition residuals

## Hypotheses

Use the actual entire G, positive coefficients a_n, and the unique R>0
with RG'(R)/G(R)=1 from L775. Put C=R^2/G(R)^2 and retain L847's
full form and original dt wedge ds orientation. Let u be any L849(18)
cutoff of its accepted local branch, with 0<a<b_0<epsilon_0<pi/2
and even cutoff chi. No effective epsilon_0 is assumed. Write

\[
 F(\Phi_u)=P_u+iQ_u,\quad \sigma_u=\operatorname{Im}q_u,\quad
 M_u=P_u I+Q_u\operatorname{adj}(Du).
                                                               \tag{1}
\]

Use L850's exact first variation D(Im q)_u[v]=-div(M_u v) and its
zero-total-integral conclusion for sigma_u. Those two identities are
checked again below before use; L850's separate exterior sign certificate
is not used. For the new finite calculation, retain L778(2)–(5)'s exact
degree-96 polynomial, all 97 interval coefficients, its uniform error on
|z|<=1600 and the step433 analytic/trusted-software qualifications.
Neither its zero count nor Fredholm norm is an input here.

All variations are real vector fields in the original angular coordinates.
Zeros of the full form and all possible transition degeneracies are retained.
No RH, zero simplicity, global nonvanishing assumption, nonlinear correction
or sign conclusion is imposed.

## Conclusion

There is a smooth real exchange-equivariant vector field v_ext on the
entire open cylinder T^2 minus the diagonal such that

\[
                    \operatorname{div}(P_0 v_{\rm ext})=Q_0,
 \qquad P_0+iQ_0=F(\Phi_0).                                \tag{2}
\]

It is smooth through every exterior P_0-zero and on a neighborhood of
each closed annulus disjoint from the diagonal. No bound or extension
to the diagonal is asserted for v_ext. Consequently every permitted
cutoff u admits a smooth real exchange-equivariant trial variation v_* on
T^2, identically zero on dist(t,s)<=2a, with

\[
 r_u:=\sigma_u-\operatorname{div}(M_u v_*)=0
 \quad\text{if }\operatorname{dist}(t,s)<2a
       \text{ or }\operatorname{dist}(t,s)>2b_0.              \tag{3}
\]

In the cylinder coordinates t=m+delta, s=m-delta, 0<delta<pi,
the residual is supported in the two closed strips
[a,b_0] and [pi-b_0,pi-a]. Its integral on each strip separately is
zero. In particular, for any b_0<d<pi/2 the residual has compact
support in the disjoint annuli

\[
 U_+=\{a/2<\delta<d\},\qquad
 U_-=\{\pi-d<\delta<\pi-a/2\}.                             \tag{4}
\]

This solves the flat-exterior portion of the actual linear target, including
its singular matrices. The full equation remains open: a smooth lift of
r_u through M_u in the transition has not been constructed or obstructed.
A correction supported in U_+ union U_- would suffice; its existence is
not asserted, and this extra support restriction is not claimed necessary
for a general global solution. This is an intermediate local advance, not
a full-torus solution, global reality/sign, a mixed-minor sign, or RH.
The new construction and certificate remain pending a separate conceptual
audit. POTENTIALLY_NEW refers only to the prior bounded source comparison,
not certified originality.

## Proof

### Coverage, imports and prerequisite checks

The unchanged invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-collar-preserving-linear-phase-correction.md`.
It covers this actual-G constrained range test with every zero retained.
The product stop in L847, failed averaged extension in L848, and pointwise
inverse stop in L850 do not decide this coupled linear problem. No new
global transport theorem is imported, and Teixeira's ordinary divergence
theorem is not substituted for smooth lifting.

The standard analytic estimates used in the finite certificate are those
already inspected for L848 and retained in L850: Jiří Lebl, *Guide to
Cultivating Complex Analysis*, version1.10, 5 November2026,
[Theorem3.3.8, p79](https://www.jirka.org/ca/ca.pdf#page=79), Cauchy's
coefficient/derivative estimates on a closed disk with a holomorphic
neighborhood. Here G-P_0 is entire and the enclosing disks lie in
|z|<=1600. For smooth local inversion use the already inspected analytic
implicit function theorem, Marc Chaperon, *On the Cauchy-Kowalevski
theorem*, 9 January2007,
[Section1, Corollary1, p2](https://webusers.imj-prg.fr/~marc.chaperon/Chaperon_Cauchy_Kowalevski.pdf#page=2).
The single real unknown derivative is strictly nonzero below. These are
known imports. The phase inequality and explicit lift are specializations
not supplied by those theorems, which is why they are calculated here.

For the operator check, a real radial variation has dot z_j=z_j v_j.
Contraction of L847's closed form gives the one-form

\[
 \beta=F(\Phi_u)\{v_2du_1-v_1du_2+i(v_2dt-v_1ds)\}.
\]

The pullback differentiation formula imported in L850 from Guillemin–
Sternberg, *Semi-classical analysis*, 13 January2010,
[Section13.13, (13.7)–(13.9), pp449–452](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449),
applies to these smooth maps and closed forms, without a nonzero complex
Jacobian. Its imaginary part is (M_u v)_2 dt-(M_u v)_1 ds, whose
exterior derivative is -div(M_u v) dt wedge ds. This verifies the sign
in (1), including at zeros. L847's homotopy makes integral q_u equal
integral q_0; real coefficients give q_0(-t,-s)=conjugate(q_0(t,s)),
so integral sigma_u=0. These checks do not audit L850's unused certificate.

### A finite exact certificate for a circular phase inequality

Set c_n=a_n R^n and, for k>=1, define the convergent real sums

\[
 B_k=\sum_{n\ge0}(2n+k-2)c_n c_{n+k}.                       \tag{5}
\]

All terms are nonnegative for k>=2. For k=1 the only negative term
is -c_0 c_1. The exact certificate gives three lower bounds b_k<=B_k,
with b_2,b_3>0, such that

\[
 \kappa:=b_1+b_2-\frac{b_2^2}{4b_3}>\frac1{4000}>0.         \tag{6}
\]

Here is the complete finite certification rule, including uncertainty.
Write [p_(n,-),p_(n,+)] for each of L778's 97 coefficient intervals
and E for its full error upper endpoint, E<3.141*10^(-48). First use
the rational endpoints

\[
             r_-=184.82837518,\qquad r_+=184.82837520.
                                                               \tag{7}
\]

For x equal to either endpoint, interval Horner evaluation of
sum_(n=0)^96 (n-1)p_n x^n encloses xP_0'(x)-P_0(x).
Cauchy on the disk centered at x with radius 1600-x gives
|(G-P_0)'(x)|<=E/(1600-x). Thus widening that interval by
E*1600/(1600-x) encloses xG'(x)-G(x), including both errors.
The resulting upper endpoint at r_- is less than zero and the lower
endpoint at r_+ is greater than zero. L775's strictly increasing
xG'(x)/G(x) and G(x)>0 give r_-<R<r_+.

For 0<=n<=11, Cauchy's estimate at zero gives

\[
 p_{n,-}-E/1600^n\le a_n\le p_{n,+}+E/1600^n.
\]

All twelve lower endpoints are checked strictly positive. Hence

\[
 c_n^-=(p_{n,-}-E/1600^n)r_-^n\le c_n
 \le(p_{n,+}+E/1600^n)r_+^n=c_n^+.                         \tag{8}
\]

For each k=1,2,3, sum the terms in (5) for 0<=n<=11-k.
Use -(c_0^+ c_1^+) for the unique negative term, and use
(2n+k-2)c_n^- c_(n+k)^- for every nonnegative term. Call the result
b_k. Every omitted term has positive weight and positive coefficients,
so these are lower bounds for the infinite sums, with no missing
negative tail. Exact rational arithmetic proves (6). Displays only:
the saddle upper and lower endpoints are approximately
-5.84835186781*10^(-12) and 1.19320962067*10^(-11), respectively,
and kappa is approximately 0.000273346304964.
The proof uses exact signs and the threshold 1/4000, not those rounded
displays or the preceding floating-point diagnostic.

The full input hash, all inherited intervals/error, both saddle enclosures,
all twelve coefficient and scaled-coefficient enclosures, every retained
term, the three exact b_k, kappa, eight checks and the empty failure list
are in `scripts/actual-g-radial-graph/exterior-phase-certificate.json`.
The exact implementation and the complete check values, including both
saddle enclosures and the rational margin, were inspected. Reproduce with
a fresh output filename, since the script refuses to overwrite evidence:

~~~text
python3 scripts/actual-g-radial-graph/exterior_phase_certificate.py --output exterior-phase-replay.json
python3 ../scripts/loop/inspect_json.py scripts/actual-g-radial-graph/exterior-phase-certificate.json --pointer /phase_margin --full
~~~

This is PASS_PENDING_INDEPENDENT_AUDIT. Fraction arithmetic is exact;
L778's analytic and trusted-software input is retained, not rebuilt or
formally verified. The separate `exterior-phase-diagnostic.json` used
floating midpoints to select this inequality and supplies no proof.

### Strict circular phase monotonicity

Let z=R exp(i theta) and put

\[
 N(\theta)=\operatorname{Re}(zG'(z)\overline{G(z)})-|G(z)|^2.
\]

Absolute convergence justifies grouping the double series: for example,
sum_n n c_n<infinity and sum_n c_n<infinity follow from entire
convergence at 2R. Direct multiplication gives

\[
 N(\theta)=\sum_{n\ge0}(n-1)c_n^2
             +\sum_{k\ge1}B_k\cos(k\theta).
\]

The saddle identity implies N(0)=0. Thus

\[
 N(\theta)=-\sum_{k\ge1}B_k(1-\cos(k\theta)).              \tag{9}
\]

For theta not in 2pi Z set x=cos(theta). Every quotient
(1-cos(k theta))/(1-cos(theta)) is nonnegative. For k=1,2,3 these
quotients are respectively 1, 2(1+x), and (2x+1)^2. Keeping these
three modes, using B_k>=0 for k>=4 and (5)–(6), gives

\[
 \begin{split}
 \frac{-N(\theta)}{1-\cos\theta}
 &\ge b_1+2b_2(1+x)+b_3(2x+1)^2\\
 &=b_3\left(2x+1+\frac{b_2}{2b_3}\right)^2+\kappa
 >\frac1{4000}.
 \end{split}                                                \tag{10}
\]

If G(R exp(i theta)) were zero, N(theta) would be zero, contradicting
(10), except possibly at theta in 2pi Z, where G(R)>0 already.
Therefore G is nonzero on this circle. This finite nonvanishing is only
an auxiliary consequence of (10), not a new zeta zero-free region or a
claim beyond the stronger finite zero information already in L778.

Define g(theta)=G(R exp(i theta))/(R exp(i theta)). There is a smooth
real phase lift phi on R with phi(0)=0, and

\[
 g(\theta)=|g(\theta)|e^{i\phi(\theta)},\qquad
 \phi'(\theta)=\operatorname{Re}\frac{zG'(z)}{G(z)}-1
             =\frac{N(\theta)}{|G(z)|^2}.                 \tag{11}
\]

For an explicit construction, integrate the last smooth real function
from zero. Differentiating g/|g| shows it has the same logarithmic
derivative as exp(i phi), and both equal one at zero. This proves the
phase identity without a global logarithm on the complex circle.
Equation (10) makes phi'<0 except at 2pi Z, where phi'=0.
Its derivative is periodic, so phi(theta+2pi)-phi(theta) is constant;
periodicity of g makes that constant an integral multiple of 2pi.
It is strictly negative by (11). Write it as -2pi nu for a positive
integer nu. Its exact value is not needed and no zero census is used.

### Global exterior coordinates and an explicit lift across every zero

The map (m,delta) -> (m+delta,m-delta) with m modulo 2pi and
0<delta<pi is a smooth one-to-one chart for the torus minus the
diagonal. Indeed the unique representative of t-s in (0,2pi) gives
2delta, then m=s+delta modulo 2pi. In these coordinates set

\[
 x=\phi(m+\delta)+\phi(m-\delta)\pmod{4\pi\nu},\qquad
 y=\delta.                                                 \tag{12}
\]

Changing m by 2pi changes the real lift of x by -4pi nu, so this
is well-defined on a circle of length 4pi nu. Moreover

\[
 x_m=\phi'(m+\delta)+\phi'(m-\delta)<0.                     \tag{13}
\]

Both derivatives could vanish only if m+delta and m-delta were in
2pi Z, forcing delta in pi Z, excluded here. For each fixed y,
the strictly decreasing lift of x traverses exactly one period as m
traverses its circle. It is therefore bijective between these circles.
The local implicit function theorem and (13) give a smooth inverse;
uniqueness makes the inverses agree. This yields global smooth cylinder
coordinates, with no phase branch jump. On each closed subcylinder
0<d<=y<=pi-d, the derivative stays bounded away from zero by compactness.

For the undeformed graph, the full formula is

\[
 F(\Phi_0)=4C g(t)g(s)\sin^2\delta=H(x,y)e^{ix},\qquad
 H=4C|g(t)g(s)|\sin^2 y>0.                                 \tag{14}
\]

It is the full F, not a form with its zeros divided out. The complex
F has no zero off the diagonal on this base graph, while P_0=H cos x
has its retained nodal curves. The area form transforms as

\[
 dt\wedge ds=-2dm\wedge d\delta
             =\mu(x,y)dx\wedge dy,\qquad
 \mu=-2/x_m>0.
\]

Put A=mu H>0. It is smooth and periodic in x with period 4pi nu.
Define a real vector field in these coordinates by

\[
 V^x=-1,\qquad
 V^y=\frac{1}{A(x,y)}\int_{\pi/2}^{y} A_x(x,\eta)\,d\eta.
                                                               \tag{15}
\]

For any point of the open cylinder the integration interval is compact
inside (0,pi). Smoothness under the integral and A>0 give a smooth
periodic field, including at cos x=0. No division by P_0 occurs.
Transforming this field back gives a smooth real angular field v.
The divergence formula follows directly by contracting the displayed
area form with P_0 V and differentiating. It gives

\[
 \begin{split}
 \mu\operatorname{div}(P_0v)
 &=\partial_x(A\cos x\, V^x)+\partial_y(A\cos x\,V^y)\\
 &=A\sin x-A_x\cos x+
       \cos x\,\partial_y\int_{\pi/2}^{y}A_x(x,\eta)\,d\eta\\
 &=A\sin x=\mu Q_0.                                      \tag{16}
 \end{split}
\]

This verifies (2) everywhere in the cylinder, including every nodal
curve, without deleting its zeros or using a pointwise matrix inverse.
In particular it is an actual smooth M_0-preimage of a suitable flux,
not merely pointwise membership in the image of M_0.

Let E swap t and s. Since P_0(E theta)=P_0(theta) and similarly for
Q_0, the field E v(E theta) also satisfies (2). Define
v_ext(theta)=(v(theta)+E v(E theta))/2. It is smooth, real,
exchange-equivariant and still satisfies (2). The cylinder and every
closed exterior dist(t,s)>=2b_0 are invariant under exchange.

### A global trial variation and its exact remaining support

Regard the L849 cutoff chi as a smooth exchange-invariant scalar on
the torus: in the cylinder it equals chi(delta) near delta=0,
chi(delta-pi) near delta=pi, and zero elsewhere. These descriptions
agree smoothly since chi is already zero for |delta|>=b_0<pi/2.
On the cylinder define

\[
                         v_*=(1-\chi)v_{\rm ext}.          \tag{17}
\]

Set it to zero on the diagonal. It is identically zero on an open
neighborhood of the diagonal, since chi=1 for dist(t,s)<=2a.
Therefore (17) extends smoothly even if v_ext has no bounded limit
there. It is real, periodic and exchange-equivariant.

In the open flat exterior dist(t,s)>2b_0, u=0, Du=0, M_u=P_0 I,
sigma_u=Q_0, and v_*=v_ext. Equation (16) proves r_u=0 there.
In the inner collar dist(t,s)<2a, v_*=0 and L849 gives sigma_u=0,
so again r_u=0. Smoothness supplies the same values at the endpoints;
the support is consequently contained in the closed strips in (3).
These are compactly contained in (4).

L850's covariance M_u(E theta)=E M_u(theta)E and the scalar symmetry
sigma_u(E theta)=sigma_u(theta) imply r_u(E theta)=r_u(theta).
The total integral of r_u is zero: integral sigma_u=0 was checked
above and the integral of the divergence of the smooth periodic field
M_u v_* is zero. In the chosen cylinder E maps
(m,delta) to (m+pi,pi-delta), exchanging the two residual strips.
It preserves the positive angular area measure. Their integrals are
therefore equal, and their sum is zero, so each integral is zero.
This is a statement about scalar integration; the orientation reversal
of E does not introduce a minus sign in that equality of measures.

Finally, if a smooth collar-vanishing w satisfies div(M_u w)=r_u,
then v=v_*+w solves the original target. A w supported in (4), made
exchange-equivariant, would suffice and preserve the collar. Zero integral
in each annulus gives only the compatibility for ordinary divergence.
It does not solve division/lifting through the transition M_u. Conversely,
a general solution of the original target need not differ from v_* by
a transition-supported field; no such necessity is claimed. Smooth
transition lifting, choice of cutoff if needed, nonlinear convergence,
global reality/nonnegativity, other orders/shifts and mixed positivity
remain unresolved.

## Mathlib

Full matching coverage for this actual-G phase inequality, cylinder
coordinate construction and exterior lift was not checked. No Mathlib
formalization or absence claim is made. Cauchy estimates and the local
implicit function theorem are known cited inputs; the exact arithmetic
certificate and informal specialization retain their stated qualifications
and await a separate conceptual audit.
