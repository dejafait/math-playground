# L814: normalized Pólya pencil — elimination and an unpaid sign

## Hypotheses

Let K be the actual theta kernel of L019 and F(z)=Xi(z) its cosine
transform, as in L020. Put

    Q(u)=8pi [2pi cosh(9u/2)-3 cosh(5u/2)] exp(-2pi cosh(2u)),
    S(z)=integral_0^infinity Q(u) cos(zu) du,
    c=F(0)/S(0), B(u)=c Q(u), G(z)=c S(z),
    d(u)=K(u)-B(u), D(z)=F(z)-G(z),
    h_tau(u)=(1-tau)B(u)+tau K(u), H_tau(z)=G(z)+tau D(z).

The definition of S is Pólya's corrected xi**: G. Pólya,
*Bemerkung über die Integraldarstellung der Riemannschen xi-Funktion*,
Acta Math. **48** (1926), 305–317, final correction on printed p.317,
[primary paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5376-11511_2007_Article_BF02565336.pdf),
DOI 10.1007/BF02565336. G. Gasper, *Using sums of squares to prove
that certain entire functions have only real zeros*,
[arXiv:0801.2996v1](https://arxiv.org/pdf/0801.2996v1), Section 3,
(3.5), printed p.6, records the same kernel and frequency.
Only this definition is imported. No all-real-zero assertion for S is used.

The collision test concerns real 0<x<=40 and 0<tau<1. A nondegenerate
event here means H_tau(x)=H_tau'(x)=0, D(x)!=0 and H_tau''(x)!=0.
Primes denote differentiation in x, not tau.

## Conclusion

The normalization is legitimate, c>1, and all derivative integrals used
below converge locally uniformly. The normalized kernels have equal mass;
d has zero integral, is strictly negative for all sufficiently large u,
and is positive somewhere. For each fixed interior tau, d/h_tau is bounded
and is not a nondecreasing function of u.

The nondegenerate events in the box are exactly the points satisfying

    F(x)G(x)<0, W(x)=0, W'(x)!=0,
    W=F G'-G F', tau=G(x)/(G(x)-F(x)).

At such an event, the exact requested product is

    D(x) H_tau''(x)=W'(x)=F(x)G''(x)-G(x)F''(x).

The elementary forward-heat test below leaves an unpaid relative
oscillatory remainder. Neither W'<=0 at events nor an actual opposite-sign
event is established. These are diagnostic identities and a narrow
kernel-order obstruction, not a collision sign theorem or an RH result.
The diagnostic passed a separate conceptual audit on 5 November 2026
(step577), with the box-edge and relative-bound qualifications below.
This verifies no actual event or collision sign.

## Proof

### Normalization, derivatives, and an actual kernel comparison

The input convention is exactly Xi(z)=xi(1/2+iz) in L018. In L017's
split Mellin integral the substitution x=exp(2u) gives I(1/2+iz)=
4 integral A(u)cos(zu)du. Hence L020's coefficient is
Xi(z)=1/2-2(z^2+1/4) integral A(u)cos(zu)du, with frequency z.
In L019, theta reflection gives psi'(1)=-(1+2psi(1))/8 and
A'(0)=psi(1)/2+2psi'(1)=-1/4. Twice integrating by parts therefore
gives exactly K=2A''-A/2 and F=integral K cos, without a missing factor.
These are checks of L019–L020's written input proofs, not extra premises.
L021's central positivity is simply F(0)=integral K>0; its moment
inequality is not needed here. L016's differentiated Gaussian-series
majorants justify the differentiation used in these input proofs.

For u>=0, cosh(9u/2)>=cosh(5u/2), so the bracket in Q is at least
(2pi-3)cosh(5u/2)>0. Also

    0<Q(u)<=C exp(9u/2) exp(-pi exp(2u))

for a fixed finite C: bound the bracket above by 2pi cosh(9u/2)
and use 2cosh(2u)>=exp(2u). Thus S(0) is finite and positive.
L021 gives F(0)>0. For each fixed integer j>=0 and finite M,
u^j Q(u) exp(Mu) is integrable. This follows, for example, by setting
y=exp(2u), after which exponential decay exp(-pi y) dominates every
fixed power of y and log y. The identical majorization for K is supplied
by L019–L020. Dominated differentiation therefore justifies every
cosine/sine derivative integral, uniformly on |z|<=M. The transforms
are entire and real on the real axis; (tau,x) dependence is analytic.

For a useful but insufficient actual comparison, denote the n=1 term of K by

    k_1(u)=4pi [2pi exp(9u/2)-3 exp(5u/2)] exp(-pi exp(2u)).

It is positive. Set s=exp(-2u), so 0<s<=1. Direct cancellation of the
positive common factors gives

    Q(u)/k_1(u)=exp(-pi s) [1+T(s)],
    T(s)=s^(7/2) (2pi s-3)/(2pi-3s).

The denominator is positive. If 2pi s-3<=0, then T(s)<=0 and
0<Q/k_1<=exp(-pi s)<1. If 2pi s-3>0, then s>3/(2pi) and 0<T(s)<=1:
indeed s^(7/2)<=1 and 2pi s-3<=2pi-3s. Consequently

    Q/k_1<=2 exp(-pi s)<2 exp(-3/2)<1.

The last strict inequality follows already from exp(3/2)>1+3/2>2.
All n>=2 terms of K are positive by L019. Hence Q<k_1<K pointwise,
including u=0. Integrating proves 0<S(0)<F(0), so c>1.

We also need a tail limit, not an uncontrolled asymptotic replacement.
With v=pi exp(2u)>=pi>3, the n-th summand satisfies

    k_n/k_1=n^2 (2v n^2-3)/(2v-3) exp(-(n^2-1)v)
             <=2n^4 exp(-(n^2-1)v).

For the inequality use 2v-3>v and 2v n^2-3<2v n^2; all
denominators and summands are positive. For n>=2, write
(n^2-1)v=3v+(n^2-4)v and then use v>=pi. Thus

    0<sum_(n>=2) k_n/k_1
       <=2 exp(-3v) sum_(n>=2) n^4 exp(-(n^2-4)pi) ->0.

The displayed constant series converges by Gaussian decay. Meanwhile
s->0 gives T(s)->0 and Q/k_1->1. It follows that K/Q->1. Therefore
d/Q=K/Q-c tends to 1-c<0. Equal mass gives integral d=0; since d is
continuous and strictly negative on a tail of positive Q mass, d must
be positive at some finite point as well.

For fixed 0<tau<1, write r=K/B>0. Then

    q_tau(u):=d(u)/h_tau(u)=(r(u)-1)/(1-tau+tau r(u)),
    -1/(1-tau)<q_tau(u)<1/tau,
    lim_(u->infinity) q_tau(u)=(1-c)/((1-tau)c+tau)<0.

The bounds follow directly by subtracting the stated endpoints, since
the denominator is positive. Since q_tau is positive somewhere and has
a strictly negative limit, it cannot be nondecreasing on [0,infinity).
This conclusion is about the kernel ratio, not its Fourier transform.

### Elimination, including exceptional cases and boundaries

If D(x)=0, then H_tau(x)=G(x)=F(x). If their common value is nonzero,
there is no zero of H_tau. If both vanish, H_tau(x)=0 for every tau,
and a double zero additionally requires (1-tau)G'(x)+tau F'(x)=0.
Such common-zero events have H_tau-parameter derivative D(x)=0 and are
outside the nondegenerate test, regardless of H_tau''; their multiplicities
are not resolved or discarded as nonexistent.

If D(x)!=0, H_tau(x)=0 forces tau=-G/D. An interior tau is equivalent
to F and G having strictly opposite signs. In particular neither is zero.
If G=0 alone the only possible parameter is tau=0; if F=0 alone it is
tau=1. These endpoints are outside the prescribed domain, not excluded
by a global statement. At x=0, F(0)=G(0)>0, so H_tau(0)>0 for every tau.
The included upper edge x=40 needs no division by x and is retained.
When F G<0 and W=0 but W'=0, the same calculation below gives
H_tau''=0. Such events are degenerate and no fold claim is made.

Substitution, without division by F', G', or H_tau'', gives

    H_tau'=G'-G D'/D=(F G'-G F')/D=W/D,
    H_tau''=G''-G D''/D=(F G''-G F'')/D=W'/D.

These equalities are evaluated with tau=-G(x)/D(x) fixed at the point;
they do not differentiate a moving parameter. The last equality uses
W'=F G''-G F'', since the first-derivative cross terms cancel.
This proves both directions of the claimed event characterization.

For orientation, H_tau-parameter derivative D!=0 permits the ordinary
implicit-function theorem to solve locally for tau=t(x). Differentiating
H_(t(x))(x)=0 at the event yields t'=0 and t''=-H_tau''/D!=0.
Hence D H_tau''<0 makes t have a strict local minimum: two nearby real
zeros occur on the larger-tau side. A positive product gives a strict
local maximum and zeros on the smaller-tau side. More explicitly,
t'=-W/D^2 and t''=-W'/D^2+2W D'/D^3 along t(x)=-G(x)/D(x).
At the event W=0, so t''=-W'/D^2. Continuity permits a real neighborhood where t'' has
its nonzero event sign. On the two sides of the event x-coordinate,
t is then strictly monotone in opposite directions. Each sufficiently
nearby parameter on the stated side has one zero on each side, and a
parameter on the other side has none in a smaller neighborhood. These
counts are local in the full real axis. At x=40 one of the two zeros
may lie above 40; two zeros inside the original box are not asserted.
Since the event parameter is interior, its neighborhood can be chosen
inside 0<tau<1. This elementary local application does not track all
complex zeros or treat a degenerate event.
It is consistent with the qualified scalar-fold source already assessed:
J.-P. Lessard, *Rigorous verification of saddle-node bifurcations in ODEs*,
[author manuscript](https://www.math.mcgill.ca/jplessard/ODEs_files/saddle_node.pdf),
Definitions 1–2 and Theorem 1, printed p.2; no sign is imported from it.

### The signed integral and the attempted square bound

Absolute Fubini is legitimate because K and B have finite second moments,
and |cos(xu)|<=1 on the real axis: an absolute majorant is
(u^2+v^2)K(u)B(v), whose double integral equals
(integral u^2 K)(integral B)+(integral K)(integral v^2 B)<infinity.
Interchanging u and v is therefore also justified. It gives

    W'(x)=integral integral (u^2-v^2) K(u) B(v)
                                cos(xu) cos(xv) du dv
         =(1/2) integral integral (u^2-v^2)
               [K(u)B(v)-K(v)B(u)] cos(xu) cos(xv) du dv.

All integrations here and below are on [0,infinity). For x>0 the cosine
product takes both signs. The established inequalities Q<K, c>1 and
the tail sign of d do not sign this double integral; no monotonicity of
K/Q or cancellation across these regions has been proved.

Here is the precise bound attempted, using the zero equation to remove
one constant term. At a double zero define

    V=integral u^2 h_tau(u) cos(xu) du=-H_tau''(x),
    E_(a,b)=integral [d(u)-(a+b u^2)h_tau(u)] cos(xu) du.

For any finite real a,b the integrals converge. Since integral h_tau cos=0,

    D(x)=b V+E_(a,b),
    D(x)H_tau''(x)=-b V^2-E_(a,b) V.

A paid bound |E_(a,b)|<=b |V| for some b>0 would suffice for the desired
nonpositive product. At a nondegenerate event the product is nonzero,
so such a bound would in fact force it to be negative.

There is no gain from choosing the coefficients using the unknown sign.
Indeed V!=0 and the exact identity E_(a,b)=D-bV make the displayed
bound equivalent to |D/V-b|<=b, that is 0<=D/V<=2b. Because also
D!=0, existence of some b>0 satisfying it is equivalent to D/V>0,
which is exactly D H_tau''=-D V<0. Thus an existential choice alone
restates the desired event sign. A usable estimate needs independent
control of the actual remainder; neither a nor the compensation e below
changes its value at the event. This audit qualification supplies no sign.

The first-derivative collision equation is also retained. For any finite
real e, subtracting e u h_tau(u) sin(xu) from the integrand defining E
does not change E at a double zero, because integral u h_tau sin=-H_tau'=0.
But no bound for this additionally compensated integral relative to |V|
has been obtained. This is a remaining signed estimate, not an assumption.

An exact normalized forward-heat identity d=(a+b u^2)h_tau cannot hold,
even at a single fixed interior tau. Boundedness of q_tau forces b=0.
Then integral d=0 and integral h_tau=F(0)>0 force a=0, contradicting
the proved negative tail of d. The stronger prerequisite that q_tau be
nondecreasing also fails, as shown above. Neither observation excludes
an approximate comparison with an independently controlled remainder.

The available absolute bound is only

    |E_(a,b)|<=A_(a,b):=integral |d-(a+b u^2)h_tau| du<infinity.

It supplies no estimate A_(a,b)<=b |V| at the event. Nondegeneracy gives
V!=0, not a quantitative lower bound; no compactness assertion supplies
one without excluding degenerate or parameter-boundary accumulation.
Thus the actual raw-kernel comparison and this square decomposition do
not pay the collision sign. No actual event or opposite-sign certificate
has been constructed. Unbounded x, degenerate events, all-real reference
proof, zeros at infinity, and the mixed-positivity assembly remain open.

## Mathlib

Full matching coverage is not checked. No absence or formal verification
is claimed. The kernel comparison, calculus identities and conditional
bound above are written out directly; the source import is the exact
definition of S, not an uninspected zero theorem.
