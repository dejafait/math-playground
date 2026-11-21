# Lemma 727: explicit actual-Xi quadratic-tail control and signed transfer

## Hypotheses

Use the actual Xi function, zero correspondence and symmetries of L018,
the imaginary-axis positivity of L021, the unconditional product of L024,
and L467's multiplicity-counted closed unit-shell bound. Logarithms are
natural. Let

    T >= exp(8), L=log T, H=2*pi*L,
    t in [T/L,T], Xi(t)!=0.

Write alpha for distinct Xi zeros and m_alpha for their full
multiplicities. Define the finite polynomial

    P(v)=product_(|Re(alpha)-t|<=H) (1-v/(alpha-t))^m_alpha.

Equality at the cutoff belongs to P. Every actual zero and its
multiplicity is retained, either in P or in its exterior complement.
There is no RH, simplicity, separation, zero projection, fixed-half-plane
or central-value lower-bound hypothesis. The normalization Xi(t)!=0
is essential to these definitions; this result does not extend them to
Xi(t)=0.

## Conclusion

Analytic cancellation defines the real entire function

    R(v)=Xi(t+v)/(Xi(t)*P(v)), R(0)=1.

R has no zeros in |v|<H. On that disk there is a unique holomorphic
logarithm E with E(0)=0 and exp(E)=R. It is real on the real interval
(-H,H), with real Taylor coefficients. Put

    Q(v)=E'(0)*v+E''(0)*v^2/2, h(v)=E(v)-Q(v).

Then, uniformly for every allowed T,t and complex |v|<=1,

    |h''(v)| <= 14*|v|/L <= 14/L.                         (1)

In particular this is a completely numerical C/log T bound with C=14
and onset exp(8), including the entire unbounded exterior-zero tail.
Also |h'(v)|<=7*|v|^2/L and |h(v)|<=7*|v|^3/(3*L).
The actual quadratic curvature is

    Q''=E''(0)=-sum_(|Re(alpha)-t|>H) m_alpha/(alpha-t)^2
       <=0,                                             (2)

an absolutely convergent, signed equality, not a discarded counterterm.

For a real twice differentiable function f, write D_1(f;v)=f'(v)^2-f(v)f''(v).
For all real |v|<=1, including every real multiple zero of P,

    D_1(Xi;t+v)
      =Xi(t)^2*exp(2*E(v))
         *[D_1(P;v)-Q''*P(v)^2-h''(v)*P(v)^2].           (3)

Thus with M_Q(v)=D_1(P;v)-Q''*P(v)^2, the denominator-free estimate is

    |exp(-2*E(v))*D_1(Xi;t+v)/Xi(t)^2-M_Q(v)|
       <= (14/L)*P(v)^2.                                (4)

In particular the independent signed-margin hypothesis

    M_Q(v) >= (14/L)*P(v)^2                              (5)

at any such real v suffices for D_1(Xi;t+v)>=0. Imposing (5) throughout
the interval suffices throughout it. No favorable margin for the actual
P is established here. Equation (3) compares Xi(t+v) with
Xi(t)*exp(Q(v))*P(v) while retaining the full signed Q'' term.

This is a quantitative specialization of known product/count/gauge
inputs, not a new positivity theorem. It supplies neither all-degree
mixed positivity, central-zero normalization, global sign coverage nor
an RH candidate. The small remainder alone does not supply (5).

## Proof

### 1. Imported inputs and analytic cancellation

Import Hadamard factorization as specialized in L024. Its primary
locator is Petrow, *Introduction to Analytic Number Theory*,
[Theorems 7.5 and 7.7, printed pp.57--59](https://www.homepages.ucl.ac.uk/~ucahpet/IANTnotes2018.pdf).
L024 checks the order-at-most-one and nonzero-origin hypotheses,
reciprocal-square summability, absence of a quadratic exponential and
locally uniform paired convergence for actual Xi. None is reproved here.
L018 puts alpha=gamma+i*delta with |delta|<1/2, and gives reflection and
conjugation with equal multiplicities. L021 already proves Xi(iy)>0 for
every real y from its positive cosine kernel. Consequently gamma!=0 for
every zero. This supporting existing low-height exclusion is needed to
avoid an unspecified finite count on Re(alpha)=0; no new exclusion is
assumed or derived in this specialization.

The complete count input, imported through the audited application
L467, is Bellotti--Wong, *Improved estimates for the argument and
zero-counting function of the Riemann zeta-function*,
[arXiv:2412.15470v2 (7 July 2025), Theorem 1.1 p.1 and Section 5
pp.23--24](https://arxiv.org/pdf/2412.15470v2). Precisely, if Gamma is
the multiset of positive real parts of all Xi zeros, counting distinct
zeros with equal real parts separately and with their full orders, then

    #{gamma in Gamma: w<=gamma<=w+1}<=18*log(w+2), w>=0.   (6)

Both endpoints and all low heights are covered by L467. The negative
real parts are the reflected multiset -Gamma by L018. The cited source's
numerical inputs and full manuscript are not independently audited here.

The zeros used by P lie in a compact rectangle, so they are finite in
number. Xi(t)!=0 makes every alpha-t nonzero and P(0)=1. Conjugation
preserves the selected set and multiplicities, so P is real. At each
selected root a=alpha-t it divides Xi(t+v) to exactly that root's order.
Consequently R extends across all those roots, is entire and has precisely
the unselected shifted zeros, with their orders. Each of those satisfies
|alpha-t|>=|Re(alpha)-t|>H. Thus R is zero-free on |v|<H, a simply
connected disk, and the normalized holomorphic logarithm E exists there.
It is unique since E(0)=0. Conjugating E gives another such logarithm,
so E(conj(v))=conj(E(v)); in particular its Taylor coefficients and
values on the real interval are real. Equivalently R is positive there,
since R(0)=1 and R has no real zero there.

### 2. Differentiated product, including cancellation points

The known reciprocal-square identity is the product identity used by
Csordas, *Fourier transforms of positive definite kernels and the Riemann
xi-Function*, [arXiv:1309.0055v2 (21 February 2014), Definition 1.1,
Proposition 2.2 proof (2.3), pp.3--4](https://arxiv.org/html/1309.0055v2).
Import the identity, not that proposition's additional zero-exclusion
positivity premise. L471 Section 1 checks its Xi specialization and
local convergence; L471 (7) also records the gauge-curvature identity.
The present use changes the local factor and quantifies its remainder.

On a compact neighborhood avoiding Xi zeros, L024's locally uniform
product and Cauchy's formula permit two differentiations. Denominators
are bounded away from zero there. Its absence of a quadratic exponential
therefore gives

    (Xi'/Xi)'(t+v)=-sum_alpha m_alpha/(v-(alpha-t))^2.

The series is absolutely and locally uniformly convergent away from the
zeros: for sufficiently large |alpha| and bounded t+v, its terms are
bounded by 4*m_alpha/|alpha|^2. No first reciprocal series is separated
or rearranged. Subtract the finite logarithmic second derivative of P.
Initially away from the selected roots this gives

    E''(v)=-sum_exterior m_alpha/(alpha-t-v)^2.             (7)

The exterior series is holomorphic throughout |v|<H, locally uniformly
by the same bound; E'' is also holomorphic there. Analytic continuation
therefore establishes (7) at the canceled roots as well. Subtracting (7)
at zero is legitimate by absolute convergence and yields

    h''(v)=-sum_exterior m_alpha
                *[(alpha-t-v)^(-2)-(alpha-t)^(-2)].        (8)

### 3. Complete uniform cubic-distance tail

For r>=H put a distance shell r<=|Re(alpha)-t|<2r. The positive-real-part
zeros in this shell have gamma in at most two intervals of length at
most r, obtained by intersecting [t+r,t+2r] and [t-2r,t-r] with gamma>0.
Each is covered by at most ceil(r)<=r+1 closed unit intervals starting
at w>=0. All their starting points satisfy w+2<=t+2r+3. If clipped at
zero, start the first unit interval at zero; this still covers every
positive ordinate and retains this bound. Thus (6) gives at most
36*(r+1)*log(t+2r+3) positive-real-part occurrences in the shell.

For negative real parts write Re(alpha)=-gamma with gamma in Gamma.
Since t>0, their distance is t+gamma. The condition r<=t+gamma<2r
places gamma in one interval [r-t,2r-t] intersected with gamma>0,
of length at most r. The same unit covering and (6) give at most
18*(r+1)*log(t+2r+3) occurrences. Reflection preserves every
multiplicity. There are no zeros with real part zero by L021. Since
r>=H>=2*3*8=48>1, the total shell count is consequently at most

    54*(r+1)*log(t+2r+3)<=108*r*log(t+2r+3).              (9)

Closed covering intervals can count endpoints twice, which only
increases these upper bounds. Equality |Re(alpha)-t|=H was already
included in P; allowing it in an upper count in the first shell is
harmless.

Let r_j=2^j*H for every integer j>=0. These shells cover the entire
exterior, with no truncation at either infinite end. Using (9) gives

    S_3:=sum_exterior m_alpha/|Re(alpha)-t|^3
      <= (108/H^2)*sum_(j>=0) 4^(-j)*log(t+2*r_j+3)
      <= (108/H^2)*[(4/3)*log(t+2*H+3)+(4/9)*log 2].      (10)

The second inequality uses
t+2*r_j+3<=2^j*(t+2*H+3),
sum 4^(-j)=4/3 and sum j*4^(-j)=4/9. Thus it proves convergence as
well as a uniform bound, including arbitrarily remote negative and
positive ordinates.

For L>=8, the exponential series gives

    T=exp(L)>L^4/24>16*L+3>4*pi*L+3.

Indeed L^4/24>= (64/3)*L, whose excess over 16*L+3 is positive
for L>=8; also pi<4. Hence t+2*H+3<2*T. Using log 2<1 and L>=8,

    log(t+2*H+3)<=L+log 2<=(9/8)*L.

Equation (10) now becomes

    S_3 <= (162*L+48)/H^2
        <=168*L/H^2=42/(pi^2*L)<14/(3*L),                (11)

where 48<=6*L and pi>3. All constants and the onset are numerical.
Only t<=T and t>0 were needed, so in particular the entire stated
interval [T/L,T] is covered.

For a=alpha-t in the exterior and |v|<=1, put s=|a|>=H>=48>8.
The exact difference and the reverse triangle inequality give

    |(a-v)^(-2)-a^(-2)|
      =|2*a*v-v^2|/(|a|^2*|a-v|^2)
      <= |v|*[(2+1/s)/(1-1/s)^2]/s^3
      <=3*|v|/s^3
      <=3*|v|/|Re(alpha)-t|^3.                           (12)

For the displayed factor, 2+1/s<=17/8 and
(1-1/s)^2>=49/64, so its ratio is at most 136/49<3.
Equations (8), (11) and (12) prove (1), uniformly on the closed complex
disk. Finally h(0)=h'(0)=0. Integrating h'' along the straight segment
from zero to v proves the stated bounds for h' and h; the factors
are respectively integral_0^1 s ds=1/2 and
integral_0^1 (1-s)*s ds=1/6. These are bounds for an already constructed
analytic logarithm, not an unsupported logarithm of Xi through its zeros.

### 4. Actual quadratic sign and zero-safe gauge comparison

At v=0, (7) gives the exact equality in (2). To verify its sign, group
the absolutely convergent exterior series into real zeros and conjugate
pairs, which the cutoff preserves. A real zero contributes m/(gamma-t)^2
to -Q''. For a nonreal pair gamma+/-i*d, 0<d<1/2, with equal
multiplicity m, put x=gamma-t. Its contribution to -Q'' is

    m*[(x+i*d)^(-2)+(x-i*d)^(-2)]
       =2*m*(x^2-d^2)/(x^2+d^2)^2>0,

since |x|>H>d. Thus Q''<=0 without assuming any sign of the local
polynomial. This uses algebraic reciprocal squares, not absolute squares.

For any holomorphic g and P, direct differentiation gives the canceled
identity

    D_1(exp(g)*P)=exp(2*g)*[P'^2-P*P''-g''*P^2].         (13)

It is an identity of holomorphic functions and involves no division
by P. Apply it to Xi(t+v)=Xi(t)*exp(E(v))*P(v), and use
E''=Q''+h''. This proves (3). Applying (13) to exp(Q)*P shows that
its first-Laguerre expression is exactly exp(2*Q)*M_Q. For real v,
E,Q,h and P are real, Xi(t)^2*exp(2*E(v))>0, and P(v)^2>=0.
Equation (1) consequently gives (4) and the sufficient condition (5).

These identities apply directly at all local real zeros. If P has
a simple zero, its contribution there is P'(v)^2; if its order is
at least two, both P(v) and P'(v) vanish and D_1(P;v)=0. The error
weight P(v)^2 vanishes at either kind of zero. No quotient P'/P or
uniform positive lower bound on P is used at these points. This
zero-safe extension in v does not remove the separate restriction
Xi(t)!=0 at the normalization center.

The signed local margin (5), higher signs and all-height coverage
remain independent. In particular exact exterior curvature information
is already implicit in the known reciprocal-square identity; this
quantitative remainder estimate supplies no new unconditional sign.
No growing-radius substitution in a fixed-radius theorem is used. ∎

### Critical application audit — 3 November 2026, step 226

The exact application passes the separately approved conceptual audit
in `drafts/literature/2026-11-03-l727-conceptual-audit.md`. No change to
the hypotheses, constants, onset or mathematical conclusions is needed.
The D1 definition above now says twice differentiable, and the Petrow
page range is corrected to the inspected printed pages. These are
wording/locator corrections, not a stronger result or repaired estimate.
The cited factorization and counting theorems remain imports; their
full source proofs and computational inputs are not independently audited.

**Cancellation and logarithm.** At a selected a=alpha-t of order m,
write Xi(t+v)=(v-a)^m U(v) and P(v)=(v-a)^m V(v), with U(a)V(a)!=0.
The quotient after cancellation is U/(Xi(t)V), which is nonzero at a.
At every unselected zero P is nonzero. This checks both entire extension
and the exact remaining zero multiset; it is stronger than merely
removing apparent poles. The strict exterior condition gives |a|>H.
The nonvanishing disk is simply connected, so R'/R has a primitive E
normalized at zero; differentiation shows exp(-E)R is identically one.
Any two normalized logarithms differ by a constant in 2*pi*i*Z and
therefore agree. Conjugating gives the same normalized logarithm,
which proves reality without taking log Xi across a root. Xi(t)!=0
is still indispensable to both definitions. The cutoff endpoints are
removed in P, and no zero on Re(alpha)=0 was omitted: L021 excludes it.

**Differentiation and multiplicities.** For a compact set avoiding
zeros, take a slightly larger zero-free neighborhood. L024's paired
partial products and their first two derivatives converge there; on the
smaller compact set their denominators are bounded away from zero.
Their logarithmic second derivatives therefore converge to (Xi'/Xi)'.
Each finite identity is the sum of the algebraic reciprocal squares
of its individual zeros. The bound 4*m_alpha/|alpha|^2 for the tail
gives absolute local uniform convergence of the resulting series.
Thus there is neither a rearranged first reciprocal series nor a
missing exponential curvature. After subtracting P, the exterior series
is holomorphic throughout the disk; its equality to E'' on the complement
of the finitely many canceled roots extends through them. This justifies
(7), its value at zero, and their subtraction in (8), for all orders.

**Both infinite tails and the constants.** In a distance shell [r,2r),
positive real parts lie in at most two intervals, each of length at
most r; negative real parts correspond to one positive-ordinate interval
of length at most r. For a clipped interval [a,b] with a>=0, covering
by intervals starting at a,a+1,... uses at most ceil(r) intervals
(one suffices for a degenerate interval). Their starting points are
at most the upper endpoint, itself at most t+2r. L467 applies at every
such nonnegative start, including zero, with full multiplicities.
Closed covers may overcount endpoints but cannot miss them. Hence
54(r+1)log(t+2r+3)<=108r log(t+2r+3) is a valid shell bound.
For each exterior zero there is a finite j>=0 with
2^j H<=|Re(alpha)-t|<2^(j+1)H. Summing these disjoint shells therefore
covers arbitrarily remote zeros of both signs, with no cutoff limit
or unbounded unestimated remainder. The exact geometric sums are
4/3 and 4/9, giving (10).

For L>=8, L^4/24>=64L/3, and
64L/3-(16L+3)=16L/3-3>0. The exponential series and pi<4 now give
exp(L)>4*pi*L+3. Together with t<=T this proves the logarithm bound
in (11), uniformly in the moving center. The numerator in (10) is
at most 162L+48<=168L; division by H^2=4*pi^2*L^2 gives
42/(pi^2 L)<14/(3L). For s=|alpha-t|>=H>48, the reciprocal-square
difference factor is at most (17/8)/(49/64)=136/49<3.
Combining these two strict upper bounds gives at most 14|v|/L on
the entire closed unit disk, including v=0 where the difference is
exactly zero. This is an all-parameter inequality, not a sampled
numerical check. Segment integration yields 7|v|^2/L and
7|v|^3/(3L), respectively. The lower endpoint t=T/L is admissible;
no hidden large-t assumption beyond 0<t<=T enters these estimates.

**Curvature and signed transfer.** The exterior set is invariant under
conjugation. Absolute summability permits grouping it into real zeros
and conjugate pairs with equal orders. In the latter case
x^2-d^2>0 follows from |x|>H and |d|<1/2, so (2) has the stated
nonpositive sign. This reasoning does not apply to the local head,
whose sign remains unproved. Differentiating exp(g)P gives cancellation
of the two g' cross terms and of g'^2 P^2, leaving exactly
P'^2-PP''-g''P^2. Thus the sign of Q'' in (3) is correct; discarding
the term would change the comparison. All these identities are
holomorphic on the disk. At a real root of P, (3) reduces to a positive
factor times P'^2; that is zero for order at least two and positive
for a simple root. The error weight is zero in either case. Consequently
(4) and the weak sufficient inequality (5) hold without division by P,
including at endpoints v=+/-1 and real multiple zeros.

The audit validates the existing quantitative specialization only.
It gives no new numerical estimate, no independent actual-local margin,
no extension to Xi(t)=0 centers, no higher signs and no global coverage.
In particular, favorable Q'' and a small h'' do not bound D1(P) from
below. The normalization calculation is complete; another refinement
of its tail is not a justified signing continuation without a new
independent input. The mathematical DAG inputs are unchanged.

## Mathlib

Not checked for the full moving-center explicit C2 bound or the signed
transfer. L024 and L467 record their supporting input coverage separately.
No matching formal theorem is claimed; unknown availability is not absence.
The [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/)
is only a locator, not evidence of full coverage.
