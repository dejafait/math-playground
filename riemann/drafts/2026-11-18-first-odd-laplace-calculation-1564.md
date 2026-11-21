# First-odd widths-1,2 Laplace test1564 — locally inconclusive

18 November 2026. Authorized scope: unchanged SPECIALIZE assessment1562.
This is a calculation of classical necessary conditions, not a proposed
RH argument or a claim of a new theorem. Preserve all external-input
qualifications in C032j/m/q/s/t/u and the finite-family stop1302.

Main gap: actual-Xi all-degree positivity in L030-L032/C032a. The one
intermediate target is the mass-one two-width law with J_eta'(0)=0.
Its possible use is discrimination of one constrained building block
for C032q. A strict wrong sign excludes this law; favorable signs or
uncontrolled constants stop this local test as inconclusive. No automatic
increase of derivative order, number of widths or cancellation order.

Write P_j=p_j(0), c_j=2*pi*P_j, e_j=2*R_j(0), T_j=p_j''(0)/P_j,
for half-variances j=1,2. Here c_j denotes the linear lift coefficient.
From C032m,

    b_j(w)=c_j*w+e_j*w^2-c_j*T_j*w^3/6+O_hol(w^4).

C032t gives K'<0 on (0,1/4]; since c_j=2*sqrt(pi)*K(1/(4*j)),
0<c_1<c_2. The unique mass-one solution is

    a_1=c_2/(c_2-c_1), a_2=-c_1/(c_2-c_1).

For F=a_1*exp(-b_1)+a_2*exp(-b_2), its linear term is zero.
The quadratic and cubic coefficients to test are

    A=-(e_1-r*e_2)/(1-r)-c_1*c_2/2, r=c_1/c_2,
    C=(c_1*c_2/(c_2-c_1))*
        ((T_1-T_2)/6+e_1-e_2+(c_2^2-c_1^2)/6).

The estimates established below are r<10^-6, e_1>1/2000, |e_j|<2,
T_1>48 and T_2<25. Hence A<0 and C>0. Both necessary derivative
tests pass for sufficiently small positive s; the approved exclusion
test stops as inconclusive. Output positivity is still unresolved.
This calculation is retained as an attempt, without creating a lemma
for favorable necessary conditions or altering the main argument.

## Inputs and elementary tail certificate

Use C032s's already assessed counting inequality, its (8), and C032j's
verification through height 100. Thus zeros with gamma<=100 are real
in the z coordinate, every gamma>14, at least one gamma is in (14,15),
and sum_(gamma>100) gamma^(-2)<3/25. Multiplicities are retained.
The counting inequality gives N(100)<40: its main term is <100/3
because pi>3 and log(100/6)<3; its error is <37/8 because log(102)<5.
Both elementary logarithmic comparisons follow from e>8/3.
These inputs remain qualified external inputs, not fresh zero-data
verification. All sums below count the full divisor.

Put epsilon=10^(-100), b=3/8. For 0<=k<=4 and a>=1/32,

    sum_(gamma>100) 4*gamma^k*exp(-a*(gamma-1)^2)
      <=(12/25)*100^6*exp(-9801/32)
      <(12/25)*100^6*b^306<epsilon.                 (1)

Indeed gamma^(k+2)*exp(-a*(gamma-1)^2) is decreasing for gamma>=100:
its logarithmic derivative is (k+2)/gamma-2*a*(gamma-1)<0.
Multiply its supremum by the reciprocal-square tail. The deliberately
larger factor 100^6 covers every indicated k. This bound controls each
high-zero quantity below, including polynomial factors from two
Gaussian derivatives. The exact rational final inequality, and every
other numerical comparison below, is checked in
scripts/smoothed-law/first_odd_laplace_1564.py, with full certificate
scripts/smoothed-law/first_odd_laplace_1564.json. Decimal previews are
not used as proof; all comparisons use rational numbers and
8/3<e<3, 3<pi<4, exp(1/16)<16/15.

For j=1,2, the elementary complex Gaussian formula gives

    |G_j(x-gamma+i*delta)|
      =exp(delta^2/(4*j))*G_j(x-gamma).

At x=0, and for two x derivatives at zero, every high-zero summand is
bounded by the summand in (1). This also holds for |p_j''(x)| on
0<=x<=1: use |x-gamma|>=gamma-1 and |delta|<1/2. Thus each of these
high-zero sums has absolute value less than epsilon. On any compact
x interval all differentiations are legitimate by C032m. Conjugate
symmetry makes each total profile and its derivatives real.

## Origin profiles and normalized second derivatives

The finite real-zero part gives

    P_1<41*exp(-49),       P_1>(1/5)*exp(-225/4),
    P_2<41*exp(-49/2),     P_2>(1/7)*exp(-225/8).       (2)

For the upper bounds use at most 40 terms with gamma>14 and
1/sqrt(4*pi*j)<1. For the lower bounds retain the real zero with
gamma<15: its terms at zero coincide after the factor 1/2 and have
prefactors >1/4 and >1/6, respectively. Subtract epsilon for the high
zeros. The certificate checks epsilon<(1/20)*3^(-57) and
epsilon<(1/42)*3^(-29), which absorb these errors using e<3; it also
checks the upper error absorptions. Consequently

    0<r=P_1/P_2<287*exp(-167/8)
        <287*b^20<10^(-6).                              (3)

For a real zero, its contribution to p_j''(0) divided by its
contribution to P_j is gamma^2/(4*j^2)-1/(2*j). For j=1 this exceeds
48.5. Hence p_1''(0)-48*P_1 is at least
(1/8)*exp(-225/4)-49*epsilon>0, by (1)-(2) and the rational certificate.
Thus T_1>48.

For j=2, zeros with gamma<=20 have this ratio <=24.75. For the
remaining real zeros through 100, the positive contribution to
p_2''(0)-24.75*P_2 is bounded by

    40*sup_(y>=20) (y^2/16)*exp(-y^2/8)
      =1000*exp(-50).

The high zeros cost <26*epsilon. Dividing by the lower bound on P_2
in (2) gives

    T_2<=24.75+7000*exp(-175/8)+182*epsilon*exp(225/8)
        <24.75+7000*b^21+182*epsilon*3^29<25.             (4)

This handles the off-line tail without treating its individual
summands as positive.

## Bounds on the quadratic exponent coefficients

The convergent definition from C032m is

    R_j(0)=integral_0^infinity (p_j(x)-P_j)/x^2 dx,
    e_j=2*R_j(0).

For x in [0,1], Gaussian differentiation bounds each low-zero term
of |p_j''(x)| by

    (32/15)*gamma^2*exp(-(gamma-1)^2/8).

The expression decreases for gamma>=14. Adding at most 40 such
terms and (1), the resulting bound is
(40*32/15)*196*b^21+epsilon<1/1000. Since p_j'(0)=0, the absolute
contribution to R_j(0) from [0,1] is <1/2000. Also P_j<1/1000 by (2).

Let S2=40/196+3/25 and Sexp=40*b^6+epsilon. Then
sum gamma^(-2)<S2 and sum exp(-gamma^2/32)<Sexp. Splitting the first
translated Gaussian at x=gamma/2 gives

    integral_1^infinity |p_j(x)|/x^2 dx
       <=(16/15)*(2*S2+Sexp).                            (5)

For precision, in x>=gamma/2 use x^(-2)<=4/gamma^2 and integrate
G_j over the whole real line; the factor 1/2 in the profile gives
2/gamma^2. In 1<=x<gamma/2 use
G_j(x-gamma)<=exp(-gamma^2/32), with integral_1^infinity x^(-2)dx=1.
The other translate has G_j(x+gamma)<=exp(-gamma^2/8). The two
remaining half factors sum to at most exp(-gamma^2/32). The complex
modulus factor is at most exp(1/16)<16/15. Tonelli applies to these
positive bounds. Thus

    |e_j|<2*(1/2000+1/1000+(16/15)*(2*S2+Sexp))<2.        (6)

For a positive lower bound on e_1 we must not assume p_1>=0.
The real-zero profiles are nonnegative everywhere; on [0,1] their
second derivatives are positive since |x+/-gamma|>13. Their
contribution to (p_1(x)-P_1)/x^2 there is nonnegative. The high-zero
part of this integral is >-epsilon/2 by its second derivative bound.

On [1,infinity), retain the real zero gamma_* in (14,15). For
gamma_*<=x<=gamma_*+1 its profile contribution is greater than
(1/2)*(1/4)*exp(-1/4)>3/32. The integral against x^(-2) over this
unit interval is therefore >3/8192. All other low-zero profiles
remain nonnegative. Subtract the entire P_1, whose integral against
x^(-2) on [1,infinity) is P_1<41*b^49<10^(-9).

To bound negative high-zero profiles on this interval, write their
first translate as

    Re G_1(x-gamma+i*delta)
      =exp(delta^2/4)*G_1(x-gamma)*cos((x-gamma)*delta/2).

It is nonnegative when |x-gamma|<=6, since the phase has absolute
value <=3/2<pi/2. In x>=gamma/2 the integral of its possible negative
part is at most

    (2*exp(1/16)/gamma^2)*integral_(|y|>6) G_1(y)dy
       <(4/9)*exp(1/16)*exp(-9)/gamma^2.

Here integral_6^infinity exp(-y^2/4)dy <=exp(-9)/3 and
sqrt(4*pi)>3. The half factor from the profile has already been
included. The portions 1<=x<gamma/2 and the second translate have
total high-zero integral <2*epsilon, by (1), using respectively
exp(-gamma^2/16) and exp(-gamma^2/4) as envelopes. Therefore the
total negative high-zero integral is less than

    (16/15)*(4/9)*(3/25)*b^9+2*epsilon<1/100000.

Combining these signed estimates proves

    R_1(0)>3/8192-1/100000-1/10^9-epsilon/2>1/4000,
    e_1>1/2000.                                         (7)

No pointwise positivity of the entire profile has been used.

## Signs and holomorphic remainder

The coefficient formulas at the start, together with (3)-(7), give

    A<-(1/2000-2/10^6)=-249/500000<0,
    C>(11/6)*c_1*c_2/(c_2-c_1)>0.                        (8)

For the second inequality use (T_1-T_2)/6>23/6, e_1-e_2>1/2000-2,
and c_2^2-c_1^2>0. The coefficient calculation uses convergent
Taylor series of entire functions, rather than endpoint moments.

Set M=V*exp(K_1), V=|a_1|+|a_2|, with C032m's finite disk bound
K_1. On |w|<=1, |F(w)|<=M; hence its coefficients f_n satisfy
|f_n|<=M by Cauchy's formula. Here f_0=1, f_1=0, f_2=A, f_3=C.
The convergent differentiated series, for real 0<w<=1/2 and s=w^2,
give

    |L'(s)-A|<=4*M*w,
    |L''(s)-3*C/(4*w)|<=9*M.                             (9)

For the first estimate, sum n*M*w^(n-2)/2 for n>=3, bounded by
M*w*sum_(k>=0)(k+3)*2^(-k)/2=4*M*w. For the second, sum
n*(n-2)*M*w^(n-4)/4 for n>=4, bounded by
M*sum_(k>=0)(k+4)*(k+2)*2^(-k)/4=(17/2)*M<9*M.
This explicitly controls derivatives of the holomorphic remainder;
no arbitrary real big-O estimate is differentiated.

In particular, for

    0<w<min(1/2, -A/(8*M), C/(24*M)),

both L'(w^2)<0 and L''(w^2)>0 hold. The threshold is positive and
finite under the retained inputs; a useful effective value is not
claimed. C032q supplies L(s)=F(sqrt(s)) as the bounded Laplace
transform of the signed output. Under the additional hypothetical
assumption that this output is positive, Mimica2015 Proposition1.4(i),
pp6-7, https://web.math.pmf.unizg.hr/~amimica/lt.pdf, requires exactly
these signs. We import that known necessity from assessment1562;
we do not reprove it, assert its sufficiency, or exchange divergent
signed moments.

## Decision, qualifications and verification

The unique constrained law passes both approved local necessary
tests. This is new evidence against this particular sign-exclusion
diagnostic, which is now stopped as inconclusive. It proves neither
all-Borel positivity nor full J_eta=0. Indeed C032l still excludes
full odd cancellation in this finite family. No density, exponential
moment, RH, actual-Xi realization, or higher-order/global sign is
inferred. The main argument and its independent gaps are unchanged.

The rational certificate has 16 checks and no failures. It verifies
only the elementary bounds in this calculation, conditional on the
analytic reductions and qualified input results above. It does not
independently verify Sra's preprints, Bellotti-Wong's counting input,
finite zero data or heat positivity. Full matching Mathlib coverage
is unchecked and unknown. This is a classical-criterion specialization,
not certified novelty or a new result beyond the sources checked.
