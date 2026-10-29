# Step 537 — batched parity/projection attempt (working checkpoint)

The unchanged pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-27-batched-incidence-zigzag.md`; its exact TARGET
is the approved target for this RESEARCH/proof_attempt. No literature
refresh or new theorem import is needed. The supplied startup files and
local DAG were used before loading detailed proofs. Existing changes and
unfinished work are preserved.

Main gap: ordinary uniform P versus NP. Intermediate target: one explicit
fixed-length scalar incidence chain between the original wrapped F_rG and
GF_r graphs, with support plus twice-counted intermediate size <=C*S for
a universal C and the original preclosure endpoint size S. Its plausible
use is the unary F_r sector of the missing fourth comparison; general F,
mixed letters, actual reception, full resources and availability remain
independent gaps.

Relevant inputs read: L110 §4 and §21's product recipe; L115 §§1–6,
including substitution and every oriented equation; L119 §§1–5 and its
complete long-cancellation endpoint formulas. L117's cancelling fixture
and L118's pure-x path support obstruction are mandatory tests, not
assumptions of existence. Attempt 053 and the immediately preceding work
and history were checked for duplication and the precise elementary-factor
stop. No cross-notebook theorem is used.

One bounded mechanism is under investigation: coalesce parity incidences
inside a nontrivial acyclic auxiliary and use an ordinary projection of
an output-dead component, with no reverse elementary companion imposed.
The candidate must give literal states, edge occurrences and every scalar
map, then check both boundaries and the right-closed transition equation.
Test L119's r=m long cancelling family, L117's cancelling fixture and
L118's r=N=2^k x-path family. Continue on complete equations and a universal
linear ledger, or on a concrete unfinished map with a discriminating next
test; stop this template on a complete failed equation or forced
superlinear count. Missing maps alone imply no impossibility.

At this checkpoint no new batched chain, numerical bound or mathematical
result is established. Reasoning below is provisional until the completed
decision and canonical evidence are written.

## Concrete mechanism under test

Batch the successive placements of the r layers by putting their complete
cut presentations into one incidence auxiliary: H_i=F_i G F_(r-i),
0<=i<=r, with the original two-factor wrapped endpoints at i=0,r.
Interior presentations use three disjoint factors and four constant
connectors. Identify their fresh sinks, retain all other vertices and
occurrences, and choose H_r's fresh source as the auxiliary's entry.
The inclusion of H_r is a fully specified scalar arrow; each other copy
has a unit-coordinate incidence map preserving transitions and the final
vector, with no claim about its different initial vector.

The proposed compression permits arbitrary parity coalescing of copied
states followed by deletion of output-dead states, but retains each copied
state as zero or one coordinate. This is a partial-function map on the
right-closed representations. No elementary reverse companion, independent
output port, raw constant/letter equation or bounded kernel depth is imposed.
Any complete chain using this compressed auxiliary must pay its graph size;
if that compulsory stage is superlinear, remaining arrows cannot repair
the size bound. This is a test of coordinate coalescing, not arbitrary
scalar changes of basis. No unfinished arrow is treated as an obstruction.

Provisional discriminator: for G the N-edge x path, the G vertex h_j,
j<N, in H_i has right-closed state residual
x^(N-j)*(1+x)^(r-i). These N(r+1) polynomials are nonzero and pairwise
distinct, by their orders at x=0 and x=1. A partial-function intertwiner
preserving the final vector cannot kill or identify two of these states.
Thus even optimistically valid parity folds/deletions leave N(r+1)
vertices, against S=10r+6N+20 for the original endpoints. This would stop
this single-auxiliary compression at r=N=2^k.

This differs from L112's literal cut count: it must survive all valid
coordinate folds and deep output-dead projections. It differs from L116:
there is one final scalar, no identity-channel port contract, and these
polynomials are not claimed linearly independent. General scalar sums can
evade the argument. The cancellation fixtures must also be checked by
explicit projection before finalizing the result.

## Completed decision

The full proof, exact hypotheses and qualifications are canonical in
`lemmas/L120-parity-folding-batched-incidence-obstruction.md`. Outcome
NEGATIVE; classification REPRODUCTION; actual task proof_attempt. This
is a local specialization and new route evidence, not a new general
automata theorem or progress beyond the inspected source-level soundness.

Both cancelling families have the explicit common target consisting only
of wrapped F_r. Keeping s,F_r,t and killing every G coordinate satisfies
all three equations. At r=6 the complete replay gives charge 92<=212 on
L117 and 92<=260 on L119 with m=6. Ordinary projections thus pass the
long-kernel test without an elementary reverse companion.

For the path family, the compulsory partial-function compression leaves
N(r+1) distinct nonzero residuals plus the final residual 1. At r=N=2^k,
its repeated graph charge is quadratic while S=16N+20. U's full occurrence
recipe and every copy incidence are explicit. Only the selected H_r copy
has the required initial boundary; other copy maps are not falsely called
accepting arrows. No complete general chain or missing-map impossibility
is asserted. The retained Q size alone stops this template.

The exact replay `scripts/batched-incidence/check_parity_folding.py`
checks all coordinates of both projections on both cancellation cases,
all nine path-copy incidences at r=N=8, and every coefficient of all 72
distinguished residuals. Full evidence is in
`scripts/batched-incidence/output-537/parity-folding.json`. All 72 values,
both complete long-branch equation products, the other projection checks
and the complete empty failure list were inspected using selected --full
JSON pointers. The symbolic proof, not finite distinctness alone, gives
the unbounded ratio.

Stop simultaneous-placement compression by coordinate identification and
deletion (Attempt 054). A different incidence mechanism must use scalar
row sums or avoid retaining a representative for every placement. A
possible refined template shares dyadic incidence relations between
adjacent x/(1+x) placements with two-coordinate scalar sums, while
avoiding the complete grid and keeping ordinary zero-output projections.
No such auxiliary, maps or size bound are supplied here. Its concrete
equation/count test remains within the unchanged EXPLORE target; the exact
next action and routing are recorded only in PROGRESS.md. Preserve all
prior stops, particularly L118's suffix support and L119's elementary
index obstruction. No new assessment is written or approved this turn.
