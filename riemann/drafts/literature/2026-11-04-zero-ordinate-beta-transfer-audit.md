# Source coverage for the critical beta-weight transfer audit

TARGET: Audit L757's uniform O(T) beta-weight transfer, checking Simonic (74) at sigma=1/2, exact finite displacement and reflection identities, principal-log derivative and arbitrary endpoint orders.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the parent exact-target and stronger-result searches; read L757 in full, L018, step 350 history and the charged-union/scalar-approval stops. No changed theorem target or new discovery search is needed.
SOURCE_EVIDENCE: Reopened Simonic arXiv:1910.08274v2 Introduction p.1, Section 4.2 p.29, and Section 4.5 p.33, complete (73)--(75), their parameter definitions and final parameter choice; source scope is adequate for the saved audit.
COMPARISON: The parent SPECIALIZE assessment remains adequate; this distinct audit checks the existing application rather than deriving a new density theorem. No stronger imported conclusion settles the branch and finite-sum bookkeeping automatically.
GAP: No essential source coverage is missing for this audit. Its mathematical verdict remains pending, including finite identities, endpoint extension, reflection, branch derivative and uniformity; full source moment proofs/constants remain imported.
REASON: Separate literature-only approval of the previously REVIEW_REQUIRED audit is complete; next turn must perform the saved mathematical audit rather than repeat source approval.
SCOPE: All nontrivial zero orders, repeated ordinates, arbitrary real T tending to infinity and T<=tau<=2T, principal logarithms in the right half-plane; no RH, Lindelof, simplicity, spacing or typical heights.

The research target's ready assessment was saved before step 350.
Reuse its precise source coverage. The essential local input is L018;
L756 is downstream only. L757's full proof was read for this approval; its audit verdict
is deferred to the research turn. Check that fixing the source's T_0 leaves sigma=1/2 admissible
for every larger T and gives constants independent of T. Preserve the
qualification that full source moment proofs and constants remain
independently unaudited.

The bounded audit should check (4)--(6) with gamma=T excluded,
gamma=2T included, beta=1/2, arbitrarily small displacements, equal
ordinates and all orders. Check that rho -> 1-conj(rho) preserves
the chosen slab. Verify the sign and modulus of F', tau/gamma<=2,
tau arg(gamma+i y)<=1, both segment orientations, and the factor 4e.
Finally verify the uniform supremum limit (9). Continue only if the
claimed O(T), hence o(T log T), holds with one common onset; otherwise
repair or record the precise failed hypothesis or estimate. No numerical
experiment, new density theorem, witness construction or sign claim is
part of this audit. Full matching Mathlib coverage is unchecked.

## Separate source-scope review, step 351

Primary source: Aleksander Simonic, *Explicit zero density estimate for
the Riemann zeta-function near the critical line*,
[arXiv:1910.08274v2](https://arxiv.org/pdf/1910.08274v2#page=33),
29 November 2019. Read p.1 count conventions, p.29 Littlewood setup,
and p.33 parameter definitions and both density cases. Equation (74)
includes the critical-line endpoint; its integral extends to 1.
The constants depend on fixed auxiliary parameters, not the running
height. The text permits ordinate endpoints by extension. Littlewood's
zero count uses analytic orders; the future audit must keep these
orders when applying its bound. The headline Theorem 1 range is not
a restriction on the upper integration endpoint in (74). Source
moment arguments and numerical constants are imported, not audited.

No additional source is essential for the elementary application checks:
L018 supplies the local correspondence and reflection. Full matching
Mathlib coverage remains unchecked. The parent assessment explains why
reproof of density is unnecessary and records the alternative complex-node
formula; that alternative is not an input to this audit.

This is readiness approval only. No transfer identity, derivative bound,
endpoint argument or uniform limit was newly proved or certified here.
The next research turn must independently assess every displayed step
of L757. In particular, distinguish the source's auxiliary mollifier
endpoint exclusion from zeta-count endpoints, and check the existing
one-sided limiting justification rather than treating discontinuous
counts as continuous. Keep the original bounded test above.

The charged-union stop concerns o(T) height measure, a different target;
the scalar-approval stop forbids unproductive repetition for its original
scope. Neither invalidates this audit. No novel mechanism or paid sign
is established by approving it. The mathematical argument and DAG are
unchanged. This repeated source confirmation is honestly STALLED as a
research outcome, with a ready concrete mathematical continuation.
