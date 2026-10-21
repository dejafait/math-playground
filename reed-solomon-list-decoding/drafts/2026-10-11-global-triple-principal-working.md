# Approved global triple principal trial — working checkpoint

The active target is exactly the SPECIALIZE trial in
`drafts/literature/2026-10-11-global-triple-small-principal-test.md`.
Main gap: arbitrary-center 68-agreement safety; 67 agreements remain open.
Test: reconstruct L022 pairs, retain L023 triples except set the full
L020 incidence to zero, check all 69 Johnson coordinates and the constant
Schur coordinate, and exhaust all actual anchor-containing principal
matrices with Boolean repetitions removed. A full above-threshold witness
stops only this batch; an exact failed matrix stops only this witness.

For anchor A and orbit (i,j,t,s), common intersection has size
68-i-j+t. Pair-only sizes are j-t, i-t, s; private sizes are t, i-s,
j-s. Consequently the prescribed incidence is exactly (5,5,3,2), with
h=5. It is invariant under reordering the three supports. No labeled
averaging is proposed. The global trial is checked directly.

For three distinct supports the normalized matrix is
[1,p_i,p_j; p_i,p_i,y; p_j,y,p_j], multiplied by positive rho.
All seven principal minors must be checked. Repeated supports give a
one- or two-index matrix and use their lower-order coordinates.
The constant Schur coordinate must be reconstructed, not assumed from
the earlier Schrijver normalization. Full conditioned PSD, representing
measures, a uniform useful bound and RS realization remain unproved.

Status: complete exact generation and independent arithmetic reconstruction
pass, with no failures. The canonical argument is L053; the full
certificates are `scripts/finite-support/global-triple-principal-results.json`
and `scripts/finite-support/global-triple-principal-audit-results.json`.
All 1500625 actual ordered orbits and 586967 stored principal minors are
covered, including 205 repetitions and the single incidence override.
All 69 pair spectra are positive before the constant Schur subtraction;
the constant Schur coordinate is zero. The objective has floor at least T.
This stops only the specified batch. Separate critical proof review remains
pending; preserve all earlier block/scalar and fixed-pair prescriptions.
