# Corollary 645s: the oblique two-coefficient endpoint test misses the rate

## Hypotheses

Use C645g's normalized Hardy spaces and C645o's exact rotated weights.
Put d=5/4, x=-d, R=11/8, U=R^2, r=1/2, epsilon=10^(-6), and
t_j=j/n. For odd m>=3 and n=3m, take the distinct unit-residue poles

    a_l=x+i*r*cos((2*l-1)*pi/(2*m)), 1<=l<=m.

The same poles and residues are used for every angle. For |u|=1 set

    b_(t,u)(v)=R*(v-t*u)/(U-t*conjugate(u)*v),
    B_u(v)=product_j b_(t_j,u)(v), W(v,u)=B_u(x)/B_u(v),
    q_u(zeta)=sum_l [W(a_l,u)/R]/(zeta-a_l/R),
    c_k(u)=sum_l W(a_l,u)*a_l^k/R^(k+1), k=0,1.

Thus c_0,c_1 are the first two exterior Fourier coefficients of q_u.
Let J be the fixed angular interval |arg(u)-pi/6|<=epsilon, with
arg chosen near pi/6. This is the original rotation u=i*exp(i*theta),
including the conjugated denominator angle. Write

    E_01(J)=(1/(2*pi))*integral_J (|c_0(u)|^2+|c_1(u)|^2) d arg(u).

## Conclusion

There is a constant C independent of m,n and u in J such that

    (|c_0(u)|^2+|c_1(u)|^2)^(1/2)
         <= C*sqrt(n)*exp(-7*n/200).                         (1)

Consequently exp(n/32)*sqrt(E_01(J)) tends to zero through this
admissible sequence. In particular C645r's first-two-coefficient
endpoint method, placed at this oblique grid and on this interval,
cannot give a uniform exp(-n/32) lower bound for all 9/20<=r<=1/2.
The endpoint r=1/2 already obstructs that particular test.

This is NOT an upper bound for ||q_u||_2, ||H_q_u||, their full
angular means, or the full angular mean of the two coefficients.
Other angular intervals, higher spatial coefficients, other inputs
and the main uniform angular detector remain open. The result is a
local method obstruction, not an RH disproof or an actual-Xi result.
It has not received a separate conceptual audit. Originality is not
certified; the source comparison did not supply this quantitative stop.

## Proof

### Source scope and purpose

Reuse the unchanged EXPLORE scope of
[the angular assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md).
C645r gives the audited endpoint-contour method, C645l (23)--(24)
the exact finite-node identity, C645g the normalization and C645o
the exact weights. Only those stated portions are used. The earlier
fixed-direction, ellipse-envelope, full-inner-input, entry-sign and
zero-evaluation stops are comparisons, not premises of (1).

The standard imported inputs are the residue theorem and simple-pole
rule in R. W. Howell and J. H. Mathews, *Complex Analysis*, online
edition (front matter updated 22 August 2025),
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and the contour-integral inequality in
[Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
The operator convention is L. Baratchart, S. Chevillard and T. Qian,
*Minimax principle and lower bounds in H2-rational approximation*,
J. Approx. Theory 206 (2016), 17--47, preprint v2,
[Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Scalar Parseval is A. Levitt, *Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.11/Corollary 1.12,
printed p.8 (PDF p.14). The inspected source assessments are reused;
no general theorem is reproved. Our circle measure is divided by 2*pi.

None of these general identities supplies the oblique rates below.
The finite rational calculation is needed to decide the nominated
extension, rather than to reproduce a known bound as a discovery.

### 1. Geometry and angular loss

The poles include x, are distinct, and satisfy M=m=n/3 and

    |a_l|^2<=29/16<(R-eta)^2, eta=1/100,
    (R-eta)^2-29/16=2029/40000.

All rotated grid zeros have modulus <1<d, so they avoid the poles.
The exterior expansion of q_u converges absolutely on the unit circle.
In particular H_q_u 1=q_u and ||H_q_u||>=||(c_0,c_1)||. An upper
bound on this lower test is not an upper bound on the operator.

Put u_0=exp(i*pi/6), c=sqrt(3)/2. All contours below have

    v=-h+i*y, h>=23/20, |y|<=51/100, |v|<2.                (2)

For u in J, cos(arg u)>.86 and |sin(arg u)|<.501. Hence
Re(conjugate(u)*v)<0 and

    |v-t*u|>=h, |U-t*conjugate(u)*v|>=U, 0<=t<=1.

There are no zeros or poles of B on these contours or their interiors.
The same bounds apply to the anchor x. Differentiating each factor
with respect to its angle gives

    |partial_phi log b_(t,exp(i*phi))(v)|
         <=1/h+2/U<2.

Integration of the real logarithm of the modulus, first at v and
then at x, gives the uniform bound

    |log|W(v,u)|-log|W(v,u_0)||<=4*n*epsilon.                (3)

The angular interval has fixed positive measure; no exponential
loss from shrinking its length is being omitted.

### 2. Both oblique endpoint weights decay too quickly

Let a_+=-d+i/2 and a_-=-d-i/2 denote segment endpoints, not extra
poles. For v=-h+i*y at u_0, define

    D1(h,y,t)=h^2+y^2+2*h*c*t-y*t+t^2,
    D2(h,y,t)=U^2+2*U*h*c*t-U*y*t+t^2*(h^2+y^2).

Then |b_(t,u_0)(v)|^2=U*D1/D2. Set

    z_sigma(t)=D1(d,sigma/2,t)*D2(d,0,t)
                  /(D1(d,0,t)*D2(d,sigma/2,t)),
    f_sigma(t)=(1/2)*log z_sigma(t), sigma in {-1,1}.

The exact rational certificate described in Section 6 proves

    integral_0^1 f_-(t)dt >=79716669307661/2048000000000000,
    integral_0^1 f_+(t)dt >=154217206077577/4096000000000000,
    both lower bounds >9/250=.036.                         (4)

These are rigorous lower bounds, not numerical quadrature estimates.
Also |f_sigma'(t)|<=2/d+(R+d)/U<4: differentiate the two logarithmic
factor moduli, use the denominator bounds above, and |a_sigma|<R.
Comparison on every interval [j/n,(j+1)/n] therefore gives

    sum_j f_sigma(j/n)>=n*integral_0^1 f_sigma(t)dt-4.

Since -log|W(a_sigma,u_0)| is exactly this sum, (3)--(4) imply

    |W(a_+,u)|, |W(a_-,u)|<=e^4*exp(-alpha*n),
    alpha=9/250-4*epsilon=8999/250000=.035996.               (5)

### 3. The continuous coefficients have the same upper decay

For k=0,1 write

    F_k(v,u)=W(v,u)*v^k/R^(k+1),
    A_k(u)=(1/pi)*integral_(-r)^r F_k(x+i*y,u)/sqrt(r^2-y^2)dy.

Use C645r's exact three-side deformation with width s=1/2: from
a_- to a_--s, then to a_+-s, then to a_+. On this rectangle
S(v)=sqrt((v-x)^2+r^2) has positive real part in its interior and
continues from the positive root on the original open segment. The
radicand has positive real part in the interior; endpoint zeros are
simple. Its exact identity is

    A_k=(1/(pi*i))*integral_(three sides) F_k(v,u)/S(v)dv.    (6)

Here F_k is holomorphic throughout the rectangle, since the grid
zeros lie to its right. Thus the hypotheses of that deformation
hold also at this oblique angle. Truncated endpoint arcs vanish as
O(sqrt(h)) for each finite n; there is no boundary-resolvent pole.

Let p_n(v,u)=-(log B_u)'(v)/n. At u_0 a single summand has real part

    (U-t^2)*[h*(U+t^2)+t*c*(U+h^2-y^2)-t*h*y]
                                             /(D1*D2).    (7)

For d<=h<=7/4, |y|<=1/2 the numerator is greater than
(U-1)*d*(U-1/2)>3/2. The denominator is less than
(73/40+1)^2*(U+73/40)^2<111, since |v|^2<=53/16<(73/40)^2.
The angular derivative of a summand of p_n has modulus at most
1/d^2+1/U<2. Thus throughout the endpoint segments, for every u in J,

    Re p_n(v,u)>3/222-2*epsilon>1/100.                      (8)

Exactly, for 0<=h'<=s,

    W(a_sigma-h',u)=W(a_sigma,u)
       *exp(-n*integral_0^(h') p_n(a_sigma-t,u)dt).

On these segments S(a_sigma-h')=sqrt(h')*sqrt(h'-sigma*i).
The remaining amplitude in (6) is uniformly bounded for k=0,1.
By (8), the absolute horizontal integrals are at most

    C*|W(a_sigma,u)|*integral_0^s exp(-n*h'/100)/sqrt(h')dh'
       <= C'*n^(-1/2)*|W(a_sigma,u)|.                      (9)

The last inequality follows by scaling; the integral of
exp(-t/100)/sqrt(t) on (0,infinity) is finite. No asymptotic expansion
or cancellation of endpoint phases is needed for this upper bound.

On the connector v=-7/4+i*y, |y|<=1/2, one has |v|>R. Therefore
|b_(t,u_0)(v)|>1>|b_(t,u_0)(x)|, by subtracting the two sides of
U*D1-D2=(|v|^2-U)*(U-t^2). For t<=1/2 a stronger ratio bound is

    |b_(t,u_0)(v)/b_(t,u_0)(x)|
      >= (7/4+c*t)/(d+t)*(U+d*c*t)/(U+(73/40)*t)
      >= K_0,
    K_0=((7/4+433/1000)/(7/4))
                       *((U+433/800)/(U+73/80))>1.         (10)

For the first inequality use |v-tu_0|>=7/4+c*t,
|U-t*conjugate(u_0)*v|<=U+(73/40)*t,
|x-tu_0|<=d+t and |U-t*conjugate(u_0)*x|>=U+d*c*t.
Both displayed ratios decrease with t; c>433/500, so evaluation
at t=1/2 gives the second inequality. At least n/2 grid indices
have t_j<=1/2. Since log K_0>=1-1/K_0, the certificate checks

    (1-1/K_0)/2=215101/5662702>3/80.

The other indices contribute nonnegative gains. Equations (3) and
(10) give |W(v,u)|<=exp(-kappa*n) on the connector, where
kappa=3/80-4*epsilon=.037496. There |S(v)|>=1/2, so its integral
is O(exp(-kappa*n)). Combining (5), (6), (9) yields

    |A_k(u)|<=C*n^(-1/2)*exp(-alpha*n)+C*exp(-kappa*n).      (11)

### 4. The finite-node error also decays faster than the threshold

Use the ellipse centered at x with horizontal semiaxis s_e=1/10
and vertical semiaxis b=sqrt(26)/10<51/100. Its parameter is

    rho=(sqrt(r^2+s_e^2)+s_e)/r=(sqrt(26)+1)/5.

It lies in (2), with 23/20<=h<=27/20. For fixed y on this strip,
the numerator in (7) is positive: dropping its positive middle term
leaves at least (U-1)*h*(U-|y|)>0. Thus |b_(t,u_0)(-h+i*y)|
increases with h. It suffices to bound its minimum at h_0=23/20.
For all real y and all t in [0,1], the exact certificate proves

    (121/100)*D1(h_0,y,t)*D2(d,0,t)
                     -D1(d,0,t)*D2(h_0,y,t)>0.             (12)

Only |y|<=51/100 is needed for the preceding monotonicity step.
Consequently every factor on the ellipse satisfies

    |b_(t,u_0)(x)/b_(t,u_0)(v)|<11/10.

The factor denominators there are nonzero, so (12) permits division.
Using log(11/10)<=1/10-1/200+1/3000=143/1500 and (3),

    sup_ellipse |F_k(v,u)|<=2*exp((143/1500+4*epsilon)*n).    (13)

C645l's exact finite-node identity (23)--(24), applied to this
holomorphic F_k, now gives

    |c_k(u)/m-A_k(u)|
         <=2*sup_ellipse |F_k(v,u)|/(rho^(2*m)-1).          (14)

The exponent is exactly 2m, with the m prescribed unit residues.
The exterior ellipse branch used by that identity is distinct from
the rectangle branch in (6); its dw/S_0=d lambda/lambda normalization
and the original arcsine average are unchanged.

Finally log rho=asinh(1/5)>=1/sqrt(26)>1961/10000. For n>=9,
2m log rho>1, so (rho^(2m)-1)^(-1)<2*rho^(-2m). Thus (13)--(14)
give

    |c_k/m-A_k|<=8*exp(-tau*n),
    tau=(2/3)*(1961/10000)-143/1500-4*epsilon
        =8849/250000=.035396>7/200.                         (15)

### 5. Comparison with the proposed exponent

Multiplying (11), (15) by m=n/3, and using both k=0,1, gives

    ||(c_0,c_1)||<=C*[sqrt(n)*exp(-alpha*n)
                   +n*exp(-kappa*n)+n*exp(-tau*n)].         (16)

All three rates alpha, kappa, tau strictly exceed beta=7/200.
The functions sqrt(n)*exp(-(kappa-beta)*n) and
sqrt(n)*exp(-(tau-beta)*n) are bounded for n>=9. This proves (1)
with one constant throughout J. Integrating (1) over its fixed
normalized measure proves the stated bound for E_01(J). Since
beta-1/32=3/800>0, the scaled root energy tends to zero.

Every estimate is uniform in u in J and along all odd m>=3. No
finite angular sweep or subsequence chosen by phase replaces that
statement. Nothing in (16) controls the omitted coefficients or angles.

### 6. Exact certificate and its scope

Reproduce from this notebook with

    python3 scripts/one-sided-hankel/angular-oblique-rate-certificate.py

The adjacent `.json` stores every interval-cell lower bound, all
parameters, rounded values, auxiliary checks and failures. All
certificate arithmetic uses Python Fraction; decimal output is only
a preview. The cosine enclosure is

    8660254037844386467/10^19 < c < 8660254037844386468/10^19,

verified by squaring against 3/4. Partition [0,1] into 4096 closed
intervals. Rational interval arithmetic uses the four endpoint products
for multiplication and reverses endpoints when taking a positive
reciprocal, so it encloses every intermediate value, even when the
same variable occurs repeatedly.

For (4), each interval gives a positive lower bound z_low>1 for
z_sigma(t). Put w=(z_low-1)/(z_low+1). The identity
log z=2*integral_0^((z-1)/(z+1)) 1/(1-s^2)ds and
1/(1-s^2)>=1+s^2 imply f_sigma(t)>=w+w^3/3. Each cell's bound
is rounded down to a multiple of 10^(-12); averaging those lower
bounds gives exactly (4). All denominators were positive. This is
a bound on the entire intervals, not on sampled integrand values.

For (12), put D1x=D1(d,0,t), D2x=D2(d,0,t), K=121/100. Its
left side is the quadratic A*y^2-t*B*y+C, where

    A=K*D2x-t^2*D1x, B=K*D2x-U*D1x,
    C=K*(h_0^2+2*h_0*c*t+t^2)*D2x
                 -(U^2+2*U*h_0*c*t+t^2*h_0^2)*D1x.

Over all 4096 cells the downward-rounded interval lower bounds obey

    A>=1081275001123/250000000000>0,
    4*A*C-t^2*B^2>=568836433547/250000000000>0.

Completing the square gives positivity for every real y, proving
(12). No sign has been inferred from a floating-point discriminant.
All 19 rational checks passed; failures are empty. The
complete selected endpoint, ellipse-minimum, auxiliary-check and
failure fields were inspected using the shared JSON inspector.
The script verifies these finite inequalities, not the analytic
deformation or the full angular detector. The earlier diagnostic file
`scripts/one-sided-hankel/angular-oblique-diagnostic.json` is not an
input to any proof and is retained only as exploratory evidence.

## Mathlib

Full matching coverage has not been checked; no absence claim is made.
Supporting ingredients are scalar Fourier identities, the residue and
contour theorems, finite rational products and elementary inequalities.
The cited general tools do not themselves assert the quantitative
oblique two-coefficient obstruction.
