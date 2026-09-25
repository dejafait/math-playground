# 2026-09-25 — First-order differential families

Read the shared and local rules, full overview, DAG, relevant proofs,
failure record, and existing changes. Preserved unfinished work and
rechecked the [prize statement](https://proximityprize.org/); its
base-field threshold and source qualifications are unchanged. The
[focused draft](../drafts/2026-09-25-first-order-differential-families.md)
saved the classification and counting idea before completing the check.

[L008](../lemmas/L008-first-order-differential-families.md) proves the
first-order polynomial-kernel classification and the precise agreement
bound after deleting fixed zero columns. It gives an explicit sufficient
slack for every such equation, with a linear bound at equality and a
constant bound above it. A common slack for all odd characteristics
gives M<=3n and the sufficient field condition q>=3 epsilon*^(-1)n
for one family. This is ADVANCE; exploration turns reset to
0/3 and STATUS stays IN_PROGRESS. Its sole prior mathematical input is
L007, used for the reduced-family count and smooth-domain facts.

The attained example shows that fixed zeros can destroy the old
zero-slack constant. It also gives the full-code lower bound n-k+1 at
k agreements, adding the necessary comparison epsilon* q>=n-k+1 for
safety there. Neither that lower bound nor the new family's sufficient
field condition determines the sharp boundary. No complete target
candidate appeared, and no cover of a general nonlinear or higher-order
interpolant was obtained.

The reason for the subsequent direction is to test the first nonlinear
extension using a particular Riccati solution. Reciprocal differences
lead to a rational linear equation; identifying the permitted pole
cancellation is needed before claiming a polynomial-family description.
No continuation result for that extension is assumed.

`python3 scripts/first-order-families/verify.py` passed 5,432 kernel,
five affine-fiber, 120 shortened-list, and 11,430 rational-slack checks.
It also found the predicted nine candidates among 81 family members
in a smooth F_81 example. Results are retained under
`scripts/first-order-families/`; these finite checks are not a proof of
the general claim or an enumeration of a full challenge list.

The required documentation checker passed with nine nodes and six edges;
bytecode writes were disabled to keep shared infrastructure read-only.
`git diff --check -- .` also passed. The new DAG edge was checked against
the actual use of L007; structural validation does not verify the proof.
