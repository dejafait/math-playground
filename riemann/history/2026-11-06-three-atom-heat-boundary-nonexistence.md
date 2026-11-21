# 6 November 2026 — fixed three-atom boundary test

STEP_ID: 2026-11-06-three-atom-heat-boundary-nonexistence.
Completed calculation, RESEARCH/REPRODUCTION, outcome NEGATIVE. Reused
the pre-invocation SPECIALIZE assessment for the exact fixed {0,1,4}
law; no further literature work or source approval was performed.

[L843](../lemmas/L843-three-atom-heat-minor-has-no-boundary.md) proves
strict determinant positivity on the entire positive simplex, excluding
the zero boundary required for the proposed flux witness. Its exact
certificate reports seven passed identity checks and no failures;
complete q0–q5, determinant and all row-derivative terms were inspected.
This is a finite specialization, not a new known-result import, a
general cone theorem or an actual-Xi sign advance. Negative-mass points
from initial elimination were rejected. No proper-minor search can
restore the impossible boundary.

Retire this fixed-family discriminator without increasing support or
rank; preserve the [attempt stop](../ATTEMPTS/2026-11-06-three-atom-boundary-flux-no-boundary.md).
Next independently audit L843's nonexistence answer to the exact same
approved target, reusing unchanged coverage. A creative actual-theta
mechanism is not justified by this test: the missing theta-specific
signed estimate remains a blocker, rather than a reason to label a
routine specialization creative. General signs/all-order transfer and
the main RH gap are unchanged. No mathematical EXPLORATION budget was
spent or reset. PROOF unchanged; DAG gains only the L843 empty-input row.

Validation: `python3 ../scripts/docs/check_structure.py --problem riemann`
passed: 930 nodes, 2258 unique edges, acyclic graph, complete file
coverage, valid local links and compact overviews. L843 has no direct
local mathematical inputs; its empty DAG row is appropriate. These
structural checks do not establish the polynomial identities or signs.
