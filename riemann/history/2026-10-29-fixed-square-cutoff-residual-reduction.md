# Fixed-square cutoff and residual reduction — 29 October 2026

STEP_ID: 2026-10-29-fixed-square-cutoff-residual-reduction

One mathematical attempt used the already approved
[fixed-square assessment](../drafts/literature/2026-10-29-fixed-cutoff-square-defect-test.md).
The earlier direct-source repair, unfinished notebook changes and
aggregate procedural stop were preserved. No new source was
imported, and no inaccessible derivative source was retried.

[L477](../lemmas/L477-fixed-cutoff-square-defect-reduction.md) resolves
the cutoff/phase/curvature transfer and checks the square's factor 4.
Its (3)--(5) give a smaller-scale transfer error and a signed residual
bound, but only a full-scale absolute upper bound. Outcome ADVANCE
is this local mathematical reduction; it is neither a completed
defect test nor an established advance beyond the literature checked.
The classification POTENTIALLY_NEW records the assessment's unmatched
specific reduction, not a claim of originality. Separate audit remains
pending.

The elementary absolute-norm step ends at O(T(log T)^3), which meets
neither the little-o threshold nor the required positive lower bound.
The surrogate is not abandoned. The two-phase residual is retained
exactly; its signed cancellation is not treated as absolute cancellation.
The working checkpoint is preserved in
[drafts](../drafts/2026-10-29-fixed-cutoff-square-defect-working.md).

The selected direction is an unapproved finite-interval multiplicative
Hardy-space norm comparison. Its
[coverage nomination](../drafts/literature/2026-10-29-fixed-square-residual-hardy-l1-coverage.md)
is REVIEW_REQUIRED: finite-height transfer and cancellation between
the components are essential missing hypotheses. The narrow local
search found L318's different generic-phase obstruction and L319's
stationary involution, not coverage for that norm transfer. Their
stops remain intact. No theorem about an infinite-time average is
silently applied to [T,2T].

The mathematical dependency check follows the actual uses of the
phase expansion, local frozen jets and zero-safe gauge identity.
The historical L318/L319 comparisons do not enter the proof. No
mathematical script or numerical sign evidence was needed.

## Preserved overview passage

The following previous first-sign overview is retained as the
PROOF.md paragraph is compacted to include the new reduction.
Its underlying canonical statements and qualifications are unchanged.

> The regulator/response and selected-law results lack global realization or regulator-uniform signs. L469 excludes U'+CU>=0 near a hypothetical multiple real Xi zero for U=wD_1, positive C^1 w and continuous C; simple zeros are locally compatible. L470 uses Valiron's theorem and xi's order-one infinite type to exclude finite homogeneous polynomial-coefficient linear ODEs for Xi, including real-open-interval identities. Both await separate audit; neither refutes RH. L471 gives a zero-safe first-sign mass majorant with cubic displacement weights; ordinary moments lose displacement and give only the full T(log T)^3 scale for N(T). L474 uses finite nearby-zero Blaschke factors and Bettin's microscopic shifted second moment to obtain B_epsilon(T)<=C epsilon^3 T(log T)^3 uniformly for 0<epsilon<=1, including multiplicities and clipped windows; its application awaits separate audit. L476 truncates the signed all-zero kernel to |t-Re z|<=h, h=(log T)^(-1/4), with weighted negative-mass error O(T(log T)^(5/2)), including zero-safe extensions and multiplicities; this specialization awaits separate audit. The retained local negative mass and L474's complementary sector d_j log T>epsilon remain uncontrolled. The full saving, individual-height and higher signs remain open.
