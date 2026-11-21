# Lemma 821: compact logarithmic-theta signed confluent minor

## Hypotheses

Let K be exactly the positive theta kernel of L019, let
m_0=integral_0^infinity K(u)du>0 as in L021, and define

    H(v)=e^v K(e^v)/m_0,       T(x,y)=H(x-y),
    Q_3(v)=det[partial_x^i partial_y^j T(v,0)]_(i,j=0)^2/H(v)^3.

Both collocation tuples in the translation-kernel convention increase.
The asserted domain is only 1/4<=u=e^v<=2.

## Conclusion

On this domain Q_3(v)>1/5. This is a computer-assisted compact
inequality: the complete interval certificate has 105 terminal
subintervals, no unresolved cells and a uniform lower endpoint
greater than 0.2180791770595388. The independent step614 audit below
verifies the proof, every terminal cell and the saved interval bounds
using exact-integer arithmetic independent of Decimal.

This verifies only one necessary confluent condition on the specified
compact domain. It asserts neither global TN3 of T, nonconfluent
minor signs, lower oscillation of a transformed function, nor Xi mixed
positivity. The positive normalization m_0 cancels exactly; no numerical
evaluation of m_0 and no zero-location assumption are used.

## Proof

**Source specialization and sign.** Thomas Simon, *Total positivity of
a Cauchy kernel*, arXiv:1305.1173v1 (6 May 2013),
[Section 3, equation (7) and its finite-difference argument, printed
pp.6–7](https://arxiv.org/pdf/1305.1173v1), supplies the necessary
confluence condition. Its row/column finite-difference argument applies
to a smooth real kernel; its Cauchy parameter classification is not used.
L016 and the derivative bounds below give the required continuous mixed
derivatives through total order four on a neighborhood of each (v,0).
Both Vandermonde factors for increasing collocation tuples are positive.
Thus TN3 would require the mixed derivative determinant to be
nonnegative at every such point. This imports the necessary condition,
not any global sufficient criterion.

Here partial_x^i partial_y^j T(v,0)=(-1)^j H^(i+j)(v).
The product of the column signs is (-1)^(0+1+2)=-1. Put ell=log H.
Multiplying H locally by exp(-ell'(v) times the argument) corresponds
to triangular row and column operations of determinant one in the
normalized ordinary derivative Hankel matrix. Equivalently, substitute
H'/H=ell', H''/H=ell''+ell'^2 and their next two derivatives directly.
After removal of ell', that matrix is

    [ 1       0          ell''                    ]
    [ 0       ell''      ell'''                   ]
    [ ell''   ell'''     ell''''+3(ell'')^2        ].

Its determinant is ell''ell''''+2(ell'')^3-(ell''')^2.
Including the column signs therefore gives the exact identity

    Q_3=(ell''')^2-ell''ell''''-2(ell'')^3.                 (1)

Constant positive scaling of H cancels from all derivative ratios and
from the determinant divided by H^3. The same is true for the local
exponential multiplication just used: its derivative transformations
are triangular with diagonal one after division by its value. This
justifies both eliminations without changing the translation orientation.

**Stable actual-kernel derivatives.** Set D=u d/du=d/dv,
c=pi exp(2u), a_n=n^2 c, p(a)=8a^2-12a, and

    B(u)=sum_(n>=1) p(a_n) exp(-(a_n-c)).

The series of L019 gives the exact factorization

    m_0 H(v)=u exp(u/2-c) B(u),
    ell(v)=v+u/2-c+log B(u)-log m_0.                       (2)

All summands of B are positive. In particular its denominator can be
bounded using p(a)=4a(2a-3), since a>=c>5 on the tested domain.
This factorization avoids subtracting enormous derivatives of exp(-c).

Define polynomials R_j in the three independent variables (u,a,c) by

    R_0=8a^2-12a,
    R_(j+1)=u partial_u R_j+2ua partial_a R_j
            +2uc partial_c R_j-2u(a-c)R_j.                 (3)

Because Da_n=2ua_n and Dc=2uc, repeated differentiation gives

    D^j B=sum_(n>=1) exp(-(a_n-c)) R_j(u,a_n,c),  0<=j<=4. (4)

The interchange in (4) is justified below, including the endpoints
through locally uniform bounds in a neighborhood, not by a finite grid.
For r_j=(D^j B)/B, the derivatives of log B needed in (1) are

    b_2=r_2-r_1^2,
    b_3=r_3-3r_1 r_2+2r_1^3,
    b_4=r_4-4r_1 r_3-3r_2^2+12r_1^2 r_2-6r_1^4.

Since D^j(v)=0 for j>=2, (2) gives

    ell''   =u/2-c(2u+4u^2)+b_2,
    ell'''  =u/2-c(2u+12u^2+8u^3)+b_3,
    ell'''' =u/2-c(2u+28u^2+48u^3+16u^4)+b_4.              (5)

These identities use only chain/product rules and the actual theta
series. They do not import L795's interlacing premise or L738's model.

**Uniform differentiated tails.** The polynomial R_j has u-degree at
most j and total (a,c)-degree at most j+2. If its coefficient of
u^i a^h c^k is beta_(i,h,k), let A_j be the sum of
abs(beta_(i,h,k))2^i. Recurrence (3), with these degree bounds, gives

    A_0=20,     A_(j+1)<=(5j+16)A_j.

Indeed the four contributions are bounded respectively by
j A_j, 4(j+2)A_j, and 4A_j+4A_j for the two drift terms.
Thus valid successive majorants, through j=4, are

    C_j = 20, 320, 6720, 174720, 5416320.                  (6)

For 1/4<=u<=2 the interval arithmetic specified below proves

    5 < pi exp(1/2) <= c <= pi exp(4) < 200.

For n>=9, a_n>=c>=1 and c<=a_n, so each monomial and (6) give

    |R_j(u,a_n,c)| <= C_j a_n^6 <= C_j 200^6 n^12.

Consequently, for every 0<=j<=4, the absolute tail after n=8 in
(4) is bounded by

    E_j=2 C_j 200^6 9^12 exp(-400).                        (7)

To see this, use exp(-(a_n-c))<=exp(-5(n^2-1)). Consecutive terms
t_n=n^12 exp(-5(n^2-1)) obey

    t_(n+1)/t_n <= 2^12 exp(-95) < 1/2,  n>=9.

Hence their sum is at most 2t_9. Formula (7) bounds *every* required
derivative tail, rather than reusing an undifferentiated estimate.
On any slightly larger compact interval of positive u, the same
polynomial recurrence and c>=c_min>0 give a summable majorant
constant times n^12 exp(-c_min(n^2-1)). Together with L016 this
justifies termwise differentiation through order four and smoothness
in neighborhoods of the evaluation points. No behavior at u=0 or
u=infinity is used.

**Rigorous interval computation.** Reproduction command, relative to
this notebook:

    python3 scripts/log-theta/confluent_compact_612.py

Full evidence is saved in `scripts/log-theta/confluent_compact_612.json`:
polynomial coefficients, constants, derivative tails, all finite and
full derivative enclosures, log derivatives, all 105 closed terminal
cells, their Q_3 enclosures, point tests, and verification/failure fields.
The implementation uses Python's standard `decimal` module at precision
90. Addition, subtraction, multiplication and reciprocal endpoints are
rounded outward with ROUND_FLOOR/ROUND_CEILING; nonnegative integer
powers use repeated interval multiplication. The correctly rounded
ROUND_HALF_EVEN exponential is widened by one representable neighbor
on each side in the same 90-digit context. All numbers encountered are
finite and within that context's exponent range. Inputs and dyadic
subdivision endpoints are exact rational numbers, converted outward.

Pi is enclosed by Machin's identity
pi=16 arctan(1/5)-4 arctan(1/239), with 120 and 40 exact rational
alternating-series terms respectively; the first omitted term bounds
each remainder with its sign. For completeness the angle identity
follows from tan(4 arctan(1/5))=120/119 and the subtraction formula:
tan(4 arctan(1/5)-arctan(1/239))=1. This angle lies in (0,pi/2),
fixing it as pi/4. No decimal digits of pi are assumed.

For each interval the script substitutes a=n^2 c into (3) exactly
before interval evaluation, sums n=1,...,8, then adds [-E_j,E_j]
using an outward upper endpoint for each E_j. It verifies B>0,
forms (5) and (1), and accepts a cell only when its Q_3 lower
endpoint is nonnegative. Otherwise it bisects in u, keeping the exact
rational partition; at the cap it would preserve all unresolved cells.
Five rigorous point tests are also recorded, but establish no covering
claim and are not used as a substitute for interval bounds.

All 105 terminal cells were accepted, with no unresolved cell; their
ordered rational endpoints are checked to join exactly from 1/4 to 2.
Every stored interval is ordered and all stored Q_3 formulas are
recomputed from their full log-derivative enclosures. The smallest
lower endpoint is

    0.2180791770595388979997650478420369128321815387879863260862710109099855592853038326426558

on u in [291/1024,589/2048]. It exceeds 1/5. Thus interval containment
and exact coverage prove the asserted bound throughout the compact
domain, conditional only on the stated arithmetic implementation.
One initial implementation failure is retained in the certificate:
expanding B_0 on the whole domain gave a spurious zero denominator.
Using the identical positive factorization 4a(2a-3) repaired it before
any conclusion. There are no unresolved arithmetic failures.

This is the local result of the approved bounded attempt, not a claim
of progress beyond all existing literature. The prior source search did not locate this exact
H-coordinate compact inequality; that search does not establish novelty.
The independent signed mechanism, unbounded integral interface,
global minors and all-degree Xi positivity remain open.

**Independent proof and complete-certificate audit (step614).**
The audit retains the original statement and margin; it introduces no
new kernel, parameter range or sign-transfer theorem. L016/L019 supply
the actual series and its regularity; only finiteness and positivity of
m_0 are used from L021. In particular no assertion about Xi zeros or
L795's polynomial roots enters this proof. Simon's cited necessary
confluence argument is reused, not reproved or promoted to sufficiency.
The mixed partials have the column signs 1,-1,1, whose product is -1.
The triangular transformations eliminating ell' have unit diagonal;
the resulting ordinary Hankel determinant is the negative of (1).
The factorization (2), all three chain-rule formulas (5), and the five
tail estimates (7) have been independently checked.

In the tail recurrence, u partial_u contributes at most j A_j,
the two a/c derivative terms together at most 4(j+2)A_j, and
the two multiplication terms at most 4A_j each. This gives exactly
5j+16, with no missing c derivative. The independently generated
coefficient norms are 20,272,4688,95696,2233296, each bounded by
(6). Both degree bounds hold for every monomial. The inequality
a>=c>=1 makes total (a,c)-degree at most six sufficient for every
j<=4, and the ratio estimate applies starting at the first omitted
term n=9. Bounds on a slightly larger positive-u compact interval
justify derivatives also at both closed-domain endpoints.

The original arithmetic implementation was reviewed operation by
operation. Its reciprocal formula is valid on either side of zero;
negation uses the exact copy_negate operation, so no default-context
rounding is introduced. Rational conversions are directed, powers use
only interval products, and all exp/neighbor calls use the same explicit
90-digit context. The contracts are documented in the
[Python 3.15 Decimal reference](https://docs.python.org/3.15/library/decimal.html),
Decimal.exp, next_minus/next_plus, Context, rounding modes and signals
(page identifying 3.15.2, inspected in step613). No exceptional
underflow, overflow, clamping, subnormal, invalid-operation or
division-by-zero flag occurred in the complete replay. These contracts
explain the original arithmetic; the independent verification below
does not call Decimal for its enclosures.

Reproduce the independent audit with

    python3 scripts/log-theta/confluent_compact_audit_614.py

It represents each interval as [L/S,U/S], where L,U are exact integers
and S=2^1024. Addition and negation are exact. Multiplication takes the
minimum and maximum of the four integer products and rounds their
quotients by S down/up. For positive endpoints a reciprocal has bounds
floor(S^2/U)/S and ceil(S^2/L)/S; negative intervals are reduced by exact
negation. Division by a positive integer rounds the integer endpoints
directly. Thus every basic operation encloses its exact real operation.
There is no fixed-exponent overflow or floating-point underflow.

For an exponential at a rational endpoint x, choose r>=0 so
z=|x|/2^r<=1. Compute sum_(k=0)^240 z^k/k! with the above intervals.
Taylor's series has a nonnegative remainder at most 2/241!: its first
omitted term is at most 1/241!, and successive term ratios are at most
1/242<1/2. Round that bound upward to the integer lattice and add it
only to the upper endpoint. If x<0, take the interval reciprocal;
then square r times. Exponential monotonicity supplies interval-input
bounds from the two endpoints. This proves containment independently
of any library exponential implementation, including when a lower
endpoint rounds to zero. Pi is recomputed from the exact alternating
rational sums and the Machin identity already justified above.

For an independent polynomial check, work formally modulo t^5 and put
Z(t)=exp(2u(exp(t)-1)). The j-th coefficient, multiplied by j!, of

    [8a^2 Z(t)^2-12a Z(t)] exp(-(a-c)(Z(t)-1))

equals R_j, since u(v+t)=u exp(t), a(v+t)=a Z(t) and
c(v+t)=c Z(t). All truncated series operations use exact rational
polynomial coefficients. This independently generates precisely every
coefficient stored for R_0,...,R_4, without calling recurrence (3).
Every degree bound and coefficient majorant is then checked.

The full audit artifact `scripts/log-theta/confluent_compact_audit_614.json`
stores the independent polynomial coefficients, constants, tails and
all 110 rows (105 covering cells and five non-covering point tests).
All 1650 scalar intervals for c, finite/full B jets, log derivatives
and Q_3 were recomputed. Each independent interval lies wholly inside
its original saved interval, with no failed containment and no omitted
row. All five independent tail intervals, the pi interval, global c
interval and geometric-ratio bound likewise lie inside their original
enclosures. Exact rational checks verify positive cell widths, matching
adjacent endpoints, the entire [1/4,2] cover and the 2048-cell cap.
Every terminal Q_3 lower endpoint exceeds 1/5. The saved minimum and
its weakest-cell record agree exactly with the minimum quoted above.

The same command replays the original program into
`scripts/log-theta/confluent_compact_replay_614.json`; every top-level
field equals the original certificate, including its runtime field.
The original script and certificate are preserved. The report records
the original certificate's SHA-256, zero verification failures and PASS.
The earlier resolved denominator-enclosure failure remains recorded.
The original Decimal certificate is therefore reproducible, and its
enclosures also have an independent exact-integer verification. Usual
trust in the stated Python integer/rational implementation, execution
and hardware remains; this is not a proof-assistant or hardware audit.
No stronger compact margin, global TN3, lower-oscillation theorem or
progress beyond the existing sign claim is asserted by this audit.

## Mathlib

Full matching coverage is unchecked. No Mathlib theorem for this
particular logarithmic-theta compact determinant bound or its decimal
certificate is claimed. L016 records supporting smooth-series/theta
coverage; that is not full coverage of this statement. The confluence
input is the precise Simon citation above, used only as a necessary
condition, not a formalized global positivity theorem.
