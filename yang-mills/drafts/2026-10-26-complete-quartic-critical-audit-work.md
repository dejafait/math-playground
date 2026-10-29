# Complete quartic critical audit — working record

STEP_ID: YM-20261026-502-complete-quartic-critical-audit

The unchanged pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-26-complete-quartic-critical-audit.md`.
Actual task: proof_audit; one RESEARCH / REPRODUCTION attempt.
Supplied overview and DAG were used before detailed proofs; existing
notebook changes, L283–L285 and ATTEMPTS/047–049 are preserved.

Main gap: the interacting continuum construction with a nonzero sector
and finite positive mass. Intermediate target: independently audit the
complete quartic N^2 limit, including its full uniform remainder.
Downstream use: determine the compensation still required from the cubic
family; no cubic cancellation is assumed. Continue only if all five
approved analytic and normalization obligations pass. Otherwise identify
the failed equation and withhold the dependent assembly.

Essential inputs: L003 L279 L280 L281 L282 L283 L284 L285, with L002's
exact product bump through L282. Retain SU(2), even N, a=8/N, relative
domains, all normal links, boundary-fixed gauge group, all colors and
both source orders. Higher Wilson jets are evaluated on L280's own
slice. The separate L281/L282 audits may be reused with these hypotheses.
Known source coverage is reused; no new external theorem is needed.

Checkpoint before the final analytic/algebraic verification: L283's
spectral shell estimate works for each one-form mode family, including
its zero cosine index. The low shell sum uses sum_{r<=M}r<=M^2,
not an invalid continuum integral bound. Both positive error matrices
give entry control, and only the fixed local U contraction converts it
to an operator bound. L285(6) uses C_12^*C_12<=L as a quadratic-form
inequality between vectors e_m(L)e_e, so no commutation is required.
The source-weighted polynomial paths vanish near every face for fixed
degree and fine mesh. The separated covariance contributes a^2 on
each entire opposite time half, which is essential for summing N^4
local errors. Raw-edge phases, source-kernel normalization and final
Wilson constants are still being independently checked; this paragraph
is not an audit acceptance.

Completed audit: all five approved obligations pass under the stated
hypotheses. The full argument and qualifications are canonical in L283
section 5, L284 section 5 and L285 section 6. The separate audit checks
the uniform spectral entries before local contraction, source kernel
grids and time recurrence, both entire time halves, every boundary
path, the complete error sum, all raw-edge Fourier phases and the
internal/external color and source multiplicities. No proof equation
or asymptotic constant needed correction, and no DAG input changed.

The three existing finite checks were rerun. Exact Wilson contractions
have residual 0 against required 0, zero failures. The selected kernel
recurrence has maximum residual 1.0229447497400734e-15 against 2e-11,
zero failures on 5148 rows (1824 normal endpoint rows). Complete selected
coefficient values and certificate summaries were read with inspect_json.
Certificates are the existing files under `scripts/quartic-response/`;
they verify finite algebra/recurrences only. Analytic acceptance rests
on the canonical audit arguments, not these checks.

Outcome ADVANCE / RESEARCH / REPRODUCTION denotes verification of the
existing local quartic asymptotic, with no claim of progress beyond
the checked literature or certified originality. It is not a complete
solution candidate. The cubic response, subleading full-coefficient
control, uniform higher remainder and all continuum/infrared gaps stay
open. The changed cubic-asymptotic target is registered REVIEW_REQUIRED
for a separate literature-only comparison next turn; it is not approved
or researched here. Existing work and historical failures are preserved.
