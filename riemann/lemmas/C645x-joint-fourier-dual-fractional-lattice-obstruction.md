# Corollary 645x: fractional lattice obstruction to the proposed joint Fourier dual

## Hypotheses

Fix an integer n>=400, x=-5/4, R=11/8, U=R^2, eta=1/100,
t_j=j/n and u=i exp(i theta), with |u|=1. Retain C645g's normalized
circle measures and the exact rotated product from C645o:

    B_u(a)=product_(j=0)^(n-1) R*(a-t_j*u)/(U-t_j*a/u),
    W_a(u)=B_u(x)/B_u(a)
          =(x/a)*product_(j=1)^(n-1)
             [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)],
    Q_a(u,zeta)=W_a(u)/(R*zeta-a).

The conjugated denominator angle is retained through 1/u=conjugate(u).
An allowed unit pole has Re(a)=x and |a|<=R-eta. The original angular
target concerns finite sums q=sum_a r_a Q_a with distinct allowed poles,
x among them, positive integer r_a and M=sum r_a<=n/3.

For this corollary, let Psi have spatial modes only -1 through -(2n+1):

    Psi(u,zeta)=sum_(ell=0)^(2n) psi_ell(u)*zeta^(-ell-1),
    psi_ell in L2 of the normalized angular circle.

There is no restriction on its angular modes. The proposed rectangle
|k|<=2n is therefore included. Write <F,G>=mean_(u,zeta) F*conjugate(G)
and use the associated L2 norm. Suppose this single test satisfies

    Re <Q_x,Psi> >= 1,
    Re <Q_a,Psi> >= -3/(2n) for every allowed a.              (1)

## Conclusion

Put gamma=251/8000. Every such test satisfies

    ||Psi||_2 >= exp(gamma*n)/(8*n*sqrt(2n+1)).                (2)

Since gamma-1/32=1/8000>0, no constant C and onset can make (1)
hold with ||Psi||_2<=C exp(n/32) for all sufficiently large n.
This rules out the nominated uniform unit-pole dual, even allowing
arbitrary angular modes with the same spatial cutoff.

The obstruction uses positive **fractional** residues and more than
n/3 distinct poles. It is not an admissible countersequence for the
original target and does not bound its full angular Hankel norm above.
The arbitrary-family detector, Xi realization and all-degree signs
remain open. A separate conceptual audit on 2 November 2026 verified
the argument without a mathematical correction; its checks appear below.
This is a local method obstruction, not an RH candidate or a claim of
certified originality.

## Proof

### 1. Source scope, normalization and the auxiliary mixture

The unchanged invocation-start
[EXPLORE assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md)
covers this Fourier/residue attempt on the exact target. C645g supplies
the normalized spaces, C645o the displayed angular product, and C645n
the pointwise anchor product estimate used below. C645o's negative-entry
example and C645p's zero-continuation cost are contrasts, not inputs to
the obstruction. A scoped search of these corollaries and the angular
working/ATTEMPTS records found no fractional-lattice dual obstruction;
that is not an exhaustive novelty claim.

Import Fourier orthogonality and Parseval from A. Levitt, *Analyse de
Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and Theorem
1.11/Corollary 1.12, printed pp.6,8 (PDF pp.12,14), as inspected in
the assessment. Dividing measure by 2*pi makes the exponentials unit
vectors. The Hankel convention is that of L. Baratchart, S. Chevillard
and T. Qian, *Minimax principle and lower bounds in H2-rational
approximation*, J. Approx. Theory 206 (2016), 17--47,
[arXiv:1501.01161v2, Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
24 March 2015. No operator norm is treated as a Hilbert norm.

Import the residue theorem and simple-pole rule from R. W. Howell and
J. H. Mathews, *Complex Analysis*, online edition (front matter updated
22 August 2025),
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and the absolute contour-integral bound from
[Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
These sources were inspected in the reused assessment chain. The
finite-product and contour estimates below supply the missing quantitative
cost; they do not reprove these standard theorems.

Set

    N=floor(27*n/50-1/2),       Y=(N+1/2)/n,
    a_j=x+i*j/n,               w_j=exp(-j^2/n),   -N<=j<=N,
    T_n=sum_(j=-N)^N w_j,      q_tilde=sum_(j=-N)^N w_j Q_(a_j).

For n>=100, 53/100<=Y<=27/50, and |j/n|<Y<=27/50. Thus all
a_j are allowed and distinct, because

    (5/4)^2+(27/50)^2=18541/10000 < (273/200)^2=(R-eta)^2.

The central weight is one; every other weight lies strictly between
zero and one. Since exp(-t^2/n) decreases for t>=0,

    T_n <= 1+2*integral_0^infinity exp(-t^2/n) dt
        < 1+4*sqrt(n) <= (81/400)*n < n/3,                 (3)

where the last inequalities use n>=400. For the strict integral bound,
substitute t=s sqrt(n), bound the integral on [0,1] by one, and use
exp(-s^2)<=exp(-s) on [1,infinity), whose integral is less than one.
No Gaussian integral formula or quadrature theorem is needed.

For each fixed n, all W_(a_j) are continuous on the angular circle,
and |a_j|/R<=273/275<1. The spatial geometric series is uniformly
absolutely convergent on both circles. Its first 2n+1 coefficients are

    S_ell(u)=sum_(j=-N)^N w_j W_(a_j)(u)*a_j^ell/R^(ell+1),
                                                       0<=ell<=2n. (4)

We will prove the pointwise bound

    |S_ell(u)| <= 4*n*exp(-gamma*n)                       (5)

uniformly in u and ell. Spatial orthogonality will then give

    ||P_(0:2n)^zeta q_tilde||_2
                  <= 4*n*sqrt(2n+1)*exp(-gamma*n).         (6)

Here P_(0:2n)^zeta retains the spatial modes in Psi. It is not a
projection of an operator norm, and (6) is not a full-symbol upper bound.

### 2. Exact product estimates and their constants

C645n, proof Section 2, (7)--(8), gives the pointwise bound

    max_(|u|=1) |B_u(x)| <= exp(-lambda*n),
    lambda=log(11/10)+(201/80)*log(201/121)-(9/4)*log(9/5)
           >47/1000.                                     (7)

This is the pointwise maximum, not just its angular mean. Its proof
maximizes each disk factor at u=1 and uses the decreasing Riemann sum
of log((U+(5/4)t)/(R*(5/4+t))). The exact logarithm lower bound is
rechecked in the certificate below. No other part of C645n is needed.

For any |u|=1 and |a|>=R, each inverse disk factor has modulus at
most one, including a zero at a pole of B_u. Indeed

    R^2*|a-t*u|^2-|U-t*a/u|^2=(U-t^2)*(|a|^2-U)>=0.

All inverse denominators a-t*u are nonzero in this region. Hence

    |W_a(u)| <= exp(-lambda*n)                 (|a|>=R).  (8)

For 1<r<R and r<=|a|<=R, minimizing a single disk factor over its
angle and then its radius gives

    |R*(a-t*u)/(U-t*a/u)| >= R*(r-t)/(U-r*t),   0<=t<1.  (9)

To check the minimization, at radius s<R its squared modulus is
U*(s^2+t^2-2*s*t*c)/(U^2+s^2*t^2-2*U*s*t*c), where c is the
relative-angle cosine. For t>0 its derivative in c has sign
-(U-s^2)*(U-t^2), so the minimum occurs at c=1; for t=0 the factor
is angle-independent and the same bound holds. The resulting
(s-t)/(U-s*t) increases in s, since its derivative is
(U-t^2)/(U-s*t)^2>0. At s=R every factor has modulus one.

Define

    kappa(r)=integral_0^1 log((U-r*t)/(R*(r-t))) dt
      =log(R/r)+((U-r)/r)*log(U/(U-r))-(r-1)*log(r/(r-1)).

The integrand is positive and increasing, with derivative
(U-r^2)/((U-r*t)*(r-t))>0. Its left Riemann sum is at most
n*kappa(r). Combining (7)--(9) therefore gives

    |W_a(u)| <= exp(-(lambda-kappa(r))*n)  (r<=|a|<=R).   (10)

The two radial estimates needed are

    kappa(31/25)<7/25,           kappa(9/8)<3/5.           (11)

For complete reproducible exact arithmetic, write their expressions as

    kappa(31/25)=log(275/248)+(1041/1984)*log(3025/1041)
                                      -(6/25)*log(31/6),
    kappa(9/8)=log(11/9)+(49/72)*log(121/49)-(1/8)*log(9).

For each positive rational q>1 put v=(q-1)/(q+1). The elementary
integrated finite geometric series gives rational bounds

    L(q)=2*sum_(k=0)^63 v^(2k+1)/(2k+1),
    L(q)<log(q)<=L(q)+2*v^129/(129*(1-v^2)).                (12)

Insert lower/upper bounds according to each coefficient's sign. The
resulting outward bounds, with denominator 10^12, are

| Quantity | Lower numerator | Upper numerator |
| --- | ---: | ---: |
| lambda | 47920019461 | 47920019462 |
| kappa(31/25) | 268917978923 | 268917978924 |
| kappa(9/8) | 541219597278 | 541219597279 |

Thus (7) and (11) follow by rational comparison. Script
`scripts/one-sided-hankel/joint-dual-contour-certificate.py` stores
every full series bound and comparison in its sibling JSON. All 20
exact constant/rounding checks pass; the complete `/rounded_value_bounds`,
`/checks` and `/failures` fields were inspected. These arithmetic checks
support the analytic proof below; they are not a sampled contour proof
or an independent audit of it.

### 3. A finite residue rectangle, with all four sides bounded

For fixed u and ell as in (4), let h=1/8 and define

    F_ell(a)=exp(n*(a-x)^2)*W_a(u)*a^ell/R^(ell+1),
    K_n(a)=2*pi*n/(exp(2*pi*n*(a-x))-1).

Let Gamma be the positively oriented rectangle with real coordinates
x-h=-R and x+h=-9/8, and imaginary coordinates -Y and Y. The only
possible a-poles of W_a are 0 and t_j*u, all to the right of Gamma:
Re(t_j*u)>=-t_j>-1. The angular denominators U*u-t_j*x cannot vanish,
since U-t_j*|x|>0. Thus F_ell is holomorphic on and inside Gamma,
uniformly well-defined for every |u|=1.

K_n has simple poles of residue one at x+i*j/n. Exactly -N<=j<=N
lie inside Gamma; none is on its boundary because n*Y=N+1/2.
The residue theorem gives the exact finite identity

    S_ell(u)=(1/(2*pi*i))*integral_Gamma F_ell(a)*K_n(a) da. (13)

No infinite lattice, Poisson summation, limiting contour or quadrature
approximation occurs here. Cancellations of a residue caused by a zero
of F_ell do not affect (13).

On the left vertical side, |K_n|<=4*pi*n. On the right side,

    |K_n| <= 4*pi*n*exp(-pi*n/4).                          (14)

These follow from |exp(2*pi*n*(a-x))|=exp(+-pi*n/4) and
1-exp(-pi*n/4)>=1/2 for n>=100. For the last inequality it suffices
that pi>3 and exp(t)>=1+t. On either horizontal side the exponential's
phase is exp(+-2*pi*i*(N+1/2))=-1, so

    |K_n(a)|=2*pi*n/(1+exp(2*pi*n*(Re(a)-x)))<=2*pi*n.    (15)

Put beta=lambda-h^2. We now bound the product on each side.

**Left vertical side.** Write a=-R+i*y. Then |a|>=R and
|a|^ell/R^ell<=(1+y^2/U)^n<=exp(n*y^2/U). By (8),

    |F_ell(a)| <= R^(-1)*exp(-beta*n)
                           *exp(-(1-1/U)*n*y^2)
               <= R^(-1)*exp(-beta*n),                   (16)

since 1-1/U=57/121>0. This includes the midpoint |a|=R.

**Right vertical side.** Here a=-9/8+i*y, |a|>=9/8 and
|a|^2<=(9/8)^2+(27/50)^2=62289/40000<U. Thus the spatial
factor is at most one. Equations (10)--(11) imply

    |F_ell(a)| <= R^(-1)*exp(-(beta-3/5)*n).

Multiplication by (14) adds rate pi/4>3/4, exceeding 3/5 by
more than 3/20. In particular

    |F_ell(a)*K_n(a)| <= (4*pi*n/R)*exp(-beta*n).          (17)

**Both horizontal sides, inside the disk.** If |a|<=R, their least
possible radius obeys

    |a|^2 >= (9/8)^2+(53/100)^2=61861/40000>(31/25)^2.

Use (10) with r=31/25. The spatial factor is at most one and
Re((a-x)^2)<=(1/8)^2-Y^2. Since Y^2-kappa(31/25)>
(53/100)^2-7/25=9/10000, one obtains

    |F_ell(a)| <= R^(-1)*exp(-beta*n).                    (18)

**Both horizontal sides, outside the disk.** If |a|>=R, use (8),
|a|^2<=U+Y^2 and ell<=2n instead. This gives

    |F_ell(a)| <= R^(-1)*exp(-beta*n)
                            *exp(-(1-1/U)*n*Y^2)
               <= R^(-1)*exp(-beta*n).                   (19)

The cases (18)--(19) cover the whole horizontal sides, including their
circle intersections; no incompatible worst-case radial and spatial
costs have been combined. With (15) their product bound is at most
the right side of (17). Equations (14), (16)--(19) therefore bound
the entire contour product by (4*pi*n/R)*exp(-beta*n).

The perimeter is 4*Y+4*h<=133/50. The absolute contour bound in (13)
now gives

    |S_ell(u)| <= (1064/275)*n*exp(-beta*n)
                <= 4*n*exp(-gamma*n),                    (20)

because beta=lambda-1/64>47/1000-1/64=251/8000=gamma.
Every inequality is uniform in u, ell and n>=400. This proves (5).
All sums in (4) are finite; spatial orthogonality and integration over
the normalized angular circle prove (6) without an operator-valued
Parseval claim or an exchange of uncontrolled limits.

### 4. The dual contradiction and its precise limits

The separate pointwise constraints (1) can be summed against the
positive real weights w_j, although those weights are not admissible
integer residues. Using w_0=1 and (3),

    Re <q_tilde,Psi>
      >= 1-(3/(2n))*(T_n-1) >= 1/2.                      (21)

Psi has only the retained spatial modes, so its pairing with q_tilde
equals its pairing with P_(0:2n)^zeta q_tilde. Cauchy--Schwarz and
(6) prove (2). Dividing (2) by exp(n/32) leaves

    exp(n/8000)/(8*n*sqrt(2n+1)) -> infinity,

so no uniform C can supply the proposed cost. For example the fourth
term of the exponential series already dominates the denominator as
n grows; this does not depend on a numerical onset.

For an actual integer-residue family, (1) together with its census
would have given the same >=1/2 pairing and a lower bound for
||q||_2, hence for the angular root mean square of the largest Hankel
norm by H_q 1=q. The obstruction shows that this particular sufficient
test cannot achieve the required exponent. It leaves tests exploiting
the number of distinct poles or integrality jointly unaddressed.

The auxiliary family has 2*N+1>n/3 distinct poles for n>=400 and
noninteger weights in (0,1) away from x. Moreover (6) controls only
the finite spatial projection. Neither the original census/intensity
constraints nor a full-operator upper bound have been supplied.
This proof therefore yields no admissible countersequence and no
failure of the original angular target. The separate conceptual audit
below verifies precisely this qualified implication.

### 5. Separate conceptual audit, 2 November 2026

The audit checked the complete proof (1)--(21), the exact-constant
generator, C645g's normalized symbol, C645o's rotated product and
C645n's pointwise maximum argument (6)--(8). The ready source comparison
was reused. No stronger theorem, source novelty, full audit of unrelated
claims in C645n/C645o, or Xi implication is asserted.

**Scaling, holomorphy and residues.** Substituting u=i exp(i theta)
gives U-t*a/u=U+i exp(-i theta)*t*a. The j=0 factor of W is x/a,
and Q=W/(R*zeta-a) has coefficient W*a^ell/R^(ell+1); no factor R
is missing. For each fixed n the allowed-pole set and both circles
are compact and avoid the product denominators. The geometric expansion
is uniformly absolutely convergent for that n; a bound independent of n
is unnecessary for its coefficient identity. As a function of a,
W has possible poles only at 0 and t_j*u, with real part greater than
-1. They lie strictly outside the closed rectangle whose right side
is -9/8. Its angular denominators obey |U*u-t_j*x|>=U-t_j*|x|>0.
K_n's denominator derivative at each zero is 2*pi*n, so its residue
is exactly one. The half-integer horizontal height excludes boundary
poles and includes exactly j=-N,...,N. At those points the Gaussian
is exp(-j^2/n). The positive orientation in (13) therefore has the
correct sign and weights. No passage to an infinite contour is used.

**Product estimates.** C645n's single-factor maximum occurs at u=1;
its decreasing positive logarithm gives the upper product bound in
(7) for every n, rather than just asymptotically. Integrating that
logarithm gives the displayed lambda. Expanding both squares verifies
the outside-disk identity in Section 2. A pole of B is merely a zero
of its rational inverse, so it does not invalidate (8). For s<R,
the angle derivative and the radius derivative in (9) have their
asserted signs; at s=R the bound extends continuously. The kappa
integrand increases, so its left Riemann sum is bounded above by its
integral. Direct antiderivatives give the two rational logarithm
expressions in (11); coefficient signs in their enclosures are correct.

**Every boundary case.** On the left side, ell<=2n gives the exact
upper bound (1+y^2/U)^n, absorbed by exp(-n*y^2) since U>1.
On the right side all radii are below R; kappa(9/8)<3/5 is absorbed
by kernel rate pi/4>3/4. Each horizontal side has radius at least
sqrt((9/8)^2+(53/100)^2)>31/25. Within the disk its spatial factor
is at most one and Y^2-kappa(31/25)>9/10000. Outside the disk its
radius is at most sqrt(U+Y^2), and Gaussian damping again absorbs
the spatial factor. These closed cases cover circle intersections
and corners. The kernel's horizontal phase is exactly -1, and its
vertical bounds use 1-exp(-pi*n/4)>=1/2. The perimeter and normalized
residue factor give (4Y+4h)*2/R<=1064/275<4. Thus the uniform rate is
beta>251/8000, including both endpoints ell=0 and ell=2n.

**Finite census and pairing.** Writing
N+1/2=27n/50-e_n gives 0<=e_n<1. Hence Y>27/50-1/n and the stated
lower height holds for n>=100. Also 2N+1>27n/25-2>n/3 for n>=400.
Monotonicity bounds the sum of positive Gaussian weights by
1+4 sqrt(n); after division by n this decreases, with value 81/400
at n=400. This is a mass bound, not a bound on the number of poles.
The central weight is one; all other weights are strictly between
zero and one. The real constraints (1) can therefore be summed to
give (21), even though this mixture is not an original admissible
family. The spatial projection is orthogonal in the product L2 space.
For arbitrary angular L2 coefficients of Psi, its pairing with the
discarded spatial modes is zero; Cauchy--Schwarz applies to the retained
symbol, not to an operator norm. This proves (2). For admissible integer
families the corresponding sufficient detector implication uses
r_x>=1, M<=n/3 and H_q 1=q. Neither implication reverses to give a
full-symbol or full-operator upper bound for the auxiliary mixture.

**Exact replay.** Running
`python3 scripts/one-sided-hankel/joint-dual-contour-certificate.py`
reproduced the original JSON byte for byte, with all 20 checks passing.
Running `python3 scripts/one-sided-hankel/joint-dual-contour-audit.py`
reproduces the additional checks. The audit certificate
`scripts/one-sided-hankel/joint-dual-contour-audit.json` records the
matching SHA256 values, nine independently accumulated 96-term logarithm
enclosures, signed combinations obtained from the analytic antiderivatives,
and all 50 floor classes modulo 50. The recurrence N(n+50)=N(n)+27
explains why those floor cases exhaust all n>=400. Its 20 aggregate
checks pass. The complete selected rounded bounds, checks, floor cases
and empty failure fields were inspected, not just previews. In
particular gamma-1/32=1/8000; the exponential-to-polynomial comparison
in Section 4 is valid without an effective onset. These arithmetic
checks support, but do not substitute for, the analytic audit above.

The method stop is accepted without changing its assertion or direct
mathematical inputs. It rules out the uniform unit-pole constraints
at this spatial cutoff, with arbitrary angular modes. It leaves the
integer-residue angular target and all actual-Xi bridges unresolved.

## Mathlib

Full matching coverage of this fractional-lattice obstruction has not
been checked; no absence claim is made. Fourier orthogonality,
Cauchy--Schwarz, finite-product modulus identities and the residue
theorem are supporting inputs, not a matching theorem for (2) or the
original angular target. The precise sources above supply the standard
analytic inputs; the quantitative specialization is written out here.
