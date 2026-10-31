# Fixed-sector aggregate kernel — nominated mathematical specialization

TARGET: Test an aggregate-kernel L2 bound for L471's sector d_j>=1/16 using the covered density, shell count and fourth moment, against B_{>=1/16}(T)=o(T(log T)^3).
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed fixed-displacement comparison and its bounded exact/standard-terminology/stronger-result searches; no exact restricted pair-mass theorem was established by the inspected sources. No novelty claim.
SOURCE_EVIDENCE: Reused primary coverage in drafts/2026-10-29-fixed-displacement-source-review-notes.md: Chourasiya--Simonic arXiv:2507.15184v1 Corollary 1/(3), Table 1 https://arxiv.org/html/2507.15184v1; Bui--Hall v1 Theorem 3/Section 7 https://arxiv.org/html/2304.05178v1; Bellotti--Wong v2 Theorem 1.1 https://arxiv.org/pdf/2412.15470v2 and L467. L471 definitions/Section 4 and L018 correspondence were previously read; no fresh source audit is claimed.
COMPARISON: Known multiplicity-counted fixed-sigma density, continuous fourth moment and closed-shell count cover the proposed inputs; none states the original restricted B sum. The difference is finite nonnegative kernel aggregation before Cauchy--Schwarz, with fixed displacement, rather than separate-pair summation or a complex disk norm.
GAP: The real-window kernel identity, its aggregate L2 bound, all multiplicity/endpoint/padding factors and the resulting actual-versus-required scale must be proved in the later attempt; no such bound is asserted here.
REASON: Nominate one bounded established-tool specialization for an independent sector after duplicate audit stalls; separate approval of this newly written assessment precedes invocation.
SCOPE: Actual Xi and the exact L471 B(T), P_T, J_j(T), one-copy F_j and full m_j, restricted to 1/16<=d_j<1/2; T tending to infinity. No RH, simplicity, separation, external half-plane premise, shrinking cutoff, discrete moment or selected-amplitude assumption.

The main unresolved gap is actual-Xi initial signs at unbounded heights
and global mixed positivity. A sector saving could remove one remaining
part of L471's sufficient mass majorant. It would leave d_j<1/16,
the full N(T) saving, individual-height exclusion and higher signs open.

Use the exact scalar-kernel substitution already in L471 Section 4,
keeping its restriction to the clipped real window. Aggregate these
nonnegative kernels with full m_j before applying the continuous fourth
moment. Test an L2 norm with a total-mass estimate from the density
count and a maximum-overlap estimate from L467. These are proposed
steps, not proved inequalities or a claimed height exponent.

Import the density result by the precise citation in the source notes;
do not reprove Ingham or optimize its constants. L018 supplies the
zero correspondence; verify one selected right-side zero per conjugate
pair, multiplicities, coincident ordinates and equality d_j=1/16.
Use a padded cumulative height such as 3T and check its source onset.
Use L467's closed shells for all overlapping windows, including both
endpoints. A singleton clipped window contributes zero. No lower
spacing, zero simplicity or unproved pointwise zeta estimate is allowed.

Continue only if a proved aggregate estimate gives little-o at the
specified scale. Otherwise record the exact exponent/logarithmic loss
or missing hypothesis and park this implementation. An upper bound
that fails this test is not a lower bound on actual pair mass. Any
useful bound is local specialization of known tools, not a new density
or moment theorem and not RH. Canonical proofs/citations belong in a
lemma file only on the later research turn. Full matching Mathlib
coverage remains unchecked; no cross-notebook mathematical input.

## Recovery disposition, 29 October 2026

Direct primary URLs have been added without changing the nominated
mathematical target or asserting its aggregate estimate. The supervisor
requires a different continuation after repeated recovery failure. This
assessment is retained as source evidence, not selected for execution.
No mathematical failure of aggregation has been established; the stop
is procedural. See ATTEMPTS/2026-10-29-aggregate-route-recovery-stop.md.
