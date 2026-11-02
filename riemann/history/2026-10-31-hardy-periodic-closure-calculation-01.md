# 31 October 2026: unit Hermite closure moment test

STEP_ID: 2026-10-31-hardy-periodic-closure-calculation-01

Completed the approved SPECIALIZE target from the supplied closure
assessment. [L582](../lemmas/L582-unit-hermite-hardy-periodic-moment-closure.md)
records the full interpolation, uniform-phase C2 law and all paired
moment comparisons. Ordinary second errors are O(H^(-2/3)/log H+1/H),
fourth errors are O(H^(-1/3)/log H+(log H)^3/H), and all four tight
odd moments vanish exactly. Both boundary phase intervals, the
reference samples beyond 2H and the normalization change are included.
This is local ADVANCE by standard specialization, not a new arithmetic
theorem or claimed originality. The application proof awaits audit.

The sole direct local mathematical input is L473's reference norm
data; the interpolation and fixed-order pointwise bounds are precisely
cited imports. L581 remains an obstruction to its exact corrected law,
not to this changed marginal. The deterministic support bound here is
only O(H^(1/6)); hard ell^2 support and positive clipped mass remain
unproved. No actual-Xi sign or RH progress is asserted beyond this
limited intermediate input.

Nominate the separate L582 application audit with unchanged source
coverage in `drafts/literature/2026-10-31-l582-closure-audit-scope.md`;
its new assessment requires next-turn approval. No central creative
target is justified by this closure alone: there is still no mechanism
connecting it to bounded positive clipped mass or actual-Xi signs.
Prior exact-law, wave and direct-import stops remain preserved.

For the compact overview's byte limit, preserve its displaced detail
here: L581's full-law defect is (log H)^2/6+O(log H), L576--L579's
finite-K bound is <1/288, and L560/L562 retain the log-concavity stop.
Their full statements remain canonical in the respective lemma files.
