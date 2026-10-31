# Lemma 487: quartic heat collision obstructs bounded negative-energy comparison

## Hypotheses

Let P(z)=(z^2-1)^2, h=1/100, I=[-2,2], and, for -h<=lambda<=0, set

    H_lambda(z)=P(z)-lambda P''(z)+(lambda^2/2)P''''(z).
    q_lambda(x)=H_lambda'(x)^2-H_lambda(x)H_lambda''(x),
    E_lambda=integral_I (-q_lambda(x))_+ dx.

Spatial primes denote x derivatives. The proposed external diffusion
flux is the sum of the two outward normal derivatives of (-q_lambda)_+
at the endpoints of I. No theta representation, actual-Xi realization,
or zero simplicity is assumed.

## Conclusion

This real even degree-four polynomial family satisfies
partial_lambda H_lambda=-partial_z^2 H_lambda and H_0(0)=1. For every
parameter, H_lambda(iy)>0 for all real y, all its complex zeros satisfy
|Im z|<=sqrt(3/100)<1/2, and q_lambda>0 on both fixed collars
[-2,-7/4] and [7/4,2]. Its external diffusion flux is zero.

At lambda=0, H_0 has double real zeros at +-1 and E_0=0. For every
-h<=lambda<0, E_lambda>0. The energy is Lipschitz on [-h,0], is smooth
away from zero, and has one-sided derivative zero at zero. Writing t=-lambda,

    E_{-t}=(512 sqrt(2)/3)t^(3/2)+O(t^2),
    d E_{-t}/dt=256 sqrt(2)t^(1/2)+O(t),
    lim_{t down to 0} t [-partial_lambda E_lambda/E_lambda]_{lambda=-t}=3/2.

Consequently no measurable C locally essentially bounded through
lambda=0 can satisfy -partial_lambda E_lambda<=C(lambda)E_lambda
almost everywhere on a left neighborhood of zero. Dependence of C on
this fixed family, I and its bounded jets does not repair the failure.
The explicit energy and its internal-interface terms are calculated below.

This is an obstruction to this generic comparison, not an actual-Xi
sign result, a disproof of RH, or a counterexample using the theta kernel.
It does not exclude singular coefficients, additional hypotheses that
rule out the collision, or other energy functionals.

## Proof

### Exact evolution, jets and zeros

Use t=-lambda in [0,h] and write F(t,z)=H_{-t}(z). Put

    beta=-2+12t,  gamma=1-4t+12t^2,
    F(t,z)=z^4+beta z^2+gamma.

The finite heat sum in the hypotheses gives exactly this expression:
P''=12z^2-4 and P''''=24. Its relevant jets are

    F_x=4x^3+2beta x,       F_xx=12x^2+2beta,
    F_xxx=24x,             F_xxxx=24,
    F_t=12x^2-4+24t=F_xx,
    F_xt=24x,              F_xxt=24,       F_tt=24.

Higher spatial derivatives after order four vanish. These identities
prove both the heat equation and its lambda sign. On the compact
rectangle, |beta|<=2 and 24/25<=gamma<=1. In particular valid bounds for
|F|, |F_x|, |F_xx|, |F_xxx|, |F_xxxx| are respectively 25,40,52,48,24;
the listed time jets are bounded as well. No singular jet develops at
the collision. Also F(0,0)=1 and

    F(t,iy)=y^4+(2-12t)y^2+gamma>0

for every real y and every parameter.

For t>0, the two roots of the polynomial in w=z^2 are

    w=1-6t +- i sqrt(8t-24t^2).

They are nonreal, distinct and nonzero. Their common modulus is
sqrt(gamma), since (1-6t)^2+8t-24t^2=gamma. For any square root z of
either w,

    (Im z)^2=(sqrt(gamma)-(1-6t))/2<=3t<=3/100<1/4.

This proves the strip claim for all four roots; at t=0 the roots are
the double real roots +-1. In fact F(t,x)>0 on the real axis for t>0:
complete the square in x^2 to get

    F(t,x)=(x^2-(1-6t))^2+8t-24t^2>0.

Real-line positivity fails exactly at the two terminal collision points,
so a positive-solution theorem requiring positivity through the terminal
slice does not apply.

### Complete defect sign regions and zero external flux

Write q(t,x)=q_{-t}(x). Direct differentiation, with the jets above, gives

    q=4x^6+2beta x^4+(2beta^2-12gamma)x^2-2beta gamma
     =4Q(t,x^2),

    Q(t,v)=v^3+(-1+6t)v^2+(-1-12t+36t^2)v
                       +1-10t+36t^2-72t^3.

At t=0, q(0,x)=4(x^2-1)^2(x^2+1)>=0. For 0<t<=h,

    Q(t,0)=(1-6t)gamma>0,
    Q(t,1)=-8t(1-3t)(2-3t)<0,
    Q(t,1/2)=3/8-(29/2)t+54t^2-72t^3>1/5,
    Q(t,3/2)=5/8-(29/2)t+90t^2-72t^3>2/5.

For the last two strict inequalities, discard the positive t^2 term
and bound the subtracted terms by 29/200+72/1000000. The resulting
lower bounds are respectively 28741/125000>1/5 and
59991/125000>2/5. Thus the cubic
has roots r_-(t) in (1/2,1) and r_+(t) in (1,3/2). It also has a
negative root, because Q(t,0)>0 and Q(t,v) tends to minus infinity as
v tends to minus infinity. These three distinct roots exhaust its
degree, so they are simple, and the leading positive coefficient fixes
all signs on v>=0. In particular, setting

    a(t)=sqrt(r_-(t)),       b(t)=sqrt(r_+(t)),

the entire negative set in I is exactly

    (-b(t),-a(t)) union (a(t),b(t)).

The defect is zero at those four endpoints and strictly positive on
the complement of their closures. Since (7/4)^2>3/2, it is positive on
both required collars for every t>0. The t=0 formula proves the same
collar condition there. Consequently (-q)_+ is identically zero in
fixed neighborhoods of both external endpoints, and both normal
derivatives, hence the external flux, vanish. This conclusion does not
set any internal-interface trace to zero.

### Exact energy, time differentiation and internal interfaces

For t>0 the real analytic implicit function theorem applies to each
simple cubic root, so a(t),b(t) are smooth on (0,h], with one-sided
interpretation at h. Define the spatial primitives

    G(t,x)=x^7/7+(-1+6t)x^5/5+(-1-12t+36t^2)x^3/3
                                      +(1-10t+36t^2-72t^3)x,
    J(t,x)=6x^5/5+(-12+72t)x^3/3+(-10+72t-216t^2)x.

Here G_x=Q(t,x^2) and J=G_t. Exact integration over both negative
intervals gives, with e(t)=E_{-t},

    e(t)=-2 integral_{a(t)}^{b(t)} q(t,x) dx
        =8[G(t,a(t))-G(t,b(t))]>0.                       (1)

The moving-endpoint terms in the time derivative vanish because
q(t,a(t))=q(t,b(t))=0. Thus Leibniz's rule gives the exact formula

    e'(t)=-2 integral_a^b partial_t q(t,x) dx
         =8[J(t,a(t))-J(t,b(t))].                       (2)

For completeness, the relevant defect jets and its heat balance are

    q_x=24x^5+8beta x^3+(4beta^2-24gamma)x,
    q_xx=120x^4+24beta x^2+4beta^2-24gamma,
    partial_t q=24x^4+(-48+288t)x^2-40+288t-864t^2,
    partial_t q=q_xx-2(F_xx^2-F_x F_xxx)
               =q_xx-(96x^4+8beta^2).                 (3)

Integrating (3) on each of the two negative intervals yields

    e'(t)=-2[q_x(t,b)-q_x(t,a)]
                         +2 integral_a^b (96x^4+8beta^2) dx. (4)

The first term is exactly minus the sum of |q_x| at all four internal
endpoints: q_x(t,a)<0, q_x(t,b)>0, and q is even. These are genuine
interface contributions, despite the zero external flux. The bulk
integral in (4) has primitive 96x^5/5+8beta^2 x. Equations (1)--(4)
therefore evaluate the full energy and all relevant flux/production
terms, without division by F or by q. As a further sign check, on the
negative intervals v=x^2 lies in (1/2,3/2), and

    partial_t Q=6(v-1)^2-16+72t(v+1)-216t^2
               <=-29/2+9/5=-127/10<0.

Hence e'(t)>0 throughout (0,h].

There is no regularity assumption hidden at t=0. The positive-part
map is 1-Lipschitz, and partial_t q is bounded on the rectangle. Thus
|e(t)-e(s)|<=integral_I |q(t,x)-q(s,x)| dx<=2480|t-s|.
Indeed the displayed time derivative has absolute value at most
384+192+40+72/25+54/625=386854/625<620 on the rectangle.
So e is Lipschitz, in particular absolutely continuous, on [0,h], with
e(0)=0 by the explicit nonnegative terminal defect. The endpoint
calculation is also an elementary specialization of the Sobolev
truncation tools covered by the assessment: Alber, *Nonlinear elliptic
and parabolic partial differential equations (PDE 2)*, 10 June 2018,
Lemma 5.2/Theorem 5.3, pp. 90--92,
[primary PDF](https://www2.mathematik.tu-darmstadt.de/~alber/pde_2.pdf).
The external trace agrees with Brezis--Ponce, *Kato's inequality up to
the boundary*, Comm. Contemp. Math. 10 (2008), 1217--1241, Theorem 7.1,
pp. 1234--1236,
[published author-hosted PDF](https://sites.math.rutgers.edu/~brezis/PUBlications/198journal.pdf).
Their smoothness/Sobolev hypotheses hold for our polynomial slices.
Neither cited theorem evaluates this energy or supplies its comparison;
the explicit calculation is needed for that uncovered difference.

### Collision limit and failure of the comparison

Here is a justified derivative asymptotic, without differentiating an
unspecified error term. Set t=r^2 and x=1+ru. The polynomial

    R(r,u)=q(r^2,1+ru)/r^2

extends polynomially across r=0: its numerator has no constant or
linear term in r. An explicit expansion, also checking this divisibility,
is

    R(r,u)=32u^2-64+64r u^3
        +r^2(56u^4+96u^2+288)
        +r^3(24u^5+96u^3+288u)
        +r^4(4u^6+24u^4+144u^2-288).

For example, substitute s=x^2-1=2ru+r^2u^2 into the exact identity
Q(r^2,1+s)=2s^2+s^3-16r^2+6r^2s^2+72r^4+36r^4s-72r^6.
In particular,

    R(0,u)=32u^2-64.

Its two roots +-sqrt(2) are simple. The real analytic implicit
function theorem gives real analytic u_-(r),u_+(r), with initial values
-sqrt(2),sqrt(2), solving R(r,u)=0 near r=0. For positive small r,
the roots 1+r u_-(r) and 1+r u_+(r) are respectively a(r^2),b(r^2):
they are positive, on opposite sides of 1, and the preceding cubic
root count leaves exactly these possibilities. Changing variables in
(1) gives

    e(r^2)=r^3 A(r),
    A(r)=-2 integral_{u_-(r)}^{u_+(r)} R(r,u) du,
    A(0)=-2 integral_{-sqrt(2)}^{sqrt(2)}(32u^2-64) du
         =512 sqrt(2)/3.

The function A is real analytic near zero: R is polynomial and its
primitive evaluated at the analytic endpoints is analytic. In particular
A(0)>0, A(r)=A(0)+O(r), and A'(r)=O(1). Ordinary differentiation of
this exact identity for r>0 now gives

    e'(t)=(3/2)sqrt(t) A(sqrt(t))+(t/2)A'(sqrt(t)),
    t e'(t)/e(t)=3/2+sqrt(t) A'(sqrt(t))/(2A(sqrt(t))) -> 3/2.

These formulas prove all three stated asymptotics and the one-sided
derivative zero at t=0. They also display an unbounded e'/e although
every relevant jet remains bounded.

Finally suppose the proposed inequality held with such a C. Choose
delta>0 and finite M with C(-t)<=M almost everywhere on [0,delta].
Changing time orientation gives e'(t)<=M e(t) almost everywhere there.
The standard integral Gronwall inequality applies to the absolutely
continuous, nonnegative e with e(0)=0, and gives e(t)<=0. This
contradicts (1) for every 0<t<=min(delta,h). The unbounded ratio above
independently identifies the missing coefficient scale, asymptotically
3/(2t). A coefficient singular at the collision is outside the
comparison being tested.

This finite polynomial calculation uses the same heat convention as
L058 and structural properties relevant to L018, but uses neither as
a mathematical premise. L469 concerns a spatial pointwise weighted
barrier; it does not evaluate this heat energy. L126/L128's
moving-supremum obstruction is a different historical limitation.
Actual-Xi realization and negative-mass estimates remain unresolved.
This is a specialization of known heat-collision and comparison tools;
the recorded search did not establish coverage of this exact certificate
and does not establish originality. No independent critical audit of
the cited general source proofs is claimed. An independent finite
certificate audit on 30 October 2026 replayed all parameter bounds,
all roots and sign intervals, the zero external flux and four internal
interfaces, collision absolute continuity, the exact scaled derivative
and the terminal Gronwall contradiction. It found no load-bearing
failure. The explicit rational sign margins, Lipschitz bound and full
scaled polynomial above make the corresponding checks reproducible
without a numerical preview or differentiating an error term. This
verifies the existing obstruction, rather than establishing a stronger
comparison failure or an actual-Xi input.

## Mathlib

Full matching theorem and supporting polynomial, root, truncation,
implicit-function and Gronwall declarations not checked. Unknown
coverage is not evidence of absence.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
