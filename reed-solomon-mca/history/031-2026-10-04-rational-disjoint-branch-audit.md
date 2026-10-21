# 031 — 2026-10-04 — Complete saved-triple exclusion

Completed one proof attempt under the unchanged ready SPECIALIZE
actual-pencil coverage. Existing changes were preserved; no additional
literature was needed for the completed target.

[L022](../lemmas/L022-disjoint-triple-complete-exclusion.md) completes the
saved disjoint-triple exclusion over the full field F_(97^20). The
[rational audit](../scripts/coefficient-feasibility/rational-branch-audit-result.json)
retains all 1817 fourth systems, all 1329 rational-root ranks, 197 rejected
weight gates, and explicit projective basis changes for 1132 full-weight
occurrences. The 1105 actual lines all fail the necessary fourth-power
identity. Kernel descent, extension scalars and a nonsparse-infinity chart
justify the class exclusion; L017–L021 then exhaust the other branches.
Full proof is canonical in L022; the
[draft](../drafts/2026-10-04-rational-disjoint-branch-audit.md) and
[route stop](../ATTEMPTS/015-saved-disjoint-triple-sixteen-count.md)
preserve the decision and its limits.

Outcome: NEGATIVE; STEP_KIND: RESEARCH; STEP_CLASSIFICATION: POTENTIALLY_NEW;
ACTUAL_TASK_TYPE: proof_attempt. Imported algebraic tools do not establish
the full restriction; originality is not certified. The global gap stays
11/q–16/q against fifteen. Thirteen exact representative total counts
remain unclassified because of lower-weight roots; they do not affect
the sixteen-count exclusion. STATUS stays IN_PROGRESS, with no complete
candidate and zero consecutive uninformative mathematical turns.

The saved triple is retired. Another fixed-triple enumeration does not
explain how to cover arbitrary inputs. The next direction is primary
source comparison for the balanced-support disjoint-triple implication,
which tests whether a general disjoint-triple mechanism is relevant.
Even a positive answer leaves the arbitrary moment/support normalization
problem. A new REVIEW_REQUIRED assessment is saved; no matching
calculation or theorem is claimed this turn. Recommended next work:
literature_comparison, standard/high.

Validation: rational_branch_audit.py passed all complete-root, rank,
weight, projective-basis-change, actual-minor, recurrence, fourth-power,
multiplicity and exact specified-field assertions, with the earlier
aggregate counts agreeing. The shared checker passed with 24 nodes and 23 edges;
`git diff --check -- .` passed. The saved certificate is complete, and the
new assessment TARGET exactly matches the sole Next action.
