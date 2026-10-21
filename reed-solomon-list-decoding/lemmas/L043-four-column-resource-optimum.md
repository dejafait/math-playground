# L043 — Exact four-column five-subset resource optimum

## Hypotheses

Let Omega={0,...,8} times F_107. Retain all graphs of polynomials
of degree at most four on the nine indicated distinct evaluation
points. Let P be a family of distinct nine-subsets of Omega, each
meeting at most four evaluation columns. Require distinct members
of P to intersect in at most four points. No blocks involving the
two extra points of a 965-point embedding are included.

For a block, its column profile is the decreasing partition a of
nine consisting of its positive column sizes. For a five-subset,
define its profile b in the same way. The resource relaxation has
one nonnegative real variable x_a for every partition a of nine
with at most four parts, and one constraint for every partition b
of five with at most four parts. The constraint counts five-subsets
of that profile, each available at most once. Its objective is
sum_a x_a. This lemma concerns exactly this relaxation, not its
integer optimum or realizability by a packing.

## Conclusion

The exact resource-relaxation optimum for added blocks is

\[
 U=348507187854/19.
\]

The imported graph baseline has 107^5=14025517307 blocks. It is
compatible with every member of P. Thus this relaxation bounds the
total by

\[
 107^5+U=614992016687/19,
 \qquad \lfloor107^5+U\rfloor=32368000878>19800269675.
\]

The prescribed resource test does **not exclude** threshold crossing.
Even its integer feasible profiles are not excluded at that threshold,
but no actual added packing is constructed. No ordinary packing lower
bound, useful L041 labeled cap, RS realization, cross-core consistency
or improvement of the 955–957 bracket follows.

## Proof

**Assessed inputs and compatibility.** The prior EXPLORE assessment
`drafts/literature/2026-10-10-four-column-packing-resource-test.md`
covers this exact finite test. Import Liqing Xu and Hao Chen,
*New Explicit Binary Constant Weight Codes from Reed-Solomon Codes*,
[arXiv:1505.06524v4](https://arxiv.org/pdf/1505.06524v4),
7 August 2015, Proposition 2.2, printed p. 3: for prime power q and
q>=w>r-1, the degree-at-most-(r-1) graphs on any w distinct field
points give q^r weight-w words of length wq and distance at least
2w+2-2r. Here 107 is prime (none of 2,3,5,7 divides it), and
107>=9>4. With (q,w,r)=(107,9,5), this supplies the specified
107^5 graph blocks, pair intersections at most four and length 963.
The graph construction is cited, not reproved. Optional augmentations
from the source's Theorems 2.1–2.2 are not retained in this test.

Each graph has one point in each column. An added block meeting
at most four columns therefore meets every graph in at most four
points. The union is an ordinary packing precisely when the added
blocks satisfy their stated pair condition. Import the terminology
from R.A. Bailey and A.C. Burgess, *Generalized packing designs*,
[arXiv:1107.4120v2](https://arxiv.org/pdf/1107.4120v2),
15 November 2011, printed p. 2, Definition 1.1.1, at
(v,k,t,lambda)=(963,9,5,1). Each five-subset is in at most one
block. The equivalence with intersections at most four follows:
a common five-subset exists exactly when the intersection has size
at least five. These positive integer parameters satisfy v>=k>=t.
No design existence or asymptotic theorem is used.

**Complete resource counts.** All five-subsets of any graph use five
distinct columns. Every five-subset of an added block uses at most
four columns, so the resource classes below are entirely unoccupied
by the graph baseline. For a resource partition b=(b_1,...,b_l),
write m_j for the number of its parts equal to j. Its actual capacity
in Omega is

\[
 c_b=\frac{9!}{(9-l)!\prod_j m_j!}
                 \prod_{i=1}^l\binom{107}{b_i}.                 \tag{1}
\]

The first factor chooses distinct labeled columns for the parts,
dividing only the assignments exchanging equal parts. The second
chooses their points. Thus (1) counts each five-subset exactly once.
It includes all column choices, without assuming that P is invariant
under a column permutation or an arbitrary point relabeling.

For a block profile a=(a_1,...,a_s), the number of five-subsets of
type b in one block is

\[
 A_{b,a}=\sum_{\substack{0\le u_i\le a_i,\ \sum_i u_i=5\\
                \operatorname{sort}(u_i:u_i>0)=b}}
                 \prod_{i=1}^s\binom{a_i}{u_i}.                 \tag{2}
\]

The choices in different columns are independent, and the vector
u specifies each five-subset uniquely. Distinct added blocks cannot
share one by packing uniqueness. Consequently their integer profile
counts satisfy A x<=c. Relaxing the counts to nonnegative reals is
therefore a valid upper bound. No sufficiency of these inequalities
for actual blocks is asserted.

There are exactly eighteen block types and six resource types. In the
table, columns are in the order 5,41,32,311,221,2111. A string such
as 5211 denotes the partition (5,2,1,1), not an integer. The last
column is W_a=17 A_(5,a)+2 A_(32,a)+A_(221,a).

| a | 5 | 41 | 32 | 311 | 221 | 2111 | W_a |
|---|---:|---:|---:|---:|---:|---:|---:|
| 9 | 126 | 0 | 0 | 0 | 0 | 0 | 2142 |
| 81 | 56 | 70 | 0 | 0 | 0 | 0 | 952 |
| 72 | 21 | 70 | 35 | 0 | 0 | 0 | 427 |
| 711 | 21 | 70 | 0 | 35 | 0 | 0 | 357 |
| 63 | 6 | 45 | 75 | 0 | 0 | 0 | 252 |
| 621 | 6 | 45 | 20 | 40 | 15 | 0 | 157 |
| 6111 | 6 | 45 | 0 | 60 | 0 | 15 | 102 |
| 54 | 1 | 25 | 100 | 0 | 0 | 0 | 217 |
| 531 | 1 | 20 | 40 | 35 | 30 | 0 | 127 |
| 522 | 1 | 20 | 20 | 40 | 45 | 0 | 102 |
| 5211 | 1 | 20 | 10 | 50 | 20 | 25 | 57 |
| 441 | 0 | 10 | 48 | 32 | 36 | 0 | 132 |
| 432 | 0 | 5 | 23 | 32 | 66 | 0 | 112 |
| 4311 | 0 | 5 | 18 | 37 | 36 | 30 | 72 |
| 4221 | 0 | 5 | 8 | 32 | 41 | 40 | 57 |
| 333 | 0 | 0 | 18 | 27 | 81 | 0 | 117 |
| 3321 | 0 | 0 | 8 | 22 | 51 | 45 | 67 |
| 3222 | 0 | 0 | 3 | 12 | 51 | 60 | 57 |

Every coefficient column sums to binomial(9,5)=126, so all subsets
of a block are accounted for. The capacities and the primal slacks
used below are:

| b | c_b | c_b-(Ax)_b |
|---|---:|---:|
| 5 | 956777094 | 0 |
| 41 | 39757339440 | 24754731624/19 |
| 32 | 81043807320 | 0 |
| 311 | 572658600780 | 238915600560 |
| 221 | 867168738324 | 0 |
| 2111 | 3501398301912 | 47720630920662/19 |

As a check on resource completeness, the only other profile of five
is 11111, whose capacity is binomial(9,5)*107^5. The sum of that
capacity and the six displayed capacities is binomial(963,5).
This last class is deliberately omitted from the added-block LP,
since its incidence coefficients for all eighteen types are zero.

**Exact optimal certificates.** Set

\[
 y=(17,0,2,0,1,0)/57.
\]

All entries of y are nonnegative. For every block type a, the table
gives (A^T y)_a=W_a/57>=1. Hence, for any feasible nonnegative x,

\[
 \sum_a x_a\le \sum_a (A^Ty)_a x_a
               =y^TAx\le y^Tc
               =\frac{17(956777094)+2(81043807320)+867168738324}{57}
               =348507187854/19.                              \tag{3}
\]

This inequality is proved directly; no LP duality theorem or
numerical optimizer is required. Equality is attained in the resource
relaxation by setting all x_a to zero except

\[
 x_{5211}=956777094,\quad
 x_{4221}=367059422016/95,\quad
 x_{3222}=1284582693324/95.                                  \tag{4}
\]

These values are nonnegative. Substitution into all six rows gives
the six nonnegative slacks displayed above. The sum of the three
variables in (4) is 348507187854/19, equal to (3). Thus the upper bound and attainment
are certified, giving the exact optimum. The primal variables in (4)
describe counts in a relaxation only. Rounding these three variables
down preserves feasibility, since A has nonnegative entries. The sum
loses less than three, so the integral total is at least
floor(107^5+U)-2=32368000876, also above 19800269675. This is merely
an integer resource witness; it is still not a packing construction.

**Reproducible exact verification.** Run, from the notebook directory:

```text
python3 scripts/finite-support/four_column_resources.py
python3 scripts/finite-support/audit_four_column_resources.py
```

The first uses rational arithmetic throughout its finite simplex and
saves every profile, coefficient, capacity, primal/dual variable,
usage, slack, objective and threshold in
`scripts/finite-support/four-column-resource-results.json`.
The second does not use the simplex or import its counting functions.
It enumerates all eighteen profiles by decreasing four-tuples,
each block's 126 actual five-subsets by point indices, and all 1287
labeled weak compositions of five into nine columns for capacities.
It then checks all 108 coefficients, all six capacities, every primal
row and every dual column, both equal rational objectives, the total
and the integer comparison. All 79 audit checks pass; failures are
empty in `scripts/finite-support/four-column-resource-audit-results.json`.
The complete relevant matrix, capacities, witnesses, slacks and dual
column values were inspected, not just a preview. These checks support
the explicit proof (1)–(4); a pivot trace is not needed for optimality.

**Downstream limit and route decision.** The canonical statements of
L041 and audited L042 were read for interpretation only; neither is
an input to the resource proof. L041's sufficient uniform cap is
19800268651. L042 would turn an actual ordinary packing above
19800268651+1024=19800269675 into an admissible family exceeding
that cap at each core after a chosen embedding. Here there is no such
packing: profile constraints omit the detailed extra/extra intersections.
Therefore this lemma obstructs only the proposed resource-exclusion
test. Park that upper diagnostic; it cannot decide the construction
question. Do not infer nonexistence, existence, actual-label symmetry,
RS realization, cross-core compatibility or safety. Independent gaps
at 67/68 agreements and the source-definition comparison remain open.

The completed step is POTENTIALLY_NEW only in the process sense that
the saved search did not identify this finite optimum. The graph
baseline and ordinary uniqueness are imported known tools; no
certified novelty or complete candidate solution is claimed. The separate
critical proof review below retains this result.

**Separate critical audit (2026-10-10).** The turn-start EXPLORE
assessment `drafts/literature/2026-10-10-four-column-resource-critical-audit.md`
covers this exact audit. Its source coverage is reused without an
additional retrieval. The following checks retain the statement and
its scope; this is REPRODUCTION of the existing finite argument,
not a new optimum or a claim of progress beyond the sources checked.

1. **Source specialization and compatibility.** The cited Xu–Chen
   proposition applies because 107 is prime and 107>=9>5-1. Its
   length is 9*107=963, weight is nine, distance is at least ten,
   and size is 107^5. Distance at least ten means intersections
   at most four. Every proposed additional block uses at most four
   columns, whereas a graph uses exactly one point per column, so
   their intersection has size at most four. They are distinct
   because their column supports have different sizes. The two
   embedding points remain unused, and source augmentations are
   absent. All remaining packing conflicts are between additions.
2. **No omitted profiles or resources.** For largest block part
   9,8,7,6,5,4,3, the numbers of partitions of nine into at most
   four positive parts are respectively 1,1,2,3,4,4,3, as listed in
   the table. A largest part at most two cannot sum to nine in four
   parts. Thus all eighteen cases occur. The partitions of five
   into at most four parts are exactly the six listed; 11111 is
   the only omitted partition. Formula (1) divides by permutations
   of equal-sized parts only, and (2) counts each five-subset by
   its unique within-column size vector. These count all labeled
   placements; no symmetry of a family is used. Aggregating the
   individual five-subset uniqueness inequalities gives Ax<=c,
   and introduces a relaxation, never a construction. The graph
   baseline consumes none of these six classes.
3. **Complete evidence and proof tables.** Every load-bearing field
   of both original certificates was inspected in full using
   `../scripts/loop/inspect_json.py` with selected pointers. The
   original audit was rerun: its independent enumeration of actual
   block subsets and all 1287 column occupancies passes 79 checks.
   The new command
   `python3 scripts/finite-support/critical_audit_four_column_resources.py`
   enumerates zero-padded partitions, evaluates (1)–(2), checks
   both complete certificates, and parses both canonical proof
   tables. All 108 displayed coefficients, eighteen W values,
   six capacities and six slacks agree. Each block contributes
   exactly 126 subsets, and the six capacities plus the 11111
   capacity sum to binomial(963,5). The script imports no optimizer
   and no counting function from either previous program. Its 45
   checks pass, with no failures, in
   `scripts/finite-support/four-column-resource-critical-audit-results.json`.
   Discovery pivots/basis are not premises: explicit feasible equal
   witnesses suffice to prove optimality.
4. **All signs and exact attainment.** The stated y has nonnegative
   coordinates. The complete W column has minimum 57, attained
   exactly at 5211,4221,3222; hence every dual inequality holds.
   All three nonzero primal coordinates are positive. All six row
   usages and slacks were reconstructed, including the zero slacks
   at 5,32,221 and the positive slacks at 41,311,2111. The primal
   coordinates sum to 348507187854/19, equal to the dual cost. Nonnegativity
   justifies both inequalities in (3). Thus this is a maximum over
   feasible real profiles, with no appeal to numerical convergence
   or unverified strong duality.
5. **Integer rounding independently checked.** The floors of the
   three nonzero coordinates, in the order of (4), are
   956777094, 3863783389, 13521923087. Their six integer slacks,
   in the table's resource order, are
   (0,1302880615,7,238915600588,58,2511612153782), all nonnegative.
   Together with the baseline they give exactly 32368000877.
   The rational total satisfies
   614992016687=19*32368000878+5, so its floor is 32368000878.
   The proof's weaker integer-witness lower bound 32368000876 is
   valid. Both comparisons exceed the required strict benchmark
   19800269675. This certifies one integer resource vector; it
   neither determines the integer optimum nor realizes its blocks.
6. **Downstream implication and limits.** L041's canonical statement
   gives b_*=19800268651; audited L042 gives loss at most 1024 at
   each core. A genuine ordinary packing with size greater than
   b_*+1024, embedded in each 965-point complement, would leave
   an admissible family larger than b_* there. Ordinary packing
   survives a bijection; actual-label admissibility would follow
   from L042's deletions, not from label symmetry. The present
   certificates never supply that packing. They only show that
   these aggregate constraints, even with integral counts, cannot
   exclude crossing the benchmark. Local admissibility would still
   not establish cross-core compatibility or an RS list. The
   67/68-agreement safety questions and source-definition comparison
   remain unresolved.

No mathematical defect was found. The separate review establishes
the checked status of this local resource result and retains the
recorded stop on the exclusion diagnostic, without changing the main
boundary. L041/L042 were used to check the conditional interpretation,
not the resource optimum, so L043 still has no local lemma inputs.

## Mathlib

Full matching coverage and supporting finite-set, polynomial and
linear-inequality declarations were **not checked**. No absence is
asserted. The exact rational files are informal certificates, not a
formal Mathlib proof.
