# Local-density L2 aggregate certificate — universal-threshold stop

The full bound, source qualifications and scale test are in
[L486](../lemmas/L486-local-density-aggregate-kernel-bound.md).
This is the approved L485 replacement in L483's aggregate kernel,
not the older separate-pair or global Blaschke-envelope method.

WHY IT FAILS: the proved uniform normalized upper bound retains
delta^(-1) exp(-delta log T/8). For the admissible cutoff
delta=log log T/log T, delta log T tends to infinity but this
factor is (log T)^(7/8)/log log T, tending to infinity. The
certificate therefore does not establish little-o for every such
cutoff. This is not a lower bound on the actual mass, a sharp
necessity threshold, or a counterexample to the desired claim.
L486 still proves a sufficient shrinking-sector saving at coefficient
8; the separate application audit now verifies that sector bound and the
universal-threshold certificate limitation, without a repair or a new input.

Stop this certificate as a route to the universal threshold unless a
materially new input changes the surviving loss. A weighted correlation
estimate, or another independently testable mechanism, could do so;
simply repeating this band sum cannot. Preserve the earlier density
and Blaschke results with their own hypotheses and stops. No global
ban on count-based methods or the mass target is inferred.
