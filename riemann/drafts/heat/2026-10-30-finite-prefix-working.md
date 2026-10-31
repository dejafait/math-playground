# Finite coefficient prefix — working record

2026-10-30. Approved target: certify the entire 2<=m<=N prefix at the
specified corner against 1, using the saved SPECIALIZE assessment
`drafts/literature/2026-10-30-finite-support-reserve-obstruction-coverage.md`.
Main gap: actual-Xi positivity; downstream collision reserve also needs
edge, tail and charges. This calculation cannot settle those gaps.

Inputs: L494's normalization and frozen cutoff, L495's full beta formula,
L496's exact sigma formula and ell0=24.18022820120389. Base-phase/saddle
imports retain their qualifications; no source decimal is a certificate.
The inspected assessment found the stronger source Proposition 6.8 claim;
this is reproduction, not novelty. The charge-approval stop stays in force.

Planned exact method: enclose a_n=b_n*n^(-sigma), then for each prime p
update c_m <- c_m-r_p*c_(m/p) in descending multiples of p. Initially
c_m=a_m. Descending order uses the pre-factor vector and hence each
prime at most once. Projection to m<=N cannot lose a contribution to
these indices, because multiplying indices never decreases them.
Certify N from square inequalities and h_ell0=1 from 2 log N<=2 ell0.
Do not assume coefficient signs. Enclose signed c_m before abs and sum.

Test: upper<1 gives only a partial budget input; lower>=1 stops this
conservative certificate; straddling requires a specific error bottleneck.
Full endpoint evidence and scripts will be stored under scripts/heat/.
At the time of this initial checkpoint no enclosure had been completed.

Completion: the approved prefix attempt succeeded. The canonical proof,
exact enclosure, scope and full certificate paths are in
`lemmas/L497-fixed-corner-finite-coefficient-prefix.md`. The complete
finer-grid consumer passes 4146045 checks with no failures. This is
known-method reproduction; no edge/tail or collision claim follows.
Current continuation and review routing live only in `PROGRESS.md`.
