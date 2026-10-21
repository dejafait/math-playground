# Full-shell column attempt — step 194, unfinished checkpoint

Approved target: test nullspace compatibility of L056's full distance-five
shell with one distance-six support, retaining L053's fixed pairs and all
represented triples. Gate: literature/2026-10-13-full-shell-nullspace-extension.md
(unchanged SPECIALIZE). Reuse its primary source coverage; no fresh literature
is needed. L056 and ATTEMPTS/038–040 do not decide this column test.

Main gap: arbitrary-center safety at 67/68 agreements. A contradiction here
would exclude only this fixed prescription; a pass would park this necessary
test. Seek exact inconsistency or a complete nonnegative compatible column.
Neither supplies the remaining energy inequality, other moments, labels,
representing measures, RS realization, or a change to 955–957.

Let D be the anchor, G=(D\U) union V with |U|=|V|=6, and
E=(D\X) union Y with |X|=|Y|=5. Candidate compression coordinates are
i=|X intersection U| and j=|Y intersection V|, each 0,...,5.
Then distance(E,G)=11-i-j; i+j>=7 is forbidden, i+j=6 is represented
at E with L056 relation (6-i,i), and i+j<=5 is free nonnegative.
The stabilizer of D,G is the product of symmetric groups on their four
regions; it is transitive on each (i,j) class. Must verify this averaging
preserves all specified entries and the full kernel condition.

Normalize column entries by rho*p_5, writing t_ij. Eliminating anchor 1
from the matrix divided by rho changes its shell column to
p_5*(t-p_6*1), and its shell block to p_5*(D_shell-p_5*J).
The constant Schur mode is strictly positive, so only the nonconstant
zero modes in L056 constrain this column; their constant correction drops
out. A complete invariant eigenbasis can be built from the six-point
intersection quotient of the distance-one Johnson relation on five-sets.
Exact arithmetic and this finite basis identification remain to be done.

Initial checkpoint had no compatibility verdict. Exact construction now
finds 20 zero modes, 21 free coordinates, equation rank 20 and a nonempty
nonnegative parameter interval. The parameter is t_23. At its lower
endpoint t_03=0 and all other required coordinates are nonnegative.
The complete solution and exact elimination transformation are in
`scripts/finite-support/full-shell-nullspace-results.json`; 182 checks pass.
Complete selected solution, fixed entries, zero-mode list and quotient
bases were inspected. The general energy inequality has not been tested.
The completed proof is canonical in L059. Its independent recurrence-based
substitution verifier passes all 342 checks, including every zero-mode
projection after anchor transport. All 36 final projections and both full
failure lists were inspected. Outcome NEGATIVE parks this necessary
kernel-exclusion diagnostic, with critical review still pending.
Preserve all prior artifacts; no energy calculation was undertaken.
