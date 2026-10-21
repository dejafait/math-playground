# Step 389 working checkpoint — approved all-r defect target

The prior SPECIALIZE assessment is unchanged:
`drafts/literature/2026-10-18-arbitrary-branch-sharp-normalization-defect.md`.
Main gap: universal primitive rational Hodge realization. The selected
local target is the sharp upper bound binom(r+1,3) for L128's completed
normalization quotient. Downstream use: local terms in an as-yet-unproved
global normalization/Euler comparison. F and collisions remain hypothetical.

Attempt in progress: for J_(j-1)=intersection_(i<j) I_i, binary union
exactness gives defect increment length S/(J_(j-1)+I_j). Distinct
quaternionic lines intersect only at zero, so each I_i restricts to the
maximal ideal m_j of the added complex plane. The product of the earlier
ideals lies in their intersection; its image is m_j^(j-1). Thus the
increment is at most binom(j,2), whose sum is binom(r+1,3).

Equality candidate: choose distinct real t_i and planes (v,t_i v) in
H^2 inside H^39. In degree d, the restriction image should be Sym^d(C^2)*
tensored with evaluation of scalar polynomials in t of degree at most d.
Verify spanning by splitting each v-monomial between the two ambient
coordinate pairs. This would give defect (d+1) max(r-d-1,0) in every degree.
Must finish: exact finite-module quotient, complete-tail justification,
normalization of the equality arrangement, and algebraic length descent.
A larger admissible defect would abandon the bound. Historical stops
ATTEMPTS/070--072 are preserved; L128's full proof and separate audit were
read. L122/L126 supply comparisons, not inputs to the proposed bound.
No mathematical scripts or external source refresh are needed.

Completed in canonical L129 in step 389: all listed proof obligations are
resolved there. This checkpoint preserves the unfinished reasoning above
as history; it is not a second canonical proof or a current next action.
