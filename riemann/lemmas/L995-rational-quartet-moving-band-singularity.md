# Lemma 995: a complete rational quartet survives the moving-band transform

## Hypotheses

Let 1/2<beta<1, gamma>0, and let mu be a positive integer. Set

    eta=beta+i*gamma,
    Q={eta, conjugate(eta), 1-eta, 1-conjugate(eta)},
    P(u)=-mu*sum_(omega in Q) 1/(u-omega),
    delta=beta-1/2, R=exp(-2*delta).

These four points are distinct. They are hypothetical rational-input
parameters, not assumed actual zeros of zeta. In L994(4), replace F
by P in BOTH shifted occurrences, leaving rho=1/4, Re(s)=1, the
positive w orientation, H_r, S_r, 1/s and every other factor intact.
Call the resulting finite-height integral I^P_(r,H), for r=1,2.
Heights tend symmetrically to infinity. Let theta=z*d/dz.

Use L994's exact definitions and its audited coefficient formula (6)
and bound (7), with m=n+r and n>=2. This is the finite K identity
ultimately supplied by L985; none of its arithmetic estimates is used.
No actual-zero decomposition, actual holomorphic complement, RH,
simple zeros, rightmost zero, nonresonance, spectral truncation or
arithmetic endpoint-separation assumption is made.

## Conclusion

The limit Z_r=lim_(H->infinity) I^P_(r,H) exists locally uniformly on
|z|<rho*exp(-2). In this rational-input problem the vertical integral
is absolutely convergent. Its exact coefficient response is

    Z_r(z)=-mu*sum_(omega in Q) sum_(n>=2) z^n
       *[integral_(n+r)^(2*(n+r)) K_(n+r)(t)*exp((omega-1)*t)dt
                       -integral_n^(2*n) K_(n+r)(t)*exp((omega-1)*t)dt]. (1)

Both series extend holomorphically to |z|<R. Formula (6) below gives
their differentiated germs by selected analytic inverse functions,
including the exact constant branch and all four endpoints.

In fact Z_2 has a reachable nonremovable square-root singularity at

    alpha_sigma=beta-1+sigma*i*gamma, sigma in {+1,-1},
    b(w)=w/(1-w), f_c(w)=w*exp(c*b(w)),
    z_*=exp(-2*alpha_+)*f_2(i)
       =R*exp(i*(pi/2+1-2*gamma)).                              (2)

Define the full collision set, without deleting any term,

    E_*={(sigma,w): sigma in {+1,-1}, w in {i,-i},
                         exp(-2*alpha_sigma)*f_2(w)=z_*},
    lambda_(sigma,w)=alpha_sigma-b(w),
    C=mu/4*(1+z_*^(-2))*sum_((sigma,w) in E_*) 1/lambda_(sigma,w). (3)

Then C!=0. With q=1-z/z_* and the square root positive for q>0,
there are functions A and B holomorphic near q=0 such that, on a
small disk about z_* cut along its outward radial ray,

    Z_2(z)=A(q)-2*C*q^(1/2)+q^(3/2)*B(q).                       (4)

Thus the COMPLETE quartet response, not just an integrand or an
isolated summand, has nonzero monodromy. The Taylor series of Z_2
at zero has radius exactly R. This proves the requested pair detects
this rational quartet; the second component already suffices.

Step286, 10 November2026: RESEARCH / POTENTIALLY_NEW under the
unchanged, pre-invocation EXPLORE review285. The contour inversion
and diagonal formula are specializations of known tools. The
complete-quartet noncancellation comparison was not supplied by
the sources checked; this is not a claim of certified originality.
The independent step288 conceptual audit below passes (1)-(8) without
changing their hypotheses or conclusions. This finite-input result supplies
no singularity of actual G, no actual signed estimate, no L993
recovery, no L984(H), and no RH candidate. Actual J_r/-C_r and all
other zeros remain outside this rational-input statement.

## Proof

### Imported tools and their precise scope

Reuse the source statements inspected in review284, step285, and
the pre-existing assessment review285. Import the residue theorem
[NIST DLMF1.10(iv), (1.10.8)](https://dlmf.nist.gov/1.10.E8),
local analytic inversion and its finite-order ramified version
[DLMF1.10(vii), (1.10.12)-(1.10.17)](https://dlmf.nist.gov/1.10#vii),
and compact-uniform improper-integral holomorphy
[DLMF1.10(viii), (1.10.18)-(1.10.19)](https://dlmf.nist.gov/1.10#viii).
The contour locations, convergence and selected branches needed to
apply these theorems are proved below; they are not imported as
conclusions about L994's actual germs.

For the diagonal formula import I. M. Gessel, *Lagrange inversion*,
[arXiv:1609.05988v1, 20 September2016](https://arxiv.org/pdf/1609.05988v1),
Theorem2.1.1, equation(2.1.4), printed pp2-3, and Theorem4.1.1
with its residue-change proof, printed pp22-23. The former gives
the power-series identity for U=x*phi(U), phi(0)!=0; the latter
allows the Laurent coefficient substitution with nonzero linear
term used for r=2. Analytic convergence is checked independently.
Rouche's theorem is used in its standard form: |g|<|f| on a simple
closed contour gives the same number of zeros for f and f+g inside.
No general residue, inversion or Rouche theorem is reproved.

The unchanged Laguerre coefficient tool is
[DLMF18.12.13](https://dlmf.nist.gov/18.12.E13), specialized in
L994(6); its real-positive bound is
[DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), specialized in L994(7).
They give K_m=(L_(m-1)^(2)-1)/(m-1) and
|K_m(t)|<=2*m*exp(t/2) for m>=2, t>=0. The present work needs
different input P and a complete-quartet singularity calculation;
none of these imported tools alone states that conclusion.

### Absolute height limit and the exact response

On |w|=rho, L994's 4/5<=Re(a(w))<=4/3 shows that every pole
lambda=omega-a(w) has Re(lambda)<1/5<1. The constant-branch
poles omega-1 have negative real part. Their imaginary parts and
absolute values are bounded uniformly on this w circle. There
are no poles on the integration line, including at finite heights.

Fix |z|<=R_0'<rho*exp(-2). Both S arguments on Re(s)=1 have
modulus at most R_0'*exp(2)/rho<1. The factors exp(j*r*s) have
bounded modulus there, so H_r is bounded uniformly in Im(s), w
and z. Every rational term after the factor 1/s is O(|s|^(-2))
for sufficiently large |s|, uniformly in w. For bounded Im(s)
the real-part pole separation gives a finite common bound.
Consequently an integrable multiple of (1+|Im(s)|)^(-2) dominates
the whole integrand. This proves the locally uniform absolute
height limit, permits Fubini, and permits extracting z coefficients
under both integrals. No such absolute claim is made for actual F.

For t>0 and Re(lambda)<1, residue calculus gives

    1/(2*pi*i)*integral_(1-i*infinity)^(1+i*infinity)
                       exp(t*s)/[s*(s-lambda)] ds
          =(exp(t*lambda)-1)/lambda.                           (5)

The value at lambda=0 is t. To verify the closing-contour hypotheses,
use rectangles with left side Re(s)=-H and horizontal sides at
Im(s)=+-H, beyond twice a common bound for |lambda|. Each horizontal
integral is O(H^(-2)*integral_(-H)^1 exp(t*x)dx)=O_t(H^(-2));
the left side is O(exp(-t*H)/H). All poles 0 and lambda lie inside,
and none lie on these rectangles. Their residues give (5), with
the coincident double-pole case supplied either directly or by the
removable limit. This checks the finite-contour specialization,
not an infinite family of zeta residues.

In the nth coefficient of H_r the four exponentials have times
2*(n+r), n+r, 2*n, n, and signs +,-,-,+. Their constant residue
terms cancel in (5). The remaining quotient is exactly

    integral_(n+r)^(2*(n+r)) exp(lambda*t)dt
                                  -integral_n^(2*n) exp(lambda*t)dt.

Use lambda=omega-a(w)=(omega-1)-b(w) in the first shifted branch,
and lambda=omega-1 in the second. Cauchy extraction with w^(-n-r)
and the factor 1/(n+r-1) gives K_(n+r), including its -1 branch,
by L994(6). The residue of P is -mu. These facts give exactly (1),
with the same K_(n+r) in BOTH intervals. Occurrences of lambda=0
on a w contour are removable in (5); no exclusion is imposed.

For each omega, Re(omega-1)+1/2 is either delta or -delta. The two
interval lengths sum to at most 2*(n+r), and t<=2*(n+r). Thus the
absolute value of the nth coefficient of (1), after summing all
four omega, is at most

    16*mu*(n+r)^2*exp(2*delta*(n+r)).

This proves normal convergence on |z|<R. Equality with the original
height-limit germ holds first on the smaller initial disk and then
defines its analytic extension. The input here is continuous
exponential density, so no arithmetic jump has been assigned or
removed. This identity does not represent the actual J_r or -C_r.

### Exact inverse-function formula with both shifted branches

For c=1,2 let U_c(x) be the small inverse of f_c, with U_c(0)=0,
and put

    phi_c(w)=exp(-c*b(w)),
    D_c(w)=1+c*w/(1-w)^2,
    E_(c,r)(v)=(exp(c*r*v)-1)/v, E_(c,r)(0)=c*r,
    h_(c,r,alpha)(w)=w^(1-r)*(1-w)^(-3)*E_(c,r)(alpha-b(w)).

For r=1, h is holomorphic near zero; for r=2 it has at most a
simple pole there. For any such Laurent germ V, write [V]_(>=2)
for V with its Laurent coefficients of degrees -1,0,1 removed
(nonexistent coefficients count as zero). This is a specified
finite subtraction, not a discarded endpoint or asymptotic error.
Define, with x=z*exp(c*alpha),

    T_(c,r,alpha)(z)=
        [h_(c,r,alpha)(U_c(x))/D_c(U_c(x))]_(>=2)
                          -E_(c,r)(alpha)*x^2/(1-x).

Then the exact differentiated response is

    Y_r(z):=(theta+r-1)Z_r(z)
       =-mu*sum_(omega in Q)
                 [T_(2,r,omega-1)(z)-T_(1,r,omega-1)(z)].       (6)

Indeed (theta+r-1) cancels the coefficient denominator n+r-1.
For endpoint slope c, the exponential-branch coefficient that
remains is

    exp(c*n*alpha)*[w^(n+r-1)]
            (1-w)^(-3)*E_(c,r)(alpha-b(w))*phi_c(w)^n.

Moving w^(1-r) into h changes this to
exp(c*n*alpha)*[w^n]h(w)*phi_c(w)^n. The imported Lagrange formula
identifies these coefficients with h(U_c(x))/D_c(U_c(x)). For
r=2 the residue substitution x=w/phi_c(w) has nonzero linear
term and dx=D_c(w)/phi_c(w) dw; the same coefficient identity
holds for Laurent h. Since U_c(x)=x+O(x^2), its only possible
negative degree is -1, so the displayed finite subtraction leaves
exactly n>=2. The other shifted branch has
[w^(n+r-1)] (1-w)^(-1)=1, giving exactly
E_(c,r)(alpha)*x^2/(1-x). This proves (6), including the sign
between c=2 and c=1. No general inversion theorem was reproved.

For completeness, the inverses used here are analytic on
|x|<exp(-c/2). On |w|=t<1, Re(b(w))>=-t/(1+t). If

    |x|<t*exp(-c*t/(1+t)),

then |x*phi_c(w)|<|w|. Rouche gives exactly one zero of
w-x*phi_c(w) inside |w|<t. The right-hand bound increases to
exp(-c/2) as t increases to 1, since its logarithmic derivative
is 1/t-c/(1+t)^2>0 for c=1,2. Taking t sufficiently close to 1
shows there is exactly one root in the entire unit disk.
The zeros of D_1 are exp(+-i*pi/3); those of D_2 are +-i.
They lie on its boundary. The root is therefore simple, and the
analytic inverse theorem and uniqueness give U_c throughout the
stated x disk. Formula (6), with its removable origin, is analytic
where these inverses are used. This supplies analytic meaning in
addition to the imported formal coefficient equality.

### The selected U_2 branch at its boundary

Put x_+=f_2(i) and x_-=f_2(-i). Both have modulus exp(-1),
and they are distinct. We verify that U_2 extends locally across
every other point of this circle and reaches the indicated critical
points, ruling out escape to the essential singularity w=1.

First, if x is in the upper half of |x|<exp(-1), then U_2(x)
has positive imaginary part. It cannot cross the real axis there,
because f_2 is real on (-1,1), and its sign near zero is positive.
By continuity from small x, the identity f_2(U_2)=x implies the
principal-argument identity

    arg(x)=arg(U_2(x))+2*Im(b(U_2(x))).

There is no multiple of 2*pi: the integer is continuous on this
connected half disk and zero near the origin. Since
Im(b(w))=Im(w)/|1-w|^2, this gives 0<Im(b(U_2(x)))<pi/2.
Conjugation gives the opposite bounds in the lower half disk, and
uniqueness gives a real U_2 for real x. Thus |Im(b(U_2))|<=pi/2.

As x approaches any nonzero boundary point, U_2 stays bounded away
from zero, since f_2(w)->0 as w->0. Also |U_2|<1, and

    2*Re(b(U_2(x)))=log|x|-log|U_2(x)|

is bounded. Hence b(U_2) is bounded, and
1-U_2=1/(1+b(U_2)) is bounded away from zero. All possible limits
lie in a compact subset of the closed unit disk excluding w=1.
In this compact set f_2(w)=x_0 has only finitely many roots.
The cluster set of U_2 at x_0 is connected: it is the intersection
of the nested compact closures of its images on the connected
sets {|x-x_0|<epsilon, |x|<exp(-1)}. Therefore it is a singleton.
The same compactness also ensures these closures remain in the
stated compact set for small epsilon. This proves a unique boundary
limit. Unless it is i or -i, f_2' is nonzero and the local inverse
theorem extends the selected U_2 holomorphically across x_0.

To select the limits at x_+ and x_-, use the explicit paths
x(t)=f_2(+-i*t), 0<=t<1. They stay in |x|<exp(-1), since

    log|f_2(i*t)|=log(t)-2*t^2/(1+t^2),
    d/dt log|f_2(i*t)|=(1-t^2)^2/[t*(1+t^2)^2]>0,

and the terminal value is -1. Uniqueness in the unit disk gives
U_2(f_2(+-i*t))=+-i*t. Consequently the unique respective boundary
limits are i and -i. The only possible critical values on this
circle are x_+ and x_-, so this also proves the assertion at every
noncritical boundary point, without a global inverse-sheet assumption.

At w_0 in {i,-i}, direct differentiation gives

    D_2'(w_0)=-1, f_2''(w_0)/f_2(w_0)=w_0.

The critical point is quadratic. If x=x_0*(1-q) with
x_0=f_2(w_0), the convergent ramified inverse expansion is

    U_2(x)=w_0-(1+w_0)*q^(1/2)+O(q),
    1/D_2(U_2(x))=(1-w_0)/2*q^(-1/2)+O(1).                    (7)

For q positive the displayed root has modulus less than 1, since
its squared modulus is 1-2*sqrt(q)+O(q); the other root has
squared modulus 1+2*sqrt(q)+O(q). This chooses the sign from the
already specified U_2. Equivalently, Taylor expansion gives
q=-(w_0/2)*(U_2-w_0)^2+O((U_2-w_0)^3).
The ramified inverse theorem makes (7) convergent on the local
q plane cut along the nonpositive real axis.

### Complete-quartet collision coefficient

At |z|=R, the c=1 factors of (6) have
|x|<=exp(-1/2-delta)<exp(-1/2). The c=2 factors of the left
pair Re(omega)=1-beta have |x|=exp(-1-4*delta)<exp(-1).
Thus these factors extend holomorphically to a neighborhood of z_*.
The constant shifted branches are also holomorphic there: all
Re(alpha)<0 and |z_*|<1 give |z_* exp(c*alpha)|<1.
Finite Laurent subtractions are holomorphic at z_*!=0.

Only the c=2 terms with alpha=alpha_+ or alpha_- can be singular
there. The preceding boundary argument makes them holomorphic
unless the relevant (sigma,w_0) belongs to E_*. For every member
of E_*, x/x_0=z/z_*, so (7) uses the SAME q and the SAME square-root
determination in the local disk. Put lambda=alpha_sigma-b(w_0).
Then Re(lambda)=delta>0, and the defining collision identity gives

    exp(2*lambda)=w_0/z_*.

For r=2 the coefficient of q^(-1/2) in its term of Y_2 is, using
the -mu sign in (6),

    -mu * (1-w_0)/2 * w_0^(-1)*(1-w_0)^(-3)
                                      *(exp(4*lambda)-1)/lambda
       =mu/4*(1+z_*^(-2))/lambda.                             (8)

Here (1-w_0)^2=-2*w_0 and w_0^2=-1. Summing (8) over the
ENTIRE collision set gives precisely C in (3); everything else
is holomorphic or has higher Puiseux order. For each summand,

    Re(1/lambda)=delta/(delta^2+Im(lambda)^2)>0.

The set is nonempty because (+1,i) belongs to it. Its reciprocal
sum is nonzero, and 1+z_*^(-2)!=0 because |z_*|=R<1. Therefore
C!=0, without any separation between the individual critical values.

More explicitly, let vartheta=pi/2+1. The four possible right-pair
critical images are R*exp(i*(epsilon*vartheta-2*sigma*gamma)),
epsilon,sigma in {+1,-1}. At the selected z_* the additional
contribution is (-1,i) exactly when 4*gamma belongs to 2*pi*Z,
or (-1,-i) exactly when 4*gamma-2*vartheta belongs to 2*pi*Z.
These alternatives cannot both occur, since pi/2<vartheta<pi.
The other critical point of the same alpha_+ does not coincide.
Formula (8) covers either exceptional collision and the generic
singleton, with every multiplicity mu retained. No cancellation
exception is excluded. Values lambda=0 away from these critical
points remain removable in E_(c,r), as specified earlier.

There are only finitely many candidate critical images on |z|=R.
Choose a small disk about z_* avoiding the other distinct ones
and zero, and cut it along z=z_*(1+t), t>=0. All terms of (6)
then have the selected analytic or convergent Puiseux extensions.
Their sum has the expansion

    Y_2(z)=C*q^(-1/2)+a(q)+q^(1/2)*b_0(q),

with a,b_0 holomorphic near zero. As (theta+1)Z_2=(z*Z_2)',
local integration gives (4); the leading primitive is
-2*z_* C*sqrt(q), followed by division by z=z_*(1-q).
No logarithm occurs because the Puiseux exponents in Y_2 start
at -1/2, not -1. The integration constant is fixed by the initial
germ, and contributes only to A. A circuit about q=0 changes the
sign of the nonzero leading square-root term, proving nonremovability.

Finally, the explicit path

    z(t)=exp(-2*alpha_+)*f_2(i*t), 0<=t<1,

starts at the initial germ, stays in |z|<R by the preceding derivative
calculation, and tends to z_*. All four input contributions are
continued together along this path. It reaches the very singular
element whose coefficient is (3), not another inverse branch.
The analytic disk from (1) and this nonremovable boundary point
give radius exactly R for Z_2. This finishes the finite rational
test only. It does not establish any complementary holomorphy for
the actual G_1,G_2 or justify summing such responses over zeta zeros.

### Independent conceptual audit — step288, 10 November 2026

RESEARCH / REPRODUCTION under the unchanged, separately approved
EXPLORE review286. The entire proof (1)-(8) was checked for every
1/2<beta<1, gamma>0 and positive integral mu. No correction to its
claims is required. This verifies the previously proposed finite
detector; it is not a second discovery or a verification of actual
zeta-complement assumptions. The following checks make explicit
the load-bearing analytic and algebraic points of the audit.

**Height limit and endpoints.** On the fixed w circle, every shifted
pole has real part strictly below 1/5, so its distance from Re(s)=1
is bounded below by 4/5. The finite pole set is bounded uniformly in
w. For a compact initial z disk the two S arguments have a common
modulus bound strictly below one. Thus H_r is uniformly bounded and
each rational term divided by s is bounded by a common multiple of
(1+|Im(s)|)^(-2), including the bounded-height part. This pays both
Fubini and coefficient extraction. Closing the right edge upward
to the left has positive orientation; the two residues in (5) are
exp(t*lambda)/lambda and -1/lambda. Their removable coincident case
is t. The four endpoint signs give

    [exp(2*n*lambda)*(exp(2*r*lambda)-1)
                  -exp(n*lambda)*(exp(r*lambda)-1)]/lambda.

The common -mu residue is therefore retained, as is the second
shifted branch yielding the -1 in K_m. With m=n+r, each omega's
two interval lengths total m+n<=2*m. L994(7) consequently gives
4*m^2*exp(2*delta*m) per omega, proving the stated total bound
16*mu*m^2*exp(2*delta*m). This establishes only the open disk R.

**Laurent extraction and analytic meaning.** For x=f_c(w)=w/phi_c(w),
one has dx=D_c(w)/phi_c(w) dw. Hence the local residue expression
for the nth coefficient of h(U_c(x))/D_c(U_c(x)) changes to

    Res_(w=0) h(w)*phi_c(w)^n*w^(-n-1) dw.

This is exactly the imported Gessel substitution, with nonzero
linear coefficient f_c'(0)=1. It applies also to r=2: h has at
most a simple pole, U_c(x)=x+O(x^2), and D_c(0)=1. There are no
degrees below -1; deleting precisely degrees -1,0,1 leaves n>=2.
The constant branch contributes E_(c,r)(alpha)*x^2/(1-x), with
the subtraction sign in (6). The Rouche inequality is strict on
every selected circle |w|=t<1, where phi_c is holomorphic inside
and on the circle. The increasing bound tends to exp(-c/2), so
uniqueness on successively larger circles gives uniqueness in
the whole unit disk. The displayed zeros of D_c lie on its boundary;
the interior root is simple and the local inverses glue uniquely.
Thus the formal identity has the claimed analytic realization.

**Boundary compactness.** In the connected upper x half disk, U_2
cannot be real, since a real w in (-1,1) has real f_2(w). Its
imaginary part is positive near x=0 and therefore throughout that
half disk. The continuous difference between arg(x) and
arg(U_2)+2*Im(b(U_2)) is in 2*pi*Z and tends to zero near the
origin. It is identically zero. Both arguments lie in (0,pi),
and Im(b(U_2))>0, proving the claimed bound by pi/2. Reflection
and uniqueness cover the lower half disk and the real axis.

Near any nonzero x_0 on |x|=exp(-1), |U_2| cannot approach zero.
The modulus identity in the proof then bounds Re(b(U_2)) on both
sides. Together with the imaginary-part bound it bounds |b(U_2)|,
so |1-U_2|=1/|1+b(U_2)| has a positive lower bound. Thus no
sequence can escape to w=1. On the resulting fixed compact set
f_2(w)-x_0 is analytic and not identically zero, so it has only
finitely many zeros. The nested closed images of the connected
disk intersections have a nonempty connected intersection; every
point in it is one of those finitely many zeros. It is a singleton.
The paths f_2(+-i*t) select the limits +-i; the derivative of their
log modulus is strictly positive for 0<t<1 and their terminal
modulus is exp(-1). At every other boundary value the resulting
limit is a regular point of f_2 and yields a local analytic inverse.

**Selected ramification and the complete sum.** At w_0=+-i,
D_2'(w_0)=-1 and f_2''(w_0)/f_2(w_0)=w_0. The two first
inverse coefficients are +/-(1+w_0). For positive real q, their
squared moduli are 1+/-2*sqrt(q)+O(q), so the inside-disk branch
has the minus sign. This verifies both coefficients in (7) and
their common square-root determination for every collision.
For a colliding term, Re(lambda)=delta>0 and exp(2*lambda)=w_0/z_*.
Its full coefficient simplifies without a sign loss as

    -mu/[2*w_0*(1-w_0)^2]*(exp(4*lambda)-1)/lambda
      =-mu/4*(-z_*^(-2)-1)/lambda
      =mu/4*(1+z_*^(-2))/lambda.

The two listed resonance conditions enumerate all additional
possibilities: the other critical point of the same alpha cannot
coincide, and the two cross-alpha possibilities cannot occur
together because pi/2<vartheta<pi. No parameter exception was
discarded. Every reciprocal in the nonempty collision set has
strictly positive real part; their sum is nonzero. The prefactor
cannot vanish since |z_*|<1. At z_*, c=1 inverse arguments and
left-pair c=2 arguments are strictly inside their inverse disks;
constant branches have |x|<1, and Laurent subtractions are regular.
Every noncolliding right-pair term has the regular continuation
just verified. The finite collection therefore admits a common
slit disk with precisely the summed coefficient C!=0.

**Primitive and radius.** Since (theta+1)Z_2=(z*Z_2)', changing
variables to q gives dz=-z_* dq. Integrating the leading term
C*q^(-1/2) gives -2*z_* C*sqrt(q); division by z_*(1-q) yields
-2*C*sqrt(q) plus terms of order q^(3/2). The analytic part and
the integration constant remain analytic. There is no exponent
-1 and hence no logarithmic term. The selected path lies in the
original analytic disk and reaches this element of the slit
extension. Its nonzero square-root term is nonremovable, proving
radius exactly R, not merely an upper bound for an isolated term.

All estimates here are for fixed allowed parameters; no uniform
limit beta down to 1/2, gamma to infinity, or infinite quartet sum
has been asserted. In particular this audit does not transport the
finite height majorant to actual F, prove holomorphy of its complement,
control J_r/-C_r after continuation, recover L993, or pay L984(H).
The only direct mathematical input remains L994; its use of L985's
finite K identity is transitive. The source tools cited above retain
their local, formal or compact-uniform qualifications. No new DAG
edge, numerical certificate, or independent r=1 singularity claim
is needed for this audit.

## Mathlib

Full matching coverage of this rational-quartet transform and its
complete collision coefficient has not been checked and is unknown.
No absence claim is made. Standard complex residue, Rouche,
analytic-inverse and power-series results are supporting tools;
their Mathlib theorem names and the ramified-inverse specialization
were not checked in this step. The exact external inputs and local
applicability arguments are recorded above. No numerical preview
or formal computation is being used as proof.
