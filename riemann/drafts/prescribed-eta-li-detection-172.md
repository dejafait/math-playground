# Prescribed-eta detection — working checkpoint, step172

Completed later in this step: the full proof and qualifications are
canonical in [L968](../lemmas/L968-prescribed-eta-li-detection.md).
The partial reasoning below is preserved as the interruption checkpoint;
its outstanding checks were completed there. Independent audit remains
pending. No separate mathematical result is asserted by this draft.

The gate-approved target and unchanged SPECIALIZE assessment are in
`literature/2026-11-10-prescribed-eta-li-detection-review-170.md`.
This is a mathematical specialization, not a new literature review.

Partial reasoning saved before the final proof: L964(7),(9)-(13)
give a pre-margin upper error eta*8*9^n*A using a single finite
A>=sum_j|beta_j|. Its negative-Li hypothesis is used only in the
later margin choice, not in that pre-margin estimate. With L966's
eta_n=1/(64*9^n), the proposed bound is Q_eta(n)-lambda_n<=A/8.
If checked, all Q_eta(n)>=0 imply lambda_n>=-A/8 for every n,
which meets Lagarias Theorem2.4(2)/(2.21) for every epsilon>0.

Still to finish in the canonical proof: explicitly verify the allowed
eta range, both separated absolute sums, reality, the direction of
the inequality, ordinary Li normalization, and the exact every-index
quantifiers. A negative-subsequence formulation must exclude finite
prefixes logically; it must not claim an effective first index.
Do not use a uniform-in-n convergence majorant or interchange n and
the infinite sum. L018/L024/L026 supply actual nodes and multiplicity;
L964 supplies the paired identity and analytic estimates, L966 the
observable. L030 explains relevance only. L967's profile obstruction
and the finite-window mixed-degree stop were read and remain intact.

No all-n theta sign, actual negative Li coefficient, off-line zero,
or proof of RH is asserted. A successful bound closes only the
prescribed-eta detection gap. This checkpoint is unfinished reasoning,
not a second proof or a substitute for the eventual canonical lemma.
