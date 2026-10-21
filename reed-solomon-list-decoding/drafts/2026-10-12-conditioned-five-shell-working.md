# Step 173 — full conditioned distance-five shell

Gate-approved target: Test L053's unchanged trial on the full singleton-conditioned half-distance-five shell, including the anchor and the exact (5,5,3,2) incidence override, by a complete stabilizer spectral certificate.

Saved before calculation. Reuse the separately approved SPECIALIZE assessment
`drafts/literature/2026-10-12-conditioned-five-shell-spectrum.md`.
The main gap is arbitrary-center safety at 68 agreements; 67 agreements
remains independently unresolved. Essential local inputs are L001, C001a,
L020–L023 and audited L053, with foundations/04,09,12.

For B in the distance-five shell of A, write X=A\B, Y=B\A.
Both have size five. For a second C, the factor relation distances r,q
give t=5-r, s=5-q and h=r+q. Boolean diagonal r=q=0 uses p_5.
Distinct entries use zero for h=1,...,4, zero at (r,q)=(2,3), and
p_5^2 p_h/p_68 otherwise. The normalized anchor row is constant p_5.
Compute the full J(68,5) x J(956,5) spectrum and subtract p_5^2
times the shell cardinality only in the constant Schur coordinate.

Continuation/abandonment test: one exact negative coordinate excludes
this fixed trial only; all nonnegative coordinates with the anchor
condition park this shell only. Complete all 36 modes, multiplicities,
entry/repetition checks and independent normalization reconstruction,
then stop without retuning. General pairs, other conditioned matrices,
representing measures, a uniform bound below
T=floor(65537^28/2^128)+1 and RS realization remain open.

Completed: [L054](../lemmas/L054-conditioned-five-shell-fixed-trial-exclusion.md)
records a complete exact exclusion of this trial: 12 negative and 24 positive
Schur modes; the nonconstant (0,1) mode of multiplicity 955 already excludes
the shell block. All 328 independent reconstruction checks pass. Full
certificates are `scripts/finite-support/conditioned-five-shell-results.json`
and `scripts/finite-support/conditioned-five-shell-audit-results.json`.
The bounded test stopped without retuning. Separate critical proof review
remains pending; no uniform bound or boundary change follows.
