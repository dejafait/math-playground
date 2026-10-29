# L167 — Completion does not force the S-marked four-edge pattern

## Hypotheses

Use the fixed disjoint parts

    S={1,8,12,18,22,27,33},
    J={47,50,64,70,75,79,85,89,96},   H=S union J.

The proposed implication concerns every family F of sixteen distinct
four-subsets of H such that any two intersect in at most one label and
every label of H has integer degree exactly four. Define the **complete**
subfamily E_2={A in F:|A intersection S|=2}, and assume 12<=|E_2|<=14.
The proposed conclusion is that four distinct members of E_2 have exactly
one singleton pair intersection in S and their other five pair
intersections are empty. No extra restriction on completing rows,
resolvability, representation, moments, weights or coding realization
is part of this implication.

## Conclusion

The implication is false. The full sixteen-row family below satisfies
every premise and has |E_2|=12. All four remaining rows have S-overlap
one. Every four members of E_2 have at least **three** intersecting
pairs, whereas the requested pattern has exactly **one**. In particular,
the witness does not rely on an isolated S label or on a partial family
that might fail to complete.

This is a local negative result for the completion-sensitive incidence
criterion. It does not refute uniform twelve-row geometric exclusion,
C152a, or the grand MCA challenge, and it supplies no coding realization
or radius improvement. Classification: **REPRODUCTION**, a specialization
of L072's known affine-plane construction under the prior EXPLORE
assessment `drafts/literature/2026-10-26-completed-family-seed-review.md`.
No mathematical originality beyond the sources checked is claimed.
Same-step independent replay and a separate critical audit on 2026-10-27
pass. This validates the local counterexample, not an additional
mathematical discovery or a coding realization.

## Proof

### Reused construction and the fixed labeling

Import the four-class construction and exact incidence rule proved in
L072. Its standard source is O. Olmez and A. Ramamoorthy, *Repairable
Replication-based Storage Systems Using Resolvable Designs*,
[arXiv:1210.2110v1](https://arxiv.org/pdf/1210.2110v1), 7 October 2012,
Section III, Definition 3 and class-selection paragraph, pp. 3–4;
Section III.A, p. 4, and Lemma 2, p. 5. This turn reuses L072's cited
construction and complete local proof; it does not claim a fresh read
of the external paper or depend on an unread configuration census.

Specifically, let K=F_2[u]/(u^2+u+1), with elements 0,1,u,u+1. Use the
sixteen points of K^2 and exactly the same four classes as L072:
vertical lines X=e and slope classes Y=mX+e for m=0,1,u, with e in K.
There are four lines per class. Each class partitions the points; distinct
lines within one class are disjoint, and lines from different classes
meet in exactly one point. Thus there are sixteen distinct four-point
lines and every point has degree four. These are the already established
incidence properties, not a reproof of general affine-plane existence.

Replace L072's abstract point labels by this explicit bijection to H:

| X \\ Y | 0 | 1 | u | u+1 |
|---|---|---|---|---|
| 0 | 1 | 47 | 50 | 64 |
| 1 | 70 | 75 | 8 | 12 |
| u | 18 | 22 | 79 | 85 |
| u+1 | 89 | 96 | 27 | 33 |

Every specified numerical label appears once. A bijection preserves
sizes, intersections and degrees, so the sixteen relabeled lines give
the required full-family incidence premises. The auxiliary field K has
characteristic two; this labeling is **not** a field embedding into the
characteristic-97 coding field and is not a moment-preserving symmetry.

The S points are the union of the two omitted-direction lines

    D_0: Y=(u+1)X,       D_1: Y=(u+1)X+1,

with P=(0,1) removed. Indeed D_0 has labels {1,12,22,27}, while D_1
has labels {47,8,18,33}, with P labeled 47. Their union minus P is
exactly the fixed S. Each retained line meets each D_i in one point,
because its direction differs from u+1. The D_i are disjoint, so the
two intersection points are distinct. The unique line through P in
each retained class consequently has one S point, and the other three
lines in that class have two. There are therefore twelve E_2 rows and
four completing rows; no S-overlap-three or S-overlap-four row has
been silently discarded.

### The entire completed family

The complete table makes this specialization independently checkable.
Rows in each group of four constitute one of the retained parallel
classes, with intercepts in the order 0,1,u,u+1.

| Row | Class | A intersection S | A intersection J |
|---|---|---|---|
| 1 | vertical | 1 | 47,50,64 |
| 2 | vertical | 8,12 | 70,75 |
| 3 | vertical | 18,22 | 79,85 |
| 4 | vertical | 27,33 | 89,96 |
| 5 | slope 0 | 1,18 | 70,89 |
| 6 | slope 0 | 22 | 47,75,96 |
| 7 | slope 0 | 8,27 | 50,79 |
| 8 | slope 0 | 12,33 | 64,85 |
| 9 | slope 1 | 1,33 | 75,79 |
| 10 | slope 1 | 27 | 47,70,85 |
| 11 | slope 1 | 12,18 | 50,96 |
| 12 | slope 1 | 8,22 | 64,89 |
| 13 | slope u | 1,8 | 85,96 |
| 14 | slope u | 12 | 47,79,89 |
| 15 | slope u | 22,33 | 50,70 |
| 16 | slope u | 18,27 | 64,75 |

Precisely rows 1,6,10,14 are outside E_2. All other rows have two
labels in each part, so E_2 is the complete twelve-row two-plus-two
subfamily, not a selected subset of a larger E_2. The entire sixteen-row
table, rather than E_2 alone, has degree exactly four at every label.
All seven S labels occur even in E_2: labels 1,12,22,27 have E_2 degree
three, and labels 8,18,33 have E_2 degree four. Hence L166's isolated-label
obstruction is not being reused as an unproved completion argument.

### Exclusion of every marked four-subset

Let four distinct E_2 rows be chosen, and let a_1,...,a_4 be their
occupancies in the four parallel classes. Each a_i is an integer between
zero and three, because each class contributes exactly three rows to
E_2, and sum a_i=4. By the exact incidence rule, an unordered pair
of chosen rows is disjoint if and only if it belongs to one class.
Thus the number t of intersecting pairs is

    t = binomial(4,2) - sum_i binomial(a_i,2).

Up to order, the only positive occupancy lists are (3,1), (2,2),
(2,1,1), and (1,1,1,1); the corresponding values of t are 3,4,5,6.
This list is exhaustive: if the largest occupancy is three, the other
one is one; if it is two, the residual two are together or separate;
if it is one, all four are one. Therefore t>=3 for every four-subset
of E_2. The proposed S-marked pattern has t=1, a contradiction regardless
of the location of any intersection. Concurrent triples do not change
this argument: it counts intersecting **pairs**, including every pair
through a common point. It does not confuse their count with the number
of distinct intersection points.

The achieved lower bound 3 is strict against the required value 1 and
is attained by three E_2 rows from one class and one from another.
One complete witness at |E_2|=12 refutes the asserted universal range
12–14. No separate conclusion about a strengthened 13–14-only claim
is proved or needed here.

### Exact evidence and limitations

The proof uses the imported explicit construction and the displayed
finite tables, independently of search completeness. Supplementary
construction and a separately transcribed table/column replay are:

```bash
make -C scripts/completed-family-extraction check
```

`scripts/completed-family-extraction/counterexample.json` saves all
sixteen rows, sixteen degrees, 120 pair intersections and every one
of the 495 four-subsets of E_2, including its six pair intersections.
`scripts/completed-family-extraction/verification.json` reconstructs
the full incidence columns from a literal table without importing the
constructor, compares all saved relevant records, and checks the target
independently using sums of binomial(coordinate multiplicity,2) in S
and J. For linear rows the target is exactly S sum one and J sum zero.
It also checks the parallel-class formula above for every four-subset.

All 657 same-step replay checks pass, with no failures. The complete
histogram of intersecting-pair counts is 36 subsets with t=3, 54 with
t=4, 324 with t=5, and 81 with t=6, totaling 495. Actual/required values
are sixteen rows/sixteen, degrees four/four, maximum pair intersection
one/at most one, |E_2|=12/in [12,14], and zero marked subsets/zero for a
counterexample. This exhaustive check of one witness is not a census
of all sixteen-row families or a separate later critical audit.

### Separate critical audit, 2026-10-27

The separate audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-27-l167-critical-audit-review.md`, reusing its
primary-source coverage without further literature discovery. It reads
L072 and this proof in full and verifies the necessary local
specialization rather than reproving general affine-plane existence.
The full plane's incidence rule is restricted to the four specified
classes; the restriction is not asserted to remain a BIBD.

The new `scripts/completed-family-extraction/audit_l167.py` imports
neither original producer. It parses both canonical coordinate tables,
uses binary-polynomial multiplication reduced by u^2+u+1 instead of
the constructor's multiplication table, and reconstructs all coordinate
blocks. All sixteen L072 blocks and its prescribed triangle agree.
For this proof, the bijection, omitted-direction lines, removed point,
all sixteen displayed rows and incidence columns agree. The complete
E_2 is exactly the twelve claimed rows, all four omitted rows have
S-overlap one, and the seven E_2 degrees are (3,4,3,4,3,3,4) in increasing
S order. Every full-family label has degree four.

The audit reconstructs and compares every field of all 120 saved pair
records, all 495 saved quadruple records, their coordinate multiplicities
and class occupancies in both existing certificates, and both complete
summaries. It checks the direct singleton-S predicate against the
multiplicity predicate separately, after establishing linearity. All
684 checks pass with no failures; the histogram is again
{3:36,4:54,5:324,6:81}. Full reconstructed evidence, checks and input
hashes are saved in
`scripts/completed-family-extraction/l167-critical-audit.json`.
Reproduce without regenerating either original certificate:

```bash
make -C scripts/completed-family-extraction audit
```

The analytic occupancy proof is also valid: the positive parts of four
nonnegative occupancies bounded by three and summing to four have exactly
the four listed partition types; different-class pairs intersect and same-class pairs
do not. Concurrent pairs retain their multiplicities. The (3,1) case
exists because every class has three E_2 rows, so the lower bound three
is attained, not merely estimated. The comparison 3>1 excludes the
target for this full witness. The endpoint |E_2|=12 lies in the proposed
universal interval, so it suffices to refute that implication without
any assertion restricted to 13–14. No hypothesis was strengthened or
coding premise inserted. Verdict: the finite abstract counterexample
passes; no mathematical correction or new dependency is required.

L072 is the direct mathematical input. L166, C152a and L165 are contrasts
or motivation only; L086/L109 supply no premise needed to verify this
abstract counterexample, and L159–L161 are not inputs. The witness even
has the necessary overlap profile (n_0,n_1,n_2)=(0,4,12), but it asserts
no syndrome plane, nonzero recovered weights, finite parameters, charts,
or actual t=0 equality events. A single resolvable witness suffices for
the counterexample; no assumption that all admissible families are
resolvable or isomorphic to it is made. Numeric-label transport of
L165, arbitrary representation, challenge identification and the sharp
radius remain separate gaps. Neither the coding target nor its frozen
11/q–16/q interval changes.

## Mathlib

Full matching coverage of this labeled completion-sensitive
counterexample: **not checked**. Supporting affine-plane and finite-set
coverage: **not checked**. No absence or formal-verification claim is
made. The standard construction is cited and imported through L072;
the additional labeling, complete E_2 calculation and pattern test are
the necessary local specialization.
