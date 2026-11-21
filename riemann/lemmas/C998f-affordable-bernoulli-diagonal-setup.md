# C998f: Affordable finite Bernoulli-corrected diagonal setup

## Hypotheses

Use C998a's unchanged exact definitions: ell=log(3)/2,
k_n=n*pi/ell, h(k)=Re psi(1/4+ik/2)-log(pi), and the three real
finite trial vectors q_j. Their254 free coefficients, n=2,...,255,
are the exact binary rationals in `free_middle_dyadics` of
`scripts/separation-seven/frozen-reference-proposal-652.npz`, SHA256
`2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6`.
The remaining coefficients are zero except the two exact neutral
completion coefficients of C999q. No rounded raw vector defines q_j.
Use664's scalar work unit: one real/integer addition, subtraction,
multiplication, division, comparison or assignment at the prescribed
bounded precision. Complex, elementary and rational calls are expanded.
This counts mathematical setup, not wall time or byte-level file I/O.

Invocation-start continuation665, separately approved666, licenses this
REPRODUCTION with K in {16,32,64}, first omitted Bernoulli index N in
{4,8,16}, fractional precision in {128,256,512}, and16384-bit registers.
Only K=16,N=8,P=128 is tested. This is not new digamma mathematics.

Import Johansson, *Arbitrary-precision computation of the gamma function*,
[arXiv:2109.08392v1](https://arxiv.org/pdf/2109.08392v1),
Sections3.1-3.2, printed pp12-14, (25)-(32), Theorems3.1-3.2,
including Theorem3.2's proof. For N>=1, w outside (-infinity,0],

    psi(w)=Log(w)-1/(2w)
           -sum_(j=1)^(N-1) B_(2j)/(2j w^(2j))+R'_N(w),
    |R'_N(w)|<=sec(arg(w)/2)^(2N+1)|B_(2N)|/(2N|w|^(2N)). (1)

Also import [DLMF5.5.2](https://dlmf.nist.gov/5.5#E2),
psi(z+1)=psi(z)+1/z, and the convention
[DLMF24.2.1](https://dlmf.nist.gov/24.2#E1),
t/(exp(t)-1)=sum B_j t^j/j!. The corresponding complex remainder
qualification is [DLMF5.11(ii)](https://dlmf.nist.gov/5.11#ii).
These general results are cited, not reproved. Source-notes665 records
the inspected hypotheses and derivative proof case. Its elementary
inclusion coverage permits the explicit finite elementary series below;
no library accuracy claim or asymptotic complexity estimate is imported.

## Conclusion

One uniform finite prescription returns128-fractional-bit dyadics H_n,
for ALL n=0,...,255, with separate errors

    |h(k_n)-H_n| <= A+E_n,
    A = 248558347354112/25891301779435861122894287109375
      <9.601e-18 <2^-45,
    max E_n =102/2^128 <2.998e-37 <2^-47.                (2)

It also constructs the exact-neutral q_j coefficient enclosures and
all768 finite normalized-cosine coefficients of Dq_j, retaining (2)'s
analytic remainder separately. A conservative complete shared scalar
setup bound is8161000<10000000 operations. Observed evaluator operands
have at most1596 bits; the construction below gives a2048-bit bound,
below the16384-bit cap. There is no adaptive precision or parameter loop.

This removes the tested scalar setup prerequisite. It does not certify
any residual Gram entry, interior quadrature work, inverse debt size,
signed S3 pairing or RH. C998e's full product/error argument is not an
input and remains unaudited. Its first-order prescription stop is retained.
The inherited source-to-Xi, analytic/arithmetic, whole-core and unreplayed
c_* contracts are not independently verified. Audit669 below upholds this
finite setup result; (2) is local known-method specialization, not a new
source theorem.

## Proof

### 1. Exact argument, formula and analytic error

Set y=k_n/2, z=1/4+iy, w=65/4+iy. All sixteen recurrence arguments
z+j have positive real part, hence avoid every pole. The shifted w
lies in the open right half-plane, so its principal logarithm is
unambiguous, |arg(w)|<pi/2, |w|>=65/4. Formula (1) applies for N=8.
Since sec(arg(w)/2)<sqrt(2) and 2^(17/2)<512, its error is bounded by

    A=512 |B_16|/[16(65/4)^16], B_16=-3617/510,           (3)

which gives exactly the rational in (2). This is evaluated at the
EXACT mathematical argument; it uses no approximate frequency or sector.
It applies also at n=0. Taking real parts does not enlarge the error.

Write F_n for the following exact elementary real expression:

    F_n=(1/2)log((65/4)^2+y^2)
         -(1/2)Re(w^-1)
         -sum_(j=1)^7 [B_(2j)/(2j)] Re(w^(-2j))
         -sum_(j=0)^15 (j+1/4)/[(j+1/4)^2+y^2]-log(pi). (4)

The recurrence gives |h(k_n)-F_n|<=A. Negative powers in (4) are
computed from w^-1=((65/4)-iy)/((65/4)^2+y^2), squaring once and
multiplying successively. No complex logarithm, sign estimate or
log-gamma relative error is substituted. The remaining task is a
finite arithmetic enclosure of F_n, not a new remainder theorem.

### 2. Constants and elementary truncations

Let S=2^128. An interval [l,u] represents [l/S,u/S] with integer
endpoints. Rational conversion uses floor(aS/b),ceil(aS/b), b>0.
Addition/subtraction use the appropriate endpoint sums/differences.
Multiplication takes the extrema of the four exact integer products,
then divides by S outward. Division, only by intervals excluding zero,
takes the outward extrema of all four endpoint quotients aS/b.
Thus each operation contains the exact real result for all admitted
inputs; induction pays input uncertainty, dependency overestimation,
coefficient rounding, arithmetic rounding and summation together.
This is elementary interval inclusion; it promises no cancellation.

For100 terms use the finite polynomials

    P(t)=2t sum_(j=0)^99 t^(2j)/(2j+1),
    Q(x)=x sum_(j=0)^99 (-x^2)^j/(2j+1).                (5)

Horner evaluation uses shared outward enclosures of1/(2j+1).
Integrating a finite geometric identity on [0,t] gives

    |log((1+t)/(1-t))-P(t)|
       <=2|t|^201/[201(1-|t|^2)] for |t|<1.             (6)

This elementary finite-tail calculation explains the specialized
constant; no divergent expansion is being summed. In particular the
right side for |t|<=1/2 is less than2^-190. Integrating the alternating
geometric identity for1/(1+x^2) similarly gives
|atan(x)-Q(x)|<=x^201/201 for0<=x<=1.

Construct pi=16 atan(1/5)-4 atan(1/239), with the two stated tails.
For completeness this elementary identity is exact: if a=atan(1/5),
tan(2a)=5/12, tan(4a)=120/119, and for b=atan(1/239),
tan(4a-b)=(120/119-1/239)/(1+120/(119*239))=1.
Also0<4a-b<4/5<pi/2, and thus4a-b=pi/4. One can check positivity
from a> (1/5)/(1+1/25) and b<1/239; pi>2 follows, for example,
from4 integral_0^1 (1+t^2)^-1 dt>2. No unverified decimal pi is used.

Construct log(2)=P(1/3) and log(3)=P(1/2), each widened by2^-190,
then ell=log(3)/2. For every positive logarithm argument X used here
(pi and the256 squared norms in (4)), divide its interval by2 until
its upper endpoint is at most2. The final interval Y is checked to
lie in[1/2,2]. If m divisions were used, compute

    log(X)=log(Y)+m log(2),
    log(Y)=P((Y-1)/(Y+1))+error, |error|<2^-190.         (7)

The tail applies to each exact reduced argument since its transformed
t lies in[-1/3,1/3]. Arithmetic uncertainty in t is enclosed through
polynomial evaluation, rather than inserted into the exact-argument
tail without justification. The wider1/2 tail in (6) covers all calls.
Widening by a rational rounds its radius upward on the dyadic grid.

Bernoulli numbers through16 are generated from their defining series:
B_0=1 and sum_(j=0)^m binom(m+1,j)B_j=0 for m>=1. Each rational
sum is reduced using explicit integer Euclid; there is no opaque
Bernoulli call. This gives B_16=-3617/510. All seven coefficients in
(4) are converted outward. This modest specialization is necessary
to pay coefficient generation rather than assume an exact table free.

### 3. Every output and the exact neutral assembly

The script evaluates k_n=n*pi/ell, y=k_n/2, and (4) using only those
interval primitives, finite loops and elementary truncations. Its
checks include ell in(1/2,3/5), pi in(3,4), all log reductions and
all nonzero divisors. By the preceding inclusion proof, its interval
[l_n,u_n]/S contains F_n. Return H_n=floor((l_n+u_n)/2)/S, keeping
the SAME128-fractional-bit grid. Then

    |H_n-F_n|<=ceil((u_n-l_n)/2)/S=:E_n.                (8)

The complete256-entry table is stored, with both endpoints, H_n,
E_n, A and total error per mode. All256 checks E_n<=2^-47 pass;
their maximum is exactly102/S. This includes every error in (4),
including all constants, input frequencies, logs, negative powers,
Bernoulli coefficients, recurrence sum, elementary tails and rounding.
There is no sampling in n or an assertion about continuous frequencies.

For each free trial vector u, C999q's exact completion is

    u_p=-sum_(n>=2,n mod2=p) r_n u_n, p=0,1,
    r_n=(nu_n/nu_p)(1/4+k_p^2)/(1/4+k_n^2).             (9)

For odd n, nu_n/nu_1=1; for even n, nu_n/nu_0=sqrt(2).
The code encloses sqrt(2) by129 exact integer bisections starting
with[S,2S], comparing mid^2 with2S^2. The resulting endpoints have
width at most one integer unit. All254 ratios are checked in(0,1).
All762 frozen free dyadics are checked against complete654 and its
audit655, as well as the unchanged archive pin; they are exactly
representable on the128-bit fractional grid. Formula (9) is evaluated
by intervals, so its exact moment cancellations are retained in the
definition, irrespective of the widths of its numerical coefficients.

Multiply these completed q_j coefficients by the numerical intervals
for F_n. If Q_nj is the completed coefficient interval, append
an outward128-bit dyadic upper bound on the analytic radius
A sup_{v in Q_nj}|v|. The returned Dq centers are again
rounded to the128-bit grid and their rounding is included in the
stored total radii. Thus every one of the768 finite Dq coefficients
is enclosed. This constructs coefficients in the normalized cosine
basis; evaluating cosine sums at quadrature points is separate work.

### 4. Full finite scalar work and register ledger

The executable mathematical algorithm is the interval evaluator above,
not its optional JSON serialization, hash calculation or proof diagnostics.
Input consists of the762 exact dyadics; decoding and copying them is paid.
All256 diagonals, including the unused-for-free-input modes0,1, are paid
once and shared. Three completions and all768 Dq coefficients are paid.
No library special-function or complex call counts as one scalar operation.

For clarity a deliberately generous template charges64 scalar operations
per interval primitive, rational conversion, widening, reduction iteration
or bisection iteration. For the largest template, signed division, there
are four numerator multiplications, eight integer divisions, eight
negations, six min/max comparisons, and at most32 endpoint/control/cache
assignments or comparisons, totaling at most58. Integer floor division
is one division with its prescribed directed rounding convention. A
remainder for Euclid is charged as division, multiplication and subtraction. Addition,
multiplication (four products), conversion and the other templates are
smaller. Loop indices, list slots and returned interval endpoints are
included in the template; proof-only instrumentation is unnecessary to
execute the mathematical algorithm. Bisection needs no square-root call.

The complete call inventory is:

| Template | Calls |
| --- | ---: |
| rational conversion |5745|
| multiplication |47732|
| negation |258|
| addition |34797|
| widening |261|
| subtraction |7676|
| division |10165|
| log range reduction |4021|
| sqrt bisection |129|
| Dq error radius assembly |768|
| total |111552|

Exact Bernoulli generation and coefficient reduction are paid separately:
64 for each rational-reduction call plus8 for EVERY Euclid iteration,
and64 for each triangle iteration's remaining binomial/arithmetic/control
work. Their recorded total is21672, without a unit-cost rational call.
An additional1000000-operation reserve is broken down explicitly:

| Additional setup | Upper charge |
| --- | ---: |
| constants and exact elementary-tail construction |20000|
| all762 input dyadic decodes/copies |100000|
| cached tables, output centers and radii |100000|
| remaining loop/index/branch/precision management |100000|
| conservative padding |680000|

These bounds can be checked directly from the finite design: fewer than
1024 scalar multiplications/divisions suffice to construct every literal
power/tail; each of762 dyadic decodes needs at most128 operations (the
exponent/mantissa decoding is finite); fewer than10000 stored scalar
endpoints/centers/radii need fewer than10 operations each. The remaining
control work is already in the64-operation templates; the100000 is
additional reserve, not a new uncharged evaluator. Constants sqrt(2),
log(2), log(3), pi, log(pi), frequency tables, Bernoulli coefficients,
three completion tables and Dq table writes are therefore all included.
There is one precision initialization and no precision doubling.

The total is64*111552+21672+1000000=8161000. This is an upper bound,
not a mandatory lower bound or timing benchmark. The previous664
mandatory cost bound applies to its different first-order prescription.

Integer endpoints have fewer than160 bits; products/scaled quotients
have fewer than320 bits. The larger exact constants arise only from
the finite atan-tail denominators201*239^201 (<2^1600), plus their
bounded scale products (<2^1730). Bernoulli arithmetic through16 is
smaller. Thus2048-bit integer work registers suffice; the instrumented
evaluator actually observes at most1596 bits. All fractional interval
precision is128 bits, including returned centers. The bit cap is checked;
this is a scalar-operation ledger, not a claim of constant bit complexity.

### 5. Reproduction, inspection and scope

Run `python3 scripts/separation-seven/higher-order-diagonal-667.py`.
Its full certificate is `scripts/separation-seven/higher-order-diagonal-667.json`.
It stores all256 intervals, all three completed coefficient and Dq
tables, every1282 finite check, failure list, source input pins and
the generator hash. All checks pass and the failure list is empty.
Full analytic, arithmetic, work and failure fields were inspected,
including the exact Bernoulli list and maximum numerical radius.
The table is generated by a proved inclusion recurrence; its radii
do not come from comparison against an uncertified reference value.

This pays exactly the approved finite setup target. It does not replay
the original source/core/c_* claims or audit the full C998e Gram product.
There is no current actual residual-size or inverse-debt certificate.
Higher/mixed endpoints, C744q/H2, non-neutral coverage and global assembly
remain independent gaps. No off-line zeta zero or full RH argument is
claimed, and no cross-notebook input is used.

### 6. Independent proof and finite-ledger audit669

This audit uses the invocation-start SPECIALIZE review667, separately
approved668, and reuses source-notes665/approval666 and elementary
coverage658. It imports no new theorem. The Johansson derivative remainder
quoted in the hypotheses is the required derivative case, with first
omitted index8, principal argument and exact w=65/4+ik_n/2. Its cut-plane
and N>=1 hypotheses hold, including n=0. The right-half-plane bound
sec(arg(w)/2)^17<2^(17/2)<512 and |w|>=65/4 yield (3) without substituting
an interval midpoint for w. The sixteen recurrence subtractions have
the correct minus sign and no pole. The real logarithm of the squared
norm in (4) is exactly Re Log(w); negative powers are complex products,
not products of their real parts.

For the elementary computation, integrating the finite geometric
identities gives precisely (6) and the stated atan tail; the log tail
is symmetric in the sign of t. The rational inequality at |t|=1/2
was independently checked. The tangent calculation in Section2, together
with 0<4atan(1/5)-atan(1/239)<4/5<pi/2, fixes the Machin branch. Positive
log arguments and every reduced interval in[1/2,2] are checked in the
finite replay, with at most19 reductions. Consequently the exact
transformed argument is in[-1/3,1/3]. Rounding of its enclosure is paid
by polynomial interval inclusion, independently of the exact-input tail.
For signed division, extrema of endpoint quotients are valid because
the denominator interval excludes zero; ceil(x)=-floor(-x) is valid
for either sign of the denominator. The midpoint floor has maximal
endpoint distance ceil((u-l)/2)/S even when u-l is odd. Thus none of
the dyadic radius formulas loses a half unit.

The independent program
`scripts/separation-seven/higher-order-diagonal-audit-669.py` imports no
previous evaluator. It performs endpoint operations as exact rational
operations followed by floor/ceil quantization, builds Bernoulli numbers
by a separate binomial recurrence, and verifies sqrt(2)'s endpoints by
integer square root and exact square comparisons. The square-root call
belongs only to the verifier: the audited algorithm still uses129 paid
bisections. It compares all17 Bernoulli numbers, all256 complete mode
records, all762 exact free dyadics against654 and the pinned NPZ,
all254 ratio enclosures, all768 completed q coefficient enclosures and
all768 Dq intervals, rounded centers and total radii. All match. The
maximum arithmetic radius remains102/S. Source pins,655's pin of654
and generator667's hash also agree;655's analytical audit is retained
as an input, not repeated here.

The normalization factors in (9) agree with C999q: nu_n/nu_1=1 for
odd n and nu_n/nu_0=sqrt(2) for even n>=2. The exact two moment ratios
therefore define the completed trial, rather than a numerically neutral
surrogate. The replay's coefficient interval contains that exact trial.
Multiplying by the F_n enclosure pays both trial uncertainty and all
elementary errors. The additional radius A sup|Q_nj| pays the remaining
analytic digamma error. Rounding the center is paid separately by the
ceil-half-width formula. This proves inclusion of every Dq coefficient;
no orthogonality or independence between coefficient errors is assumed.

The ledger was checked as a mathematical scalar algorithm, with byte
I/O, hashing, serialization and proof diagnostics excluded as prescribed.
All111552 template counts agree independently. A signed division can
be expanded into four lower and four upper directed endpoint candidates:
with candidates stored once, their arithmetic, stores, extrema comparisons
and conditional updates use at most44 operations. At most14 further
input/domain/endpoint/control operations give58, within the64 charge.
It can be unrolled, so there is no hidden four-pair iterator requirement.
Multiplication, rational conversion, sum/difference, negation and widening
use smaller templates. Range reduction has its division separately
charged; Dq radius assembly has its interval multiplication separately
charged and fewer than32 remaining arithmetic/control operations.
Bisection, including its integer squares and bracket update, also fits64.
Horner's loop/index and result storage fit the unused template allowances.
Thus template counts are not unit-cost elementary or complex calls.

The exact rational triangle has159 reduction calls,349 Euclid passes
and136 triangle passes, giving64(159+136)+8*349=21672. Reduction covers
normalization and its final divisions; the triangle charge covers its
binomial update, multiplication and accumulation outside reduction.
This separately verifies the part not in the interval inventory.

The1000000 reserve can be realized without any special-function oracle.
Literal powers for S, tails, the analytic bound and a cached dyadic power
table need fewer than1024 multiplications/divisions; their scalar stores,
branches and small rational-pair operations fit20000. The input consists
of762 binary dyadics. Given its binary64 word (byte acquisition excluded),
integer division extracts sign, exponent and mantissa; a cached power
of2 supplies the denominator. Grid representability is checked for
every value. Fewer than128 scalar operations per decode/copy fit100000;
no general real-to-binary conversion is assumed. There are fewer than
10000 cached/output scalar slots: the256 frequency/diagonal records,
254 ratios,768 q and768 Dq records, constants and polynomial coefficients.
Centers/radii and slot writes fit100000; interval multiplications and
Dq radius operations are already charged. The additional100000 control
allowance and680000 padding are not needed to hide another evaluator.
No precision search, quadrature node service or residual assembly is
included or claimed. The total8161000 is therefore a sufficient upper
bound for exactly this finite setup, below10000000; it is not a cost
lower bound or a bound for the full Gram.

The independent replay records at most150 bits in any interval endpoint
and22 bits in the Bernoulli reduction arguments. Hence endpoint products
and scaled quotients are below320 bits; the explicit Bernoulli triangle
has smaller intermediates. The largest exact elementary-tail denominator
201*239^201 has1596 bits. Its construction and possible128-bit scaling
stay below1730 bits; the other constants are smaller. Thus2048-bit work
registers suffice for the audited algorithm, below16384. The verifier's
Fraction internals are a different implementation and are not charged as
the algorithm's work registers. The original1596-bit observed diagnostic
is retained as a diagnostic, not the sole proof of the cap.

Run `python3 scripts/separation-seven/higher-order-diagonal-audit-669.py`.
The complete certificate is
`scripts/separation-seven/higher-order-diagonal-audit-669.json`:
2058 checks pass, with an empty failure list and all replayed mode/q/Dq
tables retained. All saved bounds, template counts and register checks
were inspected. This upholds the finite known-method specialization,
not progress beyond the cited source mathematics. It does not audit
C998e's product identity, produce a residual norm, establish inverse debt
or pay signed S3. All hypotheses and outstanding contracts above remain.

## Mathlib

Full matching coverage of this fixed256-frequency, three-column numerical
certificate has not been checked. This is not evidence of absence.
Bernoulli numbers, interval inclusion, elementary real functions and
finite sums are supporting mathematics; no matching Mathlib theorem is
claimed. The precise imported digamma theorem and recurrence are cited
above, with their hypotheses and this finite specialization separated.
