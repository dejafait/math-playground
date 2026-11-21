# Ready continuation: dyadic Stieltjes--Selberg specialization

TARGET: Derive S(T,tau)=sum_{T<gamma<=2T} exp(-i*tau*log(gamma))=o(T log T) uniformly for T<=tau<=2T from the localized Stieltjes identity and Selberg's unconditional second moment, retaining all zero multiplicities and arbitrary real endpoints.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact/stronger-result and duplicate comparison in 2026-11-04-zero-ordinate-exponential-cancellation-scope.md; no original cancellation theorem proposed.
SOURCE_EVIDENCE: https://arxiv.org/html/2505.14228v1 Section 2/(6)--(8), pp.3--5; https://arxiv.org/html/2006.08503v2 Section 1.2/(1.4), p.2 and Section 1.1 conventions, explicitly restating Selberg 1946 Theorems 6--7. Reuse assessed Brent--Platt--Trudgian Lemma 2/count correction, https://maths-people.anu.edu.au/brent/pd/rpb276-MC-preprint.pdf, DOI https://doi.org/10.1090/mcom/3652; L467 supplies closed-shell endpoints. Original Selberg proof independently unchecked; no RH-dependent refinement imported.
COMPARISON: The cited standard moment input improves on the pointwise input at the last line of GSS Section 2. The remaining work is elementary localization, uniform estimation and exact endpoint bookkeeping. Reproving Selberg or the contour theorem is unnecessary.
GAP: The exact uniform dyadic little-o is not established in this assessment. No beta-dependent witness weights, shorter windows, paid margins, signs or RH are covered.
REASON: Step 345 repairs the missing direct source URLs and checks source scope; a separate calculation can test the unchanged nomination with standard inputs, bypassing the RH corollary and the contour proof's unqualified good-height step. No mathematical estimate is established by this repair.
SCOPE: All real T tending to infinity, real T<=tau<=2T, all orders of all nontrivial zeros, including separate zeros sharing an ordinate. No RH, Lindelof, simplicity, typical-height or registered half-plane input. Only the scalar dyadic sum is covered.

The main gap remains actual-Xi positivity/initial signs. A signed-sum
input could later support a paid witness remainder, with weights,
analytic costs and sign margins still unpaid. Essential local input is
L467 for endpoints; L018 is only for later Xi interpretation.
Full citations and read/unread qualifications are in the completed
parent comparison and must not acquire stronger hypotheses.

Localize the cited Stieltjes identity to the dyadic interval before
using the moment bound. Seek O(T sqrt(log log T)+log T), or any uniform
o(T log T) bound. This is a target, not a result derived in step 344.
Keep the smooth main term and all endpoint corrections. Relate averaged,
strict and closed counts explicitly, retaining multiple zeros.

Continue if constants are independent of T,tau over the full band and
all corrections are below T log T. Stop and record the failed estimate
if RH, pointwise small-o for S, a typical height or an uncontrolled
endpoint order is required. This is a specialization of known inputs,
not a claim of new discovery. Full matching Mathlib coverage is unchecked.

## Step 345: direct-link and scope repair

LITERATURE_REASON: Supervisor recovery identified missing direct source
URLs in this ready assessment. Review only the saved target; reuse the
parent's duplicate and failure comparison rather than search again.

Opened both versioned arXiv HTML sources on 2026-11-04. GSS Section 2,
(6)--(8), includes the smooth term, the argument-function integral and
the correction derivative bound. Its strict-count notation does not
settle arbitrary endpoint orders; retain explicit endpoint bookkeeping.
Chirre--Quesada-Herrera Section 1.1 uses multiplicities and half endpoint
weights, defining the argument by averaging at jumps. Section 1.2,
(1.4), expressly attributes the unconditional second moment to Selberg,
*Contributions to the theory of the Riemann zeta-function*, Arch. Math.
Naturvid. 48 (1946), no.5, 89--155, Theorems 6--7. Its RH-dependent
Theorem 1 and stronger conditional remainder are outside this import.
The named standard theorem is imported through that inspected explicit
restatement; the original proof remains unread. No reproof is needed.

The BPT author-offprint refresh timed out in this turn. This does not
erase the previously inspected Lemma 2 and proof recorded in
`2026-10-07-signed-count-oscillation-comparison.md`: its correction
bound is for heights at least 2pi and its count uses half endpoints.
Reuse that assessment, including its hypotheses; do not apply its
monotone nonnegative-test lemmas directly to the complex exponential.
L467's inspected closed-shell result retains coincident ordinates and
all orders; its cited primary input is
https://arxiv.org/pdf/2412.15470v2, Theorem 1.1 and Section 5.

DECISION remains SPECIALIZE for exactly TARGET. Coverage supplies inputs
for localization and endpoint handling, not the requested uniform
estimate. This is a process repair, not progress beyond the sources.
