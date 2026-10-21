# Explicit dual audit — rejection-expectation stop

2026-10-16, step 265. This is a stopped audit harness, not a counterexample
to L073 or an exhaustion of the quotient mechanism.

## WHY IT FAILS

Fresh full replay and the distinct two-coordinate group-law chain pass,
but the late-series fixture hits the added `complete_Newton_prefix_26`
check before the expected `full_reciprocal_series` check. The fixture is
correctly rejected; the expected failure label is stale. The single stage
stops and preserves its false aggregate report without a rerun or cap change.
The full mathematical subcheck, rejection coverage and resource figures
are canonical in [L073](../lemmas/L073-conductor389-explicit-dual-kernel-algebra.md);
evidence is in `scripts/seven-torsion/dual-audit-265/`.
Correcting this expectation in a fresh copy is a specific testable repair
under the unchanged ready target. Preserve the failed audit and the
Newton-prefix check. Passing the whole bounded audit is still required
before declaring completion; ATTEMPTS/035--037 and all arithmetic gaps remain.
