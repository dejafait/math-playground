# First disjoint singular family as a sixteen-count generator

Tested 2026-10-04 under the unchanged SPECIALIZE actual-pencil coverage,
using K={1,12,22,64} for the saved disjoint triple at 0,1,2.

WHY IT FAILS: [L018](../lemmas/L018-first-disjoint-singular-family-exclusion.md)
parameterizes every full-weight specialization over arbitrary extensions,
including the exceptional-rank check. The exact coordinate-resultant
certificate forces any sixteen-count specialization to have fourth
parameter sixteen. That actual pencil has a forbidden common singular
locator root and exactly four bad parameters over the algebraic closure.
This excludes the entire stated singular family, rather than a
prime-field sample, while improving no global bound. Stop this family;
preserve the other three singular supports, all-prime configurations
with other fourth supports, arbitrary triples and the July source stop.
