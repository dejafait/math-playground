# Corollary 488f: logarithmic-floor transport through collisions and time zero

## Hypotheses

Use the actual theta heat family H_t of C488a and C488e, normalized by
H_0(z)=xi((1+iz)/2)/8 and F(lambda,z)=8H_(4lambda)(2z). Fix a real
number a and a finite real R>=200, held constant in time. Put T=1/5 and

    w(x)=exp(-sqrt(1+((x-a)/R)^2)),
    eta(x)=1/[1000 log(2+sqrt(x^2+R^2))], p(x)=w(x)eta(x),
    g(x)=40(|x|+R)log(32(|x|+R))/R^2,
    f(x,y)=1_(y!=0)[w(x)|y|+p(x)].

For each t in [0,T], sum over the distinct zeros z=x+iy of H_t with
their multiplicities m_t(z):

    A(t)=sum_(H_t(z)=0) m_t(z) f(Re z,Im z),
    B(t)=sum_(H_t(z)=0) m_t(z) g(Re z) f(Re z,Im z).

These are nonnegative sums, initially allowed to be infinite. This
definition is intrinsic to each slice and requires no global labeling
or global smooth branches. Use the source inputs and scoped local
results specified in the proof. No RH, all-real exterior at t=0, global
simplicity, positive separation, or finite-head restriction on a,R is
assumed.

## Conclusion

Both sums are finite at every t in [0,T]. B is measurable and bounded
on this time interval for each fixed a,R, and

    A(t) <= A(0)+integral_0^t B(u) du,       0<=t<=1/5.       (1)

The integral is a finite nonnegative Lebesgue integral. Thus (1) is
exactly the proposed sum over nonreal zero copies, including all
multiplicities and the endpoints. Bounds here may depend on a,R; no
uniform bound over their unbounded parameter domain is claimed.

This is a reproduction/specialization of the known collision and
endpoint mechanism for C488e's changed statistic. It is not a claimed
advance beyond the checked source mechanisms. The proof is recorded
on 21 November2026, step2123; the separate conceptual audit2125 below
passes under the unchanged hypotheses and cited source inputs.
It supplies neither initial-smallness nor exterior-forcing estimates,
nor all-height reality or L030-L032/C032a mixed positivity. It does
not assert that A is absolutely continuous through its count jumps.

## Proof

### Imported inputs and the scope of the specialization

The entry assessment is
`drafts/literature/2026-11-21-log-floor-integrated-statistic-review-2121.md`,
SPECIALIZE before this attempt. The closest existing proof is
bramble_trace, *An unsigned strip bound for the de Bruijn--Newman
constant*, rStation paper186/v1, 20 November2026,
[Appendix B, (B.1), (B.3), (B.5)-(B.6) and the subsequent collision
and time-zero paragraphs](https://rstation.ai/problems/riemann_hypothesis/papers/186).
C488a reproduces that mechanism with a different floor and scalar
majorant. Its finite-head conclusion and numerical parameters are
not inputs here. The changed floor and rate-weighted integral require
the explicit summability and passage below; that is the reason for
this specialization rather than a direct citation of the conclusion.

Import D. H. J. Polymath, *Effective approximation of heat flow
evolution of the Riemann xi function, and a new upper bound for the
de Bruijn--Newman constant*, Research in the Mathematical Sciences
6 (2019), article31,
[arXiv1904.12438v2, 4 August2019, Proposition3.1(ii), (30) and its
Taylor/Hermite/Rouche proof; Theorems1.5(i)-(ii),3.2](https://arxiv.org/html/1904.12438v2).
The collision theorem applies at every real base time and to real or
nonreal multiple centers. It describes every copy of the local cluster,
not just selected roots. Theorem3.2 is the stated form of N. C. de
Bruijn, *The roots of trigonometric integrals*, Duke Math. J.17 (1950),
197-226, Theorem13. Its original proof and the underlying saddle
estimates of Theorem1.5 are accepted cited inputs, not re-audited here.

The following scoped uses of the established local results are needed.
C488a's strip and (4) hold independently of its finite-head parameters:

    |Im z|<=1,
    #{zero copies with |Re z|<=r} <= N(r)=(r+20)log(4r+40)
                    (r>=0, 0<=t<=T).                       (2)

L058 gives joint entirety and conjugation. L488, with lambda=t/4,
confines all nonreal or multiple H_t zeros to a common compact
rectangle on each [tau,T], tau>0. Its domain is applicable since
0<tau/4<=T/4=1/20<1/8. No confinement at zero is imported.
C488e gives A'(t)<=B(t) at every regular positive time, including its
opposite-paired velocity convention and C488d's absorption through
that result. No unpaired reciprocal sum is introduced here.

### A summable majorant for the full rate trace

Since R>=200, 0<eta(x)<1. By (2), each zero copy contributes at most

    f(x,y)<=2w(x)<=2 exp(|a|/R) exp(-|x|/R).                 (3)

Here sqrt(1+v^2)>=|v| and |x-a|>=|x|-|a| justify the second bound.
The function q log(32q) is increasing for q>=R. Partition the whole
real x-axis by n<=|x|<n+1, n=0,1,2,...; each copy belongs to exactly
one shell, including integer boundary values. Its number of copies
is at most N(n+1). Consequently the B-sum on the n-th shell is at most

    M_n = [80 exp(|a|/R)/R^2] exp(-n/R)
            *(n+1+R)log(32(n+1+R))*(n+21)log(4n+44).       (4)

This bound is uniform in t in the entire closed interval [0,T].
For completeness its ratio is

    M_(n+1)/M_n = exp(-1/R)
       *(n+2+R)/(n+1+R)
       *log(32(n+2+R))/log(32(n+1+R))
       *(n+22)/(n+21)*log(4n+48)/log(4n+44).

Each of the four final ratios tends to1: for the logarithmic ones
use log(v+c)-log v=log(1+c/v)->0 with log v->infinity.
Thus the whole ratio tends to q=exp(-1/R)<1. Taking, for example,
q_*=(1+q)/2<1 gives an integer n_0 with M_(n+1)<=q_*M_n for
n>=n_0. The tail is bounded by M_(n_0)/(1-q_*), and hence

    M:=sum_(n>=0) M_n < infinity,
    sup_(0<=t<=T) B(t)<=M,
    sup_(0<=t<=T) sum_(|x|>=m) g(x)f(x,y)
                         <=sum_(n>=m) M_n ->0              (5)

as integer m tends to infinity. All sums in (5) count multiplicity.
No root labels or interchange of time derivatives is used.

Also g(x)>=g(0)=40 log(32R)/R>0. Dividing the shell bound by g(0)
therefore proves finiteness of A(t) and its uniform tail estimate

    sup_(0<=t<=T) sum_(|x|>=m) f(x,y)
                     <=g(0)^(-1) sum_(n>=m) M_n ->0.        (6)

Although M and g(0)^(-1) need not be small, they are finite for every
fixed admissible a,R. Smallness is not needed for the present claim.

### Cluster limits and finite positive-time events

At a multiple zero z_0 of order m>=2 at real time s, the cited
Proposition3.1(ii) gives, as delta decreases to0, the cluster

    z_0+sqrt(2delta) lambda_l+O(delta)       at s+delta,
    z_0+i sqrt(2delta) lambda_l+O(delta)     at s-delta,      (7)

where lambda_l are the m distinct real roots of He_m; the sign choice
of the square root merely permutes these roots. The source proof gives
uniform convergence of the rescaled analytic functions to a nonzero
multiple of the corresponding Hermite polynomial. Rouche on disjoint
small disks around its simple roots gives exactly one zero, with
multiplicity, in each rescaled disk. A fixed isolating disk around
z_0 contains exactly m zeros for all sufficiently small time changes,
so these disks exhaust its cluster. In particular there are no multiple
zeros in that disk for sufficiently small nonzero real time changes.
This uses the complete source proof, not just the O(delta) notation.

If z_0 is real, the forward disks can be centered on real points and
invariant under conjugation. Their unique zeros are exactly real.
The cluster contributes zero to A and B at s and immediately to its
right. In the backward cluster every nonzero Hermite root gives a
nonreal zero, since its leading imaginary displacement has size
proportional to sqrt(delta), dominating O(delta). If m is odd, the
central disk has a unique root and is conjugation invariant, so that
root is real; if m is even there is no central disk. Writing

    c_m=m for m even, and c_m=m-1 for m odd,

the left limits of this cluster are c_m p(z_0) for A and
c_m g(z_0)p(z_0) for B. Both jumps are downward. Simple real zeros
remain real locally by L058's implicit-function and conjugation
argument and contribute zero on both sides.

If z_0 is nonreal, choose a fixed cluster disk disjoint from the real
axis. All its m copies remain nonreal. As the time approaches s,
every root approaches z_0. Continuity of w,p,g and |y| then gives
continuity of both cluster traces, with multiplicity m at s. Simple
nonreal zeros have the same continuity by their local analytic branch.
There is thus no positive jump at either type of event.

Fix 0<tau<T. In L488's compact spacetime rectangle, the set of points
(s,z) satisfying H_s(z)=partial_z H_s(z)=0 is closed, by joint
continuity. Each slice has finitely many zeros, since H_s is nonzero
entire (H_s(0)>0). Each multiple point is isolated in real spacetime
by (7), including its cluster exhaustion and the isolated zero at s.
An infinite set of such points in the compact rectangle would have
an accumulation point, which would itself be multiple and would
contradict this isolation. There are therefore finitely many multiple
events and hence finitely many event times on [tau,T].

Locally at any slice, choose a larger rectangle with boundary zero-free
at that slice and enclosing the uniform confinement rectangle. Joint
entirety keeps this boundary zero-free for a small time neighborhood.
Rouche then gives a fixed finite set of interior clusters, and all
exterior zeros remain real and simple by confinement. Away from the
event times the interior roots have local analytic branches, so A is
C^1 locally and B is continuous locally. This suffices on each open
event-free interval; no global enumeration is needed. At an event the
finitely many cluster limits above give

    A(s)=A(s+)<=A(s-),                                     (8)

with the applicable one-sided endpoint interpretation. The same
description holds for B, though only its measurability is needed.

### Measurability and integration on positive times

The preceding finite-interval description makes B piecewise continuous
and Borel measurable on every [tau,T]. Exhaust (0,T] by
[T/k,T], k=1,2,... . Its finite assigned value at0 then makes B Borel
measurable on [0,T]. In conjunction with (5),

    0<=integral_0^t B(u)du<=tM<infinity.                    (9)

On a closed subinterval strictly between consecutive event times,
C488e and the ordinary fundamental theorem of calculus give

    A(v)-A(u)<=integral_u^v B(s)ds.

Let u,v tend to the event endpoints. The trace limits exist by the
cluster analysis. Boundedness of B justifies convergence of the
integrals. At every junction (8) adds no positive jump. Starting at
an event uses its right value, and ending at an event can only decrease
the left value. Summing over the finitely many subintervals proves

    A(t)<=A(tau)+integral_tau^t B(u)du,
                         0<tau<=t<=T.                    (10)

This proof never assumes absolute continuity across a jump, nor does
it bound the absolute value of the possibly singular zero velocities.

### The initial slice

Choose arbitrarily large S so that the lines Re z=+-S contain no
H_0 zero; such S exist because (2) gives finitely many zeros in every
bounded horizontal range. The rectangle |Re z|<S, |Im z|<2 has a
zero-free boundary at t=0. Compactness and joint continuity preserve
this property for all sufficiently small nonnegative t. Rouche and
disjoint isolating disks about its finitely many initial zeros preserve
every multiplicity and exhaust its interior zeros.

For an initial nonreal zero, the whole cluster stays away from the
real axis and its A-contribution tends to the initial multiplicity
times f. For an initial simple real zero, conjugation and the implicit
function theorem give a real branch. For an initial multiple real
zero, the forward disks in (7) at s=0 give exclusively real roots for
all sufficiently small positive times. Each of the latter two types
contributes zero, just as at0. There are only finitely many clusters
inside this fixed rectangle, so its total trace tends to the trace
at0.

The exterior trace at t and at0 is uniformly small when S is large,
by (6), for example using m=floor(S). Given epsilon>0, first choose
S with both exterior traces less than epsilon, then let t decrease
to0 for the finite interior. This proves

    lim_(tau down to0) A(tau)=A(0).                        (11)

It uses neither a confinement constant at0 nor a uniform reality
interval for all initial real zeros. By (9),
integral_0^tau B<=tau M->0. Taking tau down to0 in (10) proves (1)
for t>0; at t=0 it is equality. Possible event accumulation at0 causes
no additional passage, because (10) was proved for every tau>0 and
both limits have now been established.

### Separate conceptual audit — 21 November2026, step2125

The exact finite-integral assertion passes the audit approved by
`drafts/literature/2026-11-21-log-floor-integrated-audit-review-2123.md`
(SPECIALIZE, separate approval2124). This verifies a local specialization
of the checked mechanisms; it is not a new theorem beyond those
mechanisms or a verification of the primary sources' entire proofs.
No load-bearing defect, altered hypothesis or new mathematical input
was found. The argument and its direct local inputs are unchanged.

**Input scope.** C488a's count proof uses the actual kernel, its positive
value at zero, the strip, and 0<=t<=1/5. Its Jensen radius is arbitrary;
none of V,X,U,a,R from its later finite-head conclusion enters that
proof. It counts every copy, including boundary copies, at every slice.
The strip is independently imported from the initial xi strip and de
Bruijn's Theorem13 in Polymath's Theorem3.2 formulation. It does not use
the finite-height verification or assume reality of the tail at zero.
C488e supplies precisely the present w,p and all fixed real a,R>=200
at regular positive times. Its stronger rate26 is unnecessary here;
only rate40 is retained. The nearby-count input C488d enters through
C488e and is not a further direct input to this passage.

L488 applies with lambda in [tau/4,T/4] and spatial variable z/2:
F(lambda,z/2)=8H_(4lambda)(z). Multiplicity is preserved. Its tail
excludes multiple real zeros as well as nonreal zeros, so it confines
the entire multiple-point set, not just the contributing zeros.
L058 gives joint holomorphy and H_s(0)>0; hence no slice is identically
zero. The Hermite cluster theorem is imported with both time directions
and Rouche exhaustion, as specified above. No global zero labeling or
uniform cluster-dependent constant is required.

**Full series and parameter endpoints.** On shell n<=|x|<n+1, (2)
bounds its multiplicity by (n+21)log(4n+44). Equation(3) bounds each
copy by 2exp(|a|/R)exp(-n/R). Monotonicity of q log(32q) for q>=R
bounds the rate by 40(n+1+R)log(32(n+1+R))/R^2. Their product is
exactly M_n in(4). Thus there is neither an omitted second half-axis
nor an extra multiplicity factor. All four ratios displayed after(4)
tend to1, giving limiting ratio exp(-1/R)<1. For the stated finite
R this yields a finite geometric majorant after some n_0; no onset
uniform in R is needed. It includes R=200 and arbitrary fixed a.

The minimum of g is 40log(32R)/R>0. Consequently the same positive
series gives both uniform tails (5)-(6), on the entire closed time
interval. These are bounds for complete series, not sampled sums.
They do not assert that M is small, that g is globally bounded, or
that a finite scalar multiple of A controls B. The extra rate factor
has actually been summed. This is the needed distinction between
finite traces at individual positive times and a finite time integral.

**Clusters and event compactness.** For each selected multiple point,
choose disjoint disks around every root of the rescaled Hermite
polynomial. Its simple roots give a strict Rouche comparison for all
sufficiently small positive increments in the specified direction.
Each rescaled disk has exactly one copy; the fixed isolating disk has
m copies, so no additional nearby multiple zero is possible. This
holds in both time directions. At a real center the forward disks
are conjugation invariant, making their unique roots exactly real.
Backward nonzero Hermite roots give nonzero imaginary displacements
of order sqrt(delta), larger than the O(delta) error. If m is odd,
the sole central disk is conjugation invariant and its unique root
is exactly real. Thus the left count is c_m=m or m-1, respectively;
the lost mass is c_m p(z_0), or c_m g(z_0)p(z_0) for B. At s itself
the real zero contributes zero even when its multiplicity is m.

For a nonreal center, its disk stays off the real axis, and continuity
of each summand gives the multiplicity-weighted value at s from both
sides. Simple real roots cannot create a positive jump, by conjugation
and local uniqueness. These checks justify the right values and all
one-sided limits in(8), including at positive interval endpoints.

The common confinement rectangle times [tau,T] is compact. The equations
H_s(z)=partial_z H_s(z)=0 define a closed subset there. Cluster
exhaustion isolates each of its points in real spacetime; at time s
itself ordinary isolation of zeros also applies. An infinite closed
subset of this compact set would accumulate at one of its own points,
contradicting that isolation. Hence all positive-time multiple events
are finite on [tau,T]. This argument would fail with confinement only
of nonreal zeros; L488 supplies the stronger input actually used.

**Measurability, integration and zero time.** A larger zero-free-boundary
rectangle at each slice encloses the confinement rectangle. Joint
continuity preserves its boundary and Rouche preserves its finite
interior multiplicity locally. Off event times all these roots have
simple local branches; their real/nonreal status stays fixed locally.
Thus A is locally C^1 and B continuous there. Although g has |x|,
only its continuity is used. The finitely many event values on each
[tau,T], together with their established limits, make B Borel there.
The countable cover [T/k,T] and its assigned finite value at0 give
measurability on [0,T]. Bound(5) then gives integral_0^t B<=tM.

Integrate C488e on closed intervals strictly between successive events.
As their endpoints approach the events, boundedness by M gives
convergence of the integrals. Joining intervals adds A(s)-A(s-)<=0;
starting at s uses A(s)=A(s+). These two facts, also at tau and T,
give(10) without an absolute-continuity assumption or a bound on
the absolute derivative near a collision.

At zero choose vertical sides +-S avoiding all initial zero abscissae;
there are arbitrarily large such S by the locally finite count. The
horizontal sides at heights +-2 are outside the strip. The resulting
compact zero-free boundary persists, and finitely many disjoint initial
cluster disks exhaust its interior by Rouche. Each nonreal cluster
has its correct continuous multiplicity trace. Every real cluster,
simple or multiple, has zero trace for all sufficiently small forward
times, with the neighborhood allowed to depend on this finite set.
The interior trace therefore converges. Equation(6) bounds the absolute
error from the two exterior traces by twice a tail tending to zero.
First choose S, then let time tend to zero: this proves(11), without
interchanging an uncontrolled infinite sum with the limit. Finally
integral_0^tau B<=tau M tends to zero, so(10) yields(1). Accumulation
of events at zero is allowed and does not enter this limit argument.

This completes the audit for every fixed real a and finite R>=200,
with all copies and both endpoints. Initial smallness, exterior forcing,
all-height reality and actual-Xi all-degree signs remain unproved.
No numerical check or new mathematical script was used. Full matching
Mathlib coverage remains unchecked, as qualified below.

## Mathlib

Full matching coverage has not been checked; no absence claim is made.
No Mathlib theorem is invoked for the actual heat-family confinement,
zero count, collision theorem or C488e's transport inequality.
Supporting mathematics is Rouche's theorem, the holomorphic implicit
function theorem, compactness, convergence of a positive series by the
ratio test, Borel measurability of piecewise continuous functions, and
integration on intervals. The cited primary analytic inputs retain
their stated qualifications. No numerical certificate or mathematical
script is needed for this proof.
