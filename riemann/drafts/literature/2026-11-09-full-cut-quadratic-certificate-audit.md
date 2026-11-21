# Proposed critical audit of the fixed-grid full cut

TARGET: Critically audit L912's positive full-cut certificate, including full-kernel Cauchy remainder, derivative theta tails, weighted moments, exact accumulator scaling and normalization, without changing the grid or degree.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the inspected primary-source comparison in 2026-11-09-hall-full-cut-taylor-enclosure.md, the weighted-Hall comparison in 2026-11-08-variable-lobe-four-demand-cut-test.md and L905's step139 audit. This audit retains exactly the previously covered kernel, four demands, five resources, M=128 grid, degree two and arithmetic contracts; no broader numerical method, parameter sweep or new analytic hypothesis is proposed.
SOURCE_EVIDENCE: Makino-Berz publisher Volume4 PDF, Definitions1-3 pp383-385, exponential remainder cases p385, (2.7) p389, Theorem2 statement/proof pp390-391 and Section6 pp415-416; NIST DLMF1.9(iii), (1.9.30)-(1.9.31); complete source evidence and applicability are retained in the unchanged step165 assessment. L905/step139 supply full-cut identity and audited normalizer; L908 normalization and L910 analytic evenness/strip envelope supply the unchanged kernel interface.
COMPARISON: Standard Taylor/Cauchy enclosure is covered. L912 newly specializes it with explicit derivative tails, a global radius-1/4 bound, signed moments and exact scaled integers. Its certificate passes the selected full cut but has not received separate critical review. Internal aggregate/moment checks are not an independent cell replay or a conceptual audit.
GAP: Audit the exact application and all its effective constants; reproduce all load-bearing numerical evidence with an independent formulation, rather than assuming the original script's output proves its own implementation. No essential theorem-source gap has been identified within the unchanged scope.
REASON: This is a changed analytic certificate for a previously unresolved finite obstruction. A separate critical audit is needed before treating its positive full cut as audited local input; it does not imply RH, infinite allocation or any additional sign. Ready-method coverage is reused rather than rediscovered.
SCOPE: Only the exact TARGET. Check k=4W, full even analytic seam handling, Cauchy disks/global supremum, third-order directional remainder, complete theta derivative tails through order two, pi/endpoint/trig moments, negative-center parity, six coefficient factors, full 4,718,592-cell accumulation and denominator 8*10^160, complete transverse tails and positive A0. Preserve all old certificates. No grid/degree increase, other cut or metric reopening.
COVERED_TARGET: Critically audit L912's positive full-cut certificate, including full-kernel Cauchy remainder, derivative theta tails, weighted moments, exact accumulator scaling and normalization, without changing the grid or degree.

Prepared during step166; separately reviewed in step167 on 2026-11-09.
The exact TARGET is source-ready with DECISION: SPECIALIZE; this approval
does not perform the mathematical audit or change L912's unaudited status.
This preparation does not authorize a second mathematical attempt in the
current invocation. The assessment reuses inspected coverage whose
hypotheses and techniques have not moved; it imports no new theorem.

Primary links are retained in the step165 assessment and L912:
[Makino-Berz publisher PDF](https://www.ijpam.eu/contents/2003-4-4/2/2.pdf)
and [DLMF Cauchy formula](https://dlmf.nist.gov/1.9#E31).
The original calculation is `scripts/theta-marginal/full_cut_taylor_166.py`;
full output is `scripts/theta-marginal/full-cut-taylor-166.json`.
The check output `scripts/theta-marginal/full-cut-taylor-checks-166.json`
contains all internal consistency checks and the independently expressed
q moments. It verifies consistency only; it does not replay every cell
or independently recompute all center jets.

An audit should check the complete relevant arrays, using scripts to
save and summarize certificates rather than printing them. A failure
must be reported and corrected or the positive-cut claim qualified.
Success validates a finite sign under the explicit trusted arithmetic
contracts, not a new general theorem or a complete RH candidate.
Full matching Mathlib coverage remains unchecked. The central gap is
L030-L032/C032a actual-Xi all-degree mixed positivity; no transition
from this finite Hall pass to that gap has been proved.


## Step167 separate scope approval

LITERATURE_REASON: The supervisor requires a separate approval of the newly prepared audit assessment. Reuse step165 coverage; inspect primary hypotheses against the saved certificate's scope, without a new derivation or calculation.

Read L912's complete proof through its numerical evidence, step166's
history, the step165 source assessment and the recorded whole-box stop
`ATTEMPTS/2026-11-08-variable-hall-four-demand-budget-inconclusive.md`.
The old stop concerned interval range overestimation at the maximum mesh;
it does not prohibit this independent review of a different enclosure.
No broader Hall theorem or further parameter campaign is needed here.

Reopened the same publisher Volume 4 (2003), pp379–452 PDF, specifically
Definition 1 (p383), Definition 2 (pp383–384), Theorem 2 and proof
(pp390–391), and Section 6's coefficient-error discussion (p415).
Theorem 2 concerns finite expressions defined throughout represented
ranges. It does not automatically certify an infinite theta series or
signed weighted integration. Section 6 requires coefficient error to be
included alongside derivative remainders. Thus its application remains
conditional on independently checking L912's full-series tails and all
coefficient enclosures. No replacement theorem or general reproof is needed.

Reopened DLMF 1.9(iii), equations (1.9.30)–(1.9.31) and their surrounding
hypotheses: continuity on the contour and interior, interior analyticity,
interior evaluation point and positive orientation. The audit must check
these for the full even kernel, not a reflected truncated head. This is
an applicability checklist, not a verification of L910 or the numerical
supremum in L912. Previously inspected integration and exponential cases
remain covered by step165; no new external source is essential.

The audit boundary is unchanged: verify the stated global Cauchy bound,
third directional remainder, full derivative tails, parity at zero,
six weighted coefficients, every center and moment interval, complete
cell accumulation and denominator, transverse tails and positive A0.
Independent recomputation must cover the load-bearing arrays and cells;
aggregate self-consistency is insufficient. Preserve the fixed grid and
degree, original certificates and trusted L037 contracts. If the analytic
chain or replay fails, record and qualify the concrete failure; a positive
lower endpoint after these checks validates this finite cut only.

No exact-cut sign theorem was imported. Mathlib matching coverage remains
unchecked; the numerical certificate is not formal verification. This
review adds no mathematical evidence beyond step166 and is honestly a
STALLED source-gate approval rather than a new advance. The saved target
is now ready for a RESEARCH / REPRODUCTION conceptual audit. No new central
creative target is justified by this approval; auditing the existing
analytic certificate remains the immediate blocker.
