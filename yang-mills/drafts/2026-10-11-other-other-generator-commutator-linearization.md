# Generator-displacement commutator: first-order reduction

Ready assessment: drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
Main gap: interacting ultraviolet control and a nonzero physical continuum
sector. This bounded subtest addresses Delta_V=R_bulk-R_bulk,moved in
L111, one retained part of the transverse-H cubic coefficient. Its
downstream use is a controlled local trace limit, not an interacting bound.

Working reasoning, UNVERIFIED pending the canonical proof: write
A_r=D T_r and C_r as finite shift stencils. The exact commutator kernel
contains e_j(x+h+k-y)[b_(r,t)(x+h)-b_(r,t)(y)]. Taylor-expand only this
scalar difference. After division by a the candidate kernel is
sum_m partial_m u_r(at,ax) sum_(h,k)(x_m+h_m-y_m)
A_r(h) C_r(k) e_j(x+h+k-y). L110/L111's summable quadratic first
moments should justify the remainder by dominated convergence, without
second moments or separate absolute first moments. The actual F_l(s)^T
P F_k(t), min(s,t), both levels and full heat sum remain unchanged.

Essential inputs: L028 for globally smooth compact displacement and its
C^r convergence, L110/L111 for the exact energy kernel and placement,
L111 for the full heat majorant. L113/L114 are possible later local
projection-transfer inputs, not assumptions of this reduction. L118's
zero moved comparison does not set Delta_V to zero. Stops 028--032
remain. No scaled coefficient, equal-level substitution, upper-pin
extension or negligible earlier cubic error is assumed.

Continue if the exact normalized remainder tends to zero and the
derivative kernel admits uniform axial/spatial tail removal at cubic
scale. Abandon this Taylor shortcut if it requires an unavailable
second moment, an absolute first moment, or a small operator projection
commutator. A proved reduction may leave the local pinned-projection
trace limit and all other retained H errors unresolved.


Completed: L119 proves the proposed first-order reduction with an
o(N^3) remainder and a uniform cubic-scaled spatial/axial kernel-tail
bound. The proof needs only the first quadratic energy moment already
available in L110/L111, not a second moment. Outcome ADVANCE, local
standard-method REPRODUCTION; no coefficient limit or value is claimed.

Continuation within the unchanged approved complete other/other target:
test the fixed-(J0,R), fixed-exterior-mode trace V_N^(J0,R) of L119(3),(6).
Use compact derivative support to compare its finite projection entries
with the full-grid projection, then justify spatial/level Riemann sums
before removing kernel and heat tails. Essential inputs L028 L080 L088
L111 L113 L114 L119; L110 supplies the joint moments. Preserve min(s,t)
and the original distinct-level exterior factors until their fixed-offset
limits are justified. L028's physical prefix and L080's exact mode
normalizations must be checked for this placement; no upper pinned
extension or equal-level identity is assumed. Continue if these limits
and a uniform heat-tail bound give a finite signed limit for Delta_V;
abandon any replacement requiring an unproved boundary extension or a
small operator projection commutator. L110's exterior-circulation error,
L113/L115's placement errors and the values of L097/L098/L101/L104/L107
remain unresolved. L091/L095 fix assembly; L084/L079/L080/L082 fix the
comparison and its arithmetic qualifications. No joint compensation,
finer-scale estimate, interacting bound or Yang--Mills candidate follows.
