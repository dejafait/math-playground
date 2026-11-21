# Corollary 488b: audited quantitative local-count reduction

## Hypotheses

Use the actual family H_t and normalization of L019/L020/L058 and
C488a: H_0(z)=xi((1+iz)/2)/8 and F(lambda,z)=8H_(4lambda)(2z).
Throughout 0<=t<=1/5. Count every complex zero with its multiplicity,
and define the CLOSED-window count

    N_t(x,r)=#{z:H_t(z)=0, |Re z-x|<=r},
    r>=200, |x|>=2r.

Use C488a's strip |Im z|<=1, even paired Hadamard product, and bound

    #{z:|Re z|<=R}<=(R+20)log(4R+40), R>=0.                 (1)

For the conditional statements below, let A>=200 and 0<delta<1.
Write B_t(z)=M_t((1-iz)/2), with the source functions defined in the
proof, and assume the explicit comparison

    |H_t(v+iy)/B_t(v+iy)-1|<=delta
    (v>=A, 3<=y<=4, 0<t<=1/5).                            (2)

Condition (2) is an additional hypothesis unless invoked with the
existential onset supplied by the cited theorem. Its numerical instance
A=29399, delta=99/100 is supplied separately by C488c; this reduction
does not itself establish that instance.

## Conclusion

1. Unconditionally, the requested estimate holds in the sector

       2r<=|x|<=148r:
       N_t(x,r)<=(497/5)r log(2+|x|)<100r log(2+|x|).       (3)

2. Under (2), if |x|-r>=A+1/2, then, with D=2delta/(1-delta),

       N_t(x,r)<=(4r/3)[D+(1/2)log(2+|x|+r)].             (4)

   These estimates include t=0 and all closed spatial endpoints.
   For delta=7/10 the right side is <3r log(2+|x|).
   For delta=99/100 it is <54r log(2+|x|).

3. The known source theorem supplies some absolute A>=200 for
   delta=7/10. Thus (4), with the explicit coefficient3 just stated,
   holds beyond an EXISTENTIAL absolute onset. It does not establish
   the requested numerical domain in the remaining sector.

4. It suffices for the full constant100 target to establish (2) with
   A=29399 and delta=99/100. C488c supplies that comparison.

The conceptual audit2115 verifies this quantitative specialization of
a known off-axis counting argument. Together with C488c it proves the
whole numerical target, not a new order-of-magnitude count theorem.
No all-height reality, transport improvement, overlap with L488 at t=0,
or mixed positivity follows here.

## Proof

### Source input and its numerical qualification

Import D. H. J. Polymath, *Effective approximation of heat flow evolution
of the Riemann xi function, and a new upper bound for the de
Bruijn--Newman constant*, Research in the Mathematical Sciences 6
(2019), article31, [arXiv1904.12438v2, 4August2019,
Proposition9.1(ii), pp.56-58; (6)-(11), (42), (100), (105)](https://arxiv.org/html/1904.12438v2).
Proposition9.1(ii) gives (2) with delta=0.7, an unspecified absolute
onset, and 0<t<=1/2. It gives no numerical onset29399. Its proof
extends the effective estimates to y<=10 with adjusted, unprinted
constants; the constants stated for y<=1 cannot simply be reused.

In source notation, on C minus (-infinity,1],

    M_0(s)=(s(s-1)/16) pi^(-s/2) sqrt(2pi)
           exp((s/2-1/2)Log(s/2)-s/2),
    alpha(s)=1/(2s)+1/(s-1)+(1/2)Log(s/(2pi)),
    M_t(s)=exp(t alpha(s)^2/4)M_0(s).                       (5)

All logarithms here have the principal branch. The proof below
quantifies the counting and endpoint steps; it does not reprove the
source's asymptotic comparison. This specialization is needed because
the source's unspecified constants do not settle constant100 on the
saved numerical domain.

### Closed time endpoint and the Cauchy disk

Evenness gives N_t(-x,r)=N_t(x,r), so take x>=2r. Set
Q_t(z)=H_t(z)/B_t(z). In Im z>1 the argument (1-iz)/2 has real part
greater than1, so (5) is holomorphic and nonzero there. By L058 and
the stated normalization, Q_t tends locally uniformly to Q_0 as
t decreases to zero. Hence (2), by taking this limit at every point,
also holds at t=0. This uses no continuity assertion about a sharp
zero count.

For u>=A+1/2, the closed disk with center c=u+(7/2)i and radius1/2
lies in the comparison band. Q_t-1 is holomorphic on a neighborhood
of this disk. Cauchy's derivative formula and (2) give

    |Q_t'(c)|<=2delta, |Q_t(c)|>=1-delta,
    |Q_t'(c)/Q_t(c)|<=D.                                  (6)

This holds on the closed time interval. The disk only uses 3<=y<=4;
no bound in an enlarged vertical band has been inserted.

### Explicit comparison-factor derivative

At c, put s=9/4-iu/2 and L_u=log(2+u), where u>=200. Direct
differentiation of (5) gives

    alpha'(s)=-1/(2s^2)-1/(s-1)^2+1/(2s),
    B_t'(c)/B_t(c)=(-i/2)alpha(s)(1+(t/2)alpha'(s)).        (7)

We have |s|,|s-1|>=u/2, 1<|s|/(2pi)<=u+2, and
|arg s|<pi/2. Consequently

    |alpha(s)|<=3/u+(1/2)L_u+pi/4<(1/2)L_u+1,
    |alpha'(s)|<=6/u^2+1/u<=1/100.

Here pi<22/7 and u>=200 justify the strict first inequality.
Since e<3 gives e^4<81<202, L_u>4 and |alpha(s)|<(3/4)L_u.
Since t/2<=1/10, (7) now gives

    |B_t'(c)/B_t(c)|<=(3003/8000)L_u<(1/2)L_u.            (8)

These are explicit bounds; no Stirling error or asymptotic onset is
used in (7)-(8).

### Positive kernel and arbitrary closed windows

Write every zero copy as z_j=x_j+iy_j. By the strip and the paired
Hadamard product in C488a, the imaginary part of the logarithmic
derivative is

    U_t(u):=-Im(H_t'(u+(7/2)i)/H_t(u+(7/2)i))
      =sum_j a_j/((u-x_j)^2+a_j^2),
    a_j=7/2-y_j in [5/2,9/2].                            (9)

All summands are positive. The imaginary-part series converges
locally uniformly in u: on any fixed compact u interval its tail is
bounded by a constant times sum_j x_j^(-2), finite by (1). Pairing
therefore gives the asserted sum without an unpaired complex-series
interchange. Equations (6)-(8) imply

    0<=U_t(u)<=D+(1/2)log(2+u), u>=A+1/2.                (10)

For any zero copy with x_j in [x-r,x+r], integration of its term in
(9) over u in this same closed interval gives, with
p=x_j-(x-r) in [0,2r],

    arctan(p/a_j)+arctan((2r-p)/a_j)
      >=arctan(2r/a_j)>=arctan(4r/9)>3/2.                (11)

The first inequality follows because the left side is a concave
function of p, so its minimum on [0,2r] is at an endpoint. For the
last inequality use arctan v=pi/2-arctan(1/v)>=pi/2-1/v,
r>=200, and pi>31/10:

    pi/2-9/(4r)>=31/20-9/800=1231/800>3/2.

Both spatial endpoints and all multiplicities are included. Tonelli's
theorem applied to the nonnegative series in (9), followed by (10),
therefore yields (4). Zeros outside the interval only add positive
terms; no subtraction of global upper counts occurs.

For the stated simpler constants set L=log(2+x)>5, using
e^5<3^5=243<402. Since r<=x/2,

    log(2+x+r)<=L+log(3/2)<L+1<(5/4)L.

For delta=7/10, D=14/3, and the coefficient of rL in (4) is at most

    (4/3)(14/15+5/8)=187/90<3.

For delta=99/100, D=198, and the corresponding coefficient is at most

    (4/3)(198/5+5/8)=1609/30<54.                          (12)

This proves the local conditional estimates and, with the cited
existence of A, the restricted unconditional tail statement.

### Finite-sector payment and the precise missing comparison

Put S=x+r. Since x-r>=r>0, every zero counted lies in 0<Re z<=S.
Evenness pairs those copies with distinct copies at negative real
parts, with the same multiplicities. Thus (1) implies

    N_t(x,r)<=G(x,r):=((x+r+20)/2)log(4(x+r)+40).          (13)

For x>=400 and r<=x/2,

    4(x+r)+40<=6x+40<=(61/10)x,
    (61/10)^3=226981/1000<400<=x.

Taking logarithms gives log(4(x+r)+40)<=(4/3)log x<=(4/3)L.
If also x<=148r, then 20<=r/10 and x+r+20<=(1491/10)r.
Equation (13) proves (3), since (2/3)(1491/10)=497/5.

If instead x>148r, then x-r>147r>=29400. In particular the disks
used in (6), for u in [x-r,x+r], have real part greater than
29399.5. Condition (2) with A=29399 and delta=99/100 would cover
all of them, and (12) would give the stronger coefficient54 in this
sector. Together with (3) this proves the sufficiency assertion.

The existing global estimate does NOT bridge an arbitrary unknown
onset. At the admissible point x=40000, r=200, it gives

    G(40000,200)=20110 log(160840)
      >20000 log(40002)=100r log(2+x).                    (14)

Both factors on the left exceed their counterparts on the right.
This is an exact failed upper-estimate comparison, not a lower bound
on N_t and not a counterexample to the target. At step2113 the remaining
obligation was a uniform off-axis comparison on an unbounded horizontal
range. C488c subsequently supplies it analytically. Equation (14)
remains a valid failure of the global-only bridge; finite evaluations
or an appeal to compactness still would not supply the comparison.

### Conceptual audit — 21 November2026, step2115

The reduction passes, conditional on exactly (2). C488c is used only
in the subsequent assembly, so it is not an input to this corollary's
conditional proof. The existing DAG row needs no new mathematical input.

The source instance of (2) is Proposition9.1(ii), with its absolute
but unspecified onset. In (7), differentiation is with respect to z,
so the factor -i/2 is retained. The estimates give 3003/8000<1/2
for the coefficient of log(2+u). The Cauchy circle stays in the closed
comparison band, including its real-part boundary when u=A+1/2;
holomorphy holds on a neighborhood even there. Limiting the analytic
ratio to t=0 preserves the same nonvanishing lower bound 1-delta.

C488a's count, strip and paired product were checked in their stated
time domain. On a compact u interval, sufficiently large |x_j| give
each imaginary-part summand at most18/x_j^2. The dyadic consequence
of (1) makes this summable. Thus no unpaired complex series or unknown
linear exponential term is inserted in (9). The full count includes
both members of opposite pairs and every repeated copy.

For (11), the second derivative of arctan(p/a) is
-2ap/(a^2+p^2)^2<=0 for p>=0; applying this also to 2r-p gives
concavity on the full interval. A zero on either endpoint therefore
still contributes at least arctan(2r/a)>3/2 to the integral. Tonelli
is legitimate because every term is nonnegative. The time endpoint
requires no zero-count continuity and no simplicity hypothesis.

The finite sector uses disjoint reflected copies since x-r>=r>0.
Its coefficient is497/5<100, including x=148r. In the other sector
x-r>147r>=29400>A+1/2 for A=29399, so all required disks are paid.
The tail coefficient1609/30 is below54<100. Consequently the two
sectors cover every permitted x,r with no open boundary left over.
Evenness covers negative x. No claim about reality of those zeros is
used or obtained.

## Mathlib

Full matching coverage is not checked; no absence claim is made.
The proof uses the standard named Cauchy integral formula, Hadamard
factorization (in the already qualified C488a form), and Tonelli's
theorem. No Mathlib declaration is used as verification of the
numerical onset or of this audited informal specialization.
