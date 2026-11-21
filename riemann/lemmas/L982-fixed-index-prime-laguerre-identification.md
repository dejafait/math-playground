# Lemma 982: fixed-index compensated prime-Laguerre identification

## Hypotheses

Let Lambda be the actual von Mangoldt function, with Lambda(1)=0.
Fix an integer n>=2. For every real X>1 define, as in L981,

    ell_n(u)=L_(n-1)^(1)(u),
    P_n(X)=sum_(2<=m<=X) Lambda(m)*ell_n(log m)/m
              -integral_1^X ell_n(log x) dx/x.

Include each prime power at the cutoff fully. Use the ordinary,
undivided, nonalternating convention of L977/L980:

    -zeta'(1+s)/zeta(1+s)-1/s=sum_(j>=0) eta_j*s^j,
    S_f(n)=sum_(j=1)^n binom(n,j)*eta_(j-1).

The Laurent expansion is local at s=0. No RH, simplicity, sign
condition, uniformity in n, or limit interchange in n is assumed.
L977/L980/L981 fix notation here; none of their mathematical
conclusions, contour arguments or error estimates is an input to
the fixed-index identification. The degree-average application
below additionally uses L981's quantitative tail estimate.

## Conclusion

For each fixed integer n>=2 the unrestricted real-endpoint limit is

    lim_(X->infinity) P_n(X)=S_f(n).                 (1)

The compensator in this statement starts at1, without an additive
constant, and all prime-power endpoints have full weight. This is
a REPRODUCTION specialization of the cited fixed-index moments and
finite Laguerre formula, not progress beyond those known inputs.
Written in step229, 10 November2026; the separate step231 audit below
accepts this fixed-index statement on exactly its stated scope.
It identifies the normalization needed to connect L981's tail to
S_f. It gives no n-uniform signed bound, Li positivity or RH result.
The step235 application below proves equivalence of two unpaid
two-sided subexponential thresholds with explicit cutoff and inverse
losses; it establishes neither threshold.

## Proof

### Precise imported statements and scope

Import J. C. Lagarias, *Li coefficients for automorphic L-functions*,
Ann. Inst. Fourier **57**(5) (2007), 1689-1740,
DOI10.5802/aif.2311: Definition4.3/(4.5), Lemma4.4/(4.8),
pp1708-1709, and the unnumbered eta-moment display immediately
after(4.13), [p1709](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=22).
For each fixed integer j>=0 it states, in the zeta case,

    eta_j=(-1)^j/j! * lim_(N->infinity) M_j(N),
    M_j(N)=sum_(2<=m<=N) Lambda(m)*(log m)^j/m
                      -(log N)^(j+1)/(j+1).         (2)

Here N runs through integers and its final term is included fully.
The omitted m=1 term is zero. Definition4.3/(4.5) and(4.8) match
the Laurent and S_f conventions above; the conflicting alternating
remark(4.13) is not imported. The primary moment statement, not the
unread original1999 convergence proof, is the cited external input.
There is no asserted rate uniform in j. This exact statement and
its applicability were assessed in review227, completed in step228.

Import also [NIST DLMF18.5.12](https://dlmf.nist.gov/18.5.E12),
specialized to nonnegative integer degree n-1 and parameter1:

    ell_n(u)=sum_(j=0)^(n-1)
                  binom(n,j+1)*(-1)^j*u^j/j!.        (3)

This is a finite polynomial identity, valid for every real u.
Only finite assembly and extension of the integer endpoints in(2)
are needed; neither cited theorem is reproved.

### Exact finite compensation and integer limit

For X>1 and each j>=0, the change of variable u=log x gives

    integral_1^X (log x)^j dx/x
       =integral_0^(log X) u^j du
       =(log X)^(j+1)/(j+1).                         (4)

Thus the lower endpoint contributes zero, also for j=0. Substituting
the finite expansion(3) in both parts of P_n, and using(4), gives
the exact identity for every real X>1

    P_n(X)=sum_(j=0)^(n-1) binom(n,j+1)*(-1)^j/j!
          *[sum_(2<=m<=X) Lambda(m)*(log m)^j/m
                            -(log X)^(j+1)/(j+1)]. (5)

All sums here are finite. By(2), lim M_j(N)=(-1)^j*j!*eta_j.
Taking N->infinity in the fixed finite sum(5) therefore gives

    lim P_n(N)
      =sum_(j=0)^(n-1) binom(n,j+1)
                      *((-1)^j/j!)*((-1)^j*j!)*eta_j
      =sum_(j=0)^(n-1) binom(n,j+1)*eta_j
      =S_f(n).                                      (6)

In particular both signs cancel and no extra factorial survives.
For n=2, (5) reads P_2(N)=2*M_0(N)-M_1(N), whose limit is
2*eta_0+eta_1, matching the stipulated convention. This check is
illustrative; the full finite calculation(6) proves every fixed n.

### All real cutoffs, including jumps

Let N=floor X. The sets of integers m<=X and m<=N coincide,
including when N is a prime power. Thus their complete arithmetic
sums agree exactly, and

    P_n(X)-P_n(N)=-integral_N^X ell_n(log x) dx/x.    (7)

For all sufficiently large N, log N>=1. For 0<=j<=n-1 and
N<=x<=N+1, (3), 1/j!<=1, and the binomial sum give

    |ell_n(log x)|
      <=(log(N+1))^(n-1)*sum_(j=0)^(n-1) binom(n,j+1)
      <=2^n*(log(N+1))^(n-1).

Since 0<=X-N<1 and 1/x<=1/N, (7) implies

    |P_n(X)-P_n(N)|
       <=2^n*(log(N+1))^(n-1)/N ->0.                 (8)

For an explicit fixed-degree justification of the last limit, put
t=log(N+1). Then N=e^t-1>=e^t/2 for N>=1, and the exponential
series gives e^t>=t^n/n!. The right side of(8) is consequently at
most 2^(n+1)*n!/t, tending to zero for this fixed n. These constants
are not used as n-uniform estimates. Equations(6)-(8) prove(1).

No prime-power jump was removed, halved or approximated: equality
of the finite sums in(7) handles each one. The pole compensation is
exactly that in(2) through(4). No infinite Laguerre expansion,
contour deformation or exchange of n and X limits occurs. Combining
this identification with quantitative tails or proving a one-sided
bound for their retained head is further work. In particular the
step224 signed-payment stop and the L975/L976 obstructions remain.

### Independent fixed-index audit — step231, 10 November2026

The complete proof above was checked under the pre-existing SPECIALIZE
assessment review229. The published Lagarias Definition4.3/(4.5),
Lemma4.4/(4.8) and the full moment display after(4.13) were reopened
at the cited primary PDF. The moment statement uses the same eta
as(4.12), the actual von Mangoldt function and an ordinary integer
partial sum, with its last term included. It is not the subsequent
formal automorphic series(4.15). The conflicting alternating(4.13)
is still excluded. The cited published moment statement suffices as
an imported result; the original1999 convergence proof remains unread.

DLMF18.5.12 was also reopened. For degree n-1 and parameter1 its
coefficient of (-u)^j is

    (j+2)_(n-1-j)/[(n-1-j)!*j!]
      =n!/[(j+1)!*(n-1-j)!*j!]
      =binom(n,j+1)/j!,            0<=j<=n-1.

Here the subscript denotes the rising factorial; when j=n-1 its
length is zero and its value is1. This verifies(3), including the
top coefficient. Multiplying each coefficient in(5) by the imported
moment limit gives binom(n,j+1)*eta_j: the two factors (-1)^j cancel
and the two factorials cancel. A finite number of convergent scalar
sequences suffices, since n is fixed. Reindexing j+1 agrees exactly
with the stipulated S_f and with the definitions in L977/L980.

The substitution in(4) has lower endpoint log1=0; its antiderivative
has value zero there even for j=0. Thus no constant is missing. The
definition of P_n agrees with L981, including complete prime-power
terms. For real X, N=floor X has the same arithmetic summation set.
If X=N is a prime power, both sets include that term and(7) is zero;
if N<X<N+1, no new integer occurs. These cases exhaust the endpoints.
For N>=3, log N>=1, so every power of log x in the finite polynomial
is bounded by (log(N+1))^(n-1). The binomial coefficient sum is
2^n-1<=2^n and 1/j!<=1, proving(8). With t=log(N+1), the subsequent
bound by 2^(n+1)*n!/t is valid and tends to zero for this fixed n.
This establishes the unrestricted real limit, including sequences
approaching either side of a prime-power jump.

Audit decision at step231: accept(1), with no correction to the mathematical
argument. This independently validates an existing REPRODUCTION
interface, not a new result beyond the cited inputs. That fixed-index
proof introduces no local theorem input: L977/L980/L981 there are used
only to compare definitions. The later step235 application adds L981
as a direct input to this file's DAG row. The step231 audit does
not combine L981 with this limit, exchange n and X limits, establish
any one-sided head estimate, or supply actual-Xi positivity. Its
downstream use is limited to an accepted normalization interface.

### Quantitative degree-average application — step235, 10 November2026

This is the bounded REPRODUCTION specialization approved by
drafts/literature/2026-11-10-prime-laguerre-average-recovery-test-review-234.md.
It is recorded here rather than creating a lemma for the elementary
Cesaro specialization. This application has not yet had a separate
critical audit; the original fixed-index proof above is unchanged
mathematically.

For integers n>=2 define

    X_n=exp(10000*(n+1)^4),   q_n=P_n(X_n),
    A_n(X)=(n-1)^(-1)*sum_(k=2)^n P_k(X),
    a_n=A_n(X_n),   s_n=S_f(n),
    b_n=(n-1)^(-1)*sum_(k=2)^n s_k,
    t_k=exp(-70*(k+1)^2),   T=sum_(k=2)^infinity t_k.

The arithmetic function, compensator and complete prime-power
endpoints are exactly those in the hypotheses above. No new sign
or analytic assumption is introduced. The conclusions are

    T<=2*exp(-630),
    |a_n-(n-1)^(-1)*sum_(k=2)^n q_k|<=T/(n-1),       (9)
    |q_n-s_n|<=t_n,   |a_n-b_n|<=2*T/(n-1).          (10)

For n>=3 there is an exact moving-cutoff inverse

    q_n=(n-1)*a_n-(n-2)*a_(n-1)-D_n,
    D_n=sum_(k=2)^(n-1) [P_k(X_n)-P_k(X_(n-1))],
    |D_n|<=2*T<=4*exp(-630).                         (11)

At n=2, q_2=a_2. Consequently these statements are equivalent:

    For every epsilon>0 there is a finite C_epsilon>=0 such that
    |q_n|<=C_epsilon*exp(epsilon*n) for every n>=2.    (Q)

    For every epsilon>0 there is a finite B_epsilon>=0 such that
    |a_n|<=B_epsilon*exp(epsilon*n) for every n>=2.    (A)

In the forward direction take B_epsilon=C_epsilon+T.
In the reverse direction take

    C_epsilon=(1+4/epsilon)*B_(epsilon/2)+2*T.         (12)

Proof of the specialization. L981 supplies, for every k>=2 and
every real Y>=X_k,

    |P_k(Y)-q_k|<=t_k.                              (13)

The cutoff increases with k, including X_2=exp(810000). Thus X_n
and X_(n-1) meet every lower cutoff used below, even at k=2.
For k>=2, t_(k+1)/t_k=exp(-70*(2*k+3))<=exp(-490)<1/2;
the geometric-series bound gives T<=2*t_2=2*exp(-630).
For fixed n, sum (13) at Y=X_n over 2<=k<n; the degree n
term is q_n itself. Finite triangle inequality gives (9).

For each fixed k separately take Y to infinity in (13), using
the real-endpoint limit (1). Continuity of absolute value gives
|s_k-q_k|<=t_k. This is a statement for every integer k, obtained
without any uniform-in-k limiting assertion. Finite averaging gives
|(n-1)^(-1)*sum q_k-b_n|<=T/(n-1). Together with (9) this proves
(10). No average with growing degree was passed through a limit.

Import William T. Ross, *The Cesaro Operator*,
[arXiv2210.08091v1, Proposition3.4, p7](https://arxiv.org/pdf/2210.08091v1#page=7).
On all complex sequences its arithmetic-mean matrix has inverse
with diagonal 1,2,3,... and subdiagonal -1,-2,-3,...;
no convergence or positivity hypothesis is required. The exact
theorem and proof were inspected in the reused review233.
At one fixed real X shift its index0 to degree2: x_j=P_(j+2)(X).
Its mean at index n-2 is precisely A_n(X), so its initial row
is A_2(X)=P_2(X), and subsequent inverse rows give

    P_n(X)=(n-1)*A_n(X)-(n-2)*A_(n-1)(X),  n>=3.    (14)

This specializes the cited inverse without reproving general
inversion. At X=X_n replacing A_(n-1)(X_n) by a_(n-1)
requires a correction; multiplying that correction by n-2 gives
exactly D_n in (11). For 2<=k<=n-2, (13) at X_n and X_(n-1)
gives |P_k(X_n)-P_k(X_(n-1))|<=2*t_k. At k=n-1 the second
value is q_(n-1), so (13) gives t_(n-1) instead. Therefore

    |D_n|<=2*sum_(k=2)^(n-2) t_k+t_(n-1)<=2*T.

For n=3 the first sum is empty; degree2 still satisfies (13).
All differences use complete real-cutoff sums, so prime powers at
an endpoint require no changed weight or omitted term.

Under (Q), the mean of |q_k| for k<=n is at most
C_epsilon*exp(epsilon*n). Equation (9) proves (A) with the stated
B_epsilon, since T/(n-1)<=T*exp(epsilon*n).
Conversely assume (A) and put delta=epsilon/2. For n>=3, (11) gives

    |q_n|<=2*n*B_delta*exp(delta*n)+2*T.

For x>0, exp(x)>=x, so n*exp(-epsilon*n/2)<=2/epsilon.
The last bound is at most

    [(4/epsilon)*B_(epsilon/2)+2*T]*exp(epsilon*n).

At n=2 use q_2=a_2 and B_(epsilon/2)*exp(epsilon)<=
B_(epsilon/2)*exp(2*epsilon). Formula (12) covers both cases.
Thus the inverse's linear loss is paid at every epsilon, rather
than replacing that quantifier by a fixed exponential rate.

The discriminating result is that first-order degree averaging
preserves the unpaid two-sided threshold. Ross's inverse, L981's
tail and this fixed-index limit supply no independent estimate for
a_n. Automatic first-order smoothing is stopped on this scope.
This does not exclude independent arithmetic bounds for a_n,
other averaging orders or one-sided bounds; those require their
own coverage. Actual-Xi positivity and signed Li forcing remain
open; no new RH-equivalence assertion is needed here.

## Mathlib

Full matching Mathlib coverage of the compensated eta-moment limit
and this real-cutoff identity has not been checked and is unknown.
The precise mathematical references used are Lagarias's displayed
fixed-index moment and DLMF18.5.12; no matching Lean theorem or
absence of one is claimed. No Mathlib search or formal verification
was needed for this finite specialization.
For the step235 moving-cutoff recovery application, full matching
Mathlib coverage is also unchecked and unknown. Ross Proposition3.4
is the precise additional reference. No formalization, absence claim
or progress beyond the cited methods is asserted.
