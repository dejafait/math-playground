# Fixed derivative error budget — step 394 working record

2026-10-21. RESEARCH / proof_attempt under the pre-existing SPECIALIZE
assessment `drafts/literature/2026-10-21-fixed-complex-derivative-error-budget.md`.
The approved target fixes M=Y=128 and forbids derivative evaluation or
mathematical scripts. Existing unfinished work is preserved.

Main gap: arbitrary-curve rank versus analytic order at least two.
Intermediate target: complete omitted analytic error <=2^-30 and an
explicit finite-arithmetic enclosure contract for this fixed derivative.
Downstream use: a separately approved finite enclosure might certify
nonvanishing, replacing the published-computation provenance for this
known curve. It would not supply uniform production or a BSD solution.

Inputs inspected: L030's arithmetic/modularity proof; L031's independent
a_389=1/Fricke-sign proof and elementary outward-parameter rules;
audited L099's rank lower bound; foundations/02's analytic-rank-zero/one
theorem; the existing primary source record and duplicate/failure checks.
L035's published complex order and L100's p-adic result are excluded.
ATTEMPTS/043 and /045 remain untouched and concern different mechanisms.

Working plan, saved before completing the proof: apply Cremona 2.13.1
only after verifying analytic order >=2 and Fricke eigenvalue -1. For
G_2(x), use log(y)/y<=1 on y>=1 to majorize its full integral by
exp(-x)/x. A coarse outward c interval with lower endpoint 3/10 should
make both the n>128 geometric tail and all 128 kernel tails small.
Keep the unnormalized factor four throughout. Test against 2^-30;
park this schedule without enlargement if the full estimate fails.

Unfinished at this save: exact rational comparisons, finite-parameter
propagation, branch/finite-integration requirements and final width
accounting. No derivative interval, backend or coefficients are produced.

Completion: the canonical proof is
[L101](../lemmas/L101-conductor389-second-derivative-error-budget.md).
The full two-piece analytic error is <2^-43, beating 2^-30 without
changing cutoffs. The finite-error radius is
2^-43+200*delta+4*sum(|a_n|/n)e_n+eta, with actual output conditions
specified there. The successful bound is a known-method specialization;
no mathematical script or derivative evaluation ran. The above early
save is retained as such. Independent critical review, certified finite
outputs/backend and nonvanishing remain unfinished. Select a separate
coverage approval for the critical audit before implementation.
