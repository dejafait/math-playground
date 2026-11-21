# Finite real-box replacement — bounded attempt in progress

Completed in this invocation: the full proof and qualifications are in
`lemmas/L846-angular-period-excludes-finite-real-box-relative-replacement.md`.
The exact angular periods are 1 on the torus and 0 on every box.
The pre-completion reasoning below is preserved; it is not a second
proof or the current status record. Independent audit remains pending.

STEP_ID: 2026-11-06-finite-box-angular-relative-period

Invocation-start coverage: `drafts/literature/2026-11-06-real-zero-box-relative-cycle-test.md`, EXPLORE, exact COVERED_TARGET matching the checkpoint. One mathematical attempt; no new source review. Main gap: L030–L032/C032a all-degree actual-Xi mixed positivity.

Target: decide whether the r=2,k=1 coefficient torus can be a finite integer combination of L845 separated real-zero boxes in the specified relative pair. A separating period would retire this participation mechanism before growing-order saddle work. No infinite-chain or sign conclusion is sought.

Local reads: L845 hypotheses, exact density (4), real restriction and boundary construction, and existing audit; L775 G/radius and Katkova integral interface; L018. Relevant contour/box source records and the automatic-sign stop contain no completed duplicate period test. L844 is background only: its collar exclusion is not needed in this topology argument.

Candidate: put eta_j=Im(dz_j/z_j) and beta=eta_1 wedge eta_2/(2pi)^2. It is smooth and closed on X=(C minus zero)^2. On each vertical/horizontal G-zero branch one factor vanishes; on the diagonal both factors agree, so the wedge vanishes. The candidate torus period is 1; each negative-real box has zero angular pullback. These must be justified on ordinary relative homology rather than only smooth representatives.

Remaining proof obligations: localize a hypothetical finite relation into one compact product of annuli; include every complex G zero in that annulus; establish the compact pair is semialgebraic with real parameters; use the previously inspected natural comparison on the actual represented classes and stratified Stokes. Check all boundary/intersection strata without a normal-crossing hypothesis. Retain F_2=-R_1^2 G(z_1)G(z_2)(z_1-z_2)^2/[G(R_1)^2 z_1^2 z_2^2] and omega=F_2 dz_1/(i z_1) wedge dz_2/(i z_2), including its relative pairing and orientation/Jacobian. No lemma is accepted by this working note.

Continuation/abandonment test: prove beta is a well-defined relative invariant with values 1 versus 0, or record the precise restriction/comparison failure. A failure does not establish a class relation. A successful obstruction stops finite-box replacement only; coincident values of a single other form, other contours, growing-order participation and all mixed signs remain unresolved.
