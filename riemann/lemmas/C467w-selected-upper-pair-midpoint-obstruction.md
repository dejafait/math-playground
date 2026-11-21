# C467w — The selected upper outer datum fails the forced pair midpoint

## Hypotheses

Retain C467e/audit1017's actual coefficient flow, C467k/audit1033's
incident-pair maps, C467p/audit1049's positive-h physical graph and
backward-flow estimates, and C467v/audit1066's fixed selection. In
particular,

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,\quad
X=1/256,\quad b_*=1/4096,\quad H_*=1/128,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H=H_0+\sum_{j=1}^3\beta(z_j),\quad F=\Delta^2e^{-H},\quad
\Omega=F\bigwedge_{j=1}^3(dz_j/i).
\tag{1}
\]

B is the actual conjugation-normalized logarithm of
xi(1/2+sqrt(w))/xi(1/2); H0 is real and |beta''|<40 on the original
disk. Keep the raw time, original divisor and common minus sign.
The fixed smooth real bump satisfies 0<=f<=1, f=1 on [-b_*,b_*],
and supp f contained in (-2b_*,2b_*). No evenness, monotonicity or
nonzero derivative at the end of its plateau is assumed.

The upper pair is C467k's j=1 row: paired ranks (2,3), singleton
rank 1, slot order (1,3,2), sign -1, h<0, s=1-2lambda. Its actual
initial product is f(x)^2 f(x+h). Let q1<q2<q3 be the triple roots
from initial (x,x,x), and y=E1(t,x)/3 with inverse x=x(t,y).
Let g1 be exactly C467v(23), with its already fixed chi, delta and W.

Consider a real phi on
[0,tau] x [-X,X] x [-1,1] x [-H_*,0], for some tau>0, continuous
on this box and smooth for t>0,h<0, including s=0 and the stated
fixed-endpoint neighborhood extensions, with

\[
\phi(0,x,s,h)=f(x)^2f(x+h),\qquad
d\phi\wedge\operatorname{Re}(-Z_-^*\Omega)=0,
\]
\[
\phi(t,x,s,0)=g1\left(t,E1(t,x)/3,(1-s)/2\right).
\tag{2}
\]

All inherited actual-background qualifications are retained. In
particular C467v's construction carries L018/L021/L024/C466a's
qualified finite-zero and first-zero inputs, unreplayed here. The
argument below uses only the displayed graph/flow properties and the
fixed datum's value away from its collar; it makes no new zero claim.

## Conclusion

There is no phi satisfying (2) on any positive common time interval.
Consequently the nominated lift with range [0,1], four separate complex
L1 derivative products and the complete independent-cutoff identity
does not exist for this fixed g1. The contradiction already holds in
the weaker class (2); no integrability hypothesis is discarded from
an asserted existence result.

The necessary trace is at s=0, not at a triangle vertex. For y in a
fixed small neighborhood of the right end of the bump's plateau there
are continuous endpoint functions a(t,y), b(t,y), with

\[
\phi(t,x(t,y),0,0)=f(a(t,y))^2 f(b(t,y)),
\]
\[
a(t,y)=y+\frac{\sqrt6}{2}\sqrt t+O(t),\qquad
b(t,y)=y-\sqrt6\sqrt t+O(t),
\tag{3}
\]

for every test obeying the initial data and equation in (2), irrespective
of its free side values. The constants in (3) are uniform in that mean
neighborhood. At arbitrarily small positive times (3) conflicts with
the fixed g1 at s=0.

This is attempt1068's local obstruction, validated by independent
conceptual audit1070 below under the retained input qualifications. It stops
the fixed C467v(23) lift only. It does not invalidate C467v's two-triangle
construction, exclude a different joint choice of upper data, or settle
other interfaces, exterior payment, realization, all-degree positivity
or Xi transfer. It is neither an RH disproof nor a complete RH candidate.

## Proof

### Coverage, actual symmetry and the tools used

The prior EXPLORE assessment is
`drafts/literature/2026-11-16-selected-upper-pair-lift-nomination-1066.md`,
separately completed by review1067. This is its prescribed-data
compatibility test. The inspected literature supplied ordinary
characteristics, not this necessary midpoint value. C467s's reflected
construction remains unaudited and is not an input. Stops1058/1060
concern other selections and are contrasts, not premises.

Reuse Gerald Teschl, *Ordinary Differential Equations and Dynamical
Systems*, author-hosted April2012 preliminary version,
[Theorem2.5/proof pp40–41, Theorem2.10/proof pp45–47,
Lemma2.14/Corollary2.15 pp52–53,
Theorems3.9/3.12 pp81–84, Theorem6.1/proof pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
These are the already assessed smooth ODE existence, uniqueness,
dependence, variation and continuation tools. Apply them only on the
positive-time physical charts or at positive initial separation.
C467p supplies the estimates near the degenerating boundary. No weak
trace theorem, singular uniqueness theorem or Stokes limit is needed
to contradict the weaker class (2).

For completeness the negative-h specialization is exact. The raw equation
is

\[
Y_j'=2\sum_{k\ne j}\frac{Y_j-Y_k}{|Y_j-Y_k|^2}
                       -\overline{g(Y_j)},\qquad Y(0,u)=iu.
\tag{4}
\]

Because g(conj z)=conj g(z), conjugation transforms (4) into the same
equation with initial -iu. Uniqueness for distinct initial data and
C467k's ordered coefficient limits therefore give its actual conjugate
pair and triple maps. If C is componentwise conjugation and P23 exchanges
target slots 2 and 3, the specified upper connector satisfies

\[
Z_-(t,x,s,h)=P23\,C Z_+(t,-x,-s,-h).
\tag{5}
\]

The sign change of s restores the order inside the conjugated pair;
P23 places its singleton in slot 2, as required by j=1. In dimension
three C*Omega=-conj(Omega), while symmetry of F gives P23*Omega=-Omega.
Thus (P23 C)*Omega=conj(Omega). The common minus sign is unchanged.
The real adjoint in (2) consequently transforms exactly into the
positive-h adjoint for
phi_+(t,x,s,h)=phi(t,-x,-s,-h), with bump fsharp(u)=f(-u).
Initial data, smoothness and continuity transform as stated, without
assuming f even. The following positive-h argument can therefore be
transported back by (5).

### A forced characteristic on the midpoint despite the divisor

Use C467p(11)–(26)'s physical coordinates and its exact graph:

\[
Q=((I-q)/2-v,(I-q)/2+v,q),\qquad v=s\alpha/2,
\]
\[
p=(M_0-\eta v,M_0+\eta v,P(q)),\quad
M_0=(J-P(q))/2,\quad \eta=-\Pi_2-q\Pi_3,
\]
\[
M=\mathrm{Id}-iD_Qp,\quad u=-iM^{-1}p_t,\quad
\widehat\kappa=(F/v^2)\det M,\qquad
b=-\frac{\operatorname{Re}(\widehat\kappa u)}
          {\operatorname{Re}\widehat\kappa}.
\tag{6}
\]

Here q is the positive-h singleton, alpha its paired root gap, and
the coefficients are evaluated using C467p's inverse (I,q) chart.
The explicit smooth factor F/v^2 is C467p(23); the original form is
not replaced. Its real-part floor (24) holds also at v=0. At fixed
t>0,h>0 the (x,s,h)->Q map has nonsingular Jacobian: the (c,h)->(I,q)
Jacobian is hN/Q'(q)>0 by C467p(14), and v_s=alpha/2>0. Thus any
smooth parameter test has a smooth expression Phi(t,Q) near v=0.

Off v=0 the exact wedge calculation in C467p gives

\[
\Phi_t+b\cdot D_Q\Phi=0.
\tag{7}
\]

Every coefficient of (7) is continuous at v=0 for positive t,h,
and Phi is smooth there. Taking v->0 in (7) proves (7) at the
midpoint as well. This uses smoothness at positive separation and
time only. It neither divides the original equation on its divisor
as an independent assumption nor imposes a derivative at t=0 or h=0.

Let S exchange Q1 and Q2. The graph in (6) obeys p(SQ)=S p(Q),
since I,q are unchanged and v changes sign. Differentiation gives
M(SQ)=S M(Q) S and u(SQ)=S u(Q). Symmetry of F, invariance of v^2
and invariance of det M show widehat kappa(SQ)=widehat kappa(Q),
including v=0 by its smooth factorization. Hence b(SQ)=S b(Q).
At v=0 its first two components coincide, so b_v=0. Smooth ODE
uniqueness makes v=0 an invariant physical characteristic surface.

Most nonzero-v backward paths need not remain in the original s range;
they cannot be used to force arbitrary traces from the original initial
product. The midpoint has s=0 identically, and avoids that problem.

### These midpoint paths stay in the original parameter box

Fix a compact mean neighborhood strictly inside (-X,X); later it is
chosen around the negative of the positive plateau endpoint when using
the reflected lower pair. Start at time t>0, s=0, with original
0<h0<=sqrt(t), and with c0=x+h0/3 in that neighborhood. Restrict t
once, uniformly over the neighborhood. C467p(29)–(32) construct the
backward physical path and give, with r its running physical time,

\[
|c(r)-c0|\le Ct,\qquad h(r)^2\le h0^2+Ct,
\qquad h(r)^2\ge h0^2+d_*(t-r).
\tag{8}
\]

For the last bound choose t so (h0^2+Ct)^(1/2) is less than the fixed
collar delta in C467p(30); then the whole path is in that collar.
The constants in this paragraph are those of the audited physical
graph, and are independent of h0 and the terminal point.

Take the mean neighborhood with a fixed margin from +-X. Since
x(r)=c(r)-h(r)/3, the first two bounds of (8) imply |x(r)|<X and
h(r)<H_* after one further common time reduction. The midpoint
invariance gives s(r)=0, strictly inside [-1,1]. Thus these paths
remain in the ORIGINAL pair box, not just the auxiliary cone, for
0<r<=t. The last bound gives h(0)>=sqrt(d_*t)>0. At r=0 the
simple singleton inverse chart is smooth, c,h have limits, and
the path reaches the original initial surface at (x0,0,h_init).

Equation (7) makes Phi constant on each positive-time segment.
Continuity of the original parameter test, with s identically zero,
therefore forces its value to be fsharp(x0)^2 fsharp(x0+h_init)
in the reflected positive-h coordinates. No side values can alter
this equality. Reflection gives the corresponding original upper
product f(a)^2 f(b), where b<a are its time-zero singleton and
repeated coordinates. The lower h0>0 limit used here corresponds
to upper h=-h0<0, with all upper paths likewise inside the original
box by the same reflection.

### Endpoint continuity and the upper h=0 limit

C467p(32) and its variational argument give |D_Q R0|<=C for the
physical time-zero endpoint R0(t,Q), uniformly up to the one-sided
h=0 graph. Bounded velocity gives |R0(t,Q)-Q|<=Ct. On the interior,
flow composition also gives partial_t R0=-D_Q R0 b, so this time
derivative is bounded. These are estimates for R0 itself, independent
of the bump used to evaluate it.

At fixed positive time the h=0 boundary is the smooth graph
q=q0(t,I), with bounded I derivative, as checked in C467p(14) and
its boundary-continuity proof. Nearby interior points can be joined
within its epigraph by paths of length at most a fixed multiple of
their distance; the cone and other faces have strict margins. Applying
the bounded derivatives to each component of R0 gives a unique
continuous extension. On compact positive-time intervals the same
argument in spacetime applies because that graph is smooth in time.
Thus the endpoint limit at h=0 is continuous in t and I. This is the
same extension argument as C467p, applied to R0 rather than to G(R0).

For midpoint points every endpoint has equal paired coordinates,
by the established v=0 invariance. Taking h0 down to zero preserves
this equality. The parameter test is continuous at h=0, so its forced
product passes to that boundary. No normalized equation is imposed
there. The uniform positive h_init bound in (8) also shows that the
limiting time-zero endpoint at each fixed t>0 has strictly separated
singleton and repeated coordinate.

Transport this endpoint by the actual reflection (5), including P23.
At upper h=0,s=0 the terminal imaginary coordinates are

\[
Q_T=\left(\frac{q2+q3}{2},q1,\frac{q2+q3}{2}\right).
\tag{9}
\]

Consequently its initial endpoint (a,b,a) satisfies

\[
\left|a-\frac{q2+q3}{2}\right|+|b-q1|\le Ct.
\tag{10}
\]

These functions are continuous for positive t,y by the endpoint
extension. C467v(9)'s factored triple roots give
q1=y-sqrt(6t)+O(t^(3/2)), uniformly on the compact mean neighborhood;
the identity q1+q2+q3=3y gives the paired midpoint. Together with
(10) this proves (3), including a,b->y as t->0. The inverse
x(t,y) stays strictly inside the original x interval. Hence the
forced trace in (3) applies at exactly the mean used by g1, not at
an initial-coordinate substitute for that mean.

### The fixed plateau contradicts the selected midpoint datum

Define the right endpoint of the connected unit plateau by

\[
\rho=\sup\{r\ge b_*: f(u)=1\text{ for every }0\le u\le r\}.
\tag{11}
\]

Compact support and continuity give b_*<=rho<2b_*, f=1 on [0,rho],
and points with f<1 arbitrarily close to the right of rho. In
particular rho lies strictly inside the mean interval used above.
At y=rho, (3) gives, for every sufficiently small positive t,

\[
a(t,rho)>rho,\qquad 0<b(t,rho)<rho.
\tag{12}
\]

The continuous function a(t,rho), extended by a(0,rho)=rho,
takes every value between rho and a(T,rho) on [0,T], for each
sufficiently small T>0. Choose z in that open interval with f(z)<1;
such a z exists by (11). The intermediate value theorem gives
t in (0,T) with a(t,rho)=z. Since f(b(t,rho))=1, the forced value
at this t is

\[
\phi(t,x(t,rho),0,0)=f(z)^2<1.
\tag{13}
\]

On the other hand s=0 means lambda=z_angle=1/2. C467v(23)'s cutoff
is zero there for all sufficiently small t, since chi is zero on
[2/3,infinity) and (1/2)/(delta t^(3/2)) tends to infinity. The
prescribed value is therefore exactly

\[
g1(t,rho,1/2)=f(rho)^3=1.
\tag{14}
\]

Equations (13) and (14) contradict (2). T could be chosen below any
proposed positive common horizon, so shrinking that horizon cannot
remove the contradiction. No monotone transition or quantitative
lower bound on 1-f(z) was needed; even an infinitely flat plateau
endpoint gives the strict inequality at some arbitrarily small time.

This necessary-value contradiction completes the bounded test. The
four complex-product bounds and independent-cutoff identity cannot
repair incompatible initial and midpoint data. No separate failure
of those estimates, and no failure of the broader joint-selection
class, is asserted. The separate conceptual audit1070 below checks
normalization at v=0, original-domain confinement and the endpoint limit.

### Independent conceptual audit — 16 November 2026, step1070

This REPRODUCTION audit uses exactly the SPECIALIZE target in
`drafts/literature/2026-11-16-selected-upper-pair-midpoint-audit-nomination-1068.md`,
separately approved by review1069. C467e/audit1017, C467k/audit1033,
C467p/audit1049 and C467v/audit1066 are retained with all their input
qualifications. The finite-zero inputs remain unreplayed. C467s is
not imported; stops1058/1060 are not nonexistence premises here.

Import Teschl's cited Theorem2.5 for existence and uniqueness on regular
open charts, Theorem2.10 for smooth dependence and variations, and
Lemma2.14/Corollary2.15 for compact continuation. Time augmentation is
covered in Theorem2.10's proof and Theorem6.1. C467p(32)'s variational
estimate uses the Gronwall inequality of Lemma2.7 pp42–43 and (3.87)
p82. None of these tools alone asserts a singular-boundary limit.
The following is an audit of their necessary-class specialization,
not a reproof of those standard results.

**Actual reflection.** Conjugating (4) gives the same vector field
with initial -iu. Distinct-data uniqueness and C467k's ordered
coefficient limits therefore identify the actual conjugate pair.
If the positive-h values are Y1,Y2,Y3 in imaginary order, the upper
values are conjugate(Y3), conjugate(Y2), conjugate(Y1). Substituting
-s in the lower connector and exchanging slots 2,3 places the upper
pair in slots 1,3, with its lower member first at s=1, and singleton
in slot 2. This is exactly C467k's j=1 row. Since H0 is real and beta
commutes with conjugation, F does also. Each pulled-back dz/i is
minus its conjugate, giving C*Omega=-conjugate(Omega) in dimension
three. The odd permutation gives P23*Omega=-Omega. Their composition
thus gives (5), preserving the real zero equation and common minus
normalization. The transformed bump is fsharp(u)=f(-u), with initial
product fsharp(x)^2 fsharp(x+h); no evenness is used.

**Necessary equation at the divisor.** At positive t,h the spatial
chart determinant is hN/Q'(q) times alpha/2 times a fixed nonzero
linear-coordinate determinant. Hence Phi is smooth near v=0. In
physical coordinates the exact differential calculation is

    dZ/i = M(dQ + u dt),
    dPhi wedge Re(-Omega)
      = -v^2 [Re(widehat kappa) Phi_t
                - Re(widehat kappa u) dot D_Q Phi] dt wedge dQ.

In the second line dQ denotes dQ1 wedge dQ2 wedge dQ3; all forms
are evaluated on the original graph. This proves necessity as well
as sufficiency of (7) for v!=0, with its stated minus sign. The two
singleton gaps have imaginary parts at least ell/5, so there is no
other divisor in this cone. C467p(23) gives the smooth nonzero factor
F/v^2, and (24) its real-part floor after multiplication by det M.
Thus the smooth punctured equation tends to (7) at v=0. No equation
is imposed by division at t=0 or h=0.

For the pair exchange S, differentiation of p(SQ)=S p(Q) gives
D p(SQ)=S D p(Q) S and p_t(SQ)=S p_t(Q). Consequently det M and
widehat kappa are invariant, while u and b are equivariant. Thus
b1=b2 on Q1=Q2. The restricted smooth ODE there solves the full
ODE, and uniqueness keeps the backward path on v=0. For every
positive running time and h this is s=0 since alpha>0. This does
not assert confinement for non-midpoint paths.

**Original-box confinement.** Choose a compact mean interval around
rho in (11), strictly inside (-X,X), and a slightly larger such
interval containing its small perturbations. Smooth coefficient
dependence gives E1=3x+O(t), E1_x=3+O(t), so x(t,y)=y+O(t)
uniformly there. Approach the upper boundary with this fixed x,
s=0 and h=-h0, 0<h0<=sqrt(t). The reflected terminal mean is
c0=-x(t,y)+h0/3 and has a uniform margin inside (-X,X).

C467p(29) on its constructed backward domain gives
|c(r)-c0|<=Ct and h(r)^2<=h0^2+Ct. Choose the common time so
(1+C)t<delta^2 and sqrt(t)<delta for its fixed collar delta.
Then the whole trajectory stays in that collar, and integration
of C467p(30) gives h(r)^2>=h0^2+d_*(t-r) on the entire interval.
Furthermore

    |x(r)-c0| <= Ct + sqrt((1+C)t)/3.

Reduce time so this is smaller than the mean margin and
sqrt((1+C)t)<H_*. This proves confinement to the ORIGINAL x,h
intervals; s=0 already stays in its original interval. At time zero,
c,h have limits, and h(0)>=sqrt(d_*t)>0. The limiting x,h stay
strictly inside their original intervals. The s parameter is zero
all along, so continuity of the test reaches exactly its prescribed
initial product despite the collapsed initial pair map. Integrate
(7) on [epsilon,t] and take epsilon down to zero. Free side data
cannot change this value. Reflection gives the endpoint (a,b,a)
with b<a in the upper coordinates.

**Componentwise endpoint extension.** The smooth backward variational
equation and C467p(32) give |D_Q R0|<=C independently of h0. The
terminal neighborhoods needed for differentiation have the strict
margins of C467p(30a). Flow composition, applied componentwise, gives

    (partial_t + b dot D_Q) R0 = 0,
    |partial_t R0| <= C,       |R0(t,Q)-Q| <= Ct.

The endpoint is constant along the same trajectory, giving the first
identity; the other two follow from |b|<=C and the variational bound.
These are properties of R0 itself, independent of the scalar G(R0).

At fixed positive time, near a midpoint boundary point, the domain
in the linear coordinates (I,q,v) is q>q0(t,I), with the other faces
strictly separated. The graph has bounded I derivative. Connect two
nearby interior points by raising q above the intervening graph,
moving I and v, then lowering q. The extra height is bounded by a
fixed multiple of the I displacement, so the path length is bounded
by a constant times the distance of its endpoints. Integration of
the bounded derivative of each component of R0 along these paths
gives a unique locally Lipschitz extension to the boundary. On a
compact positive-time interval the graph is smooth in (t,I); the
same spacetime construction also uses the bounded partial_t R0 and
proves joint continuity. The local path constant may depend on that
time interval. No uniform bound on q0_t at time zero is needed.

Thus the h0 down to zero midpoint limit exists. Equality of its
paired endpoint coordinates persists, as does the positive initial
separation, by the bound already proved. Continuity of the original
test transfers its forced product to h=0. C467k's actual incident
map gives exactly the terminal coordinates (9). C467v(9)'s factored
roots imply q1=y-sqrt(6t)+O(t^(3/2)) uniformly on the chosen mean
interval; sum qj=3y determines the paired midpoint. The endpoint
displacement therefore proves (3) at the exact mean y used by g1.
It also proves a,b -> y uniformly as t tends to zero. This last
continuity follows directly from the displacement and root estimates,
not by extending a positive-time epigraph estimate to time zero.

**Plateau and time quantifiers.** The set in (11) is nonempty,
downward closed within [b_*,infinity), and bounded. Compact support
and continuity give b_*<=rho<2b_* and f=1 on [0,rho]. Every right
neighborhood of rho contains a point with f<1; otherwise the unit
interval would extend farther. Later disconnected plateaus or
infinite flatness at rho do not change this fact. The leading
sqrt(t) terms in (3) dominate the uniform O(t) errors, proving (12)
for every sufficiently small positive t. For any smaller positive T,
continuity of a on [0,T] attains every value strictly between rho
and a(T,rho) at a time in (0,T). Choose such a value z with f(z)<1.
Then the singleton stays in (0,rho), where f=1, and 0<=f(z)<1
gives the strict inequality (13).

At the same actual mean rho the prescribed g1 has angle 1/2. Its
cutoff vanishes whenever delta t^(3/2)<=3/4, giving exactly 1,
not merely 1+O(sqrt(t)). This contradicts (13) at arbitrarily small
positive times. Every reduction of time uses fixed constants and
strict margins, so T can be chosen below any proposed positive
common horizon. No derivative of f at rho is used.

All five nominated audit obligations pass. This validates the existing
obstruction for fixed C467v(23), with no new lemma, mathematical script
or originality claim. The four complex products and full cutoff
identity cannot repair nonexistence in the weaker class (2).
C467v's two-triangle result remains valid. C467e, C467k, C467p and
C467v remain the direct mathematical uses; the DAG row is unchanged.
Other joint selections, chamber and other interface matching, exterior
payment, realization, all degrees and Xi transfer remain unresolved.
This is not a complete RH candidate.

## Mathlib

Full matching coverage for this actual pair trace obstruction has not
been checked. The already assessed primary ODE results above are the
analytic imports; smooth characteristic constancy, elementary symmetry
and the real intermediate value theorem support the specialization.
No matching Mathlib theorem or absence claim is asserted, and no
formal verification is claimed. The informal specialization is checked
by the independent conceptual audit1070 above.
