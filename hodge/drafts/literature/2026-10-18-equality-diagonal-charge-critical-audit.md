# Diagonal charge — critical-audit coverage

TARGET: Critically audit L130's diagonal curvature pullback, full-tensor trace and stable/split conclusion under its unchanged equality-kernel hypotheses.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the targeted discovery and duplicate/failure search in 2026-10-18-equality-diagonal-restriction.md; inspected L130, the calculation assessment, ATTEMPTS/074 and history/395, plus relevant L071 and L052 proof ranges and L025/L044 operator locations. No new discovery search or novelty claim.
SOURCE_EVIDENCE: Reopened Verbitsky math/0107182v10 (24 June 2010), Section 3, Proposition 3.7, Lemma 3.8 and Theorem 3.9, https://arxiv.org/html/math/0107182v10#S3 ; Huybrechts author-hosted Lectures on K3 Surfaces, Chapter 9 Definition 4.7, Remark 4.8 and Theorem 4.9, printed pp. 181–182, https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182 ; Stacks Lemma 42.38.9(2) and its projective-bundle proof, https://stacks.math.columbia.edu/tag/02UA ; Section 42.45 character expansion, https://stacks.math.columbia.edu/tag/02UM . Reused the exact-h surface-source comparison cited in the existing calculation assessment.
COMPARISON: The inspected sources cover the general connection, real-Kähler polystability and Chern-naturality tools; L025/L044/L052/L071 supply the local operators and metric tests. They permit a bounded independent audit of L130, but do not certify its specialized trace, induced metric or final charge by citation alone.
GAP: The later audit must independently verify every local specialization and both surface alternatives; this source review neither checks off the proof nor establishes existence or exclusion of F.
REASON: Separate approval was required for the proposed critical audit; essential supporting coverage is adequate under unchanged hypotheses, so the next task is mathematics rather than further discovery.
SCOPE: Only L130 for identical marked K3 factors with common ordered quaternionic structures, exact real h, and hypothetical locally free rank-two Omega-polystable F with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D; no graphs other than the diagonal, new existence mechanism or transport.

LITERATURE_REASON: The startup gate required a separate comparison for the previously unapproved critical-audit scope; reuse of the ready calculation sources avoids repeating discovery.

## What was actually reviewed

The completed source-review target was: Assess coverage for a critical
audit of L130's diagonal curvature pullback, full-tensor trace and
stable/split conclusion. This file now records the exact proposed
mathematical continuation above. Its readiness is distinct from the
supervisor's next-turn approval and from verification of L130.

[Verbitsky, Section 3](https://arxiv.org/html/math/0107182v10#S3)
requires a stable holomorphic bundle and invariant first two Chern
classes in Theorem 3.9. Proposition 3.7 and Lemma 3.8 give zero
contraction for invariant curvature; the latter is a scalar-form
statement, applied to coefficient forms. The paper refers their proofs
to its cited V1, Lemma 2.1 and Theorem 2.5; those originals were not
newly read. These are imported named results, not proposed reproofs.
The audit must retain L071's stable-product passage before using them.
There is no theorem here that ordinary restriction preserves stability.

[Huybrechts, Chapter 9, pp. 181–182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182)
defines the Chern connection and Hermite–Einstein condition for a
chosen Kähler metric. Theorem 4.9 is stated for compact Kähler
manifolds and gives polystability, allowing reducibility and real
Kähler classes. Its deep proof is referred to the standard literature,
not reproduced. This covers the target's analytic setting without an
integral-polarization replacement. The local metric scaling is still
an obligation of the audit. L052's stable RR and split-lattice proof
ranges were read for scope, with their source assessment reused;
no new surface existence theorem is needed.

[Stacks 02UA(2)](https://stacks.math.columbia.edu/tag/02UA)
concerns locally finite-type maps, locally free bundles and bivariant
Chern operations. Its inspected proof base-changes the projective
bundle and its defining relation. It is not itself a theorem about
integral singular cohomology. The smooth algebraic diagonal admits
refined pullback; standard topological Chern naturality supplies the
integral statement as in the earlier assessment. The audit must keep
that distinction and the torsion-free H^4 step explicit.
[Stacks 02UM](https://stacks.math.columbia.edu/tag/02UM)
supplies the character polynomial, not the full tensor trace identity.

## Bounded audit and decision test

The main gap remains universal primitive Hodge realization; the
intermediate target is reliability of this one necessary-condition
filter. Its downstream use is deciding whether the equality-kernel
route retains the recorded diagonal non-exclusion, or needs a real
correction before further work.

Audit the actual connection and diagonal differential, induced 2g
metric and unchanged slope tests. Check the ordinary full q-dual-basis
trace with both rational blocks, the prescribed negative tensor sign,
and the integral class identification. Check both L052 alternatives
before any stable cohomology conclusion. L130's reported trace -10,
charge 25 and non-exclusion are claims to verify, not newly proved
outputs of this literature turn. The elementary trace computation is
justified as a specialization needed to fix signs and conventions;
the general imported theorems should not be reproved.

Continue through one independent proof audit. Preserve the completed
negative outcome and parked filter unless a substantive error is
found; if found, record its exact location and repair only within
covered hypotheses. Passing a necessary charge test cannot establish
a bundle, an extension from the diagonal, or Hodge algebraicity.
ATTEMPTS/074 remains the recorded nondiscrimination evidence; this
review supplies no new exclusion and reopens no exhausted mechanism.

Essential inputs: L130 to audit; L071 actual compatible connection
and full tensor convention; L025/L044 operators, dimensions and exact
h; L052 stable/split alternatives. F existence, separation, compact
ambient extension, reconstruction, transverse transport and universal
primitive Hodge realization remain unresolved. Expected audit
classification is REPRODUCTION. Mathlib matching coverage is not
checked; no absence claim is made. No lemma or mathematical script
was written, and PROOF.md and DAG.md require no change.
