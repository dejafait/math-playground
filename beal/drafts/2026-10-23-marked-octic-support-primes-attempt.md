# Support-prime calculation in progress

The gate-approved target is the complete decomposition of 2,3,5,11 in
audited L116's entire maximal ring, with explicit residue maps and exact
ideal-product certificates. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-support-prime-decomposition.md`.

The main gap is rational-point control and eventual primitive integer
emptiness; this intermediate calculation supplies support primes for
later S-unit and S-class arithmetic. It does not compute those groups,
local point images, degree-nine root recovery or either L095 integer system.

Use L116's final multiplication table. Discover the reduced finite
algebra by the nilpotent-killing Frobenius image and exhaust its small
idempotent space, within the approved arbitrary-order finite-algebra
method. Certify each proposed residue field independently by a primitive
generator, irreducible polynomial and a surjective multiplicative map.
Lift its exact kernel to a full integer ideal basis. Certify positive
ramification exponents by full integer ideal products, with reversible
lattice operations, requiring product(P_i^e_i)=pO_K and sum(e_i*f_i)=8.

Continue only when all four primes pass complete checks. Save any failed
checks and partial evidence; no dimension-only or determinant-only claim
will count as a complete decomposition. Existing work, including L108
and ATTEMPTS/050–051, is preserved. No cross-notebook input is used.

## Completed instance

L117 records the complete decompositions and their exact ideal-basis
formula in L116's fixed basis. The producer certificate and independent
replay are `scripts/pair-genus-two/marked-octic-support-primes-certificate.json`
and `scripts/pair-genus-two/marked-octic-support-primes-replay.json`.
All eight prime quotients, 38 successive-power products and 30 assembled
products were consumed by the replay; 1,210 comparisons pass. Each final
product is exactly pI_8, and each degree sum is eight.

An initial startup run rejected a descriptive source string because the
Fraction decoder treated every string containing a slash as a rational.
The traceback was a startup decoder error before field calculations;
the decoder now restricts parsing to rational-number characters. The
completed producer and independent replay have zero arithmetic failures.
No partial mathematical result was promoted to a complete decomposition.

The independently inspected quotient maps and complete ideal bases are
retained together in `scripts/pair-genus-two/marked-octic-support-primes-presentation.json`.
They agree with the canonical formula in L117. The bound and completeness
tests all pass; class/unit groups and point methods were not attempted.
The next step is approval for a separate critical audit, with its new
assessment marked REVIEW_REQUIRED. This does not reject completed work.
