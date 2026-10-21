# L427 critical audit — step 203 working record

Authorized target: the separate audit in the pre-existing SPECIALIZE
assessment `literature/2026-10-17-response-cubic-modulus-audit.md`.
The supplied overview and DAG were used before the detailed proofs.
Existing notebook changes are preserved.

The main gap is global mixed positivity. The intermediate target is
reliability of L427's fixed-law separator, with possible downstream use
as a necessary correlation constraint on covariance constructions.
Retain it only if the complete sharp actual mean, all three law
components, and the exact actual-minus-law gap greater than 7/1000 pass.
This does not test another weight or decide clipping or realization.

The first pass checks L381 (7),(9), L389's zero-safe Hardy
identification, L419 (3), L421 (4),(6), and L423 (5),(9),(10).
No analytic defect identified: fixed head then smoothing removal then
uniform head-tail passage; all rare second integrals are unnormalized;
the full covariance correction and bulk mean remain lower order.
The order-three local factor and composition tail bound have been
checked algebraically. The completed analytic audit and all full proof
details are canonical in L427's separate step-203 audit section.

Completed verification uses a separate script with no generator imports,
trial-division primes, direct binomial local coefficients, finite-difference
generating numerators for both T factors, independent outward rounding,
and complete comparisons of saved finite factors, tails, global bounds,
checks and failures at both saved cutoffs. Full evidence is saved in
`scripts/discriminant/response-cubic-modulus-second-moment-audit-203.json`:
13546 comparisons pass, with no audit failures. The earlier P=200
certificate uses the historical independent-alpha expression and failed
1/100000 test; the verifier was adapted to that format without changing
the saved artifact. Both historical failed enclosures remain recorded.
Decimal previews are not proof evidence.

Outcome ADVANCE denotes local critical validation of an existing input,
not a new discovery. The mathematical assembly and DAG are unchanged.
The bounded-covariance finite-prime question is proposed solely for a
separate source review; no mathematics for it was performed or approved.
