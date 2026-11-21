# 10 November 2026 — step176: derivative-aware profile fails on the diagonal

Reused the unchanged step175 EXPLORE assessment and completed exactly
its proof_attempt/creative. Outcome NEGATIVE, RESEARCH,
POTENTIALLY_NEW only in the bounded source-gate sense; no originality
or RH advance is claimed.

[L969](../lemmas/L969-h-derivative-boundary-profile-diagonal-obstruction.md)
preserves the complete n=2,3 face identity after the approved replacement
and proves a negative simultaneous-escape limit. This is new local
decision evidence: retire that fixed pointwise profile. Unlike L967's
old one-coordinate ray, every coordinate escapes; the negative h term
has strictly higher exponential rate than the entire other part.
Positivity and finiteness of the actual normalization suffice. No
numerical normalization bound, omitted intersection or dropped h term
is used. The integrated comparison and all-n signs remain open.

The exact script `scripts/li-theta/h-derivative-profile-check-176.py`
saved its complete certificate beside it. Both leading residuals are
zero; the two complete diagonal polynomials and all check fields were
inspected using the bounded JSON inspector with selected --full values.
It reuses the old polynomial utilities, so this is a self-check, not
an independent audit. The canonical proof supplies convergence and
the meaning of the negative limit. The scoped
[attempt stop](../ATTEMPTS/2026-11-10-h-derivative-profile-diagonal-stop-176.md)
preserves the old stops and does not infer a negative integral.

The overview records the new limitation. The DAG adds only L969's
direct mathematical inputs; L968 is motivation, not a premise of
the obstruction. Existing proofs and unfinished work are preserved.
The working draft is retained as a superseded reasoning checkpoint.

The [next assessment](../drafts/literature/2026-11-10-h-derivative-profile-audit-review-176.md)
is REVIEW_REQUIRED for a separate source-scope approval of an independent
audit, not another profile attempt. One bounded mathematical attempt
produced this informative negative; no scheduler counters or shared
infrastructure were edited. Requested settings were gpt-6-astra/max;
runtime identity and effort were not independently verified.
