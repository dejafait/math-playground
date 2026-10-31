# Actual-Hermite first-variation certificate: source-ready audit scope

TARGET: Audit L568's negative B_64(1) certificate by independently contracting all coefficient intervals and checking the L564 infinite-tail bound through two derivatives.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact-first-variation search and comparison in 2026-10-31-hermite-coupled-first-variation-test.md and its parent review; local L564/C567a audits cover the unchanged coefficients, derivative tails and interval arithmetic. This is verification of a specified new local certificate, not a new sign-theorem search or a claim of novelty.
SOURCE_EVIDENCE: Dan Romik, arXiv:1902.06330v3, https://arxiv.org/html/1902.06330v3#S2.SS1, (2.1), Theorem 2.1/(2.2)-(2.3); proof (2.20)-(2.22), https://arxiv.org/html/1902.06330v3#S2.SS3; NIST DLMF 18.9.25, https://dlmf.nist.gov/18.9.E25, and 18.14.9, https://dlmf.nist.gov/18.14.E9 (v1.2.8). These primary statements and the relevant remainder proof passage were retrieved on 2026-10-31; reuse L564 (4) and its application audit, and C567a's completed coefficient-enclosure audit, without claiming a new numerical replay.
COMPARISON: Known expansion and derivative inputs justify a finite tail plus a uniform infinite-tail enclosure; C567a certifies all required coefficients but its old polynomial evaluations do not decide B_64(1). The difference is the new complete contraction at t=1, partition at n=64, and three mixed products in L568.
GAP: L568's new certificate has not received an independent audit. Its sign and stated rational enclosure must be replayed from complete coefficient data with all errors; no interval Xi margin, all-height loss estimate or higher-form conclusion is part of this check.
REASON: The first bounded probe rejects the nominated universal sign if correct. Independently checking the finite arithmetic and applicability of the existing all-derivative bound protects that route decision; no essential source is missing for this exact audit.
SCOPE: One audit of L568 at T=t=1, N=64, M=256, j=0,1,2; no new quadrature, additional probes, new cutoff, or continuation of the refuted universal sign. The separate literature-only recovery on 2026-10-31 supplies direct primary URLs and confirms this unchanged audit scope is source-ready; no certificate audit is performed in that recovery.

The main gap remains actual-Xi all-degree positivity. This intermediate
audit could establish reliable stopping evidence for one sufficient
transfer mechanism. It is not an effort to prove a stronger negative
claim or a new mathematical mechanism in the same turn.

Essential inputs are L564 and C567a; the object to check is L568 and
`scripts/hermite-gram/first-variation-certificate.json`. L564 (4) applies
at arbitrary integer cutoff M=256. Its j<=2 bound, multiplied by
exp(t^2/2)<9 for 1<=t<=2, must cover the whole tail beyond 256.
C567a's complete coefficient source must match its audited hash;
reusing this source is explicitly allowed and must not be described
as fresh theta-node verification.

Independently check every coefficient interval used, all finite Hermite
values/derivative multipliers, the n=0,...,64 versus n=65,...,256 split,
the addition of both signs of the infinite-tail bound, and every signed
interval product. Confirm complete-rational inclusion in L568's stated
coarse bounds; merely reading display fields is not enough. Dependence
among intervals may widen them and must never be used to narrow them
without proof. Verify the endpoint t=T=1 and the actual Xi normalization.

Continue only if an independently obtained complete upper bound remains
strictly below zero with all imported hypotheses satisfied. Otherwise
repair or withdraw the unsupported enclosure while preserving the failed
evidence. A zero-containing interval is inconclusive, not positivity.
Neither outcome authorizes a wider probe grid or all-height inference.

Unresolved independent tasks are compensating polynomial margins,
quantitative signed and quadratic losses, cutoff jumps, all-height
uniformity, multiplicities and higher forms. No cross-notebook input
or nonzero-jet assumption is used. Full Mathlib coverage is not checked.

### Separate source approval and URL repair, 2026-10-31

The supervisor reported missing direct source URLs, not a mathematical
failure of L568. This separate literature turn repairs that defect.
The exact TARGET, SPECIALIZE decision and single-point scope are unchanged.

Actually read online: Romik v3 Section 2.1, (2.1)-(2.3), and Section 2.3,
(2.20)-(2.22) through its concluding bound. The theorem is for the actual
Xi and the stated coefficients, uniformly on every complex compact,
with constants depending on that compact and all integer N>=1. The
remainder proof uses the Hermite generating function and absolute
integrable majorants; it supplies no sign for the mixed contraction.
Its unspecified constants do not replace L564's explicit derivative
bound. Import this theorem; do not reprove it in the arithmetic audit.

Actually read online: DLMF v1.2.8 (release 2026-09-15), 18.9.25,
H_n'=2n H_(n-1), and 18.14.9, the normalized Hermite absolute bound
for every real argument and nonnegative integer degree. The derivative
formula uses n>=1, with the constant polynomial handled separately.
These are the physicists' normalization used locally. The TeX endpoints
were unsupported by the browser, but both complete formulas and domains
were available in the primary HTML; no essential source is blocked.

Local comparison reused the parent first-variation assessment, L564's
statement and completed application audit, C567a's completed audit status,
and the retained first-variation failure record. The existing failed
universal sign is not reopened. The exact contraction is new local work
awaiting audit, not a known conclusion imported from these sources.
This review neither reads display values as verification nor certifies
any coefficient, contraction, or infinite-tail arithmetic anew. The
coefficient source hash and full interval data must be checked next.
Mathlib coverage of the complete certificate remains unchecked.
