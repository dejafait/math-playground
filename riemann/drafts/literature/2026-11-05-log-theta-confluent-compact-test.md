# Actual logarithmic theta law: bounded confluent-minor test

TARGET: Test the signed confluent translation minor Q_3(v) of H(v)=e^v K(e^v)/m_0 on e^v in [1/4,2], seeking a rigorous negative point or a complete nonnegative interval cover within 2048 terminal subintervals.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step610's exact/log-dilation/PF3/confluence search and local duplicate comparison in 2026-11-05-log-theta-confluent-order-three.md; no matching actual-H sign theorem was located within that bounded search, and no originality claim is made.
SOURCE_EVIDENCE: Thomas Simon, Total positivity of a Cauchy kernel, arXiv:1305.1173v1 (6 May 2013), https://arxiv.org/pdf/1305.1173v1, Section3 equation(7), printed pp.6–7; full finite-difference passage and negative-determinant case rechecked in step611. Reuse step610 for the inspected theta-coordinate and derivative/grid-failure comparisons; no unread global sufficiency theorem is needed.
COMPARISON: Confluence is a standard necessary condition; the actual H sign on the chosen compact domain is not supplied by the inspected theorems. Finite positive data do not prove global translation positivity, lower oscillation or Xi mixed positivity.
GAP: Justify the source specialization and derivatives through total order four, derive implementation identities and explicit uniform theta tails, then determine the compact sign or report all unresolved intervals.
REASON: One independently falsifiable actual-theta hypothesis may retain or exclude a local input for a later signed mechanism; it differs from the parked automatic variation-sign transfer and comparison-model scans.
SCOPE: Only this compact Q_3 test, necessary confluence specialization, normalization cancellation, derivative/tail bounds and rigorous evaluation are covered; no global PF claim, all-degree result, sign-transfer theorem or further parameter scan is covered. Newly written ready continuation awaits the supervisor's separate approval.

## Definitions and input contracts

Use L019's positive theta series for K, L021's m_0=M_0>0,
and L795's normalization. Read supporting L016 uniform-series
justification only as needed for derivative interchange. No hypothesis
from L791 or L820 and no cross-notebook theorem is used. Reuse L738
and step502's stop as contrasts, not as sign inputs.

The proposed observable is defined by

    T(x,y)=H(x-y),
    Q_3(v)=det[(partial_x^i partial_y^j T)(v,0)]_(i,j=0)^2 / H(v)^3.

This fixes the signed orientation: both sample tuples increase.
Verify every sign when converting mixed partials into ordinary
derivatives. The source specialization requires real smoothness in
a neighborhood of each evaluation point through total order four.
Cite the confluence argument and give its applicability justification;
do not claim an original general theorem or use an uninspected
sufficient global criterion. Expansion and normalization cancellation
must be checked during research, not assumed from this nomination.

The domain is v in [log(1/4),log 2], equivalently u in [1/4,2].
There is no approved claim outside it. Bound the infinite theta tail
for every derivative actually used; L019's undifferentiated bound
is not by itself a derivative certificate. Algebraic/logarithmic
rescaling is permitted only with proved positive sign factors and
an exact relation to Q_3. It may avoid underflow and numerical m_0
integration, but cannot replace the actual kernel.

## Acceptance and stopping test

Use rigorous arithmetic for a final conclusion, with at most 2048
terminal subintervals in an adaptive cover. Heuristic points may guide
refinement, but cannot certify signs between points. Stop early if
a point enclosure has upper endpoint strictly below zero. Preserve
complete derivative/tail enclosures, determinant bounds, subdivision
cover, rounding conventions, failures and unresolved cells in a local
certificate. Print the conclusion, actual/required bounds and artifact
paths; a preview is not verification.

A rigorous negative point excludes TN3 of T by the necessary condition
and parks this positivity hypothesis. A complete cover whose lower
bounds are all >=0 establishes only compact Q_3>=0; record any
strict margin only if proved. If neither occurs within the cap,
report EXPLORATION and unresolved intervals without raising the budget
or presenting sampled signs as a theorem. Finite positive data alone
do not justify extending the scan: a later continuation needs an
independently useful signed bridge or a new discriminating target.

Main gap: actual-Xi all-degree mixed positivity. Even global TN3,
if separately proved, would leave lower oscillation, the unbounded
integral interface and the all-degree passage unpaid. This is a
bounded calculation, not a creative central proof mechanism.
POTENTIALLY_NEW, if used for the future research step, means only that
the recorded search did not locate its sign conclusion. Full matching
Mathlib coverage is unchecked.

## Direct-source repair and approval — step611

Primary source: Thomas Simon, *Total positivity of a Cauchy kernel*,
[arXiv:1305.1173v1](https://arxiv.org/pdf/1305.1173v1),
6 May 2013, Section3, printed pp.6–7, equation(7) and its preceding
finite-difference argument and following negative-limit case. Retrieved
2026-11-05. Both collocation tuples increase; both Vandermonde factors
are positive. The passage uses smooth real functions. The paper's TP
terminology allows nonnegative minors, matching TN in this assessment.
Its Cauchy parameter conclusions are not imported for H.

This source supplies the already assessed necessary confluence method,
not an actual-H sign theorem. Applicability to the local translation
kernel, derivative control, and normalization remain the stated research
checks. The prior comparison and step502 failure remain unchanged.
No new identity, specialization proof or sign calculation was performed.
The sole reported defect was the missing direct URL in this ready
assessment; it is repaired here. DECISION remains EXPLORE for the exact
saved target. This is a STALLED process repair, with zero mathematical
exploration attempts and no claim of renewed exploration budget.
Full matching Mathlib coverage remains unchecked.
