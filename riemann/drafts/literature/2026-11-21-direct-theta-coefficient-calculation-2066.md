# Direct actual-theta coefficient calculation — ready nomination2066

TARGET: Certify Romik's c0,c2,c4,c6 to absolute interval width at most 2^-40 using (1.7)/(3.3), explicit theta-index/spatial tails and outward-rounded composite Simpson integration.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed review2066 in 2026-11-21-direct-theta-four-coefficient-certificate-review-2065.md, including narrow duplicate/failure checks and exact coefficient/certification queries; no novelty claim.
SOURCE_EVIDENCE: https://arxiv.org/html/1902.06330v3 (1.7)/(3.1)-(3.3); https://dlmf.nist.gov/3.5.ii (3.5.6)-(3.5.8); https://dlmf.nist.gov/8.2.E2 and https://dlmf.nist.gov/8.4.E8 / https://dlmf.nist.gov/8.4.E11; https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp . Direct primary passages rechecked in recovery2067; earlier broader comparison retained in review2066.
COMPARISON: Import the coefficient formula and standard quadrature/error identities; derive only explicit tail majorants, finite integrand derivative bounds and actual-input enclosures. L530 supplies a downstream polynomial template, not actual values; L768/L821 concern different observables.
GAP: Specialized tail/derivative constants, interval constants and final four enclosures remain unproved/uncomputed. The target width is an acceptance threshold, not an asserted error or guaranteed discriminant margin.
REASON: A bounded reproduction/specialization of known formulas for the actual measure can inform a later theta-specific invariant test; the sources do not supply this certificate. No expansion reproof or generic-preservation theorem is needed.
SCOPE: One degree-six input certificate, j=0,1,2,3. Direct-source recovery2067 approves this unchanged target for a later REPRODUCTION calculation. No calculation was executed in steps2066/2067; no radius grid, higher-degree sweep, arbitrary-measure search or RH claim.

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Use: actual m_j=c_(2j)/c0 enclosures for the cubic-in-t^2 diagnostic
specified in review2064 and L530. This calculation need not decide it.

Retain the actual measure in (3.3); reuse October30 normalization.
Use no endpoint atoms, centered-series integration, tilted beta values
or Q6 values. Import Simpson's theorem for real C^4 integrands and
positive even panel counts, with its exact remainder. Prove a bound
for the finite integrand's fourth derivative throughout [1,X]; sampled
derivatives or agreement of two quadratures are insufficient.

Prove separate theta-index and spatial tails with explicit constants
and onsets; justify sum/integral comparisons and interchanges.
The gamma identity evaluates a proved majorant integral, not the
comparison itself. Retain all four error components: theta-index,
spatial, Simpson and arithmetic/constants. Certify pi/square-root
endpoints and check the actual Decimal runtime, contexts, rounding,
exponent bounds and exceptional flags. Backend correctness remains
an explicit trust assumption; no new dependency installation is needed.

Bound this attempt by X<=64, N<=32, at most 2^18 equal subintervals
per coefficient and at most 100 decimal working digits. These are
work caps, not proved adequate cutoffs. Stop at a smaller valid
certificate if possible. If a cap or width test fails, retain proved
bounds, actual achieved widths and failures; do not silently increase
the caps or switch integration methods.

Success requires complete positive finite c0,c2,c4,c6 enclosures,
each width<=2^-40, with all mathematical/arithmetic bounds written
out and full evidence saved. Ratios may then be enclosed after checking
c0's positive lower bound; this does not guarantee a discriminant sign.
Print achieved/required widths, failures and paths; inspect every
load-bearing certificate field. This target is REPRODUCTION.

Essential inputs: Romik's formulas, October30 normalization, cited
Simpson/gamma identities and arithmetic contract. L530 is a downstream
template/contrast only; no local lemma signs these coefficients.
Initial roots, collisions/multiplicities, all-degree estimates, a useful
invariant and Xi transfer remain open. Matching Mathlib coverage is
unchecked. No cross-notebook input.

### Direct-source recovery2067 (2026-11-21)

This approval repairs missing direct URLs, rather than expanding the target.
Reuse review2066's exact-statement search, duplicate checks and preserved
centered-series stop2065; no new search for coefficient novelty is needed.

Reopened Romik v3 (1.7) and Section3.1 (3.1)-(3.3). These fix the
actual theta summands, absolute convergence and even coefficient integral
on [1,infinity), including its 4sqrt(2) normalization. Import these
identities; do not substitute tilted or atomic moments. The previously
inspected asymptotic bounds still do not give numerical tail constants.

Reopened DLMF Section3.5(ii), (3.5.6)-(3.5.8), including the C^4
hypothesis, even positive panel count, h=(b-a)/n, and fourth-derivative
remainder. Its application is restricted to the finite real integrand;
the full-interval derivative bound is still owed. Reopened (8.2.2),
(8.4.8) and (8.4.11), including the nonnegative integer index and path
qualifications. Use positive real lower endpoints for majorant integrals;
these identities provide no theta-tail comparison.

Reopened the Python Decimal documentation, currently headed Python3.15.2,
Decimal.exp: its result uses ROUND_HALF_EVEN, independently of a desired
directed endpoint policy. Reuse the prior context/neighbor/signal
assessment. The later certificate must identify its actual runtime and
validate outward transcendental endpoints, constants, flags and exponent
range; this source review does not test a runtime.

Decision remains SPECIALIZE. This is source approval for known-method
reproduction, not new mathematics or a coefficient certificate. Backend
correctness remains a trust assumption; matching Mathlib coverage remains
unchecked. No new lemma, calculation or mathematical script was written.
