# C998n: Adaptive Gauss setup — all-node and weight accuracy, work unproved

## Hypotheses

Use only the single finite prescription fixed before execution in
`drafts/2026-11-13-certified-gauss-adaptive-working-692.md`, implemented
in `scripts/separation-seven/certified-gauss-adaptive-692.py`. Degrees
are N=63,81,117; D=2^640; the positive mesh is x_j=1-j^2/16384,
j=0,...,127, descending. All arithmetic is exact rational arithmetic.
The desired service has separate node/weight radii<=2^-512 and complete
setup<=5000000 scalar operations under C998g's arithmetic/comparison/
assignment convention. That service context is not a positivity input.
No witness archive, original operator contract or other notebook is used.

Use Bonnet's recurrence for P_N, and for X=[l,u] subset(0,1) set

    m=(l+u)/2, r=(u-l)/2,
    d=N(P_(N-1)(m)-m P_N(m))/(1-m^2),
    M=min{(N-1)N(N+1)(N+2)/8,4N^2/(1-u^2)^2},
    [d_-,d_+]=[d-Mr,d+Mr].                            (1)

In the initial prefix evaluate at most17 midpoint trials. Accept when
0 is excluded from[d_-,d_+] AND Mr<=|d|/8. Otherwise bisect by the
same already evaluated nonzero P_N(m), preserving opposite endpoint
signs, at most16 times. Exhaustion is failure. Reuse the accepted trial
for Newton update1; allow at most12 updates, always checking derivative
exclusion, positive-width intersection and strict rounded contraction.
For each update form

    I=m-P_N(m)/[d_-,d_+], J=I intersect X.             (2)

Binary-search the center of J within X until the dyadic cell width h
satisfies h<=max(width(J),2^-560). Expand that cell by h on each side,
intersect with X and check entire J inclusion. Require exact grid
midpoints throughout. Node width<=2^-550 triggers a freshly computed
full derivative interval and a separate weight-radius check. Reflections
and the exact zero-node weight are explicitly output for each odd N.

The invocation-start SPECIALIZE assessment687 and source-notes688 cover
this finite-inclusion method. Import Johansson--Mezzarobba, *Fast and
rigorous arbitrary-precision computation of Gauss-Legendre quadrature
nodes and weights*, arXiv:1802.03948v1,12February2018, Section1(1),(3),
Section2(5), Proposition3(7), printed pp1,4-5,
[primary PDF](https://arxiv.org/pdf/1802.03948v1).
Import scalar interval-Newton preservation from Alefeld--Claudio,
*The basic properties of interval arithmetic, its software realizations
and some applications*, Computers & Structures67(1998),3-8, Section5
Theorem2/scalar case,p6,
[primary PDF](https://na.math.kit.edu/alefeld/download/1998_The-basic_properties_of_interval_arithmetic_its_software_realization_and_some_applications.pdf).
Import the simple, real, interior zero theorem for orthogonal polynomials
from [DLMF18.2(vi)](https://dlmf.nist.gov/18.2#vi); the unit weight
on(-1,1) is positive, has finite positive mass and all moments. No source
asymptotic iteration count, work theorem or general convergence guarantee
is imported or reproved. The threshold in the prefix is only a finite
selection rule; its sufficiency is not assumed without checking(2).

## Conclusion

All261 nodes AND weights of the three Gauss-Legendre rules are enclosed.
Every node radius is<=2^-551 and every weight radius<=2^-542, separately
stronger than2^-512. All129 positive-node computations, their reflections
and all three zero-node weights are complete. The exact unscaled rational
replay passes176788 checks with no failure. Prefix fallback counts are
2..10 for63,3..11 for81 and3..12 for117; every root uses7 or8 Newton
updates, within the fixed schedules. No uncomputed cases are extrapolated.

The scheduled counter is4622876<=5000000, with headroom377124, and its
independent reconstruction passes nine checks. This is NOT yet a complete
scalar-operation upper bound. In particular domination of conversion
parity/domain guards, copies and assignments by the assigned charges is
not supplied. Audit693 below disproves the12-per-pass component charge
for the literal successful source path: at least17 counted operations
occur, even before charging either remainder. Stop this submitted source/
ledger as a paid setup prescription; all261 accuracy outputs remain valid.
The construction's raw label PASS_ALL_NODES_WEIGHTS_AND_SETUP_CAP
means its scheduled cap guard passed; it does not override this limitation.
The full setup target therefore remains open. Neither actual cost above
nor actual cost below5000000 is proved here.

This is local accuracy progress using known methods, not mathematics beyond
the checked sources. No square bank, complete square service, inverse debt,
signed S3 comparison, higher/mixed endpoint signs, C744q/H2, non-neutral
assembly or actual-Xi positivity is established; there is no RH candidate.
C998l/m remain preserved comparisons, not mathematical premises here.

## Proof

### Complete isolation and exact point evaluations

For a grid point a/D, the constructor evaluates the source recurrence as

    Q_k=k!D^k P_k(a/D), Q_0=1,Q_1=a,
    Q_(k+1)=(2k+1)a Q_k-k^2 D^2 Q_(k-1).             (3)

Substitution into Bonnet's recurrence proves this scaling identity, needed
only for the exact implementation; it does not reprove a source theorem.
The replay independently evaluates the unscaled rational recurrence
P_0=1,P_1=x,(k+1)P_(k+1)=(2k+1)xP_k-kP_(k-1), and checks the complete
values used in the certificate against(3), not merely their signs or
leading digits. All384 mesh entries and every adaptive/Newton/final/zero
value are covered. There are2606 constructor point calls; the replay
checks reused values again at their relevant uses.

All128 mesh values per degree are nonzero, giving respectively31,40,58
disjoint positive sign-change brackets. The mesh points are generated
from the stated integers, strictly descending and positive. Continuity
gives a root in each bracket. Bonnet's recurrence gives odd parity at
each of these degrees, so reflection gives the same number of negative
roots and P_N(0)=0. The imported simple-root count then accounts for all
N roots and ensures each bracket contains exactly one. This justifies
completeness without any approximate seed or uninspected seed theorem.

For every rejected adaptive trial the replay verifies the exact interval,
midpoint, adjacent polynomial values, both derivative endpoints, M and the
false stopping guard. Its bisection entry reuses the identical P_N(m),
whose sign is nonzero, and preserves opposite signs. For every accepted
trial the stopping guard is checked true, it is the last prefix trial,
and its data exactly match Newton update1. Every fallback record is
consumed once. Hence there are1141 actual fallback bisections and1270
trials, exactly one accepted trial for each of129 positive roots. The
observed maxima above verify that the fixed16-bisection ceiling sufficed;
no general theorem about that ceiling is asserted.

### Full derivative inclusion and every root-preserving update

The cited derivative formula gives d in(1). Proposition3(7) bounds
|P''_N| by the endpoint-valid first entry of M and, in the interior, by

    2^(5/2) N^(3/2)/(sqrt(pi)(1-x^2)^(5/4)).

For0<=x<=u<1 this is<=4N^2/(1-u^2)^2, because
2^(5/2)/sqrt(pi)<4, N^(3/2)<=N^2 and0<1-u^2<=1.
Both entries therefore bound the second derivative throughout X, and
the mean-value theorem gives the whole derivative enclosure in(1).
All domain and exact-midpoint guards succeed; the inherited mesh domains
and intersections keep X strictly positive, and every derivative use
checks u<1. Every division in(2) has derivative interval excluding zero.
Polynomial smoothness and the retained root provide the remaining scalar
interval-Newton hypotheses, so J retains that root. The replay recomputes
both endpoints of I and J exactly for every one of949 accepted updates.
It separately checks J has positive width; no convergence inference is
substituted for these finite checks.

Put t=max(width(J),2^-560). At each conversion the search retains the
center c of J. Its last cell[A,B] has width h with t/2<h<=t. This strict
lower bound is checked in every case, including a zero-halving case if
one occurred. Since width(J)/2<=t/2<h, expanding by h on both sides
covers J. The replay additionally checks full J inclusion directly after
intersection with the prior interval and verifies strict contraction.
Every one of71491 conversion halvings is independently checked to be
required by the prescribed stopping test and exactly available on the
640-bit grid. The final depths are checked below640. Thus no grid floor,
floating approximation or unproved convergence claim is used for accuracy.

### All weights and independent radii

For each final positive X=[l,u], the replay verifies width(X)<=2^-550
and recomputes(1) on that final interval. The cited Gauss formula gives

    w in [2/((1-l^2)max(d_-^2,d_+^2)),
          2/((1-u^2)min(d_-^2,d_+^2))].             (4)

Both factors in its denominator are positive: 0<l<=u<1 and the full
derivative interval excludes zero. Equation(4) follows by bounding
1-x^2 and P'_N(x)^2 on X, then reciprocating positive bounds. The replay
checks both complete rational endpoints, node radius(u-l)/2, weight
radius half the weight-interval width, and their separate2^-512 tests.
Negative intervals are exactly[-u,-l] with the same weights, by parity
and the cited formula; every reflected output is checked. At zero,
P'_N(0)=N P_(N-1)(0)!=0; each zero-node weight is checked exactly as
2/[N P_(N-1)(0)]^2, giving zero output radii there.

The entire output inventory is63+81+117=261, checked per degree and
globally. Exact integer comparisons give maximum node radius in
(2^-552,2^-551] and maximum weight radius in(2^-543,2^-542]. These are
bounds on the computed rational intervals, not numerical previews.
The full proof evidence is `scripts/separation-seven/certified-gauss-adaptive-692.json`;
the complete independent replay is
`scripts/separation-seven/certified-gauss-adaptive-replay-692.json`.
Its176788 checks cover all relevant values and cases and have no failures.

### What the scheduled counter establishes

The separate counter certificate is
`scripts/separation-seven/certified-gauss-adaptive-ledger-692.json`.
The complete count reconstruction is:

| N | Trials | Fallbacks | Newton | Conversion halvings | Derivative calls | Point calls |
| --- | --- | --- | --- | --- | --- | --- |
|63|280|249|225|17206|505|634|
|81|381|341|298|22190|679|808|
|117|609|551|426|32095|1035|1164|

There are129 final positive weight evaluations and three zero evaluations.
Derivative calls=trials+Newton-positive roots+final weight evaluations,
since update1 reuses its accepted trial. Point calls add128 mesh values
and the zero value per degree. These identities give2219 derivative
calls and2606 point calls, matching the full guard counts.

Assigned point recurrence charges total3169180; derivative charges266280;
adaptive control127000; Newton control85410; conversion fixed37960,
tolerance15184 and halvings857892. All remaining categories total63970.
Their sum is4622876. Every scheduled charge is nonnegative and the
complete sequence passed the cap guard. The nine counter checks verify
all categories, counts, sum, required cap and output inventory exactly.
This proves the scheduled counter statement only. A sum of assigned
charges is not a proof that all real arithmetic, comparisons and
assignments have been dominated. Audit693 identifies an actual component
undercharge below; this is an essential gap in the submitted setup service,
even though accuracy is established.

Reproduction from this notebook:

    python3 scripts/separation-seven/certified-gauss-adaptive-692.py
    python3 scripts/separation-seven/certified-gauss-adaptive-replay-692.py
    python3 scripts/separation-seven/certified-gauss-adaptive-ledger-692.py

Serialization, independent proof replay and counter reconstruction are
verification artifacts, not extra numerical prescriptions or timing
estimates. Their existence alone does not complete the service ledger.

### Audit693: the submitted conversion charge fails source-level domination

Retain exactly the692 source and numeric prescription. C998g's convention
counts each real arithmetic operation, comparison and named-register
assignment. This audit counts a subset of the literal executed source
operations, without optimizing the source or importing bit operations as
unit-cost real operations. Give both remainder computations ZERO cost;
grant every exact division by2 a single arithmetic operation. Exclude
pay/require instrumentation, serialization and Boolean overhead entirely.
These deliberately generous exclusions can only weaken the component test.

For one successful pass of quantize, the source-level inventory is:

| Executed fragment | Arithmetic | Comparisons | Assignments |
| --- | --- | --- | --- |
| while h>target_width |0|1|0|
| if depth>=BITS (false branch) |0|1|0|
| require(depth<BITS) predicate |0|1|0|
| mid=(ll+uu)/2 |2|0|1|
| (ll+uu)%2==0 predicate, remainder free |1|1|0|
| mid<=center and one endpoint copy |0|1|1|
| h%2==0 predicate, remainder free |0|1|0|
| h/=2 |1|0|1|
| depth+=1 |1|0|1|
| steps+=1 |1|0|1|
| Total subset |6|6|5|

The sum is17>12. Both endpoint branches have identical cost. The false
failure-context branch still evaluates its depth comparison. The separate
grid guard and the steps update are executed; recording the value steps
does not erase its numeric assignments. Repeated expressions are counted
as written. An implementation that eliminates them needs its own ledger;
this is not a lower bound for optimized implementations.

`scripts/separation-seven/gauss-scalar-ledger-audit-693.py` checks the
constructor/certificate hashes, the saved full rational replay and all nine
counter checks. It independently reconstructs EVERY conversion from its
complete rational intersected image, checking each true loop condition,
depth guard, both parity guards, selected endpoint, stopping cell, depth
and output. All949 conversions and71491 passes are covered. Its AST
inventory records the exact successful-path source fragments, including
the two equally costly branches. All291692 audit checks pass. The complete
certificate is `scripts/separation-seven/gauss-scalar-ledger-audit-693.json`.
The underlying unscaled polynomial accuracy replay remains the692 result;
this narrower audit does not pretend to repeat that mathematical work.

Consequently the selected source component has at least
17*71491=1215347 operations versus the assigned857892, a discrepancy of
357455. Merely replacing this one category in the scheduled total gives
4622876+357455=4980331, still below5000000 by19669. This hybrid sum is
NEITHER a complete upper bound NOR a total-work lower bound: other
categories are unproved upper allowances, not established lower counts.
Their spare allowance could in principle cover this discrepancy. Thus
this audit refutes the claimed component rate, not collective affordability
or the existence of a full bound for the numerical map. No above-cap
actual-work claim follows.

Moreover, `%2` is not among the listed real primitives; no scalar
implementation or separate cost for these two literal guards was supplied.
The checked grid invariant could support a separately specified guard
realization. It cannot silently be substituted for the submitted source's
checks in a purported code-level accounting proof. Complete constant,
copy, loop, guard and other-category accounting also remains to supply.
The first essential component test therefore stops THIS source/ledger as
a paid setup prescription. No parameter is retuned, no construction is
rerun, no accuracy certificate is rejected, and no universal work barrier
is claimed. A future scalar implementation must fix and count its own
guards before running, rather than reuse the stopped12-per-pass claim.

The first audit run had an incorrect expected AST split (5 arithmetic,
7 comparisons instead of6 and6); it failed before conversion replay.
The actual AST evidence and failed output are preserved in
`scripts/separation-seven/gauss-scalar-ledger-audit-693-first-pass.json`.
Correcting that inventory assertion leaves the total17 unchanged. It
changes no numerical construction or certificate. Reproduce the successful
audit with `python3 scripts/separation-seven/gauss-scalar-ledger-audit-693.py`.

## Mathlib

Full matching coverage for this finite adaptive prescription, complete
rational trace and operation count has not been checked. Supporting
Legendre, interval or rational-arithmetic theorems alone would not certify
the requested service. Unknown availability is not evidence of absence.
The imported primary results and their specialized hypotheses are above.
Full matching Mathlib coverage for the source-level scalar audit has not
been checked either; the AST/finite replay is supplied explicitly.
