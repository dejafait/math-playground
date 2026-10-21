# Direct first-pair centering defect

Approved scope: reuse drafts/literature/2026-09-26-current-target.md
without changing its combined-response target. One bounded mathematical
test is the original-path replacement specified by checkpoint 093.

Main gap: the full remaining Ward-response logarithm and controlled
matching remain uncomputed. Intermediate target: an O(N²) bound on
the complete heat-summed change in L070(1) when only exterior t_2,t_3
are replaced by opposite-edge averages. This could justify one reduction
toward the actual trace; it does not justify L073's diagnostic as a
coefficient. Continue if the bound retains all endpoints and mode sums;
otherwise record the uncanceled power and stop this replacement bound.

Working observation saved before completion: for positively oriented
opposite edge values A,C in direction mu and B,D in direction nu,
t_1=A+B-C-D, t_2=A+B, t_3=B-C. Their centered replacements are
(A+C+B+D)/2 and (B+D-A-C)/2. Both defects are t_1/2.
Thus the defect has one curvature exterior rather than one path exterior.
Test with L064's complete r,t_1=O(a²), W_1=O(N³), and H=O(N³)
array bounds. L069's axial-prefix circulation vanishes identically, so
the relevant W_1 is already the direct one. Preserve the exact trace
order and prove the determinant signs before applying these bounds.

Checked duplicates/failures: L064's coarse first-pair bound, L069's
axial-prefix result, L070's exact circulation/path trace and frozen
symbol, ATTEMPTS/019–022, and checkpoint 093's saved continuation.
None proves this exterior-only replacement. L066 forbids assuming a
uniform full-vector residual norm; the present test uses its already
available O(N) bound through L064, with an extra exterior curvature.
The existing SPECIALIZE literature comparison is reused; no general
flow or matching theorem is reproved and no originality is claimed.

Essential inputs: L062, L064, L069, L070 (with L018/L026's covariance
and forest conventions inherited there). L073 supplies motivation only.
Unresolved: centered original trace, axial normalization, variable
coefficients, pinned-trace remainder, other endpoint monomials and all
other response jets. Reflected error <=c_box/2, continuum fields,
reflection positivity, infrared control and finite positive mass remain
unproved. No candidate solution exists.

Completed: L074 proves the exact exterior defect and its O(N²) full
heat-sum bound for both probes. Its axial-prefix contribution is zero.
The four determinant signs were checked against L070's ordered trace;
L062/L064 supply all end-row and all-mode bounds. No mathematical
script is needed. Outcome ADVANCE / RESEARCH / REPRODUCTION: a local
replacement estimate by existing methods, not a new source-level
result, complete pair bound or coefficient. In particular this error
is not proved o(N²) and cannot be dropped at a² scale.

Continuation under the unchanged assessment: in the direct first pair,
apply the same exact row shear (c,b,q) -> (c,b-c/2,q-c/2) to the
two rough right rows, retaining the centered exterior row. Regroup the
remaining t_1 path/path monomials with the correction terms before
any norm, and test an O(N²) bound in the actual residual/covariance
order. This is an algebraic preparation for the original trace, not
a new finite diagnostic. Essential inputs: L062, L064, L069, L070,
L074; retain L066's full-vector obstruction. Continue only if an exact
new incidence or cancellation improves the complete bound; if the
generic O(N³) loss remains, record the specific surviving contraction
and park that closure. All unresolved assumptions above remain; even
a successful bound will not give a scaled coefficient or logarithm.
