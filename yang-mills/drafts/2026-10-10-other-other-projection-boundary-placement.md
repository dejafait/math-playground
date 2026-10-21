# Finite projection boundary placement in the moved bulk trace

One completed subtest under the unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The main gap remains interacting ultraviolet control and independent
continuum/infrared requirements. The intermediate test is an O(N^3)
finite-to-infinite gradient-projection replacement error in L113(8).
This could permit a later joint frozen-trace bound; no such bound,
limit or compensation is assumed here.

Essential inputs: L085 L110 L111 L112 L113. Preserve ATTEMPTS/028--032.
The moved displacement occurs before J S_alpha^T, so its compact
support restricts columns of X S_alpha^T, hence output rows of the
projection difference. It does not restrict output rows of X.

Tested mechanism: represent both projections as gradient-sandwiched
scalar heat integrals. Couple the scalar Dirichlet and infinite walks
on interior output vertices; retain every input edge. In dimension
three the full two-gradient heat tail has Hilbert--Schmidt bound
C N^(3/2) v^(-7/4). A cutoff N^2/(A log N) gives a localized
projection difference O((log N)^(3/4)). Combined with L111's summable
W_j and the actual trace order, this gives O(N^(5/2)(log N)^(3/4)),
subcubic. L114 contains the complete boundary-domain, full-spectrum,
strong-to-Hilbert--Schmidt integral and actual trace-placement checks.

Continue if the compact-column identity and localized heat estimate
hold with all boundary inputs and every heat mode. Abandon this
shortcut if it assumes compact moved output, loses a gradient in the
heat tail or needs a false factorwise absolute moment. L110/L111/L113
cubic errors remain retained; no negligible total error is assumed.

Completed: L114 establishes the subcubic boundary error for both actual
probes with both coefficient levels, original filters, all heat modes
and every boundary input retained. No mathematical script or diagnostic
is used. This is local standard-method progress, without a novelty
claim beyond the checked sources; the main target remains unresolved.

Continuation within the same approved complete-group target: test
the remaining common-index exterior product placement through the
joint E_j kernel at O(N^3) cost in R_bulk,sc,Pbulk, keeping its finite
compressions, the compact displacement and both coefficient levels.
Essential inputs: L085 L088 L090 L099 L110 L111 L112 L113 L114;
L091 supplies group assembly. L097 L098 L100 L101 L104 L107 retain
other limits; L084 L079 L080 L082 fix the reference and its arithmetic
qualifications. Continue on a controlled placement; stop if the test
needs commuting a component filter through P_inf, unsupported support
transfer or a factorwise first absolute moment. No full frozen
cancellation, cubic-bounded surviving trace, negligible earlier cubic
error, finite H limit or joint value is assumed. Finer scales, other
jets, matching and all continuum/infrared requirements remain open.
