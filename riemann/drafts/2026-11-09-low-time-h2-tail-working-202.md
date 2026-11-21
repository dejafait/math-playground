# Fixed complete-zero tail specialization, step202

Approved target: the exact TARGET in
`drafts/literature/2026-11-09-low-time-h2-complete-zero-tail-budget.md`
(prior SPECIALIZE assessment, unchanged). Main gap: all-degree actual-Xi
mixed positivity. Intermediate use: a complete H2 remainder budget may
be compared with a separately certified finite-head margin; neither
head reality/census nor that margin is supplied by this step.

Inputs read: L019, L058, L874 definitions and logarithm convention;
L488's source normalization; the parent source comparison and L917's
fixed-budget stop. Preserve step193 and L918's sign gap. No cross-notebook
input, finite-head sweep, moment-box refinement, or new source search.

Working route, not yet a certified conclusion: use the elementary bound
K(u)<=200 exp(9u/2-pi exp(2u)), a positive integral on [0,1/10] for
F(lambda,0)>1/20, and lambda*u^2<=exp(2u)/40. Splitting the remaining
exponential gives log maximum modulus <= log(200)+v log v with
v=r/2+9/4. Apply the reviewed Jensen formula at twice the count radius;
retain all zeros and then divide the count by two for opposite pairs.
Aim for an explicit O(r log r) count for r>=100, integrate the complete
reciprocal powers p=4,8,12, and bound each scaled complex rank-one term
by its Euclidean operator norm. Boundary zeros belong to the head.

Still to check: elementary constants, normalization/product hypotheses,
local logarithm extraction without a global logarithm, uniform tail
summation, conjugation symmetry, matrix scaling and final rational
budget. Continue only if all are paid; otherwise record the precise
unpaid estimate and stop this envelope. Even a finite bound cannot
establish domination without an independently certified head margin.

Completion: the proof and its qualifications are now canonical in
`lemmas/L919-uniform-low-time-complete-complex-zero-h2-tail.md`.
The complete rational constants certificate is
`scripts/heat/complete-zero-tail-202.json`; all 13 checks pass.
The entire scaled remainder is bounded above by 5.691e-6 uniformly.
This resolves the tail-only target, with no head margin, head search,
positivity claim, or independent proof audit. The working outline above
is retained as the pre-completion reasoning record, not a second proof.
