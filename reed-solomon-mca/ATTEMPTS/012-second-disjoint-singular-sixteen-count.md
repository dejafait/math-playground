# Second disjoint singular family as a sixteen-count generator

Tested 2026-10-04 under the unchanged SPECIALIZE actual-pencil coverage,
using K={8,27,50,75} for the saved disjoint triple at 0,1,2.

WHY IT FAILS: [L019](../lemmas/L019-second-disjoint-singular-family-exclusion.md)
parameterizes every full-weight specialization over arbitrary extensions,
including the rank-two exception at S=2, which cannot retain two different
full supports at one syndrome. The coordinate-resultant gcd certificate
forces any sixteen-count specialization to have fourth parameter ten.
That actual pencil has the forbidden common singular locator root T=87
and exactly four bad parameters over the algebraic closure. Thus the
entire stated family is excluded, with no global upper-bound improvement.
Stop this family; two remaining singular supports, all-prime configurations
on other fourth supports, arbitrary triples and the July source stop are
preserved. This does not refute the main challenge.
