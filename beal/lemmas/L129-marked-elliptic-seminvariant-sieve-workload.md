# L129 — Signed seminvariant regions and a fixed-sieve workload stop

## Hypotheses

Use L128's certified invariant pair

    I=8624880, J=−46962471600,
    4I³−J²=360895702709586528000>0,

and its three resolvent roots phi1>phi2>phi3, exact rational
isolating intervals, and nonzero leading-coefficient regions. Work over Q.
A quartic has coefficients (a,b,c,d,e), invariants

    I(g)=12ae−3bd+c²,
    J(g)=72ace+9bcd−27ad²−27eb²−2c³,

and seminvariants p=3b²−8ac, r=b³+8a²d−4abc.
The reduced b interval is −2|a|<b<=2|a|. Retain the identity
cover separately; this statement uses no division by a when a=0.

Fix, before arithmetic, exact divisibility of the syzygy right side
by 27 and square-image tests modulo 64,5,7,11,13. The tested traversal
would inspect each surviving integer (type,a,p), test the exact square
syzygy, retain both signs of r and zero, then recover b and reconstruct
coefficients. The caps are 200000 charged counting/inspection units
and 2000000 expanded (type,a,p,r,b) candidates. This is one fixed
traversal, not an optimality claim about every possible sieve.

## Conclusion

Put D=4(I−phi2²)/3. The source regions translate exactly as follows:

| Region | a | Closed p interval |
| --- | --- | --- |
| Type 1 | 1,...,1043 | [−4a phi1, −4a phi2] |
| Type 2, positive | 1,...,898 | [−4a phi3, D−4a phi2] |
| Type 2, negative | −1,...,−144 | [−4a phi1, D−4a phi2] |

These bounds, exact syzygy squares, complete b-congruence recovery
and integral reconstruction retain every integral representative in
the imported nonzero-a source regions. Bounds alone need not determine
the real type; keeping overlapping regions is harmless overcounting.

For the fixed sieve above, the type-one prefix 1<=a<=34 alone contains
exactly 216116 modular surviving (a,p) pairs, already above 200000.
One counting pass uses 100113 units; complete certificate verification
uses another 91850, for 191963<=200000 per pass. Two executions were
performed after an accounting repair, costing 383926 cumulatively,
above the saved cap; whole-step budget compliance is not claimed.
The prescribed traversal
therefore fails its inspection cap before exact square testing or
expansion. This is not a lower bound on actual square syzygies,
integral quartics, equivalence classes, locally soluble coverings or
Selmer size. No upper rank or Beal exclusion follows.

## Proof

### Imported algorithm and applicability

Import J.E. Cremona, *Algorithms for Modular Elliptic Curves*, second
edition (CUP, 1997), corrected online Chapter III, Section 3.6 Step 2,
printed pp.93–95, coefficient bounds p.94, syzygy (3.6.7) and
reconstruction p.95:
[author's chapter](https://johncremona.github.io/book/fulltext/chapter3.pdf).
The algorithm supplies representative regions for nonzero discriminant
and separates real types by its sign. L128 gives the required pair,
positive nonzero discriminant, root ordering and certified a maxima.
Only types 1 and 2 occur. Negative-definite type one is excluded by
real solubility; both type-two signs must remain. These are imported
representative bounds, not a new descent theorem or equivalence test.

The normalization and identity

    27r² = s(a,p) = p³−48Ia²p−64Ja³

are also stated in J.E. Cremona and T.A. Fisher, *On the equivalence
of binary quartics*, J. Symbolic Comput. 44 (2009), 673–682,
DOI [10.1016/j.jsc.2008.09.004](https://doi.org/10.1016/j.jsc.2008.09.004),
[3 December 2008 author manuscript](https://johncremona.github.io/papers/quartequiv.pdf),
Section 1, pp.1–2. The characteristic restriction excludes 2 and 3;
Q qualifies. For d use the corrected denominator 8a², also recorded in
[Cremona's errata](https://johncremona.github.io/book/errata.pdf),
26 September 2003, p.1. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-25-marked-elliptic-seminvariant-enumeration.md`.
The elementary change of traversal and its workload were the identified
instance obligations; reproving descent or class equivalence is unnecessary.

### Signed translation and integer endpoints

For type one, the source has

    (4a phi2+3b²)/(8a) <= c <= (4a phi1+3b²)/(8a).

Since a>0, substituting p=3b²−8ac reverses these c bounds and gives
the first row of the table. For type two with a>0 its c bounds are

    (4a phi2−D+3b²)/(8a) <= c <= (4a phi3+3b²)/(8a),

giving the second row. For negative a the source orders the roots
increasingly: its third root is our phi1, and its middle root remains
our phi2. Its inequalities, expressed in our notation, are

    (4a phi2−D+3b²)/(8a) >= c >= (4a phi1+3b²)/(8a).

Here −8a>0, so p increases with c. Applying that increasing affine
map to the displayed lower and upper c endpoints gives the third
row, including its signs. No positive-a division inequality was reused.
Conversely c=(3b²−p)/(8a) recovers exactly each displayed c region.

For integer p, bracket a real lower endpoint by [l0,l1] and an upper
endpoint by [u0,u1]. The outer interval is
[ceil(l0),floor(u1)] and the inner interval is
[ceil(l1),floor(u0)]. The actual integer interval lies between them.
Using L128's exact rational root brackets, the two intervals agree
for all 1043+898+144=2085 signed regions. Thus no endpoint ambiguity
remains in this instance. For the upper type-two endpoint, the verifier
evaluates 4(I−t²)/3−4at directly at phi2's endpoints: its derivative
−8t/3−4a is positive throughout the bracket for every relevant a.
This independently confirms the producer's wider interval arithmetic
and the same integer bounds. All inequalities are rational, not floats.

### Exact square and b recovery; conditional completeness

For a tested integer p require s(a,p) divisible by 27, compute the
integer quotient, and accept only if it is nonnegative and an exact
integer square q². Use r=q and r=−q, once when q=0. Modular tests
alone never perform this step. For fixed a,p, put m=|a| and M_b=8m.
Determine every residue j in {0,...,M_b−1} satisfying

    3j² = p modulo M_b.

For each such j take all integers k with

    floor((−2m−j)/M_b)+1 <= k <= floor((2m−j)/M_b),

and set b=j+k M_b. These inequalities are exactly
−2m<b<=2m after substituting b; they preserve the open lower end.
Every integer has a unique residue j and corresponding k, so this
procedure is exhaustive and has no duplicates. The interval length
4m is less than M_b, hence each j contributes at most one b. This
argument never divides by 3 modulo a modulus where 3 may be noninvertible.
It is a coverage proof, not a claim that enumerating all j fits the cap.
Every executed root trial would be charged. None was executed here.

For each recovered b reconstruct

    c=(3b²−p)/(8a),
    d=(r−b³+4abc)/(8a²),
    e=(I+3bd−c²)/(12a).

The b congruence is equivalent to c being integral, also for negative a.
Retain only integral d,e and verify both invariant equalities exactly.
The e formula already forces I(g)=I. Applying the imported syzygy
to the reconstructed quartic and comparing with the tested syzygy
gives 64a³(J(g)−J)=0, hence J(g)=J because a is nonzero.
The explicit invariant check is an additional safeguard. Conversely
an integral source representative has integer p,r, satisfies the
syzygy and b congruence, and is recovered by these inverse formulas.
It passes every necessary modular test. Thus this conditional ordering
covers the source representatives. The identity is retained separately,
and no class merging, local exclusion or identity classification is
asserted for other candidates.

### Fixed sieve, complete residue tables and CRT counting

Both 48I and 64J vanish modulo 27, so s(a,p)=p³ modulo 27.
Now 27 divides p³ exactly when 3 divides p. Likewise 48I vanishes
modulo 64 and 64J always does. The full 64-residue square-image table
shows that p³ is 27 times a square modulo 64 exactly when
p modulo 8 lies in {0,3,4}. This compression is checked at every
residue; it is not an assumption based only on odd p.

For each ell=5,7,11,13 form all ell values 27r² modulo ell and test
each p residue against that complete square image. For every counted
a retain all allowed p residues. The resulting coprime CRT moduli
are 3,8,5,7,11,13 with product M=120120. Their allowed Cartesian
product corresponds bijectively to a set R_a of residues modulo M.
The producer builds it incrementally: combining x modulo N and y
modulo ell gives x+N((y−x)N^(-1) modulo ell). This is the unique
combined residue and preserves all preceding congruences.

For a closed integer interval [L,U], the exact number of integers
p in residue q modulo M is

    max(0, floor((U−q)/M) − floor((L−1−q)/M)).

Indeed p=q+kM is in the interval exactly for integers k between
ceil((L−q)/M) and floor((U−q)/M); use
ceil((L−q)/M)=floor((L−1−q)/M)+1. Distinct residues are disjoint.
Summing the formula over R_a is therefore an exact count, without
inspecting each actual pair. The certificate saves each q, both
floor values and its contribution, not just a surviving-pair total.

Type-one a=1,...,33 give 198319 pairs. For a=34 its integer interval
is [−792265,307733], its complete residue set has 1944 elements,
and its progression count is 17797. Thus the prefix total is
198319+17797=216116. The full source-region count is not computed;
this subset alone supplies the required obstruction. No actual r
or b is claimed for any of these modular pairs. A traversal with
different rejection predicates or a method avoiding per-p inspection
is outside this result.

### Work ledger, verification and limitations

Reproduce with

    python3 scripts/pair-genus-two/seminvariant_workload.py
    python3 scripts/pair-genus-two/verify_seminvariant_workload.py

Full evidence is in
`scripts/pair-genus-two/seminvariant-workload-certificate.json` and
`scripts/pair-genus-two/seminvariant-workload-verification.json`.
All 2221 producer checks and 47610 verification checks pass, with
no failed checks. The verifier inspects every table entry, signed
integer region, CRT residue and saved floor-count tuple. It reconstructs
CRT residues independently using the direct idempotent sum
sum_j y_j (M/m_j) ((M/m_j)^(-1) modulo m_j) modulo M.
Uniqueness, product cardinality and equality with the saved residue
set establish complete recovery. It recounts all 44172 progression
records using the ceil/first-index formula, and checks every row total
and cumulative total, rather than relying on a preview.

| Charged operation | Producer | Verification |
| --- | ---: | ---: |
| Signed interval preparation/review | 2085 | 2085 |
| Divisibility residue cells | 27 | 27 |
| Square-image residue cells | 100 | 100 |
| Mod-64 predicate cells | 64 | 64 |
| Prime predicate cells | 1224 | 1224 |
| CRT inverse/idempotent preparation | 204 | 6 |
| CRT combination trials | 52237 | 44172 |
| Aggregate progression counts/recounts | 44172 | 44172 |
| Total | 100113 | 91850 |

These are the prescribed scalar work units, not machine-instruction
or big-integer bit-operation counts. Both preprocessing and verification
are recorded; combined work per execution is 191963<=200000. The first
producer ledger omitted 204 inverse preparations, displaying 99909
instead of 100113. The arithmetic output and verification passed, but
the ledger was incomplete. Correcting it and rerunning both scripts
repeated the same sieve and all its work. Counting those omitted
preparations in both executions gives 2*191963=383926>200000 actual
cumulative units. This execution overrun is preserved in the verification
certificate and history; no budget-compliant entire step is claimed.
There was no alternative-modulus search or cap increase. The mathematical
pair count is identical in both runs. The tested continuation
requires at least 216116 further explicit pair inspections, exceeding
the cap even on their own. No square tests, b-root trials, expanded
candidates or (a,b,c) triples were executed. Reconstruction failures
are an empty unattempted list, not a verified successful reconstruction.
The 2000000 expansion cap was not reached or certified feasible.

This local negative concerns the fixed sieve and per-p square testing,
not two-descent as a whole or the possibility of rank one. It does not
establish an optimal sieve, a lower bound on actual square syzygies,
or any Selmer/rank conclusion. L128's raw-loop stop is preserved.
The source comparison found no duplicate instance certificate; that
does not establish originality. This is reproduction/specialization
of known algorithms. Elliptic upper rank, the genus-two rank, marked
lifts, degree-nine recovery, both integer systems, minus-eleven and
other residual signatures remain separate gaps.

## Mathlib

Full matching traversal/completeness and this exact-instance workload
certificate were not checked in Mathlib. No absence or Lean verification
is claimed. The cited reduction/reconstruction algorithm and the exact
elementary calculations above are the informal inputs.
