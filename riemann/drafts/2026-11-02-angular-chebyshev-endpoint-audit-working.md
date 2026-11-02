# C645r conceptual audit — working record

STEP_ID being prepared: 2026-11-02-angular-chebyshev-endpoint-audit-01.
Unchanged ready coverage: `drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.
One proof audit within the saved angular target; no radius extension or
new pole family is being attempted.

Main gap: actual-Xi all-degree mixed positivity and unbounded-height
signs. Intermediate target: validate C645r's compact Chebyshev-band
lower bound at exponent 0.030504<1/32. Downstream use: exclude this
restricted class of angular countersequences and support a possible
common-pole detector. General families, Xi layer isolation, other poles,
census/clearance, simultaneous realization, an independent upper bound
and signs remain unresolved.

Accept only after checking both endpoint branches/orientations, relative
errors uniform in n,r,u, phase separation, the finite-node identity,
the full relevant rational certificate and fixed angular measure.
Otherwise repair the precise defect or downgrade the claim; a finite
screen cannot settle any of these questions.

Read C645r in full, C645g's normalization and exterior-series proof,
C645l (23)--(24) with its complete finite-node proof, C645o's exact
angular weight and Fourier normalization, and C645q's energy/rank proof
for the auxiliary consequence only. Reused the ready source comparison
and checked the endpoint history/working note and the full-energy and
ellipse method-stop records. Earlier uncommitted work is preserved.

Initial checks: the rectangle radicand has real part h^2+r^2-y^2>0
away from its endpoint zeros. The three-side path has the same integral
as the upward segment, giving the lower-minus/upper-plus orientations
in (15). The angular change u=i exp(i theta) preserves normalized
measure and the conjugated factor denominator. The first two exterior
coefficients provide a legitimate constant-input lower bound.

Still to complete: independently follow every error and exponent
comparison, replay the exact rational certificate, and inspect its
complete relevant fields. No audit conclusion is recorded yet.

## Completed audit

All of the stated checks passed without a mathematical correction.
The detailed audit is canonical in
[C645r](../lemmas/C645r-chebyshev-band-angular-endpoint-lower-bound.md).
It distinguishes the rectangle and ellipse square-root branches,
checks the two-phase singular-value bound, and compares each error
with the leading vector using constants uniform on the closed band.

Replayed `scripts/one-sided-hankel/angular-endpoint-rate-certificate.py`
after reviewing its exact rational algorithm. The upper bound remains
15559465959309/512000000000000 < 61/2000; all nine auxiliary checks
passed. Inspected the complete selected upper bound, strict margin,
auxiliary checks and empty failures via the shared JSON inspector.
This arithmetic does not replace the analytic audit. The exact gap
1/32-0.030504 is 373/500000; no onset was numerically certified.

Outcome ADVANCE / REPRODUCTION means validation of this existing local
input, not a new bound or a claim of originality. No mathematical
argument or DAG input changed; PROOF.md and DAG.md remain untouched.
The full angular detector and the actual-Xi bridges remain open.

The sole next research focus, recorded in PROGRESS.md under the same
exact target and unchanged ready assessment, is one oblique-grid test
for 9/20<r<=1/2. No estimate for that band was derived during this
audit. Earlier failed envelopes, diagnostic evidence and unfinished
reasoning are preserved.
