# Recentered Jensen from existing bounds alone — 2026-09-11

The audit produced the conditional reduction in [Lemma 135](../lemmas/L135-recentered-jensen-local-count-audit.md), not the proposed uniform theta local count. No counterexample to that local count is claimed.

WHY IT FAILS: Jensen on a translated disk subtracts the logarithm of the value at its center. The established positive lower bound is at zero, whereas translated cosine integrals oscillate. A common zero strip would ensure a nonzero center above it but supplies no uniform quantitative lower bound in this argument. The missing sufficient estimate is a polynomial bound on the local maximum-to-center ratio, explicitly isolated in the canonical proof. Using the coarse absolute upper bound requires a stronger lower bound and cannot silently replace the relative estimate. Further theta-specific horizontal estimates are needed.
