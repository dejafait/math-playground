# Step 170: fixed two-weight covariance attempt

Approved target and prior coverage:
`drafts/literature/2026-10-16-mixed-covariance-weight-added-correlation.md`
(SPECIALIZE). Work is RESEARCH / REPRODUCTION / proof_attempt.

The main gap is global mixed positivity. The intermediate test is the
specified convex combination of the individually calibrated k=13,14
weights, inside L421's unchanged high/intermediate/bulk implementation.
A feasible law would show that this added correlation still does not
force capped nondegeneracy; actual/global realization, negative-Bcal
clipping and L413's full-error regulator margin remain independent gaps.
Continue only if both R_k>S, a fixed convex parameter matches T, and
the complete L421 interface survives. Stop if any of these checks fails.

Read L419's fixed-power/gamma and Borel matrix construction, L421's
complete proof and step-163 audit, L422's coefficient proof and step-168
audit, the fixed-g0 failure, and L415/L416's precise tolerance statements.
No completed two-weight duplicate occurs in the scoped step-169 source
record. The historical single-power stop is preserved.

Completed: the exact rational specialization gives both R_k>3/2>S
and 1/3<alpha<2/3. All certificate bounds, checks and the empty failures
field were inspected in full. The full compatibility proof is canonical
in `lemmas/L423-mixed-covariance-weight-preserves-added-correlation.md`:
the new weight retains every L421 constraint and matches the added
coefficient while the capped cubic still vanishes. The construction
is local REPRODUCTION, with independent critical audit pending. No
actual-function or RH claim is made. The new audit scope is explicitly
REVIEW_REQUIRED for separate next-turn coverage approval.
