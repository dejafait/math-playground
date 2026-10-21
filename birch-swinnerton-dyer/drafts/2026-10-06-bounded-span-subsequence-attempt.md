# Bounded-span subsequence attempt checkpoint

Approved target and coverage: drafts/literature/2026-10-06-bounded-span-subsequence-limits.md.
The attempt uses L024's actual ordered pairs and index bound, with L023's natural
classical coefficient identification and L021's structure, under all
their unchanged arithmetic and granted corank/nonvanishing hypotheses.

Work in progress, before final proof/audit: fix once a splitting
S = D^2 direct sum F, D = Q_p/Z_p. For m > 3h project the actual
ordered pair to D[p^m]^2. The projected span quotient is an image of
S[p^m]/C_m, hence has length at most 3h. Lift its two-column coordinate
matrix to Z_p. Smith normal form implies determinant valuation at most
3h, since any invariant exponent at least m would already contribute
m > 3h to the finite cokernel length. Thus k_0 = 3h+1 detects the
exterior uniformly. This inference and its independence of matrix lifts
must be fully written and checked in the canonical proof.

For fixed k and m-k >= h, multiplication by p^(m-k) kills the F
coordinate. A diagonal infinite-pigeonhole subsequence should stabilize
the reductions of the same actual ordered pairs at every depth, retaining
the nonzero determinant at k_0. Check the global coefficient square
T_m -> A, T_k -> A, with multiplication p^(m-k) on both vertical maps;
the identifications must be natural, not separate abstract isomorphisms.
No fixed auxiliary primes, compatible source pairs, rational membership,
finite Sha, or equality with complex order is assumed or concluded.

Completed in canonical L025, lemmas/L025-bounded-index-actual-pair-subsequence-limits.md.
The proof verifies both deferred tests, attains exterior valuation at most
3h, and needs a later independent audit. The provisional reasoning above
is preserved as the pre-proof interruption checkpoint, not a second proof.

Continue if naturality and uniform detection hold; abandon this passage
if either requires an additional compatibility assumption. Any limit
only supplies an integral Selmer exterior with subsequential ancestry.
