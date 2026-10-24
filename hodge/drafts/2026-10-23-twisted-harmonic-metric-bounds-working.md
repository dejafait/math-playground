# Twisted harmonic metric bounds — working record

2026-10-23, step 473. One RESEARCH / REPRODUCTION attempt under the
unchanged SPECIALIZE assessment
`drafts/literature/2026-10-23-twisted-harmonic-metric-two-sided-bounds.md`.

Main gap: universal primitive rational Hodge realization. The approved
intermediate target is two-sided control of the given harmonic metric
in L147's actual rank-24 frame, for later analytic extension work.
Kernel and split-locus existence, curvature control, positivity,
cardinality, reconstruction and transport remain independent gaps.

Read L146's complete actual splitting and its audit, L147's endpoint
and frame construction, L112's full comparison and audit, the reused
BGS assessments and ATTEMPTS/060/063/066/067. Existing unfinished files
are preserved. No new source search or mathematical script is needed.

Saved calculation before the canonical write-up: analytify the actual splitting as
O -> P plus J -> O, with P of rank two, J of rank 24, incoming vector
v=xa+yb, and outgoing row u(y,-x) on P, zero on J. The unit u and
all basis coefficients retain their higher terms. The central residual
dimensions are (1,26,1), distinct from ordinary middle dimension 24.
Apply the already inspected natural BGS comparison for this smooth
Hermitian coefficient. A comparison implementing the specified derived
identification, projected to the small spectral complex, is centrally
degreewise invertible because both central differentials are zero.
It therefore pulls back a smooth positive metric H_K on P plus J.

Saved write-up/check, subsequently completed in L148: verify the natural-map spreading and actual
quotient identity. The intended exact formula is
G_b(j,j)=min_t H_K(j+t v,j+t v). Relative to the product reference
frame P perpendicular to J, compact-ball eigenvalue bounds c,C give
c||j||^2 <= G_b(j,j) <= C||j||^2. This does not divide by v and
includes every approach direction. Continue only if the comparison
and both inequalities hold for the actual metric; failure stops this
estimate mechanism without an F-nonexistence inference.

Completed: the specified comparison and quotient identity are written in
`lemmas/L148-twisted-harmonic-metric-uniform-two-sided-bounds.md`; both
constants meet the full-ball threshold. Outcome ADVANCE / REPRODUCTION,
pending separate critical audit. The new continuation assessment is
REVIEW_REQUIRED; no curvature or extension claim is added.
