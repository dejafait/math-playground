# Lemma 505: obstruction for the two-height positive-multiplier family

## Hypotheses

Retain L504's fixed R>0 and definitions

    L=log T, a=log L/pi, b=a/4, B=L/(4pi),
    lambda=pi/(2a), K(x)=1-(sin(pi x)/(pi x))^2, K(0)=0.

Here T is a sufficiently large real number. The real vector space V_R
consists of even entire functions, real on R, with smooth compactly
supported Fourier data in [-R,R], using exp(2pi i v z). Write
u(x,y)=Re f(x+iy), N(f)=integral_R |f(x)|dx and
M(f)=integral_R |f(x)|K(x)dx. The normalized subset H_a satisfies

    u(x,y)>=1 for |x|<=a and b<|y|<B.

There is no sign assumption on V_R, no gap sign on H_a and no uniform
Fourier-derivative bound. Retain Q_a and E_a=Q_a+P_b from L504. For
h in {b,2b} and 0<=y<b define

    p_h(t,y)=(1/(2h)) Re sech(pi(t+iy)/(2h)),
    w_h(t)=integral_0^b exp(-lambda y)p_h(t,y)dy,
    W_{h,b}(x)=w_h(x-a)+w_h(x+a),
    P_h(f)=integral_{-a}^a W_{h,b}(x)u(x,h)dx.

The possible infinite value w_b(0) is interpreted as an integrable
density singularity, not an atom. For arbitrary finite real
alpha,beta>=0 put

    F_{alpha,beta}=E_a+alpha P_b+beta P_{2b},
    ||F||_M=sup_{0!=f in V_R} |F(f)|/M(f).

Coefficients may depend arbitrarily on a and R. No boundedness,
attainment or strong-duality assertion is assumed for this optimization.
L504 is the sole local theorem input; its elementary kernel transform
is used with a rescaled height. No conclusion of L503 is used.

## Conclusion

The kernels and functionals are well defined, with absolutely convergent
integrals, and have angular Fourier normalization

    integral_R p_h(t,y)exp(i s t)dt=cosh(sy)/cosh(sh).       (1)

For f in H_a, at every sufficiently large T,

    Q_a(f)<=E_a(f)<=F_{alpha,beta}(f).                     (2)

Thus an O_R(a) bound on this full-space M norm would give the proposed
one-sided bound for E_a on H_a. However there are c_R>0 and T_R such
that, for every real T>=T_R and every alpha,beta>=0,

    ||F_{alpha,beta}||_M>=c_R L^(R/4)/a^2.                 (3)

In fact one f_a in V_R, independent of alpha and beta, has E_a(f_a)<0,
P_b(f_a)<0 and P_{2b}(f_a)<0 and proves (3). Consequently the infimum
over the entire nonnegative coefficient family, divided by a, tends
to infinity. The desired O_R(a) certificate is impossible in this
family, even with unbounded coefficient choices varying with a.

This is a full-space obstruction only. The witnesses do not belong to
H_a. It does not refute E_a<=C_R a M or Q_a<=C_R a M on H_a, exclude
other positive measures, give a detector-cost theorem or prove any
actual-Xi signs or height transfer. The independent critical audit of
2026-10-30 passes for precisely this scope; no stronger estimate or
originality claim is certified.

## Proof

### Applicability and the endpoint

L504 proves its kernel transform for every positive strip height.
More explicitly, starting with its kernel p_b, the identity

    p_h(t,y)=(b/h)p_b(bt/h,by/h)

and the substitution q=bt/h in its transform (6), with frequency
s h/b, give (1). The permitted range is |y|<h; our 0<=y<b lies in
that range for both heights. Angular frequency s equals 2pi v in
the convention defining V_R. This is a scaling of the established
kernel identity, not a new source theorem or a new normalization.

For r=pi t/(2h) and theta=pi y/(2h),

    p_h(t,y)=cosh(r)cos(theta)
                 /[2h(sinh(r)^2+cos(theta)^2)].             (4)

It is positive and even in t. By (1) at s=0 it has mass 1. Tonelli
therefore gives

    integral_R w_h(t)dt=integral_0^b exp(-lambda y)dy<=b.    (5)

In particular W_{h,b} is a nonnegative integrable density of mass at
most 2b. L504's fixed-height Schwartz property of u(x,h) and (5)
give absolute convergence of every integral above. The endpoint y=b
in w_b is reached only as an improper integral: (5) proves its
integrability, including the possible point singularity at t=0.
For h=2b, the entire integration interval is below the strip height.

Formula (1), the compact Fourier support and Fubini also give

    u(x,y)=integral_R p_h(x-t,y)u(t,h)dt, 0<=y<b,
    Q_a(f)=-integral_R W_{h,b}(x)u(x,h)dx.                 (6)

For example |u(t,h)| is bounded and p_h has mass 1; after integration
in y, (5) supplies an integrable majorant. Thus (6) is a continuum
identity, not a formula on a sampled set of frequencies.

For a>=1, B=e^(pi a)/(4pi)>a/2=2b; the strict inequality follows
from e^x>2x for x>0. Hence the H_a condition applies at height 2b,
and continuity from y>b supplies u(x,b)>=1 on the closed interval
[-a,a], including its two endpoints. Consequently

    P_h(f)>=integral_{-a}^a W_{h,b}(x)dx>=0  (f in H_a).

Together with L504's Q_a<=E_a, this proves (2). No positivity in
0<=y<b or outside |x|<=a was used. The upper inference from a norm
bound would be F(f)<=|F(f)|<=||F||_M M(f); no converse is asserted.

### A phase where both clipped terms have the same sign

For t>0 and 0<=y<b, the derivative in r of (4) is

    -cos(theta)sinh(r)[sinh(r)^2+2-cos(theta)^2]
      /[2h(sinh(r)^2+cos(theta)^2)^2]<0.

Thus w_h is positive and decreasing on t>0. Put theta_0=lambda b=pi/8.
For c=1,2 the scaling t=b r, y=b v yields

    w_{cb}(br)=G_c(r),
    G_c(r)=(1/(2c))integral_0^1 exp(-theta_0 v)
                                 Re sech(pi(r+iv)/(2c))dv.

In particular the numbers

    m_c=G_c(8)=w_{cb}(2a)>0                            (7)

are finite absolute constants independent of a. Positivity follows
from (4) on 0<=v<1, and at r=8 the denominator stays nonzero even
at v=1. No numerical lower approximation to m_c is needed.

Choose s>0 and an integer n>=0 with

    sa=2pi n+3pi/2.

Temporarily let g(z)=cos(sz). This is not yet a member of V_R.
Since cos(sa)=0, its gap term Q_a(g) is zero. Evenness and a change
of variable give the exact compact integral

    integral_{-a}^a W_{h,b}(x)cos(sx)dx
      =2 integral_0^{2a} w_h(t)cos(s(a-t))dt
      =-2 integral_0^{2a} w_h(t)sin(st)dt.             (8)

There are 4n+3 half-periods in [0,2a], an odd number. Set
v_h(t)=w_h(t)-w_h(2a), which is nonnegative and decreasing on this
interval and integrable even when h=b. Each consecutive positive
and negative pair of sine half-periods contributes

    integral_0^{pi/s}
      [v_h(2j*pi/s+t)-v_h((2j+1)*pi/s+t)]sin(st)dt>=0,
       j=0,...,2n.

The remaining last half-period is positive and contributes a
nonnegative integral. All these integrals are absolutely convergent
by (5); the endpoint value at zero is immaterial. The constant part
has integral 2w_h(2a)/s since cos(2as)=-1. Therefore

    integral_0^{2a} w_h(t)sin(st)dt>=2m_c/s,
    P_{cb}(g)<=-4m_c cosh(scb)/s<=-2m_c exp(scb)/s.    (9)

As E_a(g)=P_b(g), both multipliers reinforce its negative sign. This
calculation controls the complete residual for every nonnegative
coefficient choice, rather than fixing those choices before a limit.
It remains to preserve all three signs on genuine V_R functions.

### Smooth witnesses and a common onset

Fix an even nonnegative chi in C_c^infinity((-1,1)) of integral 1,
and write

    psi(z)=integral chi(v)exp(2pi i v z)dv,
    H=integral_R |psi(x)|dx,  0<H<infinity.

These properties follow from smooth Fourier inversion and integration
by parts as in L504; psi(0)=1. For each sufficiently large a set

    n=floor(Ra/2-3/4), s=(2pi/a)(n+3/4), A=a^2,
    f_a(z)=psi(z/A)cos(sz).                           (10)

For a>=4/R, n>=0 and

    pi R/2<=s<=pi R, s>=pi R-2pi/a.

Its Fourier data are

    (A/2)[chi(A(v-s/(2pi)))+chi(A(v+s/(2pi)))].

These are smooth, even and supported in [-R,R] whenever 1/a^2<=R/2.
Thus f_a lies in V_R, f_a(0)=1 and

    0<M(f_a)<=N(f_a)<=a^2 H.                          (11)

The first inequality is L504's strict positivity of M on nonzero
functions. Only M<=N is used; no reverse weighted-norm conversion
or derivative bound is assumed.

Evenness of chi and the integral remainder for cosine give

    |psi(w)-1|<=2pi^2 |w|^2 exp(2pi |Im w|).

On |x|<=a, 0<=y<=2b=a/2, and a>=1, with w=(x+iy)/a^2,
this is at most epsilon_a=C/a^2, where C=(5pi^2/2)exp(pi).
Since |cos(s(x+iy))|<=exp(sy), (5) gives

    |P_h(f_a)-P_h(g)|<=2b epsilon_a exp(sh),
    |Q_a(f_a)-Q_a(g)|<=2epsilon_a exp(sb)/s,
    |E_a(f_a)-E_a(g)|<=2epsilon_a(b+1/s)exp(sb).      (12)

Let m=min(m_1,m_2)>0 and choose the following common sufficient onset:

    a_R=max(1,4/R,sqrt(2/R),C*pi*R/m,2sqrt(C/m)).      (13)

For a>=a_R all support, phase and rectangle requirements hold, and

    2epsilon_a(bs+1)
       <=C*pi*R/(2a)+2C/a^2<=m.

Using (9) and (12), simultaneously at both heights,

    E_a(f_a)<=-m_1 exp(sb)/s,
    P_b(f_a)<=-m_1 exp(sb)/s,
    P_{2b}(f_a)<=-m_2 exp(2sb)/s.                    (14)

These are individual sign margins, so multiplying them by arbitrarily
large nonnegative coefficients creates no uncontrolled error. In fact

    -F_{alpha,beta}(f_a)
      >=[(1+alpha)m_1 exp(sb)+beta m_2 exp(2sb)]/s.   (15)

Combining (11), (15), s<=pi R and s>=pi R-2pi/a proves

    ||F_{alpha,beta}||_M
      >=m_1 exp(sb)/(pi R a^2 H)
      >=[m_1 exp(-pi/2)/(pi R H)] L^(R/4)/a^2.

Take c_R=m_1 exp(-pi/2)/(pi R H) and
T_R=exp(exp(pi a_R)). This holds for every real T>=T_R, including
the jumps of the floor in (10), uniformly over all coefficients.
The ratio of (3) to a diverges because R>0 is fixed. This proves the
obstruction to the requested infimum bound, without assuming an
optimizer exists or that the M norm is finite for every coefficient.

Finally (14) and the nonnegative P_b on H_a show explicitly that
these f_a are not in H_a. The proof therefore leaves the constrained
upper estimates, other measures and actual-Xi realization unresolved.

### Independent critical audit, 2026-10-30

The audit replayed (1)--(15), using only L504 as a local theorem input.
The scaling of p_b multiplies it by b/h and changes its angular
frequency to sh/b, giving exactly cosh(sy)/cosh(sh). In (4),
cos(theta)>0 for y<h; at h=b the missing endpoint y=b has measure
zero. Positivity, unit mass and Tonelli prove (5), including the
integrable t=0 singularity. Each fixed-height trace is bounded and
Schwartz. The compact Fourier integral and the unit kernel mass
therefore justify (6) before and after integration in y. No boundary
atom or singular endpoint evaluation is introduced. For a>=1,
e^(pi a)>2pi a proves B>2b. Continuity from the open positive
rectangle gives u(x,b)>=1 also at x=+-a. At height 2b positivity
holds directly. These are exactly the signs required for (2).

Differentiating (4) gives the negative derivative displayed above;
integrating in y makes w_h decreasing for t>0. The scaled G_c(8)
is finite and strictly positive for c=1,2, uniformly in a. At the
selected phase, cos(sa)=0 and sin(sa)=-1, so Q_a(g)=0 and the
clipped cosine integral is the negative sine integral in (8).
The count 2as/pi=4n+3 consists of 2n+1 consecutive
positive/negative pairs, indexed j=0,...,2n, and one final positive
half-period. Subtracting m_c=w_h(2a) leaves a nonnegative decreasing
integrable function. Each pair has the displayed nonnegative
integral even when the value at t=0 is infinite; the number of pairs
is finite and all integrals are absolutely convergent. The constant
part integrates to 2m_c/s. Thus P_{cb}(g)<=-2m_c exp(scb)/s,
with the same phase at both heights and E_a(g)=P_b(g).

The floor choice in (10) gives pi R-2pi/a<=s<=pi R and,
for a>=4/R, s>=pi R/2 and n>=0. The two Fourier packets are
centered at +-s/(2pi), with half-width at most 1/a^2; the support
condition in (13) places them inside [-R,R]. Evenness and reality
are preserved, f_a(0)=1, and M<=N<=a^2 H. There is no use of
N<=C M or any bound on derivatives of the Fourier data.

For the smoothing error, |(x+iy)/a^2|^2<=5/(4a^2) and
2pi|y|/a^2<=pi when |x|<=a, 0<=y<=2b and a>=1.
The cosine remainder therefore gives the stated C/a^2. Kernel
mass at most 2b bounds the P_h errors, while direct integration of
exp(sy) bounds the Q_a error. At the displayed common onset,

    2 epsilon_a(bs+1)<=C pi R/(2a)+2C/a^2<=m.

Hence the E error is at most m exp(sb)/s, and each P_h error is
at most m exp(sh)/s. Since m<=m_c, all three signs in (14)
hold separately before alpha,beta are chosen. This is the required
uniformity for coefficients growing arbitrarily with a: no error
estimate is applied after multiplying by an uncontrolled coefficient.
Equation (15), the upper bound on M, and s>=pi R-2pi/a yield
exactly the stated positive c_R and all-real-T onset T_R. No
subsequence, norm finiteness, or infimum attainment is needed.

The resulting lower bound divided by a tends to infinity for each
fixed R>0. Since P_b(f_a)<0 whereas P_b>=0 on H_a, the witnesses
are outside H_a. The audit thus validates only the two-scalar
full-space stop, not a counterexample to either constrained bound,
an arbitrary-measure obstruction, an L503 conclusion or RH.

## Mathlib

Full matching coverage is unchecked. The proof uses elementary
hyperbolic algebra, integrable monotone functions and Schwartz Fourier
inversion; no matching Mathlib theorem name is asserted. Unknown
availability is not evidence of absence.

The prior assessment is
`drafts/literature/2026-10-30-l504-two-height-positive-multiplier-test.md`.
It reused Brevig--Chirre--Ortega-Cerda--Seip, *Point evaluation in
Paley--Wiener spaces*, [arXiv:2210.13922v2](https://arxiv.org/pdf/2210.13922v2),
Theorem 3.10, printed pp. 14--15, and its endpoint warning, together
with the stated constrained-duality and positive-harmonic comparisons.
None is a premise implying the obstruction proved here. The kernel
scaling is reproduction of L504's classical calculation, needed to
verify the new family's applicability. The exact uniform obstruction
was not identified in the checked sources; this is not a novelty claim.
