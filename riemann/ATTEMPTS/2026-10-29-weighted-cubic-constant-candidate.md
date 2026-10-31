# Actual-weight cubic feasibility: constant-candidate test parked

The approved E_3 infimum was tested using its included p=1 candidate,
L477/L481 and the prior EXPLORE assessment
`drafts/literature/2026-10-29-saturation-weighted-cubic-feasibility.md`.
[The working calculation](../drafts/2026-10-29-weighted-cubic-constant-test-working.md)
preserves the full unsuccessful estimate. No new accepted lemma,
counterexample or decision of the cubic infimum results.

WHY IT FAILS: splitting D_0=F+Q_0 suppresses explicit F terms at
cost O(T(log T)^(5/2)) in the complete weighted error, but the
remaining quadratic jets have only an O(T(log T)^3) bound. Replacing
their weight by one is the precise loss. Furthermore, little-o success
for this constant would force little-o signed saturation correlation
by L477's signed bound; it would not also give a positive full-scale
certificate. Neither the candidate's true error nor the infimum over
T-dependent cubics is decided. Park this implementation after the
ordinary-moment mismatch. Reopening requires a materially new
actual-height weighted estimate or coefficient-uniform separation,
not a renamed scalar-moment test. Preserve the separate L481/L482
stops and all unfinished prior work.
