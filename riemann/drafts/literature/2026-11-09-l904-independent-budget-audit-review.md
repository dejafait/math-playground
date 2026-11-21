# L904 independent budget audit — source-scope approval

TARGET: Review source coverage for an independent audit of L904's fixed x=16,y=0 negative equal-neighbor budget, retaining its complete theta/spatial tails, half shares and L037 arithmetic contracts.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step174 reused the inspected step133/134 source comparison and duplicate/failure searches; read L904's complete proof and original program for obligation identification, L898's normalization/domination range, L019, L037 and the invoked L312 envelope/Taylor ranges. Step135 and step139 records distinguish the original test from L905's later audit. No new external search or mathematical audit was performed.
SOURCE_EVIDENCE: Reuse drafts/literature/2026-11-08-full-marginal-equal-neighbor-lobe-test.md: Johansson arXiv:1802.07942v1 Section2 steps2-4 pp2-3 and Section2.1 pp3-4; Csordas arXiv:1309.0055v2 Theorems3.5-3.7 pp6-8 and Theorems4.5-4.6 pp11-12. L037 retains the official Python Decimal contract; L312 (3)-(6) and its degree-49 Taylor paragraph supply the local supporting bounds. No new primary theorem is imported.
COMPARISON: The retained sources cover the general inclusion method and associated-kernel context, not J's sign or the new-domain tails. Those local specializations require the independent audit below. L905's audited different-domain Hall budget is comparison only; it does not audit L904. No general quadrature reproof, GHS representation, Hall theorem or positive-transform import is needed.
GAP: Independently verify the full-law Jacobian/normalizer, conserved half shares, reflected real boxes, all theta/spatial and normalization errors, signed weights, inherited arithmetic implementation and complete certificate. Source readiness establishes none of those checks or the reported negative sign.
REASON: Separate literature-only scope approval completed in step174; unchanged retained coverage suffices for the bounded L904 audit. Persistent GHS blockers remain parked. This is process readiness, not a mathematical advance or an originality finding.
SCOPE: Exactly the COVERED_TARGET below at x=16,y=0 and its three fixed intervals; inspect/replay the existing proof, original program and certificate only. No mesh refinement, new quadrature, parameter/lobe sweep, changed allocation, reserve reopening or higher-form theorem.
COVERED_TARGET: Critically audit L904's fixed x=16,y=0 negative equal-neighbor budget, checking its full-law normalization, conserved half shares, complete theta/spatial tails, signed real-box inclusion and original certificate under L037's arithmetic contracts.
LITERATURE_REASON: The saved REVIEW_REQUIRED nomination required separate source-scope approval; retained quadrature/shape coverage was reused because its hypotheses and techniques are unchanged. No additional browsing was needed.

The main gap is L030-L032/C032a's actual-Xi mixed positivity. The
intermediate target is a trustworthy verdict on the existing local
allocation obstruction. Its downstream use is to retain or repair evidence
excluding equal-neighbor half sharing before choosing a different mechanism.

Essential inputs are L904's complete proof and original certificate/program;
L898's full-law normalization; and precisely the L019/L037/L312 ranges
actually used. L905 is a comparison, not a premise for J's sign. There is
no cross-notebook input. Preserve original certificates and unfinished work.
A replay does not by itself verify analytic tails or resource accounting.
Decimal trust contracts remain assumptions.

The literature-only approval below compares these obligations with
retained coverage without doing the mathematical audit. A later audit
should retain L904 only if all
analytic bounds and its strict rational sign survive; otherwise record the
first genuine defect and its effect. Matching Mathlib coverage is unchecked.
This nomination is not a creative attempt. The source-blocked signed
interface supplies no ready new central mechanism.

## Separate scope approval — step174, 9 November 2026

The TARGET records this completed source review; COVERED_TARGET is the
exact later audit it approves. No lemma, mathematical script or original
certificate was changed. Reading formulas and code here identified the
methods requiring coverage; it did not verify their correctness or run
the computation. The original certificate and rational-check artifact
exist, but their values have not been inspected in this source review.

### Primary-source scope and applicability

Fredrik Johansson, *Numerical integration in arbitrary-precision ball
arithmetic*, arXiv:1802.07942v1, 22 February 2018,
[Section 2, steps 2–4 and Section 2.1, pp2–4](https://arxiv.org/pdf/1802.07942v1),
was inspected in step133 and reopened in step134. Its direct inclusion
branch requires an enclosure valid throughout the integration segment.
Its analytic Gaussian branch additionally requires analyticity and an
enclosing-ellipse bound; tolerance/work-limit failure is possible and
the returned enclosure radius remains decisive. L904 selects real-box
inclusion, not that analytic branch. Its product boxes with exactly
integrated signed separable weights are a local specialization requiring
verification. An interval for a signed integral needs pointwise kernel
inclusion and the cosine sign throughout each cell, not merely a sign
for the cell's integrated weight. No smoothness of the reflected finite
head across its seam may be assumed. These are audit obligations, not
an uncovered theorem needed before an audit can start. Johansson supplies
neither infinite-domain tails nor a negative J bound.

George Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-function*, arXiv:1309.0055v2, 21 February 2014,
[Theorems 3.5–3.7 and 4.5–4.6](https://arxiv.org/pdf/1309.0055v2),
has retained coverage including both sign cases in Theorem 3.5's proof.
The associated-kernel admissibility result uses a full admissible kernel
and strict logarithmic concavity; the all-degree Fourier criterion needs
positive definiteness in addition. Neither theorem signs this three-lobe
budget. No normalization-sensitive identity from Theorem 4.6 or shape
theorem is essential to the proposed audit: its full-law normalization
and integrability inputs are precisely L898's first proof subsection and
L019. Tuck's contextual source is likewise unnecessary. Their access
limitations do not block this target, and no GHS/Newman source is used.

L037's [official Decimal reference](https://docs.python.org/3/library/decimal.html)
is retained as a contract, not new evidence of implementation correctness:
directed basic operations, nearest-correctly-rounded exp widened to
adjacent representables, exact integer/rational inputs and rejection of
exceptional arithmetic. The audit must inspect the actual inherited
implementation, precision, pi enclosure and trigonometric reduction.
Interpreter/Decimal correctness remains trusted even after a successful
replay. This review does not turn those assumptions into formal proofs.

### Exact remaining audit obligations

- Check L904 against L898's complete y=0 law, including the Jacobian,
  evenness, absolute Fubini, positive normalizer and complete central-lobe
  half share. Check conservation and the absolute convergence needed for
  its interpretation over all lobes; the computation tests only one.
- Check L312 (3)–(6) on the arguments actually used, then every constant,
  endpoint and exponential comparison in L904 (3)–(6). The earlier
  conditional-order certificate has a different domain and cannot supply
  these new tails. Include both density tails, all three weighted lobe
  errors and both moment-tail errors in the normalizer.
- Inspect `scripts/theta-marginal/equal_neighbor_budget_135.py` and its
  actual imports from `scripts/laguerre/certify_conditional_cosine.py`
  and `scripts/hankel/certify_hankel.py`. Verify every reflected box,
  endpoint, kernel cap, signed cosine weight and finite sum, plus the
  Machin/Taylor routines actually called. L036's higher-order quadrature
  is not used and need not be imported or reproved.
- Inspect the complete load-bearing evidence in
  `scripts/theta-marginal/equal-neighbor-budget-135-m32.json`: every
  kernel cache entry and cosine weight, all `/bounds` and `/result`,
  parameters and arithmetic settings. Compare the retained rational-check
  artifact and independently replay/check the fixed computation if
  needed. A selected preview, self-check or repeated summary is not an
  audit. Preserve original evidence and write any audit output separately.

The threshold remains J>=0; the claim to audit is the existing strict
rational enclosure -32/1000<J<-2/1000 under the stated contracts.
Continue with this bounded audit only. Retain the claim only if its
analytic, accounting and arithmetic obligations all survive; otherwise
document the first genuine defect and its effect on the conclusion.
Do not refine a grid or change allocations to rescue it in this audit.
Even a successful verdict leaves other allocations, complete-transform
signs, nonzero heights and all-degree mixed positivity unresolved.

Step135's history and the fixed-share ATTEMPTS record preserve the old
failure. Step139's audit validates L905's different variable-share cuts,
not this budget. The step133/134 source/duplicate comparisons therefore
remain applicable without a new discovery search or novelty claim.
All essential inputs are local: L904 is the audit object; L019, L037,
L312 and L898 supply the invoked interfaces. No cross-notebook theorem
is proposed. Full and supporting Mathlib coverage remain unchecked.

The next work is proof_audit/conceptual_audit: the delicate point is
combining signed integration, complete-tail errors and conserved resource
accounting under an actual infinite theta law. This is reproduction and
validation of existing work. No justified creative central mechanism is
ready while the independent signed interface and higher-degree bridge
remain missing; the source-blocked route stays parked.
