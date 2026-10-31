# Positive two-branch weighted detector: bounded implementation stop

The complete reduction, hypotheses, source citations and retained
correlations are canonical in
[L500](../lemmas/L500-weighted-two-branch-detector-reduction.md).
It records the first mathematical test of the separately approved
detector target, at delta=log log T/log T, with both branches and all
multiplicities. Its reduction has not received an independent audit.

WHY IT FAILS: positive squaring of the Gamma detector leaves the
zero-selected two-height statistic (6), with Gamma mass comparable to
log(1/delta) and a second zeta-squared factor. The short tail leaves
the selected polynomial statistic (7). Its length and divisor-size
coefficients satisfy a fixed margin in Fazzari Lemma 2.1, but that
continuous deterministic-polynomial theorem does not control its
sampling measure. Neither correlation has the required estimate (4).
Baier's final theorem uses a different polynomial weight. Applying it
here, averaging away the selected count, or deleting the Gamma branch
would insert an unproved premise. The available count-only fallback
(5) has normalized upper bound C(log T)^(15/16), not the required
O((log T)^(-c)). A losing upper bound is not a lower bound on W_delta.

Stop this positive detector implementation. Reopening requires a new
mixed weighted input or a quantitatively specified cancellation
mechanism, with separate source coverage. This does not rule out all
zero detectors, a stronger source, the desired bound or RH. The
count-only, selected-supremum and Blaschke stops retain their scopes.
The proposed weighted Green-identity continuation uses a different
continuous log-modulus statistic; it is REVIEW_REQUIRED, not a proved
replacement or an approved mathematical attempt.
