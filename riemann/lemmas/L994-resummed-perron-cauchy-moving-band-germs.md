# Lemma 994: resummed Perron-Cauchy moving-band germs

## Hypotheses

Let Lambda be the actual von Mangoldt function, including all prime
powers. For integers n>=2 and r in {1,2}, put m=n+r and use L985's
exact polynomial and the full-right/excluded-left convention of L989:

    K_m(t)=[L_(m-1)^(2)(t)-1]/(m-1),
    T(f;u,v)=sum_(exp(u)<q<=exp(v)) Lambda(q)*f(log q)/q
                                                     -integral_u^v f(t)dt,
    D_(n,r)=T(K_m;m,2*m)-T(K_m;n,2*n),
    G_r(z)=sum_(n>=2) D_(n,r)*z^n.

Here q ranges over integers, not just primes. No RH, zero simplicity,
rightmost zero, nonresonance, arithmetic separation, zero-height
clearance or infinite-zero exchange is assumed. All Perron height
limits below are symmetric. Set

    rho=1/4, R_0=rho*exp(-2),
    a(w)=1/(1-w), b(w)=a(w)-1, |w|=rho,
    F(s)=-zeta'(s)/zeta(s) for Re(s)>1.

The w circle has positive orientation. Define analytic functions on
|v|<1 by the logarithm with log(1)=0:

    S_1(v)=-log(1-v)-v,
    S_2(v)=[-log(1-v)-v-v^2/2]/v, S_2(0)=0,
    H_r(w,s,z)=w^(-r)*[(exp(2*r*s)-1)*S_r(z*exp(2*s)/w)
                       -(exp(r*s)-1)*S_r(z*exp(s)/w)].             (1)

In the uses below both S arguments have modulus less than one.
For real x>=1, set

    j_m(x)=Lambda(x)*K_m(log x)/(2*x) if x is an integer,
           0 otherwise.

Lambda vanishes at integers that are not prime powers. Keep the four
jumps explicitly, without using transcendence to remove them:

    J_r(z)=sum_(n>=2) z^n*[j_m(exp(2*m))-j_m(exp(m))
                           -j_m(exp(2*n))+j_m(exp(n))].           (2)

## Conclusion

The actual series G_r converges absolutely and locally uniformly on
|z|<exp(-1). On the smaller explicit disk |z|<R_0 it has the
degree-resummed representation

    G_r(z)=lim_(H->infinity) I_(r,H)(z)+J_r(z)-C_r(z),             (3)

where H>=1,

    I_(r,H)(z)=1/(2*pi*i)^2 * integral_(|w|=rho) dw
      * integral_(1-i*H)^(1+i*H)
        H_r(w,s,z)/s * [(1-w)^(-3)*F(s+a(w))
                                  -(1-w)^(-1)*F(s+1)] ds,       (4)

    C_r(z)=1/(2*pi*i)*integral_(|w|=rho)
               (1-w)^(-3)*H_r(w,-b(w),z)/(-b(w)) dw
                                                   -r*S_r(z).   (5)

C_r is exactly the degree sum of the two continuum-integral
differences in D_(n,r), with no discarded density or constant term.
The limit in (3) is locally uniform. Equations (10)-(13) below give
the complete finite-height remainder, including near arithmetic
endpoints, and a summable bound uniform in height. Absolute
convergence of the infinite vertical contour is not asserted.

Step282, 10 November2026: REPRODUCTION under the pre-existing,
separately approved SPECIALIZE assessment review280. This constructs
a local analytic interface using known tools, not a new prime bound
beyond the checked sources, a zero-singularity theorem or an RH
candidate. The independent step284 audit below verifies this scope. No contour has
been shifted and no all-zero representation is claimed. The L993
inverse, actual signed outputs, both complements and L984(H) remain
unpaid; L030-L032/C032a and L966/L968 remain open.

## Proof

### Imported tools and the common line

Import the Laguerre generating function
[NIST DLMF18.12.13](https://dlmf.nist.gov/18.12.E13):

    sum_(d>=0) L_d^(2)(t)*w^d=(1-w)^(-3)*exp(-b(w)*t), |w|<1.

Cauchy's coefficient formula therefore gives, for fixed t>=0,

    K_m(t)=1/(m-1)*1/(2*pi*i)*integral_(|w|=rho) w^(-m)
              *[(1-w)^(-3)*exp(-b(w)*t)-(1-w)^(-1)] dw.           (6)

The second factor has coefficient one in every nonnegative degree;
it retains the exact -1, also at the smallest m used here. L985
supplies the identification with the original averaged polynomial.
The global inequality [DLMF18.14.8](https://dlmf.nist.gov/18.14.E8),
for real t>=0, alpha>=0 and integral degree>=0, gives
exp(-t/2)|L_(m-1)^(2)(t)|<=m*(m+1)/2. With the constant subtraction,
L989's already justified normalization yields

    |K_m(t)|<=2*m*exp(t/2), m>=2, t>=0.                         (7)

Import H.L. Montgomery and R.C. Vaughan, *Multiplicative Number
Theory I: Classical Theory*, Cambridge2007, section5.1, Theorems5.1-5.2
and Corollary5.3, printed pp137-140, especially Corollary5.3 and
its near/far/endpoint proof cases, in the
[author-hosted primary chapter](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/09.0_pp_137_167_Dirichlet_series_II.pdf#page=2).
Use the complex-coefficient version: for alpha(s)=sum a_q*q^(-s),
c>max(0,sigma_a), x>0 and H>=1, the vertical integral of
alpha(s)*x^s/s equals the midpoint prefix plus an error bounded by
a constant (at fixed c) times

    sum_(x/2<q<2*x,q!=x) |a_q|*min(1,x/(H*|x-q|))
                  +(4^c+x^c)/H *sum_(q>=1) |a_q|/q^c.           (8)

Equality q=x is excluded from the near sum. Its finite-height cost
is covered by the far majorant in (8); the limiting prefix has
weight one half there. These are the inspected contracts in review279,
with direct-source approval in review280. Import the general theorem
and generating-function proofs; only the joint specialization is new
to this local argument. The standard Dirichlet-series identity
F(s)=sum_(q>=2) Lambda(q)*q^(-s) is used only for Re(s)>1.

On |w|=rho, the extrema of Re(1/(1-w)) are 1/(1+rho) and
1/(1-rho). For example, writing w=rho*exp(i*theta) makes its real
part (1-rho*cos theta)/(1-2*rho*cos theta+rho^2), an increasing
function of cos theta. Thus 4/5<=Re(a(w))<=4/3. For coefficients
a_q(w)=Lambda(q)*q^(-a(w)), the absolute abscissa is at most1/5,
so the common line c=1 is admissible. On that line the series is
F(s+a(w)); the constant branch uses Lambda(q)/q and F(s+1).
Both satisfy the common finite majorant

    M=sum_(q>=2) log(q)/q^(9/5)<infinity.                        (9)

Convergence follows from the integral test. In particular both zeta
arguments stay in their absolute-convergence half-plane, uniformly
in w and in the imaginary part of s. No meromorphic continuation
or information about zeros is used.

### Full finite-height error and exact jumps

For x>=exp(2), define the real nonnegative error majorant

    E(x,H)=sum_(x/2<q<2*x,q!=x) log(q)*q^(-4/5)
                                  *min(1,x/(H*|x-q|))
                                      +(4+x)*M/H.              (10)

This bounds (8) for both coefficient families, uniformly in w,
with a single constant C_MV for c=1. For fixed x the near sum is
finite, all its denominators are nonzero, and each term tends to
zero. Therefore E(x,H)->0. No lower bound on |x-q| uniform in x
has been used, including when x itself is a prime power.

Let A_m(x)=sum_(q<=x) Lambda(q)*K_m(log q)/q, with full weight,
and A_m^*(x)=A_m(x)-j_m(x). Apply (6) to these finite prefixes.
For each w, replace the midpoint complex prefix by its finite
Perron integral, using (8). The resulting polynomial prefix is

    P_(m,H)(x)=1/(m-1)*1/(2*pi*i)^2 *integral_(|w|=rho) w^(-m) dw
      *integral_(1-i*H)^(1+i*H) x^s/s
                  *[(1-w)^(-3)*F(s+a(w))-(1-w)^(-1)*F(s+1)] ds.

The midpoint correction in this Cauchy extraction is exactly j_m(x)
by (6). Consequently

    A_m(x)=P_(m,H)(x)+j_m(x)+R_(m,H)(x),
    |R_(m,H)(x)|<=A_0*rho^(1-m)/(m-1)*E(x,H),
    A_0=(100/27)*C_MV.                                         (11)

Indeed the contour length divided by 2*pi is rho, while
|(1-w)^(-3)|+|(1-w)^(-1)|<=64/27+4/3=100/27.
The remainder is defined by this exact equality, irrespective of
which error-sign convention is used in the source.

For D_(n,r) the prefix signs, in order, are + at exp(2m), - at
exp(m), - at exp(2n), + at exp(n). This is precisely
(exp(m),exp(2m)] minus (exp(n),exp(2n)], even if an endpoint is
shared. Applying (11) with these signs gives all four terms of
(2). There is no extra full-weight correction at a left endpoint:
subtracting the full prefix there implements its exclusion.

### Absolute degree convergence and the summed kernel

By (7), each arithmetic interval, in absolute value, is at most

    2*m*sum_(2<=q<=exp(2*m)) Lambda(q)/sqrt(q)
       <=4*m^2*sum_(1<=q<=exp(2*m)) q^(-1/2)<=8*m^2*exp(m).

Here Lambda(q)<=log q<=2m and sum_(q<=X)q^(-1/2)<=2*sqrt(X).
Each continuum integral is at most
integral_0^(2m)2*m*exp(t/2)dt<=4*m*exp(m). Hence

    |D_(n,r)|<=(16*m^2+8*m)*exp(m).

This proves the claimed convergence of the actual G_r for
|z|<exp(-1), without a signed saving. Also, if x=exp(t) is an
integer, (7) gives |j_m(exp(t))|<=m*t*exp(-t/2). At the four
endpoints n<=t<=2m, their total absolute value is at most
8*m^2*exp(-n/2). Thus (2) is locally normally convergent even on
|z|<exp(1/2). It is retained exactly, whether or not jumps vanish.

Start the contour calculation with finitely many degrees and finite
H. All coefficient, arithmetic and vertical integrals then have
the stated finite or absolutely convergent meanings. The elementary
logarithmic series give, for r=1,2,

    S_r(v)=sum_(n>=2) v^n/(n+r-1), |v|<1.

On Re(s)=1 and |z|<=R<R_0, both |z*exp(j*s)/w|<=R*exp(2)/rho<1,
j=1,2. Consequently the sum of the four prefix factors is uniformly
absolutely convergent on the finite contours and equals

    sum_(n>=2) z^n*w^(-n-r)/(n+r-1)
           *[exp(2*(n+r)*s)-exp((n+r)*s)-exp(2*n*s)+exp(n*s)]
      =H_r(w,s,z).

This proves (4) after taking the finite-degree limit at fixed H.
The logarithms in (1), rather than an unevaluated degree series,
are the resulting kernel. The denominators are n for r=1 and
n+1 for r=2; in particular the n=2 terms have denominators2 and3.
Bounds from (9) and finite contour length justify this limit and
holomorphy of every I_(r,H) on |z|<R_0.

### Continuum compensator, including the constant subtraction

In the exponential branch of (6), integration from u to v gives
[exp(-b(w)*v)-exp(-b(w)*u)]/(-b(w)). On the w circle b(w)!=0,
so this division is legitimate. Moreover Re(-b(w))<=1/5. On
|z|<=R<R_0 the two series arguments at s=-b(w) have modulus at
most R*exp(2/5)/rho<1. Thus finite-degree integration and then
uniform geometric domination justify summing this branch, yielding
the contour term in (5).

The constant branch of K_m is exactly -1/(m-1). The difference
between the two interval lengths is m-n=r. Its entire contribution
to the continuum difference is therefore -r/(n+r-1), and summing
gives -r*S_r(z). This proves (5), with its sign. Equivalently,
partial_s H_r(w,0,z)=r*w^(-r)*S_r(z/w); Cauchy extraction of
(1-w)^(-1) gives the same term. The full expression C_r, not just
the exponential branch, is subtracted in (3).

### Locally uniform height limit, including arbitrarily near endpoints

After the degree limit at fixed H, (11) gives the exact error
Q_(r,H)(z)=G_r(z)-I_(r,H)(z)-J_r(z)+C_r(z). On |z|<=R<R_0,

    |Q_(r,H)(z)|<=A_0*sum_(n>=2)
       R^n*rho^(1-n-r)/(n+r-1)
         *[E(exp(2*m),H)+E(exp(m),H)
                              +E(exp(2*n),H)+E(exp(n),H)].      (12)

Here the order of limits is finite degree, then infinite degree at
fixed height, then height to infinity. To justify all remainder
series and this last limit, first bound the near sum in (10).
There are at most2x positive integers in (x/2,2x) when x>=exp(2).
Each has log(q)<=log(2x) and q^(-4/5)<=(x/2)^(-4/5). Hence

    E(x,H)<=2^(9/5)*x^(1/5)*log(2x)+(4+x)*M/H.

For H>=1 and each of the four x, x<=exp(2m). With

    B=2^(9/5)*(2+log 2)+5*M,

the right side is at most B*m*exp(2m): use
log(2x)<=2m+log2<=(2+log2)*m and 4+x<=5*exp(2m).
Since m/(m-1)<=2, the nth summand of (12) is at most

    C_r^err*q_R^n,
    q_R=R*exp(2)/rho<1,
    C_r^err=8*A_0*B*rho^(1-r)*exp(2*r).                       (13)

In particular its tail n>N is bounded by
C_r^err*q_R^(N+1)/(1-q_R), independently of H. For fixed N all
remaining E(x,H) tend to zero by the finite-sum argument after
(10). Choose N to make the displayed tail arbitrarily small,
then H to control this finite head. This proves uniform convergence
Q_(r,H)->0 on |z|<=R, including the exact arithmetic endpoint case.
It also proves convergence of every error series used in passing
to infinite degree at fixed H. No inverse-separation estimate was
hidden in the tail. This establishes (3) and its claimed holomorphy.

The vertical integral was never bounded absolutely as H->infinity;
a crude integrand bound would only give an integral of order log H.
It is the imported truncated Perron error, followed by (12)-(13),
that proves this particular symmetric, locally uniform limit.
There is no identification of H with a closed spectral cutoff.
All four jumps, the -1 branch and the continuum density remain.
Continuation to a zero-sensitive boundary, crossed residues and
cancellation with any remaining contour require further work.

### Independent conceptual audit — step284, 10 November 2026

Under the separately approved SPECIALIZE review282, reconstruct the
identity before passing to either infinite limit. This verifies the
existing statement by REPRODUCTION; it strengthens no bound and
introduces no new zero or sign hypothesis. Only L985's exact finite
kernel identity and L989's global normalization and full-endpoint
convention are used from those lemmas. Their other claims, including
Vaughan estimates and finite spectral cutoffs, are not premises here.

For N>=2 define G_(r,N), J_(r,N), and C_(r,N) by restricting their
degree sums to 2<=n<=N. In C_(r,N) use the defining continuum
difference integral_m^(2m)K_m(t)dt-integral_n^(2n)K_m(t)dt.
Let I_(r,H,N) be (4) with H_r replaced by its finite degree sum.
Applying (11) separately to each full prefix gives exactly

    G_(r,N)=I_(r,H,N)+J_(r,N)-C_(r,N)+Q_(r,H,N),
    Q_(r,H,N)=sum_(n=2)^N z^n*
      [R_(m,H)(exp(2m))-R_(m,H)(exp(m))
                 -R_(m,H)(exp(2n))+R_(m,H)(exp(n))].           (14)

All four R terms use the same m=n+r. In particular the last two
prefixes use K_m, not K_n. Formula (14) fixes the sign of the full
error and of the continuum subtraction independently of the source's
error notation. A shared endpoint cancels algebraically with its
displayed multiplicity; it is not assigned another endpoint rule.

For the common-line step, the Cauchy numerator in (6), after division
by q, is exactly

    (1-w)^(-3)*q^(-a(w))-(1-w)^(-1)*q^(-1).

Thus it produces the two claimed Dirichlet series. The uniform margin
Re(s+a(w))>=9/5>1 and Re(s+1)=2 permits their use on every finite
height segment, with majorant M. The source proof of Theorem5.2 and
Corollary5.3 on printed pp139-140 was checked at the cited primary
URL: it estimates scalar inversion errors before summing |a_q|.
Consequently its constant at c=1 does not depend on w, the imaginary
coefficient phases, x or H. Its two strict near ranges exclude q=x,
and the remaining O term retains that coefficient. In (10) the
q=x contribution to (4+x)*sum |a_q|/q divided by H is at least
|a_x|/H. Keeping this far majorant therefore pays the equality case;
removing equality from the near sum does not discard its error.

The coefficient extraction uses w^(-m), not w^(-m-1), since the
Laguerre degree is m-1. Its denominator is m-1=n+r-1. Specifically
S_1(v)=v^2/2+v^3/3+... and S_2(v)=v^2/3+v^3/4+... . These verify
the smallest degree for both r. The branch log(1)=0 on |v|<1 and
the removable value of S_2 give single-valued holomorphic kernels;
their arguments on the finite contours stay strictly in that disk.

The continuum branch is the integral of exp(-b*t); its four endpoint
numerators give H_r(w,-b,z)/(-b). On this circle
|b|=|w/(1-w)|>=1/5, and Re(-b)<=1/5. There is no singular division
or unlicensed logarithmic branch in (5). The other branch contributes
-(m-n)/(m-1)=-r/(n+r-1) at each degree. Therefore C_(r,N) tends to
the whole C_r in (5), including -r*S_r(z), and (14) subtracts it.

For the uniform remainder, an interval (x/2,2x) has at most
(3/2)*x+1<=2x integers for x>=exp(2). Replacing the minimum in
(10) by one gives its stated near bound. For all four endpoints,
x<=exp(2m), so E(x,H)<=B*m*exp(2m), H>=1. The contour-length
factor is rho, and 64/27+4/3=100/27. Substitution into (11) yields
for the nth contribution to (14), uniformly on |z|<=R<R_0,

    R^n*4*A_0*rho^(1-n-r)*B*m*exp(2m)/(m-1)
      <=8*A_0*B*rho^(1-r)*exp(2r)*(R*exp(2)/rho)^n.

This recovers every factor in (13). Its geometric tail is independent
of H, including arbitrarily close non-equal prime-power endpoints.
For a fixed finite set of degrees, each near sum is finite and every
non-equal denominator is nonzero. Its terms tend to zero as H grows;
the far term also tends to zero. Hence no uniform separation in n
has entered the finite-head argument.

Finally, (7) gives the already stated absolute bounds for G and J
and for the degree sum defining C. At each fixed finite H the finite
kernel sum converges uniformly on the compact product of contours,
since R*exp(2)/rho<1 and M is finite. Thus every term of (14) has a
locally uniform N-limit, giving precisely the Q identity before (12).
Given epsilon>0, choose N so that the displayed geometric tail is
less than epsilon/2, for every H>=1. For this N choose H_0 so that
the finite sum of error bounds is less than epsilon/2 for all H>=H_0.
This proves Q_(r,H)->0 uniformly on the closed disk. Every I_(r,H)
is holomorphic there, and the resulting limit agrees with G_r-J_r+C_r.
No bound uniform in H for an absolutely integrated vertical contour
is needed or asserted. In particular this reasoning does not shift
that contour or allow extraction of an infinite family of residues.

Audit verdict: equations (3)-(13), including both radii, all four
jumps, the exact continuum term and the locally uniform symmetric
height limit, pass without a mathematical repair. Formula (14) makes
the pre-limit reconstruction explicit; it changes no conclusion.
This establishes a reliable local input, not progress beyond the
checked source tools, an RH bound, or a zero-singularity theorem.
The existing direct mathematical inputs in the DAG remain correct.

## Mathlib

Full matching Mathlib coverage of this degree-resummed moving-band
representation and its locally uniform Perron limit is unchecked
and unknown. The source contracts and the argument above are an
informal proof, not a formal certificate or evidence of absent
library coverage. Cauchy extraction and dominated/geometric
convergence alone would not supply an omitted arithmetic error.
