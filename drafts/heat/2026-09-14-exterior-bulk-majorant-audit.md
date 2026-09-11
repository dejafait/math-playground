# Exterior bulk majorant audit — 2026-09-14

Existing work through L216 is complete and preserved. The remaining
region contains c/N,d/N in [8/5,17/10] for all sufficiently large N:
its products lie in [64/25,289/100], away from 1,2,4, and its
factors stay away from sqrt(2). The positive ratio product there has
a fixed positive lower bound by L195. Hence the sum of positive ratio
products over the remaining ordered pairs is of order N².

Checkpoint before promotion: verify real-N integer counts, all four
moving exclusions, and normalization. The L213 uniform fixed-pair
majorant therefore sums to order Rh, not order Nh. This is a lower
bound on the majorant only, never on actual exact-cell mass.

Proposed precise reduction: define A_cd=N²/(Rh) times the exact
sum of W over a,b,m. Then 0<=A_cd<=C, with all original cells and
coprimality intact. The remaining mass divided by Nh equals
(R/N³) sum A_cd max(r(c/N)r(d/N),0). For R comparable to
N^(3/2), an Nh bound requires this weighted sum to be O(N^(3/2)),
a factor N^(-1/2) below its geometric majorant. Actual suppression
is unproved; do not infer it from this calculation.

Completed: L217 proves the geometric majorant obstruction and exact
weighted-mean threshold. It does not prove suppression of actual mass.
The next scoped arithmetic test is the fixed interior box used above.
