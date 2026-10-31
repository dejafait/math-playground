# L498 — Fixed-corner complementary coefficient mass

## Hypotheses

Use exactly the finite coefficients and parameters of L495–L497:

    t=.16836, x=6000284561421.5, N=691004,
    P={primes p<=307}, ell0=24.18022820120389,
    sigma=.5+(t/4)*log(sqrt(1+x*x)/(4*pi))-t/(2*(1+x*x)),
    w_q=exp(t*log(q)^2/4)*q^(-sigma), r_p=w_p,
    r_d=product_(p|d) r_p  (d squarefree over P), r_1=1,
    c_m=beta_m*m^(-sigma)
       =sum_(d|m, d squarefree over P, 1<=m/d<=N) mu(d)*r_d*w_(m/d),
    h(m)=max(1,2*log(m)/ell0-1), H=160N=110560640.

Every finite decimal is an exact rational. The coefficient support is
finite. Retain L497's complete elementary-function interval ledger and
the qualifications of its completed critical audit. The finite numerical calculation is
independent of the truth of the base-phase or saddle theorem. L494's
normalization, L495's resultant interpretation and L496's imported
base-phase qualification are retained for subsequent heat-function use.

## Conclusion

The complete complementary mass satisfies

    C_N=sum_(m>N) |c_m|*h(m)
        <=21688332681815698/72057594037927936
        <.30098607886352571339
        <.301408572679396256667379418689.

Together with L497's prefix upper bound this gives

    sum_(m>=2) |c_m|*h(m) < .999577507,
    1-sum_(m>=2) |c_m|*h(m) > .00042249.

This is a known-method fixed-corner reproduction. The separate critical
audit in Section 4 accepts L497's input, the proof/code and the complete
independent divisor-moment and signed-edge replay. No
comparison with either L495 charge, uniform transport, H1, collision
exclusion, other times or zero time is claimed. In particular this does
not establish actual-Xi positivity or RH.

## Proof

### 1. Imported finite splitting and specialization

The source is Michel Planat, *Collective Contraction in the de
Bruijn–Newman Heat Flow: Off-Zero Logarithmic Derivatives and Certified
Barrier Refinements*, [arXiv:2609.37164v2, 7 October 2026, Section 6.6,
equations (40)–(41), Lemma 6.7 and Proposition 6.8, PDF pp.22–23](https://arxiv.org/html/2609.37164v2#S6.SS6).
The complete statement and both proof cases were read in the prior
approved source assessment. Its reported decimal certificate is not
imported as verified. We use the finite-sum identity for the specified
rational ell0; this is permitted because its hypotheses are ell0>0
and H<exp(ell0), independently of its later phase interpretation.
The exact arithmetic below verifies

    floor(exp(ell0))=31720474772 > H.

Therefore h(m)=1 throughout the edge N<m<=H. For m>H, triangle
inequality applied to the complete signed divisor formula gives

    C_N <= E+P_tail,
    E=sum_(N<m<=H) |c_m|,
    P_tail=sum_(d squarefree over P) r_d
                  *sum_(1<=q<=N, dq>H) w_q*h(dq).            (1)

This is a majorant, not an equality for the grouped complement. Every
divisor channel, including those with d>exp(ell0), is retained. Finite
support justifies all reorderings; no analytic limit is interchanged.

For y>=0 put

    A(y)=sum_(1<=q<=min(N,floor(y))) w_q,
    B(y)=sum_(1<=q<=min(N,floor(y))) w_q*log(q).

Write A_N=A(N), B_N=B(N), and T=exp(ell0). For d<=T define
q0=min(N,floor(H/d)), qc=min(N,floor(T/d)). Lemma 6.7's first
case gives the contribution

    r_d*[A(qc)-A(q0)
         +(2/ell0)*(log(d)*(A_N-A(qc))+B_N-B(qc))
         -(A_N-A(qc))].                                   (2)

The first difference is the unit-weight part; the remaining expression
is the logarithmic part. Both parts are nonnegative sums. In particular
qc>=1 in this case. Integer products dq can be compared exactly with
floor(T), so qc=floor(floor(T)/d), clipped at N. This handles all
integer/equality cases without a guessed transcendental split.

For the other case let

    R=product_p(1+r_p),
    Rlog=sum_(d squarefree over P) r_d*log(d),
    R_> = R-sum_(d<=T) r_d,
    Rlog_> = Rlog-sum_(d<=T) r_d*log(d).

Here the subscript > denotes d>T, not >=T. The finite Euler expansion
gives Rlog=R*sum_p log(p)*r_p/(1+r_p). The second case contributes
exactly

    (2/ell0)*(A_N*Rlog_>+B_N*R_>)-A_N*R_>.                 (3)

Our implementation retains the last negative term with outward
subtraction; it never replaces a residual interval by a point estimate.
Equations (2) and (3) are imported known algebra. Their restatement is
needed to specify the clipped moments, equality conventions and full
certificate, rather than to claim a new proof of the source result.

### 2. Elementary inputs and exact grid arithmetic

`scripts/heat/complementary-mass-seeds.py` consumes every row of L497's
691004-row initial interval ledger and checks its SHA-256 against the
L497 certificate. The source intervals have denominator 10^30. For each
nonnegative source interval [a,b], integer division converts it to

    [floor(Q*a),ceil(Q*b)]/Q, Q=2^56=72057594037927936.

This preserves inclusion. All w_q and log(q) intervals, including q=1,
are stored in `scripts/heat/complementary-mass-seeds.bin`; all 63 prime
radii and logarithms are also recorded in the text config. They use the
exact sigma in the hypotheses, not a rounded saddle value. The
seed/report scripts check the fixed inputs, N, prime set and scalar
metadata, and the C++ producer compares every prime radius/logarithm
with its corresponding input row.

The check of exp(ell0) reuses L497's rigorously bounded positive Taylor
series, scaling, reciprocal and outward integer arithmetic. In detail,
ell0/64<1/2, so that algorithm encloses exp(-ell0/2), its reciprocal
encloses exp(ell0/2), and its square encloses exp(ell0). At denominator
10^30 the resulting endpoints are the integers

    31720474772362245239271114172998572549125,
    31720474772362245239271125471985706154840.

Both have integer part 31720474772. The seed generator explicitly checks
the uniform logarithmic and Taylor tail inequalities from L497; it
does not use a floating-point exponential. The factor 2/ell0 is also
enclosed by exact rational division, rounded outward to denominator Q.

For grid intervals [a,b]/Q and [c,d]/Q, sums/subtractions use the
respective endpoint sums/differences. Products take the minimum and
maximum of ac,ad,bc,bd, divide by Q and round the lower endpoint down
and the upper endpoint up. C++ signed integer division is corrected
to implement mathematical floor, including negative operands. All
products fit signed 128-bit integers because their factors are signed
64-bit endpoints; each resulting endpoint and each sum is checked for
64-bit overflow before storage. No floating-point arithmetic occurs
in the mathematical C++ calculation. Builds retain assertions; no
`NDEBUG` flag is used.

The nonnegative quantities A differences, B differences, residual
moments and the separate logarithmic tail contributions may have their
lower endpoints clipped at zero using their exact nonnegativity.
Upper endpoints are not reduced. In particular subtraction in (3)
uses the lower enclosure of the positive term being subtracted.
The absolute-value enclosure of [a,b] is [a,b] if a>=0, [-b,-a]
if b<=0, and [0,max(-a,b)] otherwise. All signed channels are
combined before applying this operation.

### 3. Completeness and full numerical evidence

The C++ producer `scripts/heat/complementary-mass.cpp` constructs all
squarefree supported divisors d<=floor(T) recursively, starting with
d=1, r=1, log(d)=0 and sign +1. A child appends one prime with strictly
larger prime index. Unique increasing prime factorizations show each
allowed divisor occurs exactly once. A branch stops when d>T/p;
every later prime is at least p, and every descendant product is
larger, so no admissible divisor is lost. Radius intervals multiply
the individual r_p; they are never replaced by a heat weight w_d.
Logarithms add individual prime log intervals. Signs alternate.

Every enumerated divisor contributes to both finite moments and (2).
There are 25983188 divisors through floor(T). Full depth counts are
in `scripts/heat/complementary-mass-moments.json`. The Euler moments
are computed independently of this enumeration by starting at
(R,Rlog)=(1,0) and applying, for each prime,

    Rlog_new=(1+r_p)*Rlog_old+R_old*r_p*log(p),
    R_new=(1+r_p)*R_old.

Subtracting the entire enumerated moments encloses the two residual
moments for (3). There are no omitted high-divisor channels.
The complete residual intervals, as integers over Q, are

    R_> in [618965698,644964578]/Q,
    Rlog_> in [15637095030,16242989522]/Q.

The sum of (2), (3), and their total are enclosed by

    clipped case: [1877321477310825,1877321625388969]/Q,
    d>T case:    [3183604600,3496383707]/Q,
    P_tail:      [1877324660915425,1877325121772676]/Q.

All 1189963 divisors through H, including d=1, are saved in
`scripts/heat/complementary-mass-divisors.bin` with their radius
endpoints and signs. The remaining edge computation uses 110 blocks.
For a block [u,v] and every stored d, it includes exactly

    ceil(u/d)<=q<=min(N,floor(v/d)), m=dq,

adding mu(d)*r_d*w_q to the signed interval for m. All edge indices
are retained, including zero and sign-uncertain intervals. A divisor
larger than v cannot contribute, and d>H cannot divide any edge m,
so restricting the stored edge divisors is exact. Blocks partition
N+1,...,H and make no assumption about convolution values outside
their own output range. There are 297341182 channel updates and
109869636 edge outputs. Every block's endpoints, update count,
signed-case counts and maximum interval width are preserved in
`scripts/heat/complementary-mass-blocks.tsv`.

The complete sum is

    E in [19811007261571712,19811007560043022]/Q,
    E+P_tail in [21688331922487137,21688332681815698]/Q.

The interval for E+P_tail encloses the majorant, and its lower
endpoint is **not** asserted to bound C_N from below. Its width is
759328561/Q<1.054*10^(-8); this is much less than the achieved strict
budget margin. Source decimal agreement is not used to accept it.

The separate `scripts/heat/complementary-mass-report.py` consumes
every input seed and all block and edge-divisor records. A recursion
pruned at H replays every stored edge divisor/radius/sign; all depth
counts and total edge channel updates agree. It recomputes both prefix
moments and full Euler moments, checks residual subtraction and (3),
sums every block with endpoint continuity checks, and compares the
final rational upper bound with the exact required threshold. It also
checks that 1 minus L497's prefix upper bound equals that threshold.
The claimed coarse full bound and margin are checked by rational
comparisons. All checks pass with zero failures. This consumer does
not independently recompute every signed coefficient or the complete
floor(T)-divisor moment enumeration. Section 4 supplies those previously
missing audit computations; the original consumer record is preserved.

Reproduce from the notebook directory:

    python3 scripts/heat/complementary-mass-seeds.py
    clang++ -O3 -std=c++17 -Wall -Wextra scripts/heat/complementary-mass.cpp -o /tmp/riemann-complementary-mass
    /tmp/riemann-complementary-mass scripts/heat
    python3 scripts/heat/complementary-mass-report.py

Full scalar inputs are in `scripts/heat/complementary-mass-seeds.json`;
the exact result is in `scripts/heat/complementary-mass-result.json`;
the consumer outcome, exact bounds, qualifications and artifact hashes
are in `scripts/heat/complementary-mass-verification.json`. Binary
ledgers use little-endian signed 64-bit integers; the tested platform
uses that representation. The divisor record is (d,r_lo,r_hi,sign);
the seed record for each successive q is (w_lo,w_hi,log_lo,log_hi).
Reproduction on another representation requires decoding explicitly.

The source already reports the full grouped estimate M_160<.999577540.
This local calculation reproduces its unit budget with a separate
enclosure and replaces its unverified
numerical ledger at this single corner; it is not a new theoretical
mass estimate, nor a certification of that paper's global assembly.

### 4. Separate complete critical audit, 2026-10-30

The audit reused the approved source comparison of the complete finite
identity, including both cases of Planat v2 Lemma 6.7, and checked the
full local proofs, seed generator, C++ producer, Python reporter and
L497's two implementations. Both strict thresholds pass. This verifies
known-method reproduction without any claim beyond the cited source
or any manuscript-level audit.

**Elementary interface.** L497 Section 4 verifies the full finer-grid
prefix replay. The new audit driver
`scripts/heat/l497-l498-audit.py prepare` additionally checked every one
of the 691004 source-to-binary seed conversions, in index order, using
explicit little-endian decoding. Multiplying each 10^30-grid endpoint
by 2^56 and rounding with Python integer division reproduces every
stored seed endpoint exactly. It checked q=1, all 63 prime/radius/log
rows, the exact rational factor 2/ell0, config fields, input file hashes,
lengths and EOF. These tests use the complete data, not samples.

The reviewed independent degree-32 exponential routine at denominator
10^40 gives exp(ell0) in

    [317204747723622452392711199829130219728509161666832,
     317204747723622452392711199829130231027496295272548]/10^40.

This is inside the old denominator-10^30 interval; both endpoints have
integer part 31720474772, greater than H. Thus the split floor and h=1
throughout the edge are independently certified. The preparation record
is `scripts/heat/mass-audit/preparation.json`; it reports 2073174 further
checks with zero failures, besides L497's 4146045 comparisons.

**Complete divisor moments.** The separate implementation
`scripts/heat/l497-l498-replay.cpp` includes or executes no producer code.
Its recursion selects strictly decreasing prime indices, unlike the
producer's increasing-index traversal. Each squarefree divisor has a
unique decreasing list; a candidate is skipped exactly when p>T/d.
Smaller primes are still tried, so no permissible smaller factor is lost.
The empty subset is consumed once. For every visited divisor the program
recomputes its radius from the selected primes in increasing order, and
its logarithm by addition, without reading any producer aggregate. The
original multiplication parenthesization is retained to permit exact
interval comparison; the enumeration and evaluation are independent.

The traversal computes A and B from every seed; for every d<=floor(T)
it computes both enumerated moments and the entire expression (2).
It independently expands the full Euler moments by Section 3's recurrence,
subtracts the enumerated moments and evaluates (3), retaining the negative
term. Nonnegative clipping is justified by the finite-sum interpretation:
A/B differences are sums of omitted nonnegative terms; the logarithmic
part has dq>T and weight 2*log(dq)/ell0-1>1; both residual moments sum
over d>T. Thus replacing only a negative lower endpoint by zero preserves
inclusion. Every clipped upper endpoint is checked nonnegative.
Correlated quantities are enclosed independently, never replaced by points.

All eleven moment intervals match the original JSON exactly, including
the cancellation-sensitive residuals in Section 3. The independent count
is 25983188 divisors. All 64 depth counts match, with nonzero counts only
at depths 0 through 10. The complete moments and counts are in
`scripts/heat/mass-audit/replay.json`. The earlier partial checkpoint
`replay-moments.json` explicitly marks its edge as incomplete; only the
final replay record establishes completeness.

**Every edge output.** Both complete edge-divisor lists are sorted by d
and compared record by record, after explicit little-endian signed
decoding of the original file. There are 1189963 entries including d=1;
the audit checks distinctness, every radius/sign, and exact EOF. Its new
list came from the independent full T-enumeration.

For each output block the replay visits divisors in decreasing numeric
order and q in decreasing order. The lower q is
floor(first/d)+1_{d does not divide first}, selecting exactly
first<=dq<=last and 1<=q<=N. Every product index is checked to lie in
its block. Each channel's signed interval is added before taking an
absolute value. Endpoint additions are exact on the grid, so changing
their order preserves the original per-output enclosure; each radius
and weight product has the same outward endpoints. Every output,
including sign-uncertain ones, contributes its full absolute interval.

All 109869636 outputs and 297341182 signed channel updates were replayed.
Every field of every original block row matches: endpoints, update count,
sum, sign counts and maximum coefficient width. Blocks partition the
complete edge. The independently predicted channel count
sum_d(min(N,floor(H/d))-floor(N/d)) agrees with the observed count. The final
edge and tail intervals equal Section 3's values, not just their decimals.

`scripts/heat/mass-audit/coefficient-blocks.tsv` records every replay
block's count, exact sum and a fingerprint consuming each output index
and both signed endpoints. Fingerprints document traversal, not interval
validity. No individual original edge coefficient ledger exists, and
no comparison with such a ledger is claimed. Each new coefficient was
actually recomputed and included; the rigorous justification is the
reviewed finite algorithm and its complete execution, not a hash or
sampled coefficient test.

**Machine arithmetic and provenance.** In the original C++ code, every
product of signed 64-bit endpoints has magnitude at most 2^126 and fits
signed 128-bit arithmetic. Negating it for ceiling division is safe.
Signed quotient/remainder correction gives mathematical floor, and
ceil(x/Q)=-floor(-x/Q). Sums, subtractions, absolute-value negations and
widths are widened before use and checked before narrowing. The separate
replay uses sign-based floor/ceiling formulas, all four products and
checked narrowing excluding INT64_MIN. Its largest checked endpoint
magnitude was 5778099493585936496, below 9223372036854775807. Adding
Q-1 in its rounding formula remains within signed 128-bit range because
2^126+2^56<2^127. No overflow is used as rounding.

For indices, every recursive product is <=T<2^35, every edge product dq
is <=H<2^27, and first+d-1<2H. Block endpoints are below H+10^6.
There are at most T distinct divisors and at most N*H channels, both
below 2^64. Depth is at most 63. These bounds also cover the original
unsigned counters and casts. The full Euler moments require no enormous
divisor-index products. Python mathematical integers do not overflow.
Floating elapsed times and the old reporter's small-prime diagnostic do
not enter the audit's comparisons; its prime test uses integer isqrt.

The audit ran on little-endian arm64 with 8-byte int64 and Python
optimization level zero. The new C++ build rejects NDEBUG and used
undefined-behavior sanitization with recovery disabled; compilation and
the complete run exited zero. Input reads check complete records and
trailing data; audit output streams check writes/close. A final read
verifies the complete result, block records and preserved original hashes.
The original producer did not check every output stream failure, and its
historical binary/build flags were not retained. Those limits cannot be
recovered from a PASS flag. The present complete, separately built replay
establishes the extant certificate independently of that historical build.
Command, compiler, source/binary hashes and run status are recorded in
`scripts/heat/mass-audit/build.json`.

**Exact thresholds.** The final Python audit compares exact fractions,
checks that the complementary budget equals one minus L497's prefix
upper endpoint, and obtains

    prefix_upper+complement_upper
      =33540255459984951334775747294832060977
        /33554432000000000000000000000000000000
      <.999577507,
    1-prefix_upper-complement_upper
      =14176540015048665224252705167939023
        /33554432000000000000000000000000000000
      >.00042249.

It also verifies the strict complementary threshold, displayed outward
decimal and provisional integer-grid comparison constant. The lower
endpoint of E+P_tail still bounds only that majorant, not C_N from below.
Final evidence, exact actual/required bounds, failures and artifact hashes
are in `scripts/heat/mass-audit/audit.json` (zero failures).

Reproduce without overwriting the original certificates:

    python3 scripts/heat/l497-l498-audit.py prepare
    clang++ -O3 -std=c++17 -Wall -Wextra -fsanitize=undefined -fno-sanitize-recover=all scripts/heat/l497-l498-replay.cpp -o /tmp/riemann-l497-l498-replay
    /tmp/riemann-l497-l498-replay scripts/heat
    python3 scripts/heat/l497-l498-audit.py finish

The build metadata records this invocation; a later compiler or binary
requires its own provenance record. No comparison with L495's charges,
transport, H1, collision exclusion, other-time or zero-time result follows.
Base-phase and saddle imports retain their qualifications. There is no
complete RH candidate.

## Mathlib

Full matching coverage was not checked and is unknown. Supporting
mathematics is finite distributivity, unique prime factorization,
finite Euler moments, the triangle inequality, elementary logarithms
and exponentials, and exact integer interval arithmetic. No Lean
verification of the imported source, arithmetic implementations,
coefficient budget or RH is claimed.
