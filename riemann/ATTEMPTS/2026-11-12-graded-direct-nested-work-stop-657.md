# Direct nested graded quadrature657: execution budget stop

Canonical local bounds and the work proof are in
[C998b](../lemmas/C998b-graded-nested-carleman-work-stop.md). The complete
planning certificate is `scripts/separation-seven/graded-nested-work-657.json`;
the scoped attempt record is
[attempt657](../drafts/2026-11-12-graded-full-norm-attempt-657.md).

WHY IT FAILS: This prescribed direct nested evaluator still accumulates
203210364 real coefficient-times-kernel contributions after common inner
data, shared reciprocals and reflected-output reuse. That exceeds the
declared100000000 contribution budget before finite scalar, outer action,
forcing and projection work. The full residual-norm ledger and execution
therefore stop here. The count is specific to this proposed degree rule
and direct summation; it is not a necessary complexity lower bound or
a complete sufficient norm prescription. All three norms remain unknown.
A differently organized inner evaluator, different degree rule or fast
transform is not excluded. Preserve652 and all prior stops. The nominated
finite-cosine special-function evaluator needs separate source review;
no formula or certification for it is supplied by this failed attempt.
