# Lemma 716: uniform nonzero limit of the exact resolvent ratio

## Hypotheses

Use the exact coefficients and polynomial from L714:

    U=121/64, A=27/10, d=5/4, c_0=1/8,
    alpha=d+c_0=11/8, u=(3+4i)/10,
    n=12q+3, q>=1, N=n-1,
    b_(n,j)=(-1)^j*n^N/[j!*(N-j)!]
                         *product_(k=1)^N (U-j*k/n^2),
    H_n(z)=sum_(j=0)^N b_(n,j)*z^j.

All roots of H_n are real and greater than one, by the audited part
of L714. Let ell_n be the analytic logarithm of H_n(z)/H_n(0) with
ell_n(0)=0 on |z|<1. Use the audited L715 limit ell_n/n -> F locally
uniformly on this disk, including its probability measure kappa on
[0,1] and its inverse identification. No other assertion of L714 is
an input to the proof.

Keep the original fixed bump interval, with

    omega=A*[log(9/5)-4/5+(121/100)*log(201/121)],
    I=[omega-delta,omega+delta],  0<delta<1/3000.

In particular delta is fixed before n; it can be the original L703
width. No extension, regularity or endpoint law of the bump is needed.
Define z_v=exp(-u*v/A) and the standalone finite ratio

    Q_n(v)=[sum_(j=0)^N b_(n,j)*z_v^j/(alpha+u*j/n)]/H_n(z_v).

The coefficients, original spatial unit masses, anchor, inverse angle,
j=0 term, both physical endpoints and all moments are unchanged.
Those additional family data are not assumptions about cancellation.

## Conclusion

Uniformly for every v in the entire closed interval I,

    Q_n(v) -> Q(v)=1/[alpha+u*z_v*F'(z_v)].                 (1)

The limit is continuous and satisfies the explicit bounds

    Re[alpha+u*z_v*F'(z_v)] >= 1/24,
    8/47 <= |Q(v)| <= 24.                                 (2)

Consequently Q_n is nonzero on I for all sufficiently large permitted
n, and eventually inf_I |Q_n|>=4/47. The onset is existential; no
effective convergence rate or assertion for every finite n is made.

This is a local advance beyond the conclusions of the sources checked
for this ratio, not certified originality. It passed the separate
conceptual audit in Section 6 (step 183, 3 November 2026).
L714's finite inverse-density application passed its separate step-185
audit; this result does not evaluate the fixed signed bump integral,
other response terms or any spatial Jensen defect. Amplitude/full
charge, angular persistence, H/support, Xi realization and all-degree
positivity remain open. This is not an RH candidate.

## Proof

### 1. Reused coverage and the exact integral

Use the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-resolvent-polynomial-ratio.md`.
Its target is precisely this ratio on I. The general endpoint
asymptotic theorems inspected there do not automatically apply to
the growing array. The proof below instead establishes its required
majorant directly. It does not reprove the zero-distribution theorem.

The source behind the audited L715 input is J. Jalowy, Z. Kabluchko
and A. Marynych, *Zeros and exponential profiles of polynomials I*,
[arXiv:2504.11593v1](https://arxiv.org/pdf/2504.11593v1),
Definitions 1.1--1.2, p.3, and Theorem 2.2(a),(b),(e), pp.5--6.
All application hypotheses, normalization and the unique open-disk
logarithm were checked in L715. Here only that established local
input and L714's audited coefficient/root part are reused.

For each fixed n, Re(alpha+u*j/n)>=alpha>0. Direct integration of
each exponential, followed by a finite sum, therefore gives

    Q_n(v)=integral_0^infinity e^(-alpha*t)
                  H_n(z_v*exp(-u*t/n))/H_n(z_v) dt.        (3)

This is absolutely convergent for each n: expanding the numerator
gives finitely many decaying exponentials, and the denominator is
nonzero. The enclosure in Section 3 verifies v/A>2/5, hence |z_v|<1.
No contour deformation or infinite-sum interchange is involved in
(3). Uniformity in n will follow from a separate bound below.

### 2. Exact moments for the limiting logarithmic derivative

Write m_k=integral_0^1 a^k kappa(da). From L715,

    F(z)=-sum_(k>=1) m_k*z^k/k,
    y(z)=-z*F'(z)=sum_(k>=1) m_k*z^k,  0<=m_k<=1.         (4)

These series and their differentiated series converge uniformly on
compact subdisks. Set J(t)=integral_0^1 s/(U-t*s)ds. L715's inverse
relation, first for negative real z near zero, implies

    y=z*phi(y),  phi(y)=(1+y)*exp(-J(-y)),
    J(-y)=sum_(l>=0) (-1)^l*y^l/[(l+2)*U^(l+1)].          (5)

Indeed at z=-x, x>0 small, L715 gives z*F'(z)=t(x) and
x=t(x)/(1-t(x))*exp(J(t(x))). Set y=-t(x) to obtain (5).
Both sides are analytic near zero, so equality extends there.
The map y/phi(y) has nonzero derivative at zero because
phi(0)=exp(-1/(2U))>0; the inverse branch is the one in (4).

The classical Lagrange--Bürmann coefficient inversion, specialized to
(5), gives

    m_k=exp(-k/(2U))*c_k,
    c_k=(1/k)*[w^(k-1)] (1+w)^k
            *exp(sum_(l>=1) e_(k,l)*w^l),
    e_(k,l)=k*(-1)^(l+1)/[(l+2)*U^(l+1)].                 (6)

For completeness, this specific coefficient identity is checkable by
Cauchy's coefficient formula, without importing an asymptotic result.
Change the small coefficient contour from z to w=y(z), using
z=w/phi(w). Its residue becomes the residue of

    phi(w)^k*w^(-k)-phi(w)^(k-1)*phi'(w)*w^(1-k).

If a_(k-1)=[w^(k-1)]phi(w)^k, the first residue is a_(k-1)
and the second is (k-1)*a_(k-1)/k (zero when k=1).
Their difference is a_(k-1)/k, proving (6). The change of variable
is justified by the analytic inverse just verified. This short
specialization is included to justify the exact implemented moments,
not to claim a new inversion theorem.

Only k<=80 is computed. If h_m is the coefficient of w^m in
exp(sum_(l>=1) e_(k,l)w^l), its exact finite recurrence is

    h_0=1,
    h_m=(1/m)*sum_(l=1)^m l*e_(k,l)*h_(m-l),
    c_k=(1/k)*sum_(m=0)^(k-1) binom(k,k-1-m)*h_m.         (7)

The recurrence follows by differentiating that exponential and
equating coefficients. All numbers in (7) are rational. It requires
no evaluation of a complex inverse away from zero or boundary law.

### 3. A certified bound along the whole Laplace path

Put z(x)=exp(-u*x), x>=2/5, and

    G(x)=-Re[u*z(x)*F'(z(x))]
        =Re[u*sum_(k>=1) m_k*z(x)^k].                     (8)

We prove G(x)<4/3 for every such x. Write p=3/10, b=2/5, so
u=p+i*b and |u|=1/2. On [2/5,6/5], |z(x)|<=exp(-3/25)<9/10.
Truncate (8) at K=80. From 0<=m_k<=1, the absolute tail is at most

    (1/2)*sum_(k=81)^infinity (9/10)^k
      =5*(9/10)^81.                                     (9)

On the same interval, termwise differentiation of (8) gives

    |G'(x)| <= |u|^2*sum_(k>=1) k*(9/10)^k=45/2.         (10)

Use the 401 grid points x_j=2/5+j/500, 0<=j<=400. Every point of
the closed interval has distance at most 1/1000 from one of them,
so the Lipschitz cost in (10) is 9/400. At each grid point the
finite sum is

    sum_(k=1)^80 m_k*exp(-p*k*x_j)
                  *[p*cos(b*k*x_j)+b*sin(b*k*x_j)].       (11)

The exact certificate is
`scripts/one-sided-hankel/resolvent-tail-certificate-181.json`,
generated by

    python3 scripts/one-sided-hankel/resolvent-tail-certificate-181.py

The script implements (6)--(7) with exact rational arithmetic and
outward intervals on the scale 2^120. To specify the transcendental
enclosures fully: for 0<=r<=1, the degree-41 and degree-40 alternating
Taylor polynomials bound exp(-r) from below and above. For sin(r)
and cos(r), sum the terms with indices 0 through 20 and subtract
the magnitude of the next (negative) term for a lower endpoint.
Alternating remainders justify these enclosures. The actual arguments
are 1/(2U), p*x_j and b*x_j, all in [0,1]. Interval powers of
exp(-1/(2U)) give the moments in (6); complex interval powers of
exp(-p*x_j)*(cos(b*x_j)-i*sin(b*x_j)) give (11).
Every product uses all four endpoint products and rounds its lower
endpoint down and upper endpoint up. Sums are exact on the scale.

For omega the code uses, at x=9/5 and x=201/121,

    r=(x-1)/(x+1),
    2*sum_(j=0)^11 r^(2j+1)/(2j+1)
       <=log(x)
       <=2*sum_(j=0)^11 r^(2j+1)/(2j+1)
                          +2*r^25/[25*(1-r^2)].          (12)

This follows by integrating the geometric series for 1/(1-r^2);
all omitted terms are positive and their denominators are at least
25. No floating-point comparison is used for a decision. Full exact
moments, all grid rows, bounds and failures are saved in the JSON.

The complete finite calculation passes all nine checks. In particular
the maximum upper endpoint of (11), plus BOTH (9) and 9/400, is

    M = 143309089951166564695849146572596572514780254635826974054275429128688156899539220671638561517
        /109951162777600000000000000000000000000000000000000000000000000000000000000000000000000000000
      < 4/3.                                            (13)

Its decimal preview is 1.30338858026486; the strict rational
comparison, not this preview, is the certificate. The same calculation
verifies exp(-3/25)<9/10, exp(-9/25)<7/10, and

    (omega-1/3000)/A>2/5,
    (omega+1/3000)/A<6/5.                               (14)

Equations (9)--(13) prove the bound on the entire compact interval,
not only at the grid points. For x>=6/5, |z(x)|<=7/10 and (4) gives
the independent analytic bound

    G(x)<=|u|*|z(x)|/(1-|z(x)|)<=7/6<4/3.               (15)

This covers the unbounded remainder of the path. The moments are
those of the unique L715 measure; no sampled finite-n zero law or
unverified numerical inverse is used.

### 4. Eventual uniform domination for the growing array

Cauchy's integral formula applied on slightly larger compact subdisks
to the audited convergence ell_n/n -> F gives

    ell_n'/n -> F' locally uniformly on |z|<1.             (16)

In particular, for

    G_n(x)=-Re[u*z(x)*ell_n'(z(x))/n],

the convergence G_n -> G is uniform on [2/5,6/5]. From (13), choose
one n_0, along the full permitted sequence, such that

    G_n(x)<=65/48,  2/5<=x<=6/5, n>=n_0.                 (17)

Indeed 65/48-4/3=1/48>0, and (16) makes the error smaller than that
fixed gap. This onset is independent of v. For x>=6/5, use the
finite root factorization with a_(n,k)=1/rho_(n,k) in (0,1):

    z*ell_n'(z)/n=-(1/n)*sum_(k=1)^(n-1) a_(n,k)*z/(1-a_(n,k)*z).

It implies, for EVERY n,

    |u*z*ell_n'(z)/n|<=(1/2)*|z|/(1-|z|)<=7/6
                                   when |z|<=7/10.      (18)

Thus (17) holds for all x>=2/5 after the same n_0. There is no
appeal to local convergence on an unbounded set.

For v in I and t>=0, (14) gives x=v/A+t/n>=2/5. Differentiating
the real logarithm of the root-free ratio along this path gives

    d/dt log|H_n(z_v*exp(-u*t/n))/H_n(z_v)|
        =G_n(v/A+t/n).

At t=0 this logarithm is zero. Integrate (17)--(18) and include the
factor in (3) to obtain the global majorant

    |e^(-alpha*t)*H_n(z_v*exp(-u*t/n))/H_n(z_v)|
       <=exp(-(alpha-65/48)*t)=exp(-t/48),
                          n>=n_0, v in I, t>=0.        (19)

The entire tail is now paid uniformly in both parameters.

### 5. Uniform limit and its nonvanishing

For each fixed T<infinity the analytic logarithm difference is exactly

    ell_n(z_v*exp(-u*t/n))-ell_n(z_v)
      =-integral_0^t u*z_v*exp(-u*s/n)
                    *ell_n'(z_v*exp(-u*s/n))/n ds.       (20)

All arguments lie in a common compact subdisk. By (16), continuity
of F' and the uniform convergence exp(-u*s/n)->1 for s<=T, (20)
converges to -u*z_v*F'(z_v)*t uniformly for v in I, 0<=t<=T.
Exponentiation preserves this uniform convergence on a bounded set.
The integrand of (3) therefore tends locally uniformly to

    exp(-lambda(v)*t),  lambda(v)=alpha+u*z_v*F'(z_v).

Equations (8), (13)--(15) give Re(lambda(v))>=alpha-4/3=1/24.
For a fixed cutoff T, integrate the uniform convergence on [0,T].
The remaining tails are bounded uniformly by 48*exp(-T/48) from
(19), and 24*exp(-T/24) for the limiting exponential. Let n tend
to infinity first, then T tend to infinity. This proves uniform
convergence of (3) to integral_0^infinity exp(-lambda(v)*t)dt
=1/lambda(v), establishing (1) with both endpoints included.

The denominator is continuous and has positive real part. From (4),
|z_v|<=9/10 and |u|=1/2,

    |lambda(v)|<=alpha+(1/2)*9=47/8.

This proves both bounds in (2). Uniform convergence then makes
|Q_n-Q|<4/47 throughout I for all sufficiently large n, giving
the eventual lower bound. No zero assertion is extrapolated from
finite numerical ratios. The separate Decimal diagnostic in
`scripts/one-sided-hankel/resolvent-ratio-diagnostic-181.py` is not
an input to any inequality or limit in this proof.

### 6. Separate conceptual audit — 3 November 2026, step 183

**Verdict: accepted within exactly the stated closed-interval scope.**
The audit uses the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-resolvent-ratio-conceptual-audit.md`.
No equation, constant, conclusion or direct mathematical input requires
correction. This is independent validation of the existing local
argument, classified REPRODUCTION; no stronger result or certified
originality is claimed. The finite certificate is checked independently
below, together with the analytic premises that computation cannot prove.

**Inverse moments and sources.** The audited L715 identity is
dF(-x)/dx=t(x)/x. Hence F'(-x)=-t(x)/x,
(-x)F'(-x)=t(x), and y(-x)=-t(x). Substitution in X(t) gives
z=y*exp(J(-y))/(1+y), with exactly the sign in (5).
J(-y) is analytic for |y|<U; phi(0)=exp(-1/(2U)) is nonzero,
so the derivative of y/phi(y) at zero is exp(1/(2U)), not zero.
The local analytic inverse is consequently the same germ as -zF'(z).
The identity theorem is applied only near zero; no global inverse
branch or boundary continuation is presumed.

The named standard inputs are the local analytic inverse and
Lagrange--Bürmann residue formulas in
[NIST DLMF 1.10(vii), (1.10.12)--(1.10.14)](https://dlmf.nist.gov/1.10.vii),
and Cauchy's function/derivative formulas in
[DLMF 1.9(iii), (1.9.30)--(1.9.31)](https://dlmf.nist.gov/1.9.iii),
as inspected in the ready assessment on 3 November 2026. Their
analyticity and nonzero-derivative/contour hypotheses are supplied
here and in Sections 2 and 4, respectively. The JKM input remains
the precisely cited and audited L715 specialization; it is not
reproved or extended. The small-contour substitution in Section 2
is valid on the biholomorphic neighborhood just obtained. Its two
residues have coefficients a_(k-1) and (k-1)*a_(k-1)/k; the latter
is zero at k=1. Thus the implemented moments have the correct 1/k
normalization, including m_1=exp(-32/121). The rational recurrence
(7) follows coefficient by coefficient from the derivative of its
exponential, without convergence assumptions beyond this local germ.

**Full finite evidence.** The original Python source was read in full,
including all rounding and transcendental functions. A separate program
and full certificate are

    scripts/one-sided-hankel/resolvent-tail-audit-183.py
    scripts/one-sided-hankel/resolvent-tail-audit-183.json

Reproduce them with

    python3 scripts/one-sided-hankel/resolvent-tail-audit-183.py

The independent coefficient check does not repeat the original
exponential recurrence followed by a binomial convolution. Write

    B_k(w)=(1+w)^k*exp(sum_(l>=1)e_(k,l)*w^l)=sum_(m>=0) a_m*w^m.

Its logarithmic derivative has coefficient

    D_l=k*(-1)^(l+1)+l*e_(k,l)

at w^(l-1). Therefore a_0=1 and

    a_m=(1/m)*sum_(l=1)^m D_l*a_(m-l),
    c_k=a_(k-1)/k.

For every 1<=k<=80 this independent rational c_k equals the original
saved coefficient exactly. The new program uses outward intervals
with scale 2^192. Exponential Taylor degrees 44 and 45 bracket
exp(-r); sine/cosine terms through index 22 bracket their functions
after subtracting the next negative term at degrees 47 and 46.
Every argument is in [0,1], where the relevant alternating terms
decrease in modulus. All quantities are rational before outward
rounding. Integer floor division gives the lower endpoint even for
negative products; divmod with positive denominator gives the upper
ceiling. Taking all four endpoint products, or subtracting opposite
endpoints, preserves inclusion. Repeated interval multiplication
therefore encloses exp(-k/(2U))*c_k for each computed moment.

For each of the 401 exact grid points, the independent program
evaluates sum_(k=1)^80 m_k*z^k by complex Horner iteration, then
takes p*Re minus b*Im. This differs from the original sum of successive
complex powers, and retains the required positive b*sin term in (11).
Every new moment interval and every new grid interval lies inside its
original saved interval. This proves validity of those complete saved
enclosures, not merely agreement of decimal centers. All rows are read;
the original maximum, the exact fraction (13), both costs, and each of
the nine original checks are recomputed and checked against their
specified thresholds. Source/certificate hashes and full rational
coefficient and row evidence are saved. No decimal preview participates
in a decision. There are 1885 passing exact audit checks and no failures.

The initial scale-2^128 Horner calculation already met the 4/3 threshold
in all cells but produced intervals too wide to prove containment in
the original intervals: all 401 containment checks failed. That is not
a contradiction between the enclosures and was not accepted as a
completed certificate audit. Its complete script and evidence are
preserved as `resolvent-tail-audit-183-first-pass.py` and `.json` in
the same directory. Raising only the arithmetic precision to 2^192
resolved containment; no mathematical threshold or claim was weakened.

The geometric-series tail is exactly 5*(9/10)^81. Differentiating the
absolutely convergent moment series costs
|u|^2*sum k*(9/10)^k=45/2; nearest-grid distance 1/1000 costs 9/400.
The mesh covers both endpoints of [2/5,6/5]. The original upper M,
including both costs, is the exact fraction (13), strictly below 4/3.
For the independent check, logarithm sums through index 15, with
remainder 2*r^33/[33*(1-r^2)], give a narrower enclosure of omega
inside the original one. They retain both inequalities (14) for every
fixed 0<delta<1/3000. The exponential radius bounds and 7/6<4/3
verify the separate unbounded-path estimate (15). These computations
use the probability-measure moments from L715; no empirical zero law
or inversion away from zero enters.

**Uniform analytic passage.** The root location makes H_n zero-free
and defines its normalized analytic logarithm on the disk used in (3).
At finite n the coefficient denominators have real part at least
alpha; the finite-sum integral is therefore absolutely convergent
without any uniform estimate being presumed. On the compact path
segment choose radii r<r'<1 containing it strictly. Cauchy's derivative
formula on circles with a fixed positive separation, applied to
ell_n/n-F, proves (16) uniformly there. The positive fixed gap
65/48-4/3=1/48 then yields one n_0 for the whole segment along
n=12q+3. Beyond x=6/5, the exact n-1 reciprocal roots and division
by n give (18) for every n. Thus the same n_0 works for every
v in the original closed I and every t>=0, including t comparable
to or larger than n. Compact convergence has not been used on an
unbounded parameter range without this separate root estimate.

Along the root-free path the derivative of log modulus is G_n;
its value starts at zero. Integration gives the full majorant
exp(-t/48) in (19), with no hidden denominator constant depending
on n or v. The analytic logarithm difference in (20) fixes any phase
ambiguity because its exponential is exactly the polynomial ratio.
For fixed T all its arguments remain in one compact subdisk and
exp(-u*s/n) tends uniformly to one. The asserted compact integrand
convergence follows. If its uniform error on I times [0,T] is
epsilon_n(T), the full integral error is at most

    T*epsilon_n(T)+48*exp(-T/48)+24*exp(-T/24).

First n tends to infinity at fixed T; then T tends to infinity.
This proves uniform convergence including both bump endpoints.
The strict damping leaves Re(lambda)>=1/24; the geometric moment
bound gives |lambda|<=47/8. These are respectively the upper bound
24 and lower bound 8/47 for the limiting modulus. Uniform convergence
with error less than 4/47 proves the eventual nonvanishing and stated
4/47 lower bound for Q_n. The onset remains existential.

The direct mathematical inputs remain the exact L714 coefficients/root
part and audited L715, exactly as recorded in the unchanged DAG.
L714 (2), its signed decomposition, other response terms, the fixed
outer bump integral and its possible cancellations were not used in
this audit. The preserved signed-bump, absolute-contour and positive-
blend failures do not contradict this quotient result. No boundary
law, effective rate, complementary Jensen-defect payment or Xi
realization has been obtained.

## Mathlib

Full coverage of this exact quotient limit has not been checked.
No absence claim is made. The proof uses the standard Cauchy integral
formula and its derivative-convergence consequence, local analytic
inversion/Lagrange--Bürmann coefficient inversion, geometric and
alternating Taylor series, and a finite exact interval certificate.
Matching supporting Mathlib theorem names have not been checked.
The underlying polynomial limit remains the precisely cited JKM
input specialized and audited in L715. No formal verification of the
new argument or its certificate is claimed.
