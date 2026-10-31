# L491 — Explicit gamma-log linearization on closed unit disks

## Hypotheses

Let t be real with 1/25 <= t <= 11/50, and let X be real with
X >= 4*pi*exp(10000)+2. Let w be complex with |w| <= 1.
Throughout, Log is the principal holomorphic logarithm away from the
nonpositive real axis. On Omega = C minus (-infinity,1], define the
specific holomorphic logarithm

    ell_0(s) = Log(s)+Log(s-1) -(s/2)*log(pi)
               +log(sqrt(2*pi)/16)
               +(s/2-1/2)*Log(s/2)-s/2,
    alpha(s) = 1/(2s)+1/(s-1)+(1/2)*Log(s/(2*pi)),
    ell_t(s) = ell_0(s)+(t/4)*alpha(s)^2,
    q_t(s) = ell_t'(s) = alpha(s)+(t/2)*alpha(s)*alpha'(s).

These are the exact source definitions, not a principal logarithm
of the value exp(ell_t(s)). Put

    G_t(z) = ell_t((1+iz)/2)-ell_t((1-iz)/2),
    L = log(X/(4*pi)),
    g(X,t) = (X/(4*pi))*L-X/(4*pi)+11/8+(t/16)*L.

## Conclusion

On the entire closed domain in the hypotheses,

    |G_t(X+w)-i*(2*pi*g(X,t)-pi)-(i/2)*L*w|
        <= (L+20)/X
        < 5010/10^12 < 1/100.

This is a quantitative specialization of a known asymptotic model.
It supplies no zero count, exhaustion of zeros, real/simple tail cutoff,
or collision exclusion. In particular no estimate for H_t is assumed
or proved by this lemma. The first separate critical audit, recorded
below, verifies the stated certificate and its branch choices.

## Proof

### Source inputs and scope of specialization

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, Research in the Mathematical Sciences 6 (2019), article 31,
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2),
equations (7),(9),(10),(42),(100) give the definitions above and

    alpha'(s) = -1/(2s^2)-1/(s-1)^2+1/(2s).

Lemma 9.2 gives the qualitative center phase and local variation with
an unspecified O(log X/X) constant. We retain that structure and
derive explicit constants from the formulas. No saddle estimate or
theorem on zeros is used or reproved.

There is a source qualification: the alpha bound printed as (76)
cannot be used as written. At sigma=0, x=200, formula (9) gives

    |alpha(ix/2)-(log(x/(4*pi))/2+i*pi/4)|
      >= 1/200+100/10001 > 1/97 = 2/(200-6),

contradicting that displayed bound. The first inequality takes the
absolute value of the imaginary part of 1/(ix)+1/(-1+ix/2).
For the strict rational comparison, the numerator after multiplying
by the positive common denominator 200*10001*97 is
30001*97-200*10001=909897 > 0. This concerns the printed auxiliary
estimate, not a claimed refutation of any theorem on zeros.
We therefore verify the small estimates directly rather than import
(76). This verification of a suspect constant and the needed numerical
specialization justify the elementary calculation below.

For real x >= 200 and 0 <= sigma <= 1 put s=sigma+ix/2 and
a_x=log(x/(4*pi))/2+i*pi/4. The exact branch identity

    Log(s/(2*pi))=log(x/(4*pi))+i*pi/2+Log(1-2i*sigma/x)

and the logarithm series give

    |alpha(s)-a_x| <= 3/x+sigma/(x-2*sigma)
                   <= 4/(x-2).                    (1)

Indeed |1/(2s)| <= 1/x, |1/(s-1)| <= 2/x, and
|Log(1+u)| <= |u|/(1-|u|) for |u|<1. The branch identity follows
because its imaginary part is pi/2-arctan(2*sigma/x), the principal
argument of s. From the exact formula for alpha' we also obtain

    |alpha'(s)| <= 1/x+6/x^2 <= 1/(x-6).          (1a)

This reproduces the source's (75), or (43) with Im(s)>3, and explicitly
checks its constant. Neither upper-half-plane estimate is inserted
at a negative imaginary part.

### Branches and conjugation

We have X >= 201 and L > 10000. For |z-X| <= 1 write z=x+iy.
Then x >= X-1 >= 200, |y| <= 1, and

    s_+(z)=(1+iz)/2=(1-y)/2+ix/2,
    s_-(z)=(1-iz)/2=(1+y)/2-ix/2.

Both images avoid the cut in an open neighborhood of the closed disk,
so G_t is holomorphic there. Principal Log commutes with conjugation
off its cut. The explicit formulas, all of whose other constants and
t are real, therefore give

    ell_t(conj(s))=conj(ell_t(s)),
    alpha(conj(s))=conj(alpha(s)),
    alpha'(conj(s))=conj(alpha'(s))                 (2)

on Omega. In particular G_t(X)=2i*Im(ell_t((1+iX)/2)).
Bounds for s_-(z) below follow by (2) from the upper point
(1+y)/2+ix/2, whose real part lies in [0,1].

### The fixed-branch center phase

Set s=(1+iX)/2. Since the arguments of s and s-1 are respectively
arctan(X) and pi-arctan(X),

    Im(Log(s)+Log(s-1))=pi                         (3)

as an equality of the specified logarithms, not modulo 2*pi.
Also the branch identity

    Log(s/2)=log(X/4)+i*pi/2+Log(1-i/X)             (4)

holds: the imaginary part on the right is pi/2-arctan(1/X),
which is the principal argument of s/2. By the convergent logarithm
power series on the unit disk, write

    Log(1-i/X)=-i/X+R,
    |R| <= 1/[2*X^2*(1-1/X)].                    (5)

For completeness, the bound follows by summing
sum_(n>=2) X^(-n)/n <= (1/2)*sum_(n>=2) X^(-n).
Inserting (3)–(5) into the displayed definition of ell_0 gives

    Im(ell_0(s)) = P_0+epsilon_0,
    P_0=(X/4)*L-X/4+7*pi/8,
    epsilon_0=Im(((-1+iX)/4)*Log(1-i/X)).          (6)

Indeed the terms outside the last logarithm have imaginary part
pi-(X/4)*log(pi)+(X/4)*log(X/4)-pi/8-X/4.
The leading correction satisfies

    ((-1+iX)/4)*(-i/X)=1/4+i/(4X).

Consequently, using sqrt(1+X^2) <= X+1 and X >= 3,

    |epsilon_0|
      <= 1/(4X)+sqrt(1+X^2)/[8*X^2*(1-1/X)]
      <= [1/4+(X+1)/(8*(X-1))]/X <= 1/(2X).     (7)

Let a=L/2+i*pi/4. The first inequality in (1) at sigma=1/2 gives,
since X >= 2,

    |alpha(s)-a| <= 3/X+1/[2*(X-1)] <= 4/X.

Since L >= 0, pi < 4 and X >= 4, this implies

    |alpha(s)^2-a^2|
      <= (4/X)*(L+2+4/X) <= 4*(L+3)/X.           (8)

Here we used |a| <= L/2+1 and the elementary difference-of-squares
bound |(a+r)^2-a^2| <= |r|*(2|a|+|r|).
The imaginary part of a^2 is pi*L/4. Put

    P_t=P_0+t*pi*L/16.

By (7)–(8), (2), and 0 <= t/2 <= 1/8,

    |G_t(X)-2i*P_t|
      <= 1/X+(t/2)*4*(L+3)/X
      <= (L/2+5/2)/X.                           (9)

Direct substitution in the definition of g gives
2*P_t=2*pi*g(X,t)-pi, including its constant 7*pi/4.

### Uniform variation over the closed complex disk

For z=x+iy as above, put L_x=log(x/(4*pi)). Formulas (1),(1a), with
sigma=(1-y)/2, and then with sigma=(1+y)/2 followed by (2), yield

    |alpha(s_+)-(L_x/2+i*pi/4)| <= 4/(x-2),
    |alpha(s_-)-(L_x/2-i*pi/4)| <= 4/(x-2),
    |alpha'(s_+)|, |alpha'(s_-)| <= 1/(x-6).      (10)

Here L_x >= 0. Define the nonnegative bound
Q=L_x/2+pi/4+4/(x-2); then |alpha(s_+)|,|alpha(s_-)| <= Q.
The chain rule, with the minus sign in G_t included, gives

    G_t'(z)=(i/2)*(q_t(s_+)+q_t(s_-)).

The leading imaginary constants in (10) cancel, so

    |G_t'(z)-(i/2)*L|
      <= |L_x-L|/2+4/(x-2)+(t/2)*Q/(x-6).        (11)

Because |x-X| <= 1 and x >= X-1, the real logarithm's derivative
or its integral gives |L_x-L| <= 1/(X-1). Thus, for X >= 201,

    Q <= L/2+1/[2*(X-1)]+1+4/(X-3) <= L/2+2.

The last inequality follows, for example, from
1/[2*(X-1)] <= 1/400 and 4/(X-3) <= 4/198.
Replacing each denominator in (11) by X-7 and using t/2 <= 1/8,
then 1/(X-7) <= 2/X, gives throughout the disk

    |G_t'(z)-(i/2)*L|
      <= (L/16+19/4)/(X-7)
      <= (L/8+19/2)/X.                          (12)

The segment X+u*w, 0 <= u <= 1, stays in the closed disk. Integrating
the exact holomorphic derivative along it, using |w| <= 1, and then
adding (9) proves

    |G_t(X+w)-i*(2*pi*g(X,t)-pi)-(i/2)*L*w|
      <= [L/2+5/2+L/8+19/2]/X
      = (5*L/8+12)/X <= (L+20)/X.               (13)

### All-height numerical comparison and endpoints

Let X_0=4*pi*exp(10000). For X >= X_0, the function

    f(X)=(log(X/(4*pi))+20)/X

is strictly decreasing, since
f'(X)=(-log(X/(4*pi))-19)/X^2 < 0.
Our domain is contained in X >= X_0. Hence (13) is bounded by

    f(X_0)=10020/[4*pi*exp(10000)]
      < 10020*6/[12*10000^3]
      = 5010/10^12 < 1/100.                     (14)

This uses only pi > 3 and the exponential power series inequality
exp(10000) > 10000^3/6, so there is no floating-point evaluation or
finite-height sampling. All estimates hold with the closed disk and
time endpoints. The two units of height padding are retained exactly;
they are not a height-transfer or counting claim. The explicit formulas
are imported source definitions and identities. The elementary estimates
replace the suspect (76) and supply the numerical specialization, not
a new asymptotic structure or a discovery about zeta zeros.

### Separate critical audit, 2026-10-30

The unchanged statement passes its first full-domain audit. This is
independent replay of the numerical specialization, not a new theorem
about zeros or an audit of the source saddle estimates. The source
formulas were checked directly in the linked v2: (7)–(10), (43),
(75)–(76), and Lemma 9.2 with (100). Its unspecified asymptotic errors
are not numerical inputs to this proof.

First, differentiating ell_0 exactly gives

    ell_0'(s)=1/s+1/(s-1)-(1/2)log(pi)+(1/2)Log(s/2)-1/(2s)
             =alpha(s).

The equality uses division of the logarithm's argument by the
positive real pi, so adds no branch constant. Differentiating the
time correction gives q_t as stated. At s=100i, the difference from
a_200 is exactly

    -1/10001-i*(1/200+100/10001).

Thus the modulus is at least 30001/2000200, exceeding source (76)'s
1/97 by 909897/194019400. The reported discrepancy is confirmed;
it was already recorded before this audit. No claim concerning other
source conclusions follows from it.

For all x>=200 and sigma in [0,1], the logarithm decomposition in (1)
has argument pi/2-arctan(2*sigma/x) in (0,pi/2]. In particular it
also holds at sigma=0. All denominators are positive. Explicitly,

    sigma/(x-2*sigma)<=1/(x-2),
    4/(x-2)-[3/x+1/(x-2)]=6/[x*(x-2)]>=0,
    1/(x-6)-[1/x+6/x^2]=36/[x^2*(x-6)]>0.

These verify both replacement bounds without the suspect (76).
For the closed disk the two image imaginary parts are respectively
x/2 and -x/2 with x>=X-1>=200; hence neither image meets the cut,
even in a neighborhood of the disk. The conjugated lower image has
real part (1+y)/2 in [0,1]. All three conjugation identities (2)
therefore apply with the same constants and real t.

At the center the two arguments in (3) add to exactly pi. Formula
(4) has argument arctan(X), and its remainder series is absolutely
convergent. The product of its leading correction with (-1+iX)/4
is 1/4+i/(4X); treating 1/4 as an imaginary error would invalidate
the phase calculation. The remainder bound gives (7), since
(X+1)/(X-1)<=2 for X>=3. At sigma=1/2 the error bound is <=4/X
for X>=2. Squaring a=L/2+i*pi/4 gives Im(a^2)=pi*L/4, so the time
term in Im(ell_t) is t*pi*L/16 with error at most t*(L+3)/X.
Doubling to form G_t gives (9) using t/2<=11/100<1/8.
The constant identity is exact: 2*pi*(11/8)-pi=7*pi/4.

Both chain-rule signs in G_t' were checked: differentiating its
second summand contributes +i*q_t(s_-)/2. The leading imaginary
alpha constants cancel, yielding (11). The real segment from X to
x stays above X-1, proving the logarithm difference bound for either
sign of x-X. Since 1/400+4/198=899/39600<1, Q<=L/2+2.
All terms in (11) are nonnegative; replacing their denominators by
X-7 gives numerator

    1/2+4+(1/8)*(L/2+2)=L/16+19/4.

Also X>=201>14 implies 1/(X-7)<=2/X. Integration along X+u*w
uses a holomorphic derivative on a neighborhood of the whole segment,
not a derivative of a principal logarithm of exp(ell_t). Combining
the resulting bound with (9) gives (5*L/8+12)/X, which is <=(L+20)/X
because L>10000. This verifies all of (10)–(13), including |w|=1.

Finally, f'(X)=(-L-19)/X^2<0 on X>=X_0. The strict inequalities
pi>3 and exp(10000)>10000^3/6 yield
f(X_0)<5010/10^12=501/100000000000<1/100. This covers all unbounded
X and the time endpoints; no finite sampling or limiting interchange
is used. The height padding is stronger than needed for this
component and has not been dropped.

The exact-arithmetic replay
`python3 scripts/heat/l491-arithmetic-certificate.py` passed all nine
checks. Its complete relevant evidence is in
`scripts/heat/l491-arithmetic-certificate.json`, fields `checks` and
`source_discrepancy`; the certificate proves rational comparisons
only. The preceding analytic replay supplies the continuum proof.
No statement repair or dependency change was required. Mathlib
coverage remains as below. Reflection of an H_t residual, strict
counts, exhaustion, collisions and t tending to zero remain open.

## Mathlib

Full matching coverage for this particular explicit gamma-log
inequality is not checked. No absence claim is made. The proof uses
elementary logarithm identities and power series, conjugation,
holomorphic differentiation, integration on a line segment and real
monotonicity; specific supporting Mathlib theorem names were not
looked up. The source definitions and identities are the mathematical
imports; the printed (76) is explicitly not assumed.
