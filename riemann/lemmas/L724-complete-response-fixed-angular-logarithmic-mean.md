# Lemma 724: a fixed signed logarithmic arc for the complete response

## Hypotheses

Use the full rational response of L666 with the original fixed actual
profile and accepted pointwise rate of L723. In particular

    n=12q+3, q>=1, M=n/3, d=5/4, x=-d, R=11/8, U=121/64,
    h=27/(10n), t_j=j/n, u_*=(3+4i)/10,
    Z_n={x} union {x+i*h*(m+1/2+e_m): -2q<=m<2q},
    |e_m|<=1/8,
    W_a(u)=(x/a)*product_(j=1)^(n-1)
        [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)],
    G_n(u,z)=R^(-1)*sum_(a in Z_n) W_a(u)
                                  *sum_(k=0)^(M-1)(a*z/R)^k.

The profile is fixed before n varies, with precisely L723's bump and
support endpoint b. Put r=r(b) and g_n(u)=G_n(u,-1). The accepted input is

    limsup_(q->infinity) log|g_(12q+3)(u_*)|/(12q+3)=r>1/200.  (1)

Here and below log(0)=-infinity. The definition of W is the rational
angular continuation, including its inverse denominator angle and j=0
factor x/a. All original masses, endpoints and all M moments are kept.
Let theta_*=arg(3+4i), with 0<theta_*<pi/2.

## Conclusion

There is a fixed explicit arc width

    s=exp(-100000),       eta=s/10 in (0,pi/10),

such that every finite-n integral below is finite, and

    limsup_(q->infinity) (1/(2*eta*n))
        *integral_(theta_*-eta)^(theta_*+eta)
          log|G_n((1/2)*exp(i*theta),-1)| dtheta
                                     >= r-1/2000 > r/4.       (2)

The lower estimate uses a single subsequence realizing (1). The arc is
fixed before that subsequence and does not depend on n. The result is
about the signed logarithm, including its integrable singularities at
zeros, rather than log-plus or a maximum. Neither eventual nonvanishing
on the arc nor a full-sequence rate limit is asserted.

Status: derived in step 205; accepted by the separate step-206
conceptual audit in Section 5 below.
This is a quantitative specialization within the prior EXPLORE coverage,
not certified originality or an RH candidate. Since the spatial maximum
S_(n,1)(u) includes z=-1, (2) supplies one possible lower contribution
to its angular logarithmic mean. The arc is extremely small. The
complementary angular contribution, spatial Jensen defect, full charge,
H/support, Xi realization and actual-Xi all-degree positivity remain
unresolved. None is paid by (2).

## Proof

### 1. Source scope and the quantitative difference

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-complete-response-angular-log-propagation.md`
and its exact COVERED_TARGET. The actual complete response and the
interior-circle peak in (1) are essential. The exterior-anchor
countermodel recorded in the bounded-coefficient stop is a comparison,
not an input or a replacement for (1).

The local zero-factor/harmonic-factor method is known. Its inspected
source is Yu. Il'yashenko and S. Yakovenko, *Counting Real Zeros of
Analytic Functions Satisfying Linear Ordinary Differential Equations*,
J. Differential Equations **126** (1996), 87–105,
[Sections 1.1, 1.3–1.4, Lemmas 1–3 and their proofs, pp.93–99](https://www.wisdom.weizmann.ac.il/~yakov/jde-95.pdf).
The local statements do not require the function to satisfy an ODE.
For the zero-free factor we use the standard disk Harnack inequality:
if v>=0 is harmonic on |w|<rho, then

    v(w) <= ((rho+|w|)/(rho-|w|))*v(0),       |w|<rho.   (3)

This is the positive harmonic inequality used in the proof of their
Lemma 2. Their zero division and Jensen argument permit zeros in the
original function. The standard maximum-modulus principle is also used.
For the disk Jensen interface, the reused inspected source is
R. B. Ash and W. P. Novinger, *Complex Variables* (2004),
[Theorem 4.8.3 and Lemma 4.8.4, printed pp.33–36](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=94).
No boundary-zero limiting theorem is needed below: comparison circles
are chosen without zeros. Zeros on the real trace are retained.

These general theorems are imported, not claimed as new. The uncovered
quantitative difference authorized by EXPLORE is a signed trace loss
tending to zero with a fixed arc width, uniformly over this growing
family. Sections 3–4 give that bound by an explicit near/far zero split.
It cannot be replaced by an unspecified O(n) loss. No Remez exponent,
planar-to-line convergence theorem, or complex continuation of the bump
is assumed. The elementary near-root integral estimate is included
because it pays this specific remaining loss.

### 2. Common analytic disk, complete upper bound and integrability

Set

    u(w)=u_* exp(i*w/10),       F_n(w)=g_n(u(w)).

For |w|<=1, the exponential series gives

    |u(w)-u_*| <= (1/2)*(exp(1/10)-1) < 1/18,
    Re u(w)>11/45>1/5,        |u(w)|<5/9<3/5.          (4)

For example exp(1/10)-1<sum_(k>=1)(1/10)^k=1/9,
so these bounds require no numerical approximation.
L666's finite family satisfies |Im a|<9/20, a!=0 and

    |a|^2 < 353/200 < (273/200)^2,
    |a| < 273/200 < R,       |x/a|<=1.                (5)

All nonanchor ordinates are nonzero, since |e_m|<=1/8. Directly from
(4), for 0<=t<1 and a in Z_n,

    |a-t*u| >= d+t*Re u >= d,
    |U*u-t*x| >= U*Re u+d*t > U/5,
    |x-t*u|/|a-t*u| < (d+3/5)/d=37/25<3/2,
    |U*u-t*a|/|U*u-t*x| < (3*U/5+R)/(U/5)=73/11<7.

Thus every denominator in the rational continuation stays nonzero on
the closed w-disk, and the full product obeys

    |W_a(u(w))| <= 11^(n-1).                           (6)

For a=x this also holds, since W_x=1 after exact cancellation.
The strict denominator margins give analyticity on a neighborhood of
the closed disk for each n. The disk and the estimates are common to n.
Using every one of the M spatial moments, (5) gives

    sum_(k=0)^(M-1)|a/R|^k <= 1/(1-273/275)=275/2,
    |F_n(w)| <= 100*M*11^(n-1) <= 100*n*11^n < exp(5*n),
                                                    |w|<=1. (7)

For the last, n>=15 and 100*n<2^n (check n=15 and induct on n).
Also exp(1)>2 and exp(3)>1+3+9/2+27/6=13>11, so even
100*n*11^n<exp(4*n). The looser exponent 5 is convenient below.
This is a coarse absolute upper bound; the signed lower input remains
exactly (1).

We also verify that no finite-n g_n is the zero rational function.
Choose any nonanchor a and t_1=1/n. At u=a/t_1 the term W_a has a
genuine simple pole: its factor a-t_1*u vanishes simply; the other
a-t_j*u do not vanish; U*u-t_j*x is nonreal; and each numerator
x-t_j*u and U*u-t_j*a is nonzero. In the latter case
U*u-t_j*a=a*(U/t_1-t_j), with U>1>t_1*t_j.
No other atom has a pole there. Indeed b/t_j=a/t_1 implies, by
comparing real parts x/t_j=x/t_1, that j=1 and then b=a; all poles
t_j*x/U are real. The coefficient multiplying W_a in g_n is

    R^(-1)*sum_(k=0)^(M-1)(-a/R)^k
                       =[1-(-a/R)^M]/(R+a) != 0,      (8)

because |a|<R. Hence this pole survives in g_n. This uses an outer
pole only to certify that the rational function is nonzero, not to
propagate an exterior anchor value or obtain a lower bound.

Since u(w) is a nonconstant holomorphic map, F_n cannot vanish
identically. Its zeros on the compact real interval [-s,s] are
therefore finite. At a real zero w_0 of multiplicity k it factors as
(w-w_0)^k times a locally nonvanishing analytic function. Consequently
log|F_n(w)| is Lebesgue integrable there, including at interval endpoints.
This proves finite-n integrability without assuming nonvanishing or
using a limiting trace theorem.

### 3. A uniform signed trace loss, including zeros

For this section take an allowed n with |F_n(0)|>=1, and initially
any 0<s<1/4. Choose rho in (1/2,3/4) such that F_n has no zero on
|w|=rho. This is possible because its zeros on |w|<=3/4 are finite.
The comparison radius may depend on n; the integrated interval [-s,s]
does not. List the zeros a_j inside this circle, with multiplicities.
None equals zero. Define the finite disk Blaschke factors and quotient

    B_j(w)=rho*(w-a_j)/(rho^2-conjugate(a_j)*w),
    H(w)=F_n(w)/product_j B_j(w).

Removable singularities are filled in. H is analytic and nonvanishing
on a neighborhood of |w|<=rho; |B_j|=1 on its boundary and |B_j|<1
inside. By (7) and the maximum-modulus principle,

    v(w)=5*n-log|H(w)| >=0

is harmonic in the disk. Evaluating the factorization at zero gives
the exact nonnegative Jensen budget

    D=5*n-log|F_n(0)|
      =v(0)+sum_j log(rho/|a_j|),       0<=D<=5*n.      (9)

This identity and Harnack are used only at finite n. Empty zero lists
cause no exception.

Call a zero near if |a_j|<=sqrt(s), and far otherwise. A near zero
costs at least

    L(s)=log(1/(2*sqrt(s)))>0

in (9). Therefore the number N_near, with multiplicities, is at most
D/L(s).

For any complex c!=0, the elementary bound

    (1/2)*integral_(-1)^1 log|1-t/c| dt >= -2           (10)

holds with integrable real-root singularities. To see this, if |c|>2,
the integrand is at least -log(2)>-1. If |c|<=2, then
|t-c|>=|t-Re c|. For any real alpha, the integral of
(-log|t-alpha|)^+ over [-1,1] is at most
integral_(-1)^1 -log|v| dv=2, by translation and restriction to
|v|<1. It follows that the mean of log|t-c| is at least -1.
Subtracting log|c|<=log 2 gives (10), since log 2<1.

For a near zero apply (10) with c=a_j/s and w=s*t. The exact ratio is

    B_j(w)/B_j(0)=(1-w/a_j)/(1-conjugate(a_j)*w/rho^2).

On [-s,s], log|1-conjugate(a_j)*w/rho^2| is at most
log(1+|a_j|*s/rho^2)<=s/rho<2*s. Consequently

    (1/(2*s))*integral_(-s)^s
       [log|B_j(w)|-log|B_j(0)|] dw >= -2-2*s >= -3.   (11)

This pays every near zero, even if it lies on the trace.

For a far zero, -log|B_j(w)| is positive harmonic on |w|<|a_j|.
Apply (3) on smaller concentric disks and let their radii increase to
|a_j|. For |w|<=s this gives

    log|B_j(w)|-log|B_j(0)|
       >= -[2*s/(|a_j|-s)]*log(rho/|a_j|)
       >= -beta(s)*log(rho/|a_j|),
    beta(s)=2*sqrt(s)/(1-sqrt(s)).                     (12)

The positivity used here holds because B_j maps the rho-disk into the
unit disk. A zero on |w|=|a_j| causes no issue in the smaller-disk
application. Likewise Harnack for v on |w|<rho yields

    log|H(w)|-log|H(0)| >= -[2*s/(rho-s)]*v(0)
                                      >= -beta(s)*v(0), (13)

since rho>1/2 and 0<s<1/4 imply
2*s/(1/2-s)<=2*sqrt(s)/(1-sqrt(s)).

Integrate the finite factorization, using (11) for near zeros and
(12)–(13) for the other terms. All integrals are finite as verified
above, so this operation involves no interchange with n or an infinite
zero sum. From (9) and N_near<=D/L(s),

    (1/(2*s))*integral_(-s)^s log|F_n(w)| dw
       >= log|F_n(0)|-delta(s)*D,
    delta(s)=3/L(s)+2*sqrt(s)/(1-sqrt(s)).              (14)

The two uses of D make this deliberately nonoptimal but valid.
In particular delta(s) tends to zero as s decreases. No eventual
zero-free trace or upper bound for the degree has been presumed.

### 4. Fix the arc, then choose the common peak subsequence

Fix s=exp(-100000), independently of n. Then

    L(s)=50000-log 2>49999,
    3/L(s)<1/16000.

Also exp(50000)>1+50000+50000^2/2>100000, so

    sqrt(s)<1/100000,
    beta(s)<2/99999<1/40000,
    delta(s)<1/16000+1/40000=7/80000<1/10000.           (15)

Thus (9) and (14), for each permitted n with |F_n(0)|>=1, imply

    (1/(2*s*n))*integral_(-s)^s log|F_n(w)| dw
                       >= log|F_n(0)|/n-1/2000.        (16)

By (1) there is one increasing subsequence of allowed n along which
log|F_n(0)|/n tends to r>0. Eventually |F_n(0)|>=1 on this same
subsequence. Equation (16) holds there with the same s. Taking its
lower limit and then the full-sequence upper limit gives at least
r-1/2000. No pointwise limsups at other angles are substituted.

Finally u(w)=(1/2)*exp(i*(theta_*+w/10)). With eta=s/10, substitution
theta=theta_*+w/10 gives exactly

    (1/(2*eta))*integral_(theta_*-eta)^(theta_*+eta)
       log|g_n((1/2)*exp(i*theta))| dtheta
          =(1/(2*s))*integral_(-s)^s log|F_n(w)| dw.

This proves (2). Since r>1/200, one has 1/2000<r/10, so the obtained
lower bound is actually greater than 9*r/10, in particular r/4.
The tiny fixed arc is a legitimate existential answer to this test;
it supplies no quantitative payment for the rest of the circle.

### 5. Separate conceptual audit — 3 November 2026, step 206

This audit accepts (2), including every finite-n integrability assertion,
under exactly the stated hypotheses. It reuses the unchanged EXPLORE
assessment and COVERED_TARGET cited in Section 1. It verifies a local
specialization of the imported analytic tools; it neither strengthens
the theorem nor asserts novelty. No mathematical correction to
Sections 2–4 was needed.

**Complete family and common disk.** Independently, the extreme
ordinate satisfies

    |Im a|<=h*(2q-3/8)<2q*h=27q/(5n)<9/20.

Adjacent nonanchor ordinates differ by at least 3h/4 and each is at
distance at least 3h/8 from zero. Hence there are exactly M=4q+1
distinct atoms, including x. The bounds (5) follow from
d^2+(9/20)^2=353/200 and
(273/200)^2-353/200=3929/40000>0. On the complex w-disk,
Re(a-tu)=-d-t Re(u) and Re(Uu-tx)=U Re(u)+dt. These give
the modulus lower bounds (6) uses, without assuming u is real.
The two upper ratios in (4)–(6) multiply to less than
(3/2)*7<11. Also R^(-1)*(275/2)=100 and |Z_n|=M;
thus (7) sums every atom and all M moments. The induction for
100n<2^n starts with 1500<32768 at n=15 and uses n+1<=2n.
These are uniform bounds on a common disk, not pointwise estimates
on the angular trace alone.

**Nonidentity and trace zeros.** At u=n*a for a nonanchor atom,
no numerator vanishes and the factor a-u/n has a simple zero.
Every other possible nonreal pole b/t_j is distinct: its real
part would force t_j=1/n, then b=a. The shared real poles cannot
coincide with n*a. The coefficient (8) is nonzero because
|a/R|<1 and Re(R+a)=1/8. Therefore cancellation by another term
cannot remove this pole. Nonconstancy of w->u(w), the open mapping
theorem and the identity theorem exclude F_n identically zero on
the local disk. The compact trace has finitely many zeros, each
contributing a finite multiple of log|w-w_0| plus a bounded
continuous term locally. This includes endpoints and proves absolute
logarithmic integrability at every allowed n, even off the peak
subsequence.

**Comparison circles and the budget.** Finite zeros in the compact
3/4 disk permit a zero-free comparison circle with
1/2<rho_n<3/4 for each n. Dividing out all its zeros makes H
nonvanishing near the closed rho_n disk; the possible Blaschke
denominator poles lie outside it. Boundary equality |H|=|F_n|
and maximum modulus give v>=0. The identity (9) is exact since
|B_j(0)|=|a_j|/rho_n. Its nonnegative summands justify both the
near-zero count and the far-zero budget. No bound on the total
number of zeros, or uniform choice of rho_n, is required.

**Signed loss and harmonic domains.** In (10) the negative part of
log|t-Re(c)| has integral at most 2 on any translated interval;
discarding its positive part gives the asserted lower bound. Thus
the near-zero estimate is for the signed integral and covers a zero
on the trace. Its Blaschke denominator contributes at most
log(1+|a_j|s/rho_n^2)<=s/rho_n<2s. For a far zero,
-log|B_j| is nonnegative harmonic on every concentric disk of
radius less than |a_j|; its pole has modulus rho_n^2/|a_j|>rho_n.
Harnack can therefore pass to the radius |a_j|, yielding (12).
For H, rho_n>1/2>sqrt(s) gives the bound in (13). The integrated
finite factorization has loss at most

    3*N_near+beta(s)*(v(0)+sum_far log(rho_n/|a_j|))
       <=[3/L(s)+beta(s)]*D.

This verifies (14) without an infinite sum, a trace-limit theorem,
or an unquantified linear error.

**Constants and quantifiers.** The inequalities
48000<49999, 80000<99999 and 7/80000<1/10000 verify (15).
The choice s=exp(-100000) precedes all n, circle and subsequence
choices. Along one subsequence realizing the finite positive L723
limsup, eventually |F_n(0)|>=1, so 0<=D<=5n. The lower limit
of the normalized integrals along this subsequence is at least
r-1/2000. The upper limit along all permitted n is no smaller.
The angular change of variable has dtheta=dw/10 and eta=s/10,
so no factor of ten or arc measure is lost. Since r>1/200,
the resulting rate exceeds 9r/10 and hence the required r/4.

The direct mathematical inputs remain L666's exact family and L723's
accepted peak; fixed-profile information is inherited through L723.
The exterior-anchor stop is a contrast, not a dependency. This audit
does not reopen L723's audited proof, extend the arc, or pay the
complementary angular mean, spatial Jensen defect, full charge or
Xi realization. No numerical check or mathematical script is needed
for these exact inequalities and analytic arguments.

## Mathlib

Full matching coverage for this complete-family signed logarithmic arc
estimate has not been checked. No formalized theorem is claimed.
Maximum modulus, disk Jensen factorization and Harnack are standard
supporting inputs, with the precise informal citations and applicability
above; their presence would not by itself formalize (4)–(16) or L723.
Unknown coverage is not evidence of absence. No numerical script or
preview is used as proof. The meaningful checks here are the exact
product inequalities, finite-zero integrability, the signed integral
estimate (10), the budget (9), the explicit bound (15), and the common
subsequence/change-of-variables argument. Section 5 records the separate
conceptual audit of these points; formalization remains unchecked.
