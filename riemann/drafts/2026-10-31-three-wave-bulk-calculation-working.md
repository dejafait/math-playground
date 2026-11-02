# Three-wave bulk calculation: working record

Approved target: exactly the S3 test in the existing EXPLORE assessment
`drafts/literature/2026-10-31-three-wave-stationary-bulk-review.md`.
Main gap is actual-Xi all-degree positivity. Intermediate target: full K
of L473 (6), stationary bounded ordinary derivatives, and clipped mean
at least 1/288. A pass could supply a derivative-consistent bulk only;
an upper bound below 1/288 rejects this choice. Full fourth constraints,
rare paths, derivative-preserving corrections and actual-data transfer
remain open. L576's two-wave stop is preserved. No cross-notebook input.

Startup overview/DAG and prior assessment supplied in full. Read L473
through Section 4 and complete L576 plus its attempt record; no matching
completed three-wave calculation was found in the scoped prior checks.
Existing unrelated unfinished changes are preserved.

Plan: specialize the phase covariance for all paired entries and prove
stationarity/support directly; then seek an exact analytic upper bound
or a complete certified integral enclosure for the nonlinear statistic.
Any numerical exploratory estimate is explicitly not evidence of the
threshold. Save any load-bearing certificate in scripts/three-wave/.

An exploratory sample (2,000,000 draws, seed 473576) returned mean
0.00119351, versus 1/288=0.00347222. This is not a proof or a
probabilistic certificate. It suggests trying a deterministic upper bound.

Proposed certificate: replace signed frequencies by independent uniform
[0,1/2] frequencies using phase reflection. Composite tensor trapezoids
with 16 frequency panels and 48 phase panels. The positive part inherits
coordinate semiconvexity from D=SS''-(S')^2: lower second derivative
-4 in each frequency and -(2/3)(2u_i^2+sum_(j!=i)u_j^2) in phase i.
Thus the normalized upper quadrature errors are at most 1/(4*16^2)
and 2*pi^2/(9*48^2). Grid values will use exact integer arithmetic
and rationally certified trig rounding with uniform error <=6/2^24.
This was unfinished reasoning at the initial checkpoint. Completed below.

Completed proof is canonical in L577. Its deterministic bound uses
pi<22/7 (verified from the rational Machin enclosure) for a short rational
phase-error expression. The complete exact tensor sum is
T=1891247392706538463615488 over 543338496 nodes, giving rounded
grid average 1231280854626652645583/1020031160299843366158336.
All errors included, E Q<=470333750554794227838685/
149944580564076974825275392<13/4000<1/288. No sampled estimate is
used in this comparison. Inspected the complete exact bounds, overflow
checks, all frequency slices and all 96 trig enclosures; the certificate
reports no failures. The script was rerun after replacing the long pi
error expression by the rigorously larger 22/7 bound and reproduced T.

Outcome NEGATIVE: stop this bulk at the prescribed threshold, preserving
the independent covariance and stationary-support conclusions. New L577
has not received a separate independent audit. Its proposed audit has
reused source-scope coverage, pending separate supervisor approval.
No new central creative mechanism is justified by this finite-wave
comparison; actual nonlinear law/tail transfer remains missing.
