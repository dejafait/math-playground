# L497 — Fixed-corner finite coefficient prefix

## Hypotheses

Use the normalization and frozen cutoff of L494 and the exact finite
coefficients of L495, with

    t=.16836, x=6000284561421.5,
    N=floor(sqrt(x/(4*pi)+t/16)), P={primes p<=307},
    sigma=.5+(t/4)*log(sqrt(1+x*x)/(4*pi))-t/(2*(1+x*x)),
    b_n=exp(t*log(n)^2/4), ell0=24.18022820120389,
    beta_m=sum_(d|m, d squarefree over P, 1<=m/d<=N)
                mu(d)*(product_(p|d)b_p)*b_(m/d),
    h_ell0(m)=max(1,2*log(m)/ell0-1).

All finite decimals are exact rationals. The sigma formula is L496 (3),
not a rounded saddle approximation. L496 supplies the interpretation
of ell0 as a phase floor on L494's domain, retaining its imported Planat
Lemma 6.3 qualification. The purely finite numerical sum below does not
require the truth of a saddle or phase theorem: it uses the specified
rational ell0. Those imported qualifications matter to subsequent use
as a bound for the actual heat-function resultant.

## Conclusion

The cutoff is N=691004, the weight is h_ell0(m)=1 for 2<=m<=N,
and the complete prefix satisfies the exact rational enclosure

    0.698591427320603743332618250912
      <= sum_(2<=m<=N) |beta_m|*m^(-sigma)*h_ell0(m)
      <= 0.698591427320603743332620581311 < 1.

Thus 1 minus the prefix is at least
.301408572679396256667379418689. This is a partial budget, not the
reserve of a complete resultant certificate. L498 separately supplies
the complementary mass. Both L495 charges, uniform transport, finite
collisions, other times and zero time remain unresolved by this prefix.

This independently reproduces a finite part of the computation reported
in Michel Planat, *Collective Contraction in the de Bruijn–Newman Heat
Flow: Off-Zero Logarithmic Derivatives and Certified Barrier Refinements*,
[arXiv:2609.37164v2, 7 October 2026, Section 6.6, equations (40)–(41),
Lemma 6.7 and Proposition 6.8; Section 6.7, equation (44), PDF pp.22–23,26](https://arxiv.org/html/2609.37164v2#S6.SS6).
The source reports the stronger full grouped bound M_160<.999577540
and rounded main entry .698591428. Neither report is imported as
verified. The computation here claims no advance beyond that source
method and is not an all-degree positivity or RH result.

## Proof

### 1. Complete coefficient grouping on the finite prefix

Put a_n=b_n*n^(-sigma) and r_p=a_p. Then exactly

    c_m=beta_m*m^(-sigma)
       =sum_(d|m, d squarefree over P, 1<=m/d<=N)
          mu(d)*(product_(p|d)r_p)*a_(m/d).

Initialize c_m=a_m for 1<=m<=N. For each prime p in P, replace

    c_m <- c_m-r_p*c_(m/p)

at multiples of p in descending order. At the time an index m is
updated, m/p<m has not yet been updated for this prime. The update
therefore multiplies the previous coefficient array by the single
factor 1-r_p*[p], where [p] shifts index n to pn. Induction on the
prime set proves the displayed squarefree-divisor formula, with every
divisor channel once. Multiplication can only increase an index, so
discarding indices >N at each stage cannot affect any retained output.
For m<=N the restriction m/d<=N holds automatically, but no divisor
of that selected m is discarded. In particular b_d is never substituted
for product_(p|d)b_p.

All updates use signed intervals before absolute values. If c_m lies
in [a,b], the absolute-value enclosure is [a,b] for a>0, [-b,-a] for
b<0, and [0,max(-a,b)] when the interval contains zero. These cases
include exact zero. No coefficient-sign theorem is assumed.

### 2. Exact scalar and elementary-function enclosures

The producer `scripts/heat/finite-prefix-certificate.py` uses only
integer and Fraction arithmetic for the mathematics. Its grid is
1/Q with Q=10^30. Division rounds each lower endpoint down and upper
endpoint up by exact integer division. Products use all four endpoints,
or the equivalent sign-specific formulas when a positive Euler radius
multiplies a signed coefficient interval. Sums are exact on the grid;
reciprocals have positive denominators. These operations enclose the
exact real arithmetic by interval inclusion, including correlated
quantities treated as independent intervals.

Machin's identity gives pi=16*atan(1/5)-4*atan(1/239). Each alternating
arctangent series has 50 terms, j=0,...,49. The next term is positive
and bounds the remainder above; zero bounds it below. Thus for n=5,239
the exact omitted upper bound is 1/(101*n^101). This gives pi without
assuming a stored decimal.

For a positive rational argument, range reduction writes q=2^k*v,
1<=v<2. With z=(v-1)/(v+1), 0<=z<=1/3,

    log v=2*sum_(j>=0) z^(2j+1)/(2j+1).

The producer encloses 35 terms by forward powers and interval
arithmetic. The remaining positive tail is at most

    2*(1/3)^71/[71*(1-1/9)] < 1/Q.

It adds one grid unit to the upper endpoint. The same formula at v=2
encloses log 2; signed multiplication by k gives log q for either sign
of k. Monotonicity gives the logarithm of a positive interval from
its endpoints. For the many integer logarithms a sieve gives a prime
factor p of every composite n; log n=log p+log(n/p) uses already
enclosed lower indices. Primes use the just-proved log series.
This is an exact identity, not a numerical approximation to factorization.

For every exponent e=t*(log n)^2/4-sigma*log n at 2<=n<=N,
the script checks that e<=0 and 0<=-e/32<=1/2. It encloses exp(-e/32)
by its positive Taylor series through degree 26. Its tail is at most

    (1/2)^27/27! * 1/(1-1/56) < 1/Q.

Here 1/56 bounds every subsequent term ratio after the first omitted
term. One grid unit added upward therefore suffices. Five interval
squarings followed by a reciprocal enclose exp(e). Each recurrence,
square and reciprocal rounds outward. For n=1 the value is exactly 1.
No floating-point value enters the enclosures or comparisons.

The scalar certificate evaluates

    Lstar=log(1+x*x)/2-log(4*pi),
    sigma=.5+t*Lstar/4-t/(2*(1+x*x)),
    Y=x/(4*pi)+t/16.

It obtains sigma in
[1.631876020425340544871953709841,
1.631876020425340544871953709983]. It verifies N^2<=Y<(N+1)^2
for N=691004; no uncertain square-root rounding determines the floor.
It also verifies log N<ell0, so log m<=log N<ell0 gives
2*log(m)/ell0-1<1 and h_ell0(m)=1 on the entire prefix.
The fixed corner satisfies t*log(x/(4*pi))<5.17 and the closed lower
bounds in L494. These checks include all scalar hypotheses relevant
to the intended interpretation.

### 3. Complete numerical evidence

Reproduce from this notebook with

    python3 scripts/heat/finite-prefix-certificate.py
    python3 scripts/heat/finite-prefix-verify.py

The producer writes `scripts/heat/finite-prefix-certificate.json` and
two full grid-endpoint ledgers (the common denominator is Q):

- `scripts/heat/finite-prefix-certificate-initial.tsv.gz` stores all
  691004 integer logarithm and a_n enclosures, including n=1.
- `scripts/heat/finite-prefix-certificate-coefficients.tsv.gz` stores
  every one of the 691003 output c_m and absolute-value enclosures.

The JSON stores exact inputs, scalar endpoints, uniform tail comparisons,
the complete prime set/radii, stage update counts, enclosure widths,
actual/required unit bounds, failures and ledger hashes. The sieve
enumerates the 63 primes through 307; the largest needed prime is
included, and no other prime enters. There are 1393107 signed updates.
All radius intervals are strictly between zero and one.

The final producer intervals have 690940 definitely positive outputs,
no definitely negative outputs and 63 intervals containing zero.
The latter contribute zero only to the lower sum; their full upper
absolute-value endpoints are retained in the upper sum. No conclusion
about their exact signs is needed. Adding every absolute-value lower
and upper endpoint yields exactly the rational interval in the
conclusion; its width is 2330399/Q. This sum has no rounding error
beyond the individual already enclosed endpoints.

The separate consumer `scripts/heat/finite-prefix-verify.py` imports
and executes no producer code. It reads both complete ledgers and
uses a finer grid 10^(-40). Its independent elementary evaluations use
70 alternating arctangent terms, 45 atanh logarithm terms evaluated
by Horner's rule, and a degree-32 exponential polynomial evaluated
by the backward recurrence P=1+(a/k)*P, k=32,...,1. The corresponding
positive tails are bounded by

    2*(1/3)^91/[91*(1-1/9)] < 10^(-40),
    (1/2)^33/33! * 1/(1-1/68) < 10^(-40).

The alternating arctangent remainder is 1/(141*n^141).
The same outward interval induction and five squarings/reciprocal
argument validate these different evaluations. A separate sieve selects
the largest small prime divisor, rather than the producer's smallest;
the exact log factorization identity still applies.

Every recomputed log and a_n interval must lie inside its stored
producer interval. The consumer then applies the primes in reverse
order and uses generic four-endpoint multiplication. The finite
factor operators commute: multiplying index by p then q has the same
effect as q then p, with scalar multiplier r_p*r_q. Thus this order
computes the same exact c_m. Each finer c_m interval must lie inside
the corresponding stored interval. It also checks every stored
absolute-value endpoint, row index, count, total and ledger hash, and
requires its complete finer sum to lie inside the reported sum.
This consumes the full evidence, not sampled coefficients or a preview.
All 4146045 consumer checks pass with zero failures. Its complete outcome
is `scripts/heat/finite-prefix-verification.json`.

This was the internal complete numerical verification of the reproduction.
The later separate-turn critical audit below accepts the finite prefix;
the original consumer's self-report alone was not that mathematical audit.
No edge or tail computation is hidden in this prefix claim.

### 4. Separate critical audit, 2026-10-30

The complete proof and both Python implementations were checked under
the previously approved combined L497/L498 scope. The audit accepts the
stated prefix enclosure, without changing its hypotheses or endpoints.
This verifies local reproduction of the cited method, not a result beyond
that source and not any imported saddle or base-phase theorem.

The series checks apply to the *rounded* argument intervals too: both
exponential implementations check the upper scaled endpoint is at most
1/2. All omitted exponential terms are positive; successive omitted-term
ratios are bounded by 1/56 and 1/68 respectively. For the logarithm,
z<=1/3 bounds the omitted powers by a geometric series with ratio 1/9,
while replacing later denominators by the first omitted denominator
increases the tail. Thus the four rational tail inequalities above justify
their single added upper grid unit. The 50- and 70-term alternating
arctangent sums end with a negative term; the next positive term bounds
the omitted remainder above. Machin's identity therefore has the stated
outward subtraction signs. Signed range reduction multiplies log(2) by
an integer with the correct endpoint reversal for a negative multiplier.

The producer's sieve marks a composite n by a prime divisor p with
p<n and n/p<n; its first marking selects the smallest such divisor.
The consumer's overwriting sieve still marks only with primes and chooses
a possibly different prime divisor. Unmarked integers >=2 are prime,
since every composite has a prime divisor at most its square root.
Induction on n thus validates both logarithm arrays. Python's integer
endpoints have arbitrary precision; the factor indices fit the platform's
32-bit unsigned array entries because n<=691004. Every positive reciprocal
checks its denominator. The signed convolution's descending index order
uses the pre-factor coefficient, and the commuting finite factor operators
justify the reverse-order consumer. There is no absolute value before
grouping and no sign assumption at a zero-straddling output.

`scripts/heat/l497-l498-audit.py prepare` reran the reviewed independent
consumer at grid 10^40 with its output redirected into `mass-audit/`.
It read both complete compressed ledgers, checked their headers, indices,
row counts, EOF and hashes, and recomputed every elementary interval and
every coefficient. All 4146045 comparisons passed. The finer prefix sum is

    [6985914273206037433326194158971403859470,
     6985914273206037433326194158971406385662]/10^40,

strictly contained in the stated interval. The fresh consumer JSON agrees
with the retained one in every field. Its full record is
`scripts/heat/mass-audit/finite-prefix-verification.json`. The audit also
checked the full prime list, every radius metadata entry and stage count,
and recomputed the scalar containment, cutoff, weight and domain checks.
All original input files and certificate hashes were preserved; no
producer was rerun to replace the evidence being audited.

The combined audit's seed checks and complementary computation are
recorded in L498. Its final exact comparisons are in
`scripts/heat/mass-audit/audit.json`. Script output and hashes are evidence
of the reviewed deterministic calculations, not an independent theorem
about the historical programs' build environment. Full Mathlib coverage
remains unknown.

## Mathlib

Full matching coverage was not checked and is unknown. No Mathlib
formalization of this finite heat-weight convolution or the certificate
is claimed. Supporting mathematics is finite distributivity, elementary
interval arithmetic, geometric/alternating/Taylor series remainders,
logarithm/exponential identities and Machin's standard identity.
The rational scripts are checkable computational evidence, not Lean
proofs of either the imported analytic inputs or RH.
