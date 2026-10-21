# Step 152 — auxiliary affine translations (work in progress)

The gate-approved target is exactly the 18,769 common auxiliary affine
translations of L047's five fixed quadratics under its original labeling
and original 61-core. The saved SPECIALIZE assessment is
`literature/2026-10-11-embedded-quadratic-affine-translate-rank.md`.
Inputs inspected: L047's full signed matrix and common-root proof,
C047a's common-root/tuple method (no scaling is applied here), L030's
incidence-only independence proof, and C012a's field/generator certificate.
ATTEMPTS/021,031 stop narrower cap models, not this rank diagnostic.

Plan: reconstruct representatives before exponents, all supports and
subset intersections, complete signed stars, and exact 12-column RREFs.
Save all operations and transformations; replay them and check the full
transformation identity and both inverse identities when full rank.
Save every singular case with a checked nonzero kernel. Compare (0,0)
with the audited L047 matrix and determinant 26669. Certificates are
split by a to keep selected JSON inspection bounded. The shared core
plus each outside intersection represents the full support intersection.

Decision test: a single singular case refutes universal full rank, without
asserting distinct-message realization. Verified full-rank cases provide
additional fixed-label exclusions only. Cap strength, all-core transport,
cross-core consistency, compatible subfamilies and safety remain open.
The exact fixed-instance bracket stays 955–957.

Completed: all 18,769 matrices have rank 12, both inverse identities pass,
and all 2,119,867 invertible operations replay. No singular cases or failed
checks occurred. The base case matches L047 including determinant 26669.
Full reasoning and qualifications are canonical in L049; complete evidence
is under `scripts/finite-support/embedded-quadratic-affine-translations/`.
The new independent critical-audit continuation requires separate approval.
