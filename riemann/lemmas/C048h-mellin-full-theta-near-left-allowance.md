# Corollary C048h: the full-theta absolute near-left allowance

## Hypotheses

Let p be complex and use C048c's sector, saddle and principal branches:

\[
 r=|p|,\quad L=\log r\ge12,\quad \Re p\ge-r/(4L),\quad
 w=W_0(2p/\pi)=U+iV,\quad u_0=w/2,\quad d=1/(3L),
\]
\[
 h_p(u)=2p\operatorname{Log}u-\pi e^{2u},\quad
 g(u)=8\pi^2e^{9u/2}/u,\quad K(s)=g(u_0+s)/g(u_0),\quad
 A_0=-h_p''(u_0)/2.
\]

On the open strip |Im u|<pi/4 define

\[
 F(u)=1-\frac3{2\pi e^{2u}}+
 \sum_{n=2}^{\infty}\left(n^4-\frac{3n^2}{2\pi e^{2u}}\right)
                      e^{-\pi(n^2-1)e^{2u}},
\]
\[
 T_{\rm nearleft}(p)=
 \frac{\displaystyle\int_{-1}^{-d}
    |K(s)F(u_0+s)e^{h_p(u_0+s)-h_p(u_0)}|\,ds}
      {|\sqrt{\pi/A_0}|}.                              \tag{1}
\]

This is an integral of moduli, with the full n>=2 series. The square
root is principal. No continued origin, global contour identity or
positivity of a complex theta sum is assumed.

The source is K. Kawano, *Logarithmic Inequalities of Arbitrary Order
for the Riemann Xi Coefficients*, [Preprints.org202611.0383v1,
posted4 November2026, DOI10.20944/preprints202611.0383.v1](https://www.preprints.org/manuscript/202611.0383/v1),
Section5.2(28), Lemma5.1(i), the left-side proof of (31), AppendixB's
C_n/B_-/B_f split and full-mode bounds, and AppendixC's A_- allocation.
The finite segment and absolute observable (1) are the specialization
specified in source-notes1644, inferred from that split and nonnegative
envelope; the source does not separately name (1). Assessment1644
approved this exact reproduction before step1645. The quantitative
claim is a conclusion to verify, not an assumed theorem.

## Conclusion

The complete segment is in Re u>1 and |Im u|<pi/4, and (1) exists.
Uniformly on the full closed sector,

\[
 T_{\rm nearleft}(p)\le A_-\frac{L^{9/2}}r,\qquad
 A_- = \frac{(3/2)\sqrt{6/\pi}}{133/54}
          \sqrt{y_0}\,e^{-(1007/2430)y_0}<0.091191,
 \qquad y_0=e^{12}/12^4.                              \tag{2}
\]

The exact certificate encloses A_- strictly between
0.091190139998283 and 0.091190139998284. This is REPRODUCTION
of the specified source allowance; the independent conceptual audit1647
below confirms the stated finite bound. It is not a result beyond the sources checked or an RH
candidate. The distant-left/origin, full assembly, zero counts,
inversion and sufficient actual-Xi mixed signs remain separate.

## Proof

### 1. Entire segment and normalization

C048c(4)-(10) and its branch calculation give

\[
 U>3L/4\ge9,\quad |V|<\pi/2,\quad |w|<L,\quad
 \cos V>1/L,\quad v_0:=\pi e^U\cos V>2r/L^2,
 \quad \Re A_0>0,\quad |A_0|<6r/L,                    \tag{3}
\]
\[
 |\sqrt{\pi/A_0}|=\sqrt{\pi/|A_0|},\qquad
 g(u_0)e^{h_p(u_0)}\sqrt{\pi/A_0}=S(p).              \tag{4}
\]

Write x_0=U/2 and y=V/2. As 0<d<=1/36<1, [-1,-d] is ordered.
For each s there, x=x_0+s>x_0-1>7/2>1 and
|y|<pi/4<1. Thus x>|y|; the whole segment lies strictly inside
the theta strip and the principal Log domain. All denominators in
(1) are nonzero, including A_0 and g(u_0).

Only the strip convergence argument and identity(4) of L799 are used
from that lemma, not its different saddle estimates. They give F=P/H,
where

\[
 P(u)=\sum_{n\ge1}(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2})
                                  e^{-\pi n^2e^{2u}},\qquad
 H(u)=4\pi^2e^{9u/2-\pi e^{2u}}.
\]

Indeed on each compact subset of the strip, Re(pi e^(2u)) has a
positive minimum, so the series has a summable polynomial-times-
Gaussian majorant. It is normally convergent there; H never vanishes.
In particular F is continuous on this entire finite segment. Exactly,

\[
 e^{2p\operatorname{Log}u}\frac{2P(u)}u
       =g(u)e^{h_p(u)}F(u).                           \tag{5}
\]

For u=u_0+s, du=ds. Dividing the absolute value of (5) by |S(p)|
using (4) gives precisely the integrand and denominator in (1).
The factor 2/u, the saddle ratio in K, and the source normalization
are all retained. This identifies a finite component only, without a
global Mellin deformation or an interchange at an endpoint of the strip.

### 2. Left phase in both real-part cases

Suppose first Im p>=0; write p=sigma+i beta with beta>=0.
C048c gives y>=0. On x_0-1<=x<=x_0 set

\[
 Q(x)=\frac{\sigma x+\beta y}{x^2+y^2},\qquad
 H_p(x)=\Re h_p(x+iy).
\]

The saddle equation implies p/u_0=pi e^(2u_0), so

\[
 Q(x_0)=v_0>0,\qquad
 H_p'(x)=2Q(x)-2v_0e^{2(x-x_0)}.                     \tag{6}
\]

If sigma>=0, then x>|y| and beta,y>=0 give

\[
 Q'(x)=\frac{\sigma(y^2-x^2)-2\beta xy}{(x^2+y^2)^2}\le0.
\]

If sigma<0, the numerator sigma*x+beta*y decreases as x increases.
For x<=x_0 it is therefore at least its strictly positive value at
x_0. Thus Q(x)>0 throughout the segment, and

\[
 Q'(x)=\frac{\sigma-2xQ(x)}{x^2+y^2}<0.
\]

In either case Q(x)>=v_0. For s in [-1,0], integrate (6) backwards
from x_0. The reversed orientation is essential:

\[
 \begin{split}
 H_p(x_0+s)-H_p(x_0)
 &=-\int_s^0 H_p'(x_0+t)\,dt\\
 &\le-\int_s^0 2v_0(1-e^{2t})\,dt
   =-v_0\phi(s),\qquad \phi(s)=e^{2s}-1-2s.          \tag{7}
 \end{split}
\]

For Im p<0, principal Lambert conjugation and principal Log
conjugation on the right half-plane send the entire segment to that
for the conjugate parameter. They leave v_0 and the real phase
unchanged. Hence (7) holds there too. For real p the sector forces
p>0, so y=beta=0 and the sigma>=0 case applies directly. The sigma=0
case and both angular boundaries require no limiting argument.

### 3. Complete theta factor, including the denominator ratio

For u=u_0+s on [-1,-d] define

\[
 a(u)=\frac3{2\pi}e^{-2\Re u}<\frac1{14}<\frac12,
 \qquad t=\Re(\pi e^{2u})=v_0e^{2s}
                      >\frac{2e^{L-2}}{L^2}>2.      \tag{8}
\]

For the a bound use Re u>1, pi>3 and e^2>7. For the t bound use
(3), s>=-1 and monotonicity of e^(L-2)/L^2 for L>=12.
At L=12, e^10>7^5>144. The inequality e^2>7 follows from its
positive exponential series: the terms through degree4 sum to7.

The absolute nth term of the n>=2 correction is at most
b_n=(n^4+n^2/2) exp(-(n^2-1)t). The polynomial coefficient ratio
is at most ((n+1)/n)^4<=81/16. Consequently

\[
 \frac{b_{n+1}}{b_n}\le\frac{81}{16}e^{-(2n+1)t}
       <\frac{81}{16}e^{-5}<\frac1{10}.              \tag{9}
\]

Here e>2 and e^2>7 give e^5>98 and 81/(16*98)<1/10.
Geometric summation bounds the complete infinite tail by
(10/9)b_2=20e^(-3t)<20/343, because t>2 and e^6>343.
Normal convergence justifies the triangle inequality for the whole
series. Thus

\[
 |F(u)|<1+1/14+20/343.                               \tag{10}
\]

The negative displacement makes the saddle denominator ratio larger,
so it must not be dropped. The triangle inequality, |s|<=1 and
|u_0|>=U/2>9/2 give

\[
 \left|\frac{u_0}{u_0+s}\right|
 \le\frac1{1-1/|u_0|}\le\frac1{1-2/U}<\frac97.
\]

In fact

\[
 \frac97\left(1+\frac1{14}+\frac{20}{343}\right)
       =\frac{6975}{4802}<\frac32
       \quad(13950<14406).                           \tag{11}
\]

Using K(s)=e^(9s/2)u_0/(u_0+s), combine (7), (10) and (11) to get
on the whole finite segment

\[
 |K(s)F(u_0+s)e^{h_p(u_0+s)-h_p(u_0)}|
       \le\frac32 e^{9s/2-v_0\phi(s)}.               \tag{12}
\]

No sign of a complex mode or complex kernel is assumed.

### 4. Left tangent and exact uniform allowance

Since phi''(s)=4e^(2s)>0, the real exponent
f(s)=9s/2-v_0 phi(s) is concave. Its tangent at -d satisfies

\[
 f(s)\le-9d/2-v_0\phi(-d)+\lambda(s+d),\qquad s\le-d,
 \qquad\lambda=9/2+2v_0(1-e^{-2d})>0.                \tag{13}
\]

This is the reflected tangent-envelope method in Luc Devroye,
[*Non-Uniform Random Variate Generation* (1986), ChapterVII Section2.6,
pp299-300](https://luc.devroye.org/chapter_seven.pdf), the envelope
before Theorem2.6 and the reflected case/first integral of its proof.
Here (13) follows directly by differentiation of a real scalar
function; no probability normalization or theta log-concavity is used.
The reproof supplies exactly the moving-parameter quantitative bounds.

Taylor's theorem with integral remainder, for x>=0, gives
e^(-x)<=1-x+x^2/2 and e^(-x)>=1-x+x^2/2-x^3/6. These hold since
the third and fourth derivatives of e^(-x) are respectively negative
and positive. Taking x=2d and using d<=1/36 yields

\[
 1-e^{-2d}\ge2d(1-d)\ge2d\frac{35}{36},\qquad
 \phi(-d)\ge2d^2(1-2d/3)\ge2d^2\frac{53}{54}.
\]

Use the weaker v_0>(19/10)r/L^2 from (3). Then

\[
 \lambda>\frac{38}{15}\frac{35}{36}\frac r{L^3}
           =\frac{133}{54}\frac r{L^3},\qquad
 v_0\phi(-d)>\frac{19}{45}\frac{53}{54}\frac r{L^4}
           =\frac{1007}{2430}\frac r{L^4}.           \tag{14}
\]

Integrate (12) using (13), extending only the positive scalar tangent
exponential from [-1,-d] to (-infinity,-d]. Its integral is
exp(-9d/2-v_0 phi(-d))/lambda. Neither (7) nor (8) nor any theta
estimate is asserted on that extension. Dropping e^(-9d/2)<=1 and
dividing by the exact normalization in (4), (3) and (14) give

\[
 T_{\rm nearleft}(p)
 \le\frac{(3/2)\sqrt{6/\pi}}{133/54}
       \frac{L^{5/2}}{\sqrt r}
             e^{-cr/L^4},\qquad c=1007/2430.          \tag{15}
\]

Put y=e^L/L^4. Its derivative is y(1-4/L)>0 for L>=12,
so y>=y_0. Also y_0>7^6/12^4>5>1/(2c). Therefore
the derivative of sqrt(y)e^(-cy) has the sign of 1/(2y)-c and is
strictly negative on y>=y_0. Dividing (15) by L^(9/2)/r leaves
exactly the prefactor times sqrt(y)e^(-cy). Its maximum is at y_0,
which proves (2) with the stated exact A_-.

All estimates include L=12, the two angular boundaries and unbounded
L. The strip margins need not have a positive infimum over the sector:
for each parameter they are strictly positive on the segment, and the
displayed constants are uniform. There is no asymptotic onset, numerical
parameter grid or unproved passage to an infinite theta contour.

### 5. Exact scalar certificate

Run from the active notebook:

```bash
python3 scripts/mellin-horizontal-local/near_left_constants_1645.py
```

The full certificate is
`scripts/mellin-horizontal-local/near_left_constants_1645.json`.
The program uses rational arithmetic throughout; floats occur only in
the short display after all comparisons. It verifies all 15 listed
comparisons, with no failures. It adapts the elementary scalar method
of the right-ray certificate; neither that right-ray inequality nor
its numeric output is used as a premise of this proof.

For x>0 and degree N with x<N+2, let E_N(x)=sum_{k=0}^N x^k/k!.
The omitted positive terms, starting at x^(N+1)/(N+1)!, have successive
ratios at most x/(N+2). Thus

\[
 E_N(x)<e^x\le E_N(x)+
   \frac{x^{N+1}/(N+1)!}{1-x/(N+2)}.                  \tag{16}
\]

For arctan(x), 0<x<1, alternating-series bounds use the sum of an
even number N of terms as a lower endpoint and add the next term
for the upper endpoint. The Machin identity
pi=16 arctan(1/5)-4 arctan(1/239) then gives pi bounds. To check its
branch, put a=arctan(1/5), b=arctan(1/239). Double-angle formulas give
tan(4a)=120/119 and tan(4a-b)=1; also 0<4a-b<4/5<pi/2, so
4a-b=pi/4. No numerical value of pi is assumed in the enclosure.

With N=120 for exp(12), and respectively N=24 and N=8 for the two
arctangents, the exact comparisons give

\[
 \frac{1627547914190039}{10^{10}}<e^{12}
       <\frac{1627547914190040}{10^{10}},\qquad
 \frac{3141592653589793}{10^{15}}<\pi
       <\frac{3141592653589794}{10^{15}}.              \tag{17}
\]

Let y_lo,y_hi be the exp endpoints divided by 12^4 and pi_lo,pi_hi
the pi endpoints. Bound the square root in A_- by the square roots
of 6y_lo/pi_hi and 6y_hi/pi_lo. Integer square roots with scale 10^18
give rational endpoints R_lo,R_hi whose squared inequalities are
checked exactly. Formula (16) with N=80 at c*y_lo and c*y_hi supplies
D_lo<exp(c*y_0)<D_hi. All endpoints are positive. With B=(3/2)/(133/54),

\[
 B R_{\rm lo}/D_{\rm hi}<A_-<B R_{\rm hi}/D_{\rm lo}.
\]

The exact endpoints and every Taylor remainder are stored in the
certificate, not just their decimal preview. Outward rounding to
15 decimal places is checked by rational comparison and gives

\[
 \frac{91190139998283}{10^{15}}<A_-
       <\frac{91190139998284}{10^{15}}
       <\frac{91191}{10^6}.                          \tag{18}
\]

The upper slack against 91191/10^6 exceeds 1/10^8, also checked
exactly. These scalar checks establish the coefficient only; the
analytic argument above establishes the all-parameter bound.

### Independent conceptual audit1647 — 19 November 2026

The unchanged SPECIALIZE assessment1645, separately source-approved1646,
covers this exact audit. The full proof and producer were checked,
together with C048c(4)-(10), its branch normalization and relevant audit,
and L799's general strip convergence/identity(4). The source comparison
and inspected primary cases in source-notes1644 were reused. The bound
(2), including its exact coefficient, survives without a mathematical
repair or additional hypothesis. This verifies a local reproduction,
not mathematics beyond the sources checked.

**Admissibility and normalization.** The stronger C048c facts apply
at the saddle, independently of this longer segment: U>3L/4 and
cos V>1/L give v_0=2r cos V/|w|>2r/L^2. On the entire segment,
x>7/2>|y|, so the principal logarithm and 1/u are valid. For each
fixed p the segment is compact inside the open theta strip; L799's
polynomial-times-Gaussian majorant applies to the complete series.
No uniform positive strip clearance at infinite L is needed.
Multiplying H by (2/u)exp(2p Log u) gives exactly g exp(h_p), hence
(5), without a missing Jacobian or a factor of two. C048c gives
arg(sqrt(A_0)),arg(w) in (-pi/4,pi/4); thus w sqrt(A_0)/2 has
positive real part and is the principal sqrt(p(1+w)). Substitution
recovers its exact S(p), and taking moduli gives sqrt(|A_0|/pi)
as the normalization factor in (1).

**Phase and full amplitude.** For sigma>=0 the numerator of Q' is
nonpositive since x>|y| and beta*y>=0. For sigma<0,
sigma*x+beta*y>=sigma*x_0+beta*y=v_0(x_0^2+y^2)>0;
then Q'=(sigma-2xQ)/(x^2+y^2)<0. Thus both cases give Q>=v_0.
Integrating this lower bound for H_p' backwards gives an upper
bound for H_p(x_0+s)-H_p(x_0), exactly (7). Conjugation covers the
lower half-plane, and positive real p and sigma=0 cause no division
by a vanishing height. All comparisons include the angular boundaries.
The theta parameter exceeds 2 because exp(L-2)/L^2 increases from
L=12 and exp(10)>7^5>144. For the full series,
(n^4+n^2/2)/n^4=1+1/(2n^2) decreases, proving the polynomial
ratio used in (9); the positive geometric sum therefore bounds every
mode. The left denominator ratio is bounded by 9/7, not by 1.
Its product with (10) is exactly 6975/4802<3/2, so (12) pays the
complete amplitude before integration.

**Tangent and all radii.** The tangent to f at -d is an upper bound
because f''=-4v_0 exp(2s)<0. Its derivative there is the positive
lambda in (13), so the integral towards -infinity is finite and
has denominator lambda, with the displayed orientation. Only this
scalar tangent is extended; all phase and theta estimates are used
on [-1,-d]. Integral Taylor remainders give the two opposing signs
needed for (14). With d<=1/36, their factors are 35/36 and 53/54;
multiplication by (19/10)r/L^2 yields exactly 133/54 and 1007/2430.
Multiplication by sqrt(6r/(pi L)) then gives L^(5/2)/sqrt(r) in
(15). Dividing by the required L^(9/2)/r leaves sqrt(y)exp(-cy).
Here y'=y(1-4/L)>0 and y>=y_0>7^6/12^4>5>1/(2c), so the last
function decreases over the entire range. This checks L=12 and
unbounded L analytically, without a sampled or asymptotic argument.

**Independent exact certificate.** Run

```bash
python3 scripts/mellin-horizontal-local/near_left_audit_1647.py
```

The complete evidence is
`scripts/mellin-horizontal-local/near_left_audit_1647.json`.
The checker does not import the producer or overwrite its certificate.
It recomputes the exponential sums using powers and factorials rather
than the producer's recurrence, and pairs the alternating arctangent
terms. The exp remainder ratio starts at x/(N+2), strictly below 1
in all three uses. The Machin tangent identities are exact; their
branch is fixed by 0<b<a<1/5 and 0<4a-b<4/5<pi/2. Root endpoints
are on the 10^-18 grid and their adjacent squared endpoints bracket
each positive radicand; no reliance on an unchecked isqrt output is
needed. The positive numerator is bounded upwards with pi_lo and
y_hi, while the denominator is bounded downwards using exp(c*y_lo);
the lower enclosure reverses these choices. Thus division has the
correct directions despite dependence on the same y_0.

All 15 original comparisons were independently reconstructed and all
292 schema/value checks match the saved certificate in full, including
the large rational Taylor remainders and unrounded endpoints. The
audit's 35 exact comparisons have no failures. They give precisely
(18), with upper slack >1/100000000. Selected full root and rounded
values were also inspected; truncated previews are not the verification.
The certificate establishes the fixed scalar bound; the preceding
argument establishes analytic uniformity.

The direct mathematical inputs remain C048c and the stated general
portion of L799. No L802, C048g, global contour, continued-origin or
complex-theta positivity premise is added. The distant-left/origin,
assembly, zero-count, inversion and mixed-sign gaps remain open.

## Mathlib

Full matching coverage is not checked; no absence claim is made.
This proof uses C048c's established sector/branch estimates, L799's
normal-convergence identity, elementary real convexity and Taylor
remainder signs, positive geometric tails, and exact rational scalar
comparisons. No specific Mathlib declaration or formal verification
is asserted. Audit1647 verifies the informal reproduction and exact scalar
evidence; it makes no claim of formal verification.
