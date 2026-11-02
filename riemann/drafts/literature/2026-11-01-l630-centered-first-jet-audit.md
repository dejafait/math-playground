# L630 centered first-jet audit: reuse of unchanged source scope

TARGET: Audit L630's 2 log N+6 bound for all complex a, checking the scalar compression, exact centered boundary entries, weighted row directions and absolute constants against L623/L624/L627.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed exact-statement, numerical-radius, restricted-shift, rational Bernstein and multiplicative-weight comparison in 2026-11-01-centered-first-jet-numerical-radius.md; this is an audit of the same all-N, all-complex-vector inequality, with no new hypotheses or broader theorem. No fresh search or novelty claim.
SOURCE_EVIDENCE: Direct primary sources: Hedenmalm–Lindqvist–Seip arXiv:math/9512211v1 https://arxiv.org/pdf/math/9512211v1 Section 2.2/(2-7)/Lemma 2.3, printed pp. 7–9; Haagerup–de la Harpe (1992) https://access.archive-ouverte.unige.ch/access/metadata/2e3d55fc-f7d2-42af-95ae-6c06df864dbb/download Theorem 1(1) and Proposition 1 proof, printed p. 372. Reopened both on 2026-11-01. Reuse the preceding assessment's inspected Baranov–Zarouf https://arxiv.org/pdf/1310.1182v1 Theorem 2.3/(2.5), Section 4.3 Step 3/(4.11), and Gorkin–Partington https://eprints.whiterose.ac.uk/id/eprint/146209/1/norms_of_ttos_final.pdf Theorem 3.4 and proof, pp. 8–9; these two were not newly read. Local L623/L624/L627 identities remain audit inputs, not externally verified conclusions.
COMPARISON: L630 uses an elementary weighted quadratic estimate for the actual rational-tensor matrix, with a finite factorial bound and the retained exceptional lowering map; it does not specialize the nilpotent or one-variable restricted-shift theorems. The existing comparison covers this same object and target constant. A critical audit is still required.
GAP: Verify the written proof uniformly for N>=2 and arbitrary complex vectors, including the full-tail scalar identity, centering, all boundary cases, the two weight ratios, N/k<2 and the absolute constant. Do not assume the new result to justify any of these checks.
REASON: L630 establishes a local intermediate estimate within the already approved scope; independent replay must detect a hidden tail truncation, conjugation error, incorrect row orientation or constant loss before the estimate is used further. This newly written ready continuation receives separate supervisor approval next turn.
LITERATURE_REASON: Supervisor recovery identified missing direct primary-source URLs in this audit assessment; repair provenance for the unchanged ready target only, without repeating discovery or deriving mathematics.
SCOPE: Exactly L630's N>=2, G_N, analytic B_N with |Re q_j|<1/4, all r in S_N, all complex coefficients and rational-basis indices n<=N; only the first scalar jet. No higher-jet, full signed-budget or pointwise-sign target is preapproved.

This assessment reuses
[the completed comparison](2026-11-01-centered-first-jet-numerical-radius.md)
and its referenced full-Gram coverage. The original nomination added no primary reading or new mathematical
scope. The separate recovery review below supplies direct URLs and
rechecks the relevant statements without enlarging that scope. The same constant-2 claim was already gate-ready
before that turn. The proposed task is verification of its now explicit
proof, not deriving and approving an uncovered result together.

Read the canonical L630 proof and the exact used ranges: L627
(4)–(6)/(9), L623's full Gram identity (1) and its proof, and L624's
convergence/normalization argument and (5). Check the projection in
the scalar form only; the rational basis vectors themselves have
infinite divisor tails. Check the 0-to-1 raising coefficient, the
other raising cases and the 1-to-0 lowering entry separately. Replay
the finite sum Q(X), both weighted rows and their combination with
the centered diagonal for complex coefficients. Check the constant
6 from a convergent majorant, including the elementary inequalities
used in its integral bound. L629 (3) is needed only if replaying the
reported downstream cost, not to establish the scalar inequality.

Continuation succeeds if these checks verify the same uniform bound
with one absolute constant and no unstated premise. A failed identity,
an uncontrolled output tail or a coefficient-dependent constant must
be recorded and repaired or must qualify the result. A floating matrix
cannot settle any of these universal claims. The older freezing,
prefix, absolute-Cauchy and signed-jet stops remain evidence, but
do not contradict this scalar estimate.

The audit does not promote L623/L624/L627 or L629 to fully audited
status outside the exact identities it checks. Higher degrees, the
total signed budget, the remaining local/source audits and pointwise
Xi transfer remain independent gaps. Full matching Mathlib coverage
remains unchecked and unknown. No cross-notebook input is required.


## Separate source-provenance recovery, 1 November 2026

The supervisor reported that a ready assessment needs a direct source
URL. This review repairs that omission in SOURCE_EVIDENCE; it does
not audit L630 or change TARGET, DECISION or SCOPE.

Reopened [Hedenmalm–Lindqvist–Seip, v1](https://arxiv.org/pdf/math/9512211v1),
Section 2.2, printed pp. 7–9, including the normalized Haar construction,
(2-7), its Plancherel identity and Lemma 2.3 with proof. Square-summable
coefficients yield an L2 character-space isometry. Pointwise tail
convergence is not asserted. This supports the full-Gram framework;
it does not prove L630's centered compression or constant.

Reopened [Haagerup–de la Harpe, published version](https://access.archive-ouverte.unige.ch/access/metadata/2e3d55fc-f7d2-42af-95ae-6c06df864dbb/download),
printed p. 372, Theorem 1(1) and the general numerical-radius identity
in the proof of Proposition 1. The first requires nilpotency; the
second retains all complex angles. Neither supplies the target's
uniform logarithmic estimate. Reuse the preceding assessment's
complete nilpotent-proof and rational/restricted-shift comparisons;
no new specialization or reproof is attempted here.

The preceding assessment and the recorded signed-jet budget stop
were checked for overlap. The source comparison remains adequate
for exactly the saved audit. No essential source blocker was found.
No stronger matching result, novelty claim or new mathematical result
is reported. Mathlib matching coverage remains unchecked and unknown.

Outcome: STALLED / LITERATURE / NOVELTY_UNCHECKED, actual task
source_extraction. This is a provenance repair, not mathematical
progress or an informative negative result. Preserve L630 as unaudited;
next perform the saved audit, with its existing all-N/all-complex-vector
success test and failure qualifications. No lemma, mathematical script,
PROOF.md or DAG.md was changed by this review.
