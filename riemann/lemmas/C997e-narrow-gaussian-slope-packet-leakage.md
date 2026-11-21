# Corollary 997e: narrow Gaussian slope packets retain the target but leak on the data band

## Hypotheses

Use the COMPLETE response H_n^+(z;mu) in C997c(1), with its original
K_(n+2)=(L_(n+1)^(2)-1)/(n+1), n>=2 an integer. Set

    I=[7/4,9/4], E=J=[15/8,17/8], delta=1/8,
    z_star=1+i/8,
    theta(c)=arccos(1-c/2),
    phi(c)=theta(c)+sqrt(c*(4-c))/2,
    q(c)=phi'(c)=(1/2)*sqrt((4-c)/c).

On the real interval J take positive square roots and theta in (0,pi).
These functions have the local holomorphic extensions specified below.
For a fixed real A>0 define an absolutely continuous complex measure

    Z_(n,A)=integral_J exp(-A*n*(c-2)^2)dc,
    dmu_(n,A)(c)=Z_(n,A)^(-1)*1_J(c)*exp(-A*n*(c-2)^2)
                                      *exp(i*n*(phi(c)-c))dc.       (1)

The curvature A is fixed before n tends to infinity. No uniformity for
A=A_n is claimed. J is a fixed compact subinterval of the interior of I.
These are hypothetical finite slope measures, not actual zeta data.
Both short intervals, both beta contributions and K's -1 are retained.

## Conclusion

There exists a finite A_0>=16 such that, for every fixed A>=A_0,
||mu_(n,A)||_TV=1 for every n>=2, and

    H_n^+(z_star;mu_(n,A))=n^(-3/2)*(B_star+o(1)), B_star!=0,
    H_n^+(2;mu_(n,A))=n^(-3/2)*exp(n*S_A)*(B_A+o(1)), B_A!=0,
    S_A=2*beta+beta^2/(4*A), beta=1/8+i,
    Re(S_A)=lambda_A=1/4-63/(256*A)>=961/4096>0.                (2)

The limits hold through all sufficiently large integers. The constants
B_star and B_A are explicitly defined in (6) below; A_0 and the onset
are existential. In particular these packets meet the target-retention
requirement |H_n^+(z_star)|>=exp(-o(n)), but

    lim_(n->infinity) n^(-1)*log|H_n^+(2;mu_(n,A))|=lambda_A>0. (3)

Since 2 belongs to the closed data band E, they cannot meet its required
uniform exp(-sigma*n) suppression for any fixed sigma>0, even on an
unbounded integer subsequence. This is a stop ONLY for (1) with fixed
sufficiently large A. Smaller A, other phases/densities, n-dependent
curvature and the general point inequality remain undecided.

Step327, 10 November 2026: RESEARCH / POTENTIALLY_NEW, outcome NEGATIVE,
under the pre-invocation EXPLORE assessment review325 and its approved
COVERED_TARGET. The result is a local subclass obstruction using known
bulk asymptotics, not a novelty certification or an RH result. Independent
conceptual audit was pending at step327; the step329 audit below accepts
the stated result without changing its bounds. No actual-Xi positivity, selected-response
normalization, signed recovery, complement or regulator claim follows.

## Proof

### Imported analytic bulk input and the required specialization

Import M. Vanlessen, *Strong asymptotics of Laguerre-type orthogonal
polynomials and applications in random matrix theory*,
[math/0504604v2, 29 August 2005](https://arxiv.org/pdf/math/0504604v2),
Theorem 2.4(b)/(2.13), Remarks 2.3/2.5, Proposition 3.31 and
Theorem 3.32/(3.110), and Proposition 5.1/(5.5)-(5.6), printed
pp5-7,32-34,39. Use Q(x)=x, alpha=2>-1, and degree N=n+1.
The orthonormal-to-Laguerre conversion is

    p_N(t)=(-1)^N*L_N^(2)(t)/sqrt((N+1)*(N+2)), beta_N=4*N,

using the norm and leading coefficient in
[DLMF Table18.3.1](https://dlmf.nist.gov/18.3#T1).
These inspected contracts were already covered in reviews291/325.
The exact bulk formula and its analytic error matrix, not merely the
real-axis O symbol, are essential here. The general source theorem is
not reproved. Cauchy's theorem, the Cauchy derivative estimate, finite
integral Fubini and the Gaussian integral are used in their standard
named forms. The contour specialization below is needed because the
sources do not evaluate the original-TV packet response.

Here is that specialization, including normalization and error structure.
On a fixed complex neighborhood U of J there are exact holomorphic
amplitudes B_(-,n)(c,u), B_(+,n)(c,u), for 0<=u<=2, such that, for
all sufficiently large n,

    L_(n+1)^(2)(c*(n+u))/(n+1)
      =n^(-3/2)*exp(c*(n+u)/2)*[
           exp(-i*n*phi(c))*B_(-,n)(c,u)
          +exp( i*n*phi(c))*B_(+,n)(c,u)],
    B_(+/-,n)(c,u)=b_(+/-)(c)*exp(+/- i*c*u*q(c))+O(1/n),
    a(c)=sqrt(2/pi)*c^(-5/4)*(4-c)^(-1/4),
    b_(+/-)(c)=(a(c)/2)*exp(+/- i*(5*theta(c)/2-5*pi/4)).    (4)

The O(1/n) terms are holomorphic in c and uniformly bounded on U,
uniformly for real u in [0,2]. In particular there is NO separate
uncontrolled additive real-axis remainder in the first equality.

To justify the domain and exact formulation, fix the source's lens and
endpoint disks. A compact interval about J/4 lies strictly inside the
bulk lens, away from its reduced contour and the disks. The error matrix
R_N is holomorphic on a neighborhood there, including across the real
bulk interval, by Proposition 3.31, and R_N=Id+O(1/N) uniformly by
Theorem 3.32. Choose nested fixed neighborhoods, so c*(n+u)/(4*N)
remains in the larger one for c in the smaller U, all u in [0,2] and
all sufficiently large n. All branches in (5.5)-(5.6) have holomorphic
local extensions there. Their exact upper-half-plane identity extends
across the real interval by the identity theorem. Split both cosines
in (5.6) into exponentials and retain R_N inside the amplitudes.
The scalar factor written 1+O(1/N) in (5.1) comes from the leading
coefficient, is independent of c, and is likewise retained exactly.

The phase and prefactor conversions can be checked explicitly. Write
s=c*(n+u)/N and z=s/4. For Q(x)=x the source has
psi(z)=(2/pi)*sqrt((1-z)/z) on the real bulk interval, so

    pi*integral_1^z psi(v)dv=phi(s)-pi,
    arccos(2*z-1)=pi-theta(s),
    N*phi(c*(n+u)/N)
          =n*phi(c)+theta(c)+c*u*q(c)+O(1/n).

The last equality follows by uniform holomorphic Taylor expansion and
phi(c)-c*q(c)=theta(c). Thus the first cosine after multiplication by
(-1)^N has phase n*phi(c)+c*u*q(c)+5*theta(c)/2-5*pi/4+O(1/n).
The second cosine has an analytic O(1/n) coefficient. The prefactor in
(2.13), multiplied by sqrt((N+1)*(N+2))/N, equals
n^(-3/2)*exp(c*(n+u)/2)*(a(c)+O(1/n)). These facts give (4), including
the factor 1/2 from splitting the cosine. The exact analytic amplitudes
also absorb the exponentials of the O(1/n) phase errors. All bounds
hold on fixed complex compact sets; Cauchy's estimate bounds the
derivatives on a smaller U as needed.

### Separate the exact dominant beta term and pay the other terms

On the real line phi is real, so (1) has TV exactly one. Also

    Z_(n,A)~sqrt(pi/(A*n)).                                  (5)

Substitute x=sqrt(A*n)*(c-2) and use dominated convergence and the
Gaussian integral; both rescaled endpoints tend to infinity.

Expand cosh(3t/8) and L_(n+1)^(2)(t)-1 in C997c's upper interval.
The coefficient -2 cancels the 1/2 from cosh. The upper positive-beta
Laguerre term is exactly

    -integral_J exp(-cn/4)*integral_(cn)^(c(n+2))
                  L_(n+1)^(2)(t)/(n+1)*exp((-1/8+i*z)*t)dt
                                                         dmu_(n,A)(c).

For z in {z_star,2}, put

    beta_z=1/8+i*(z-1),
    A_(z,+/-,n)(c)=-c*integral_0^2
                   exp(c*u*(3/8+i*z))*B_(+/-,n)(c,u)du,
    d_z(c)=3/8+i*z-i*q(c),
    A_(z,-)(c)=-b_-(c)*(exp(2*c*d_z(c))-1)/d_z(c),
    B_star=A_(z_star,-)(2),
    c_A=2+beta/(2*A), B_A=A_(2,-)(c_A).                     (6)

Interpret the quotient by its removable value when d_z(c)=0.
Both amplitudes A_(z,+/-,n) are uniformly bounded and holomorphic on U,
with uniform holomorphic limits, by (4) and finite integration. For the
minus amplitude the limit is the displayed A_(z,-).

Substitute t=c*(n+u) in the exact positive-beta term. Then

    H_n^+(z;mu_(n,A))=n^(-3/2)*Z_(n,A)^(-1)*[I_(z,-)+I_(z,+)]
                                                    +Rem_(n,z),
    I_(z,-)=integral_J exp(n*(-A*(c-2)^2+beta_z*c))
                                               *A_(z,-,n)(c)dc,
    I_(z,+)=integral_J exp(n*(-A*(c-2)^2+beta_z*c+2*i*phi(c)))
                                               *A_(z,+,n)(c)dc. (7)

Rem is exactly the reflected-beta Laguerre upper term, the entire
constant-subtraction upper term, and the COMPLETE lower interval.
For both z under consideration,

    |Rem_(n,z)|<=C*(n+2)*exp(-n/16).                         (8)

Indeed L997(4)'s K bound, after adding 1/(n+1), gives
|L_(n+1)^(2)(t)/(n+1)|<=C*(n+2)*exp(t/2) for t>=0.
For the reflected-beta upper Laguerre term the real exponential after
this bound is exp(-cn/4-3t/8)<=exp(-5cn/8). For the entire constant
subtraction, cosh(3t/8)<=exp(3t/8) leaves
exp(-cn/4-t/8)<=exp(-3cn/8). Here t>=cn and the interval lengths
are at most 9/2. At z_star the extra exp(-t/8) improves both bounds.
Integrate against the original |mu|, whose mass is one. Finally
C997c(5) bounds the complete lower interval at z=2 by
8*exp(3/4)*(n+2)*exp(-n/16), and at z_star by that quantity times
exp(-n/8), since t>=n. This proves (8) for every separated term.

### Fix the analytic strip and curvature before taking limits

Shrink U if necessary. Choose h>0 so that the rectangle

    2-delta<=Re(c)<=2+delta, 0<=Im(c)<=h

and a neighborhood of it lie in U, and Re(q(c))>=1/3 there.
This is possible because q is real and greater than 1/3 on J.
Since phi is real on J, vertical integration gives

    Im(phi(x+i*y))=integral_0^y Re(q(x+i*v))dv>=y/3.         (9)

At c=2, q=1/2, theta=pi/2, and b_-(2)=1/(4*sqrt(pi)). Thus

    d_(z_star)(2)=1/4+i/2,  exp(4*d_(z_star)(2))=exp(1+2i),
    d_2(2)=3/8+3i/2,       exp(4*d_2(2))=exp(3/2+6i).

The two numerators in (6) are nonzero because the exponentials have
modulus greater than one. Hence B_star!=0 and A_(2,-)(2)!=0.
Continuity gives a disk about 2 on which A_(2,-) is nonzero.
Choose A_0>=16 so large that, for every A>=A_0,

    y_A=1/(2*A)<h, c_A=2+1/(16*A)+i/(2*A)

lies in that disk and has real part strictly between the endpoints
of J. This fixes a finite A_0 independent of n. Thereafter fix
A>=A_0. Constants and onsets may depend on this fixed A.

### Target retention, including the unwanted Laguerre branch

At z=z_star, beta_z=0. Gaussian concentration, uniform amplitude
convergence and (5) give

    Z_(n,A)^(-1)*I_(z_star,-) -> A_(z_star,-)(2)=B_star.

This retains a nonzero complex value, not merely an upper bound.
To control I_(z_star,+), deform its interval to height y_A inside
the fixed rectangle. Cauchy's theorem gives the shifted horizontal
segment and two vertical endpoint segments. Its holomorphic amplitude
is uniformly bounded on ALL these segments.

On the horizontal segment, (9) gives

    Re[-A*(c-2)^2+2*i*phi(c)]
       <=-A*(Re(c)-2)^2+1/(4*A)-1/(3*A)
       =-A*(Re(c)-2)^2-1/(12*A).

On a vertical endpoint c=2+/-delta+i*v, 0<=v<=y_A, it gives

    Re[-A*(c-2)^2+2*i*phi(c)]
       <=-A*delta^2+A*v^2-2*v/3<=-A*delta^2,

because A*v<=1/2. Segment lengths and amplitude bounds are fixed.
Thus I_(z_star,+)=O(exp(-n/(12*A))+exp(-A*delta^2*n)); division
by Z_(n,A) adds only O(sqrt(n)). Equation (8) is exponentially
smaller than n^(-3/2). This proves the first asymptotic in (2).

### Actual data leakage at the interior observation point 2

Now z=2 and beta_z=beta=1/8+i. Complete the square exactly:

    -A*(c-2)^2+beta*c=S_A-A*(c-c_A)^2.                      (10)

Move I_(2,-) to height y_A, retaining its endpoint segments. On this
horizontal line c-c_A is real and its center Re(c_A)=2+1/(16*A)
lies strictly inside J. A Gaussian change of variable and uniform
amplitude convergence give the horizontal contribution

    exp(n*S_A)*sqrt(pi/(A*n))*(A_(2,-)(c_A)+o(1)).           (11)

Dominated convergence after rescaling uses the uniform amplitude bound;
both rescaled endpoints tend to infinity. This integrates the EXACT
analytic error amplitudes on the shifted contour. It does not integrate
an absolute real-axis O(1/n) error against an oscillating exponential.

At either vertical endpoint and 0<=v<=y_A,

    Re[-A*(c-2)^2+beta*c]
      =-A*delta^2+(2+/-delta)/8+A*v^2-v
      <=v_A:=1/4+delta/8-A*delta^2=(17-A)/64.               (12)

The same bound holds with +2*i*phi(c), by (9). Thus both branches'
vertical contributions are O(exp(v_A*n)). These pay the actual compact
cutoff: its indicator is not assumed holomorphic across an endpoint.

For I_(2,+) on the horizontal line, (9)-(10) give

    Re[-A*(c-2)^2+beta*c+2*i*phi(c)]
             <=lambda_A-A*(Re(c)-Re(c_A))^2-1/(3*A).       (13)

Its horizontal contribution is O(exp((lambda_A-1/(3*A))*n)).
All margins needed for (11) to dominate are explicit:

    lambda_A>=961/4096>0,
    lambda_A-v_A=(4*A^2-4*A-63)/(256*A)>0, A>=16,
    lambda_A-(lambda_A-1/(3*A))=1/(3*A)>0.                  (14)

Since Z_(n,A)~sqrt(pi/(A*n)), polynomial factors cannot close these
fixed positive gaps. The complete remainder (8) also decays
exponentially. Substitution in (7) proves the second asymptotic in (2),
with B_A!=0, and hence (3).

For sufficiently large n, the first asymptotic gives
|H_n^+(z_star)|>=(|B_star|/2)*n^(-3/2). Taking
a_n=max{0,(3/2)*log n+log(2/|B_star|)} supplies a_n>=0 with
a_n/n->0. The data asymptotic gives an incompatible positive rate at
a point of E; the rest of E need not be estimated for this negative
result.

### Scope and unresolved work

This is a conflicting lower bound for the specified narrow Gaussian
family, verified by the step329 audit below. No noncancellation subsequence
is assumed. Smaller curvature and other admissible measures are not
excluded. The source domain and amplitude nonvanishing yield an
existential A_0 only; no numerical A is certified to lie above it.
The general packet assay, the point inequality, both-sign/selected
transfer, C997a(8)'s extra term, original assay, reconstruction, signed
recovery, infinite-zero complements, regulator uniformity, L993 and
L984(H) remain open. No infinite-zero sum or target-equivalent positivity
enters this finite-input argument.

### Independent conceptual audit — step329, 10 November 2026

RESEARCH / REPRODUCTION under the pre-invocation SPECIALIZE review327's
exact COVERED_TARGET. The audit accepts (1)-(14) for every fixed A>=one
existential A_0, with no numerical A_0 or varying-A assertion. This
verifies an existing local input using known tools, not a stronger
packet theorem, originality claim or RH candidate. No bound required
correction. The following explicit checks make the analytic-error and
noncancellation steps independently inspectable.

**Exact amplitudes, not a continued O symbol.** The Vanlessen source
cited above was reconsulted at (1.1)-(1.2), Theorem2.4(b), Remarks2.3/2.5,
Proposition3.31, Theorem3.32 and (5.1),(5.5)-(5.6), with (3.4),(3.14)
for the scalar normalization. These are the pre-assessed contracts.
Write R_N for its residual matrix, gamma_N for the positive leading
coefficient of p_N, and ell=-2-4*log(2). Set

    kappa_N=gamma_N*(4*N)^(N+3/2)*exp(N*ell/2)*sqrt(pi/2)/4,
    s=c*(n+u)/N, w=s/4, N=n+1,
    P_1=N*phi(s)+(3/2)*theta(s)-5*pi/4,
    P_2=N*phi(s)+(1/2)*theta(s)-pi/4,
    F_(n,u)(c)=kappa_N*(n/N)^(3/2)
                         *sqrt((N+1)*(N+2))/N*a(s).

Equations (3.4),(3.14) give the EXACT identity
p_N(4*N*w)=gamma_N*(4*N)^N*U_11(w); hence kappa_N is a scalar,
independent of w. The leading-coefficient estimate in (5.1), equivalently
(2.7), gives kappa_N=1+O(1/N). Taking the first row of (5.6) and the
normalization in (4) gives exactly

    L_N^(2)(c*(n+u))/N
      =n^(-3/2)*exp(c*(n+u)/2)*F_(n,u)(c)
         *[R_(N,11)(w)*cos(P_1)-16*i*R_(N,12)(w)*cos(P_2)]. (15)

The coefficient 16 is 4^alpha with alpha=2. To check the sign, the
source's two cosine arguments are N*pi-P_1 and N*pi-P_2. The factor
(-1)^N in the conversion from p_N cancels each of these parity factors.
The prefactor simplifies using
w^(-1/4)*(1-w)^(-1/4)=2*s^(-1/4)*(4-s)^(-1/4), giving precisely
F_(n,u). In particular its limit is a(c), not a(c) times an additional
power of n or a parity sign.

For epsilon in {+1,-1} an exact choice of (4)'s amplitudes is therefore

    B_(epsilon,n)(c,u)=(F_(n,u)(c)/2)*[
      R_(N,11)(w)*exp(epsilon*i*(P_1-n*phi(c)))
      -16*i*R_(N,12)(w)*exp(epsilon*i*(P_2-n*phi(c)))].       (16)

Here all quantities in P_j and F use this same s and u. On the chosen
fixed neighborhood, s-c=c*(u-1)/N=O(1/N) uniformly for 0<=u<=2.
Taylor expansion with bounded holomorphic second derivatives yields

    N*phi(s)-n*phi(c)=phi(c)+c*(u-1)*q(c)+O(1/n)
                    =theta(c)+c*u*q(c)+O(1/n).

Thus P_1-n*phi(c)=c*u*q(c)+5*theta(c)/2-5*pi/4+O(1/n),
and P_2-n*phi(c) is uniformly bounded there. Since R_11=1+O(1/N),
R_12=O(1/N) and F=a(c)+O(1/n), (16) proves exactly (4)'s two limits.

For domain control, choose a simply connected neighborhood V of J/4
whose closure avoids the reduced contour and both endpoint disks,
with its upper part in the source bulk region. Proposition3.31 removes
the real bulk jump of R_N. Choose a smaller such neighborhood and a
neighborhood U of J with closure compactly contained in its fourfold
dilate. The maps c -> c*(n+u)/(4*N) remain in V for all large n and
all u in [0,2]. The source uniform estimate then applies to R_N at
every such argument. Choose local branches agreeing on the real
interval; their holomorphic extensions and R_N make (15)-(16)
holomorphic on U. Equality on its upper part extends by the identity
theorem. Shrinking once more provides bounded amplitudes and derivatives
on a neighborhood of the entire later contour. This does not extend
the source's principal lower-boundary convention by fiat, and it does
not assert holomorphy of the compact-support indicator.

**Original normalization and the complete response.** On J the packet
phase is real, so the total variation of (1) is its positive Gaussian
integral divided by Z_(n,A), exactly one for every n. For fixed A,
the change x=sqrt(A*n)*(c-2) proves (5) with both finite endpoints
retained until dominated convergence. In C997c(1), -2 times the
positive exponential of cosh contributes -1. Substitution t=c*(n+u)
then has Jacobian c and leaves exp(c*u*(3/8+i*z)), exactly as in (6).
Multiplication by exp(i*n*(phi-c)) cancels the minus phase and adds
2*i*phi to the plus phase, proving the signs and beta_z in (7).
Integration of the minus limiting amplitude over u gives (6), including
the removable value -2*c*b_-(c) at d_z(c)=0.

For the reflected-beta Laguerre term the absolute exponent is
-cn/4-3*t/8; for the entire -1 term it is at most -cn/4-t/8.
Their interval lengths are 2*c<=9/2. L997(4) bounds the Laguerre term
after adding 1/(n+1), and integration uses the original variation one.
For the lower interval use the full measure variation in C997c(5).
At z_star its positive support t>=n adds exp(-n/8); at z=2 its
Fourier multiplier has modulus one. These observations verify (8)
for the complete response, including both beta signs and both intervals.
All integrations and their rearrangements have finite variation on
compact rectangles; no zero sum or limit interchange is implicit.

**Nonzero limits and the order of choices.** At c=2 the minus amplitude
has b_-(2)=1/(4*sqrt(pi)). The values of d_z and their exponentials
listed after (9) have positive real exponents 1 and 3/2. Consequently
neither numerator vanishes and neither leading constant at 2 is zero.
Continuity supplies one nonvanishing disk for A_(2,-). Since
|c_A-2|=|beta|/(2*A) decreases to zero, a single finite A_0 can place
every c_A for A>=A_0 in that disk, inside the horizontal endpoints,
and below h. The compact real interval has min q>1/3; continuity
gives (9) on one fixed rectangle before A_0 is chosen. Fix A only
afterward. No estimate uniform as A varies with n has been used.

At the target, Gaussian concentration of the exact minus amplitude
gives B_star. On the upper horizontal contour the plus-branch rate
is at most -1/(12*A)-A*(x-2)^2. On either vertical endpoint it is
at most -A*delta^2 since A*v<=1/2<2/3. Thus its contribution divided
by Z tends to zero exponentially, while (8) is also negligible after
multiplication by n^(3/2). This proves an actual nonzero target limit.

At the data point, completion of the square in (10) is exact. Along
c=x+i*y_A, c-c_A=x-Re(c_A) is real. The exact amplitudes converge
uniformly there; boundedness after Gaussian rescaling supplies domination,
and the endpoints tend to opposite infinities because Re(c_A) is
strictly interior. This verifies (11) with the complex factor
exp(n*S_A), and B_A!=0 follows from the preceding disk choice.

For both endpoint signs, A*v^2-v<=0 on [0,1/(2*A)]. Maximizing the
remaining (2+/-delta)/8 gives v_A=(17-A)/64. Adding 2*i*phi only
decreases that real part. The other branch on the horizontal contour
loses at least 2*y_A/3=1/(3*A). Finally
lambda_A>=961/4096, and the numerator 4*A^2-4*A-63 in (14) is
positive at 16 (value 897) and strictly increasing for A>=16.
Each vertical segment, the unwanted horizontal branch and the complete
remainder therefore has a fixed strictly smaller exponential rate.
The factors from 1/Z and n^(3/2) are polynomial for fixed A, so they
cannot undo these gaps. This proves the second nonzero asymptotic
through all sufficiently large integers, not just a chosen subsequence.

This is an analytic audit; no numerical preview or sampling is used as
evidence. Direct local mathematical inputs remain L997(4),(7) and
C997c(1),(5). The audited subclass stop is retained, while all scope
limitations listed above remain. Mathlib matching coverage stays unknown.


## Mathlib

Full matching coverage for this obstruction and its complex-uniform
Laguerre bulk input has not been checked and is unknown. No absence
claim or Lean verification is made. Standard Cauchy, Gaussian and
finite-integration facts support the informal proof; its precise
external asymptotic input is cited above.

