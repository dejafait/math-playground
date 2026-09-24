# Mellin pole dominance audit — 2026-09-12

The exact contour shift and scale estimates are proved in [Lemma 145](../lemmas/L145-mellin-contour-and-pole-scale-audit.md).

**WHY IT FAILS.** Isolating the zeta pole in the smoothed dual series does not provide the needed center lower bound: its residue has modulus sqrt(π)A² exp(1−τ²/4), exponentially below the O(sqrt(t)) uncertainty after normalization. The remaining contour integral has a proved O(t^(3/2)) upper bound but no lower bound; that upper bound cannot be converted into a typical size or nonvanishing statement. Any successful use of this representation must control cancellation in the integral itself. This rules out the automatic pole-dominance inference, not the possibility of further estimates and not RH.
