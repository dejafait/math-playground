# Corollary C033a: zero-mean gamma integral and fixed Fourier tail

## Hypotheses

Let sigma be real in[1,2] and w complex with |w|<=2. Use precisely
C032z's integrated pair h(a)=e_(sigma,a)(w), with its ordinary Fourier
convention hat(h)(y)=integral_R h(r)*exp(-2*pi*i*r*y)dr. Its audited
equations(2)-(4)/(10) give, with C=8+704*exp(121/32),

    q(v)=exp(-sigma*v^2)*(cosh(w*v)-1)/v, v>0; q(0)=0,
    h(a)=-2*integral_0^infinity q(v)*cos(a*v)dv,
    |h(r)|<=C/(1+r^2), r real,
    hat(h)(y)=-2*pi*q(2*pi*|y|), including hat(h)(0)=0,
    |q(v)|<=2*v*exp(-v^2+2*v), v>=0.                    (1)

In particular h is even, complex-valued in general, in L1(R), and
integral_R h=0. These are existing inputs, not formal Fourier rules
or conclusions inferred from this corollary. Define

    Gamma_sigma(w)=integral_R
                      h(r)*Re psi(1/4+i*r/2)dr/(4*pi).  (2)

For its use as the gamma contribution in C032z's actual-divisor formula,
retain that formula's multiplicities, no-ordinate-zero condition,
strip/counting assumptions and normalization. Probability-law use
additionally retains the finite-zero, heat and fixed-v1 source
qualifications of C032j/m/q. The analytic identity here requires no
RH, zero coordinates, real-valued h or heat positivity. It does not
independently verify those external source data.

Import NIST DLMF, Section5.9(ii),
[equation5.9.16](https://dlmf.nist.gov/5.9.E16), with its Re(z)>0
hypothesis preceding equations5.9.12-16:

    psi(z)+gamma_E=integral_0^infinity
                    (exp(-t)-exp(-z*t))/(1-exp(-t))dt.  (3)

This is the exact source identity covered in assessment1608 (recorded
version1.2.8, 15 September2026); its domain and formula were also
checked at the primary page in this attempt. The combined-integrand
exchange below is a specialization to(1), not a reproof of(3).

## Conclusion

There is an ordinary, absolutely convergent representation

    Gamma_sigma(w)=integral_0^infinity I_(sigma,w)(v)dv,
    I_(sigma,w)(v)=exp(-sigma*v^2-v/2)*(cosh(w*v)-1)
                           /[v*(1-exp(-2*v))], v>0,
    I_(sigma,w)(0)=w^2/4.                              (4)

The endpoint value is the continuous right extension, uniformly in
the full closed parameter set. No principal value, distribution or
singular correction is present. With precisely the cutoff16,

    sup_(sigma in[1,2], |w|<=2)
       |Gamma_sigma(w)-integral_0^16 I_(sigma,w)(v)dv|
          <=4*exp(-128)<4/129<1/16.                    (5)

Thus the fixed analytic gamma-tail benchmark passes. Finite arithmetic
and quadrature on[0,16], the pole/prime terms, O_sigma evaluation,
coefficient amplification and dictionary1570's residual<1/2 remain
unpaid. Neither positivity of this complex expression nor positivity
of the full evaluator follows. This is REPRODUCTION/specialization
under the prior SPECIALIZE assessment1608, with a new local effective
input but no claim of discovery beyond the sources checked. Separate
critical audit1611 below validates these claims without correction.
No full odd cancellation, arbitrary-variation
exclusion, unsmoothed Xi realization or RH candidate is supplied.

## Proof

### 1. A uniform integrable bound for the combined integrand

For every real r, z=1/4+i*r/2 has positive real part. Take the real
part of(3) before multiplying by h(r). Its pointwise identity is

    Re psi(1/4+i*r/2)+gamma_E
       =integral_0^infinity
          [exp(-t)-exp(-t/4)*cos(r*t/2)]/[1-exp(-t)]dt. (6)

Taking the real part here is legitimate in the convergent source
integral for fixed r. No operation Re(h*psi)=h*Re(psi) is asserted.
We will prove absolute integrability of the product of h(r) with the
combined integrand of(6) on R times(0,infinity).

First, integral_R |h(r)|dr<=C*pi by(1). For0<t<=1 retain

    exp(-t)-exp(-t/4)*cos(r*t/2)
      =[exp(-t)-exp(-t/4)]+exp(-t/4)*[1-cos(r*t/2)].

The first difference has modulus at most3*t/4, by the mean value
theorem for exp(-x) on[t/4,t]. For real u,
0<=1-cos(u)<=min(u^2/2,2). Splitting at |r|=2/t therefore gives

    B(t):=integral_R |h(r)|*|1-cos(r*t/2)|dr
      <=(C*t^2/8)*integral_(|r|<=2/t) r^2/(1+r^2)dr
         +2*C*integral_(|r|>2/t) 1/(1+r^2)dr
      <=(C*t^2/8)*(4/t)+2*C*t
       =(5/2)*C*t.                                   (7)

For the last tail comparison replace1/(1+r^2) by1/r^2; its integral
over the two tails is t. Thus(7) uses no finite absolute first or
second moment of h. Also exp(t)>=1+t implies
1-exp(-t)>=t/(1+t)>=t/2 on this interval. Consequently

    integral_R |h(r)|*
      |exp(-t)-exp(-t/4)*cos(r*t/2)|/[1-exp(-t)]dr
         <=(3/2)*C*pi+5*C,              0<t<=1.        (8)

For t>=1, the denominator is at least1-exp(-1)>1/2, since e>2.
As |cos(r*t/2)|<=1, the same r integral is at most

    2*C*pi*[exp(-t)+exp(-t/4)],          t>=1.         (9)

The bounds(8)-(9) are integrable in t and independent of sigma,w.
Tonelli applied to the absolute value proves that the combined
complex integrand is in L1 of the product measure. Fubini now applies
to it. Equation(6) and h in L1 also prove absolute convergence of(2)
(alternatively C032z's logarithmic digamma bound already gives it).
No two nonintegrable endpoint terms have been integrated separately.

### 2. Zero mean, Fourier normalization and the change of variable

Integrate(6) against h(r) and use the justified exchange. The constant
gamma_E disappears because integral_R h=0. For each fixed t>0 the
inner r integrals are absolutely defined, so their constant piece
exp(-t)*integral_R h vanishes there, before integration in t. Hence

    Gamma_sigma(w)=-(1/(4*pi))*integral_0^infinity
       exp(-t/4)/(1-exp(-t))*
                     [integral_R h(r)*cos(r*t/2)dr]dt. (10)

The inner cosine transform equals hat(h)(t/(4*pi)): evenness of h
makes the sine integral zero, also for complex h. By the ordinary
transform in(1), it is exactly -2*pi*q(t/2). This minus sign cancels
the one in(10), and its2*pi cancels half of4*pi. Thus

    Gamma_sigma(w)=(1/2)*integral_0^infinity
                         exp(-t/4)*q(t/2)/(1-exp(-t))dt
                  =integral_0^infinity
                         exp(-v/2)*q(v)/(1-exp(-2*v))dv,

where v=t/2 and dt=2*dv. Substituting q proves(4) for v>0.
The absolute integrability proved before(10) survives the inner
integration and change of variable; this is an ordinary integral.

At the origin, C032z's audited expansion is
q(v)=w^2*v/2+O(v^3), uniformly on sigma in[1,2], |w|<=2. Together
with exp(-v/2)=1+O(v) and1-exp(-2*v)=2*v+O(v^2), it gives

    I_(sigma,w)(v)=w^2/4+O(v), v down to0,

uniformly on that parameter set. This proves the claimed extension
and its boundedness near0. At w=0, h,q,I and Gamma all vanish
identically, including that endpoint. The cusp in hat(h) has produced
a finite one-sided value; no smooth Mellin-test hypothesis is used.

### 3. The fixed uniform tail benchmark

For v>=16, exp(2*v)>=1+2*v>=33>2, so1-exp(-2*v)>1/2. Apply
the q bound in(1), retaining the factor exp(-v/2):

    |I_(sigma,w)(v)|
       <=4*v*exp(-v^2+(3/2)*v)
       <=4*v*exp(-v^2/2), v>=16.                     (11)

The second inequality follows from v>=3, which implies
(3/2)*v<=v^2/2. Therefore

    integral_16^infinity |I_(sigma,w)(v)|dv
       <=integral_16^infinity 4*v*exp(-v^2/2)dv
        =4*exp(-128).                                (12)

Finally exp(128)>1+128=129, and64<129. These exact elementary
comparisons prove4*exp(-128)<4/129<1/16, with no floating-point
approximation. Bounds(8)-(12) include both width endpoints and the
entire complex disk. The tail error in(5) follows by the triangle
inequality. No cutoff growth, smaller parameter domain, asymptotic
remainder estimate, numerical quadrature or optimizer is used.

This avoids the particular separate allowances in C032z's literal
series stop1586; it does not falsify that cost obstruction or certify
any complete evaluator. The full E formula can use(4) only with all
of C032z's inherited qualifications and its other terms intact.

### Critical audit1611 — 18 November2026

The four claims pass a separate conceptual audit under unchanged
SPECIALIZE assessment1609, approved in1610. No statement, cutoff,
parameter domain or proof correction is required. This validates a
local input by reproducing its checks; it is not a new theorem beyond
the cited sources or a finite evaluator. Reused source coverage1608
supplies the exact DLMF5.9.16 identity and its Re(z)>0 hypothesis;
C032z's ordinary-transform proof and audit1585 supply the inputs in(1).
The checks below do not assume a smooth Mellin test or any divisor sign.

**Absolute Fubini before cancellation.** Write F(r,t) for the combined
quotient on the right of(6). The functions are measurable; h is
continuous by its Gaussian-dominated representation in(1). On0<t<=1,
put R=2/t. The central oscillatory contribution is at most

    C*t^2/8 * integral_(-R)^R r^2/(1+r^2)dr
       <= C*t^2/8 * 2*R = C*t/2.

The two tails contribute at most

    2*C * integral_(|r|>R) r^(-2)dr
       = 4*C/R = 2*C*t.

Their sum is exactly the upper bound(5/2)*C*t in(7). This split is
essential: replacing it by a bound involving integral |r*h(r)|dr
would not be justified by inverse-square decay. The nonoscillatory
difference contributes at most(3*t/4)*C*pi. Dividing the combined
bound by t/2 gives(8). For t>=1, both exponential terms have the
common integrable bound(9). Integrating these estimates explicitly
gives the uniform finite product bound

    integral_0^infinity integral_R |h(r)*F(r,t)|dr dt
      <= C*[3*pi/2+5+2*pi*(exp(-1)+4*exp(-1/4))].        (13)

Consequently complex Fubini is applicable, by its real and imaginary
parts if desired. Pointwise(6) also yields

    integral_R |h(r)|*|Re psi(1/4+i*r/2)|dr
      <= |gamma_E|*C*pi + right side of(13) < infinity.

Thus the gamma integral itself is absolutely defined independently
of the subsequent zero-mean cancellation. After this check, for each
fixed t>0 the inner integral of the constant exp(-t) is zero. This
does not integrate either separate divergent endpoint term in t.
The estimate |integral_R h*F dr|<=integral_R |h*F|dr also proves that
the cancelled expression(10) remains absolutely integrable in t.

**Complex-test factors.** The real-part operation in(6) occurs before
multiplication by h. For every real r the substitution has Re(z)=1/4;
the pointwise source formula therefore applies with no zero-free or
RH hypothesis. Directly using the two Fourier values gives

    integral_R h(r)*cos(r*t/2)dr
      = [hat(h)(t/(4*pi))+hat(h)(-t/(4*pi))]/2
      = -2*pi*q(t/2).

All these r integrals are absolute. This calculation needs evenness,
not conjugate symmetry or reality of h or w. It checks both transform
signs without an imaginary-part shortcut. The coefficient in(10)
becomes (-1/(4*pi))*(-2*pi)=1/2; the change t=2*v contributes the
remaining factor2. The resulting kernel is precisely(4), including
the exp(-v/2) and1-exp(-2*v) factors. The constant gamma_E vanishes
only through the already established ordinary integral of h.

**Jointly continuous origin.** A check avoiding division by w uses
Taylor's integral remainder and the elementary exponential identity:

    A(v,w)=integral_0^1 (1-s)*cosh(s*w*v)ds,
    B(v)=integral_0^1 exp(-2*s*v)ds,
    cosh(w*v)-1=w^2*v^2*A(v,w),
    1-exp(-2*v)=2*v*B(v).

For v>0, these identities rewrite the claimed integrand as

    I_(sigma,w)(v)
      = (w^2/2)*exp(-sigma*v^2-v/2)*A(v,w)/B(v).        (14)

Here A(0,w)=1/2, B(0)=1, and B(v)>=exp(-2)>0 on0<=v<=1.
Both compact integrals are jointly continuous in their parameters.
The right side of(14) is consequently continuous on the compact set
[0,1] times[1,2] times{|w|<=2}. Uniform continuity proves that its
limit at0 is w^2/4 uniformly in sigma,w. The previously audited
q(v)=w^2*v/2+O(v^3) also recovers the stated uniform O(v) remainder.
This covers w=0 without dividing by it, complex boundary points
|w|=2, and both sigma endpoints. There is no delta mass or endpoint
term to add to an ordinary absolutely convergent integral.

**Full-parameter tail.** The only parameter estimates used are
sigma>=1 and |w|<=2, through(1); they hold on the full closed set.
For v>=16 the denominator exceeds1/2. Therefore

    |I_(sigma,w)(v)|<=4*v*exp(-v^2+3*v/2)
                     <=4*v*exp(-v^2/2).

The last inequality follows from v>=3. Its integral on[16,infinity)
is4*exp(-128), with no missing factor2. Since exp(128)>129>64,
this is strictly less than1/16. The common majorant bounds every
tail, so taking the parameter supremum preserves the same bound.
For w=0 the tail is identically zero; no exceptional case is lost.

The audit therefore validates(4)-(5) and all four saved obligations
without numerical evidence or a mathematical script. C032z remains
the only direct local mathematical input; the imported standard
identity is cited above. Its divisor, multiplicity, no-ordinate-zero,
strip/counting and additional probability qualifications remain
exactly as stated. They were retained, not independently proved here.
This check neither audits the full source chain nor supplies compact
quadrature, arithmetic errors, pole/prime/O evaluation, coefficient
control or the actual variation2 residual. Stops1586/1608 retain
their stated scope; no signed-theta upper control, unsmoothed Xi
realization or all-degree positivity has been inferred.

## Mathlib

Full matching coverage of this combined digamma/Fourier specialization
and explicit uniform tail has not been checked and is unknown. Named
standard Fubini/Tonelli and elementary integration results support the
argument mathematically; no particular Mathlib theorem or formalization
of the whole result is claimed. The external analytic identity is
precisely DLMF5.9.16 above, and C032z supplies the already audited
ordinary transform. Unknown coverage is not evidence of absence.
