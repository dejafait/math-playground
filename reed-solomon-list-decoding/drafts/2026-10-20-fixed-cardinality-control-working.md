# Exact-cardinality normalized control — work in progress

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-fixed-cardinality-normalized-control.md`.
This step tests only its frozen singleton mixture; no solve or retuning.

Main gap: arbitrary-center 68-agreement safety (67 also remains open).
Target: derive and test all 64 exact-N triple contractions after verifying
objective N and the inherited scalar/pair/PSD controls. A nonzero-distance
failure would exhibit an additional necessary cardinality constraint,
not a uniform bound. Continue only on such a failure with controls passed;
otherwise park this diagnostic.

Inputs: L001,L021,L022,L023,L097; foundations/04,12,13. Prior stops in
ATTEMPTS/033,034,080 concern different prescriptions or the old batch.
For a fixed ordered pair at half-distance i, four-region counting gives
coefficient binom(i,t)binom(68-i,j-t)binom(i,s)binom(956-i,j-s).
The source multinomial product divided by binom(68,i)binom(956,i)
must equal this integer. The proposed homogeneous equation is the sum
of these coefficients times y_ij^(t,s), over every actual orbit, equal
to N*p_i. At i>0, Z=X and Z=Y each contribute p_i. At i=0 the equation
is just the objective normalization. These statements still require
the complete justification and exact evidence in the canonical result.

Completed in L098. Both full scripts and their certificates are under
`scripts/finite-support/fixed*cardinality*`; the canonical lemma states
the exact paths. All 64 nonzero rows fail after inherited controls pass.
The prospective reasoning above is preserved as the pre-calculation
checkpoint, not as a second proof. Other moments, labeled restrictions,
RS realization, ABF comparison and the 955–957 boundary remain unresolved.
No fixed-size representing measure follows from convex normalization.
