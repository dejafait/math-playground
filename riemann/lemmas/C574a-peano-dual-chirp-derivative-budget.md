# Corollary 574a: Peano density dual and complete chirp derivative budget

## Hypotheses

Use L574 for arbitrary sufficiently large real T, with its unconditional
finite-mean-square and Mertens imports retained. Write

    L=log T, h=1/L, M=floor(sqrt(T/(2 pi))),
    J=[T+h,2T-h], ell=T-2h,
    F(t)=|sum_(n<=M)n^(-1/2-it)|^2,
    D(t)=F(t+h)-2F(t)+F(t-h),
    Q(t)=F(t+h)+2F(t)+F(t-h)+L, g(t)=D(t)/Q(t),
    c=sin(1/32)^4 log(2)^2/512.

The integer M is fixed in every height differentiation. Use C481a's
complete ratio component U=-F'' and L477's exact decomposition R=U+V,
where all pairs in

    V(x)=sum_(n,m<=M) a_nm cos(f_nm(x)),
    a_nm=log(n/m)^2/sqrt(nm),
    f_nm(x)=2theta(x)-x log(nm)

are ordered. Retain L477's analytic phase estimates
theta'=log(x/(2pi))/2+O(T^(-2)), theta''=1/(2x)+O(T^(-3)),
uniformly on [T,2T], and its finite L2 estimates for P_j, j<=2.
No RH, simplicity, independent phases, moving cutoff or weighted
denominator decorrelation is assumed.

Define on the real line

    psi(x)=-h^(-2) integral_J (h-|x-t|)_+ g(t) dt.

## Conclusion

The multiplier is real, supported on [T,2T], belongs to C^1 on the
real line, and satisfies

    |psi|<=1, psi(T)=psi(2T)=psi'(T)=psi'(2T)=0,
    ||psi'||_infinity<=2L,
    v:=integral_T^(2T)|psi'(x)|dx<=2L integral_J |g(t)|dt
                                             <=2L ell.       (1)

Its exact weighted Peano pairing, including both boundary strips, is

    integral_T^(2T) U(x)psi(x)dx
       =h^(-2) integral_J D(t)^2/Q(t)dt >= c T L^3.           (2)

Finite first-derivative estimates for the complete chirp give

    |integral_T^(2T) V(x)psi(x)dx|
       <= min{64 T M, 32 M(v+1)}
       <= min{64 T M, 32 M(2L ell+1)}.                       (3)

Independently, the finite L2 estimates already in L477 give

    |integral_T^(2T) V(x)psi(x)dx| <= C T L^3                (4)

for an absolute, unspecified C. None of (3)--(4) proves the required
upper bound (c/2)T L^3 or a little-o bound. In particular, the two
explicit upper budgets in the last line of (3), divided by that
threshold, tend to infinity. This is failure of these guaranteed
budgets, not a lower bound for the actual correlation or a refutation
of the desired estimate. The direct variation-based implementation
is parked. No full-residual lower bound, Xi sign or RH result follows.

Conditionally, if the additional leakage bound (c/2)T L^3 did hold,
(2) and |psi|<=1 would imply integral |R|>=(c/2)T L^3 and then
L477's transfer would give E(T)>=(c/4)T L^3 eventually. This conditional
use supplies the relevance of (2), not its missing premise.

## Proof

### 1. Actual regularity and all convolution boundaries

All finite densities are smooth in t. Since Q>=L>0 for every real t,
g is smooth on the real line, and L574 gives |g|<=1. Extend its
restriction to J by zero, writing b=1_J g. This extension can have
jumps at T+h and 2T-h; we do not assign it smoothness there. Put
K(u)=(h-|u|)_+. Then psi=-h^(-2)K*b and

    psi'(x)=-h^(-2)[integral_x^(x+h)b(t)dt
                              -integral_(x-h)^x b(t)dt].    (5)

The right side is continuous: each bounded b integral with moving
endpoints is a difference of Lipschitz antiderivatives. Integrating
the elementary piecewise derivative of K, or first using its absolute
continuity, proves (5) everywhere. Thus psi is globally C^1; in fact
psi' is Lipschitz. Its almost-everywhere second derivative is

    psi''(x)=-h^(-2)[b(x+h)-2b(x)+b(x-h)],                 (6)

so |psi''|<=4L^2 almost everywhere. On each open interval separated
by T,T+h,T+2h,2T-2h,2T-h,2T, it is smooth. No all-order uniform
derivative bounds across these transitions are asserted or needed.

The area of K is h^2, whence |psi|<=1. The support is J+[-h,h]
=[T,2T]. At either endpoint its convolution overlap has length zero;
the same holds for the two integrals in (5), proving the four zero
endpoint values in (1). Since ||K'||_1=2h, finite Fubini and the
triangle inequality give

    integral_R |psi'|<=h^(-2)||K'||_1 integral_J |g|
                     =2L integral_J |g|.

Also (5) gives |psi'|<=2/h=2L. These prove (1). No endpoint strip,
jump of b or internal boundary contribution has been omitted.

### 2. Sign, normalization and exact positive pairing

C481a's Peano identity for this same fixed M is

    D(t)=-integral_(t-h)^(t+h) K(x-t)U(x)dx.

It specializes Carl de Boor, *Divided Differences*, Surveys in
Approximation Theory 1 (2005), 46--69, Section 9, p. 62, (46)--(48),
[primary text](https://surveys-in-approximation-theory.com/papers/2/2.pdf#page=17).
The hypotheses are C^2 of F on the three distinct knots t-h,t,t+h;
the finite F here is C^infinity and h>0. The full Peano theorem is
imported through C481a, not reproved. The extra weight g requires
only the following finite Fubini specialization.

For t in J the entire support [t-h,t+h] lies in [T,2T]. All
integrands are bounded on the compact product region, so ordinary
Fubini applies even with signed U and g. Multiplying the displayed
identity by g, integrating over J, and using the definition of psi
gives

    integral U psi=-h^(-2) integral_J g(t)
                          integral_T^(2T)K(x-t)U(x)dx dt
                 =h^(-2) integral_J g(t)D(t)dt
                 =h^(-2) integral_J D(t)^2/Q(t)dt.

Both minus signs cancel and h^(-2)=L^2. L574's lower bound cTL
therefore proves (2) at all the same sufficiently large real T.
No boundary approximation or sign of g is assumed.

### 3. Nonstationary phases including exact cutoff heights

The terms n=m have exactly zero a_nm and contribute nothing. For
each remaining ordered pair write

    alpha=log(M/n), beta=log(M/m), d=alpha+beta.

Here d>0 and |log(n/m)|=|alpha-beta|<=d. Since the largest
distinct-index product is M(M-1),

    d>=log(M/(M-1))>=1/M.

Also T>=2pi M^2. The analytic phase estimates retained from L477
give, uniformly on the whole interval,

    f_nm'(x)=log(x/(2pi nm))+O(T^(-2))>=d/2>0,
    f_nm''(x)=1/x+O(T^(-3))>0,                            (7)

once one absolute lower threshold for T is chosen. Uniformity follows
because T^(-2)=o(1/M). This includes T=2pi M^2. The only possible
zero of the unperturbed endpoint gap at n=m=M had zero coefficient
and was removed before division. Thus no stationary or exceptional
interval remains for these original phases. No Fourier mode has been
added to them.

### 4. Exact finite integration by parts and complete ordered sum

For f=f_nm, ordinary integration by parts is valid because psi is
C^1 and f is C^2 with f'>0. It gives

    integral_T^(2T)psi e^(if)
       =[psi e^(if)/(i f')]_T^(2T)
          -integral_T^(2T)e^(if)
                         [psi'/(i f')-psi f''/(i f'^2)].   (8)

The bracket is exactly zero by (1), rather than neglected. With (7),
monotonicity of f' and |psi|<=1, the remaining terms have total bound

    v/f'(T)+integral_T^(2T)f''/f'^2
       =v/f'(T)+1/f'(T)-1/f'(2T)
       <=2(v+1)/d.                                      (9)

The trivial integral bound is T. Formula (8) already holds across
all six convolution transition points; splitting there would give
canceling internal boundary terms since psi and f' are continuous.
This direct calculus identity is the finite-endpoint alternative
explicitly allowed by the source assessment. It is not a reproof of
a general stationary-phase theorem, and avoids the unverified high
derivative scale conditions of the compact-support sources.

For j=0,1,2 put S_j=sum_(n<=M)log(M/n)^j/sqrt(n), with the
zeroth power defined as 1. The nonnegative function
x^(-1/2)log(M/x)^j is decreasing on (0,M] (constant-power j=0
included), so each summand is at most its integral over [n-1,n].
The improper integral is convergent, and the substitution x=M e^(-u)
gives

    S_j<=sqrt(M) integral_0^infinity e^(-u/2)u^j du
        =2^(j+1) j! sqrt(M).

Thus S_0<=2sqrt(M), S_1<=4sqrt(M), S_2<=16sqrt(M).
The *complete ordered* coefficient sum is

    sum_(n,m<=M) a_nm=2S_0 S_2-2S_1^2<=64M.             (10)

Using (alpha-beta)^2<=d^2 on the off-diagonal also gives

    sum_(n!=m) a_nm/d
       <=sum_(n,m<=M)(alpha+beta)/sqrt(nm)
        =2S_0 S_1<=16M.                                  (11)

Adding diagonal terms in this last nonnegative upper bound is allowed;
none was divided by d. Multiplying T and (9), respectively, by the
coefficients and summing proves (3). Equal products have not been
identified as independent frequencies; summing all representations
only enlarges an absolute upper bound. No arithmetic cancellation is
claimed or needed for (10)--(11).

### 5. Comparison with the required leakage and scope of the stop

Since M/sqrt(T) tends to 1/sqrt(2pi), the explicit guaranteed bounds
in the last line of (3), divided by (c/2)T L^3, are respectively

    128 M/(c L^3) -> infinity,
    64 M(2L ell+1)/(c T L^3) ~128 M/(c L^2) -> infinity.

Using (1) to estimate variation has not earned any useful oscillatory
saving at this threshold. This compares upper budgets only. It gives
no lower bound on v or on the chirp integral; either could be much
smaller for the actual quotient.

For completeness retain the stronger known full-scale upper bound:
L477's finite algebra has

    V=2 Re(e^(2i theta)(P_0 P_2-P_1^2)).

Consequently |psi|<=1 and Cauchy--Schwarz give

    |integral V psi|<=2(||P_0||_2||P_2||_2+||P_1||_2^2)
                      <=C T L^3,

by L477's ||P_j||_2<=C_j sqrt(T)L^(j+1/2). This proves (4),
but certifies no constant C<=c/2 and no vanishing normalized bound.
It would be incorrect to report the larger derivative budget as a
new obstruction on the actual correlation while suppressing (4).

Finally integral |R|>=|integral R psi|, and (2) shows the conditional
use claimed above if the missing leakage estimate is provided.
L477's defect error is O(T L^(5/2))=o(T L^3), so c/4 is an eventual
valid lower constant in that conditional case. No such premise has
been established. The finite regularity, exact positive pairing and
failed direct derivative budgets are the entire result of this step.
This is a known-tool calculus specialization, not a claimed discovery
beyond the sources checked. Improving it requires additional structure
of the actual weight, not repetition of the same total-variation bound.

## Mathlib

Full matching and supporting Mathlib coverage are unchecked. Unknown
availability is not evidence of absence. This informal proof uses
finite convolution/Fubini, ordinary integration by parts, finite sums,
and L477/C481a/L574 with their stated imported-source qualifications.
L574's Curran v2 Lemma 2.3 and Mertens imports remain unaudited at the
source-proof level; they are not reproved or strengthened here.
