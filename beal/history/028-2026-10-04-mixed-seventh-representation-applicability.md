# 028 — 2026-10-04: original-solution representation applicability

STEP_ID: beal-2026-10-04-028-mixed-seventh-representation-applicability
STEP_KIND: RESEARCH
STEP_OUTCOME: ADVANCE
STEP_CLASSIFICATION: REPRODUCTION
ACTUAL_TASK_TYPE: proof_audit

Completed the saved SPECIALIZE audit in [L019](../lemmas/L019-mixed-seventh-weight-two-representation-applicability.md). One geometric weight-two plus representation now meets all four hypotheses of L017 for every primitive nonzero signed solution of X^5+Y^3=Z^7. Thus, when reducible, its trace at the chosen prime over 29 is ±2. This reproduces the inspected source interface; it is not an independently new representation theorem or a signature exclusion.

The key audit points were fixing the geometric Tate module before using finite flatness, matching the degree-15 Euler model and degree-four quotient, retaining all four valuation patterns at 7, and proving the conductor upper-bound passage by saturated invariants and wild averaging. The proof does not assume residual irreducibility or apply the irreducible-only level-lowering theorem to the reducible sector. The general geometric and finite-flat results remain cited inputs. [Working notes](../drafts/2026-10-04-mixed-seventh-representation-audit.md) preserve the bounded test.

The representation applicability gap is removed at this cited-theorem level. Original exceptional-algebra applicability, irreducible-sector exhaustion, pure-field/global descent and uniform residual-signature emptiness remain missing. The external candidate stays UNVERIFIED and STATUS stays IN_PROGRESS. The next target is the conditional reducible exceptional-algebra assembly; its new exact scope has a REVIEW_REQUIRED stub, with the existing inspected sources identified for a narrow comparison. The persistent blocked sources are not needed and were not retried. Exploration usage is 0/3.

The previously screened versioned primary theorem statements were reopened for exact applicability, not for a new literature search. SymPy was unavailable; a standard-library exact coefficient calculation instead checked the smoothness identities and inertness at 7 successfully. Existing unfinished lemma, draft and script work was preserved; no mathematical script was changed. The only new DAG edge is L017 as input to L019's concluding trace assertion; L016 and L018 are prospective assembly context, not inputs to this result.

Validation: `python3 ../scripts/docs/check_structure.py --problem beal` and `git diff --check -- .` passed. The checker verifies structure, not correctness of imported theorems or the informal proof.
