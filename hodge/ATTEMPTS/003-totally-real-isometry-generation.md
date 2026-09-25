# Attempt 003 — Spanning real multiplication by Hodge isometries

Date: 2026-09-25. Outcome: stopped as a means of producing non-scalar real-multiplication actions, including closed chains through other projective K3 surfaces.

The tested mechanism was Buskin's algebraicity theorem for rational Hodge isometries, followed by rational linear combinations and composition. The relevant threshold is all of the full endomorphism field E, not just some algebraic correspondences. The exact conditional calculation for a quartic with totally real E is proved in [L004](../lemmas/L004-totally-real-isometry-span.md).

**WHY IT FAILS.** When E is totally real, every rational Hodge self-isometry of T(S) is +id or -id. Full H^2 isometries restrict to these, and a closed chain through other K3 surfaces is again a self-isometry. Thus this mechanism has transcendental span of dimension 1, whereas the required dimension is [E:Q]. Together with divisor products its span is exactly the previous divisor-plus-diagonal span and misses [E:Q]-1 dimensions when [E:Q] > 1. This does not obstruct nonisometric algebraic correspondences or assert that any missed class is nonalgebraic; the full-field hypothesis also excludes applying this stop to the CM case. A degree-two rational self-map is a materially different possible source because it need not preserve the pairing.
