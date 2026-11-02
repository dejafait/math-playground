# Two-center approximate values — bounded joint-target attempt

Prepared STEP_ID: 2026-11-02-two-center-values-research-01.
Reuse the unchanged EXPLORE assessment
`literature/2026-11-02-joint-full-grid-polynomial-dual.md`; the target,
integer family, full grid, angular mean and squared rate 1/16 are unchanged.
This is finite polynomial/residue development, not a new general
approximation theorem or an audit of inherited inputs.

Main gap: actual-Xi all-degree mixed positivity. A lower bound for this
joint projection could support the sufficient constant-input detector;
Xi realization, matching upper bounds, signs and audits remain open.

Read the complete L655 argument, L654's adaptive contour proof,
L651's Gram/correction proof and the relevant definitions and responses
in C645y, L649 and L650. The scoped duplicate/failure search found
L652's excessive repeated-jet cost, L654's distinct-count restriction,
L655's single narrow cloud, and L647's constant grouping stop. None
licenses adding independently optimized cloud bounds. Reuse the saved
primary-source assessment without new browsing or novelty inference.

## Reasoning saved before completing the bounds

Suppose Z lies within distance h of two selected centers c1,c2 in Z,
which may coincide. Use m=ceil(n/2048) and the artificial polynomial
Q(z)=(z-c1)^m (z-c2)^m, of degree 2m independent of |Z| and the
original residues. When 2m<=M, take the remainder H of the reflected
rational function f modulo Q. This means a single degree-<2m
polynomial, with confluent conditions if centers coincide.

On the union of radius r=m/(8n) disks about the centers, the regularized
kernel (Q(w)-Q(z))/(w-z) controls H on the full spatial circle. Boundary
points are at least r from both centers even when disks overlap, so
the denominator is at least r^(2m); no inverse separation occurs.
Writing B=max(|W_c1|,|W_c2|), the boundary value bound is B exp(m).
The prospective norm bound is
4m exp(m)(22n/m)^(2m-1) B.

For a pole within h of one center, |Q(a)|<=(3h)^m, since center
distance is less than 2. The complete Cauchy remainder therefore
suggests absolute error <=[2r/(r-h)] exp(m)(3h/r^2)^m B.
This controls both clouds with the same H, including all cross-cloud
values. Convert absolute error to weighted pairing error using
B<=sqrt(sum r_a|W_a|^2) and sum r_a|W_a|<=sqrt(M sum r_a|W_a|^2).

Test n>=32768 and h=2^(-34). Then r>=2^(-14), so error should be
at most 3*4^(-m) B and relative pairing error at most 1/4. The full
norm should be at most B exp(n/64). This leaves amplitude budget for
the original r_a^2 diagonal and L651's entire correction. If M<2m,
L654's sparse result applies. These constants are provisional until
the complete proof and scalar witnesses are checked.

Continuation test: prove the prescribed rate on this two-cloud
subfamily with constants and onset uniform in center separation,
original mass and distinct count, or record the precise failed
error/norm inequality. A large upper cost or a bad single angle is
not a counterexample. Dense support outside two such disks remains
open even if this attempt succeeds.

## Completed bounded attempt

L656 is the canonical proof. Outcome: RESEARCH / ADVANCE /
POTENTIALLY_NEW; actual task proof_attempt. The two-center construction
meets the stated rate with constant 1/4 for n>=32768 and radius
2^(-34), uniformly in all center separations and original residues.
It retains one full polynomial and all cross-cloud errors. The smaller
radius does not replace L655's larger one-cloud result. Both the new
proof and inherited inputs remain separately unaudited.

All 19 exact scalar checks passed; the entire /checks array was read
using the shared JSON inspector. The proof, rather than this scalar
certificate, supplies the analytic and uniform-family claims. No
unrestricted dense spread estimate or RH candidate was obtained.

The next proposed direction changes mechanism to a localized
logarithmic mean of the full spatial moment polynomial. Its source
comparison is incomplete and is recorded as REVIEW_REQUIRED in the
new assessment; no dependent mathematics was undertaken here.
