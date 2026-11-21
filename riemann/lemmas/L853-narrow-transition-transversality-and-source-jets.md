# Lemma 853: narrow cutoff crossings are transverse and admit finite source-jet cancellation

## Hypotheses

Use L847's actual entire G, positive R,C and full form, in the original
angular coordinates theta=(t,s):

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},\quad
 z_j=R e^{u_j+i\theta_j},\quad
 q_u=F(\Phi_u)J,\quad J=1-\det(Du)-i\operatorname{tr}(Du).       \tag{1}
\]

Use exactly L848's prescribed h,b and L849's accepted real analytic
branch beta. Retain L848's qualified sector input G(-1000)<0 and
L850's qualified bounds R<256 and G(-R)>1/100. Their inherited
L778(2)–(5)/step433 analytic and trusted-software qualifications remain.
No new numerical estimate or zero list is an input.

For 0<epsilon<epsilon_0 choose the explicit L849(18) cutoff with
a=epsilon/2 and b_0=epsilon. Denote it by chi_epsilon. In the collar,

\[
 u_1=\chi_\epsilon(\delta)B(m,\delta),\quad
 B(m,\delta)=h(m)+\delta\beta(m,\delta),\quad
 u_2=\chi_\epsilon(\delta)(h(m)-\delta\beta(m,\delta)),
 \qquad (t,s)=(m+\delta,m-\delta).                           \tag{2}
\]

Extend by zero as in L849. All widths and thresholds below are
existential. Do not assume simple zeros of G, a nonzero J, global
nonvanishing, an effective collar width or RH.

## Conclusion

There is epsilon_1>0 such that, for every 0<epsilon<epsilon_1,
the set of points

\[
 p=(\pi,\pi-2\delta),\qquad
 \epsilon/2<\delta<\epsilon,\qquad G(z_1(p))=0               \tag{3}
\]

is nonempty and finite. At each such p,

\[
 A_{12}(p)=\partial_s u_1(p)>0,\qquad
 G(z_2(p))\ne0,\qquad z_1(p)\ne z_2(p).                    \tag{4}
\]

In a neighborhood of p the map
w=u_1-u_1(p)+i(t-p_1) is a real analytic coordinate. If n is the
multiplicity of G at z_1(p), then

\[
                    F(\Phi_u)=w^n K,\qquad K(p)\ne0.       \tag{5}
\]

There is a smooth real, periodic, exchange-equivariant variation v,
supported in the open transition strips and hence zero on a smaller
diagonal collar, such that at every point (3) and its exchange partner,

\[
 \partial^\alpha\bigl(Dq_u[v]+q_u\bigr)(p)=0
                         \quad (|\alpha|\le n).            \tag{6}
\]

Thus the required imaginary-part equation has no obstruction through
the multiplicity order at these actual forced crossings. If J(p)=0,
the first possibly nonzero source order can be higher than n; (6)
does not claim cancellation through that higher order.

This is a finite-jet result, **not** a smooth solution on any
neighborhood or on the torus. It does not handle every transition
zero, all rank degeneracies, or global flux assembly. It supplies
neither a full-range obstruction nor global reality/nonnegativity.
The original bounded attempt remains EXPLORATION against that stronger
threshold. The separate conceptual audit below accepts (3)–(6), with
their inherited qualifications and no stronger conclusion.
The construction-stage POTENTIALLY_NEW label records only bounded
source coverage, not certified originality.

## Proof

### Coverage, imports and prerequisite scope

The unchanged invocation-start assessment
`drafts/literature/2026-11-06-collar-preserving-linear-phase-correction.md`
has DECISION EXPLORE and covers this constrained operator/source test.
The transition inverse stop and L852's value condition do not determine
smooth local range. Searches in the relative-phase working notes,
histories and failure records found no prior transition transversality
or finite source-jet construction. No new general PDE theorem is used.

Import the isolated-zero theorem for a nonzero holomorphic function:
Jiří Lebl, *Guide to Cultivating Complex Analysis*, version 1.10,
5 November 2026, [Theorem 2.4.7, pp49–50](https://www.jirka.org/ca/ca.pdf#page=49),
already inspected in the L847 source comparison. Here G is entire and
G(0)>0, so it is not identically zero. Taylor factorization at an
isolated zero retains its finite multiplicity. For the local analytic
coordinate use the real analytic inverse function theorem, equivalently
the implicit function theorem in Marc Chaperon, *On the Cauchy-Kowalevski
theorem*, 9 January 2007,
[Section 1, Corollary 1, p2](https://webusers.imj-prg.fr/~marc.chaperon/Chaperon_Cauchy_Kowalevski.pdf#page=2),
already inspected for L849/L851. Its Jacobian condition is proved below.
These known inputs do not themselves give (4) or the source cancellation;
the required cutoff and full-form specializations are written out.

Before use I checked L852's full endpoint and point-value argument:
on t=pi the accepted positive collar has G(z_1)<0, because it starts
at G(-1000)<0 and q_u>0 prevents a G-zero there; the flat endpoint
has G(-R)>0. The intermediate value theorem therefore places a zero
strictly inside the transition for every permitted cutoff. Neither
this argument nor its first-variation formula divides by F or J.
This is a prerequisite check of that implication, not a fresh replay
of unchanged numerical inputs or a blanket upstream audit. The present
proof uses its crossing assertion, not L851's exterior certificate.

### A finite set of possible root radii

Put H=h(pi)=log(1000/R)>0. Uniformly for 0<=delta<=epsilon,

\[
                         B(\pi-\delta,\delta)\longrightarrow H.
                                                               \tag{7}
\]

Choose eta>0 so that G(-r) has no zero for
1000-eta<=r<=1000+eta; this is possible because G(-1000)<0.
The zeros of G(-r) on the compact interval [R,1000+eta] form a
finite set {rho_1,...,rho_N}. Isolation, compactness and the
nonzero endpoint values show that every rho_j lies strictly between
R and 1000. The endpoint sign change makes this set nonempty.

For sufficiently small epsilon, (7) makes B positive and
R exp B<=1000+eta on the path. Since 0<=chi_epsilon<=1, every
radius R exp(chi_epsilon B) on the path is in [R,1000+eta].
At any point (3) it therefore equals some rho_j, and

\[
 \chi_\epsilon(\delta)
     =\frac{\log(\rho_j/R)}{B(\pi-\delta,\delta)}.          \tag{8}
\]

All the finitely many limits log(rho_j/R)/H lie in (0,1).
Consequently one can fix 0<eta_0<1/2, independent of epsilon,
so that at every such crossing, for sufficiently small epsilon,

\[
                  \eta_0\le\chi_\epsilon\le1-\eta_0.       \tag{9}
\]

This argument uses no zero count, simplicity or approximate location.
L852 ensures at least one crossing in (3).

### Transversality from the explicit cutoff

In epsilon/2<delta<epsilon the exact L849 cutoff satisfies

\[
 \log\frac{\chi_\epsilon}{1-\chi_\epsilon}
  =-\frac1{\epsilon^2-\delta^2}
      +\frac1{\delta^2-\epsilon^2/4}.
\]

Differentiation gives

\[
 -\chi_\epsilon'
 =2\delta\chi_\epsilon(1-\chi_\epsilon)
 \left\{(\epsilon^2-\delta^2)^{-2}
           +(\delta^2-\epsilon^2/4)^{-2}\right\}.
                                                               \tag{10}
\]

At a crossing, 2delta>=epsilon and both positive denominators before
squaring are <=epsilon^2. With d=eta_0(1-eta_0)>0 this implies
-chi_epsilon'>=2d epsilon^(-3). On a fixed compact neighborhood
of (pi,0), B and its derivatives are bounded independently of epsilon.
Shrink epsilon so B>=H/2 along the path, and choose a fixed K_0
bounding |B_m-B_delta| there. In the original angular coordinates,

\[
 \begin{split}
 A_{12}
 &=\tfrac12\{\chi_\epsilon(B_m-B_\delta)-\chi_\epsilon' B\}\\
 &\ge\tfrac12\{dH\epsilon^{-3}-K_0\}>0                   \tag{11}
 \end{split}
\]

for all sufficiently small epsilon at every crossing.
This is an actual bound versus the required threshold zero;
its constants and onset are existential, not numerically evaluated.

On the path, the derivative of u_1(pi,pi-2delta) is -2A_12.
Thus each solution of the level equation u_1=log(rho_j/R)
is isolated. The crossing set is closed in [epsilon/2,epsilon],
has no endpoint there, and has no accumulation point by (11).
Compactness makes it finite.

For each rho_j choose a complex disk about -rho_j containing no
other zero of G. At a crossing with z_1=-rho_j,

\[
 z_2=-\rho_j\exp\{-2\chi_\epsilon\delta\beta(m,\delta)
                             -2i\delta\}.                 \tag{12}
\]

The boundedness of beta makes z_2 tend uniformly to -rho_j as
epsilon tends to zero. Finitely many disks suffice, so for all
sufficiently small epsilon it lies in the corresponding disk.
It is not its central root: 0<2delta<pi implies its imaginary
part is nonzero. Hence G(z_2)!=0, and z_2!=z_1 as well.
This proves (4) while allowing every finite multiplicity at z_1.

Finally, the derivative of (Re w,Im w) with respect to (t,s) is
the matrix with rows (A_11,A_12) and (1,0), of determinant -A_12.
It is nonzero by (11). Inside the transition the explicit cutoff
and the branch are real analytic, so the cited inverse function
theorem applies. Since z_1=z_1(p)exp w, Taylor factorization gives
G(z_1)=w^n g(w), with g(0)!=0. All other factors in (1) are
nonzero near p by (4). Their product gives precisely (5).

### Exact first variation and cancellation through order n

Work near one point p and keep the original coordinates (t,s).
Define the regular complex function

\[
 \kappa=\frac{z_2G'(z_2)}{G(z_2)}
                       -\frac{2z_2}{z_1-z_2}-2.           \tag{13}
\]

Its denominators are nonzero on a neighborhood by (4). Direct product
differentiation, including on G(z_1)=0, gives z_2 partial_(z_2)F=F kappa.
Thus (13) is not division of the full form by its zero.
For a real variation v=(0,f), only the second row of Du varies, and

\[
 D J[(0,f)]=A_{12} f_t-(A_{11}+i)f_s,
\]
\[
 Dq_u[(0,f)]
   =F\{J\kappa f+A_{12}f_t-(A_{11}+i)f_s\}.               \tag{14}
\]

This exact identity follows from (1) and requires no nonzero J.
Write a=A_11(p), b=A_12(p)>0, j_R=Re J(p), j_I=Im J(p).
Choose the real affine function, in a coordinate neighborhood,

\[
 f(t,s)=\frac{a j_I-j_R}{b}(t-p_1)+j_I(s-p_2).             \tag{15}
\]

It has f(p)=0 and
b f_t(p)-(a+i)f_s(p)=-j_R-i j_I=-J(p).
It follows that the smooth bracket

\[
                T=J\kappa f+A_{12}f_t-(A_{11}+i)f_s+J
\]

vanishes at p. Equations (5) and (14) give
Dq_u[(0,f)]+q_u=w^n K T. Every derivative of total order at
most n vanishes at p: w^n vanishes to order n and T vanishes
to order at least one. This proves (6) locally as a statement
about jets, including J(p)=0. It does not assert T=0 nearby.

There are finitely many crossing points. Their exchange partners
are distinct and lie in the other open transition strip; none is
on the diagonal. Choose disjoint small coordinate neighborhoods of
these points and partners, with closures in those strips. For each
unexchanged point multiply (0,f) by a smooth bump equal to one near
that point and supported in its neighborhood, and add its exchanged
field theta -> E v(E theta), where E swaps the components and angles.
The sum is a globally smooth real periodic exchange-equivariant v
with support in the transition strips. The bumps can be made from
the same exp(-1/x) smooth cutoff as L849. They leave the jets (15)
unchanged. Because F is symmetric and Du transforms by conjugation
under exchange, q_u(E theta)=q_u(theta); differentiating this identity
shows that (6) also holds at each partner. This proves the global
admissible finite-jet assertion.

### Limit of this test

The constructed variation has no equation imposed between the finite
crossings; bump derivatives create unrestricted residuals there.
Even locally the remaining bracket T need not vanish. No convergence,
smooth solution of the singular PDE, or source-jet condition above
order n has been established. Other zeros and det M=0 loci remain,
with M=Re F I+Im F adj(Du) as in L850. This test therefore does not
resolve the approved full-torus equation. It removes an unverified
transversality assumption for this narrow family and checks its first
potential source order, but does not justify another exploration-budget
reset or a global route stop. No conclusion about Xi signs follows.

### Separate conceptual audit, 6 November 2026

STEP_ID: 2026-11-06-l853-crossing-jet-conceptual-audit.
The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-06-l853-crossing-and-jet-audit.md`.
This is a REPRODUCTION audit of the existing actual-form application.
Reuse the precise Lebl isolated-zero/factorization and Chaperon analytic
inverse statements cited above; neither general theorem is reproved.
The root-radius, cutoff, full-variation and localization checks below
are the application-specific obligations, not new source theorems.

**Input boundary and orientation.** The normalization of G is exactly
L775's entire power series, with real positive coefficients and G(0)>0.
The needed part of L847 is its full form and
J=det(I-iDu)=1-det(Du)-i tr(Du), in the original (t,s) order.
No change to mean/separation area orientation is made. L848's sector
at -1000 gives G(-1000)<0; L850 supplies 0<R<256 and G(-R)>1/100.
These are retained qualified inputs. L852's proof records its exact
negative-axis replay; this audit neither reruns it nor independently
certifies L778's directed-arithmetic backend. It retains all
L778(2)–(5)/step433 analytic and trusted-software qualifications.
Only L852's endpoint crossing argument is used, not its residual
statement or L851's exterior lift. L849 supplies the accepted analytic
branch on a fixed cylinder, positive full density before cutoff, and
the smooth explicit cutoff (18).

**One width threshold for every crossing.** Fix a smaller closed
cylinder inside L849's analytic domain. The function
B(pi-delta,delta) and its first derivatives are bounded there, and
B(pi,0)=H=log(1000/R)>0. Choose a fixed eta>0 with G(-r) nonzero
for 1000-eta<=r<=1000+eta. Isolation and compactness give finitely
many distinct root radii rho_j in [R,1000+eta]; the nonzero values at
R and near 1000 put all of them in (R,1000). Endpoint signs ensure
that this list is nonempty. This list, and disks isolating its roots
from every other complex zero, are fixed before epsilon is chosen.

Uniform continuity gives B>=H/2 and R exp B<=1000+eta on the slice
for all sufficiently small widths. Consequently every slice crossing
uses a root on this fixed list. If ell_j=log(rho_j/R), then the
finite set ell_j/H lies strictly inside (0,1). Equation (8), with
B converging uniformly to H, therefore puts every crossing in one
fixed cutoff-value interval [eta_0,1-eta_0]. This is independent of
both the number and positions of crossings for a particular epsilon;
there is no assumption of a uniform separation between crossings.

For the stated cutoff the log-odds derivative is exactly (10). At a
crossing each denominator before squaring is at most epsilon^2 and
2delta>=epsilon, giving -chi'>=2d epsilon^(-3), where
d=eta_0(1-eta_0)>0. Since partial_s=(partial_m-partial_delta)/2,
the complete product derivative is exactly (11). Thus

\[
 A_{12}\ge\tfrac12(dH\epsilon^{-3}-K_0)>0
 \quad\hbox{when }dH\epsilon^{-3}>K_0.
\]

K_0 is fixed on the cylinder; only the cutoff derivative grows.
All restrictions so far can be met by a single positive upper bound
on epsilon. The threshold remains existential, as asserted.

At delta=epsilon/2, smooth flatness makes the graph and its first
derivatives equal the uncut positive collar. On the path from zero
to that endpoint, q>0 off the diagonal excludes a zero of G(z_1);
continuity from G(-1000)<0 fixes its negative sign. At delta=epsilon,
G(z_1)=G(-R)>0. This verifies L852's strictly interior crossing use.
For each fixed permitted epsilon the zero set is closed in the compact
slice interval and misses both endpoints. At a crossing the derivative
of its level function is -2A_12!=0. More explicitly, near that point
the radius is close to just one rho_j, and the nonzero derivative makes
the level locally injective. Thus there is no accumulation point,
even when G has a multiple zero; compactness proves finiteness.

**Second factor and analytic coordinate.** Equation (12) follows from
u_2-u_1=-2chi delta beta and s-t=-2delta. For bounded real beta its
right side tends uniformly to -rho_j over the finite list. Shrink the
same width threshold so z_2 belongs to the corresponding isolating
disk. Its imaginary part is
rho_j exp(-2chi delta beta) sin(2delta)>0 when 0<2delta<pi.
It is therefore not the disk's sole root -rho_j. This proves both
G(z_2)!=0 and z_2!=z_1 without a simplicity assumption or a census
of nonreal roots outside those disks.

The derivative matrix for (Re w,Im w) is exactly
((A_11,A_12),(1,0)), with determinant -A_12!=0. Each crossing lies
strictly inside the analytic transition, so the real analytic inverse
theorem applies on an open neighborhood; it is not applied at a flat
cutoff endpoint. Write the isolated-zero factorization as
G(z)=(z-z_1(p))^n H_1(z), H_1(z_1(p))!=0. Since
z_1-z_1(p)=z_1(p)(exp(w)-1), and (exp(w)-1)/w has nonzero value
1 at zero, G(z_1)=w^n g(w), g(0)!=0. The other factors of F are
nonzero on a sufficiently small neighborhood. Hence (5) holds with
K real analytic and nonzero there. It is not necessary, or asserted,
that all of K be holomorphic in the real coordinate w.

**Full variation, including J=0.** With A=Du and v=(0,f), the changing
row of A is (f_t,f_s). Direct differentiation gives

\[
 D\det A[(0,f)]=A_{11}f_s-A_{12}f_t,\qquad
 D\operatorname{tr} A[(0,f)]=f_s.
\]

For F, differentiation of the G(z_2), squared-difference and z_2^(-2)
factors gives exactly kappa in (13). The G(z_1) factor is unchanged;
this product identity is valid even where it is zero. Thus (14)
contains both D F and D J, with no division by F or J. The affine
function (15) is real and satisfies

\[
 f(p)=0,\quad f_s(p)=j_I,\quad
 b f_t(p)-(a+i)f_s(p)
 =a j_I-j_R-a j_I-i j_I=-J(p).
\]

Therefore T(p)=0 exactly, not just Im T(p)=0. Every derivative of
w^n of total order below n vanishes at p, because w(p)=0; in a
derivative of w^n K T of order at most n, either fewer than n
derivatives hit w^n or none remain to remove T(p)=0. The Leibniz
rule proves (6), including mixed derivatives in the original angles.
If J(p)=0, (15) gives the zero affine function and q already has
vanishing jets through order n. No division by J and no assertion
about the next nonzero source order has entered.

**Simultaneous localization and scope.** For each fixed epsilon,
finiteness gives disjoint coordinate neighborhoods of all crossings
and their exchange partners, with closures in the two open strips.
Neighborhood sizes and variation norms may depend on epsilon. No
uniform norm estimate is asserted. Multiplication by bumps identically
one near the centers leaves the local functions, hence all the needed
jets, unchanged. Extension by zero is smooth, including across angular
coordinate seams, because each bump is supported inside a torus chart.

For the exchanged sum v, both u and u+tau v are exchange-equivariant.
Their derivative matrices at exchanged points are conjugate by the
permutation matrix. F is symmetric, while determinant and trace are
unchanged by conjugation. Consequently q_(u+tau v)(E theta) equals
q_(u+tau v)(theta) as a scalar in the original coordinate convention.
Differentiating in tau and permuting the derivative multi-index proves
all partner cancellations. There is no extra orientation sign in this
scalar identity. The support stays away from a smaller diagonal collar.

All claims (3)–(6) pass this separate audit; no mathematical correction
or additional dependency is needed. This validates a local input for
later separately assessed constructions, not a new theorem beyond the
sources compared. The original finite-jet/range stop remains: T need
not vanish near a crossing, bump derivatives leave uncontrolled
residuals elsewhere, and higher jets when J(p)=0 remain unpaid.
No neighborhood solution, global flux assembly, phase/sign conclusion,
effective width, other-order result or RH candidate is certified.

## Mathlib

Full matching Mathlib coverage for this actual cutoff transversality,
its constrained variation and simultaneous jets has not been checked.
No formalization or absence claim is made. Isolated zeros, analytic
inversion, product differentiation and smooth cutoffs are standard
inputs; their precise uses and the inherited numerical qualifications
are given above. The separate informal conceptual audit above accepts
the stated local result; no Lean proof or additional Mathlib lookup
was performed.
