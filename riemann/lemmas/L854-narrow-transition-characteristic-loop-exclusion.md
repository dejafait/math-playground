# Lemma 854: narrow transition strips contain no smooth characteristic loop

## Hypotheses

Use the actual entire G, positive constants R,C, and full oriented form
of L847, with the prescribed h,b and accepted analytic branch beta of
L848/L849. Thus G has positive real coefficients,
RG'(R)/G(R)=1, C=R^2/G(R)^2, and

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},\quad
 z_j=R e^{u_j+i\theta_j},\quad (\theta_1,\theta_2)=(t,s),
 \qquad q_u=F(\Phi_u)\det(I-iDu).
 \tag{1}
\]

Retain L851's qualified conclusions

\[
 184.82837518<R<184.82837520<200,
 \qquad G(R e^{i\theta})\ne0\quad(\theta\in\mathbb R).
 \tag{2}
\]

Their L778(2)–(5)/step433 analytic and trusted-software qualifications
remain. Only these conclusions of L851 are used, not its exterior
vector field. The proof below records the prerequisite check; this is
not an independent audit of all its inputs.

For 0<epsilon<epsilon_0 use exactly L849(18) with a=epsilon/2 and
b_0=epsilon. In the diagonal collar, put

\[
 t=m+\delta,\quad s=m-\delta,\quad
 H=\frac{u_1+u_2}{2}=\chi_\epsilon(\delta)h(m),\quad
 V=\frac{u_1-u_2}{2}=\chi_\epsilon(\delta)\delta\beta(m,\delta).
 \tag{3}
\]

Here h(m)=log(r(m)/R),
r(m)=-400 cos m+sqrt(600^2-400^2 sin^2 m), and 200<=r<=1000.
The cutoff is smooth, even, one on |delta|<=epsilon/2 and zero on
|delta|>=epsilon. Extend u by zero as in L849. Let

\[
 F(\Phi_u)=P+iQ,\quad \sigma=\operatorname{Im}q_u,\quad
 M=P I+Q\operatorname{adj}(Du).
 \tag{4}
\]

Use L850's checked identity D(Im q)_u[v]=-div(Mv), including its
sign in dt wedge ds. A characteristic curve means a regular C^1
curve whose nonzero normal n satisfies M^T n=0 at every point.
There is no assumption of simple G zeros, a nonzero complex Jacobian,
an effective collar width, or RH.

## Conclusion

For all sufficiently small positive epsilon, neither closed strip

\[
 S_+=\{\epsilon/2\le\delta\le\epsilon\},\qquad
 S_-=\{-\epsilon\le\delta\le-\epsilon/2\}
 \tag{5}
\]

contains a regular closed characteristic curve. In particular there
is no smooth compact domain whose nonempty boundary is characteristic
and has every connected component contained in one of these strips.

This excludes a transition-confined smooth flux barrier for this
narrow-cutoff subclass. It does not exclude boundaries passing through
the flat exterior, nonsmooth barriers, other cutoff widths, or other
range obstructions. No domain with nonzero integral of sigma, and no
full-torus solution of div(Mv)=sigma, is constructed. Against that
invocation-start threshold this remains EXPLORATION, the third since
L851; it is not a resolution of the linear equation or an RH advance.
The new exclusion is pending separate critical audit. Its classification
POTENTIALLY_NEW reflects only the prior bounded source comparison.

## Proof

### Coverage, known inputs and prerequisite checks

The unchanged prior EXPLORE assessment is
drafts/literature/2026-11-06-collar-preserving-linear-phase-correction.md.
Its range-test scope includes this characteristic-boundary test. Searches
in the named collar/transition notes, histories and stops found no prior
closed-barrier calculation. L852's forced crossings and L853's finite
source jets do not imply the present claim; their conclusions are not
used as premises.

For standard inputs, reuse the inspected isolated-zero theorem and
Cauchy estimates: Jiří Lebl, *Guide to Cultivating Complex Analysis*,
version1.10, 5 November2026,
[Theorem2.4.7, pp49–50 and Theorem3.3.8, p79](https://www.jirka.org/ca/ca.pdf).
G is entire with G(0)>0, so its zeros are isolated and any compact
disk contains finitely many. No zero census or simplicity is imported.
For the flux implication use Lebl, *Tasty Bits of Several Complex
Variables*, version4.4, 31 May2026,
[Appendix C, Theorem C.6 and regularity remark, p224](https://www.jirka.org/scv/scv.pdf#page=224).
The fields here are smooth; Stokes on a compact smooth domain gives
integral_D div(Mv)=integral_boundaryD n dot Mv. These named results
are imported, not reproved. The cutoff and boundary calculations are
needed because these sources do not decide this constrained range.

Before using (2), checked L851's saddle enclosures, its absolutely
convergent Fourier identity for
N(theta)=Re(zG'(z) conjugate(G(z)))-|G(z)|^2, and its completed-square
lower bound -N(theta)/(1-cos theta)>1/4000. At a putative G zero away
from theta=0 that inequality contradicts N=0; at theta=0 positivity
of G(R) suffices. The saddle signs and the increasing mean-radius
function give the displayed radius bracket. Inspected the complete
implementation scripts/actual-g-radial-graph/exterior_phase_certificate.py
and all eight exact checks and the empty failure list in the already
saved exterior-phase-transition-replay.json in that same directory,
using the shared JSON inspector. The signs required are upper<0 at
the lower radius, lower>0 at the upper radius, and phase margin
>1/4000; the recorded bounds meet each. No unchanged calculation was
rerun, and its analytic/software qualifications have not been removed.

Also checked L850's contraction: Im beta=(Mv)_2 dt-(Mv)_1 ds,
so d Im beta=-div(Mv) dt wedge ds. This verifies the operator sign
without nonvanishing. A domain with the stated characteristic boundary
would therefore require integral_D sigma=0 for every solution. The
test below excludes only the specified candidate boundaries, not every
way to test that necessary condition.

### All full-form zeros in a narrow transition are isolated

By (2), h_*:=min h=log(200/R)>0. On a fixed smaller compact collar,
beta and its first derivatives are bounded. Write
B_+=h+delta beta and B_-=h-delta beta. For small epsilon both are
at least h_*/2, and R exp(B_+) and R exp(B_-) are at most 1100.
Since 0<=chi<=1, all radii of z_1,z_2 on the two strips lie in
[R,1100]. There are finitely many possible G roots zeta in
R<=|zeta|<=1200, and none has |zeta|=R by (2).

Put theta_zeta=arg zeta modulo 2pi and c_zeta=log(|zeta|/R)>0.
For a z_1 crossing in S_+, t=theta_zeta and m=theta_zeta-delta;
the exact level equation is

\[
 c_\zeta=\chi_\epsilon(\delta)
 B_+(\theta_\zeta-\delta,\delta).
 \tag{6}
\]

Uniformly as epsilon tends to zero, the B factor tends to
h(theta_zeta). For a z_2 crossing the corresponding B_- factor at
m=theta_zeta+delta has the same limit. The sector conclusion of
L848 excludes G(r(theta_zeta) exp(i theta_zeta))=0. Consequently
c_zeta/h(theta_zeta) is never 1. Roots with ratio>1 cannot satisfy
either crossing equation for sufficiently small epsilon. The finitely
many remaining ratios lie strictly in (0,1). Thus there is
0<eta<1/2, independent of epsilon, such that every crossing in S_+
has eta<=chi<=1-eta. If there are no remaining roots the assertion
about crossings is vacuous and the isolation conclusion is immediate.

For epsilon/2<delta<epsilon, direct differentiation of L849(18) gives

\[
 -\chi_\epsilon'
 =2\delta\chi_\epsilon(1-\chi_\epsilon)
 \{(\epsilon^2-\delta^2)^{-2}
       +(\delta^2-\epsilon^2/4)^{-2}\}.
 \tag{7}
\]

At a crossing this is at least 2eta(1-eta) epsilon^(-3).
Choose K bounding both |(B_+)_m-(B_+)_delta| and
|(B_-)_m+(B_-)_delta| on the fixed collar, and put d=eta(1-eta).
At the respective crossings,

\[
 \partial_s u_1
 =\tfrac12\{\chi((B_+)_m-(B_+)_\delta)-\chi' B_+\}
 \ge\tfrac12(dh_*\epsilon^{-3}-K)>0,
 \tag{8}
\]
\[
 \partial_t u_2
 =\tfrac12\{\chi((B_-)_m+(B_-)_\delta)+\chi' B_-\}
 \le\tfrac12(K-dh_*\epsilon^{-3})<0.
 \tag{9}
\]

The last inequalities hold once epsilon is sufficiently small. At
fixed t, (8) makes the radial level crossing locally unique; at fixed
s, (9) does the same for z_2. Hence each G-factor zero on S_+ is
isolated, regardless of its holomorphic multiplicity. At the inner
endpoint L849 gives q>0, hence F!=0; at the outer endpoint (2)
excludes both G zeros. Compactness and isolation make the zero sets
finite, including the endpoints. Since 0<delta<pi/2, z_1=z_2 is
impossible: their angular difference 2delta is not zero modulo 2pi.
Thus F has only finitely many zeros in S_+. Exchange gives the same
conclusion on S_-. Simultaneous zeros of both G factors are allowed;
no claim about the complex Jacobian was used.

### Exact characteristic equations and the absence of midpoint turns

Let J_0 be the real quarter-turn matrix and let T be a tangent in
(t,s) coordinates. A normal is proportional to J_0 T. The matrix
identity adj(A)^T J_0=J_0 A gives

\[
 M^T J_0 T=J_0(P I+Q A)T.
\]

After the constant coordinate change (t,s)=(m+delta,m-delta),
the characteristic condition is therefore exactly

\[
 P\dot m+Q\dot H=0,\qquad
 P\dot\delta+Q\dot V=0.
 \tag{10}
\]

This computation does not divide by F. At a point on a characteristic
curve where F!=0, Q cannot be zero, since otherwise P!=0 and (10)
forces both tangent components to vanish. Put lambda=-P/Q there.
Then D(H,V)(dot m,dot delta)=lambda(dot m,dot delta); hence
|lambda|<=||D(H,V)|| in Euclidean operator norm. In a compact
neighborhood of any point, this norm is bounded by some K_1, so

\[
                         |\dot H|\le K_1|\dot m|.
 \tag{11}
\]

At the finitely many F zeros on a regular closed curve, (11) extends
by continuity. Indeed regularity locally makes the curve injective
(one coordinate has a nonzero derivative), so a finite set of points
cannot contain a curve segment; one may approach from F!=0 points.
In the open transition H_delta=chi' h<0. If dot m=0 at any such
point, (11) gives dot H=0, whence
0=H_m dot m+H_delta dot delta implies dot delta=0. This contradicts
regularity. Thus the midpoint coordinate has no stationary point
on a characteristic curve in the open strip, even at F zeros.

### A cut in the midpoint circle and the strip endpoints

At m=0 the accepted branch satisfies beta(0,delta)=0 for small
delta. Here is the needed check. L848 gives h'(0)=b(0)=0 and
z(0)=200>0. L849's primitive has
A(0,i tau)=-200^(-2)|G(200 exp(i tau))|^2 sin^2 tau real;
therefore J(0,i delta) is purely imaginary. Its scalar branch equation
Im[alpha J]=0 holds at beta=0 since alpha(0)=i. The normalized
equation also holds at delta=0. The uniqueness in the fixed tube
about b from L849(14) identifies this with the accepted branch.

Thus at m=0 the two graph points are conjugate, of common radius
rho=R exp(chi h(0)) in [R,200], and

\[
 F=\frac{4C}{\rho^2}|G(\rho e^{i\delta})|^2\sin^2\delta>0
 \quad(\epsilon/2\le\delta\le\epsilon)
 \tag{12}
\]

for sufficiently small epsilon. To justify strict nonvanishing,
G is strictly positive on the compact positive segment [R,200],
so it is nonzero on a uniform complex neighborhood of that segment;
rho exp(i delta) lies there for all small delta. Consequently
Q=0 and M=P I is invertible on this entire midpoint cut. No
characteristic curve can meet m=0.

A closed curve in S_+ therefore has a single continuous real lift
of m with values in (0,2pi). It has a maximum on its parameter
circle, where dot m=0. Such a point cannot lie in the open strip
by (11). At delta=epsilon/2, q>0 and sigma=0, so L850's identity
det M=|F|^2-Q sigma=|F|^2>0 excludes every characteristic tangent.
At delta=epsilon, the function delta along a curve contained in S_+
has a maximum, so dot delta=0 there. Together with dot m=0 this
again contradicts regularity. These cases exhaust S_+, proving the
claim. Exchange equivariance carries S_- to S_+ and preserves the
characteristic condition, so the same exclusion holds there.

A smooth compact domain has boundary components that are regular
closed curves, giving the stated domain consequence. No step here
excludes a curve that enters the exterior delta>epsilon: it need
not have a delta maximum at a seam crossing. That unresolved case
prevents this bounded calculation from becoming a global flux
obstruction or a range theorem.

## Mathlib

Full matching Mathlib coverage of this actual-G cutoff and
characteristic-loop exclusion was not checked. The isolated-zero,
Cauchy and Stokes inputs are known cited theorems; supporting
formalizations may exist. No full formalization or absence claim is
made. The new proof and the inherited numerical/analytic inputs retain
their stated audit and trusted-software limitations.
