# Step 543 — dyadic full-relation attempt (working record)

The supplied unchanged EXPLORE assessment
`drafts/literature/2026-10-28-residual-relation-generators.md` covers this
one mathematical attempt. No new literature or cross-notebook input is
required. Existing changes and all earlier stopped lifts are preserved.

Main gap: ordinary uniform P versus NP. The immediate intermediate target
is a full basis of the original dyadic endpoint relation with uniformly
linear expanded support, acyclic shift realization and both boundaries.
Its possible use is the unary fourth comparison, still conditional on
the independent reception, general-operand and resource gaps.

Inputs read: L110 §4 (right closure), L122 hypotheses/§2 (literal endpoints,
all transition rows and S=16N+20), and the whole L124 (finite full basis,
shift, boundaries and graph). Attempts 056/057 and history 542 distinguish
the restricted old stops. The current exact-target source audit is already
recorded in foundations/01-model-and-target.md. The supplied primary-source
assessment is reused; qualitative common-source existence is known, not
a claimed discovery here.

Plan and bounded test: retain all original coordinates; first produce
complete N=8 equations and an actual singleton DAG for a Pascal-block
extension of the N=4 basis. Then determine the expanded support recurrence
of that construction. Continue toward a linear claim only with a justified
uniform recurrence or an informative all-basis bound. A failed rank,
equation, boundary or acyclicity check rejects the proposed construction.
A superlinear recurrence stops only that recursion unless an all-basis
argument is supplied. No compressed XOR circuit counts as expanded support.

Partial reasoning saved before computation: outside the six zero-residual
coordinates and paired final coordinate, write y=1+z. A's residual blocks
are z^(N+1)y^j and z^(j+1), while B's are zy^j and
z^(j+1)(1+z^N), 0<=j<N, in reverse f/h coordinate order.
The Pascal coefficient matrix P_N has row j equal to the coefficients of
y^j. Comparing low and high degrees reduces the core to rows
`(r, (b+r)P_N; b, rP_N)` in the block order (A_f,A_h;B_f,B_h).
This reduction and any recursion will be verified against the literal
graphs, not used as an unchecked replacement of the endpoints.

At this pre-calculation checkpoint no asymptotic conclusion had been
reached. N=4 optimality does not imply uniform optimality.

## Completed attempt

The complete result is canonical in
[L125](../lemmas/L125-dyadic-balanced-residual-basis-support.md).
Balanced monomial products supply a full uniform basis and a
degree-triangular shift. The first tie convention selected q=z rather
than q=y on low rows of odd popcount; its complete finite certificate is
preserved in `scripts/batched-incidence/output-543/residual-dyadic.json`.
Selecting the opposite, equally weighted tie reproduces L124 exactly.
The final certificate and independent audit are in
`scripts/batched-incidence/output-543-matched/`. This correction changes
the finite shift counts, not the expanded support recurrence; neither
variant is asserted to minimize shift support.

All N=8 equations pass. Its full basis has support 78 and dimension 23;
the literal graph has 25 vertices and 47 occurrences with shift support
41 and both boundaries. The audit reconstructs the original endpoints,
right closures and every arrow product. It also enumerates all 65536
vectors of the core: the finite threshold ranks prove minimum core
support 70 and full support 78, with no all-N inference.

The discriminating uniform calculation is negative for this recursion:
expanded support is 8+H_k, H_(k+2)=2H_(k+1)+H_k, H_0=5,H_1=12.
Its ratio to S is unbounded. This is not a failure of equations,
acyclicity, boundaries or finite basis optimality. Attempt 058 preserves
the stop. The route changes to a basis-independent tensor bound on the
rank of low-weight relation vectors; that bound is presently unproved.
No additional literature, cross-notebook import, production/cap change,
supervisor-state edit or commit was used.
