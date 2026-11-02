# Constant-offset cosine bulk: uniform threshold stop

The canonical argument is [L588](../lemmas/L588-offset-periodic-bulk-clipped-threshold-obstruction.md),
with its exact rational certificate in `scripts/offset-periodic/zero_atom_certificate.json`.
The joint residual-cone hypothesis forces a^2<=4194/19649, and the
clipped mean is at most 2097/628768<1/288, with gap 97/707364.
The separate conceptual audit in L588 Section 4 passes: an independent
scaled-series recurrence and a different complete-tail cutoff reproduce
the bound and the strict gap. Retain the family stop with this evidence.

WHY IT FAILS: A nonnegative function in the actual lag-one entry space
controls the removable constant spectral mass more strongly than the
same-height PSD constraints. Combining it with a pointwise phase
inequality rules out the threshold for every 0<b<a and
0<omega<=1/2, including all limiting regimes. Changing the parameters
cannot evade this bound. Stop this family; do not extend this argument
to mixtures of unrelated offset paths or general stationary laws.
Full moment feasibility from L587, positive clipped mass for other
families and actual-Hardy/Xi transfer remain distinct questions.
