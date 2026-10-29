# Attempt 047 — full cancellation-cut materialization is not linear

Step 525 tests the prior EXPLORE cancellation-cut target. The complete
representation, oriented scalar maps, raw/right-closed equations, allowed
counterfamily and ledger are canonical in
[L112](../lemmas/L112-dcomm-full-cut-materialization-obstruction.md).

**WHY IT FAILS.** Materializing a distinct cut for every marked F edge and
G vertex costs at least N(N+2) states on unary paths of lengths N and N+1,
while the independent R_axiom/P endpoint size is only 12N+38. The explicit
four-copy implementation's total map-support and intermediate-g ratios
both grow quadratically in N. Its two cancellation arrows are sound, but
cannot repair those charges, and no R-to-stage chain was supplied. This
stops the full table and any implementation retaining all its distinct
cut indices before quotienting; it does not reject a quotient constructed
without that table, other sparse certificates, or finite feasibility for
the actual job. The uniform counterfamily does not alter the fixed inputs.
The next proposed target isolates direct unary-product simulation, with
its exact compression-theorem comparison marked REVIEW_REQUIRED.
