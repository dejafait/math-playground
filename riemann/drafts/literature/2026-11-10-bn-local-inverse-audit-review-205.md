# Interior b_m inverse — nominated specialization audit

TARGET: Audit the actual-xi inverse lambda_n/n=sum_{m>=n} binom(m,n)b_m on an unconditional radius R>1 and determine the lower-tail decay needed to meet L968's every-epsilon Li criterion.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step205's exact b_n/binomial inverse/convergence/one-sided-growth searches and scoped duplicate/stop comparison in 2026-11-10-coffey-bn-inversion-review-204.md; no exact unconditional bound was inspected and no novelty is claimed.
SOURCE_EVIDENCE: [Coffey v1](https://arxiv.org/pdf/0912.2390v1#page=2), (1.1)-(1.3), pp2-3; [He-Jejjala-Minic v2](https://arxiv.org/pdf/0903.4321v2#page=8), (3.2)-(3.4), p8 and Section3.3 p14; [DLMF power series](https://dlmf.nist.gov/1.9.vi), (1.9.48),(1.9.63), [Taylor](https://dlmf.nist.gov/1.10.E1), [binomial](https://dlmf.nist.gov/4.6.E7), version1.2.8; [Lagarias published Theorem2.4(2)/(2.21)](https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf#page=15), reused through audited L968 including zeta normalization. Direct URLs and relevant passages confirmed in recovery step206; earlier primary reading details remain in the step205 assessment.
COMPARISON: The inverse identity is already stated in the literature; standard Taylor/Cauchy/binomial tools cover its interior analytic verification. The local actual-xi domain and quantitative one-sided decay specialization remain to be checked. This is reproduction/specialization, not a new mechanism or a source-proved lower bound.
GAP: Establish an RH-free R>1, branch consistency and absolute convergence of the complete differentiated inverse; quantify a sufficient near-2^-m lower-tail hypothesis and its amplification against every epsilon. Actual b_m lower bounds, Q signs and initialization remain open.
REASON: Prepare one bounded mathematical audit with a definite acceptance test, avoiding the unapproved forward alternating exchange and full-radius claim. Separate literature approval completed in recovery step206 with direct primary URLs; research may use this unchanged target next turn. No specialization was derived in step205 or step206.
SCOPE: Only the displayed inverse for n>=1 and b_m defined by the local logarithm F(z)=log xi(1/(1-z)) at z=-1. Actual zeros with multiplicities, no RH, no radius2 assumption, no forward transform or ordinate-only integral. Permitted outcome is a conditional transfer with an explicitly unproved lower-tail hypothesis, or an identified domain/quantifier defect.

Use L024/L026 localization and L964/L968 normalization. The logarithm
must be defined on the chosen zero-free disk and agree with its ordinary
Li germ near z=0. Verify a radius strictly greater than1 without assuming
the maximal radius2 or using any claimed unconditional full-disk proof.
The source's inverse is not to be reconstructed as a novelty claim;
local verification is justified because its cited derivation invokes
an unpaid radius assertion. Cite the known formula and standard tools.

The bounded test is to verify that inverse on one explicitly justified
disk, then quantify its transfer of a hypothetical one-sided lower
envelope b_m>=-C(delta)*(2-delta)^(-m) for every 0<delta<1, all m>=1.
This is a proposed hypothesis to test, not an established sufficient
condition or an actual-xi estimate. Retain constants, all indices,
possible finite exceptions and complete tails. Compare the resulting
lambda bound with the exact every-epsilon criterion rather than with
one fixed exponential rate. A weaker absolute bound at a fixed radius
does not automatically provide the needed one-sided threshold.

Continue only if R>1, complete-sum operations and all threshold
quantifiers can be verified without RH. Abandon this transfer proof
if it requires an unproved larger zero-free domain or a nonvanishing
tail/error; record the specific defect. Even success leaves the
independent actual-b_m lower bound unpaid and supplies no RH proof.
The downstream use is a certified criterion for evaluating a later
signed coefficient mechanism, not a claimed resolution. No such
mechanism is nominated until this cost is understood. Full matching
Mathlib coverage is unknown; no new search is essential for the audit.


## Recovery approval, 2026-11-10, step206

The reported defect was missing direct URLs in this ready assessment.
The exact target and SPECIALIZE scope are unchanged. Reused the prior
search/duplicate/failure comparison rather than repeat discovery.
Opened both versioned primary PDFs and the DLMF pages above. The
inverse is stated in He-Jejjala-Minic (3.4), printed p8. The preceding
radius-two assertion is not accepted as proof of logarithm analyticity;
Section3.3, p14, keeps the later positivity formulas hypothetical.
Coffey (1.3) fixes the same local coefficient convention; its abstract
explicitly conditions the asymptotic on RH. No actual coefficient
lower estimate is imported.

DLMF (1.10.1) requires analyticity on the disk; (1.9.48) and its
preceding paragraph give absolute uniform convergence on closed
strict subdisks; (1.9.63) gives termwise derivatives inside the radius.
DLMF (4.6.7) holds for complex exponent and absolute argument less
than one, with unrestricted argument only for terminating
nonnegative integral exponents. These tools do not supply the
actual-xi zero-free disk. Its verification and consistent logarithm
remain the mathematical audit's obligations, using L024/L026;
L964/L968 fix normalization and the required every-epsilon threshold.
L974 does not pay the proposed actual-b_m lower envelope.

Approval: sufficient source coverage for the bounded specialization
only, with the existing continuation/abandonment test. This is a
process repair, STALLED mathematically; no new obstruction, coefficient
bound, lemma, script or novelty claim. Full matching Mathlib coverage
remains unknown. PROOF.md and DAG.md require no change.
