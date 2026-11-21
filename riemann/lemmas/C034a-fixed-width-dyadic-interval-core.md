# Corollary C034a: one fixed-width dyadic interval core

## Hypotheses

Use C033y's four unit panels with12 Gauss nodes per panel and C033z's
finite definition

    Jhat(w)=q sum_(j=1)^48 omega_j exp(-x_j^2) R(x_j q), q=w^(-1/2),
    R(z)=exp(z/2)/(2 sinh z)-1/(2z), R(0)=1/4.

Here x_(k,i)=k+(1+r_i)/2 and omega_(k,i)=lambda_i/2, k=0,1,2,3,
where r_i and lambda_i are the12-point Gauss-Legendre nodes and weights
on[-1,1]. This result concerns exactly w=2 and its w=1 reference;
2 is a supplied exact test width, not an asserted member of the780
outer widths. Assume C033z(4)-(8),(11)-(13),(17), including their
proved finite input and uniform approximation contracts. The original
construction did not independently audit those contracts; the finite
application audit1837 below checks precisely the imports used here.

Count each rational addition, subtraction, multiplication, division and
comparison as one operation. The implementation additionally tests each
exact divisor for zero, charging that comparison separately. Rational
constants0 and1, loop indexing, assignments and storage are free. Other
needed integer constants are constructed by addition. Integer extraction,
bit inspection, hashes, serialization and comparison with old evidence
are verification only and do not select evaluator outputs. No library
rounding, floor, bit extraction, integer division or fused arithmetic is
an evaluator primitive. Fraction reduction implements the rational field
primitive; no bit-cost model is asserted.

## Conclusion

The specified comparison-rounded evaluation encloses Jhat(2)-Jhat(1)
in[L/2^256,U/2^256], where

    L=-6062525147311844448914997086481546586058144467929674660064502160252413785037,
    U=-6062521712131471821691666344727883333814105359636532624940487641567651397732.

Its radius is

    (U-L)/2^257
      =3435180372627223330741753663252244039108293142035124014518684762387305/2^257
      < 2^-24.

The illustrative midpoint is about-0.05235697420828551 and the radius
about1.4833398357580422e-8; these decimals are not the certificate.
All retained numerical interval endpoints have denominators dividing2^256.
All144 interval divisors exclude zero; the96 positive quotient-core
divisors are at least the exact positive value recorded below. Exact
constructor divisors also exclude zero. The complete measured local
ledger is20,921,533 operations, including input construction, conversions,
interval propagation, clamps, runtime error tests and final enlargement.
This is a local finite REPRODUCTION under SPECIALIZE review1833.

Ordinary complete evidence replay and independent application audit1837
of the finite imports, enclosure logic and full count pass. This
single difference is neither a completed C033w scalar nor a general
all-width theorem. In particular, the count exceeds10^6 and supplies no
revised global cap or runtime bound. It is not progress beyond the known
general enclosure principles, and it is not an RH candidate.

## Proof

### Imported principles and need for this specialization

Import local enclosure propagation and the requirement that a quotient's
denominator interval exclude zero from Fredrik Johansson,
*Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic*,
[arXiv1611.02831v1, Sections3.1.1-3.2,4,5-5.1, pp5-8](https://arxiv.org/pdf/1611.02831v1),
and the frozen Arb2.23.0
[`arb_div` contract](https://arblib.org/arb.html#c.arb_div).
The exact-input versus prior-uncertainty distinction is also covered by
[MPFR4.2.2, Sections4.4,4.6,5.2](https://www.mpfr.org/mpfr-4.2.2/mpfr.html#Rounding).
These are general principles, not a theorem about this particular grid,
expression, input construction or cost. No Arb or MPFR call is used.
Source coverage and overlap/failure comparison are reused from
`drafts/literature/2026-11-20-fixed-width-interval-core-attempt-review-1833.md`,
source-notes1809 and scope1813. No reproof of general enclosure theory
or claim of novelty is needed. C033z supplies the instance-specific
Taylor/input bounds; what follows specifies and checks their rounded
finite application. C033y imports Gauss exactness from Johansson,
*Numerical integration in arbitrary-precision ball arithmetic*,
[arXiv1802.07942v1, Sections2/2.1, pp2-3](https://arxiv.org/pdf/1802.07942v1).
No new quadrature or integration error is claimed here.

### Comparison conversion and interval schedule

Construct integers2,...,256 by255 additions. Construct h=2^-256,
delta=2^-60 and eta=2^-168 by repeated halving. For every exact scalar
to be converted, test that it lies in[-64,64]. Bisect that closed interval
263 times. At each step form m=(lo+hi)/2; if x<m retain[lo,m], otherwise
retain[m,hi]. Equality thus takes the upper half, including when x is
already on the final grid. The output cell has width2^(7-263)=h and
contains x. Both endpoints are integer multiples of h. The top endpoint
64 is included by the all-upper path. Each conversion costs

    2+263*(1 addition+1 division+1 divisor test+1 branch comparison)=1054.

Every range test passes in the saved complete trace. This establishes
both containment and the absolute denominator grid; a significand
precision alone would not establish the latter.

For point conversion retain both cell endpoints. For an interval
operation, compute the usual exact endpoint extremes, then convert the
lower and upper extremes separately, retaining respectively the lower
and upper cell endpoint. Addition/subtraction use two exact field
operations. Multiplication computes all four endpoint products and uses
six comparisons to select their minimum and maximum. Division first
charges both tests b_lo>0 and b_hi<0 and requires one to hold. It then
computes four quotients, each with its separate exact zero test, and
six extreme-selection comparisons. Thus costs per interval operation,
including two conversions, are respectively

    addition/subtraction:2110, multiplication:2118, division:2124.

Clamps apply the two successive rational comparisons with0 and1 to each
endpoint. All retained endpoints, including exact0,1 and dyadic q, stay
on the stated grid by induction. Exact reference polynomials, cardinal
weights, Taylor coefficients, endpoint products/quotients before rounding
and exact error-bound arithmetic are distinguished from retained numerical
endpoints. The error bounds are certification scalars, not working
numerical interval endpoints. Their off-grid values are saved, not
silently designated grid endpoints. Final midpoint and radius may have
denominator2^257; they are reporting/certification scalars as well.

### Input construction and its errors

Regenerate P12 with the C033z three-term recurrence, scan all129 nonnegative
j/128 positions, and refine each of its six positive sign-change cells
by160 exact bisections. Reflect, form the12 midpoints, and compute every
cardinal-integral weight exactly as in C033z(11)-(12). The saved P12
coefficients, all12 brackets, midpoints and cardinal weights agree exactly
with the corresponding complete1802 data. All brackets are sign-changing,
inside(-1,1), disjoint and of midpoint radius<=eta. Their number equals
the degree, so each contains exactly one simple root and there are no
missing roots. The prior C033z seed-separation/weight sensitivity proof
applies unchanged. Hence

    |xhat_j-x_j|<=2^-169, |omegahat_j-omega_j|<2^-70.

Clamping the weight to[0,1] preserves this bound. For each exact xhat,
point-convert xhat and the clamped exact rational weight. The latter
need not itself be dyadic; its retained enclosure is. Compute the interval
T40(-xhat^2/16) using outward-rounded Horner arithmetic, clamp its interval
to[0,1], then square its interval four times. Let the resulting interval
be[g_lo,g_hi] and select ehat=g_lo. This contains the exact rational
value clamp(T40(-xhat^2/16))^16. C033z(13) consequently gives

    |ehat-exp(-x_j^2)|
       <=g_hi-g_lo+48/41!+8*2^-169=:epsilon_j.

All48 exact epsilon_j values are saved, computed and compared with delta;
their maximum is about1.44556e-48 and each is <=delta. The lower endpoint
satisfies0<=ehat<=1 because it is below the enclosed exact clamped power
in[0,1], and the rounded squarings of a nonnegative interval keep the
lower endpoint nonnegative. This certifies the chosen Gaussian inputs;
it does not drop their construction rounding into a library tolerance.

For w=2, bisect[0,1]64 times with the exact test2*m^2>1, then take the
midpoint and clamp to[0,1]. Every branch is replayed by its exact squared
inequality; the final bracket has width2^-64 and contains1/sqrt(2).
Thus |qhat-1/sqrt(2)|<=2^-65<delta. For w=1 take qhat=1 exactly.
No first17-panel q<=1/4 flag is applied to this test. All original input
families therefore meet C033z's delta contract. The interval arithmetic
below encloses the rational approximant using these fixed approximate
inputs; input error is paid separately next.

Every exact construction divisor is nonzero: recurrence divisors are
integers n+1>=2; scan, midpoint and conversion divisors are128 or2;
factorials and their powers-of-two multiples are positive; cardinal
weight denominators are products of differences of distinct isolated
root midpoints. The remaining error denominators are41!,17!,23!,
24*25 and1-16/(24*25)>0, or positive small constants. These are the
complete types of exact divisions in the evaluator, apart from interval
quotients, whose separate tests and full intervals are saved. The added
per-division zero comparisons all pass.

### The48 contributions for both widths and the exact target

Point-convert every coefficient of C033z's E16,U10, retaining T40's
converted coefficients for the input construction above. At each of the48
positions for both widths evaluate, in this order, with interval operations,

    ahat=omegahat*ehat, z=xhat*qhat, v=z*z,
    E=E16(z), U=U10(v), T=z*U, S=1+z*T,
    A=(E-T)/(2*S), term=ahat*A.

Accumulate each term into an interval initialized at zero, and multiply
the final sum by qhat. Save z,S,2*S,A,term and the prefix at every
position. Both entire48-term lists are replayed. There are48 divisions
by the negative singleton-16 in Gaussian construction and96 divisions
by the positive core intervals2*S. Their recorded signs all pass. The
minimum core lower endpoint is exactly

    115792909457653099564482533485532314586713404798486833123099867695689966258387
      /57896044618658097711785492504343953926634992332820282019728792003956564819968
      >2.

This explicitly checks rounded denominators rather than inferring their
sign solely from the unrounded S10>=1. Outward interval propagation
therefore encloses both rational approximate sums, including every
conversion and arithmetic rounding uncertainty. Subtract the w=1 sum
from the w=2 sum by one further rounded interval subtraction.

For the original exact finite sum using R, C033z(5) supplies

    dE=8*2^15/17!,
    dS=(4^22/23!)/(1-16/(24*25)), dT=dS/4,
    dR=(dE+dT)/2+2*dS.

For each width the R-to-A error is <=4*dR, since q<=1 and
sum omega_j exp(-x_j^2)<=4. C033z(8) bounds the perturbed-input error
for each width by1024*delta; it also covers the exact q=1 reference.
Thus enlarge the rounded difference interval at both ends by

    E_total=8*dR+2048*delta.

This retains the existing truncation/input allowances without counting
new rounding as zero. It does not replace the finite target by the
rational A expression or by the untruncated integral. Compute the enlarged
exact endpoints, convert them outward once more, and calculate the
radius with charged arithmetic. This gives precisely L,U above.
The full trace and expression replay verify the displayed integers and
the exact comparison(U-L)/2^257<=2^-24. No sampled or decimal comparison
is used in that conclusion.

### Complete local count and evidence

The measured phase totals, including every exact division's zero test,
are:

| Phase | Operations |
| --- | ---: |
| Integer constants, h,delta,eta and negative64 |1224|
| P12 roots and cardinal weights |34248|
| Taylor/factorial coefficients and their conversions |70826|
| Exact w=2 q bisection, midpoint and clamps |389|
|48 Gaussian/input constructions and error tests |8830084|
| w=1 core |5990214|
| w=2 core |5990214|
| Difference, explicit errors, enlargement, target test and reporting |4334|
| Total |20921533|

These totals can also be checked directly from the fixed schedule.
The reference total is440 recurrence,258 scan-coordinate,3096 scan-Horner,
256 seed-test,150 initial-sign,27840 refinement,12 reflection,36 midpoint,
1848 cardinal-product,288 integration and24 final-weight operations.
The coefficient phase has208 nonconversion operations and67 conversions.
The Gaussian phase has8352 conversions,48*546 interval field/selection
operations,192 clamp comparisons,384 affine-map/clamp operations,288
error/max-test operations and4 error-constant operations. Each width core
has2833 interval operations,5666 conversions and18250 nonconversion
operations, giving5990214. Across the run there are19755 conversions,
9795 interval-operation records, one additional final interval retention,
and48 Gaussian clamp records. Final error arithmetic has116 operations
outside its two traced rounded operations/retentions. Source code and
saved per-phase primitive counts specify the complete remaining breakdown;
there is no uncharged rounding or field floor operation.

Run from the notebook:

    python3 scripts/smoothed-law/fixed_width_interval_core_1835.py
    python3 scripts/smoothed-law/fixed_width_interval_core_check_1835.py

Both refuse to overwrite their preserved evidence. The full artifacts are
`scripts/smoothed-law/fixed_width_interval_core_1835.json`,
`scripts/smoothed-law/fixed_width_interval_core_trace_1835.jsonl.gz`, and
`scripts/smoothed-law/fixed_width_interval_core_check_1835.json`.
The compressed trace contains every conversion's raw rational, all263
branches, cell endpoints and count, and every interval recurrence's full
operands/output and associated conversions. All48 initial inputs, both
48-term contribution lists, every interval divisor and final exact error
are saved. Exact temporary numerator/denominator bit lengths are at most
2012/2015 in this run; retained endpoint numerator/denominator bit lengths
are at most260/257. These are different assertions: denominator bit length
257 permits denominator2^256. They impose no bound on all future widths.

The ordinary evidence checker examines every trace record and independently
re-evaluates the intended48 input and96 core expressions using integer
verification arithmetic. All129157 checks pass. It replays all64 q
branches and all19755 complete conversion paths by cell/tie identities,
checks all coefficients, Gaussian errors, prefixes, denominators and final
error/enclosure. It also checks traced primitive charges and total addition,
saving the untraced constructor/error counts for later application audit.
Integer floor and bit extraction in this evidence checker are verification
operations; they are not substituted into the comparison evaluator or its
ledger. This replay is not independent review of C033z's imported derivative
and truncation proofs or every constructor-count derivation.

The result addresses the specific rounded-core execution bottleneck.
Further widths, profile/scalar assembly and budgets, conditioning,
interpolation, weights, TV, observations, signed height, cancellation and
actual-Xi realization remain open. Any downstream use retains C033w/u,
C032s/q/w/j's actual divisor, conjugation/multiplicity, excluded ordinate0,
strict strip/gamma>14, counting, real-zero and reciprocal-square-tail,
heat positivity/separate errors, both fixed-v1, zero drift/killing and
Gaussian half-variance qualifications. Source-wide and finite-zero validity
remain unverified. Prior GMP1823 and width-only1832 stops remain unchanged.

### Independent finite application audit1837

**Scope and verdict.** The separate SPECIALIZE approval1836 of
assessment1835 covers exactly this fixed-instance audit. Under the
hypotheses above, the R-based enclosure, strict radius bound, retained
grid, divisor exclusions and complete local count pass. This is a
REPRODUCTION/application audit of known enclosure principles, not new
general mathematics or an extension to the780 outer widths. No source-wide
verification, global cap or RH claim is made. No original bound needed
correction. C033y and C033z remain the only local mathematical inputs.

**Imported finite contracts.** The four unit panels are exactly C033y's
definition following its equation(6), with12 Gauss-Legendre nodes each.
Standard Gauss positivity and constant-polynomial exactness give positive
weights summing to1 on each unit panel, hence omega_j<=1 and total4.
Only this finite rule is needed; its integration-error theorem is not
being used to change the target into J(2)-J(1).

C033z(4)-(6) applies on the whole real segment[0,4]. For clarity about
its load-bearing derivative hypotheses, write S=sinh(z)/z. The positive
series imply E16<=E, T10<=T and the analogous derivative inequalities.
The integral formulas in C033z give E'(z)<=e^2/8<1 and
S'(z)<=sinh(4)/2<e^4/4<16 on that entire segment. Also T10' is
increasing and T'(4)=S'(4)/4-(S(4)-1)/16<4. Together with E,T<2
and S10>=1 these justify the claimed bound |A'|<35 by the quotient
rule; neither an endpoint sample nor a derivative of an error estimate
has been substituted for the segment bound. The positive omitted series
for S,T have respective first terms4^22/23! and4^21/23!, and all
successive ratios at most16/(24*25)<1. The divided exponential
remainder gives dE=8*2^15/17!. Thus their uniform bounds are exactly
dS,dT,dE above, and |R-A|<=dR. The audit checks the complete exact
rational inequality dR<2^-28. The removable point z=0 is included.

The regenerated P12 recurrence is checked coefficient by coefficient.
All129 scan values are nonzero; exactly the six listed positive seed
cells change sign. The audit independently redoes all960 refinements
and checks their nonzero midpoint values, all12 final sign-changing
brackets, midpoint radii<=2^-168, and gaps>1/32. IVT and the degree12
count prove uniqueness and simplicity in each bracket and exhaust the
roots. Recomputing every cardinal polynomial and its integral reproduces
every saved weight, with all132 denominator factors nonzero. The
segment from true roots to midpoints stays in the separated seed cells;
C033z's weight-sensitivity proof therefore applies. Its m<=12 bounds
|L_i|<=2^(7m), |partial_(r_i)L_i|<=64m*2^(7m)<2^94 and
|partial_(r_k)L_i|<=2^(7m-1)+2^(7m+6)<2^91 use direct numerator
differentiation, including x=r_k. After integration the derivative sum
is <2^99. Hence the actual panel-node and weight errors are respectively
<=2^-169 and <2^-70. There is no unchecked approximate-root premise.

For each Gaussian input the exact rational polynomial value being
enclosed is clamp(T40(-xhat^2/16))^16. The node midpoint is in[0,4],
so its argument is in[-1,0]. C033z(13) bounds its error relative to
exp(-x_j^2) by48/41!+8*2^-169. The rounded interval contains that
exact polynomial value. Selecting its lower endpoint therefore adds
at most the whole interval width, precisely the saved epsilon_j.
All48 intervals, epsilon_j and comparisons with delta are independently
recomputed. Nonnegative clamped endpoints remain nonnegative under each
rounded square: the lower cell endpoint of a nonnegative raw product
is nonnegative. Since the interval contains a value in[0,1], its lower
endpoint is also<=1. These are exactly the range and accuracy
hypotheses for ehat in C033z(8).

The64 q decisions are checked against their exact squared inequalities,
and the final bracket has width2^-64 and contains1/sqrt(2). Its
midpoint is in[0,1], with error<=2^-65. This specializes C033z(17)
to exact W=2, so there is no width-input error and no low-panel flag.
The reference q=1 is exact. All perturbed arguments xhat*qhat stay
in[0,4]. Telescoping the outer factor, arguments and weights now gives
C033z(8)'s8*delta+700*delta+192*delta=900*delta<1024*delta
for each width. The interval evaluator encloses that perturbed rational
A-sum, including all conversion errors. The exact R-sum differs from
the unperturbed A-sum by<=4*dR per width because sum a_j<=4 and
q<=1. Thus8*dR+2048*delta is the correct additional allowance for
the difference. No rounding term is discarded or charged twice.

**All conversion cases and exact divisors.** After263 halvings of
[-64,64], put H=2^256 and let i be the integer represented by the
263 branch bits. The final endpoints are-64+i/H and-64+(i+1)/H.
For x<64 the comparisons select the unique such half-open cell
containing x; equality at an internal midpoint selects its upper half.
For x=64 all branches are upper and the last closed cell contains64.
For x=-64 all branches are lower. Consequently the integer verification
oracle i=min(floor((x+64)H),2^263-1) represents every comparison
decision, including ties. Floor occurs only in verification. Checking
the entire saved bit string against this oracle checks all branches;
there is no sampling of a conversion prefix. All19755 conversions are
checked in the intended expression order against their exact raw inputs.

The imported enclosure principles then apply at each step: multiplication
uses all four endpoint products; division uses all four quotients only
after a signed interval exclusion. The audit matches every trace operand,
conversion association, output and saved contribution, including all
prefixes. All144 interval divisors exclude zero;48 are the singleton-16
and96 are positive core intervals with the displayed minimum>2.
For exact construction, every integer/factorial denominator is positive,
the cardinal products are nonzero by isolation, and the error denominator
1-16/(24*25) is positive. These exhaust the source program's exact
division forms. Conversion and q divisors are2. The primitive zero test
is charged on every exact division, including all four interval quotients.

All retained endpoints, including singleton q and the final enlarged
endpoints, have denominators dividing H. Midpoints, radii, raw operation
results, coefficients and error scalars have the separately stated roles;
no off-grid scalar is silently used as a retained endpoint. Both final
integers L,U and their strict radius comparison are verified exactly.

**Complete operation accounting.** Beyond the traced interval costs,
the audit independently derives every constructor/error count. The
P12 recurrence has sum_(n=1)^11(n+2)=88 coefficient cells costing5
each; the129 scan coordinates cost258 and their Horner evaluations
3096. Seed tests cost256, six initial-sign evaluations150, and960
refinements cost29 each, since none is an equality stop. Reflection
costs12 and midpoint formation36. The cardinal polynomial and divisor
construction costs12*2*(sum_(m=1)^11 m+11)=1848; integration costs288
and final weight divisions24. This gives34248, including all zero tests.

Each coefficient phase has73 multiplications,67 divisions with67 tests,
and one subtraction outside its67 conversions. Each q slot has one
addition, one division and its test, two products and one branch test;
the final midpoint and two clamps give389. The Gaussian construction
has98 untraced divisions/tests,192 additions,48 subtractions,48
multiplications and384 other comparisons. The latter include all
weight clamps, Gaussian interval clamps, error tests and maximum tests;
their branch counts are checked on all actual operands. The final
error/reporting phase has3 subtractions,5 additions,43 products,32
divisions with32 tests and one radius comparison outside its traces.
Its exact denominators and required2^-24 construction are included.

For every phase these independently derived residual primitive vectors
are added to the trace-derived vectors. They agree componentwise with
the original full ledger, not merely its grand total. All eight phase
totals in the table above sum to20,921,533. The19755 conversions,
9795 interval operations,48 clamps and one final additional retention
are exhausted; no unused or uncharged trace suffix remains. This count
is greater than10^6, so it supplies no original global-cap certificate.

**Saved evidence and reproducibility.** Run

    python3 scripts/smoothed-law/fixed_width_core_audit_1837.py
    python3 scripts/smoothed-law/fixed_width_core_replay_1837.py

Both refuse to overwrite preserved evidence. The independent program
imports no evaluator and saves its complete report in
`scripts/smoothed-law/fixed_width_core_audit_1837.json`:238447 passing
checks, no failures. It consumes the entire original trace in the intended
expression order and independently constructs all exact reference data,
coefficients, inputs, contributions, final errors and count vectors.
The written analytic arguments above are essential; the numerical report
alone is not their proof. Integer conversion arithmetic is an audit tool,
not an evaluator operation or a saving in its count.

The second program is explicitly an ordinary execution replay of the
original evaluator, saved separately as
`scripts/smoothed-law/fixed_width_core_replay_1837.json` and
`scripts/smoothed-law/fixed_width_core_replay_trace_1837.jsonl.gz`.
Its check report is
`scripts/smoothed-law/fixed_width_core_replay_check_1837.json`.
Every mathematical certificate field and the complete decompressed trace
agree with1835. This additionally reproduces the ancillary instrumented
temporary maxima2012/2015 bits and old-P12 comparison; these maxima
are an ordinary replay claim, not an independently proved complexity
bound. Wall time, gzip metadata and changed artifact paths are excluded
from equality, with no mathematical information excluded. All original
artifacts, including the original audit-pending labels, remain preserved.

This closes the fixed-instance audit. Full-profile/scalar assembly,
other widths, numerical conditioning, exact interpolation weights,
TV and observation coverage remain unpaid. All downstream divisor,
zero-data, heat-error, fixed-v1 and Gaussian normalization qualifications
stated above persist. No signed-height or realization input is obtained.

## Mathlib

Full matching coverage of this finite conversion/evaluation/count contract
has not been checked; availability is unknown. General ordered-field,
finite-sum and interval facts would support components. Neither supporting
facts nor the external numerical libraries constitute a matching formal
certificate. The known enclosure principles are imported above; only their
fixed finite application, inputs, exact grid and measured ledger are supplied.
Audit1837 checks the informal finite application; matching formal coverage
remains unchecked and unknown.
