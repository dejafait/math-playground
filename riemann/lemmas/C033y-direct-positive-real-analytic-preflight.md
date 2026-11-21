# Corollary C033y: direct positive-real analytic preflight

## Hypotheses

Use C033w's exact eight transforms m(1),m(2),k(s,sigma), with
s in {1,2}, sigma in {1,3/2,2}. In particular, with multiplicities,

    H(u)=sum_(rho in Z+) exp(-u*z_rho^2),
    ell_sigma(t)=H(t/(1+4*sigma*t))/(t*sqrt(1+4*sigma*t)),
    B_sigma(s)=integral_0^infinity (1-exp(-s*t))*ell_sigma(t)dt,
    k(s,sigma)=exp(-B_sigma(s)).

For m(s), the exponent is the same width-one integral restricted to
(0,infinity)\[1,3/2]. Retain the actual divisor, conjugation and
multiplicity, excluded ordinate zero, |beta-1/2|<1/2, gamma>14, the
counting input below, real z_rho through100, a retained real zero in
(14,15), reciprocal-square tail, heat positivity and separate fixed-j
heat-error qualifications, both fixed-v1 qualifications, zero drift
and killing, and Gaussian half-variance. In particular the exact
exponents are real and nonnegative. No source-wide correctness or
finite-zero data is independently verified here.

Import C032s's qualified inequalities

    |N(v)-M(v)|<=4+log(v+2)/8, v>=0,
    M(v)=v/(2*pi)*(log(v/(2*pi))-1), M(0)=0,
    sum_(gamma>100) gamma^-2<1,

and C033u's enlarged-width explicit formula (5). Set

    a=2^-30, b=1/4, L=log(b/a)=28*log(2)<20,
    F(w)=p_w(0), w_sigma(y)=sigma+exp(-y)/4,
    g_s(y)=sqrt(pi)*exp(-y/2)*(1-exp(-s*exp(y))).

All quadrature nodes, weights, constants and elementary operations in
the analytic construction below are exact. Finite arithmetic is a
separate, unresolved requirement, not an implicit hypothesis that a
library achieves its requested tolerance.

## Conclusion

There is an explicitly specified exact-node quadrature expression
Q_(s,sigma) for the compact exponent integral on [a,b], with the
following uniform error allowances for each of the eight exponents:

    small Levy-time tail                    <2^-11,
    large Levy-time tail                    <2^-14,
    outer analytic Gauss quadrature          <2^-12,
    inner archimedean quadrature/truncation  <2^-12,
    omitted prime powers                    <2^-11.

Thus |Q-B|<25/16384<2^-9. The same Q_(s,1) approximates both
B_1(s) and the residual exponent, with their separately justified
tail errors; it does not identify those exact exponents. If its
finite arithmetic error is at most2^-10 and the final exponential
is computed with error at most2^-10, clamping the computed exponent
to [0,infinity) yields error <57/16384<2^-8 in each final scalar.

The exact construction uses780 profile positions,37440 variable-width
inner Gauss positions,272 fixed inner positions, at most14040 prime
summands,1560 outer weighted summands, and8 final exponentials. These
are named sampling/summation positions, NOT a certified aggregate
elementary-operation cost. At construction1800 the10^6-term preflight was INCOMPLETE:
certified node/weight generation, constants, cancellation-sensitive
profile arithmetic, elementary-function radii, final exponentials and
their complete cost remained unpaid. C033z subsequently supplies that
arithmetic construction. The separate application audit1806 below and
in C033z passes under the retained qualifications. No transform was evaluated.

This is a local quantitative specialization under saved assessment1799,
recorded19 November2026, with application audit1806 now passed. It pays an
analytic input, not the requested full evaluator, interpolation,
conditioning, TV<=2, a full-interval residual, cancellation, signed
height or actual-Xi positivity. It is not progress beyond the inspected
general source theorems, an algorithmic lower bound, or an RH candidate.

## Proof

### Imported identities and the remaining application work

Reuse C032s and C033u without reproving the counting theorem, Gaussian
transform, explicit formula or analytic Gauss rule. Precise sources are:

- Suvrit Sra, *On some positivity properties of the Riemann Xi function*,
  [2610.00584v1,20 October2026](https://hexagonmath.org/pdf/2610.00584v1),
  Section2.1(2.1)-(2.3), p3; Lemma2.1, pp3-4; PropositionB.1 and proof,
  p17. The counting consequence and zero data retain C032s's qualifications.
- Sra, *Some positivity properties of Riemann Xi under smoothing*,
  [2611.00345v1,11 November2026](https://hexagonmath.org/pdf/2611.00345v1),
  Proposition3.1(3.2)-(3.3), pp5-6, proof C.1 p21. Variance is2*sigma.
- Alain Connes, *Heat Expansion and Zeta*,
  [2402.13082v1, Section2(4)-(9), p4](https://alainconnes.org/wp-content/uploads/heat-zeta.pdf),
  through C033u(5), over the full complex divisor, not an RH spectrum.
- Fredrik Johansson, *Numerical integration in arbitrary-precision ball
  arithmetic*, [1802.07942v1, Sections2/2.1, pp2-3](https://arxiv.org/pdf/1802.07942v1).
  For a function holomorphic near a closed Bernstein ellipse of parameter
  rho=2 and bounded there by M, n-point Gauss error on an interval of
  length h is at most(h/2)*50*M*4^-n. We also use its positive weights,
  which sum to h. This is an exact-rule theorem, not a rounding contract.

The new work is the cutoff-specific endpoint allowance and regularized
inner/outer majorants. C033u's bound64 for a width DIFFERENCE is not
used for the undifferenced exponent. C033x and stops1781/1782 concern
different evaluators and remain unchanged.

### The small Levy-time tail

Write H_0(u)=sum exp(-u*gamma^2), L_u=log(1/u), and
A=1/(8*sqrt(pi))<1/12. C032s's Gaussian counting main integral is
I_0(u)=A*u^-1/2*(L_u-c), c=gamma_E+2*log(4*pi)>0.
Stieltjes integration by parts, with vanishing endpoints, gives

    |H_0(u)-I_0(u)|
      <=integral_0^infinity 2*u*v*exp(-u*v^2)
                                      *(4+log(v+2)/8)dv
      <(67+L_u)/16, 0<u<=1.                         (1)

Indeed, set x=sqrt(u)*v and use
log(v+2)<=L_u/2+log(x+2)<L_u/2+1+x/2. The two Gaussian
integrals needed are integral 2*x*exp(-x^2)=1 and
integral 2*x^2*exp(-x^2)=sqrt(pi)/2<1. The endpoints vanish
because M(0)=N(0)=0 and the Gaussian dominates the counting bound.

The strip gives |H(u)|<=exp(u/4)*H_0(u). For0<t<=a and
1<=sigma<=2, put d=1+4*sigma*t and u=t/d. Then1<=d<=2,
L_u<=log(1/t)+1, and exp(u/4)<9/8. Consequently

    |H(u)|/sqrt(d)
      <=(9/8)*[A*t^-1/2*(log(1/t)+1)
                              +(68+log(1/t))/16].     (2)

The factor d cancels exactly in the first term. Using
1-exp(-s*t)<=2*t and integrating (2), the omitted small-time
exponent is bounded in absolute value by

    (9/8)*[4*A*sqrt(a)*(log(1/a)+3)
                            +a*(69+log(1/a))/8]
      <9/32768+13/2^30<2^-11.                       (3)

Here log(1/a)=30*log(2)<21 and sqrt(a)=2^-15. This also
proves the needed absolute endpoint domination; no asymptotic O
constant or differentiated remainder has been used.

### The large Levy-time tail and exact residual restriction

For t>=b and1<=sigma<=2, u=t/(1+4*sigma*t) lies in[1/12,1/4].
The counting inequality gives N(100)<100: log(100)<5,
log(102)<8 and2*pi>6 suffice. The through100 input makes those
z_rho real, so their total absolute heat contribution is at most
100*exp(-196*u)<100*exp(-16).

For gamma>100, Re(z_rho^2)>=3*gamma^2/4, and hence

    gamma^2*|exp(-u*z_rho^2)|
       <=gamma^2*exp(-gamma^2/16)
       <=10000*exp(-625)<exp(-16).

The middle inequality follows by differentiation of x*exp(-x/16)
for x>=10000; the last follows from e>2 and10000<2^14.
Summing against the qualified reciprocal-square tail yields
|H(u)|<101*exp(-16). Since sqrt(1+4*sigma*t)>=2*sqrt(t),

    integral_b^infinity |(1-exp(-s*t))*ell_sigma(t)|dt
      <101*exp(-16)/sqrt(b)
       =202*exp(-16)<202*(3/8)^16<2^-14.             (4)

For the residual exponent the large domain is exactly
[b,infinity)\[1,3/2]. Its absolute integral is bounded by the
same majorant. The removed interval remains an absolutely continuous
Levy restriction; it introduces no endpoint atoms. Since b<1, the
compact residual integral equals the width-one compact integral.
No equality of the full residual and width-one transforms follows.

### Regularizing and scaling the archimedean integral

Use C033u's notation

    B(t)=exp(t/2)/(2*sinh(t)),
    I(w)=integral_0^infinity (exp(-w*t^2)-exp(-t/2))*B(t)dt,
    R(z)=exp(z/2)/(2*sinh(z))-1/(2*z), R(0)=1/4,
    J(w)=integral_0^infinity exp(-w*t^2)*R(t)dt.

The apparent pole of R at0 is removable by the power series. Its
other poles are at nonzero integer multiples of pi*i. On

    Re(z)>=-1/8, |Im(z)|<=3/8,

one has |R(z)|<3. To check this completely, first suppose |z|<=1
and write S(z)=sinh(z)/z. Then |S-1|<|z|^2/5 and |S|>4/5,
while |exp(z/2)-1|<|z|. Thus

    |R(z)|=|exp(z/2)-S(z)|/(2*|z|*|S(z)|)<3/4.

These inequalities extend to z=0 by continuity. The numerical bound
sinh(1)-1<1/5 follows, for example, from e<11/4 and e^-1>4/11;
e<11/4 follows by bounding the exponential series tail after degree4
by1/100. If |z|>1 in the displayed strip, x=Re(z)>7/8, and

    |B(z)|<=exp(-x/2)/(1-exp(-2*x))<2,
    |1/(2*z)|<1/2.

This proves the claimed bound in the second case as well.

The exact identity on Re(w)>0 is

    I(w)=I(1)-Log(w)/4+J(w)-J(1).                    (5)

Here Log is the principal logarithm on the right half-plane. To
justify (5), subtract I(1) before separating the1/(2*t) term.
The difference integral is convergent at both ends. Its1/(2*t)
part vanishes at w=1 and has derivative -1/(4*w), by dominated
differentiation on compact subsets of Re(w)>0. This proves its
value -Log(w)/4 there. The remaining difference is J(w)-J(1).
R is bounded on the positive real ray, so the J integrals and
their parameter derivatives have the same compact domination.
There is no splitting of the original divergent pieces at zero.

For real w>=1, scale x=sqrt(w)*t with the positive square root:

    J(w)=w^-1/2*integral_0^infinity
                            exp(-x^2)*R(x/sqrt(w))dx. (6)

This exact change of variables preserves0,infinity and supplies
a uniform, bounded inner integration problem even at enlarged widths.

### Uniform inner quadrature bounds

Approximate J(w) in (6) on[0,4] with four unit panels, each using
12-point Gauss quadrature; denote the result by Jhat(w). The
rho=2 ellipse of any unit panel has real extension1/8 and imaginary
semiaxis3/8. Scaling by1/sqrt(w)<=1 keeps it in the strip just
proved. Also |exp(-x^2)|<2 there. Thus the analytic integrand is
bounded by6 on every ellipse, including the removable point0, and

    |Jhat(w)-J(w)|<=E_J:=600/4^12+(3/8)*exp(-16).    (7)

The tail uses |R|<3 and integral_4^infinity exp(-x^2)dx<=exp(-16)/8;
the factor w^-1/2 is at most1. Use the same construction once for J(1).

Compute I(1) on[0,16] with sixteen unit panels of degree14. Its
integrand h(z)=(exp(-z^2)-exp(-z/2))*B(z) is holomorphic at0
and bounded by6 on the same ellipses. For |z|<=1 the numerator
is less than4*|z|, and |z*B(z)|<5/4, giving bound5. For |z|>1,
the second case above gives |B|<2, |exp(-z^2)|<2 and
|exp(-z/2)|<1, giving bound6. On the real ray t>=16,
|h(t)|<=4*exp(-t), so

    |Ihat(1)-I(1)|<=E_I:=2400/4^14+4*exp(-16).      (8)

In C033u(5), replace I(w) by
Ihat(1)-log(w)/4+Jhat(w)-Jhat(1). Its profile error, before
prime truncation or arithmetic, is uniformly less than

    (E_I+2*E_J)/(2*pi)
      <[2400/4^14+4*(3/8)^16
            +2*(600/4^12+(3/8)*(3/8)^16)]/6
      <2^-16.                                      (9)

All constants and square roots in this statement are still exact.

### The undifferenced outer ellipse and weighted error

On the20 equal logarithmic panels of[log(a),log(b)], each length
L/20<1, their rho=2 ellipses satisfy |Im(y)|<3/8 and
Re(y)>log(a)-1/8. Therefore Re(w_sigma(y))>1,
|w_sigma(y)|<2^30 and |Log(w_sigma(y))|<23.

For completeness, (5) gives an undifferenced bound |F(w)|<6 on
these domains. The pole term A(w) and c/(4*pi) in C033u(5) are
each less than1 in modulus. One has |I(1)|<3: on(0,1) its
absolute integrand is at most t+1/2, and on(1,infinity) at most
4*exp(-t). Also |J(1)|,|J(w)|<3 for Re(w)>=1. Finally C033u's
prime-series majorant is less than9 before its1/(2*pi) factor.
Together with (5) these give

    |F(w)|<2+9/6+9/6+23/24<6.                      (10)

For z=s*exp(y) in the right half-plane,
|1-exp(-z)|<=min(2,|z|). If r=exp(-Re(y)/2), this implies
|g_s(y)|<=sqrt(pi)*min(2*r,s/r)<4. The actual compact
exponent integrand g_s(y)*F(w_sigma(y)) is therefore holomorphic
and bounded by24 on all the ellipses. Use degree13 on each of
the20 panels. The exact outer quadrature error is less than

    (L/2)*50*24*4^-13<12000/4^13<2^-12.             (11)

The positive-weight sum of g_s at these real nodes is less than13.
Indeed the same quadrature theorem applied to g_s alone has error
<2000/4^13<1, while splitting the full positive real integral at
t=1/s and using1-exp(-s*t)<=min(1,s*t) gives

    integral_R g_s(y)dy<=4*sqrt(pi)*sqrt(s)<12.

Hence replacing all profile integrals with (7)-(8) contributes at
most13*2^-16<2^-12 to each outer sum, by (9). This pays the
DISCRETE weight sum; an integral bound alone would not suffice.

### Cutoff-adapted prime tails, including every prime power

At each exact real outer node evaluate all prime powers n<=N(w)
in C033u(5), with their exact von Mangoldt weights, where

    N(w)=2 if w>=128;
         4 if32<=w<128;
         8 if8<=w<32;
         16 if4<=w<8;
         32 if1<=w<4.

For the last case, and indeed for all w=sigma+r^2/4 with sigma>=1,
the weighted omitted prime contribution for a cutoff N>=4 is

    <=(1/(2*sqrt(pi)))*sum_(n>N) n^-1/2*exp(-(log n)^2)
    <=(1/(2*sqrt(pi)))*exp(-(log N)^2+log(N)/2).       (12)

The first inequality uses Lambda(n)<=log(n),
r*exp(-r^2*(log n)^2/4)<1/log(n), and the real Laplace
factor at most1. The second writes the summand as n^-2 times
exp(-l^2+3*l/2), decreasing for l>=log(N)>3/4, and uses
sum_(n>N)n^-2<=1/N. This dominates all omitted prime powers
by all integers and is the undifferenced version of C033u's tail argument.
For N=32 its exponent is less than -10, using
56/81<log(2)<25/36 from C033u.

For each smaller adaptive cutoff use instead Lambda(n)<=n and
the decreasing factor exp(-w*l^2+(5/2)*l). When log(N)>=5/(4*w),

    sum_(n>N) Lambda(n)*n^-1/2*exp(-w*(log n)^2)
       <=exp(-w*(log N)^2+(3/2)*log N).              (13)

At the respective lower widths128,32,8,4 and N=2,4,8,16,
the exponent in (13) is less than -20, by2/3<log(2)<7/10;
these same bounds verify the monotonicity condition. On the real
axis g_s<3. Including1/(2*pi), the weighted pointwise error is
therefore less than exp(-20)/2, which is smaller than the bound
exp(-10)/(2*sqrt(pi)) in (12). Thus all adaptive cases have a
common pointwise allowance, and the positive outer weights sum to L:

    E_prime <(20/3)*exp(-10)
            <(20/3)*(3/8)^10<2^-11.                (14)

There are18 prime powers through32. We count every one at each
of the780 profiles as an upper bound, granting no width sharing.
No prime-density asymptotic or individual zero coordinates enter.

### Conditional final radius, actual work and the missing contract

Add (3),(4),(11), the propagated (9), and (14). Their displayed
dyadic allowances sum to25/16384. For any nonnegative exact exponent
B, projection x -> max(0,x) cannot increase |x-B|, and exp(-x)
is1-Lipschitz on[0,infinity). Therefore the proposed two additional
arithmetic allowances2^-10 give final error less than57/16384.
This is conditional error propagation, not certification of those
allowances. It applies separately to all8 scalars, including both
different residual exponents.

The declared exact-node construction uses260 outer nodes shared by
the3 widths and the2 s-values. Thus it has780 profile positions,
780*48=37440 variable inner samples,224+48=272 fixed inner samples,
at most780*18=14040 prime summands,6*260=1560 weighted outer
summands, and8 final exponentials. The two residual compact sums reuse
the width-one sums, with the exact tail qualification already proved.
The sum53320 counts these positions only. It omits node/weight and
constant generation, per-position arithmetic, elementary expansions
and their rounding; it is neither a full operation count nor a runtime.

In particular the expression R(z)=B(z)-1/(2*z) can suffer cancellation
when z is small at enlarged widths. Analytic removability and the bound3
do not establish a finite-precision callback radius. Nor do a chosen
precision, requested tolerance or an integration eval_limit establish
the full10^6-term cost. No finite-arithmetic implementation has been
specified and proved here. The aggregate gate is therefore incomplete
and evaluation stops. These are essential mathematical/numerical
obligations, not a source-access blocker or a refutation of the method.

`python3 scripts/smoothed-law/direct_positive_real_preflight_1800.py`
saves the complete rational allowance comparisons, adaptive thresholds,
prime-power count, sample-position accounting and unresolved obligations
in `scripts/smoothed-law/direct_positive_real_preflight_1800.json`.
It evaluates no transform and no Gauss callback. Its checks establish
only the stated rational implications, not this proof or source inputs.

### Application audit1806 — 19 November2026

This is the separately approved SPECIALIZE1803 audit, reusing the
primary statements and proof cases recorded in source-notes1799/1804.
It checks the local application, not the source-wide correctness of
either fixed-v1 preprint, the counting consequence, or finite-zero data.
All hypotheses above remain in force. No analytic bound changes.

The heat/profile normalization is exact:
F(w)=H(1/(4*w))/sqrt(4*pi*w). With t=exp(y) and
w=sigma+1/(4*t), the product g_s(y)*F(w) is exactly
(1-exp(-s*t))*H(t/(1+4*sigma*t))/sqrt(1+4*sigma*t).
This is the exponent density after dt/t=dy. There is no missing factor
from pairing, positive ordinates or Gaussian half-variance. The residual
deletion[1,3/2] is disjoint from[a,b]; only its compact sum is shared.
The absolute tail estimate covers the restricted large domain separately.

The small-time integration by parts is justified by the qualified
counting bound and Gaussian domination. After x=sqrt(u)*v, its error
is at most4+L_u/16+1/8+sqrt(pi)/32<(67+L_u)/16.
The strip estimate uses absolute values and assumes no reality of
unverified zeros. At large time u lies in[1/12,1/4]; reality is used
only through100, and the reciprocal-square sum only beyond100.
Thus(3)-(4) retain those hypotheses and use no effective asymptotic
constant or differentiated O remainder.

Regularization(5) subtracts I(1) before separating the singular term.
The derivative -1/(4*w), base value0 and compact domination justify
-Log(w)/4 on the right half-plane. The strip avoids every nonzero pole
of R, and its removable value at0 handles ellipses containing0.
For(10), the prime bound can be checked directly from Lambda(n)<=n:
sum n^(-2)*exp(-l^2+(5/2)*l)<exp(25/16)<8<9.
Also |J(w)|<=3*integral_0^infinity exp(-x^2)dx<3 for Re(w)>=1.
The strict strip and right-half-plane margins provide holomorphy near
the closed ellipses required by the cited Gauss theorem. Exact positive
weights are used to prove the discrete bound sum weight*g_s<13;
an integral estimate alone has not been substituted for that bound.

Equation(12) bounds all omitted prime powers by all integers, with
the required decreasing factor above N>=4. For the four smaller
cutoffs the lower-width/logarithm bounds give decay strictly above20
and separately satisfy(13)'s monotonicity hypothesis. C033z's cutoff32
reduces the nonnegative omitted-prime component in the error triangle
inequality; it need not reduce the total signed error of a quadrature
sample. Its subsequent finite suppression has its own arithmetic charge.

The independent verifier
`python3 scripts/smoothed-law/direct_positive_real_audit_1806.py`
checks all five rational allowances, adaptive thresholds and their
25/16384 dyadic sum. Full evidence is in
`scripts/smoothed-law/direct_positive_real_audit_1806.json`.
The analytic proof is necessary in addition to this certificate; a
successful rational comparison does not verify an integral or an
imported theorem. No defect was found within the qualified application.
C033z's audit pays finite arithmetic separately. No scalar value,
interpolation, TV, signed-height or actual-Xi conclusion follows.

## Mathlib

Full matching coverage is unchecked and unknown. No formalization of
the qualified divisor inputs, explicit formula, quadrature callback,
regularized evaluator or arithmetic cost is claimed. The general tools
are imported through the precise sources above; this local analytic
specialization has passed the qualified application audit1806 above.
