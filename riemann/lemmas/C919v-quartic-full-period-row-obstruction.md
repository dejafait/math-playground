# Corollary919v: all noninitial full-period curvature rows are negative

## Hypotheses

Let K(y)=exp(-y^4-y^2), and let x be the exact least positive cosine
zero certified by C919s. Retain that result's explicit CPython
integer/Fraction, libmpdec directed-operation, correctly rounded exp
and representable-neighbor contracts. They are assumptions here;
there is no new numerical computation or verification of that software.
In particular, use its complete root interval

    150761/32768 < x < 75381/16384 < 5

and its positive smooth function

    G(u)=x integral_0^infinity K(u+t) sin(xt) dt,  u>=0.

Set a=pi/x. For u,t,s>=0 define

    A_u(t,s)=K'(u+t)K'(u+s)
       -[K''(u+t)K(u+s)+K(u+t)K''(u+s)]/2,

    R_j(u)=integral_(2ja)^((2j+2)a) integral_0^infinity
                   A_u(t,s) sin(xt) sin(xs) ds dt, j>=0.

## Conclusion

Every displayed double integral is absolutely convergent. For each
u>=0 the series of rows is absolutely convergent and

    (G'(u))^2-G(u)G''(u)=x^2 sum_(j>=0) R_j(u).             (1)

Thus nonnegativity of every row would suffice for nonpositive
logarithmic curvature at that u, because G(u)>0. However, in this
fixed first-zero model,

    R_j(1)<0 for every integer j>=1.                        (2)

The proposed nonnegative-row premise therefore fails even though
C919s proves negative logarithmic curvature at1. This rejects a
stronger sufficient premise only. It does not decide generic marginal
log-concavity, actual-Xi applicability, iteration, all-degree mixed
positivity or RH. Audit2271 below validates this conditional result;
it does not independently verify C919s's software contracts.

## Proof

### Imported tools and the necessary specialization

The prior EXPLORE assessment2267 covers exactly this fixed-model
identity and row-sign test. Its inspected general inputs are:

- K. Conrad, *Differentiating under the integral sign*, author-hosted
  30-page version inspected21November2026, Theorem12.3, printed p16,
  https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf .
  Continuity on a parameter neighborhood and parameter-uniform
  integrable bounds for the integrand and its derivative are required.
- T. Tao, *245B, notes0: a quick review of measure and integration
  theory*,1January2009, Theorem4(1)-(2),
  https://terrytao.wordpress.com/2009/01/01/245b-notes-0-a-quick-review-of-measure-and-integration-theory/ .
  The signed Fubini theorem requires absolute integrability on the
  product of sigma-finite measure spaces.
- E.O. Tuck, *On positivity of Fourier transforms*, Bull. Austral.
  Math. Soc.74(2006),133-138, pp133-135, equations(1)-(4) and the
  complete half-period comparison proof on p134,
  https://doi.org/10.1017/S0004972700047511 . Its positive decreasing
  amplitude comparison motivates the pairing below. The finite-period
  equality is written explicitly to fix the phase and strict sign;
  no general sine-transform theorem is reproved.

Forrester's determinant identity and Dimitrov--Xu's frequency-derivative
theorems are comparisons in2267, not mathematical inputs. Direct product
integration suffices for(1); no determinant theorem is needed. The new
work is checking the fixed translated-derivative interfaces and the
polynomial sign that those sources do not supply. No novelty beyond
the sources checked is certified. C919t/u concern distinct failed
premises and are not mathematical inputs.

### Local differentiation, absolute products and complete row sum

Put V(y)=y^4+y^2 and p(y)=V'(y)=4y^3+2y. Then

    K'= -p K,       K''=(p^2-p')K.                         (3)

These formulas supply polynomial-times-K majorants. Explicitly, for
each M>=1 and m=0,1,2 there is a finite C_(M,m) such that, for every
|u|<=M and t>=0,

    |K^(m)(u+t)| <= B_(M,m)(t)
       := C_(M,m)(1+t)^(3m) exp(-t^4/16).                 (4)

To verify this, for t>=2M+1 we have u+t>=t/2 and
|u+t|<=t+M. Use(3), whose polynomial degrees are0,3,6,
and V(u+t)>=(u+t)^4>=t^4/16. On the compact remaining
rectangle enlarge C_(M,m) by the finite maximum of the continuous
ratio in(4). Each B_(M,m) is integrable: eventually its polynomial
factor is at most exp(t^4/32), and exp(-t^4/32) has a finite integral.
This proves a parameter-uniform majorant on an open neighborhood of
every u>=0, including0, without just assuming uniform tail decay.

Write M_m(u)=integral_0^infinity K^(m)(u+t) sin(xt)dt.
Conrad's theorem applied twice with(4) gives

    G=x M_0,       G'=x M_1,       G''=x M_2.              (5)

At0 the integral formula on an open real neighborhood defines the
derivatives; its restriction agrees with C919s's smooth G. The exact
root is held fixed during differentiation. All integrands are continuous
and measurable, and Lebesgue measure on[0,infinity) is sigma-finite.
For a fixed u within the selected neighborhood,

    |A_u(t,s) sin(xt) sin(xs)|
       <= B_1(t)B_1(s)+[B_2(t)B_0(s)+B_0(t)B_2(s)]/2,

where B_m denotes B_(M,m). The double integral of this majorant is
||B_1||_1^2+||B_0||_1||B_2||_1<infinity. Signed Fubini therefore gives

    integral_0^infinity integral_0^infinity
           A_u(t,s) sin(xt) sin(xs) ds dt
       =M_1(u)^2-M_0(u)M_2(u).                            (6)

Partition the t half-line into the complete intervals
[2ja,(2j+2)a), j>=0. Their endpoints form a measure-zero set.
The sum of |R_j(u)| is bounded by the same absolute double integral.
Countable additivity for integrable functions now identifies(6) with
the full row sum, with no tail omitted and no conditional rearrangement.
Equations(5)-(6) prove(1). Since(log G)''=(GG''-(G')^2)/G^2,
positivity of G from C919s pays the claimed sufficient implication.

### Exact one-variable reduction at1

Use C919s's weakened certified enclosures

    0.03370892 < g:=G(1) < 0.03377948,
    -0.29928826 < G'(1) < -0.29896072,
    2.14972505 < k:=G''(1) < 2.15124695.

Consequently h:=-G'(1) satisfies

    g>3/100,       0<h<3/10<10g,       k>0.               (7)

These are imports, not new quadrature or evaluations at an approximate
root. In particular all coefficients refer to the same exact x in the
full certified interval. Integrating first in s in(6), and using(3),(5),
gives, with y=1+t,

    integral_0^infinity A_1(t,s) sin(xs)ds
       =-[K(y)/x] q(y),
    q(y)=g[p(y)^2-p'(y)]/2-h p(y)+k/2.                    (8)

The sign of a far row can therefore be tested without replacing the
signed inner integral by an absolute bound.

### A decreasing positive amplitude beyond y=2

For y>=2, p>=36, p'=12y^2+2>0, p''=24y>0, and

    p' <=3p/y <=3p/2.                                    (9)

The first inequality follows from12y^2+2<=12y^2+6. By(7)-(9),

    q > (g/2)[p^2-p'-20p]
      >=(g/2)p[p-43/2] >0.                               (10)

The constants g,h,k do not depend on y. Direct differentiation gives

    p q-q'=(g/2)[p^3-3p p'+p'']
                 -h[p^2-p']+k p/2.

Dropping the positive terms g p''/2, h p' and k p/2 and using
h<10g yields

    p q-q' > (g/2)[p^3-3p p'-20p^2]
            >=(g/2)p^2[p-49/2] >0.                       (11)

Thus K(y)q(y)>0 and (Kq)'=K(q'-p q)<0 for every y>=2.
This is a whole-ray analytic inequality, not an asymptotic expansion
with an unpaid remainder. The polynomial q times K is integrable.

### Every noninitial row has the wrong sign

The elementary Archimedean bound pi>3 and C919s's x<5 give
2a=2pi/x>6/5>1. Hence for j>=1 the entire row has
y=1+t>=1+2ja>2. Define f(t)=K(1+t)q(1+t).
By(10)-(11), f is positive and strictly decreasing throughout these
rows. Since xa=pi and x(2ja)=2j*pi, splitting each row into its two
half-periods gives the exact identity

    R_j(1)=-(1/x) integral_0^a
       [f(2ja+v)-f((2j+1)a+v)] sin(xv) dv.                (12)

For every0<v<a, both the bracket and sine in(12) are strictly
positive. The continuous integral is therefore strictly positive,
and x>0 gives(2). This treats all j>=1, including the entire distant
tail, and does not assert a sign for j=0. Absolute summability was
already proved independently of this pairing.

C919s's total curvature sign is compatible with these negative rows;
one must not infer the total determinant sign from a tail row. The
continuation/abandonment threshold in2267 is met: abandon this
nonnegative-row sufficient premise. Generic curvature, any useful
different grouping, actual-Xi applicability and repeated removal remain
unproved. Refuting this premise is not a disproof of those claims or RH.

### Critical audit2271: analytic interfaces and every row

22 November2026. Independently checked the complete argument against
assessment2269, using C919s's hypotheses, conclusion and complete
single-curvature enclosure section. No discrepancy requiring a repair
was found. This is local verification of the specialization, not a
new row obstruction or a proof beyond the sources already assessed.

For (4), choose M strictly larger than the absolute value of the
parameter being differentiated. On t>=2M+1, t/2<=u+t<=t+M
uniformly on |u|<=M. The polynomial factors of K, K', K'' have
degrees0,3,6, so a constant times (1+t)^(3m) suffices. The
remaining parameter/t rectangle is compact and the proposed majorant
is positive there. Enlarging its constant therefore works uniformly.
The majorants are integrable on the full half-line. Continuity and
these bounds permit first differentiating M_0 with bound B_1 and
then M_1 with bound B_2; at0 an open neighborhood is available.
The parameter is u, with the same exact x fixed throughout.

The absolute product majorant has double integral exactly
||B_1||_1^2+||B_2||_1||B_0||_1, finite before any sign claim.
The product space is sigma-finite and the integrands are continuous.
Thus signed Fubini gives M_1^2-M_0 M_2, including the factor1/2
on both mixed terms. The disjoint half-open intervals
I_j=[2ja,(2j+2)a) have union [0,infinity), and

    sum_j |R_j| <= sum_j integral_(I_j x [0,infinity)) |A sin sin|
                 = integral_([0,infinity)^2) |A sin sin| < infinity.

Consequently the row sum is the original integral, not a selected
tail or a conditional rearrangement. Multiplication by x^2 gives
(G')^2-GG'', the negative of C919s's curvature determinant.

The root bracket and three coefficient bounds in (7)-(8) are exactly
the weakened enclosures displayed in C919s; its root-radius inflation
covers a common exact root, not three separately chosen points.
In particular 75381<5*16384=81920 proves x<5 without a new
numerical computation. The decimal endpoints are terminating
rationals: g>0.03370892>0.03, 0.29896072<h<0.29928826<0.3,
and k>2.14972505>0. Thus h<0.3<10g, strictly. No imported
enclosure or runtime contract has been strengthened.

In the inner integration M_0=g/x, M_1=-h/x and M_2=k/x.
Hence K'M_1-(K''M_0+KM_2)/2=-Kq/x, confirming the minus sign
in (8). For y>=2, p>=36 and yp'=12y^3+2y<=3p. Thus
p'<=3p/2. Substituting h<10g and k>0 yields
q>(g/2)p(p-43/2)>0. Expanding the differentiated polynomial gives
pq-q'=(g/2)(p^3-3pp'+p'')-h(p^2-p')+kp/2.
The terms gp''/2, hp' and kp/2 are positive; dropping them and
using h<10g gives pq-q'>(g/2)p^2(p-49/2)>0. Both numerical
thresholds are below36. Therefore Kq is positive and strictly
decreasing on the entire ray, with an integrable polynomial tail.

Finally pi>3 and x<5 imply 2a>6/5. The first required row,
j=1, already starts at y=1+2a>2; every later row stays in the
proved ray. In its first half sin(x(2ja+v))=sin(xv), and in its
second half sin(x((2j+1)a+v))=-sin(xv), because xa=pi.
Thus (12) has precisely its displayed negative prefactor. For
0<v<a the sine and decreasing-amplitude difference are strictly
positive, so the integral is strictly positive and R_j(1)<0.
This treats every integer j>=1, with no finite cutoff or unchecked
distant tail. It makes no assertion about R_0's sign.

The audit accepts only the conditional failure of all-row
nonnegativity. It does not audit C919s's computation again, identify
total curvature with a tail sign, or settle generic preservation,
actual-Xi hypotheses, repeated removal or all-degree positivity.
The only direct local mathematical input remains C919s; the DAG
needs no change. Full matching Mathlib coverage remains unchecked.
No mathematical script or numerical replay was needed.

## Mathlib

Full matching coverage is unchecked, not asserted absent. No Mathlib
theorem is a premise and no Lean verification is claimed. The named
dominated-differentiation and signed-Fubini results support the analytic
interfaces; their availability would not by itself establish C919s's
root/certified coefficients, the polynomial inequalities, or the row sign.
