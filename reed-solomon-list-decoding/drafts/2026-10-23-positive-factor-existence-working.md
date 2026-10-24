# Step 416 — bounded positive-factor attempt

Approved target: Determine whether positive distance-invariant product factors exist for L098's exact distinct-edge demands on all actual permitted triangles, without upper capacities.

Start assessment: `drafts/literature/2026-10-23-positive-triangle-factor-existence.md`
(SPECIALIZE, saved before this invocation). Actual task: proof_attempt.
Reuse its inspected Csiszar–Shields Theorems 3.1–3.2; no new literature
or numerical solve is needed. L108's cone conclusion alone is insufficient.
L110/ATTEMPTS/093 and ATTEMPTS/082 retain their stops.

Main gap: arbitrary-center safety at 67/68 agreements; on this route,
shared capacitated-triangle feasibility at L098's fixed pairs. The
existence-only intermediate target could remove an independent
hypothesis from the product ansatz. Capacities, Boolean lower rows,
full source lift, PSD and RS realization remain independent gaps.

Working construction to verify: let k_i count all permitted third
supports on a distance-i edge and E_i count equilateral completions.
Both are positive and invariant on edge classes. Choose
eta=(1/2) min_(5<=i<=68) d_i/k_i. A baseline eta on every permitted
triangle leaves positive residual r_i=d_i-eta*k_i. Add r_i/E_i on
each equilateral distance-i triangle. This should give full feasible
support, unlike cone membership alone.

Normalize by the forced mass H*(N-2)*(N-1)/6 and normalize the positive
reference product c_i*c_j*c_h separately. Import the finite projection
theorem with one edge-incidence feature per permitted edge. Uniqueness
should make the projection invariant under S_1024; average its real
edge log potentials, not factors, and absorb the scalar normalizer
equally into the three distance factors. Check repetitions and every
actual source multiplicity when translating back.

Continue only if this constructs full support and finite positive
distance factors with every demand exact. Otherwise record the precise
failed hypothesis and park the implication. This is not a capacity
test or a restart of a stopped numerical prescription. No mathematical
script is planned: the evidence sought is a complete finite symbolic
applicability proof, to be saved canonically if successful.

Completion: the support, normalization and log-potential obligations
were discharged in L111, the canonical full proof. This working note
preserves the pre-proof checkpoint; no separate derivation is maintained
here. The result is existence-only and still needs independent critical
review. No mathematical script or capacity test was run.
