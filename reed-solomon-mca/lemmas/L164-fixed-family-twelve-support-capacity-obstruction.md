# L164 — A coordinate-capacity obstruction on the fixed L162 family

## Hypotheses

Use the exact ordered sets S=(1,8,12,18,22,27,33) and
J=(47,50,64,70,75,79,85,89,96), original Cartesian lexicographic
labeling, and four fixed labels (35,522,477,566) of L162. Let
T_j=I_j union K_j be each original support. Use precisely L163's
forty-label set B, with no symmetry quotient. Degrees count incidences
as ordinary nonnegative integers, not as elements of F_97.

The finite selection problem asks for eight distinct labels from B
whose supports, together with the four fixed supports, have every
pairwise intersection of size at most one and every coordinate in
S union J of degree at most four.

For the additional fixed-family consequence, work over the algebraic
closure E of F_97, use L162's planes L_[r:s], and require all additional
rows to have exact restricted rank one and to be pairwise linear with
the four fixed supports. These are necessary conditions only; no coding,
weight, chart, descent or actual-event assertion is assumed.

## Conclusion

The finite selection problem is infeasible. In fact the degree bound
alone permits at most three labels from B to be added to the four
fixed supports. Thus seven is an upper bound on the total number of
rows in any such selection, without an attainment claim.

Consequently no plane in the fixed L162 family admits twelve distinct
supports containing its four fixed supports and satisfying the stated
pairwise intersection, exact-rank-one and degree requirements. This
does not exhaust the locus of planes satisfying the original four
rank conditions, exclude other plane families, or resolve the MCA
challenge. This is REPRODUCTION under the invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-26-l163-forty-support-compatibility-review.md`.
Its separate critical audit passed on 2026-10-26, as recorded below.

## Proof

### Complete reconstruction and the obstruction

There are binom(9,2)=36 choices of K for each I. Therefore the
zero-based original label j has I-index floor(j/36) and K-index
j modulo 36. Both pair lists are in increasing lexicographic order.
The complete set B splits into the following blocks:

| I-index | I | All labels in this block |
| --- | --- | --- |
| 4 | {1,27} | 145,147,148,149,160,161,171,174 |
| 9 | {8,27} | 325,327,328,329,340,341,351,354 |
| 16 | {18,27} | 577,581,582,583,595,596,609,610 |
| 18 | {22,27} | 649,653,654,655,667,668,681,682 |
| 20 | {27,33} | 723,724,726,727,748,749,751,752 |

Each interval [36m,36m+35] for the displayed I-index m contains
exactly its displayed eight labels. Direct enumeration of binom(S,2)
gives the stated I-pairs. These five blocks contain all forty labels
of L163 and show that 27 belongs to every T_j for j in B, independently
of K_j. No compatibility-based pruning or symmetry is used here.

The four fixed supports, in their designated order, are

    T_35 ={1,8,89,96},    T_522={12,33,64,85},
    T_477={12,27,50,70},  T_566={18,22,75,79}.

Thus the fixed contribution to degree at coordinate 27 is exactly one.
For any subset A of B the degree at 27 in the selected family is
exactly

    d_27 = 1 + |A|.

The required inequality d_27<=4 implies |A|<=3. In particular eight
additions would give d_27=9>4. This contradiction applies to every
eight-element subset of the complete B, regardless of any of its
other intersections or degrees. It is a short complete impossibility
certificate, not a relaxation asserted to be sufficient for feasibility.

For the fixed-family consequence, suppose a larger selection contains
the four fixed supports. Any additional support satisfying their four
pairwise intersection tests is eligible in L163. By L163, no eligible
additional row has rank one away from [1:94]; at [1:94] the eligible
rank-one labels are exactly B. Hence all additional rows, if any, must
be in B at that parameter. The bound just proved allows at most three.
At all other parameters no additional row is possible. This proves
the asserted fixed-family upper bound, retaining every hypothesis.

### Exact certificate and independent checking

The proof uses only finite incidence reconstruction and integer capacity
addition. The reviewed binary capacity formulation is documented in
SCIP 8.0.4, [Constraint Handlers, Knapsack Constraints and Linear
Constraints](https://www.scipopt.org/doc-8.0.4/html/group__CONSHDLRS.php).
No solver, complexity assertion, maximal-clique theorem or general
enumeration reproof is needed: the single coordinate inequality
already contradicts the requested cardinality.

Reproduce from the active notebook with

```bash
python3 scripts/seven-coordinate/forty_support_compatibility.py
python3 scripts/seven-coordinate/verify_forty_support_compatibility.py
```

The producer enumerates all 756 original labels and saves all forty
candidate supports, four fixed supports, all 946 pair intersections,
all sixteen fixed degrees, all sixteen candidate-universe degrees,
the common-coordinate set, and the obstruction in
`scripts/seven-coordinate/forty-support-compatibility.json`. All forty
candidates pass the four fixed-support intersection tests; the fixed
rows pass their six mutual tests. Candidate-universe degrees are
degrees of all forty rows, not degrees of a selected eight-row family.
The proof uses only their common incidence at 27.

The verifier imports no producer code. It reads the complete canonical
B from L163, independently rebuilds the 756-label table using explicit
ordered index loops, and checks every stored support and intersection,
every coordinate count, all forty common incidences, the fixed-row
contribution and the exact integer contradiction. It checks source
SHA-256 bindings and retains the certificate hash. All 226 checks pass,
with no failures, in
`scripts/seven-coordinate/forty-support-compatibility-verification.json`.
These same-step independent computations support the displayed complete
arithmetic proof; those original same-step checks are not proof-assistant
verification or the separate later critical audit below. No incomplete
search or sample underlies exclusion.

### Separate critical audit, 2026-10-26

The first separate audit under the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-26-l164-critical-audit-review.md` passes without
changing the hypotheses, conclusion or direct mathematical inputs. The
complete producer and verifier scripts were read; replaying the existing
verifier passes all 226 checks. A further checker importing neither
script is reproduced from the active notebook by

```bash
python3 scripts/seven-coordinate/audit_l164.py
```

Its full certificate is `scripts/seven-coordinate/l164-critical-audit.json`.
All 276 checks pass, without failures. It reads the complete canonical B
from L163, checks its forty distinct labels and disjointness from the
fixed labels, and binds the original certificate to exactly the two
required source files. It independently decodes pair ranks using their
triangular prefix counts, rather than either earlier enumeration. Every
one of the 44 records, all 946 intersections, all sixteen fixed degrees
and all sixteen candidate-universe degrees match. All six fixed/fixed
and 160 candidate/fixed intersections have size at most one. The five
I-blocks contain eight labels each and decode to precisely the displayed
five I-pairs. All forty candidates contain 27, and row 477 is the only
fixed user of 27. The entire replay-verification record and its source
hash match. The retained support records and both complete degree maps
were also inspected, not inferred from a summary or sample.

The hypothesis application was checked separately from computation.
Distinct original supports have distinct labels because S and J are
disjoint and each support recovers its I and K by intersection with
them. Thus any additional distinct original support satisfying the four
fixed intersection tests is an eligible additional label in L163's
exact sense. Audited L162 supplies a genuine plane and all four exact
ranks at every parameter. Audited L163 covers every eligible row over
E, including the endpoints and rank-zero exclusions: its rank-one locus
is empty or exactly [1:94], and the nonempty labels are exactly B.
At every other parameter no addition is possible. At [1:94], any
selection A has the ordinary integer degree 1+|A| at 27, so degree at
most four implies |A| at most three. This applies to every subset of B;
candidate/candidate compatibility need not be presumed or exhaustively
searched to obtain this necessary bound. The full intersection records
are checked, but their mutual compatibility is not asserted.

No discrepancy requires reopening L163's polynomial certificates. This
is local verification progress using the precise standard capacity
coverage already cited, not new mathematics beyond those sources. The
audit adds no premise from L159–L161, no attainment at seven, and no
all-plane, finite coding-field, coding-realization or MCA conclusion.
Python and ordinary integer arithmetic remain shared implementation
assumptions; neither proof-assistant verification nor Mathlib coverage
is claimed. The main argument and dependency graph are unchanged.

## Mathlib

Full matching Mathlib coverage is not checked. This instance needs only
finite-set incidence counting and integer addition; no absence claim
about formal-library coverage is made.
