# Normal-closure degree audit — step367

The invocation-start SPECIALIZE assessment is
`literature/2026-10-20-normal-closure-degree-critical-audit.md`.
The main gap is original finite B>=A. This audit checks L092's exact
indices and two distinct source comparisons, to identify which degree
argument a normal-closure repair loses. Continue only if the complete
ambient/core calculation, all six orderings, every primary valuation
and both ratios agree; otherwise correct the precise failure.

Read L092 and L090's complete relevant ambient, kernel, conjugacy and
audit arguments. Reused the degree-test assessment, step364 proof-use
ledger and step350's delta definition. Checked step365's calculation
and ATTEMPTS/033–035; the cyclic-Frobenius and authentication routes
remain parked. Existing notebook changes are preserved.

Reasoning saved for the canonical audit: reduction GL_2(Z/4) onto
GL_2(F_2) has sixteen elements in each fiber. The actual full joint
image gives ambient order 96*48*480. The six orderings give three full
kernels twice; the core retains both +++ and --- sectors. T is the
full mod-two field of degree six, not merely a parameter of degree at
most six. Thus the relative tower divisors are 8*6 and 2*6. All seven
factorizations and both ratios agree with L092.

Re-ran `python3 scripts/normal-closure-degree/check.py` and inspected
the complete `/values` object using the shared JSON inspector. All
seven values and 21 prime valuations match the factorization argument;
no arithmetic failure was reported. The script does not verify its
ambient/core premises. Full audit reasoning is canonical in L092.

Verdict: passes without mathematical correction or changed dependency.
This verifies a relevant known-method input, not a discovery beyond
the checked sources. No local degree, different or repair verdict is
derived. The distinct proposed local-at-two continuation is uncovered,
marked REVIEW_REQUIRED, and reserved for a separate source review.
