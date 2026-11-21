# Corollary919s: the fixed quartic first-zero test has negative curvature at1

## Hypotheses

Let K(u)=exp(-u^4-u^2) on R and

    F(z)=integral_0^infinity K(t)cos(zt)dt.

Use the standard tools cited below. The numerical certificate assumes
correct CPython integer/Fraction arithmetic, libmpdec directed basic
operations, correctly rounded HALF_EVEN exp and representable-neighbor
operations. These software contracts are explicit qualifications and
were not independently formally verified. Recorded runtime:
CPython3.15.2/libmpdec4.0.1, precision70. No floating-point trigonometric
routine, sampled maximum, or unvalidated adaptive quadrature is used.

## Conclusion

K is positive, even and smooth, with (log K)''=-12u^2-2<0 everywhere.
For every integer m>=0 and B>0,
exp(B|u|)|K^(m)(u)| tends to zero at both infinities. F has a least
positive real zero x, which is simple and satisfies

    150761/32768 < x < 75381/16384 < 8.                     (1)

For u>=0 put

    G(u)=x integral_u^infinity K(t)sin(x(t-u))dt.             (2)

Its even extension is smooth and strictly positive, every derivative
has every fixed exponential decay rate, and its entire cosine
transform is F(z)/(1-z^2/x^2), with removable values at +/-x.
In particular it is the continuous integrable inverse kernel of that
quotient, rather than only a formal solution of an ODE.

The fixed curvature determinant satisfies the strict rational bounds

    -17109/1000000 < G(1)G''(1)-G'(1)^2 < -16709/1000000.    (3)

Thus (log G)''(1)<0. This test supplies no counterexample to
log-concavity preservation. It proves no log-concavity away from1,
no generic preservation theorem, and no actual-Xi or RH conclusion.
It is a source-supported fixed calculation with no claim of originality.
Audit2259 checked the numerical and analytic assembly under the stated
software contracts; it did not independently verify those contracts.

## Proof

### Sources, specialization, and admissibility

Use E.O. Tuck, *On positivity of Fourier transforms*, Bull. Austral.
Math. Soc.74(2006),133-138, pp133-134, equations(1)-(4), specifically
the strict positive decreasing-amplitude sine-transform result:
for a bounded continuous positive strictly decreasing integrable f
on[0,infinity), its sine integral is positive at every positive
frequency. Its half-period comparison proof was inspected in
source notes2257; it is not a curvature-preservation theorem.
Direct source: https://doi.org/10.1017/S0004972700047511 .

Differentiation under the integral uses K. Conrad, *Differentiating
under the integral sign*, author-hosted30-page version inspected
21November2026, Theorem12.3, p16:
https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf .
Fourier inversion uses T. Tao, *245C, Notes2: The Fourier transform*,
6April2009, Section3 Exercise30 and formula(11):
https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/ .
The fixed quadrature uses composite Simpson, NIST DLMF3.5(ii),
equations(3.5.6)-(3.5.8), https://dlmf.nist.gov/3.5.ii , and real
Taylor's theorem with Lagrange remainder (Strang--Herman, *Calculus
Volume2*, Section6.3, Theorem6.7):
https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series .
The relevant hypotheses and proof-read qualifications are retained
in source notes2249/2257; their ready coverage is reused.

No general tool is reproved. The explicit model hypotheses, errors,
first-zero condition and origin specialization must be checked here;
C919m's actual-theta hypotheses do not establish them. That result
serves only as a construction template, not a mathematical input.
L049/L050 and C919p/q do not decide this first-zero shape question.
No cross-notebook theorem or all-real-zero theorem for F is imported.

Write V(u)=u^4+u^2. Recursively, K^(m)=P_m K, where P_0=1 and

    P_(m+1)=P_m'-(4u^3+2u)P_m.                              (4)

Every P_m is a polynomial. Thus exp(B|u|)|P_m(u)|exp(-V(u))
tends to0 for every fixed m,B. Using rate B+1 also proves all
weighted derivative integrals are finite. This verifies the full
every-derivative/every-exponential hypothesis, not just Schwartz
decay. Positivity, evenness, analyticity and strict logarithmic
curvature including u=0 follow directly from K. Exponential moments
and polynomial weights dominate the cosine integral and every
z-derivative uniformly on each compact complex disk; F is entire.

### Root certification: complete finite integration errors

The reproducible computation is

    python3 scripts/real-zero-origin/quartic_first_zero_2258.py

Full evidence: scripts/real-zero-origin/quartic_first_zero_2258.json.
The certificate contains all148 census cells, all10 bisections,
derivative polynomials, errors, endpoint intervals, runtime contracts
and source checksum. Its reported status is NONPOSITIVE_CURVATURE,
with no failed setup or arithmetic assertions. The separate complete
cell inequality inspection is saved in
scripts/real-zero-origin/quartic_first_zero_inspection_2258.json.

Here are the whole-interval estimates underlying that certificate.
For m>=1 set k=ceil(m/4) and b_m=max{1,(k/2)^k}, and set b_0=1.
For 0<=t<=1, t^m K(t)<=1. For t>=1, writing s=t^4 gives

    t^m K(t) <= t^(4k) exp(-t^4)
              =s^k exp(-s) <=(k/e)^k <=(k/2)^k.

The elementary maximum follows by differentiating s^k exp(-s);
e>2 follows from its positive power series. Therefore the sum of
absolute coefficients of P_j weighted by b_m bounds |K^(j)|
globally. Applying the same estimate to tP_j+jP_(j-1) bounds
|(tK)^(j)|. From (4), for j=0,...,4 these bounds are respectively

    B_j:  1, 6, 42, 508, 5228;
    C_j:  1, 7, 54, 634, 12316.                             (5)

For every 0<=y<=8, the absolute fourth t-derivative of K(t)
times either cos(yt) or sin(yt), including a phase shift by-y,
is at most sum_(j=0)^4 binom(4,j)8^(4-j)B_j=53996.
The corresponding bound for -tK(t)sin(yt) is71772. These are
global polynomial bounds, not grid maxima.

Use h=1/512 and N=2048 panels on[0,4]. Simpson's C4 hypothesis
holds for all these analytic integrands; the even panel count and
whole-interval bounds give error at most4 h^4 D/180. Consequently
the errors for F and F' are, respectively, less than

    1.746101e-8 and 2.320934e-8.                            (6)

On[1,4] the same mesh has1536 even panels and error less than
1.309576e-8 for either shifted sine or shifted cosine integral.

The complete omitted tail also has an explicit bound. For t=4+s,
V(t)>=272+264s, since V'(t)>=264 for t>=4. Hence

    integral_4^infinity K(t)dt <= exp(-272)/264 <2.821e-121,
    integral_4^infinity tK(t)dt
       <=exp(-272)(4/264+1/264^2) <1.130e-120.              (7)

These cover F, F', and both shifted integrals, with no omitted
index or unbounded oscillatory endpoint.

All quadrature nodes and weights are exact rationals before outward
Decimal conversion. K(t) is enclosed by evaluating exp on outward
neighbors of its rational exponent, rounding HALF_EVEN, then taking
one outward representable neighbor. Monotonicity of exp and its stated
rounding contract ensure inclusion. The trigonometric increment has
0<=yh<=1/64. The sine polynomial through degree25 and cosine
polynomial through degree24 have a common absolute Taylor remainder
at most(yh)^26/26! (the degree25 cosine coefficient is0).
Their polynomial sums are exact Fractions; endpoints include this
remainder. Starting from sin(0)=0, cos(0)=1, outward interval
evaluation of the angle-addition recurrences encloses every node.
For the shifted integrals it starts again at t=1, phase0. Every
rounding/wrapping error remains inside those intervals. Simpson's
error and (7) are added outward to the finite interval sums. No
approximate trigonometric node is treated as exact.

### Every smaller positive zero is excluded

Dominated differentiation gives |F''(y)|<=integral_0^infinity t^2K(t)dt<1
for real y. Indeed K<=exp(-t^2); integration by parts makes that
Gaussian second moment half its zeroth moment, which is less than
(1+exp(-1)/2)/2<1 by splitting at1 and using t>=1 on the tail.
All endpoints vanish by Gaussian decay. This is also a Lipschitz
bound of1 for F'.

On a frequency interval of length d=1/32 the real interpolation
remainder is bounded by d^2/8=1/8192. Thus if both endpoint lower
bounds exceed this amount, the entire cell is strictly positive.
All first147 cells, covering[0,147/32], meet this test. The smallest
certified interpolation margin exceeds0.00031823 (cell146 in
zero-based indexing); F(0)>0 is included in the census.

The next cell is[147/32,37/8]. Its endpoint enclosures imply

    F(147/32)>0.00044030,    F(37/8)<-0.00146124.

At its midpoint the certificate bounds F' above by
-0.06084930249; adding its radius1/64 times the Lipschitz bound1
gives F'<-0.04522430249 throughout the cell. Therefore it has
exactly one zero, this zero is simple, and none smaller is positive.
The intermediate value theorem and this strict derivative bound
justify the census; a sign change alone would not suffice.

Ten signed bisections within this same cell give (1). The final
endpoint certificates read

    F(150761/32768)>9.8579158e-7,
    F(75381/16384)<-8.5631636e-7.                            (8)

All inequalities displayed here are weakened outward from the full
certificate. The root interval lies inside the already proved
monotonicity cell, so no later simplicity or uniqueness assumption
is introduced by the bisection.

### The actual inverse, complete tails, and origin

For every fixed B>0 the finite constant
M_B=integral_0^infinity exp(Bt)K(t)dt gives
T(u)=integral_u^infinity K(t)dt<=M_B exp(-Bu). In (2), ordinary
differentiation of its endpoint and integrable trigonometric factors
is justified uniformly on compact u intervals by a constant times
K(t); the endpoint sine vanishes. It gives

    G'(u)=-x^2 integral_u^infinity K(t)cos(x(t-u))dt,
    G''(u)=x^2(K(u)-G(u)).                                  (9)

Thus |G|<=xT and |G'|<=x^2T. Iterating (9) gives
G^(m+2)=x^2(K^(m)-G^(m)). Together with (4), this proves
|G^(m)(u)|<=C_(m,B)exp(-Bu) for every fixed m,B. Applying rate
B+1 proves every polynomially weighted exp(Bu) integral finite
and each exp(Bu)G^(m)(u)->0. The differentiation uses an open
neighborhood in u by the same formula with its signed lower limit;
K is entire on the real line, so the endpoint0 causes no missing
one-sided hypothesis. Alternatively (9) extends the derivatives
continuously to0.

The exact root condition, not a nearly zero decimal value, gives
G'(0)=-x^2 F(x)=0. All odd derivatives of K vanish at0. Induction
in (9) with odd m proves all odd derivatives of G vanish there.
Its even extension is consequently C-infinity across0, without an
unpaid cusp or delta mass. For u>=0, K(u+t) is bounded, continuous,
positive, strictly decreasing on t>=0 and integrable. Strict decrease
includes u=t=0 because V(b)>V(a) whenever0<=a<b. Tuck therefore
gives G(u)>0, including0; evenness covers the negative half-line.
No first-zero assertion was needed for this sine positivity, but the
exact root was essential at the origin.

Let Q(z)=integral_0^infinity G(u)cos(zu)du. The complete exponential
tails, including polynomial weights, make Q entire and permit two
integrations by parts for complex z. They give

    integral_0^infinity G''(u)cos(zu)du =-z^2 Q(z),
    (x^2-z^2)Q(z)=x^2 F(z).                                (10)

The first boundary term is-G'(0)=0; all infinity terms vanish at a
decay rate greater than |Im z|. The sine boundary at0 is0.
Thus Q is precisely the entire quotient, removing one simple factor
at each of +/-x. The simple root established above is sufficient;
no assumptions about other zeros have entered. A difference of two
decaying half-line ODE solutions is A cos(xu)+B sin(xu); evaluating
on their two quarter-period sequences shows A=B=0. This also fixes
the homogeneous ambiguity.

For real y, (10)'s integration-by-parts identity implies
|Q(y)|<=||G''||_1/y^2 when y!=0, while |Q|<=||G||_1 everywhere.
So Q is integrable. The smooth even extension of G and its first
two derivatives are integrable and locally absolutely continuous.
In Tao's Fourier convention its transform is2Q(2*pi*eta);
inversion therefore gives G(u)=(2/pi)integral_0^infinity Q(y)cos(yu)dy
at every real u. This pays the inverse interpretation and normalization.

### The single curvature enclosure and its limitation

Set c=301523/65536 and r=1/65536, the midpoint and radius of(1).
For y in that root interval define

    A(y)=integral_1^infinity K(t)sin(y(t-1))dt,
    B(y)=integral_1^infinity K(t)cos(y(t-1))dt.

Their y-derivatives are absolutely bounded by
integral_1^infinity (t-1)K(t)dt <=integral_1^infinity t exp(-t^2)dt
=exp(-1)/2<1/2. The same bound justifies differentiation under the
integral on an open neighborhood of this compact interval. Therefore
enclosing A(c),B(c) by Simpson plus (7) and adding radius r/2
covers A(x),B(x), without treating the approximate root as exact.
Using (9) gives G(1)=xA(x), G'(1)=-x^2B(x), and
G''(1)=x^2(exp(-2)-G(1)). The complete outward enclosures imply

    0.03370892 < G(1) < 0.03377948,
    -0.29928826 < G'(1) < -0.29896072,
    2.14972505 < G''(1) < 2.15124695.

The full intervals, rather than these weakened display bounds,
are multiplied/subtracted to obtain

    -0.017108533136863 < Delta < -0.016709525820705,

which proves(3). Since G(1)>0, logarithmic curvature has the sign
of Delta. The required counterexample threshold Delta>0 is missed
strictly. The fixed test is closed without retuning; its negative
result concerns only this member and this spatial point. The
generic first-zero invariant, actual-Xi hypotheses, repeated-removal
closure and all-degree transfer remain unresolved. No finite sign
or equivalent criterion is substituted for RH.

### Audit2259: complete evidence and analytic interfaces

Reproduction command:

    python3 scripts/real-zero-origin/audit_quartic_first_zero_2259.py

Full audit evidence is in
scripts/real-zero-origin/quartic_first_zero_audit_2259.json;
the isolated full replay is in
scripts/real-zero-origin/quartic_first_zero_replay_2259.json.
The audit passed981 recorded checks with no failure. It preserved
the original source and certificate byte for byte. A parsed copy of
the source redirected only its output assignment; every certificate
field other than runtime was compared for exact equality. This is a
replay, not an independent numerical algorithm or a verification of
CPython/libmpdec. Both executions retain the explicit contracts above.

Independent sparse integer polynomial arithmetic reproduced every
P_j and the rational B_j,C_j bounds in(5), then recomputed the two
complete fourth-derivative bounds and all three Simpson errors.
Exact Fraction comparisons checked every census interval's endpoint
ordering, contiguous frequency endpoints and identical shared
enclosures, all147 strict interpolation margins and the final
whole-cell derivative estimate. All10 bisection midpoints and signs
were checked in order, including their final endpoint evidence,
midpoint and radius. The audit also checked complete tail majorants,
the even panel counts and exact shifted range, both root-radius
inflations, every outward product/subtraction in the curvature
assembly and each displayed strict numerical bound in this proof.
The full certificates, not a bounded JSON preview, were consumed.

The trigonometric recurrence uses old sine and cosine intervals on
both right-hand sides of Python's simultaneous assignment. Thus it
implements angle addition with a common enclosed increment, with no
use of an updated sine interval to form cosine. The degree25 real
Taylor remainder is valid for cosine as well as sine: cosine's
degree25 coefficient is zero and both derivatives of order26 have
absolute value at most1 on the real line. The error-inflated base
increment and outward basic operations therefore enclose every
successive node, regardless of interval dependency or wrapping.
For exp, enclosing a rational exponent before evaluation and then
enlarging each correctly rounded HALF_EVEN endpoint by a neighboring
representable value is outward by monotonicity. No reliance on the
global Decimal context's default rounding enters these operations.

The analytic audit checked the following load-bearing distinctions.
Every weighted derivative integral follows from a strictly larger
exponential decay rate; mere boundedness at the chosen rate would
not prove integrability. Differentiation of(2) can be justified by
splitting at a fixed finite endpoint on a compact u-neighborhood:
the finite part obeys the ordinary Leibniz rule and the fixed tail
has parameter-independent K(t) majorants. This covers an open real
neighborhood of0 as well as positive u. The recurrence(9) then gives
all higher derivatives and their tails. Exact F(x)=0 gives G'(0)=0;
the odd cases of the same recurrence give every remaining odd
derivative at0. Hence even extension introduces no boundary mass.
Tuck's theorem applies to the strictly decreasing translated K even
when u=0, where a zero derivative at the endpoint does not prevent
strict decrease. The census, separately, makes x the least positive
root and proves simplicity without an all-real-zero assumption.

Finally, on each complex z disk the exponential tail bounds dominate
G, G' and G'' multiplied by cosine or sine. Both integration by
parts boundary terms in(10) are therefore paid. The exact origin
condition removes the only potential boundary correction, so the
entire quotient follows with no homogeneous addition. Its real-axis
L1 bound follows from G'' in L1 and the O(1/y^2) identity, together
with boundedness near0. Fourier inversion uses the even real kernel
and the factor2 and angular-frequency change stated above. These
checks validate only the specialized result(1)-(3); they supply no
comparison of curvature at other spatial points or other kernels.

## Mathlib

Full matching coverage was not checked and is not asserted absent.
The named standard calculus, Fourier and quadrature tools above are
the precise imports; no Mathlib theorem is used as a premise. Their
possible supporting formalizations would not themselves prove the
root census, error bounds or specialized curvature inequality.
