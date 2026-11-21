# Corollary 999g: shifted theta core and an inconclusive first-exponential comparison

## Hypotheses

Let theta(q)=sum_{n in Z} exp(-pi*n^2*q), initially Re(q)>0,
and let xi_Q(w,s)=s(s-w) Z_Q(w,s)/(2w) be the entire completion
of J. C. Lagarias and E. Rains, *On a Two-Variable Zeta Function
for Number Fields*, [arXiv:math/0104176v5, 7 July 2002](https://arxiv.org/pdf/math/0104176v5),
Theorem 2.1 and (2.9), printed pp. 8--9. Set

    G(w,t)=xi_Q(w,w/2+i*t),  1<=w<=3/2,  40<=t<=45,
    y=pi/8, z=x+i*y, v=exp(2x), V=exp(4).

The theta convention and distinguished slice G(1,t)=Xi(t) are those
of L018/L019. No zero, collision, curvature, transport or RH assumption
is made. A w derivative always holds t fixed and moves s=w/2+i*t.

Use the holomorphic logarithm in Re(q)>0 continued from positive
real theta values. Nonvanishing and the branch are supplied by the
source Proposition 3.2/(3.7), printed p. 12, and its use in Lemma 4.5;
the same product is [DLMF 20.5.3](https://dlmf.nist.gov/20.5.E3).
On |Im(z)|<pi/4 put

    T(z)=theta(exp(2z)), B(z)=log T(z), b(z)=z/2+B(z),
    d(z)=(b'(z))^2-1/4=B'(z)+(B'(z))^2.

Primes below mean z derivatives. Import the normalized full-line
formula from the source Theorem 4.4 **proof (4.8)** and its equivalent
(4.9), printed pp. 21--24, with Lemmas 4.5--4.7:

    xi_Q(w,s)=1/2 integral_R gamma(w,x+i*y) exp(s*(x+i*y)) dx,
    gamma=(partial_z^2+w*partial_z)[(T(z)^w-1)/w].             (1)

The proof's factor exp(i*s*y) is retained. The theorem display that
omits it is not used. Source compact-strip convergence applies because
y=pi/8 is strictly inside the strip. These are imported theorems, not
local contour reproofs. C999f motivates the comparison but its unreviewed
claims and real-axis tail constants are not inputs to this proof.

## Conclusion

Define

    M(w,z)=exp(w*b(z))*[b(z)*b''(z)+(1+w*b(z))*d(z)],
    C(w,t)=exp(-t*y) Re integral_0^2 M(w,x+i*y) exp(i*t*x) dx.

Then the complete centered derivative satisfies

    G_w(w,t)=C(w,t)+R_tail(w,t),
    |R_tail|<=E(t)
       :=8190 exp(-t*y-2V)*(V^2/2+V/2+1/4)<10^(-40).        (2)

In particular, C is exactly

    Re partial_w [(1/2) integral_{-2}^2
                     gamma(w,x+i*y) exp((w/2+i*t)*(x+i*y)) dx],

with t fixed, as in the approved target. The source 1/2 occurs once.
There are no omitted finite vertical connectors: (1) is used directly.

Here is the particular signed approximation tested. Put

    u=pi*exp(2z), p(z)=2 exp(-u),
    M_0(w,z)=exp(w*z/2)*[(z/2)*p''+(1+w*z/2)*p']
            =4u exp(w*z/2-u)*[z*(u-1-w/2)-1],
    A(w,t)=exp(-t*y) Re integral_0^2 M_0(w,x+i*y) exp(i*t*x) dx,
    R_0=14625 exp(-4).

The complete error of this approximation obeys

    |G_w-A|<=exp(-t*y)*R_0+E(t),
    |A|<9 exp(-t*y),             R_0>180.                    (3)

Thus the certified interval centered at the **signed** A, with the
error allowance in (3), strictly contains zero everywhere in the box.
Even an exact evaluation of A would not make this particular allowance
meet either sign test. R_0 is an upper error allowance, NOT a lower
bound on the actual error or on the size of higher theta terms.
Sharper signed treatment remains logically possible.

This is an inconclusive comparison, not a positive margin, a certified
nonpositive point, a no-go theorem for G_w, or an RH result. The formula
and all stated bounds passed the later conceptual audit in step431
(11 November 2026), under exactly the hypotheses above. This validates
the local specialization and its inconclusive enclosure, not a new
sign theorem or a result beyond the literature comparison's scope.

## Proof

### Centering, branch, and differentiation

The source Theorem 2.1 remark identifies xi_Q(1,s)=xi(s), so L018
gives G(1,t)=Xi(t) with no further rescaling. In the half-plane
Re(q)>0, the product (3.7) has nonzero factors and locally summable
deviations from 1; hence it is nonzero. The holomorphic logarithm
theorem on this simply connected half-plane gives the branch used
above. Its real normalization also fixes conjugation. These are
applicability checks for the cited source inputs, not a reproof of
its entire-family or shifted-contour theorem.

Differentiating the source definition of gamma gives the algebraic
identity, including its removable w=0 value,

    gamma=exp(w*B)*[B''+w*(B')^2+w*B'],
    exp(w*z/2)*gamma(w,z)=K(w,z)
       :=exp(w*b(z))*[b''(z)+w*d(z)].

Its w derivative is exactly M. In particular the z/2 in b keeps the
derivative of exp(w*z/2), including the outside exp(i*w*y/2) in (1).
There is no discarded completion term: the completed source formula
is differentiated as a whole. Equivalently the left derivative is
(partial_w xi_Q+(1/2)*partial_s xi_Q)(w,w/2+i*t), not partial_w
xi_Q with s held fixed. Source (4.8)-(4.9), with its exp(i*s*y),
was checked again against the full proof and the hypotheses of
Lemmas 4.5--4.7 in step431. Lemma 4.6 supplies the compact-uniform
statement; no uniform assertion from the remark after Lemma 4.7 is
needed, and its w=0 subtraction case is not a premise here.

The Jacobi transformation underlying L019 extends holomorphically
to the strip and gives T(-z)=exp(z)*T(z). The branch identity
B(-z)=z+B(z) follows by equality on the real axis and the identity
theorem; it is not a new pointwise principal-log choice. Consequently
b and M are even, and for real w they commute with conjugation.

We give explicit domination, so the remaining differentiation is not
inferred from pointwise smoothness. On either line z=x+/-i*y, x>=0,
write S=T-1. Since pi/sqrt(2)>2 and pi<4, the theta series gives

    |S|<=3 exp(-2v),
    |T'|<=17 v exp(-2v),
    |T''|<=170 v^2 exp(-2v).                                (4)

For details, n^2>=1+3(n-1), n^2<=4^(n-1), and
n^4<=16^(n-1) for n>=1. The Taylor series gives e^3>20,
hence e^6>400. Therefore the three sums without the factors from
differentiation satisfy

    sum exp(-2n^2 v) <=(400/399)exp(-2v),
    sum n^2 exp(-2n^2 v) <=(100/99)exp(-2v),
    sum n^4 exp(-2n^2 v) <=(25/24)exp(-2v).

Here T'= -4 sum u_n exp(-u_n), T''=8 sum (u_n^2-u_n)exp(-u_n),
where |u_n|<4n^2v. Thus their constants are bounded respectively by
16*(100/99)<17 and 128*(25/24)+32*(100/99)<170, proving (4).
The differentiated series converge locally uniformly.

Since e^2>7, |S|<3/7<1/2. This S bound also holds throughout
Re(z)>=0, |Im(z)|<=y, since cos(2*Im(z))>=1/sqrt(2).
The convergent log(1+S) therefore agrees with the specified branch
by analytic continuation from the positive real axis in this
connected half-strip, and by continuity on its boundary.
The logarithmic derivative formulas imply

    |B|<=6 exp(-2v), |B'|<=34v exp(-2v),
    |B''|<=510v^2 exp(-2v), |d|<=200v^2 exp(-2v).            (5)

Indeed |1/T|<2; the constants for B'' and d are bounded by
340+1156/7<510 and 34+1156/7<200. Also

    |b|<=x/2+y/2+6/7<x/2+2.

For complex |w|<=2, |exp(w*b)|<=exp(x+3), because
|w*z/2| in real part is at most x+y and 2|B|<=12/7.
It follows that

    |M|<=54540 v^3 exp(-2v),
    |K|<=24570 v^(5/2) exp(-2v).                            (6)

For M use 510(x/2+2)+200(1+2(x/2+2))=455x+2020,
exp(3)<27, and x+1<=exp(x). The K bound is immediate from (5).
Reflection gives the same bounds on the negative half-line, using
the opposite shifted line at positive x. For |Im(t)|<=1 and
|Re(t)|<=46 the extra factor exp(i*t*z) is bounded by
exp(|x|+23). This remains integrable against both bounds (6).
They dominate on a complex neighborhood of the real parameter box.
Dominated holomorphic differentiation in w of imported (1) now gives

    G_w=(exp(-t*y)/2) integral_R M(w,x+i*y) exp(i*t*x) dx.    (7)

For real w,t, evenness and conjugation make the two half-line
integrals in (7) conjugate: M(w,-x+i*y)=M(w,x-i*y)
=conj(M(w,x+i*y)), while exp(-i*t*x)=conj(exp(i*t*x)).
The same is true for their truncations
and complements. This proves the asserted expression for C and
reduces the tail estimate to the positive half-line.

### Full differentiated complex tail

For real w in the box the constants improve to
|exp(w*b)|<=exp(3x/4+9/7)<9exp(x), using e<3. Thus (5) gives

    |M|<=9exp(x)*(405x+1820)*v^2 exp(-2v)
         <=16380 v^3 exp(-2v).                             (8)

Integrating (8) over x>=2, and substituting v=exp(2x), yields E(t)
in (2); the factor 1/2 in (7) has already been canceled by the two
reflected tails. No part of the differentiated complement is omitted.

For an elementary numerical bound, V=e^4>50, since e^3>20 and
e>8/3. The function exp(-2V)*(V^2/2+V/2+1/4) is decreasing.
Hence E(t)<11000000 exp(-100-t*y). Further e^100>e^99>20^33>
10^42, while t*y>=5pi>15 and e^15>20^5=3200000. These inequalities
give E(t)<10^(-40), with ample slack, without numerical quadrature.
Explicitly, the derivative of exp(-2V)*(V^2/2+V/2+1/4) is
-V^2*exp(-2V), and its prefactor at V=50, after multiplication
by 8190, is 20888595/2<11000000. The preceding estimates give
E(t)<(55/16)*10^(-42)<10^(-40). For the elementary constants,
sum_{k=0}^8 3^k/k!=806769/40320>20, and e>8/3 follows from
its terms through degree3. Also 2^30=1024^3>10^9 implies
20^33>10^42. Thus these are strict rational comparisons, not
decimal approximations to a numerical integral.

### Signed first-exponential term and its nonlinear error

The retained term M_0 is the part linear in p of the exact expression
for M; its displayed closed expression follows from
p'=-4u exp(-u), p''=8(u^2-u)exp(-u). Its oscillatory integral A is
retained with its sign. There is no saddle assumption or substitution
of a favorable smaller rectangle.

For completeness bound all terms dropped from this approximation.
Let r=S-p. For n>=2, n^2>=4+5(n-2),
n^2<=4*4^(n-2), and n^4<=16*16^(n-2). Since e^10>8000,
geometric summation gives

    |r|<=4 exp(-8v), |r'|<=80v exp(-8v),
    |r''|<=2400v^2 exp(-8v).                               (9)

For the last two constants the corresponding n^2 and n^4 sums
are less than 5exp(-8v) and 17exp(-8v); thus
128*17+32*5=2336<2400. Using e^4>49 and |S|<1/2,
the log series and logarithmic derivative formulas yield

    |B-p|<=10 exp(-4v),
    |B'-p'|<=104v exp(-4v),
    |B''-p''|<=2230v^2 exp(-4v),
    |d-p'|<=1260v^2 exp(-4v).                              (10)

To check each loss: |B-S|<=|S|^2; then add |r|.
For B'-p', write r'-T'S/(1+S), whose constants are less than
2+102. For B''-p'', write
r''-T''S/(1+S)-(T'/T)^2, whose constants are less than
49+1020+1156=2225. Finally add |B'|^2 to the preceding first
derivative bound to obtain 104+1156=1260, using v>=1.

Put A_0=(z/2)*p''+(1+w*z/2)*p', so M_0=exp(w*z/2)*A_0,
and A_1=b*B''+(1+w*b)*d. Since |z|/2<=x/2+1/4,
|p'|<=16v exp(-2v) and |p''|<=160v^2 exp(-2v),

    |A_0|<=(92x+62)v^2 exp(-2v).

The exact difference is

    A_1-A_0=(z/2)(B''-p'')+B*B''
              +(1+w*z/2)(d-p')+w*B*d.

Equations (5) and (10) give

    |A_1-A_0|<=(2060x+7150)v^2 exp(-4v).

Here the four constant contributions are
2230(x/2+1/4), 3060, 1260(11/8+3x/4), and 1800.
Also |exp(wB)|<9 and |exp(wB)-1|<=81exp(-2v).
Expanding exp(wB)*A_1-A_0 therefore proves

    |M-M_0|<=72000v^3 exp(-4v).                            (11)

Indeed 81*92+9*7150=71802<72000, after bounding each linear
polynomial by its stated larger coefficient times x+1, and using
exp(3x/4)*(x+1)<=exp(2x).
More explicitly, before this simplification the coefficient is
81*(92x+62)+9*(2060x+7150)=25992x+69372,
which is at most 71802*(x+1). The coefficient 7150 above is
2230/4+3060+1260*(11/8)+1800; its slope is
2230/2+1260*(3/4)=2060. All four omitted terms are included.

Integration of (11), allowing the interval to increase from [0,2]
to [0,infinity), gives

    |C-A|<=exp(-t*y)*36000 integral_1^infinity v^2 exp(-4v)dv
           =exp(-t*y)*14625exp(-4).

Similarly |M_0|<=96v^3exp(-2v), hence

    |A|<=exp(-t*y)*48 integral_1^infinity v^2exp(-2v)dv
         =exp(-t*y)*60exp(-2)<9exp(-t*y).

For these integrations, integral_1^infinity v^2exp(-a*v)dv
=exp(-a)*(1/a+2/a^2+2/a^3), a>0, by two integrations by
parts. Its polynomial factors are 13/32 at a=4 and 5/4 at
a=2. Moreover 92x+62<=96*(x+1) justifies the bound for M_0.
The factor 1/2 from dx=dv/(2v) appears in 36000 and 48;
there is no second uncanceled half-line normalization.

Finally e^4<81 implies R_0>14625/81>180. The lower endpoint
in (3) is less than (9-180)exp(-t*y)<0; its upper endpoint is
greater than (180-9)exp(-t*y)>0. These statements concern the
chosen enclosure, not the actual sign of G_w. They prove the
failure of this single conservative comparison to meet the required
uniform margin or nonpositive-point threshold. No conclusion about
G_tt, event existence, higher multiplicities or global transport follows.

## Mathlib

Full matching coverage is unchecked and unknown. No formal verification
of the shifted family, derivative or constants is claimed. The source
entire-family and contour theorems are imported with the exact branch
and normalization stated above; standard holomorphic differentiation,
the identity theorem and geometric-series bounds support the local
specialization. No general positivity theorem is invoked.
