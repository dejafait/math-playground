# Attempt 054 — simultaneous-placement coordinate folding

Step 537, 2026-10-28. The complete auxiliary, copy incidences, permitted
compression, proof, projections and resource qualifications are canonical
in [L120](../lemmas/L120-parity-folding-batched-incidence-obstruction.md).
The unchanged ready batched-incidence assessment was reused.

**WHY IT FAILS.** Combining all F_i G F_(r-i) placements into one retained
auxiliary and compressing their states by parity coalescing and deletion
still needs N(r+1)+1 coordinates when G is the N-edge x path. Its selected
right-closed residuals x^(N-j)(1+x)^(r-i) are nonzero and pairwise distinct;
a zero/unit-row map preserving transition and final equations cannot
annihilate or identify them. At r=N=2^k the twice-counted graph charge is
at least 2(N(N+1)+1), against S=16N+20. This rejects even direct generation
of the compressed auxiliary, without charging an uncompressed table.
Unlike a bounded elementary factor, an ordinary projection DOES remove
the long cancelled branch: both cancelling fixtures have explicit chains
with charge 12r+20<=2S. The failed path test therefore adds a different
obstruction. It uses one final scalar, not L116's independent ports, and
pairwise distinctness, not linear independence. Nonfunctional scalar sums,
auxiliaries that avoid retaining all placements, and arbitrary scalar
chains remain outside the stop. Missing later arrows are not its proof.
No receiver, cap, production format or historical recovery route changes.
