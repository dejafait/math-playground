# Degree-67 cubic/cofactor constant-weight upper estimate

Tested on 2026-10-04 under the saved SPECIALIZE upper-test coverage.

## WHY IT FAILS

The [canonical cap and limitation](../lemmas/L016-cubic-cofactor-sieve-cap-and-limitation.md)
retain the complete residual-factor sum and eliminate its linear phases.
The cubic cycle weight is still 770, giving binomial(835,66). The
resulting uniform cap exceeds 320297 times the actual threshold; rational
square-root refinement still exceeds 294741 times threshold. More
decisively, the complete-cofactor norm identity shows that replacing
every cubic subset sum by that same cycle cap before taking absolute
values has an allowance above 35496 times threshold, even with exact
cofactor magnitudes. This is a limitation of that estimate, not a lower
bound for actual lists or errors. Exact cofactor evaluation and removal
of integer rounding alone cannot rescue it. Preserve the degree-67
dictionary and averaging failure. Correlated cancellation, smaller
nonuniform subset sums or a useful fully-split subtraction need different
estimates; the family and the full-code grid radius remain undecided.
