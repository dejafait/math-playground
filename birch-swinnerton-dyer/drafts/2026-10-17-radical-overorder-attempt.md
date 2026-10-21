# Full radical-action first overorder — step 295 working record

Approved target: Construct and independently verify one strict 31-overorder
of L077 using the Frobenius radical and full action on I/31I, with exact
integral lifting witnesses and no ideal-power expansion.
The unchanged SPECIALIZE assessment is
`drafts/literature/2026-10-17-prime-local-overorder-construction.md`.

The main gap is arbitrary-curve rational-rank equality at analytic order
at least two. A first corrected order could support later complete
units/classes for L066. All other index primes, maximality, unit/class
completeness, descent conditions, successful localization, rational
membership and complex-order comparison remain missing.

Inputs are audited L067/L077/C077a: entire degree-48 field, original
H=343h, all original basis/product/transport data, prime 31 and gcd
T²+24. Reuse Stevenhagen Section 9 pp.233–235 and Del Corso–Dvornicich–Simon
Proposition 9/Theorem 2(ii) as assessed. No step-293 partial output,
L026 premise or cross-notebook result is an input.

One producer and one independently implemented full replay, each at most
180 internal/181 external seconds, combined files at most 134217728 bytes.
Require full Frobenius and I/31I action kernels, both integral preimages
with two-sided generation identities, all new products/transports and
exact index 961. A cap, missing coverage or failed identity permanently
ends this execution without retry, resumption or larger limits.

Implementation plan: use the full original product table for producer
Frobenius/action computations. Lift row-reduced kernel bases together
with 31 times all 48 coordinate vectors. Selected generator columns give
triangular integral bases; explicit integer matrices verify both
generation directions. Replay modular Frobenius by independent polynomial
arithmetic and all new products by polynomial divisibility in original H.
Complete finite-field row operations, pivots, terminal zeros and kernels
are retained. No ideal-power witness is expanded.

Completed result: the one producer and one independent replay both pass.
Frobenius rank and action rank are each 46, both kernel dimensions are two,
both integral preimages and full transports pass, index is 961, and all
110592 old-product, 110592 action and 110592 new-product slots pass.
Producer time is 1.558305 internal/1.837445 external seconds; replay time
is 1.340107/1.422083. The consolidated directory uses 9430944 bytes.
All 72 original files are preserved, and no failure or retry occurs.

The canonical proof is L078; `scripts/seven-torsion/radical-overorder-295/`
contains full certificates, reports and summary. This is known-method
reproduction and supplies no result beyond the checked source theorems.
The new assembly awaits a separate critical audit. The next assessment
is `drafts/literature/2026-10-17-radical-overorder-critical-audit.md`,
which needs separate supervisor approval before execution. All broader
limitations above remain; the original stopped power log stays parked.
