# Two parallel fibers — bounded mathematical working record

Approved target: Test whether two parallel auxiliary lines can both have coefficient-image affine dimension two while satisfying all six transverse evaluation matchings in the pinned L030 labeling.

Prior assessment: `literature/2026-10-28-two-parallel-fiber-cyclic-matchings.md`
(EXPLORE, saved before invocation). This is one mathematical attempt.
The supplied PROOF.md and DAG were used before reading L030's model,
the saved span-three working record, ATTEMPTS/109–110 and history/538–539.
Existing notebook changes and unfinished work are preserved. No
cross-notebook input or new source theorem is used.

## Scope, relevance and decisive test

Keep q=137, T={16,64,70,102,112,118,121}, E=F_65537,
F=F_(65537^28), H=<19139> of order 1024, k=64, any 61-core C,
the original bijection sigma onto H minus C, K=E or F, a in T
and h!=0 in F_137. Write x_(t,y)=sigma(t,y), x_0=x_(a,0),
x_1=x_(a,h), and d_r=h/(r-a). The two families R_w,S_z have
degree at most two; repetitions are allowed. All six full matchings
R_w(x_(r,(r-a)w))=S_(w-d_r)(x_(r,(r-a)w)) and both fiber
constancies at x_0,x_1 are required. All actual labels are distinct.

The main gap is arbitrary-center 67/68 safety. A uniform obstruction
would constrain coexistence of rank-two fibers in a full sheet;
a permitted exact witness would abandon only this reduced obstruction.
A lone rank-two fiber, global collapse, partial retention, compatible
laws and RS transfer remain independent gaps. The decisive test is
an exact permitted witness checking all 822 matching equalities,
both constancies and both dimensions, or an impossibility proof
uniform in C,sigma,a,h,K. Generic rank and sampled failure decide neither.

## Initial mechanism and checkpoint

Subtract a common polynomial of degree at most one interpolating the
two fiber-constant values at distinct x_0,x_1. This preserves all
matching equalities and affine dimensions and makes those constants
zero. The two coefficient planes then meet in the line spanned by
(X-x_0)(X-x_1). The intended test is to exploit this common line and
the six cyclic shifts simultaneously, retaining arbitrary labels and
repeated coefficient points; no projectivity or equivariance is assumed.
This checkpoint is saved before the longer mathematical attempt.

## Reflection construction test (unfinished)

For an existential test, choose a permitted labeling with x_0=1,
x_1=-1 and h=1. Both anchors lie in H and are distinct. Prescribe

\[
 R_w(X)=V_w(X^2-1)+U_w(X-1),\qquad S_z(X)=R_{-z}(-X).
 \tag{1}
\]

This is an ansatz for a witness, not a consequence imposed on arbitrary
solutions. The two constancies are zero automatically. The affine
dimensions of the two coefficient images agree, and equal the affine
dimension of the points (U_w,V_w). A transverse matching r joins w to
v=d_r-w, where d_r=1/(r-a); hence it is an involution. Its unique fixed
point is w=d_r/2 in F_137. At this point the matching says
R_w(x)=R_w(-x), or 2U_w x=0. Every permitted actual label is nonzero
and the characteristic is odd, so all six fixed-point U values vanish.

For a nonloop edge {w,v}, oriented from w, the matching polynomial is

\[
 Q_{wv}(X)=(V_w-V_v)(X^2-1)+U_w(X-1)+U_v(X+1).
 \tag{2}
\]

It must have a root x in H other than the anchors. Since
Q_{vw}(-X)=-Q_{wv}(X), a chosen root x can serve the reverse matching
at -x. The 408 nonloop edges would therefore need distinct antipodal
pairs, followed by six unused distinct labels for the loops. This
would use all 822 transverse labels. This paired choice is sufficient
for a witness, not necessary for every solution of the ansatz.

There are two sound propagation rules before searching for those roots.
If U_w=U_v=0 and {w,v} is an edge, (2), with x not equal to either
anchor, forces V_w=V_v. If a vertex has two distinct neighbors both
carrying one even polynomial P=V(X^2-1), its polynomial agrees with P
at their two distinct actual labels and at the anchor 1, so it equals P.
The initially considered three-neighbor rule is valid but unnecessarily
weak; the automatic anchor root sharpens its threshold to two. These rules can be
iterated from the six fixed points, merging equal-value classes.
The bounded first test will compute this closure for each a in T.
Complete closure would exclude this particular construction, while
incomplete closure would not supply any permitted assignment.

## Exact closure result and its limits

The script `scripts/finite-support/two_fiber_reflection_closure.py`
enumerates every nonloop edge of each of the seven involution graphs.
It starts with the six forced-even vertices, merges adjacent even
vertices, and adds any vertex with two neighbors in one equal-polynomial
class, until neither rule applies. It records all edges, adjacency lists,
propagation events and final classes in
`scripts/finite-support/two-fiber-reflection-closure.json`.

| a | Forced-even vertices | Largest forced-equal class | Maximum neighbors in one class at an unmarked vertex |
|---|---:|---:|---:|
| 16 | 6 | 2 | 1 |
| 64 | 6 | 1 | 1 |
| 70 | 6 | 2 | 1 |
| 102 | 6 | 1 | 1 |
| 112 | 6 | 2 | 1 |
| 118 | 6 | 2 | 1 |
| 121 | 6 | 1 | 1 |

The required propagation threshold is two, and full collapse would
require all 137 vertices to lie in one equal-polynomial class. Neither
occurs. Each graph has six loops and 408 distinct nonloop edges:
each involution has 68 nonloop pairs, and a pair determines its sum
d_r, so different directions do not share an edge. All enumerated
checks pass, including exhaustion of these two rules. These checks
do not exhaust the original polynomial constraints or other consequences
of them. In particular they do not prove the ansatz feasible.

The generator check gives exact order 1024, and H has 512 antipodal
pairs. After reserving the anchor pair {1,-1}, 511 pairs remain.
Selecting 408 distinct pairs would leave 206 individual labels, more
than the six needed for loops. After choosing those six, 200 labels
would remain. Of these, 61 can form C; the other 139 fill the 135
unused labels in the a column and the four dummies. Thus an assignment
of the edge roots, coefficients and ranks described here really would
extend to an original permitted sigma and a 61-core. This is a label
capacity and extension check, not the missing root assignment.

The complete final equality classes, subgroup checks, label capacities
and failure list were inspected with the shared JSON inspector. The
initial conservative three-neighbor computation and the sharpened
two-neighbor computation give the same classes. The executable and
saved certificate use the stronger two-neighbor rule. No random rank
sample, nonpermitted-label witness or full-sheet assertion is reported.

Reproduction:

```bash
python3 scripts/finite-support/two_fiber_reflection_closure.py
```

## Saved simultaneous compatibility problem

Choose an orientation w<v on each of the 408 nonloop edges, and
choose x_e in H minus {1,-1}, with all unordered pairs {x_e,-x_e}
distinct. Equation (2) is exactly

\[
 V_w-V_v=-\frac{U_w}{x_e+1}-\frac{U_v}{x_e-1}.
 \tag{3}
\]

All denominators are nonzero. Six coordinates U_(d_r/2) must be zero.
The graph is connected: compositions of two distinct reflections
w -> d_r-w act as a nonzero translation of F_137, which has order
137 and is transitive. A spanning tree therefore has 136 edges.
For fixed edge labels, (3) along that tree determines all V values
from the U values and one freely chosen V value. Each remaining edge
requires the signed sum of the right side of (3) around its fundamental
cycle to be zero. Conversely those 272 cycle equations ensure (3) on
every edge, because the tree already determines the endpoint differences.

Consequently this witness search reduces exactly to 272 homogeneous
linear cycle constraints in the 131 unfixed U coordinates, with the
408 distinct antipodal label pairs still to be chosen. A nonzero kernel
is necessary but does not by itself verify affine dimension two.
After reconstructing V, at least one determinant

\[
 (U_j-U_i)(V_k-V_i)-(U_k-U_i)(V_j-V_i)
 \tag{4}
\]

must be nonzero. These are differences of points, so this tests affine
dimension, not merely the linear span of their coordinates. Adding a
common constant to all V changes neither (3) nor (4). If the cycle
matrix has full column rank, U=0 and connectivity makes V constant,
so that particular label choice collapses. No cycle-matrix rank is
computed or asserted here. Searching arbitrary label permutations
and reporting generic full rank would not settle this problem.

If (3), the six zero coordinates and (4) are satisfied, assign x_e and
-x_e to the two endpoints of the matching in its original r column.
At a loop use any of the six remaining distinct labels: its U is zero
and R_w is even, so its equality holds at every label. Formula (1)
then verifies every one of the 822 original matchings and both fiber
constancies. Reflection and index negation are invertible, so both
coefficient images have the same affine dimension two. This explains
precisely what a future witness certificate must contain; no such
coefficient assignment or set of edge roots has been found.

## Outcome, continuation and Mathlib

EXPLORATION. Required: a permitted exact witness or a uniform
impossibility proof for the approved target. Achieved: a new reflected
construction mechanism and a complete check showing that its forced
even-polynomial closure does not settle it. No canonical lemma, source
import, improvement to 955–957 or progress beyond checked sources is
claimed. PROOF.md and DAG.md remain unchanged. Mathlib coverage was
not checked; no absence claim is made.

Stop the forced-even closure as a sufficient argument; further identical
closure runs have no purpose. The refined continuation is one bounded
attempt to assign actual subgroup roots and coefficients in (3)–(4),
starting with a=64, h=1, K=E and the two anchors 1,-1. The unchanged
prior EXPLORE assessment already covers this existential special case;
it introduces no outside theorem, new target or extra hypothesis on a
claimed universal result. An exact witness would stop only the reduced
two-fiber obstruction. Failure of a bounded search is not impossibility;
a proof excluding this ansatz would still not exclude arbitrary two-fiber
assignments. This is the second consecutive mathematical EXPLORATION
turn, so a third without advance or informative negative requires a
mechanism reassessment. The lone-fiber, full-sheet, retention, compatible
law and RS-transfer gaps and all earlier stop evidence remain open.
