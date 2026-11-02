# 2 November 2026 — polynomial arc-cost obstruction (step 52)

One bounded proof attempt reused the unchanged invocation-start EXPLORE
assessment `drafts/literature/2026-11-02-inverse-parameter-polynomial-separator.md`.
It completed the preserved unfinished argument in
`drafts/2026-11-02-inverse-polynomial-arc-cost-working.md`, after reading
L675/L676 and the relevant complete-product and failure passages.
No external source refresh, cross-notebook input or second mechanism
was introduced.

The canonical result is
[L677](../lemmas/L677-full-degree-polynomial-arc-cost-obstruction.md).
Its uniform lower cost has exponential rate strictly above 1/100 for
the full degree<=n, prescribed-zero, segment-positive class and every
angular preimage. Thus the step is NEGATIVE: it changes the decision
from constructing within that class to parking it pending independent
audit. It does not obstruct all separators or resolve the main Xi gap.
Classification POTENTIALLY_NEW refers only to the family-specific
difference left uncovered by the recorded search; this is completion
of existing working reasoning, with no certified novelty or priority
beyond the inspected sources.

The 15 exact constant checks passed, with their complete evidence and
rate comparison inspected in
`scripts/one-sided-hankel/polynomial-arc-cost-check.json`.
Those checks do not audit the all-preimage estimate, arc-mass proof,
Poisson cancellation or L675. The proof and its input remain separately
unaudited. The stop is recorded in
`ATTEMPTS/2026-11-02-full-degree-polynomial-arc-cost-stop.md`.

The next action is an independent conceptual audit of precisely those
claims. Its new coverage nomination reuses the already inspected
Fourier source and the unchanged original target scope; the supervisor
must approve that new assessment separately before the audit. No
constructive replay within the stopped class is scheduled. Later
construction requires changed hypotheses or a different mechanism
with its own coverage, while the general cone/H/support/Xi gaps remain.

L677 uses L675 for all product, coefficient and norm inputs, as recorded
in the DAG. L666 is inherited through L675; L674/L676 are
comparisons, not premises. PROOF.md changes because the simultaneous
degree/zero/sign/cost target now has a proposed obstruction. To keep
its overview compact, L675's former explicit threshold is left in its
canonical proof: degree<=3n/7 costs more than
(1254/1495)*exp(1503*n/97790). All earlier proofs and evidence are
preserved. No RH candidate is claimed; STATUS stays IN_PROGRESS.
