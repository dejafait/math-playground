# Fixed U12 exact compression attempt875 — work in progress

Approved target: Test whether the fixed U12 neutral compression at T=4log(3) satisfies the generalized Schur positivity criterion for V=U6, including positivity of the Z block and its kernel-range condition.

Invocation-start assessment874 is SPECIALIZE. This is one REPRODUCTION
calculation, using C750c's exact spaces, C750a's chi, L744(6)-(8) and
L750 Proof3-4. No sign is yet certified. All previous work is retained.

Plan saved before calculation: for each reflection parity, define the
five exact neutral modes b_k=phi_k-mu_k/mu_p phi_p, pivot p=1 or2,
k=p+2,p+4,...,p+10. Keep the first two as V coordinates and subtract
their exact original-L2 Gram projection from the last three as Z
coordinates. Evaluate five diagonal energies and ten same-parity
sum energies with full outward errors; polarize the latter. Prove
cross-parity entries zero by reflection. Attempt unshifted interval
LDL elimination of each complementary energy block before any inverse
or Schur conclusion. Unresolved pivots are inconclusive, not singular
kernels. A finite passing result still leaves infinite-complement,
non-neutral and actual-Xi/global gaps.

The old UNVALIDATED preview872 suggests complementary eigenvalues
near5e-8 and8e-8 and a full eigenvalue near1e-15; these are diagnostic
only. The approved existing error method may fail to resolve this
scale. No mode/window/shift sweep, negative-zero claim or automatic
precision escalation is part of this attempt.

## Completed bounded attempt

All30 energies completed at the single prescribed grid. Full methods,
coordinates and qualifications are canonical in C750c Proof5; complete
certificates are in scripts/neutral-exact-schur/. Exact accounting passes139
checks, but both second complementary pivots overlap zero. No inverse,
singular kernel or Schur sign is established. Outcome EXPLORATION.
The evaluator is parked; the sole future source nomination is assessment875,
REVIEW_REQUIRED, and no dependent zero-sum mathematics was undertaken.
