# Corollary C048g: the full-theta absolute right-ray allowance

## Hypotheses

Use C048c's parameters and principal branches:

\[
 r=|p|,\quad L=\log r\ge12,\quad \Re p\ge-r/(4L),\quad
 w=W_0(2p/\pi)=U+iV,\quad u_0=w/2,\quad d=1/(3L),
\]
\[
 h_p(u)=2p\operatorname{Log}u-\pi e^{2u},\quad
 g(u)=8\pi^2e^{9u/2}/u,\quad K(s)=g(u_0+s)/g(u_0),\quad
 A_0=-h_p''(u_0)/2.
\]

Define the full theta factor by the strip series

\[
 F(u)=1-\frac3{2\pi e^{2u}}+
 \sum_{n=2}^{\infty}\left(n^4-\frac{3n^2}{2\pi e^{2u}}\right)
                          e^{-\pi(n^2-1)e^{2u}}.
\]

The sum is the R_modes in the approved assessment1640. Initially define
the following nonnegative improper integral with values in [0,infinity]:

\[
 T_{\rm right}(p)=\frac{\displaystyle\int_d^\infty
       |K(s)F(u_0+s)e^{h_p(u_0+s)-h_p(u_0)}|\,ds}
                         {|\sqrt{\pi/A_0}|}.             \tag{1}
\]

The square root is principal. No convergence, contour identity or
positivity of the complex theta factor is assumed.

This reproduces the separate right allowance of K. Kawano,
*Logarithmic Inequalities of Arbitrary Order for the Riemann Xi
Coefficients*, [Preprints.org202611.0383v1, posted4 November2026,
DOI10.20944/preprints202611.0383.v1](https://www.preprints.org/manuscript/202611.0383/v1),
Section5.2(28), Lemma5.1(i), the right-side proof of (31),
AppendixB's B_+ and full-mode envelope, and AppendixC's A_+.
The preprint's quantitative claim is a conclusion to verify, not an
assumption. Assessment1640 approved precisely (1) and this constant
before step1641. Its operational absolute-integral qualification is
proved below; no signed-integral estimate is substituted for (1).

## Conclusion

The complete ray lies in the theta strip and principal Log domain,
the integral (1) is finite, and uniformly on the full closed sector

\[
 T_{\rm right}(p)\le A_+\frac{L^{9/2}}r,\qquad
 A_+=\frac{(3/2)e^{1/8}\sqrt{6/\pi}}{62/25}
          \sqrt{y_0}\,e^{-(19/45)y_0}<0.096514,
 \quad y_0=e^{12}/12^4.                               \tag{2}
\]

In the display above the constant has the exact source normalization.
The rational certificate below encloses it strictly between
0.096513538928204 and 0.096513538928205.

This is REPRODUCTION of one source component, established in step1641
and independently checked in conceptual audit1643 below. It supplies no conclusion
beyond that checked source allowance. Left tails, the full Mellin
assembly, zero counts, inversion and a sufficient actual-Xi mixed-sign
bridge remain independent. It is not an RH candidate.

## Proof

### 1. Geometry and normalization on the whole ray

C048c(4)-(10) gives

\[
 U>3L/4,\quad |V|<\pi/2,\quad |w|<L,\quad \cos V>1/L,
 \quad v_0:=\pi e^U\cos V>2r/L^2,
 \quad \Re A_0>0,\quad |A_0|<6r/L.                   \tag{3}
\]

Write x_0=U/2 and y=V/2. For every s>=0, Re(u_0+s)>=x_0>9/2>1
and |Im(u_0+s)|=|y|<pi/4. Thus the entire ray stays in the
open right half-plane and the theta strip. This is a direct check,
not an extrapolation of a finite-segment phase estimate.
The denominators u_0, u_0+s and A_0 are nonzero. C048c's branch
calculation gives exactly

\[
 |\sqrt{\pi/A_0}|=\sqrt{\pi/|A_0|},\qquad
 g(u_0)e^{h_p(u_0)}\sqrt{\pi/A_0}=S(p).               \tag{4}
\]

Only the normalization identity in (4) is used, without any assertion
that the present ray equals a globally continued Mellin integral.

### 2. The right phase, including negative real part

First suppose Im p>=0 and write p=sigma+i beta, beta>=0.
C048c's branch geometry gives y>=0. For real x>=x_0>|y| set

\[
 Q(x)=\frac{\sigma x+\beta y}{x^2+y^2},\qquad
 H(x)=\Re h_p(x+iy).
\]

Since we^w=2p/pi, p/u_0=pi e^{2u_0}. In particular

\[
 Q(x_0)=v_0>0,\qquad
 H'(x)=2Q(x)-2v_0e^{2(x-x_0)}.                       \tag{5}
\]

If sigma>=0, differentiation gives

\[
 Q'(x)=\frac{\sigma(y^2-x^2)-2\beta xy}{(x^2+y^2)^2}
       \le0.                                       \tag{6}
\]

If sigma<0, wherever Q>0 the alternative expression

\[
 Q'(x)=\frac{\sigma-2xQ(x)}{x^2+y^2}<0               \tag{7}
\]

shows decrease. The numerator sigma*x+beta*y is strictly decreasing;
after it becomes nonpositive it cannot become positive again. Starting
from Q(x_0)>0, these two facts give Q(x)<=Q(x_0) on the complete
half-line also in this case. This argument does not assume that Q
remains decreasing after it has become negative.

Integrating (5) from x_0 to x_0+s, s>=0, now gives

\[
 \Re(h_p(u_0+s)-h_p(u_0))\le-v_0\phi(s),\qquad
 \phi(s)=e^{2s}-1-2s.                               \tag{8}
\]

For Im p<0, conjugation preserves the principal Lambert and logarithm
branches in this domain, sends u_0 to its conjugate, and leaves the real
phase and v_0 unchanged. Applying the upper-half-plane argument to
the conjugate proves (8). Positive real p, sigma=0, both allowed angular
boundaries and L=12 are included. The phase proof is the full right-side
specialization of source(31), rechecked because its uniform use is
essential to the claimed effective estimate.

### 3. Complete theta amplitude and absolute domination

Use only L799's strip normal-convergence proof and identity(4), which
are independent of its different saddle. They give exactly F=P/H with

\[
 P(u)=\sum_{n\ge1}(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2})
                          e^{-\pi n^2e^{2u}},\qquad
 H(u)=4\pi^2e^{9u/2-\pi e^{2u}}.
\]

On a compact subset of the strip, Re(pi e^{2u}) has a positive
minimum, so the absolute summands are bounded by a summable constant
times (n^4+n^2)e^{-delta*n^2}. Thus the series defining F is normally
convergent and continuous on every compact subray. Dividing by the
nonzero H gives precisely the coefficients in (1); the common factor
2/u cancels in F=(2P/u)/(2H/u), with u_0/(u_0+s) retained in K.
No mode, Jacobian or extra normalization is omitted.

For u=u_0+s, s>=0, put

\[
 a(u)=\frac3{2\pi}e^{-2\Re u}<\frac1{14}<\frac12,
 \qquad t=\Re(\pi e^{2u})=v_0e^{2s}>2.               \tag{9}
\]

For the first bound use Re u>1, pi>3 and e^2>7. For the second,
e^L/L^2 increases on L>=12 and e^{12}>2^{12}>144, so r/L^2>1
and (3) applies. For n>=2 the absolute nth correction is bounded by

\[
 b_n=(n^4+n^2/2)e^{-(n^2-1)t}.
\]

The coefficient ratio is at most ((n+1)/n)^4<=81/16, and hence
b_{n+1}/b_n<=(81/16)e^{-5t}<(81/16)e^{-5}<1/10.
Indeed e>2 and e^2>7 imply e^5>98, and 81/1568<1/10.
Consequently the complete infinite tail is less than
(10/9)b_2=20e^{-3t}. The elementary strict estimates e^2>7 and e>2
follow from the positive exponential series (the terms through degree4
at 2 sum to7). Thus e^6>343, and

\[
 |F(u)|\le1+a(u)+\sum_{n=2}^{\infty}b_n
 <1+\frac1{14}+\frac{20}{343}<\frac32.               \tag{10}
\]

In fact (10) bounds the sum of the absolute values of all individual
mode coefficients, a stronger fact than a bound on the summed modulus.

Finally

\[
 K(s)=e^{9s/2}\frac{u_0}{u_0+s},\qquad
 |u_0+s|^2=|u_0|^2+2x_0s+s^2\ge|u_0|^2.
\]

Combining this identity, (8) and (10), on the whole ray gives

\[
 |K(s)F(u_0+s)e^{h_p(u_0+s)-h_p(u_0)}|
 \le\frac32\exp(9s/2-v_0\phi(s)),\qquad s\ge0.     \tag{11}
\]

No series is interchanged with an improper integral to get (11).
The summed integrand is continuous on finite subrays and its absolute
majorant will now be integrated directly.

### 4. Integrable tangent envelope and its constants

Since phi''(s)=4e^{2s}>0, for every s>=d,

\[
 9s/2-v_0\phi(s)
 \le9d/2-v_0\phi(d)-\lambda(s-d),\qquad
 \lambda=2v_0(e^{2d}-1)-9/2.                         \tag{12}
\]

This is the elementary tangent envelope used in Luc Devroye,
[*Non-Uniform Random Variate Generation* (1986), ChapterVII Section2.6,
pp299-300](https://luc.devroye.org/chapter_seven.pdf), the displayed
envelope preceding Theorem2.6 and the first integral of its proof.
Here convexity proves (12) directly for an unnormalized real envelope;
no log-concavity of the complex theta kernel or prior integrability
is assumed. A strictly positive lambda is essential.

The positive exponential series gives

\[
 e^3>\sum_{k=0}^8\frac{3^k}{k!}=\frac{89641}{4480}>20,
 \qquad e^{12}>20^4=160000>145800.
\]

The function e^L/L^3 is increasing for L>=12. Therefore
r/L^3>160000/1728>675/8; the last comparison is equivalently
160000>145800. Using v_0>(19/10)r/L^2 from (3) and
e^{2d}-1>=2d, we obtain the uniform strictly positive rate

\[
 \lambda>\frac{38}{15}\frac r{L^3}-\frac92
 >\frac{62}{25}\frac r{L^3}>0.                      \tag{13}
\]

For the middle inequality, 38/15-62/25=4/75 and
(4/75)(675/8)=9/2. Also phi(d)>=2d^2 by the positive exponential
series, so

\[
 v_0\phi(d)>\frac{19}{45}\frac r{L^4},\qquad
 9d/2=3/(2L)\le1/8.                                \tag{14}
\]

Integrating the positive exponential in (12) over [d,infinity)
is now legitimate and gives its endpoint value divided by lambda.
It bounds every finite truncation of (1); monotone convergence of
the nonnegative truncated integrals proves finiteness of (1).
Use (3)-(4), (11), (13)-(14) to get

\[
 T_{\rm right}(p)
 \le \frac32\sqrt{\frac{|A_0|}{\pi}}
           \frac{e^{9d/2-v_0\phi(d)}}{\lambda}
 \le \frac{(3/2)e^{1/8}\sqrt{6/\pi}}{62/25}
       \frac{L^{5/2}}{\sqrt r}
                  e^{-(19/45)r/L^4}.                \tag{15}
\]

The normalization uses |A_0|, not Re A_0. The proof has bounded the
integral of the modulus throughout, including all modes and the
complete infinite interval.

### 5. Radial uniformity and the strict decimal bound

Set y=e^L/L^4. Its logarithmic derivative is 1-4/L>0 on L>=12,
so y>=y_0. Since y_0>160000/20736>45/38, the logarithmic derivative
of sqrt(y)e^{-(19/45)y}, namely 1/(2y)-19/45, is negative on
[y_0,infinity). Divide (15) by L^{9/2}/r; the remaining factor is
exactly sqrt(y)e^{-(19/45)y} times the constant in (15).
Its maximum is therefore at y_0, which proves the exact A_+ bound
in (2), including all unbounded radial parameters.

The fixed scalar verification is reproducible by

    python3 scripts/mellin-horizontal-local/right_ray_constants_1641.py

Its complete certificate is
`scripts/mellin-horizontal-local/right_ray_constants_1641.json`.
It uses only exact rational arithmetic and integer square roots.
For x>0 and n+2>x, the positive exponential series gives the strict
lower S_n(x) and upper

    S_n(x) + [x^(n+1)/(n+1)!]/[1-x/(n+2)].

Every successive ratio in the omitted tail is at most x/(n+2), so
this upper bound is rigorous. At x=12,n=120 it certifies

    162754.7914190039 < exp(12) < 162754.7914190040.

For pi the alternating arctangent series at 1/5 (24 terms) and
1/239 (8 terms), with next-term remainders, is used in
pi=16 atan(1/5)-4 atan(1/239). To verify this identity directly,
tan(2 atan(1/5))=5/12 and tan(4 atan(1/5))=120/119; subtracting
atan(1/239) gives tangent 1. The resulting angle is between 0 and
pi/2: it is less than 4/5<pi/2 and positive since
atan(1/5)>=5/26 and atan(1/239)<1/239. It is consequently pi/4.
The alternating-series remainder also follows by integrating the
finite geometric expansion of 1/(1+t^2). These bounds certify

    3.141592653589793 < pi < 3.141592653589794.

Writing y_lo,y_hi for the exp(12) bounds divided by 12^4, the script
bounds sqrt(6y/pi) between roots of 6y_lo/pi_hi and 6y_hi/pi_lo.
For each rational radicand q it computes
k=isqrt(floor(q*10^36)) and checks
(k/10^18)^2<=q<((k+1)/10^18)^2 exactly. It also encloses e^{1/8}
with degree 30 and e^{(19/45)y_lo}, e^{(19/45)y_hi} with degree 80.
Combining positive endpoints monotonically gives the stored exact
interval for A_+; rounding it outward yields the rational inequalities

\[
 \frac{96513538928204}{10^{15}}<A_+
 <\frac{96513538928205}{10^{15}}
 <\frac{48257}{500000}=0.096514.                     \tag{16}
\]

All 13 exact comparisons passed, with no failures, including a certified
gap greater than 10^{-9} below the required threshold. The complete
rounded interval, radicands, root bounds and square comparisons were
inspected. Finite scalar calculations establish only these constants;
the proofs in sections 1-5 establish the closed-sector and whole-ray
uniformity. No sampled parameter grid or numerical quadrature is used.

### Independent conceptual audit1643 — 19 November 2026

The unchanged SPECIALIZE assessment1641, separately approved in step1642,
covers precisely (1)-(2). The complete proof and producer program were
read, along with C048c's hypotheses, geometry (4)-(10), exact complex
normalization and prior geometry audit, and L799's strip-series proof
and identity (4). The full-ray estimate passes without changing its
hypotheses, constant or argument. This is verification of the cited
source component, not a result beyond the checked source.

**Geometry and phase.** C048c provides U>3L/4, |w|<L, cos V>1/L,
Re A_0>0 and |A_0|<6r/L on the same closed sector; from
pi e^U=2r/|w| one obtains v_0>2r/L^2. Adding nonnegative real s
preserves the strict strip and principal-Log conditions. The saddle
identity p/u_0=pi e^{2u_0} fixes both Q(x_0)=v_0 and (5).
Differentiating Q verifies both (6) and (7). For sigma<0 the interval
where its affine numerator is positive ends at most once; Q decreases
there, and is nonpositive thereafter. Hence Q<=v_0 throughout even
though Q need not decrease once negative. Integrating its upper bound gives exactly
2v_0s-v_0(e^{2s}-1), the right-hand side of (8). No bound on |Q|,
or restriction to a finite s interval, is substituted. Conjugation
respects the principal branches and gives the lower half-plane case.
At Im p=0 the sector forces p>0, so this endpoint involves neither
a negative-real-axis branch nor division by the imaginary part.

**Full theta series and normalization.** The general strip argument of
L799 is independent of its rotated saddle and its quantitative bounds.
Dividing its normally convergent P by nonzero H gives exactly F=1+rho.
Thus the coefficient of the lower-power term is 3/(2pi e^{2u}),
and the higher-mode exponential is -(n^2-1)pi e^{2u}. Multiplication
by 2/u is exactly the factor converting H to g exp(-pi e^{2u});
it cancels in the ratio defining F, while u_0/(u_0+s) remains in K.
For n>=2,

    [(n+1)^4+(n+1)^2/2]/[n^4+n^2/2]
       <= ((n+1)/n)^4 <= 81/16.

The ratio follows because 1+1/(2n^2) decreases. Since t>2, the
geometric ratio used in the proof is strictly less than 1/10 and
b_2=18 exp(-3t); summing every n>=2 gives the stated 20 exp(-3t).
The elementary bounds give 1+1/14+20/343<3/2 with strict slack.
Together with |u_0/(u_0+s)|<=1 this proves (11) for the sum of the
absolute modal contributions, so it also bounds |F|. Continuity on
finite subrays comes from normal convergence, not an interchange of
the infinite sum with an unbounded integral. The principal root has
modulus sqrt(pi/|A_0|), and C048c's identity for S(p) retains the
complex phase; no Re A_0 normalization is used.

**Convergence and unbounded parameters.** Convexity of phi gives (12)
for every s>=d. The exact rate difference is 4/75, with
(4/75)(675/8)=9/2, while e^L/L^3>=e^12/12^3>160000/1728>675/8.
Consequently lambda>(62/25)r/L^3>0. Also
(19/10)(2/9)=19/45 and 9/(2*3*12)=1/8, verifying every constant
in (13)-(14). For each fixed p the finite integrals are bounded by
the integral of a positive exponential of rate lambda; their monotone
limit proves absolute convergence. This does not assume a common
strip margin as L tends to infinity. The estimates themselves hold
uniformly for every p in the closed sector. In (15) division by
L^(9/2)/r leaves sqrt(r/L^4); y=e^L/L^4 increases for L>=12 and
y_0>45/38. Hence sqrt(y)exp(-19y/45) decreases on the entire needed
range. Both angular boundaries, L=12 and arbitrarily large L are
included, without a compactness assumption or sampled-parameter test.

**Complete scalar evidence.** The audit command is

    python3 scripts/mellin-horizontal-local/right_ray_audit_1643.py

It replays the original producer and verifies byte-for-byte identity
with the existing certificate, then reads and checks every scalar
record: all five positive-exponential series, both arctangent series,
their exact endpoints, the pi and y_0 intervals, square inequalities,
the assembled coefficient and all 13 producer comparisons. Direct
factorial sums independently check the producer's recurrent sums.
The original Machin identity is justified in section 5, including
the necessary angle range; no transcendental floating-point value
enters these checks.

To check the direction of the exponential-denominator enclosure by a
different construction, the audit also uses the degree81 and degree82
Taylor polynomials S_n(-x) for exp(-x). Taylor's integral remainder is

    exp(-x)-S_n(-x)=(-1)^(n+1)/n!
                         integral_0^x exp(-t)(x-t)^n dt.

For x>0 this makes the odd degree a strict lower bound and the even
degree a strict upper bound, without requiring decreasing early terms.
Use x=(19/45)y_hi for the lower and x=(19/45)y_lo for the upper,
then multiply by the positive root and exp(1/8) endpoint bounds.
The resulting independent exact interval also lies strictly inside
(96513538928204/10^15,96513538928205/10^15), with slack greater
than 10^-9 below 48257/500000. The complete audit certificate is
`scripts/mellin-horizontal-local/right_ray_audit_1643.json`:
37 checks pass and its failure list is empty. These are exact scalar
checks; the analytic proof above, rather than this certificate, supplies
the entire-ray and entire-sector statements.

The direct mathematical inputs remain C048c and L799. L801 is only
an overlap contrast. No left-tail estimate, full-contour deformation,
inversion, zero count or sufficient actual-Xi sign result has been used
or established by this audit. The historical global-import stop remains
in force for that particular automatic-import approach.

## Mathlib

Full matching coverage has not been checked; no absence claim is made.
The strip normal-convergence input is L799's proved general series
identity, and the sector geometry and branches are the proved C048c
estimates. The tangent specialization and all scalar bounds are justified
above. No Lean or other formal verification of the full result is claimed.
