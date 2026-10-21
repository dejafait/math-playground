# Riemann hypothesis

Apply ../GOAL.md as the shared research policy.

Prove or disprove: every non-trivial zero of the Riemann zeta function has real part 1/2. A disproof requires an actual off-line nontrivial zero with a rigorous certificate.

## Literature baseline (checked 2026-10-21)

Before proposing a new zero-free region, reciprocal-series continuation, or reopening a parked arithmetic estimate, read [the October 2026 source and overlap assessment](drafts/literature/2026-10-21-openai-quasi-rh-overlap.md) and [the external-input register](foundations/2026-10-quasi-riemann-input.md). OpenAI family 003 supplies the cited fixed half-plane Re(s)>7/8, with a weaker alternate 11/12 proof; Liu's subsequent preprint improves the boundary slightly. Do not spend research turns reproving those stated conclusions as new discoveries. The boundary lines are not excluded. Full RH, all-degree mixed positivity, critical-line signs and realization of the selected jet laws remain separate. Existing proofs and countermodels retain their stated hypotheses; the new input requires reassessing L330/L331's older analytic envelopes before treating their route stops as current limitations on available zeta estimates.

## Known traps (do not treat these as a proof of RH)

- Assuming the explicit formula plus “error too small” without a proved zero-free region stronger than what is already known.
- Weil / explicit-formula positivity arguments that smuggle RH-equivalent positivity.
- Interchanging sums, products, or contours without a dominated or compact estimate.
- “All computed zeros lie on the line, therefore all zeros do.”
- Claiming a proof of Li’s criterion, Robin’s inequality, Lagarias, or Nyman–Beurling without proving the criterion itself in full strength.
- Using the prime-number theorem with an error term that already encodes RH.
- A “new contour” that is the same as a standard contour plus an estimate equivalent to a zero-free strip.
