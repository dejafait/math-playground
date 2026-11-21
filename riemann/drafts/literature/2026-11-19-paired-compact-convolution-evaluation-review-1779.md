# Compact signed-convolution evaluation: comparison completed1780

TARGET: Assess certified compact evaluation of C033s's order-128 signed convolution integrals uniformly over sigma in [1,2] at n=1, delta=1/16, with total paired-observable error at most2^-20 and without literal high-dimensional enumeration.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1780 completed the changed-target comparison using exact signed-transform/compact-evaluation searches and local stops1571/1576/1768; queries, inspected cases and unused leads are in drafts/literature/2026-11-19-paired-compact-evaluation-source-notes-1780.md. Reuse comparison1778 for unchanged truncation inputs; no novelty inference.
SOURCE_EVIDENCE: Inspected Mimica2015 Proposition1.4(iv), pp6-7; Cekanavicius-Vellaisamy2018 Section1 after(1); Connes2402.13082v1 Section2/(4)-(9), p4, and Gaussian/prime proof cases; Chirre-Goncalves2103.06237v2 Proposition5, pp3-4; Johansson1802.07942v1 Section2/2.1, pp2-3. Direct links and precise scope are in source-notes1780; signed Laplace applicability is already justified in C033j(9).
COMPARISON: C033j/r already provide scalar transform mechanisms; C033m's E/O evaluator retains C032x's spatial-disk cost stop. Direct compact jump-transform quadrature avoids that representation, but requires new numerical bounds over an enlarged Gaussian-width range. Generic quadrature or transform algebra alone does not deliver the requested error/cost certificate.
GAP: Derive or fail the direct scalar uniform error/cost preflight in assessment1780 before implementation. C033s remains unaudited; compact integrands, enlarged-width bounds, normalization, arithmetic and full cost are unresolved, as is a positive separator at these fixed parameters.
REASON: Primary ingredient coverage supports one bounded SPECIALIZE preflight, not a claimed numerical evaluator. No new mathematics or scripts were produced in literature review1780; its newly written ready continuation requires separate approval.
LITERATURE_REASON: Essential missing coverage concerned the compact evaluator, signed scalar factorization, enlarged Gaussian widths and cost, beyond ready omitted-part assessment1778.
SCOPE: C033s's a=2^-256, b=2^256, orders0 through128, exact Qc_sigma, Mc_sigma, P and m, paired Gaver n=1, delta=1/16, and signed width TV<=2. No positive separator, feasible runtime, global inverse or RH implication is assumed.

Review1780 is recorded in
[source-notes1780](2026-11-19-paired-compact-evaluation-source-notes-1780.md).
It approves ingredient coverage only for
[preflight1780](2026-11-19-paired-scalar-error-cost-preflight-review-1780.md).
No full numerical target is achieved. The10^7-term/512-bit cost test is
prospective and must count nested work and any width partition. Existing
signed transform identities are reused, not presented as new lemmas.

## Original nomination1779, retained as historical scope

The main gap remains actual-Xi all-degree positivity, including signed
height, cancellation and realization. A compact evaluator could turn
the qualified finite range-obstruction construction into a numerical
observable enclosure; it would not pay those independent gaps.

Reuse assessments1773/1778 and their ready primary evidence. First
compare a proposed compact evaluation mechanism with C033m, the coarse
independent-box stop1571 and common-disk enumeration stop1576. Do not
reopen either stopped evaluator under a new name. Direct enumeration
of128-dimensional cubes is not authorized. Seek a genuinely different
representation or certified convolution strategy, not just an assertion
that finite integration terminates. Inspect precise theorem hypotheses
and essential proof cases before approving any application.

Continuation test: an assessed method must expose all compact-integrand,
width-uniform, scalar and arithmetic allowances and an explicit finite
cost preflight. If it only restates analytic effectivity, depends on an
unnamed constant or reproduces the parked enumeration, record that
limitation and choose an independently testable target. No new compact
mathematics has been approved by this nomination.

Essential local inputs are C032s and C033i/j/m/r/s. Preserve the full
actual-divisor, finite-zero, heat/counting, multiplicity/conjugation,
half-variance and both fixed-v1 qualifications stated in C033s. The
2^-44 bound covers omissions only; any compact computation must include
its own normalization accuracy and width TV factor. Full matching
Mathlib coverage for the requested evaluator is unchecked/unknown.
