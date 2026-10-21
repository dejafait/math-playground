# 2026-10-05 — Exact basic Delsarte LP limitation and overview repair

Completed the approved finite-instance LP test, reusing the prior SPECIALIZE
assessment. [L021](../lemmas/L021-basic-delsarte-support-lp-optimum.md)
records exactly feasible rational primal and dual witnesses with equal
objectives; independent arithmetic auditing checks all coefficients and
constraints. The optimum reproduces L001's support ratio and exceeds
threshold, so the basic LP cannot improve the 955–957 bracket. This is
NEGATIVE, REPRODUCTION: a new local route decision, not a novel extremal
theorem or evidence of actual unsafety. See
[ATTEMPTS/011](../ATTEMPTS/011-basic-delsarte-support-lp.md).

Condensed PROOF.md to repair the supervisor's reported length failure;
canonical proofs, dependencies and unfinished work are preserved. The
new LP limitation is now part of the argument overview and traps check.

Proposed a materially different relaxation using joint triple-distance
semidefinite constraints. Its exact theorem, constant-weight hypotheses
and tractable certificate scope remain uninspected, so the new
[assessment](../drafts/literature/2026-10-05-triple-distance-sdp-certificate.md)
is REVIEW_REQUIRED and the next turn is literature comparison only. No
SDP theorem, bound or implementation was derived here. Mathematical
exploration usage remains 0/3 after this informative negative result.
