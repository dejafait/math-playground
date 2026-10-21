# Corollary 426b: the saved global-complement core/tail comparison cannot sign I

## Hypotheses

Use exactly L426's A(g), I, full prime-Haar response
G=gfrak(|Zcal|^2), fixed L423 mixture, and literal two-stage selector.
Use C426a's rational enclosing endpoints a,b and its bounds on A(a),
validated by its separate step-198 critical audit. No endpoint
attainability is assumed. Retain the audited L422 coefficient
enclosures, as evaluated by L426's source_coefficients routine.

Assume correct Python integer, Fraction and isqrt execution and the
outward elementary-function and jet contracts of L037, L426 and C426a.
For r=1,...,8 let U_r be the exact upper endpoints of /G_moments/r-1/moment
in `scripts/discriminant/bulk-core-tail-moments-196.json`; these bound
the complete E G^r. In particular U_1=1. Fix the particular global
complement bound

    M_* = 22238018019465783340019/20000000000000000000000,

the upper endpoint of (1+sqrt(3b/80))/2 evaluated outward. This is an
allowed bound A(g)<=M_* throughout [a,b], from L426 (13).
The assertion below concerns these computed moment upper bounds and
this M_*. It does not rule out improved moment enclosures, a smaller
complement bound, or another response partition.

## Conclusion

Under the arithmetic contracts,

    1/800000 < 64574401593678031/50000000000000000000000
                <= A(30)
                <= 1334416391978678617527/1000000000000000000000000.

There is a nondegenerate certified negative core [a,a+1/100000], with

    A(g)<=-delta_0,
    delta_0=4003756700931958219485019/12500000000000000000000000000
            > 0.

Nevertheless, for EVERY c in (a,b) and delta>0 for which A<=-delta
on [a,c], the particular computed Markov comparison obeys

    pbar(c)=min(1, U_1/c,...,U_8/c^8),
    -delta(1-pbar(c))+M_* pbar(c) > 1/3100 > 0.

Thus no eligible cutoff can make this global-complement implementation
prove I<0, even with a better certified core using the same lower
endpoint. This is an obstruction to a sufficient certificate, not to
negativity of I. The retained enclosure of I remains step 190's
[-.194,.114]. No transport defect, rejection/realization of L423,
actual clipping, regulator margin, positivity extension, zero exclusion
or RH conclusion follows. The separate step-198 critical audit below
validates this fixed-bound obstruction under the arithmetic contracts.

## Proof

This is RESEARCH / REPRODUCTION / calculation under the prior unchanged
SPECIALIZE assessment `drafts/literature/2026-10-17-bulk-haar-signed-core-response-tail.md`.
The numerical specialization is local progress using known tools, not a
claim of a new general theorem or progress beyond the checked sources.

**Imported probability and Euler inputs.** Import Markov's inequality,
with its nonnegative-variable and positive-threshold hypotheses, from
S. Sheffield, *MIT 18.175 Lecture 8*, undated PDF accessed 2026-10-17,
[one-based PDF pp. 40--41](https://math.mit.edu/~sheffield/175/Lecture8.pdf#page=40).
Here G is positive and bounded, and each c>0, so the inequality applies
to G^r at threshold c^r. L426's already justified prime-Haar identity is

    E |Zcal|^(2j)=C_j
      =product_p sum_(e>=0) binom(j+e-1,e)^2 p^(-5e).

Its absolutely convergent Euler theorem is
[DLMF 27.4.1--27.4.3 and 27.4.10](https://dlmf.nist.gov/27.4),
with integer j and Re(s)>1. L426 supplies the character-orthogonality
specialization; composite coordinates are not made independent.

Write the fixed polynomial as G=d_0+d_13 W^13+d_14 W^14, W=|Zcal|^2,
where

    d_0=alpha(1-theta_13)+(1-alpha)(1-theta_14),
    d_13=alpha theta_13/C_13,
    d_14=(1-alpha)theta_14/C_14.

All three coefficients are strictly positive by L423 and its certified
intervals. Finite multiplication of this polynomial r times gives
nonnegative coefficients h_(r,j), with j<=14r<=112; therefore
E G^r=sum_j h_(r,j) C_j. The exact normalization E G=1 also follows
from alpha+(1-alpha)=1 and the calibrated C_13,C_14 factors. Intersect
only that raw first-moment enclosure with {1}; no higher moment is
normalized or guessed.

Recompute every needed C_j by L422 (9)--(10), rather than reusing a
preview of step 192. There are 45 orders including zero, and 2024
nontrivial local factors for the 46 primes through 200. For each factor
retain terms through e<=1024, check the decreasing next ratio
((j+e)/(e+1))^2 p^(-5)<1, and include its geometric local tail. Require
that tail at most 10^-110 times the retained lower sum; the largest
actual exponent is 167. For every j separately check the positive
denominator in L422 (10) and 0<r_C(j)<1, then retain the complete
omitted-prime multiplier [1,1/(1-r_C(j))]. These are L422's proved
tail bounds at the changed finite orders, not a new Euler theorem.
All coefficient uncertainty is retained by outward 160-place arithmetic.
Every local sum, tail, ratio, factor, global tail, polynomial coefficient
and resulting full moment is in `bulk-core-tail-moments-196.json` under
`scripts/discriminant/`. No unknown critical-line moment is used.

**Certified positive conditional point.** Reuse the complete angular
partition from C426a as the starting partition. Apply exactly its real
angular jets, both selector stages, true interval squares, root/domain
checks, endpoint values and strict-cell trapezoids at g=30. The imported
closed-cell C^2 trapezoidal error is
[DLMF 3.5.1--3.5.3](https://dlmf.nist.gov/3.5.i): in normalized angular
mass m and ordinary angular width h, the error is at most
m h^2 sup|f''|/12. Each strict cell also retains its direct range;
intersect the two integral bounds. Every unresolved selector cell
receives its full mass times L426 (13), without claiming differentiability
through a tie. The selector is independent of g, so no new branch rule
or equality convention is introduced.

Bisect the cell with greatest integral width until the lower sum is
positive, or the saved caps are reached. The final 1848 cells have
positive exact masses summing to one and disjoint interiors, covering
the entire normalized circle. Their full selector metadata, vector jets,
averaged second derivatives, endpoint values, quadrature errors, intersections and
contributions are retained in `scripts/discriminant/bulk-core-tail-196.json`.
Summing their exact rational endpoints yields the A(30) enclosure in
the conclusion. It is not a sample-based sign or a support assertion.

**A genuine core.** L426 (17)--(18) give, for each state,

    f(g)=exp(-tg)(pg+qg^2),
    f'(g)=exp(-tg)[p+(2q-tp)g-tqg^2],
    0<=t<=T=13/4,
    |p|<=B=1/4+3/sqrt(80),
    |q|<=C=(3/2)(1+1/sqrt(80)).

On 0<=g<=e=a+1/100000, exp(-tg)<=1, so every state and hence A
has absolute derivative at most D=B+(2C+TB)e+TCe^2. Differentiation
under the angular mean is justified by L426's entire continuation and
compact domination. The outward bound is

    D <= 198912771938042013914981/125000000000000000000000.

Apply the real mean-value theorem, [DLMF 1.4.11](https://dlmf.nist.gov/1.4.E11),
to C426a's upper bound at a. Its upper endpoint plus D/100000 is
exactly -delta_0 as recorded above. This covers the whole core, with
one response transport slab. The universal derivative bound is valid
even at angular ties because the selector does not depend on g.

**Why no cutoff can pass with the chosen global bound.** If c>=30,
the purported uniformly negative core contains 30, contradicting the
strict positive point. Thus every eligible c is below 30. Since a
belongs to every such core, C426a's lower bound also forces

    delta <= -A(a)
          <= d_max=152385234424669149849/250000000000000000000000
          < 61/100000.

For the saved U_r, exact rational arithmetic gives

    pbar(c)>=min(1,U_1/30,...,U_8/30^8)
             =:p_0 >169/200000,
    M_*>111/100.

This is a lower bound on the COMPUTED Markov upper bound, not on
the actual tail probability. It does not assert that Markov is sharp
or that tighter source enclosures must fail. The comparison is
decreasing in delta and increasing in pbar, because M_*,delta>0
and 0<=pbar<=1. Consequently it is strictly greater than

    -(61/100000)(1-169/200000)+(111/100)(169/200000)
       =6569309/20000000000 >1/3100.

The less weakened exact comparison lower bound in the certificate is
approximately .0003316414445. These inequalities cover all c, not just
the 32 recorded rational candidates. The one explicitly certified core
has c<1, pbar=1, and therefore comparison M_*>0. No candidate without
a core certificate is reported as having an actual signed comparison.

For completeness, the desired sufficient implication, had its strict
inequality held, would use E A(G)<=-delta(1-p)+M p with p=P(G>c),
then p<=pbar and M+delta>0. This is finite-measure monotonicity, with
the full response range included. Its hypotheses were not replaced
by endpoint attainability or a sampled distribution.

**Replay, failures and limits.** Reproduction commands:

    python3 scripts/discriminant/certify_bulk_core_tail_moments.py
    python3 scripts/discriminant/certify_bulk_core_tail.py
    python3 scripts/discriminant/verify_bulk_core_tail.py

The verifier reads every final angular cell, replays both branches,
all jets and integration bounds, and checks exact partition/aggregate
identities. It recomputes all 2024 local Euler factors, all global tails,
all eight positive polynomial expansions, 32 candidate Markov bounds,
the genuine core and the universal obstruction. All 14 checks pass in
`scripts/discriminant/bulk-core-tail-verification-196.json`. This is a
full arithmetic replay under the contracts, not an independent critical
audit or a proof of Python's correctness.

A preliminary [a,1] derivative enclosure was approximately
[-.303314,.324218], too wide for useful transport. Its 4674 state
derivative evaluations and complete cell records are preserved in
`bulk-core-tail-preliminary-196.json`. An earlier reverse-division
dispatch error had evaluated 900 strict-state derivatives before
failure; no numerical result was accepted. Its failed execution and
recovery are retained in `bulk-core-tail-failed-196.json`. The legacy counters report 21219 pre-verification callbacks and 40546
including replay. Step 198 below corrects their omitted fallback-bound
evaluations to 21244 and 40595 respectively, still below the caps. A nondegenerate
core is certified before 65536. There are two response centers (the
reused a and new 30), 32 candidates, one response slab, 1848 angular
leaves and at most 160 places. All assessment caps are met.

Stop because a universal obstruction now rules out every cutoff for
this specified global-M implementation; further refinement with those
same U_r and M_* cannot produce success. This does not exhaust the
broader assessed option of certifying a smaller full-complement bound.

### Separate critical audit — 2026-10-17, step 198

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-17-bulk-haar-core-tail-critical-audit.md`.
It validates the statement as written, with U_r and M_* fixed. It
neither improves a bound nor imports a new general result. C426a's
separate audit in this same step checks the complete inherited endpoint
input, elementary interval implementation and literal angular branches.
The named Markov, Euler, real quadrature and mean-value inputs above
are reused with their already assessed hypotheses.

**Coefficient provenance and every full moment.** The full L422 source
bounds match their audited counterparts. Independent rational interval
evaluation checks alpha, both theta_j and all three positive weights,
with strictly positive divisors. Interval dependence can enlarge these
bounds but cannot invalidate containment of the single fixed mixture.
For each positive integer j, the absolutely convergent prime-Haar
expansion gives C_j; composites are not independent coordinates.
The exact calibration gives E G=1. Intersecting the raw first moment
with {1} is justified for this reason alone, and is not used for r>1.

The complete 14-check replay recomputes every one of the 2024 local
factors and 44 nonconstant global moments. The separate audit script
`python3 scripts/discriminant/audit_bulk_core_tail_198.py` instead sums
binom(j+k-1,k)^2/p^(5k) directly as exact Fractions, retaining every
term through each saved e. For every (j,p) it verifies containment of
that finite sum, of its exact geometric remainder bound and of their
sum by the saved local factor. The next ratio is nonincreasing for
j>=1, so the geometric upper bound covers all later terms. Every ratio
lies in (0,1), e<=1024, and the saved tail satisfies the 10^-110
relative criterion. The complete local set is exactly the required
44 orders times all 46 primes through 200; its maximum e is 167.

For each order the exact denominator 1-j^2/201^5 is positive and
0<r_C(j)<1. The previously justified multiset bound
binom(j+e-1,e)<=j^e controls every larger prime, and summation over
all integers above 200 gives precisely L422 (10). Thus the multiplier
[1,1/(1-r_C(j))] encloses the entire omitted product. The independent
script multiplies the saved local rational bounds without intermediate
rounding and checks containment of the resulting global bound. This
verifies the rounded product in addition to the analytic tail argument.

For every r=1,...,8 the audit constructs the polynomial independently
by the multinomial formula. Terms with k copies of d_13 and l copies
of d_14 have coefficient binom(r,k)binom(r-k,l), degree 13k+14l,
and r-k-l copies of d_0. Equal degrees are added, not treated as
independent moments. All coefficients are nonnegative. The saved
iterative polynomial encloses these direct coefficients. Exact rational
summation against all full C_j intervals is contained in the saved raw
moment, with {1} applied only at r=1. The union of orders is exactly
45 including zero, with maximum 112. Full direct finite sums and tails,
global conditions and checks are saved in
`scripts/discriminant/bulk-core-tail-audit-198.json`; none was inferred
from a selected-factor preview.

**Positive point and response transport.** The full angular replay
checks all 1848 cells at g=30, including every state jet, endpoint and
error. There are 1824 strict cells and 24 fallback cells of total mass
3/65536. Independent rational partition, branch and aggregate checks
recover exactly the conclusion's A(30) enclosure and its lower margin
1/800000. Both stages use the same g-independent selector audited in
C426a. No support claim at g=30 is needed.

For a state exp(-tg)(pg+qg^2), differentiation gives exactly the
formula in the proof. On the whole slab 0<=g<=e=a+1/100000,
exp(-tg)<=1, t<=T, |p|<=B, |q|<=C yield
|f'(g)|<=B+(2C+TB)e+TCe^2. These uniform compact bounds justify
differentiation under the angular integral even at angular ties.
The replay recomputes the outward derivative upper endpoint; the
independent rational audit verifies the slab endpoints, inherited upper
anchor and exact subtraction yielding delta_0. This proves a whole
nondegenerate core, not merely two negative samples. The preliminary
[a,1] calculation remains too wide and is not used as a core bound.

**Universal scope of the obstruction.** Markov applies to each bounded
nonnegative G^r at the positive threshold c^r. The resulting pbar is an
upper bound on the true tail. If a core [a,c] has margin delta>0,
A(30)>0 implies c<30, including exclusion of c=30. The inherited
lower anchor gives delta<=d_max. Each saved U_r is positive and
U_r/c^r>=U_r/30^r; taking the minimum with 1 preserves this
inequality. The independent rational calculation verifies p_0>169/200000,
d_max<61/100000 and M_*>111/100. The comparison decreases with
delta and increases with pbar on 0<=pbar<=1. Therefore its uniform
lower bound is strictly greater than 6569309/20000000000>1/3100.
The exact retained lower bound is approximately .0003316414445248816.
This argument covers every eligible real cutoff and every certified
margin, independently of the 32 candidate records. It lower-bounds
neither the true probability nor E A(G). Smaller M, tighter U_r and
other partitions are not excluded. In particular endpoint attainability
is unnecessary: requiring a core on the full enclosing interval already
forces its margin to respect A(a).

**Complete records, failures and work.** Both original verifiers pass
again (12 and 14 checks); the independent supplement passes all eight
checks. The 1582 preliminary derivative records were all replayed,
and their length is checked separately before accepting the aggregate;
no zip truncation can omit a cell. The legacy counters record 900 strict-state evaluations in the failed
execution and 4674 in the preliminary pass. A real accounting omission
was found: each complete preliminary pass also evaluates the universal
response-derivative bound on 24 unresolved cells, but these evaluations
are absent from both the preliminary counter and the verifier counter.
Charge those 24 in the original pass and original replay, and charge
one attempted bound evaluation at the failed execution's first unresolved
cell. The corrected historical step-196 total is therefore
40546+24+24+1=40595; pre-verification work is 21219+24+1=21244,
still below 65536. Original records and their legacy counters remain
preserved; the corrected accounting is in the audit supplement.

The current replay adds 19327+24=19351 evaluations, including all
4674 strict-state derivatives, all 24 fallback derivative bounds and
the single transport derivative bound. Together with C426a's new
31274 this audit uses 50625 callbacks; including both corrected
historical totals gives 75193+40595+50625=166413<262144. No failed
or preliminary enclosure is promoted to a sign result. The supplement
uses no new selector/state/derivative evaluation; it checks saved records
and response/Euler arithmetic. Its initial JSON schema mismatch, before
any such callbacks, is preserved as described in C426a. All final
supplement failures are empty. This accounting correction changes no
numerical interval, proof inequality or cap decision; counts are checked
against the preserved records and executable replay, without claiming
access to absent historical execution traces.

No new mathematical input or DAG edge is required. The analytic proof,
complete replays and independent rational supplement jointly validate
the local fixed-bound stop under correct integer/Fraction/isqrt execution.
They do not certify Python, the sign of I, actual clipping or realization,
capped nondegeneracy, L413's full-error margin, or global mixed positivity.

## Mathlib

Full matching coverage for this selector-specific numerical comparison
has not been checked. Supporting integration, Markov, differentiation,
Euler-product or interval theorems do not verify the concrete bounds.
No Lean verification or absence claim is made.
