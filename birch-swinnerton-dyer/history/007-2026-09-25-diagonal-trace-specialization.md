# 2026-09-25 — The ordinary dual-family trace misses the diagonal branch

Preserved existing work and inactive branches. Rechecked the official
Clay statement; the rank target and its distinction from the refinement
are unchanged. The [saved test](../drafts/2026-09-25-diagonal-cycle-specialization.md)
records the gap, relevance, and decision criterion.

The [construction audit](../foundations/08-diagonal-cycle-specialization.md)
locates the actual maps. The new mathematical evidence is
[L007](../lemmas/L007-ordinary-dual-family-stabilization-obstruction.md):
ordinary tame-dual continuation selects the crossed inverse root.
Thus that contraction cannot run through the diagonal stabilization
needed by the restricted rank-two certificate. This tests the geometry
behind specialization rather than repeating the previous Selmer bounds.

The proof was checked at both endpoints: unique unit root in weights
at least two, continuity of U_p, and alpha beta = chi(p) at weight one.
It assumes an accumulating sequence of classical tame-twist pairs;
it does not assert that a dense set automatically accumulates, that
crossed families exist, or that every motivic lift must use this route.
The tentative finite-level character argument was not established and
was excluded. No numerical check or Mathlib lookup was needed.

Decision: stop the ordinary dual-family contraction, preserving it in
[the failed attempt](../ATTEMPTS/005-ordinary-dual-trace-specialization.md).
The trace on the isolated Artin fiber survives. This motivates testing
its first-order Galois deformation obstruction in the CM setting;
even a lift would leave a geometric comparison to prove. This is a
different mechanism from retaining classical tame duality throughout
the family, not a claim that the required lift is available.

There is no improved rational-rank bound: L006 still gives r <= 2,
or 1 <= r <= 2 with Theorem B, while the required lower bound is
r >= 2. Kummer membership, analytic nonvanishing input, auxiliary
choices, and the universal higher-rank comparison remain missing.
The new DAG row is empty: L007 uses elementary root arithmetic and
continuity; L006 and the vanishing theorem are contextual uses only.

Completed step BSD-2026-09-25-007-diagonal-trace-specialization is
NEGATIVE, with new evidence changing the geometric route decision.
STATUS remains IN_PROGRESS; no complete candidate exists. Exploration
turns without an advance or informative negative result remain 0 of 3.
