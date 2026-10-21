# 026 — 2026-10-04: conditional exceptional-field parameter bridge

STEP_ID: beal-2026-10-04-026-mixed-seventh-parameter-bridge
STEP_KIND: RESEARCH
STEP_OUTCOME: ADVANCE
STEP_CLASSIFICATION: REPRODUCTION
ACTUAL_TASK_TYPE: proof_audit

Completed the saved SPECIALIZE target mathematically in [L018](../lemmas/L018-mixed-seventh-exceptional-parameter-bridge.md). The explicit exceptional-algebra isomorphism forces 29 not to divide XYZ and eta modulo 29 to lie in {10,14,24,28}. The t0 conversion gives L016's four curve parameters. This is a conditional result reproduced from the screened source claim, not a result beyond the checked literature or a new signature exclusion.

The [new exact reproducer](../scripts/mixed-seventh-certificate/check_parameters.py) verifies 27 ordinary cases, every unit in all three branch models (84 cases), and the exceptional polynomial plus two fixed factors. All squarefreeness and factor-type checks agree with the source. Explicit products of a linear factor and two root-free cubics independently certify the exceptional type and all four survivors. The [saved output](../scripts/mixed-seventh-certificate/parameter-results.json) contains every Frobenius gcd degree and factor type.

The local proof accounts for all seven roots at every positive coordinate valuation by simple-root lifting over unramified extensions. It avoids an invalid unchanged-degree factorization argument on the scaled polynomials and reconstructs the local models without using the unread original descent. This removes the conditional four-parameter gap; original algebra applicability, original representation hypotheses, irreducible-packet exhaustion, pure-field/global descent and uniform residual-signature emptiness remain missing. The external fixed-signature candidate stays UNVERIFIED and STATUS stays IN_PROGRESS.

Next, assess the original representation hypotheses of L017 against PVT's exact small-characteristic and weight-two statements. This changed hypothesis requires a separate REVIEW_REQUIRED source comparison, rather than repeating the completed finite tables. The existing original-descent and modular-archive blockers stay parked. Mathematical exploration usage is 0/3 after this relevant advance. Existing unfinished parameter reasoning was preserved and extended, and no other notebook was edited.

Validation: `python3 scripts/mixed-seventh-certificate/check_parameters.py` passed. `python3 ../scripts/docs/check_structure.py --problem beal` passed with 19 nodes and 19 unique edges; `git diff --check -- .` passed. The new DAG node has no previous lemma inputs: its proof uses the explicit hypotheses, named general results and its own finite computations. L016 and L017 are downstream context, not mathematical premises of L018.
