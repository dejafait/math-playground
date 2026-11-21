# C998m: Tolerance-capped Gauss conversion — finite setup counter stop

## Hypotheses

Consider ONLY the prescription fixed before execution in
`drafts/2026-11-13-certified-gauss-tolerance-cap-working-691.md`, implemented
by `scripts/separation-seven/certified-gauss-tolerance-cap-691.py`.
Its target is all Gauss-Legendre nodes AND weights for N=63,81,117,
separate interval radii<=2^-512 and setup<=5000000 scalar operations.
C998g's convention counts real arithmetic, comparisons and assignments
separately. It is context for the counter, not an operator or positivity
premise. The witness archive is not used. No bit-complexity claim is made.

Put D=2^640 and use the positive rational mesh 1-j^2/16384,
j=0,...,127, in descending order. Require exactly(N-1)/2 sign-change
brackets. For each bracket perform exactly16 sign bisections, then
at most12 safeguarded interval-Newton updates. Stop the whole prescription
at its first failed guard, exhausted schedule or counter excess.
All polynomial evaluations and interval endpoints are exact rationals.
The zero root and reflection have their own weight/output checks.

For X=[l,u] subset(0,1), m=(l+u)/2,r=(u-l)/2, use

    M=min{(N-1)N(N+1)(N+2)/8, 4N^2/(1-u^2)^2},
    [d_-,d_+]=[P'_N(m)-Mr,P'_N(m)+Mr].                 (1)

Require this derivative interval to exclude zero, form
I=m-P_N(m)/[d_-,d_+], and intersect with X to give J.
Require positive width. Binary-search the center of J within X,
halving an exactly dyadic cell until its width h satisfies

    h<=max(width(J),2^-560).                          (2)

Expand that cell by h on both sides and intersect with X. Require exact
grid arithmetic, full J inclusion and strict contraction. Node width
<=2^-550 triggers a new derivative enclosure and a separate weight test.
No grid refinement, alternative schedule or retuning is allowed in this run.

The pay function adds each scheduled charge to a counter and stops
immediately if it exceeds5000000, before the charged computation.
Its constants include a10000-operation administration reserve and
a4000-operation tolerance-constant reserve. The table below specifies
its complete executed counter schedule. These are conservative assigned
charges, not lower bounds on necessary work. We do not infer failure of
the accuracy/work target from an overestimate of required work.

Invocation-start assessment687 (SPECIALIZE) and source-notes688 cover
this finite inclusion/recurrence method. Import Johansson--Mezzarobba,
*Fast and rigorous arbitrary-precision computation of Gauss-Legendre
quadrature nodes and weights*, arXiv:1802.03948v1,12February2018,
Section1(1),(3), Section2(5), Proposition3(7), printed pp1,4-5,
[primary PDF](https://arxiv.org/pdf/1802.03948v1).
Import the simple-root theorem for orthogonal polynomials from
[DLMF18.2(vi)](https://dlmf.nist.gov/18.2#vi): positive unit weight
on(-1,1) has finite positive mass and all moments, so all N roots
are simple, real and internal. Scalar interval-Newton root preservation
is Alefeld--Claudio, *The basic properties of interval arithmetic,
its software realizations and some applications*, Computers & Structures
67(1998),3-8, Section5 Theorem2/scalar case,p6,
[primary PDF](https://na.math.kit.edu/alefeld/download/1998_The-basic_properties_of_interval_arithmetic_its_software_realization_and_some_applications.pdf).
No asymptotic convergence schedule or finite source work bound is imported
or reproved. C998k and C998l are historical comparisons, not premises
constraining all implementations.

## Conclusion

This prescription stops at the upfront point-evaluation payment for the
third bisection of positive root index52 (zero-based, descending order)
for N=117. Immediately before that payment the counter is4998958;
the scheduled1532 charge makes it5000490>5000000. The evaluation itself
is not performed. All earlier guards succeed; this is not another grid
precision failure.

Before stopping, all63 and81 outputs and104 degree117 outputs are
constructed:248 node/weight pairs, with separate node radii<=2^-559
and weight radii<=2^-548, hence both<=2^-512. The degree117 positive
mesh isolates all58 roots, but only the first52 have completed Newton
refinement and weights; six positive roots, their reflections and the
zero-root weight remain unpaid. No complete261-output setup is established.

The exact counter stop is established, not a lower bound exceeding the
budget on the actual rational operations. Completeness of a full setup
operation upper bound is not asserted. The square bank, full square
error/work, signed S3, inverse debt, higher/mixed signs, C744q/H2 and
actual-Xi/global assembly remain open. This is local implementation
evidence using known methods, with no mathematical advance beyond the
checked general sources and no RH candidate.

## Proof

### Root and weight inclusion for the complete recorded prefix

Use Bonnet's recurrence, specialized by exact scaling to

    Q_k=k!D^k P_k(a/D), Q_0=1,Q_1=a,
    Q_(k+1)=(2k+1)aQ_k-k^2D^2Q_(k-1).                 (3)

Substitution into the cited recurrence verifies the scaling; this is
an implementation identity, not a reproof of a general source theorem.
The independent replay uses the unscaled rational recurrence and checks
every complete adjacent value against(3), including all mesh values,
every recorded bisection, every Newton midpoint, every final weight
midpoint and both completed zero nodes. In total3214 point evaluations
are checked in full. No sign or value is inferred from a preview.

At each degree all128 mesh values are nonzero. They yield respectively
31,40,58 disjoint sign-change brackets. Continuity gives a root in each;
parity gives reflected roots and the zero root (P_N(-x)=(-1)^N P_N(x)
follows inductively from Bonnet's recurrence). The imported degree-N
simple-root count makes these a complete and nonredundant isolation.
Each checked bisection retains opposite signs. The final incomplete
root has only two recorded bisections; no third polynomial value is claimed.

The derivative is evaluated by the cited identity
P'_N(m)=N(P_(N-1)(m)-mP_N(m))/(1-m^2). Every used midpoint lies
strictly inside(0,1). Proposition3(7) supplies the endpoint-valid
bound on |P''_N| in(1) and the interior bound
2^(5/2)N^(3/2)/(sqrt(pi)(1-x^2)^(5/4)). For0<=x<=u<1 this is
<=4N^2/(1-u^2)^2, using2^(5/2)/sqrt(pi)<4,N>=1 and1-u^2<=1.
Thus(1) encloses the derivative on all X by the mean-value theorem.
The replay checks exclusion of zero, exact Newton endpoints and exact
intersection for every one of the735 accepted updates. Smoothness and
the already isolated root supply the other scalar inclusion hypotheses.

To justify the changed conversion, let t=max(width(J),2^-560).
Every executed conversion starts with width(X)>2^-550 and J subset X,
so width(X)>t/2; its checked final cell has h<=t<2h. The binary-search comparisons retain
the center c of J in the final cell[A,B]. Since width(J)/2<=t/2<h,
J lies inside[A-h,B+h]. Intersecting with X therefore preserves its
root. The replay additionally verifies full J inclusion and strict
contraction directly for every update and checks all67033 actual
halvings, their stopping tests and their exact dyadic endpoints.
No generic convergence guarantee is substituted for these finite checks.

For a completed positive node interval[l,u], recompute(1). Its weight
is enclosed by the cited formula using the positive denominator:

    w in [2/((1-l^2)max(d_-^2,d_+^2)),
          2/((1-u^2)min(d_-^2,d_+^2))].               (4)

Every full rational endpoint and both independent radii are checked,
as are all reflected nodes and copied weights. For a completed odd-degree
zero node, P_N(0)=0, P'_N(0)=N P_(N-1)(0)!=0, and the exact weight
2/[N P_(N-1)(0)]^2 is checked separately. The maximum positive-node
radius is in(2^-560,2^-559] and maximum weight radius in(2^-549,2^-548],
verified by exact integer comparisons. Reflections preserve radii;
the two zero-node weights have zero radius. Thus the248-output assertion
does not rely on a floating approximation or an unfinished node.

### Exact finite counter stop

The construction's counter schedule is reproduced below. Each rate is
part of the fixed prescription; it is not a proved necessary cost.
Root/point/final counts are obtained from the complete trace, not samples.

| Category | Scheduled charge | Prefix total |
| --- | --- | --- |
| Grid generation |640*6|3840|
| Administration and tolerance constants |10000+4000|14000|
| Recurrence tables and degree bounds |117*20+3*30|2430|
| Mesh generation and order/domain |128*20+600|3160|
| Mesh evaluation control |384*12|4608|
| Bracket inventory and count |3*(127*12+20)|4632|
| Root initialization |124*100|12400|
| Bisection control |1971*40|78840|
| Point recurrence upfront charges |sum_N calls_N*(13*(N-1)+24)|3844534|
| Derivative enclosures |858*120|102960|
| Newton image/control |735*90|66150|
| Conversion fixed and tolerance |735*(40+16)|41160|
| Conversion halvings |67033*12|804396|
| Weight formation/output |123*100|12300|
| Reflection/output |123*40|4920|
| Zero-node formation |2*80|160|

The point-call counts for63,81,117 are841,1048,1326; the last includes
one prepaid but unexecuted call. All other counts agree with the trace:
1970 recorded bisections,735 updates,123 completed positive outputs,
and two zero outputs. The third bisection at the incomplete root pays
its40 control charge and checks the midpoint before requesting ev.
The ev charge is13*(117-1)+24=1532, paid before its point-domain guard
or any recurrence calculation. The recorded point-domain guard count
is therefore3214, one less than the number of upfront recurrence charges.

The category sum is5000490. Subtracting the last1532 gives4998958,
and4998958<=5000000<5000490. Every scheduled charge is nonnegative;
the reconstructed earlier prefix is consequently below the cap.
The pay function thus stops at exactly this request. Reconstructing
all categories independently gives exact equality with the reported
counter. This argument proves only the prescribed counter guard,
without assuming its conservative estimates are actual-cost lower bounds.

The full rational trace is
`scripts/separation-seven/certified-gauss-tolerance-cap-691.json`.
The unscaled complete recorded-prefix replay is
`scripts/separation-seven/certified-gauss-tolerance-cap-replay-691.json`:
156979 checks pass, with no failed check. The separate counter
reconstruction is `scripts/separation-seven/certified-gauss-tolerance-ledger-691.json`:
all six checks pass. They respectively verify rational inclusion/output
evidence and the counter arithmetic; neither is a full operation audit
or a certificate for the13 uncomputed outputs.

Reproduction from this notebook:

    python3 scripts/separation-seven/certified-gauss-tolerance-cap-691.py
    python3 scripts/separation-seven/certified-gauss-tolerance-cap-replay-691.py
    python3 scripts/separation-seven/certified-gauss-tolerance-ledger-691.py

Preserve this stopped prescription and the distinct C998k/C998l evidence.
An adaptive initial-refinement safeguard would be a separate finite
construction requiring its own complete checks; success is not inferred
from the accuracy of these248 outputs. No bank or signed comparison
is computed here.

## Mathlib

Full matching coverage for this finite prescription, its rational trace
and counter stop has not been checked. Supporting Legendre, rational
arithmetic or interval theorems would not by themselves certify this
service. Unknown availability is not evidence of absence. The precise
general source inputs and their applicable hypotheses are given above.
