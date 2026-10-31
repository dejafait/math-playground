# Lemma 508: norm obstruction for every finite positive vertical-side measure

## Hypotheses

Fix R>0 and retain L504's definitions, with real T sufficiently large:

    L=log T, a=log L/pi, b=a/4, B=L/(4pi),
    lambda=pi/(2a), beta=lambda*b=pi/8,
    K(x)=1-(sin(pi x)/(pi x))^2, K(0)=0.

The real vector space V_R consists of even entire functions real on R
with representation

    f(z)=integral_R phi(v)exp(2pi i v z)dv,
    phi in C_c^infinity(R), supp phi subset [-R,R].

Put u(x,y)=Re f(x+iy), N(f)=integral_R |f(x)|dx,
M(f)=integral_R |f(x)|K(x)dx, and

    Q_a(f)=-integral_0^b exp(-lambda y)[u(a,y)+u(-a,y)]dy.

Let nu be any finite nonnegative Borel measure on the closed interval
[b,B], independent of f. It may depend arbitrarily on R,T and may have
endpoint atoms, singular parts and arbitrarily large finite mass. Set

    J_{a,nu}(f)=Q_a(f)
                   +integral_[b,B] [u(a,y)+u(-a,y)]dnu(y),
    ||J_{a,nu}||_M=sup_{0!=f in V_R}|J_{a,nu}(f)|/M(f).

For the applicability statement only, H_a is the subset of V_R with
u(x,y)>=1 whenever |x|<=a and b<|y|<B. Neither H_a nonemptiness nor
any sign condition on V_R is assumed. There is no bound on Fourier
derivatives, no minimizing measure, and no duality or attainment premise.

The sole local input is L504's definitions and elementary Fourier/norm
facts. L505 and L507 are contrasts, not theorem inputs. The source
comparison in `drafts/literature/2026-10-30-vertical-side-finite-measure-norm-test.md`
was EXPLORE before this calculation: it found no matching conclusion.
No theorem from its point-evaluation or optimization sources is imported.
The exact packet construction below uses only smooth Fourier inversion,
two integrations by parts, elementary differentiation and finite-measure
integration already within that assessed scope. It is not a claimed new
general theorem about Paley--Wiener spaces or positive kernels.

## Conclusion

Every displayed functional is well defined. For each fixed R,T,nu,
||J_{a,nu}||_M is finite. If f belongs to H_a, then

    Q_a(f)<=J_{a,nu}(f)-2nu([b,B])<=J_{a,nu}(f).        (1)

There are constants c_R>0 and T_R such that, for every real T>=T_R
and every allowed nu,

    ||J_{a,nu}||_M>=c_R L^(R/8)/a.                    (2)

One smooth Fourier witness f_a, independent of nu, proves (2). Thus

    (1/a) inf_{finite nu>=0 on [b,B]} ||J_{a,nu}||_M
        >=c_R L^(R/8)/a^2 -> infinity.               (3)

This excludes an O_R(a) full-space certificate throughout this family.
It does not refute Q_a<=C_R a M on H_a: the witness lies outside H_a.
It excludes neither general rectangle-supported measures nor bounds
using additional positivity information on H_a. No detector realization,
actual-Xi sign, arithmetic error bound or RH conclusion follows. The
independent critical audit of 30 October 2026 below passes without a
repair or stronger bound. Neither that replay nor the prior literature
comparison certifies originality.

## Proof

### Well-definedness, normalization and conditional applicability

The real trace of f is Schwartz. Fourier inversion and evenness/reality
make phi real and even, and give |phi(v)|<=N(f). Therefore

    u(x,y)=integral_{-R}^R phi(v)cos(2pi vx)cosh(2pi vy)dv,
    |u(x,y)|<=2R exp(2pi R|y|)N(f).                  (4)

In particular u(-a,y)=u(a,y). Continuity on the compact side interval
and finiteness of nu imply absolute convergence. If

    I_b(s)=integral_0^b exp(-lambda y)cosh(sy)dy,
    A_nu(s)=integral_[b,B] cosh(sy)dnu(y),

then the actual functional, with the 2pi Fourier convention, is

    J_{a,nu}(f)=2 integral_{-R}^R phi(v)cos(2pi va)
                       [A_nu(2pi v)-I_b(2pi v)]dv.  (5)

All exchanges in (5) have an absolute bound from compact frequency
support, bounded y<=B, and finite nu mass. No formal cosine is being
treated as a member of V_R.

For completeness, the elementary weight conversion used in L504
extends to every f in this space by the same bandwidth argument.
Take eta=1/(8R+2) and k=inf_{|x|>=eta}K(x)>0. The positivity follows
from |sin(pi x)|<pi|x| for x!=0, continuity, and K(x)>=1-1/pi^2
for |x|>=1. Equation (4) at y=0 gives

    integral_{|x|<eta}|f(x)|dx<=4R eta N(f)<N(f)/2,
    M(f)>=k N(f)/2,       M(f)<=N(f).                (6)

This argument is included because the earlier supplementary conclusion
was stated for a restricted dilation family; (4) applies to all of V_R.
In particular M(f)>0 for every nonzero f. Direct integration of (4)
gives the finite, nonuniform bound

    |J_{a,nu}(f)|
      <=4R [b exp(2pi Rb)+nu([b,B])exp(2pi RB)]N(f).

Combining with (6) proves fixed-parameter boundedness, without bounding
nu mass uniformly or claiming a useful asymptotic upper estimate.

For T>exp(1), 0<b<B since log L<L. If f is in H_a, continuity from
the interior b<y<B implies u(+-a,b)>=1 and u(+-a,B)>=1 as well.
The side integrand is consequently >=2 on all of [b,B], including
both endpoints, which proves (1). Thus an O_R(a) bound on this norm
would indeed have supplied the proposed one-sided Q bound.

### Two smooth packets and their exact side traces

Fix once and for all a nonnegative real smooth function chi, supported
compactly in (-delta,delta), delta=1/4, with integral 1. It may be
taken even. Define g(t)=chi(t)/cos(t) on that interval and extend it
by zero; g is globally smooth and compactly supported. Choose

    s_1=(2pi/a)floor(Ra/4),
    s_2=(2pi/a)floor(Ra/2),
    w_j(t)=g(t)sech(s_j b+t/4),
    F_j(z)=integral_R w_j(t)cos((s_j+t/a)z)dt,
    f_a=F_2-F_1.                                     (7)

For a>=32/R the angular frequencies on these supports obey

    pi R/4 <=s_1+t/a<=5pi R/8=:l,
    h:=7pi R/8<=s_2+t/a<=9pi R/8<2pi R.              (8)

Indeed the lower endpoints are at least pi R/2-(2pi+delta)/a
and pi R-(2pi+delta)/a; the upper endpoints are at most pi R/2+delta/a
and pi R+delta/a. Substitution of a>=32/R gives (8). These inequalities
hold at every real a satisfying the onset, including the floor jumps.

Each F_j is even, entire and real on the real axis. Its exact Fourier
data in the 2pi convention are

    phi_j(v)=pi a [w_j(a(2pi v-s_j))+w_j(a(-2pi v-s_j))]. (9)

Changing variables in the two exponential terms of the cosine verifies
(9). The data are real, even, globally smooth and supported in [-R,R]
by (8). Thus F_1,F_2,f_a are genuine members of V_R.

Since s_j a is an integral multiple of 2pi and b/a=1/4, cancellation
of cos(t) in (7) gives, for every y>=0,

    Re F_j(a+iy)=Re F_j(-a+iy)
      =integral chi(t) r_{s_j+t/a}(y)dt,
    r_s(y)=cosh(sy)/cosh(sb).                         (10)

This is an exact identity for all side heights, rather than a compact
approximation to a pure cosine. In particular each trace equals 1
at y=b.

For s>0,

    partial_s log r_s(y)=y tanh(sy)-b tanh(sb).        (11)

The function x -> x tanh(sx) is strictly increasing for x>=0,
as follows from its derivative tanh(sx)+sx sech(sx)^2, positive for
x>0. Consequently r_s(y) is increasing in s for y>b, constant in s
for y=b, and decreasing in s for 0<=y<b. The ordered supports (8)
and the nonnegative probability weights chi in (10) imply

    u_a(+-a,y)>=0 for every y>=b,
    u_a(+-a,y)<=0 for 0<=y<=b,
    u_a(+-a,b)=0,                                    (12)

where u_a=Re f_a. For example, every high-frequency value of r_s(y)
is at least every low-frequency value when y>=b, so the same order
holds between their averages. The order reverses below b. No upper
height restriction or error depending on nu is involved in (12).

### A fixed positive gap contribution

Let

    d=exp(-5/4)(1-exp(-1/4))>0,
    q_R=exp(-beta)d/(pi R)>0.

Impose also b>=2/(pi R) and b>=h^(-1)log(2/d). For
tau in [1/(pi R),2/(pi R)], put y=b-tau>=0. By (8), (10) and
monotonicity below b,

    Re F_1(a+iy)-Re F_2(a+iy)>=r_l(y)-r_h(y).         (13)

For any s>0 and 0<=tau<=b, elementary exponential algebra gives

    r_s(b-tau)
      =exp(-s tau)
        + exp(-2sb)[exp(s tau)-exp(-s tau)]/[1+exp(-2sb)].

The second term is nonnegative and at most exp(-s(2b-tau)). Hence

    r_l(b-tau)-r_h(b-tau)
      >=exp(-l tau)-exp(-h tau)-exp(-h(2b-tau))
      >=d-exp(-hb)>=d/2.                             (14)

The middle inequality uses l tau<=5/4, (h-l)tau>=1/4 and tau<=b.
The gap integrand is nonnegative everywhere by (12), so restricting
the Q integral to this interval loses no negative contribution.
Also exp(-lambda y)>=exp(-lambda b)=exp(-beta). Including both
sides in Q, (13)--(14) yield

    Q_a(f_a)
      =2 integral_0^b exp(-lambda y)
                    [Re F_1(a+iy)-Re F_2(a+iy)]dy
      >=2 exp(-beta)(d/2)/(pi R)=q_R.                (15)

Thus f_a is nonzero. Combining (12) and (15), for every finite
nonnegative nu on [b,B], including arbitrary endpoint atoms,

    J_{a,nu}(f_a)>=Q_a(f_a)>=q_R.                    (16)

The measure contributes a nonnegative quantity exactly. There is no
mass-dependent smoothing error and no reduction to atomic measures.

### The real-axis norm and a common onset

Write ||.||_1 for integration in the real variable t, and set

    C_chi=4exp(1/16)[(17/16)||g||_1
                            +(1/2)||g'||_1+||g''||_1]>0.

For real x, sech(x)<=2exp(-x), |sech'(x)|<=sech(x), and
|sech''(x)|<=sech(x). The derivative formulas are
sech'=-sech*tanh and sech''=sech*(2tanh^2-1). Applying these to
w_j(t)=g(t)sech(s_j b+t/4), with |t|<=1/4, gives

    ||w_j||_1+||w_j''||_1
       <=2exp(1/16)exp(-s_j b)
                    [(17/16)||g||_1+(1/2)||g'||_1+||g''||_1]. (17)

Let H_j(v)=integral w_j(t)exp(itv)dt. For |v|<=1,
|H_j(v)|<=||w_j||_1. Two integrations by parts, with zero boundary
terms from compact smooth support, give |H_j(v)|<=||w_j''||_1/v^2
for |v|>1. Integration over both regions yields

    integral_R |H_j(v)|dv<=2(||w_j||_1+||w_j''||_1).

For real x, F_j(x)=Re[exp(is_j x)H_j(x/a)], so (17) implies

    N(F_j)<=C_chi a exp(-s_j b),
    0<M(f_a)<=N(f_a)<=2C_chi a exp(-s_1 b).          (18)

Here s_2>s_1 follows from (8). The strict lower bound for M uses
nonzeroness from (15) and (6). No uniform derivative bound on the
Fourier data in (9) has been assumed.

One simultaneous sufficient onset is

    a_R=max(1,32/R,8/(pi R),(32/(7pi R))log(2/d)),
    T_R=exp(exp(pi a_R)).                            (19)

For every real T>=T_R, (8) and both conditions preceding (13) hold.
Also B>b, and all norm and sign arguments apply. This is a symbolic
sufficient onset, not a numerically evaluated height.

Finally s_1>=pi R/2-2pi/a and b=a/4, whence

    exp(s_1 b)>=exp(-pi/2)exp(pi R a/8)
                   =exp(-pi/2)L^(R/8).

Dividing (16) by (18) proves (2) with

    c_R=q_R exp(-pi/2)/(2C_chi)>0.

The same f_a works for every nu, so taking the infimum gives (3),
without an attainment assumption. Since R>0 is fixed, the exponential
exp(pi R a/8) divided by a^2 tends to infinity.

The endpoint identity u_a(+-a,b)=0 in (12) proves f_a is outside H_a:
membership would force these values to be >=1 by continuity from the
open height interval. This is why the full-space obstruction supplies
no counterexample to the constrained inequality. It also supplies no
new signs for Xi or realization of any detector.

### Independent critical audit, 30 October 2026

The separately approved audit replays the stated result, including its
unrestricted measure quantifier, rather than the comparison manuscripts.
No external optimization or point-evaluation theorem is a premise.
L504 remains the sole direct local input. The following checks found
no defect and require no change to (1)--(19).

For fixed parameters the Schwartz inversion bound is
|phi(v)|<=N(f), without a 2pi factor. Thus the mass in (-eta,eta)
is at most 4R eta N(f), where 4R eta=4R/(8R+2)<1/2.
The complement has K>=k>0, proving M>=kN/2 for the whole V_R.
This verifies both the norm's nondegeneracy and fixed-parameter
boundedness of J. The finite upper estimate is allowed to depend
on nu([b,B]) and exp(2pi RB); neither quantity enters the lower
bound. Tonelli/Fubini in (5) only uses a finite compact-domain
absolute integral, not a uniform mass assumption.

Recomputing the change of variable in each half of the cosine in
(7) gives (1/2)dt=(pi a)dv, exactly the coefficient in (9).
The two bumps are smooth through their support boundaries. Their
positive angular supports satisfy (8): under a>=32/R,
(2pi+1/4)/a<=((2pi+1/4)/32)R<pi R/8 and
(1/4)/a<=R/128<pi R/8. These inequalities even give a stronger
lower bound for the low packet than the displayed pi R/4.
Both reflected supports are therefore strictly within [-R,R] in
ordinary frequency, and the low and high angular supports are
disjoint. Floor discontinuities do not affect these uniform bounds.

At either side, taking the real part of the cosine gives
cos(s_j a+t)cosh((s_j+t/a)y). Since s_j a is an integer multiple
of 2pi and (s_j+t/a)b=s_j b+t/4, dividing by cos(t) and the
hyperbolic cosine leaves exactly (10). The weights chi have mass
one in both packets; no packet-dependent probability normalization
is missing. For each fixed s>0, the derivative of x tanh(sx)
is strictly positive for x>0. Equation (11) consequently orders
every high-frequency integrand against every low-frequency
integrand, including y=0 and equality at y=b. Averaging preserves
this order. It holds for all y>=b, not just a bounded rescaled
interval. Hence the same witness works through B for every nu,
including arbitrarily large atoms at b or B. In particular there
is no approximation remainder to amplify by the measure mass.

The lower-bound interval in (13) has length 1/(pi R) and lies in
[0,b]. Its two frequency constants satisfy l tau<=5/4 and
(h-l)tau>=1/4. Thus the main exponential difference is at least
d; only the high packet's nonnegative correction is subtracted.
That correction is at most exp(-h(2b-tau))<=exp(-hb)<=d/2.
The two sides and the weight exp(-lambda y)>=exp(-beta) give
2*(1/(pi R))*(d/2)*exp(-beta)=q_R, exactly (15).
Outside this interval the gap integrand remains nonnegative.

For the real-axis norm, differentiating w_j twice gives the three
terms g'' sech, (1/2)g' sech' and (1/16)g sech'', evaluated at
s_j b+t/4. Together with ||w_j||_1 this gives the coefficient
17/16 in (17). The local and tail integrations of H_j each
contribute a factor two: its integral is at most
2||w_j||_1+2||w_j''||_1. Rescaling x/a contributes a, so the
constant is exactly C_chi in (18). The triangle inequality and
s_2>s_1 give 2C_chi a exp(-s_1 b); using M<=N is the correct
direction for this lower operator-norm bound.

The four entries of a_R in (19) imply respectively a>=1, the
support separation, b>=2/(pi R), and b>=h^(-1)log(2/d).
Moreover T>=exp(exp(pi a_R)) is precisely sufficient for a>=a_R,
and gives B>b. All these conditions hold simultaneously for every
real T above this one onset. Finally
s_1 b>=pi R a/8-pi/2, verifying both the exponent R/8 and the
constant exp(-pi/2). Division by a again yields the divergent
ratio in (3) for every fixed R>0. No optimizing measure is needed.

For the conditional application, H_a positivity extends continuously
to both side endpoints, so (1) includes atoms at each endpoint.
In contrast the witness has u_a(+-a,b)=0 and cannot lie in H_a.
The audit therefore validates stopping only this full-space positive
vertical-measure family. The constrained Q bound, other supports,
actual-Xi transfer and all-degree positivity remain unresolved.

## Mathlib

Matching coverage of the full positive-measure norm obstruction has
not been checked. Smooth Fourier inversion, finite-measure integration,
elementary hyperbolic derivatives and integration by parts are the
supporting mathematics; no formalization or exact Mathlib theorem match
is asserted. The preapproved literature comparison did not identify
this full conclusion, which is not evidence of certified novelty.
