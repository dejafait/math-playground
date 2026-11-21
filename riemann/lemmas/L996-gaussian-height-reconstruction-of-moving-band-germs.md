# Lemma 996: Gaussian height reconstruction on the initial germ disk

## Hypotheses

Use precisely L994's actual von Mangoldt function, K_m, G_r, J_r,
C_r, H_r, a(w), rho=1/4 and R_0=rho*exp(-2). Here n>=2,
r=1,2, m=n+r, |w|=rho and Re(s)=1. Both vertical limits are
symmetric. Let omega run over ALL nontrivial zeta zeros, each with
its actual multiplicity, and put gamma_omega=Im(omega). Set

    B=-EulerConstant/2-1+log(4*pi)/2,
    A(u)=-B-log(pi)/2+1/(u-1)+(1/2)*psi(u/2+1),
    F_epsilon(u)=A(u)-sum_omega exp(-epsilon*gamma_omega^2)
                                   *[1/(u-omega)+1/omega],       (1)

where epsilon>0 and psi is the digamma function. Define
I_(r,H)^epsilon by replacing F with F_epsilon in BOTH occurrences
of L994(4). Its other factors, including 1/s, are unchanged.
No epsilon-dependent constant is added. No RH, simplicity, rightmost
zero, nonresonance, prime-power endpoint separation, or holomorphic
actual complement is assumed. Critical-line pairs are counted with
their actual multiplicities, not as four distinct points.

## Conclusion

For each fixed epsilon>0 the symmetric limit of I_(r,H)^epsilon
exists locally uniformly on |z|<R_0. On every |z|<=R<R_0,

    lim_(epsilon down to0) lim_(H->infinity) I_(r,H)^epsilon(z)
      =lim_(H->infinity) lim_(epsilon down to0) I_(r,H)^epsilon(z)
      =G_r(z)-J_r(z)+C_r(z),  r=1,2.                            (2)

Each indicated limit is uniform on this compact disk. The proof
does NOT assert a common H-tail modulus uniform in epsilon or
convergence along arbitrary coupled paths (epsilon,H).

For a function h on the positive real axis write

    Dcal_(n,r)[h]=integral_m^(2m) K_m(t)*h(t)dt
                                 -integral_n^(2n) K_m(t)*h(t)dt,
    Q_(n,r)(omega)=Dcal_(n,r)[exp((omega-1)*t)],
    h_arch(t)=exp(-3*t)/(1-exp(-2*t)),
    A_(n,r)=Dcal_(n,r)[1-h_arch(t)].

An exact form of the first inner limit is

    lim_(H->infinity) I_(r,H)^epsilon(z)
       =sum_(n>=2) z^n*[A_(n,r)-sum_omega
                    exp(-epsilon*gamma_omega^2)*Q_(n,r)(omega)]. (3)

The real pole gives the 1 in A_(n,r); the gamma term gives
-h_arch. The fixed canonical constants have zero transform here,
as verified below, rather than being dropped from (1).
J_r and C_r retain their exact definitions and signs from L994.

Step290, 10 November2026: RESEARCH / REPRODUCTION under unchanged
pre-invocation SPECIALIZE review288 and the supplied ready-target
gate. This is a specialization of the classical explicit formula,
Gaussian Abel summation and conditional Fourier inversion. It is
local progress, not a result beyond the checked source methods,
a zero-free estimate, actual signed output or an RH candidate.
The independent step291 conceptual audit below verifies this scope
without changing the statement. In particular (2)
does not continue a complementary sum to L995's singularity, exclude
cancellation there, prove L993 recovery or L984(H), or close
L030-L032/C032a or L966/L968.

## Proof

### Imported statements and why specialization is needed

Import H. L. Montgomery and R. C. Vaughan, *Multiplicative Number
Theory I: Classical Theory*, Cambridge2007:

- Corollary10.14, (10.28)-(10.30), and Theorem10.13,
  in section10.2, printed pp346-350, in the
  [analytic-properties chapter](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/14.0_pp_326_357_Analytic_properties_of_the_zeta_function_and_L-functions.pdf).
  These supply the full compensated logarithmic derivative and
  N(T+1)-N(T)=O(log(T+2)). In particular F=-zeta'/zeta is (1)
  with all Gaussian factors replaced by one, and
  sum_omega |omega|^(-2)<infinity. The standard zero strip is
  0<Re(omega)<1; all multiplicities are included.
- Theorem12.5, (12.3)-(12.4), printed pp400-401, and Lemma12.14,
  (12.27), printed pp414-416, in the
  [explicit-formula chapter](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/16.0_pp_397_418_Explicit_formulae.pdf).
  The former applies for x>=c>1 and T>=2, uses midpoint psi_0,
  and has nearest-OTHER-prime-power error. The latter applies to
  J in L1(R) of bounded variation with J(x)=J(0)+O(|x|) at zero,
  and fixed real parameters a,b>0. It evaluates the symmetric
  conditional Fourier integral of psi(a+ibt)*Jhat(t).
- AppendixA, TheoremsA.1-A.4, printed pp486-490, in the
  [Stieltjes chapter](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/20.1_pp_486_494_The_RiemannStieltjes_integral.pdf),
  for finite-cutoff integration by parts. Infinite passages below
  have separate bounds; they are not consequences of this citation
  alone.

The already assessed proof of Lemma12.14 invokes AppendixC. To
make its conditional-integral use checkable, the supporting
TheoremC.1 (C.17), printed p523, and TheoremC.5 and its derivative
estimate, pp526-527, were followed narrowly in the
[gamma chapter](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/20.3_pp_520_534_The_gamma_function.pdf).
C.1 gives psi(v)=log(v)+O(1/|v|) uniformly in any closed sector
away from the negative real axis and the origin. The proof of C.5
uses psi'(v)=sum_(k>=0)(k+v)^(-2)=O(1/|Im(v)|) for
|Im(v)|>=1, uniformly on the horizontal ranges in question.
On a fixed positive real strip, the absolute-value bound follows
also by comparison with integral_0^infinity dx/(x^2+Im(v)^2).
These are supporting estimates of the approved gamma inversion,
not a new target or a reproof of its general theorem.

L994(6) supplies the finite Cauchy coefficient identity and its
endpoint convention; L995(5) supplies the scalar inversion for
exp(t*s)/[s*(s-lambda)], with t>0 and Re(lambda)<1. Only that
scalar identity is used from L995, not quartet noncancellation.
The elementary constant-input Perron inversion is the one used
in L994's cited Theorems5.1-5.2. General source proofs are imported.
The work here is the common-line, compact-degree and regulator
specialization, which a pointwise canonical product alone does not
justify. All spectral cutoffs below are T, distinct from H.

### Start with finite cutoffs; remove epsilon at fixed H

Begin with 2<=n<=N, |gamma_omega|<=T and finite H. These are
finite sums and finite contours. For fixed H, all arguments u=s+d,
with d=a(w) or d=1, lie in a compact set with Re(u)>=9/5.
They are separated from every zero and from the real pole. For
large |omega| the entire compensated bracket is

    1/(u-omega)+1/omega=u/[omega*(u-omega)]=O_H(|omega|^(-2)),

uniformly on this compact set. The finitely many remaining terms
are bounded there. Thus the spectral limit is normally convergent,
uniformly for 0<epsilon<=1; dominated convergence gives
F_epsilon->F uniformly on these finite contours. On |z|<=R<R_0,
the degree expansion of H_r has ratio at most R*exp(2)/rho<1,
with its denominator n+r-1. It can therefore be summed on the
finite contours before or after this limit. Consequently

    lim_(epsilon down to0) I_(r,H)^epsilon=I_(r,H)               (4)

uniformly on that disk. L994 then proves the H-limit in this
order equals G_r-J_r+C_r. This alone would not prove the other
order, which is addressed next.

### Conditional A inversion, with all constants retained

Let d range over the compact set {a(w):|w|=rho} union {1}.
Then 4/5<=Re(d)<=4/3 and |Im(d)|<=1/3. The cited gamma estimates,
with the rational pole separated on Re(s)=1, give uniformly in d

    |A(1+i*y+d)|<=C*log(2+|y|),
    |A'(1+i*y+d)|<=C/(1+|y|).                                 (5)

The constants also cover bounded y by compactness. If
g_d(y)=A(1+i*y+d)/(1+i*y), then for |y|>=1

    |g_d(y)|<=C*log(2+|y|)/|y|,
    |g_d'(y)|<=C*log(2+|y|)/y^2.

Integration by parts against exp(i*t*y), separately on each tail,
therefore bounds the tails of the individual prefix integral by

    C*exp(t)*log(2+H)/(t*H), t>=2, H>=1.                       (6)

Here the boundary term at infinity is zero; the bound follows by
integrating log(2+y)/y^2. Thus every prefix has a conditional
H-limit uniform in d, with magnitude <=C*exp(t). The same bounds
hold for a constant input, by applying the argument to 1/(1+i*y).

For 2<=u<v, put p_(u,v)(s)=(exp(v*s)-exp(u*s))/s.
The constant-input integral has limit 1-1=0. Hence the fixed
-B-log(pi)/2 in A has zero interval response. The rational pole
1/(s+d-1), using L995(5) with lambda=1-d, gives
integral_u^v exp((1-d)*t)dt. Indeed Re(1-d)<=1/5<1;
the coincident case lambda=0 is removable in that scalar formula.

For the gamma term write d=d_0+i*d_1 and y'=y+d_1. Define

    alpha=(1+d_0)/2+1>0, b=1/2,
    J(x)=2*pi*exp(-2*pi*(1-i*d_1)*x)
                         *indicator_{[-v/(2*pi),-u/(2*pi)]}(x).

Choose midpoint values at its two endpoints, which do not affect
its integral. This J is L1 and of bounded variation, and vanishes
on a neighborhood of zero, so all hypotheses of Lemma12.14 hold.
With Jhat(y')=integral_R J(x)*exp(-2*pi*i*y'*x)dx, substitution
gives Jhat(y')=p_(u,v)(1+i*(y'-d_1)). The shift of the symmetric
endpoints from +-H to +-H+d_1 changes the gamma integral by
O_(u,v)(log(H)/H): |p|<=C_(u,v)/H on these bounded-length
segments and psi=O(log H). This error is uniform in d.
Lemma12.14 with the plus sign now yields

    lim_H (1/(2*pi*i))*integral_(1-iH)^(1+iH)
                 p_(u,v)(s)*(1/2)*psi((s+d)/2+1)ds
       =-integral_u^v exp(-(d+2)*t)/(1-exp(-2*t))dt.             (7)

For clarity, its gamma integral is multiplied by 1/(4*pi).
Its right side before substitution is
-integral_0^infinity exp(-4*pi*alpha*x)*J(-x)
/(1-exp(-4*pi*x))dx. Setting t=2*pi*x gives (7), including its
sign and the exponent d+2. Uniformity of the limit on the w
circle follows from (6), not an assumed uniform constant in the
fixed-test statement of Lemma12.14.

Combine the pole and gamma responses in the first branch d=a(w)
with coefficient (1-w)^(-3), and the second d=1 with coefficient
-(1-w)^(-1). L994(6), with m fixed, gives respectively
K_m(t) and -K_m(t)*exp(-3*t)/(1-exp(-2*t)). Thus the moving
interval difference is precisely A_(n,r). This establishes its
identification without discarding any constant or archimedean term.

Finally (6) bounds every A-input degree coefficient, both before
and after its height limit, by

    C*rho^(1-m)*exp(2*m)/(m-1),                                (8)

after the four endpoints and the bounded w factors are included.
For |z|<=R the degree series is summable since
q_R=R*exp(2)/rho<1. Its finite head converges uniformly in z
and w; its tail is uniform in H. This justifies the infinite degree
passage for A, without asserting absolute vertical convergence.

### Height limit for the Gaussian rational part

For fixed epsilon>0 the count bound implies
M_epsilon=sum_omega exp(-epsilon*gamma_omega^2)<infinity and
sum_omega exp(-epsilon*gamma_omega^2)/|omega|<infinity.
Accordingly at this stage only, split off the constant
sum_omega exp(-epsilon*gamma_omega^2)/omega. Its interval response
is zero by the constant-input calculation above. No unweighted
sum of 1/omega is split off as epsilon tends to zero.

For d as above, delta=1+Re(d)-Re(omega)>=4/5. Cauchy-Schwarz gives

    integral_R dy/(|1+i*y|*|1+i*y+d-omega|)
       <=sqrt(pi)*sqrt(pi/delta)<=pi*sqrt(5/4).                 (9)

The imaginary shift in the second factor does not change its L2
integral. Multiplication by M_epsilon gives an integrable majorant
for the sum of rational terms after 1/s, uniformly in w. Since
H_r is bounded for |z|<=R on the full vertical line, Fubini and
the absolute-integral tail justify the H-limit and the spectral
sum for this part. Uniformity in w can also be seen by bounding
each supremum over its compact d set by an integrable translate
envelope; alternatively split a finite spectral head and use (9)
for the arbitrarily small weighted tail, before integrating w.

For a finite spectral head, apply L995(5) to lambda=omega-d.
Its real part is <=1/5<1. The four constant residues cancel;
L994(6) then gives exactly Q_(n,r)(omega), with the minus sign
from (1). The constant 1/omega in each bracket has the already
verified zero interval response. At fixed epsilon, (9) bounds
the finite-height rational degree coefficient by the right side
of (8) times C*M_epsilon. The constant part has the same bound
times its finite absolute constant sum. Therefore the degree
tail is summable uniformly in H at each fixed epsilon, and (3)
follows. Dependence of these particular bounds on epsilon is
allowed: they are not used for the subsequent regulator limit.

### Uniform spectral response bound including all sharp endpoints

For T>=0 and t>=2 define the finite symmetric sum

    S_T(t)=sum_(|gamma_omega|<=T) exp(omega*t)/omega.

Theorem12.5 gives, for x=exp(t)>=exp(2), T>=2,

    S_T(t)=exp(t)-psi_0(exp(t))-log(2*pi)
                 -(1/2)*log(1-exp(-2*t))+R(exp(t),T),
    |R(x,T)|<=C*[log(x)*min(1,x/(T*dist_other(x)))
                                      +x*(log(x*T))^2/T].       (10)

dist_other(x)>0 is the distance to the nearest other prime power;
this includes the equality case at a prime power. Since
psi_0(x)<=x*log x, the minimum is <=1, 1/T<=1/2 and
sup_(T>=2)(log T)^2/T<infinity, there is a fixed C_0 such that

    |S_T(t)|<=C_0*exp(t)*(1+t)^2, t>=2, T>=0.                  (11)

For 0<=T<2 enlarge C_0 using the finite set of zeros of height
at most2, each with Re(omega)<1 and omega!=0. Thus no assertion
about the first zero is needed. For fixed t, (10) converges to
its displayed main expression, including midpoint psi_0; near a
prime power use the bounded domination (11), not uniform
convergence across the jump. A boundary zero in the spectral
cutoff is taken in full. If a half-weight height convention is
used instead, Theorem10.13 bounds the discrepancy by
O(exp(t)*log(T+2)/T); hence the same limits and domination hold.

Write Q_(n,r)(T)=sum_(|gamma_omega|<=T) Q_(n,r)(omega).
For one interval [u,v], finite integration by parts, with
phi_m(t)=K_m(t)*exp(-t), gives exactly

    sum_(|gamma_omega|<=T) integral_u^v K_m(t)*exp((omega-1)*t)dt
       =[phi_m(t)*S_T(t)]_u^v-integral_u^v phi_m'(t)*S_T(t)dt.   (12)

There are no discarded endpoint terms. To bound both intervals,
differentiate L994(6) in its finite t variable. Since
Re(-b(w))<=1/5 and |b(w)|<=1/3, one obtains

    |K_m(t)|<=B_m*exp(t/5), |K_m'(t)|<=B_m*exp(t/5),
    B_m=4*rho^(1-m)/(m-1), t>=2.                              (13)

Indeed the two numerator bounds for K are 64/27 and 4/3,
whose sum is 100/27<4; for K' the bound is 64/81<4.
Consequently |phi_m'|<=2*B_m*exp(-4*t/5). With four endpoint
terms, total interval length m+n<=2m and t<=2m, (11)-(12) give

    |Q_(n,r)(T)|<=C_0*B_m*(4+4*m)*exp(2*m/5)*(1+2*m)^2
       <=288*C_0*m^2*rho^(1-m)*exp(2*m/5)=:M_(n,r),            (14)

uniformly for T>=0. The last inequality uses m>=3,
(m+1)/(m-1)<=2 and 1+2m<=3m. This coarse bound is enough;
it is not a signed or subexponential estimate in degree.

Dominated convergence in (12) is now legitimate for each fixed
degree. Put P_(n,r) for the difference of the two midpoint
arithmetic interval sums with weight Lambda(q)*K_m(log q)/q.
The limiting main expression in (10) has continuous derivative
exp(t)-1/(exp(2*t)-1), apart from the negative prime-power jumps.
Its constant -log(2*pi) contributes zero to (12). Integrating
the continuous part against phi_m gives the interval response
of 1-h_arch. For a jump at u or v the endpoint values in (10)
give half its mass. This follows directly by applying (12) to
a step function: an interior jump contributes its full phi_m
value and a boundary jump contributes half. Hence

    lim_(T->infinity) Q_(n,r)(T)=A_(n,r)-P_(n,r).                (15)

The full-right/excluded-left convention satisfies
P_(n,r)=D_(n,r)+C_(n,r)-J_(n,r), where C_(n,r) and J_(n,r)
are the degree coefficients of L994's C_r and J_r. In particular
the correction at a lower endpoint has the opposite sign to that
at an upper endpoint. This keeps precisely all four terms of J_r.

### Gaussian Abel averaging and the second compact-uniform limit

At finite spectral cutoff use Stieltjes integration by parts with
the continuous Gaussian. Letting that cutoff tend to infinity,
using (14) for the boundary term and the Gaussian decay, yields

    Q_(n,r)^epsilon:=sum_omega exp(-epsilon*gamma_omega^2)
                                      *Q_(n,r)(omega)
       =integral_0^infinity 2*epsilon*T*exp(-epsilon*T^2)
                                      *Q_(n,r)(T)dT.           (16)

This can equivalently be checked first for a finite collection of
zeros from integral_(|gamma|)^infinity 2*epsilon*T*exp(-epsilon*T^2)dT
=exp(-epsilon*gamma^2), then by absolute convergence at fixed
epsilon. An atom at height0 would also be included; no zero
symmetry or multiplicity is lost. The positive kernel in (16)
has total mass one. Thus |Q_(n,r)^epsilon|<=M_(n,r), uniformly
for every epsilon>0. For a fixed degree, (15) implies

    Q_(n,r)^epsilon -> A_(n,r)-P_(n,r).                         (17)

Explicitly, if the difference in (15) is at most delta for T>=T_0,
the error in (17) is at most delta+2*M_(n,r)*(1-exp(-epsilon*T_0^2)).
This is an ordinary Abelian preservation of an already convergent
symmetric sum, not a substitution of a holomorphic Gaussian for
the literal height weight.

On the compact disk, (14) supplies the degree majorant

    R^n*M_(n,r)=288*C_0*rho^(1-r)*exp(2*r/5)
                                  *(n+r)^2*q^n,
    q=R*exp(2/5)/rho < exp(-8/5)<1.                            (18)

The required threshold is q<1. The strict initial-disk condition
gives the displayed margin without a numerical experiment. In
particular the degree tail n>N is bounded by the constant in (18)
times

    q^(N+1)*[(N+1+r)^2/(1-q)
       +2*(N+1+r)*q/(1-q)^2+q*(1+q)/(1-q)^3].                 (19)

It is uniform in T and epsilon. The A_(n,r) terms are summable
by (8), or directly by (13) and boundedness of h_arch for t>=2.
Choose N using (19), then use (17) on its finite head. This proves
that (3) converges uniformly as epsilon tends to zero to
sum_(n>=2)P_(n,r)*z^n=G_r-J_r+C_r. Together with (4) and L994,
this proves both iterated limits in (2). All contours retain both
shifted branches, and all pole, gamma and endpoint terms have been
identified before their respective infinite passages.

### Independent conceptual audit — step291, 10 November 2026

This audit reuses the unchanged SPECIALIZE review288 for exactly (2).
It is REPRODUCTION, with no stronger radius, joint-path assertion,
actual-zero isolation or new signed estimate. The source checks below
reopen the already assessed statements; they are not another literature
assessment or approval of an enlarged target.

First check the two transforms separately. On each finite vertical
segment the u arguments remain in Re(u)>=9/5. The bound for the
COMPLETE compensated bracket before (4) is therefore uniform on the
product of the w and s contours. Its summable |omega|^(-2) tail
allows epsilon removal before integration; separating 1/omega at this
stage would be unjustified. The H_r series is uniformly convergent
there because R*exp(2)/rho<1. Thus (4) is a compact-uniform assertion
at each fixed H, and the subsequent H-limit uses precisely L994.

For the opposite order, verify that conditional A inversion supplies
a height-uniform degree bound before epsilon is removed. From (5),
differentiate g_d(y)=A(1+iy+d)/(1+iy) to obtain the stated
O(log(2+|y|)/y^2) derivative. Integration by parts on each of
[H,infinity) and (-infinity,-H] gives (6); its boundary term tends
to zero. The central integral over [-1,1] is O(exp(t)), and the
tails starting at1 have that bound uniformly for t>=2. Thus the
finite and infinite prefixes are bounded by C*exp(t) independently
of d and H>=1. Four prefixes, the w-contour length and the coefficient
denominator m-1 give (8). No absolute gamma integral is asserted.

Theorem12.5, printed pp400-401, and Lemma12.14, printed pp414-416,
were reopened at the primary explicit-formula URL above. In the
latter use only its J(0)=0 case. Substituting x=-t/(2*pi) into
the stated Jhat gives exactly integral_u^v exp((1+i*(y'-d_1))*t)dt.
The gamma parameter is alpha=(3+d_0)/2, not (1+d_0)/2. The
prefactor 1/(4*pi) times the source's 2*pi/b, with b=1/2, is1;
the minus sign comes from J(0)-J(-x). The remaining exponential
is exp(-(2*alpha-1+i*d_1)*t)=exp(-(d+2)*t). This confirms (7).
If the source is read for real J, its application to this complex
J follows by applying the linear identity to real and imaginary
parts, both L1 and BV and both zero near0. Shifting symmetric
cutoffs by bounded d_1 costs O_(u,v)(log H/H). Uniformity in d
is supplied independently by (6), not by source constants for
varying J. The real-pole response and both Cauchy branches then
produce exactly 1-h_arch. The canonical constant's interval
response is zero, rather than an omitted renormalization.

At fixed epsilon, the count bound makes both weighted scalar sums
before (9) finite. The two squared L2 norms in (9) are pi and
pi/delta, where delta>=4/5. This proves a common L1 bound for
each rational summand. To justify a uniform H-tail after summing,
first choose a finite spectral head so that the weighted mass of
its complement is small; (9) bounds that complement for every H
and w. Every head term has an O(y^(-2)) tail uniformly on the
compact d set, once |y| exceeds its fixed pole heights. This
finite-head argument avoids inferring a common pointwise majorant
merely from an L1 norm bound. H_r is bounded uniformly in z,w,y,
so it proves the required compact-uniform rational limit. The
weighted constant is treated by conditional constant inversion.
L995(5) applies to each head pole since Re(omega-d)<=1/5<1;
after subtracting the four endpoints its constant residues cancel.
The degree tail follows from (8) at this fixed epsilon. None of
these bounds is required to remain bounded as epsilon decreases.

For the later epsilon-limit, Theorem12.5 permits all T>=2 and
includes the exact arithmetic endpoint case by excluding x itself
from the nearest-other-prime-power distance. The bound
(t+log T)^2/T <= t^2+2*(log T)^2/T for T>=2, together with
the trivial psi_0 bound, verifies (11) with one constant for all
t>=2. A finite low-height head handles T<2. Full inclusion of
zeros at height T is the convention used in (12); changing to
half weights costs O(exp(t)*log(T+2)/T) for T>=2 and changes
neither its limit nor its domination. All counts include multiplicity.

In (12), phi_m is smooth and both integration intervals are finite.
Thus (11) dominates its integral as well as its four endpoint
values. Differentiating the continuous part of the limiting S_T
gives exp(t)-1/(exp(2*t)-1); multiplying by phi_m gives exactly
the density 1-h_arch. For a unit upward step at an endpoint,
[phi*S]_u^v-integral phi'*S assigns phi(u)/2 or phi(v)/2;
for an interior step it assigns phi at the jump in full. The
prime-power steps in S have negative size Lambda(q). Hence (15)
has A-P with midpoint P, and P=D+C-J, including the relative sign
of the two intervals and both lower-endpoint corrections. No smooth
convergence across a prime-power jump is needed.

The bounds (13) give endpoint cost4 and integrated derivative
cost at most4m in (14). Substitution of B_m gives the numerical
factor 16*(m+1)/(m-1)*(1+2m)^2 <=288*m^2 for m>=3.
This is the required regulator-independent bound, not the
epsilon-dependent estimate used for the H-limit. At fixed epsilon
the sum of absolute |Q_(n,r)(omega)| weights is finite, since
Re(omega)<1 bounds each fixed-degree interval response independently
of height. Consequently the finite-sum verification of (16) extends
by absolute convergence, even for a possible height-zero atom.
The averaging kernel is nonnegative of mass1. Its mass on [0,T_0]
is 1-exp(-epsilon*T_0^2); (14)-(15) give precisely the finite-head
error after (17). Conjugate, reflected and critical-line zeros are
never regrouped into fictitious four-point multiplicities.

Finally (18) follows by separating m=n+r, with
q=R*exp(2/5)/rho<exp(-8/5)<1. The three terms in (19) are the
exact sums of (N+1+r+k)^2*q^k for k>=0, multiplied by q^(N+1).
For epsilon removal, choose the degree cutoff using this bound
and then apply (17) to its finite head. For H removal at fixed
epsilon, instead use (8) and the fixed weighted masses, then
the finite-degree H-limits. For the reverse iterated limit use
(4) first and L994 second. These distinct arguments establish
all the uniformities claimed in (2), without exchanging all
three infinite limits at once.

Audit verdict: (2)-(19) pass without a mathematical repair or
stronger conclusion. The direct uses of L994 and L995 already
listed in the DAG are sufficient; L995 is used only for its scalar
inversion, not its quartet singularity conclusion. The audit makes
the existing local reconstruction a checked input. It supplies no
actual complementary continuation, sign, zero-free region or RH
candidate. Further such questions require a new assessed target.

## Mathlib

Full matching coverage of this coupled Gaussian/Perron/degree
statement has not been checked and is unknown. No Mathlib theorem
is claimed to prove (2) or (18). Supporting analytic and Stieltjes
tools were imported from the precise primary sources above; this
is an informal proof with the conceptual audit above, not a Lean
certificate. No numerical or mathematical script was used.
