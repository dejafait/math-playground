# Fixed endpoint Rayleigh test: inconclusive and closed

9 November 2026, step206. The single gate-approved endpoint calculation
used exactly the saved panel0, R=100, D=diag(1,200,40000), c=(1,-2,1),
and threshold 5691/10^9. Full proof and complete certificate references
are canonical in [L920](../lemmas/L920-fixed-endpoint-rayleigh-margin-test-inconclusive.md).

**WHY IT FAILS.** The sufficient-margin obstruction test needs a head
Rayleigh upper bound <=0.000005691. Exact contraction plus the complete
complex-zero directional tail instead gives the enclosing interval
[-0.000045239559,0.000046415197], straddling that threshold. All finite
checks pass, but the saved coefficient widths do not permit this test
to decide the required comparison. This is neither a certified negative
head quotient nor evidence of feasibility. The test stops without a
refined quadrature, direction change, cutoff change or sweep. The older
step193 signed-reserve, step195 determinant-box and step204 approval-loop
stops are preserved. No RH conclusion follows.

The proposed different target concerns L918's unpaid local origin
condition at a hypothetical actual contact. A joint null-row elimination
could preserve correlations lost in the old absolute row bounds; it has
not been carried out or approved here. Its source assessment is marked
REVIEW_REQUIRED, not ready. This is not an automatic head-search campaign
or a retry of the endpoint contraction.
