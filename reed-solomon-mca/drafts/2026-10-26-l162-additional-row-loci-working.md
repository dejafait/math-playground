# L162 additional-row loci — step 507 working record

Approved target: Determine the exact rank-one parameter loci on L162's projective family for every additional original row whose support meets each of its four supports in at most one point.

Invocation-start assessment: `drafts/literature/2026-10-26-l162-additional-row-parameter-loci-review.md`, SPECIALIZE; completed work will be REPRODUCTION. No further source search is needed.

Main gap: uniform twelve-row exclusion. The intermediate calculation restricts only the audited fixed L162 family; complete loci could test its compatibility with further rows. Other families, coding realization, source identification and radius remain unresolved.

Plan: enumerate all 756 Cartesian original labels, exclude the four fixed labels, record all four support intersections, and retain exactly those with all sizes at most one. Construct Q directly from L109's products. Save four-by-two homogeneous linear entries and six homogeneous quadratic minors. On r=1, certify both the minor gcd and entry gcd by division and Bezout identities over F_97. Handle identically zero systems separately; test r=0 directly. Rank one is minor vanishing minus entry vanishing. Independently reconstruct products and verify every certificate, including excluded labels and endpoints.

Continuation/abandonment test: accept only complete original-label coverage, exact polynomial witnesses, extension-root validity and explicit rank-zero removal. An incomplete calculation leaves the target open. No base-field sampling inference or twelve-row conclusion is authorized.

Inputs: L109's map formulas only and L162's audited four vectors and all-parameter plane proof. No L159–L161 classification premise. All earlier work is preserved.

Completed: all 756 original labels were tested; 112 additional rows are eligible. Their minor gcds on r=1 are 1 (72 rows) and t+3 (40 rows). All 112 entry gcds are 1. Both projective endpoints have rank two for every eligible row. Thus exactly forty rows have locus {[1:94]} and the other 72 have empty locus. Canonical proof and qualifications are in L163; no larger-family conclusion was attempted.

Full producer and independent verification certificates are `scripts/seven-coordinate/l162-additional-row-loci.json` and `scripts/seven-coordinate/l162-additional-row-loci-verification.json`. The independent reconstruction passes 4,946 checks, with no failures, including complete coverage, every homogeneous coefficient, all divisibility/Bezout witnesses and direct endpoint minors. Shared Python/arithmetic remains a limitation; separate critical audit is the proposed next action.
