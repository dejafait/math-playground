# Lemma 984: a one-sided prime-degree average bound suffices for RH

## Hypotheses

Let Lambda be the actual von Mangoldt function, with every prime
power included fully at a real cutoff. For integers k>=2 and X>1 set

    ell_k(u)=L_(k-1)^(1)(u),
    P_k(X)=sum_(2<=m<=X) Lambda(m)*ell_k(log m)/m
              -integral_1^X ell_k(log x) dx/x.

For each integer n>=2 put

    X_n=exp(10000*(n+1)^4),
    a_n=A_n(X_n)=(n-1)^(-1)*sum_(k=2)^n P_k(X_n).

Assume the following one-sided bound, which is NOT established here:

    For every epsilon>0 there is a finite C_epsilon>=0 such that
    a_n<=C_epsilon*exp(epsilon*n) for every integer n>=2.       (H)

Use L018's actual entire completion xi, and ordinary, undivided Li
coefficients lambda_n. Use L980/L982's nonalternating convention

    -zeta'(1+s)/zeta(1+s)-1/s=sum_(j>=0) eta_j*s^j,
    S_f(k)=sum_(j=1)^k binom(k,j)*eta_(j-1).

No lower bound for a_n, zero simplicity, RH, regularized Q_n sign,
or interchange of an infinite degree sum with a cutoff limit is
assumed. All constants may depend on the fixed zeta function.

## Conclusion

Hypothesis (H) implies RH: every nontrivial zeta zero has real part
1/2. This is a sufficient arithmetic criterion, not a proof of (H)
or an unconditional proof of RH. No converse is needed or asserted.

The intermediate conclusion used below is

    c_n=sum_(k=2)^n lambda_k >= -D_epsilon*exp(epsilon*n)
    for every epsilon>0 and every integer n>=2,                (1)

with a finite nonnegative D_epsilon. The cumulative germ for c_n
retains a pole at every mapped zero strictly inside the unit disk.
Pringsheim's theorem rules out these poles under (1).

Written in step238, 10 November 2026, under the pre-existing
SPECIALIZE assessment review236. Classification: REPRODUCTION,
a local specialization of inspected standard methods, with no
claim of a result beyond the sources checked. The separate step240
conceptual audit below accepts the implication without a mathematical
correction. The arithmetic premise and the notebook's actual-Xi
positivity gap remain open.

## Proof

### Imported inputs and scope of the specialization

L981 supplies its audited all-real-endpoint tail estimate. L982
supplies only its audited fixed-index limit for the argument below;
we independently check the needed average error rather than assume
the unaudited step235 application. L980 supplies its exact arithmetic
split and unconditional smooth trend:

    lambda_k=S_infty(k)-S_f(k)+1,
    S_infty(k)=(k/2)*log k+c*k+O(1),
    c=(EulerGamma-1-log(2*pi))/2.                              (2)

The precise external sources for (2), retained in L980, are
J. C. Lagarias, *Li coefficients for automorphic L-functions*,
Ann. Inst. Fourier **57**(5) (2007), 1689-1740,
Definition4.3/(4.5), Lemma4.4/(4.6)-(4.8),
[pp1708-1709](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=21),
and Theorem5.1/(5.1)-(5.4),
[pp1712-1713](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=25),
in the explicitly included trivial GL(1) case N=Q=1, kappa=K=0.
The pole term is +1. Neither the conflicting alternating remark
(4.13) nor the stopped Section6 contour estimate is used. The
weak-height residual conclusion of L980 is not needed.

Import the ordinary Li generating germ from Andre Voros,
*Zeta functions over zeros of Zeta functions and an
exponential-asymptotic view of the Riemann Hypothesis*,
[arXiv1403.4558v2, 26 July 2014, (31)-(32), p10](https://arxiv.org/pdf/1403.4558v2#page=10):
for the completed function normalized to value 1 at s=1,

    log(2*xi(1/(1-z)))=sum_(k>=1) (lambda_k/k)*z^k            (3)

as an analytic germ at z=0, with logarithm value 0 there.
Voros's completed function is in the s variable, not the notebook's
real-height Xi. The coefficient lambda_k/k in (3) is divided by k;
lambda_k in (2) is ordinary Li. These conventions agree, as also
checked for L968. Multiplication of xi by 2 changes only a constant
logarithm and leaves ordinary Li coefficients unchanged. We import
no saddle asymptotic or source radius assertion for our cumulative
observable; its singularities are checked below.

Import Pringsheim's theorem in P. Flajolet and R. Sedgewick,
*Analytic Combinatorics — Complex Asymptotics*, zeroth edition,
8 May 2004,
[TheoremIV.3(ii), printed pp15-16/PDF23-24](https://algo.inria.fr/flajolet/Publications/ch4567.pdf#page=23):
a power series with nonnegative real coefficients and finite positive
Taylor radius R is singular at the positive real point R. Both
the theorem's hypotheses and its proof were inspected in the reused
assessment. It is imported without reproof. Taylor differentiation,
zero-order factorization and the identity theorem are the standard
analytic facts in [DLMF1.10(i)-(ii)](https://dlmf.nist.gov/1.10).

The inspected individual-coefficient criterion in Lagarias
Theorem2.4(2)/(2.21), pp1702-1703, is not applied to averages.
The specialization needed here is precisely the cumulative germ,
its coefficient direction and the moving-cutoff error. L976's
different translated logarithm is comparison only: its radius
obstruction, which holds even under RH, is not an input here.

### The moving cutoff causes a bounded total error

For k>=2 write

    q_k=P_k(X_k),    s_k=S_f(k),
    t_k=exp(-70*(k+1)^2),    T=sum_(k=2)^infinity t_k.

L981 gives |P_k(Y)-q_k|<=t_k for every real Y>=X_k.
For each fixed k separately, let Y tend to infinity. The audited
fixed-index conclusion of L982 and continuity of absolute value give

    |s_k-q_k|<=t_k.                                         (4)

The ratio t_(k+1)/t_k=exp(-70*(2*k+3)) is at most exp(-490)<1/2.
Thus the positive geometric majorant gives T<=2*exp(-630).
For any fixed n and every 2<=k<=n, X_n>=X_k, so

    |P_k(X_n)-s_k|
       <=|P_k(X_n)-q_k|+|q_k-s_k|<=2*t_k.

Summing these finitely many inequalities proves

    |sum_(k=2)^n s_k-(n-1)*a_n|<=2*T<=4*exp(-630).           (5)

This rechecks the exact interface needed from step235. For k=n
the first difference vanishes, but the coarser bound suffices.
The full endpoint weights and the compensator starting at 1 are
unchanged. The proof takes a limit at each fixed k before any finite
sum, and makes no assertion about a growing degree inside a limit.

### Direction and quantifiers of the cumulative Li bound

From the unconditional trend (2), choose a finite M>=0 such that

    |S_infty(k)+1|<=M*k^2,       k>=2.                       (6)

Such an M exists: log k<=k, the remainder in (2) is bounded for
all sufficiently large k, and the finitely many remaining values
can be included by enlarging M. No effective value is required.
It follows that |sum_(k=2)^n (S_infty(k)+1)|<=M*n^3.
Combining the exact split in (2), the upper side of (5) and (H),
for any delta>0 we obtain

    c_n=sum_(k=2)^n (S_infty(k)+1)-sum_(k=2)^n s_k
       >=-M*n^3-(n-1)*C_delta*exp(delta*n)-2*T.              (7)

The minus sign before S_f is essential: the hypothesis supplies
an upper bound on its sum and therefore a lower bound on c_n.
It does not give a two-sided bound or the individual Li criterion
by subtraction of consecutive means.

For an arbitrary epsilon>0 take delta=epsilon/2. The exponential
series gives exp(epsilon*n)>=(epsilon*n)^3/6 and
exp(epsilon*n/2)>=epsilon*n/2. Hence

    n^3<=6*epsilon^(-3)*exp(epsilon*n),
    (n-1)*exp(epsilon*n/2)<=(2/epsilon)*exp(epsilon*n).

Equation (1) follows from (7), for example with

    D_epsilon=1+6*M/epsilon^3
                  +(2/epsilon)*C_(epsilon/2)+2*T.           (8)

This is finite and positive for every epsilon>0 and covers every
n>=2. Finite degrees in (6) have been retained, not discarded.

### The ordinary Li partial-sum germ

Put H(z)=2*xi(1/(1-z)). By L018 it is holomorphic for |z|<1
and H(0)=1. It is nonzero on some disk about 0, where (3) is
normalized and analytic. Differentiating its convergent power
series locally and multiplying by z gives

    B(z)=z*H'(z)/H(z)=sum_(k>=1) lambda_k*z^k.               (9)

In a sufficiently small disk, also of radius less than 1, multiplying
the absolutely convergent series B(z)-lambda_1*z by the geometric
series 1/(1-z) is legitimate and yields

    F(z)=[z*H'(z)/H(z)-lambda_1*z]/(1-z)
        =sum_(n>=2) c_n*z^n.                                (10)

The coefficient at n>=2 is exactly sum_(k=2)^n lambda_k. The
constant and degree1 coefficients are zero; degree1 was explicitly
subtracted and has not been silently included in a_n. Conjugation
symmetry in L018 and the normalized real logarithm near 0 make
all lambda_k and c_n real. The quotient in (10) gives a single-valued
meromorphic continuation on |z|<1; it requires no global logarithm
branch and no summation of individual zero contributions.

### An off-line zero forces a nonremovable interior pole

Suppose RH is false. By L018, reflection rho -> 1-rho supplies a
nontrivial zero rho with Re rho>1/2. All such zeros have 0<Re rho<1
and are neither 0 nor 1. Its image w=1-1/rho satisfies

    |w|^2=|rho-1|^2/|rho|^2
         =1+(1-2*Re rho)/|rho|^2<1,                         (11)

and H(w)=0. The map s(z)=1/(1-z) has derivative rho^2!=0 at w,
so it preserves every positive zero multiplicity.

Choose one such image w_1. H is a nonzero holomorphic function
on a neighborhood of the compact disk |z|<=|w_1|<1. Its zeros
there are finite (otherwise compactness gives an accumulation point
in its holomorphy domain, contradicting H(0)=1). They are nonempty
and exclude 0. Choose w_* of smallest modulus among them and set
R=|w_*|. Then 0<R<1 and H has no zero in |z|<R. In particular
the expression (10) is holomorphic there and agrees with the Taylor
germ by the identity theorem. The Taylor radius of F is at least R.

Let m>=1 be the multiplicity of the zero at w_*. On a sufficiently
small disk around w_* there is a holomorphic nonzero function u with

    H(z)=(z-w_*)^m*u(z),
    H'(z)/H(z)=m/(z-w_*)+u'(z)/u(z).

Equation (10) therefore has a simple pole at w_* of residue

    m*w_*/(1-w_*),                                         (12)

which is nonzero because m>=1, w_*!=0 and w_*!=1. The analytic
term involving lambda_1 cannot cancel it. Thus the Taylor radius
of F is exactly R: a larger Taylor disk would analytically extend
(10) across this genuine pole. The argument permits arbitrary
orders and requires no separation estimate or zero simplicity.

### Positive-radius regularity and Pringsheim contradiction

For real 0<=x<1, s(x)=1/(1-x)>=1. L018 excludes xi zeros there
and gives xi(1)=1/2. Its reality and continuity therefore give
H(x)>0 throughout this interval, including H(R)>0. Since R<1,
choose a disk U about the positive real point R that lies in |z|<1
and contains no H zero. The expression (10) is holomorphic on U.
On U intersected with |z|<R it is exactly the same quotient already
identified with the Taylor germ. It is an extension of that germ
across R, not a newly chosen logarithm or a boundary value of a
different function.

Now choose epsilon=-(log R)/2>0 and put a=exp(-epsilon)=sqrt(R).
Then R<a<1. The universal quantifier in (1) supplies D_epsilon
from (8) for this epsilon; knowledge of an effective R is unnecessary.
The correction

    E(z)=D_epsilon*(z/a)^2/(1-z/a)
        =sum_(n>=2) D_epsilon*exp(epsilon*n)*z^n             (13)

is holomorphic on |z|<a. Hence K(z)=F(z)+E(z) has nonnegative
Taylor coefficients at every degree: the first two are zero, and
the remaining ones are c_n+D_epsilon*exp(epsilon*n)>=0 by (1).
It is analytic for |z|<R and retains the nonzero pole (12), since
E is analytic at w_*. Its Taylor radius is consequently exactly
the finite positive number R.

Shrink U so that it also lies in |z|<a. Both the continued F and E
are holomorphic on this U, so K extends holomorphically across the
positive point R. This contradicts the precisely cited Pringsheim
theorem, whose nonnegativity and finite-radius hypotheses have now
both been verified. The supposition that RH is false is impossible
under (H), proving the stated implication.

### Qualifications and stopping decision

The arithmetic bound (H) is wholly unpaid. The argument does not
establish it, individual P_k signs, all Q_n>=0, or actual-Xi mixed
positivity. Only the sufficiency question approved in review236 is
settled. The pole of s(z) at z=1, the zeta pole compensation in P_k, and
the +1 in (2) have not been discarded; z=1 stays outside every
interior disk used in the contradiction. No infinite degree sum
is exchanged with a prime limit, and no numerical evidence enters.

The step235 automatic two-sided smoothing stop and L983's lobe
counterexample remain in force on their original scopes. This
successful conditional criterion does not revive either automatic
payment claim. Further criterion-only reformulation is stopped
unless a distinct, independently testable payment mechanism is
identified and separately covered. The conceptual audit below must
not be confused with payment of (H) or validation of a complete RH
candidate.

### Independent conceptual audit — step240, 10 November 2026

This audit uses the unchanged SPECIALIZE scope in review238,
separately approved in step239. It checks the whole implication above,
not the unaudited inverse in L982's step235 application. The inspected
primary contracts are reused: Lagarias's exact split and unconditional
smooth trend, Voros's ordinary-Li germ, the named Pringsheim theorem,
and the cited elementary holomorphic-function facts. Their full
general proofs are not reproduced. L018 and the separately audited
L981 tail and L982 fixed-index limit supply the remaining local inputs.

**Cutoff, initial degree and endpoint audit.** The cutoff X_k is
increasing for every k>=2, and X_2=exp(810000). L981 applies with
the same complete prime-power terms and the same integral starting
at 1. At a fixed k, taking Y to infinity in its uniform inequality
uses only L982's fixed-index real limit, giving (4). For fixed n,
each X_n is admissible in that inequality, so the two comparisons
with q_k give 2*t_k. Here t_2=exp(-630), and for k>=2 the exact
ratio is exp(-70*(2*k+3))<=exp(-490)<1/2. Thus T<=2*exp(-630)
and the total error in (5) is at most 4*exp(-630), independent of n.
For n=2 the sum has one term and the difference P_2(X_2)-q_2
vanishes; the stated bound remains valid. This verifies all initial
and jump cases without changing any endpoint convention. There is
no growing-degree limit in this step: first a separate scalar limit
for each k, then a finite sum.

**Normalization, sign and quantifier audit.** The trivial GL(1)
specialization in L980 includes the pole contribution +1 and the
minus sign before S_f. Its coefficients are ordinary lambda_k;
normalizing the completion to 2*xi only adds a constant logarithm.
The source's fixed-function O(1) smooth remainder is bounded after
one finite onset. Each earlier S_infty(k) is finite, so enlarging M
covers every k>=2 in (6). In particular no initial Li sign is needed.
The upper side of (5) gives sum S_f(k)<=(n-1)*a_n+2*T.
Subtracting this from the smooth sum gives exactly (7), with a lower
bound, not an absolute bound, on c_n. For any given epsilon>0,
use (H) only with delta=epsilon/2. The two exponential-series
inequalities following (7) absorb n^3 and n-1 respectively. Since
exp(epsilon*n)>=1, the constant 2*T is also absorbed. Formula (8)
is consequently finite and positive, works for every n>=2, and
retains the required quantifier over every epsilon. No assertion
about consecutive-average subtraction is used.

**Local generating-function audit.** The map s(z)=1/(1-z) is
holomorphic in the unit disk. L018 gives H(0)=2*xi(1)=1,
so a normalized holomorphic logarithm exists on a small disk about
0. Formula (3) is the ordinary-Li expansion on precisely that germ;
z times its derivative has coefficients lambda_k, without a residual
factor k or 1/k. The subtraction of lambda_1*z removes the whole
degree-one term. Multiplication by 1/(1-z), within a common disk
of absolute convergence, therefore has coefficient c_n for n>=2
and coefficients zero for n=0,1. Reality follows from L018's
conjugation symmetry and the logarithm normalized to zero at 0.
Thereafter (10) uses the logarithmic derivative H'/H, which is a
single-valued meromorphic quotient; it needs no global logarithm.

**Interior radius and multiplicity audit.** If RH fails, the
reflection in L018 gives a zero rho with Re rho>1/2. Equation (11)
puts w=1-1/rho strictly in the unit disk, and w is neither 0 nor 1.
The derivative rho^2 of s at w is nonzero, preserving its positive
integer order. The compact disk determined by any one such w lies
strictly inside H's holomorphy domain. Its nonempty zero set is
finite by isolation and compactness, and omits 0 since H(0)=1.
Its minimal modulus R is also the global minimal zero modulus:
any smaller-modulus zero would belong to the same compact disk.
Thus 0<R<1 and the quotient (10) is holomorphic throughout |z|<R.

For a zero w_* of this modulus and arbitrary order m>=1,
factorization gives H'/H=m/(z-w_*)+u'/u with u nonzero locally.
Multiplication by z/(1-z) makes the residue m*w_*/(1-w_*),
which cannot vanish. The subtracted rational term is holomorphic
there. Hence the Taylor radius of F cannot exceed R: a larger
Taylor disk would give a holomorphic function agreeing with the
quotient on the nonempty inner part of a punctured neighborhood of
w_*, and uniqueness would remove its nonzero pole, a contradiction.
Combined with holomorphy in |z|<R this proves radius exactly R.
Distinct zeros cannot cancel this local residue, and multiple zeros
increase m rather than remove it. No zero count or simplicity is used.

**Same-germ continuation and Pringsheim audit.** For 0<=x<1,
the number s(x) is real and at least 1; L018 excludes all xi zeros
there, including the endpoint s=1. Reality, continuity and H(0)=1
give H(x)>0, so H(R) is nonzero. Take a small disk U about R
inside the unit disk with H nonzero. Its intersection with |z|<R
is nonempty, and the holomorphic expression (10) is the same
quotient on both regions. This gives continuation of the original
Taylor germ across R, not a branch selected after the fact.

Because R is strictly between 0 and 1, epsilon=-log(R)/2 is
positive and a=exp(-epsilon)=sqrt(R)>R. The universal quantifier
already proved in (1) permits this choice even though R is not
effective. The correction (13) is holomorphic on |z|<a and has
exact coefficients D_epsilon*exp(epsilon*n) for n>=2 and zero
for n=0,1. Thus K has real nonnegative Taylor coefficients at every
degree. E is analytic at w_*, so K retains the nonzero pole and
has finite positive Taylor radius exactly R. Shrink U into |z|<a;
F+E then extends the same K germ holomorphically across positive R.
These are exactly the contradictory conclusion and all hypotheses
of the imported Pringsheim theorem. The only assumed arithmetic
estimate in the contradiction is (H).

Audit decision: accept the conditional implication without changing
its proof or hypotheses. This validates a local REPRODUCTION input;
it is not a new arithmetic estimate or a result beyond the checked
standard methods. The proof's four direct local inputs are exactly
L018, L980, L981 and L982. L968/L976 and the step235/L983 stops
are comparisons, not premises. No DAG change is needed. Hypothesis
(H), actual-Xi positivity, and every independent payment mechanism
remain unresolved; there is no complete RH candidate to validate.

## Mathlib

Full matching Mathlib coverage for this moving-cutoff arithmetic
criterion, its cumulative germ and the Pringsheim application has
not been checked and is unknown. The precise mathematical references
are those cited above and in L981/L982. Supporting analytic facts
do not themselves supply the full specialization. No formalization
or absence-of-coverage claim is made.
