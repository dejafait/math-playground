# Uniform quadratic-curvature budget — working checkpoint

Approved input assessment: `drafts/literature/2026-11-01-uniform-resonant-entry-block-scope.md` (SPECIALIZE, supplied before invocation).
Main gap: actual-Xi all-degree signs and uniform collision exclusion.
Target: its exact COVERED_TARGET, on the one prescribed closed interval.
Inputs: C499c; L494, L495, L496, L499, with L497/L498 through the accepted mass.
No other notebook is used. Existing unfinished changes are preserved.

Attempt in progress: write eta/(2*pi)=x/(4*pi)+t/16-delta(x), where
delta=t*atan(1/x)/(8*pi)+3*t*x/(4*pi*(1+x*x))>0. Subtract
j*(j-1)/2 from -eta*log(j)/(2*pi); its exponential on integer j is
unchanged. Residual second derivative is eta/(2*pi*j*j)-1.
The last integer at a cutoff equality may have negative curvature;
it must be paid absolutely. Integer first-derivative resonances are
allowed by the assessed Arias de Reyna Lemma 5.

Planned certificate: bound delta and the analytic domain uniformly,
test every tail length for the full prefix at Y with exact arithmetic,
and build a valid uniform prefix/weight/product/two-charge envelope.
Floating-point diagnostics suggest the curvature-plus-tail bound is
larger than 256 for every split; this is not certified evidence yet.
No precision-based or mathematical success is claimed in this checkpoint.
If the explicit envelope misses r0 at adequate precision, park it.
This would not prove the actual uniform resultant is large.

Completed: the canonical specialization and qualifications are in C499d,
`lemmas/C499d-uniform-quadratic-curvature-envelope-stop.md`.
The exact certificate is `scripts/heat/uniform-quadratic-curvature-budget.json`.
All 255 tail choices lose to 256 for the full uniform prefix; their
affine dependence on prefix length supplies every smaller prefix.
The endpoint-specific test also loses, including all smooth initial
lengths. The actual finite phases are retained in the algebra; the
eventual triangle/product bound is deliberately conservative.
Uniform weights use sigma(X), not the endpoint Y weights. Both charges
are proved independently with full support and the full epsilon_1.

780 implementation checks pass, with no implementation failures.
The mathematical budget is explicitly ENVELOPE_FAIL: total lies in
(.00072254689054510978,.00072254689054510979), above
r0=.00042249381587054327798642829... . Width <1e-30, so no
precision refinement is needed. Exact best-row/weight/envelope values
and the empty implementation-failure list were inspected with the
scoped inspector. No actual supremum or collision is certified.

Outcome NEGATIVE, classification REPRODUCTION. Park this precise
curvature/absolute-tail/Abel envelope; do not repeat endpoint certificates
or claim a lower bound on the actual sum. A possible different estimator
would retain signed finite sums while enclosing spatial variation;
this is only a source-review nomination and is REVIEW_REQUIRED.
It has no source approval or new mathematical claim in this step.
PROOF's assembly is unchanged. The one new DAG row records C499d's
actual mathematical inputs; no prior result or unfinished work is removed.
