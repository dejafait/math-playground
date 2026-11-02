# Lemma 657: exact logarithmic divisors and bounded local angular pole cost

## Hypotheses

Retain L649's complete family: integer n>=5, x=-d=-5/4,
R=11/8, U=R^2=121/64, eta=1/100, r_*=R-eta=273/200,
rho=r_*/R=273/275 and t_j=j/n. The common finite set Z has
N distinct poles a with Re(a)=x and |a|<=r_*, includes x, and
has positive integer original residues r_a with M=sum_a r_a<=n/3.
There is no separation, symmetry or coefficient-integrality assumption.
For |u|=1 use the full product and conjugated denominator angle

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1) sum_a r_a W_a(u)(a/R)^k,
    G(u,zeta)=sum_(0<=k<M) c_k(u) zeta^k.

All angular and spatial circle measures are normalized. Write

    D=mean_u d_n(u),
    d_n(u)=sum_a r_a^2 |W_a(u)|^2/(U-|a|^2),
    m(u)=mean_zeta log|G(u,zeta)|.

Thus D is exactly L649's D_single,n, not a diagonal with unsquared
residues or a truncated grid. All logarithms are natural. Put J=n-1 and

    A_a(u)=product_(1<=j<n)(a-t_j*u),
    C_a(u)=product_(1<=j<n)(U*u-t_j*a),
    Q(u)=C_x(u) product_(b in Z, b!=x) A_b(u),
    H_M(v)=sum_(0<=k<M) v^k,

    K(u,zeta)=R^(-1) [r_x Q(u) H_M(x*zeta/R)
       + sum_(a!=x) r_a*(x/a)*A_x(u)*C_a(u)
           *product_(b!=x,a) A_b(u)*H_M(a*zeta/R)].       (1)

The sum in (1) is empty when N=1. For theta_0 on the angular circle,
let I_0 be the connected centered arc of normalized length n^(-2);
in an unwrapped angular coordinate it is
[theta_0-pi/n^2,theta_0+pi/n^2]. Endpoints have measure zero.

## Conclusion

The identity G=K/Q holds on both unit circles. K is a nonzero complex
polynomial of degrees at most NJ in u and M-1 in zeta. Q never
vanishes on the angular unit circle. No slice G(u,.) for |u|=1,
or rational angular slice G(.,zeta) for |zeta|=1, is identically zero.
The product logarithm log|G| is absolutely integrable; zeros on the
torus are allowed. Every positive-measure arc mean in the target is
therefore finite.

For each |u|=1 let d_u be the actual spatial degree, gamma_u its
nonzero leading coefficient, and alpha its spatial roots, with
multiplicity. Then, including degree drops and boundary roots,

    m(u)=log|gamma_u|+sum_alpha log max(1,|alpha|).        (2)

There is also a complete full-circle angular accounting. Put

    p_j=t_j*x/U,
    P_n=sum_(1<=j<n) log(1/|p_j|)
       =-log[(80/121)^J * J!/n^J].

For almost every spatial zeta, count all zeros beta of K(.,zeta)
in the open angular unit disk, including cancellations with Q, and set

    Z_n=mean_zeta sum_(|beta|<1) log(1/|beta|),
    m_0=mean_zeta log|G(0,zeta)|.

Here u=0 is rational continuation. The exceptional finite set where
K(0,zeta)=0 is omitted from this integral. It has measure zero. Then

    mean_u m(u)=m_0+Z_n-P_n,                             (3)
    log[M*d^2/(R*r_*^2)] <= m_0
                         <= log[M/(R*(1-rho))].         (4)

Z_n is finite and nonnegative. Formula (3) retains every angular
interior pole and numerator zero. It is not a lower bound for Z_n.

The angular denominator cost on every I_0 is bounded uniformly:

    |mean_(I_0) log|Q(u)|-log|Q(e^(i theta_0))||
                                               <=4*pi/3. (5)

Consequently the exact paid expression is

    log mu(I_0)+2 mean_(I_0 x T) log|G|
      =-2 log n+2 mean_(I_0 x T) log|K|
            -2 log|Q(e^(i theta_0))|+e_Q,
    |e_Q|<=8*pi/3.                                      (6)

The full diagonal satisfies

    |d/dtheta log d_n(e^(i theta))|<=30*n,
    d_max/(30*e*pi*n)<=D<=d_max.                         (7)

In particular choose theta_0 attaining d_max and define

    A_0=mean_(I_0 x T)
        log|K(u,zeta)/(Q(e^(i theta_0))*sqrt(d_max))|.

For this concrete arc the exact relative expression, with all costs,
is

    log mu(I_0)+2 mean_(I_0 x T) log|G|-log D
        =-2 log n+2 A_0+e_Q+log(d_max/D),                (8)
    |e_Q|<=8*pi/3,
    0<=log(d_max/D)<=log(30*e*pi*n).

Thus the angular denominator variation costs O(1), and replacing the
diagonal mean by its maximum costs O(log n). The numerator A_0 and
the correlated zero contribution Z_n remain uncontrolled. No uniform
rate-1/16 inequality, all-arcs countersequence, or assertion that a
diagonal-maximizing arc is sufficient has been proved. These statements
do not settle L651's response comparison, Xi realization or signs.
This family-specific reduction has not received a separate audit.

## Proof

### 1. Source scope and purpose

The unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`
covers exactly this rational clearing, divisor accounting and angular
localization. Its primary inputs are reused without a new literature
turn. L649 supplies the family and coefficient conventions. L651 is
the proposed downstream use, not a premise of the estimates below.
C645p's ambient continuation loss and C645x's fractional dual stop
remain contrasts, not obstructions to this nonlinear criterion.

Import the logarithmic-integrability theorem for a nonzero complex
polynomial in finitely many variables from Z. Issa and M. Lalin,
*A generalization of a theorem of Boyd and Lawton*,
[arXiv:1203.5379v1, Remark 3.8 and Theorem 4.1/proof, printed p.7](https://arxiv.org/pdf/1203.5379v1),
24 March 2012, using s=1. No uniform small-value constant or
Boyd--Lawton limiting assertion is imported.

Import the exact one-variable root integral from F. Brunault and
W. Zudilin, *Many Variations of Mahler Measures*, ISBN 9781108794459,
[Proposition 1.4, publisher excerpt pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf):
the normalized integral of log|e^(i theta)-alpha| is
log max(1,|alpha|), including |alpha|=1. The source's boundary-root
case was inspected in the assessment. Rational Jensen may equivalently
be imported from T. Tao, *246B, Notes 1: Zeroes, poles, and factorisation
of meromorphic functions*, 23 December 2020,
[Theorem 2 and formulas (1), (3)--(5)](https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/).
The center-zero exception is treated below; no infinite center
logarithm is inserted into that theorem.

These identities and integrability results are known inputs. The
specialization is necessary to verify the actual numerator, exceptional
slices, all pole factors and a degree-uniform arc cost. It does not
reprove Jensen or replace the required correlated numerator bound by
a generic degree estimate. The numerical diagnostic mentioned in the
working record supplies no premise of this proof.

### 2. Clearing denominators without losing poles

Keeping 1/u=conjugate(u) on the circle, direct division of the full
products gives the rational continuation

    W_a(u)=(x/a) * A_x(u) C_a(u)/(A_a(u) C_x(u)).       (9)

The factor at t_0=0 is x/a; all other factors remain in A and C.
For a=x, W_x=1. Multiplying the sum defining G by Q cancels A_a
for a!=x and proves (1). This also proves the degree assertions.
The roots of C_x are p_j with |p_j|<80/121<1. The roots of each
A_b are b/t_j, of modulus >d>1. Thus Q has no boundary zeros.
Its leading factors and full-circle logarithmic mean are exactly

    mean_u log|Q(u)|=J log U+J sum_(b!=x) log|b|.       (10)

In particular the exterior factors have not been silently removed
when taking a mean. Equation (10) follows from the cited root identity;
for A_b its leading factor t_j cancels log t_j from |b/t_j|.

For fixed |u|=1, none of W_a(u) is zero or infinite: A_x,A_a have
all roots outside, C_x,C_a all roots inside, with |t_j*a/U|<1.
If every c_0,...,c_(M-1) vanished, then for all polynomials f of
degree at most N-1 one would have sum_a r_a W_a(u) f(a/R)=0,
because N<=M. Choosing the Lagrange polynomial that is one at a/R
and zero at every other b/R gives r_a W_a(u)=0, a contradiction.
This proves nonvanishing of every spatial polynomial slice without
assuming a separation bound.

For completeness no angular slice at |zeta|=1 is identically zero
either. If N=1, it is the nonzero constant r_x H_M(x*zeta/R)/R.
If N>=2, fix a!=x and j>=1. The exterior pole a/t_j of W_a is
simple and noncancelled in (9). Indeed A_x cannot vanish there
(real parts would force t_l=t_j and then a=x); C_a cannot vanish
there because U>t_j*t_l; and the other A_a factors have different
roots. It is not a pole of any W_b with b!=a: b/t_l=a/t_j and
Re(a)=Re(b)=x force t_l=t_j and b=a. Its coefficient in G is
r_a H_M(a*zeta/R)/R, which is nonzero since |a*zeta/R|<1 and
H_M(v)=(1-v^M)/(1-v) has no zero in that disk. Thus this angular
rational function has a nonzero exterior residue and cannot vanish
identically. These facts also cover unequal original multiplicities.

At u=0, the paired ratios in (9) cancel to give W_a(0)=x/a.
Q(0) is nonzero, and

    Re c_0(0)=R^(-1) sum_a r_a*d^2/|a|^2
                              >=M*d^2/(R*r_*^2)>0.    (11)

Hence K(0,zeta), and therefore K itself, is not the zero polynomial.
The imported polynomial theorem makes log|K| absolutely integrable
on the product torus. On the angular circle log|Q| is bounded and
continuous. Their difference proves the claimed integrability of
log|G|. Restriction to any positive-measure arc preserves absolute
integrability and gives a finite normalized mean. Fubini is now
justified, including torus zeros; no bounded-log assumption was used.

### 3. Complete spatial and angular divisor identities

For each angular u on the circle, factor the nonzero spatial
polynomial with its actual degree. The cited one-root integral gives
(2). A degree drop uses its actual nonzero leading coefficient;
no roots at infinity are inserted. The formula includes zero roots
and roots on the spatial circle. Its value equals the spatial
integral already shown to be integrable in u.

For almost every spatial zeta, K(0,zeta)!=0; the exceptional set is
finite by (11). Apply the finite polynomial root formula to
K(.,zeta), using its actual angular degree. Subtract the logarithm
of its constant value, expressed using its roots. This gives

    mean_u log|K(u,zeta)|-log|K(0,zeta)|
                        =sum_(|beta|<1) log(1/|beta|).  (12)

Boundary roots contribute zero to the right side and have integrable
logarithms on the left. The exceptional center-zero slices are
excluded only from this almost-everywhere identity. Similarly Q's
interior zeros are exactly p_j; its other zeros are exterior, so

    mean_u log|Q(u)|-log|Q(0)|=P_n.                    (13)

Both the product integral of log|K| and the one-variable integral
of log|K(0,zeta)| are absolutely finite by the imported theorem.
Thus (12) has an integrable, nonnegative right side. Integrating
(12), subtracting (13), and using Fubini proves (3) and finiteness
of Z_n. If an interior pole of G cancels, its zero remains in K
and cancels the corresponding charge from Q in this identity.
There are no omitted angular poles, residues or cancellation terms.

Apply the same cited spatial root formula to G(0,zeta). Its mean
is at least log|c_0(0)|, giving the lower bound in (4) by (11).
For the upper bound, |x/a|<=1 and |H_M(a*zeta/R)|<=1/(1-rho),
so |G(0,zeta)|<=M/[R*(1-rho)] on the spatial circle. Integrating
the logarithm gives the upper bound. Zeros do not invalidate this
upper bound or integrability. The formula for P_n follows directly
from |p_j|=(80/121)j/n. No zero-displacement estimate for Z_n has
been derived from positivity of the residues.

### 4. Uniform local denominator and diagonal costs

Every factor of Q is nonzero on the circle. For any differentiable
nonzero complex function f(theta),
|d log|f|/dtheta|<=|f'/f|, obtained by differentiating |f|^2.
The factors of C_x give

    |d/dtheta log|C_x(e^(i theta))||
                <=J*U/(U-d)=J*121/41.

Each factor of A_b gives t_j/|b-t_j*u|<=1/(d-1)=4.
Consequently

    |d/dtheta log|Q(e^(i theta))||
        <=J*(121/41+4*(N-1))<4*N*J.                  (14)

For each point in I_0 the angular distance to its center is at most
pi/n^2. Integrating (14), then taking its normalized arc mean,
gives a bound of 4*N*J*pi/n^2<=4*pi/3 because N<=M<=n/3 and
J<n. This proves (5). Substituting G=K/Q and mu(I_0)=n^(-2)
gives (6), with e_Q=-2(mean_(I_0)log|Q|-log|Q(center)|).
This argument uses a continuous real logarithm of the modulus;
it requires no holomorphic logarithm or unrecorded branch choice.

For (9), the two A factors contribute at most 4J each to the
absolute logarithmic derivative. The C_a numerator contributes
at most J*U/(U-r_*)=J*3025/841 and C_x contributes at most
J*121/41. Therefore, uniformly in a and u,

    |d/dtheta log|W_a(e^(i theta))||
        <=J*(8+3025/841+121/41)<15*n.                 (15)

The strict rational comparison follows from
3025*41+121*841=225786<241367=7*841*41.
For a=x the derivative is zero, which also obeys the bound.
The logarithmic derivative of the positive sum d_n is a convex
combination of the logarithmic derivatives of its positive summands.
Each of those is twice the derivative in (15); the factors r_a^2
and U-|a|^2 are constant in theta. This proves the first part of (7).

Continuity and positivity give an attained d_max. On the centered
arc of angular radius 1/(30n) around a maximizer, integration of
the bound 30n yields d_n>=d_max/e. The normalized length of this
arc is 1/(30*pi*n). Integrating it gives the lower bound for D
in (7); the upper bound follows from the definition of d_max.
This auxiliary arc is used only to compare the diagonal mean and
maximum, not to replace I_0 in the target.

Finally divide K by Q(center)*sqrt(d_max) in (6), subtract log D,
and apply (7). This is exactly (8). In particular all of the remaining
exponential uncertainty in this sufficient fixed-arc comparison lies
in A_0, not in an unpaid denominator oscillation or the diagonal
mean-to-maximum conversion. Other arcs may do better; no conclusion
about their existence follows from (8) alone.

## Mathlib

The reused assessment inspected
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html).
Supporting univariate results include
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_mul`. Lean's totalized real logarithm does
not remove the analytic nonzero hypotheses checked above. A full
matching theorem for this rational two-variable localization and its
constants was not identified in that module; broader multivariate
coverage has not been checked. The cited primary sources supply the
analytic imports, and no absence claim for Mathlib as a whole is made.
