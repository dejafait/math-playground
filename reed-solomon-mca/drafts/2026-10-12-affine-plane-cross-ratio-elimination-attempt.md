# Affine-plane cross-ratio elimination attempt

Started 2026-10-12 under the unchanged EXPLORE assessment
`drafts/literature/2026-10-12-affine-plane-equality-realization.md`.
The exact target remains deciding realization of L072 for any H-bijection.
The main local gap is sixteen versus the allowable fifteen bad parameters;
uniform triangle twelve, extraction and challenge qualifications remain open.

Intermediate target: eliminate L077's normalized projective seeds, or
extract a uniform necessary condition from the repeated singleton tuples
that has a concrete closure test. A uniform contradiction would exclude
this exact family through L075/L076. Passing tuples do not establish
moment compatibility. Retain all projective infinity and collision cases.

Inputs: L010, L026, L072 and unaudited L073–L077. Their conditional
rank/fullness chain and L077's full cross-ratio argument were inspected.
ATTEMPTS/020, /027 and /028 preserve the sampling, incidence-only and
forced-zero failures. No new positive-only label sampling is authorized.
The supplied ready assessment is reused; no source refresh is needed.

Continuation test: continue on a uniform exclusion, an exact original
kernel realization, or a new necessary restriction with a concrete
remaining closure test. If a bounded elimination pass yields none,
record that outcome and reassess the mechanism. All arbitrary extension
weights and original charts remain; no passing labeling is assumed.

Completed: L078 eliminates all syndrome directions from the twelve
quadrilateral equations containing V0. After sending V0 to infinity,
M0D0 to zero and M1D0 to one, six equations recover three h/e pairs;
the other six reduce to five affine linear equations on d_1,d_2,d_3.
All five augmented four-by-four minors have the same factor
R=(U-DV)^2+4BCD(1-A)(1-B), with U=A+B-AB-AC and V=A+C-AC-BC.
Necessary vanishing is uniform in every labeling and original chart.
For each admissible A,B,C the polynomial has at most two D roots;
its V=0 branch is nonconstant linear, not discarded.

The full proof and qualifications are in
`lemmas/L078-affine-plane-seed-free-ratio-obstruction.md`.
`scripts/triangle-incidence/affine_plane_ratio_elimination.py` checks
all five exact polynomial identities, with complete zero differences
and coefficients saved to `scripts/triangle-incidence/affine-plane-ratio-minors.json`.
Their complete relevant evidence was inspected using the JSON inspector.
One explicit row-major H-labeling has R=7 and augmented rank four.
This is an obstruction regression, not a labeling campaign or bound
inferred from positive samples. No 95^4 ratio census was run.

Outcome: partial ADVANCE toward the same family target, without a
realization or uniform exclusion. This seed-free restriction has a
concrete closure test: enforce it and the remaining quadrilateral
identities for all H-bijections, retaining every affine-system rank
drop, direction collision and projective infinity case. A passing
ratio tuple is insufficient and still needs the complete original
matrix/kernel and all L010 gates. L073–L078 remain unaudited; no
novelty certification, global count improvement or challenge candidate
is claimed. The unchanged literature assessment remains ready.
