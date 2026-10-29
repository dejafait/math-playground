# Span-two pencil consequence — step 544 working record

Approved target: Determine whether L137's common dual line rules out coefficient-difference span exactly two on the full pinned L030 affine sheet, including the exceptional evaluation direction and a common primal point at infinity.

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-28-span-two-collinearity-consequence.md`.
The main gap is arbitrary-center 67/68 safety. The intended intermediate
result excludes only dimension two for the full-sheet coefficient family;
span three, retention, compatible laws and RS transfer remain independent.

Initial reasoning saved before final write-up: under dimension two,
L135 leaves six or seven complete direction classes of pairwise distinct
genuine affine evaluation lines. L137 puts their dual points on one
K-line. Imported arbitrary-field projective duality therefore supplies
one K-rational primal pencil point Q. For every auxiliary P, any two
retained directions supply distinct affine lines containing g_P. If Q
is infinite, their projective closures contain both Q and the finite g_P,
contradicting distinctness. If Q is finite, uniqueness of the intersection
forces g_P=Q for every P, including P=0, so V=0 instead of dimension two.

Continuation/abandonment test: check that each chosen direction remains
complete after the allowed omission, all selected lines are distinct,
the pencil is defined over K, and every g_P has the required actual
incidences. Continue only if both affine-chart cases close without
message injectivity or an auxiliary-field embedding. If a premise fails,
preserve the precise missing implication rather than claiming exclusion.

Relevant prior stops checked: ATTEMPTS/109 leaves universal residual rank
unproved; ATTEMPTS/110's span-three intersections are lines rather than
unique points; ATTEMPTS/111–112 leave reflected two-fiber assignments
unfinished. This pencil argument uses the audited span-two geometry and
does not extend, discard or restart those assignments. It does not use
the blocked design-matrix import or an arbitrary direction omission.

Completed: both branches close under the original hypotheses. The full
proof and its precise imported geometry are in
`lemmas/C137a-full-sheet-span-two-exclusion.md`; the reasoning above is
only the saved initial sketch. The corollary is a local specialization
pending separate critical audit, not a full-sheet collapse theorem or
an RS result. Its audit handoff is REVIEW_REQUIRED. No numerical test
or mathematical script is needed for this incidence consequence.
