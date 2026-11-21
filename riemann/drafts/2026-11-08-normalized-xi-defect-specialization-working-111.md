# Normalized Xi-defect specialization — working checkpoint

Completion note: the reasoning below was saved before the final checks.
The completed proposed proof is now canonical in L899; it remains
unaudited. This earlier plan is retained as the interruption checkpoint.

2026-11-08, step111. Research on the exact preapproved SPECIALIZE target
in drafts/literature/2026-11-08-normalized-xi-defect-interpolation.md.
No source refresh or target extension is needed. L019/L020 and L898
have been read; the L898 fixed-endpoint stop and L309/L312 ordering
contrasts were checked in the existing assessment and local records.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
The bounded intermediate target is full-L1 Lipschitz control in y² for
the same normalized W_y. A later interpolation use requires an
independently proved sign margin; none is assumed here.

Proof in progress: use mu=W_(1/2)/B, B=A_0(1/2), a=A_0(0),
p=u+v, and Psi_y=log(sinhc(p/2)/sinhc(yp)). The cited sinh product,
with log(1+x) Lipschitz on x>=0, should give
|Psi_y-Psi_r|<=p²|y²-r²|/6, including zero without differentiating an
integral. Hence 0<=Psi_y<=p²/24; positive-measure neighborhoods of
p=0, rather than that null line itself, should give essinf Psi_y=0.
Exact normalization should be Z_y=A_0(y)/B>=a/B.

Candidate constant for full L1 after Sprungk Theorem8:
M=Q/(3a), Q=integral_R² p⁴ sinhc(p/2) Phi(u)Phi(v) du dv.
All coefficients, finite-moment domination and source hypotheses still
need final checking and canonical recording. Continue only with a
finite explicit M uniform at zero; abandon on an essential failed
hypothesis or an unbounded constant. No frequency signs, numerical
certificate, all-height claim or new general stability theorem is sought.
