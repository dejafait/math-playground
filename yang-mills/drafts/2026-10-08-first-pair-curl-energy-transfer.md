# Exact curl-energy transfer for the actual circulation/path trace

Working step YM-20261008-099-first-pair-curl-energy-transfer.
Reuse the unchanged SPECIALIZE assessment in
`literature/2026-09-26-current-target.md`; this is a mathematical
attempt within its combined-response target, not a new literature review.

Main gap: ultraviolet-uniform interacting response and ultimately the
reflected-error bound c_box/2. Intermediate test: remove the full right
covariance from one generator placement of L076(1), retaining the actual
variable coefficients, then bound the other placement and Q_3+Q_6 by
O(N²). A successful reduction would isolate the possible N³ contribution
in an actual finite local trace and permit a later signed asymptotic test.
Continue only if the relative boundary identities and the O(N²) remainder
hold; otherwise preserve the exact decomposition without claiming a
coefficient. This does not retry ATTEMPTS/019–025's norm-only closure.

Saved unfinished reasoning: Z_l=D^T bar Q_l S is transversely co-closed,
as is X_l=Sigma_T Z_l. The full field I_T X_l is co-closed, so
L_0 I_T X_l=I_T Z_l. For y=E_0 g, L_0 y=E_0 Delta_V g.
The two generator placements therefore separate exactly. The potentially
large one is <I_T^T K_a E_0 g,Z_l>/2; the other involves
E_0^T K_a I_T X_l. Its axial derivative should transfer onto the compact
u_mu coefficients because E_0 is axially constant. This requires the
exact endpoint and clover averages, not a bulk Fourier substitution.

Essential inputs under inspection: L009, L062, L064, L065, L066,
L070, L074, L075, L076. L077 is a contrasting frozen diagnostic only.
Known results and duplicates checked in the supplied assessment and
the targeted canonical proofs and weighted-high-trace draft. No primary
renormalization theorem needs reproving. All exterior indices and pinned
rows remain; no internal covariance cutoff is introduced.

Independent open tasks: signed local-trace asymptotics, centered path/path,
scaled exterior defect, all nine mixed placements, shared quartic subtraction
once, all remaining action/measure/insertion/flow jets and logarithm,
continuum fields, reflection positivity, infrared control and finite mass.

Completed: L078 proves the exact reduction and O(N²) remainder for
both actual probes. Its proof retains the relative co-closed column,
full axial inverse before cancellation, actual clover/endpoint averages,
compact coefficient derivatives, curvature subtractions and complete
exterior heat sum. The reverse placement's mixed whitened norm is
bounded; the forward placement retains the growing mechanism in the
explicit finite transverse trace (2). No comparison with the frozen
diagnostic, asymptotic value or full first-pair bound is asserted.

Outcome ADVANCE / RESEARCH / REPRODUCTION: a controlled reduction
of an actual contribution, not a new general theorem beyond the sources
checked. No mathematical script was needed. The input domains, signs,
axial normalization and pinned endpoint terms were checked analytically.

Continuation within the unchanged approved target: evaluate or bound
L078(2)'s signed transverse trace with all k,l and levels retained.
Seek a controlled N^(-3) limit or an O(N²) bound; neither is supplied
by its finite definition. Essential inputs L028, L062, L064, L065,
L070, L074, L075, L076, L078; L077 remains diagnostic only. The
unresolved assumption is a justified asymptotic for the two pinned
Green factors with variable coefficients. The independent gaps above
remain; no additional literature assessment was written or changed.
