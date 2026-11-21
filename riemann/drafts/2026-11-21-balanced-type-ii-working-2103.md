# Balanced Type II diagnostic2103: working checkpoint

Approved target: review2101's unchanged fixed-state arbitrary-factor
balanced-block test, separately approved in2102. This is one research
calculation; source coverage is reused, not refreshed.

Proposed proof to check before finalizing: for alpha=beta=1 every
ordered product lies between 9X/16 and25X/36, so the hyperbolic cutoff
deletes nothing. For real X>=576 the number of indices is at least
sqrt(X)/24. In the finite Fourier sum retain (mn/X)^(1/4); each
positive amplitude is at least log(36/25)(9/16)^(1/4)/sqrt(X).
For a fixed sufficiently small interval about u=0 all phases have
cosine at least1/2. C034r section5 gives W(0)>0 and continuity,
hence positive band mass. Integrate the full finite square on this
interval to seek c_h X. No actual-Mobius lower or upper follows.

Remaining checks: integer floors at every real X, inclusion of the
fixed interval in 4log X, exact Plancherel constant, positive c_h,
ordered multiplicity, and the contradiction only for epsilon<1/2.
No new arithmetic mechanism has been found. Preserve the direct-import
and localization stops within their original scopes.

Finalized this same attempt in canonical C034x: the listed checks are
resolved there and the diagnostic lower holds for every real X>=576.
This draft preserves the interim reasoning, not an additional proof
or current next-action record. A separate critical audit is pending.
