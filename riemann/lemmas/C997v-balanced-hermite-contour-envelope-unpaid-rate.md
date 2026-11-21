# Corollary 997v: the balanced Hermite contour envelope leaves the upper-window rate unpaid

## Hypotheses

Let n>=1024 be an integer. Retain C997c(1),(4)–(6) and C997s's
complete kernel, with

    I=[7/4,9/4], z_star=1+i/8,
    gamma_j=15/8+j/(4n), 0<=j<=n,
    g_n(t)=((L_(n+1)^(2)(t)-1)/(n+1)) exp(-t/2) cosh(3t/8),
    k_n(c,z)=-2 exp(-cn/4) [integral_(cn)^(c(n+2)) g_n(t)exp(izt)dt
                             -integral_n^(n+2) g_n(t)exp(izt)dt].

No coefficient cap is imposed. Put

    h=(n+1)/(8n), phi=3h, s=cos h, d=sin h,
    a=exp(2ih), b=exp(4ih),
    m=floor((n+1)/2), ell=n+1-m,
    alpha=(-7/2+i/2)n, R=1/5,
    omega(y)=(y-a)^m (y-b)^ell.                         (1)

On the simply connected half-plane D={y: Re(exp(-i phi)y)>0},
use the branch

    Log_n(y)=Log(exp(-i phi)y)+i phi,
    f_n(y)=exp(alpha Log_n(y)),                          (2)

where Log on the right half-plane has argument in (-pi/2,pi/2).
Let p_n be its degree-at-most-n Hermite interpolant at a,b, of
multiplicities m,ell. Define A_(j,n)=[y^j]p_n and

    e_n(t)=exp(i z_star t)-exp(15it/8)p_n(exp(it/(4n))),
    D_n(c)=k_n(c,z_star)-sum_(j=0)^n A_(j,n)k_n(c,gamma_j).

All definitions concern hypothetical finite responses, not actual Xi.

## Conclusion

Write D_n=U_n+V_n, where

    U_n(c)=-2 exp(-cn/4) integral_(cn)^(c(n+2)) g_n(t)e_n(t)dt,
    V_n(c)= 2 exp(-cn/4) integral_n^(n+2) g_n(t)e_n(t)dt. (3)

There are fixed finite constants C_U,C_L such that

    ||U_n||_C(I) <= C_U(n+2) exp(kappa n),
    ||V_n||_C(I) <= C_L(n+2)
                     exp(n[B-1/16-log 4-(log n)/2]),    (4)
    B=-3/16+(7/2)log(100/79)+10/79+(1/2)log(125/3),
    kappa=B+9/32+(1/2)log(5/256).

Here B<8/3 and kappa is between 0.942341404098 and
0.942341404100. The lower-window term is therefore
O(exp(-n/64)), with substantial slack. The upper bound in (4)
does NOT pay the desired rate.

More specifically, for the enclosing circle

    C_n={exp(i phi)(s+R exp(i theta)): 0<=theta<=2pi},
    M_n=max_(zeta in C_n) |f_n(zeta)/omega(zeta)|,

the following is a valid, nonnegative upper envelope for ||U_n||:

    Bcal_n=18 exp(27/16)(n+2)exp(9n/32)
                 *80*M_n*sup_(t in [7n/4,9(n+2)/4])
                                    |omega(exp(it/(4n)))|. (5)

Even with its EXACT M_n, this particular envelope satisfies

    liminf_(n->infinity) log(Bcal_n)/n >= beta > 3/8,
    beta=9/32-3/16-(7/2)log(cos(1/8)-1/5)
          -(1/2)log(1/25+sin(1/8)^2)
          +(1/2)log(4 sin(5/32) sin(1/32)).             (6)

Equation (6) is a lower bound on an UPPER ENVELOPE, not on U_n or D_n.
It does not disprove O(exp(-n/64)) for the interpolant itself, for another
contour/estimate, or for general uncapped approximation. No conclusion
about C997s's capped E_n follows. The proposed exact-band-null measure
bound remains conditional on the still-unproved complete-residual rate.

Step383, 11 November 2026: RESEARCH / REPRODUCTION / EXPLORATION under
the unchanged pre-invocation EXPLORE review382. This is an inconclusive
specialization of known interpolation tools, with an explicit limitation
of the tested absolute estimate. The complete target was not achieved;
this write-up is independently unaudited and is not an RH candidate.

## Proof

### Imported contracts and the finite construction

The exact repeated-node remainder is imported from J.-P. Calvi,
*Lectures on Multivariate Polynomial Interpolation*, Hanoi, summer2005,
Chapter1, Theorem1.9 p14 and Theorems1.17–1.18 p21, (1.36)–(1.39),
[author PDF](https://www.math.univ-toulouse.fr/~calvi/res_fichiers/MPI.pdf).
Parent review381/step382 inspected the hypotheses and complete relevant
proofs. It applies to each holomorphic f_n separately, with repeated
nodes counted in omega and a piecewise C1 contour of index one around
the nodes and evaluation point inside a simply connected domain:

    f_n(y)-p_n(y)=(1/(2pi i)) integral_C_n
                     omega(y) f_n(zeta)/[omega(zeta)(zeta-y)] dzeta. (7)

No fixed-function asymptotic theorem is applied to this growing-n
function. We justify this specialization below; interpolation theory
is not reproved. The distinct-node version alone, e.g. DLMF3.3.6,
would not justify the multiplicities without the repeated-node input.

For an explicit finite construction let T_(a,m-1) denote truncation of
the analytic Taylor expansion at a after degree m-1. Then

    p_n(y)=(y-b)^ell T_(a,m-1)[f_n(y)/(y-b)^ell]
            +(y-a)^m T_(b,ell-1)[f_n(y)/(y-a)^m].        (8)

The two expansions are legitimate since a!=b. Indeed b/a=exp(2ih)
and 0<2h<1. Each summand has degree at most m+ell-1=n. At a, the
first differs from f_n by a zero of order at least m and the second
has that zero; the analogous statement holds at b with order ell.
Thus (8) is the imported Hermite interpolant and constructs all A_j.
They are independent of c, with no assertion concerning sum|A_j|.

C997c supplies the bound |g_n(t)|<=2(n+2)exp(3t/8) for t>=0,
including the original subtraction. Its cited input is the real
Laguerre inequality [DLMF18.14.8](https://dlmf.nist.gov/18.14.E8).
Its exact finite-measure representation and C997s's step373 audit
give, for the full upper/lower window densities, the variation costs

    T_U=18 exp(27/16)(n+2)exp(9n/32),
    T_L= 8 exp(3/4)(n+2)exp(-n/16).                    (9)

Only these audited contracts are used. C997r/t/u are scope contrasts,
not mathematical premises. Both beta terms, both windows and K's -1
remain in (3); no division by g_n or exclusion of its zeros occurs.

### Branch and enclosing geometry

The circle bounds the disk centered at exp(i phi)s with radius R.
Its rotated real part is at least s-R>79/100, so its closed disk lies
in D. The two nodes are exp(i phi)(s-id) and exp(i phi)(s+id), and
d<=h<=1025/8192<R. Both are strictly inside the circle.

For y=exp(it/(4n)) put delta=t/(4n)-phi. On the upper window,

    0<1/16-3/(8n)<=delta<=3/16+3/(4n).

On the lower window |delta|<=h+1/(4n). Both are within (-pi/2,pi/2),
so (2) gives Log_n(y)=it/(4n), with no winding or branch jump. Hence

    exp(15it/8) f_n(exp(it/(4n)))=exp(i z_star t).       (10)

Using |exp(i delta)-1|<=|delta| and 1-cos h<=h^2/2,

    |exp(-i phi)y-s| <= |delta|+h^2/2 <79/400           (11)

on BOTH closed windows. To check the strict inequality for all n>=1024,
each positive upper bound decreases in n; substitute n=1024 into
3/16+3/(4n)+h^2/2 and h+1/(4n)+h^2/2. These are rational quantities
strictly below 79/400. Thus every evaluation point lies strictly inside
C_n and its distance from that contour is greater than
1/5-79/400=1/400. The circle is smooth and positively oriented,
has index one as required, and avoids every node and evaluation point.
At y=a or b, (7) is interpreted directly with omega(y)=0, without any
division by a vanishing evaluation factor. The circle length is 2pi/5,
so (7),(10),(11) yield

    |e_n(t)|<=80 |omega(exp(it/(4n)))| M_n.             (12)

### A fully charged upper bound

For zeta=exp(i phi)x on C_n, |x|>=s-R>79/100 and
|arg x|<=R/(s-R)<20/79. The latter follows by bounding
|Im x|/Re x and using |arctan u|<=|u|. Therefore

    |f_n(zeta)|<=exp(n[-3/16+(7/2)log(100/79)+10/79]), (13)

since phi>=3/8. This includes the modulus of the n-dependent target
on the entire contour, not just its values on the spectral arcs.

Put w=x-s, so |w|=R. The paired node product obeys

    |(zeta-a)(zeta-b)|=|w^2+d^2|>=R^2-d^2>3/125,
    |zeta-b|>=R-d>7/100.                              (14)

For even n, omega has n/2 paired factors and one extra factor
zeta-b. For odd n it has (n+1)/2 paired factors; the extra half-pair
is bounded below by sqrt(3/125)>7/100. Hence in either case

    |omega(zeta)| >=(7/100)(3/125)^(n/2),
    M_n <=(100/7)exp(Bn).                             (15)

The inequalities in (14) follow already from d<=1025/8192; no numerical
trigonometric approximation is required for them.

For t in the upper window the chord bound gives

    |y-a|<=5/16+7/(8n)=(5/16)(1+14/(5n)),
    |y-b|<=1/16+5/(8n)=(1/16)(1+10/n).

Both right sides are less than one. The same parity split as above,
now for an upper bound, gives

    |omega(y)|<=exp(32/5)(5/256)^(n/2).                (16)

Here (1+x)<=exp(x) pays all finite-n corrections. On the lower window,

    |y-a|<=1/(4n), |y-b|<=1/4+1/(2n),
    |omega(y)|<=((n+2)/(16n^2))^(n/2)
                    <=e (1/(4 sqrt(n)))^n.            (17)

Equations (9),(12),(15)–(17) prove (4), for example with

    C_U=18 exp(27/16)*(8000/7)*exp(32/5),
    C_L=8 exp(3/4)*(8000/7)*e.

The exact scalar certificate below gives B<8/3. Since n>=1024,
log(4 sqrt(n))>=log128>4 (e<3 implies e^4<81<128). Thus the
lower-window exponential rate in (4) is less than
8/3-4-1/16=-67/48<-1. The factor n+2 is absorbed with strict
exponential slack, proving the stated O(exp(-n/64)) for V_n.

The achieved coarse upper-window rate is positive, whereas the target
requires at most -1/64, with enough slack for its polynomial prefactor.
This fact alone is not a lower obstruction for the actual error.

### The limitation of this particular absolute envelope

Equation (5) is precisely the result of using (12) on the upper
window and multiplying by (9)'s upper variation bound, with M_n
left exact. Consider the single contour point

    zeta_n=exp(i phi)(s-R).

Its two node distances are equal, giving

    M_n >= exp(-n phi/2)(s-R)^(-7n/2)
                           (R^2+d^2)^(-(n+1)/2).      (18)

For the upper endpoint y_n=exp(i*9(n+2)/(16n)), the two node
distances are exactly

    |y_n-a|=2 sin(5/32+7/(16n)),
    |y_n-b|=2 sin(1/32+5/(16n)).                       (19)

The sines are positive. Substitute (18),(19) into (5), then take
logarithms, divide by n and pass to the limit on this explicit lower
bound. We use only h->1/8, phi->3/8, m/n->1/2, ell/n->1/2,
continuity of logarithms at positive numbers and log(n+2)/n->0.
This proves (6); no asymptotic interchange of integrals is involved.
The certificate gives

    0.38435966017144 < beta < 0.38435966017146.

In particular the exact-sup envelope (5) cannot be O(exp(-n/64)).
This conclusion concerns the nonnegative expression (5). Neither
triangle inequality used to obtain it can be reversed. Oscillatory
cancellation in the Hermite integral or in the complete kernel might
still matter. Other contours are not excluded, and no assertion that
the balanced interpolant itself fails has been established.

### Verification, bounded decision and downstream limitation

Reproduction command from this notebook:

    python3 scripts/adaptive-slope/two-center-hermite-envelope-383.py

The full certificate is
`scripts/adaptive-slope/two-center-hermite-envelope-383.json`.
It records exact rational geometric bounds, 12-term alternating
Taylor enclosures for the four trigonometric values in (6), outward
80-digit Decimal intervals for every logarithmic rate, and all ten
scalar checks. The Decimal logarithm is correctly rounded; adjoining
the neighboring representable values gives outward endpoint bounds.
Every arithmetic operation is similarly widened. The checks establish
the scalar claims used above; they are not a numerical approximation
to the actual residual or an independent conceptual proof audit.

Under review382's one-attempt rule, park the BALANCED recipe with its
actual rate unresolved. The superexponential factor in (17) motivates
considering a different allocation of multiplicities; no estimate for
that uncovered target is derived here. C997r's cap/defect stop, C997t's
constant-ODE stop and C997u's parked determinant rate retain their scopes.

If a later argument proves ||D_n||<=C exp(-n/64), then for any finite
complex Borel measure mu on I with TV<=1 and EXACT pairings
integral k_n(c,gamma_j)dmu(c)=0, finite summation and the variation
inequality give

    |integral k_n(c,z_star)dmu(c)|=|integral D_n(c)dmu(c)|
                                  <=||D_n||_C(I).     (20)

This explains the downstream use; its desired premise is not proved
by (4). Unrestricted coefficients supply no bound for the original
capped objective. C997a(8), selected/both-sign transfer,
assay/reconstruction, complements/regulators, L993, L984(H),
L966/L968 forcing and L030–L032/C032a actual-Xi positivity remain open.

## Mathlib

Full matching coverage of this growing-n two-center complete-kernel
estimate has not been checked. No Mathlib theorem is used as an input.
The precise interpolation import is Calvi's result cited above;
unknown formal-library coverage is not evidence of absence.
