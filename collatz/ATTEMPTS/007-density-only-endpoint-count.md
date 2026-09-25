# Attempt 007 — Use endpoint density to exclude bounded starts

Tested on 2026-09-25. The proposal after L007 was to count endpoints
of K allowed blocks below (27/16)^K(N+5), a cutoff containing every
endpoint arising from a start at most N. A count eventually below one
for each fixed N would exclude infinite itineraries in {(2,1),(3,1)}.

## WHY IT FAILS

[L008](../lemmas/L008-endpoint-count-and-boundary.md) gives an exact
disjoint residue description and a shrinking density contribution at the
proposed cutoff, but the available interval-error bound is 2^(K-1).
That estimate never reaches the required count below one. Its explicit
four-block witness has an endpoint below the cutoff while the density
contribution is less than one, so dropping the boundary term is false.
This stops the inference from density and disjointness alone, not a future
argument controlling the residue offsets. It also does not show that the
actual count fails to vanish, exclude all other arithmetic mechanisms, or
resolve restricted escape or Collatz. The count includes some histories
starting above N, so it is a sufficient overcount rather than an exact
count of bounded starts.
