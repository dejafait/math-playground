# Stop: bounded smaller-complement core/tail test

The canonical proof, exact conditional anchor and full-record
qualification are in [C426c](../lemmas/C426c-smaller-complement-bounded-test.md).

WHY IT FAILS: The new bound on the entire complement of the retained
tiny core is M0 approximately 1.050631, smaller than M_* but still
positive; its computed Markov bound is 1, so its comparison is M0.
A(1) is certified negative, but the response transport enclosures
between anchors fail to certify a negative core at every other saved
cutoff. The 14-slab calculation and complete consistency check leave
1124 of the original combined 262144 callbacks, below one additional
full derivative slab's 5496 cost. Park this implementation and keep
the global-M_*, joint-subdivision and signed-polynomial stops. This
is not a lower bound on the true tail, a proof that A is positive
inside a core, or evidence that I is nonnegative. Reopening requires
a materially different justified mechanism, not another cap reset.
