# C468a — Common seam incidence, original pair hits and the forced center trace

## Hypotheses

Retain C467e/audit1017's actual coefficient flow, C467p/audit1049's
original lower connector and auxiliary physical field, and
C467z/C467/audit1083's chamber graph and incidence diagnostic. Thus

\[
n=3,\quad R=1/4,\quad a_0=1/16,\quad T_0=1/1920,\quad
X=1/256,\quad b_*=1/4096,\quad H_*=1/128,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H=H_0+\sum_j\beta(z_j),\quad F=\Delta^2e^{-H},\quad
\Omega=F\bigwedge_j(dz_j/i).
\]

B is the actual conjugation-normalized logarithm of
xi(1/2+sqrt(w))/xi(1/2), H0 is real, beta(0)=beta'(0)=0 and
|beta''|<40 on |z|<R. Keep raw time, the original divisor,
algebraic-square weight and common minus sign. All inherited
L018/L021/L024/C466a finite-zero/product qualifications remain.
The sign interpretation using C467 retains C467u/audit1062's
qualified finite-zero input, including its unreplayed verification
through ordinate100 and first-zero isolation in (14,15). This proof
does not reverify or strengthen that external input.

Let f be any fixed smooth real [0,1]-valued function, one on
[-b_*,b_*] and supported in (-2b_*,2b_*). No evenness is assumed.
Write G(Q)=product_j f(Q_j). Use exactly the closed initial chamber
collar

\[
u=(x-d,x+d,x+h),\quad |x|\le X,\quad 0\le h\le H_*,
\quad 0\le d\le h/4,
\]

and the original pair box |x|<=X, |s|<=1, 0<=h<=H_*. The latter
map is C467p(2), with imaginary coordinates

\[
Q=(m-v,m+v,q),\quad I=2m+q,\quad
v=s\alpha(t,x,h)/2.
\tag{1}
\]

Here alpha is the actual lower gap of the ordered trace from
(x,x,x+h); q is its singleton. Scalars are continuous on their
closed domains, smooth in the regular positive-time interiors, and
satisfy their original undivided real-adjoint equations. Their
initial values are G(u) and f(x)^2f(x+h), respectively. No derivative
at time zero, s=0 or a collision face is assumed. Outer-face values
are not prescribed beyond the nominated initial data and continuity.
The two s endpoints are identified only by the original lower-slot
permutation when imposing the joint match.

## Conclusion

After a common positive time reduction the following statements hold.

**Exact incidence.** At every positive-t,h lower seam there is a
local physical defining function

\[
\rho(t,Q)=v^2-w_0(t,m,q),
\]

with chamber side rho>=0 and positive-s pair side rho<=0. Let p_c
and p_p be the actual chamber and pair graphs, and define, at the
seam,

\[
M_j=1-iD_Qp_j,\quad A_j=F(p_j+iQ)\det M_j,\quad
u_j=-iM_j^{-1}\partial_t p_j,\quad
b_j=-\frac{\operatorname{Re}(A_ju_j)}{\operatorname{Re}A_j},
\quad \mu_j=-\operatorname{Re}A_j>0\quad(j=c,p).
\]
\[
\nu_j=\rho_t+D_Q\rho\,b_j,\qquad
\mu_p\nu_p=\mu_c\nu_c,\qquad
\nu_c=\frac{2\det D_t}{N}\,\mathfrak D(t,x,h).
\tag{2}
\]

D_t is the initial-coefficient derivative of E_t, N>0 is defined
in (8) below, and mathfrak D is C467z(14)'s diagnostic. Thus the
seam has the same glancing set and normal sign for both fields.
Where mathfrak D<0 the chamber feeds the pair; where mathfrak D>0
the pair feeds the chamber. C467's positive-x quadratic glancing
layer applies to both sides. This asserts neither equality of the
normalized velocities nor a rule at a glancing hit. The negative-s
endpoint has the same conclusion after the original permutation.

**Original-domain hits.** Fix 0<epsilon<min(X,H_*). There is
tau_epsilon>0, independent of h and s, such that backward paths
from

\[
0<t\le\tau_\epsilon,\quad |x|\le X-\epsilon,\quad
0<h\le H_*-\epsilon,\quad 0<|s|<1
\tag{3}
\]

first hit an s endpoint before time zero and before any x or h
outer face. Write r_b for their first backward hit time, x_b,h_b
for its original parameters, and v_t=s alpha(t,x,h)/2. For one
finite uniform M,

\[
\frac4{25}e^{-2M}v_t^2\le r_b\le4e^{2M}v_t^2,
\qquad 0<r_b<t.
\tag{4}
\]

Every allowed pair scalar necessarily obeys

\[
\phi(t,x,s,h)=\phi(r_b,x_b,\operatorname{sgn}s,h_b).
\tag{5}
\]

This argument alone does not exclude a tangential first hit; no
continuity of the hit map at glancing is asserted here. The direct characteristic argument stops at
that hit and cannot import an auxiliary time-zero product as a
necessary value. This does not make its endpoint datum independently
free or prove nonuniqueness of the original pair problem.

**Forced center and separated trace.** Let R_p(t,Q) denote C467p's
auxiliary backward time-zero map, used with its original field.
For every allowed pair scalar and the core in (3),

\[
\phi(t,x,0,h)=G(R_p(t,Q(t,x,0,h)))=\phi_p(t,x,0,h).
\tag{6}
\]

The equality extends to h=0 and t=0 by continuity. It is forced
despite the vanishing of the original form on s=0, and does not
force phi_p at s=1. If the endpoint values are identified under
the original permutation, (5) also forces phi(t,x,s,h) to be even
in s on this core; f need not be even in x.

For each fixed eta>0, the chamber trace on
|x|<=X-epsilon, eta<=h<=H_*-epsilon remains C467z's T_c for a
possibly smaller time depending on eta and epsilon. Its backward
paths then stay in the nominated collar, including its d<=h/4
restriction, until time zero.

These are local inputs for the approved joint-selection test, not
a joint construction or an obstruction to every joint selection.
Repeated hits, glancing transmission, smoothness after transmission,
outer-face choices and full common-horizon h=0 continuity remain
unproved. Integrability, cyclic reselection, exterior payment,
realization and Xi transfer are separate. Attempt1088's claims used here are checked in conceptual audit1094 below. No novelty or RH resolution
is claimed.

## Proof

### Coverage and source scope

Use nomination1086/review1087, saved as EXPLORE before this attempt,
at `drafts/literature/2026-11-16-boundary-fed-chamber-pair-nomination-1086.md`.
Its exact target includes actual-domain hits and forced values for
jointly selected adjoints. C468/audit1086 stops the previous fixed
selection, and is a contrast, not a premise for a new stop here.
The earlier smooth-class, fixed-datum and uniform-access stops keep
their original scopes. The sources inspected in review1087 do not
supply this joint selection.

For the local duplicate comparison, C467v's common-side construction
uses strict transversality and a single crossing; it does not cover
this glancing seam. C467w(6)–(7) already records the same pair-field
midpoint invariance, and forces its scalar there by assuming
smoothness at s=0 and extending the normalized equation to that
surface. C467x preserves that known midpoint constraint in a
different pair/triangle selection. Midpoint invariance is therefore
not a new mechanism here. The present target allows only continuity
on the divisor: (4)–(6) instead justify its value by actual endpoint
hits and their time-zero limit. The symmetry check is retained for
the seam permutation and these weaker scalar hypotheses; the earlier
selected-upper-datum obstruction is not used as a new lower obstruction.

Import the already assessed regular ODE tools from Gerald Teschl,
*Ordinary Differential Equations and Dynamical Systems*, April2012
author preliminary version, [Theorems2.5/2.10 pp40–47,
Lemma2.14/Corollary2.15 pp52–53, Theorems3.9/3.12 pp81–84 and
Theorem6.1/proof pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
Their use is confined to C467p/z's verified open physical charts.
The common backward continuation and integrable derivative bounds
are imported from C467p(26)–(34), not inferred from a general
grazing theorem. The application work below is the seam algebra,
original-domain exit and a continuity argument. No general transport
existence theorem is reproved or extended through an unverified divisor.

### The two graphs and their common normal flux

For positive t,h, C467p(12)–(19) gives a smooth inverse from (I,q)
to the initial (c,h), where c=x+h/3. Hence the squared actual lower
half-gap w0=alpha^2/4 is a smooth function of (t,I,q) locally.
It is positive. Both physical graphs are smooth in a neighborhood
of the positive endpoint v=sqrt(w0); the chamber graph here is
C467z's coefficient extension, which agrees with the actual chamber
on its side. The pair graph is exactly the affine interpolation of
the two endpoint momenta with the singleton unchanged. Consequently
p_p=p_c on rho=0. Since partial_v rho=2v is nonzero there,
Hadamard's integral formula in a normal coordinate gives locally

\[
p_p-p_c=\rho a
\tag{7}
\]

with a smooth real vector a. This applies at any positive-t,h seam,
without a uniform bound for a as h tends to zero. On separated
time-zero charts it is also the factorization in C468(10), but no
fixed-h Taylor remainder is used here.

At the seam put n=D_Q rho and W=-i M_c^{-1}a. The determinant
and rank-one inverse identities, applied to M_p=M_c-i a n, give

\[
A_p=A_c(1+nW),\qquad
A_pu_p=A_c\{(1+nW)u_c+W(\rho_t-D_Q\rho\,u_c)\}.
\]

In particular,

\[
A_p(\rho_t-D_Q\rho\,u_p)=A_c(\rho_t-D_Q\rho\,u_c).
\]

Both matrices are invertible by C467p(21) and C467z(8) after a
common time reduction. The value of F is the same on both graphs
at the seam. Taking real parts gives the middle equality in (2).
The strict signs mu_j>0 follow from C467p(24) and C467z(9): at
this seam v>0 and all physical gaps are positive. These are the
full complex densities, not modulus replacements. The common minus
sign changes both signs together and leaves the velocity ratios
unchanged.

### Orientation relative to the original chamber collar

Here are all determinant signs relating rho to the original initial
gap. Let k=(u2-u1)^2=4d^2 and x=c-h/3. The initial coefficient map
near a separated lower double root is

e0(c,h,k)=(3c, 3c^2-h^2/3-k/4,
 c^3-c h^2/3+2h^3/27-(c+2h/3)k/4).

At k=0 its Jacobian in the ordered variables (c,h,k) is h^2/2.
For physical variables (I,q,w), w=v^2, write m=(I-q)/2. Their
coefficient vector is (I,m^2+2mq-w,(m^2-w)q), whose Jacobian
in (I,q,w) is
(q-m)^2-w=(q-Q1)(q-Q2)=Q_t'(q)>0 at the seam.
These formulas are direct differentiation of the displayed cubics.

For clarity define C467p's positive tangential minor completely:

\[
e_c=(3,6c,3c^2-h^2/3),\quad
W_0=(0,-2/3,-2c/3+2h/9),\quad L(q)=(q^2,-q,1),
\]
\[
D_t=D_{e^0}E_t(e^0(c,h,0)),\quad
a_1=(D_te_c)_1,\ b_1=(D_tW_0)_1,\quad
a_2=L(q)D_te_c,\ b_2=L(q)D_tW_0,\quad
N=a_1b_2-b_1a_2>0.
\tag{8}
\]

The simple singleton root formula gives
det partial(I,q)/partial(c,h)=hN/Q_t'(q)>0.
Also det D_t>0 by C467e(21)–(22). Therefore the full Jacobian
of (c,h,k) to (I,q,w) is det(D_t)h^2/(2Q_t'(q)). Taking its
Schur complement against the positive tangential minor yields

\[
\left.\frac{\partial w}{\partial k}\right|_{t,I,q,k=0}
 =\frac{h\det D_t}{2N}>0.
\tag{9}
\]

Thus the recovered initial gap function k(t,Q) and rho have the
same local sign, with dk=[2N/(h det D_t)] d rho on the seam,
including their time differentials. The collar side near d=0 is
k>=0; the pair side has |s|<=1 and therefore rho<=0. C467z(14)
gives the forward chamber derivative
(partial_t+b_c.D_Q)k=4 mathfrak D/h. Inserting (9) proves the
last equality of (2). The sign and glancing assertions follow.

Lower-slot permutation conjugates D_Qp and M, leaves F and the
determinant invariant, and transforms the velocity as a vector.
It changes v to -v and leaves I,q,rho fixed. This proves the
negative-endpoint statement without choosing an extra datum.
No assertion about tangential velocity agreement follows from (2).

### Backward paths must hit an original pair endpoint

Use C467p's auxiliary field solely to locate original-domain hits.
Its backward paths exist to r=0 for every original terminal point;
their original h(r) stays positive. Along them, with
lambda(r)=h(r)+sqrt(r), C467p(26),(31)–(32) imply

\[
\int_0^t C[1+1/\lambda(r)+r/h(r)]\,dr\le M<\infty
\tag{10}
\]

uniformly on a sufficiently small common horizon. These estimates
remain valid in the whole auxiliary cone, including its segment
from v=0 to any given v at fixed I,q. That segment has the same
h and lambda.

The field is equivariant under v to -v, so its v component is odd.
Hadamard's one-variable integral formula consequently gives along
each path

v'=a_v v,    |a_v|<=C[1+1/lambda+r/h].

Indeed the v component is zero at v=0, and its v derivative on
the intervening segment is bounded by C467p(26), after the fixed
linear coordinate change (1). Equation (10) then proves

e^(-M)|v_t|<=|v(r)|<=e^M|v_t|,    sign v(r)=sign v_t.

For the original pair, its available half-width at time r is
alpha(r,c(r),h(r))/2. C467p(8) gives sqrt(r)<=alpha<=5sqrt(r)
on the whole auxiliary initial-parameter box. Thus nonzero v_t
cannot stay inside the original pair down to time zero. Its
auxiliary endpoint has nonzero v, whereas the original width tends
to zero.

It remains to exclude other original faces on the core, rather
than silently using the enlarged box. C467p(29) gives
|c(r)-c(t)|<=Ct and |h(r)^2-h(t)^2|<=Ct. For nonnegative h this
implies |h(r)-h(t)|<=sqrt(Ct), and hence

|x(r)-x(t)|<=Ct+sqrt(Ct)/3.

Choose tau_epsilon so these bounds are smaller than epsilon/2.
Then |x(r)|<X and h(r)<H_* for all the backward path; its lower
h face is excluded by C467p(30)–(31). These assertions hold even
after a hypothetical s exit and so justify, without circularity,
the first-exit argument on the original box.

Continuity and the strict terminal |s|<1 now give a first backward
hit r_b in (0,t), at the endpoint with sign s. There may have been
earlier hits at smaller times in the auxiliary continuation; they
are not used. At this first hit
|v(r_b)|=alpha(r_b,c(r_b),h(r_b))/2. Substituting both bounds for
alpha and both exponential bounds for v proves exactly (4).

Until this hit, the auxiliary path is an actual original pair
characteristic with s nonzero. The original undivided equation is
equivalent there to the physical transport equation, by C467p(22)–(25).
The ordinary chain rule makes the candidate scalar constant on
the open segment. Its permitted continuity gives (5) at the hit.
No scalar value is assigned along the auxiliary continuation beyond
the hit. In particular this argument does not force the product
at that continued endpoint on a noncentral original pair point.

### The center limit is nevertheless forced

Fix t,x,h in the core with t,h positive, and let s tend to zero
from either side. Equation (4) and v_t=s alpha(t,x,h)/2 give
r_b<=25 e^(2M)s^2 t, so r_b tends to zero. The bounded auxiliary
physical velocity gives

|Q(r_b;t,Q_t(s))-R_p(t,Q_t(s))|<=C r_b.

The endpoint map R_p is continuous by C467p(32)–(34). Thus these
hit points tend to R_p(t,Q_t(0)). The central auxiliary path has
v identically zero and stays in the original x,h core margins.
Its time-zero h is strictly positive by C467p(30)–(31). Hence
R_p(t,Q_t(0))=(x_e,x_e,x_e+h_e), with h_e>0. The smooth inverse
singleton chart near time zero and this positive h_e implies
(x_b,h_b) tends to (x_e,h_e).

Uniform continuity of the candidate phi on its closed compact box,
and its prescribed initial value at both endpoints, give

phi(r_b,x_b,sign(s),h_b) -> f(x_e)^2 f(x_e+h_e).

The left side of (5) tends to phi(t,x,0,h). This proves (6), with
no use of a divided equation or derivative at s=0. C467p(33)–(36)
identifies the expression as the old selected center value and
supplies its continuous extension at h=0 and t=0. The candidate
is also continuous there, so the identity extends by limits.

Reflection of the auxiliary paths preserves I,q and their hit
times, and changes only the signs of v,s. Under the stipulated
endpoint permutation the right sides of (5) agree. This proves
the claimed evenness in s, without reflecting x or the bump.

### The separated forced trace remains valid on the smaller collar

Fix positive eta and epsilon with a nonempty stated face range.
The separated coefficient charts in C467z are smooth uniformly
on this compact range. For sufficiently small time their backward
paths keep h(r)>=eta/2 and the strict x and upper-h margins.
C467z(16) gives 0<=k(r)<=12(t-r). Reduce time further to
t<eta^2/192. Then

k(r)<=12t<eta^2/16<=h(r)^2/4.

Since k=4d^2, this is precisely d<h(r)/4 away from the terminal
lower face; the backward paths satisfy the nominated collar
restriction. At earlier positive times k>0. They reach the
time-zero interior without a free outer datum, and the original
equation and continuity give T_c exactly as in C467z. This time
choice depends on eta; it asserts no uniform initial access as
eta tends to zero.

Consequently a joint trace must agree with T_c in these separated
regions and must propagate through the pair according to (5),
with the forced limiting center (6). The positive normal ratio in
(2) removes a possible two-sided incidence conflict, but does not
prove that these requirements have a jointly continuous, interior-
smooth solution across glancing. The values at later chamber inflow
can be linked to earlier chamber outflow by pair paths; they cannot
be declared free independently. No regularity of that return
relation, control of repeated hits or full outer-face construction
has been established here. These are the remaining mathematical
obligations for the unchanged target.

### Independent conceptual audit — 16 November 2026, step1094

This REPRODUCTION audit uses the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-16-joint-glancing-trace-audit-nomination-1092.md`,
separately approved at review1093. It checks the load-bearing incidence,
orientation and original-hit inputs to C468b/c/e, including the domain
qualifications. The regular ODE imports cited above retain their open-chart,
smoothness and compact-continuation hypotheses. C467e/audit1017,
C467p/audit1049 and C467z/C467/audit1083 are used within their verified
boxes; no general glancing theorem is substituted for the following checks.

**Flux and orientation.** At a positive-time, positive-h endpoint the
physical gaps and Re A_c, Re A_p are nonzero. Set n=D_Q rho and
W=-i M_c^{-1}a in (7). Then M_p=M_c(1+W n), so the determinant
factor is 1+nW. Writing U_j=partial_t p_j at fixed physical Q,
we also have U_p=U_c+a rho_t. The
rank-one inverse formula therefore gives exactly the two displayed
identities following (7), and hence

    A_p(rho_t-n.u_p)=A_c(rho_t-n.u_c).

Since rho_t and n are real, its real part is
Re A_p (rho_t+n.b_p)=Re A_c (rho_t+n.b_c).
Multiplication by minus one gives (2) with the positive densities mu_j.
F has the same value on the two graphs at the seam; it has not been
replaced by a modulus. Using w0(t,m,q) or w0(t,I,q) is equivalent
because I=2m+q; partial_v is taken with these other coordinates fixed.

Direct differentiation gives det d(e0)/d(c,h,k)=h^2/2 and
det d(e)/d(I,q,w)=(q-m)^2-w=Q_t'(q)>0. The tangential determinant
is hN/Q_t'(q)>0 by C467p(12)–(17). Their quotient is exactly
h det D_t/(2N), proving (9), with a positive sign. Since k and rho
vanish on the same smooth spacetime seam, their full differentials,
including the time component, have the stated positive ratio there.
C467z's forward derivative is 4D/h (its backward derivative is -4D/h).
Thus X_c rho=2 det D_t D/N. This verifies every sign in (2).
Locally k>0 gives real distinct initial lower roots. At each fixed
h>0 one may shrink further so d<h/4 and the singleton ordering and
outer margins hold. This is a local original-collar assertion, not
an identification of the entire enlarged real-root region with that
collar. Lower-slot permutation preserves rho and conjugates the
matrices and vector fields, so it introduces no additional sign.

**First hits.** C467p(26),(30)–(32) supply a backward auxiliary path
to zero and the integrals 2sqrt(t) and
 t(2sqrt(t/d_*)+t/delta) for 1/lambda and r/h. At fixed (r,I,q),
the segment between v and zero has the same h,lambda and stays in
the cone. Oddness of b_v and the derivative bound therefore justify
the scalar equation v'=a_v v and both exponential comparisons in
(10). Nonzero v never changes sign or tends to zero at time zero.
The original available width is between sqrt(r)/2 and 5sqrt(r)/2,
so a backward endpoint hit must occur at a positive time. At that
hit these comparisons give the lower constant 4/25 and upper
constant 4 in (4). The bounded changes of h^2 and c, and
|h(r)-h(t)|<=sqrt(Ct), keep all x and upper-h faces out of reach
on the fixed-margin core. C467p's outward backward inequality at
h=0 excludes the lower face. These bounds hold before any proposed
exit and on the auxiliary continuation, so the first-exit reasoning
is not circular. Characteristic constancy is used only up to the hit,
where the original scalar is defined and v is nonzero.

**Nonessential consequences also checked.** For fixed t,h>0 and
s tending to zero, (4) gives r_b=O(s^2 t). Bounded velocity and the
continuous auxiliary endpoint map give convergence of the hit to
its central time-zero endpoint. That endpoint has h_e>0 by C467p's
backward collar estimate, so the inverse initial chart is regular
there. Joint continuity and the prescribed initial products, rather
than a divided equation on s=0, give (6). Reflection of the paths
and the stipulated endpoint permutation give evenness in s; they
never reflect x or require even f. For the separated chamber trace,
12t<eta^2/16<=h(r)^2/4 when t<eta^2/192 and h(r)>=eta/2.
Since k=4d^2, this verifies precisely d<h(r)/4. These two consequences
are not needed for C468e's glancing contradiction.

The audited claims pass with their original finite-zero/product and
existential-time qualifications. No uniform boundary derivative, free
inflow, or initial access in the glancing layer has been established.

## Mathlib

Full matching coverage of this actual chamber/pair normal-flux and
original-hit statement is unchecked. Matrix determinant identities,
the chain rule, Gronwall and regular ODE facts are supporting tools,
not a formalization of the joint target. No Mathlib absence claim
is made, and no result here is an all-degree positivity theorem.
