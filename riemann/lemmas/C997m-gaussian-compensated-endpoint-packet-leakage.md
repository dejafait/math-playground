# Corollary 997m: compensated endpoint packets retain the target, but strong tapers leak

## Hypotheses

Use C997c(1)'s COMPLETE response, for integer n>=2:

    K_(n+2)(t)=(L_(n+1)^(2)(t)-1)/(n+1),
    g_n(t)=K_(n+2)(t)*exp(-t/2)*cosh(3t/8),
    H_n^+(z;mu)=-2*integral_I exp(-cn/4)*[
      integral_(cn)^(c(n+2)) g_n(t)*exp(izt)dt
      -integral_n^(n+2) g_n(t)*exp(izt)dt]dmu(c).

Put I=[7/4,9/4], J=[15/8,17/8], delta=1/8, z_star=1+i/8,
and use C997e's real phase and its local holomorphic extension:

    phi(c)=arccos(1-c/2)+sqrt(c*(4-c))/2,
    phi'(c)=(1/2)*sqrt((4-c)/c)>1/3 on J.

Fix theta>0, lambda>0 and A>=A_0 before n, with A_0>=16 the
existential threshold in C997e. No numerical admissible A is presumed.
For x=c-2 define

    q_n=floor(theta*n), r_n=floor(lambda*n),
    E_r(u)=sum_(j=0)^r u^j/j!,
    b_n(x)=(1-64*x^2)^q_n,
    w_n(x)=b_n(x)*exp(-An*x^2)*E_(r_n)(An*x^2),
    P_n(c)=b_n(c-2)*E_(r_n)(An*(c-2)^2),
    M_n=integral_(-delta)^delta w_n(x)dx,
    dmu_n(c)=M_n^(-1)*1_J(c)*w_n(c-2)
                                     *exp(in(phi(c)-c))dc.       (1)

An exponent zero denotes the constant polynomial one, including at
the endpoints. These are hypothetical finite slope measures, not
actual zeta-zero data. Both slope endpoints, both Laguerre branches,
both beta terms, both short intervals and K's -1 remain in H.

## Conclusion

Every measure in (1) has ORIGINAL total variation one. With
kappa=2(theta+lambda), its polynomial has degree exactly
2(q_n+r_n)<=floor(kappa*n). For EVERY fixed parameter choice above,

    sqrt(n)*M_n -> sqrt(pi/(64*theta)),
    H_n^+(z_star;mu_n)=n^(-3/2)*(B_star+o(1)),
    B_star=-(exp(1+2i)-1)/(4*sqrt(pi)*(1/4+i/2)) != 0.          (2)

Thus this family retains the target at size exp(-o(n)) through all
sufficiently large integers, not just a subsequence.

There exists a finite Theta_0>=16, depending only on C997e's fixed
analytic amplitudes and their neighborhood, such that if additionally

    theta>=Theta_0 and lambda>=A,                            (3)

then the data point 2 leaks at a positive exponential rate. More
precisely put beta=1/8+i, t_n=q_n/n and, for real t sufficiently large,

    s_t=delta^2*beta/(t+sqrt(t^2+delta^2*beta^2)),
    Phi_t(z)=t*log(1-z^2/delta^2)+beta*(2+z),
    S_t=Phi_t(s_t).                                         (4)

The square root has positive real part, and the logarithm is the
analytic germ with log(1)=0 near z=0. There is a nonzero D_theta with

    H_n^+(2;mu_n)=n^(-3/2)*exp(n*S_(t_n))*(D_theta+o(1)),
    lim_(n->infinity) log|H_n^+(2;mu_n)|/n
                        =Re(S_theta)>=29/128>0.             (5)

Consequently (3) cannot give uniform exp(-sigma*n) suppression on
the CLOSED J for any sigma>0, on any unbounded integer subsequence.
This is a stop only for the strong-taper, lambda>=A regime (3).
Smaller theta and lambda<A remain undecided. Theta_0 and the onsets
are existential; no varying-parameter uniformity is asserted.
The stopped regime is nonempty: choose any fixed A>=A_0, lambda=A
and theta>=Theta_0, all before n.

Step347, 11 November 2026: RESEARCH / POTENTIALLY_NEW, outcome NEGATIVE,
under the unchanged pre-invocation EXPLORE assessment345. This is a
local packet specialization using known analytic tools; the checked
sources did not identify its exact complete-response statement.
POTENTIALLY_NEW is not a certification of originality. The proof was
unaudited at step347; the independent conceptual audit in step349 below
accepts (1)-(21) without changing their hypotheses or bounds. No actual-Xi
positivity, signed forcing, RH candidate or family-wide obstruction is
claimed.

## Proof

### Reused contracts and the purpose of the specialization

Use the audited exact analytic amplitudes in C997e(4),(15)-(16).
Their source is M. Vanlessen, *Strong asymptotics of Laguerre-type
orthogonal polynomials and applications in random matrix theory*,
[math/0504604v2](https://arxiv.org/pdf/math/0504604v2), Theorem2.4(b),
Proposition3.31, Theorem3.32 and Proposition5.1/(5.5)-(5.6), with
the normalization and domain specialization already proved in C997e.
No general Laguerre asymptotic is reproved or analytically continued
from a real-axis O term here. C997c supplies the exact finite spectral
measures and their complete lower-interval variation bound.

For the finite exponential use NIST DLMF version1.2.8, released
15 September 2026, [8.4.7-11](https://dlmf.nist.gov/8.4#E7) and
[8.2.1](https://dlmf.nist.gov/8.2#E1). For integer r>=0 and real u>=0,
these give exactly

    Q_r(u):=exp(-u)*E_r(u),
    1-Q_r(u)=1/r!*integral_0^u v^r*exp(-v)dv.              (6)

The integer shape r+1 satisfies Re(r+1)>0, and this finite real
integral has no path qualification to resolve. The exponential series
in [DLMF1.10.2](https://dlmf.nist.gov/1.10#E2), dominated convergence,
Cauchy's integral theorem, the identity theorem, the real Gaussian
integral and ordinary integration by parts are used in their standard
named forms. Reviews329/332/344/345 supply the inspected contracts.

The new work is the original-TV normalization, the charged replacement
of Q_r on the REAL data integral, and the floor-dependent endpoint
phase calculation. A plain Bessel transform or Gaussian approximation
does not account for its nonconstant exact amplitudes and complete
response, so those are not substituted for this calculation.

### Positive weight, exact degree and original normalization

Equation (6), or direct differentiation of the finite sum, gives

    0<Q_r(u)<=1, Q_r(0)=1,
    Q_r'(u)=-exp(-u)*u^r/r!<=0, u>=0.                     (7)

For each n, w_n is nonnegative on [-delta,delta], continuous and
positive in its interior. Hence 0<M_n<infinity. The phase in (1) is
real on J, so its modulus is one and the original TV is exactly one.
The two factors of P_n have nonzero leading coefficients of degrees
2q_n and 2r_n. Their product has exactly the stated degree, including
zero-degree cases; its integer degree is <=floor(2(theta+lambda)n).

Extend the rescaled weight by zero outside |y|<=delta*sqrt(n). Then

    sqrt(n)*M_n=integral_R 1_(|y|<=delta*sqrt(n))
       *(1-64*y^2/n)^q_n*Q_(r_n)(A*y^2)dy.                (8)

For fixed y, r_n tends to infinity, so the exponential series gives
Q_(r_n)(A*y^2)->1; the other factor tends to exp(-64*theta*y^2).
For all sufficiently large n, q_n/n>=theta/2, and (7) and
log(1-v)<=-v for 0<=v<1 bound the integrand by
exp(-32*theta*y^2). At the endpoints q_n>=1 and the integrand is zero.
Dominated convergence and the Gaussian integral prove the first
limit in (2). The same proof without Q gives

    N_n:=integral_(-delta)^delta b_n(x)dx
                         ~sqrt(pi/(64*theta*n)).           (9)

The normalized w_n also concentrate at x=0. This follows either
from (8) or by bounding their mass outside any fixed |x|<epsilon
using b_n(x)<=exp(-64*q_n*epsilon^2), then dividing by M_n.
For q_n>=1 the weight is even, decreases on [0,delta], has w_n(0)=1
and vanishes at both endpoints. It is continuously differentiable,
and therefore

    integral_(-delta)^delta |w_n'(x)|dx=2.                 (10)

### Exact complete-response reduction

Write B_(+/-,n)(c,u) for C997e's exact holomorphic amplitudes. On
one fixed neighborhood U of J they and their c derivatives are
uniformly bounded, for real 0<=u<=2 and all sufficiently large n.
They converge uniformly on smaller neighborhoods as specified there.
For z in {z_star,2} set

    a_(z,+/-,n)(c)=-c*integral_0^2
                         exp(c*u*(3/8+iz))*B_(+/-,n)(c,u)du,
    beta_z=1/8+i*(z-1).

These are uniformly bounded holomorphic functions, with uniformly
bounded first derivatives on a smaller U and uniform limits a_(z,+/-).
In particular, with b_-(c) as in C997e,

    d_z(c)=3/8+iz-i*phi'(c),
    a_(z,-)(c)=-b_-(c)*(exp(2*c*d_z(c))-1)/d_z(c),          (11)

using the removable value if d_z(c)=0. Direct substitution into the
positive-beta upper Laguerre term gives the EXACT identity

    H_n^+(z;mu_n)=n^(-3/2)*M_n^(-1)*(I_(z,-,n)+I_(z,+,n))
                                                      +Rem_(n,z),
    I_(z,-,n)=integral_J w_n(c-2)*exp(n*beta_z*c)
                                                   *a_(z,-,n)(c)dc,
    I_(z,+,n)=integral_J w_n(c-2)*exp(n*beta_z*c+2in*phi(c))
                                                   *a_(z,+,n)(c)dc,
    |Rem_(n,z)|<=C*(n+2)*exp(-n/16).                      (12)

For completeness, -2 times the positive term of cosh contributes -1,
and t=c(n+u) has Jacobian c. Combining exp(-cn/4), the Laguerre
exp(t/2), exp((-1/8+iz)t) and the measure phase gives precisely
beta_z and the two phases in (12). The reflected-beta upper Laguerre
term has absolute exponent at most -cn/4-3t/8 after the real Laguerre
bound in C997e; the entire K subtraction has exponent at most
-cn/4-t/8. Their intervals have length 2c<=9/2. The complete lower
interval is bounded by C997c(5), at most
8*exp(3/4)*(n+2)*exp(-n/16) times the original TV. At z_star its
additional exp(-t/8) improves these bounds. These estimates use the
original TV=1, so the growing polynomial has not been omitted from a
remainder estimate. All integrations are over compact sets with finite
variation. Both beta signs, both intervals and -1 are accounted for.

### Target retention for all fixed positive parameters

Here beta_(z_star)=0. Concentration and uniform amplitude convergence
give I_(z_star,-,n)/M_n -> a_(z_star,-)(2)=B_star. Formula (11),
b_-(2)=1/(4*sqrt(pi)) and d_(z_star)(2)=1/4+i/2 give (2)'s explicit
constant; it is nonzero because |exp(1+2i)|=e>1.

For the other branch put f_n(c)=a_(z_star,+,n)(c)/(2i*phi'(c)).
Its value and derivative are uniformly bounded on J. Integration
by parts, with both boundary values zero for q_n>=1, yields

    I_(z_star,+,n)=-1/n*integral_J
       [w_n'(c-2)*f_n(c)+w_n(c-2)*f_n'(c)]*exp(2in*phi(c))dc.

Equations (7),(10) bound this by C/n. Dividing by M_n=Theta(n^(-1/2))
gives O(n^(-1/2)), hence zero in the limit. The remainder in (12),
multiplied by n^(3/2), also tends to zero. This proves the second
limit in (2). Eventually |H_n^+(z_star)|>=(|B_star|/2)*n^(-3/2);
take a_n=max{0,(3/2)*log n+log(2/|B_star|)} for the required
nonnegative sublinear exponent.

### Pay compensation on the real interval before any deformation

Assume lambda>=A. Let k=r_n+1>lambda*n. Equation (6) gives
1-Q_(r_n)(u)<=u^k/k!. The elementary bound
log(k!)>=integral_1^k log(v)dv>=k*log k-k implies k!>=(k/e)^k.
For 0<=u<=An/64, using e<4,

    0<=1-Q_(r_n)(u)<=(e*u/k)^k
                  <=16^(-k)<=exp(-2*lambda*n).             (13)

The last inequality uses log16>2. Thus |w_n-b_n|<=b_n*exp(-2*lambda*n)
on the REAL interval. It follows also that
|M_n-N_n|<=2*delta*exp(-2*lambda*n).

At z=2, |exp(n*beta*c)|<=exp(17n/64) and the extra real-axis phase
exp(2in*phi(c)) has modulus one. Uniform boundedness of both exact
amplitudes therefore bounds the error in EACH integral of (12), on
replacing w_n by b_n, by

    C*exp(-(2*lambda-17/64)*n).                            (14)

Since lambda>=A>=A_0>=16, this has a strictly negative exponent,
even before comparison with the growing contribution below. Division
by M_n adds only a polynomial factor. No approximation to Q_r on a
complex path is used: (14) is paid before the replacement integral is
deformed. This is why real-axis compensation is sufficient in regime (3).

### A charged saddle for the endpoint factor

Shrink U and fix h>0 so a neighborhood of
2-delta<=Re(c)<=2+delta, 0<=Im(c)<=h lies in U and
Re(phi'(c))>=1/3 there. Vertical integration then gives
Im(phi(x+iy))>=y/3 for real x in J and 0<=y<=h.
The limiting a_(2,-)(2) is nonzero: in (11), d_2(2)=3/8+3i/2
and |exp(4*d_2(2))|=exp(3/2)>1. Fix a nonvanishing disk about 2.

For t>=8 define s_t as in (4). The radicand has positive real part,
so the chosen square root has positive real part and

    |s_t|<=|beta|*delta^2/t<=1/(32t)<=1/256,
    beta=2t*s_t/(delta^2-s_t^2), Phi_t'(s_t)=0.             (15)

Write s_t=a_t+i*y_t. Taking imaginary parts of the middle identity,

    Im(beta)=2t*y_t*(delta^2+|s_t|^2)/|delta^2-s_t^2|^2=1,

shows y_t>0. Also s_t->0 as t->infinity. Choose a finite T>=8 so
that for ALL t>=T, y_t<h and 2+s_t is in the chosen nonvanishing
disk. Set Theta_0=max{16,T+1}. If theta>=Theta_0 and n>=2 then
t_n>=theta-1/n>=T. All these choices precede n; no admissible
small-A interval or n-dependent parameter is assumed.

For |64*s_t^2|<=1/(16t^2)<=1/1024, the convergent logarithm series
gives |log(1-64*s_t^2)|<=128*|s_t|^2. Consequently

    |S_t-2*beta|<=3/(16t), Re(S_t)>=29/128, t>=8.          (16)

For each n deform the two b_n replacement integrals from the real
interval to height y_(t_n). The polynomial b_n and both exact
amplitudes are holomorphic on the whole rectangle, as is phi for the
plus branch. Cauchy's theorem retains the horizontal segment AND
both vertical endpoint segments.

On a horizontal outer piece delta/2<=|x|<=delta and
0<=y<=1/256,

    |1-64*(x+iy)^2|
       <=1-64*x^2+128*|x|*y+64*y^2
       <=3/4+1/16+1/1024=833/1024<7/8.                    (17)

At either vertical endpoint x=+/-delta, the sharper bound is
16*y+64*y^2<=65/1024<7/8. On all these pieces,
Re(beta*(2+x+iy))=(2+x)/8-y<=17/64. Thus for t=t_n>=8
the absolute rate of b_n*exp(n*beta*(2+x+iy)) is at most

    17/64+t*log(7/8)<=17/64-t/8<=-47/64.                 (18)

The plus branch only decreases this bound, since Im(phi)>=0.
Segment lengths and amplitude bounds are fixed. Both slope endpoints
and both outer pieces are therefore exponentially negligible.

On the central horizontal segment |x|<=delta/2 use Phi_t from (4).
It is an exact phase there, because q_n=n*t_n is an integer and the
local logarithm exponentiates to the original polynomial. Let
w=(x+iy)/delta and v=w^2. Then |v|<=257/1024<1/3 and

    Phi_t''(x+iy)=-128*t*(1+v)/(1-v)^2.

To check real concavity explicitly, multiply by (1-conj(v))^2.
The numerator's real part is at least
1-|v|-3|v|^2-|v|^3>=8/27, while |1-v|^4<=256/81. Hence
Re((1+v)/(1-v)^2)>=3/32 and Re(Phi_t'')<=-12t.
Since Phi_t'(s_t)=0 and a_t is strictly in the central segment,

    Re(Phi_t(x+i*y_t))<=Re(S_t)-6t*(x-a_t)^2.             (19)

This pays the entire central complex growth of the endpoint polynomial.
It is not a Gaussian replacement of that polynomial on the contour.

### Exact local limit, other branch and floors

In the minus central integral put x=a_(t_n)+v/sqrt(n). The endpoints
tend to opposite infinities. For fixed v, uniform holomorphic Taylor
expansion, t_n->theta and the exact amplitude convergence give

    n*(Phi_(t_n)(s_(t_n)+v/sqrt(n))-S_(t_n))
                          ->Phi_theta''(s_theta)*v^2/2,
    a_(2,-,n)(2+s_(t_n)+v/sqrt(n))->a_(2,-)(2+s_theta).

Equation (19) and t_n bounded below by a positive constant supply an
integrable Gaussian domination on the rescaled line. Dominated
convergence proves that the minus replacement integral is

    exp(n*S_(t_n))*n^(-1/2)*[
      a_(2,-)(2+s_theta)*sqrt(2*pi/(-Phi_theta''(s_theta)))+o(1)]. (20)

The complex Gaussian formula used here follows from the real Gaussian
integral by the holomorphic identity theorem on Re(d)>0 for
integral_R exp(-d*v^2/2)dv; compact subsets are dominated by a real
Gaussian. Here Re(-Phi_theta'')>0 by (19), so the square root has its
unambiguous positive-real-part branch. The leading factor in (20)
is nonzero by the choice of T. Equation (18) pays the parts omitted
from this central calculation.

On the central horizontal segment the plus branch has the additional
factor of modulus <=exp(-2*n*y_(t_n)/3). Since y_(t_n)->y_theta>0,
(19) bounds its integral by
C*n^(-1/2)*exp(n*Re(S_(t_n))-2*n*y_(t_n)/3), which is exponentially
smaller than (20). Its outer and vertical pieces satisfy (18).
The compensation error (14) and the COMPLETE remainder (12) are also
exponentially smaller, using (16). No cancellation between a leading
term and an uncontrolled error has been presumed.

Finally divide (20) by M_n from (2) and insert (12). This proves (5)
with the explicit nonzero coefficient

    D_theta=sqrt(128*theta/(-Phi_theta''(s_theta)))
                                             *a_(2,-)(2+s_theta). (21)

Crucially exp(n*S_(t_n)) was retained throughout: replacing it by
exp(n*S_theta) times 1+o(1) would not follow from t_n->theta and is
not asserted. For the logarithmic rate, continuity suffices:
S_(t_n)->S_theta, log(n)/n->0, and D_theta+o(1) stays bounded away
from zero. Thus the rate in (5) holds through all sufficiently large
integers. The point 2 belongs to the closed J, so its positive rate
alone contradicts the requested uniform negative band rate.

### Scope, overlap and unresolved work

For every fixed theta,lambda>0 the target half of the test is now
proved in (2). The band calculation closes only (3). In particular a
failed contour estimate outside that regime is not an impossibility
statement. No assertion is made for varying theta,lambda or A.

C997i separately excludes the overlap with actual degree 2(q_n+r_n)<=n
and fixed A>=max{A_0,6553600}; its audited result is reused as comparison,
not reproved or used in (2)-(21). If kappa<=1 that degree condition
holds for every n. If kappa>1, the degree exceeds n eventually, since
2(q_n+r_n)>=kappa*n-4. Regime (3) has theta>=16, hence eventual degree
strictly above n; (5) is not just C997i's already excluded overlap.
C997f's different phase and C997g/l's imposed response jets are absent
from this family. Failures340/341's unpaid spectral tail is not invoked.

No general point inequality or counterexample to it follows. The point
bridge, selected/both-sign transfer, C997a(8), original assay and actual
reconstruction, signed recovery, complementary zeros and regulators,
L993, L984(H), and L030-L032/C032a actual-Xi positivity remain unpaid.
There is no cross-notebook mathematical input. The independent step349
audit below verifies this local calculation only on its stated scopes.

### Independent conceptual audit — step349, 11 November 2026

RESEARCH / REPRODUCTION, proof_audit/conceptual_audit, under the unchanged
pre-invocation SPECIALIZE review347 and its exact COVERED_TARGET. The
audit accepts (1)-(21): every fixed positive theta,lambda retains the
target, and only theta>=Theta_0, lambda>=A has the proved data leakage.
This establishes a checked local input, not a stronger theorem or
progress beyond the standard tools compared in that assessment. No
numerical threshold, all-family stop or RH candidate follows.

**Original measure and target limit.** On the real support, b_n>=0 and
0<Q_(r_n)<=1, with strictly positive interior weight. The real phase has
modulus one, so division by M_n gives exactly the original TV=1. The
product's leading coefficient is nonzero, including either degree-zero
case; integer degree 2(q_n+r_n)<=2(theta+lambda)n implies the stated
floor bound. These conclusions hold for every n>=2, independently of
the eventual asymptotics.

For each fixed real y the integrand in (8) tends to
exp(-64*theta*y^2). Extend it by zero to R. For all sufficiently large n,
q_n/n>=theta/2, giving the integrable majorant exp(-32*theta*y^2);
the endpoints are zero because q_n>=1. Thus dominated convergence
applies on the whole line, not just separately on finite intervals.
The same argument with Q=1 proves (9). For 0<epsilon<delta the
normalized mass of |x|>=epsilon is at most
2*delta*exp(-64*q_n*epsilon^2)/M_n, which tends to zero. The weight
is C^1 on the closed original interval, even and decreasing on its
positive half, with values 1 at zero and 0 at its endpoints for q_n>=1.
Consequently its derivative has integral absolute value exactly 2.
No differentiability of the zero extension is required.

C997e(4),(15)-(16) gives exact amplitudes on a fixed complex neighborhood,
with uniform convergence and derivative bounds on smaller neighborhoods.
Finite integration in u preserves these properties in (11). In the
positive-beta upper term, the coefficient from -2*cosh is -1 and
t=c(n+u) has Jacobian c. The remaining exponential is
exp(n*(1/8+iz)*c)*exp(in*(phi(c)-c))*exp(+/-in*phi(c));
it gives exactly beta_z and the two signs in (12). For the other upper
terms the absolute exponents are -cn/4-3t/8 and -cn/4-t/8. Their
lengths are <=9/2, and the original variation is one. C997c(5) pays
the complete lower interval, including both beta terms and K's -1.
At z_star, t>=n gives additional decay. This verifies (12) for the
entire response without dividing its remainder by M_n again.

At z_star the minus integral divided by M_n tends to a_(z_star,-)(2)
by concentration and uniform amplitude convergence. Here
b_-(2)=1/(4*sqrt(pi)), d_(z_star)(2)=1/4+i/2, so the constant in (2)
has exactly the stated sign and factor and cannot vanish. For the plus
integral, phi'>1/3 and its holomorphic derivatives are bounded on J.
Thus f_n and f_n' in the integration by parts are uniformly bounded,
and both boundary terms vanish. Its absolute value is at most
(2*||f_n||_infinity+M_n*||f_n'||_infinity)/n. Division by M_n leaves
O(n^(-1/2)). The complete remainder times n^(3/2) tends to zero.
This proves actual nonzero target retention through all large integers.

**Real compensation charge.** With k=floor(lambda*n)+1>lambda*n,
the exact finite integral (6) gives 1-Q_(r_n)(u)<=u^k/k!.
Integrating the increasing log function gives
log(k!)>=k*log(k)-k+1, hence the factorial bound used in (13).
For u<=An/64 and lambda>=A,
e*u/k<e/64<1/16. Therefore (13) holds uniformly on the entire REAL
interval. Multiplication by b_n, both bounded amplitudes and the data
modulus exp(n*c/8)<=exp(17n/64) gives (14) for each integral.
This is an absolute error before contour deformation. Its later
normalization costs only M_n^(-1)=O(sqrt(n)); no complex bound for Q_r
and no replacement of the compact-support indicator is assumed.

**Saddle branch and fixed domain.** Here
beta^2=-63/64+i/4, so t^2+delta^2*beta^2 has positive real part for
t>=8. Its positive-real-part square root is continuous on this range,
and |t+sqrt(t^2+delta^2*beta^2)|>=t. Since |beta|<=2,
|s_t|<=1/(32t). Rationalizing the definition gives
beta*s_t^2+2t*s_t-beta*delta^2=0; since |s_t|<delta, this is precisely
the saddle identity in (15). Its imaginary part gives y_t>0, with
no choice between two uncontrolled saddle contributions. The other
quadratic root is not used in the deformation.

The fixed strip with Re(phi')>=1/3 follows by continuity on compact J.
The limiting minus amplitude is nonzero at 2 because d_2(2)=3/8+3i/2
and |exp(4*d_2(2))|=exp(3/2)>1. A fixed disk of nonvanishing therefore
exists. The bound s_t->0 supplies one T for ALL t>=T inside that disk
and below the strip height. With Theta_0=max{16,T+1}, the floors obey
t_n>=theta-1/n>=T for n>=2. Thresholds and parameters are fixed before n;
the amplitude identities themselves are required only for all large n.

For |64*s_t^2|<=1/(16t^2)<=1/1024, the log series gives
|log(1-64*s_t^2)|<=128*|s_t|^2. Thus
|S_t-2*beta|<=128*t/(32t)^2+2/(32t)=3/(16t), proving
Re(S_t)>=1/4-3/128=29/128. No numerical admissible Theta_0 is inferred.

**Both endpoints and the central maximum.** Cauchy's theorem applies
to the polynomial b_n and exact amplitudes on a neighborhood of the
whole rectangle; the plus branch's phi is holomorphic there as well.
The shifted horizontal segment has the original orientation, and both
vertical segments must be retained. On its outer pieces,
|1-64*(x+iy)^2|<=3/4+1/16+1/1024=833/1024<7/8.
At EITHER endpoint x=+/-delta the corresponding bound is 65/1024.
The real linear exponent is <=17/64 throughout these pieces, and
log(7/8)<=-1/8. Their rate is consequently <=-47/64 for t>=8.
Vertical integration of phi' gives Im(phi)>=y/3, so the extra plus
phase can only improve these bounds. The endpoint logarithm is never
used: the integer polynomial itself is deformed.

On the central segment, put v=((x+iy)/delta)^2. Then
|v|<=257/1024<1/3, so its local logarithm is valid. The exact identity
exp(n*t_n*log(1-64*z^2))=(1-64*z^2)^q_n holds there.
The real numerator after multiplying (1+v)/(1-v)^2 by
(1-conj(v))^2 is at least 1-|v|-3*|v|^2-|v|^3>=8/27;
the denominator is at most (4/3)^4=256/81. This yields
Re(Phi_t'')<=-128*t*(3/32)=-12t. Since |Re(s_t)|<=1/256<delta/2
and Phi_t'(s_t)=0, integrating twice along that horizontal line gives
(19) on its whole central segment, including both sides of the saddle.

**Whole-line limit and complete-response dominance.** Extend the
rescaled central integrand by zero outside its moving interval.
The rescaled endpoints tend to opposite infinities because
|Re(s_theta)|<delta/2. For fixed real v, the saddle derivative vanishes
exactly and uniform local third-derivative bounds give the Taylor
remainder O_theta(|v|^3/sqrt(n)); t_n stays in a compact interval
about theta. The exact amplitudes converge uniformly at the moving
arguments. After factoring exp(n*S_(t_n)), (19) bounds the whole
rescaled integrand by C*exp(-48*v^2). This is a single integrable
majorant on R, so the complex dominated-convergence theorem proves
(20), including its phase, not merely its modulus.

The precise reused limit input is Sheldon Axler, *Measure, Integration
& Real Analysis*, author version 12 June 2026,
[Theorem3.31, pp92-93](https://measure.axler.net/MIRA.pdf), including
the infinite-measure proof case and the complex-valued extension after
6.22, p157. The complex Gaussian value follows directly from
[NIST DLMF7.7.3](https://dlmf.nist.gov/7.7#E3) at zero linear parameter
and evenness, with quadratic coefficient d/2, d=-Phi_theta''(s_theta).
Here Re(d)>=12*theta>0, satisfying the source hypothesis; the square
root branch agrees with positive real d. This also verifies the
identity-theorem argument in the original proof. The amplitude and
Gaussian factor are nonzero, so (20) has a nonzero leading coefficient.

For clarity, the complete error comparison can be made after division
by n^(-3/2)*exp(n*S_(t_n)). For all sufficiently large n its error
terms, besides the central o(1) and normalization o(1), have bounds

    outer pieces and both vertical segments:
        O(sqrt(n)*exp(-123*n/128));
    real compensation errors in the two integrals:
        O(sqrt(n)*exp(-(2*lambda-5/128)*n));
    central plus branch:
        O(exp(-n*y_theta/3));
    COMPLETE Rem_(n,2):
        O(n^(5/2)*exp(-37*n/128)).

The first two use Re(S_(t_n))>=29/128, the third uses
y_(t_n)>=y_theta/2>0 eventually, and the last includes the original
TV normalization already built into (12). Every exponent decays under
the stated hypotheses, in particular lambda>=A>=16. Hence none can
cancel (20)'s nonzero coefficient. Combining its Gaussian factor with
sqrt(n)*M_n->sqrt(pi/(64*theta)) gives exactly D_theta in (21).
The argument retains exp(n*S_(t_n)); continuity of S alone is used
only after taking log modulus and dividing by n. No unjustified
multiplicative removal of the floors occurs.

Direct mathematical inputs remain C997c and C997e; L997's real bound
and phase enter through those contracts. C997i is only a comparison:
its degree<=n hypothesis does not hold eventually in regime (3).
Both all-parameter retention and the scoped leakage therefore pass
independent analytic audit. No script, numerical sample, new parameter
regime or source-blocked theorem is used. All unresolved transfer,
positivity and smaller-parameter qualifications above remain in force.

## Mathlib

Full matching coverage for this packet statement and its moving complex
saddle specialization has not been checked and is unknown. The general
integration, holomorphic and Gaussian facts above are standard informal
inputs; no matching Mathlib theorem names, absence claim or Lean
verification is asserted. C997e retains the qualification on its
complex-uniform Laguerre input.
